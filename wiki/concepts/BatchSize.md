---
title: "BatchSize"
type: concept
tags: [ai-ml-learning, training, deep-learning]
sources: [2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

## Summary
Batch size는 한 번의 forward/backward pass에서 함께 처리하는 training sample 수다.

## Key Claims
- batch size가 `B`이면 한 [[Iteration]]에서 보통 `B`개 sample의 평균 loss로 gradient를 계산한다.
- 1 [[Epoch]]의 iteration 수는 `ceil(N / B)`로 계산한다.
- 큰 batch size는 gradient noise를 줄일 수 있지만 GPU memory를 더 많이 쓰고 generalization에 영향을 줄 수 있다.
- memory가 부족할 때는 [[GradientAccumulation]]으로 더 큰 effective batch size를 흉내낼 수 있다.

## Connections
- [[2026-05-08-day16-ai-ml-learning-review]] — epoch, iteration, batch size 관계를 다룬 Day 16 lesson.
- [[Epoch]], [[Iteration]], [[GradientAccumulation]]
