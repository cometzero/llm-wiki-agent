---
title: "Overfitting"
type: concept
tags: [generalization, training, deep-learning]
sources: [2026-04-27-day05-ai-ml-learning-review, 2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

## Summary
Overfitting은 train 데이터에는 지나치게 잘 맞지만 새로운 데이터에는 성능이 떨어지는 현상이다.

## Key Claims
- [[EmpiricalRisk]]만 지나치게 낮추면 일반화가 나빠질 수 있다.
- 데이터 부족, 과도한 모델 복잡도, 약한 규제가 흔한 원인이다.
- [[Regularization]], validation, early stopping 같은 기법으로 완화한다.
- Day 16 lesson은 [[Dropout]]을 overfitting을 줄이는 대표적인 stochastic regularization 방법으로 설명한다.

## Connections
- [[EmpiricalRisk]], [[Regularization]], [[MachineLearning]], [[Objective]]
- [[Dropout]] — 학습 중 일부 activation을 랜덤하게 제거해 특정 feature에 대한 과의존을 줄인다.
- [[2026-05-08-day16-ai-ml-learning-review]] — Dropout의 동기와 overfitting 완화 효과를 설명한 source.
