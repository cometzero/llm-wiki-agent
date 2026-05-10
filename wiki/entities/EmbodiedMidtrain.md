---
title: "EmbodiedMidtrain"
type: entity
tags: [EmbodiedAI, VLM, VLA, MidTraining, DataSelection]
sources:
  - embodiedmidtrain-2604-20012-references
last_updated: 2026-05-10
---

## Description
[[EmbodiedMidtrain]]는 로봇 조작 과업에서 바로 적용 가능한 거대한 모델 확장보다, VLM 내부의 [[DistributionShift]]와 목표 도메인 정합을 기반으로 한 데이터 선택이 더 큰 성능 이득을 낼 수 있음을 보인 파이프라인/연구 축이다.

## Core Idea
- VLM backbone의 전체 크기보다, VLA 적합 sample을 선별하는 [[DataSelection]]이 성능을 좌우한다.
- [[ProximityEstimator]]를 통해 VLM feature 위에서 target-aligned scoring을 만들고 top-K 샘플로 [[MidTraining]]을 수행한다.
- 결과적으로 같은 backbone라도 downstream [[RobotManipulation]] 성능이 달라질 수 있다.

## Connections
- [[VLM]], [[VLA]], [[MidTraining]], [[RepresentationAlignment]], [[DataSelection]], [[ProximityEstimator]], [[RobotManipulation]], [[MMD]], [[VLM4VLA]], [[InternVL3.5]], [[Qwen3VL]]

## Notes
이 엔티티는 [[OpenVLA]], [[Pi0]], [[GR00T]] 같은 VLA 계열 대비 데이터 정렬 기반 성능 개선 루트를 제시한다.