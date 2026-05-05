---
title: "Linear Layer"
type: concept
tags: [ai-ml-learning, neural-networks]
sources: [2026-05-05-day13-ai-ml-learning-review]
last_updated: 2026-05-05
---

## Summary
A [[LinearLayer]] applies a matrix multiplication plus bias, commonly written as `Wx + b`. It generalizes the [[Perceptron]] weighted-sum calculation to many outputs at once.

## Connections
- [[LinearCombination]] — each output unit computes a linear combination of inputs.
- [[MultiLayerPerceptron]] — MLPs stack linear layers with [[ActivationFunction]] steps.
- [[Transformer]] — transformer feed-forward and projection layers rely on linear layers.
