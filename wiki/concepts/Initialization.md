---
title: "Initialization"
type: concept
tags: [training-stability, weights, neural-network]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[Initialization]] defines the starting values of model parameters before training.

In neural networks, it strongly affects signal/gradient scale during early training and can determine whether learning is stable, slow, or diverges.

## Key Claims
- Initialization is not arbitrary: scale must be controlled.
- If weights are too large, forward/backward values can explode.
- If too small, signal can disappear and learning stalls.
- [[SymmetryBreaking]] is necessary so neurons can learn different features.

## Related Methods
- [[XavierInitialization]]
- [[HeInitialization]]

## Practical Checklist
1. Use random, non-identical start values.
2. Match scale to activation family.
3. Pair with optimization/norm techniques ([[LayerNorm]], [[ResidualConnection]], [[GradientClipping]]).

## Common Pitfalls
- Zero initialization for hidden-layer weights causes redundant neurons.
- Forgetting scale often causes NaN or no-learning traces.
