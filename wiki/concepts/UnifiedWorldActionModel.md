---
title: "Unified World-Action Modeling"
type: concept
tags:
  - world-model
  - action-generation
  - diffusion
  - robotics
  - embodied-ai
sources:
  - worlddit-2607-23909-paper-ko
last_updated: 2026-07-29
---

## Unified World-Action Modeling

**Unified World-Action Modeling**은 한 개의 예측기에서 `action`과 `future observation`을 모두 다루는 방식이다. 로봇 제어에서는 이를 통해 정책이 행동이 유발할 미래 장면/상태 신호를 보조적으로 반영하며 학습된다.

## 핵심 원리

- action branch와 visual 미래 예측 branch를 별도 모델이 아니라 같은 shared 백본에서 학습
- action target/예측 보조 목표를 결합 손실로 처리
- inference에서는 task 목적에 맞춰 action-only 경로로 경량화

## 구현 예시

- [[WorldDiT]]: shared [[DiffusionTransformer]로 `continuous action` chunk와 future normalized RGB patch patch token velocity를 동시 학습.
- 학습: noise injection + `L_total = λ_action * L_action_velocity + λ_rgb * L_rgb_velocity`
- 배치 제어: receding window, 3-step 실행+재계획 운영

## 기대효과

- world signal을 직접 action branch로 억지로 주입하지 않고, shared backbone가 공통 표현을 통해 간접 정렬
- VLA/AD 설계에서 large action backbone 의존도를 낮추며 compact 모델의 성공률-파라미터 효율을 개선

## 관련 항목

- [[WorldActionModel]]
- [[FlowMatching]]
- [[DiffusionTransformer]]
- [[Model-PredictiveControl]]
- [[ActionGeneration]]
