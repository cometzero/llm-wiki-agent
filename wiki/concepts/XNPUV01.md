---
title: "XNPUV01"
type: concept
tags:
  - RISC-V Extension
  - Matrix Instruction
  - Barrier
  - Event
  - SoC
sources:
  - npu-v0-1-isa-spec
last_updated: 2026-05-03
---

## Definition
[[XNPUV01]]는 [[NPUv01]]에서 사용되는 비표준 RISC-V 확장으로, matrix contraction(`nmmaz`/`nmma`), barrier/event, device query/동기화 제어를 처리한다. v0.1에서는 opcode encoding이 확정되지 않았으나, semantic contract는 명시적으로 고정한다.

## Instruction Classes
- Matrix: `nmmaz.bf16`, `nmma.bf16`
- Matrix: `nmmaz.f16`, `nmma.f16`
- Matrix: `nmmaz.i8`, `nmma.i8`
- Sync/Event: `nbar.arrive`, `nbar.wait`, `nbar.arrive_wait`, `nevt.wait`
- DMA wait semantics: pseudo `ndma.wait` (CSR write 방식 구현)

## Architecture Principle
- No architected matrix register file; hidden psum buffer + vector group pack-in/out
- BF16/FP16 tile class는 8x8x16, INT8은 16x8x32
- assembler에서는 pseudo-op로 정의할 수 있지만 software semantics는 유지되어야 함

## Relation to System
- Tile-local execution에서 멀티-hart 동기화와 completion path를 규정하여 병렬 커널 실행의 정합성을 높인다.
- [[MMIO]]와 함께 동작해 DMA 완료 및 event 처리의 software handshake를 정의한다.
- [[Kernel]] ABI 및 launch 파라미터와 조합되어 toolchain이 stable binary semantics로 배치되도록 함

## Existing linkage
- [[NPUISA]]
- [[NPUv01]]
- [[RV64]] / [[RVV]]
- [[DMA]]
- [[MMIO]]
