---
title: "Argmin"
type: concept
tags: [optimization, objective, notation]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Argmin은 함수 값을 최소화하는 입력 집합/지점을 뜻한다. 최소값의 크기 자체와 혼동하지 않는다.

## Key Claims
- 함수 \(J(\theta)\)에서 \(\theta^* = \arg\min_\theta J(\theta)\)는 값을 가장 작게 만드는 \(\theta\)의 위치를 나타낸다.
- 최소값 \(\min_\theta J(\theta)\)는 하나의 스칼라 값이고, [[Argmin]]은 파라미터의 위치(또는 위치 집합)다.
- 최적화에서 argmin은 실제로 갱신해야 할 [[Parameter]]의 목표를 지정한다.

## Connections
- [[Optimization]], [[Objective]], [[OptimizationProblem]], [[GradientDescent]], [[Constraint]]
