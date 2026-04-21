---
title: "ONNX Runtime"
type: concept
tags: [inference, runtime, optimization, npu, compiler]
sources:
  - san19-211
last_updated: 2026-04-20
---

## Definition
[[ONNXRuntime]] is a high-performance runtime for running [[ONNX]] models across multiple hardware targets with modular execution backends.

## Core mechanisms
- **Graph optimization**: removes dead/identity nodes, fuses patterns, and performs constant folding.
- **Graph partitioning**: splits subgraphs by execution capability and assigns nodes to suitable backends.
- **Execution provider model**: supports kernel-level and graph-level providers (e.g., [[CUDA]], [[TensorRT]], [[nGraph]], CPU).
- **API usability**: offers lightweight bindings (including [[Python]] and [[C#]]) centered on `InferenceSession`-style workflow.

## Key claims from source
- Supports cross-platform inference (Windows/Mac/Linux), CPU/GPU/edge targets.
- Includes lightweight training runtime in addition to inference; 학습/추론 모두 지원.
- Uses plugin-friendly architecture for adding accelerators and optimization tooling.

## Related concepts
- [[ONNX]]
- [[GraphOptimization]]
- [[ExecutionProvider]]
- [[HeterogeneousInference]]
- [[ONNXModelConversion]]

## Connections
- [[AzureML]], [[AzureCustomVision]], and [[ONNXZoo]] appear as adjacent model and deployment pathways.
- Operational evidence is linked to [[Microsoft]] deployments.