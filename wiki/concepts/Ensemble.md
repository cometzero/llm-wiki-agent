---
title: "Ensemble"
type: concept
tags: [machine-learning, bagging, boosting]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Ensemble** methods combine multiple machine learning models to produce a single, more robust prediction. The key idea is that aggregating diverse models reduces variance and improves generalization.

## Types
- **[[Bagging]]** (e.g., [[RandomForest]]): Train models independently in parallel, then average/vote.
- **[[Boosting]]** (e.g., [[AdaBoost]], [[GradientBoosting]]): Train models sequentially, each correcting previous errors.
- **Stacking**: Train a meta-model on outputs of base models.

## Key Points
- Diversity among models is crucial; identical models provide no benefit.
- Ensemble methods are widely used in tabular data competitions (e.g., Kaggle).
- The concept extends to LLMs (e.g., SelfConsistency, multiple chain-of-thought samples).

## Connections
- [[RandomForest]] — bagging + decision trees.
- [[Boosting]] — sequential ensemble.
- [[Bootstrap]] — resampling for diversity.
- [[Variance]] — ensemble reduces variance.