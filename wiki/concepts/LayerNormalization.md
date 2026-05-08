---
title: "LayerNormalization"
type: concept
tags: [normalization, training, deep-learning]
sources: [2026-05-08-day16-ai-ml-learning-review]
last_updated: 2026-05-08
---

**Layer Normalization (LayerNorm)** normalizes activations across the feature dimension for each individual sample, rather than across the batch dimension like [[BatchNormalization]]. This makes it independent of batch size and more suitable for sequence models like [[Transformer]] and [[LLM]]s, where batch statistics can be unstable due to varying sequence lengths. LayerNorm is the standard normalization in Transformer architectures. Related: [[BatchNormalization]], [[InternalCovariateShift]], [[Transformer]].