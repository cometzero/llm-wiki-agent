---
title: "Pre-LN (Pre-LayerNorm)"
type: concept
tags: [transformer, normalization]
sources: [2026-05-15-day23-ai-ml-learning-review.md]
last_updated: 2026-05-15
---

## Definition

Transformer architecture variant where [[LayerNorm]] is applied **before** the [[Attention]] and [[PositionWiseFFN]] sublayers:

```
x = x + Attention(LayerNorm(x))
x = x + FFN(LayerNorm(x))
```

## Comparison: Pre-LN vs Post-LN

| Aspect | Pre-LN | Post-LN |
|--------|--------|---------|
| LayerNorm position | Before sublayers | After sublayers |
| Training stability | More stable | Less stable |
| Use in modern LLMs | Dominant | Rare |
| Original "Attention is All You Need" | No | Yes |

## Advantages of Pre-LN

- Better gradient flow through deeper networks
- More stable training with larger learning rates
- Reduced sensitivity to initialization

Modern large models (GPT-4, LLaMA, Claude) use Pre-LN almost exclusively.

## Related Concepts

- [[LayerNorm]] — the normalization technique
- [[PostLN]] — alternative positioning
- [[ResidualConnection]] — works synergistically with Pre-LN
