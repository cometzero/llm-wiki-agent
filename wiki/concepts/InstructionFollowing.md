---
title: "Instruction Following"
type: concept
tags: [llm, alignment, instruction-tuning]
sources: [2026-05-18-day26-ai-ml-learning-review]
last_updated: 2026-05-18
---

## Definition
Instruction following is an LLM's ability to read a user request, infer the intended task and constraints, and produce a response that follows the requested content, format, tone, and safety boundaries.

## Key Points
- [[InstructionTuning]] and [[SupervisedFineTuning]] are common ways to improve instruction-following behavior.
- It changes the model from simply continuing text into acting like an assistant that answers, summarizes, translates, explains, or writes code on request.
- Good instruction following depends on diverse, high-quality instruction-response examples and later preference alignment.

## Connections
- [[RLHF]] and [[PreferenceOptimization]] can further refine instruction following by rewarding responses people prefer.
- [[PromptEngineering]] depends on the model having learned to respect prompt instructions and constraints.
