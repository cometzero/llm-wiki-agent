---
title: "Layer Normalization (LayerNorm)"
type: concept
tags: [deep-learning, normalization, training]
sources: [2026-05-07-day15-ai-ml-learning-review, 2026-05-14-day22-ai-ml-learning-review]
last_updated: 2026-05-14
---

## Definition

**Layer Normalization** (LayerNorm) normalizes the activations of a layer by computing mean and variance across the feature dimension for each individual sample, stabilizing training by keeping numerical values in consistent ranges.

## In Transformers

LayerNorm is applied before attention and FFN (pre-norm) or after (post-norm):

```
Pre-norm: LayerNorm(X) → Attention → Add → LayerNorm → FFN → Add
Post-norm: LayerNorm(X + Attention(...)) → ...
```

## Key Properties

1. **Per-sample normalization** — statistics computed within each sample
2. **No batch dependency** — unlike BatchNorm, doesn't require batch dimension
3. **Stable gradients** — prevents vanishing/exploding activations
4. **Enables deeper stacking** — critical for training 100+ layer transformers

## Connections

- [[TransformerBlock]] — essential stability component
- [[ResidualConnection]] — often used with residual connections
- [[Attention]] — LayerNorm often applied before attention computation
- [[FFN]] — LayerNorm often applied before FFN
