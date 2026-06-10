---
title: "Vision-Language-Action (VLA)"
type: concept
tags: [robotics, multimodal, policy-learning]
sources: [tbd-vla-2606-07895, visualthink-vla-2605-30011, robosemanticbench-2606-02277, physbrain-1-0-2605-15298, reflectdrive-2-2605-04647, humannet-2605-06747, embodiedmidtrain-2604-20012]
last_updated: 2026-06-10
---

## Overview
**Vision-Language-Action (VLA)** 모델은 visual observation과 natural language instruction을 executable robot action으로 매핑하는 generalist robotic policy다. 최근 VLM(Vision-Language Model) backbone을 활용하여 visual understanding과 language instruction following capability를 robot control에 적용하는 방향으로 발전하고 있다.

## VLA Architecture Families

### 1. Continuous Action Expert Family
VLM은 perception/language reasoning 담당, 별도 action head가 continuous control 생성
- [[π0.5]], [[GR00T-N1]], [[SmolVLA]]

### 2. Autoregressive Discrete Action Token Family
Action을 discrete token으로 다루지만 token-by-token AR로 latency 증가
- [[OpenVLA]], [[MolmoAct]], [[VLA-0]]

### 3. Parallel/Diffusion Discrete Action Family
병렬성 활용하지만 temporal dependency 모델링 약함
- [[TBD-VLA]] (block-level AR 추가), [[OpenVLA-OFT]], [[DiscreteDiffusionVLA]]

## Key Research Areas
- [[SemanticGrounding]] — aligning language instructions with actions
- [[VisualReasoning]] — visual intermediate reasoning for action planning
- [[PhysicalCommonsense]] — physical understanding for manipulation

## Connections
- Backbone models: [[Qwen]], [[Qwen3-VL]], [[InternVLA-M1]]
- Benchmarks: [[LIBERO]], [[SimplerEnv]], [[RoboSemanticBench]], [[Calvin]]
- Related: [[EndToEndDeepLearning]], [[FoundationModel]]
