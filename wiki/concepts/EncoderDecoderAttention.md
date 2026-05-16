---
title: "Encoder-Decoder Attention"
type: concept
tags: [transformer, attention, encoder-decoder, cross-attention]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
**Encoder-decoder attention** (also called **cross attention**) is a mechanism where decoder queries attend to encoder key-values, enabling the decoder to access encoded input information during generation.

## Key Properties
- **Query**: comes from decoder hidden states
- **Key/Value**: comes from encoder hidden states (called "memory")
- Enables input-output alignment in seq2seq tasks
- Present in T5, original [[Transformer]], BART
- Absent in decoder-only models like [[GPT]]

## Mathematical Formulation
```
Q = H_decoder W_Q     # From decoder
K = H_encoder W_K     # From encoder (memory)
V = H_encoder W_V     # From encoder (memory)

CrossAttention(Q,K,V) = softmax(QK^T / √d_k) V
```

## Applications
- Machine translation — Align source/target words
- Summarization — Access source document while generating summary
- Question answering — Attend to passage when generating answer
- Speech recognition — Attend to audio features
- Image captioning — Attend to image features

## Related Concepts
- [[SelfAttention]] — Same formula, different Q/K/V sources
- [[Memory]] — Encoder output as decoder's reference
- Alignment — What cross attention reveals
- Encoder-decoder architecture — Architecture containing this mechanism
