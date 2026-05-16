---
title: "Memory (Transformer context)"
type: concept
tags: [transformer, encoder-decoder, hidden-state]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
In Transformer context, **memory** refers to the encoder's hidden states that the decoder attends to via [[EncoderDecoderAttention]]. It stores the encoded representation of the input sequence.

## Key Properties
- Shape: [source_sequence_length, d_model]
- Contains contextualized representations of all input tokens
- Reused across all decoder steps during generation
- Unlike RNN hidden state (single vector), memory is a full sequence of vectors

## Role in Generation
1. Encoder processes input → produces memory
2. Decoder queries memory at each step via cross attention
3. Different decoder positions attend to different memory positions (alignment)
4. Memory is static for given input; decoder reads it repeatedly

## Example
For translation "I love cats" → "나는 고양이를 좋아한다":
- Memory contains 3 hidden state vectors for "I", "love", "cats"
- Decoder step "고양이를" attends mostly to memory position for "cats"
- Decoder step "좋아한다" attends mostly to memory position for "love"

## Related Concepts
- [[EncoderDecoderAttention]] — Mechanism accessing memory
- [[HiddenState]] — General concept of stored representations
- Encoder-decoder architecture — Architecture producing memory
