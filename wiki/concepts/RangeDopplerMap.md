---
title: "Range-Doppler Map"
type: concept
tags:
  - RadarSignal
  - Spectrogram
  - FrequencyDomain
  - SensorProcessing
sources:
  - how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy-nvidia-technical-blog
last_updated: 2026-05-03
---

## 핵심 정의
[[RangeDopplerMap]]는 레이더 신호를 거리(range)와 도플러 속도 축으로 변환한 중간 출력이며, 신호 레벨 분석·시각화·학습 입력으로 사용될 수 있다.

## Source Context
중앙 집중식 레이더 처리에서 [[NVIDIA DRIVE]]는 이 출력과 각도-FFT 맵을 상위 레이어가 직접 접근하도록 한다.

## Use Cases
- 신호 기반 다중센서 융합
- 초기 물체 탐지 전 처리
- 신경망 기반 표상 학습 입력

## Relationships
- [[CentralizedRadarProcessing]]
- [[RawADC]]
- [[ProgrammableVisionAccelerator|PVA]]
- [[SensorFusion]]
- [[ADAS]]