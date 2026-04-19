# NPU v0.1 Implementation Design

*RTL / Compiler / Runtime Bring-up and Delivery Plan*

| 문서 버전 | v0.1 |
| --- | --- |
| 상태 | Internal Draft |
| 적용 대상 | RTL, DV, Compiler, Runtime, Integration |
| 핵심 Deliverable | bring-up 가능한 HW/SW baseline |
| 작성일 | 2026-04-19 |

> **문서 상태**
> 
> 본 문서는 NPU v0.1 baseline을 기준으로 한 internal draft이며, v0.2에서 opcode encoding, multi-tile 확장, preemption, virtualization, security hardening 항목이 추가/수정될 수 있다.

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서명 | NPU v0.1 Implementation Design |
| 대상 독자 | 프로젝트 리드, RTL/DV, compiler, runtime, platform SW |
| 목적 | NPU v0.1의 실제 구현 범위, 모듈 분해, 검증 및 bring-up 계획을 정의한다. |
| 적용 범위 | single-tile baseline 구현과 1차 소프트웨어 통합 |
| 기준 베이스라인 | 2 harts/tile, RV64GC + RVV256 + IME-style matrix pipe, shared SPM 2 MB/16 banks, DMA 3채널, command queue 없음, IREE/MLIR 기반 AOT ELF kernel |

## 개정 이력

| 버전 | 상태 | 날짜 | 주요 변경 |
| --- | --- | --- | --- |
| v0.1 | Initial Draft | 2026-04-19 | NPU v0.1 baseline에 대한 최초 문서화 |

## 1. Implementation baseline

v0.1 구현은 기능 시연보다 baseline 고정과 재현 가능한 bring-up에 우선순위를 둔다. 따라서 모든 구성요소는 '작게 시작해서 명확하게 연결'하는 방식으로 정의한다. HW는 single-tile RTL과 모델링 가능한 MMIO 인터페이스를 제공하고, SW는 IREE backend plugin과 external HAL driver를 제공한다.

| 영역 | v0.1 구현 범위 | 제외/후순위 |
| --- | --- | --- |
| RTL | 2-hart tile, IME, SPM, DMA, barrier, PMU | multi-tile coherency, aggressive power management |
| Compiler | RVV lowering, IME tensorization, SPM planner, ELF emission | auto-scheduler, wide autotuning |
| Runtime | remote ELF loader, immediate launch, profiling, fault handling | full async queue scheduler, preemption |
| Verification | RVV-only, IME-enabled, DMA/barrier regression | safety certification artifacts |

> **Entry criteria**
> 
> 본 구현 계획은 ISA와 HW/SW 아키텍처 문서에서 정의한 baseline이 승인되었다는 가정 하에 사용한다.

## 2. Repository and ownership model

| Repository / Tree | 책임 영역 | 주요 산출물 |
| --- | --- | --- |
| rtl/ | tile top, hart, VRF, IME, SPM, DMA, barrier, PMU | RTL, UVM env, synthesis scripts |
| dv/ | ISA regression, random/dir test, fault injection | testplan, scoreboard, coverage |
| compiler/plugins/riscv_ime/ | backend plugin, dialect, pass pipeline, ukernels | MLIR pass, object/bitcode library |
| runtime/nputile/ | HAL driver, remote loader, profiling | driver, device shim, integration test |
| tests/ | kernel regression, end-to-end model smoke | golden vectors, perf smoke scripts |

## 3. RTL work breakdown

| 모듈 | 입/출력 관점 | 핵심 구현 포인트 |
| --- | --- | --- |
| tile_ctrl | launch regs, hart boot, timeout/fault aggregate | doorbell, hart mask, completion/fault status |
| hart_core | fetch/decode, scalar/vector issue | dual-issue in-order, LMUL-aware scoreboard |
| vrf | 4R/2W slice-based vector regfile | W0/W1 arbitration, bypass, collector share port |
| ime_pipe | collector, A/B buf, hidden psum, 8x8 array | collector FSM, chain accumulate, wb pack |
| spm_2mb | 16 bank shared SRAM | address decode, ECC, bank arbiter |
| dma_subsys | 3 channel MMIO DMA | 2D/3D stride, transpose, pack mode, completion event |
| barrier_block | 8 barrier slots, event mux | epoch, target_count, wakeup |
| pmu_trace | counter/traces | cycle/stall/dma/ime activity |

RTL baseline은 parameterization보다 명확한 reference implementation을 우선한다. 즉 bank 수, hart 수, VLEN, DMA 채널 수를 우선 고정하고, 이후 공통화/parameterization을 수행하는 것이 안정적이다.

## 4. Interface definition priorities

| 인터페이스 | 우선 확정 항목 |
| --- | --- |
| Launch MMIO | entry, ctx_ptr, hart_mask, flags, doorbell, status |
| DMA MMIO | SRC/DST, X/Y/Z, MODE, START, STATUS, completion_event |
| CSR | mnpuinfo, mspmcfg, mspmwin, barrier/event, PMU |
| SPM local address | bank_id/row/byte layout, group coloring contract |
| IME intrinsic API | tile class, type, accumulate/zero-init semantic |
| Kernel param block | binding pointer, shape/stride, spm/mmio/perf base |

위 인터페이스는 cross-team contract로 취급하며, opcode bit encoding보다 먼저 freeze해야 한다.

