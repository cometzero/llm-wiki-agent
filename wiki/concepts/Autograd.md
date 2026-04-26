---
title: "Autograd"
type: concept
tags: [deep-learning, software, automatic-differentiation]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

Autograd (automatic differentiation) is a technique that automatically computes gradients by recording operations performed on tensors and then applying the [[ChainRule]] in reverse. It is the engine behind frameworks like PyTorch and TensorFlow.

## Key Points
- Builds a [[ComputationalGraph]] implicitly during the forward pass.
- Backward pass traverses the graph to compute gradients of all parameters.
- Eliminates the need for manual derivative computation.
- [[VanishingGradient]] and [[ExplodingGradient]] are numerical issues that autograd cannot prevent but can help detect.

## Connections
- [[Backpropagation]] — the algorithm autograd implements.
- [[ComputationalGraph]] — the data structure autograd uses.
- [[ChainRule]] — the mathematical rule autograd applies.
- [[GradientDescent]] — the optimizer that consumes autograd's output.