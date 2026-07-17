## [2026-07-17] ingest | LWN.net Weekly Edition for July 9, 2026

Added source. Key claims: Eric Biggers modernizing kernel crypto with 2.5x faster library functions; iomap layer abstracting filesystem I/O; negative dentry accumulation causing soft-lock issues; RCU expedited grace period improvements reducing memory 33-41%; kmalloc_nolock enabling lockless BPF allocation; two LLM-assisted MM patch sets (van Riel 1GB HugePage, Shutsemau VM tracking) with mixed community reception.

New entity pages: EricBiggers, RikVanRiel, KirylShutsemau, LinuxSecuritySummit, LSFMMbpfSummit2026, ChristianBrauner

New concept pages: KernelCryptography, Iomap, NegativeDentry, RCU, kmalloc_nolock, LLMAssistedKernelDevelopment

## [2026-07-15] ingest | 2026-W29 HF Weekly ABot-N1 and Flow-ERD validation repair

- Added deterministic source pages for missing raw deliverables after partial ingest timeout.
- Added placeholder concept pages for unresolved ABot-N1/Flow-ERD support wikilinks.

## [2026-07-15] ingest | Flow-ERD: Agent-type Aware Flow Matching with Entropy-Regularized Distillation for Diverse Traffic Simulation

Added source. Key claims: AFM backbone + entropy-regularized distillation으로 traffic simulation realism-diversity trade-off 완화; WOSAC benchmark에서 Pareto 개선 입증; VLA/E2E AD policy의 world model/evaluator 역할.

Created entity pages: [[WOSAC]].

Created concept pages: [[FlowMatching]], [[FlowERD]], [[EntropyRegularizedDistillation]], [[AgentTypeKinematics]], [[ClosedLoopEvaluation]].

## [2026-07-15] ingest | Flow-ERD: Agent-type Aware Flow Matching with Entropy-Regularized Distillation for Diverse Traffic Simulation

Added source. Key claims: AFM+ERD 결합으로 realism-diversity trade-off 동시 해결, WOSAC benchmark에서 RMM 0.7840 달성 및 Pareto frontier 개선. Entity pages: FlowERD, SeulbinHwang, WOSAC. Concept pages: FlowMatching, MultiAgentSimulation, CovariateShift, ModeCollapse, ParetoFrontier, EntropyRegularizedDistillation.

## [2026-07-15] ingest | ABot-N1: 범용 Visual Language Navigation foundation model을 향하여

Added source. Key claims: slow-fast VLN foundation model; pixel goal intermediate representation; POI arrival 77.3%/indoor 95.4%/outdoor 92.9% SR. Created concept pages for [[SlowFastArchitecture]], [[PixelGoal]], [[VLN]]. Linked to existing [[ABot-N0]], [[Qwen-RobotNav]], [[VisualThink-VLA]] pages.

## [2026-07-15] ingest | ABot-N1: 범용 Visual Language Navigation foundation model을 향하여 — References

Added source. Key claims: ABot-N1 레퍼런스 요약으로 benchmark→backbone→deployment 읽기 순서 제안; [[ABot-N0]], [[Qwen-RobotNav]], [[GR00TN1]], [[π0.5]], [[OpenVLA]] 등 VLN/VLA 핵심 연구와 연결; [[VisualLanguageNavigation]], [[ABot-N1]] entity 생성

## [2026-07-15] ingest | ABot-N1: Toward a General Visual Language Navigation Foundation Model

Added source. Key claims: slow-fast VLM architecture with pixel goal intermediate representation; unifies five navigation tasks (point/object/POI/instruction/person-following); achieves 77.3% POI arrival, 95.4% indoor, 92.9% outdoor SR. Created entity page for [[ABot-N1]]. Created concept pages for [[VisualLanguageNavigation]], [[PixelGoal]], [[SlowFastArchitecture]], [[Waypoint]], [[ActionGrounding]].

## [2026-07-15] ingest | ABot-N1: Toward a General Visual Language Navigation Foundation Model

Added source. Key claims: slow-fast VLN foundation model decouples cognition and control; pixel goal as intermediate representation bridges semantic intent and continuous waypoint; unifies 5 navigation tasks; POI arrival 77.3% (+35.0%p); indoor 95.4%, outdoor 92.9% SR. Created entity pages for [[AMAP-CVLab]], [[ABot-N0]]. Created concept pages for [[VisualLanguageNavigation]], [[SlowFastArchitecture]], [[PixelGoal]], [[PixelGoalNavigation]], [[ABotN-PointBench]], [[ABotN-POIBench]].

## [2026-07-10] ingest | LWN.net Weekly Edition for July 2, 2026

Added Korean LWN Weekly translation source. Key claims: [[DebianProtestware]] exposes locale-dependent package behavior as a distribution trust issue; [[Git255]] and [[RhombusMetaprogramming]] cover developer-tool and language-design changes; [[KernelHardening]], [[KernelWriteback]], [[BPFLocalStorage]], and [[LinuxKernel72]] extend kernel security/I/O/BPF coverage; [[SecureBootCertificateExpiration]], [[ObjectStorageAlternatives]], and [[OSPM2026]] cover operational trust, storage, and scheduling. Manual source materialization used after LLM ingest returned malformed NVIDIA JSON.

## [2026-07-08] ingest | Embodied.cpp 참고 레퍼런스 요약

Added source. Key claims: 10개 선행 연구 정리 - Execution-State Capsules(complete restorable state), MuseVLA(adaptive multimodal sensing), LaWAM(latent WAM), DAM-VLA(multi-rate execution 100Hz), WAM survey(taxonomy), Being-H0.7(WAM/VLA hybrid), Stop Wandering(spatial memory/planner state as runtime object), H2O(memory orchestration), vla.cpp(predecessor), VLA family(π0/π0.5/OpenVLA/RT-2). Created 1 entity page(vla.cpp), 7 concept pages(Execution-State Capsules, Multi-Rate Execution, LatentWorldActionModel, OnDeviceInference, HeterogeneityAwareOrchestration, AdaptiveMultimodalSensing, SpatialMemoryNavigation).

## [2026-07-08] ingest | Embodied.cpp 분석: VLA/WAM을 로봇 edge에 올리기 위한 runtime contract

Added source. Key claims: five-layer C++ runtime architecture for VLA/WAM deployment; multi-rate execution separates perception/backbone/prediction/action refresh rates; latency-first batch-1 optimization for closed-loop control; HY-VLA 100.0%/π0.5 91.0% success rate; LingBot-VA GGUF Q4_K quantization reduces VRAM 312.2→88.1 MiB. Created entity pages for [[HY-VLA]], [[π0.5]], [[LingBot-VA]]. Created concept pages for [[FiveLayerRuntime]], [[MultiRateExecution]], [[LatencyFirstBatch1]], [[ClosedLoopRobot]], [[GGUFQuantization]], [[HeterogeneousScheduling]], [[PredictedFuture]].

## [2026-07-08] ingest | Embodied.cpp: 이기종 로봇을 위한 Embodied AI 모델의 휴대형 추론 런타임

Added source. Key claims: VLA/WAM을 위한 portable C++ inference runtime 제안, multi-rate execution/latency-first fused inference/extensible I/O 세 가지 핵심 설계, five-layer architecture, HY-VLA 100.0%/π0.5 91.0% success rate, WAM Q4_K에서 3.6× memory reduction. Created 4 entity pages (Embodied-cpp, HY-VLA, LingBot-VA, SEU-PAISys) and 4 concept pages (MultiRateExecution, LatencyFirstInference, EmbodiedInterface, FiveLayerArchitecture).

## [2026-07-03] ingest | LWN.net Weekly Edition for June 25, 2026

Added Korean LWN Weekly translation source. Key claims: [[FreeThreadedPython]] moves GIL removal toward stable runtime adoption; [[AURSupplyChainAttack]] exposes community package repository risk; [[Fedora2FA]] ties provenpackager authority to stronger authentication; [[LinuxKernel72]] and [[BPF]] coverage include [[BPFArena]], [[BPFCoroutines]], [[BPFKASAN]], [[RMRBRMR]], and [[OSPM2026]]. Manual source materialization used after LLM ingest returned malformed JSON.

## [2026-07-01] ingest | HF Weekly 2026-W27 Qwen-RobotNav and Object-Centric Residual RL validation repair
- Added missing source coverage pages and placeholder concept nodes for newly emitted wikilinks.

## [2026-07-01] ingest | Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — references

Added source. Key claims: VLA backbone([[π0]]/[[π0.5]]/[[π0.6]]/[[GR00T-N1]])과 ResidualRL의 조합이 sim-to-real transfer의 핵심; reading order로 1)VLA family 2)Residual RL 3)Perception stack([[SAM-2]]) 제안. Created 2 entity pages(PhysicalIntelligence, NvidiaRobotics) and 3 concept pages(VLA, ResidualRL, Sim-to-Real-Transfer).

## [2026-07-01] ingest | Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — Korean analysis

Added source. Key claims: zero-shot sim-to-real transfer via object-centric residual TD3 on frozen VLA, achieving 42%→76% success rate improvement on FR3 robot. Paired sim/real VLA training with pose noise/dropout for robustness. Created entity pages for [[FR3]] and [[MuJoCo]]. Created concept pages for [[ObjectCentricResidualRL]], [[SimToRealTransfer]], [[CompoundingError]], [[PairedSimRealTraining]], [[ResidualRL]], [[TD3]], [[ConfidenceGating]], and [[SelfImprovementLoop]].

## [2026-07-01] ingest | Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

Added source. Key claims: object-centric pose 기반 residual RL로 VLA의 zero-shot sim-to-real transfer 달성, 42%→76% success rate 향상. Object-centric observation(6-DoF pose + proprioception + base action)이 visual domain gap을 회피하여 simulation-only training으로 real robot에 직접 deployment 가능함을 보여줌. TD3 기반 residual policy, FoundationPose+SAM2 pose tracking, FR3 robot evaluation 포함.

Created/updated: 4 concept pages (ObjectCentricResidualRL, ZeroShotSimToReal, ObjectCentricObservation, ResidualRL), 1 entity page (FR3).

## [2026-07-01] ingest | Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System — learning guide

Added source. Key claims: Task-adaptive observation encoding with (B, γ, w_c) parameters; temporal decay for observation history weighting; camera weight varies by driving situation; Qwen-RobotNav achieves VLN-CE 76.5% and NAVSIM 91.4 PDMS. Created entity pages for Qwen-RobotNav and NAVSIM. Created concept pages for TaskAdaptiveObservationEncoding, TemporalDecay, CameraWeight, ActionGrounding, PDMS, and AgenticNavigation.

## [2026-07-01] ingest | Qwen-RobotNav Technical Report — references

Added source. Key claims: navigation/VLN/autonomous driving 레퍼런스를 3축(Foundation Model, Trajectory Planning, Agentic EQA)으로 정리. [[AllDayNav]], [[GN0]], [[ABot-N0]], [[ColaVLA]], [[FAST-EQA]], [[AstraNav-World]], [[Habitat-GS]], [[Planning-aligned Token Compression]], VLN-MME, Memory Centric EQA 등 10개 논문 인용. 6개 entity page ([[AllDayNav]], [[GN0]], [[ABot-N0]], [[ColaVLA]], [[AstraNav-World]], [[Habitat-GS]])와 4개 concept page ([[Vision-Language Navigation]], [[Lifelong Navigation]], [[Embodied Question Answering]], [[Planning-aligned Token Compression]]) 생성.

## [2026-07-01] ingest | Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System

Added source. Key claims: Qwen3-VL backbone 기반 unified navigation model로 VLN-CE 76.5%, NAVSIM 91.4 PDMS 달성; [[ParameterizedNavigationInterface]]로 inference-time configurable; [[AgenticNavigation]] dual-system interface 제안; 15.6M mixed navigation corpus 사용.

New pages: entities/Qwen3VL.md, entities/NAVSIM.md; concepts/ParameterizedNavigationInterface.md, AgenticNavigation.md, WaypointTrajectory.md, VisionLanguageCoTraining.md

## [2026-07-01] ingest | Qwen-RobotNav Technical Report (Korean translation)

Added source. Key claims: navigation diversity is a context modeling problem (not architecture explosion); Qwen3-VL + parameterized interface handles VLN-CE 76.5%, EVT-Bench 90.0%, NAVSIM 91.4 PDMS; trajectory-only training collapses to reactive mapper — vision-language alignment loss required; synthetic data pipeline uses LLM→video→VLM filter→depth/pose→kinematic filter. Created entity pages for [[Qwen3-VL]] and [[SigLIP]]. Created concept pages for [[AgenticNavigation]], [[TaskAdaptiveObservationEncoding]], [[WaypointActionHead]], [[ContextModeling]], [[NAVSIM]], [[OnDeviceInference]], [[EmbodiedPromptDesign]].

## [2026-06-24] ingest | Hugging Face Weekly 2026-W26 VLA/WAM update pass

Added World Action Models survey and PolicyTrim raw deliverables; repaired validation links and index coverage.

## [2026-06-24] ingest | PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training — learning

Added source. Key claims: PolicyTrim은 2단계 RL post-training으로 VLA [[ActionChunk]] utilization 3배, [[PhysicalSteps]] 51.4% 감소, 5.83배 speedup 달성. Phase 1 [[HorizonSuccessReward]]로 [[TailDegradation]] 완화, Phase 2 [[RedundancyAwareReward]]로 불필요 step 절감. [[IntrinsicPolicyEfficiency]]는 architecture efficiency(pruning/quantization)와 구분되는 개념으로, policy behavior 자체의 효율성을 최적화함. Benchmarks: [[LIBERO]], [[ManiSkill]], [[MetaWorld]]. Created 7 concept pages: [[PolicyTrim]], [[IntrinsicPolicyEfficiency]], [[TailDegradation]], [[HorizonSuccessReward]], [[RedundancyAwareReward]], [[PhysicalSteps]], [[ActionChunk]]. No contradictions with existing wiki.

## [2026-06-24] ingest | PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training — references

Added source. Key claims: PolicyTrim 논문의 8개 축 레퍼런스 정리(π0/OpenVLA/GR00T VLA 계열, LIBERO/ManiSkill/Meta-World benchmark, RL post-training, efficient VLA 연구). 읽기 순서 제안 포함. [[ActionChunk]] concept page 생성.

## [2026-06-24] ingest | PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training — analysis

Added source. Key claims: RL 2-stage post-training으로 VLA deployment 병목인 action chunk tail degradation와 redundant steps를 해결, 3x action chunk utilization, 51.4% physical steps 감소, 5.83x speedup 달성. 적용 모델: π0.5, OpenVLA-OFT, GR00T. Created entity pages: OpenVLA-OFT. Created concept pages: ActionChunk, PolicyEfficiency, RLPostTraining.

## [2026-06-24] ingest | PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training

Added source. Key claims: VLA deployment 병목은 compute-centric efficiency가 아닌 intrinsic policy efficiency 문제; PolicyTrim은 두 단계 RL post-training(신뢰 가능한 action chunk 확장 + 중복 단계 감축)으로 action chunk utilization 3배, physical steps 51.4% 감소, 5.83배 speedup 달성. Entity pages 생성: π0.5, GR00T, OpenVLA-OFT, LIBERO, ManiSkill, Meta-World. Concept pages 생성: IntrinsicPolicyEfficiency, ActionChunk, RLPostTraining, ComputeCentricEfficiency.

## [2026-06-24] ingest | World Action Models: A Survey — WAM 서베이 학습 자료

Added source: raw/learning.md → sources/world-action-models-survey-2606-20781-learning.md

Key claims:
- WAM은 "dream less, act more" 철학으로 action-facing future prediction에 집중
- Predictive substrate (pixel/latent/language/geometry) 4가지 수준
- Action coupling 3가지 패턴: Render-and-Decode, Latent-Only, Video-Generation-Free
- 5단계 step-by-step WAM 분석 프레임워크 제공

New concept pages: [[WorldActionModel]], [[PredictiveSubstrate]], [[ActionCoupling]], [[RenderAndDecode]], [[LatentOnly]], [[VideoGenerationFree]]

## [2026-06-24] ingest | World Action Models: A Survey — references

Added source. Key claims: WAM survey(2606.20781) 레퍼런스를 7축으로 정리 — VLA 일반, Video World Models, DriveDreamer/Drive-WM/OmniDreams 계열, VisualThink-VLA/TBD-VLA/ReflectDrive, Latent world model, Action-scoring/MPC, Evaluation papers. 읽기 순서 제안: VLA4AD → DriveDreamer/OmniDreams → VLA repo 논문 → WAM survey 통합 정리. Created [[Vision-Language-ActionModels]], [[LatentWorldModels]], [[Model-PredictiveControl]] concept pages; [[DriveDreamer]], [[VLA4AD]] entity pages. No contradictions.

## [2026-06-24] ingest | World Action Models: A Survey — analysis