## 5. Compiler implementation design

| 파일/모듈 | 구현 내용 | 완료 조건 |
| --- | --- | --- |
| Registration.cpp | backend option/target 등록 | iree-compile에서 backend 인식 |
| NPUTileOps.td | ime_mma, spm_copy, barrier op 정의 | parser/printer/verify 통과 |
| ResolveEncodings.cpp | tile class, pack mode 결정 | planner input IR 안정화 |
| PlanScratchpad.cpp | SPM offset/bank group/DMA channel 할당 | report + verifier 제공 |
| TensorizeIME.cpp | mmt4d/packed contraction -> ime_mma | BF16/INT8 main path emission |
| ConvertNPUTileToLLVM.cpp | IME intrinsic, MMIO helper call lowering | asm/obj emission |
| rvv_*.c | LN/softmax/GELU/depthwise ukernel | unit test + end-to-end pass |

Compiler는 '작동하는 generic path'를 먼저 확보하고, 그 위에 IME tensorization과 SPM planner를 단계적으로 추가해야 한다. 처음부터 모든 kernel을 IME로 내리려 하면 regression과 디버그 비용이 급증한다.

## 6. Runtime and platform implementation design

| 모듈 | 구현 항목 |
| --- | --- |
| driver.c / device.c | device registration, query, queue model |
| remote_elf_loader.c | ELF upload, relocation, symbol patch |
| executable_cache.c | feature/version based executable reuse |
| command_buffer.c | HAL dispatch record 후 immediate launch translation |
| mmio_transport.c | doorbell, DMA register access, poll/interrupt support |
| profiling.c | PMU/trace readback, JSON/CSV report |

Runtime의 핵심은 HAL abstraction을 유지하되 hardware queue를 가정하지 않는 것이다. 즉 command buffer는 존재하더라도 최종 실행은 즉시 launch다.

## 7. Bring-up phases

| Phase | 목표 | Exit Criteria |
| --- | --- | --- |
| P0: Modeling | MMIO model, SPM/DMA/barrier reference model 구축 | software simulator에서 kernel skeleton 실행 |
| P1: RVV-only | RVV kernel, SPM, DMA, barrier RTL 동작 | LN/softmax/depthwise regression pass |
| P2: IME Enable | IME pipe와 intrinsic emission 연결 | matmul/MLP/QKV kernel pass |
| P3: End-to-End | IREE backend + HAL driver + RTL/emulator 통합 | fused kernel launch demo |
| P4: Hardening | fault handling, PMU, trace, perf smoke | product gate PG-01..06 충족 |

- 각 phase는 regression green 상태에서만 다음 단계로 진행한다.
- P1 이전에 opcode encoding freeze를 시도하지 않는다.
- P3 이후에만 representative model benchmark를 제품 판단 자료로 사용한다.

## 8. Verification strategy

| 축 | 검증 내용 |
| --- | --- |
| ISA/Kernel Regression | RVV op, pseudo-op, CSR/MMIO sequence, IME main tile, tail fallback |
| DMA/Barrier | overlap, completion event, timeout, error code, bank conflict corner |
| Golden Numerical | BF16/FP16/INT8 matmul, LN, softmax, GELU, DWConv golden compare |
| Fault Injection | illegal op, ECC, DMA address fault, barrier misuse |
| Compiler/Runtime E2E | ELF generation, load, launch, completion, PMU report |

RVV-only reference path는 항상 golden anchor로 유지해야 한다. IME path는 성능 경로이지만, 수치/기능 검증은 RVV-only 또는 software reference와의 비교를 통해 수행한다.

## 9. Performance and observability plan

| 지표 | 설명 | 수집 위치 |
| --- | --- | --- |
| Kernel latency | launch~complete 시간 | host/runtime |
| IME active cycles | matrix pipe util | PMU |
| DMA overlap | DMA active vs compute active 중첩 | PMU/trace |
| SPM spill ratio | on-chip vs DDR intermediate | compiler report + trace |
| Barrier stall | sync wait cost | PMU |

성능 최적화는 P3 이후에 시작하되, 관측성 수단은 P1부터 넣어야 한다. 측정 없는 최적화는 v0.1 범위에서 금지한다.

## 10. Open issues and decision log

| 항목 | 현재 결정 | 후속 검토 |
| --- | --- | --- |
| Opcode encoding | provisional | v0.2 freeze |
| IME intrinsic naming | backend local naming 허용 | toolchain alignment |
| SPM protection | minimum mode | privilege/security hardening |
| Interrupt model | polling 우선, interrupt 옵션 | platform integration |
| Multi-tile | software partitioning | global barrier/coherency 여부 |

Open issue는 phase 진행을 막지 않는 범위와 baseline을 뒤흔드는 범위를 구분해 관리해야 한다. 실행 모델, kernel ABI, SPM contract는 뒤흔들지 않는 것을 원칙으로 한다.

## 11. Deliverables for v0.1 sign-off

- Single-tile RTL 및 MMIO/CSR spec 일치
- RVV-only 및 IME-enabled kernel regression pass
- IREE backend plugin + `nputile` HAL driver 동작
- embedded ELF kernel load/launch demo
- PMU/trace 기반 기본 profiling report
- 문서 패키지(PRD/ISA/HW/SW/Implementation) 최신화
