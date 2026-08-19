---
title: "Urban Navigation References"
type: concept
tags: [navigation, benchmark, embodied-ai, references]
last_updated: 2026-08-19
---

도시 내비게이션 관련 연구 계열의 reference 집합은 `vision-language navigation`, `trajectory-bound benchmark`, `map/text grounding`, `simulation realism`을 하나의 reading map으로 연결해 성능 병목의 층위를 분리해 본다.

현재 기준에서 [[360CityArena]] 레퍼런스 맵은 다음 축을 묶는다.
- outdoor street navigation: [[StreetLearn]], [[TOUCHDOWN]], [[SidewalkBench]]
- reconstruction 기반 시뮬레이션: [[Vid2Sim]], [[EmbodiedCity]], [[CARLA]]
- map representation: [[Tag Map]]
- embodied/route reasoning: [[360CityArena]]

이 개념은 베이스라인을 나열하는 수준이 아니라, 어떤 벤치마크가 `perception`, `memory`, `route planning`, `action grounding`의 어느 부분을 고정적으로 드러내는지 정렬하는 데 사용된다.