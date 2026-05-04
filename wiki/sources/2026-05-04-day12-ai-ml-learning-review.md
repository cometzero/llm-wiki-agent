---
title: "2026-05-04 AI/ML Learning Day 12 — Random Forest, Boosting, PCA"
type: source
tags: [diary, ai-ml-learning, random-forest, boosting, pca]
date: 2026-05-04
source_file: raw/ai_ml_learning/2026-05-04-day12-ai-ml-learning-review.md
source_hash: 2e32edcfdafed162
---

## Event Summary
Day 12 of AI/ML learning journey (12/30). Milestone: Classical ML models. Covered three core concepts: [[RandomForest]] and [[Bootstrap]], [[Boosting]] and AdditiveModel, [[PCA]] and [[DimensionalityReduction]].

## Key Decisions
- Focus on understanding the assumptions behind pre-deep-learning models.
- Use intuitive examples (house prices, student scores) to ground mathematical ideas.

## Energy & Mood
Not explicitly stated; assumed steady progress at beginner-intermediate level.

## Connections
- [[RandomForest]] — ensemble of [[DecisionTree|decision trees]] using [[Bootstrap]] and FeatureSubsampling to reduce [[Overfitting]].
- [[Boosting]] — sequential ensemble of weak learners (shallow trees) correcting previous errors; includes [[AdaBoost]] and [[GradientBoosting]].
- [[PCA]] — unsupervised [[DimensionalityReduction]] via eigenvectors of [[Covariance]] matrix; ExplainedVariance measures information retained.
- [[Ensemble]] — general concept of combining multiple models for stability.
- [[Bagging]] — bootstrap aggregating, used in [[RandomForest]].
- XGBoost, LightGBM, CatBoost — modern gradient boosting implementations.
- SelfConsistency — LLM technique analogous to ensemble voting.
- FeatureImportance — from [[RandomForest]]; not causal.

## Shifts & Contradictions
None with existing wiki content.

## Key Claims
- [[RandomForest]] reduces variance by averaging many decorrelated trees; [[Bootstrap]] and FeatureSubsampling are essential for decorrelation.
- [[Boosting]] builds an AdditiveModel where each new WeakLearner fits the residual of the previous ensemble.
- [[PCA]] finds directions of maximum variance without using labels; ExplainedVariance quantifies information preserved.
- [[GradientBoosting]] is often superior to deep learning on tabular data.
- PCA is useful for visualizing high-dimensional embeddings but not always optimal for classification.

## Key Quotes
> "랜덤포레스트는 '서로 조금씩 다르게 공부한 결정트리 여러 명에게 투표시키는 모델'" — Random Forest intuition.
> "부스팅은 '처음부터 강한 모델 하나를 만들기보다, 약한 모델을 하나씩 추가하면서 이전 실수를 고쳐 가는 방법'" — Boosting intuition.
> "PCA는 '데이터가 가장 많이 퍼져 있는 방향을 찾아, 그 중요한 방향 몇 개만 남겨 데이터를 더 작고 단순하게 표현하는 방법'" — PCA intuition.

## Contradictions
- None identified.