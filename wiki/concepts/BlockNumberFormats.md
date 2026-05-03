---
title: "Block Number Formats"
type: concept
tags: [Quantization, SharedExponent, TensorFormats]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[BlockNumberFormats]] are numeric schemes where several adjacent values share a common exponent or scale. The idea is that nearby tensor elements often have similar magnitude, so one shared scale can preserve useful precision while saving bits.

The source cites approaches such as [[Nervana Flexpoint]], [[Microsoft MSFP12]], [[Nvidia VSQ]], and [[OCP Microscaling]] as related directions.

## Connections
- [[NeuralNetworkQuantization]] — source context.
- [[Microscaling]] — standardization direction for shared-scale formats.
- [[Tensor]] — data structure where locality of scale often appears.
- [[Nervana Flexpoint]] — early related approach.
- [[Microsoft MSFP12]] — related shared-scale format.
- [[Nvidia VSQ]] — related shared-scale format.
