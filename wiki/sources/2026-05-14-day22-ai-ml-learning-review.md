---
title: "AI/ML Learning Review — Day 22 (2026-05-14): Transformer Block, Multi-Head Attention, Positional Encoding"
type: source
tags: [ai-ml-learning, transformer, attention, day22]
date: 2026-05-14
source_file: raw/ai_ml_learning/2026-05-14-day22-ai-ml-learning-review.md
source_hash: d03ece7db64b6c34
---

## Summary
Day 22 of a 30-day AI/ML beginner-intermediate course covers the foundational architecture of Transformers. The lesson explains how [[TransformerBlock]] combines attention with feed-forward networks, why [[MultiHeadAttention]] enables diverse relationship capture through parallel heads, and how [[PositionalEncoding]] provides critical order information to models that otherwise process tokens simultaneously.

## Key Claims
- [[TransformerBlock]] consists of attention sublayer, FFN, residual connection, and LayerNorm — not just attention alone
- [[FFN]] processes each token's hidden state independently to transform information brought by attention
- [[MultiHeadAttention]] allows multiple attention patterns to run in parallel, capturing grammar, semantics, location, and reference relationships simultaneously
- [[PositionalEncoding]] is essential because self-attention treats tokens as an unordered set; without it, "개가 사람을 물었다" and "사람이 개를 물었다" would be indistinguishable
- [[ResidualConnection]] and [[LayerNorm]] stabilize training when stacking many transformer blocks

## Key Quotes
> "Transformer block은 단순히 attention 하나가 아니라, '문맥 혼합 + 표현 가공 + 안정적 학습'을 한 묶음으로 만든 구조입니다."

> "Multi-head attention은 한 사람이 한 가지 기준으로만 문장을 보는 대신, 여러 명의 독자가 동시에 다른 관점으로 문장을 읽게 하는 방식입니다."

> "Transformer는 순서를 자동으로 완벽히 알지 못하기 때문에, position information을 따로 넣어야 합니다."

## Connections
- [[TransformerBlock]] — today's primary structural concept
- [[MultiHeadAttention]] — core mechanism within transformer blocks
- [[PositionalEncoding]] — required for order awareness
- [[SelfAttention]] — previous day's concept (Day 21), single-head vs multi-head comparison
- [[FFN]] — token-wise representation refinement after attention
- [[LayerNorm]] — training stability component
- [[ResidualConnection]] — gradient flow and information preservation
- [[QKV]] — related to attention mechanism from Day 21

## Review Questions Covered
1. Attention sublayer mixes context between tokens; FFN refines each token's representation independently
2. Multi-head allows parallel attention patterns for diverse relationships (grammar, semantics, location, reference)
3. Without positional encoding, same words in different orders become indistinguishable to the model

## Contradictions
- None identified; content aligns with standard transformer architecture understanding from Attention Is All You Need principles
