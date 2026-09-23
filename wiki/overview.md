# Wiki Overview

## 2026-W39: Feasibility-Gated Safety와 World-Model Representation Distillation
- **ShieldVLA**는 VLM rubric으로 visual safety margin을 만들고 HJ reachability-inspired critic이 VLA update를 feasible reward optimization과 infeasible recovery optimization으로 나눈다. 이는 closed-loop navigation/manipulation에서 SR과 cumulative safety cost를 함께 다루는 explicit safety layer지만, critic/rubric의 learned score는 formal safety guarantee나 real-road rare-event evidence가 아니다.
- **THAW-VLA**는 heavy world model의 future rollout을 online control에서 제거하고 cached internal feature만 compact VLA student에 distill한다. base policy와 동일한 deployment graph로 physical/dynamics prior를 전달한다는 latency 장점이 있으나, representation alignment는 multi-agent planning·traffic-rule compliance·safety를 자동으로 보장하지 않는다.
- 두 작업은 VLA 배포에서 "더 많이 reason/generate"하는 것보다 safety/physical representation을 어떤 constrained interface로 action policy에 전달하고, deployment compute를 어떻게 제한하며, closed-loop 위험을 어떤 metric으로 검증하는지가 핵심임을 보강한다.

## 2026-W37/W38: Closed-Loop Driving Distillation and Robust Vision–Action Interfaces
- [[DriveZero]]는 autonomous driving에서 perception/action의 학습 regime을 분리한다. privileged structured-state [[ClosedLoopReinforcementLearning]] teacher가 mixed-agent world에서 행동을 만들고, multi-VFM representation을 쓰는 camera-only planner가 그 rollout을 distill한다. 이는 human-log imitation의 단일 미래·policy-induced state 공백을 보완하지만 simulator, reward, privileged perception gap이 안전성 상한을 정한다.
- [[LatentInterfaceTraining]]은 VLA/WAM의 direct visual conditioning을 terminal-pose reconstruction을 받는 latent bottleneck으로 바꿔 [[VisionActionShortcut]]을 줄이려 한다. LIBERO-Plus의 camera/noise/layout shift 개선은 공간 action grounding 신호지만 language shift 및 broader real-world reliability는 별도 검증이 필요하다.
- 두 작업의 공통점은 visual/language representation의 크기 자체보다, 어떤 representation이 어떤 constrained interface를 통해 executable trajectory/action으로 전달되고 interactive OOD rollout에서 검증되는지가 중요하다는 것이다.

## 2026-09-03 LWN Weekly: Runtime Governance, Kernel Change, and Suspend-Security Boundaries
- [[Python]] JIT 논의는 compiler 성능이 실제 지원 기능이 되려면 PEP 기반 ownership, debugger/profiler·extension 호환성, memory/warm-up/throughput 지표, 그리고 release-manager의 명시적 판단이 필요함을 보여 준다.
- Rust `rnull` block driver와 [[LinuxKernel|Linux kernel]] 7.3 merge window는 memory-safety language 도입과 기능 병합이 block-layer lifecycle, ABI, concurrency, distribution regression이라는 기존 운영 계약을 대체하지 않음을 보인다.
- [[Virtualization]]의 steal-time 기반 vCPU moderation은 host contention을 guest scheduling에 반영할 수 있지만, latency-sensitive workload에서는 관측·정책·fallback을 함께 설계해야 한다.
- LUKS suspend key regression과 security advisory 목록은 crypto correctness가 algorithm selection에 그치지 않고 power-state transition, 물리 접근, package update·reboot의 end-to-end 대응을 포함한다는 점을 보강한다.

## 2026-W36: Driving Foundation Model과 Behavior-Intent VLA Supervision
- **Qwen-Drive-1.0**은 shared vision-language representation에 외부 BEV perception head와 Planning Expert를 결합한다. 3D detection·semantic occupancy·BEV map은 inspectable geometry interface가 되고, cached VLM key/value는 numerical ego trajectory를 생성하는 condition이 된다. 따라서 VQA가 그럴듯한 설명을 만든다는 것만으로 action grounding을 주장하지 않고, open-loop ADE/RFS와 NAVSIM/AlpaSim의 collision·progress·comfort 관점을 분리해 검증한다.
- **Act with Intent (INDI)** 는 executed behavior를 본 training-only teacher VLM의 semantic intent를 student VLA의 intermediate latent에 증류한다. 목적과 execution progress를 공유 latent로 만들고 action·visual outcome·textual purpose grounding을 공동 학습하며, phase/cross-task intervention으로 latent의 policy 영향력을 시험한다.
- 두 작업은 VLA가 text를 직접 actuator command로 바꾸는 것보다, **shared representation 또는 latent intent가 어떤 constrained numerical action interface를 통해 실제 control에 전달되는가**가 핵심임을 보인다. 다만 simulator/finite tabletop success는 vehicle/robot safety guarantee가 아니므로 uncertainty, rule/constraint validation, timing watchdog, fallback/shield가 배포 boundary에 남는다.

