---
title: "PMF"
type: concept
tags: [probability, probability-distribution, discrete]
last_updated: 2026-04-26
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Summary
PMF(Probability Mass Function)는 이산형 확률변수에서 가능한 각 값이 나타날 확률을 직접 할당하는 함수다.

## Key Claims
- [[PMF]]는 이산 변수의 각 값 $x$에 대해 $P(X=x)$를 정의한다.
- 가능한 값의 집합이 유한하거나 가산 무한할 때 합산으로 정규화되어 \(\sum_x P(X=x)=1\)을 만족한다.
- [[CDF]]는 PMF로부터 누적되어 값을 구할 수 있다.
- [[PDF]]와 구분되어야 하며, 서로 혼용하면 확률 계산이 어긋난다.

## Connections
- [[Discrete]] — PMF가 적용되는 변수 유형.
- [[RandomVariable]] — PMF는 확률변수의 분포 표현 방식 중 하나.
- [[ProbabilityDistribution]] — PMF는 그 하위 표현.
- [[CDF]] — 누적분포와의 관계 축.
- expectation(기댓값) — PMF 기반 기대값 계산과 직접 연결.

## AI Connections
- [[Classification]] 및 생성/예측 모형에서 클래스별 이산 확률 벡터를 기술할 때 사용된다.
- 불확실성 해석에서 카테고리형 출력 확률을 이해하는 기초 표기이다.

## Contradictions
- No explicit contradiction identified.