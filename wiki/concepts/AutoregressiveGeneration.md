---
title: "Autoregressive Generation (AR Generation)"
type: concept
tags: [generation, autoregressive, video]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Autoregressive Generation (AR Generation)

과거 예측값을 조건으로 다음 timestep을 예측하는 생성 패러다임. Video generation과 world model에서 널리 사용.

## Overview
Autoregressive generation은 sequential prediction을 통해 temporal coherence를 확보하지만, [[Exposure Bias]]와 [[Rollout Drift]] 문제가 있다. OmniDreams는 [[Diffusion Forcing]]을 통해这些问题를 완화한다.

## Key Properties
- Sequential prediction: timestep-by-timestep generation
- Temporal coherence: 과거 context 활용
- Conditional generation: action/state에 조건화

## In OmniDreams
- Action-conditioned video generation
- Causal masking + rolling KV cache
- Real-time inference (68-105 FPS)

## Connections
- [[OmniDreams]] — 적용 사례
- [[DiffusionForcing]] — 개선 기법
- [[ExposureBias]] — 문제점
- [[RolloutDrift]] — 장기 문제
