# Wiki Overview

*Living synthesis of all ingested sources.*

## Current State

This wiki documents a broad range of topics including AI/ML fundamentals, infrastructure and chip ecosystems, Linux and systems engineering, automotive software, and AI operations.

### AI/ML Learning Path

The learning journey has progressed from basic ML concepts (Day 1–18) through convolutional and representation basics to production-oriented system design.

### AI Engineering and Agentic Development (2026-05-10)

The keynote and recent sources keep reinforcing that AI productivity scales through verifiable operational systems over one-shot benchmark gains.

- [[Anthropic]] introduced patterns like [[ClaudeManagedAgents]] and outcome-oriented loops emphasizing multi-agent orchestration.
- The practical theme is shift from generation-only coding to repeatable quality cycles with human oversight and explicit validation criteria.

### Tesla Shift: Modular AV to EndToEnd Optimization

A new source clarifies [[Tesla]]’s autonomy evolution across 2021–2022 transition steps and the FSD v12 inflection. The stack moved from a largely modular decomposition to an [[EndToEndDeepLearning]] architecture that jointly optimizes [[Perception]] and [[Planning]] under a single [[Objective Function]].

- 2021 emphasized [[HydraNet]]-driven multi-head perception and hybrid planning methods (A* variants plus learned tree search) with partially modular control.
- 2022 added [[OccupancyNetwork]] and [[OccupancyFlow]], improving 3D world understanding and trajectory scoring.
- FSD v12 framed the decisive shift: remove hand-coded planning heuristics (or at least de-emphasize them) and train planning behavior jointly with perception signals.
- This does not discard historical modules; instead it preserves diagnostic visibility while aligning global training gradients to drive global behavior quality, including rare-event anticipation and long-horizon safety.

### Tesla Explainability and Simulation-First Autonomy

A new [[Tesla]] source on the FSD demo strengthens an already emerging thread: safe autonomy requires not only performance but interpretable decision traces.

- [[Tesla]] can provide natural-language explanation for driving actions, which strengthens [[Verifiability]] and supports human comprehension in edge scenarios.
- The source frames autonomy as both fast reactive control and deeper deliberation: [[System1]] handles immediate responses, while [[System2]] activates for non-routine conditions.
- [[Tesla]]’s [[GaussianSplatting]] approach is presented as a faster, higher-fidelity 3D scene representation stack that improves both observability and real-time utility.
- The source also emphasizes closed-loop simulation: a [[WorldSimulator]] built from state-action inversion enables massive synthetic scenario generation, corner-case injection, and policy retraining.

### Tesla Occupancy-Centric 3D Perception (2026-05-10)

A new source documents why [[Tesla]] moved from object-centric modules toward [[OccupancyNetwork]]-style world representations for safety-critical driving.

- The source argues that fixed ontology and box-centric detection can miss irregular hazards.
- The architecture is centered on multi-camera feature extraction, temporal occupancy fusion, and output of [[OccupancyVolume]] and [[OccupancyFlow]].
- [[NeuralRadianceField]] is positioned as a consistency check for scene reconstruction.

### LLM Inference Infrastructure and Token Economics

A major source emphasizes that serving economics are constrained by the max of [[t_compute]] and [[t_memory]], with both GPU compute utilization and memory movement latency shaping cost.

- [[Transformer]] execution is interpreted as a two-phase flow: [[Prefill]] then [[Decode]].
- [[KVCache]] design and lifecycle dominates interactive cost and latency.
- GPU and memory systems alter throughput envelopes but do not remove the need for execution engineering.
- Cost control is linked to token economics via dynamic scheduling, context-length policy, and cache-aware runtime techniques.

### Software Paradigms and the AI Era Shift

A major interview source from [[Andrej Kapassi]] extends the software paradigm timeline into operational AI practice.

- [[Software 1.0]] is framed as explicit rule/code writing by developers.
- [[Software 2.0]] shifts emphasis to learned weights and model training.
- [[Software 3.0]] reframes programming as [[Prompting]] and orchestration where [[ContextWindow]] construction and agent handoff become first-class engineering tasks.
- The source argues that [[NeuralComputer]] patterns make many current abstractions transient.

### Compiler Design and Translation Infrastructure (2025 EuroLLVM)

A 2025 EuroLLVM source adds a strong compiler-design thread to the wiki by tracing how [[MLIR]] evolved into a reusable lowering pipeline toward [[LLVM]] backends.

- Early conversion from [[MLIR]] to [[LLVM IR]] was designed for minimal friction with LLVM and initially direct.
- As target coverage widened to [[GPU]], [[OpenMP]], and accelerators, design shifted to interface-driven lowering.
- Increasing dialect count raises compile-time and maintenance complexity, creating governance pressure for selective extension.

### Systems and Virtualization: QEMU Internals

A technical source provides a practical deep-dive into [[QEMU]] internals.

- [[QEMU]] executes guests through dynamic translation and object-model-driven device modeling.
- [[TCG]] translation blocks and SoftMMU memory flows are central to cross-ISA emulation.
- Debug workflows combine QMP/monitor controls with kernel-level and host-level GDB.

### ML Compiler Stacks and Heterogeneous Deployment (New)

A new source on [[IREE]] adds a compiler-centric thread focused on practical heterogeneous deployment.

- [[IREE]] applies a [[Host-Device Programming Model]]: host scheduling and dispatch orchestration preserve dependency clarity, then hand off compact command sequences to devices.
- [[MLIR]] is used for dialect-rich progressive lowering, enabling both high-level tensor programs and backend-facing programs.
- The final artifact, [[VMFB]], acts as a stable deployment unit; performance is practical with further custom tuning at dispatch level.
- Hardware extension remains centered on [[HAL]] and plugin-style integration.

