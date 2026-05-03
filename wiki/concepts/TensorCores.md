---
title: "Tensor Cores"
type: concept
tags:
  - NVIDIA
  - AIHardware
  - Matrix
  - CUDA
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
[[TensorCores]]는 [[NVIDIA]] GPU에서 행렬 연산(AI에서 흔한 GEMM 포함)을 빠르게 처리하기 위해 설계된 특수 하드웨어 유닛이다. 특히 AI 추론·학습에서 전체 연산의 큰 비중을 차지하는 행렬 곱셈과 누적 연산을 고속화한다.

## Key Claims
- 텐서 코어는 동일 연산을 더 높은 처리량으로 수행하도록 튜닝된 연산 유닛이다.
- 많은 워크로드에서 입력은 [[FP16]] 등 저정밀도를 쓰고, 누산·출력은 [[FP32]] 같은 고정밀 누산으로 오차를 통제한다.
- 텐서 코어는 `[[WMMA]]` 기반 API 및 타일링 전략과 결합될 때 성능 이점이 가장 잘 드러난다.
- 일반적인 CUDA 코어 구현 대비 특정 행렬 형태(16x16 타일 패턴 기반)에서 더 큰 이득을 낼 수 있다.

## Connections
- [[CUDA]] — 텐서 코어를 호출하고 제어하는 소프트웨어 스택.
- [[WMMA]] — 텐서 코어를 추상화한 CUDA matrix API.
- [[FP16]] / [[FP32]] — 정밀도-성능 트레이드오프의 핵심.
- [[Warp]] — 텐서 코어 연산을 실행하는 협업 단위와 깊게 연결.
- [[GFLOPS]] — 성능 비교의 대표 지표.

## Notes
[[TensorCores]]는 성능 지표만으로 완성되지 않으며, 메모리 레이아웃, 패딩, 타일링이 성능을 결정한다.