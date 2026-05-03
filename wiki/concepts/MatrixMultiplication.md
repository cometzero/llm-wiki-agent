---
title: "Matrix Multiplication"
type: concept
tags:
  - LinearAlgebra
  - CUDA
  - AI
  - TensorCore
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
[[MatrixMultiplication]]은 AI 연산의 중심 연산으로, 행렬 곱셈 결과를 통해 dense 연산 파이프라인의 성능이 결정되는 경우가 많다. 소스는 이 연산이 연산 비용의 대부분을 차지하며, 하드웨어 특화 장치 사용이 필요함을 강조한다.

## Key Claims
- 텐서 코어는 행렬 곱셈 연산을 빠르게 처리하기 위해 존재한다.
- 실제 구현은 전체 행렬을 작은 타일로 나누어 처리함으로써 제약된 텐서 코어 크기에 맞춘다.
- 메모리 접근 순서(행 우선/열 우선)와 패딩은 계산 정확도와 성능에 직접 영향.
- [[GFLOPS]]로 성능 비교 시 행렬 크기, 실행시간, 연산량 공식을 함께 봐야 한다.

## Connections
- [[TensorCores]] 및 [[WMMA]] — 대규모 [[MatrixMultiplication]]의 하드웨어 가속 경로.
- [[Warp]] — 타일 단위 병렬 협업 수행 단위.
- [[CUDA]] — 구현 플랫폼.

## Notes
행렬 곱셈의 타일링은 단순히 최적화 기교가 아니라 텐서 코어 제약을 시스템적으로 만족시키기 위한 최소 단위이다.