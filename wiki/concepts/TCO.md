---
title: "Total Cost of Ownership"
type: concept
tags:
  - AIInfrastructure
  - Capex
  - Opex
  - ComputeEconomics
last_updated: 2026-05-03
sources:
  - groq-inference-tokenomics-speed-but-at-what-cost
---

## Definition
[[TCO]] (total cost of ownership) is the full economic metric for AI inference infrastructure, including capital expenditure, operating expenditure, system integration cost, utilization, and workload behavior.

## Formula used in source
The source emphasizes an explicit performance-over-cost framing:

**performance / TCO**

Notably, this is applied at the deployment layer rather than only chip spec level.

## Components
- **CAPEX**: hardware, packaging, networking, racks, and platform-level components.
- **OPEX**: power, maintenance, and operational overhead.
- **Utilization**: batch size and concurrency shape actual unit economics.
- **Vendor costs and margins**: includes ODM/OEM margins and service-level markups.
- **Model serving mode**: latency-optimized vs throughput-optimized pathways.

## Source-specific implications
- Inference comparisons that omit power and margin can invert conclusions.
- GPU systems with higher apparent BOM can still win when throughput and utilization are high.
- Low-latency single-stream winners may lose under throughput-scale economic assumptions.

## Related links
- [[AIInfrastructure]]
- [[InferenceOptimization]]
- [[Tokenomics]]
- [[LatencyOrientedInference]]
- [[ThroughputOrientedInference]]
- [[EdgeInference]]