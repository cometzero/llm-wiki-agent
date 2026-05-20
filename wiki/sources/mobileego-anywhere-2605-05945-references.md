---
title: "MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라 — references"
type: source
tags: [egocentric-vision, robotics, VLA, datasets, references]
date: 2026-05-20
sources: [mobileego-anywhere-2605-05945]
last_updated: 2026-05-20
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W21/mobileego-anywhere-2605-05945/references.md
source_hash: 3c030a671e0b4b0f
---

## Summary
MobileEgo Anywhere의 관련 연구 레퍼런스 10편을 정리한 페이지로, [[EgoScale]], [[UMI]], [[Ego4D]], [[EPIC-KITCHENS]], [[Ego-Exo4D]], [[HOI4D]], [[HOT3D]], [[ARCTIC]], [[WiLoR]], [[MCAP]] 등 egocentric vision, dexterity manipulation, hand tracking 분야의 핵심 데이터셋과 방법을 소개한다.

## Key References

### 1. [[EgoScale]] (arXiv:2602.16710)
- **관계**: MobileEgo가 직접 인용하는 scaling-law/egocentric manipulation 선행 연구
- **차별점**: MobileEgo는 EgoScale보다 훨씬 긴 episode와 commodity smartphone 수집성을 강조

### 2. [[UMI]] (Universal Manipulation Interface) — RSS 2024
- **관계**: in-the-wild robot teaching을 낮은 장벽으로 만든 대표 연구
- **차별점**: MobileEgo는 UMI의 특수 gripper/마운트 부담보다 더 범용적인 smartphone sensor suite를 선택

### 3. [[Ego4D]] — CVPR 2022
- **관계**: 대규모 egocentric video의 대표 데이터셋
- **한계**: MobileEgo가 원하는 연속 6-DoF pose, RGB-D, long-horizon state tracking이 부족

### 4. [[EPIC-KITCHENS]] / EPIC-KITCHENS-100 — ECCV 2018 / IJCV 2022
- **관계**: 주방 egocentric action recognition의 핵심 데이터셋
- **차별점**: MobileEgo는 action recognition을 넘어 VLA pretraining용 trajectory/hand/action hierarchy를 제공

### 5. [[Ego-Exo4D]] — CVPR 2024
- **관계**: first-person/third-person paired skilled activity dataset
- **한계**: Project Aria 등 비범용 장비 의존성이 커서 [[mobileego-anywhere-2605-05945]]와 차별화됨

### 6. [[HOI4D]] — CVPR 2022
- **관계**: 4D human-object interaction dataset
- **연결**: [[mobileego-anywhere-2605-05945]]의 hand-object interaction annotation 필요성과 연결

### 7. [[HOT3D]] — CVPR 2025
- **관계**: 고정밀 hand/object tracking benchmark
- **연결**: [[mobileego-anywhere-2605-05945]]는 대규모 unconstrained recordings에서 ground-truth-free consistency metric으로 hand pose 품질 점검

### 8. [[ARCTIC]] — CVPR 2023
- **관계**: dexterous bimanual hand-object manipulation dataset
- **비교**: [[mobileego-anywhere-2605-05945]]의 MANO hand-pose 평가와 비교되는 controlled high-precision dataset

### 9. [[WiLoR]] — arXiv:2409.12259
- **관계**: [[mobileego-anywhere-2605-05945]]의 3D hand trajectory pipeline에서 hand pose estimation에 사용되는 핵심 방법

### 10. [[MCAP]] — mcap.dev
- **관계**: RGB-D/IMU/pose raw stream을 표준 로그 포맷으로 저장하기 위한 container
- **역할**: downstream VLA dataset conversion의 기반

## Connections
- [[mobileego-anywhere-2605-05945]] — 이 레퍼런스 페이지의 대상 논문
- [[VLA]] — 관련 데이터셋들이 pretraining에 사용되는 컨텍스트
- [[Ego4D]] — MobileEgo와 가장 직접적으로 비교되는 대규모 egocentric dataset
- [[EPIC-KITCHENS]] — egocentric action recognition의 대표 데이터셋
- [[HandTracking]] — WiLoR, ARCTIC, HOT3D 관련 개념
- [[DexterousManipulation]] — EgoScale, UMI, ARCTIC 관련 개념

## Contradictions
- 없음. 기존 [[mobileego-anywhere-2605-05945]] 소스 페이지와 일관됨.
