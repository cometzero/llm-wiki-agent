---
title: "Discrete Diffusion"
type: concept
tags: [diffusion, discrete-tokens, trajectory-generation]
sources: [reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-13
---

## Overview
Discrete diffusion는 연속적 noise를 추가하는 표준 diffusion과 달리, discrete token 시퀀스에 masked noise를 적용하고 역순으로 복원하는 생성 모델링 기법이다.

## Application in ReflectDrive-2
- BEV trajectory를 discrete token 시퀀스로 변환
- Masked discrete diffusion을 통해 trajectory draft 생성
- 병렬 unmasking으로 빠른 draft generation 가능
- Shared-prefix KV reuse, ASD, fused CUDA unmasking으로 latency 최적화

## Advantages
- Autoregressive generation 대비 병렬 처리 가능
- Token-space generation으로 action grounding 용이
- In-place editing과 호환

## Connections
- [[ReflectDrive2]] — 사용처
- [[MaskedDiffusion]] — related technique
- [[DiscreteToken]] — representation
