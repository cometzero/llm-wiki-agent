---
title: "SimWAM"
type: entity
last_updated: 2026-08-12
tags:
  - autonomous-driving
  - world-action-model
  - flow-matching
  - low-latency
  - action-planner
sources:
  - simwam-2608-07468
---

## 개요
**[[SimWAM]]**은 자율주행 분야의 [[WorldActionModel]] 계열로, 학습 단계에서 VideoWorldModel의 표현력을 교사 신호처럼 사용하고 배포 시에는 [[Action]] branch만 남기는 저지연 구조를 제안한다.

## 핵심 특성
- 훈련에서는 [[FlowMatching]]과 대형 비디오 백본(Wan2.2-5B 등)을 통해 미래 동역학 신호를 반영한다.
- 배포에서는 [[IsolatedAttentionMask]]로 분리된 [[InferenceTimeActionOnlyDeployment]] 경로를 사용해 영상 분기 없이 action trajectory를 직접 생성한다.
- action branch와 video branch의 파라미터를 분리해 action scaling 및 경량 실행이 유리하다.
- NAVSIM에서 PDMS 개선과 RL 정렬 실험을 보고한다.

## 실험 포인트
- action-only baseline 대비 video prior 반영 및 RL 보상 결합에서의 단계적 개선(ablation 기반)이 중요.
- 실차 배포에서는 센서 결함, 장거리 규칙 위반, 극단 OOD에서 추가 안전성 검증이 필요.

## 관련 링크
- [[FlowMatching]]
- InferenceTimeActionOnlyDeployment
- [[IsolatedAttentionMask]]
- [[NAVSIM]]
- nuScenes
