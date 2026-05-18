---
title: "Chinchilla Scaling"
type: concept
tags: [llm, scaling, training]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
Chinchilla scaling refers to the compute-optimal training insight that model size and training data should be balanced, rather than increasing parameters alone.

## Key Points
- A model can be too large for the number of tokens it sees, wasting capacity.
- More training tokens can be more valuable than simply adding parameters under a fixed compute budget.
- This is a practical refinement of broader [[ScalingLaw]] reasoning.

## Connections
- Connects [[ParameterCount]], [[DataScaling]], and [[ComputeBudget]] into one planning trade-off.
