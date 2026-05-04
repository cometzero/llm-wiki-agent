---
title: "Dimensionality Reduction"
type: concept
tags: [feature-engineering, unsupervised, pca]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Dimensionality Reduction** is the process of reducing the number of features (dimensions) in a dataset while preserving as much relevant information as possible. It helps with visualization, noise reduction, and computational efficiency.

## Methods
- **Linear**: [[PCA]] (Principal Component Analysis), LDA (Linear Discriminant Analysis).
- **Non-linear**: t-SNE, UMAP, autoencoders.

## Key Points
- [[PCA]] is unsupervised; finds directions of maximum variance.
- Dimensionality reduction is not always beneficial for prediction; it may discard discriminative information.
- Commonly used to visualize high-dimensional embeddings (e.g., from LLMs).

## Connections
- [[PCA]] — most common linear method.
- [[Embedding]] — often reduced for visualization.
- FeatureScaling — important preprocessing.
- Noise — reduction can help remove noise.