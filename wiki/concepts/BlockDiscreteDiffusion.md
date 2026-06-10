---
title: "Block Discrete Diffusion"
type: concept
tags: [diffusion, discrete, block-parallel, vla, latency]
sources: [tbd-vla-2606-07895-analysis, reflectdrive-2-2605-04647]
last_updated: 2026-06-10
---

## Overview
Block Discrete Diffusion은 discrete action token sequence를 block 단위로 병렬 생성하는 diffusion 기법이다. 각 block 내부에서는 masked discrete diffusion으로 병렬 복원하며, block 간에는 autoregressive dependency를 유지하여 temporal coherence를 보존한다.

## Key Mechanism
1. **Block Partitioning**: 긴 action sequence를 temporal block으로 분할
2. **Intra-block Parallelism**: block 내부 masked token을 병렬로 복원
3. **Inter-block Autoregression**: 이전 block을 조건으로 다음 block 생성
4. **Token Shift**: diffusion objective를 next-token prediction과 정렬

## Advantages
- Pure parallel decoding보다 temporal coherence 우수
- Token-by-token AR보다 latency 낮음
- VLM backbone의 pretraining objective와 정렬 가능

## Related Concepts
- [[TemporalBlockDiffusion]] — 시간적 의존성을 다루는 방식
- [[DiscreteDiffusion]] — 이산 공간에서의 diffusion
- [[MaskedDiffusion]] — masked token 복원 기반 diffusion
- [[TBDVLA]] — Block Discrete Diffusion을 사용하는 VLA framework
- [[ReflectDrive2]] — autonomous driving에서의 discrete diffusion应用

## Applications
- Robot action generation (TBD-VLA)
- Autonomous driving trajectory planning (ReflectDrive2)
- Future waypoint/token generation
