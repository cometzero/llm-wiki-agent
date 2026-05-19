---
title: "Top-K Sampling"
type: concept
tags: [decoding-strategy, llm, inference, sampling]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Top-k sampling restricts the candidate token set to the k highest-probability tokens, then samples from this restricted distribution.

## Key Properties
- **Selection criterion**: Count-based (fixed number of candidates)
- **k = 1**: Equivalent to greedy decoding
- **Advantage**: Bounds the diversity of outputs
- **Limitation**: k is fixed regardless of distribution shape — may include very unlikely tokens if k is large, or miss good candidates if k is small

## Example
If k=3 and probabilities are:
- "dog": 0.5, "cat": 0.3, "bird": 0.1, "car": 0.05, "rock": 0.05

Top-3 keeps: dog, cat, bird (discards car, rock)

## Related Concepts
- [[GreedyDecoding]] — k=1 limit
- [[TopP]] — alternative with dynamic candidate count based on probability mass
- [[Temperature]] — modifies distribution before top-k filtering
- [[BeamSearch]] — different approach to balancing exploration
