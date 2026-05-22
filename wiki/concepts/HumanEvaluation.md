---
title: "Human Evaluation"
type: concept
tags: [ai-ml, evaluation, alignment]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

Human evaluation is manual assessment of model outputs by people. It is used when automatic metrics cannot fully capture usefulness, correctness, style, safety, or instruction following.

## Why It Matters

LLM outputs can be valid in many forms, so a single numeric metric may miss important quality differences. Human judgments help evaluate nuanced response quality and can produce preference data for alignment.

## Connections
- [[Evaluation]] — human evaluation complements automatic metrics and benchmarks.
- [[RLHF]] — preference data from human judgments can guide alignment training.
- [[FeedbackLoop]] — user and reviewer judgments can feed future eval sets.
