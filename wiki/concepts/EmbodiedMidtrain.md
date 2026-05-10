---
title: "EmbodiedMidtrain"
type: concept
tags:
  - Robotics
  - VLM
  - VLA
  - MidTraining
  - DataSelection
  - RepresentationAlignment
sources:
  - embodiedmidtrain-2604-20012-study-guide
last_updated: 2026-05-10
---

## Definition
[[EmbodiedMidtrain]]는 [[VLM]]에서 바로 [[VLA]]로 파인튜닝하는 대신, VLA에 가까운 샘플을 선별해 추가 학습([[MidTraining]])을 수행해 백본의 출발점을 정렬하는 학습 전략이다.

## Mechanism
- 1) 후보 [[VLM]] 데이터와 목표 [[VLA]] 코퍼리를 준비한다.
- 2) frozen된 [[VLM]]에서 특징(feature)을 추출한다.
- 3) [[BinaryClassification|이진 분류]]로 VLA-like vs non-VLA-like 멤버십 라벨을 학습해 score를 얻는다.
- 4) top-K 샘플을 뽑아 [[MidTraining]] 코퍼리로 재학습한다.
- 5) mid-trained backbone으로 downstream [[RobotManipulation]] 파인튜닝을 수행한다.

## Key Insight
- 핵심은 모델 크기 확장보다 **데이터 정렬 품질**이다.
- 분포 간 차이([[DistributionShift]])가 큰 상황에서는 sample-level 선택이 random/데이터량 확장보다 효율적이다.

## Evidence
- [[MMD]]와 [[t-SNE]]로 VLM/VLA 분포가 분리됨을 점검.
- [[Calvin]], [[SimplerEnv]], [[LIBERO]]에서 [[InternVL3.5|InternVL3.5-1B]], [[Qwen3VL|Qwen3VL-2B]] 성능 향상으로 실증.

## Links
- [[ProximityEstimator]]
- [[MidTraining]]
- [[DataSelection]]
- [[VLM]]
- [[VLA]]
- [[RobotManipulation]]
- [[DistributionShift]]

## Notes
- 기존 [[OpenVLA]], [[GR00T]], [[Pi0]]류와 비교해 아키텍처 변경 없이도 적용 가능한 데이터 중심 적응 경로로 볼 수 있다.
