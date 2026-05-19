---
title: "Top-P Sampling (Nucleus Sampling)"
type: concept
tags: [decoding-strategy, llm, inference, sampling]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Top-p (nucleus) sampling dynamically selects the smallest set of highest-probability tokens whose cumulative probability exceeds threshold p, then samples from this set.

## Key Properties
- **Selection criterion**: Cumulative probability mass (dynamic count)
- **p = 1.0**: All tokens (equivalent to no filtering)
- **p close to 0**: Very few tokens (similar to greedy)
- **Advantage**: Adapts to distribution shape — narrow distributions keep fewer tokens, flat distributions keep more
- **Common default**: p ≈ 0.9 in many LLM APIs

## Example
If p=0.8 and probabilities are:
- "dog": 0.5, "cat": 0.3, "bird": 0.1, "car": 0.05, "rock": 0.05

Cumulative: dog (0.5) → cat (0.8) → bird (0.9) exceeds p

Keep: dog, cat (discards bird, car, rock)

## Why "Nucleus"?
The name refers to the "nucleus" of high-probability tokens that contain most of the probability mass.

## Related Concepts
- [[TopK]] — fixed count vs dynamic probability mass
- [[Temperature]] — often combined with top-p
- [[GreedyDecoding]] — deterministic p→0 limit
- [[BeamSearch]] — beam width is another way to control exploration
