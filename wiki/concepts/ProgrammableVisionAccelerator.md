---
title: "Programmable Vision Accelerator"
type: concept
tags:
  - NVIDIA
  - PVA
  - Accelerator
  - RadarSignalProcessing
  - DrivePlatform
sources:
  - how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy-nvidia-technical-blog
last_updated: 2026-05-03
---

## 핵심 정의
[[ProgrammableVisionAccelerator|PVA]]는 고성능 저전력의 신호 처리 가속기로, 본 소스에서 레이더 DSP 전체 체인을 중앙 플랫폼에서 수행하는 데 사용된다.

## 엔진 역할
- 레이더 ADC 입력을 기반으로 Range-Fast Fourier Transform, Doppler 처리, 각도 변환 등 표준/파생 DSP 단계 수행
- [[NVIDIA DRIVE]]의 [[GPU]]가 수행할 인지/계획 워크로드와 리소스 경합을 줄이기 위한 오프로드 장치 역할

## Source-backed Properties
- 높은 처리량의 반복 계산에 맞는 구조
- 결정적/예측 가능한 실행 패턴을 전개하기 쉬운 워크로드 성격
- DRAM에서 중간 출력(중간 주파수/공간 도메인)을 재사용 가능하게 유지

## Connections
- [[CentralizedRadarProcessing]]
- [[NVIDIA DRIVE]]
- [[RangeDopplerMap]]
- [[TensorCore]] (비교 아키텍처 맥락에서 리소스 분담 관점)

## Notes
문헌에서는 PVA를 통해 [[GPU]] 활용도를 줄이고 인지 모델·계획 모듈로 자원을 회수할 수 있다고 제시한다.