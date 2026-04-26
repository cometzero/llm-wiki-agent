---
title: "Backpropagation"
type: concept
tags: [deep-learning, optimization, algorithm]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

Backpropagation is the algorithm that computes gradients of a [[LossFunction]] with respect to all parameters in a neural network by applying the [[ChainRule]] on a [[ComputationalGraph]]. It propagates error signals from the output backward to the input.

## Key Points
- Steps: forward pass → loss computation → backward pass (gradient initialization → local gradient computation → chain rule multiplication → parameter gradient accumulation) → optimizer update.
- Enables training of deep networks by efficiently computing gradients for millions of parameters.
- [[VanishingGradient]] and [[ExplodingGradient]] are failure modes of backpropagation in very deep networks.

## Connections
- [[ChainRule]] — the mathematical foundation.
- [[ComputationalGraph]] — the structure on which backpropagation operates.
- [[GradientDescent]] — the optimizer that uses the computed gradients.
- [[Autograd]] — automated implementation of backpropagation.
- [[ForwardPass]] — the prerequisite computation.
- [[VanishingGradient]] — gradient becomes too small.
- [[ExplodingGradient]] — gradient becomes too large.