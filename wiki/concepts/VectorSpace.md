---
title: "VectorSpace"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
A vector space is a mathematical structure where vector addition and scalar multiplication are defined and satisfy specific axioms (closure, associativity, commutativity, identity, inverse, distributivity).

## Key Properties
- Vectors in a vector space are abstract objects, not tied to any specific coordinate representation.
- Coordinates are basis-dependent numerical representations of vectors.
- The same vector can have different coordinates under different [[Basis]] choices.
- This distinction (vector = invariant, coordinate = basis-dependent) is foundational for understanding [[PCA]], basis change, and representation learning.

## Relevance to AI/ML
- [[LLM]] token embeddings, hidden states, and gradients are all vectors in high-dimensional vector spaces.
- [[Embedding]] spaces are vector spaces where semantic relationships are encoded geometrically.
- Understanding vector spaces is prerequisite for grasping [[LinearMap]], [[DotProduct]], [[Norm]], and [[CosineSimilarity]].

## Related Concepts
- [[Basis]] — the reference frame for coordinate representation
- [[LinearMap]] — transformations between vector spaces
- [[Embedding]] — learned vector representations in NLP/ML
- [[Norm]] — measuring vector magnitude in a vector space
