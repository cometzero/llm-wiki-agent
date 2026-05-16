---
title: "AI/ML Learning Review — Day 24 (2026-05-16): Causal Mask, Padding Mask, Encoder-Decoder Attention, Transformer Parallelism"
type: source
tags: [ai-ml, transformer, attention, masking, cross-attention]
date: 2026-05-16
source_file: raw/ai_ml_learning/2026-05-16-day24-ai-ml-learning-review.md
source_hash: 9019a16ff6fc06c1
---

## Summary
Day 24 of a 30-day AI/ML beginner-intermediate course covers three core Transformer concepts: [[AttentionMasking]] through causal and padding masks, [[EncoderDecoderAttention]] (cross attention) connecting decoder queries to encoder memory, and the computational trade-offs of [[TransformerParallelism]] with its quadratic attention complexity. The lesson emphasizes how masking defines "what information is accessible" and how cross attention bridges input understanding to output generation.

## Key Claims
- **Causal mask** prevents current tokens from seeing future tokens in autoregressive models, ensuring training matches inference conditions
- **Padding mask** prevents attention to meaningless `<pad>` tokens added for batch processing, maintaining clean token representations
- **Encoder-decoder attention** (cross attention) uses decoder hidden states as queries and encoder hidden states as keys/values, enabling input-output alignment
- **Self-attention has O(n²) complexity** in sequence length n, causing memory bottlenecks for long contexts
- **[[KVCache]]** enables efficient autoregressive inference by reusing past key/value computations

## Key Quotes
> "Causal mask는 현재 token이 미래 token을 보지 못하게 막는다. Padding mask는 의미 없는 padding token을 못 보게 막는다."

> "Encoder-decoder attention은 '입력과 출력 사이의 연결 통로'다. Encoder가 입력을 이해하고, decoder가 출력을 만들며, cross attention이 둘을 연결한다."

> "Transformer는 '병렬화 덕분에 학습이 강력해졌지만, 긴 sequence에서는 제곱 비용이 병목이 된다'는 trade-off를 가진다."

## Connections
- [[SelfAttention]] — Core mechanism extended by masking and cross attention variants
- [[MultiHeadAttention]] — Where masking is applied in practice
- [[Transformer]] — Architecture these concepts belong to
- [[Autoregressive]] — Causal mask enables autoregressive generation
- [[EncoderDecoderAttention]] — Cross attention connects encoder and decoder components
- [[QuadraticComplexity]] — The computational cost of self-attention

## Contradictions
- None identified. This educational content aligns with standard transformer literature.

## Key Technical Details

### Causal Mask Math
```
mask =
[0   -inf -inf
 0    0   -inf
 0    0    0  ]
```
Softmax converts -inf to 0 weight, preventing attention to blocked positions.

### Cross Attention Shapes
- Encoder hidden states: [source_length, d_model]
- Decoder hidden states: [target_length, d_model]
- Attention matrix: [target_length, source_length]

### Quadratic Complexity Example
| Sequence length n | Attention scores n² |
|---:|---:|
| 4 | 16 |
| 8 | 64 |
| 16 | 256 |
| 32 | 1,024 |
