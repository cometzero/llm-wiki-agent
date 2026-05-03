---
title: "NPUv01"
type: entity
tags:
  - NPU
  - EdgeAI
  - Compiler
  - Runtime
  - Hardware
  - RV64
  - RVV
  - IME
  - HAL
  - MMIO
sources:
  - npu-v0-1-prd
  - npu-v0-1-implementation-design
  - npu-v0-1-isa-spec
  - npu-v0-1-hw-architecture
  - npu-v0-1-sw-architecture
last_updated: 2026-05-03
---

## Summary
[[NPUv01]]는 RV64GC 기반의 tile형 Edge AI 가속기 v0.1 프로젝트군으로, global command queue를 배제하고 host-driven **immediate launch** 중심 실행 모델을 채택한다. 목표는 single-tile 기준에서 컴파일러/런타임 contract를 안정화한 뒤 2/4 tile SKU로 점진 확장하는 것이다.

컴파일/런타임 구조는 [[IREE]]/[[MLIR]] 기반의 AOT fused-kernel 경로를 유지하면서, backend plugin과 external [[HAL]] driver로 하드웨어 특수성(`riscv-ime-cpu`, `nputile`)을 국소화한다.

## Key Points
- [[NPUv01]] v0.1 baseline: 2-hart tile, 2 MB shared [[SharedScratchpadMemory]], 3-channel [[DMA]], RVV256 + IME-style contraction.
- execution model: no global command queue, host MMIO/doorbell trigger and runtime-level immediate dispatch.
- interface contract: [[Kernel]] ABI, SPM 배치, barrier/event, DMA wait semantics은 compile-time/ABI level에서 결정.
- observability: [[PMU]]/trace/fault-report 중심으로 v0.1 단계에서 회귀와 안정성 게이트 강화.
- preemption/virtualization/security hardening/opcode freeze는 v0.2 이후 scope로 미룸.

## Related Sources
- [[NPU v0.1 PRD]]
- [[NPU v0.1 Implementation Design]]
- [[NPU v0.1 ISA Specification]]
- [[NPU v0.1 Hardware Architecture]]
- [[NPU v0.1 Software Architecture]]
- [[IREE]] / [[MLIR]]
- [[IREE/MLIR Compiler Stack]]

## Notes
- [[NPUv01]]는 성능 고도화 이전에 재현성, deterministic execution, regression lock을 우선한다.
