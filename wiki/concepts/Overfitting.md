---
title: "Overfitting"
type: concept
tags: [generalization, training]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Overfitting은 train 데이터에는 지나치게 잘 맞지만 새로운 데이터에는 성능이 떨어지는 현상이다.

## Key Claims
- [[EmpiricalRisk]]만 지나치게 낮추면 일반화가 나빠질 수 있다.
- 데이터 부족, 과도한 모델 복잡도, 약한 규제가 흔한 원인이다.
- [[Regularization]], validation, early stopping 같은 기법으로 완화한다.

## Connections
- [[EmpiricalRisk]], [[Regularization]], [[MachineLearning]], [[Objective]]
