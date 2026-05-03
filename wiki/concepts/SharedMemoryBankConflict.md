---
title: "Shared Memory Bank Conflict"
type: concept
tags:
  - SharedMemory
  - BankConflict
  - MatrixMultiplication
  - Swizzling
  - GPU
last_updated: 2026-05-03
sources:
  - modular-matrix-multiplication-on-blackwell-part-2-using-hardware-features-to-optimize-matmul
---

## 정의
[[SharedMemory]]은 여러 뱅크로 구성되어 동시 접근을 병렬 처리하지만, 동일 뱅크에 다수 요청이 집중되면 [[SharedMemoryBankConflict]]가 발생해 처리 사이클이 늘어난다.

## Blackwell 맥락
- BMxBK/BNxBK 타일에서 코어 행렬 배치가 잘못되면 특정 뱅크로 트래픽이 편중되어 대기 비율이 커진다.
- [[Swizzling]]은 대표적인 완화 수단이며, 본 소스에서 128B 스위즐 패턴이 핵심 사례로 제시된다.

## 연계
- [[Swizzling]]
- [[TensorMemoryAccelerator]]
- [[MatrixMultiplication]]
- [[Blackwell]]
