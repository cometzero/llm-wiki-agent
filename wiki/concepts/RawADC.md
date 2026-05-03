---
title: "Raw ADC"
type: concept
tags:
  - SensorData
  - Radar
  - SignalProcessing
  - DataFidelity
sources:
  - how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy-nvidia-technical-blog
last_updated: 2026-05-03
---

## 핵심 정의
[[RawADC]]는 레이더 신호의 디지털 샘플링 최종 원시 입력 형태로, 센서 앞단에서 즉시 생성되는 저수준 물리 신호이다.

## 왜 중요한가
중앙 집중형 처리에서는 센서 엣지에서 고정된 축약 결과를 출력하는 대신 [[RawADC]]를 플랫폼으로 이동시켜 정보량 손실을 줄인다.

## 관련 파이프라인
- 센서 동기화 및 드라이버 스택을 통해 중앙 메모리로 수집
- [[ProgrammableVisionAccelerator]]에서 신호 처리 체인 수행
- [[RangeDopplerMap]] 등 신호 표상 생성 및 상위 AI 접근

## Benefits
- 포인트클라우드로만 보낼 때 대비 신호 밀도/주파수 도메인 정보 보존
- 다중 센서 공동 학습과 신호 수준 융합 모델에 적합

## Links
- [[CentralizedRadarProcessing]]
- [[NVIDIA DRIVE]]
- [[SensorFusion]]
- [[VLA]]