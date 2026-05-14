---
title: "Transformer Block"
type: concept
tags: [transformer, neural-network, architecture]
sources: [2026-05-14-day22-ai-ml-learning-review]
last_updated: 2026-05-14
---

## Definition

A **Transformer Block** (also called Transformer layer) is the fundamental repeating unit in Transformer models. It combines an attention sublayer, a feed-forward network (FFN), residual connections, and LayerNorm to enable stable stacking of multiple layers.

## Core Components

1. **Attention Sublayer** — tokens see each other to gather contextual information
2. **FFN (Feed-Forward Network)** — independent per-token representation transformation
3. **Residual Connection** — preserves original input information and aids gradient flow
4. **LayerNorm** — stabilizes numerical scales for consistent training

## Key Insight

```
Input token representation
→ Attention: mix context between tokens
→ FFN: refine each token representation independently
→ Next block
```

The attention sublayer handles "what information to gather from other tokens," while FFN handles "how to interpret and organize the gathered information within each token's representation."

## Mathematical Form

```
H1 = X + Attention(LayerNorm(X))        # pre-norm style
H2 = H1 + FFN(LayerNorm(H1))
```

Key properties:
- Input/output shape preserved: `n × d_model` → `n × d_model`
- FFN expands and contracts: typically `d_model → 4×d_model → d_model`

## Why Multiple Blocks?

- Early blocks: local word relationships, simple grammar
- Middle blocks: sentence structure, semantic relations
- Deep blocks: high-level clues for prediction/classification

## Connections
- [[MultiHeadAttention]] — the attention mechanism within each block
- [[PositionalEncoding]] — provides order information to the block's input
- [[FFN]] — per-token refinement component
- [[ResidualConnection]] — information preservation
- [[LayerNorm]] — training stability
- Attention Is All You Need — original paper describing transformer architecture

## Common Misconceptions

1. ❌ "Transformer block = attention only"
   ✓ It includes FFN, residual connection, and LayerNorm

2. ❌ "FFN mixes information between tokens"
   ✓ FFN operates independently on each token; attention does token mixing

3. ❌ "More blocks always means better"
   ✓ Requires balanced data, model size, optimizer, and training stability
