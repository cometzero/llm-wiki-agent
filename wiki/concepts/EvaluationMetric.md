---
title: "Evaluation Metric"
type: concept
tags:
  - metric
  - model-evaluation
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[EvaluationMetric]]은 모델의 성능을 수치로 표현하는 기준값이다. 같은 예측이라도 어떤 [[Metric]]을 볼지에 따라 모델의 장단점 해석이 달라질 수 있다.

## Core Idea
평가지표는 “무엇을 맞았는가”를 넘어서 “무엇을 더 중요하게 보완해야 하는가”를 결정한다. 모델 목표(비용/리스크/사용 시나리오)에 따라 적합한 지표를 골라야 한다.

## Core Metrics in Classification
- [[Accuracy]]: 전체 정답률
- [[Precision]], [[Recall]], [[F1Score]]: positive 예측의 정확성과 누락 균형
- [[AUROC]]: threshold별 구분력을 요약

## Core Principle
- [[ImbalancedData]]에서는 [[Accuracy]]만으로 의사결정하면 오판 가능성이 크다.
- threshold를 조정하면 precision-recall 관계가 바뀌므로, 실제 운영 목적에 맞는 지점을 정해야 한다.

## Relation
- [[Loss]]과 [[Metric]]는 동일하지 않다.
- [[Loss]]은 학습 최적화 목적이 되고, [[Metric]]은 사람의 성능 판단 프레임이다.