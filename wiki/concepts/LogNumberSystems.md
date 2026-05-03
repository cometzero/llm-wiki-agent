---
title: "Log Number Systems"
type: concept
tags: [Quantization, LogarithmicRepresentation, AlternativeFormats]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[LogNumberSystems]] represent values in logarithmic space rather than linear space. They can make rounding error small in relative terms, but addition becomes expensive because the representation is no longer aligned with standard adder hardware.

The source presents log number systems as one possible route beyond 8-bit scaling, but notes that the adder cost is a major obstacle.

## Connections
- [[NeuralNetworkQuantization]] — source context.
- [[FloatingPoint]] — related by using exponent-like structure.
- [[BlockNumberFormats]] — alternative route to better precision efficiency.
