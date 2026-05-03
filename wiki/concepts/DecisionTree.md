---
title: "Decision Tree"
type: concept
tags:
  - tree-model
  - interpretable-ml
  - information-gain
  - classification
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[DecisionTree]]는 규칙(feature 조건 질문)을 순차적으로 적용해 데이터를 분할하고, 마지막 노드에서 예측값을 결정하는 분류/회귀 모델이다.

## Structure
- RootNode: 첫 질문
- InternalNode: 중간 분기
- [[LeafNode]]: 최종 예측
- Split: 질문 조건으로 좌/우 그룹으로 나누기

## Split Quality
- [[InformationGain]]
- [[Entropy]](또는 불확실성) 감소량이 큰 split을 선호
- [[GiniImpurity]]는 유사한 역할의 대체 지표

## Overfitting Control
- 트리가 너무 깊으면 훈련 데이터 노이즈를 과적합
- Pruning, MaxDepth, 최소 그룹 크기 조건으로 제어

## Relations
- 트리 기반 앙상블: RandomForest, GradientBoosting, XGBoost, LightGBM, CatBoost
- 기존 DeepModel 대비 해석 가능성이 높고, tabular data에서 실무 성능이 강함
- [[LLM]] 본체보다는 Explainability 관점의 기준 모델로 활용 빈도가 높음.