Added source. Key claims: WAM을 "action-facing predictive model"로 정의하여 VLA/video world model/broad world model과 경계 재정립; 3분류 taxonomy(Render-and-Decode, Latent-Only, Video-Generation-Free); 4축 anatomy(predictive substrate, backbone, action coupling, deployment regime); 평가 지표를 visual quality(FVD)에서 action utility/causality/latency/generalization으로 재정렬. Entities: OmniDreams, ReflectDrive, TBD-VLA, VisualThink-VLA. Concepts: WorldActionModel, ActionFacingPredictiveModel, PredictiveSubstrate, WAMTaxonomy.

## [2026-06-24] ingest | World Action Models: A Survey — WAM 서베이

Added source. Key claims: WAM은 [[PredictiveAction]] method로 VLA, broad world model, video generation과 구분되며, 세 가지 설계 철학(Render-and-Decode, Latent-Only, Video-Generation-Free)과 네 축 해부(Predictive substrate, Backbone, Action coupling, Deployment regime)를 제시함. 자율주행 VLA에서 WAM은 lane change, braking, yielding, cut-in 대응 같은 executable decision 개선에 초점을 둠.

New concept pages: [[WorldActionModel]], [[PredictiveSubstrate]], [[ActionCoupling]], [[RenderAndDecode]], [[LatentOnlyWAM]], [[VideoGenerationFreeWAM]]

## [2026-06-19] ingest | LWN.net Weekly Edition for June 11, 2026

Added source. Key claims:
- AI 에이전트가 Fedora와 여러 프로젝트에서 오작동 (Nathan Giovannini 계정)
- 커널에 spawn template API 제안, posix_spawn() 개선 논의
- vmsplice() 제거 패치가 Linus Torvalds 찬성 하에 진행
- BPF 루프 검증 개선을 위한 스칼라 진화 기술 개발
- fanotify에 namespace/cgroup 감시 기능 추가 예정
- PyPI 신뢰할 수 있는 게시 36%+ 채택

Created 6 entity pages (NathanGiovannini, AdamWilliamson, MikeFiedler, LiChen, EduardZingerman, MartinKolman) and 5 concept pages (SpawnTemplate, TrustedPublishing, Vmsplice, Fanotify, BPFScalarEvolution).

## [2026-06-12] ingest | LWN.net Weekly Edition for June 4, 2026

Added Korean LWN Weekly translation source. Key claims: MeshCore shows trademark governance can constrain open-source naming; x32 ABI maintenance depends on user/test coverage more than technical efficiency; open-source security is a coordinated ecosystem activity; kernel coverage connects [[FilesystemMergePolicy]], [[MemoryManagement]], [[KernelFunctionSignatures]], [[XattrCaching]], [[BPF]], and [[FIPSCertification]].

## [2026-06-10] ingest | NVIDIA OmniDreams: Closed-loop 자율주행 시뮬레이션을 위한 실시간 생성형 World Model — learning

Added source. Key claims: WAM architecture가 VLA보다 driving에 적합, Diffusion Forcing + Self Forcing으로 closed-loop AR generation 구현, world-scenario map이 simulator state와 photorealistic generation을 연결. Created entity pages for Cosmos, AlpaSim, Alpamayo. Created concept pages for WorldActionModel, DiffusionForcing, SelfForcing, WorldScenarioMap.

## [2026-06-10] ingest | NVIDIA OmniDreams: Closed-loop 자율주행 시뮬레이션을 위한 실시간 생성형 World Model — references

Added source. Key claims: Cosmos/Cosmos-Predict2.5 백본 의존성, Alpamayo baseline 비교 기준, Diffusion Forcing/Self Forcing training 안정화 기법, WAM vs VLA architecture 논쟁, closed-loop evaluation 패러다임의 중요성. Created 11 entity pages (Cosmos, Cosmos-Predict2.5, Alpamayo1, Alpamayo1.5, AlpaSim, NuRec, DriveDreamer, Drive-WM, Waymo, CARLA, nuPlan) and 5 concept pages (WorldActionModel, DiffusionForcing, SelfForcing, DistributionMatchingDistillation, ClosedLoopSimulation).

## [2026-06-10] ingest | NVIDIA OmniDreams analysis

Added source. Key claims: OmniDreams는 Cosmos-Predict 2.5 기반 realtime action-conditioned generative world model로 68-105 FPS multi-view generation 달성. WAM(World Action Model)이 VLA보다 parameter-efficient할 수 있다는 관점 제시. Closed-loop reactivity가 핵심 지표이며, reconstruction simulator의 novel event generation 한계를 극복. Created 6 entity pages (CosmosPredict, AlpaSim, Alpamayo, NVIDIA, GB300) and 11 concept pages (WorldActionModel, ClosedLoopSimulation, PolicyReactivity, ReconstructionSimulator, WorldScenarioMap, DiffusionForcing, ExposureBias, AutoregressiveGeneration, RolloutDrift, SelfForcing, MultiViewConsistency). 기존 VLA 중심 연구와의 관점差异 noted.

## [2026-06-10] ingest | NVIDIA OmniDreams: Closed-loop 자율주행 시뮬레이션을 위한 실시간 생성형 World Model

Added source. Key claims: (1) Cosmos 기반 generative world model로 720p 68~105 FPS 실시간 생성, (2) [[WorldActionModel]] backbone으로 2B param이 10B VLA보다 나은 collision metric 달성, (3) KV cache + factorized attention으로 efficient multi-view generation. Created 10 entity pages (NVIDIA, Cosmos, Alpamayo, AlpaSim, GB300, PAI-AV-NuRec, RDS, RDS-HQ-1M, Sanja Fidler, Qwen2.5-VL-7B, SIL-Wheel) and 9 concept pages (WorldModel, WorldActionModel, ClosedLoopSimulation, DiffusionForcing, SelfForcing, DMD, MultiViewGeneration, ActionConditioning, FlexAttention).

## [2026-06-10] ingest | TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델 — learning

Added source. Key claims: VLA [[BlockDiffusion]] 학습 가이드로 [[TemporalAR]] 구조로 병렬 디노이징과 순차 블록 처리를 결합하여 closed-loop latency와 temporal coherence를 동시에 달성. [[RTC]] 실시간 chunk 갱신, [[ActionTokenization]]의 discrete token 사용 이유, block size `m` hyperparameter의 latency-quality 트레이드오프 정리.

New concept pages created:
- [[BlockDiffusion]] — block 단위 병렬 디노이징 기법
- [[TemporalAR]] — 시간적 자기회귀 구조
- [[RTCRealTimeChunking]] — 실시간 chunk 갱신 메커니즘
- [[ActionTokenization]] — continuous action의 discrete token 변환

## [2026-06-10] ingest | TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델 — references

Added source. Key claims: TBD-VLA 관련 10개 레퍼런스 정리 (Fast-dVLA, Discrete Diffusion VLA, Qwen3-VL, LIBERO-Plus, InternVLA-M1, VLA-0, LLaDA-VLA, OpenVLA, π0.5, FAST). 읽기 우선순위: Discrete Diffusion 계열(1순위) → Qwen3-VL backbone(2순위) → baseline 비교(VLA-0, OpenVLA, π0.5, 3순위) → evaluation benchmarks(LIBERO-Plus, 4순위). Created entity pages for Fast-dVLA, DiscreteDiffusionVLA, VLA-0, LLaDA-VLA, FAST. Created concept pages for TemporalBlock, TemporalAutoregression, BlockDiffusionDecoding.

## [2026-06-10] ingest | TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델 — analysis

Added source. Key claims: Block Discrete Diffusion으로 discrete VLA의 action-token latency를 줄이면서 Block-level AR로 temporal coherence를 유지. RTC 지원으로 closed-loop control 가능. Qwen3-VL 2B backbone, SimplerEnv Google Robot 88.7%/0.086s 성능. [[ReflectDrive2]]와 trajectory tokenization 관점에서 연결.

New entity pages: [[Qwen3VL]], [[SimplerEnv]], [[LIBERO]]
New concept pages: [[BlockDiscreteDiffusion]], [[TemporalBlockDiffusion]], [[RealTimeChunking]], [[DiscreteVLALatency]]

## [2026-06-10] ingest | TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델

Added source. Key claims: Block discrete diffusion achieves 0.086s latency with 88.7% SimplerEnv success; enables Real-Time Chunking via temporal in-painting; outperforms π0.5 (50.0% → 67.1%) in real-world manipulation. Created entity pages for SungWookLee, XuhuiKang, YenLingKuo, Qwen3VL. Created concept pages for TBDVLA, BlockDiffusion, RealTimeChunking, VisionLanguageAction, TemporalInpainting.

## [2026-06-05] ingest | LWN.net Weekly Edition for May 28, 2026

Added Korean LWN Weekly translation source. Key claims: AI-generated bug reports are reshaping Linux kernel security workflow; GCC-BPF is closing feature gaps with LLVM; LSFMM+BPF discussions connect [[BPF]], [[PageCache]], [[MemoryController]], [[MemoryTiering]], and [[TransparentHugePage]]; MOT frames openwashing as a measurable [[OpenSource]] AI problem.

## [2026-06-03] ingest | VisualThink-VLA: Visual Intermediate Reasoning — learning

Added learning source for VisualThink-VLA paper. Key claims: Visual reasoning > textual CoT for VLA latency (22.8× speedup), semantic decision과 motor execution 분리 중요, VQA performance ≠ action grounding capability. Created concept pages for [[ActionGrounding]], [[VisualReasoning]], [[TeacherStudentDistillation]].

## [2026-06-03] ingest | VisualThink-VLA: Visual Intermediate Reasoning References

Added source. Key claims: VisualThink-VLA(2605.30011) 관련 10개 레퍼런스 정리 - [[DeepThinkVLA]]/[[InternVLA-M1]]은 [[LanguageGrounding]]→[[Action]] 과제, [[FastECoT]]/[[VisualPlanning]]은 textual vs visual reasoning 비교 기준, [[π0.5]]/[[SmolVLA]]는 대표 [[VLAPolicy]] baseline. 신규 entity: [[PhysicalIntelligence]]; 신규 concept: [[ReasoningAugmentedVLA]], [[π0.5]].

## [2026-06-03] ingest | VisualThink-VLA: 효과적이고 저지연인 VLA 정책을 위한 Visual Intermediate Reasoning — analysis

Added source. Key claims: textual CoT 대신 visual evidence states 사용으로 22.8× latency reduction (8.377s→0.367s), candidate evidence bank + selective routing + visual state composer 구조, route supervision + counterfactual utility training. 연결: [[SemanticGrounding]] 해결, [[ClosedLoopLatency]] 개선, [[RoboSemanticBench]] 평가 맥락과 일치.

## [2026-06-03] ingest | VisualThink-VLA: 효과적이고 저지연인 VLA 정책을 위한 Visual Intermediate Reasoning

Added source. Key claims: Visual intermediate reasoning으로 textual CoT의 latency(8.377s→0.367s, 22.8× speedup)와 weak visual grounding 문제를 동시에 해결. 6-channel evidence bank → selective router → visual state composer → action decoder 파이프라인. VisualEvidence-Kit (754.7k supervision/audit set) 제공.

New pages: source, 3 concept pages (VisualIntermediateReasoning, ECoT, VisualEvidenceKit), 1 entity page (VisualEvidenceAgent)

## [2026-06-03] ingest | RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기 — learning

Added source. Key claims: (1) VLA의 VQA 성능 ≠ action grounding 능력, (2) GSR/TSR/nSG metric으로 motor vs semantic 병목 분리 가능, (3) high GSR + low TSR = semantic action grounding 실패, (4) shortcut behavior는 색/위치 편향으로 인한 spurious success. Created concept pages: [[SemanticGrounding]], [[ShortcutBehavior]], [[ActionPrediction]].

## [2026-06-03] ingest | RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기 — references

Added source. Key claims: RoboSemanticBench(arXiv:2606.02277)의 관련 연구 레퍼런스 10편 정리. 핵심 연결은 [[SemanticGrounding]]이 [[ActionPrediction]]으로 전달되지 않는 문제. [[LangForce]], [[StarVLA]], [[ActionsAsLanguage]], [[AttentionRecalibration]] 등 VLA [[SemanticGrounding]] 핵심 연구 포함. 25개 엔티티(연구자) 페이지, 11개 컨셉(VLAForgetting, VisionOverride, LinguisticDiversity 등) 페이지 생성.

## [2026-06-03] ingest | RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기 — analysis

Added analysis source. Key claims: RSB benchmark로 VLA의 [[SemanticGrounding]] 격차를 GSR/TSR/nSG 메트릭으로 분리 측정, [[OpenVLA]]/[[GR00T]] 계열의 near-random 수준 semantic target selection 실패 실증, 자율주행 VLA에도 동일한 위험 적용. Created entity pages for GSR, TSR, nSG, RSB-Math, RSB-HardMath, RSB-General concepts.

## [2026-06-03] ingest | RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기

Added source. Key claims: [[VLA]] 모델의 [[SemanticGrounding]] 격차를 진단하는 [[RoboSemanticBench]] benchmark 도입 — grasp는 성공하지만 semantic target selection은 near-random 수준임을 실험적으로 보여줌. Semantic expert와 action expert 간 integration 실패가 motor control 문제가 아님을 입증.

Created entity pages: [[RoboSemanticBench]]

Created concept pages: [[SemanticGrounding]], [[SemanticExpert]], [[ActionExpert]], [[EmbodiedBenchmark]]

Updated sources/index.md

## [2026-05-29] ingest | LWN.net Weekly Edition for May 21, 2026

Added source covering openSUSE ToS age restriction controversy, LSFMM+BPF Summit memory management discussions (MGLRU integration, COW context, BufferedAtomicWrites, SwapTable, CXL, HugeTLB live update), 10th OpenPGP Email Summit PQC transition, and kernel 7.1-rc4 release. Created entity pages for Kairui Song, Lorenzo Stoakes, Shakeel Butt, Dan Williams, Phil Zimmermann, Peter G. Neumann, openSUSE, LSFMM+BPF Summit, OpenPGP Email Summit. Created concept pages for BufferedAtomicWrites, MGLRU, COWContext, CXL, SwapTable, FlashFriendlySwap, Post-Quantum Cryptography, PolicyGroups, HugeTLB, Autocrypt, HKPv2.

## [2026-05-24] ingest | AI/ML Learning Review — Day 30 (2026-05-24): Evaluation, Serving, and AI System Design

Added source. Key claims: [[Evaluation]]과 [[Benchmark]]의 차이와 한계, [[Serving]]과 [[InferenceOptimization]] (latency/throughput/quantization/KV cache), AI 시스템 네 층 ([[DataPipeline]], [[TrainingStack]], [[InferenceStack]], [[FeedbackLoop]])을 통합 정리. 13개 concept page 생성: [[Evaluation]], [[Benchmark]], [[HumanEvaluation]], [[Serving]], [[InferenceOptimization]], [[Latency]], [[Throughput]], [[Quantization]], [[KVCache]], [[DataPipeline]], [[TrainingStack]], [[InferenceStack]], [[FeedbackLoop]]. Overview 업데이트로 Day 1-30 전체 아키텍처 요약 포함. 기존 Day 30 (2026-05-22, 2026-05-23) 소스와 중복 → 최신 버전으로 교체 권장.

## [2026-05-23] ingest | AI/ML Learning Review — Day 30 (2026-05-23): Evaluation, Serving, and AI System Design

Added source. Key claims: (1) Benchmark scores alone don't represent full model capability—real-world performance depends on data distribution, latency, cost, safety; (2) Serving and inference optimization balance latency, throughput, memory, and quality via quantization, KV cache, batching; (3) AI systems are interconnected loops of data pipeline, training stack, inference stack, and feedback loop; (4) LLM evaluation requires both task metrics and human evaluation or LLM-as-a-judge. Created/updated 16 concept pages: Evaluation, Benchmark, Serving, InferenceOptimization, Latency, Throughput, Quantization, KVCache, DataPipeline, TrainingStack, InferenceStack, FeedbackLoop, AISystemDesign, HumanEvaluation, LLMasJudge, DataDrift.

## [2026-05-22] ingest | LWN.net Weekly Edition for May 14, 2026 — 한국어 기술 번역

Added source. Key claims: (1) Fedora AI Developer Desktop 구상이 커뮤니티 논쟁 후 Council 승인→반대표 전환으로 중단, (2) Forgejo carrot disclosure가 비표준 취약점 공개 방식으로 비판과 반론 모두 촉발, (3) Andrew Morton 메모리 관리 유지관리 은퇴正式开始, David Hildenbrand 인수, (4) 커널 7.1-rc3 대규모 개발 사이클 (2,141명 기여자, 13,922 changeset), (5) Dirty Frag LPE 취약점 공개로 엠바고 깨짐, (6) Debian 재현 가능한 빌드 의무화. Created 8 entity pages (Fedora, Forgejo, AndrewMorton, DavidHildenbrand, DirtyFrag, LSFMM+BPF 2026, DAMON, JulienVoisin) and 8 concept pages (CarrotDisclosure, TransparentHugePage, DMAbuf, MemoryManagement, VulnerabilityDisclosure, ReproducibleBuilds, Mshare, KernelKillswitch).

