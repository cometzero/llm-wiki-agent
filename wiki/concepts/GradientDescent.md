---
title: "GradientDescent"
type: concept
tags: [optimization, machine-learning, algorithm]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

Gradient descent is an iterative optimization algorithm that minimizes a function by moving parameters in the direction opposite to the [[Gradient]] of the function. It is the core optimizer for training neural networks.

## Key Points
- Update rule: θ ← θ - η ∇L(θ), where η is the [[LearningRate]].
- The gradient points in the direction of steepest increase; moving opposite decreases the [[LossFunction]].
- Variants include stochastic gradient descent (SGD), momentum, Adam.
- [[LearningRate]] controls step size; too large can diverge, too small slows convergence.

## Connections
- [[Gradient]] — the direction used for updates.
- [[LearningRate]] — scales the gradient step.
- [[Backpropagation]] — computes the gradients used by gradient descent.
- [[LossFunction]] — the function being minimized.
- [[Derivative]] — the one-dimensional case.