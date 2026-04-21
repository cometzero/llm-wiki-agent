---
title: "Execution Provider"
type: concept
tags: [runtime, execution, hardware, inference]
sources:
  - san19-211
last_updated: 2026-04-20
---

## Definition
An [[ExecutionProvider]] (EP) is a runtime layer that maps [[ONNX]] operators or subgraphs to a specific execution backend.

## Types described
- **Kernel-based EP**: implements individual operator execution (예: [[CudaExecutionProvider]], [[MKLDNNExecutionProvider]]).
- **Runtime-based EP**: executes whole or partial graphs (예: [[TensorRT]], [[nGraphExecutionProvider]]).

## Role in ONNX inference
- EP selection and ordering determines where each graph node runs.
- Provider capabilities are checked and nodes are assigned greedily according to preferred order.
- This enables efficient [[HeterogeneousInference]] by combining CPU, GPU, and accelerator strengths.

## Connections
- [[ONNXRuntime]]
- [[GraphPartitioner]]
- [[GraphOptimization]]
- [[NVIDIA]], [[Intel]]