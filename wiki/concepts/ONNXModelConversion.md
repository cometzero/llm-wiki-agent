---
title: "ONNX Model Conversion"
type: concept
tags: [interop, framework, ml]
sources:
  - san19-211
last_updated: 2026-04-20
---

## Definition
[[ONNXModelConversion]] is the process of exporting models from source frameworks into [[ONNX]] format.

## Source methods
- Framework conversion tools (TF2ONNX, keras2onnx, onnx-onnxmltools).
- Native export paths (PyTorch, CNTK).
- Import from repository/service channels (e.g., [[ONNXZoo]], [[AzureCustomVision]]).

## Significance
Conversion allows models trained across frameworks (e.g., [[TensorFlow]], [[PyTorch]], [[Keras]]) to be standardized and deployed through the same runtime stack.

## Connections
- [[ONNXRuntime]]
- [[ONNXZoo]]
- [[ONNXRuntimeTraining]]
- [[ONNX]]