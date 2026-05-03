---
title: "CUDA Programming Model"
type: concept
tags: [cuda, programming-model, gpu]
sources: [part-i-intro-to-gpus]
last_updated: 2026-05-03
---

[[CUDA]] exposes GPU execution through kernels, blocks, warps, and memory spaces so programmers can map work to the hardware hierarchy. The source emphasizes that performance depends on aligning access patterns with these abstractions, especially for global memory, shared memory, and registers.

## Connections
- [[GPU]]
- [[SIMT]]
- [[SharedMemory]]
- [[Registers]]
- [[Warp]]
