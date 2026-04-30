---
title: "Underfitting"
type: concept
tags:
  - ai-ml-learning
  - overfitting
  - model-complexity
sources:
  - 2026-04-30-day08-ai-ml-learning-review
last_updated: 2026-04-30
---

## Summary
[[Underfitting]]은 모델이 데이터의 기본 규칙을 충분히 학습하지 못해 훈련 데이터와 검증/테스트 데이터 모두에서 성능이 낮은 상태다.

## Definition
[[Underfitting]]은 모델 표현력이 부족하거나 학습이 불충분해 실제 함수의 구조를 못 맞추는 상황이다. 학습 데이터에 대한 오차가 높고, 일반화 성능도 대체로 낮다.

## 핵심 증상
- Training/Validation 양쪽 모두에서 성능이 낮음
- 학습이 더 진행되어도 병목 개선이 작음
- 모델이 지나치게 단순한 규칙만 학습

## 왜 발생하나
- 모델이 너무 단순
- 데이터/피처가 부족
- 학습 시간이 짧음
- 학습률 설정/초기화/정규화가 과도함
- 지나친 제약(예: [[Regularization]] 과잉, 과도한 [[Underfitting]])

## 정리
[[Underfitting]]은 [[Bias]]가 큰 상태와 연결된다. 해결은 보통 [[ModelComplexity]] 확대, 더 좋은 [[FeatureMatrix]] 구성, 적절한 학습 시간/학습률 조정, 가끔은 [[Regularization]] 완화다.

## Related
- [[Overfitting]]
- [[BiasVarianceTradeoff]]
- [[Bias]]
- [[ModelCapacity]]
- [[Generalization]]

## References in this wiki
- [[2026-04-30-day08-ai-ml-learning-review]]