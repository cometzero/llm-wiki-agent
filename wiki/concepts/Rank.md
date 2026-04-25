---
title: "Rank"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
Rank is the dimension of the image (column space) of a [[Matrix]] or [[LinearMap]] — the number of linearly independent directions in the output space that the transformation can produce.

## Key Properties
- Rank measures how much independent information a linear transformation preserves.
- Full rank: all input dimensions are preserved in the output.
- Low rank: some directions of information are collapsed or lost.
- Rank cannot exceed the smaller of the input dimension or output dimension.

## Relevance to AI/ML
- [[LoRA]] (Low-Rank Adaptation) fine-tunes large models by learning low-rank weight updates, dramatically reducing parameter count.
- Low-rank approximation is used for model compression and efficient inference.
- Bottleneck architectures intentionally use low-rank layers to force information compression.
- Understanding rank helps interpret model capacity and expressiveness.

## Related Concepts
- [[LinearMap]] — the transformation whose rank is measured
- [[Matrix]] — the numerical representation
- [[LoRA]] — practical low-rank fine-tuning technique
- [[VectorSpace]] — the spaces between which rank is measured
