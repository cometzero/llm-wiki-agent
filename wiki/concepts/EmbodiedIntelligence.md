---
title: "Embodied Intelligence"
type: concept
tags: [AI, robotics, embodied-AI, physical-AI]
sources: [humannet-2605-06747, embodiedmidtrain-2604-20012-ko-analysis]
last_updated: 2026-05-13
---

환경과 물리적으로 상호작용하는 AI 시스템에 대한 연구 분야. [[VLM]]과 달리 실제 세계의 물리적 제약을 가진 행동을 수행한다.

**핵심 병목:**
- 기존 연구: 작은 robot log, 특정 플랫폼, 특정 control interface에 묶여 있음
- HumanNet 논문: "모델 크기보다 데이터 인프라 병목에 더 강하게 묶여 있다"

**접근 방식:**
1. **Data-centric**: [[HumanNet]] — 인간 활동 비디오의 스케일링
2. **Alignment-centric**: [[EmbodiedMidtrain]] — VLM-VLA 분포 정렬

**응용 분야:**
- Autonomous vehicles
- Robotics (manipulation, locomotion, navigation)
- Human-robot interaction

**연관:**
- [[VLA]] — vision-language-action model
- [[RobotLearning]] — 구체적 학습 방법
- [[PhysicalAI]] — 더 넓은 범위
- [[FoundationModels]] — 기반 모델
