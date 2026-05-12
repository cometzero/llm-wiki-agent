---
title: "AI/ML Learning Review — Day 20 (2026-05-12): LSTM/GRU, Embedding, Attention"
type: source
tags: [ai-ml, learning-review, sequence-models, lstm, gru, embedding, attention]
date: 2026-05-12
source_file: raw/ai_ml_learning/2026-05-12-day20-ai-ml-learning-review.md
source_hash: 49fa50ea933ea37e
---

## Summary
Day 20 of the AI/ML learning series covers three foundational concepts in sequence modeling: LSTM/GRU gating mechanisms for selective memory, word embedding for semantic representation compression, and attention for information selection in long sequences.

## Key Claims
- [[LSTM]] and [[GRU]] use learnable gate values (0-1 range via sigmoid) to control what information to remember, forget, and output
- Embedding compresses discrete tokens into dense vectors where semantically similar words cluster together in vector space
- [[AttentionMechanism]] solves the compression bottleneck by allowing models to selectively attend to relevant input positions via weighted context vectors
- These three concepts form the evolutionary path from RNNs to modern [[Transformer]] architectures

## Key Concepts
1. **LSTM/GRU Gating**: Gate values (0-1 via sigmoid) regulate information flow; forget gate decides what to discard, input gate decides what to add, output gate decides what to expose
2. **Word Embedding**: Dense vector representation where semantic similarity correlates with vector proximity; learned from context patterns
3. **Attention**: Query-Key-Value mechanism computing relevance scores, converting to weights via softmax, producing context vectors as weighted sums

## Connections
- [[LSTM]] — the gated RNN variant with cell state architecture
- [[GRU]] — simplified LSTM with update and reset gates
- [[Embedding]] — foundational text representation for [[LLM]] and [[RAG]] systems
- [[AttentionMechanism]] — core of [[Transformer]] architecture
- [[VanishingGradient]] — the problem LSTM/GRU addresses

## Review Questions Covered
1. Why LSTM gates use 0-1 values and how they regulate information flow
2. Difference between one-hot vector and embedding for semantic similarity
3. Role of attention weights and context vectors in handling long sequences
