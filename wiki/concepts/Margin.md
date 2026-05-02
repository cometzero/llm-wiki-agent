---
title: "Margin"
type: concept
tags:
  - ai-ml
  - classification
  - robustness
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Margin은 데이터 점이 [[DecisionBoundary]]에서 얼마나 떨어져 있는지를 나타내는 거리 직관이다.

경계에서 멀리 떨어질수록 작은 perturbation에서 label이 바뀔 확률이 상대적으로 낮아지는 안정성이 커질 수 있다.

## Core Idea
- margin이 작으면 경계 주변에서 불안정한 분류가 나올 수 있다.
- margin이 큰 모델은 일반적으로 더 넓은 구분 여유를 가진다.

## Connections
- [[DecisionBoundary]], [[Hyperplane]], [[LinearSeparability]].
- [[SupportVectorMachine]]: margin 극대화와 직접 연결되는 대표 알고리즘.
- [[Robustness]], [[Generalization]]: 실무적 안정성 관점의 연결점.
