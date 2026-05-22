---
title: "Inference Stack"
type: concept
tags: [ai-ml, serving, infrastructure, deployment]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

The [[InferenceStack]] is the complete infrastructure for serving trained models in production—handling user requests, model execution, and response delivery.

## Components

1. **API server**: Receives and routes requests
2. **Model runtime**: Executes model inference
3. **Serving optimization**: [[Quantization]], [[Batching]], [[KVCache]]
4. **Response delivery**: [[Streaming]], pagination
5. **Monitoring**: [[Latency]], error rates, cost tracking

## Design Considerations

- **Latency vs. throughput trade-off**: [[Batching]] increases throughput but may hurt latency
- **Memory management**: Model size, [[KVCache]] size, concurrent users
- **Cost per query**: Hardware efficiency directly affects margins

## Connection to Training Stack

Inference and [[TrainingStack]] have different optimization goals:
- Training: Achieve best model quality
- Inference: Minimize latency and cost per query

This often requires model conversion (e.g., to INT8 for [[Quantization]]).

## Connections
- [[Serving]] — inference stack enables serving
- [[TrainingStack]] — produces the models inference stack serves
- [[Latency]] — primary performance metric
- [[Throughput]] — capacity metric
- [[Quantization]] — common inference optimization
- [[KVCache]] — memory optimization for inference
- [[Batching]] — throughput optimization
- [[Streaming]] — response optimization
