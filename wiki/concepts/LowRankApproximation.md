---
title: "LowRankApproximation"
type: concept
tags: [mathematics, linear-algebra, ml-foundations, model-compression]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
[[LowRankApproximation]] is the process of approximating a high-[[Rank]] [[Matrix]] with a lower-[[Rank]] one, typically via truncated SVD. It captures the most important directions while discarding less significant ones.

## Key Properties
- Minimizes Frobenius norm of the reconstruction error among all rank-r approximations (Eckart-Young theorem).
- Trades off information fidelity for computational and storage efficiency.

## Connection to AI/ML
- [[LoRA]] applies [[LowRankApproximation]] to weight updates for parameter-efficient fine-tuning.
- Model compression: prune singular values below a threshold.
- Bottleneck layers in neural networks implicitly perform low-rank projection.
- Understanding [[Rank]] as preserved information dimensionality makes [[LowRankApproximation]] intuitive: keep the dimensions that matter most.

## Sources
- [[2026-04-23-day01-ai-ml-learning-review]]