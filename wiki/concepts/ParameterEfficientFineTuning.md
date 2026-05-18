---
title: "Parameter-Efficient Fine-Tuning"
type: concept
tags: [fine-tuning, llm, efficiency]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
Parameter-efficient fine-tuning adapts a pretrained model by updating only a small subset of parameters or small added modules instead of all model weights.

## Key Points
- It lowers compute and memory cost compared with full [[FineTuning]].
- It is useful when the base model has a large [[ParameterCount]].
- LoRA-style adapters are a common example of the approach.

## Connections
- [[SupervisedFineTuning]] can be implemented either as full fine-tuning or parameter-efficient fine-tuning.
