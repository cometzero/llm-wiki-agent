---
title: "2026-04-30 AI/ML Learning Day 08"
type: source
tags:
  - diary
  - ai-ml-learning
  - overfitting
  - underfitting
  - bias-variance-tradeoff
  - regularization
  - weight-decay
  - l1-l2-penalty
date: 2026-04-30
source_file: raw/ai_ml_learning/2026-04-30-day08-ai-ml-learning-review.md
sources:
  - 2026-04-30-day08-ai-ml-learning-review
last_updated: 2026-04-30
---

## Summary
Day 08는 [[Overfitting]]과 [[Underfitting]]의 구조적 차이를 학습 데이터 성능과 [[Generalization]]의 차원에서 정리한다. 모델이 훈련 데이터에서만 잘 맞추는 상태와 실제로는 새로운 데이터에서 틀리는 상태를 구분하는 진단 프레임으로 [[Bias]]와 [[Variance]]를 연결한다.

또한 [[BiasVarianceTradeoff]]의 균형을 통해 모델의 표현력과 민감도 제어가 왜 문제 특성·데이터량·잡음과 함께 조율되어야 하는지를 다루며, 마지막으로 [[Regularization]]의 핵심 실무기법인 [[L1Penalty]], [[L2Penalty]], [[WeightDecay]], [[EarlyStopping]], [[Dropout]], [[DataAugmentation]]의 목적을 한 번에 연결한다.

## Key Claims
- [[Overfitting]]은 학습 데이터 내 패턴과 노이즈를 동시에 외워 [[TrainingLoss]](또는 train 성능)는 높게 만들지만 [[ValidationLoss]]/[[ValidationSet]] 성능이 나빠지는 상태다.
- [[Underfitting]]은 모델이 데이터의 기본 규칙 자체를 충분히 못 배우는 상태로, train 성능도 test 성능도 낮게 나오는 경향이 있다.
- train 성능과 validation 성능 간의 괴리는 [[GeneralizationGap]]의 실전 신호이며, validation이 training보다 나빠질수록 [[Overfitting]] 가능성을 강하게 의심한다.
- [[Bias]]가 큰 모델은 구조적으로 단순해 표현력이 부족하고, [[Variance]]가 큰 모델은 데이터 샘플 변화에 따라 예측이 흔들리는 편이다.
- [[BiasVarianceTradeoff]]는 단순함과 복잡도 조절의 균형 문제로, 모델이 너무 단순하면 [[Underfitting]], 너무 복잡하면 [[Overfitting]]으로 흐른다.
- [[Regularization]]은 모델 복잡도를 제어해 일반화 성능을 높이는 장치이며, 특히 [[WeightDecay]], [[L1Penalty]], [[L2Penalty]]가 핵심이다.
- 정규화 강도를 과하게 주면 [[Underfitting]]이 생길 수 있으므로 [[Lambda]](정규화 강도) 조절이 핵심이다.

## Key Quotes
> "모델이 학습 데이터를 잘 외우는 것과 새 데이터를 잘 맞히는 것은 같은 말이 아니다." — Day 08의 핵심 직관

> "learning curve에서 training loss는 계속 내려가는데 validation loss가 올라가면 과적합 신호로 보는 게 일반적이다." — 학습 곡선 진단 규칙

> "L2 penalty는 큰 weight를 매우 강하게 억제하고, L1 penalty는 일부 weight를 0 근처로 밀어내 feature 선택 효과가 난다." — 정규화 벌점의 실전 차이

## Connections
- [[Overfitting]] — 학습 데이터 과적합의 실전 진단 및 원인
- [[Underfitting]] — 학습 데이터조차 설명하지 못하는 저적합 상태
- [[Generalization]] — 본원 목표
- [[GeneralizationGap]] — train/validation/test 성능 격차의 핵심 개념
- [[TrainingLoss]], [[ValidationLoss]] — 모델 성능 진단의 기본 지표
- [[TrainValidationTestSplit]] — 학습/조정/최종검증 분리의 기반
- [[Bias]]와 [[Variance]] — 오류 분해 관점
- [[BiasVarianceTradeoff]] — 모델 복잡도 균형의 핵심 구조
- [[ModelComplexity]] — 복잡도가 커질수록 noise fitting 위험 증가
- [[Regularization]] — 복잡도 제어 장치
- [[WeightDecay]], [[L1Penalty]], [[L2Penalty]] — 대표 정규화 기법
- [[LearningRate]], [[Epoch]], [[EarlyStopping]] — 정규화와 함께 쓰는 과적합 제어 수단
- [[AdamW]] — deep learning에서 [[WeightDecay]]가 실무적으로 많이 쓰이는 optimizer 축
- [[DataAugmentation]]와 [[NoiseInjection]] — 입력 차원의 보조 정규화
- [[LLM]] 및 [[Embedding]] — 텍스트/문장 패턴 학습에서 과적합·과소적합이 모두 문제로 나타나는 대표 장면
- [[Transformer]] 및 [[Attention]] 모델 학습 튜닝의 [[Hyperparameter]] 설계에서 핵심 축

