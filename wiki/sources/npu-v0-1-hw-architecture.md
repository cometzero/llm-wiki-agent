---
title: "NPU v0.1 Hardware Architecture"
type: source
tags:
  - NPU
  - 하드웨어아키텍처
  - Tile
  - RV64
  - RVV
  - IME
  - SPM
  - DMA
  - SoC
  - RTL
  - DV
  - AXI
  - NoC
date: 2026-04-19
source_file: raw/NPU/v0.1/NPU_v0.1_HW_Architecture.md
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## Summary
본 문서는 [[NPUv01]]의 기반 규격인 [[TileBasedNPU]] 구조를 설명하며, 제어 평면은 CPU/호스트에서 직접 수행하고 NPU를 **kernel machine**으로 두는 설계를 정의한다. 핵심은 높은 처리량보다 **edge latency**와 **deterministic execution**을 우선하고, 전역 명령 큐 없이 doorbell 기반 즉시 실행 경로를 채택하는 것이다.

문서는 단일 tile의 baseline을 2-hart 구조로 잡고, 이를 2/4 tile SKU로 확장하는 경로를 제시한다. [[RV64]] + [[RVV]] + IME-style matrix pipeline을 결합해 shared SPM, DMA, barrier/event 동기화, PMU/trace 기반 관측 계측까지 포함한 엔드투엔드 하드웨어 동작 집합을 정리한다.

또한 [[IREE]]/[[MLIR]] 기반 AOT ELF kernel 실행 모델을 기준으로, RVV-only 모드와 IME-enabled 모드의 DV 분리 전략, ECC 및 fault path까지 포함한 bring-up/검증 관점의 운영 요구사항을 제시한다.

## Key Claims
- v0.1은 global command processor를 두지 않고 host가 doorbell로 kernel을 launch하는 구조이며, tile 내부 hart가 DMA/compute/barrier orchestration을 직접 처리한다.
- baseline tile은 2-hart 구성, RVV 256b vector architecture, 2 MB shared scratchpad(16 banks), 3개 DMA 채널(R0/R1/W0)로 설계한다.
- IME는 architected matrix register file를 두지 않고, [[VectorRegisterFile]] 기반 operand collect + hidden psum buffer 방식으로 동작한다.
- VRF는 R3 포트를 collector 공유 포트로 사용해 RVV ternary op와 IME prepare 경로를 겹쳐 처리하되, regfile multi-port 확장 비용을 줄인다.
- scratchpad는 cache가 아니라 compiler-managed local memory로, bank group coloring을 통해 activation/weight/output/temp 분리를 유도한다.
- DMA는 command queue 기반 가속기가 아니라 MMIO-programmed helper engine이며, start bit 기반으로 시작하고 event/wait pseudo-op로 완료를 수신한다.
- 동기화는 8-slot barrier 기반이며 tile-local epoch/counter를 유지해 멀티-hart/멀티-tile 확장성 여지를 둔다.
- 1/2/4 tile SKU는 tile 복제 + NoC 분배로 구현하며, software-visible partitioning을 기본으로 하여 global coherency fabric을 필수로 두지 않는다.
- v0.1은 preemption, virtualization, 멀티테넌시를 제외하고, power는 block-level clock gating 중심으로 우선한다.
- Reliability 관점에서 ECC, fault register, PMU(최소 4 counter), trace, watchdog timeout을 정의해 DV와 compiler tuning 루프에 연결한다.

## Key Quotes
> "HW는 global command processor를 포함하지 않는다. host는 doorbell 기반으로 kernel을 launch하고, tile 내부 harts가 DMA/compute/barrier를 직접 orchestration한다." — [[NPUv01]] 결정

> "v0.1은 out-of-order보다 dual-issue in-order를 선택한다. 이유는 compiler-scheduled kernel machine에서 검증 비용과 전력 증가 대비 실익이 제한적이기 때문이다." — execution model

> "IME는 architected matrix state를 추가하지 않는다. accumulator는 hidden psum buffer에만 존재하며, visible state는 vector register group으로만 노출된다." — IME state 모델

> "SPM은 cache가 아니라 관리형 local memory다. compiler는 bank group coloring을 이용해 activation ping/pong, weight, output/temp를 배치해야 한다." — 메모리 관리 원칙

## Connections
- [[NPUv01]] — 본 문서의 baseline 아키텍처와 동일 프로젝트군의 중심 개념.
- [[TileBasedNPU]] — [[2-hart tile]], [[IME]], [[SharedScratchpadMemory]], [[DoorbellLaunch]]의 통합 동작 구조.
- [[RV64]] / [[RVV]] — hart 핵심 execution ISA baseline.
- [[IME]] — matrix contraction path와 hidden psum 기반 accumulator 동작.
- [[SharedScratchpadMemory]] — banked local memory 정책과 compiler-managed 배치.
- [[DMA]] — activation/weight preload와 output storeback용 helper engine.
- [[AXI]], [[NoC]] — DDR/MMIO 경로 인터페이스.
- [[BarrierSynchronization]] — 도착 카운트/epoch 기반 tile-local 동기화.
- [[IREE]] / [[MLIR]] — AOT ELF kernel 기반 빌드/배포 경로.

## Contradictions
- 기존 위키의 [[NeuralProcessingUnit]] 관련 문맥은 Linux NPU 서브시스템의 시스템 통합 제약을 다루는 반면, 본 소스는 특정 SoC NPU 블록 내부 구현 의도와 마이크로아키텍처 규격을 제시한다. 상호 충돌이 아니라 계층이 다르므로 **보완 관계**이다.
