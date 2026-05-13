---
title: "Decision-Draft-Reflect Pipeline"
type: concept
tags: [VLA, autonomous-driving, architecture, diffusion]
sources: [reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-13
---

## Overview
Decision-Draft-Reflect는 VLA planner에서 trajectory를 생성하고 수정하는 3단계 파이프라인이다.

## Stages

### 1. Decision (Goal Posterior)
Visual + route instruction + ego state를 입력으로 behavior hypothesis를 샘플링한다.

### 2. Draft (Masked Discrete Diffusion)
BEV trajectory tokens에 대해 병렬 masked unmasking을 수행해 4초 trajectory draft를 생성한다.

### 3. Reflect (AutoEdit)
Draft trajectory tokens를 입력으로 token-to-token rewrite를 수행해 drivable area, safety, reward alignment를 개선한다.

## Key Innovation
기존 planner와 달리 "고칠 수 있는 계획"을 생성한다. 자율주행 error가 longitudinal/lateral 축으로 구조화되어 나타나는 특성에 맞춰, structure-aware perturbation을 사용한 supervision이 적용된다.

## Connections
- [[ReflectDrive2]] — concrete implementation
- [[VLA]] — foundation model type
- [[DiscreteDiffusion]] — draft generation method
- [[AutoEdit]] — reflection/correction method
- [[ClosedLoopReward]] — training objective
