---
title: "Linear Separability"
type: concept
tags:
  - ai-ml
  - geometry
  - classification
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Linear Separability는 데이터 클래스가 하나의 선형 경계(직선/평면/초평면)로 완전히 분리 가능한 성질이다.

이 성질이 성립하면 선형 분류기가 안정적으로 학습 성능을 낼 수 있다.

## Core Idea
- 선형 분리가 가능하면 결정 경계가 한 번에 존재한다.
- 불가능하면 비선형 변환이나 더 깊은 모델이 요구된다.

## Connections
- [[DecisionBoundary]], [[Hyperplane]]: 실제 분리 경계의 수학적 표현.
- [[FeatureSpace]]: 동일한 데이터라도 표현 공간 변환 시 separability 변화 가능.
- [[NeuralNetwork]], [[Activation]], [[RepresentationLearning]]: 비선형 재표현으로 분리 가능성 향상.
