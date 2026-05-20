---
title: "MobileEgo Anywhere: 범용 하드웨어 기반 장기 egocentric 데이터 수집 오픈 인프라"
type: source
tags: [VLA, egocentric-data, robotics, dataset, mobile-sensing]
date: 2026-05-20
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W21/mobileego-anywhere-2605-05945/paper-ko.md
source_hash: d57be74bf508c7a3
---

## Summary
MobileEgo Anywhere는 commodity smartphone(LiDAR 탑재 iPhone Pro)를 활용한 장기 egocentric 데이터 수집 오픈 인프라를 제안한다. 기존 egocentric dataset이 수 분 수준의 짧은 episode에 제한되는 문제를 해결하기 위해 200시간规模的 장기 데이터셋을 공개하며, STERA라는 이름의 처리 파이프라인과 mobile app도 함께 제공한다. VLA(Vision-Language-Action) 모델 학습에 필요한 long-horizon temporal dependency와 hierarchical action instruction을 포함한다.

## Key Claims
- **200시간 dataset**: 16명의 contributor가 수행한 354개 session, 평균 21.2분, 최장 108분
- **Commodity hardware**: LiDAR 탑재 iPhone Pro + head-worn rig만으로 데이터 수집 가능
- **STERA 인프라**: raw mobile capture를 VLA 학습용 표준 포맷(MCAP → 3D hand trajectory, atomic action labels, hierarchical instruction tree)으로 변환하는 Python processing suite
- **ARKit pose drift**: trajectory 길이 대비 0.1% 미만으로 long-horizon tracking 안정성 확보
- **Hand pose 품질**: WiLoR 기반 21-joint MANO hand pose, bone length CV median 1.27%~1.43%

## Key Quotes
> "VLA pretraining에는 long-horizon human interaction trajectory가 필요한데, 기존 egocentric dataset은 episode가 너무 짧고 state consistency가 끊긴다" — 문제의식

> "MobileEgo Anywhere가 VLA dataset creation을 democratize하고, 더 나은 future VLA model로 가는 path를 제공하기를 기대한다" — Conclusion

## Hierarchical Data Structure
| Level | Median Duration | Description |
|-------|-----------------|-------------|
| Atomic spans | 5s | 짧은 조작 단위(labeling) |
| Episodes | 42s | 하나의 목표 단위 |
| Sub-goals | 3.9 min | 의미론적 그룹 |
| Sessions | 15.5 min | 전체 활동 |

4단계 간 temporal separation: 인접 레벨 간 4~8배 분리 유지

## Connections
- [[HumanNet]] — 동일 주제(egocentric video dataset)의 related work, [[Ego4D]]/[[EPIC-KITCHENS]] 참고
- [[VLA]] — 주요 타겟下游 task
- [[Ego4D]] — 기존 egocentric dataset 관련, action recognition 중심
- [[EPIC-KITCHENS]] — 기존 egocentric dataset 관련
- [[UMI]] — robot teaching hardware barrier 감소 관련 비교
- [[WiLoR]] — hand estimation에 사용된 모델
- [[ARKit]] — iOS의 VIO(Visual-Inertial Odometry) 기반 6-DoF pose tracking
- [[ARCore]] — Android counterpart
- [[NVIDIAGR00T]] — [[VLA]] 관련 최신 로보틱스 foundation model
- [[PhysicalIntelligencePi]] — [[VLA]] 관련 로보틱스 연구기관
- [[GeminiRobotics]] — [[VLA]] 관련 로보틱스 연구기관

## Contradictions
- 없음. 기존 wiki 내 [[Ego4D]], [[EPIC-KITCHENS]], [[HumanNet]]과 complementary한 관계로, 이들 dataset의 limitation(짧은 episode)을 직접적으로 해결하는 새로운 접근
