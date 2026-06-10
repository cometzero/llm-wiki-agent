---
title: "Multi-View Consistency"
type: concept
tags: [computer-vision, generation]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Multi-View Consistency

Multiple camera view에서 geometry와 appearance의 일관성 유지. Autonomous driving simulation의 핵심 요구사항.

## Overview
OmniDreams는 multi-view video generation을 지원하며, 4-camera scenario에서 105 FPS를 달성한다. Attention factorization으로 camera 간 consistency를 확보.

## Key Requirements
- Geometry consistency:同一 object가 여러 view에서 일관된 위치/형태
- Appearance consistency: Lighting, color, texture의 일관성
- Temporal consistency: Timestep 간 camera pose 변화 일관성

## Solutions in OmniDreams
- **Attention Factorization**: Cross-view attention을 분리하여 효율적 consistency modeling
- **World-Scenario Map**: Structural prior로 geometric consistency 보장

## Connections
- [[OmniDreams]] — 핵심 기능
- [[WorldScenarioMap]] — consistency 지원
- [[AttentionFactorization]] — 구현 기법
