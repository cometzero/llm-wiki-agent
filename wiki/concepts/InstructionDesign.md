---
title: "Instruction Design"
type: concept
tags: [prompting, llm, instruction-following]
sources: [2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
Instruction design is the part of [[PromptEngineering]] that states the task, role, constraints, reasoning order, and output format an [[LLM]] should follow.

## Practical Role
Clear instructions help the model select the desired behavior from many plausible completions. They are especially useful in [[RAG]] prompts where the model must answer from retrieved context and avoid unsupported claims.

## Related Concepts
- [[PromptEngineering]] — broader design practice
- [[SystemPrompt]] — global role and policy layer
- [[Hallucination]] — reduced by grounded instructions, but not eliminated

## Sources
- [[2026-05-21-day29-ai-ml-learning-review]]
