---
title: "Residual Connection"
type: concept
tags: [deep-learning, transformer, optimization]
sources: [2026-05-15-day23-ai-ml-learning-review.md]
last_updated: 2026-05-15
---

## Definition

A neural network architectural pattern where the input `x` is added to the output of a transformation `F(x)`:

```
y = x + F(x)
```

The direct path from input to output is called the **skip path** or **shortcut connection**.

## Key Properties

1. **Information Preservation** — Original hidden state passes unchanged through the block
2. **Incremental Learning** — Each block learns a "delta" or correction rather than full representation
3. **Gradient Path** — Creates direct gradient route to early layers without passing through complex transformations

## Mathematical Significance

Gradient can flow through two paths:
1. Direct path: gradient reaches `x` without passing through `F(x)` weights
2. Through-path: gradient passes through `F(x)` computations

This multi-path structure prevents gradient vanishing in deep networks.

## In Transformers

Applied after [[Attention]] and [[PositionWiseFFN]]:

```
x₁ = x + Attention(x)
x₂ = x₁ + FFN(x₁)
```

Enables stacking 12–100+ transformer layers in models like [[GPT]], [[BERT]], and LLaMA.

## Related Concepts

- [[SkipPath]] — alternative term for the direct x→y path
- [[Gradient]] — benefits from shortened propagation path
- [[HiddenState]] — preserved and incrementally modified
- [[PreLN]] — LayerNorm variant that works synergistically with residual connections
