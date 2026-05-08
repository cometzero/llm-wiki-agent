---
title: "BatchNormalization"
type: concept
tags: [normalization, training, deep-learning]
sources: [2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

**Batch Normalization (BatchNorm)** normalizes the activations of a layer within each mini-batch to have zero mean and unit variance, then applies learnable scale (gamma) and shift (beta) parameters. It stabilizes training by reducing [[InternalCovariateShift]], allows higher learning rates, and can have a slight regularization effect. During training, mini-batch statistics are used; during inference, running mean and variance accumulated during training are used. Commonly used in [[CNN]] architectures like [[ResNet]]. In [[Transformer]] models, [[LayerNormalization]] is more common. Related: [[InternalCovariateShift]], [[LayerNormalization]], [[Dropout]].