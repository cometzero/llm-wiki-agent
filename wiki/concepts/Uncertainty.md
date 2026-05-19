---
title: "Uncertainty"
type: concept
tags: [llm, reliability, calibration, uncertainty]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
Uncertainty is the degree to which a model should be unsure about an answer, prediction, or generated claim. In LLM systems it matters because fluent language can hide low confidence or missing evidence.

## Role in LLM Reliability
Uncertainty expression lets an assistant say when information is missing, when evidence is weak, or when a claim needs verification. It complements [[Calibration]], which asks whether confidence matches actual accuracy, and [[Grounding]], which anchors answers to external evidence.

## Practical Signals
- The model lacks relevant context or source documents.
- Retrieved evidence is incomplete or contradictory.
- The question concerns private, recent, or niche facts.
- Multiple plausible answers exist and cannot be distinguished from context.

## Related Concepts
- [[Calibration]] — matching confidence to real correctness.
- [[Hallucination]] — risk when uncertainty is not handled well.
- [[Grounding]] — reducing uncertainty by using external evidence.
