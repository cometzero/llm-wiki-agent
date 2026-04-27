---
title: "Parameter"
type: concept
tags: [model, optimization, learning]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Parameter는 모델이 학습 과정에서 값을 조정하는 내부 변수다. weight, bias, embedding vector처럼 데이터에 맞게 바뀌는 숫자들이 여기에 해당한다.

## Key Claims
- [[MachineLearning]] 학습은 [[Parameter]]를 조절해 [[Objective]] 또는 [[LossFunction]]을 개선하는 과정이다.
- [[GradientDescent]]와 [[Backpropagation]]은 각 parameter가 얼마나 바뀌어야 하는지 계산한다.
- parameter 수와 구조는 모델의 표현력, 계산량, 과적합 위험에 직접 연결된다.

## Connections
- [[Objective]], [[LossFunction]], [[Gradient]], [[GradientDescent]], [[Regularization]]
