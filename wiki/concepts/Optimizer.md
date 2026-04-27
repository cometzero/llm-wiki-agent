---
title: "Optimizer"
type: concept
tags: [optimization, training]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Optimizer는 계산된 gradient를 사용해 실제 파라미터 업데이트를 수행하는 알고리즘 또는 모듈이다.

## Key Claims
- [[Backpropagation]]이 gradient를 계산하면 [[Optimizer]]가 그 결과를 [[UpdateRule]]에 따라 적용한다.
- [[GradientDescent]], [[SGD]], [[Adam]]은 optimizer 계열의 대표 예시다.
- learning rate scheduling, momentum, adaptive scaling 같은 전략은 optimizer 설계에 포함된다.

## Connections
- [[GradientDescent]], [[UpdateRule]], [[Gradient]], [[LearningRate]], [[SGD]], [[Adam]]
