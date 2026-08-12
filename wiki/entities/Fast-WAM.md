---
title: "Fast-WAM"
type: entity
tags:
  - world-action-model
  - test-time-imagination
  - autonomous-driving
sources:
  - simwam-2608-07468-references
last_updated: 2026-08-12
---

## 개요
[[Fast-WAM]]은 test-time future imagination의 필요성을 직접적으로 묻는 연구군이다.

## 핵심 연결
- [[SimWAM]]의 핵심 논점(미래 video를 훈련 신호로만 사용해도 되는가)에 대한 실험적 반대축으로 활용됨.
- 추론 비용과 미래 예측 품질 간 trade-off를 검증하는 중요한 비교군.

## 관계
- [[SimWAM]]: future video prior 의존도 축 비교군.
- [[IsolatedAttentionMask]]: 정보 누설 제어가 필요한 환경에서의 대체 접근점 관찰 재료.

## 관련 개념
- [[WorldActionModel]]
- [[InferenceTimeActionOnlyDeployment]]
- [[FlowMatching]]
