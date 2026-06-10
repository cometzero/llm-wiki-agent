---
title: "SimplerEnv"
type: entity
tags: [robotics, simulation, benchmark, widow-x, google-robot]
sources: [tbd-vla-2606-07895-analysis, physbrain-1-0-2605-15298]
last_updated: 2026-06-10
---

## Overview
SimplerEnv는 VLA(Vision-Language-Action) 모델의 manipulation 성능을 평가하기 위한robot simulation 환경이다. Widow-X 및 Google Robot 환경을 지원하며, TBD-VLA의 주요 평가 벤치마크로 사용된다.

## Evaluation Results (TBD-VLA)
- **Google Robot environment**: 88.7% success rate
- **Latency**: 0.086s inference time
- **Comparison**: discrete VLA baseline 대비 superior performance

## Related Concepts
- [[LIBERO]] — 또 다른 robot manipulation benchmark
- [[BlockDiscreteDiffusion]] — TBD-VLA의 핵심 기술
- [[RealTimeChunking]] — TBD-VLA의 closed-loop control 지원

## References
- TBD-VLA evaluation environment
- PhysBrain 1.0에서도 언급된 평가 환경
