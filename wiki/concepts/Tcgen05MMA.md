---
title: "Tcgen05MMA"
type: concept
tags: [Blackwell, PTX, TensorCores, MMA]
sources: [2512-02189, nvidia-tensor-core-evolution-from-volta-to-blackwell]
last_updated: 2026-05-03
---

## Summary
[[Tcgen05MMA]] is the Blackwell-era tensor core PTX instruction family exposed through [[tcgen05.mma]]. The corpus treats it as the software-visible surface for 5th-generation tensor core execution.

## Key Claims
- tcgen05.mma enables more fine-grained tensor dispatch than earlier warp-group style execution.
- It maps to different SASS operations depending on precision and operand configuration.
- It is central to the measurement of single-instruction latency and throughput in Blackwell.

## Connections
- [[Blackwell]] — the architecture that introduces it.
- [[TensorCores]] — the compute hardware it drives.
- [[PTX]] — the ISA layer where it appears.
- [[SASS]] — the lower-level machine code mapping.

## Contradictions
- None identified.
