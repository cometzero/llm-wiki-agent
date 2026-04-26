---
title: "2026-04-25 AI/ML Learning Day 03"
type: source
tags: [diary, ai-ml-learning, function-approximation, representation, dimensionality]
date: 2026-04-25
source_file: raw/ai_ml_learning/2026-04-25-day03-ai-ml-learning-review.md
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Summary
Day 03는 AI/ML 30일 학습에서 핵심을 [[FunctionApproximation]] 시각으로 정리한 복습이다. 머신러닝은 입력에서 출력을 생성하는 함수를 학습하는 문제로 보고, 이를 구성하는 후보 함수 집합인 [[HypothesisSpace]]와 선택 기준인 [[LossFunction]]의 역할을 분리해 설명한다. 또한 데이터는 [[FeatureMatrix]] 형태로 정리하고, 딥러닝에서는 [[Tensor]] 차원과 [[TensorShape]]를 정확히 읽는 능력이 계산의 의미를 이해하는 핵심이 됨을 강조한다. 마지막으로 [[CurseOfDimensionality]]를 통해 고차원에서의 과적합·거리 붕괴 문제를 짚고 [[Regularization]], [[DimensionalityReduction]], [[RepresentationLearning]]의 필요성을 정리한다.

## Key Claims
- [[MachineLearning]]은 `입력 → 출력` 규칙을 학습하는 과정이며, 이를 [[FunctionApproximation]] 문제로 해석할 수 있다.
- [[HypothesisSpace]]는 모델이 고를 수 있는 후보 함수들의 집합이고, [[LossFunction]]는 각 후보의 성능을 정량적으로 평가해 학습 신호를 제공한다.
- [[FeatureMatrix]]는 각 행이 sample, 각 열이 feature인 표기준으로 정리한 입력 구조이며, 딥러닝에서는 [[Tensor]] 기반의 [[TensorShape]]이 일반화된 형태로 동작한다.
- [[LLM]]도 본질적으로 `이전 토큰 -> 다음 토큰 확률분포`를 예측하는 [[FunctionApproximation]]이며, [[Transformer]] 내부에서 [[RepresentationLearning]]이 병행되어 입력 표현이 점진적으로 개선된다.
- [[CurseOfDimensionality]]에서는 고차원에서 데이터가 희소해지고 거리 기반 판단이 불안정해지며, 이에 따라 overfitting 및 일반화 저하 위험이 커진다.
- [[Regularization]], 적절한 [[DimensionalityReduction]], 그리고 잘 설계된 [[RepresentationLearning]]이 고차원 학습 안정성과 일반화 성능을 확보하는 핵심 축이다.

## Key Quotes
> "머신러닝은 결국 입력을 출력으로 바꾸는 좋은 함수를 찾는 문제다." — 함수 근사 관점의 직관 정리

> "고차원에서는 데이터가 너무 성기게 퍼져서 가까운 이웃 찾기와 거리 비교가 덜 믿을 만해진다." — 고차원 공간에서의 직관적 설명

> "Transformer에서 입력 token은 처음부터 완벽한 feature가 아니다. embedding, attention, MLP를 거치며 점점 더 유용한 representation이 된다."

## Connections
- [[FunctionApproximation]] — 이 source의 중심 프레임
- [[HypothesisSpace]] — 후보 함수 집합
- [[LossFunction]] — 모델이 얼마나 맞는지 측정하는 기준
- [[FeatureMatrix]] — 기초적 정형 입력 표현
- [[Tensor]] — 딥러닝 입력/중간 표현의 일반화 구조
- [[TensorShape]] — 연산 가능성 및 구현 해석의 기본 규칙
- [[LLM]] — 다음 토큰 예측을 함수 근사로 재해석
- [[Transformer]] — 순차 입력을 단계적으로 처리하는 표준 구조
- [[RepresentationLearning]] — 좋은 표현을 함께 배우는 과정
- [[CurseOfDimensionality]] — 고차원 데이터 학습의 핵심 난제
- [[Regularization]] — 학습 안정화 및 일반화 완충 장치
- [[DimensionalityReduction]] — 표현 축소로 과적합/거리 문제를 완화
- [[MachineLearning]] — 상위 맥락
- [[Autograd]] 및 [[LossFunction]]의 실무 연결은 Day04의 [[GradientDescent]]/[[Backpropagation]]로 자연스럽게 연계됨.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.