---
title: "Gradient Boosting"
type: concept
tags: [boosting, additive-model, gradient-descent]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Gradient Boosting** is a [[Boosting]] method where each new WeakLearner is trained to fit the negative gradient of the loss function with respect to the current ensemble's predictions. This generalizes [[AdaBoost]] to arbitrary differentiable loss functions.

## Key Points
- Builds an AdditiveModel sequentially.
- [[LearningRate]] (shrinkage) controls contribution of each new learner.
- Popular implementations: XGBoost, LightGBM, CatBoost.
- Often state-of-the-art on tabular data.
- Prone to overfitting if hyperparameters (n_estimators, max_depth, learning_rate) are not tuned.

## Connections
- [[Boosting]] — parent concept.
- AdditiveModel — mathematical form.
- [[GradientDescent]] — conceptual similarity.
- [[Residual]] — what each learner fits.
- [[DecisionTree]] — typical weak learner.