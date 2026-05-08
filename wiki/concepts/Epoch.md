---
title: "Epoch"
type: concept
tags: [ai-ml-learning, training, deep-learning]
sources: [2026-04-30-day08-ai-ml-learning-review, 2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

## Summary
학습 데이터 전체를 모델이 한 번 모두 본 학습 단위.

## Key Claims
- 1 epoch은 전체 training dataset을 한 번 사용하는 것이다.
- 1 epoch 안의 [[Iteration]] 수는 보통 `ceil(N / B)`로 계산한다. 여기서 `N`은 데이터 수, `B`는 [[BatchSize]]다.
- 여러 epochs를 돌면 같은 데이터셋을 반복해서 보며 optimizer step을 누적한다.

## Connections
- [[2026-04-30-day08-ai-ml-learning-review]] — Day 08 AI/ML lesson context.
- [[2026-05-08-day16-ai-ml-learning-review]] — epoch, iteration, batch size 관계를 복습한 Day 16 lesson.
- [[Iteration]], [[BatchSize]], [[GradientAccumulation]]
