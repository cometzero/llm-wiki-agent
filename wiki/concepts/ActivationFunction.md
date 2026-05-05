---
title: "Activation Function"
type: concept
tags: [neural-network, nonlinearity, activation]
sources: [2026-05-05-day13-ai-ml-learning-review]
last_updated: 2026-05-05
---

## Summary
An activation function introduces nonlinearity into a neural network, applied after each linear transformation. Without it, deep networks would be equivalent to a single linear layer. Common activations include [[ReLU]], [[Sigmoid]], and [[Tanh]].

## Key Ideas
- Enables learning of complex, non-linear decision boundaries.
- ReLU (max(0,x)) is widely used due to efficient gradient flow in positive region.
- Sigmoid squashes output to (0,1) but suffers from saturation (vanishing gradients).
- Tanh squashes to (-1,1), also saturates.
- Modern LLMs use variants like GELU, SwiGLU.

## Connections
- [[Perceptron]] — originally used step function; modern networks use smooth activations.
- [[MultiLayerPerceptron]] — requires activation between layers.
- [[Backpropagation]] — gradient flow depends on activation derivative.
- [[VanishingGradient]] — saturation causes small gradients.
- [[ReLU]] — specific activation.
- [[Sigmoid]] — specific activation.
- [[Tanh]] — specific activation.