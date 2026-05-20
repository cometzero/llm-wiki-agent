---
title: "PEFT (Parameter-Efficient Fine-Tuning)"
type: concept
tags: [peft, parameter-efficient, fine-tuning, lora]
sources: [2026-05-20-day28-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
PEFT (Parameter-Efficient Fine-Tuning) refers to techniques that fine-tune large models by modifying only a small subset of parameters rather than updating all weights. This reduces GPU memory, training time, and storage requirements.

## Why PEFT is Needed
- Modern LLMs have billions to hundreds of billions of parameters
- Full fine-tuning requires significant GPU memory, training time, and storage
- Many adaptation tasks only require small adjustments (tone, format, domain vocabulary)
- Cost-effective when shared across multiple applications or customers

## Key Methods

### Full Fine-Tuning
- Updates all parameters
- Most powerful but expensive
- Risk of overfitting

### LoRA (Low-Rank Adaptation)
- Fixes large weight matrix W
- Learns small low-rank decomposition matrices A and B
- Change: h = (W + ΔW)x where ΔW = BA
- Example: 10,000 parameter W with rank-4 LoRA uses only 800 trainable parameters

### Adapter
- Inserts small trainable modules between model layers
- Original model weights remain frozen

### Prompt Tuning / Prefix Tuning
- Adds learnable prompt vectors at the input
- Modifies model behavior without changing internal weights

## Real-World Applications
- Adapting to company document styles
- Domain-specific tone (medical, legal, financial)
- Customer-specific model variants
- Multi-tenant serving: shared base model + small per-customer adapters

## Cost Example
| Component | Full Fine-Tuning | LoRA |
|-----------|------------------|------|
| Base model | 10 GB | 10 GB |
| Trained weights | 10 GB | 100 MB |
| Per customer (10) | 100 GB | 1 GB |

## Connections
- [[LoRA]] — specific PEFT method
- [[FoundationModel]] — what PEFT adapts
- [[TransferLearning]] — the paradigm PEFT enables
- [[FineTuning]] — contrast with full fine-tuning
