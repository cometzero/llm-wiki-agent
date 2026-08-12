---
title: "SimWAM 학습-배포 분리"
type: concept
tags:
  - training-inference-gap
  - autonomous-driving
  - world-model
  - action-only
sources:
  - simwam-2608-07468-paper-ko
last_updated: 2026-08-12
---

## 개념
[[SimWAM 학습-배포 분리]]는 학습 단계에서 world prior를 활용하고, 배포 단계에서는 해당 prior 경로를 제거해 action-only path만 쓰는 설계 방식이다. 핵심은 "학습 신호는 풍부한 모달리티를 쓰되, 런타임은 최소 경로로 줄인다"는 것이다.

## 구성
- 학습: 영상 생성/trajectory 생성기를 공동 학습
- 제약: [[IsolatedAttentionMask]]로 action branch 누출 억제
- 배포: 영상 branch 제거(속도·메모리 효율)
- fine-tune: [[ReinforcementLearning]]로 compositional reward 정렬

## 의의
- closed-loop AD 설정에서 latency-sensitive 배포 요구를 반영
- world-model 성능의 장점을 유지하면서 inference 계산량을 줄이는 선택지 제공
- [[InferenceTimeActionOnlyDeployment]]의 구체적 구현 패턴 중 하나

## 관련 항목
- [[SimWAM]]
- [[WorldActionModel]]
- [[FlowMatching]]
- [[IsolatedAttentionMask]]
- [[NAVSIM]]
- [[nuScenes]]