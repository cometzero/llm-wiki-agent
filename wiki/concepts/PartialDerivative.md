---
title: "PartialDerivative"
type: concept
tags: [calculus, optimization, machine-learning]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

A partial derivative measures how a multi-variable function changes when only one variable is varied while holding others constant. It is the derivative of the function with respect to a single input dimension.

## Key Points
- Partial derivatives are the components of the [[Gradient]] vector.
- Used to compute sensitivity of a [[LossFunction]] to each parameter individually.
- Essential for [[Backpropagation]] where gradients flow through multiple dimensions.

## Connections
- [[Derivative]] — the single-variable case.
- [[Gradient]] — vector of all partial derivatives.
- [[DirectionalDerivative]] — rate of change in an arbitrary direction, expressed as dot product with gradient.
- [[Jacobian]] — matrix of partial derivatives for vector-valued functions.