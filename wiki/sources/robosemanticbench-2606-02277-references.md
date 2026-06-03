---
title: "RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기 — references"
type: source
tags: [vla, semantic-grounding, benchmark, robotics, references]
date: 2026-06-03
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W23/robosemanticbench-2606-02277/references.md
source_hash: 6e176a2b3d921962
---

## Summary
RoboSemanticBench(arXiv:2606.02277)의 관련 연구 레퍼런스 10편을 정리한 페이지. VLA(Vision-Language-Action) 모델의 [[SemanticGrounding]] 실패를 진단하는 RSB benchmark의 이론적·평가적 배경을 제공한다. 핵심 레퍼런스는 [[LanguageGrounding]]이 action으로 전달되는지라는 질문과 직접 연결된다.

## Key References

### UAM: A Dual-Stream Perspective on Forgetting in VLA Training
- **arXiv:** 2605.15735
- **Authors:** [[Jianke Zhang]], [[Yuanfei Luo]], [[Yucheng Hu]]
- **Citations:** 1
- **관계:** VLA [[Forgetting]] 메커니즘에 대한 dual-stream 분석으로 [[SemanticGrounding]] 손실과 관련

### StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing
- **arXiv:** 2604.05014
- **Authors:** [[S. Community]]
- **Citations:** 34
- **관계:** [[StarVLA]] 코드베이스로 VLA 개발 표준화, [[SemanticGrounding]] → action 연결 검증에 핵심

### vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models
- **arXiv:** 2603.13966
- **Authors:** [[Suhwan Choi]], [[YUN-OO Lee]], [[Yubeen Park]]
- **Citations:** 3
- **관계:** [[VLA]] 평가 프로토콜 표준화. RoboSemanticBench는 이 평가 체계의 [[GroundingLatency]] 차원 보완

### Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration
- **arXiv:** 2603.06001
- **Authors:** [[Ning Zhang]], [[Bin Zhu]], [[Shijie Zhou]]
- **Citations:** 3
- **관계:** [[AttentionRecalibration]]로 [[SemanticGrounding]] 복원 기법. RSB와 직접 연결

### When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs
- **arXiv:** 2602.17659
- **Authors:** [[Yu Fang]], [[Yuchun Feng]], [[Dong Jing]]
- **Citations:** 4
- **관계:** VLA의 [[CounterfactualFailure]] 분석. [[VisionOverride]] → [[GroundingLoss]] 병목 연구

### LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries
- **arXiv:** 2601.15197
- **Authors:** [[Shijie Lian]], [[Bin Yu]], [[Xiaopeng Lin]]
- **Citations:** 10
- **관계:** [[LangForce]] 프레임워크로 [[LanguageGrounding]] → [[ActionPrediction]] 변환 분석

### TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers
- **arXiv:** 2601.14133
- **Authors:** [[Bin Yu]], [[Shijie Lian]], [[Xiaopeng Lin]]
- **Citations:** 11
- **관계:** [[TwinBrainVLA]] 아키텍처로 VLM의 [[EmbodiedTask]] 적용 연구

### Limited Linguistic Diversity in Embodied AI Datasets
- **arXiv:** 2601.03136
- **Authors:** [[Selma Wanna]], [[Agnes Luhtaru]], [[Jonathan Salfity]]
- **Citations:** 3
- **관계:** [[EmbodiedAI]] 데이터셋의 [[LinguisticDiversity]] 부족 → [[SemanticGrounding]] 제한 분석

### How Do VLAs Effectively Inherit from VLMs?
- **arXiv:** 2511.06619
- **Authors:** [[Chuheng Zhang]], [[Rushuai Yang]], [[Xiaoyu Chen]]
- **Citations:** 6
- **관계:** [[VLA]]의 [[VLMPretraining]] 상속 메커니즘 연구. [[SemanticGrounding]] 전달 경로 분석

### Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting
- **arXiv:** 2509.22195
- **Authors:** [[Asher Hancock]], [[Xindi Wu]], [[Lihan Zha]]
- **Citations:** 31
- **관계:** [[ActionsAsLanguage]] 패러다임으로 [[CatastrophicForgetting]] 없이 VLM→VLA 변환 연구

## Connections
- [[RoboSemanticBench]] — 이 레퍼런스들의 평가 대상 benchmark
- [[SemanticGrounding]] — 공통 핵심 개념
- [[VLA]] — 공통 연구 대상
- [[OpenVLA]], [[GR00T]] — 관련 VLA 모델

## Contradictions
- 없음
