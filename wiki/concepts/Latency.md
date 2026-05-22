---
title: "Latency"
type: concept
tags: [ai-ml, performance, serving, metrics]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

[[Latency]] is the time from when a request is received until the response is delivered. For LLM services, this includes:
- **Time to First Token (TTFT)**: How quickly the first token appears
- **Time Per Output Token (TPOT)**: Average time per subsequent token
- **Total Latency**: Complete response time

## Why Latency Matters

Users perceive responses as "slow" when first tokens take too long. Even with high-quality output, a 30-second delay creates poor user experience. First token latency is particularly important because seeing immediate response makes users feel the system is "fast."

## Latency vs. Throughput

| Metric | Perspective | Question Answered |
|--------|-------------|-------------------|
| [[Latency]] | Individual user | "How long do I wait?" |
| [[Throughput]] | System operator | "How many can we serve?" |

These metrics can be in tension—optimizing for one may harm the other.

## Optimization Techniques

- **[[Streaming]]**: Send tokens as generated
- **[[KVCache]]**: Reuse computed values to skip recomputation
- **[[Quantization]]**: Smaller models compute faster
- **[[Batching]]**: Trade latency for throughput (wait for batch)

## Connections
- [[Serving]] — latency is a core serving metric
- [[Throughput]] — often in tension with latency
- [[Streaming]] — reduces perceived latency
- [[KVCache]] — reduces per-token computation time
