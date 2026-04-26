---
title: "Derivative"
type: concept
tags: [calculus, optimization, machine-learning]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

The derivative measures the instantaneous rate of change of a function at a point. It is the slope of the tangent line and provides a first-order (linear) approximation of the function near that point.

## Key Points
- Derivative = local sensitivity of output to input changes.
- Foundation for [[GradientDescent]]: the optimizer uses the derivative to decide whether to increase or decrease a parameter.
- [[LearningRate]] scales the step based on the derivative magnitude.
- In multiple dimensions, the [[Gradient]] generalizes the derivative.

## Connections
- [[PartialDerivative]] — derivative with respect to one variable in a multi-variable function.
- [[ChainRule]] — how derivatives compose through function composition.
- [[Backpropagation]] — systematic application of derivatives through a [[ComputationalGraph]].
- [[LossFunction]] — the function whose derivative is computed during optimization.