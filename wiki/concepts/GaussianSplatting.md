---
title: "Gaussian Splatting"
type: concept
tags: [ComputerVision, 3DReconstruction, Autonomy, Rendering]
last_updated: 2026-05-10
sources:
  - tesla-s-ai-can-explain-itself-ashok-s-mind-blowing-fsd-demo
---

## Summary
[[GaussianSplatting]]은 다수 카메라 시점에서 연속적인 3D 장면을 빠르게 재구성하는 기법군으로, 이번 소스에서 [[Tesla]] FSD의 장면 인식 및 안전성 설명력 향상 목적에 연결되어 소개된다.

## Key Claims
- 기존 가우시안 기반 방식의 시점 특이성/왜곡 문제를 낮추고, 장면 전환이 잦은 자율주행 환경에서도 더 일관된 공간 표현을 제공한다.
- Tesla 사례에서 의미론적 객체 정보와 기하(geometry) 정합성을 함께 유지해 행동 판단(우회/회피/제동)에 쓰일 수 있다.
- 빠른 업데이트 주기(수백 ms 수준)는 실시간 제어 친화성을 높이고 디버깅 및 관측 가능성에 기여한다.

## Connections
- [[Tesla]]
- [[EndToEndAutonomy]]
- [[AutonomousVehicle]]
- [[GaussianModeling]]
- [[FSD]]
- [[SceneUnderstanding]]
- [[System2]]
