---
title: "Trajectory-Bound Benchmark"
type: concept
tags: [benchmark, urban-navigation, embodiment]
last_updated: 2026-08-19
---

Trajectory-bound benchmark는 에이전트가 연속 영상(trajectory) 구간 내에서 관측을 갱신하며 탐색·추론을 수행하도록 설계된 평가 체계이다.

[[360CityArena]]는 trajectory-bound 특성을 갖고 있으며, 정적 장면의 단일 뷰 기반 벤치마크보다 `route continuity`, `spatial context retention`, `dynamic observation` 측면에서 다른 성능 병목을 보인다.

주요 비교 대상:
- [[StreetLearn]] (일부 static/discrete panorama 스타일 요소)
- [[CARLA]] (free-moving 물리 시뮬레이션)
- [[Visual Navigation]](trajectory continuity가 다른 방식으로 구현되는 계열)
