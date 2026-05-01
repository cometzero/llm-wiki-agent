---
title: "K-Fold Cross Validation"
type: concept
tags:
  - evaluation
  - cross-validation
  - fold
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[KFoldCrossValidation]]은 [[CrossValidation]]의 대표 구현으로, 데이터를 K개 조각으로 나누고 각 조각을 번갈아 validation으로 사용한다.

## Key Claim
한 번의 학습/평가로는 놓치기 쉬운 분할 의존성을 줄이기 위해 K번의 성능을 집계해 [[ModelSelection]]과 [[Generalization]] 판단을 개선한다.

## Procedure
1. 데이터셋을 K개 fold로 균등 분할한다.
2. 1개 fold를 검증용으로, 나머지 K-1개를 학습용으로 고정한다.
3. K회 반복 후, 각 회차 성능의 평균을 최종 점수로 사용한다.

## Caveat
- 큰 모델에서는 학습 비용이 K배로 증가할 수 있다.
- [[HyperparameterTuning]]·모델 비교 시 신뢰도 개선 효과가 크다.

## Connections
- [[CrossValidation]], [[ValidationSet]], [[Generalization]], [[GeneralizationGap]], [[TrainValidationTestSplit]].