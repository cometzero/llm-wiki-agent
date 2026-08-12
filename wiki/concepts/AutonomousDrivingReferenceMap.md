---
title: "AutonomousDriving Reference Map"
type: concept
tags:
  - autonomous-driving
  - world-action-model
  - literature-map
sources:
  - simwam-2608-07468-references
last_updated: 2026-08-12
---

## 개요
[[AutonomousDrivingReferenceMap]]는 자율주행 WAM/AD planning 계열의 선행 연구를 설계축별로 정렬해 읽는 맵 개념이다. 특히 [[SimWAM]] 문맥에서 `world prior`, `inference-time budget`, `zero-shot transfer`, `test-time imagination`의 대조축을 한 번에 잡는 데 쓰인다.

## 읽기 축
- 학습-추론 분리 축: [[SimWAM]] 대 [[DriveDreamer-Policy]], Uni-World VLA
- action leakage 제어 축: [[IsolatedAttentionMask]], [[FlowMatching]]
- zero-shot 전이 축: World Action Models are Zero-shot Policies, nuScenes, [[AD-MCQ]]
- test-time imagination 축: [[Fast-WAM]]

## 관련 엔티티
- [[DriveWAM]]
- [[DriveVA]]
- [[ExploreVLA]]
- [[DriveDreamer-Policy]]
- Uni-World VLA
- DriveLaW
- [[SimWAM]]

## 비고
이 맵은 문헌 정리용 개념으로, 개별 성능 비교 수치 자체보다 design choice의 상호 비교를 강조한다.
