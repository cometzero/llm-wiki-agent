---
title: "Ampere"
type: concept
tags: [NVIDIA, GPUArchitecture, TensorCores]
sources: [nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Definition

[[Ampere]]는 데이터 이동 병목을 줄이기 위해 비동기 데이터 경로와 WMMA/텐서 데이터 레이아웃 최적화를 도입한 NVIDIA 텐서 코어 세대이다.

## Key characteristics

- [[AsynchronousDataCopy|비동기 데이터 복사]](cp.async)로 레지스터/공유메모리 사이 동작 부담을 완화
- [[WGMMA]] 이전 단계로서 전체 워프 기반 협업 형태 정비
- [[ldmatrix]]를 통해 데이터 레이아웃/로딩 효율 개선
- [[BF16]]가 실무 정밀도로 강화되는 분기

## Cross-links

- [[Volta]]
- [[TensorCores]]
- [[Hopper]]
- [[MMA]]
- [[BF16]]
- [[TMEM]]