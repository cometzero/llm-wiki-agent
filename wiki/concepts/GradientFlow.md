---
title: "Gradient Flow"
type: concept
tags: [deep-learning, optimization, training]
sources: [2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

Gradient flow is the movement of gradient signals backward through a model during [[Backpropagation]]. Healthy gradient flow lets early and late layers receive useful learning signals. If gradients become too small, training can suffer from vanishing gradients; if they become too large, training can become unstable. Architectures such as [[Transformer]]s use mechanisms like residual connections and normalization to help keep gradient flow stable.
