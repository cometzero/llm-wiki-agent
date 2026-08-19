---
title: "360CityArena 참고 문헌과 urban navigation 연결 고리"
document_type: references
source_url: https://arxiv.org/html/2608.08814
hf_url: https://huggingface.co/papers/2608.08814
arxiv_id: "2608.08814"
arxiv_url: https://arxiv.org/abs/2608.08814
pdf_url: https://arxiv.org/pdf/2608.08814
week: "2026-W33"
ingested_at_kst: "2026-08-19 09:40:35 KST"
selected_reason: "photorealistic urban navigation, map grounding, embodied benchmark, VLA 연결을 위한 핵심 선행 연구를 정리한다."
---

# 360CityArena 참고 레퍼런스

> 아래 목록은 Semantic Scholar `ARXIV:2608.08814/references` 응답과 논문 bibliography에서 중요한 항목을 골랐다.

## 1. Realistic Virtual World — 360CityArena의 기반 환경

- **Takenawa et al. (2025), _Building and Evaluating a Realistic Virtual World for Large Scale Urban Exploration from 360° Videos_.**
- arXiv: https://arxiv.org/abs/2510.11447
- 360° video collection을 large-scale urban exploration용 virtual world로 연결한다. 360CityArena는 이 RVW의 Akihabara reconstruction 위에 task taxonomy와 benchmark protocol을 올린다.

## 2. SidewalkBench — urban visual navigation의 인접 benchmark

- **Liu et al. (2026), _SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks_.**
- arXiv: https://arxiv.org/abs/2606.16953
- sidewalk의 complex structure와 pedestrian behavior를 다룬다. 360CityArena는 이를 보완해 language/image goal, map path, relation, count까지 포함하는 도시 탐색 진단을 제공한다.

## 3. Vid2Sim — video-to-simulator 계보

- **_Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation_ (2025).**
- arXiv: https://arxiv.org/abs/2501.06693
- 실제 video를 navigation simulation으로 전환하는 접근이다. 360CityArena는 단일/짧은 clip 대신 연결된 360° trajectory로 district-scale exploration을 지향한다.

## 4. EmbodiedCity — 실제 도시 embodied benchmark

- **Gao et al. (2024), _EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-World City Environment_.**
- arXiv: https://arxiv.org/abs/2410.09604
- real-world city setting의 embodied agent benchmark다. 360CityArena의 비교 표에서 3D simulator 기반 photorealism/structural complexity trade-off를 보여 주는 핵심 비교군이다.

## 5. TOUCHDOWN — street-view VLN과 spatial reasoning

- **Chen et al. (2019), _TOUCHDOWN: Natural Language Navigation and Spatial Reasoning in Visual Street Environments_.**
- arXiv: https://arxiv.org/abs/1811.12354
- 자연어 instruction을 따라 street environment에서 이동하는 VLN setting을 만들었다. 360CityArena의 VLN은 이 계보를 photorealistic dynamic 도시 graph에서 확장한다.

## 6. StreetLearn — city navigation from Street View

- **Mirowski et al. (2019), _Learning to Navigate in Cities Without a Map_.**
- arXiv: https://arxiv.org/abs/1804.00168
- Street View panorama 기반 대도시 navigation을 제시했다. 360CityArena는 GSV의 static/discrete panorama 한계를 360° video trajectory의 연속 motion으로 보완하려 한다.

## 7. CityNav — aerial navigation의 보완 축

- **_CityNav: A Large-Scale Dataset for Real-World Aerial Navigation_ (2024).**
- arXiv: https://arxiv.org/abs/2406.14240
- aerial viewpoint의 real-world navigation을 다룬다. 360CityArena는 그와 달리 ground-level egocentric city exploration을 평가하며, 두 benchmark는 multi-scale planning 연구에서 상호보완적이다.

## 8. Tag Map — LLM planning을 위한 map grounding

- **_Tag Map: A Text-Based Map for Spatial Reasoning and Navigation with Large Language Models_ (2024).**
- arXiv: https://arxiv.org/abs/2409.15451
- LLM planner가 사용할 수 있는 text-based map representation을 연구한다. 360CityArena에서 current-location map이 항상 성능을 올리지 못한 관찰은 map representation과 visual grounding의 alignment가 별도 문제임을 시사한다.

## 9. RT-2 — VLA action grounding의 기준점

- **Brohan et al. (2023), _RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control_.**
- arXiv: https://arxiv.org/abs/2307.15818
- vision-language knowledge를 robot action token으로 옮기는 VLA의 대표 사례다. 360CityArena는 low-level robot control을 내지는 않지만, VLA가 action에 앞서 해결해야 할 visual–language–spatial grounding과 long-horizon decision 문제를 노출한다.

## 10. CARLA — 자율주행 simulation의 비교 기준

- **Dosovitskiy et al. (2017), _CARLA: An Open Urban Driving Simulator_.**
- arXiv: https://arxiv.org/abs/1711.03938
- sensor suite, vehicle dynamics, interaction이 있는 AD simulator다. 360CityArena는 CARLA를 대체하지 않으며, 더 사실적인 시각 도시 환경에서 route/spatial reasoning을 stress-test하는 보완 benchmark로 읽어야 한다.

## 읽는 순서

1. StreetLearn·TOUCHDOWN으로 outdoor/VLN 기본 setting을 파악한다.
2. Vid2Sim·RVW·EmbodiedCity로 realism과 interactivity trade-off를 비교한다.
3. Tag Map으로 map-to-view grounding 문제를 본다.
4. RT-2와 CARLA를 기준으로 360CityArena가 VLA/AD stack의 어느 계층을 시험하는지 정리한다.
