---
title: "LayerNorm"
type: concept
tags: [normalization, training-stability]
sources: [2026-05-07-day15-ai-ml-learning-review]
last_updated: 2026-05-07
---

## Summary
layer 내부 activation의 scale을 정규화해 학습을 안정화하는 normalization 기법이다. Transformer와 LLM에서는 residual connection과 함께 깊은 모델의 안정적인 gradient flow를 돕는다.

## Connections
- [[2026-05-07-day15-ai-ml-learning-review]] — introduced or reinforced this concept in the Day 15 AI/ML lesson.
- [[Initialization]] — scale control and stable learning context.
- [[VanishingGradient]] and [[ExplodingGradient]] — gradient-flow problems this concept helps address or diagnose.
