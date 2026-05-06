---
title: "Backpropagation"
type: concept
tags: [deep-learning, optimization, algorithm, training]
sources: [2026-04-26-day04-ai-ml-learning-review, 2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

Backpropagation is the algorithm that computes gradients of a [[LossFunction]] with respect to all parameters in a neural network by applying the [[ChainRule]] on a [[ComputationalGraph]]. It propagates error signals from the output backward to the input.

Day 14 emphasizes that backpropagation does **not** directly update [[Parameters]]. It solves the [[CreditAssignment]] problem by computing gradients for weights, biases, and intermediate layers; an [[Optimizer]] then uses those gradients to update parameter values.

## Key Points
- Steps: forward pass → loss computation → backward pass (gradient initialization → local gradient computation → chain rule multiplication → parameter gradient accumulation) → optimizer update.
- Enables training of deep networks by efficiently computing gradients for millions or billions of parameters.
- [[VanishingGradient]] and [[ExplodingGradient]] are failure modes of backpropagation in very deep networks.
- Stable [[GradientFlow]] is crucial for training modern architectures such as [[Transformer]]s.

## Connections
- [[ChainRule]] — the mathematical foundation.
- [[ComputationalGraph]] — the structure on which backpropagation operates.
- [[GradientDescent]] — an optimizer family that uses computed gradients.
- [[Optimizer]] — updates parameters after gradients are computed.
- [[Autograd]] — automated implementation of backpropagation.
- [[ForwardPass]] — the prerequisite computation.
- [[CreditAssignment]] — responsibility assignment problem solved by gradient propagation.
- [[VanishingGradient]] — gradient becomes too small.
- [[ExplodingGradient]] — gradient becomes too large.
