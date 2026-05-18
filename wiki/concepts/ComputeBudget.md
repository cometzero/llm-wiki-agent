---
title: "Compute Budget"
type: concept
tags: [llm, training, resources]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
The total computational resources available for training, measured in GPU hours, FLOPs (floating-point operations), or monetary cost. It determines how long and how thoroughly a model can be trained.

## Key Factors
- **GPU count**: Number of GPUs available for distributed training
- **GPU type**: H100 vs A100 vs other accelerators
- **Training duration**: How many hours/days/weeks the training run lasts
- **Efficiency**: Hardware utilization, parallelization strategies

## Relationship to Model Development
- Compute budget is often the primary constraint
- [[ScalingLaw]] helps allocate compute between:
  - Model size (more parameters)
  - Data scale (more training tokens)
  - Training duration (more passes over data)

## Practical Decisions
- "Should we train a 7B model longer or a 13B model shorter?"
- "Do we need more data or a bigger model?"
- [[ScalingLaw]] provides guidance for these budget allocation decisions

## Connections
- Core dimension of [[ScalingLaw]]
- Affects [[ParameterCount]] (larger models need more compute)
- Related to training infrastructure: [[DistributedTraining]], GPU clusters
- Links to inference cost considerations (larger models = more compute per query)
