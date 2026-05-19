---
title: "Hallucination"
type: concept
tags: [llm, reliability, alignment, trustworthiness]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Hallucination refers to the phenomenon where an LLM generates confident-sounding but factually incorrect, fabricated, or nonsensical content. The model produces outputs that appear plausible and well-structured but do not accurately reflect reality.

## Why It Happens
LLMs are trained on next-token prediction objective — they optimize for producing natural-sounding text, not for verifying factual accuracy. This creates a gap between:
- **Fluent**: Outputs sound natural and grammatically correct
- **Factual**: Outputs accurately represent real-world information

## Types of Hallucination
1. **Intrinsic**: Output contradicts facts provided in the input/context
2. **Extrinsic**: Output contains fabricated information not present in any source

## Common Triggers
- Questions about niche topics, recent events, or private information
- When model lacks relevant training data
- Overconfident responses on uncertain topics
- Long generations where errors compound

## Mitigation Strategies
- [[Grounding]]: Connect answers to external evidence (RAG, citations, search)
- [[Calibration]]: Train model to express uncertainty
- Retrieval augmentation: Fetch facts before answering
- Chain-of-thought: Encourage verification steps

## Related Concepts
- [[Grounding]] — connecting outputs to evidence
- [[Calibration]] — expressing appropriate uncertainty
- [[RAG]] — retrieval-augmented generation for factual grounding
- [[Uncertainty]] — knowing what the model doesn't know
