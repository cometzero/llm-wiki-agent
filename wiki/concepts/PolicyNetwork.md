---
title: "Policy Network"
type: concept
tags: [ReinforcementLearning, AutonomousVehicle, Robotics]
last_updated: 2026-05-10
sources:
  - tesla-s-ai-can-explain-itself-ashok-s-mind-blowing-fsd-demo
---

## Summary
[[PolicyNetwork]]는 상태/센서 입력을 받아 제어 출력(조향·가감속 등)으로 변환하는 핵심 신경망 계층으로, 본 소스에서는 [[Tesla]] 자율주행의 행동 결정 엔진으로 다루어진다.

## Key Claims
- 정책망은 즉시 반응 동작과 긴호흡 추론 결과를 모두 수용하면서, 위험 상황에서의 선제 제어에 사용된다.
- [[WorldSimulator]]에서의 반복 학습을 통해 정책망은 새로운 시나리오와 실패 케이스에 대한 일반화 성능을 강화할 수 있다.
- 사용자 질의형 디버깅("왜 그렇게 했는가")은 정책망의 내부 추론을 외부에서 점검하는 실무 경로가 될 수 있다.

## Connections
- [[ReinforcementLearning]]
- [[AutonomousVehicle]]
- [[FSD]]
- [[WorldSimulator]]
- [[System1]]
- [[System2]]
- [[ActionPrediction]]
