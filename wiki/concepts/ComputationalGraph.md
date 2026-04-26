---
title: "ComputationalGraph"
type: concept
tags: [deep-learning, optimization, machine-learning]
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

A computational graph is a directed graph where nodes represent operations (e.g., addition, multiplication, activation functions) and edges represent data flow (tensors). It decomposes a complex function into a sequence of elementary operations.

## Key Points
- Forward pass computes values; backward pass computes gradients via [[Backpropagation]].
- Each node knows its local gradient, enabling modular gradient computation.
- Frameworks like [[Autograd]] (PyTorch, TensorFlow) build computational graphs automatically.

## Connections
- [[Backpropagation]] — the algorithm that traverses the graph backward.
- [[ChainRule]] — the mathematical rule used at each node.
- [[ForwardPass]] — computation of node values.
- [[BackwardPass]] — propagation of gradients.
- [[Autograd]] — automated graph construction and gradient computation.