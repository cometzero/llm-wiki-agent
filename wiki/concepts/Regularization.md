---
title: "Regularization"
type: concept
tags: [machine-learning, optimization, generalization, deep-learning]
sources: [2026-04-25-day03-ai-ml-learning-review, 2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

# Regularization

[[Regularization]] is any constraint, penalty, architectural choice, or training procedure that discourages overly complex models and improves generalization.

## Core Idea
- It controls model capacity.
- It helps prevent [[Overfitting]], especially in sparse, high-dimensional, or high-parameter regimes.
- It can be implemented through penalties, architectural constraints, data augmentation, early stopping, or stochastic training methods.
- In Day 16, [[Dropout]] is introduced as a stochastic regularization technique that randomly removes activations during training.

## Connections
- [[CurseOfDimensionality]] — one of the main reasons regularization matters.
- [[HypothesisSpace]] — regularization effectively narrows the usable region of the search space.
- [[Dropout]], [[Overfitting]], [[2026-05-08-day16-ai-ml-learning-review]]
