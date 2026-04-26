---
title: "ExplodingGradient"
type: concept
tags: [deep-learning, optimization, problem]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

Exploding gradient is a problem in deep neural networks where gradients become extremely large during [[Backpropagation]], causing unstable updates and divergence of the training process.

## Key Points
- Often occurs in recurrent networks or very deep networks with large weights.
- Mitigated by gradient clipping, careful weight initialization, and normalization techniques.
- Contrast with [[VanishingGradient]] where gradients become too small.

## Connections
- [[Backpropagation]] — the process where exploding occurs.
- [[VanishingGradient]] — the opposite problem.
- [[Gradient]] — the quantity that explodes.
- [[ChainRule]] — repeated multiplication of large local gradients causes the issue.
- [[GradientDescent]] — the optimizer that becomes unstable.