---
title: "Vector Space"
type: concept
tags: [mathematics, linear-algebra, machine-learning]
last_updated: 2026-04-25
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## Definition
[[VectorSpace]] is a mathematical setting where [[Vector]] addition and scalar multiplication are defined and closed.

## Why it matters in AI
Vector representations underpin [[Embedding]], [[LLM]], and optimization states such as [[Gradient]]. When data is embedded into a [[VectorSpace]], model computations become geometric: similarity, projection, and transformation can be reasoned as operations on vectors.

## Key points
- [[Coordinate]] values are descriptions of a fixed [[Vector]] within a chosen [[Basis]].
- Different [[Basis]] choices change numeric representation without changing the underlying vector.
- Many [[LLM]] operations (token embedding, attention weights, hidden states) are vector-space computations.

## Connections
- [[LinearMap]], [[Basis]], [[Coordinate]], [[Matrix]], [[Embedding]], [[Attention]]
- [[RepresentationLearning]]
