---
title: "Special Token"
type: concept
tags: [tokenization, llm]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
A special token is a reserved vocabulary entry used to control model behavior or formatting rather than represent ordinary text. Examples include `<bos>`, `<eos>`, `<pad>`, and `[MASK]`.

## Connections
- [[Tokenization]] — special tokens are inserted by tokenizers or training pipelines.
- [[PaddingMask]] — uses padding special tokens to hide non-semantic positions.
- [[MaskedLanguageModel]] — often uses `[MASK]` as a special token.
