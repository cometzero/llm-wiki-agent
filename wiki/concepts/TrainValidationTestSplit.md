---
title: "TrainValidationTestSplit"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[TrainValidationTestSplit]]는 데이터를 [[TrainSet]], [[ValidationSet]], [[TestSet]]로 분리해 학습·검증·최종 평가의 역할을 분리하는 실무 표준이다. 목표는 모델이 새로운 입력에서 성능을 낼 수 있는지를 추정하는 것이다.

## Data Roles
- [[TrainSet]]: 파라미터 학습 데이터.
- [[ValidationSet]]: 학습 중 하이퍼파라미터 선택과 모델 개선 판단.
- [[TestSet]]: 최종 학습 종료 이후의 성능 추정.

## Key Points
- [[TestSet]]는 여러 번 열면 leakage 성격의 평가 붕괴가 생길 수 있다.
- 시계열, 사용자 단위, 그룹 기반 문제에서는 무작위 분리보다 time-based 또는 group-based split이 더 적절하다.
- [[ValidationSet]]도 과도하게 쓰면 [[ValidationSet]]에 대한 과적합이 생긴다.

## Connections
- [[TrainSet]]
- [[ValidationSet]]
- [[TestSet]]
- [[DataLeakage]]
- [[Hyperparameter]]
- [[EarlyStopping]]
- [[Generalization]]
- [[OutOfSample]]
