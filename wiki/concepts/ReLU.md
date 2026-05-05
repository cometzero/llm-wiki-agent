---
title: "ReLU"
type: concept
tags: [ai-ml-learning, neural-networks, activation]
sources: [2026-05-05-day13-ai-ml-learning-review]
last_updated: 2026-05-05
---

## Summary
[[ReLU]] (Rectified Linear Unit) is an [[ActivationFunction]] defined as `max(0, x)`. It passes positive values through and clamps negative values to zero, adding [[Nonlinearity]] to neural networks.

## Connections
- [[ActivationFunction]] — ReLU is a common activation function.
- [[MultiLayerPerceptron]] — MLPs often use ReLU-like activations between layers.
- [[Gradient]] — ReLU has simple gradients for positive inputs, but can suffer from dead ReLU for persistently negative inputs.
