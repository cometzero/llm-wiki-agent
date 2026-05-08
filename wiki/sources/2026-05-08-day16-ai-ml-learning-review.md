---
title: "AI/ML Learning Review Day 16 (2026-05-08)"
type: source
tags: [deep-learning, training, normalization, regularization]
date: 2026-05-08
source_file: raw/ai_ml_learning/2026-05-08-day16-ai-ml-learning-review.md
source_hash: 2ec1727cb1aa5499
---

## Summary
Day 16 of the AI/ML learning journey covers three fundamental deep learning training concepts: epoch/iteration/batch size, Batch Normalization ([[BatchNormalization]]), and [[Dropout]]. The lesson explains how training data is divided into mini-batches, why normalizing intermediate activations stabilizes training, and how randomly dropping neurons prevents overfitting. The follow-up review reinforces these concepts with practical examples and connections to real training workflows.

## Key Claims
- [[Epoch]], [[Iteration]], and [[BatchSize]] are the core units of deep learning training: epoch = one full pass over the dataset, iteration = one optimizer update, batch size = number of samples per update.
- [[BatchNormalization]] normalizes mini-batch activations to zero mean and unit variance, then applies learnable scale (gamma) and shift (beta) to stabilize training and reduce internal covariate shift.
- [[Dropout]] randomly zeroes out a fraction of activations during training (with inverted scaling) to prevent co-adaptation and overfitting; it is turned off during inference.
- Training and inference behavior differ for both BatchNorm and Dropout: BatchNorm uses running statistics at inference, Dropout is disabled.
- [[GradientAccumulation]] allows effective larger batch sizes by accumulating gradients over multiple micro-batches before an optimizer step.

## Key Quotes
> "epoch은 전체 training dataset을 모델이 한 번 모두 본 것을 뜻한다." — Epoch definition
> "BatchNorm은 layer 중간값들의 평균과 크기를 너무 들쭉날쭉하지 않게 맞춰서, 딥러닝 모델이 더 안정적으로 학습되도록 돕는 방법이다." — BatchNorm intuition
> "Dropout은 학습 중에 neural network의 일부 neuron을 일부러 랜덤하게 꺼서, 모델이 특정 neuron 몇 개에만 과하게 의존하지 않도록 만드는 방법이다." — Dropout intuition

## Connections
- [[Epoch]] — core training unit
- [[Iteration]] — optimizer update step
- [[BatchSize]] — samples per iteration
- [[BatchNormalization]] — activation normalization technique
- [[Dropout]] — stochastic regularization
- [[Regularization]] — broader class of overfitting reduction methods
- [[Overfitting]] — problem Dropout addresses
- [[InternalCovariateShift]] — motivation for BatchNorm
- [[LayerNormalization]] — alternative normalization used in Transformers
- [[GradientAccumulation]] — technique to simulate larger batch sizes
- [[CNN]] — architecture where BatchNorm is commonly used
- [[Transformer]] — architecture where LayerNorm is preferred
- [[LLM]] — large language models that use dropout variants
- [[ResNet]] — example architecture using BatchNorm
- [[PyTorch]] — framework with train/eval mode for BatchNorm and Dropout
- [[2026-05-07-day15-ai-ml-learning-review|AI/ML Learning Review Day 15 (2026-05-07)]] — previous day on initialization and gradient flow
- [[2026-05-06-day14-ai-ml-learning-review|AI/ML Learning Review Day 14 (2026-05-06)]] — previous day on forward pass and backpropagation

## Contradictions
- None identified.