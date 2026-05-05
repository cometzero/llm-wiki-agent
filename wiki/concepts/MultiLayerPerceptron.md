---
title: "Multi-Layer Perceptron (MLP)"
type: concept
tags: [neural-network, feed-forward, deep-learning]
sources: [2026-05-05-day13-ai-ml-learning-review]
last_updated: 2026-05-05
---

## Summary
An MLP is a feed-forward neural network with one or more hidden layers between input and output. Each layer applies a linear transformation followed by a nonlinear [[ActivationFunction]], enabling the network to learn complex, non-linear patterns.

## Key Ideas
- Structure: input layer → hidden layers → output layer.
- Without activation functions, multiple linear layers collapse to a single linear transformation.
- [[UniversalApproximation]] theorem: with sufficient capacity, MLP can approximate any continuous function.
- Hidden layers learn intermediate representations.

## Connections
- [[Perceptron]] — basic unit of MLP.
- [[ActivationFunction]] — essential for nonlinearity.
- [[Transformer]] — MLP blocks are key components in transformer architectures.
- [[HiddenLayer]] — intermediate representations.
- [[Backpropagation]] — training algorithm.