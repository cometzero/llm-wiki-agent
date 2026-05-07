---
title: "SymmetryBreaking"
type: concept
tags: [initialization, representation, neural-network]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[SymmetryBreaking]] means giving neurons different starting conditions so they can learn different functions.

If all neurons in a layer start identically, they receive identical gradients and remain functionally redundant.

## Key Claims
- Same init values can cause neurons to evolve identically.
- Randomized initial weights reduce symmetry and increase representational diversity.

## Why it matters
- Diversity across neurons enables richer [[FeatureExtraction]] and better decomposition of signals.
