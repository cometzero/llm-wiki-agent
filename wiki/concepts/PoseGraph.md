---
title: "PoseGraph"
type: concept
tags:
  - navigation-graph
  - localization
  - route-planning
  - urban-navigation
date: 2026-08-19
sources:
  - 360cityarena-2608-08814-learning
last_updated: 2026-08-19
---

## PoseGraph

## Definition
[[PoseGraph]]는 장소/시점(node)과 이동 transition(edge)로 도시 탐색 상태를 근사한 그래프이다.

### In this source
[[360CityArena]]는 360° node 중심 pose graph(예: 193 node, 305 edge)로 도시 경로를 구성해 탐색 길항을 측정한다.

### Risks
- node/edge 연결성만으로는 물리 제약(속도, 동역학, 충돌)을 전부 반영하지 못한다.
- landmark 정합과 heading 정렬 실패가 큰 성능 하락 요인이 된다.