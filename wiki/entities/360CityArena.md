---
title: "360CityArena"
type: entity
tags:
  - benchmark
  - embodied-navigation
  - urban
  - vla
  - autonomous-driving
sources:
  - 360cityarena-2608-08814-analysis
  - 360cityarena-2608-08814-references
  - 360cityarena-2608-08814-learning
last_updated: 2026-08-19
---

# 360CityArena

## What it is
[[360CityArena]]는 Tokyo [[Akihabara]] 기반의 360° 비디오 도시 환경에서 photorealistic trajectory traversal을 구성한 embodied navigation benchmark이다.

## Scope
- environment 이해: [[Localization]], [[Landmark]] grounding, observation parsing
- path planning: route selection, turn decision, progress tracking
- spatial reasoning: relation, counting, semantic retrieval

## Core model
본 benchmark는 open/closed loop의 구분에서 특히 `observation-memory-action` 반복 과정을 검증한다.

## Importance
- AD/로보틱스 연구에서 full-physical simulator와 분리된, city-scale visual reasoning 병목 진단 기준으로 활용된다.
- 특히 [[Map navigation]]에서의 취약성이 `spatial cognition` 및 `route interface`의 한계를 명시한다.

## Contradictions / caveats
- 차량 동적 제어, 충돌/안전 제약, 법규 준수 항목이 중심 평가지표는 아니다.
- free 3D simulation보다 관측 시퀀스 기반 realism stress test에 가깝다.

## See also
- [[EmbodiedNavigation]]
- [[PoseGraph]]
- [[AutonomousDrivingVLA]]
- [[Vision-Language Navigation (VLN)]]
