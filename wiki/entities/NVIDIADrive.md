---
title: "NVIDIA DRIVE"
type: entity
tags:
  - Automotive
  - AutonomousDriving
  - Radar
  - EdgeToCloud
  - SensorFusion
sources:
  - how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy-nvidia-technical-blog
last_updated: 2026-05-03
---

## Overview
[[NVIDIA DRIVE]]는 자율주행 차량용 소프트웨어 및 계산 플랫폼으로, 이번 소스에서는 레이더 처리의 중앙 집중화를 수행하는 핵심 실행 환경으로 다뤄진다.

## Role in this Source
- 센서에서 생성된 [[RawADC|원시 ADC]]를 플랫폼 메모리로 수집·동기화
- [[PVA]] 기반 레이더 DSP를 운용해 신호 처리 체인을 중앙화
- 레이더 신호의 중간 출력(예: [[RangeDopplerMap]])을 상위 인지/계획 모듈이 활용할 수 있도록 노출

## Key Claims Confirmed
- 엣지 방식 대비 더 높은 레이더 데이터 충실도를 공급 가능
- [[ADAS]]/L4 스택에서 저수준 멀티모달 학습 및 융합 모델 설계를 지원
- [[CentralizedRadarProcessing]] 구현을 통해 [[GPU]]를 인지 및 계획 워크로드에 집중 배치

## Associated Pages
- [[NVIDIA DRIVE AGX Thor]]
- [[CentralizedRadarProcessing]]
- [[ProgrammableVisionAccelerator|PVA]]
- [[DriveDriverStack|DRIVE driver stack]]
- [[VLA]]

## Notes
이 항목은 기존 [[NVIDIA]] 인프라 문헌(추론/컴퓨팅/시스템 효율)과 달리 차량 센서 처리의 플랫폼 통합 관점에서 위치한다.