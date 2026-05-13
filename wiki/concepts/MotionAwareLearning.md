---
title: "Motion-aware Learning"
type: concept
tags: [robotics, video-learning, motion]
sources: [humannet-2605-06747]
last_updated: 2026-05-13
---

HumanNet이 제안한 학습 패러다임으로, 비디오에서 물체(object)와 손/몸의 움직임을 동시에 이해하여 물리적 상호작용을 학습한다.

**구성 요소:**
- 3D hand/body pose detection
- Monocular SLAM
- Motion retargeting
- Action ordering

**목표:**
- Hand-object contact 이해
- Body motion pattern 학습
- Physical state change 포착

**[[VLA]] 학습에서의 역할:**
- Action grounding의 원천
- Robot-relevant kinematics 제공
- Egocentric view와 exocentric view의 결합

**연관:**
- [[HumanNet]] — 제안된 데이터셋
- [[InteractionAwareLearning]] — 관련 개념
- [[RobotLearning]] — 적용 대상
