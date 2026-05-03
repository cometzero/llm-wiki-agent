---
title: "NPU v0.1 ISA Specification"
type: source
tags:
  - NPU
  - ISA
  - CSR
  - MMIO
  - ABI
  - RV64
  - RVV
  - DMA
  - Barrier
  - Event
  - Matrix
date: 2026-04-19
source_file: raw/NPU/v0.1/NPU_v0.1_ISA_Spec.md
sources:
  - npu-v0-1-isa-spec
last_updated: 2026-05-03
---

## Summary
본 문서는 [[NPUv01]]의 [[RV64GC]] + [[RVV]] 위에 추가되는 [[XNPUV01]] 커스텀 확장으로, 커널 가시 인터페이스인 ISA, [[CSR]], [[MMIO]], 그리고 [[Kernel]] ABI를 정의한다. v0.1은 matrix tile 연산, 동기화, 이벤트/완료 대기, 그리고 SPM/DMA 연동을 위한 소프트웨어-공개 동작 의미를 규정하고, opcode encoding은 v0.2에서 확정될 예정이라고 명시한다.

문서의 핵심은 architected matrix register file 없이 vector register group으로 tile 오퍼랜드를 인코딩해 IME-style matrix pipeline을 활용하고, SPM을 캐시가 아닌 compiler-managed local memory로 다루며, 동기화와 completion을 barrier/event 및 MMIO wait 경로로 맞추는 것이다. 또한 인터럽트 기반 preemption을 지원하지 않는 v0.1에서 trap/fault 기반의 오류 처리 경로를 강조한다.

## Key Claims
- [[NPUv01]]의 programmer-visible baseline는 kernel machine 가정, RV64GC+[[RVV]] + [[XNPUV01]]로 구성되며, v0.1에서 opcode encoding은 provisional이다.
- [[XNPUV01]]는 8x8x16(BF16/FP16)과 16x8x32(INT8) tile 연산군을 `nmmaz.*`/`nmma.*`로 제공하고, zero-init/accumulate 구분 semantic을 둔다.
- 동기화는 8개 barrier slot, target_count/arrived_count/epoch를 갖고, `nbar.arrive`, `nbar.wait`, `nbar.arrive_wait`로 동작한다.
- event/dma completion은 CSR write-sequence 또는 pseudo-op 형태로 대기하며, 정의상 barrier/event는 assembler pseudo-op로도 해석 가능하다.
- CSR 집합(`mnpuinfo`, `mspmcfg`, `mspmwin`, `mbarsel`, `mbarcmd`, `mbarstat`, `mevtwait`, `mdmawait`, `mperfctl`, `mperfcnt0..3`)은 runtime 가시 레지스터 의미를 제공한다.
- DMA는 opcode가 아닌 [[MMIO]]-programmed 엔진으로 동작하며, kernel은 채널 레지스터 설정 후 START_MASK 설정 및 wait 경로로 완료를 동기화한다.
- kernel ABI는 [[IREE]] [[MLIR]] AOT ELF와 호환되되, entry 시 `nputile_kernel_params_t*` 구조체를 `a0`로 받고 `a1`~`a4`에 local context 정보를 전달한다.
- v0.1은 가상메모리 미지원(machine-mode 중심), no preemption, no virtualization을 전제한다.
- fault는 precise trap 성격을 목표로 하지만 DMA completion/비동기 엔진 오류는 completion 시점 fault report path를 통해 보고될 수 있다.

## Key Quotes
> "XNPUV01 is provisional opcode in v0.1, and encoding freeze is explicitly deferred to v0.2." — encoding section

> "IME instruction은 matrix A/B/Acc를 vector register group으로 인코딩한다." — matrix semantics

> "SPM은 cache가 아니라 compiler-managed local memory다." — memory model

## Connections
- [[NPUv01]] — tile 기반 baseline과 v0.1 ISA의 대상 프로젝트/블록.
- [[TileBasedNPU]] — 2-hart tile 구조 및 shared [[SharedScratchpadMemory]]/DMA 전제가 같은 계열이다.
- [[RV64]] / [[RVV]] — 기본 ISA 바탕 위에 XNPUV01 커스텀 확장이 덧붙어짐.
- [[XNPUV01]] — matrix, barrier/event 제어, CSR/MMIO 연동을 담당하는 핵심 확장.
- [[SharedScratchpadMemory]] — 글로벌 메모리 직접 벡터 접근은 허용되더라도 성능 보장 범위 밖이라는 설계 규범의 중심 메모리 계층.
- [[IREE]] / [[MLIR]] — kernel ABI와 연결되는 빌드/배포 경로.
- [[DMA]] / [[MMIO]] — 비동기 전송 및 완료 동기화가 pseudo-wait 경로로 통합됨.
- [[Kernel]] ABI — `nputile_kernel_params_t` 기반 진입 규약으로 v0.1 커널 진입을 제약.

## Contradictions
- 기존 [[NPU v0.1 Hardware Architecture]] 소스는 하드웨어 구조와 경로(doorbell, 2-hart tile, 3채널 DMA)를 다루는 반면, 본 문서는 같은 프로젝트의 ISA/CSR/MMIO/API를 규정한다. 계층이 달라 직접 충돌이 아니라 보완 관계이다.
