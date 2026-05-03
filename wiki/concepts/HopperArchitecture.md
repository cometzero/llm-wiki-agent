---
title: "Hopper Architecture"
type: concept
tags:
  - NVIDIA
  - AI
  - HPC
  - GPU
  - Architecture
sources:
  - nvidia-hopper-아키텍처-심층-분석하기-nvidia-technical-blog
last_updated: 2026-05-03
---

## Definition
[[HopperArchitecture]]은 [[H100]]/[[GH100]] 세대에서 나타나는 AI 데이터센터 아키텍처 설계 계열로, 연산 유닛 확대, 고대역폭 메모리, 네트워크 확장, 동기/비동기 실행 모델을 통합한다.

## 핵심 구성 요소
- 4세대 [[TensorCores]] 및 텐서/FP 계산 경로의 강화.
- [[FP8]]를 포함한 정밀도 동적 조정 설계.
- [[TransformerEngine|Transformer Engine]] 기반의 대형 모델 적합성.
- [[ThreadBlockCluster]]와 [[TensorMemoryAccelerator|TMA]] 중심의 비동기 실행 패턴.
- [[DPX]]와 같은 특수 명령어를 활용한 워크로드 특화 가속.
- [[MIG]]와 [[ConfidentialComputing]] 결합으로 격리형 배치 운용.

## 성능 의미
성능 향상은 단일 지표가 아니라 네트워크-메모리-연산-동기화의 동시 최적화로 이해되어야 한다.

## 관련
- [[H100]]은 HopperArchitecture의 대표 구현.
- [[NVLink]], [[NVSwitch]], [[PCIeGen5]]는 이 아키텍처의 스케일링 축이다.
- [[AsynchronousExecution]]은 동시성 극대화의 실행 모델 축이다.
