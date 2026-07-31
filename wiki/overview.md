# Wiki Overview

## 2026-W31 Data Pyramid & WorldDiT update
- [[DataPyramidForEmbodiedManipulation]] adds a data-centric lens for VLA/embodied systems: real-robot, UMI-style, egocentric/exocentric, simulation, and general VL data should be mixed according to [[RobotAlignment]], scalability, [[PhysicalFidelity]], diversity, and action grounding.
- [[WorldDiT]] adds a compact world-action modeling baseline: one shared [[DiffusionTransformer]] learns continuous [[ActionChunking]] and [[FutureRGBPatchPrediction]], then uses [[InferenceTimeActionOnlyDeployment]] with receding-horizon replanning at inference.
- Together, the W31 papers strengthen the autonomous-driving VLA study thread around data recipe design and deployment-efficient world supervision: future visual/BEV/occupancy prediction can train richer state representations while the runtime path stays action/trajectory focused.
- Caveat: WorldDiT reports LIBERO simulation results with staged checkpoint-selection caveats, so its parameter-success point should be treated as a useful baseline rather than a fully unbiased deployment estimate.

## 2026-W30 Robotics Scale & Transfer Update
- [[Xiaomi-Robotics-1]]은 100K+ 시간대 real-world 조작 trajectory와 [[StateTransitionCaptioning]] 기반 supervision으로 데이터 스케일·모델 스케일·cross-embodiment 정합이 실제 성능으로 이전되는 지점을 보인다.
- 이 작업은 [[Qwen3-VL]] 백본 + action chunk generator 설계에서 baseline 대비 실행성능과 시뮬레이션 성능(예: [[RoboCasa365]]/[[RoboDojo]])을 함께 다루며, VLA 파운데이션의 "데이터 규모-표현 품질-배치 정합" 축을 확장한다.
- 이번 레퍼런스 워크플로 정리는 [[UMI]], [[pi0]], [[pi0.5]], [[RT-1]], [[DROID]] 및 공개 데이터([[Bridge V2]])의 계보를 정리해 Xiaomi 라인을 VLA scaling 및 benchmark 축으로 재구성한다.
- 이번 학습 노트는 state-transition 언어 감독이 task label보다 높은 grounding 밀도를 제공하며, AD로의 전이에서는 "장면/경로 전이 상태 + traffic-rule 제약" 설계로 바꿔 읽을 수 있음을 제시한다.

## Xiaomi-Robotics-1 레퍼런스 워크플로 정리
- 선행 정렬 우선순위는 `UMI → π0/π0.5/RT-1 → 공개 데이터(DROID, Bridge V2) → 시뮬레이션 평가(RoboCasa365, RoboDojo)`로 수렴한다.
- 이 분해는 data scaling(수집), model scaling(사전 학습/액션 생성), post-training 정합(cross-embodiment/benchmark)로 이어져, 기존 [[FlowERD]], [[ABotN1]], [[Embodied-cpp]] 계열을 연결하는 로보틱스 실험 경로를 강화한다.
- 특히 Xiaomi는 action-generation 표현력뿐 아니라 [[StateTransitionCaptioning]] 기반 grounding으로 action chunk 해석 정합도를 높였다는 점에서 기존 VLA baseline과 차별화된다.

## 2026-W29 Hugging Face VLA/navigation and traffic simulation update
- [[ABotN1]] extends the navigation/VLA corpus toward a slow-fast interface: a slow VLM reasoner produces explicit reasoning plus [[PixelGoal]] anchors, and a fast action expert turns them into continuous [[Waypoint]] outputs for point/object/POI/instruction/person-following tasks.
- [[FlowERD]] extends the autonomous-driving simulation corpus: [[FlowMatching]] is combined with agent-type kinematics and [[EntropyRegularizedDistillation]] to improve the realism-diversity Pareto trade-off in closed-loop traffic rollout.
- Together these papers shift the weekly thread from only VLA policy generation toward the systems around it: action-grounding interfaces, closed-loop evaluation, simulator diversity, and deployment latency/safety constraints.

## 2026-W28 Hugging Face VLA deployment/update
- [[Embodied-cpp]] extends the VLA/WAM corpus toward deployment infrastructure: multi-rate execution, latency-first batch-1 inference, and five-layer C++ runtime abstraction for heterogeneous robots and edge devices.
- [[VLACorrector]] extends the action-chunking corpus toward adaptive closed-loop execution: [[LatentSpaceVisionMonitor]] detects stale chunks and [[OnlineGradientGuidance]] guides recovery replans.
- Together these papers emphasize that VLA progress depends not only on action generation quality, but also on runtime scheduling, monitoring, invalidation, and recovery under real closed-loop constraints.

## LWN Weekly Linux/Open Source Tracking
- [[lwn-weekly-edition-2026-07-23-1083123]]: LWN.net Weekly Edition 2026-07-23 번역은 [[LLMAssistedKernelDevelopment]]의 community/process 논쟁, [[GNOMESessionRestore]], [[FedoraChangeProcess]], [[BPFTracepoints]], [[BPFLsmSecurity]], [[Famfs]], [[SchedExt]], [[PyPISupplyChainSecurity]], [[XZBackdoor]]를 Linux/open-source 추적 축에 추가한다.
- [[lwn-weekly-edition-2026-07-16-1081915]]: LWN.net Weekly Edition 2026-07-16 번역은 AI scraper/residential proxy를 통한 공개 웹 부담, [[io_uring]] lockless MPSC FIFO, [[BPFExploitMitigation]], [[BPFDirectPacketSending]], [[Kitty]], [[QBECompilerBackend]]를 Linux/open-source 추적 축에 추가한다.
- The July 2, 2026 LWN translation adds [[DebianProtestware]], [[Git255]], [[RhombusMetaprogramming]], [[KernelHardening]], [[KernelWriteback]], [[BPFLocalStorage]], [[SecureBootCertificateExpiration]], and [[ObjectStorageAlternatives]] to the recurring Linux/open-source operations corpus.
- Across the May–July LWN sources, the wiki now tracks a continuous thread from package and publishing trust ([[SupplyChainSecurity]], [[AURSupplyChainAttack]], [[TrustedPublishing]]) to kernel release flow ([[LinuxKernel72]], [[BPF]], [[KernelHardening]]) and operational infrastructure ([[OSPM2026]], [[RMRBRMR]], [[ObjectStorageAlternatives]]).

- [[lwn-weekly-edition-2026-07-09-1080835]]: LWN.net Weekly Edition 2026-07-09 번역은 kernel cryptography 현대화, iomap, negative dentry 제한, RCU/lockless allocation, LLM-assisted MM patch review를 Linux 커널 지식 축에 추가한다.