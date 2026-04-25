---
title: "LinearMap"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
A linear map (or linear transformation) is a function between two [[VectorSpace]]s that preserves vector addition and scalar multiplication: f(u+v) = f(u) + f(v) and f(cv) = c·f(v).

## Key Properties
- Every linear map between finite-dimensional vector spaces can be represented as a [[Matrix]] once bases are chosen.
- A matrix is not just a table of numbers — it is the computational representation of a linear map.
- [[Rank]] of a linear map is the dimension of its image (output space), representing how many independent dimensions of information are preserved.
- High rank = more information preserved; low rank = information compression or loss in certain directions.

## Relevance to AI/ML
- Dense layers, projection layers, and [[Attention]]'s Q/K/V projections in [[LLM]] are all linear maps implemented as matrix multiplications.
- [[LoRA]] (Low-Rank Adaptation) exploits low-rank structure to efficiently fine-tune large models.
- Low-rank approximation and bottleneck layers intentionally reduce rank for compression or regularization.
- Understanding matrices as linear maps (not just number grids) is essential for grasping why certain architectures work.

## Related Concepts
- [[Matrix]] — the numerical representation of a linear map
- [[Rank]] — the dimension of independent information preserved
- [[VectorSpace]] — domain and codomain of the map
- [[LoRA]] — practical application of low-rank linear maps
- [[Attention]] — uses linear maps for Q/K/V projections
