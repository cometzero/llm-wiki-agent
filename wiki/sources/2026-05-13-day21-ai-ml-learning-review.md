---
title: "AI/ML Learning Review — Day 21 (2026-05-13): QKV, Scaled Attention, Self-Attention"
type: source
tags: [ai-ml-learning, transformer, attention, beginner-intermediate]
date: 2026-05-13
source_file: raw/ai_ml_learning/2026-05-13-day21-ai-ml-learning-review.md
source_hash: 3e5d7bf4cbc0c09e
---

## Summary
Day 21 of an AI/ML learning journey covers Transformer attention fundamentals: Query/Key/Value role separation, Scaled Dot-Product Attention with `sqrt(d_k)` scaling, and Self-Attention's expressive power for contextual token representation. The lesson builds toward understanding sequence models and attention mechanisms for sequential data.

## Key Claims
- Query, Key, Value separate "what I'm looking for", "search tags", and "actual content" in attention mechanisms
- Scaled Dot-Product Attention uses `sqrt(d_k)` to prevent softmax from becoming too extreme when vector dimensions are large
- Self-Attention allows tokens to reference other tokens within the same sequence to build context-dependent representations
- The attention mechanism is a key building block of Transformer-based LLMs like GPT, BERT, and Vision Transformer

## Key Quotes
> "Attention은 query로 필요한 정보를 찾고, key로 관련성을 계산하고, value를 attention weight만큼 섞어서 각 token의 문맥적 표현을 만드는 메커니즘" — Day summary

> "Self-Attention에서 'self'는 같은 sequence 안에서 attention을 한다는 뜻입니다. 자기 자신만 본다는 뜻이 아닙니다." — Core misunderstanding clarified

## Connections
- [[Transformer]] — built on QKV attention architecture
- [[BERT]], [[GPT]] — LLM architectures using self-attention
- [[Embedding]] — QKV vectors are derived from input embeddings
- [[VisionTransformer]] — applies self-attention to image patches
- [[FlashAttention]] — optimization technique for attention computation
- [[TokenInteraction]] — Self-Attention enables direct token-to-token connections

## Contradictions
- None identified. Day 20 covered "Attention mechanism for sequence modeling" which is a prerequisite; this day provides deeper technical detail on the same topic without conflict.
