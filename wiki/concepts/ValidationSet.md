---
title: "ValidationSet"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[ValidationSet]]는 학습 중 모델 구조/설정 조정과 조기 종료 판단에 사용하는 데이터다.

## Key Points
- 학습되지 않은 데이터에서 성능을 점검해 [[Hyperparameter]]를 고른다.
- train보다 적은 과적합 위험이 있지만, 반복된 의존 사용 시 [[ValidationSet]] 과적합이 가능하다.
- 보통 model selection, architecture tuning, stopping criteria에 사용한다.

## Connections
- [[TrainSet]]
- [[TestSet]]
- [[TrainValidationTestSplit]]
- [[Generalization]]
- [[Hyperparameter]]
- [[EarlyStopping]]
