---
title: "TaskMetric"
type: concept
tags: [ai-ml, evaluation, metrics]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

A [[TaskMetric]] is a scoring rule chosen for a specific AI task, such as classification, summarization, code generation, retrieval, or safety evaluation.

## Key Points

- Classification tasks often use accuracy, precision, recall, and F1.
- Generation tasks may use exact match, BLEU, ROUGE, pass@k, win rate, or human preference scores.
- The right metric depends on the product goal and the cost of different errors.
- In LLM systems, task metrics are usually combined with [[HumanEvaluation]], [[Benchmark]] results, latency, and cost.

## Connections

- [[Evaluation]] — uses task metrics to measure model quality.
- [[Benchmark]] — packages tasks, datasets, and metrics into a repeatable comparison setup.
- [[HumanEvaluation]] — complements automatic task metrics when output quality is subjective.
