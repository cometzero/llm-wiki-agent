# Wiki Overview

## 2026-W35/W34: Selective World Imagination and Hierarchical VLA Adaptation
- **RISE**는 autonomous-driving World Action Model에서 future rollout을 모든 scene에 고정하지 않고, latent prefix의 risk와 **future planning gain**이 cost를 상회할 때만 계속하는 selective imagination을 제시한다. nuScenes open-loop와 NAVSIM closed-loop를 함께 평가하지만, generated counterfactual과 simulator score는 real-vehicle safety guarantee가 아니다.
- **EXIMO**는 VLM의 high-level language subgoal을 VLA의 closed-loop manipulation execution에 grounding하고, 그 rollout을 SFT로 standalone policy에 증류한 뒤 residual off-policy RL로 refinement한다. 이는 VLA가 language explanation을 직접 actuator로 쓰지 않고, bounded subgoal interface와 motor policy를 분리해야 함을 강조한다.
- 두 작업은 더 많은 prediction/reasoning 자체보다 **언제 계산하고 어떻게 executable action으로 연결할지**가 deployment latency·safety·data efficiency를 좌우한다는 공통점을 보인다. RISE는 driving trajectory planning의 adaptive compute, EXIMO는 robotics의 hierarchical language-to-action post-training을 다룬다.

## 2026-08-13 LWN Weekly: Programmable Execution, Isolation, and Failure-Path Engineering
- 공개 한국어 번역은 BPF 기반 `binfmt_misc` 실행 디스패치가 재배치 가능한 프로그램과 컨테이너의 로더 선택을 유연하게 만드는 한편, setuid·mount namespace·리소스 제한을 신뢰 경계로 유지해야 함을 정리한다.
- KVM planes와 BPF 형식 검증 기사는 정적 안전성, confidential-computing 격리, 런타임 watchdog 사이의 역할 분리를 보여 준다. 운영 환경에서는 메모리 안전성뿐 아니라 지연·패킷 손실·권한 상승 방지가 검증 대상이다.
- CrossPoint와 block-layer 오류 주입은 제약된 장치에서의 resource-budget 설계와 스토리지의 failure-path 테스트가 Linux 생태계에서 같은 운영 원칙(명시적 범위와 복구 가능성)으로 연결됨을 보여 준다.
- 비밀번호 만료 정책과 security advisory 목록은 주기적 일괄 교체보다 MFA·침해 대응·배포판별 신속한 패치 관리로 이동하는 보안 운영 신호를 보존한다.

## 2026-W33 Spatial Memory, City-Scale Navigation, and Calibration Trends
- [[SpatialMemoryAgent]]는 frozen [[VisionLanguageModel|VLM]]을 유지한 채, verifier 보상 기반의 절차적 메모리(`summary + transferable lesson + TRS`)를 생성하고 재사용해 [[RoboSpatial]], [[ERQA]], [[Omni3D]], [[SAT]], [[EmbSpatial]]에서 개선을 보인다.
- [[360CityArena]]는 photorealistic 360° video 기반 Akihabara 도시 벤치마크로 [[EnvironmentUnderstanding]], [[PathReasoning]], [[SpatialReasoning]]을 한 번에 진단해 city-scale embodied navigation의 병목을 드러낸다.
- [[360CityArena]]의 결과는 최신 [[LMM]]들이 human 수준과 큰 격차를 보이며, 특히 map navigation과 multi-step route reasoning이 여전히 취약하다는 점을 보여 준다.
- [[360CityArena]]는 602개의 360° video segment, 193 node, 305 edge pose graph, 175 human-authored task로 구성되어 localization, landmark search, map navigation, VLN, relational spatial reasoning, object count를 함께 측정한다.
- [[360CityArena]]의 image-goal/language-goal 비교와 난이도 스케일링은 visual grounding과 route reasoning의 상호작용을 정량해, 실무에서 metric 설계의 우선순위를 정리한다.
- [[SpatialMemoryAgent]]의 참고문헌 축은 세 갈래로 정리된다. [[SpatialVLM]]·[[SpatialRGPT]]·[[EmbSpatial-Bench]]는 공간 grounding을 학습된 표현과 벤치마크 관점에서 다루고, [[RAG]]·[[Mem0]]·[[MemP]]는 retrieval/memory의 기본 가정을, [[SpaceTools]]·[[S-Agent]]·[[SpatialEvo]]는 tool use와 self-evolution 대안을 보여 준다.
- 이 방법의 핵심은 단순 의미 유사도 검색이 아니라 실제 전이 성과를 반영한 신뢰도 보정이다.
- 배포 모드는 read-only로 구성되어 `training-free` 성격을 유지한다. 따라서 성능 향상은 재학습이 아니라 메모리 정책(필터링·점수화·쓰기 정책) 개선으로도 가능하다.
- 반대로 verifier 오판, reflection hallucination, reward credit assignment 불분해성, OOD에서의 embedding 한계는 운영 리스크이며, top-k 제어·trusted write·action safety shield가 필요하다.

## 2026-W33 Urban Navigation Reference Synthesis
- [[360CityArena]]는 [[SidewalkBench]], [[TOUCHDOWN]], [[StreetLearn]], [[Vid2Sim]], [[EmbodiedCity]], [[CityNav]], [[TagMap|Tag Map]], [[RT-2]], [[CARLA]]와의 비교 축에서 `city-scale photorealistic trajectory traversal`의 위치를 정한다.
- 이 레퍼런스는 realism(예: [[Vid2Sim]], [[Realistic Virtual World|Takenawa et al. (2025)]], [[EmbodiedCity]]), outdoor VLN lineage(예: [[TOUCHDOWN]], [[StreetLearn]]), map-text grounding(예: [[TagMap|Tag Map]]), VLA/AD action grounding(예: [[RT-2]])로 축을 분리해 [[360CityArena]]의 개선 지점을 좁힌다.
- 결과적으로 [[360CityArena]]는 AD 전체를 대체하는 도구가 아니라, 특히 [[AutonomousDrivingVLA]]에서 perception-grounding과 long-horizon route reasoning을 검증하는 stress test로 작동한다.

## 2026-W33 360CityArena learning-note synthesis
- [[360CityArena]] 학습 노트는 `observation-memory-action` 루프를 실무적으로 분해해 [[ObservationToActionLoop]] 설계의 최소 패턴을 제시한다.
- map prior 사용은 지도 정확도/좌표 변환/랜드마크 대응이 정합될 때만 유효하며, 정합 실패 시 오히려 오차를 키운다.
- image-goal 성능 이점은 고정되지 않고, task visibility 및 grounding 정합이 먼저 확보되어야만 안정적으로 유지된다.
- 배포 관점에서는 `place recognition confidence`, `heading uncertainty`, `stagnation/reroute detector`, `route-progress monitor`를 최소 탑재해야 긴 경로에서의 compounding error를 제어할 수 있다.
- 본 소스는 closed-loop safety score로 오해되는 한계를 명시해, [[360CityArena]]를 physical simulator와 구분해 사용하는 방향을 제안한다.