---
title: "Principal Component Analysis (PCA)"
type: concept
tags: [dimensionality-reduction, unsupervised, eigenvector]
sources: [2026-05-04-day12-ai-ml-learning-review]
last_updated: 2026-05-04
---

**Principal Component Analysis (PCA)** is an unsupervised [[DimensionalityReduction]] technique that finds the directions (principal components) of maximum variance in the data. It projects the data onto these components, reducing dimensionality while preserving as much variance as possible.

## Key Points
- Does not use labels; finds directions of maximum spread, not necessarily optimal for classification.
- Components are orthogonal eigenvectors of the [[Covariance]] matrix.
- ExplainedVariance ratio indicates how much total variance each component captures.
- Requires feature scaling (e.g., standardization) before application.
- Useful for visualization of high-dimensional data (e.g., embeddings) and noise reduction.

## Connections
- [[DimensionalityReduction]] — broader category.
- Eigenvector / Eigenvalue — mathematical foundation.
- [[Covariance]] — measures feature co-variation.
- [[Embedding]] — PCA often used to visualize embeddings.
- FeatureScaling — necessary preprocessing step.