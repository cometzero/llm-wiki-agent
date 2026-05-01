---
title: "Regression Loss"
type: concept
tags:
  - regression
  - loss
  - optimization
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[RegressionLoss]]는 연속값 예측에서 정답 값과 예측 값의 차이를 벌점으로 변환해 최적화하는 손실군이다.

## Common formulas
- [[MSE]]: 오차 제곱의 평균(큰 오차를 더 크게 벌점)
- [[MAE]]: 오차 절댓값의 평균(이상치 둔감도가 상대적으로 높음)

## Interpretation
회귀 문제에서는 "얼마나 숫자가 멀리 틀렸는지"가 핵심이므로 거리 기반 손실이 자연스럽다.

## Relation
- [[Regression]], [[Outlier]], [[Optimizer]], [[Gradient]].