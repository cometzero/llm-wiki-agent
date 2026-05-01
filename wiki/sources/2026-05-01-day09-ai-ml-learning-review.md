---
title: "2026-05-01 AI/ML Learning Day 09"
type: source
tags:
  - diary
  - ai-ml-learning
  - cross-validation
  - evaluation-metric
  - regression
  - classification
  - loss
  - model-generalization
  - overfitting
  - model-selection
date: 2026-05-01
source_file: raw/ai_ml_learning/2026-05-01-day09-ai-ml-learning-review.md
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
Day 09는 [[Generalization]]을 안정적으로 추정하기 위한 실전 학습 프레임을 정리한다. 핵심은 [[CrossValidation]]을 통해 평가의 분산을 줄이고, 문제 특성에 맞는 [[EvaluationMetric|metric]]를 선택하며, [[Regression]]과 [[Classification]]의 목적에 맞는 [[Loss|loss function]]를 구분해 학습 신호를 정확히 설계하는 것이다.

특히 한 번의 split으로 성능을 재는 방식이 얼마나 불안정할 수 있는지 보여 주고, 여러 번 나누어 본 평균 성능이 왜 더 신뢰 가능한지 설명한다. 이어서 임계값 기반 분류의 함정(imbalanced data, precision-recall trade-off), 그리고 regression/classification에서의 최적화 대상 차이를 통해 실무에서의 모델 튜닝 방향을 정리한다.

Follow-up 정리에서 제시된 복습 정답은 개념 정리와 일치하며, 각 개념을 실제 모델 결정(하이퍼파라미터 튜닝, 운영 지표 설계, 손실 선택)로 연결한다.

## Key Claims
- [[CrossValidation]]은 데이터를 여러 번 나누어 [[TrainValidationTestSplit|train/validation/test]] 전략을 더 안정적으로 보완하는 평가 방법으로, 단일 validation split의 운(우연) 의존도를 줄인다.
- 과적합을 피하고 성능을 신뢰성 있게 비교하려면 [[ValidationSet]]은 [[HyperparameterTuning|모델 설정 조정]]에, [[TestSet]]는 최종 한 번의 신호용 평가에 쓰는 분리 원칙이 중요하다.
- 평가에서 [[Metric]]는 단순한 보고 숫자가 아니라 제품/도메인 목표를 반영한 의사결정 기준이며, [[Accuracy]]만으로는 [[ImbalancedData]] 상황에서 큰 오판을 낳을 수 있다.
- 분류는 TP/TN/FP/FN로 분해하고 [[Precision]], [[Recall]], [[F1Score]], [[AUROC]]를 함께 해석해야 하며, [[Threshold]] 설정은 recall-precision trade-off를 직접 바꾼다.
- 회귀와 분류의 손실은 본질적으로 다르며, regression은 값의 거리(예: 오차) 중심의 penalty가, classification은 정답 class 확률 배치 중심의 penalty가 핵심이다.
- [[RegressionLoss]]과 [[ClassificationLoss]]의 차이는 LLM 학습 포함 전체 파이프라인에서 optimizer가 받는 학호신호가 달라지는 원인이다.

## Key Quotes
> "교차검증은 한 번의 운 좋은 split/운 나쁜 split에 덜 흔들리고, 여러 상황에서 성능이 얼마나 안정적인지 본다." — Day 09 핵심 직관

> "평가지표는 모델의 성능을 숫자로 표현하는 방법이 아니라, 어떤 실수를 덜 중요하고 더 중요하게 만들지 정하는 기준이다." — 분류 평가 핵심

> "손실은 학습 중 optimizer가 파라미터를 어떻게 바꿀지 알려주는 신호이고, metric은 사람이 성능을 해석하는 척도다." — 손실/지표 분리의 핵심

