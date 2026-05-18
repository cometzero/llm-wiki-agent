---
title: "Scaling Law"
type: concept
tags: [llm, training, scaling]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
An empirical relationship describing how model performance (measured by loss) varies predictably with model size (parameter count), data scale (training tokens), and compute budget (GPU hours/operations/cost).

## Key Components

### Parameter Count
- Number of learnable parameters in the model
- In Transformers: embedding matrices, Q/K/V projections, feed-forward layers
- Modern LLMs: billions to hundreds of billions of parameters

### Data Scaling
- Amount and diversity of training tokens
- More data = exposure to more contextual patterns
- Data quality and diversity matter as much as quantity

### Compute Budget
- Total computational resources for training
- Includes GPU hours, FLOPs, and cost
- Determines how fully a model can converge

## Core Insight
**Balance, not just "bigger is better."** Simply scaling one dimension while neglecting others leads to inefficiency:
- Large model + insufficient data → underutilized capacity
- Large data + small model → insufficient representation capacity
- Large model + large data + insufficient compute → incomplete convergence

## Mathematical Perspective
- Performance improvements follow predictable curves
- Diminishing returns apply to all three dimensions
- Optimal training plans find the best combination within a given compute budget

## Related Concepts
- [[ParameterCount]] — the size dimension of scaling
- [[ComputeBudget]] — the resource dimension
- [[DataScaling]] — the data dimension
- [[ChinchillaScaling]] — the hypothesis that model size and data should be scaled proportionally

## Connections
- [[ScalingLaw]] is foundational to decisions about GPT, LLaMA, Claude model development
- Guides practical decisions like "train 7B longer or 13B shorter?"
- Links to inference cost considerations
