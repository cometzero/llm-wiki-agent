---
title: "Greedy Decoding"
type: concept
tags: [decoding-strategy, llm, inference]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Greedy decoding is the simplest token selection strategy: at each generation step, the model selects the token with the highest probability. No randomness or exploration of alternative paths occurs.

## Key Properties
- **Selection criterion**: Pick token with maximum softmax probability at each step
- **Advantages**: Fast, deterministic, reliable outputs
- **Disadvantages**: Tends to produce repetitive, monotonous text; can get stuck in local optima
- **Does not guarantee**: Globally optimal output sequence (optimal per-step ≠ optimal overall)

## Mathematical Description
Given probability distribution P(t_i | context), greedy decoding selects:
t* = argmax_i P(t_i | context)

## Related Concepts
- [[BeamSearch]] — explores multiple candidates instead of picking just one
- [[TopK]] — restricts candidates to top k before selection
- [[TopP]] — restricts candidates by cumulative probability threshold
- [[Temperature]] — modifies the probability distribution before selection

## Usage Context
- Code generation: often uses low temperature/greedy for accuracy
- Factual QA: reliable but may be repetitive
- Not suitable for: creative writing, brainstorming, diverse outputs
