---
title: "ReflectDrive-2"
type: entity
tags: [autonomous-driving, VLA, research-project]
sources: [reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-13
---

## Overview
ReflectDrive-2는 자율주행 VLA planner에서 trajectory를 discrete token으로 만들고, masked diffusion draft와 AutoEdit rewrite를 RL terminal reward로 함께 정렬하는 Decision-Draft-Reflect 아키텍처를 제안하는 연구이다.

## Key Components
- **Goal Posterior**: behavior hypothesis 선택 모듈
- **Masked Discrete Diffusion**: BEV trajectory tokens에 대한 병렬 unmasking으로 4초 trajectory draft 생성
- **AutoEdit**: token-to-token rewrite를 통한 drivable/safe/reward-aligned correction
- **RL Fine-tuning**: draft-and-edit composed rollout 전체에 closed-loop PDMS reward 적용

## Performance
- NAVSIM 91.0 PDMS (camera-only)
- Best-of-6: 94.8 PDMS
- NVIDIA Thor ~30ms latency

## Connections
- [[DecisionDraftReflectPipeline]] — architectural pattern
- [[VLA]] — foundation model type
- [[NAVSIM]] — benchmark
- [[NVIDIAThor]] — deployment hardware
