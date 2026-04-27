---
title: "Update Rule"
type: concept
tags: [optimization, gradient-descent, training]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Update Rule은 현재 파라미터를 다음 파라미터로 어떻게 바꿀지 정하는 공식이다. optimizer의 핵심 동작을 가장 직접적으로 표현한다.

## Key Claims
- 가장 기본적인 [[UpdateRule]]은 [[GradientDescent]]의 \(	heta_{t+1}=	heta_t-\eta
abla J(	heta_t)\) 형태다.
- [[Gradient]]는 방향을, [[StepSize]] 또는 [[LearningRate]]는 이동 크기를 결정한다.
- [[Optimizer]]마다 momentum, adaptive scaling 같은 추가 항이 붙을 수 있다.

## Connections
- [[GradientDescent]], [[Gradient]], [[StepSize]], [[LearningRate]], [[Optimizer]]
