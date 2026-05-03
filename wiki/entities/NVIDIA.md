---
title: "NVIDIA"
type: entity
tags: [Hardware, GPU, AI, Quantization]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

NVIDIA is referenced here as the dominant vendor driving practical [[NeuralNetworkQuantization]] and low-precision AI hardware adoption. In this source, NVIDIA appears through its use of [[FP8]], [[FP4]], [[FP6]], [[TensorCores]], and related hardware design choices that shape the efficiency/accuracy tradeoff for [[LLM]] inference and training.

## Connections
- [[NeuralNetworkQuantization]] — major hardware driver of reduced-precision deployment.
- [[FP8]] — low-precision format emphasized in Hopper-era training.
- [[FP4]] — low-precision inference format emphasized in Blackwell-era design.
- [[FP6]] — additional low-precision format used in Blackwell-era design.
- [[TensorCores]] — the compute substrate for low-precision matrix math.
- [[Hopper]] — generation that popularized FP8 training recipes.
- [[Blackwell]] — generation that extends low-precision and tensor-memory design.
