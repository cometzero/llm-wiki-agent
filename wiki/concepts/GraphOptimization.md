---
title: "Graph Optimization"
type: concept
tags: [inference, compiler, graph]
sources:
  - san19-211
last_updated: 2026-04-20
---

## Definition
[[GraphOptimization]] refers to transformations applied to an [[ONNX]] computational graph before execution to improve runtime efficiency.

## Common transforms
- Dropout/identity node removal.
- Operator fusion.
- Constant folding.

## Optimization levels
- Level 0: applies after graph partitioning (e.g., cast/memcpy insertions).
- Level 1: generic, provider-agnostic optimizations.
- Level 2: provider-specific optimizations.

## Why it matters
It reduces unnecessary work and enables better matching between graph structure and backend strengths, especially when combined with provider partitioning.

## Connections
- [[ONNXRuntime]]
- [[ExecutionProvider]]
- [[ONNXGraphPartitioning]]
- [[ONNXModelConversion]]
- [[HeterogeneousInference]]