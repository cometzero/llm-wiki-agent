---
title: "DriveWAM"
type: entity
tags:
  - world-action-model
  - autonomous-driving
  - video-generative-prior
sources:
  - simwam-2608-07468-references
last_updated: 2026-08-12
---

## 개요
[[DriveWAM]]는 자율주행용 [[WorldActionModel]] 계열에서 비디오 생성 prior를 action modeling에 결합하는 대표 선행군으로 언급되는 연구군이다.

## 핵심 역할
- [[SimWAM]]의 design space를 이해할 때, training-time world dynamics 학습을 어떤 수준까지 외연화할 수 있는지 비교하는 기준점.
- 비디오 생성 branch 의존도가 높은 WAM 설정에서, 추론 비용과 latency를 어디서 줄일 수 있는지 추정하는 비교군.

## 관계
- [[SimWAM]]은 이 계열의 “학습-배포 분리” 변형으로, SimWAM 참고 레퍼런스에서 동일 계열 비교군으로 정렬됨.
- [[DriveVA]], [[DriveDreamer-Policy]], [[Fast-WAM]]와 함께 [[AutonomousDrivingVLA]]에서 world-action 대체축으로 함께 읽히는 논문군.

## 관련 개념
- [[WorldActionModel]]
- VideoWorldModel
- [[InferenceTimeActionOnlyDeployment]]
