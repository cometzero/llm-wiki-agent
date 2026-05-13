---
title: "Compatibility Score"
type: concept
tags: [attention, transformer]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Compatibility Score** measures how well a [[Query]] matches a [[Key]], determining the initial attention weight before softmax. Computed via [[DotProduct]].

## Key Concepts
- Also called "attention score" or "similarity score"
- Computed: `score = q · k` (dot product)
- Later passed through [[Softmax]] to get [[AttentionWeight]]
- Higher score = query and key are more aligned

## Connections
- [[Query]], [[Key]] — inputs to compatibility calculation
- [[DotProduct]] — computation method
- [[Softmax]] — converts score to weight
- [[ScaledDotProductAttention]] — scaling is applied before softmax
