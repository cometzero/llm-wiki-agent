---
title: "Biases"
type: concept
tags: [neural-network, deep-learning, training]
sources: [2026-05-06-day14-ai-ml-learning-review]
last_updated: 2026-05-06
---

Biases are trainable [[Parameters]] added after a weighted sum to shift a layer's baseline output. In `y = wx + b`, changing `b` moves the output up or down even when the input stays the same. Bias terms let neural-network layers represent offsets instead of being forced through the origin, and they are updated during training using gradients computed by [[Backpropagation]].
