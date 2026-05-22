---
title: "Training Stack"
type: concept
tags: [ai-ml, training, infrastructure, mlops]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

The [[TrainingStack]] encompasses all infrastructure for training models: training code, data loaders, GPUs, optimizers, loss functions, and distributed training tools.

## Components

1. **Training code**: Model architecture, forward/backward passes
2. **Data loader**: Efficient data fetching and batching
3. **Hardware**: GPUs, TPUs, distributed training clusters
4. **Optimizer**: Loss minimization algorithm (Adam, SGD, etc.)
5. **Distributed training**: Multi-GPU, multi-node parallelism
6. **Checkpointing**: Saving model states during training

## Key Concepts

- **Loss function**: Measures prediction error
- **Gradient**: Direction and magnitude of weight updates
- **Optimizer**: Algorithm for applying gradients to weights
- **[[ScalingLaws]]**: Guidelines for model size vs. data size trade-offs

## Connection to Inference

Training stack and [[InferenceStack]] have different priorities:
- Training: Maximize learning quality,不在乎 latency
- Inference: Maximize speed and efficiency

This is why models trained for weeks may need conversion/optimization before serving.

## Connections
- [[InferenceStack]] — serves what training stack produces
- [[DataPipeline]] — provides training data
- [[FeedbackLoop]] — training may use feedback data
- [[Evaluation]] — evaluates trained model quality
