---
title: "Qwen-RobotNav Technical Report — references"
type: source
tags: [references, VLA, embodied-navigation, autonomous-driving, VLN]
date: 2026-06-01
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W27/qwen-robotnav-2606-18112/references.md
source_hash: 58949d58903daa8f
---

## Summary
Qwen-RobotNav 관련 레퍼런스를 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축으로 정리한 문서이다. VLN/embodied navigation foundation model 계열, autonomous driving trajectory/planning 계열, agentic navigation/EQA 계열로 3축으로 분류하여 읽기 순서를 제안한다.

## Key References

### VLN/Embodied Navigation Foundation Model 계열
- **[[AllDayNav]]** (2026) — Hang Yin, Yinan Liang, Jiazhao Zhang, Jiahang Liu. Lifelong self-learning navigation framework that implicitly encodes scene dynamics into billion-scale parameters.
  - 관계: Qwen-RobotNav의 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교
  
- **[[GN0]]** (2026) — Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jian Dong. Unified paradigm for generation, evaluation, and policy learning in Vision-Language Navigation. GN-Mat dataset으로 대규모 navigation data 자동화 파이프라인 개발.
  - 관계: VLN task generalization과 long-horizon capability 배경

- **[[ABot-N0]]** (2026) — Zedong Chu, Shichao Xie, Xiaolong Wu, Yanfen Shen. Unified VLA foundation model achieving "Grand Unification" across 5 core tasks (Point-Goal, Object-Goal, Instruction-Following, POI-Goal, Person-Following). Hierarchical "Brain-Action" architecture with LLM-based Cognitive Brain.
  - 관계: Qwen-RobotNav의 agentic navigation dual-system interface와 직접 비교 가능

- **[[VLN-MME]]** (2025) — Xunyi Zhao, G. Zhou, Qi Wu. Diagnosing MLLMs as language-guided visual navigation agents.
  - 관계: VLN에서 [[MultimodalLLM]] 성능 평가 프레임워크

### Autonomous Driving Trajectory/Planning 계열
- **[[Planning-aligned Token Compression]]** (2026) — Zhixuan Liang, Yuxiao Chen, Yurong You, Peter Karkus. Monolithic vision-action models의 token sequences가 real-time computational budget을 초과하는 문제 해결을 위한 planning-aligned token compression.
  - 관계: VLA deployment의 inference efficiency 병목 해결책과 직접 관련

- **[[ColaVLA]]** (2025) — Qihang Peng, Xuesong Chen, Chen Yang, Shaoshuai Shi. Cognitive latent reasoning for hierarchical parallel trajectory planning in autonomous driving. VLM-based planner의 세 가지 challenge 해결.
  - 관계: autonomous driving trajectory planning의 hierarchical approach와 관련

### Agentic Navigation/EQA 계열
- **[[FAST-EQA]]** (2026) — Haochen Zhang, Nirav Savaliya, Faizan Siddiqui, Enna Sachdeva. Efficient Embodied Question Answering with global and local region relevancy. 물리적 검색을 question-relevant subspaces로 제한.
  - 관계: agentic navigation의 embodied reasoning과 직접 연결

- **Memory Centric Power Allocation for [[Multi-Agent Embodied QA]]** (2026) — Chengyang Li, Shuai Wang, Kejiang Ye, Weijie Yuan. Multi-agent EQA에서 memory quality 강조, quality of memory (QoM) model 제안.
  - 관계: long-horizon multi-agent scenario의 memory 관리와 관련

- **[[AstraNav-World]]** (2025) — Junjun Hu, Jintao Chen, Haochen Bai, Minghua Luo. End-to-end world model for foresight control and consistency. Diffusion-based video generator + vision-language policy 통합.
  - 관계: agentic navigation의 world modeling과 foresight planning과 관련

### Simulation/Data 계열
- **[[Habitat-GS]]** (2026) — Zi-Xiang Xia, Jing Xu, C. Cui, Yuanhong Yu. High-fidelity navigation simulator with Dynamic Gaussian Splatting. Mesh-based rasterization의 visual realism 한계를 해결.
  - 관계: embodied navigation training environment와 관련

## 읽는 순서 (Suggested Reading Path)
1. **VLN/embodied navigation foundation model 계열**: [[ABot-N0]], [[GN0]], [[AllDayNav]], [[VLN-MME]]
2. **Autonomous driving trajectory/planning 계열**: [[Planning-aligned Token Compression]], [[ColaVLA]], [[AstraNav-World]]
3. **Agentic navigation/EQA 계열**: [[FAST-EQA]], Memory Centric EQA, [[Habitat-GS]]

## Key Concepts Covered
- [[Vision-Language Navigation (VLN)]] — embodied agent navigation with language instructions
- [[VLA]] — unified vision-language-action model for multiple navigation tasks
- [[Embodied Question Answering (EQA)]] — query robot teams on what they have seen
- [[Lifelong Navigation]] — persistent scene understanding from fragmentary observations
- [[Planning-aligned-Token-Compression]] — making long-context VLA inference computationally feasible
- [[World Model]] — joint reasoning about future visual states and action sequences

## Connections
- [[QwenRobotNav]] — primary source; 이 references 문서의 대상 논문
- [[ABot-N0]] — VLA foundation model의 "Grand Unification" 접근법; Qwen-RobotNav의 dual-system과 비교 가능
- [[Planning-aligned Token Compression]] — VLA deployment efficiency 문제의 솔루션
- [[FAST-EQA]] — embodied agent reasoning의 benchmark
- [[ColaVLA]] — hierarchical trajectory planning의 접근법

## Contradictions
- 없음. 기존 wiki 문서와 직접적 모순 없음.
