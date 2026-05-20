---
title: "Transfer Learning"
type: concept
tags: [transfer-learning, foundation-model, adaptation]
sources: [2026-05-20-day28-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
Transfer learning is the approach of reusing knowledge learned from one task or large dataset to improve performance on a different but related task. Rather than training from scratch, transfer learning leverages pre-trained weights, embeddings, and hidden representations as a starting point.

## Process
1. **Source Learning**: Pre-train on large data or related tasks
2. **Reuse**: Use learned weights, embeddings, or representations as starting point
3. **Adaptation**: Adjust model to new task with task-specific data
4. **Evaluation**: Verify performance improvement on new task

## Example: Visual Domain
A model trained on natural images already learned to recognize edges, textures, and shapes. These capabilities transfer to medical X-ray classification without learning visual basics from scratch.

## Example: LLM Domain
A language model that learned language structure, context, factual knowledge, and code patterns can adapt to legal document summarization or customer service response generation with less data.

## Connection to Foundation Models
Foundation models are the modern embodiment of transfer learning:
- Pre-training on massive data captures general knowledge
- Fine-tuning or prompt engineering adapts to specific tasks
- One base model serves multiple downstream applications

## Connections
- [[FoundationModel]] — modern transfer learning implementation
- [[FineTuning]] — adaptation method
- [[LoRA]] — efficient transfer learning technique
- [[PEFT]] — parameter-efficient variants
