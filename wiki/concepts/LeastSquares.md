---
title: "Least Squares"
type: concept
tags:
  - ai-ml
  - loss
  - regression
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Least Squares는 예측 잔차(residual)를 제곱해 더한 손실을 최소화하는 방법이다.

잔차의 부호 상쇄를 제거하고 큰 오차를 더 크게 벌점화하는 것이 핵심 직관이다.

## Core Formula

a) Residual: `r_i = y_i - \hat{y}_i`
b) Sum of Squared Error: `SSE = \sum_i r_i^2`
c) MSE: `\frac{1}{n}\sum_i r_i^2`

## Key Claims
- `\sum r_i^2`를 최소화하면 큰 오차가 학습에서 더 크게 반영된다.
- 분류가 아닌 회귀 문제에서 오차 크기 자체를 직접 최소화할 때 사용된다.
- 로그 손실, cross-entropy와 달리 값의 거리 기반을 다룬다.

## Connections
- [[LinearRegression]]: 대표적으로 least squares 기반 모델.
- [[MSE]]: 평균 제곱 오차로 정규화한 형태.
- [[Residual]]: 제곱의 대상.
- [[Objective]] / [[LossFunction]]: 최적화의 목표 함수 틀.
- [[GradientDescent]]: 큰 데이터에서 수치적으로 최소화.
