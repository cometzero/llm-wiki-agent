---
title: "Foundation Model"
type: concept
tags: [foundation-model, pretraining, adaptation]
sources: [2026-05-20-day28-ai-ml-learning-review.md, 2026-05-18-day26-ai-ml-learning-review.md]
last_updated: 2026-05-20
---

## Definition
A foundation model is a large-scale pre-trained model that serves as a base for multiple downstream tasks. Unlike task-specific models trained from scratch, foundation models learn general patterns from massive data and can be adapted through various methods like prompt engineering, fine-tuning, or RAG.

## Key Properties
- **Pre-training**: Learns general patterns from massive datasets (e.g., 1 trillion tokens for LLMs)
- **Representation Learning**: Compresses data distributions into parameters via next-token prediction
- **General-Purpose Capability**: One model handles multiple input types and tasks
- **Adaptation**: Customized for specific purposes via prompt engineering, instruction tuning, RLHF, RAG, or tool use
- **Deployment**: Combined with search systems, databases, safety filters, and monitoring in production

## Foundation Model Workflow
1. **Pretraining**: Learn general patterns from large data (e.g., next-token prediction for LLMs)
2. **Representation Learning**: Convert words, sentences, images, code into embedding/hidden state vectors
3. **General-Purpose Capability**: Handle diverse inputs and tasks
4. **Adaptation**: Fine-tune for specific purposes using various methods
5. **Deployment**: Integrate with production infrastructure

## Examples in Production
- **LLMs**: ChatGPT, Claude, Gemini — trained with instruction tuning and safety learning
- **Enterprise chatbots**: Foundation model + RAG for company document retrieval
- **Coding assistants**: Foundation model + code data and tool execution capabilities
- **Vision models**: CLIP, Stable Diffusion, vision-language models for search, generation, classification

## Contrast with Task-Specific Models
| Aspect | Task-Specific | Foundation Model |
|--------|-------------|-----------------|
| Training data per task | 100,000+ examples | 100 examples + prompt |
| Reusability | Single task only | Multiple tasks |
| Cost | High (per task) | Lower (shared base) |

## Connections
- [[Pretraining]] — the initial training phase
- [[TransferLearning]] — enabled by foundation models
- [[FineTuning]] — adaptation method
- [[LoRA]] — efficient adaptation technique
- [[RAG]] — retrieval-augmented adaptation
- [[LLM]] — foundation model example
- [[ChatGPT]], [[Claude]], [[Gemini]] — production examples
