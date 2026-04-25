---
title: "LoRA"
type: concept
tags: [ml, parameter-efficient-fine-tuning]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that decomposes weight updates into low-[[Rank]] matrices, drastically reducing trainable parameters while maintaining performance.

## Mathematical Basis
- A full weight update ΔW is approximated as the product of two low-[[Rank]] matrices: ΔW ≈ BA, where B ∈ ℝ^(d×r) and A ∈ ℝ^(r×k) with r ≪ min(d,k).
- This exploits [[LowRankApproximation]]: the effective information change often lives in a low-dimensional subspace.
- Directly connected to the concept of [[Rank]] as a measure of preserved information dimensionality in a [[LinearMap]].

## Connection to AI/ML
- Enables fine-tuning of large [[LLM]]s on consumer hardware.
- The [[Rank]] hyperparameter r controls the trade-off between expressiveness and efficiency.

## Sources
- [[2026-04-23-day01-ai-ml-learning-review]]