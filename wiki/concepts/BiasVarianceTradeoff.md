---
title: "Bias-Variance Tradeoff"
type: concept
tags:
  - ai-ml-learning
  - optimization
  - generalization
sources:
  - 2026-04-30-day08-ai-ml-learning-review
last_updated: 2026-04-30
---

## Summary
[[BiasVarianceTradeoff]]는 모델이 너무 단순하면 생기는 [[Bias]](과소적합)와, 너무 민감해 생기는 [[Variance]](과적합)를 균형 있게 다루는 핵심 이론이다.

## Core Idea
학습 모델이 복잡해질수록 데이터에 맞추는 능력은 좋아지지만, 노이즈에 대한 민감도도 커질 수 있다.
- 단순 모델: [[Bias]] 큰 오차(체계적 누락)
- 복잡 모델: [[Variance]] 큰 오차(샘플 의존성)

## 직관
너무 똑똑하게 외우면 새 문제에서 흔들리고, 너무 멍청하면 기본 규칙도 못 잡는다. 양쪽 사이의 균형이 [[Generalization]] 성능을 만든다.

## 핵심 연관
- [[Overfitting]]과 [[Underfitting]]의 이론적 설명 프레임
- [[ModelCapacity]]와 하이퍼파라미터 조합에서 실전적으로 조정됨
- [[Regularization]], [[TrainValidationTestSplit]], [[EarlyStopping]]으로 제어

## Practical Use
- train/validation gap이 커지는 방향(복잡도 증가)을 보면 [[Variance]] 증가 신호를 점검
- train과 validation이 모두 나쁘면 [[Bias]] 개선이 먼저 필요
- 데이터 증가/더 많은 특성/더 정교한 모델을 쓰는 것보다 정규화가 먼저인 경우가 많음

## Related
- [[Bias]]
- [[Variance]]
- [[Generalization]]
- [[Regularization]]
- [[ModelComplexity]]
- [[TrainingLoss]]
- [[ValidationLoss]]

## References in this wiki
- [[2026-04-30-day08-ai-ml-learning-review]]