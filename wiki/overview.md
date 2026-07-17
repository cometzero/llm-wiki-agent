# Wiki Overview

## 2026-W29 Hugging Face VLA/navigation and traffic simulation update
- [[ABotN1]] extends the navigation/VLA corpus toward a slow-fast interface: a slow VLM reasoner produces explicit reasoning plus [[PixelGoal]] anchors, and a fast action expert turns them into continuous [[Waypoint]] outputs for point/object/POI/instruction/person-following tasks.
- [[FlowERD]] extends the autonomous-driving simulation corpus: [[FlowMatching]] is combined with agent-type kinematics and [[EntropyRegularizedDistillation]] to improve the realism-diversity Pareto trade-off in closed-loop traffic rollout.
- Together these papers shift the weekly thread from only VLA policy generation toward the systems around it: action-grounding interfaces, closed-loop evaluation, simulator diversity, and deployment latency/safety constraints.

## 2026-W28 Hugging Face VLA deployment/update
- [[Embodied-cpp]] extends the VLA/WAM corpus toward deployment infrastructure: multi-rate execution, latency-first batch-1 inference, and five-layer C++ runtime abstraction for heterogeneous robots and edge devices.
- [[VLACorrector]] extends the action-chunking corpus toward adaptive closed-loop execution: [[LatentSpaceVisionMonitor]] detects stale chunks and [[OnlineGradientGuidance]] guides recovery replans.
- Together these papers emphasize that VLA progress depends not only on action generation quality, but also on runtime scheduling, monitoring, invalidation, and recovery under real closed-loop constraints.

## LWN Weekly Linux/Open Source Tracking
- The July 2, 2026 LWN translation adds [[DebianProtestware]], [[Git255]], [[RhombusMetaprogramming]], [[KernelHardening]], [[KernelWriteback]], [[BPFLocalStorage]], [[SecureBootCertificateExpiration]], and [[ObjectStorageAlternatives]] to the recurring Linux/open-source operations corpus.
- Across the May–July LWN sources, the wiki now tracks a continuous thread from package and publishing trust ([[SupplyChainSecurity]], [[AURSupplyChainAttack]], [[TrustedPublishing]]) to kernel release flow ([[LinuxKernel72]], [[BPF]], [[KernelHardening]]) and operational infrastructure ([[OSPM2026]], [[RMRBRMR]], [[ObjectStorageAlternatives]]).

- [[lwn-weekly-edition-2026-07-09-1080835]]: LWN.net Weekly Edition 2026-07-09 번역은 kernel cryptography 현대화, iomap, negative dentry 제한, RCU/lockless allocation, LLM-assisted MM patch review를 Linux 커널 지식 축에 추가한다.
