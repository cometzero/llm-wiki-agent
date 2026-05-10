---
title: "EndToEndDeepLearning"
type: concept
tags: [DeepLearning, AutonomousVehicle, FSD, EndToEndAutonomy]
sources:
  - tesla-s-shift-to-end-to-end-deep-learning-full-breakdown
last_updated: 2026-05-10
---

## Definition
[[EndToEndDeepLearning]]은 전체 의사결정 파이프라인을 분리된 모듈 손실 함수가 아니라 단일 목표 함수로 통합해 학습하는 접근이다. 

## 핵심 아이디어
- [[Perception]]과 [[Planning]]을 서로 독립적으로 학습하는 것이 아니라, 상호작용을 반영한 공동 최적화를 수행한다.
- 출력 단계에서 조향·감속·가속 같은 제어 신호가 전 과정을 통해 직접 영향을 받도록 설계한다.

## Why It Matters
자율주행/로보틱스에서 모듈 경계에서의 정보 손실을 줄이고, 희귀한 엣지케이스에서 더 일관된 장기 행동을 기대할 수 있다.
