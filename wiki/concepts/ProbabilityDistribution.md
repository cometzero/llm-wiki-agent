---
title: "ProbabilityDistribution"
type: concept
tags: [probability]
last_updated: 2026-04-25
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Definition
[[ProbabilityDistribution]]은 [[RandomVariable]]가 어떤 값 영역에서 얼마만큼의 확률을 갖는지 수학적으로 설명하는 함수군이다.

## Core idea
모델링에서 핵심은 변수형태(이산/연속)와 표현 방식의 일치다. 같은 현상을 [[PMF]], [[PDF]], [[CDF]]로 각각 해석할 수 있으며, 용도에 따라 변환된다.

## Key claims
- 분포는 개별 값(확률 질량/밀도)뿐 아니라 누적 확률로도 해석할 수 있다.
- ML에서는 로그우도, prior/posterior 계산, 샘플링 기반 추론 등에서 기본 단위가 된다.

## Connections
- [[PMF]]
- [[PDF]]
- [[CDF]]
- [[BayesTheorem]]
- [[GenerativeModeling]]
- [[Sampling]]