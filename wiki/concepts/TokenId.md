---
title: "Token ID"
type: concept
tags: [tokenization, representation]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
A token ID is the integer identifier assigned to a token in a tokenizer [[Vocabulary]]. Models operate on token IDs by looking up their vectors in an [[EmbeddingLookup]] table.

## Example
If `밥을` maps to 42, the model receives the integer `42`, not the raw text, and retrieves the corresponding embedding vector.
