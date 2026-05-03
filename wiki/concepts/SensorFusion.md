---
title: "Sensor Fusion"
type: concept
tags:
  - AutonomousDriving
  - Multimodal
  - Perception
  - Radar
  - Camera
sources:
  - how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy-nvidia-technical-blog
last_updated: 2026-05-03
---

## 핵심 정의
[[SensorFusion]]은 서로 다른 센서의 정보를 정렬·정합하여 단일 환경 인식 표현으로 통합하는 과정이다.

## 이 소스의 핵심 주제
본 소스는 신호 레벨 단계에서 레이더 융합을 강조한다.
- 다중 레이더 간 신호 정합
- 카메라와의 타임스탬프 동기화
- 포인트클라우드 이전 표현을 결합해 고밀도 감지 신뢰성 강화

## 주요 이점
- 엣지 축약 데이터보다 높은 충실도의 멀티센서 결합
- 악천후/간섭 시나리오에서 커버리지 개선 잠재

## Linked Nodes
- [[NVIDIA DRIVE]]
- [[CentralizedRadarProcessing]]
- [[RawADC]]
- [[RangeDopplerMap]]
- [[Level4Autonomy]]
- [[VLA]]