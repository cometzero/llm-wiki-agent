---
title: "Tile-Based NPU"
type: concept
tags:
  - NPU
  - architecture
  - tile
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## 정의
[[TileBasedNPU]]는 단일 tile 단위를 반복 구성 가능한 NPU 하드웨어 단위로, 각 tile이 독립적으로 compute, memory, DMA, control를 수행하는 구조다. v0.1 기준 단일 tile이 최소 제품 단위이며 1/2/4 tile 구성이 상위 확장으로 제시된다.

## 핵심 특성
- 2-hart + shared [[SharedScratchpadMemory]] + 2 IME 파이프 + 3-channel [[DMA]]
- host doorbell launch + tile-local orchestration
- software-visible partitioning 기반 멀티타일 분배

## 설계 장점
- 검증 단순화(커맨드 큐 제거)
- tile-local 동작과 fault/trace 경로 분리 용이
- SoC 통합에서 확장성 있는 SKU 구성 (1/2/4 tile)

## 연관 페이지
- [[NPUv01]], [[SharedScratchpadMemory]], [[IME]], [[DoorbellLaunch]], [[DMA]], [[BarrierSynchronization]]
