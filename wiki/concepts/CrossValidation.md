---
title: "Cross Validation"
type: concept
tags:
  - evaluation
  - model-validation
  - generalization
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[CrossValidation]]은 전체 데이터를 여러 번 분할해 [[ValidationSet]] 성능을 여러 번 계산하고 평균내는 평가 방법이다. 단일 분할에서 생기는 운(우연)에 덜 민감하게 만들어 [[Generalization]] 추정을 안정화한다.

## Core Idea
단일한 train/validation split은 데이터가 적거나 샘플 분포가 잡음이 많을 때 편향이 클 수 있다. [[KFoldCrossValidation]]은 이를 완화해, 매번 다른 fold를 validation으로 쓰고 나머지로 학습해 반복 측정한다.

## Procedure
- 데이터를 K개의 fold로 분할한다.
- 각 fold를 한 번씩 validation으로 두고 K번 학습/평가한다.
- K개의 성능을 평균(및 분산/편차)로 본다.
- 단, test 집합은 최종 성능 확인에만 사용한다.

## Relation to Other Concepts
- [[TrainValidationTestSplit]]의 의도를 보강한다.
- [[HyperparameterTuning]]에서 설정 비교의 신뢰도를 높인다.
- [[GeneralizationGap]]을 줄이는 추정 절차에 가깝다.

## Notes
- [[Overfitting]] 점검, 모델 튜닝, 소규모 데이터 환경에서 특히 유용하다.
- 비용이 커서 딥러닝 대형 모델에서는 full K-fold를 모두 실행하기 어렵기 때문에 대체 전략을 함께 사용하기도 한다.

## Key Claims
- 교차검증은 성능의 "한 번성”을 다스리는 기법이다.
- 평균 성능이 높은 것보다, 분할 간 성능 변동성도 안정성 판단에 중요하다.
- [[ValidationSet]] 반복 사용만으로 test 역할을 수행하면 누수 위험이 커지므로 엄격한 분리 원칙이 필요하다.