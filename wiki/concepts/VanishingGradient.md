---
title: "VanishingGradient"
type: concept
tags: [deep-learning, optimization, problem]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

Vanishing gradient is a problem in deep neural networks where gradients become extremely small as they are backpropagated through many layers, causing early layers to learn very slowly or not at all.

## Key Points
- Caused by repeated multiplication of small local gradients (e.g., sigmoid/tanh activations).
- Makes it difficult to train very deep networks without techniques like ReLU, batch normalization, residual connections.
- Contrast with [[ExplodingGradient]] where gradients grow uncontrollably.

## Connections
- [[Backpropagation]] — the process where vanishing occurs.
- [[ExplodingGradient]] — the opposite problem.
- [[Gradient]] — the quantity that vanishes.
- [[ChainRule]] — repeated multiplication causes the issue.
- [[ComputationalGraph]] — the structure where gradients flow.