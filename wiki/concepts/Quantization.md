---
title: "Quantization"
type: concept
tags: [ai-ml, model-compression, serving, optimization]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

[[Quantization]] is the technique of representing model weights and activations using lower-precision numbers (e.g., 32-bit float → 8-bit integer). This reduces memory usage and computation cost while trading off some accuracy.

## How It Works

Neural networks can tolerate small numerical errors because millions of weights work together—individual precision loss doesn't collapse overall patterns. For example:
- **FP32**: 4 bytes per weight (32 bits)
- **INT8**: 1 byte per weight (8 bits)
- **INT4**: 0.5 bytes per weight (4 bits)

Memory reduction: ~4x (FP32→INT8), ~8x (FP32→INT4)

## Trade-offs

| Precision | Memory | Speed | Accuracy |
|-----------|--------|-------|----------|
| FP32 | 100% | 100% | Baseline |
| INT8 | ~25% | ~2-3x faster | ~1-2% loss |
| INT4 | ~12.5% | ~4x faster | ~3-5% loss |

Too aggressive quantization (e.g., INT2) can cause significant quality degradation.

## Use Cases

- **On-device AI**: Smartphones, laptops with limited memory
- **Cost reduction**: Cloud services with budget constraints
- **[[Throughput]] boost**: More requests handled per GPU

## Connections
- [[Serving]] — enables efficient serving of large models
- [[Throughput]] — increases throughput via faster computation
- [[Latency]] — can reduce latency via faster inference
- [[KVCache]] — smaller models = smaller cache memory footprint
