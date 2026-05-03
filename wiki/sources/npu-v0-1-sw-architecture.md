---
title: "NPU v0.1 Software Architecture"
type: source
tags:
  - NPU
  - SoftwareArchitecture
  - Compiler
  - Runtime
  - HAL
  - IREE
  - MLIR
  - RVV
  - IME
  - SharedScratchpadMemory
  - DMA
  - MMIO
  - PMU
  - Trace
  - EmbeddedELF
date: 2026-04-19
source_file: raw/NPU/v0.1/NPU_v0.1_SW_Architecture.md
sources:
  - npu-v0-1-sw-architecture
last_updated: 2026-05-03
---

## Summary
본 문서는 [[NPUv01]] v0.1의 소프트웨어 스택을 정의하며, frontend import부터 execution 완료 보고까지의 전체 흐름을 [[IREE]]/[[MLIR]] 중심으로 정리한다. 핵심은 전체 stack의 특수 하드웨어 의존을 plugin으로 국소화하고, runtime을 얇게 유지한 채 compile-time에서 가능한 한 많은 결정을 고정하는 것이다.

소스와 HW/ISA/구현 문서군과의 정합성을 맞추기 위해, `global command queue` 없이 **immediate launch**를 채택하고 shared SPM, DMA, barrier/event를 컴파일러-가시 contract로 처리한다. v0.1에서는 안정적 bring-up과 deterministic 동작, 관측성 확보가 성능 고도화보다 우선한다.

## Key Claims
- [[NPUv01]] v0.1 software stack은 새 VM/HAL 스택을 새로 만들지 않고, frontend에서 [[IREE]]/[[MLIR]]를 재사용해 `riscv-ime-cpu` backend plugin과 `nputile` external [[HAL]] driver 조합으로 구성한다.
- 실행 모델은 command queue 없이 host가 [[MMIO]]/doorbell 기반 **즉시 실행**(`immediate launch`)을 수행하고, tile 내부가 `Runtime`/`Kernel` 동작을 오케스트레이션한다.
- `riscv-ime-cpu` backend는 `RVV` generic path와 late IME tensorization을 분리해, 보편적인 연산은 generic path로 두고 matmul·1x1/QKV contraction 같은 연산만 explicit `ime_mma` 변환 대상으로 잡는다.
- SPM, barrier, DMA는 compiler-visible contract로 다루어, [[SharedScratchpadMemory]] bank-group coloring, ping/pong, prefetch/storeback, barrier insertion을 compile-time에 결정하고 runtime은 최소 개입으로 실행한다.
- `nputile` external HAL driver는 command buffer를 내부 표현으로 기록한 뒤 실제 실행 시 즉시 launch로 translate 하며, `executable_cache`/`remote_elf_loader`/`queue`/`profiling` 모듈로 분리된다.
- kernel lifecycle은 Compile→Load→Prepare→Launch→Execute→Complete 5단계로 구조화되며, runtime은 parameter block 채움, 실행 준비, 결과 회수 중심만 담당한다.
- ukernel 전략은 초기 `RVV ukernel` 최소 세트(LN/softmax/GELU/depthwise/quant dequant) + inline IME intrinsic를 우선하고, unsupported shape는 RVV fallback으로 처리한다.
- 관측성은 compile-time dump, PMU/trace, fault code normalization(예: DMA fault, illegal op, barrier timeout, SPM ECC)로 일관화해 regression과 성능 분석을 지원한다.
- v0.1에서 frozen 되는 것은 실행 모델, kernel ABI, SPM planning contract이며, opcode encoding/heuristic/provisional encoding은 추후 버전에서 흡수/변경한다.

## Key Quotes
> "새 VM/HAL 스택을 만들지 않는다. compiler는 `riscv-ime-cpu` backend plugin, runtime은 `nputile` external HAL driver로 구현한다." — SW 핵심 결정

> "HAL command buffer는 SW 내부 표현에 불과하며, 실제 submit 시에는 즉시 실행(immediate launch)으로 번역된다." — Runtime/HAL 실행 모델

## Connections
- [[NPUv01]] — 전체 v0.1 프로젝트의 대상.
- [[NPU v0.1 ISA Specification]] — ISA/CSR/MMIO/ABI 계약을 정의한 상위 규격.
- [[NPU v0.1 Hardware Architecture]] — tile, hart, SPM, DMA, barrier 기반 하드웨어 전제의 기술적 배경.
- [[NPU v0.1 Implementation Design]] — 구현 단계(P0~P4)와 관측/회귀 지향 전략과 정합.
- [[NPU v0.1 PRD]] — 인터페이스 freeze 우선순위와 제품 게이트를 소프트웨어 설계로 연결.
- [[IREE]] 및 [[MLIR]] — front-end import와 AOT 컴파일·ELF emission의 핵심 툴체인.
- [[riscv-ime-cpu]] — backend plugin 이름 및 특화 패스 세트의 실행 주체.
- [[nputile]] — external HAL driver 및 remote ELF loader 기반 runtime.
- [[SharedScratchpadMemory]] — compiler-managed local memory이며 HAL buffer와 분리되는 개념.
- [[Embedded ELF]] — v0.1 executable path의 핵심 산출물 포맷.
- [[ImmediateLaunch]] — command queue를 배제한 host-triggered launch 방식.
- [[PMU]]/[[Trace]]/[[Fault]] — v0.1 관측성/안정성 루프의 핵심 요소.

## Contradictions
- 기존 [[NPU v0.1 PRD]], [[NPU v0.1 Implementation Design]], [[NPU v0.1 ISA Specification]], [[NPU v0.1 Hardware Architecture]]과 충돌 없음. 오히려 immediate launch, single-tile 기반 확정, global command queue 배제라는 동일 원칙을 소프트웨어 계층에서 구체화한다.