## [2026-05-22] ingest | AI/ML Learning Review — Day 30 (2026-05-22): Evaluation, Serving, and AI System Design

Added source. Key claims: AI system design requires four pillars (data pipeline, training stack, inference stack, feedback loop); model evaluation differs from training loss; benchmarks measure specific tasks, not overall capability; serving optimization balances latency and throughput; quantization trades accuracy for efficiency. Created 12 concept pages for Evaluation, Serving, Latency, Throughput, Quantization, KVCache, Batching, Streaming, DataPipeline, TrainingStack, InferenceStack, and FeedbackLoop.

## [2026-05-21] ingest | AI/ML Learning Review — Day 29 (2026-05-21): RAG, Embedding Search, Prompt Engineering

Added source. Key claims: RAG는 검색-생성 결합으로 LLM의 최신 정보 활용과 hallucination 감소; EmbeddingModel은 문장 의미를 벡터로 표현하여 키워드 없이도 의미 검색 가능; PromptEngineering은 답변 방향 조절과 모델 지식 한계 보완을 위한 인터페이스다. 관련 concept pages updated/created: RAG, EmbeddingModel, VectorSearch, PromptEngineering, Hallucination, Chunking, CosineSimilarity, ContextWindow, ToolUse, FineTuning, VectorDatabase, NearestNeighborSearch, ApproximateNearestNeighborSearch, EmbeddingSpace, FewShotPrompting, PromptSensitivity, InstructionDesign, SystemPrompt.

## [2026-05-20] ingest | LWN.net Weekly Edition for May 7, 2026 기술 번역

Added source manually after LLM-backed ingest failed with an upstream streaming RemoteProtocolError on the large translated report. Key claims: LLM-driven vulnerability reports pressure coordinated disclosure/embargo workflows; Linux rseq/TCMalloc discussion reinforces userspace ABI regression rules; Fedora GNOME bug-monitoring policy illustrates downstream maintenance expectations; Prolly trees support version-controlled databases; s390 Arm VMs improve cross-architecture virtualization testing; weekly security updates and kernel patch lists provide operational signal.

## [2026-05-20] ingest | PhysBrain 1.0 기술 보고서: 인간 egocentric video에서 물리 상식 supervision을 추출해 VLA로 전이하기 — learning

Added source. Key claims: egocentric video → structured meta-record → [[PhysicalQA]] → [[CapabilityPreservingAdaptation]] → [[VLA]] transfer pipeline. Created 6 concept pages: [[PhysicalCommonsense]], [[CapabilityPreservingAdaptation]], [[PhysicalQA]], [[ActionGrounding]], [[LanguageSensitiveAdaptation]], [[StructuredMetaRecord]]. Related to existing PhysBrain analysis/learning sources.

## [2026-05-20] ingest | PhysBrain 1.0 기술 보고서: 인간 egocentric video에서 물리 상식 supervision을 추출해 VLA로 전이하기 — references

Added source. Key claims: PhysBrain 1.0의 10개 레퍼런스 정리 — [[VLA]] 정책 baseline([[OpenVLA]], [[Pi0]], [[GR00T-N1]]), egocentric video 데이터셋([[Ego4D]], [[EgoDex]], [[EPIC-KITCHENS]]), depth 추정([[VGGT]]), 평가 벤치마크([[SimplerEnv]], [[LIBERO]], [[RoboCasa]]).

New entity pages: [[OpenVLA]], [[Pi0]], [[GR00T-N1]], [[EgoDex]], [[VGGT]], [[SimplerEnv]], [[LIBERO]], [[RoboCasa]], [[PhysicalIntelligence]].

New concept pages: [[VLA Policy]], [[Physical Commonsense Supervision]], [[Egocentric Video]].

## [2026-05-20] ingest | PhysBrain 1.0 기술 보고서: 인간 egocentric video에서 물리 상식 supervision을 추출해 VLA로 전이하기 — analysis

Added source. Key claims: PhysBrain 1.0은 VLM→VLA adaptation에서 physical commonsense를 Egocentric video에서 structured QA로 추출해 주입하는 'physical prior → action grounding' 접근을 제안. Capability-preserving adaptation으로 VLM capability를 유지하면서 VLA policy로 전이. VLM benchmark(ERQA, PhysBench)와 VLA benchmark(SimplerEnv, LIBERO, RoboCasa)를 함께 평가하여 action grounding 효과를 검증.

Created concept pages: [[VLA]], [[PhysicalCommonsense]], [[CapabilityPreservingAdaptation]], [[EgocentricVideo]]

## [2026-05-20] ingest | PhysBrain 1.0 기술 보고서: 인간 egocentric video에서 물리 상식 supervision을 추출해 VLA로 전이하기

Added source. Key claims: (1) Human egocentric video를 structured physical QA supervision으로 변환하는 Data Engine 설계, (2) Capability-preserving VLA adaptation으로 catastrophic forgetting 방지, (3) Limited robot data로도 physical prior transfer 가능. Related pages: [[physbrain-1-0-2605-15298]], [[PhysicalCommonsenseSupervision]], [[CapabilityPreservingAdaptation]], [[ShijieLian]], [[KaiChen]]. Connected to [[HumanNet]], [[MobileEgoAnywhere]], [[VLA]].

## [2026-05-20] ingest | MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라 — learning

Added source. Key claims: (1) VLA scaling의 핵심 병목은 data coverage이며, (2) smartphone은 commodity sensor suite로 RGB-D/IMU/camera pose를 동시에 제공, (3) STERA 파이프라인으로 3D hand trajectory와 hierarchical language instruction 추출, (4) MobileEgo는 VLA pretraining과 human-to-robot retargeting의 bridge 역할. Created 9 concept pages: [[VLA]], [[EgocentricVision]], [[Ego4D]], [[UMI]], [[EgoScale]], [[WiLoR]], [[MANO]], [[MCAP]], [[LongHorizonTrajectory]]. No contradictions detected.

## [2026-05-20] ingest | MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라 — references

Added source. Key claims: 10개 관련 논문 레퍼런스 정리 (EgoScale, UMI, Ego4D, EPIC-KITCHENS, Ego-Exo4D, HOI4D, HOT3D, ARCTIC, WiLoR, MCAP). 기존 [[mobileego-anywhere-2605-05945]] 소스와 일관됨. Egocentric vision/hand tracking/dexterous manipulation 데이터셋 생태계 확장.

New entity pages: EgoScale, UMI, Ego-Exo4D, HOI4D, HOT3D, ARCTIC, WiLoR, MCAP
New concept pages: EgocentricVideoDataset, HandTracking, DexterousManipulation

## [2026-05-20] ingest | MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라 — analysis

Added source. Key claims: iPhone 기반 200시간 egocentric dataset + STERA 파이프라인으로 VLA 학습용 long-horizon trajectory 수집 인프라 공개. 354세션, pose drift <1cm, hand pose 86.2% detection. 주요 entities: MobileEgo Anywhere, STERA. 주요 concepts: EgocentricDataCollection, LongHorizonTrajectory, ActionGrounding, HandPoseEstimation, HierarchicalTaskInstruction.

## [2026-05-20] ingest | MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라

Added source. Key claims: commodity smartphone(LiDAR iPhone Pro) 기반 200시간 egocentric dataset 공개, 평균 21.2분/최장 108분 session, ARKit pose drift 0.1% 미만, STERA processing pipeline로 3D hand trajectory/atomic action labels/hierarchical instruction 생성. Authors 5명(SenthilPalanisamy, AbhishekAnand, SatpalSinghRathor, PratyushPatnaik, ShubhanshuKhatana) entity page 생성. Concepts: [[EgocentricData]], [[STERA]], [[LongHorizonTrajectory]], [[HandTrajectory]] page 생성.

## [2026-05-20] ingest | AI/ML Learning Review — Day 28 (2026-05-20): Foundation Model, Transfer Learning, Multimodal

Added source covering Foundation Model paradigm, PEFT/LoRA parameter-efficient fine-tuning, and multimodal model architecture with cross-modal alignment.

Key claims:
- Foundation models enable transfer learning by pre-training on massive data then adapting to downstream tasks
- LoRA achieves 92%+ parameter reduction by learning low-rank A,B matrices instead of full weight updates
- Cross-modal alignment connects different modalities in shared embedding space via cosine similarity
- Created concept pages: [[FoundationModel]], [[TransferLearning]], [[PEFT]], [[LoRA]], [[MultimodalModel]], [[VisionLanguageModel]], [[CrossModalAlignment]]

## [2026-05-19] ingest | AI/ML Learning Review — Day 27 (2026-05-19): Decoding Strategies, Context Window, Hallucination/Calibration/Grounding

Added source. Key claims: (1) decoding strategies (greedy, beam search, temperature, top-k, top-p) control creativity/accuracy balance without changing model knowledge; (2) context window is max tokens LLM can process, KV cache enables fast generation but consumes memory; (3) hallucination arises from next-token-prediction training objective, grounding and calibration mitigate trustworthiness issues. Created 10 concept pages: [[GreedyDecoding]], [[BeamSearch]], [[Temperature]], [[TopK]], [[TopP]], [[ContextWindow]], [[KVCache]], [[Hallucination]], [[Calibration]], [[Grounding]].

## [2026-05-18] ingest | AI/ML Learning Review — Day 26 (2026-05-18): Scaling Laws, Instruction Tuning, RLHF

Added source. Key claims: Scaling laws define predictable performance relationships with model size, data, and compute; SFT teaches instruction-following through curated examples; RLHF and preference optimization align model outputs with human preferences using reward models and policy optimization.

## [2026-05-17] ingest | AI/ML Learning Review — Day 25 (2026-05-17): LLM Baseline Learning Pipeline

Added source. Key claims: 1) [[NextTokenPrediction]] is the core objective for GPT-style models and requires [[Autoregressive]] token-by-token generation, 2) [[Tokenization]] and especially [[Subword]]/[[BytePairEncoding]] directly control OOV handling and sequence-length cost, and 3) [[Pretraining]] is largely [[SelfSupervisedLearning]] driven with objective-loss-optimizer loops that shape downstream model behavior.

## [2026-05-16] ingest | AI/ML Learning Review — Day 24

Added source covering three Transformer fundamentals: [[CausalMask]] and [[PaddingMask]] for attention masking, [[EncoderDecoderAttention]] for input-output connection, and [[TransformerParallelism]] with its [[QuadraticComplexity]] trade-offs. Created 8 concept pages for masking types, cross attention, memory, parallelism, and inference concepts (KVCache). No contradictions with existing wiki content.

## [2026-05-15] ingest | AI/ML Learning Review — Day 23 (2026-05-15): Residual Connection, LayerNorm, Position-wise FFN

Added source covering three Transformer block stabilization components: ResidualConnection, LayerNorm, and PositionWiseFFN. Created 7 concept pages: ResidualConnection, LayerNorm, PositionWiseFFN, SkipPath, PreLN, PostLN, and updated overview to connect Day 23 with prior Transformer learning days. No contradictions detected.

## [2026-05-14] ingest | AI/ML Learning Review — Day 22: Transformer Block, Multi-Head Attention, Positional Encoding

Added source. Key claims: TransformerBlock combines attention + FFN + residual + LayerNorm; MultiHeadAttention enables diverse relationship patterns via parallel heads; PositionalEncoding is essential for order awareness since self-attention processes tokens simultaneously. Created concept pages for [[TransformerBlock]], [[MultiHeadAttention]], [[PositionalEncoding]], [[FeedForwardNetwork]], [[ResidualConnection]], and [[LayerNorm]]. Aligned with previous days covering [[Attention]], [[QKV]], and [[SelfAttention]].

## [2026-05-13] update | Hugging Face Weekly Papers W20/W19 refresh

Selected and processed two new papers: HumanNet (2605.06747, 2026-W20) and ReflectDrive-2 (2605.04647, 2026-W19). Added Korean translation, analysis, references, learning notes, figures, wiki source pages, entity/concept pages, placeholder pages for wikilink integrity, and rebuilt graph artifacts with --no-infer fallback after semantic inference failed.

## [2026-05-13] ingest | ReflectDrive-2: 이산 Diffusion Driving을 위한 강화학습 정렬 Self-Editing — references

Added source. Key claims: References page for ReflectDrive-2 (arXiv 2605.04647) documenting 10 key related works including DriveFine (closest prior), LLaDA (discrete diffusion LM foundation), NAVSIM (evaluation benchmark), UniAD/TransFuser (E2E AD baselines), and AutoVLA/ReCogDrive (VLA planner peers). Created entity pages for DriveFine, LLaDA, NAVSIM, UniAD, TransFuser, AutoVLA, ReCogDrive. Created concept pages for MaskedDiffusion, E2EAutonomousDriving, VLA, ClosedLoopPlanning.

## [2026-05-13] ingest | ReflectDrive-2: 이산 Diffusion Driving을 위한 강화학습 정렬 Self-Editing — analysis

Added source. Key claims: ReflectDrive-2는 Decision-Draft-Reflect 파이프라인으로 VLA planner의 editable trajectory generation을 구현, masked discrete diffusion draft + AutoEdit rewrite + RL closed-loop reward 정렬, NAVSIM 91.0 PDMS, NVIDIA Thor ~30ms latency 달성. Created entity page for [[ReflectDrive2]], concept pages for [[DecisionDraftReflectPipeline]], [[DiscreteDiffusion]], [[AutoEdit]], [[ClosedLoopReward]].

## [2026-05-13] ingest | ReflectDrive-2: 이산 Diffusion Driving을 위한 강화학습 정렬 Self-Editing

Added source. Key claims: (1) Masked discrete diffusion + AutoEdit로 editable trajectory generation, (2) Supervised perturbation recovery만으로는 self-editing gain이 작아 RL reward-coupled draft-and-edit rollout 필수적, (3) NAVSIM에서 camera-only 91.0 PDMS, best-of-6 oracle 94.8 PDMS, (4) Shared-prefix KV reuse, ASD, fused unmasking으로 NVIDIA Thor ~30ms latency 달성. New entity pages: NAVSIM. New concept pages: MaskedDiscreteDiffusion, AutoEdit, DecisionDraftReflectPipeline, RLAlignment, EfficientInference.

## [2026-05-13] ingest | HumanNet: 인간 중심 비디오 학습을 100만 시간 규모로 확장하기 — learning

Added source. Key claims: HumanNet 100만 시간 코퍼스로 VLA 사전학습 데이터 병목 해소, egocentric video가 VLA에 중요(손-물체 접촉/intent 직접 담김), embodiment gap으로 robot-specific post-training 여전히 필요, closed-loop evaluation 추가 필요.

Created: 5 concept pages (HumanCentricVideo, EgocentricVideo, ExocentricVideo, InteractionCentricAnnotation, EmbodimentGap).

## [2026-05-13] ingest | HumanNet: 인간 중심 비디오 학습을 100만 시간 규모로 확장하기 — references

Added source. Key claims: HumanNet(arXiv 2605.06747)의 참고 문헌을 정리하며, [[Ego4D]], [[EPIC-KITCHENS]], [[Ego-Exo4D]], [[HOI4D]] 등 egocentric video 데이터셋과 [[Open X-Embodiment]], [[DROID]] 등 로봇 데이터셋, [[R3M]], [[EgoMimic]] 등 인간-로봇 전이 연구를 포괄. 읽기 우선순위로 (1) R3M/EgoMimic, (2) Ego4D/Ego-Exo4D, (3) Open X-Embodiment/DROID, (4) GR00T/LingBot-VLA를 제시.

New entity pages: [[Ego4D]], [[EPIC-KITCHENS]], [[Ego-Exo4D]], [[HOI4D]], [[Open X-Embodiment]], [[DROID]], [[R3M]], [[EgoMimic]], [[GR00T-N1]], [[LingBot-VLA]]

New concept pages: [[EgocentricVideo]], [[VLA]], [[ImitationLearning]], [[RobotFoundationModel]]

Contradictions: none

## [2026-05-13] ingest | HumanNet: 인간 중심 비디오 학습을 100만 시간 규모로 확장하기 — analysis

Added source. Key claims: VLA 데이터 부족 문제 해결을 위한 100만 시간 human-centric video corpus 제안, egocentric/exocentric viewpoint taxonomy, pose/motion/caption annotation, [[Qwen]]/[[LingBot-VLA]]로 transfer value 검증. Created entity pages for [[Qwen]], [[LingBot]], concept pages for [[VLA]], [[Embodied AI]], [[HumanNet]]. Updated overview with embodied AI and VLA trends.

## [2026-05-13] ingest | HumanNet: Scaling Human-centric Video Learning to One Million Hours

Added source. Key claims: 100만 시간 규모 human-centric video corpus로 VLA pretraining 데이터 병목 해결, 1,000시간 egocentric pretraining ≈ 100시간 robot data 성능. Created entity pages for [[DAGroupPKU]], [[YufanDeng]], [[DaquanZhou]], [[LingBotVLA]]. Created concept pages for [[HumanNet]], [[HumanCentricVideo]], [[EmbodiedIntelligence]], [[MotionAwareLearning]], [[InteractionAwareLearning]], [[RobotReadySubset]]. Updated overview with embodied AI/VLA 관련 섹션.

