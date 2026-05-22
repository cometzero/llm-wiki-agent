---
title: "Inference"
type: concept
tags: [ai-ml, serving, optimization]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

Inference is the process of using a trained model to compute an output for a new input. In an LLM service, inference means generating tokens in response to a user prompt.

## Why It Matters

Training changes model parameters; inference uses the learned parameters in production. Inference quality, latency, throughput, and cost determine whether a model can be served reliably to users.

## Connections
- [[Serving]] — serving exposes inference as a user-facing system.
- [[InferenceStack]] — infrastructure that runs inference in production.
- [[Latency]] — request-level speed metric for inference.
- [[Throughput]] — aggregate inference capacity metric.
- [[KVCache]] — common optimization for autoregressive inference.
