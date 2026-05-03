---
title: "VeraRubinNVL72"
type: entity
tags: [NVIDIA, VeraRubinPlatform, RackScale, NVLink6, HeterogeneousInference]
sources: [nvidia-interview-groq-3-lpx-with-vera-rubin-ai-deep-analysis-gtc-2026]
last_updated: 2026-05-03
---

[[VeraRubinNVL72]] is the rack-scale successor to [[Blackwell]] GB200 NVL72 as described in the GTC 2026 interview source. The corpus presents it as the high-throughput side of a heterogeneous serving stack: it handles prefill, attention, and intent processing while [[Groq3LPX]] handles decode-side FFN work.

## Key Characteristics
- Contains 72 [[VeraRubinPlatform|Rubin GPUs]] and 36 [[Vera CPU]]s per rack.
- Uses [[NVLink6]] to connect all GPUs with roughly 3.6 TB/s of scale-up bandwidth.
- Organizes each rack into 18 compute trays, with 4 GPUs and 2 CPUs per tray.
- Uses a modular, cable-free tray design to reduce assembly time and failure points.

## Connections
- [[VeraRubinPlatform]] — GPU side of the rack-scale architecture.
- [[Groq3LPX]] — decode-side heterogeneous partner.
- [[NVIDIA]] — platform owner.
- [[HeterogeneousInference]] — architectural pattern the rack enables.
- [[ModularDesign]] — manufacturing simplification principle.
