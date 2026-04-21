---
title: "ONNX Runtime Training"
type: concept
tags: [training, runtime, edge]
sources:
  - san19-211
last_updated: 2026-04-20
---

## Definition
[[ONNXRuntimeTraining]] is the training-oriented path within the ONNX runtime family, enabling lightweight learning workloads with a compact binary footprint.

## Characteristics
- Lightweight training runtime binary is about 3MB; combined with inference runtime around 5MB.
- Supports reinforcement and finetuning/retraining scenarios.
- Integrates with multiple frontend frameworks and accelerator backends.

## Connections
- [[ONNXRuntime]]
- [[ONNXModelConversion]]
- [[TensorRT]]
- [[TVM]]
- [[Halide]]