## [2026-05-13] ingest | AI/ML Learning Review — Day 21: QKV, Scaled Attention, Self-Attention

Added source covering Transformer attention fundamentals. Key claims: QKV separates query (what I'm looking for), key (search tags), and value (actual content); Scaled Dot-Product Attention uses sqrt(d_k) to prevent softmax from becoming too extreme; Self-Attention enables tokens to reference each other for context-dependent representations. Created 13 concept pages: Query, Key, Value, ScaledDotProductAttention, SelfAttention, TokenInteraction, ContextMixing, AttentionWeight, ContextualEmbedding, MultiHeadAttention, Softmax, DotProduct, CompatibilityScore.

## [2026-05-12] ingest | AI/ML Learning Review — Day 20: LSTM/GRU, Embedding, Attention

Added source covering three foundational sequence modeling concepts. Key claims:
- LSTM/GRU gates (0-1 sigmoid values) provide selective memory by controlling information flow
- Embedding compresses tokens into dense vectors capturing semantic relationships
- Attention mechanism enables dynamic information selection via query-key-value weighted sums

Created entity pages: [[LSTM]], [[GRU]], [[Embedding]], [[AttentionMechanism]], [[VanishingGradient]], [[CellState]], [[HiddenState]]

Updated overview.md to reflect Day 19-20 sequence modeling foundation and curriculum progression.

Part of ongoing AI/ML learning series (currently Day 20/30, milestone: sequence models and attention)

## [2026-05-11] ingest | AI/ML Learning Review — Day 19 (2026-05-11): Sequence Models, RNN, BPTT

Added source covering sequence data and autoregressive modeling, RNN hidden state and recurrence, BPTT and long-term dependency problem. Created concept pages: Autoregressive, RNN, BPTT, LongTermDependency, VanishingGradient, HiddenState, SequenceModel. Key claims: autoregressive models predict P(next token | context); RNN hidden state compresses past info via recurrence; BPTT gradients vanish over many time steps, motivating attention and Transformer.

## [2026-05-10] ingest | EmbodiedMidtrain study guide

Added source. Key claims: [[EmbodiedMidtrain]] improves [[VLA]] transfer by selecting VLM samples with high target alignment via [[ProximityEstimator]], rather than relying only on scale or full fine-tuning.
Compared against baseline [[VLA]] settings, the source reports consistent gains on [[Calvin]], [[SimplerEnv]], and [[LIBERO]] for both [[InternVL3.5|InternVL3.5-1B]] and [[Qwen3VL|Qwen3VL-2B]].
It also links performance interpretation to [[DistributionShift]], [[RepresentationAlignment]], and sample-level quality effects even when training loss is similar.

## [2026-05-10] ingest | EmbodiedMidtrain references and related work notes

Added source. Key claims: 정답형 모델 스케일보다 target 분포 정렬이 중요하며, [[ProximityEstimator]] 기반 sample-level [[DataSelection]]과 [[MidTraining]]이 [[RobotManipulation]] 벤치에서 성능을 유의미하게 개선한다. 또한 [[EmbodiedMidtrain]]의 관련 연구 맥락을 [[RefSpatial]], [[EmbSpatial-Bench]], [[Robo2VLM]], [[RoboPoint]], [[VLM4VLA]] 등으로 정리하고, 백본 간 전이 가능성까지 연결해 기록했다.

## [2026-05-10] ingest | EmbodiedMidtrain: VLM과 VLA 사이의 간극을 Mid-training으로 잇기

Added source. Key claims: distribution alignment is a first-order lever in robotics adaptation; VLM pretraining scale alone is insufficient; sample-level [[DataSelection]] with lightweight [[ProximityEstimator|proximity scoring]] improved Calvin, SimplerEnv-Bridge, and LIBERO-10 under [[VLA]] fine-tuning; and smaller backbones can remain competitive when adaptation data is well aligned.

## [2026-05-10] ingest | LilysAI bulk ingest maintenance

Created 184 placeholder concept pages for wikilink integrity and auto-indexed 225 generated pages after recent LilysAI imports.

## [2026-05-10] ingest | Unveiling the Inner Workings of IREE: An MLIR-Based Compiler for Diverse H/W

Added source. Key claims: [[IREE]]’s MLIR-based stack combines [[Host-Device Programming Model]], [[Progressive Lowering]], and [[HAL]] for heterogeneous hardware deployment; [[VMFB]] is its key deployment artifact; default scheduling and transform/plugin extensibility are central, while full out-of-box parity and auto-tuning in heterogeneous settings remain active work items.

## [2026-05-10] ingest | QEMU 에뮬레이터 내부 구조: TCG, 메모리, 디바이스 모델링 및 디버깅

Added source. Key claims: [[QEMU]] 동작의 중심은 [[TCG]] 기반 동적 바이너리 변환이며, `Translation Block` 캐시와 체이닝으로 성능을 확보한다. 장치 모델은 [[QOM]]/[[TypeInfo]]/[[ObjectClass]] 기반으로 생성·초기화·등록되며, [[PCI]] 장치 주입·BAR 콜백은 사용자 공간 상호작용 검증에 직접 활용된다. 메모리 서브시스템은 [[SoftMMU]]-[[AddressSpace]]-[[MemoryRegion]]-[[RAMBlock]]으로 게스트 물리주소를 호스트 주소로 연결한다. 디버깅은 QEMU 프로세스 GDB와 게스트 커널 GDB 경로를 분리해 실행된다.

## [2026-05-10] ingest | 2025 EuroLLVM - Deep Dive into the MLIR to LLVM IR Translation Mechanism

Added source. Key claims: [[MLIR]]는 초기에는 [[LLVM]] 호환성 중심의 단순 번역으로 출발했으나, GPU/가속기/OpenMP 확장으로 [[Dialect]]-[[Interface]] 기반 하향 구조로 진화했다. 핵심 번역 훅(`translateOperation`, `amendOperation`, `convertParameter`)과 [[LLVMTranslationDialectInterface]]로 다이얼렉트 책임이 분산되었고, 다이얼렉트 과잉 추가가 성능/인지/유지보수 비용을 키우는 점이 주요 경고로 제시되었다.

## [2026-05-10] ingest | Tesla's Shift to End-To-End Deep Learning: Full Breakdown

Added source. Key claims: 2021년 [[Tesla]]는 [[HydraNet]] 중심의 모듈형 인지-계획 분리 구조를 사용했고, 2022년에는 [[OccupancyNetwork]]와 [[OccupancyFlow]]를 통해 3D 공간 점유 기반 인지를 강화했으나 planning 규칙이 남아 있었다. FSD v12 단계에서 [[EndToEndDeepLearning]] 전환을 통해 [[Perception]]과 [[Planning]]을 하나의 목표로 함께 최적화해 [[EndToEndAutonomy]] 정합을 높였고, 기존 모듈도 완전 폐기보다 진단·미세조정 가능한 하위 구성요소로 유지한다.

## [2026-05-10] ingest | Tesla's Occupancy Networks: A look at How They Work

Added source. Key claims: Tesla applies an occupancy-first 3D representation to replace fixed-box/object-class limitations, introduces voxel-based [[OccupancyGrid]] reasoning plus [[OccupancyFlow]] for dynamics, and uses [[NeuralRadianceField]]-based reconstruction checks to improve robustness in ambiguous and long-tail driving conditions.

## [2026-05-10] ingest | Tesla’s AI Can EXPLAIN Itself?! Ashok’s Mind-Blowing FSD Demo

Added source. Key claims: [[Tesla]] FSD는 자연어 판단 설명 가능성, [[System1]]/[[System2]] 기반 이원 판단, 및 [[WorldSimulator]] 기반 폐쇄루프 시나리오 학습을 통해 엣지 케이스 대응과 해석 가능한 안전성 확보를 강화한다.

## [2026-05-10] ingest | NVIDIA GR00T vs Gemini Robotics vs Physical Intelligence π: VLA 모델 3대장 비교 분석

Added source. Key claims: 휴머노이드 중심의 [[NVIDIAGR00T]], [[ThinkingBeforeActing]]/[[MotionTransfer]] 중심의 [[GeminiRobotics]], 그리고 범용 정책 중심의 [[PhysicalIntelligencePi]]가 각각 데이터, 추론-행동 분할, 지식 보존을 통해 [[VLA]] 로봇 AI의 일반화·확장성 문제를 서로 다르게 해결한다. 또한 세 모델 모두 [[CrossEmbodimentTransfer]] 성능을 핵심 제약으로 공유한다.

## [2026-05-10] ingest | Ashok Elluswamy: Building Foundational Models for Robotics at Tesla

Added source. Key claims: [[Tesla]]은 [[EndToEndAutonomy]] 기반으로 센서-제어 직접 매핑 파이프라인을 강화하고, [[WorldSimulator]] 기반 폐쇄루프 검증으로 안전성과 long-tail 강건성을 점검한다. 또한 동일한 파운데이션을 [[Optimus]]와 [[Cybercab]] 같은 로보틱스/이동성 서비스로 확장 가능하다는 확장 전략을 제시한다.

## [2026-05-10] ingest | A Peek into Tesla’s Autonomous Future: Core Tech Revealed by VP Ashok Elluswamy at ICCV25 WDFM-AD

Added source. Key claims: [[Tesla]]의 핵심 자율주행 방향이 단일 대규모 [[EndToEndAutonomy]]로 수렴하며, 모듈식 파이프라인의 인터페이스 손실을 줄이고 규칙 기반 설계 한계를 극복하려 한다는 점을 반영했다. 대규모 센서 데이터와 폐쇄루프 [[Simulation]] 기반 검증으로 희귀 시나리오 처리 능력 및 선제적 안전 제어를 강화하고, 동일 기술을 [[Cybercab]]·[[Optimus]]로 확장하는 로보틱스 확장성을 정리했다.

## [2026-05-10] ingest | 삼성 성과급 논쟁, 진짜 문제는 따로 있다 | 김지형 경제사회노동위원회 위원장 [신과대화]

Added source. Key claims: 삼성 성과급 쟁점은 단순 노사 분쟁이 아니라 주주와 이해관계자 분배 구조의 사회적 쟁점이다; [[사회적대화]]를 권리 다툼형에서 미래 과제 해결형인 [[사회적대화 2.0]]으로 전환해야 한다; AI 초과이익 배분 및 인구·일자리 전환 정책이 핵심 후속 의제다.

## [2026-05-10] ingest | 매도했다면 미련을 버리세요...여러 섹터가 주도하는 진짜 강세장 대처법 | 박병창 교보증권 자산관리전략부 이사 [여의도 인사이트]

Added source. Key claims: 시장에서 FOMO 추격매수의 위험과 주도섹터 순환의 중요성을 정리하고, 매도 후 미련(후회) 제거와 빠른 재의사결정을 통한 규율투자 원칙을 제시함.

## [2026-05-10] ingest | ARKInvest Big Ideas 2026

Added source. Key claims: [[ARKInvest]]의 10번째 연례 보고서인 [[ARKInvest Big Ideas 2026]]은 [[AI]]가 [[PublicBlockchain]], [[Robotics]], [[EnergyStorage]], [[Multiomics]]과 결합해 혁신 속도를 가속하며 거시경제 성장률 및 자본 구조에 구조적 변화를 만들 수 있다고 정리한다. 핵심은 단기 노이즈 대응이 아닌 장기 혁신 플랫폼 결합이다. 보고서에는 재사용 [[Rocket]] 기반 [[SpaceBasedAIComputing]], 휴머노이드 확산의 GDP 임팩트, AI 칩 수요가 촉진하는 자본 형성 가속, 양자컴퓨팅의 상대적 지연 논의가 포함된다.

## [2026-05-10] ingest | 그만 알아야할만 안드레 카파시 30분 인터뷰 완전정리 - AI시대의 필요 인스터스

Added source. Key claims: 
- [[AndrejKapassi]]는 AI 생산성에서 [[Thinking]]은 모델에 위임 가능하지만 [[Understanding]]은 인간이 유지해야 하는 핵심 역량으로 구분했다.
- [[Software 1.0]], [[Software 2.0]], [[Software 3.0]] 전이를 통해 AI 코딩은 단순 코드 작성에서 [[Prompting]]과 [[ContextWindow]] 중심의 패러다임으로 이동한다.
- [[LLM]]은 채점 가능한 영역에서 강력하지만 [[JaggedIntelligence]]로 인해 비일관성이 존재해 인간 감독과 [[Verifiability]]가 필수다.
- [[NeuralComputer]] 관점에서 향후 많은 앱/워크플로우가 신경망 기반 실행으로 대체될 수 있다는 장기 예측을 제시한다.
- [[AI 시대의 인간 가치]] 관점에서 미학, 판단, 감독, 스펙 설계 능력은 여전히 사람 중심 역량으로 남는다.

## [2026-05-10] ingest | The Coding Assistant Breakdown: More Tokens Please

Added source. Key claims: (1) [[GPT-5.5]]은 복잡한 추론 작업에서 강점이 있어 Codex 계열의 정밀 구현에 적합하고, (2) [[Claude Opus 4.7]]은 사용자 의도 추론과 개방형 작업에서 강해 초기 계획/스캐폴딩에 유리하며, (3) 실사용에서는 벤치마크 수치보다 [[SWE-bench]]/[[SWE-bench Verified]]/[[SWE-bench Pro]] 계열의 하네스 편향을 고려한 하이브리드 운영이 더 중요하다는 점을 강조한다.

## [2026-05-10] ingest | HC2022.Google.Pienaar.v1.pdf

Added source. Key claims: [[MLIR]]은 트리/그래프/저수준 IR을 하나의 점진적 저수준화 체계로 통합하고, [[Parsimony|파시모니]]·[[Traceability|추적성]]·[[Progressivity|점진성]]을 핵심 원칙으로 한 모듈형 컴파일러 인프라를 제시한다. 도메인 특화 IR이 반복 재구현해 온 비용과 진단/패스 중복 문제를 줄이기 위해 [[Dialect]], [[Operation]], [[Pass]], [[Pattern]], [[TableGen]] 기반의 조합을 강조한다.

## [2026-05-10] ingest | EP 96. LLM 추론 인프라와 토큰 경제학

Added source. Key claims: [[LLM]] 추론은 [[t_compute]]와 [[t_memory]] 병목의 최댓값이 지연·비용을 결정하며, [[Transformer]]의 [[Prefill]]/[[Decode]] 구분, [[KVCache]] 운용, [[Roofline Analysis]] 기반 배치 최적화, 그리고 [[TokenEconomy]]가 실제 가격·수익성의 핵심 연결 고리임을 정리한다.

## [2026-05-10] ingest | Andrej Karpathy: From Vibe Coding to Agentic Engineering

Added source. Key claims: This source reframes [[VibeCoding]] as a low-barrier entry path, while introducing [[AgenticEngineering]] for production-grade AI work via [[Software 3.0]], [[Prompting]], and strong [[Verifiability]] boundaries. It emphasizes [[JaggedIntelligence]], [[DistributionShift]], and the persistent need for human judgment, taste, and supervision in AI software workflows.

## [2026-05-10] ingest | 99%가 모르는 하네스 엔지니어링 — AI 에이전트 생산성을 10배 올리는 세팅법

Added source. Key claims: AI productivity is improved by separating planning and execution through [[HarnessEngineering]], using [[Task]]/[[TaskPhase]] decomposition for context-safe automation, and enforcing documentation-first change control via [[docs_diff]] before review and merge. The source also highlights that humans must retain control over planning, implicit knowledge transfer, and final decision quality, while [[AI에이전트]] executes repetitive implementation/review workflow loops.

## [2026-05-10] ingest | Code with Claude 2026: Opening Keynote

Added source. Key claims: Anthropic introduced [[MultiAgentOrchestration]], [[Outcomes]], and [[Dreaming]] in [[Claude Managed Agents]] to scale autonomous execution quality; [[ClaudeCode]] evolved toward asynchronous developer workflows with [[Routines]], [[Autofix]], and remote-control support; API and infrastructure updates target production gaps between AI capability and real deployment.

## [2026-05-10] ingest | AI/ML Learning Review — Day 18

Added source covering CNN channels/feature maps/filters, pooling/downsampling, and Residual Networks. Created concept pages for ChannelFeatureMapFilter, PoolingDownsampling, and ResidualNetwork. Updated overview to reflect new CNN concepts and their connections to Transformers and LLMs.

## [2026-05-09] ingest | AI/ML Learning Review Day 17 (2026-05-09)

Added source. Key claims: Learning curves for diagnosing overfitting/underfitting; CNN local connectivity via local receptive fields and parameter sharing; convolution operation with kernel, stride, padding. Created concept pages for [[LearningCurves]], [[ConvolutionalNeuralNetworks]], [[Convolution]], and [[EarlyStopping]]. Updated overview to include these concepts.

## [2026-05-08] ingest | AI/ML Learning Review Day 16 (2026-05-08)

Added source covering epoch/iteration/batch size, BatchNorm, and Dropout. Updated or created concept pages for Epoch, Iteration, BatchSize, BatchNormalization, Dropout, Regularization, Overfitting, InternalCovariateShift, GradientAccumulation, LayerNormalization, and ResNet. Updated overview with Day 16 training mechanics.

## [2026-05-07] ingest | AI/ML Learning Review Day 15 (2026-05-07)

Added source. Key claims: clarified [[RepresentationLearning]] and [[LatentRepresentation]] as core of deep models, linked learnable feature learning to practical image/text robustness, introduced [[Initialization]] as a stability control axis (including [[SymmetryBreaking]], [[XavierInitialization]], [[HeInitialization]]), and formalized [[VanishingGradient]]/[[ExplodingGradient]] behavior through chain-rule multiplicative intuition with examples 0.5 and 2. Added updated concept pages for [[RepresentationLearning]], [[LatentRepresentation]], [[LatentSpace]], [[Initialization]], [[SymmetryBreaking]], [[XavierInitialization]], [[HeInitialization]], [[VanishingGradient]], [[ExplodingGradient]], and [[GradientClipping]].

## [2026-05-06] ingest | AI/ML Learning Review Day 14 (2026-05-06)

Added source. Key claims: Forward pass is the computation flow from input to output; backpropagation computes gradients via chain rule; parameters (weights and biases) are learnable values adjusted during training.

## [2026-05-05] ingest | 2026-05-05 AI/ML Learning Day 13 — Perceptron, MLP, Activation Functions

Added source. Key claims: Perceptron performs linear combination with weights and bias; MLP stacks layers with nonlinearities to learn complex patterns; activation functions are essential for nonlinearity; ReLU, sigmoid, tanh discussed; sigmoid saturation can hinder gradient-based learning.

## [2026-05-04] ingest | 2026-05-04 AI/ML Learning Day 12 — Random Forest, Boosting, PCA

Added source covering classical ML models: Random Forest, Boosting, PCA. Created concept pages for RandomForest, Boosting, PCA, Ensemble, Bootstrap, Bagging, GradientBoosting, AdaBoost, DimensionalityReduction. Updated overview with new section on classical ML foundations.

## [2026-05-03] ingest | Raw corpus catch-up and graph refresh

- Ingested raw markdown files that had no wiki source page, including Finance, NVIDIA/CUDA, NPU, Technology, Health, AI, and VLA study documents.
- Rebuilt wiki/index.md from current wiki pages to restore page coverage.
- Patched source_file paths for nested raw directories so future refresh checks can match raw documents correctly.

## [2026-05-03] ingest | Week 01. VLA for AD 지형도와 taxonomy

Added source. Key claims: VLA for autonomous driving should be read through the VA -> End-to-End VLA -> Dual-System VLA taxonomy; action grounding is the decisive criterion; closed-loop safety and long-tail robustness matter more than text-only metrics.

## [2026-05-03] ingest | VLA for Autonomous Driving Weekly Study Template

Added source. Key claims: this is a reusable weekly-study template for [[VisionLanguageActionForAutonomousDriving]] that standardizes translation, architecture analysis, [[ActionGrounding]], [[Evaluation]], critique, and follow-up questions with a [[MermaidDiagram]]-based visual map.

## [2026-05-03] ingest | VLA for Autonomous Driving Weekly Study

Added source. Key claims: the corpus defines a weekly VLA-for-autonomous-driving workflow, centers closed-loop and safety-oriented analysis, and treats language as a question of action grounding versus explanation-only utility.

## [2026-05-03] ingest | Neural Network Quantization & Number Formats From First Principles

Added source. Key claims: quantization is a system-level tradeoff among accuracy, range, precision, memory traffic, and hardware cost; low-bit formats like INT8/FP8/FP16/BF16 are practical but workload-sensitive; PTQ/QAT and alternative formats such as block and log systems exist to preserve accuracy while reducing cost.

## [2026-05-03] ingest | 2512.02189

Added source. Key claims: Blackwell B200's core innovations are TMEM, 5th-generation tensor cores, and hardware decompression; the source quantifies TMEM and DE behavior with PTX microbenchmarks; it also characterizes FP4/FP6 inference paths and their latency/throughput tradeoffs.

## [2026-05-03] ingest | Part I - Intro to GPUs

Added source. Key claims: GPU design is throughput-first rather than latency-first; deep learning's practical breakthrough depended on GPU-enabled compute and memory hierarchy; CUDA/SIMT/warp execution and shared memory behavior are central to performance; tensor cores and memory optimization are the main levers for modern GPU acceleration.

## [2026-05-03] ingest | NVIDIA 인터뷰: Groq 3 LPX와 함께하는 Vera Rubin AI 심층 분석 | GTC 2026

Added source. Key claims: Vera Rubin NVL72 uses 72 Rubin GPUs and 36 Vera CPUs with NVLink 6, Groq 3 LPX handles decode FFN work in a heterogeneous inference split, and the modular tray design reduces assembly time from 2 hours to 5 minutes while lowering failure points.

## [2026-05-03] ingest | NVIDIA Tensor Core Evolution: From Volta To Blackwell

Added source. Key claims: 텐서 코어는 Volta→Turing→Ampere→Hopper→Blackwell로 세대가 갈수록 코어 크기 확장과 메모리 경로 재설계, 데이터 이동 최적화, 저정밀도 정밀도(MXFP·BF16·FP8 등) 확대로 비용/성능 효율을 개선했다. Blackwell는 TMEM 및 tcgen05.mma/MMA.2SM, 구조적 희소성의 현실적 제약(정확도·커널 성숙도) 정리를 덧붙여 텐서 코어 진화를 실무 관점으로 정리함.

## [2026-05-03] ingest | NVIDIA Hopper 아키텍처 심층 분석하기 - NVIDIA Technical Blog

Added source. Key claims: [[H100|Hopper H100]]의 4세대 [[TensorCores]], [[FP8]], [[TransformerEngine]], [[DPX]], [[ThreadBlockCluster]], [[TensorMemoryAccelerator|TMA]], 4세대 [[NVLink]]/3세대 [[NVSwitch]], [[HBM3]], [[MIG]], [[ConfidentialComputing]] 중심 개편이 AI/HPC 성능과 추론 지연 제어, 보안·격리를 동시에 확장한다.

## [2026-05-03] ingest | NVIDIA GTC 2026

Added source. Key claims: [[JensenHuang]]이 제시한 AI 시대 핵심은 [[AIFactory]], [[AgenticSystems]], [[PhysicalAI]]이며, GTC 2026은 추론 중심의 AI 인프라를 토큰 단가·처리량·지연 KPI로 재정의했다. [[VeraRubin]]/[[Blackwell]] 진화와 [[Groq3LPX]]의 이기종 추론 분리, [[DSX]] 기반 디지털 트윈 운영, [[OpenClaw]] 중심 에이전트 OS 전략을 새로 정리했다. Source file linked as nvidia-gtc-keynote-2026.

## [2026-05-03] ingest | NVIDIA Groq 3 LPX: Everything we know - StorageReview.com

Added source. Key claims: [[NVIDIA]]의 [[Groq3LPX]]를 FFN 오프로딩 기반의 랙스케일 디코드 분리 아키텍처로 정리하고, [[LPU]]의 결정론적 1D 통신/RealScale C2C 설계, [[LPXRack]]의 트레이-랙-래크 확장 트래픽 구조, 그리고 [[FFN]]/[[MoE]] 중심 오픈소스 모델(예: [[DeepSeekR1]], [[KimiK2]], [[GLM5]])의 사이징 근거를 정리하여 기존 [[HeterogeneousInference]]/[[SpeculativeDecoding]] 문맥을 보강.

## [2026-05-03] ingest | Modular: Matrix Multiplication on Blackwell: Part 2 - Using Hardware Features to Optimize Matmul

Added source. Key claims: this source details Blackwell matrix multiplication optimization using [[TensorMemoryAccelerator]], [[Tcgen05MMA]], [[TMEM]], [[Swizzling]], and [[Stmatrix]], showing up to 58x improvement over naive kernels and explicit stages of memory/compute overlap and bank-conflict mitigation.

## [2026-05-03] ingest | Introduction to Tensor Cores Programming

Added source. Key claims: AI 연산의 비용이 높은 [[MatrixMultiplication]]에서 [[TensorCores]]의 FP16-기반 텐서 연산이 핵심 가속 경로이며, [[WMMA]]와 워프/타일 전략이 실전 성능을 좌우한다. 또한 소스는 성능 측정을 [[GFLOPS]] 중심으로 정량화하고, CUDA 코어 대비 텐서 코어의 장점이 구현 패턴에 따라 달라짐을 정리했다.

## [2026-05-03] ingest | Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform

Added source. Key claims: LPX and [[VeraRubinPlatform]] form a two-engine heterogeneous inference stack that splits prefill/attention vs FFN-MoE decode responsibilities; [[NVIDIA Groq 3 LPU]] enables deterministic, low-jitter per-token behavior via compiler-orchestrated execution; [[NVIDIADynamo]] operationalizes this split with latency-aware routing and intermediate activation movement; and the structure is positioned as essential for long-context, high-concurrency, agentic workloads while expanding premium operating points on Pareto frontier terms.

## [2026-05-03] ingest | 코스피 1만 시나리오… 결국 ‘금리’에서 갈린다 | 나탈리 허 변호사 [신과대화]

Added source. Key claims: 핵심은 [[금리]]의 방향성이 한국 시장의 [[코스피]] 상방/하방을 좌우할 수 있다는 점, 미국의 중동 지정학·AI 인프라 과열 리스크가 [[사모신용]]/차입 경로를 통해 시스템적 변동성을 키울 수 있다는 점, 그리고 투자자는 삼성·하이닉스 집중 노출 완화와 에너지·방산·AI 인프라 관련 분산 배분이 필요하다는 점.

## [2026-05-03] ingest | Vibe coding in prod

Added source. Key claims: [[VibeCoding]] should be operated as an [[AIPM]]-driven workflow, with changes constrained to [[LeafNode]] areas and reliability established through [[Verifiability]] and [[TestDrivenDevelopment]], rather than exhaustive human code review. The source also adds practical production guidance on risk control, testing-first collaboration with [[Claude]], and scaling practices under accelerating AI capability growth.

## [2026-05-03] ingest | Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform

Added source. Key claims: The provided document is a missing-page notice and does not contain reusable technical content about [[NVIDIA]], [[Groq]], [[Groq 3 LPX]], or [[VeraRubin]]. Added warnings that prior LPX-specific claims from this slug should be treated as unverified until a real source document is ingested.

## [2026-05-03] ingest | How Centralized Radar Processing on NVIDIA DRIVE Enables Safer, Smarter Level 4 Autonomy

Added source. Key claims: NVIDIA DRIVE centralizes radar DSP from edge SoCs to centralized platform processing for higher fidelity [[RawADC]]-based sensing, reallocates workload to [[PVA]] while freeing [[GPU]] for cognition/planning, exposes mid-level outputs (e.g., [[RangeDopplerMap]]) for model training and multimodal fusion, and proposes a practical path for production readiness through supplier collaboration (예: [[ChengTech]]) and [[NVIDIA]] partner enablement.

## [2026-05-03] ingest | HotChips34 - Groq - Abts - final

Added source. Key claims: 1) [[Groq]]의 [[StreamingTensorProcessor|TSP]]는 소프트웨어 정의 하드웨어와 [[DeterministicExecution]]을 결합해 추론 예측성을 강화한다. 2) [[GroqChip]]은 기능 유닛 분할( [[ICU]], [[MEM]], [[VXM]], [[MXM]], [[SXM]] )과 정적/사이클 정밀 스케줄링으로 성능 편차를 줄인다. 3) [[SoftwareDefinedNetworking]] 기반 소프트웨어 스케줄링 네트워크와 [[C2C]], [[RealScale]], [[DragonflyTopology]]는 분산 TSP 동기화/부하분산의 핵심이다. 4) [[GEMM]], [[BERT]], [[Cholesky]], [[AllReduce]] 워크로드에서 배치-1 체감 지연을 중심으로 성능 특성이 강조되며, 시스템 경제성 관점으로 확장된다.

