---
title: "TBD-VLA"
type: concept
tags: [VLA, block-diffusion, temporal-modeling, discrete-diffusion]
sources: [tbd-vla-2606-07895]
last_updated: 2026-06-10
---

## Overview
**Temporal Block Diffusion Vision Language Action Model (TBD-VLA)**는 discrete token 기반 VLA에서 block discrete diffusion을 통해 temporal action generation을 수행하는 framework다. Action sequence를 temporal block으로 나누어 block 내부에서는 masked discrete diffusion으로 병렬 denoising을, block 사이에서는 autoregressive generation을 수행한다.

## Core Innovation
1. **Temporal Block Factorization**: action sequence를 K개 block으로 나누어 병렬+순차 hybrid generation
2. **Temporal-level Token Shift**: VLM의 AR 성질과 diffusion objective 정렬
3. **Block-level Attention Masking**: future block 정보 누출 방지
4. **Real-Time Chunking (RTC)**: 실행 중인 prefix 유지하며 미래 block만 재생성

## Architecture
- **Backbone**: [[Qwen3-VL]] 2B
- **Action Representation**: discretized action tokens (proprioception과 동일한 dictionary)
- **Prompt Format**: `State: {state}, Task: {instruction}, Actions: {placeholders}`

## Performance
| Metric | Value |
|--------|-------|
| Latency | 0.086s (with all optimizations) |
| SimplerEnv Success | 88.7% |
| Real-World Success | 67.1% (with RTC) |

## Connections
- Extends [[VisionLanguageAction]] with temporal block diffusion
- Enables [[RealTimeChunking]] via temporal in-painting
- Competes with [[OpenVLA]], [[π0.5]], [[GR00T-N1]]
