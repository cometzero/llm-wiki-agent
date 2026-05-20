---
title: "Egocentric Data Collection"
type: concept
tags: [data-collection, VLA, robotics, embodied-AI]
sources: [mobileego-anywhere-2605-05945-analysis, humannet-2605-06747-analysis, humannet-2605-06747-learning]
last_updated: 2026-05-20
---

## Definition
제3자 시점이 아닌 착용자(행위자) 시점에서第一人称 시점(egocentric perspective)으로 비디오, 센서 데이터, trajectory를 수집하는 방법론.

## Why It Matters for VLA
- VLA 정책이 인간의 동작을 모방(behavior cloning)하려면 인간의 수행 데이터가 필요
- 기존 robot demonstration은expensive hardware, limited diversity制约
- human egocentric video는 더 저렴하고 다양한 환경에서 대규모 수집 가능
- 단, human hand trajectory → robot end-effector로의 IK/retargeting gap이 과제

## Key Projects
- [[mobileego-anywhere-2605-05945]] — iPhone 기반 200시간 household 데이터
- [[HumanNet]] — 100만 시간 규모 egocentric video corpus
- [[Ego4D]] — 3,000시간 이상의 일상 활동 egocentric 데이터
- [[EPIC-KITCHENS]] — 주방 중심 egocentric 액션 데이터

## Technical Requirements
| Requirement | Description |
|---|---|
| RGB-D | Depth 정보로 3D 복원 |
| 6-DoF Pose | Head/body 위치·자세 추적 |
| Hand Trajectory | 3D 손 위치로 action grounding |
| Hierarchical Labels | Long-horizon task structure |

## Connection to Other Concepts
- [[VLA]] — downstream 활용
- [[ActionGrounding]] — human-to-robot mapping 핵심 문제
- [[LongHorizonTrajectory]] — VLA 학습에 필요한 동작 연속성
- [[VisualSpatialRepresentation]] — egocentric 기반 표현 학습
