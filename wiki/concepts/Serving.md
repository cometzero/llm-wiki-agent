---
title: "Serving"
type: concept
tags: [ai-ml, serving, inference, deployment]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

[[Serving]] is the process of making a trained model respond to real user requests in production. It encompasses the entire flow: user submits a query via app, server calls the model, model generates an answer, and the result is returned to the user.

## Relationship to Inference

- **[[Inference]]**: Computing outputs from a trained model for new inputs (the computation itself)
- **[[Serving]]**: Providing this inference as an actual service (the operational layer)

## Serving Components

1. **Model selection**: Choosing which model to deploy
2. **Hardware**: CPU, GPU, NPU selection
3. **Request handling**: Sequential vs. batched processing
4. **Memory management**: Storing model parameters, hidden states, KV cache
5. **Response streaming**: Token-by-token delivery to reduce perceived latency

## Key Metrics

- **[[Latency]]**: Time from request to first/last token response
- **[[Throughput]]**: Requests or tokens processed per unit time
- **Cost per query**: Critical for business viability

## Optimization Techniques

- **[[Batching]]**: Grouping multiple requests for parallel GPU utilization
- **[[Streaming]]**: Sending tokens as generated rather than waiting
- **[[Quantization]]**: Reducing model weight precision for faster inference
- **[[KVCache]]**: Reusing computed keys/values across tokens

## Why Serving Matters

Even smart models fail as services if:
- Response is too slow (users abandon)
- Cost per query is too high
- System can't handle concurrent users
- Memory constraints limit context length

## Connections
- [[Inference]] — the computation being served
- [[Latency]] — critical user experience metric
- [[Throughput]] — system capacity metric
- [[Quantization]] — serving optimization technique
- [[KVCache]] — memory optimization for LLM serving
- [[Batching]] — throughput optimization technique
- [[Streaming]] — latency optimization technique
