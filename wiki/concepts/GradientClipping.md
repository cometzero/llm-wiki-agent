---
title: "GradientClipping"
type: concept
tags: [optimization, training-stability, exploding-gradient]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[GradientClipping]] limits the norm or per-value magnitude of gradients before parameter updates.

It acts as a safety mechanism when backprop outputs contain occasional huge values.

## Key Claims
- It does not fix all training pathologies, but prevents extreme jump updates from dominating optimization.
- Most useful when combined with learning rate and initialization controls.