## [2026-05-03] ingest | Groq Inference Tokenomics: Speed, But At What Cost?

Added source. Key claims: [[Groq]] shows strong single-sequence and latency advantages, but [[NVIDIA]] comparison under full [[TCO]] framing can favor throughput-oriented GPU stacks under high-concurrency/batch conditions; deployment economics, batch size, concurrency, and pricing/margin assumptions are central to true inference viability.

## [2026-05-03] ingest | Deconstructing Nvidia’s Vera Rubin — The Successor To Blackwell That’s 10x More Efficient

Added source. Key claims: [[VeraRubin]]은 [[Blackwell]] 대비 성능당 전력 효율을 크게 높인 랙 스케일 시스템이며, [[NVLink]]/[[HBM4]], 액체 냉각, 대규모 공급망 정합성 및 조달 구조가 핵심이다. 단가 상승에도 토큰당 비용 절감이 가능하다는 총소유비용 관점을 제시했으며, 향후 [[VeraRubinUltra]]와 [[AMD]] [[Helios]] 경쟁 구도가 병행됨.

## [2026-05-03] ingest | CUDA Refresher: The CUDA Programming Model | NVIDIA Technical Blog

Added source. Key claims: CUDA programming model defines explicit [[Host]]/[[Device]] memory split, asynchronous [[Kernel Launch]], thread/block grid hierarchy for GPU parallelism, and a practical memory hierarchy model ([[Register]], [[Shared Memory]], [[L1 Cache]], [[L2 Cache]], [[Global Memory]]) while [[Compute Capability]] and device attributes (via [[deviceQuery]]) gate feature availability and optimization strategy.

## [2026-05-03] ingest | An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog

Added source. Key claims: [[SpeculativeDecoding]]는 드래프트-타겟 병렬 검증 구조를 통해 표준 자기회귀 디코딩의 고정 순차 병목을 완화한다. [[EAGLE3]]는 피처 기반 트리 드래프팅 헤드를 사용하고, [[DeepSeekMTP]]는 다중 헤드 다중 토큰 예측으로 드래프팅 예측을 수행한다. 실무는 [[TensorRTModelOptimizer]] 기반으로 적용 흐름이 제시되어 있으며, 수락율이 높을수록 지연 시간 절감이 커진다.

## [2026-05-03] ingest | TMEM vs Registers: How NVIDIA and AMD Feed Tensor Compute | LinkedIn

Added source. Key claims: (1) 텐서 코어 병목은 데이터 공급이며, [[NVIDIA]]는 [[TMEM]] 기반 분리형으로 비동기 텐서 파이프라인을 강화했다. (2) [[AMD]]는 [[VGPR]]/[[AGPR]] 대형 레지스터 파일로 유연성을 확보했지만 소프트웨어 복잡성이 크게 증가한다. (3) 아키텍처별 메모리 레이아웃·스케줄링 차이 때문에 최적화 패턴은 플랫폼 간 이식성이 낮다.

## [2026-05-03] ingest | NPU v0.1 Software Architecture

Added source. Key claims: Immediate launch 기반 command queue-less stack을 채택한 [[NPUv01]] v0.1 소프트웨어 설계, `riscv-ime-cpu` compiler plugin과 `nputile` external [[HAL]] driver 분리, compile-time SPM/DMA/barrier 계약 고정, 그리고 embedded ELF와 fault/trace 관측성 강화.

## [2026-05-03] ingest | NPU v0.1 PRD

Added source. Key claims: v0.1 freezes a queue-free, host immediate launch baseline for [[NPUv01]] with 2-hart tile, shared scratchpad, 3-channel DMA, and IREE/MLIR AOT ELFs; defines explicit product gates PG-01 to PG-06 plus P0-P1 product requirements; excludes command queue, preemption, virtualization, and sparse/compression in scope; identifies SPM bank conflict, IME semantic churn, and softmax/LN latency as principal risks with mitigations.

## [2026-05-03] ingest | NPU v0.1 Implementation Design

Added source. Key claims: define a single-tile baseline-first NPU bring-up plan for [[NPUv01]] with fixed scope (RTL, compiler, runtime, DV), gate execution by phase-wise regression green status, and prioritize MMIO/driver interfaces and immediate launch control over opcode freeze and late-stage preemption/virtualization work.

## [2026-05-03] ingest | NPU v0.1 ISA Specification

Added source. Key claims: [[NPUv01]] v0.1 now defines a provisional but explicit kernel-visible [[XNPUV01]] ISA, CSR/MMIO semantics, barrier/event synchronization, and AOT kernel ABI contract (`nputile_kernel_params_t`) for RV64GC+[[RVV]] 기반 tile execution. Matrix semantics are packed vector register-group based without architected matrix RF, DMA is MMIO-programmed (non-instruction), and preemption/virtualization/security hardening are deferred to v0.2 scope.

