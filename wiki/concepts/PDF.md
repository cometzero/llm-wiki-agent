---
title: "PDF"
type: concept
tags: [probability, probability-distribution, continuous]
last_updated: 2026-04-26
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
PDF(Probability Density Function)는 연속형 확률변수가 특정 구간에서 가질 확률을 밀도로 표현하는 함수다.

## Key Claims
- [[PDF]]는 확률밀도로 직접 "확률"이 아니라 "밀도"를 제공한다.
- 특정 구간 확률은 적분으로 계산한다: \(P(a \le X \le b)=\int_a^b f(x)dx\).
- 확률밀도는 음수가 될 수 없고, 전체 적분값이 1이다.
- [[CDF]]는 PDF의 적분으로 얻어진다.
- [[PMF]]와 구분되어야 하며, 연속 공간에서 값을 단일 점에 대해 직접 확률로 다루면 안 된다.

## Connections
- [[Continuous]] — PDF의 적용 대상.
- [[RandomVariable]] — PDF가 기술하는 확률변수 유형.
- [[ProbabilityDistribution]] — 확률분포의 연속형 표현.
- [[CDF]] — 적분 관계를 가진 누적분포.
- [[Expectation]] — 적분 기반 기대값 계산에 사용.

## AI Connections
- 회귀·연속 값 출력 모델에서 오차 분포 가정이나 생성모형의 연속 분포 표현에 기반.
- [[GaussianModeling]] 등에서 핵심 표기다.

## Contradictions
- No explicit contradiction identified.