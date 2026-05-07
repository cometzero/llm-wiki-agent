---
title: "VanishingGradient"
type: concept
tags: [backpropagation, optimization, deep-learning]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
A [[VanishingGradient]] occurs when gradients become extremely small as they are propagated to earlier layers through many multiplication steps in [[Backpropagation]].

Front layers then receive almost no update signal.

## Key Claims
- Multiplicative chain terms below 1 across depth quickly push gradients toward zero.
- Early-layer learning slows or stalls while output layer may still update.

## Examples
- `1 -> 0.5 -> 0.25 -> 0.125 ...` illustrates shrinking magnitude across depth.

## Mitigations
- Proper [[Initialization]] (e.g., [[XavierInitialization]])
- Activation choice (e.g., [[ReLU]] behavior)
- [[ResidualConnection]], [[LayerNorm]], normalization techniques
