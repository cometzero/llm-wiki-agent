---
title: "Fixed Point"
type: concept
tags: [Numerics, Quantization, Scaling]
sources: [neural-network-quantization-number-formats-from-first-principles]
last_updated: 2026-05-03
---

[[FixedPoint]] represents values as integers plus an implicit scale factor. It is simple to implement and can be efficient, but it struggles when values span a wide dynamic range because the scale is shared across the represented set.

In the source, fixed point is used as a conceptual bridge from integers to more flexible numeric representations. It is also a reminder that many practical reduced-precision schemes are just integers with carefully chosen scaling conventions.

## Connections
- [[NumberFormat]] — broader representation category.
- [[INT8]] — integer base that often underlies fixed-point schemes.
- [[FloatingPoint]] — more flexible alternative for large dynamic ranges.
