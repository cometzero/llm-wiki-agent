---
title: "Prompt Sensitivity"
type: concept
tags: [prompting, llm, reliability]
sources: [2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
Prompt sensitivity is the tendency of an [[LLM]] to produce noticeably different outputs after small changes in wording, ordering, examples, or constraints in the prompt.

## Why It Matters
Because prompts alter the input token sequence, they change hidden states, attention patterns, and next-token probabilities. Production systems therefore test prompts across many cases instead of trusting a single example.

## Related Concepts
- [[PromptEngineering]] — manages prompt behavior
- [[InstructionDesign]] — reduces ambiguity
- [[ContextWindow]] — limits how much prompt context can be used

## Sources
- [[2026-05-21-day29-ai-ml-learning-review]]
