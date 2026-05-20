---
title: "VLA (Vision-Language-Action)"
type: concept
tags: [robotics, multimodal, policy-learning]
sources: [physbrain-1-0-2605-15298-analysis, humannet-2605-06747-analysis, reflectdrive-2-2605-04647-analysis, embodiedmidtrain-2604-20012-ko-analysis]
last_updated: 2026-05-20
---

## Overview
VLA(Vision-Language-Action)는 vision과 language 입력을 기반으로 robot action을 생성하는 정책(policy) 모델이다. [[VLM]]의 시각적 이해能力和 언어적 추론能力을 robot control에 확장한 것으로, end-to-end로 학습되어 language-conditioned robotic action을 출력한다.

## Key Characteristics
- **입력**: Visual observation (image/video) + Language instruction
- **출력**: Robot action (continuous control 또는 discrete action token)
- **학습 방식**: Robot trajectory imitation, RL fine-tuning, 또는 VLM에서 adaptation

## Related Concepts
- [[physbrain-1-0-2605-15298]] — physical commonsense를 VLA로 전이하는 연구
- [[HumanNet]] — VLA pretraining용 human-centric video corpus
- [[ReflectDrive2]] — driving domain의 VLA planner
- [[EmbodiedMidtrain]] — VLM과 VLA 사이의 간극을 mid-training으로 극복
- [[NVIDIAGR00T]], [[GeminiRobotics]], [[PhysicalIntelligencePi]] — 주요 VLA 모델들

## Challenges
- Robot data의稀缺성 (expensive, platform-specific)
- Out-of-distribution generalization
- Physical commonsense 부족으로 인한 action grounding 실패
