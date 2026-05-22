---
title: "Batching"
type: concept
tags: [ai-ml, serving, optimization, throughput]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

[[Batching]] groups multiple user requests together for parallel GPU processing, increasing [[Throughput]] by utilizing GPU parallelism more efficiently than processing requests one-by-one.

## Why It Matters

GPU parallelism is most efficient when processing many similar operations together. Single-request processing leaves most GPU resources idle. Batching amortizes this overhead.

## Analogy: Cafe

- **Sequential**: One coffee at a time (2 min each)
  - 10 customers = 20 minutes total wait
- **Batched**: Multiple drinks prepared simultaneously
  - 10 customers = ~5-7 minutes total wait

## Trade-offs

| Benefit | Cost |
|---------|------|
| Higher [[Throughput]] | Higher [[Latency]] for some users (wait for batch) |
| Better GPU utilization | Need to handle variable-length sequences |
| Lower cost per request | Requires careful scheduling |

## Types

- **Static batching**: Fixed batch size, simple but may waste resources
- **Dynamic batching**: Adaptive batch size based on load
- **Continuous batching**: New requests added as others complete (most common for LLMs)

## Connections
- [[Serving]] — key serving optimization technique
- [[Throughput]] — batching primarily increases throughput
- [[Latency]] — batching may increase latency for some requests
- [[InferenceStack]] — batch scheduling is a core serving component
