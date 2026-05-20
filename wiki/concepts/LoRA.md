---
title: "LoRA (Low-Rank Adaptation)"
type: concept
tags: [lora, low-rank-adaptation, parameter-efficient, fine-tuning]
sources: [2026-05-20-day28-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that fixes the original large weight matrix W and learns only small low-rank decomposition matrices A and B to represent weight changes ΔW.

## Core Idea
Rather than updating all parameters of W, LoRA decomposes the change into:
- ΔW = BA
- Where B is (d × r) and A is (r × k)
- r (rank) is much smaller than d and k

## Mathematical Formulation
- Original: h = Wx
- Full fine-tuning: h = W_new \times x (updates all of W)
- LoRA: h = (W + ΔW)x = (W + BA)x
  - W stays frozen (frozen parameters)
  - Only A and B are trainable parameters

## Parameter Efficiency Example
| Matrix | Dimensions | Parameters |
|--------|------------|------------|
| W (original) | 100 × 100 | 10,000 |
| A | 4 × 100 | 400 |
| B | 100 × 4 | 400 |
| **Total trainable** | - | **800** |

Reduction: 10,000 → 800 (92% fewer parameters)

## Intuition
The "low-rank" assumption means complex weight changes can be approximated by changes along just a few important directions, rather than all independent directions.

## Use Cases
- Customer-specific model variants with shared base
- Domain adaptation (legal, medical, financial)
- Style transfer for responses
- Instruction following improvements

## Limitations
- Not always better than full fine-tuning
- When large behavioral changes are needed, full fine-tuning may be preferable
- Inference still requires the full base model

## Connections
- [[PEFT]] — the category LoRA belongs to
- [[FoundationModel]] — what LoRA adapts
- [[TransferLearning]] — the paradigm it enables
- [[FineTuning]] — contrast with full fine-tuning
