# NPU v0.1 ISA

*Instruction Set and Programmer's Interface Specification*

| 문서 버전 | v0.1 |
| --- | --- |
| 상태 | Internal Draft / Provisional |
| 프로파일 | RV64GC + V + XNPUV01 |
| 범위 | kernel-visible ISA, CSR, MMIO, ABI |
| 작성일 | 2026-04-19 |

> **문서 상태**
> 
> 본 문서는 NPU v0.1 baseline을 기준으로 한 internal draft이며, v0.2에서 opcode encoding, multi-tile 확장, preemption, virtualization, security hardening 항목이 추가/수정될 수 있다.

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서명 | NPU v0.1 ISA Specification |
| 대상 독자 | Compiler backend, assembler, RTL decode, bring-up 담당 |
| 목적 | NPU v0.1의 programmer-visible ISA 및 MMIO/CSR/ABI를 정의한다. |
| 적용 범위 | tile 내부 hart가 실행하는 kernel binary와 host/device launch interface |
| 기준 베이스라인 | 2 harts/tile, RV64GC + RVV256 + IME-style matrix pipe, shared SPM 2 MB/16 banks, DMA 3채널, command queue 없음, IREE/MLIR 기반 AOT ELF kernel |

## 개정 이력

| 버전 | 상태 | 날짜 | 주요 변경 |
| --- | --- | --- | --- |
| v0.1 | Initial Draft | 2026-04-19 | NPU v0.1 baseline에 대한 최초 문서화 |

## 1. 문서 범위와 규범

본 문서는 NPU v0.1의 커널 실행에 필요한 programmer-visible 인터페이스를 정의한다. 여기서 정의하는 ISA는 표준 RISC-V RV64GC+V 위에 internal custom extension XNPUV01을 추가한 형태이며, v0.1에서 opcode encoding은 provisional이다.

본 문서에서 must/shall로 표현한 항목은 v0.1 필수 요구사항이며, should로 표현한 항목은 권장 사항이다. 예시 어셈블리와 pseudo-op는 의미를 설명하기 위한 것이며, 최종 assembler syntax는 toolchain 통합 단계에서 조정될 수 있다.

> **주의**
> 
> XNPUV01은 제품 내부 확장이다. 표준 RISC-V 확장과 충돌하지 않도록 custom opcode space를 사용하며, v0.2에서 encoding freeze를 수행한다.

## 2. 아키텍처 프로파일

| 항목 | 정의 |
| --- | --- |
| Base ISA | RV64GC |
| Vector | RVV, VLEN = 256b, 32 architectural vector registers |
| Custom Extension | XNPUV01 (IME-style matrix op, barrier/event control, device query CSR) |
| Privilege Model | kernel runtime 기준 machine-mode, no virtual memory in v0.1 |
| Endianness | Little-endian |
| Numerics | INT8/INT32, FP16/BF16, FP32 accumulation |
| Architected Matrix RF | 없음. matrix operands/result는 vector register group에 존재 |

XNPUV01의 설계 원칙은 architected matrix register file을 추가하지 않고 기존 vector register model을 유지하는 것이다. matrix instruction은 packed vector register group을 입력/출력으로 사용하며, 내부 psum buffer는 microarchitecture에만 존재한다.

## 3. Programmer-visible state

| 상태 | 설명 |
| --- | --- |
| x0-x31 | 일반 목적 레지스터. base ABI는 RV64를 따른다. |
| f0-f31 | 부동소수점 레지스터. scalar FP 보조 경로에 사용한다. |
| v0-v31 | 256b vector registers. IME operand/result packing에도 사용한다. |
| vl/vtype/vcsr | RVV standard control state. |
| XNPUV01 CSR | mnpuinfo, mspmcfg, mspmwin, mbarsel, mbarcmd, mbarstat, mevtwait, mdmawait, mperfctl, mperfcnt0..3 |

IME instruction은 matrix A/B/Acc를 vector register group으로 인코딩한다. 구체적인 packing은 compiler가 결정하며, v0.1의 normative tile class는 BF16/FP16용 8x8x16, INT8용 16x8x32이다.

## 4. 메모리 모델과 주소 공간

| 주소 공간 | 용도 | 접근 방법 |
| --- | --- | --- |
| Global Memory (DDR) | 입력/출력/weight/bias 및 호스트 공유 버퍼 | DMA, scalar load/store, optional slow-path vector load/store |
| SPM Window | tile-local scratchpad | 일반 load/store 및 vector LSU; mspmwin으로 window 속성 설정 |
| MMIO | DMA, launch, perf, fault register | uncached scalar load/store |

v0.1의 고성능 경로는 Global Memory와 SPM 사이를 DMA로 이동하고, 계산은 SPM 상의 데이터를 대상으로 수행하는 것이다. 글로벌 메모리에 대한 직접 vector access는 허용되더라도 성능 보장 범위가 아니다.

