---
title: "Positional Encoding"
type: concept
tags: [transformer, sequence, architecture]
sources: [2026-05-13-day21-ai-ml-learning-review, 2026-05-14-day22-ai-ml-learning-review]
last_updated: 2026-05-14
---

## Definition

**Positional Encoding** (or Position Embedding) is the mechanism that provides sequential order information to Transformers, which otherwise process all tokens simultaneously without inherent order awareness.

## The Problem

Self-attention treats input as an unordered set of tokens:

```
[나는, 밥을, 먹었다]  vs  [밥을, 나는, 먹었다]
```

Without positional information, these would have identical representations.

## Core Solution

```
input_i = token_embedding_i + positional_encoding_i
```

The position vector is combined with the token embedding before entering transformer blocks.

## Common Methods

### 1. Sinusoidal Encoding (Original Transformer)
- Uses sine/cosine functions with different frequencies per dimension
- Allows generalization to longer sequences than trained

### 2. Learned Position Embedding
- Trainable parameters for each position
- Used by GPT and many modern LLMs

### 3. Relative Position (RoPE, ALiBi)
- Encodes distance between tokens rather than absolute positions
- RoPE (Rotary Positional Embedding) widely used in modern LLMs (LLaMA, etc.)

## Key Properties

1. **Same dimension as token embedding** — enables element-wise addition
2. **Unique per position** — model can distinguish "1st token" from "100th token"
3. **Captures both absolute and relative positions** — depending on method

## Why Essential for Transformers

- RNNs inherently process sequentially → built-in order
- Transformers parallelize → order must be explicitly provided
- Critical for: language, code, time series, image patches

## Connections

- [[TransformerBlock]] — receives position-encoded input
- [[SelfAttention]] — cannot distinguish order without positional encoding
- RoPE — modern relative position encoding method
- Attention Is All You Need — original paper introducing sinusoidal encoding

## Long Context Considerations

When extending context beyond training length:
- Absolute position embeddings may fail (new positions unseen)
- RoPE scaling allows smoother generalization
- Context extension is not just increasing max length — position handling matters

## Common Misconceptions

1. ❌ "Self-attention automatically knows token order"
   ✓ It computes relationships without positional awareness

2. ❌ "Position 1, 2, 3 can be used directly as numbers"
   ✓ Positions must be vectors of d_model dimension to combine with embeddings

3. ❌ "Sinusoidal is the only/best method"
   ✓ Learned embeddings, RoPE, and relative position methods have different trade-offs
