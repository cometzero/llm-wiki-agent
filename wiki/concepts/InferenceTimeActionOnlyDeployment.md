---
title: "Inference-Time Action-Only Deployment"
type: concept
tags: [embodied-ai, inference, control, optimization]
last_updated: 2026-07-29
sources:
  - worlddit-2607-23909-paper-ko
---

## 정의

[[InferenceTimeActionOnlyDeployment]]는 학습 단계에서 예측 보조 신호(world, aux tasks 등)를 사용하되, 실제 추론/배포에서는 액션 생성 분기만 남겨 경량 추론 경로를 사용하도록 설계한 운영 전략이다.

## 핵심 요소

- 학습 시 다중 분기: action + 보조 world 예측
- 추론 시 경량 분기 선택: action-only 경로
- 재계획 주기 결합: 주로 rolling/receding-horizon control (`execute first K steps`, replan)
- latency/안정성 trade-off 개선: 예측 분기 제거로 추론 비용 감소

## 관련 사례

- [[WorldDiT]]는 future RGB patch auxiliary를 학습에만 쓰고 추론에서 action branch만 사용해 이 개념의 대표적 예시를 제공한다.

## 사용 시점

- 액션 결정이 초당 빈번하게 요구되며, 보조 예측이 실시간성보다 학습 안정성에 도움이 되는 시나리오
- safety-critical 추론에서 uncertainty/failure detector와 결합이 필요한 환경
