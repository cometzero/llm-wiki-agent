---
title: "Floating Point"
type: concept
tags: [Numerics, Quantization, Range, Precision]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[FloatingPoint]] represents numbers with a sign, exponent, and mantissa. It is more complex than fixed-point or integer formats, but it offers a much larger dynamic range and better relative precision across very small and very large values.

The source uses floating point to explain why formats such as [[FP16]], [[BF16]], and [[FP8]] are useful for neural networks even when pure integer arithmetic is cheaper.

## Connections
- [[IEEE754]] — standard floating-point encoding family.
- [[FP16]] — reduced-precision float.
- [[BF16]] — reduced-precision float with larger exponent range.
- [[FP8]] — very low-precision float used in modern AI systems.
- [[FixedPoint]] — simpler but less range-flexible alternative.
