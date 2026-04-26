---
title: "2026-04-26 AI/ML Learning Day 04 — Derivatives, Gradients, and Backpropagation"
type: source
tags: [diary, ai-ml-learning, derivative, gradient, backpropagation]
date: 2026-04-26
source_file: raw/ai_ml_learning/2026-04-26-day04-ai-ml-learning-review.md
---

## Event Summary
Day 04 of a 30-day AI/ML learning review focused on the core of differentiation and optimization. The session covered three key concepts: [[Derivative]] and rate of change, [[PartialDerivative]] and [[Gradient]], and [[ChainRule]] with [[ComputationalGraph]]. The material connects these mathematical tools directly to how [[GradientDescent]] and [[Backpropagation]] enable training of large neural networks.

## Key Decisions
- Focus on understanding the relationship between local linearization (first-order approximation) and optimization, rather than just memorizing formulas.
- Emphasize the directional derivative interpretation of gradient as the direction of steepest ascent.
- Treat backpropagation as a systematic application of the chain rule on a computational graph.

## Energy & Mood
Not explicitly recorded, but the structured review questions and detailed answers suggest a thorough, self-paced study session.

## Connections
- [[Derivative]] — local rate of change, slope of tangent, first-order approximation
- [[PartialDerivative]] — sensitivity of multi-variable functions to one variable
- [[Gradient]] — vector of partial derivatives, direction of steepest ascent
- [[ChainRule]] — composition of derivatives via multiplication
- [[ComputationalGraph]] — decomposition of complex models into atomic operations
- [[Backpropagation]] — algorithm that applies chain rule on computational graph
- [[GradientDescent]] — optimization algorithm that moves opposite to gradient
- [[LossFunction]] — the function being minimized (connects to [[2026-04-25 AI/ML Learning Day 03]])
- [[LearningRate]] — step size in gradient descent, tied to local linearization
- [[Autograd]] — automated gradient computation system
- [[VanishingGradient]] — gradient flow problem in deep networks
- [[ExplodingGradient]] — gradient flow problem in deep networks
- [[DirectionalDerivative]] — rate of change in an arbitrary direction
- [[Jacobian]] — generalization of gradient to vector-valued functions
- [[ForwardPass]] — computation of values in computational graph
- [[BackwardPass]] — propagation of gradients from output to input

## Shifts & Contradictions
None. This source is consistent with the mathematical foundations laid in [[2026-04-23 AI/ML Learning Day 01]] (linear algebra) and [[2026-04-25 AI/ML Learning Day 03]] (loss functions). It deepens the understanding of how gradients are computed and used in optimization.