## Contradictions
- No explicit contradiction with existing wiki content was identified.

## 오늘의 3개 핵심 개념

### 1) [[Overfitting]]과 [[Underfitting]]

- [[Overfitting]]: 학습 데이터의 노이즈·우연 패턴까지 과하게 맞춤
- [[Underfitting]]: 기본 규칙도 못 잡아 train 성능부터 낮음
- [[TrainingLoss]]가 낮고 [[ValidationLoss]]가 높으면 보통 [[Overfitting]]을 의심
- 둘 다 낮으면 단순성 부족을 의심(= [[Underfitting]])

실전적으로는 정답 키워드는 "새 데이터에서의 안정성"으로, 즉 [[Generalization]]의 측정치다.

### 2) [[BiasVarianceTradeoff]]

- [[Bias]]↑, [[Variance]]↓ 방향: 너무 단순한 규칙, [[Underfitting]] 위험
- [[Bias]]↓, [[Variance]]↑ 방향: 데이터 노이즈까지 추종, [[Overfitting]] 위험
- 좋은 모델은 둘 다 완전히 최소가 아니라, 문제 난이도와 데이터 크기에 맞는 균형점에 가까워야 함

### 3) [[Regularization]](정규화)와 모델 복잡도 제어

- 목적: [[LossFunction]] 최적화뿐 아니라 일반화 성능까지 고려
- 방법: loss에 penalty 추가 + 학습 과정 제어 + 데이터 제어
- 대표: [[L1Penalty]], [[L2Penalty]], [[WeightDecay]]
- 강도는 [[Lambda]]로 조절, 크면 [[Underfitting]], 작으면 과적합 방어 미약

## 복습 질문 3개

1. [[TrainingLoss]]는 낮아지는데 [[ValidationLoss]]가 올라간다면 어떤 현상을 의심해야 할까요? 왜 그런가요?
2. [[Bias]]가 큰 모델과 [[Variance]]가 큰 모델은 각각 어떤 예측 행동을 보이나요?
3. [[L1Penalty]]와 [[L2Penalty]]는 [[Weight]]에 어떤 벌점을 주며, 실전에서 어떤 차이를 만들 수 있나요?

## Follow-up 정리 답안

### 1) training loss는 내려가는데 validation loss가 올라가면?

**정답: 과적합(overfitting) 의심**

학습 데이터는 계속 잘 맞추는데, unseen 데이터의 성능은 떨어지는 패턴은 보통 모델이 규칙보다 데이터 특이 패턴을 외우는 상태다.

### 2) bias가 큰 모델과 variance가 큰 모델

- [[Bias]] 큰 모델: 예측이 구조적으로 한쪽으로 치우쳐 있고, train/val 모두 성능 저하
- [[Variance]] 큰 모델: train은 잘 맞히는데, train 샘플 변경·새 입력에서 예측이 요동

### 3) L1 vs L2

- [[L1Penalty]]: 
  - 예: w=[3, -4]일 때 `|3| + |-4| = 7`
  - 큰 penalty지만 일부 weight를 0에 가깝게 밀어내는 경향(특징 선택/희소성)
- [[L2Penalty]]: 
  - 예: w=[3, -4]일 때 `3² + (-4)² = 25`
  - 큰 weight에 극적으로 강한 제약을 주어 안정적 예측 경로를 선호
- 실전: L1은 feature가 많고 실제로 쓸 만한 것이 일부일 때 유리, L2는 딥러닝 전반에서 default에 가깝게 쓰임

## 오늘의 한 줄 요약
좋은 AI 모델은 학습 데이터 적합력과 새 데이터 일반화력을 함께 최적화하며, [[Overfitting]]과 [[Underfitting]] 사이에서 적절한 [[ModelComplexity]]를 잡고 [[Regularization]]으로 일반화를 강화한다.