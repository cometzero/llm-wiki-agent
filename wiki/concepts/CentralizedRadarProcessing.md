---
title: "Centralized Radar Processing"
type: concept
tags:
  - Radar
  - NVIDIA
  - AutonomousDriving
  - SensorPipeline
  - SoftwareDefinedAutomotive
sources:
  - how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy-nvidia-technical-blog
last_updated: 2026-05-03
---

## 핵심 정의
[[CentralizedRadarProcessing]]은 레이더 신호의 전처리·신호처리 체인을 센서 엣지 SoC에서 중앙 플랫폼으로 이동해 수행하는 차량용 파이프라인 패턴이다.

## 핵심 원리
- 센서에서 [[RawADC]]를 직접 출력
- 고대역폭 통신으로 중앙 메모리로 스트리밍
- [[PVA]] 등 플랫폼 가속기에서 Range/Doppler/Angle 단계 처리 수행
- [[ADAS]] 상위 스택에 포인트클라우드 이전 표상까지 노출

## 소스 기반 인사이트
본 엔지니어링 접근은 기존 엣지 처리의 "압축 출력 위주" 한계를 넘어, 신호 풍부도를 높여 [[Level4Autonomy|L4 자율주행]] 인지 정확성과 학습 가능성을 개선한다.

## Benefits Claimed
- 데이터 손실 감소(포인트클라우드만 사용할 때 대비)
- 대규모 모델의 신호-레벨 학습에 유리
- 멀티센서 신호 정렬 기반 융합의 개선 가능성
- [[GPU]]를 인지/계획용으로 더 효율 배치

## Related Concepts
- [[RawADC]]
- [[ProgrammableVisionAccelerator|PVA]]
- [[SensorFusion]]
- [[RangeDopplerMap]]
- [[VLA]]
- [[NVIDIA DRIVE]]