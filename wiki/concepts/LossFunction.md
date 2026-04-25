---
title: "Loss Function"
type: concept
tags: [machine-learning, optimization]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-25
---

# Loss Function

[[LossFunction]]은 모델의 예측이 정답과 얼마나 다른지 측정하는 기준이다.

## Core Idea
- 회귀에서는 MSE 같은 오차 함수를 사용한다.
- 분류에서는 cross-entropy 같은 목적 함수를 많이 쓴다.
- 최적화는 loss를 줄이는 방향으로 진행된다.

## Connections
- [[FunctionApproximation]] — 어떤 함수가 더 좋은지 판단하는 기준
- [[HypothesisSpace]] — 후보 함수 공간 안에서 비교하는 척도