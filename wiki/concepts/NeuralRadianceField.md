---
title: "Neural Radiance Field"
type: concept
tags: [3DReconstruction, NeRF, Autonomy, Vision]
last_updated: 2026-05-10
sources:
  - tesla-s-occupancy-networks-a-look-at-how-they-work
---

## Definition

[[NeuralRadianceField]](NeRF)는 다중 시점 이미지에서 장면의 3D 방사 특성을 재구성하는 기법군으로, 장면을 연속적 색/밀도 분포로 근사한다.

## Use in This Source

이 소스에서 [[Tesla]]는 점유 기반 3D 예측의 결과를 [[NeuralRadianceField]] 기반 재구성으로 대조해 정합성(사실관계 일관성)을 검사한다.

- [[NeRF]] 재구성은 장면 재생성 품질을 기준으로 점유 예측의 오차를 간접 점검
- [[FleetAverage|fleet averaging]] 및 디스크립터 기반 비교를 통해 시점 변화/비안정 영상에서 검증 견고성 강화

## Connection

- [[Simulation]] 기반 시뮬레이터 구축 및 오차 추적 파이프라인과 결합될 수 있음
- [[Tesla]]의 3D 지각 정밀도 향상에 보조 검증 신호로 활용
