---
title: "Instruction Tuning"
type: concept
tags: [llm, fine-tuning, alignment]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
The process of training an LLM to follow questions, requests, and commands by providing instruction-response examples. The goal is to transform a next-token predictor into an instruction-following assistant.

## Implementation: Supervised Fine-Tuning (SFT)

### Data Structure
1. **Instruction**: The user\'s request (e.g., "Summarize this text in 3 lines")
2. **Input/Context**: Additional material needed for the task
3. **Response/Answer**: The ideal output the model should learn to produce

### Training Objective
- Uses next-token prediction loss
- Unlike pretraining (any text continuation), SFT uses specifically crafted instruction-answer pairs
- Adjusts model parameters via gradient to maximize probability of correct answer tokens

## Key Principles
- **Quality over quantity**: Poor examples teach poor behavior
- **Diversity of instructions**: Models trained only on summarization fail at coding or reasoning
- **Format matters**: SFT strongly influences "how to answer" more than "what is known"

## Position in LLM Pipeline
1. Large-scale pretraining on web text
2. Instruction data → SFT
3. (Optional) RLHF or preference optimization for further alignment

## Connections
- [[InstructionTuning]] is the first major step in making models behave as assistants
- [[SupervisedFineTuning]] is the practical implementation method
- Builds on [[TransformerArchitecture]] learned during pretraining
- Leads to [[RLHF]] for fine-grained preference alignment
- Related to [[PromptEngineering]] (using, not training)
- See also [[FineTuning]] for general terminology
