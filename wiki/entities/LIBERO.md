---
title: "LIBERO"
type: entity
tags: [robotics, benchmark, simulation, task-suite]
sources: [tbd-vla-2606-07895-analysis, physbrain-1-0-2605-15298]
last_updated: 2026-06-10
---

## Overview
LIBERO는 다중 task suite와 perturbation을 포함한 robot manipulation benchmark이다. SimplerEnv와 함께 TBD-VLA의 주요 평가 환경으로 사용된다.

## Variants
- **LIBERO**: 기본 task suite
- **LIBERO-Plus**: perturbation을 포함한 확장 버전

## Evaluation Role in TBD-VLA
Multiple task suite에서 strong performance를 보여주며, discrete VLA baseline과 비교하여 temporal coherence와 low-latency의 이점을 실증한다.

## Related Concepts
- [[SimplerEnv]] — 또 다른 평가 환경
- [[BlockDiscreteDiffusion]] — TBD-VLA 기술
- [[VisionLanguageAction]] — 평가 대상 VLA 모델
