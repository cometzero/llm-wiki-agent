---
title: "Discrete VLA Latency"
type: concept
tags: [latency, discrete, vla, action-token, inference]
sources: [tbd-vla-2606-07895-analysis, visualthink-vla-2605-30011]
last_updated: 2026-06-10
---

## Overview
Discrete VLA Latency는 VLM(Vision Language Model)이 action token을 순차적으로 생성할 때 발생하는 inference latency 문제를 의미한다. Token-by-token autoregressive generation은 높은 interpretability를 제공하지만, 실시간 robot control에 필요한 low-latency 요구를 충족하기 어렵다는 근본적 trade-off가 있다.

## The Bottleneck
1. **Token-by-token Generation**: 각 action token이 이전 token에 종속
2. **Sequential Decoding**: parallel computation 불가
3. **Cumulative Latency**: 긴 action sequence 생성 시 지연累積
4. **Control Frequency**: closed-loop control에 필요한 high-frequency update 곤란

## Solutions
1. **Block Discrete Diffusion** (TBD-VLA):
   - Block 내 병렬 생성으로 intra-block latency 감소
   - Block 간 AR로 temporal consistency 유지
   - 최종 inference: 0.086s 달성

2. **Visual Intermediate Reasoning** (VisualThink-VLA):
   - Visual evidence states로 textual CoT 대체
   - 22.8× speedup (8.377s → 0.367s)

3. **Parallel Decoding Methods** (OpenVLA-OFT):
   - 극단적 병렬 처리
   - 단, temporal coherence牺牲 가능성

## Performance Comparison

| Method | Latency | Approach |
|---|---|---|
| TBD-VLA (final) | 0.086s | Block diffusion + AR block |
| VisualThink-VLA | 0.367s | Visual intermediate reasoning |
| Textual CoT | 8.377s | Standard textual chain-of-thought |

## Related Concepts
- [[TBDVLA]] — Block diffusion으로 latency 해결
- [[VisualThinkVLA]] — Visual reasoning으로 latency 감소
- [[VisionLanguageAction]] — discrete VLA 일반 개념
- [[InferenceOptimization]] — latency 최적화 기법
