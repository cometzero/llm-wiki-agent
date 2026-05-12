---
title: "Attention Mechanism"
type: concept
tags: [neural-networks, sequence-models, transformer]
sources: [2026-05-12-day20-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
Attention allows models to selectively focus on relevant parts of the input when producing each output, computed as a weighted combination of values based on query-key compatibility.

## The Query-Key-Value Trilogy

| Component | Role | Intuition |
|-----------|------|----------|
| **Query** | What information am I looking for? | Current token's question |
| **Key** | What information do I contain? | Each token's advertisement |
| **Value** | What information to extract? | Actual content to retrieve |

## Computation Flow
1. Compute relevance scores between query and all keys
2. Apply softmax to convert scores to attention weights (sum = 1)
3. Compute weighted sum of values using attention weights

```
scores = Q · K^T
weights = softmax(scores)
context = weights · V
```

## Example: Translation
Input: `I / love / cats` → Output: `고양이`

Attention weights might be:
- `I` → 0.05
- `love` → 0.10
- `cats` → 0.85

Result: Context vector strongly reflects "cats" information.

## Types of Attention

| Type | Description | Use Case |
|------|-------------|----------|
| Encoder-Decoder | Decoder attends to encoder states | Translation |
| **Self-Attention** | Tokens attend to other tokens in same sequence | [[LLM]], [[Transformer]] |
| Cross-Attention | Different sequences attend to each other | Multimodal |

## Why It Matters

### Solves Compression Bottleneck
Instead of compressing entire sequence into one vector (RNN last hidden state), attention:
- Preserves all position representations
- Selects relevant information per output
- Enables handling of long dependencies

### Enables Parallelization
Unlike sequential RNN, attention computations across positions are independent (can parallelize in [[Transformer]]).

## Connection to [[Transformer]]
Self-attention is the core operation in [[Transformer]] architecture:
- Multi-head attention = multiple attention mechanisms in parallel
- Each head can focus on different relationship types

## Computational Consideration
Self-attention is O(n²) in sequence length—challenging for very long contexts. Solutions:
- [[RAG]] for external knowledge
- Sliding window attention
- Efficient attention variants (FlashAttention, etc.)

## Connections
- [[LSTM]]/[[GRU]] — evolutionary predecessors addressing same problem
- [[Transformer]] — built on self-attention
- [[Embedding]] — attention operates over embedded tokens
- [[VanishingGradient]] — attention sidesteps this via direct connections
