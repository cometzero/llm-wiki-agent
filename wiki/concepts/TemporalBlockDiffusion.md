---
title: "Temporal Block Diffusion"
type: concept
tags: [diffusion, temporal, block, coherence, vla]
sources: [tbd-vla-2606-07895-analysis]
last_updated: 2026-06-10
---

## Overview
Temporal Block Diffusion은 VLA(Vision-Language-Action) 모델에서 시간적으로 상관된 action sequence를 생성하기 위한 diffusion 기법이다. Action trajectory를 시간 순서의 block으로 나누어 각 block을 독립적으로 병렬 생성하면서도 block 간의 시간적 일관성을 유지한다.

## Core Idea
1. **Temporal Partitioning**: 긴 trajectory를 temporal block으로 분할
2. **Block-level Generation**: 각 block을 병렬로 생성
3. **Temporal Autoregression**: 이전 block을 조건으로 사용
4. **Coherence Preservation**: 순수 병렬 diffusion보다 temporal consistency 향상

## Difference from Standard Block Diffusion
- Block Discrete Diffusion과의 차이: temporal dependency를 명시적으로 모델링
- 시간 흐름에 따른 action의 순차적 의존성 고려
- robot control에서 물리적 일관성 보장

## Related Concepts
- [[BlockDiscreteDiffusion]] — 구현 기법
- [[RealTimeChunking]] — 실행 중 block 갱신
- [[TBDVLA]] — 핵심 적용 사례
- [[TemporalReasoning]] — 시간적 추론 일반 개념

## Applications
- Robot manipulation task execution
- Closed-loop control with temporal consistency
- Future action chunk generation
