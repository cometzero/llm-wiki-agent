---
title: "AdaBoost"
type: concept
tags: [boosting, ensemble, weak-learner]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**AdaBoost** (Adaptive Boosting) is one of the first practical [[Boosting]] algorithms. It assigns higher weights to misclassified samples after each iteration, forcing the next WeakLearner to focus on hard cases. The final prediction is a weighted vote of all weak learners.

## Key Points
- Typically uses shallow [[DecisionTree|decision trees]] (stumps) as weak learners.
- Sensitive to noisy data and outliers.
- Precursor to [[GradientBoosting]].

## Connections
- [[Boosting]] — parent concept.
- [[GradientBoosting]] — generalization.
- WeakLearner — base component.
- [[Ensemble]] — broader category.