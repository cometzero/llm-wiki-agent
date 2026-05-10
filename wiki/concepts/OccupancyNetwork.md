---
title: "Occupancy Network"
type: concept
tags: [AutonomousVehicle, Perception, SpatialRepresentation]
last_updated: 2026-05-10
sources:
  - tesla-s-occupancy-networks-a-look-at-how-they-work
---

## Definition

[[OccupancyNetwork]]는 3차원 공간을 정규 그리드(대개 [[Voxel]] 단위)로 나누고, 각 셀의 점유 상태(비어 있음/점유됨)를 추정하는 모델/표현 체계다.

## Core Idea

- 기존의 객체 분류 기반 [[ObjectDetection]] 중심 파이프라인과 달리, 객체 종류보다는 공간이 실제로 점유되어 있는지 여부를 예측한다.
- 결과는 [[OccupancyVolume]] 형태로 누적되어, 차량이 통행 가능한 공간과 잠재적 장애물을 연속적으로 인식하도록 돕는다.

## In This Source

이 소스는 [[Tesla]] 자율주행에서 [[OccupancyNetwork]]가 fixed-box detection의 한계를 보완하는 핵심 장치로 제시되었다.

- [[2D]] 객체 박스의 기하학적 제약 완화
- 데이터셋 외 객체(ontology gap)에도 반응성 향상
- 복합/비정형 장애물(돌출부 등)에 대한 점유 표현 향상

## Related Concepts

- [[OccupancyGrid]]
- [[OccupancyFlow]]
- [[NeuralRadianceField]]
- [[EndToEndAutonomy]]

## Practical Effects

- 경로 계획과 충돌 회피 판단의 안정성 개선
- 가려진 영역(occlusion) 근사와 장기 예측 루틴의 보완
