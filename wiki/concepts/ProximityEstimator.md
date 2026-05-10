---
title: "Proximity Estimator"
type: concept
tags:
  - DataSelection
  - RepresentationAlignment
  - MidTraining
  - Robotics
  - VLM
  - VLA
sources:
  - embodiedmidtrain-2604-20012-study-guide
last_updated: 2026-05-10
---

## Definition
[[ProximityEstimator]]는 특정 샘플이 [[VLA]] 목표 분포에 얼마나 가까운지 예측하는 점수 함수로, 보통 frozen [[VLM]] 표현공간에서 학습된 분류기 출력으로 구현한다.

## Typical Formulation
- 양성 클래스: [[VLA]] 타깃 데이터
- 음성 클래스: 일반 [[VLM]] 후보 샘플
- 모델: 경량 [[BinaryClassification|이진 분류기]]
- 출력: sigmoid score `s(x)`를 proximity score로 사용

## Role in EmbodiedMidtrain
- sample-level로 상위 점수 샘플만 고르면, 선택된 코퍼리로 [[MidTraining]] 시점의 초기화 품질이 올라간다.
- [[MMD]]/[[t-SNE]]로 분포가 맞아들어가는 방향성도 함께 확인하는 패턴이 일반적이다.

## Why It Helps
- 데이터 전체를 쓰는 방식보다 **VLA 정합 샘플의 밀도를 높인다**.
- random/거리 기반/퍼플렉시티 기반 baseline 대비 downstream behavior 성능에서 안정적 우위가 보고되었다.

## Relations
- [[EmbodiedMidtrain]]
- [[DataSelection]]
- [[RepresentationAlignment]]
- [[DistributionShift]]
- [[VLM]]
- [[VLA]]
