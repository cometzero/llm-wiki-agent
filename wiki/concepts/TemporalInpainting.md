---
title: "Temporal In-painting"
type: concept
tags: [temporal-modeling, inpainting, autoregressive]
sources: [tbd-vla-2606-07895]
last_updated: 2026-06-10
---

## Overview
**Temporal In-painting**은 [[TBD-VLA]]에서 사용하는 개념으로, 실행 중인 action prefix 이후의 future block을 채우는 메커니즘이다. 이는 이미지 인페인팅에서 마스킹된 영역을 주변 정보로 채우는 것과 유사하게, 시간 축에서 미래 timesteps를 이전 context로 생성한다.

## Application in TBD-VLA
- [[Real-Time Chunking]]의 핵심 동작 원리
- 실행된 action block들을 조건으로 사용하여 미래 block 재생성
- perturbation 대응이나 plan 수정에 활용

## Connections
- Enabled by [[TBD-VLA]]'s block-level discrete diffusion
- Similar concept to spatial in-painting in image generation
- Related to [[AutoregressiveGeneration]] and [[TemporalModeling]]