- SPM은 cache가 아니라 compiler-managed local memory다.
- 동일 tile 내 hart 간 SPM 공유는 barrier/event로 명시적으로 동기화해야 한다.
- DMA completion 이전에 대상 SPM 영역을 읽는 것은 정의되지 않는다.
- MMIO와 CSR 접근은 strongly ordered로 취급한다.

## 5. XNPUV01 instruction classes

v0.1은 세 가지 계층으로 ISA를 구성한다. 첫째, 일반 scalar/vector 연산은 표준 RV64GC+V를 그대로 사용한다. 둘째, matrix contraction은 XNPUV01 matrix mnemonic으로 표현한다. 셋째, barrier/event/dma wait은 CSR 또는 pseudo-op로 표현한다.

| 분류 | mnemonic | 기능 |
| --- | --- | --- |
| Matrix | nmmaz.bf16 / nmma.bf16 | 8x8x16 BF16 tile multiply-accumulate (zero-init 또는 accumulate) |
| Matrix | nmmaz.f16 / nmma.f16 | 8x8x16 FP16 tile multiply-accumulate |
| Matrix | nmmaz.i8 / nmma.i8 | 16x8x32 INT8 tile multiply-accumulate |
| Sync | nbar.arrive / nbar.wait / nbar.arrive_wait | barrier slot에 도착/대기 |
| Event | nevt.wait | event mask가 완료될 때까지 대기 |
| Device Query | csrr | mnpuinfo, mspmcfg 등 읽기 |
| DMA Wait | ndma.wait (pseudo) | DMA completion mask 대기. mdmawait CSR write로 구현 |

## 6. Matrix instruction semantics

Matrix mnemonic은 packed vector register group에 담긴 타일을 입력으로 받아 내부 psum buffer에서 accumulation을 수행한 뒤 결과를 packed vector register group으로 기록한다. architected matrix register file은 없다.

| Mnemonic | 입력/출력 의미 | 고정 타일 클래스 | 비고 |
| --- | --- | --- | --- |
| nmmaz.bf16 vd, va, vb | vd <- A×B | M=8, N=8, K=16 | zero-init |
| nmma.bf16 vd, va, vb | vd <- vd + A×B | M=8, N=8, K=16 | accumulate |
| nmmaz.f16 vd, va, vb | vd <- A×B | M=8, N=8, K=16 | zero-init |
| nmma.f16 vd, va, vb | vd <- vd + A×B | M=8, N=8, K=16 | accumulate |
| nmmaz.i8 vd, va, vb | vd <- A×B | M=16, N=8, K=32 | INT32 acc |
| nmma.i8 vd, va, vb | vd <- vd + A×B | M=16, N=8, K=32 | INT32 acc |

```asm
# BF16 MLP fragment (pseudo-assembly)
# va: packed A tile, vb: packed B tile, vd: packed accumulator tile
nmmaz.bf16 v8, v4, v6      # v8 = A x B
nmma.bf16  v8, v10, v12    # v8 += A1 x B1
# epilogue는 RVV path에서 bias/GELU/residual 처리
```

compiler는 full tile loop를 nmma 계열로 tensorize해야 하며, tail/fringe는 RVV path로 분리하는 것을 기본 정책으로 한다.

## 7. Barrier, event, wait semantics

barrier는 총 8 slot을 제공한다. 각 slot은 target_count, arrived_count, epoch를 가진다. nbar.arrive_wait는 선택된 slot에 도착한 뒤 마지막 participant가 도착할 때까지 대기한다.

| Pseudo-op | 정의 | 비고 |
| --- | --- | --- |
| nbar.arrive imm3 | mbarsel <- imm3; mbarcmd <- ARRIVE | non-blocking |
| nbar.wait imm3 | mbarsel <- imm3; mbarcmd <- WAIT | blocking |
| nbar.arrive_wait imm3 | mbarsel <- imm3; mbarcmd <- ARRIVE_AND_WAIT | common case |
| nevt.wait rs1 | mevtwait <- event_mask | DMA/event completion 동기화 |
| ndma.wait rs1 | mdmawait <- dma_mask | DMA 채널 완료 대기 |

barrier/event instruction은 implementation에서 CSR write 시퀀스로 풀어낼 수 있다. 즉 assembler pseudo-op로 구현해도 ISA 규약을 만족한다.

## 8. CSR specification

