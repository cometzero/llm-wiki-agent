---
title: "EarlyStopping"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[EarlyStopping]]은 [[ValidationSet]] 성능이 악화되기 시작할 때 학습을 멈추는 규칙이다.

## Key Points
- 과적합 구간에서 계속 업데이트되는 것을 방지한다.
- 보통 validation loss/accuracy의 최고 성능 시점 가중치 checkpoint를 저장한다.
- 학습률/정규화와 함께 practical generalization 방어선으로 쓰인다.

## Connections
- [[ValidationSet]]
- [[TrainSet]]
- [[Generalization]]
- [[Overfitting]]
- [[TrainValidationTestSplit]]