## Connections
- [[Overfitting]]: 데이터 분할과 반복 검증으로 신뢰도 보완
- [[Underfitting]]: metric/손실 설계가 틀리면 train/val 모두에서 놓치기 쉬움
- [[Generalization]]: 교차검증 및 다중 지표를 통한 추정 안정화
- [[CrossValidation]]: K-fold 분할 기반의 안정적 평가
- [[KFoldCrossValidation]]: K번 반복되는 실전 평가 절차
- [[ValidationSet]], [[ValidationLoss]], [[ValidationAccuracy]]: 튜닝/중간 점검 데이터의 역할
- [[TrainValidationTestSplit]]: 교육-검증-최종평가 분리 원칙
- [[HyperparameterTuning]]: 모델 설정 조합(learning rate, tree depth, regularization 등) 비교
- [[EvaluationMetric]]: 목표 정렬형 성능 척도 체계
- [[Accuracy]], [[Precision]], [[Recall]], [[F1Score]], [[AUROC]]: 분류 문제의 핵심 지표군
- [[ConfusionMatrix]]: TP/TN/FP/FN 구조의 기본 해석 틀
- [[ImbalancedData]]: accuracy 함정이 크게 드러나는 데이터 분포
- [[Threshold]], [[Classification]]: 확률 임계값이 성능 지표 트레이드오프를 좌우
- [[Regression]], [[Classification]], [[RegressionLoss]], [[ClassificationLoss]], [[CrossEntropy]], [[MSE]], [[MAE]]: 손실 설계의 문제형 적합성
- [[Optimizer]], [[Gradient]], [[LearningRate]]: 손실 함수 선택이 직접 학습 신호에 반영
- [[LLM]]: 다음 토큰 분류 관점에서 [[CrossEntropy]]가 핵심 손실로 작동

## Contradictions
- No explicit contradiction with existing wiki content was identified.

## 1) 교차검증의 목적
- [[CrossValidation]]은 한 번의 split에서 생길 수 있는 분할 편향을 완화해, 모델 성능을 여러 데이터 분할에서 반복 측정한 뒤 [[Average]]로 추정한다.
- 교차검증은 모델 성능을 올리는 기법이 아니라, 성능 추정의 신뢰도를 높이는 기법이다.
- 핵심 오해를 피하려면 [[ValidationSet]]에서만 모델을 선택하고, 최종 품질 판정은 별도 [[TestSet]]로 마무리해야 한다.

## 2) 평가지표의 선택
- [[Metric]]은 문제 목적이 다르면 성능 해석이 완전히 달라진다.
- [[Accuracy]]는 클래스 비율이 치우친 [[ImbalancedData]]에서 오판정 가능성이 크므로 [[Precision]], [[Recall]], [[F1Score]]와 함께 본다.
- [[Threshold]]를 바꾸면 분류의 오답 유형 분포가 이동해 precision/recall trade-off가 생긴다.

## 3) 회귀와 분류의 손실 차이
- [[Regression]]은 연속값 오차를 벌점화하며 [[MSE]]/[[MAE]]류가 직관적이다.
- [[Classification]]은 정답 class에 대한 확률 배치의 질을 벌점화하며 [[CrossEntropy]]/log loss 관점이 중심이다.
- 같은 모델이라도 metric(해석 지표)과 loss(학습 신호)를 분리해 이해해야 한다.

## 복습 질문 3개
1. [[CrossValidation]]이 [[ValidationSet]] 단일 split보다 안정적인 이유는 무엇인가요?
2. [[Accuracy]]가 95%이지만 실제로는 나쁜 모델일 수 있는 상황은?
3. [[Regression]]과 [[Classification]]에서 [[Loss]]가 다른 이유는 무엇인가요?

## 오늘의 한 줄 요약
[[TrainValidationTestSplit]], [[CrossValidation]], 그리고 적절한 [[Metric]]·[[Loss]] 설계가 결합될 때 모델은 train 데이터 적합만이 아니라 새 데이터에서도 믿을 수 있는 성능을 갖게 된다.