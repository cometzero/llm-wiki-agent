---
title: "Function Approximation"
type: concept
tags: [machine-learning, foundation]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-25
---

# Function Approximation

[[FunctionApproximation]]은 머신러닝을 입력을 출력으로 보내는 함수를 찾는 문제로 보는 관점이다.

## Core Idea
- 모델은 데이터로부터 근사 함수 `f(x)`를 학습한다.
- 좋은 모델은 훈련 데이터에만 맞는 함수가 아니라 새로운 입력에도 잘 일반화되는 함수를 찾는다.

## Connections
- [[HypothesisSpace]] — 후보 함수들이 놓인 공간
- [[LossFunction]] — 후보 함수의 품질을 측정하는 기준
- [[FeatureMatrix]] — 함수가 입력을 받는 데이터 표현
- [[CurseOfDimensionality]] — 고차원에서 함수 근사가 어려워지는 이유