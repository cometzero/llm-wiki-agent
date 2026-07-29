---
title: "Data Pyramid for Embodied Manipulation"
type: concept
tags:
  - data-strategy
  - embodied-ai
  - vision-language-action
  - alignment
sources:
  - data-pyramid-for-embodied-manipulation-2607-24744
last_updated: 2026-07-29
---

## 정의

`Data Pyramid for Embodied Manipulation`은 로봇 정책 학습에서 데이터의 효율을 `robot execution alignment` 기준으로 5단으로 정렬하는 설계도다.

## 5개 층

- **Real-Robot Data**: 실제 동작/제어 신호가 있는 최고 정렬층.
- **UMI-style Data**: object/end-effector 중심 데모를 low-cost로 획득하는 전이 계층.
- **Egocentric/Exocentric Data**: 인간 상호작용 다양성, 장면 분해와 지시문 표현 강화.
- **Simulation Data**: 폐루프 대량 생성과 privileged label 보완.
- **General VLM Data**: 일반 멀티모달 의미론과 규칙/상식 정보 보강.

## 핵심 메시지

- 실사용 [[VisionLanguageAction]]의 병목은 모델 크기보다 데이터 레시피의 정렬이다.
- [[ActionGrounding]]이 약한 데이터는 semantic 성능을 높여도 closed-loop 실환경 성능으로 잘 안 넘어간다.
- 실패/복구, rare case, [[TactileSensing]] 빈약성은 별도 축에서 보완해야 한다.

## 연결

- [[RobotAlignment]], [[CrossEmbodimentAlignment]], [[PhysicalFidelity]], [[WorldActionModel]], [[AutonomousDrivingVLA]], [[FailureRecoveryTrajectory]]