## 2026-08-27 LWN Weekly: Copyleft Enforcement, AI License Design, and Post-Quantum Migration
- [[BambuLab|Bambu Lab]]과 [[SoftwareFreedomConservancy|Software Freedom Conservancy]]의 사례는 copyleft가 문구만으로 자동 집행되지 않으며, 권리자·사용자의 검증 및 조치가 필요함을 보여 준다.
- [[OpenMDW]] 논의는 모델·데이터·가중치·소프트웨어를 하나의 라이선스로 포괄하려는 시도가 [[OpenSourceDefinition|Open Source Definition]] 및 종료 조항과 충돌할 수 있음을 드러낸다.
- [[PostQuantumCryptography|Post-Quantum Cryptography (PQC)]]는 [[OpenSSL]] 설정, TLS hybrid 전환, [[OpenPGP]] 상호운용성까지 포함하는 운영 과제가 되었다.
- [[LinuxKernel72MergeWindow|Linux Kernel 7.2 Merge Window]], [[Remind]], [[Quickshell]] 및 주간 보안·배포판 요약은 기술 변화가 유지보수·신뢰 경계·도구 통합 비용과 분리될 수 없음을 보강한다.

## 2026-08-20 LWN Weekly: Governance, Trust Chains, and Kernel Operational Boundaries
- [[Debian]]의 LLM 사용 투표는 생성형 도구를 허용/금지하는 단순 선택이 아니라 출처, 라이선스, 검토 책임, 커뮤니티 합의를 배포판의 재현 가능한 작업 흐름에 어떻게 연결할지의 문제로 제시한다.
- Python `pathlib`와 [[BootstrappableBuilds]]는 서로 다른 계층에서 문자열/기존 binary에 암묵적으로 의존하는 경계를 줄인다. 전자는 API의 의미·이식성을, 후자는 compiler/toolchain의 build provenance를 명시한다.
- Fedora의 [[AFALG]] 제한, Arm page-table 확장, [[BPF]]의 stable-branch CI는 kernel 기능을 추가하는 것만으로 충분하지 않으며, attack surface, backport, architecture coverage, real workload regression을 함께 운영해야 한다는 공통 신호다.
- 이 호의 AMD memory-controller 연구와 distribution security advisory는 kernel 권한 획득 뒤에도 firmware·hardware trust boundary가 남는다는 점을 보여 주며, patch cadence와 least privilege를 결합한 대응이 필요하다.

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

## 2026-09-02 VLAct: Representation-Centric Continued Pretraining for VLA
- [[VLAct]]는 [[VisionLanguageAction]]의 병목을 데이터 규모가 아니라 representation 보존과 alignment 문제로 재정의한다. pretrained [[VisionLanguageModel|VLM]]을 시작점으로 유지하면서 robot trajectory와 caption data를 병합 학습해 visual-language prior drift를 억제한다.
- 핵심 설계는 shallow-layer protection/caption mixing, [[OFT]]·[[PI]]·[[GR00T]] multi-head continuous action co-supervision, 그리고 partially unified action layout이다. 즉 shared gripper처럼 물리적으로 대응되는 semantics만 embodiment 간 정렬한다.
- [[LIBERO-Plus]], [[RoboTwin 2.0]], [[VLA-Arena]], [[DOMINO]], [[RoboCasa-GR1]], [[RoboDojo]]의 결과는 transfer와 sample efficiency 신호지만 real-world safety 보증은 아니다. 자율주행 전이에서는 vehicle action semantics와 closed-loop validation을 별도로 설계해야 한다.

## 2026-09-02 PonderPounce: pretrained MLLM을 episode context engine으로 쓰는 로봇 제어
- [[PonderPounce]]는 pretrained [[MultimodalModel|MLLM]]의 native causal context를 [[PersistentMemory|episode memory]]로 재사용한다. 느린 [[Ponder]]가 history를 누적하고 빠른 [[Pounce]]가 latest continuous cognition과 age를 받아 action chunk를 생성한다.
- [[RoboMME]]와 RoboCasa-DC에서 memory/demonstration conditioning 개선을 보였지만, 9B+3B serving cost, stale cognition, simulator-derived supervision cost가 핵심 제약이다. closed-loop 배포에는 freshness watchdog과 conservative fallback이 필요하다.
- 관련 reference map은 [[RoboTTT]], [[MEM]], [[MemoryVLA]], [[SeeTraceAct]], [[Latent Bridge]], [[Libra-VLA]], [[StreamVLA]], [[Running VLAs at Real-time Speed]]를 통해 memory substrate, action grounding, asynchronous serving의 trade-off를 정렬한다.

## 2026-09-02 VLAct 실행·참고 문헌 요약
- [VLAct 참고 문헌](sources/vlact-2608-27550-references.md)은 [[VLAct]]를 [[StarVLA]], [[StarVLA-Alpha]], [[pi0.5]], [[GR00T-N1]], [[ABot-M0]], [[Xiaomi-Robotics-1]], [[RoboDojo]], [[VLA-Arena]]와 연결한다.
- [VLAct 학습 노트](sources/vlact-2608-27550-learning.md)는 lower-layer freeze, caption auxiliary supervision, multi-head action co-training, active-dimension masking과 wrap-aware residual의 구현 포인트를 정리한다.
