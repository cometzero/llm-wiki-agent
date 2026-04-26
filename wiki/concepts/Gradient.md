---
title: "Gradient"
type: concept
tags: [calculus, optimization, machine-learning]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

The gradient is a vector of all partial derivatives of a scalar-valued function. It points in the direction of the steepest increase of the function, and its magnitude indicates the rate of increase.

## Key Points
- Gradient descent moves opposite to the gradient to minimize a [[LossFunction]].
- The directional derivative in direction v is ∇f·v; maximum when v aligns with gradient.
- [[VanishingGradient]] and [[ExplodingGradient]] are problems where gradient magnitudes become too small or too large during [[Backpropagation]].

## Connections
- [[PartialDerivative]] — components of the gradient.
- [[GradientDescent]] — optimization algorithm using gradient direction.
- [[Backpropagation]] — computes gradients through a [[ComputationalGraph]].
- [[Autograd]] — automated gradient computation.
- [[Jacobian]] — generalization to vector outputs.