---
title: "Distributed Training"
type: concept
tags: [training, compute, infrastructure]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
Distributed training uses multiple accelerators or machines to train a model faster or to train models too large for a single device.

## Key Points
- It is a practical way to spend a large [[ComputeBudget]].
- Common forms include data parallelism, tensor/model parallelism, and pipeline parallelism.
- Communication overhead and memory placement become major engineering concerns at LLM scale.

## Connections
- Larger [[ParameterCount]] and [[DataScaling]] often require distributed training to be feasible.
