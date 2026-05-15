---
title: "Position-wise Feed-Forward Network"
type: concept
tags: [deep-learning, transformer, mlp]
sources: [2026-05-15-day23-ai-ml-learning-review.md]
last_updated: 2026-05-15
---

## Definition

An MLP (multi-layer perceptron) applied independently to each token position in a Transformer:

```
FFN(x) = W₂ · σ(W₁ · x + b₁) + b₂
```

Where:
- `x`: token's hidden state vector
- `W₁`: expands hidden dimension to intermediate dimension
- `σ`: non-linear activation (ReLU, GELU, SwiGLU)
- `W₂`: contracts back to hidden dimension

## Key Properties

1. **Position-independent** — Same FFN applied to every token; no cross-token mixing
2. **Expansion-Contraction** — Typically 4x expansion (e.g., 768 → 3072 → 768)
3. **Feature Transformation** — Complements [[Attention]]'s cross-token mixing with per-token non-linear transformation

## Architecture

```
Input [d_model] → Linear(W₁) → [d_intermediate] → Activation → Linear(W₂) → [d_model]
```

## Role in Transformers

| Component | Function |
|-----------|----------|
| [[Attention]] | Token-to-token information mixing |
| Position-wise FFN | Per-token feature transformation |

FFN processes the context gathered by attention, transforming it into richer token representations.

## Parameter Distribution

FFN typically contains 2/3 of Transformer parameters:
- 768 × 3072 + 3072 × 768 = ~7M params (per layer)
- vs Attention: ~4M params (per layer)

## Related Concepts

- [[Attention]] — complementary; mixes between tokens
- [[MultiLayerPerceptron|MLP]] — FFN is an MLP per position
- [[FeedForwardNetwork]] — broader term
- [[ResidualConnection]] — FFN output added via residual connection
- [[LayerNorm]] — often applied before/after FFN
