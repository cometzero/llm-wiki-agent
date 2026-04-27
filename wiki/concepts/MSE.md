---
title: "Mean Squared Error"
type: concept
tags: [loss, regression]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
MSE는 예측값과 정답값의 차이를 제곱해 평균낸 손실 함수다. 회귀 문제에서 가장 기본적인 [[LossFunction]] 중 하나다.

## Key Claims
- 오차를 제곱하기 때문에 큰 오차에 더 큰 벌점을 준다.
- [[LinearRegression]] 같은 회귀 문제의 기본 손실로 자주 사용된다.
- 미분 가능해서 [[GradientDescent]] 기반 학습에 잘 맞는다.

## Connections
- [[LossFunction]], [[LinearRegression]], [[GradientDescent]], [[SurrogateLoss]]
