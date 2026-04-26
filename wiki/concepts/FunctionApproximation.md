---
title: "Function Approximation"
type: concept
tags: [machine-learning, modeling]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Definition
[[FunctionApproximation]]은 입력 데이터에서 원하는 출력을 내는 함수를 학습하는 문제다. 즉, 실제 시스템이나 분포를 완전히 아는 대신, 데이터로부터 `f(x) ≈ y` 형태의 근사함수 `f`를 학습해 일반화 가능한 예측기를 만든다.

## 핵심 포인트
- 머신러닝의 핵심은 "좋은 함수를 찾는 것"이다.
- 이 관점은 [[MachineLearning]], [[Optimization]], [[LossFunction]] 및 generalization(일반화) 흐름과 직접 연결된다.
- 같은 문제를 해결하더라도 가정하는 함수군([[HypothesisSpace]])이 달라지면 성능과 해석이 달라진다.

## Related Concepts
- [[HypothesisSpace]] — 후보 함수 집합
- [[LossFunction]] — 근사 오차를 정량화
- [[FeatureMatrix]] — 입력을 구조화한 표현
- [[RepresentationLearning]] — 입력이 더 잘 근사되기 위한 내부 표현 학습
- [[LLM]] — `이전 토큰 -> 다음 토큰 분포`를 출력하는 함수로 이해 가능
- [[Transformer]] — 거대한 함수 근사기의 구현 패턴

## Notes from Source
- 이 source는 함수 근사를 "집의 가격 예측"에 비유해 직관적으로 설명하며, 모델을 손으로 설계하지 않고 데이터로부터 자동 학습하는 과정을 강조한다.
- linear regression, decision tree, neural network, [[Transformer]]를 서로 다른 [[HypothesisSpace]]를 가진 함수 근사기로 분류한다.

## Possible Conflicts
- No explicit contradiction found with existing wiki pages.