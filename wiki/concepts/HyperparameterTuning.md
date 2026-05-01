---
title: "Hyperparameter Tuning"
type: concept
tags:
  - model-selection
  - training
  - optimization
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[HyperparameterTuning]]은 사람이 정하는 학습 설정(예: [[LearningRate]], [[TreeDepth]], [[Regularization]], [[BatchSize]])의 조합을 탐색해 좋은 모델을 고르는 과정이다.

## Core rule
[[ValidationSet]]을 기준으로 여러 설정을 비교하고, 최종 모델 품질 평가는 [[TestSet]]로 한정한다.

## Relation
- [[CrossValidation]], [[Generalization]], [[Overfitting]], [[Underfitting]], [[EarlyStopping]].