---
title: "Progressive Lowering"
type: concept
tags:
  - MLIR
  - LLVM
  - Dialect
  - Compiler
  - Optimization
last_updated: 2026-05-10
sources:
  - unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w
---

## 정의

[[ProgressiveLowering]]은 고수준 표현을 점진적으로 더 저수준 표현으로 변환해, 각 단계에서 아키텍처와 최적화 부담을 이전 단계에서 다음 단계로 이행하는 컴파일 전략이다.

## IREE 적용

- 입력 모델(예: [[PyTorch]]/[[TensorFlow]])은 [[MLIR]] 다이얼렉트 영역으로 낮춰진다.
- 이후 디바이스별로 더 구체적 연산 형태로 하향한다.
- 마지막에 [[LLVM]] 대상 코드/바이너리 경로로 수렴한다.

## 핵심 효과

- 표현의 유연성 유지
- 다양한 백엔드 통합 간소화
- 중간 단계에서의 분석/최적화 가능성 확대
