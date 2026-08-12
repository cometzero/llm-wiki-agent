---
title: "DriveVA"
type: entity
tags:
  - autonomous-driving
  - video-action-model
  - zero-shot
sources:
  - simwam-2608-07468-references
last_updated: 2026-08-12
---

## 개요
[[DriveVA]]는 video action model이 driving policy에 쓰이는 AD 설계군으로 정리되는 연구군으로, 영상 역학과 행동 예측의 연결성 비교에서 참고됨.

## 핵심 연결
- [[SimWAM]]의 zero-shot 전이 성능(예: nuScenes)을 이해할 때, video dynamics→action 연결 baseline으로 읽힌다.
- [[DriveVA]]는 [[AD-MCQ]]와 정량 검증 체계보다 action policy 성능에 가까운 설계 비교 포인트를 제공한다.

## 관계
- [[SimWAM]]: 학습에 world prior 활용 + 추론 경량화라는 axis 대비군.
- [[DEFT-RLVR]]: 추론 과정의 근거 정합 문제와 직접 1:1 대응은 아니나, 의사결정 신뢰성 관점 비교의 배경군.

## 관련 개념
- [[WorldActionModel]]
- [[Action]] trajectory prediction
- Zero-shot transfer