| CSR | 접근 | 설명 |
| --- | --- | --- |
| mnpuinfo | RO | tile_id, local_hart_id, barrier_slots, dma_channels, supported dtype class |
| mspmcfg | RO | bank_count, line_bytes, total_kbytes |
| mspmwin | RW | SPM window base와 속성 |
| mbarsel | RW | 선택된 barrier slot id |
| mbarcmd | WO | 0=arrive, 1=wait, 2=arrive_and_wait, 3=drop |
| mbarstat | RO | done bit, epoch summary |
| mevtwait | WO | event mask 대기 |
| mdmawait | WO | DMA channel done mask 대기 |
| mperfctl | RW | PMU enable/reset/select |
| mperfcnt0..3 | RO | cycle, stall, dma_active, ime_active 등 구현정의 카운터 |

mspmwin은 런타임이 kernel entry 전에 설정하는 것이 기본이며, 일반 kernel은 이를 변경하지 않는 것이 좋다. PMU counter set은 구현 정의지만 event class와 read semantics는 stable하게 유지해야 한다.

## 9. DMA MMIO programmer's interface

DMA는 ISA opcode가 아니라 MMIO-programmed local engine으로 제공된다. 커널 코드는 MMIO register를 설정하고 start bit를 기록한 뒤, event 또는 DMA wait pseudo-op로 완료를 기다린다.

| 오프셋 | 레지스터 | 핵심 필드 |
| --- | --- | --- |
| 0x000 | CAP | 채널 수, 기능 비트 |
| 0x004 | INT_STATUS | done/err 상태 |
| 0x00C | START_MASK | bit[i]=start channel i |
| 0x100+n*0x40 + 0x00 | CHn.CTRL | enable, reset, dir, prio |
| ... + 0x08/0x10 | CHn.SRC/DST | src/dst address |
| ... + 0x18..0x30 | CHn.X/Y/Z | bytes, count, stride |
| ... + 0x34 | CHn.MODE | transpose, pack_mode, pad_mode, bank_group, completion_event |
| ... + 0x38 | CHn.PAD_VALUE | zero/constant pad value |

```asm
# DMA-R0: DDR -> SPM packed copy (pseudo)
li   t0, DMA_CH0_BASE
sd   a0, 0x08(t0)        # SRC
sd   a1, 0x10(t0)        # DST
sw   t1, 0x18(t0)        # X_BYTES
sw   t2, 0x1c(t0)        # Y_COUNT
sw   t3, 0x34(t0)        # MODE (pack + event)
sw   x1, DMA_START_MASK  # start ch0
li   t4, 1               # wait ch0
ndma.wait t4
```

## 10. Kernel ABI

IREE executable outer ABI는 기존 executable library ABI를 유지하되, 내부 커널 진입 시에는 nputile_kernel_params_t parameter block을 전달한다. 필수 인자는 binding pointer, shape/stride, workgroup index, spm_base, mmio_base, perf_base다.

| 레지스터 | 의미 |
| --- | --- |
| a0 | nputile_kernel_params_t* |
| a1 | local_hart_id |
| a2 | hart_count |
| a3 | spm_base |
| a4 | perf_base (optional) |

- v0.1 커널은 재진입을 가정하지 않는다.
- stack은 글로벌 메모리 또는 구현 정의 local scratch stack을 사용한다.
- interrupt-driven preemption은 지원하지 않으며, fault 발생 시 kernel은 trap/fault code로 종료된다.
- SPM layout과 bank group 배치는 compiler metadata가 결정한다.

## 11. 예외와 fault model

| 분류 | 설명 | 권장 처리 |
| --- | --- | --- |
| Illegal Instruction | 지원하지 않는 XNPUV01 mnemonic 또는 잘못된 encoding | trap + fault register 기록 |
| Barrier Protocol Error | slot id 범위 오류, target_count mismatch | kernel abort |
| DMA Fault | address/protection/alignment/timeout | channel err_code 기록 후 kernel abort |
| SPM Fault | ECC error 또는 bank protection violation | fatal 또는 recoverable policy를 구현 정의 |

v0.1은 precise trap 성격을 유지하는 것을 목표로 하지만, DMA와 같은 비동기 엔진 오류는 completion 시점에 fault register를 통해 보고될 수 있다.

## 12. Encoding policy (provisional)

opcode bit-level encoding은 v0.1에서 frozen이 아니다. 단, 다음 원칙은 고정한다.

- XNPUV01 matrix/control instruction은 custom opcode space를 사용한다.
- Matrix zero-init와 accumulate는 별도 funct 구분 또는 mode bit로 분리한다.
- CSR와 MMIO programmer's interface의 소프트웨어 의미는 stable하게 유지한다.
- toolchain은 mnemonic 수준 호환성을 우선 보장하고, binary encoding freeze는 v0.2에서 수행한다.

> **실무 가이드**
> 
> RTL/assembler bring-up 단계에서는 inline asm 또는 intrinsic wrapper를 사용하고, compiler는 late tensorization 이후에만 nmma 계열을 emission하는 정책을 사용한다.
