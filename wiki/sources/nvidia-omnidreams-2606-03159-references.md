---
title: "NVIDIA OmniDreams: Closed-loop 자율주행 시뮬레이션을 위한 실시간 생성형 World Model — references"
type: source
tags: [autonomous-driving, world-model, closed-loop-simulation, references]
date: 2026-06-10
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W23/omnidreams-2606-03159/references.md
source_hash: ebdca4aa7d1d08fa
---

## Summary
OmniDreams 관련 핵심 레퍼런스를 PDF reference/related-work 섹션과 본문 citation을 기준으로 정리한 문서. [[Cosmos]], [[Alpamayo]], [[DiffusionForcing]], [[SelfForcing]], [[DistributionMatchingDistillation]] 등 WAM 기반 world model과 VLA 비교를 위한 배경 연구를 제공한다.

## Key References

### World Model & Diffusion Foundation
- **[[Cosmos]] / [[Cosmos-Predict2.5]]** — NVIDIA의 physical AI/world model 기반. OmniDreams의 visual prior와 diffusion backbone 출발점.
- **[[DiffusionForcing]]** (Chen et al., 2024) — bidirectional diffusion/video model을 causal autoregressive generation으로 바꾸기 위한 training method.
- **[[SelfForcing]]** (Huang et al., 2025) — teacher forcing과 inference self-rollout mismatch를 줄이기 위한 distillation/training framework.
- **[[DistributionMatchingDistillation]]** (Yin et al., 2024) — generated video distribution을 real data manifold로 맞추는 holistic objective.

### Autonomous Driving Policy
- **[[Alpamayo1]] / [[Alpamayo1.5]]** — NVIDIA 자율주행 policy/VLA baseline. OmniDreams closed-loop integration과 [[WorldActionModel]] 비교의 기준.
- **[[AlpaSim]]** — policy action과 simulator state update를 관리하는 orchestrator. OmniDreams를 reactive environment로 연결한다.
- **[[DriveDreamer]] / [[DriveWM]] 계열** — 자율주행 world model 연구의 전형적 배경.

### Simulators & Evaluation
- **[[NuRec]]** — reconstruction-based neural simulator. Photorealistic reconstruction은 강하지만 novel dynamic scenario 일반화가 제한적이다.
- **[[Waymo]] / [[CARLA]] / [[nuPlan]] style closed-loop evaluation** — open-loop metric 한계를 보완하는 평가 패러다임.

### Architecture Perspective
- **[[WorldActionModel]] (WAM) in robotics** — [[VLA]]와 대비되는 policy architecture 관점. OmniDreams는 AV에서도 WAM이 경쟁력 있음을 제시한다.

## Reading Priority

1. **[[Cosmos]] / [[Cosmos-Predict2.5]]** — backbone과 physical AI world model 관점
2. **[[DiffusionForcing]] + [[SelfForcing]]** — autoregressive video generation 안정화
3. **[[NuRec]] / reconstruction-based simulator** — 비교 대상의 한계 이해
4. **[[Alpamayo1]] / [[WorldActionModel]] vs [[VLA]]** — 자율주행 policy architecture 논쟁

## Connections
- [[OmniDreams]] — parent source
- [[WorldModel]] — broader concept this work builds upon
- [[VLA]] — competing architecture OmniDreams compares against
- [[ClosedLoopSimulation]] — evaluation paradigm
