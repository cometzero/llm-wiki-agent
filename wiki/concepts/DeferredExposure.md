---
title: "Deferred Exposure"
type: concept
tags: [method, verifiability, reasoning, autonomous-driving]
sources:
  - deft-rlvr-2608-01755-paper-ko
last_updated: 2026-08-12
---

## Definition
[[DeferredExposure]]는 모델이 scene-level reasoning을 먼저 생성한 뒤, 예측/행동 후보나 미래 trajectory를 나중에 공개해 정답 선택을 수행하게 하는 학습·추론 설계이다.

## In DEFT context
- 1단계: **candidate-blind reasoning** — 장면 근거로 위험요인, 교통규칙, maneuver intent 등 생성
- 2단계: **candidate-grounded decision** — 후보 trajectory를 본 뒤, 앞 단계의 reasoning과 후보 간 연결을 점검해 선택

## Benefits
- post-hoc rationalization 유도 감소
- 추론 trace와 최종 선택의 정합성 검사 강화
- AD-MCQ 같은 candidate-based 벤치에서 검증 신뢰도 상승

## Connections
- [[DEFT-RLVR]]
- [[AD-MCQ]]
- [[RLVR]]
- [[AutonomousDrivingVLA]]

## Notes
본 논문은 AD-MCQ에서 candidate 지연 노출이 성능 및 신뢰성 균형을 동시에 개선하는 것으로 보고한다.