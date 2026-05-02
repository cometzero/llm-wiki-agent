---
title: "Decision Boundary"
type: concept
tags:
  - ai-ml
  - classification
  - geometry
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Decision Boundary는 모델이 입력 공간에서 class를 바꾸는 경계면이다.

2D에서는 선, 3D에서는 평면, 고차원에서는 [[Hyperplane]] 또는 비선형 곡면 형태로 나타난다.

## Core Idea
- 결정 경계는 score가 임계점에 해당하는 집합에서 class가 전환되는 지점이다.
- 로지스틱 회귀처럼 선형 점수 모델은 보통 `w^Tx+b=0` 경계를 만든다.

## Connections
- [[LogisticRegression]], [[BinaryClassification]]: 선형 경계의 기본 예시.
- [[Hyperplane]], [[LinearSeparability]], [[Margin]], [[FeatureSpace]].
- [[LLM]]: 분류 token 선택에서 높은 차원의 경계 직관을 해석하는 데 사용.

## Notes
- 고차원 모델에서는 경계의 시각화가 어려우나, 의미론적으로 class partitioning의 핵심 개념이다.