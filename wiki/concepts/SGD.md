---
title: "Stochastic Gradient Descent"
type: concept
tags: [optimization, training]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
SGD는 전체 데이터 대신 샘플 또는 mini-batch의 gradient를 사용해 파라미터를 갱신하는 경사하강법 변형이다.

## Key Claims
- 계산량을 줄이고 큰 데이터셋에서 학습을 가능하게 한다.
- gradient 추정치에 잡음이 있어도 실전에서는 빠른 학습에 유리할 수 있다.
- [[Optimizer]] 계열의 기본 기준점으로 자주 비교된다.

## Connections
- [[GradientDescent]], [[Optimizer]], [[StepSize]], [[LearningRate]]
