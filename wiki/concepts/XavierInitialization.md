---
title: "XavierInitialization"
type: concept
tags: [initialization, neural-network, variance]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[XavierInitialization]] (Glorot initialization) sets weight scale based on layer connectivity (`fan_in`, `fan_out`) to keep activations in a stable range.

A common simplification uses scale proportional to `sqrt(2 / (fan_in + fan_out))`.

## Key Claims
- Helps preserve variance across layers compared to naive random assignment.
- Often paired with symmetric activations like [[Tanh]] or [[Sigmoid]].

## Related Concepts
- [[Initialization]], [[HeInitialization]], [[ActivationFunction]]
