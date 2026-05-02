---
title: "Feature Space"
type: concept
tags:
  - ai-ml
  - representation
  - geometry
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Feature Space는 입력을 의미 공간의 축(feature)으로 표현한 공간이다.

같은 데이터라도 feature의 선택/변환에 따라 [[LinearSeparability]] 성능이 크게 달라진다.

## Core Idea
- 피처가 잘 설계되면 선형 모델도 좋은 분리를 만들 수 있다.
- 신경망은 여러 층에서 feature space를 바꾸어 더 분리가 쉬운 표현으로 변환한다.

## Connections
- [[LinearRegression]], [[LogisticRegression]]: 원공간 기반 분류/회귀 계산이 일어나는 입력 공간.
- [[RepresentationLearning]], [[DenseLayer]], [[NeuralNetwork]].
- [[DecisionBoundary]]: 분류 경계가 작동하는 공간.
