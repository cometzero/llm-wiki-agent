---
title: "Momentum"
type: concept
tags: [optimizer, gradient-descent, optimization]
sources: [2026-04-28-day06-ai-ml-learning-review]
last_updated: 2026-04-28
---

## Summary
[[Momentum]]은 이전 업데이트 방향 정보를 누적해 현재 gradient 업데이트를 보정하는 [[Optimizer]] 기법이다. 기존의 진동을 완화하고, 일관된 방향으로의 진행을 가속화한다.

## Core Intuition
현재 mini-batch gradient가 매 스텝 흔들릴 때, 모멘텀은 이전 방향을 가중 평균해 "관성"을 만든다. 이를 통해 좌우로 흔들리는 스텝이 줄고, 좁고 긴 골짜기(ill-conditioned surface)에서 안정적으로 빠르게 진행하기 쉬워진다.

## Update Rule
\[
v_t = \beta v_{t-1} + (1 - \beta) g_t
\]
\[
\theta_{t+1} = \theta_t - \eta v_t
\]

여기서 \(g_t\)는 현재 gradient, \(v_t\)는 velocity, \(\beta\)는 과거 기여 유지 비율이다.

## Relation to Existing Concepts
- [[SGD]]: 현재 gradient만 쓰는 기본 방식의 확장
- [[LearningRate]]: 모멘텀과 결합해 스텝 크기와 동작성을 함께 조절
- [[Convergence]]/Oscillation: 잦은 방향 전환을 완화해 수렴 경로를 매끈화
- [[Adam]]: 모멘텀 아이디어를 1차 모멘트 통계로 일반화한 확장 계열

## Practical Notes
- 보통 [[Momentum]] 계수는 약 0.8~0.99 범위에서 설정한다.
- 너무 큰 모멘텀은 과도한 관성을 만들 수 있어 튐 현상이 커질 수 있다.
- mini-batch noise가 크면 모멘텀의 효과가 더 유의미할 때가 많다.