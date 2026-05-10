---
title: "Data Selection"
type: concept
tags: [DataPreparation, RepresentationAlignment, DistributionShift, VLM, VLA]
last_updated: 2026-05-10
---

## Definition
[[DataSelection]]은 대규모 사전학습 모델을 특정 목표 도메인에 맞게 성능을 끌어올리는 과정에서, 대상 과업에 유리한 샘플을 선별해 사용하거나 가중치를 부여하는 전략이다.

## In VLM-to-VLA Context
- 단순 증분 학습량 증가보다 target-domain 정렬이 중요할 수 있다.
- [[EmbodiedMidtrain]]는 sample-level 선별을 통해 [[RobotManipulation]] 성능 개선을 보였다.
- 모델 수 자체보다 데이터의 분포 정렬이 성능 민감도에 더 직접적으로 작용하는 사례로 활용된다.

## Related
- [[ProximityEstimator]], [[DistributionShift]], [[MidTraining]], [[RepresentationAlignment]], [[VLA]], [[VLM]]