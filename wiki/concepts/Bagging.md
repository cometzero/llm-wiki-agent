---
title: "Bagging"
type: concept
tags: [ensemble, bootstrap, variance-reduction]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Bagging** (Bootstrap Aggregating) is an [[Ensemble]] method that creates multiple training datasets via [[Bootstrap]] sampling, trains a separate model on each, and combines predictions by averaging (regression) or voting (classification). It primarily reduces variance.

## Key Points
- Models are trained independently (parallel).
- [[RandomForest]] extends bagging with FeatureSubsampling.
- Effective for high-variance models like [[DecisionTree|decision trees]].

## Connections
- [[Bootstrap]] — resampling technique.
- [[RandomForest]] — bagging + decision trees + feature subsampling.
- [[Ensemble]] — broader category.
- [[Variance]] — what bagging reduces.