---
title: "Key"
type: concept
tags: [transformer, attention, qkv]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
In attention mechanisms, the **Key** represents the "searchable tags" or features of each candidate token. Keys are compared against queries to determine relevance scores, which determine how much each value contributes to the output.

## Key Concepts
- Key is the "searchable identifier" that allows tokens to be found
- Generated via: `k = xW_K` where `W_K` is a learned weight matrix
- Key represents "under what context should I be found"
- Value represents "what information to deliver when selected"
- Keys and values come from the same token but serve different roles

## Examples
- In a library search analogy: keys are book titles, tags, classification numbers, and subject keywords
- "사과" (apple) might have a key representing "I am an edible object" to match queries asking about eating

## Connections
- [[Query]] — query-key compatibility determines attention weights
- [[Value]] — keys determine selection, values are the actual content mixed
- [[ScaledDotProductAttention]] — dot product of Q and K yields compatibility scores
- [[DotProduct]] — method for computing query-key relevance

## Mathematical Form
```
k = xW_K
```
Where:
- `x` is the input embedding
- `W_K` is a learned weight matrix
- `k` is the resulting key vector
