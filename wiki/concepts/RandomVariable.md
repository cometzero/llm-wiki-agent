---
title: "RandomVariable"
type: concept
tags: [probability, statistics]
last_updated: 2026-04-25
sources: [2026-04-24-day02-ai-ml-learning-review]
---

## Definition
[[RandomVariable]]는 실험의 불확실한 결과를 실수값(또는 벡터값)으로 대응시키는 함수다.

## Core idea
LLM/ML 맥락에서 [[RandomVariable]]는 노이즈, 레이블, 점수, 임베딩 차원 값 등 확률적으로 변하는 양을 수학적으로 모델링할 때 쓰인다.

## Key claims
- 실험 결과와 확률을 연결하는 매핑이다.
- [[Discrete]]/[[Continuous]] 성질에 따라 다루는 분포 형식([[PMF]], [[PDF]])이 달라진다.
- 분포 자체를 다루려면 [[Expectation]], [[Variance]] 같은 요약 통계량과 연결한다.

## Connections
- [[ProbabilityDistribution]]
- [[Expectation]]
- [[BayesTheorem]]
- [[MachineLearning]]