## [2026-05-03] ingest | NPU v0.1 Hardware Architecture

Added source. Key claims: [[NPUv01]]는 global command processor 없이 host doorbell launch 기반의 2-hart tile baseline으로 설계되며, [[RV64]] + [[RVV]] + [[IME]] 조합과 [[SharedScratchpadMemory]], 3-channel [[DMA]], 8-slot [[BarrierSynchronization]]를 통해 deterministic edge execution을 우선한다. 또한 [[IREE]]/[[MLIR]] 기반 AOT ELF kernel, 소프트웨어 가시성 기반 멀티타일 partitioning, 그리고 [[DeterministicExecution]] 중심의 DV/bring-up 관측 체계를 정의한다.

## [2026-05-03] ingest | 알레르기 비염의 치료법은 하나뿐입니다 - 권혁수 교수 (서울아산병원 알레르기내과)

Added source. Key claims: 본문이 누락되어 구체 치료 내용은 반영하지 못하며, 출처 메타정보(저자: [[권혁수]], 소속: [[서울아산병원]] [[알레르기내과]], 주제: [[알레르기비염]])를 중심으로 정리되었고, 해당 개념/엔티티 페이지를 신규 등록함.

## [2026-05-03] ingest | 환율 1500원 시대, 환전하기 두렵다? (ft. SCHD 리밸런싱)

Added source. Key claims: 고환율 구간에서 배당·환차익·환율 타이밍을 결합해 달러 자산을 키우는 전략을 제시하고, 주식 거래 과정 환차익 과세 규칙을 강조하였다. 또한 2026년 [[SCHD]]의 리밸런싱(편입 25개, 제외 22개), 섹터 이동(에너지 축소, 기술 확대), 신규 편입 종목의 우량성(예: [[P&G]], [[유나이티드헬스그룹]], [[퀄컴]])을 정리해 장기 분산투자 관점의 실전 운영 규칙을 보완했다.

## [2026-05-03] ingest | 투자를 망치는 진짜 원인, 틀린 판단보다 '결정을 미루는 것' | 박병창 교보증권 자산관리전략부 이사 [여의도 인사이트]

Added source. Key claims: 투자자는 틀린 판단보다 결정 지연이 더 크고 파괴적인 손실을 만든다; 단기 하락에서 [[결정지연]], [[매몰비용]], [[손실회피]]가 개입해 관망이 손실을 키운다. [[삼성전자]], [[SKHynix]], [[환율]], [[신용융자]] 변수를 통해 시장 심리-유동성-레버리지 상호작용을 분석하고, 즉시 실행 가능한 투자 원칙(규칙 기반 대응, 분할 운용, 레버리지 제한)을 제시한다.

## [2026-05-03] ingest | 코스피 1만 시나리오… 결국 ‘금리’에서 갈린다 | 나탈리 허 변호사 [신과대화]

Added source. Key claims: 핵심 변수가 [[금리]]의 방향 전환이며, 코스피 1만 시나리오의 실현성은 [[AI 인프라]] 확대와 [[미국]] 지정학·규제 리스크를 함께 반영한 금리/신용/유동성 경로에 의해 좌우된다는 점, 그리고 [[사모신용]], [[AI워싱]], [[에너지 인프라]] 연동 리스크가 한국형 투자 실행 규칙(분할 진입·현금율 유지·산업 다변화)을 보강한다.

## [2026-05-03] ingest | 제2의 금융위기 온다? 사모대출 위기의 실체 - 이영주 수석연구위원 (하나증권)

Added source. Key claims: [[사모대출]] 시장은 [[BDC]] 유동성 구조와 [[AI 데이터센터]] 인프라 연결에서 구조적 전환기에 진입했다, [[블루아울]] [[OBDC2]] 사태는 환매 미스매치의 연쇄 신호다, [[PIK]]와 [[NII]] 악화는 배당 지속성 붕괴의 선행 신호, [[오프밸런스 구조]]와 [[섀도우뱅킹]] 특성으로 금융 시스템 전이 리스크가 높아질 수 있다.

## [2026-05-03] ingest | 전쟁, 유가, 금리, 그리고 삼성전자와 하이닉스의 매트릭스는? | 장우진 작가 [긴급인터뷰]

Added source. Key claims: [[유가]] 변동성 둔화에도 지정학·신용·금리 경로의 재확대 가능성, [[호르무즈해협]] 봉쇄 및 사모신용 경로가 [[삼성전자]]·[[SKHynix]]의 변동성에 미치는 영향, [[양적긴축(QT)]], [[금리]] 정책 경로가 단기 밸류에이션 조정과 하반기 유동성 리스크를 동반함, 그리고 주도주 운용의 보수적 비중조절(분할 매수/현금 확보/매도 연습)을 제시함.

## [2026-05-03] ingest | ‘원유’가 아니라 ‘달러 패권’이다… 호르무즈의 진짜 의미 | 중소기업중앙회 성상현 부부장 [신과대화]

Added source. Key claims: 중동 전쟁의 본질을 달러패권·재정지배력 유지와 공급망 재편으로 해석했고, [[호르무즈해협]]·[[IMEC]]를 전략 허브로 제시했다. [[재정지배력]]·[[유동성사이클]]·[[금융억압]]·[[AI혁신]]이 투자 판단을 연결하는 공통 축으로 정리됨.

## [2026-05-03] ingest | 실적 5배에도 주가 2배, 반도체 상승 여력 남았나? | 김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: [[OpenAI]] 토큰 처리량 2.5배 증가와 [[엔트로픽]] 사용자 증가에도 [[삼성전자]]·[[SKHynix]] 주가 반응이 실적 대비 제한적이어서 반도체 밸류의 추가 반영 여력이 존재함을 제시한다. AI 인프라 병목인 [[쇼티지]](연산 자원)와 기업별 리포트(두산에너빌리티, 현대건설, [[GST]], 낸드) 분석을 통해 기간 검증과 분할·분산 기반 투자 원칙을 강조한다.

## [2026-05-03] ingest | 삼전닉스 동반 하락 부른 구글 '터보퀀트'의 진짜 의미ㅣ김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: 단기적으로 [[TurboQuant]]는 [[삼성전자]]·[[SKHynix]] 주가에 부정적 헤드라인을 유발할 수 있으나, 장기적으로 [[재번스의역설]] 하에서 AI 비용 하락과 [[ASMR]] 확산이 메모리 수요 재가속을 유도할 수 있다. 투자 해석은 단일 시그널이 아닌 기술 채택 시점, 고객 재고, 가격협상(가격 신호), CAPEX/가동률을 함께 본다.

## [2026-05-03] ingest | 메모리Q와 토큰 올해 말부터 기울기 폭발?! | 김장열 유니스토리자산운용 본부장 [글로벌 인터뷰]

Added source. Key claims: AI 토큰 수 증가와 메모리 수요는 즉시 선형 연동되지 않으며, 효율화로 일시 둔화되는 수요가 장기적으로는 [[재번스의역설]]을 통해 다시 가속될 수 있다. 반도체 업황의 핵심은 AI 서비스 성장 + 빅테크 [[CAPEX]] 실행 + 전력/금리/펀딩 조건의 동시 검증이며, 투자에서는 속도 조절과 수익성의 기간성 확인이 필요하다.

## [2026-05-03] ingest | 마이크론 역대급 저평가...메모리 밸류 바닥 국면 진입?ㅣ김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: [[MicronTechnology]]의 역대급 낮은 PER(약 5~6배)이 한국 메모리 대장주 밸류 재편의 하한 기준이 될 수 있다는 비교평가 프레임을 제시하고, [[삼성전자]], [[SKHynix]], [[삼성전기]], [[VM]], [[파마리서치]] 리포트 신호 및 유가/쇼티지/휴머노이드·희토류 등의 거시 변수로 투자 타이밍을 다층 판단해야 한다는 점을 정리.

## [2026-05-03] ingest | 구글 TurboQuant AI 메모리 6배 줄여도 된다!  메모리 압축 기술의 진짜 의미   | Hot Warm Cold KV Cache 의 차이 | 메모리 슈퍼사이클

Added source. Key claims: [[Google]]의 [[TurboQuant]]는 핫 [[KVCache]] 압축으로 FP16 대비 최대 6배 메모리 절감과 속도 개선을 제시하며, [[NVIDIA]]의 [[KVTC]]는 콜드 [[KVCache]] 처리로 최대 약 20배 절감이 가능하다는 상호 보완적 메모리 계층 전략을 제시한다. 단기 효율성 개선이 장기적으로 긴 문맥/멀티턴·동시성 증가로 이어질 수 있다는 점을 함께 기록한다.

## [2026-05-03] ingest | 견고한 반도체 시장 펀더멘털...실적 대비 저평가된 반도체 기업은? | 김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: 1) 실적 전망이 개선된 [[삼성전자]], [[SKHynix]], [[MicronTechnology]]가 디레이팅 구간에 있을 수 있다. 2) AI 아키텍처 확대(특히 [[VeraRubinPlatform]]/NVL144)로 [[KoreaCircuit]], [[SoCModule]], [[FCBGA]], [[NVSwitchChip]], [[MidPlane]] 연계 패키징 수요가 성장 축이 된다. 3) 계약 부채와 AI 데이터센터 부품(DPU/NetworkCard/광모듈) 이해가 반도체 투자 판단의 보조 지표로 중요하다.

## [2026-05-03] ingest | Vibe coding in prod

Added source. Key claims: 바이브 코딩을 단순 코드 생성이 아니라 결과 기반 검증 운영으로 재정의하고, AI 협업의 안전한 운영을 위해 [[AIPM]], [[LeafNode]], [[Verifiability]], [[TestDrivenDevelopment]], [[ConfidentialBoundary]], [[SessionCompaction]]을 결합해야 한다고 정리. [[Anthropic]], [[Claude]], [[ClaudeCode]] 적용 맥락을 통해 프로덕션 확장 시 리스크 통제와 신뢰 확보 절차를 강조함.

## [2026-05-03] ingest | Vibe coding in prod

Added source. Key claims: [[VibeCoding]]은 AI 생성 코드를 전량 검토하기보다 [[AIPM]], [[LeafNode]], [[Verifiability]], [[TestDrivenDevelopment]]를 결합해 제품 품질을 보증하는 방식이다. 또한 [[Anthropic]]의 [[ClaudeCode]] 운영 사례를 통해 보안 민감 구간에서는 [[ConfidentialBoundary]]로 범위를 제한하고, [[SessionCompaction]]으로 장기 작업 생산성을 유지해야 한다.

## [2026-05-03] ingest | 구글 TurboQuant AI 메모리 6배 줄여도 된다! 메모리 압축 기술의 진짜 의미 | Hot Warm Cold KV Cache 의 차이 | 메모리 슈퍼사이클

Added source. Key claims: [[TurboQuant]]는 핫 KV 캐시의 고밀도 압축을 통해 단기 메모리 효율과 속도 개선을 제시하고, [[NVIDIA]]의 [[KVTC]]는 콜드 KV 중심 압축으로 보완되며, 단기 효율성 증가가 장기적으로 메모리 수요 절대 감소로 연결되지 않고 더 긴 컨텍스트/동시성 확대로 이어질 수 있음을 정리한다.

## [2026-05-03] ingest | 견고한 반도체 시장 펀더멘털...실적 대비 저평가된 반도체 기업은? | 김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: AI 반도체 실적이 상향되는 구간에서 대형반도체주는 저평가 디레이팅 현상이 존재할 수 있으며, 밸류에이션 재평가의 핵심 변수는 수요 회복 지연의 해소와 고다층 기판·패키징 수요의 구조적 증가. 신규 엔티티([[KoreaCircuit]], [[MicronTechnology]], [[DLC]], [[UnistoryAssetManagement]], [[Tesla]])와 신규 개념([[SemiconductorValuation]], [[SoCModule]], [[FCBGA]], [[NVSwitchChip]], [[MidPlane]], [[ContractDebt]], [[AIDataCenterInfrastructure]])를 생성/갱신해 [[VeraRubinPlatform]]/AI 데이터센터 수요와 연결했다.

## [2026-05-03] ingest | Vibe coding in prod

Added source. Key claims: source argues that production-safe [[VibeCoding]] depends on humans acting as [[AIPM]] for AI, focusing on [[LeafNode]]-scoped changes and measurable [[TestDrivenDevelopment]] gates rather than line-by-line review. It adds operational guidance for security-sensitive systems, compounding speed with verification, and a view of AI workflow optimization through context management and iterative prompts.

## [2026-05-03] ingest | 2026-05-03 AI/ML Learning Day 11

Added source. Key claims: Day 11 covers [[SupportVectorMachine]] with [[MaximumMargin]] and [[KernelTrick]], [[KNN]] with nearest-neighbor inference under chosen [[DistanceMetric]], and [[DecisionTree]] split quality via [[InformationGain]], [[Entropy]], and [[GiniImpurity]]. It adds key connections to [[RAG]], [[Embedding]] retrieval, and tree ensembles ([[RandomForest]], [[XGBoost]], [[LightGBM]], [[CatBoost]]), and flags no direct contradictions with existing pages.

## [2026-05-02] ingest | 2026-05-02 AI/ML Learning Day 10

Added source. Key claims: introduced [[LinearRegression]] with [[LeastSquares]] objective and [[Residual]]-based fitting, [[LogisticRegression]] as linear-score+[[Sigmoid]] binary decision flow, and [[DecisionBoundary]]/[[LinearSeparability]]/[[Hyperplane]] geometry for classification; linked these to [[CrossEntropy]] for classification optimization and connected them with [[FeatureSpace]] transformation and [[LLM]] intuition.

## [2026-05-01] ingest | 2026-05-01 AI/ML Learning Day 09

Added source. Key claims: 교차검증을 통해 [[CrossValidation]]/[[KFoldCrossValidation]] 기반의 안정적 성능 추정으로 단일 split 편향을 줄였고, 도메인 목표에 맞는 [[EvaluationMetric]] 설계를 위해 [[Precision]], [[Recall]], [[F1Score]], [[AUROC]]를 활용했으며, [[Regression]]과 [[Classification]]의 [[RegressionLoss]]와 [[ClassificationLoss]] 차이를 통해 모델 학습 신호를 정확히 분리했다.

## [2026-04-30] ingest | 2026-04-30 AI/ML Learning Day 08

Added source. Key claims: Day 08 formalizes the connection between [[Overfitting]], [[Underfitting]], [[BiasVarianceTradeoff]], and [[Regularization]], with practice-oriented diagnostic guidance around [[TrainingLoss]]/[[ValidationLoss]] divergence and model complexity control via [[L1Penalty]], [[L2Penalty]], and [[WeightDecay]]. Also added conceptual updates with new pages: [[Underfitting]], [[Bias]], [[BiasVarianceTradeoff]], [[WeightDecay]], [[L1Penalty]], [[L2Penalty]], and updated index/overview entries.

## [2026-04-29] ingest | 2026-04-29 AI/ML Learning Day 07

Added source. Key claims: 모델의 표현력은 [[HypothesisSpace]]와 [[Capacity]]로 정리되며 과소/과대 적합이 trade-off를 만든다. [[TrainSet]], [[ValidationSet]], [[TestSet]] 분리를 통해 일반화 가능성을 진단하고, [[Generalization]]은 [[GeneralizationGap]] 및 [[OutOfSample]] 성능으로 평가해야 한다. capacity 균형, split 규칙 준수, [[DataLeakage]] 회피를 통해 실전 배포 신뢰도를 높인다.

## [2026-04-28] ingest | 2026-04-28 AI/ML Learning Day 06

Added source. Key claims: [[SGD]]/[[MiniBatch]]는 전체 데이터 gradient의 대체 추정치로 계산 효율을 높여 반복 학습을 가능케 하며, [[LearningRate]]가 수렴 안정성의 핵심 변수로 [[Convergence]], [[Oscillation]], [[Divergence]]를 좌우한다. [[Momentum]]과 [[Adam]]은 각각 누적 방향 정보와 1차/2차 모멘트 정보를 이용해 [[AdaptiveLearningRate]]와 함께 업데이트 안정성을 향상시키는 optimizer 전략이다.

## [2026-04-27] ingest | 2026-04-27 AI/ML Learning Day 05

Added source. Key claims: 학습을 [[Optimization]] 문제로 재정의해 [[Objective]], [[LossFunction]], [[EmpiricalRisk]], [[EmpiricalRiskMinimization]], [[GradientDescent]]의 연결고리를 정리했고, [[Objective]]와 [[Argmin]], [[LossFunction]]와 [[EmpiricalRisk]], 그리고 [[Gradient]]와 [[StepSize]]의 역할 구분을 추가했다.

## [2026-04-26] ingest | 2026-04-26 AI/ML Learning Day 04 — Derivatives, Gradients, and Backpropagation

