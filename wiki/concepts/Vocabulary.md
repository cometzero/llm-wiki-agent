---
title: "Vocabulary"
type: concept
tags: [tokenization, llm]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
A [[Vocabulary]] is the finite set of tokens a tokenizer and model know how to represent. Each entry maps to a [[TokenId]], which is used for embedding lookup and output logits.

## Trade-off
A larger vocabulary can represent common words as fewer tokens, but increases embedding and output-layer size. A smaller vocabulary can improve coverage through [[Subword]] pieces, but may increase [[SequenceLength]].
