---
title: "BayesTheorem"
type: concept
tags: [probability, inference, machine-learning]
last_updated: 2026-04-25
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Definition
[[BayesTheorem]]은 관측 후 사후확률을 사전확률과 가능도로 연결하는 확률 정리이다.

## Core idea

- \(P(y|x) \propto P(x|y)P(y)\)
- 즉 [[Posterior]]는 [[Prior]]와 [[Likelihood]]의 결합으로 갱신된다.

## Key claims
- 분류에서는 클래스 사전분포를 관측가능도와 결합해 판단 확률로 전환한다.
- 분류기, 캘리브레이션, 질병 진단, 스팸 분류 등에 정규적으로 적용되는 프레임이다.

## Connections
- [[Prior]]
- [[Likelihood]]
- [[Posterior]]
- [[ConditionalProbability]]
- [[Classification]]
- [[Calibration]]
- [[SpamFiltering]]