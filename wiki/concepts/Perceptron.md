---
title: "Perceptron"
type: concept
tags: [neural-network, linear-classifier, fundamental]
sources: [2026-05-05-day13-ai-ml-learning-review]
last_updated: 2026-05-05
---

## Summary
The perceptron is the simplest artificial neuron, performing a weighted sum of inputs plus bias and applying a threshold to produce a binary output. It is the building block of modern neural networks.

## Key Ideas
- Computes [[LinearCombination]]: z = w·x + b
- Applies a step function (or modern activation) to z to produce output.
- Can only learn linearly separable patterns.
- Weight and bias are learned via training.

## Connections
- [[MultiLayerPerceptron]] — stacks perceptrons with nonlinearities.
- [[ActivationFunction]] — modern networks use smooth activations instead of step function.
- [[LinearLayer]] — core computation in deep learning is Wx + b.
- [[Backpropagation]] — used to update weights.