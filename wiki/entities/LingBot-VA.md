---
title: "LingBot-VA"
type: entity
tags: [WAM, robot-model]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
LingBot-VA는 Embodied.cpp에서 WAM(World Action Model) block benchmark에 사용된 모델이다. GGUF Q4_K quantization으로 VRAM 312.2 MiB에서 88.1 MiB로 감소하며, cosine similarity >0.9997을 유지한다.

## Key Properties
- **Type**: World Action Model (WAM)
- **Use case**: Single Transformer block microbenchmark
- **Quantization**: [[GGUFQuantization]] Q4_K
- **Memory**: 312.2→88.1 MiB (71.8% reduction)
- **Quality**: cosine similarity >0.9997

## Connections
- [[WAM]] — model category
- [[EmbodiedCpp]] — deployment runtime
- [[GGUFQuantization]] — memory reduction technique
