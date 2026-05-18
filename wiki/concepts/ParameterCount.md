---
title: "Parameter Count"
type: concept
tags: [llm, model-size, architecture]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
The number of learnable parameters (weights and biases) in a neural network model. In Transformers, this includes embedding matrices, attention projection weights, and feed-forward layer weights.

## Scale in Modern LLMs
- Small models: millions of parameters
- Popular open models (LLaMA, Mistral): 7B-70B parameters
- Frontier models (GPT-4, Claude, Gemini): hundreds of billions

## Components in Transformer Architecture
- Token embeddings
- Position embeddings
- Query/Key/Value projection matrices
- Attention output projections
- Feed-forward network weights
- Layer normalization parameters

## Trade-offs
- Larger models: more capacity to store patterns, but higher training and inference costs
- Smaller models: faster and cheaper, but may lack representation capacity
- [[ScalingLaw]] guides optimal parameter count given data and compute

## Connections
- Key dimension in [[ScalingLaw]] alongside [[DataScaling]] and [[ComputeBudget]]
- Directly affects [[ComputeBudget]] requirements
- Related to model serving costs and [[InferenceOptimization]]
- [[ParameterEfficientFineTuning]] methods (LoRA, adapters) reduce trainable parameters
