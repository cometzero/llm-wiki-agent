---
title: "Hyperplane"
type: concept
tags:
  - ai-ml
  - linear-model
  - geometry
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Hyperplane은 고차원에서의 선형 결정 경계이다. 일반적으로 `w^Tx + b = 0` 형태로 쓰인다.

선형 분류 모델의 핵심 기하학적 경계로 사용된다.

## Core Idea
- 2D: 직선, 3D: 평면으로 축소해 이해 가능.
- 고차원에서도 동일한 선형 부등식으로 표현.

## Connections
- [[DecisionBoundary]]: 분류 경계의 선형 특수형.
- [[DotProduct]]: `w^Tx` 계산 기반.
- [[LinearSeparability]], [[Margin]]: 경계 품질의 보조 지표.
- [[SupportVectorMachine]](if exists): 선형 경계와 margin 최적화를 다루는 대표 모델군.
