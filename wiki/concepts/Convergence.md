---
title: "Convergence"
type: concept
tags: [optimization, training]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Convergence는 반복 최적화 과정에서 파라미터나 손실 값이 안정된 해에 가까워지는 현상이다.

## Key Claims
- [[StepSize]]가 너무 크면 수렴하지 않고 진동하거나 발산할 수 있다.
- [[GradientDescent]]와 optimizer의 설계는 수렴 속도와 안정성에 큰 영향을 준다.
- 실전에서는 loss curve, validation metric, gradient norm 등을 함께 보며 판단한다.

## Connections
- [[GradientDescent]], [[StepSize]], [[LearningRate]], [[Optimizer]]
