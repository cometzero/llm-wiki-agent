---
title: "Blackwell"
type: entity
tags:
  - NVIDIA
  - GPU
  - TensorCores
  - MatrixMultiplication
last_updated: 2026-05-03
sources:
  - modular-matrix-multiplication-on-blackwell-part-2-using-hardware-features-to-optimize-matmul
---

[[Blackwell]]는 [[NVIDIA]]의 차세대 GPU/AI 연산 아키텍처 계열로, 본 소스에서 [[MatrixMultiplication]] 커널 튜닝과 고밀도 텐서 연산 최적화의 실전 타겟으로 등장한다.

## 요약
본 문서는 [[Blackwell]]에서 행렬 곱셈 성능 최적화가 어떻게 이루어지는지 다루며, [[TensorMemoryAccelerator]], [[Tcgen05MMA]], [[TMEM]], [[Swizzling]]을 결합한 실전 튜닝을 정리한다. 특히 공유 메모리 구조의 병목([[SharedMemoryBankConflict]])을 다루는 것이 Blackwell 튜닝의 핵심 축으로 제시된다.

## 중요 성격
- 텐서 코어/텍스처/메모리 계층을 결합한 고효율 연산 경로를 제공한다.
- AI 추론/학습의 핵심 연산인 행렬 곱셈(GEMM)에서 I/O 병목과 계산 병목을 동시에 다루는 구조로 설계된다.
- 마이크로아키텍처 특성상 [[nvcuda::wmma]] 같은 상위 API보다도 TMA, 스위즐링, 메모리 배리어 설계가 성능 차이를 크게 만든다.

## 소스 연결
- [[TensorMemoryAccelerator]]
- [[Tcgen05MMA]]
- [[TMEM]]
- [[SharedMemory]]
- [[Swizzling]]
- [[Stmatrix]]
- [[cuBLAS]]

## 요약 성능
해당 소스는 커널 단계별 최적화로 나이브 대비 58배 성능 향상, 그리고 Swizzling 적용 커널에서 288.3 TFLOPs까지 달성했으나 cuBLAS 완전성 대비 갭이 남아 있다고 정리한다.
