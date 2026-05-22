---
title: "Throughput"
type: concept
tags: [ai-ml, performance, serving, metrics]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

[[Throughput]] is the amount of work a system can process per unit time—measured as requests/second, tokens/second, or queries/second.

## Why Throughput Matters

A system may respond instantly to a single user but fail when 1,000 concurrent users arrive. [[Throughput]] determines how many users the service can handle simultaneously without degradation.

## Latency vs. Throughput

| Metric | Perspective | Question |
|--------|-------------|----------|
| [[Latency]] | Individual user | "How long do I wait?" |
| [[Throughput]] | System operator | "How many can we serve?" |

High throughput with high latency means "many users get slow responses." Low throughput with low latency means "few users get fast responses." The goal is balanced optimization.

## Optimization Techniques

- **[[Batching]]**: Process multiple requests together for GPU efficiency
- **[[Quantization]]**: Smaller weights = faster computation
- **[[KVCache]]**: Reuse computations across tokens
- **Hardware scaling**: More GPUs for parallel processing

## Trade-offs

Batching increases throughput but may increase individual latency (waiting for batch to fill). Serving strategies must balance these based on use case—interactive chatbots prioritize latency, batch processing prioritizes throughput.

## Connections
- [[Serving]] — throughput is a core serving metric
- [[Latency]] — often in tension with throughput
- [[Batching]] — increases throughput at potential latency cost
- [[Quantization]] — enables higher throughput
