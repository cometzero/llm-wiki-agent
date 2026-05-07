---
title: "HeInitialization"
type: concept
tags: [initialization, relu, neural-network]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[HeInitialization]] is commonly used with [[ReLU]]-like activations and sets weight scale based mainly on `fan_in`.

A common rule uses approximately `sqrt(2 / fan_in)`.

## Key Claims
- Better matches ReLU behavior where roughly half activations can be zero.
- Controls variance so layers do not inflate signals as depth grows.

## Related Concepts
- [[Initialization]], [[ReLU]], [[Variance]], [[VanishingGradient]], [[ExplodingGradient]]
