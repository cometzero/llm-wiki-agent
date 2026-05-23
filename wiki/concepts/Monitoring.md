---
title: "Monitoring"
type: concept
tags: [ai-ml, ml-ops, operations]
sources: [2026-05-23-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Monitoring is the ongoing observation of a deployed AI system's behavior, performance, quality, and cost after release.

## Why It Matters
AI systems can degrade after deployment because user inputs, data distributions, traffic patterns, and product requirements change. Monitoring helps teams detect latency spikes, error increases, quality regressions, cost growth, and [[DataDrift]].

## Common Signals
- [[Latency]] and [[Throughput]] for serving performance
- Error rate and failed requests
- Output quality and user feedback
- Data distribution changes and drift
- Cost per request or token

## Connections
- [[InferenceStack]] — monitoring is part of production inference operations
- [[FeedbackLoop]] — monitored failures feed future improvements
- [[Evaluation]] — offline evals complement online monitoring
- [[DataDrift]] — monitoring helps detect distribution shifts
