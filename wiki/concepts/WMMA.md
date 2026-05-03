---
title: "WMMA"
type: concept
tags:
  - CUDA
  - Matrix
  - GPU
  - TensorCore
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
[[WMMA]]는 NVIDIA CUDA에서 텐서 코어 기반 행렬 연산을 다루기 위한 API 집합으로, 프래그먼트 로드/곱셈/누적/저장 패턴을 제공한다. 특히 행렬 곱셈을 워프 수준에서 협업 수행하기 위한 표준 방식이다.

## Key Claims
- `load_matrix_sync` 기반으로 입력 텐서를 텐서 코어가 처리 가능한 형태로 로드한다.
- `mma_sync`를 통해 곱셈-누산을 한 번에 수행해 연산 효율을 높인다.
- `store_matrix_sync`로 결과를 메모리에 반영한다.
- 워프 협업 환경과 메모리 레이아웃 지정이 성능 결정에 큰 영향을 준다.

## Connections
- [[TensorCores]] — 텐서 코어의 주요 상위 추상화 API.
- [[Warp]] — 단위 병렬 실행 컨텍스트.
- [[CUDA]] — 구현 플랫폼.
- [[TensorCores]]의 [[SinglePrecision]], [[HalfPrecision]] 동작 특성을 구현적으로 연결.

## Notes
WMMA는 텐서 코어 활용의 실무적 입구점이므로, 알고리즘 설계보다는 연산 블록(tiling) 설계와 정밀도/레이아웃 설정이 더 중요해지는 경우가 많다.