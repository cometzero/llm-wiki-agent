---
title: "Temporal AR"
type: concept
tags: [autoregression, temporal-modeling, vla]
sources: [tbd-vla-2606-07895, tbd-vla-2606-07895-learning]
last_updated: 2026-06-10
---

## Definition

Temporal AR(Temporal Autoregression)은 [[VLA]] policy에서 시간적으로 연속된 action block 사이의 의존성을 모델링하는 구조이다. 각 block `k`는 이전 block들 `0..k-1`에 조건화되어 순차적으로 생성된다.

## Contrast with Pure AR

기존 pure autoregressive model:
- 각 timestep token을 순차적으로 생성
- 높은 temporal coherence, 높은 latency

Temporal AR:
- Block 내부는 병렬 [[BlockDiffusion]] 디노이징
- Block 사이만 순차 조건화
- coherence와 latency의 균형 달성

## Mathematical Foundation

```text
p(a_1:H | o,g) = Π_k pθ(block_k | o,g, block_<k)
```

각 block의 조건부 분해로 효율성과 품질을 동시에 확보.

## Related Concepts

- [[BlockDiffusion]] — block 내 병렬 처리
- [[RTCRealTimeChunking]] — 실시간 chunk 갱신
- [[DiscreteDiffusion]] — discrete token 기반 처리

## Applications

- [[TBDVLA]] — temporal block diffusion VLA
- [[ReflectDrive-2]] — autonomous driving trajectory planning

## Connections

- [[VLAPolicy]] — 적용 정책 구조
- [[ClosedLoopLatency]] — temporal modeling과 latency 관계
