---
title: "Value"
type: concept
tags: [transformer, attention, qkv]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
In attention mechanisms, the **Value** represents the actual content that is retrieved and mixed when a token is selected by the attention mechanism. Unlike keys (which determine selection), values are the information actually added to the output representation.

## Key Concepts
- Value is the "actual content" that gets mixed into output representations
- Generated via: `v = xW_V` where `W_V` is a learned weight matrix
- Final attention output is a weighted sum of values: `weights × V`
- Keys determine what to look for; values determine what to learn

## Examples
- In a library search analogy: values are the actual book contents you read
- In a photo search app: values are the actual photo data you view, not just the tags
- For the word "은행" (bank): key might say "I could be financial or river-related" while value carries the actual semantic information

## Connections
- [[Query]] — queries determine which values to retrieve
- [[Key]] — keys determine selection, values carry content
- [[WeightedSum]] — final output is weighted sum of value vectors
- [[SelfAttention]] — self-attention mixes values from same sequence

## Mathematical Form
```
v = xW_V

output = attention_weights × V
```
Where:
- `x` is the input embedding
- `W_V` is a learned weight matrix
- `v` is the resulting value vector
- Final output is a weighted combination of value vectors
