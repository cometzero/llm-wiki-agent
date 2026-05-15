---
title: "AI/ML Learning Review — Day 23 (2026-05-15): Residual Connection, LayerNorm, Position-wise FFN"
type: source
tags: [ai-ml-learning, transformer, deep-learning]
date: 2026-05-15
source_file: raw/ai_ml_learning/2026-05-15-day23-ai-ml-learning-review.md
source_hash: c89ef3486730df5d
---

## Summary
Day 23 covers three foundational components of the [[Transformer]] block that enable stable deep learning: [[ResidualConnection]], [[LayerNorm]], and [[PositionWiseFFN]]. Each component serves a distinct role in preserving information flow, stabilizing numerical scales, and transforming token representations.

## Key Claims
- [[ResidualConnection]] creates a "shortcut path" (`y = x + F(x)`) that preserves original information while allowing incremental modifications, enabling stable gradient propagation in deep networks.
- [[LayerNorm]] normalizes each token's hidden state along the feature dimension (not batch dimension), providing stability against scale fluctuations across [[Transformer]] layers.
- [[PositionWiseFFN]] applies an MLP independently to each token position after [[Attention]] mixing, transforming features through expansion-activation-contraction (e.g., 768 → 3072 → 768 dimensions).

## Key Quotes
> "Residual connection은 '블록이 새로 계산한 내용만 더하고, 원래 정보는 그대로 지나가게 해 주는 지름길'이다. 그래서 모델이 깊어져도 정보와 gradient가 길을 잃지 않는다."

> "LayerNorm은 각 token의 hidden state 안에서 feature 값들의 크기와 중심을 정리해, 다음 block이 너무 크거나 너무 작은 숫자에 흔들리지 않게 해 주는 안정화 장치다."

> "Attention이 '누구의 정보를 볼지'를 결정한다면, FFN은 '그 정보를 보고 내 token 표현을 어떻게 가공할지'를 담당한다."

## Connections
- [[Transformer]] — all three concepts are core components of Transformer blocks
- [[Attention]] — Position-wise FFN operates on attention's output
- [[Gradient]] — Residual connection enables gradient flow through skip paths
- [[HiddenState]] — LayerNorm normalizes; ResidualConnection preserves; FFN transforms
- [[PreLN]] / [[PostLN]] — LayerNorm positioning variants in Transformer architecture
- [[SkipPath]] — alternative name for residual connection's direct path
- [[BatchNormalization|BatchNorm]] — contrast with LayerNorm (feature-wise vs batch-wise normalization)
- [[MultiLayerPerceptron|MLP]] — Position-wise FFN is an MLP applied per token position

## Contradictions
- None identified. Content is consistent with established [[Transformer]] architecture knowledge.

## Review Questions
1. Why does `y = x + F(x)` help gradient propagation in deep models?
2. What dimension does LayerNorm normalize, and how does it differ from BatchNorm?
3. What distinct roles do [[Attention]] and [[PositionWiseFFN]] play in a Transformer block?
