---
title: "Step Size"
type: concept
tags: [optimization, learning-rate, convergence]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Step Size는 반복 최적화에서 한 번에 파라미터를 얼마나 이동시킬지 결정하는 크기이다. 실무에서는 보통 [[LearningRate]]와 동의어로 쓰인다.

## Key Claims
- [[Gradient]]는 방향을, [[StepSize]]는 이동 거리 크기를 정한다.
- step이 너무 크면 발산/진동, 너무 작으면 학습이 느리다.
- [[SGD]], [[Adam]] 같은 optimizer는 기본적으로 같은 구조의 step scaling을 변형한 형태다.

## Connections
- [[GradientDescent]], [[LearningRate]], [[UpdateRule]], [[Convergence]], [[Optimization]], [[SGD]], [[Adam]]
