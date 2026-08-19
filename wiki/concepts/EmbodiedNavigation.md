---
title: "Embodied Navigation"
type: concept
tags:
  - embodied-ai
  - navigation
  - spatial-reasoning
sources:
  - 360cityarena-embodied-agent-urban-navigation-benchmark
last_updated: 2026-08-19
---

[[EmbodiedNavigation]]는 에이전트가 관측, 기억, 계획, 행동을 이용해 물리적 또는 준물리적 환경을 탐색하는 문제 영역이다. [[360CityArena]] 같은 benchmark는 도시 규모의 photorealistic 환경에서 이 능력을 평가한다.

핵심 병목은 위치 추정, landmark grounding, path reasoning, 그리고 실제 행동까지 이어지는 폐쇄루프 정합이다.

## Connections
- [[360CityArena]] — 도시 내비게이션 benchmark
- [[SpatialReasoning]] — 공간 관계 추론 능력
- [[ClosedLoopEvaluation]] — 관측-계획-행동 loop 평가