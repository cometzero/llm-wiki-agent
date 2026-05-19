---
title: "Beam Search"
type: concept
tags: [decoding-strategy, llm, inference, search-algorithm]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Beam search is a decoding strategy that maintains multiple candidate sequences (beams) simultaneously, rather than committing to a single path. At each step, it expands all beams and keeps the top k most promising candidates.

## Key Properties
- **Key parameter**: beam width (number of candidates kept)
- **Trade-off**: Better outputs than greedy but more computation
- **Common use**: Machine translation, text summarization
- **Limitation**: Still suboptimal — true optimal requires exhaustive search (too expensive)

## Comparison with Greedy Decoding
- Greedy: 1 beam, picks best at each step
- Beam search: keeps N beams, explores multiple partial sequences

## When to Use
- Tasks requiring coherent long outputs
- Translation, summarization where quality matters more than speed
- Less common in modern chat LLMs (often replaced by nucleus/top-p sampling)

## Related Concepts
- [[GreedyDecoding]] — single-path baseline
- [[TopP]] — probabilistic alternative with implicit beam diversity
- [[Temperature]] — controls exploration/exploitation balance
