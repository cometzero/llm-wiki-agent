---
title: "Number Format"
type: concept
tags: [Numerics, Representation, Quantization]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

A [[NumberFormat]] is a scheme for representing values in bits. In machine learning hardware, the format determines how much range, precision, and implementation cost a computation has.

This source contrasts [[FixedPoint]], [[FloatingPoint]], integer formats like [[INT8]], and reduced-precision formats such as [[FP16]], [[BF16]], and [[FP8]]. The main point is that format choice is a system-level decision, not a purely mathematical one.

## Connections
- [[FixedPoint]] — scale-based representation.
- [[FloatingPoint]] — exponent-based representation.
- [[INT8]] — common integer format in inference.
- [[FP16]] — reduced-precision floating-point format.
- [[BF16]] — floating-point format with wider range.
- [[FP8]] — low-precision floating-point format.
