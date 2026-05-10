---
title: "MMD"
type: concept
tags:
  - DistributionShift
  - Statistics
  - RepresentationLearning
sources:
  - embodiedmidtrain-2604-20012-ko-analysis
last_updated: 2026-05-10
---

## 개념

[[MMD]](Maximum Mean Discrepancy)는 두 분포의 거리(kernel-based nonparametric distance)를 측정하는 지표로, 분포 차이가 있는 representation space에서 집합 간 정렬 정도를 비교할 때 쓰인다.

## EmbodiedMidtrain에서의 역할

- [[VLM]] 데이터군과 [[VLA]] 데이터군의 분포 간 거리를 정량화.
- VLA에 가까운 샘플과 먼 샘플이 혼재되는 구조를 보일 때 데이터 선별 근거로 활용.

## 주의

- MMD 자체는 여러 특성 선택/커널 설정에 민감하므로, proxy 신호로서 학습 파이프라인 전체와 함께 해석한다.

## 관련 항목

- [[DistributionShift]]
- [[BinaryClassification|BinaryClassification]]
- [[FeatureSpace]]
