---
title: "GradientNormClipping"
type: concept
tags: [ml, optimization, training-stability]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
[[GradientNormClipping]] is a training technique that constrains the L2 [[Norm]] of the gradient vector to a maximum threshold, preventing exploding gradients during backpropagation.

## Mechanism
- If ‖∇‖ > threshold, scale ∇ ← ∇ × (threshold / ‖∇‖).
- Preserves gradient direction (analogous to [[CosineSimilarity]] preserving direction) while capping magnitude.

## Connection to AI/ML
- Essential for training stability in deep [[LLM]]s, especially with long sequences.
- Directly relies on the L2 [[Norm]] concept.
- Related to [[Regularization]] in that both constrain parameter/gradient magnitudes, but clipping operates on gradients while regularization operates on weights.

## Sources
- [[2026-04-23-day01-ai-ml-learning-review]]