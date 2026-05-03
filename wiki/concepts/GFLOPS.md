---
title: "GFLOPS"
type: concept
tags:
  - Performance
  - Matrix
  - Benchmark
  - Inference
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
[[GFLOPS]]는 초당 수행 가능한 부동소수점 연산량을 나타내는 성능 지표이다. 행렬 곱셈 성능 비교에서 CUDA 코어, 텐서 코어, 타일링/라이브러리 최적화 전략을 정량적으로 비교할 때 유용하다.

## Key Claims
- 실행 시간 단독보다 연산량 정규화 지표로서 분석 효율이 높다.
- 행렬 곱셈에서 총 연산 수는 대체로 `2 x M x N x K`로 추정된다.
- 동일 입력 대비 [[TensorCores]] 경로는 특정 크기에서 더 높은 [[GFLOPS]]를 보일 수 있다.
- 미완성 최적화 구현과 cuBLAS 같은 고도로 최적화 구현 간 간극을 비교할 때 특히 유의해야 한다.

## Formula
총 연산량(대략) = `2 * M * N * K`

## Connections
- [[MatrixMultiplication]] — GFLOPS 계산의 핵심 워크로드.
- [[TensorCores]] — 하드웨어 가속 효과를 정량 확인하는 지표군.
- [[cuBLAS]] — 최적화 기준점 비교에 자주 사용.

## Notes
정확한 성능 평가는 구현 효율뿐 아니라 메모리 이동비용, 정렬, 배치 크기까지 함께 평가해야 한다.