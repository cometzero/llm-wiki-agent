---
title: "2026-04-29 AI/ML Learning Day 07"
type: source
tags:
  - diary
  - ai-ml-learning
  - hypothesis-space
  - model-capacity
  - train-validation-test
  - generalization
  - overfitting
date: 2026-04-29
source_file: raw/ai_ml_learning/2026-04-29-day07-ai-ml-learning-review.md
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
Day 07는 [[HypothesisSpace]]와 [[Capacity]], [[Expressivity]], [[InductiveBias]]의 관계를 통해 모델이 얼마나 복잡한 패턴을 표현할 수 있는지와 그 대가인 과적합 위험을 정리한다. 이어서 실전 학습에서 필수인 [[TrainSet]], [[ValidationSet]], [[TestSet]] 분리의 의도를 설명하고, [[Generalization]] 관점에서 왜 최종 성능이 중요한지 다룬다. 마지막으로 [[GeneralizationGap]](또는 [[train 성능]]과 [[validation 성능]] 차이)를 정량적으로 해석하고, [[train accuracy]]가 높아도 왜 [[test accuracy]]가 낮으면 신뢰도가 떨어지는지 사례 중심으로 정리한다.

## Key Claims
- [[HypothesisSpace]]는 모델이 표현할 수 있는 가능한 규칙/함수의 집합이며, 이 집합의 크기와 다양성이 [[Capacity]]로 드러난다.
- [[Capacity]]가 낮으면 [[Underfitting]] 위험이 커지고, [[Capacity]]가 과도하게 높으면 [[Overfitting]] 및 [[DataLeakage]] 유사 형태의 신뢰도 문제로 이어질 수 있다.
- [[Capacity]] 자체는 나쁨이 아니라, 문제 난이도·데이터량·품질에 대한 균형이 핵심이며, 특히 [[LLM]]처럼 큰 [[Transformer]]에서는 큰 용량이 강력하지만 잡음/편향을 그대로 암기할 위험도 커진다.
- [[TrainSet]], [[ValidationSet]], [[TestSet]]는 학습-중간점검-최종평가의 서로 다른 역할을 갖고, 특히 [[TestSet]]는 최종 외삽 성능 추정용으로 분리해 두는 것이 원칙이다.
- 학습 중간 점검은 [[ValidationSet]]에서 반복해도 되지만, 이를 남용하면 [[ValidationSet]]에도 과도하게 맞춰져 [[Generalization]]이 떨어질 수 있다.
- [[Generalization]]은 처음 보는 데이터에서의 성능으로, [[OutOfSample]] 성능과 밀접하다.
- [[GeneralizationGap]]이 크다는 것은 훈련 데이터에 과적합했거나 데이터 분포가 다르거나, 학습-평가 파이프라인이 불안정했을 가능성을 시사한다.

## Key Quotes
> "모델은 아무 답이나 만들 수 있는 것이 아니라, 자신이 표현할 수 있는 답의 후보들 안에서만 배운다." — [[HypothesisSpace]]의 직관

> "train set은 공부용, validation set은 중간 점검용, test set은 최종 시험용으로 분리한다." — 데이터 분리의 핵심

> "generalization은 훈련 데이터가 아니라 처음 보는 데이터에서의 성능이다." — ML 목표의 본질

