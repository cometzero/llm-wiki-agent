---
title: "Block Diffusion Decoding"
type: concept
tags: [diffusion, decoding, vla]
sources: [tbd-vla-2606-07895-references]
last_updated: 2026-06-10
---

## Definition
블록 단위로 diffusion decoding을 수행하는 방식. Token compression 대신 사용.

## Key Points
- Token을 개별적으로 처리하지 않고 블록 단위로 처리
- 병렬 처리 가능으로 latency 감소
- [[FAST]]의 token compression과 대조적 접근

## Related Concepts
- [[DiscreteDiffusion]]
- [[TemporalBlock]]
- [[Latency]]
