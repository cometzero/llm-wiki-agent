---
title: "HydraNet"
type: entity
tags: [Tesla, Perception, ComputerVision, MultiTaskLearning]
sources:
  - tesla-s-shift-to-end-to-end-deep-learning-full-breakdown
last_updated: 2026-05-10
---

## Summary
[[HydraNet]]는 여러 인식 과업을 하나의 네트워크 백본에서 처리하는 멀티태스크 구조로, 같은 피처 인코딩을 공유하면서 객체/차선/차선경계 같은 인지 신호를 동시에 산출한다.

## Key Role
- [[Tesla]] 초기 자율주행 아키텍처에서 [[Perception]]의 핵심 백본 역할을 수행.
- 2D 기반 감지 성능을 강화하고, 후속 [[OccupancyNetwork]] 전환 이전까지의 기반 모듈로 사용됨.

## Notes
단일 모델로 다수 헤드를 운용함으로써 반복 계산을 줄이고, 2021년 [[Tesla]]의 모듈형 스택에서 주력 인지 블록으로 기록된다.