## Connections
- [[MachineLearning]]의 핵심은 표현력 조절이므로 [[ModelSelection]]과 [[Regularization]] 설계와 직결된다.
- [[HypothesisSpace]] — 모델이 선택 가능한 함수 집합을 제공하고, 이는 [[Capacity]]와 연결된다.
- [[Capacity]] — 표현력의 크기, 복잡한 패턴 학습 가능성, 및 [[Overfitting]]-[[Underfitting]] 트레이드오프를 설명한다.
- [[Expressivity]] — [[Capacity]]와 중첩되나, 성능 보장과는 구분되어야 한다.
- [[InductiveBias]] — 주어진 구조의 모델이 데이터가 적을 때 안정적으로 해를 가리는 경향성.
- [[TrainSet]], [[ValidationSet]], [[TestSet]] — 데이터 분할의 역할 규정.
- [[TrainValidationTestSplit]] — 시간, 사용자, 그룹 단위 분할 시점에서의 변형 전략.
- [[DataLeakage]] — 분할 무결성 붕괴의 대표 오류.
- [[Hyperparameter]] — [[ValidationSet]] 기반의 학습 설정 튜닝 대상.
- [[EarlyStopping]] — [[Overfitting]] 완화와 최적 시점 저장의 핵심 기법.
- [[Generalization]] — [[OutOfSample]], [[DistributionShift]]와의 관계로 서비스 품질 판단.
- [[GeneralizationGap]] — train/validation 또는 train/test 성능 격차의 정량 지표.
- [[LLM]] — 큰 [[Capacity]]의 양면성(능력/암기)이 특히 뚜렷하게 나타나는 사례군.

## Contradictions
- No explicit contradiction with existing wiki content was identified during this ingest pass.

## Daily Concepts
### 1. [[HypothesisSpace]]와 [[Capacity]]

- [[HypothesisSpace]]는 후보 함수들의 집합이다. 집합의 범위가 넓어질수록 [[Expressivity]]는 커지며, 데이터에 대한 적합도 또한 커진다.
- [[Capacity]]가 너무 작으면 [[Underfitting]], 너무 크면 [[Overfitting]]이 나타나는 것이 구조적이다.
- [[ModelCapacity]] 조절은 무조건 큰 모델 선호가 아니라, 문제 복잡도/데이터 품질/평가 지표의 일관성을 함께 본다.

### 2. [[TrainSet]], [[ValidationSet]], [[TestSet]] 분리

- [[TrainSet]]: 파라미터 학습에 직접 사용.
- [[ValidationSet]]: 하이퍼파라미터 탐색, 중간 점검, 조기 종료 시점 판단.
- [[TestSet]]: 최종 성능의 사실상 외부 판정 데이터, 마지막 단계에서 사용.
- [[TestSet]]를 반복 조정 루프에 쓰면 사실상 [[ValidationSet]]화되어 신뢰도가 떨어진다.

### 3. [[Generalization]]과 [[GeneralizationGap]]

- [[Generalization]]은 [[OutOfSample]] 성능이다.
- [[GeneralizationGap]]은 train 성능 대비 validation/test 성능의 열화량.
- gap이 크고 절대 성능이 높다면 과적합 가능성, gap이 작아도 절대 성능이 낮으면 [[Underfitting]]일 수 있다.

## 복습 질문 3개
1. [[HypothesisSpace]]와 [[Capacity]]는 각각 무엇을 의미하며, [[Capacity]]가 너무 작거나 너무 크면 어떤 문제가 생길까?
2. [[TrainSet]], [[ValidationSet]], [[TestSet]]는 각각 어떤 역할을 하며, [[TestSet]]를 자주 보면 왜 문제가 될까?
3. train 정확도가 99%이고 test 정확도가 75%라면 [[GeneralizationGap]] 관점에서 어떻게 해석할까?

## 복습 질문 정답

1) [[HypothesisSpace]]는 모델이 선택할 수 있는 함수/규칙의 전체 집합, [[Capacity]]는 그 후보군의 표현·조합 능력이다. capacity가 너무 작으면 [[Underfitting]], 너무 크면 [[Overfitting]]으로 훈련 데이터의 noise까지 학습한다.

2) [[TrainSet]]는 파라미터 학습, [[ValidationSet]]는 hyperparameter/조기 중단/구조 선택 점검, [[TestSet]]는 최종 검증이다. [[TestSet]]를 반복 확인하면 평가용 데이터로 유출된 판단이 생겨 실제 운영 성능을 과대평가한다.

3) train 정확도 99%와 test 정확도 75%는 [[AccuracyGap]]이 24%p로 매우 커 [[Generalization]]이 나쁨을 뜻한다. 이는 [[Overfitting]] 가능성이 크거나 [[DistributionShift]]/[[DataLeakage]]로 평가가 과대추정되었을 가능성이 높다는 신호다.