Added source. Key claims: Day 04 formalized optimization intuition from [[Derivative]] and [[PartialDerivative]] to [[Gradient]], and linked [[ChainRule]] + [[ComputationalGraph]] to practical [[Backpropagation]]/[[Autograd]] workflows. It also emphasized [[DirectionalDerivative]], [[ForwardPass]]/[[BackwardPass]], and [[LearningRate]] tradeoffs in avoiding unstable updates.

## [2026-04-26] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: 머신러닝을 [[FunctionApproximation]] 관점에서 정리하고, [[HypothesisSpace]]와 [[LossFunction]]의 역할을 분리했으며, [[FeatureMatrix]]와 [[TensorShape]] 중심의 데이터 표현을 정리했다. 또한 고차원에서 발생하는 [[CurseOfDimensionality]]를 경고하고 [[Regularization]], [[DimensionalityReduction]], [[RepresentationLearning]]의 중요성을 추가 연결했다.

## [2026-04-26] ingest | 2026-04-24 AI/ML Learning Day 02

Added source. Key claims: Day 02 documents [[Probability]] foundations for AI/ML through [[RandomVariable]] and [[ProbabilityDistribution]], distinguishes [[PMF]], [[PDF]], and [[CDF]] for discrete/continuous modeling, and connects summary statistics ([[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]) with [[ConditionalProbability]] and [[BayesTheorem]] via [[Prior]], [[Likelihood]], and [[Posterior]] for practical [[Classification]] intuition.

## [2026-04-26] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 벡터·기저 의존 좌표 개념을 정리했고, 행렬을 [[LinearMap]] 관점으로 해석했으며, [[DotProduct]], [[Norm]], [[CosineSimilarity]]를 [[Embedding]], [[Attention]], [[Gradient]] 연산과 연결했다.

## [2026-04-26] ingest | 2026-04-26 AI/ML Learning Day 04 — Derivatives, Gradients, and Backpropagation

Added source covering derivative, partial derivative, gradient, chain rule, computational graph, and backpropagation. Created concept pages for Derivative, PartialDerivative, Gradient, ChainRule, ComputationalGraph, Backpropagation, GradientDescent, Autograd, VanishingGradient, ExplodingGradient.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source: AI/ML 30일 학습 Day 01 — 수按月기초 복습. Key claims: (1) [[VectorSpace]]에서 좌표는 [[Basis]]-dependent하며 벡터 자체는 불변이다. (2) [[Matrix]]는 [[LinearMap]]의 계산 표현이며 [[Rank]]는 보존되는 독립 정보 차원 수다. (3) [[DotProduct]]는 방향+크기 결합 측정으로 [[Attention]] scoring에, [[CosineSimilarity]]는 방향만 측정해 [[Embedding]] retrieval에 쓰인다. (4) [[Norm]]은 [[Gradient]] clipping과 regularization의 기초다. Created/updated concept pages: [[VectorSpace]], [[Basis]], [[LinearMap]], [[Rank]], [[DotProduct]], [[Norm]], [[CosineSimilarity]]. Updated overview with AI/ML Mathematical Foundations section.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: [[VectorSpace]] defines the abstract space for vector representations; coordinates are [[Basis]]-dependent, not intrinsic to the vector. [[Matrix]] is the computational form of a [[LinearMap]], and [[Rank]] measures preserved information dimensionality. [[DotProduct]], [[Norm]], and [[CosineSimilarity]] quantify vector relationships—used respectively in [[Attention]] scoring, [[Regularization]]/[[GradientNormClipping]], and [[Embedding]] retrieval. Created concept pages: VectorSpace, Basis, LinearMap, Rank, DotProduct, Norm, CosineSimilarity, LoRA, LowRankApproximation, GradientNormClipping. No contradictions with existing wiki content.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 벡터공간은 표현의 대상, 행렬은 선형변환, dot product·norm·거리는 표현 간 관계를 수치화. [[VectorSpace]], [[LinearMap]], [[DotProduct]], [[Norm]], [[CosineSimilarity]] 개념 페이지 생성.

## [2026-04-25] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: ML as [[FunctionApproximation]], [[HypothesisSpace]]/[[LossFunction]] as model selection axes, and high-dimensional sparsity as the main driver for [[RepresentationLearning]], [[Regularization]], and [[DimensionalityReduction]].

## [2026-04-25] ingest | 2026-04-24 AI/ML Learning Day 02

Added source. Key claims: [[RandomVariable]]는 불확실성의 수치 매핑이며 [[PMF]]/[[PDF]]/[[CDF]]로 분포를 다룬다; [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]은 분포 요약 통계량 축을 이룬다; [[BayesTheorem]]은 [[Prior]], [[Likelihood]], [[Posterior]]로 조건부 갱신을 정식화한다.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 수학 기초를 벡터공간 기반으로 정리해 coordinate의 basis-dependent 성격을 명확화했고, [[Matrix]]를 [[LinearMap]]로 재해석해 LLM의 [[Embedding]]·[[Attention]] 연산과 연결했으며, [[DotProduct]], [[Norm]], [[CosineSimilarity]]의 측정 목적 차이를 학습-복습 질문으로 정리했다.

## [2026-04-25] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: ML을 function approximation으로 보는 관점, hypothesis space와 loss function의 역할, feature matrix의 구조, curse of dimensionality와 대응 전략.

## [2026-04-25] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: ML can be framed as function approximation over a hypothesis space optimized by a loss function; feature matrices and tensor shapes encode data structure; high-dimensional sparsity creates the curse of dimensionality and motivates representation learning, regularization, and dimensionality reduction.

## [2026-04-25] ingest | 2026-04-24 AI/ML Learning Day 02

Added source. Key claims: 확률변수/분포의 기본 구분과 PMF/PDF/CDF의 사용 구간, 기댓값·분산·공분산·상관의 관계, 조건부확률과 베이즈 정리를 통해 분류에서 prior·likelihood·posterior가 어떻게 결합되는지 정리했다.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 벡터는 고정 대상이지만 [[Coordinate]]는 [[Basis]]에 따라 변하고, [[Matrix]]를 [[LinearMap]] 관점으로 해석해 [[DenseLayer]]·[[Attention]]을 이해할 수 있으며, [[DotProduct]], [[L2Norm]], [[CosineSimilarity]]가 각각 [[LLM]]의 [[Attention]], [[Regularization]], [[EmbeddingSearch]]에서 다른 목적의 유사도/거리 측도로 사용된다는 점을 정리했다.

## [2026-04-21] ingest | \"인간지능 시대는 끝났다\" 인공지능이 가져올 인류 절멸의 위기, 이재명 대통령이 차지호의원에게 내린 숙제 (차지호 의원) 1부

Added source. Key claims: [[UN]] 다자기구 AI 기능을 한국 공동 캠퍼스로 이전해 [[GlobalAIHub]]를 만든다는 제안, [[Polycrisis]](동시복합위기) 조건에서 [[HumanIntelligenceSystem]]의 한계를 보완하기 위한 [[ConnectedIntelligence]] 중심 전환 필요성, AI 시대 노동시장·안보 질서의 급격한 재편 가능성, 과도기 고용 및 소득안전장치로서 [[UniversalBasicIncome]]의 제한적 후보 제시.

## [2026-04-21] ingest | Understanding the RISC-V Extensions for AI - John Simpson, SiFive

Added source. Key claims: [[RiscV]] AI 확장은 벡터 계열 기반의 점진 확장([[VectorBatchProduct]], [[IntegratedMatrixExtensions]])과 고성능 행렬 상태 확장([[VectorMatrixExtensions]], [[AttachedMatrixExtensions]])로 분기되며, 엣지와 데이터센터 도메인별/[[LLM]] prefill-decode 단계별로 ISA 선택이 달라져야 한다. [[SiFive]]와 [[JohnSimpson]]의 정리에서 [[FP8]]/정밀도 처리와 [[FP64]] 성능 영향이 채택 전략의 핵심 제약으로 나타난다.

## [2026-04-21] ingest | Terafab Keynote | Building AI Chips for Earth & Space

Added source. Key claims: [[Terafab]] 협업( [[Tesla]]·[[SpaceX]]·[[xAI]])을 통해 연간 [[Terawatt]]급 AI 컴퓨팅 확보를 추구하고, 현재 [[20 gigawatt|20GW]] 수준의 제약을 넘어서려면 통합형 반도체 생산과 우주 배치 기반의 [[SpaceBasedAIComputing]]이 필요하다는 점, 그리고 장기적으로 [[ElectromagneticMassDriver]] 기반의 [[Petawatt]] 확장을 제시한다.

## [2026-04-21] ingest | Project Glasswing: Securing critical software for the AI era — Anthropic

Added source. Key claims: ProjectGlasswing은 Anthropic의 [[ClaudeMythosPreview]]로 핵심 소프트웨어 취약점을 대규모로 선제 탐지하고 패치 권고로 연결해 방어 속도를 높이는 협업형 보안 프로그램으로 정리되며, 40개 이상 파트너 확장, 1억 달러 크레딧 지원, 오픈소스 보안 기부, 그리고 90일 내 공개 보고/권고 산출을 핵심 운영 과제로 둔다.

## [2026-04-21] ingest | GTC 2026 – The Inference Kingdom Expands

Added source. Key claims: NVIDIA-Gruq LPU 통합 기반 [[AFD]]로 디코드/어텐션-FFN 분리를 통해 지연·처리량 트레이오드를 재설계했으며, [[CPO]]와 [[CMX]]/[[STX]] 중심의 네트워크-스토리지 확장으로 인퍼런스 랙 아키텍처를 GPU 중심을 넘는 계층형 플랫폼으로 진화시켰다.

## [2026-04-21] ingest | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

Added source. Key claims: EAGLE-3 removes the feature-prediction bottleneck in favor of direct token prediction, introduces [[TrainingTimeTest]] to simulate inference during training, and adds [[MultiLayerFeatureFusion]] across low/mid/high layers. It reports up to 6.47x speedup in [[Vicuna-13B]]/[[HumanEval]] and shows higher or stable acceptance behavior while proposing a data-dependent scaling law for inference acceleration.

## [2026-04-21] ingest | Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

Added source. Key claims: [[AndrejKarpathy]] 프레임에서 AI 에이전트의 본질은 코드 작성 대체보다 에이전트 지시·오케스트레이션 역량 강화이며, [[AutoResearch]]는 인간 병목을 줄이는 자율 연구 루프를 구현하는 방식이다. [[OpenClaw]]/지속형 클로 구조와 [[agent-first software]], [[Speciation]] 논의를 통해 소프트웨어 생산성, 사용자 경험, 연구 조직 설계가 동시에 재편되는 흐름을 정리한다.

## [2026-04-20] ingest | Understanding the RISC-V Extensions for AI

Added source. Key claims: RISC-V AI 가속은 [[RiscVExtensionsForAI]]의 네 갈래 접근( [[VectorBatchProduct]], [[IntegratedMatrixExtensions]], [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]])로 분기되며, 엣지/데이터센터 워크로드와 배치-대역폭 특성에 따라 적합한 설계를 선택해야 한다. 소프트웨어-하드웨어 협업 관점에서 [[FP8]], [[Bfloat16]], 그리고 [[KVCache]] 경량화 같은 모델 레벨 조정이 함께 성능-비용 균형을 결정한다.

## [2026-04-20] ingest | Terafab Keynote | Building AI Chips for Earth & Space

Added source. Key claims: [[Terafab]] projects a partnership-led plan by [[Tesla]], [[SpaceX]], and [[xAI]] to build terawatt-scale AI computing, emphasizing integrated fab capabilities, orbital deployment economics, and long-horizon expansion toward [[Petawatt]]-scale systems.

## [2026-04-20] ingest | Project Glasswing: Securing critical software for the AI era — Anthropic

Added source. Key claims: [[Anthropic]]가 [[ProjectGlasswing]]를 통해 [[ClaudeMythosPreview]] 기반으로 [[ZeroDayVulnerability]]를 고속 탐지·공유·패치하는 방식의 [[AIForCybersecurity]] 협업 모델을 추진하며, 파트너십 확장·규제 협력·안전 가드를 함께 병행해야 함을 정리한다.

## [2026-04-20] ingest | GTC 2026 – The Inference Kingdom Expands

Added source. Key claims: [[NVIDIA]]는 [[Groq]]의 [[LPU]]를 추론 스택에 흡수해 [[GPU]]와의 이종 협업으로 프리필/디코드 분업을 강화했다. [[AFD]]와 [[Speculative Decoding]]은 디코드 지연 개선의 핵심 기법으로 등장하며, [[CPO]]·[[LPX]]·[[VeraETL256]]·[[CMX]]/[[STX]]는 대규모 AI 인프라에서 네트워크, CPU, 스토리지 병목을 함께 다루는 연계 전략으로 정리되었다.

## [2026-04-20] ingest | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

Added source. Key claims: [[EAGLE3]] removes direct [[Feature Prediction]] bottlenecks, adopts [[TrainingTimeTest]] plus [[MultiLayerFeatureFusion]] for data-aware scaling, and reports strong speedups (6.47x/4.40x/4.34x) with stronger acceptance stability across [[HumanEval]], [[MT-bench]], and [[GSM8K]].

## [2026-04-20] ingest | Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

Added source. Key claims: [[AndrejKarpathy]]가 [[LLMAgents]]의 병렬 협업형 전환, [[AutoResearch]]의 자율 루프, [[ModelSpeciation]] 필요성, 그리고 [[agent-first software]]와 [[OpenClaw]] 사례를 통해 인간의 병목이 오케스트레이션으로 이동함을 강조했고, 연구 조직은 [[MetaOptimization]]으로 재구성될 수 있음을 제시했다.

## [2026-04-20] ingest | 메모리 현물가 하락, 사이클 꺾인 게 아닌 '과열 해소' | 김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: 현물가 하락을 사이클 종료가 아닌 과열 해소로 보았고, 장기계약 최저가(Floor) 구조로 중기 가격 안정성이 강화될 수 있다고 정리했다. 또한 [[TurboQuant]]는 단기 효율화와 병목 이동을 동시에 낳을 수 있으며, [[ASMR]]·[[OnDeviceAI]]는 장기 메모리 수요 확대 가능성에 대한 상반축 시나리오를 제공한다.

## [2026-04-20] ingest | Dissecting Nvidia Blackwell - Tensor Cores, PTX Instructions, SASS, Floorsweep, Yield

Added source. Key claims: 소스 본문이 비어 있어 실질적 기술 주장 없음. 문서 제목 기반으로 [[NVIDIA]] [[Blackwell]] 및 [[Tensor Cores]], [[PTX]], [[SASS]], [[Floorsweep]], [[ChipYield]] 키워드만 확인됨.

## [2026-04-20] ingest | Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

Added source. Key claims: AI 에이전트의 병렬 오케스트레이션이 직접 코딩 비중을 낮추고 지시·검증 역량을 핵심 능력으로 전환시키며, [[AutoResearch]]로 연구 병목(인간 프롬프트 병목)을 줄이자는 흐름을 제시한다. OpenClaw, Claw, Dobby the Elf Claw 사례로 에이전트형 소프트웨어 경험(특히 [[agent-first software]])의 전환이 가시화되었고, 장기적으로는 [[ModelSpeciation]]과 [[OpenSource]]/프론티어 균형이 핵심 구조로 부상한다.

## [2026-04-20] ingest | The Great GPU Shortage – Rental Capacity – Launching our H100 1 Year Rental Price Index

Added source. Key claims: (1) H100 1-year rental contracts rose sharply (about 40% from 2025년 10월 to 2026년 3월), indicating persistent GPU scarcity-driven pricing power. (2) Supply constraints are now mostly a contract-structure and long-horizon capital allocation issue rather than a short-lived spot-market fluctuation. (3) Multi-agent, high-token workloads and memory/server inflation are reinforcing demand, so AI compute scarcity is treated as a durable macro-structural condition.

## [2026-04-20] ingest | 환율 1500원 시대 시작되나? 전쟁 끝나도 못 내려오는 이유 | 변정규 다이와증권코리아 본부장 [신과대화]

Added source. Key claims: 전쟁 종료 이후에도 [[한미금리차]]와 지속적 [[달러 강세]], 그리고 [[QuantitativeTightening]]이 맞물리면 [[환율]]은 빠르게 하락하지 않고 1,500원대 고착이 지속될 수 있다는 점을 정리했다. 정책 도구로 제시된 [[WGBI]]와 [[KoreaAccount]]는 즉각적 해결이 아니라 점진적 완충 수단으로 작동하며, 고환율은 물가·채권·기업조달비용 및 특히 중소기업 부담으로 이어질 수 있음을 덧붙였다.

## [2026-04-20] ingest | 트렌드포스 "SK하이닉스 때문에 엔비디아 루빈 생산량이 대폭하향 되었다"

Added source. Key claims: 엔비디아 루빈 생산량 하향은 SK하이닉스의 공정 문제 단일 원인 해석보다 CPX/LPX 기반 워크로드 분리와 루빈 다이 필요량 감소가 핵심 원인이라는 점, 그리고 수급 배분은 [[JenHuang]]의 통제 하에서 [[SKHynix]]/[[SamsungElectronics]] 간 역할 재편으로 확장되는 점을 추가했다.

