---
title: "E2E Autonomous Driving"
type: concept
tags: [autonomous-driving, end-to-end, deep-learning]
sources: [reflectdrive-2-2605-04647-references, reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-13
---

## Overview
End-to-End Autonomous Driving(E2E AD)는 perception-prediction-planning을 단일 신경망으로 통합하는 패러다임이다. [[UniAD]], [[TransFuser]] 등初期 연구에서 [[NAVSIM]] 등 벤치마크를 통해 평가되며, [[ReflectDrive-2]]는 discrete diffusion 기반 VLA로 E2E planning의 새로운 접근법을 제시한다.

## Key Approaches
- Unified query-based architecture (UniAD)
- Multi-modal sensor fusion (TransFuser)
- Diffusion-based trajectory generation (ReflectDrive-2)

## Connections
- [[ReflectDrive-2]] — diffusion-based E2E planner
- [[UniAD]] — unified E2E baseline
- [[TransFuser]] — fusion-based E2E planner
- [[NAVSIM]] — evaluation benchmark
- [[VLA]] — model architecture category

## Contradictions
- None identified.
