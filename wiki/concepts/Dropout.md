---
title: "Dropout"
type: concept
tags: [ai-ml-learning, regularization, training, deep-learning]
sources: [2026-04-30-day08-ai-ml-learning-review, 2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

## Summary
학습 중 일부 뉴런이나 activation을 임시로 꺼 특정 패턴에 과도하게 의존하지 않도록 하는 정규화 기법.

## Key Claims
- [[Dropout]]은 training 중 activation 일부를 확률적으로 0으로 만들어 [[Overfitting]]을 줄이는 [[Regularization]] 방법이다.
- inverted dropout은 남은 activation을 keep probability로 나누어 기대 activation scale을 유지한다.
- inference 때는 dropout을 끄고 전체 network를 사용한다.

## Connections
- [[2026-04-30-day08-ai-ml-learning-review]] — Day 08 AI/ML lesson context.
- [[2026-05-08-day16-ai-ml-learning-review]] — Dropout과 확률적 정규화를 다룬 Day 16 lesson.
- [[Regularization]], [[Overfitting]], [[BatchNormalization]]
