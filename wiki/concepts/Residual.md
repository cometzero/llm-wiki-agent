---
title: "Residual"
type: concept
tags:
  - ai-ml
  - regression
  - loss
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Residual은 모델 예측값과 실제값의 차이로, 예측 오차의 부호 있는 값이다.

회귀에서 residual의 부호는 상쇄될 수 있으므로 보통 제곱을 사용해 오차 크기만 남긴다.

## Formula
`r_i = y_i - \hat{y}_i`

## Connections
- [[LeastSquares]], [[MSE]]: residual 기반 손실.
- [[LinearRegression]]: 학습 신호 정의의 기초.
- [[GradientDescent]]: residual 기반 경사 계산 흐름의 구성요소.
