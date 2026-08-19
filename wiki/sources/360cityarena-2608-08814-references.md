---
title: "360CityArena 참고 문헌과 urban navigation 연결 고리"
type: source
tags:
  - urban-navigation
  - benchmark
  - embodied-ai
  - references
  - visual-language-navigation
  - autonomous-driving
  - spatial-reasoning
date: 2026-08-19
source_url: https://arxiv.org/html/2608.08814
hf_url: https://huggingface.co/papers/2608.08814
arxiv_id: "2608.08814"
arxiv_url: https://arxiv.org/abs/2608.08814
pdf_url: https://arxiv.org/pdf/2608.08814
week: "2026-W33"
ingested_at_kst: "2026-08-19 09:40:35 KST"
selected_reason: "360CityArena의 실험 맥락을 강화하는 계보 정리로, realistic-urban navigation, map/path grounding, trajectory-bound benchmark, VLA/AD 비교축을 함께 정렬한다."
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W33/360cityarena-urban-navigation-2608-08814/references.md
source_hash: a9bd8f689aeca778
---

# 360CityArena 참고 레퍼런스

> 아래 목록은 `Semantic Scholar arXiv:2608.08814/references` 응답과 논문 bibliography에서 핵심 계보를 추린 항목이다.

## 1. Realistic Virtual World — 360CityArena의 기반

- **Takenawa et al. (2025), _Building and Evaluating a Realistic Virtual World for Large Scale Urban Exploration from 360° Videos_.**
- arXiv: https://arxiv.org/abs/2510.11447
- 360° 비디오를 대규모 도시 탐색 시뮬레이션에 재구성한 기반으로, [[360CityArena]]는 이를 Akihabara reconstruction 위에 구축한 과제·경로 진단 설계로 읽을 수 있다.

## 2. SidewalkBench — Urban visual navigation의 인접 benchmark

- **Liu et al. (2026), _SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks_.**
- arXiv: https://arxiv.org/abs/2606.16953
- Sidewalk-level 보행 환경과 pedestrian behavior를 다루며, [[360CityArena]]는 언어/이미지 goal, map path, relation, count를 통합한 도시 탐색 진단으로 이를 보완한다.

## 3. Vid2Sim — video-to-simulator 계보

- **_Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation_ (2025).**
- arXiv: https://arxiv.org/abs/2501.06693
- 실제 영상으로부터 navigation simulation을 만들고, [[360CityArena]]가 도시 구간 연속 탐색(trajectory chain)에서 real-world 동학을 일부 보존하려는 흐름의 선행으로 읽힌다.

## 4. EmbodiedCity — 실제 도시 embodied benchmark

- **Gao et al. (2024), _EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-World City Environment_.**
- arXiv: https://arxiv.org/abs/2410.09604
- real-world city의 embodied benchmark로서 [[360CityArena]]의 photorealism vs interactivity trade-off를 정량 비교할 때 중요한 비교군.

## 5. TOUCHDOWN — street-view VLN와 spatial reasoning

- **Chen et al. (2019), _TOUCHDOWN: Natural Language Navigation and Spatial Reasoning in Visual Street Environments_.**
- arXiv: https://arxiv.org/abs/1811.12354
- [[Vision-Language Navigation (VLN)]] 계보의 고전 baseline으로, outdoor street navigation의 instruction following과 spatial inference 축을 형성한다.

## 6. StreetLearn — city navigation from Street View

- **Mirowski et al. (2019), _Learning to Navigate in Cities Without a Map_.**
- arXiv: https://arxiv.org/abs/1804.00168
- 기존 [[StreetLearn]] 계열은 static/discrete panorama 중심이라면, [[360CityArena]]는 연결 도시를 촬영 동적 시퀀스로 확장해 route complexity를 강화한다.

## 7. CityNav — aerial navigation의 보완 축

- **_CityNav: A Large-Scale Dataset for Real-World Aerial Navigation_ (2024).**
- arXiv: https://arxiv.org/abs/2406.14240
- 항공 시점(large-scale aerial) 대비, [[360CityArena]]는 ground-level의 long-horizon egocentric urban traversal을 다룬다.

## 8. Tag Map — LLM planning을 위한 map grounding

- **_Tag Map: A Text-Based Map for Spatial Reasoning and Navigation with Large Language Models_ (2024).**
- arXiv: https://arxiv.org/abs/2409.15451
- text map + LLM planning의 대표 계보로, [[SpatialReasoning]]에서 map representation이 반드시 성능 보장을 주지 않음을 보여 주며 [[360CityArena]]의 현재 location grounding 한계와 맞닿는다.

## 9. RT-2 — VLA action grounding의 기준점

- **Brohan et al. (2023), _RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control_.**
- arXiv: https://arxiv.org/abs/2307.15818
- robot action token으로의 지식 transfer 기반의 대표 VLA 축으로, 360° city benchmark는 저수준 제어보다 [[SpatialReasoning]]/route planning stress-testing 관점에서 어떻게 VLA가 확장되는지 보여 준다.

## 10. CARLA — 자율주행 simulation 비교 기준

- **Dosovitskiy et al. (2017), _CARLA: An Open Urban Driving Simulator_.**
- arXiv: https://arxiv.org/abs/1711.03938
- 센서·vehicle dynamics·interaction 중심의 AD 시뮬레이터인 [[CARLA]]와 달리, [[360CityArena]]는 현실형 360° 도시 시각 경험으로 route/spatial reasoning을 집중 stress-test한다.

## 읽는 순서

1. [[StreetLearn]]·TOUCHDOWN으로 outdoor/VLN 기반을 이해한다.
2. [[Vid2Sim]], [[Realistic Virtual World|Takenawa et al. (2025)]], [[EmbodiedCity]]로 realism/interactive realism trade-off를 비교한다.
- [[TagMap|Tag Map]]로 map-text grounding framing을 검토한다.
4. [[RT-2]]와 [[CARLA]]를 기준으로, 360CityArena가 VLA/AD 스택의 어느 레이어를 진단하는지 정리한다.

## Connections

- [[360CityArena]] — 본 연구의 상위 레퍼런스 map
- [[EmbodiedNavigation]] — 거리 기반 탐색 및 경로 추론 문제의 공통 실험 대상
- [[StreetLearn]] / [[Vision-Language Navigation (VLN)]] — outdoor VLN 계보
- [[TagMap|Tag Map]] / [[SpatialReasoning]] — map 표현과 공간 추론 연결
- [[RT-2]] — VLA 관점의 action grounding 전사
- [[CARLA]] — 물리 기반 AD 시뮬레이터 비교군

## Contradictions

- [[CARLA]] 계열이 물리·vehicle-level 인터랙션을 강조하는 것과 달리, [[360CityArena]]는 trajectory-bound 360° city observation을 우선시한다는 점에서 시뮬레이션 포인트가 다르다.
- Static panorama형 street navigation의 접근과 달리, 이 소스는 긴 동선/연속 관측을 통해 dynamic 연결성을 중시한다고 본다.
