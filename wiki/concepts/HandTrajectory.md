---
title: "Hand Trajectory"
type: concept
tags: [robotics, manipulation, hand-tracking]
sources: [mobileego-anywhere-2605-05945]
last_updated: 2026-05-20
---

## Definition
3D 공간에서 인간의 손 움직임을 추적한 경로. 2D keypoint를 depth로 unproject한 뒤 camera pose로 global frame에 정렬하여 생성.

## MobileEgo Anywhere Implementation
- **Input**: 2D hand keypoint + LiDAR depth map + ARKit 6-DoF pose
- **Model**: WiLoR 기반 21-joint MANO hand pose estimation
- **Output**: world frame에 anchor된 3D hand trajectory
- **품질**: bone length CV median 1.27%~1.43% (pinky distal phalanx 제외 1% 미만)

## VLA 학습에서의 역할
Human motion을 robot end-effector frame으로 매핑하는 supervision 역할. atomic action label과 함께 low-level manipulation primitive 학습에 활용.

## Connections
- [[mobileego-anywhere-2605-05945]] — 수집 프레임워크
- [[WiLoR]] — hand estimation 모델
- [[VLA]] — supervision target
- [[MANO]] — hand skeleton 모델
