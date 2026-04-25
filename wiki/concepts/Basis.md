---
title: "Basis"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
A basis is a set of linearly independent vectors that span a [[VectorSpace]]. Every vector in the space can be uniquely expressed as a linear combination of basis vectors.

## Key Properties
- Coordinates are not properties of the vector itself but of the vector relative to a chosen basis.
- Changing the basis changes the coordinates, even though the underlying vector remains invariant.
- The number of basis vectors equals the dimension of the vector space.

## Relevance to AI/ML
- Basis change is central to [[PCA]] (Principal Component Analysis), where data is re-expressed in a new basis that maximizes variance.
- Representation learning can be viewed as learning a useful basis for representing data.
- Token [[Embedding]] in [[LLM]] can be understood as mapping discrete tokens to coordinates in a learned vector space with a specific basis.

## Related Concepts
- [[VectorSpace]] — the space spanned by the basis
- [[LinearMap]] — can be represented as a matrix once bases are chosen for domain and codomain
- [[Rank]] — the dimension of the image space, i.e., the number of basis vectors in the output
- [[PCA]] — a specific basis change technique
