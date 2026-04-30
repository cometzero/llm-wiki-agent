---
title: "Bias"
type: concept
tags:
  - statistics
  - bias-variance
  - ai-ml-learning
sources:
  - 2026-04-30-day08-ai-ml-learning-review
last_updated: 2026-04-30
---

## Summary
여기서의 [[Bias]]는 사회적 편향이 아니라 통계학적/학습 이론적 bias를 뜻한다. 즉, 모델의 예측이 실제 규칙에서 구조적으로 벗어나는 정도다.

## Definition
[[Bias]]는 같은 데이터 분포에서 반복 학습한 평균 예측값이 정답에서 얼마나 떨어져 있는지를 나타낸다. 머신러닝에서는 주로 [[BiasVarianceTradeoff]]의 한 축으로 쓰인다.

## 핵심 포인트
- [[Bias]]가 크면 모델이 문제의 기본 구조를 못 잡아 [[Underfitting]]으로 기울어짐.
- [[Bias]]가 너무 크면 train/validation 성능 모두 떨어지는 경향.
- [[Bias]]는 항상 나쁜 값이 아니라 데이터·표현력 균형 안에서 필요한 편차를 반영한다.

## Relation
- [[Variance]]가 모델 예측의 흔들림을 본다면, [[Bias]]는 예측의 중심 이동을 본다.
- [[Bias]]↑ + [[Variance]]↓는 과소적합 쪽 경향.

## Practice
- 개선 방식: 모델 구조 확장, 더 적절한 feature, 더 긴 학습, [[HypothesisSpace]]/[[Capacity]] 조정

## Related
- [[BiasVarianceTradeoff]]
- [[Underfitting]]
- [[ModelComplexity]]
- [[Generalization]

## References in this wiki
- [[2026-04-30-day08-ai-ml-learning-review]]