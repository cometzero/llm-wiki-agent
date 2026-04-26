---
title: "CDF"
type: concept
tags: [probability, probability-distribution]
last_updated: 2026-04-26
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
CDF(Cumulative Distribution Function)는 확률변수가 특정 값 이하일 누적 확률을 주는 함수이다.

## Key Claims
- CDF는 \(F(x)=P(X\le x)\)로 정의된다.
- 이산형에서는 PMF의 누적합으로 계산할 수 있다.
- 연속형에서는 PDF의 적분으로 계산할 수 있다.
- CDF는 단조 증가이며, 극한에서 0에서 1로 수렴한다.
- 분포의 구간 비교, 분위수 계산, 임계확률 해석에 기본적으로 쓰인다.

## Connections
- [[PMF]] / [[PDF]] — 이산/연속 분포의 누적 연결 고리.
- [[Discrete]], [[Continuous]] — 양쪽 구간을 잇는 공통 표현.
- [[RandomVariable]], [[ProbabilityDistribution]] — 전체 분포의 누적 관점.
- [[Expectation]] — 누적분포 기반 성질 분석과의 연계.

## AI Connections
- 예측 확률의 임계값 설정, 의사결정 경계, 위험 관리에서 누적 확률 해석으로 사용된다.

## Contradictions
- No explicit contradiction identified.