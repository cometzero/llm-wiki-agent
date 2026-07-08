---
title: "GGUF Quantization"
type: concept
tags: [quantization, model-compression, edge-deployment]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
GGUF(Generic GPU Format) Quantization은 [[WAM]] 모델의 메모리 사용량을 줄이기 위한 양자화 기법이다. [[LingBot-VA]] WAM block에서 Q4_K quantization으로 VRAM 312.2 MiB에서 88.1 MiB로 71.8% 감소했다.

## Key Results
- **Original**: 312.2 MiB
- **Q4_K quantized**: 88.1 MiB
- **Reduction**: 71.8%
- **Quality maintained**: Cosine similarity >0.9997

## Use Case
Edge deployment에서 메모리 제약이 큰 환경에서 [[WAM]] 모델을 실용적으로 실행할 수 있게 한다.

## Connections
- [[WAM]] — quantization target
- [[LingBot-VA]] — benchmark subject
- [[EmbodiedCpp]] — runtime support for quantized models
