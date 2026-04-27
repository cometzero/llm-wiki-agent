---
title: "Adam"
type: concept
tags: [optimization, training]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Adam은 gradient의 1차/2차 모멘트 추정을 활용해 파라미터별로 학습률을 적응적으로 조정하는 optimizer다.

## Key Claims
- [[SGD]]보다 초기 학습이 빠르고 안정적인 경우가 많다.
- gradient 크기 차이가 큰 파라미터들에 서로 다른 step scaling을 적용한다.
- 딥러닝 실무에서 널리 사용되지만, 문제에 따라 일반화 특성이 다를 수 있다.

## Connections
- [[Optimizer]], [[GradientDescent]], [[SGD]], [[LearningRate]], [[StepSize]]
