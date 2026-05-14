---
title: "Feed-Forward Network (FFN)"
type: concept
tags: [transformer, neural-network, architecture]
sources: [2026-05-14-day22-ai-ml-learning-review]
last_updated: 2026-05-14
---

## Definition

The **Feed-Forward Network** (FFN) within a [[TransformerBlock]] is a two-layer fully-connected network applied independently to each token's hidden state. It transforms each token's representation after attention has mixed contextual information.

## Architecture

```
FFN(x) = Linear → Activation → Linear
      = max(0, xW_1 + b_1)W_2 + b_2  (with ReLU)
```

Typical shape: `d_model → 4×d_model → d_model`

## Role in Transformer

- **Attention** handles: "What information to gather from other tokens?"
- **FFN** handles: "How to transform and refine within my own representation?"

```
Token gets information from attention → FFN processes → refined representation
```

## Key Properties

1. **Applied per-token** — no mixing between different tokens
2. **Independent across tokens** — can be parallelized efficiently
3. **Contains majority of parameters** — ~2/3 of transformer parameters
4. **Expansion ratio** — typically 4× creates a "bottleneck and expand" pattern

## Connections

- [[TransformerBlock]] — sublayer within each block
- [[MultiHeadAttention]] — attention provides input to FFN
- [[ResidualConnection]] — FFN output added to input
- [[LayerNorm]] — often applied before FFN in pre-norm architecture

## Common Misconceptions

1. ❌ "FFN mixes information between tokens"
   ✓ Each token gets its own independent FFN transformation

2. ❌ "FFN and attention are alternatives"
   ✓ They are complementary — both required in a transformer block

3. ❌ "Only needed for large models"
   ✓ FFN provides non-linear transformation capacity regardless of model size
