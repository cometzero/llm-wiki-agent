---
title: "Supervised Fine-Tuning (SFT)"
type: concept
tags: [llm, fine-tuning, training]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
The method of further training an already pretrained model on labeled data (instruction-answer pairs) to adapt its behavior for specific tasks or patterns.

## How It Works
- Uses standard next-token prediction loss
- Unlike pretraining: uses curated instruction-response pairs, not arbitrary web text
- Goal: maximize probability of generating the correct response tokens

### Tensor Shapes (Simplified)
- Input shape: [batch_size, sequence_length]
- Example: 2 examples, each 8 tokens → [2, 8]
- Logits shape: [batch_size, sequence_length, vocab_size]
- Loss calculated only on answer portion tokens

## Role in LLM Development
1. **Pretraining**: Learn language patterns from massive web text
2. **SFT**: Learn to behave as an assistant, follow instructions
3. **RLHF** (optional): Fine-tune to human preferences

## Key Properties
- Changes "how to answer" more than "what is known"
- Data quality is critical: models learn both good AND bad behaviors from examples
- Diversity of instruction types prevents overfitting to specific formats

## Common Use Cases
- Chatbots and virtual assistants
- Code generation models
- Customer support AI
- Educational tutors
- Summarization and translation services

## Connections
- Implements [[InstructionTuning]] in practice
- Follows [[Pretraining]] and precedes [[RLHF]] in standard pipeline
- Related to [[FineTuning]] (broader term)
- [[InstructionFollowing]] ability emerges from SFT
- [[ParameterCount]] affects model capacity for learning response patterns
