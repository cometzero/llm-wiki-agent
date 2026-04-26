---
title: "Loss Function"
type: concept
tags: [machine-learning, optimization]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Definition
[[LossFunction]]은 학습이 예측한 값과 정답 사이의 오차를 수치화해, 가설 함수를 비교·개선하기 위한 학습 신호를 제공한다.

## 역할
- 모델 성능의 정량화 기준을 제공한다.
- [[Optimization]]에서 손실 값을 최소화하는 방향으로 학습이 진행된다.
- 같은 [[HypothesisSpace]]에서도 손실 정의에 따라 최적점이 달라질 수 있다.

## 정렬되는 개념
- [[MachineLearning]]에서의 학습 루프 핵심 축
- [[Backpropagation]]/[[GradientDescent]]와 결합해 실제 파라미터 업데이트를 유도한다.
- Day04의 [[Autograd]] 이해를 위해서는 손실의 미분 가능성도 중요하다.

## Source Alignment
- Source Day03은 손실 함수를 "후보 함수가 얼마나 틀렸는지 재는 기준"으로 정의하고, 학습을 손실 감소 과정으로 설명한다.

## Possible Conflicts
- No explicit contradiction found with existing wiki pages.