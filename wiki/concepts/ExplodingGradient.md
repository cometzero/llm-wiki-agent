---
title: "ExplodingGradient"
type: concept
tags: [backpropagation, optimization, training-stability]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[ExplodingGradient]] occurs when gradients grow too large during backpropagation, often due to repeated multiplicative growth.

This produces unstable parameter jumps and can make training diverge.

## Key Claims
- Multiplicative chain factors greater than 1 repeatedly can produce huge gradients.
- This often causes loss spikes, noisy optimization, or NaN updates.

## Example
- `1 -> 2 -> 4 -> 8 -> 16 ...` shows rapid growth.

## Mitigations
- [[GradientClipping]]
- Reasonable [[LearningRate]]
- Stable [[Initialization]] and normalization
- [[ResidualConnection]] / [[LayerNorm]] for deep stacks