### Representation Alignment for Robotics Mid-Training (New)

A new source for [[EmbodiedMidtrain]] extends the robotics thread from architecture change to data-level intervention.

- The core insight is that [[VLM]]과 [[VLA]] 간 성능 간극은 백본 크기 확장보다 [[DistributionShift]]와 target domain 정합으로 더 설명되기도 한다.
- [[ProximityEstimator|proximity estimator]] 기반으로 [[VLA]] 정합 샘플을 선별해 [[MidTraining]]을 수행하면 [[Calvin]], [[SimplerEnv]], [[LIBERO]] 벤치마크에서 일관된 성능 향상이 확인된다.
- sample-level selection은 무작위/거리 기반 대비 더 안정적이며, [[RepresentationAlignment]]을 개선한다.
- 동일 데이터 selection이 [[InternVL3.5|InternVL3.5-1B]]에서 뽑혀 [[Qwen3VL|Qwen3VL-2B]]로도 유의미하게 이전될 수 있어, 데이터 축의 도메인 신호가 모델별로 공유될 가능성을 보여준다.

### Robotics Study-Guide Consolidation

A practical study-guide style source provides implementation and QA synthesis for [[EmbodiedMidtrain]], including:

- 간단한 실습 설계(표기: [[CLIP]], [[SigLIP]], 로지스틱 회귀 기반 [[BinaryClassification]]).
- top-K selection 전후 분포 이동 확인( [[t-SNE]], [[UMAP]] )과 시각화 점검.
- ablation 세트(random/nearest-neighbor/learned)로 행동 성능 비교.
- “loss 유사하지만 task 성능 차이”를 [[ActionGrounding]], [[TemporalConsistency]], [[Robustness]]로 해석하는 분석.

### Open Questions

- How should we standardize validation for end-to-end autonomy when behavior must remain interpretable?
- Which long-tail metrics are sufficient when model behavior becomes more fused and less module-transparent?
- How should cross-domain simulation loops quantify tradeoffs between preemptive safety and comfort in AV-to-robot transfer?
- In compiler ecosystems, where should we draw the line between default transform coverage and custom plugin customization to avoid maintenance debt while still achieving target-specific peak performance?
- In systems emulation, what is the most effective test matrix for validating QEMU device emulation against real hardware semantics at API, timing, and interrupt fidelity levels?
- For robotics data pipelines, how much target-domain data is sufficient to train a reliable proximity estimator, and how does that threshold change by task family complexity?
- How should sample-level dataset selection balance diversity and embodiment alignment so that general visual-language ability is not lost while improving manipulation transfer?
- How can we measure when representation alignment gains saturate relative to scaling gains in multi-backbone VLA transfer?

## Recently Added (Autonomous Systems)

- [Tesla’s Shift to End-To-End Deep Learning: Full Breakdown](sources/tesla-s-shift-to-end-to-end-deep-learning-full-breakdown.md) — [[Tesla]]의 모듈형 경로에서 종단간 최적화로의 전환을 시간축으로 정리한다.
- [A Peek into Tesla’s Autonomous Future: Core Tech Revealed by VP Ashok Elluswamy at ICCV25 WDFM-AD](sources/a-peek-into-tesla-s-autonomous-future-core-tech-revealed-by-vp-ashok-elluswamy-at-iccv25-wdfm-ad.md) — [[Tesla]]의 end-to-end 철학과 로보틱스 확장 논리를 정리한다.
- [Ashok Elluswamy: Building Foundational Models for Robots at Tesla](sources/ashok-elluswamy-building-foundational-models-for-robots-at-tesla.md) — 파운데이션 모델 확장 논리를 정리한다.
- [Tesla's Occupancy Networks: A look at How They Work](sources/tesla-s-occupancy-networks-a-look-at-how-they-work.md) — 3D 점유 표현의 실전 장점을 정리한다.
- [2025 EuroLLVM - Deep Dive into the MLIR to LLVM IR Translation Mechanism](sources/2025-eurollvm-deep-dive-into-the-mlir-to-llvm-ir-translation-mechanism.md) — 다이얼렉트 및 인터페이스 기반 번역 구조의 역사적 진화를 정리한다.
- [QEMU 에뮬레이터 내부 구조: TCG, 메모리, 디바이스 모델링 및 디버깅](sources/qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅.md) — QEMU 런타임 번역과 SoftMMU 디버그 워크플로우를 정리한다.
- [Unveiling the Inner Workings of IREE: An MLIR-Based Compiler for Diverse H/W](sources/unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w.md) — [[MLIR]] 기반 이기종 배포형 컴파일러의 구조와 스택 확장 전략을 정리한다.
- [EmbodiedMidtrain: VLM과 VLA 사이의 간극을 Mid-training으로 잇기](sources/embodiedmidtrain-2604-20012-ko-analysis.md) — [[VLM]] 데이터에서 [[VLA]] 정합 샘플을 뽑는 mid-training과 실증 성능 향상 경로를 정리한다.
- [EmbodiedMidtrain references and related work notes](sources/embodiedmidtrain-2604-20012-references.md) — [[EmbodiedMidtrain]]의 reference 맥락을 정리하고, [[ProximityEstimator]] 기반 샘플 선별이 [[RobotManipulation]] 성능에 미치는 영향을 정렬.
- [EmbodiedMidtrain study guide](sources/embodiedmidtrain-2604-20012-study-guide.md) — sample-level 데이터 정렬을 중심으로 한 실습/재현 프레임을 정리해 위키 지식체계에 바로 적용 가능한 체크리스트를 추가한다.

## Sources Ingested

See [Index](index.md) for full list.
