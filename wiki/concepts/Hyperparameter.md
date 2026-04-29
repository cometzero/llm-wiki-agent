---
title: "Hyperparameter"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[Hyperparameter]]는 학습 과정에서 모델이 자동으로 최적화하지 않는 값(또는 설정)이다.

## Key Points
- [[LearningRate]], batch size, layer 수, dropout rate 등이 하이퍼파라미터에 포함된다.
- 보통 [[ValidationSet]] 성능을 기준으로 선택한다.
- Hyperparameter 검색이 잘못되면 [[ValidationSet]]에 과도하게 맞춰지는 현상이 생긴다.

## Connections
- [[TrainValidationTestSplit]]
- [[ValidationSet]]
- [[EarlyStopping]]
- [[Capacity]]
- [[Overfitting]]
