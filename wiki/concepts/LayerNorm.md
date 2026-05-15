---
title: "Layer Normalization"
type: concept
tags: [deep-learning, transformer, normalization]
sources: [2026-05-15-day23-ai-ml-learning-review.md]
last_updated: 2026-05-15
---

## Definition

Normalization applied along the feature dimension of each token's hidden state independently:

```
ŷ = γ * ((x - mean(x)) / sqrt(variance(x) + ε)) + β
```

Where `γ` (scale) and `β` (shift) are learnable parameters.

## Key Properties

1. **Per-token normalization** — Computes statistics within a single token's feature vector
2. **Feature-dimension based** — Normalizes across hidden dimension (e.g., 768 values), not across batch
3. **Batch-independent** — Works with variable batch sizes and sequence lengths

## Comparison with BatchNorm

| Aspect | LayerNorm | BatchNorm |
|--------|-----------|-----------|
| Normalization axis | Feature dimension | Batch dimension |
| Batch size sensitivity | Low | High |
| NLP suitability | Excellent | Poor |
| Inference/training consistency | Consistent | Can differ |

## In Transformers

Two main variants:
- **Pre-LN**: LayerNorm before Attention/FFN (modern, more stable)
- **Post-LN**: LayerNorm after Attention/FFN (original "Attention is All You Need")

Modern LLMs predominantly use Pre-LN for training stability.

## Role in Stability

Prevents hidden state scale from exploding or vanishing through deep layers:
- Layer 1: `[1, 2, 1]`
- Layer 2: `[100, -80, 120]` (without LayerNorm)

LayerNorm ensures consistent statistical properties across all layers.

## Related Concepts

- [[ResidualConnection]] — LayerNorm often precedes or follows residual additions
- [[PreLN]] / [[PostLN]] — Transformer block architectural variants
- [[BatchNormalization|BatchNorm]] — contrasted normalization approach
- [[HiddenState]] — the vector being normalized
