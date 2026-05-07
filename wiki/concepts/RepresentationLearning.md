---
title: "RepresentationLearning"
type: concept
tags: [deep-learning, feature-extraction, hidden-representation]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
[[RepresentationLearning]] is a machine learning approach where the model learns internal numeric features from data, rather than relying on manually specified human features.

In deep networks, layers transform input into progressively more abstract [[HiddenLayer]] outputs, often yielding structures in [[LatentSpace]] that are more useful for prediction, retrieval, generation, or translation tasks.

## Key Claims
- In [[Image]]- and [[NaturalLanguage]]-like domains, manual feature design is often incomplete, while learned representations capture subtle, task-relevant patterns.
- Good representation quality improves downstream performance even when later layers are simple.
- In practical systems, representation learning appears as learned [[Embedding]]s, [[HiddenState]]s, and intermediate activations.

## Core Mechanics
- Input `x` is transformed through functions `h = f(x)` where `f` is a stack of layer operations.
- Different network layers often increase semantic abstraction: edge/texture/part/object for [[CNN]], local context→global context for [[LLM]] token streams.
- Similar semantic items become close in representation space (often by learned similarity metrics).

## Usage in AI systems
- [[CNN]] / [[ImageNet]] style vision models
- [[LLM]]s and [[Transformer]]s through token/context embeddings
- Search/recommendation systems via vector spaces
- [[Autoencoder]]/generative pipelines with compressed latent representations

## Key Terms
- [[Embedding]]: raw symbol/feature to vector map
- [[LatentRepresentation]]: latent/internal representation in hidden layers
- [[LatentSpace]]: learned feature manifold over which representations are compared
- [[TransferLearning]]: reusing learned representations for related tasks

## Conflicts
- None identified.
