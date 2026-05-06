---
title: "Credit Assignment"
type: concept
tags: [deep-learning, optimization, training]
sources: [2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

Credit assignment is the problem of deciding which internal [[Parameters]], layers, or intermediate computations are responsible for a model's final error or success. In deep learning, [[Backpropagation]] addresses credit assignment by using the [[ChainRule]] to propagate gradients backward from the loss to earlier layers. This tells the [[Optimizer]] which weights and biases should be adjusted and in what direction.
