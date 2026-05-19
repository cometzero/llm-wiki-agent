---
title: "Temperature"
type: concept
tags: [decoding-strategy, llm, inference, probability]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Temperature is a scaling factor applied to logits before softmax that controls the "sharpness" of the probability distribution. Lower temperature makes high-probability tokens even more dominant; higher temperature flattens the distribution, allowing lower-probability tokens to be selected more often.

## Key Properties
- **T < 1.0**: Conservative, deterministic, focused outputs (lower creativity)
- **T = 1.0**: Original probability distribution unchanged
- **T > 1.0**: Exploratory, diverse, creative outputs (higher risk of odd tokens)
- **T = 0**: Equivalent to greedy decoding (argmax)

## Mathematical Description
P(t_i) = softmax(logit_i / T) = exp(logit_i / T) / Σ exp(logit_j / T)

## Practical Guidelines
- **Code generation**: T ≈ 0.1–0.3 (accuracy critical)
- **Creative writing**: T ≈ 0.7–1.0 (diversity desired)
- **Chat/rag**: T ≈ 0.5–0.8 (balance)
- **Extraction/classification**: T ≈ 0.1 (low randomness)

## Related Concepts
- [[GreedyDecoding]] — T=0 limit
- [[TopP]] — often used together with temperature
- [[TopK]] — can combine with temperature for fine control
- [[Calibration]] — temperature affects confidence expression
