---
title: "Random Forest"
type: concept
tags: [ensemble, decision-tree, bootstrap, bagging]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Random Forest** is an [[Ensemble]] learning method that constructs many [[DecisionTree|decision trees]] during training and outputs the mode (classification) or mean (regression) of the individual trees. It reduces [[Overfitting]] and variance by decorrelating trees via [[Bootstrap]] sampling and FeatureSubsampling.

## Key Points
- Uses [[Bagging]] (bootstrap aggregating) to create diverse training sets for each tree.
- FeatureSubsampling: at each split, only a random subset of features is considered.
- Effective on tabular data; does not require feature scaling.
- Provides FeatureImportance scores, but these are not causal.
- Not ideal for raw image/text/audio data.

## Connections
- [[Boosting]] — another ensemble method, but sequential rather than parallel.
- [[DecisionTree]] — base learner.
- [[Bootstrap]] — resampling technique.
- [[Overfitting]] — problem that random forest mitigates.
- SelfConsistency — LLM technique with similar ensemble spirit.