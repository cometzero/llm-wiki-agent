---
title: "Weights"
type: concept
tags: [neural-network, deep-learning, training]
sources: [2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

Weights are trainable [[Parameters]] that determine how strongly each input feature contributes to a layer's output. In a simple model such as `y = wx + b`, increasing `w` makes the same input have a larger effect on the output. In neural networks and LLMs, weights are usually matrices in linear layers, embeddings, attention projections, and feed-forward blocks. [[Backpropagation]] computes gradients for weights, and an [[Optimizer]] updates them to reduce the loss.
