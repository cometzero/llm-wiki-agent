---
title: "Post-LN (Post-LayerNorm)"
type: concept
tags: [transformer, normalization]
sources: [2026-05-15-day23-ai-ml-learning-review.md]
last_updated: 2026-05-15
---

## Definition

Original Transformer architecture variant where [[LayerNorm]] is applied **after** the [[Attention]] and [[PositionWiseFFN]] sublayers:

```
x = LayerNorm(x + Attention(x))
x = LayerNorm(x + FFN(x))
```

## Comparison: Post-LN vs Pre-LN

| Aspect | Post-LN | Pre-LN |
|--------|---------|--------|
| LayerNorm position | After sublayers | Before sublayers |
| Training stability | Less stable | More stable |
| Use in modern LLMs | Rare | Dominant |
| Original paper | "Attention is All You Need" | Later improvement |

## Challenges with Post-LN

- More sensitive to learning rate and initialization
- Requires warmup schedules for stable training
- Gradient clipping often necessary

Modern large models predominantly use [[PreLN]] instead.

## Related Concepts

- [[LayerNorm]] — the normalization technique
- [[PreLN]] — the dominant modern alternative
- [[ResidualConnection]] — interacts with LayerNorm placement
