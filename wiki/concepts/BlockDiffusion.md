---
title: "Block Diffusion"
type: concept
tags: [diffusion, vla, temporal-modeling]
sources: [tbd-vla-2606-07895, tbd-vla-2606-07895-learning]
last_updated: 2026-06-10
---

## Definition

Block Diffusion은 [[VLA]] policy에서 action sequence를 시간 단위의 block으로 나누어 처리하는 diffusion 기법이다. 각 block 내부 token을 mask한 후 병렬로 복원하며, block 사이의 의존성은 순차적으로 처리한다.

## Key Properties

- **병렬 디노이징**: block 내부 token은 mask되어 병렬로 예측
- **순차 조건화**: 각 block은 이전 block들에 조건화됨
- **Latency-Quality 트레이드오프**: block size `m`이 주요 hyperparameter
  - `m=1`: 강한 temporal modeling, 높은 latency
  - `m=H`: 빠른 처리, 약한 temporal dependency

## Mathematical Formulation

```text
p(a_1:H | o,g) = Π_k pθ(block_k | o,g, block_<k)
```

where `block_k` depends on previous blocks `block_<k`.

## Related Concepts

- [[DiscreteDiffusion]] — discrete token 기반 diffusion
- [[TemporalAR]] — 시간적 자기회귀 구조
- [[RTCRealTimeChunking]] — 실행 중 chunk 갱신 메커니즘
- [[ActionTokenization]] — continuous action의 token 변환

## Applications

- [[TBDVLA]] — temporal block diffusion VLA
- [[ReflectDrive-2]] — 자율주행 trajectory planning
- [[FastDVLA]] — 저지연 VLA inference

## Connections

- [[VLAPolicy]] — 적용되는 policy 구조
- [[ClosedLoopLatency]] — block size에 의해 결정되는 latency
