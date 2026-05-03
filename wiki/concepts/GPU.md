---
title: "GPU"
type: concept
tags: [hardware, throughput, parallel-compute]
sources: [part-i-intro-to-gpus]
last_updated: 2026-05-03
---

[[GPU]] design prioritizes throughput over single-request latency. The concept is central to deep learning because massive matrix multiplication and other data-parallel workloads can keep many execution units busy at once.

## Key Ideas
- Throughput-first compute
- High parallelism
- Latency hiding through work switching
- Strong dependence on memory hierarchy efficiency

## Connections
- [[CPU]]
- [[CUDA]]
- [[SIMT]]
- [[TensorCores]]
- [[InferenceOptimization]]
