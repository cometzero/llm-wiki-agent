---
title: "MMA"
type: concept
tags: [TensorCores, GPUArchitecture, TensorOps]
sources: [nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Definition

[[MMA]](Matrix Multiply-Accumulate)는 행렬 곱셈과 누적 연산의 핵심 연산 형태로, 텐서 코어에서 특화된 형태로 하드웨어화되어 AI 워크로드의 핵심 연산량을 처리한다.

## Evolution notes

- [[Volta]]: 워프 스코프/쿼드페어 기반 동작 방식
- [[Ampere]]: 전체 워프 기반 동작과 데이터 레이아웃 정리
- [[Hopper]]: 워프그룹 기반의 [[WGMMA]]로 전개
- [[Blackwell]]: [[tcgen05.mma]]와 다중 SM 협업(MMA.2SM) 구조

## Cross-links

- [[TensorCores]]
- [[HMMA]]
- [[WGMMA]]
- [[TCGen05MMA]]
- [[WMMA]]