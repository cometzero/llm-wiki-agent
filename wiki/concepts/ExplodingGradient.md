---
title: "ExplodingGradient"
type: concept
tags: [optimization, neural-networks, training-stability]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[ExplodingGradient]]는 역전파에서 기울기가 과도하게 커져 파라미터 업데이트가 급격히 발산하는 현상이다. 학습이 발산하거나 불안정한 진동을 유발한다.

## Key Claims
- 역전파 시 gradient 크기가 큰 값으로 누적되면 수치 불안정이 생긴다.
- [[LearningRate]]가 크거나 네트워크의 민감도가 큰 구간에서 더 흔하다.
- [[GradientNormClipping]] 같은 제약, 정규화, 적절한 학습률 정책으로 통제한다.

## Relation
- [[VanishingGradient]] — 다층 네트워크에서의 반대 극단적 문제.
- [[Backpropagation]] — 실제 훈련 불안정성의 주된 원인 중 하나.
- [[Optimization]] 및 [[LossFunction]] 학습의 신뢰성 관리 포인트.