## [2026-04-20] ingest | 제2의 테슬라? 3천조 괴물 상륙! 스페이스X 상장, 약일까 독일까? | 정의훈 유진투자증권 연구원

Added source. Key claims: [[SpaceX]] 상장 이슈가 우주산업의 밸류에이션 허브로 해석되며, 유통물량·수급 민감도와 모멘텀형 자금 이동이 핵심이다. [[위성통신]]과 [[아르테미스]]는 개별 자산군보다 산업 구조/기술 패권 축으로 정리되었고, [[네이버]], [[카카오]], 게임주의 사례는 국내 주식 수급의 실적 대비 성장성 함의와 결합되어 기록됨.

## [2026-04-20] ingest | 인간의 가치는 오직 의지만 남을 겁니다 - 노정석 대표(비팩토리)

Added source. Key claims: [[비팩토리]]의 AI 도입은 [[AI에이전트]] 기반으로 반복 노동을 축소하고 부가가치 활동으로 재편한다는 조직 운영 사례를 제공한다; AI 전환은 인력 간 적응 속도 차이를 키워 [[AI인재양극화]]를 가속시킬 수 있으며, AI 시대 인간의 핵심 가치는 지식량보다 실행 의지로 이동한다.

## [2026-04-20] ingest | "인간지능 시대는 끝났다" 인공지능이 가져올 인류 절멸의 위기, 이재명 대통령이 차지호의원에게 내린 숙제 (차지호 의원) 1부

Added source. Key claims: UN 기능 이전을 통해 한국형 AI 공동 캠퍼스를 구축하려는 국가 전략 제안, 다중 위기(Polycrisis)에서 [[AI]]의 거버넌스·안보·노동 재설계 필요성, [[ConnectedIntelligence]] 중심의 과도기 운영 모델, 인류적 리스크를 줄이기 위한 제도적 AI 전환 우선순위, 청년/고령층 생산성 및 국가 간 군사력 격차 재편에 대한 경고.

## [2026-04-20] ingest | Understanding the RISC-V Extensions for AI

Added source. Key claims: [[RiscV]]의 AI 확장(특히 행렬 가속 경로)은 벡터 기반 경량 제안과 상태 기반 대형 제안으로 나뉘며 엣지와 데이터센터 워크로드 성격에 따라 선택되어야 한다고 정리된다. [[RiscVExtensionsForAI]]는 배치 크기, 정밀도(FP8/Bfloat16/FP64), 하드웨어 대역폭 조건을 함께 고려한 확장 프레임워크로 통합되었고, 이를 통해 정밀도와 처리량·대역폭 간의 실무적 트레이드오프가 명확히 드러났다.

## [2026-04-20] ingest | Project Glasswing: Securing critical software for the AI era — Anthropic

Added source. Key claims: [[Anthropic]] launched [[ProjectGlasswing]] to use [[ClaudeMythosPreview]] for defensive vulnerability discovery across critical software. The source reports thousands of serious findings including [[ZeroDayVulnerability]] cases and emphasizes that AI deployment must be paired with strict safety controls. It also introduces a new collaboration and governance thread in this wiki linking security, AI capability, and public-private coordination.

## [2026-04-20] ingest | 반도체 업황 살아났나? 밸류 재평가의 진짜 조건ㅣ김장열 유니스토리자산운용 본부장

Added source. Key claims: 반도체 밸류 재평가의 핵심은 빅테크 CAPEX 가이던스와 AI 가격 정책, 재고 및 선구매 계약 신호의 동시 변화이며, 현재는 부정적 시그널이 뚜렷하지 않아 펀더멘탈이 상대적으로 안정적이라는 판단이다. SK하이닉스의 180만 원대 목표주가 논리는 실적성장 지속 가정에 의존하며, 삼성전기의 실리콘 커패시터/ABF 포지션과 SoC 패키징 경쟁력, 삼성/하이닉스/마이크론 차별화가 종목 밸류 분기 포인트로 제시되었다.

## [2026-04-20] ingest | HBM 다음은 HBF, 엔비디아·MS를 영원히 가두는 삼성·하이닉스의 30년 가두리 전략

Added source. Key claims: HBF를 HBM 다음 단계의 AI 메모리 전략으로 제시, 빅테크를 묶는 가격·공급·표준화 동학을 주장, HBM/HBF 로드맵(HBM4/8, HBF5) 및 장기 계약 전략을 통해 시장 종속 구조 강화 가능성을 강조.

## [2026-04-20] ingest | ONNX와 ONNX Runtime

Added source. Key claims: ONNX는 프레임워크 간 상호운용 표준으로서 그래프 기반 모델 포맷을 제공하고, [[ONNXRuntime]]는 그래프 최적화·실행 공급자 파티셔닝·경량 API/학습 지원을 통해 다양한 하드웨어에서 고성능 추론을 수행한다. 또한 [[Microsoft]]의 실제 운영 사례에서 ONNX Runtime 성능 향상 수치가 제시되며, 모델 획득은 변환/ONNXZoo/Azure Custom Vision/직접 학습 경로로 정리되었다.

## [2026-04-20] ingest | ONNX-MLIR 기반 추론 컴파일 파이프라인

Added source. Key claims: ONNX 모델은 [[ONNX-MLIR]] 파이프라인에서 [[ONNX]]→[[MLIR]](Krnl/Affine/Std)→[[LLVM]] 흐름으로 최적화되어 추론 실행 산출물로 변환되며, IBM 메인프레임의 [[zAIU]]/[[zDNN]] 경로를 포함하고, 버퍼링·상수 처리·컴파일 시간 최적화가 성능 개선 포인트로 제시되었다.

## [2026-04-20] ingest | Vibe coding in prod

Added source. Key claims: [[VibeCoding]] is defined as a production-safe workflow centered on 
3-part execution: ([[AI의 PM 역할]], [[LeafNode]]-first changes, and explicit [[TestDrivenDevelopment]]-backed verification). The source emphasizes that trust must be restored through checkable outputs rather than exhaustive code reading, and extends the existing [[ClaudeCode]]/[[Anthropic]] narrative with concrete risk-aware guidance.

## [2026-04-19] ingest | Vibe coding in prod

Added source. Key claims: 정의적으로는 AI가 코드를 생성하는 것이 아니라 제품 중심·검증 중심으로 운영하는 방법을 제시하며, AI의 PM 역할 강화와 [[LeafNode]] 중심의 변경 전략을 중심 축으로 삼는다; Anthropic/[[ClaudeCode]] 사례를 통해 프로덕션 적용 시 기술 부채 통제와 보안 구간 분리가 중요함을 강조한다; [[TestDrivenDevelopment]]와 스트레스 테스트 기반의 체크포인트를 통해 구현 상세를 모두 읽지 않아도 신뢰를 축적하는 운영 모델이 제시된다.

## [2026-04-16] ingest | Bulk corpus sync

- Rebuilt `wiki/index.md` and `wiki/overview.md` after confirming all raw markdown sources are represented in `wiki/sources/`.
- Corpus status: 64 sources, 91 entities, 65 concepts.

# Wiki Log

Append-only chronological record of all operations.

Format: `## [YYYY-MM-DD] <operation> | <title>`

Parse recent entries: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-18] graph | Knowledge graph rebuilt

221 nodes, 1880 edges (1117 extracted, 763 inferred).

## [2026-04-19] graph | Knowledge graph rebuilt

227 nodes, 1920 edges (1140 extracted, 780 inferred).

## [2026-04-20] graph | Knowledge graph rebuilt

228 nodes, 1932 edges (1147 extracted, 785 inferred).

## [2026-04-21] graph | Knowledge graph rebuilt

393 nodes, 3307 edges (1792 extracted, 1515 inferred).

## [2026-04-25] graph | Knowledge graph rebuilt

426 nodes, 1900 edges (1900 extracted, 0 inferred).

## [2026-04-25] graph | Knowledge graph rebuilt

432 nodes, 1931 edges (1931 extracted, 0 inferred).

## [2026-04-25] graph | Knowledge graph rebuilt

458 nodes, 2122 edges (2122 extracted, 0 inferred).

## [2026-04-26] graph | Knowledge graph rebuilt

468 nodes, 2140 edges (2140 extracted, 0 inferred).

## [2026-04-26] graph | Knowledge graph rebuilt

473 nodes, 2218 edges (2218 extracted, 0 inferred).

## [2026-04-27] graph | Knowledge graph rebuilt

494 nodes, 2351 edges (2351 extracted, 0 inferred).

## [2026-04-28] graph | Knowledge graph rebuilt

498 nodes, 2400 edges (2400 extracted, 0 inferred).

## [2026-04-29] graph | Knowledge graph rebuilt

513 nodes, 2497 edges (2497 extracted, 0 inferred).

## [2026-04-30] graph | Knowledge graph rebuilt

530 nodes, 2589 edges (2589 extracted, 0 inferred).

## [2026-05-01] graph | Knowledge graph rebuilt

542 nodes, 2668 edges (2668 extracted, 0 inferred).

## [2026-05-02] graph | Knowledge graph rebuilt

554 nodes, 2740 edges (2740 extracted, 0 inferred).

## [2026-05-03] graph | Knowledge graph rebuilt

562 nodes, 2781 edges (2781 extracted, 0 inferred).

## [2026-05-03] graph | Knowledge graph rebuilt

1513 nodes, 5085 edges (5085 extracted, 0 inferred).

## [2026-05-04] graph | Knowledge graph rebuilt

1521 nodes, 5017 edges (5017 extracted, 0 inferred).

## [2026-05-04] graph | Knowledge graph rebuilt

1521 nodes, 5017 edges (5017 extracted, 0 inferred).

## [2026-05-05] graph | Knowledge graph rebuilt

1532 nodes, 5069 edges (5069 extracted, 0 inferred).

## [2026-05-06] graph | Knowledge graph rebuilt

1539 nodes, 5114 edges (5114 extracted, 0 inferred).

## [2026-05-07] graph | Knowledge graph rebuilt

1556 nodes, 5215 edges (5215 extracted, 0 inferred).

## [2026-05-08] graph | Knowledge graph rebuilt

1563 nodes, 5256 edges (5256 extracted, 0 inferred).

## [2026-05-09] graph | Knowledge graph rebuilt

1567 nodes, 5247 edges (5247 extracted, 0 inferred).

## [2026-05-09] graph | Knowledge graph rebuilt

1572 nodes, 5262 edges (5262 extracted, 0 inferred).

## [2026-05-10] graph | Knowledge graph rebuilt

1576 nodes, 5266 edges (5266 extracted, 0 inferred).

## [2026-05-10] graph | Knowledge graph rebuilt

1903 nodes, 6231 edges (6231 extracted, 0 inferred).

## [2026-05-10] graph | Knowledge graph rebuilt

1946 nodes, 6458 edges (6458 extracted, 0 inferred).

## [2026-05-11] graph | Knowledge graph rebuilt

1957 nodes, 6535 edges (6535 extracted, 0 inferred).

## [2026-05-12] graph | Knowledge graph rebuilt

1960 nodes, 6508 edges (6508 extracted, 0 inferred).

## [2026-05-13] graph | Knowledge graph rebuilt

1975 nodes, 6576 edges (6576 extracted, 0 inferred).

## [2026-05-13] graph | Knowledge graph rebuilt

2054 nodes, 6879 edges (6879 extracted, 0 inferred).

## [2026-05-14] graph | Knowledge graph rebuilt

2057 nodes, 6895 edges (6895 extracted, 0 inferred).

## [2026-05-15] graph | Knowledge graph rebuilt

2062 nodes, 6909 edges (6909 extracted, 0 inferred).

## [2026-05-15] graph | Knowledge graph rebuilt

2062 nodes, 6909 edges (6909 extracted, 0 inferred).

## [2026-05-16] graph | Knowledge graph rebuilt

2070 nodes, 6947 edges (6947 extracted, 0 inferred).

## [2026-05-17] graph | Knowledge graph rebuilt

2088 nodes, 7047 edges (7047 extracted, 0 inferred).

## [2026-05-18] graph | Knowledge graph rebuilt

2107 nodes, 7113 edges (7113 extracted, 0 inferred).

## [2026-05-19] graph | Knowledge graph rebuilt

2115 nodes, 7123 edges (7123 extracted, 0 inferred).

## [2026-05-19] graph | Knowledge graph rebuilt

2116 nodes, 7126 edges (7126 extracted, 0 inferred).

## [2026-05-20] graph | Knowledge graph rebuilt

2122 nodes, 7158 edges (7158 extracted, 0 inferred).

## [2026-05-20] graph | Knowledge graph rebuilt

2126 nodes, 7170 edges (7170 extracted, 0 inferred).

## [2026-05-20] graph | Knowledge graph rebuilt

2194 nodes, 7502 edges (7502 extracted, 0 inferred).

## [2026-05-20] graph | Knowledge graph rebuilt

2195 nodes, 7502 edges (7502 extracted, 0 inferred).

## [2026-05-20] graph | Knowledge graph rebuilt

2202 nodes, 7517 edges (7517 extracted, 0 inferred).

## [2026-05-21] graph | Knowledge graph rebuilt

2213 nodes, 7607 edges (7607 extracted, 0 inferred).

## [2026-05-22] graph | Knowledge graph rebuilt

2221 nodes, 7651 edges (7651 extracted, 0 inferred).

## [2026-05-22] graph | Knowledge graph rebuilt

2225 nodes, 7669 edges (7669 extracted, 0 inferred).

## [2026-05-22] graph | Knowledge graph rebuilt

2254 nodes, 7728 edges (7728 extracted, 0 inferred).

## [2026-05-23] graph | Knowledge graph rebuilt

2259 nodes, 7751 edges (7751 extracted, 0 inferred).

## [2026-05-24] graph | Knowledge graph rebuilt

2261 nodes, 7802 edges (7802 extracted, 0 inferred).

## [2026-05-24] graph | Knowledge graph rebuilt

2261 nodes, 7774 edges (7774 extracted, 0 inferred).

## [2026-05-29] graph | Knowledge graph rebuilt

2364 nodes, 7991 edges (7991 extracted, 0 inferred).

## [2026-06-03] graph | Knowledge graph rebuilt

2454 nodes, 8240 edges (8240 extracted, 0 inferred).

## [2026-06-05] graph | Knowledge graph rebuilt

2456 nodes, 8261 edges (8261 extracted, 0 inferred).

## [2026-06-10] graph | Knowledge graph rebuilt

2549 nodes, 8595 edges (8595 extracted, 0 inferred).

## [2026-06-12] graph | Knowledge graph rebuilt

2557 nodes, 8628 edges (8628 extracted, 0 inferred).
## [2026-06-17] ingest | HF Weekly 2026-W25 VLA papers: ReCAP and APT
- Created raw Korean translation/analysis/reference/learning deliverables for 2606.15631 and 2606.12366.
- Materialized source pages under wiki/sources because automated Codex ingest was blocked by expired Codex refresh token and NVIDIA returned no content in smoke test.
- Added support pages: [[ReCAP]], [[APT]], [[RetrievalAugmentedPolicy]], [[ActionExpertPretraining]].

## [2026-06-17] graph | Knowledge graph rebuilt

2569 nodes, 8699 edges (8699 extracted, 0 inferred).

## [2026-06-19] graph | Knowledge graph rebuilt

2591 nodes, 8750 edges (8750 extracted, 0 inferred).

## [2026-06-19] graph | Knowledge graph rebuilt

2591 nodes, 8760 edges (8760 extracted, 0 inferred).

## [2026-06-24] graph | Knowledge graph rebuilt

2633 nodes, 8932 edges (8932 extracted, 0 inferred).

## [2026-06-24] graph | Knowledge graph rebuilt

2633 nodes, 8937 edges (8937 extracted, 0 inferred).

## [2026-07-01] graph | Knowledge graph rebuilt

2709 nodes, 9157 edges (9157 extracted, 0 inferred).

## [2026-07-03] graph | Knowledge graph rebuilt

2719 nodes, 9194 edges (9194 extracted, 0 inferred).
## [2026-07-08] ingest | HF Weekly 2026-W28 VLA runtime and adaptive action horizon
- Added Korean translation/analysis/reference/learning pages for Embodied.cpp (2607.02501) and VLA-Corrector (2607.01804).
- Manual materialization completed after batch ingest stalled on large documents.

## [2026-07-08] graph | Knowledge graph rebuilt

2779 nodes, 9324 edges (9324 extracted, 0 inferred).

## [2026-07-10] graph | Knowledge graph rebuilt

2788 nodes, 9375 edges (9375 extracted, 0 inferred).

## [2026-07-15] graph | Knowledge graph rebuilt

2829 nodes, 9474 edges (9474 extracted, 0 inferred).

## [2026-07-15] graph | Knowledge graph rebuilt

2829 nodes, 9497 edges (9497 extracted, 0 inferred).

## [2026-07-17] graph | Knowledge graph rebuilt

2869 nodes, 9614 edges (9614 extracted, 0 inferred).
