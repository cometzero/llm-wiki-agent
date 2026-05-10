---
title: "OccupancyNetwork"
type: entity
tags: [Tesla, AutonomousVehicle, OccupancyGrid, Perception]
sources:
  - tesla-s-shift-to-end-to-end-deep-learning-full-breakdown
last_updated: 2026-05-10
---

## Summary
[[OccupancyNetwork]]는 환경의 연속적 공간 점유 상태를 학습해 추정하는 자율주행 인지 구성요소로, 고정 크기 객체 박스보다 공간적 존재성 자체를 예측하는 데 강점을 둔다.

## Key Role
[[Tesla]]는 이를 통해 [[OccupancyGrid]]를 구성하고, 각 [[Voxel]]의 점유 정보를 기반으로 주변 동역학을 더 안정적으로 인지·추론하도록 했다.

## Characteristics
- [[Perception]] 입력을 2D 표현에만 의존하지 않고 공간-체적 관점으로 변환한다.
- 정지 물체뿐 아니라 움직이는 장면(예: [[OccupancyFlow]])과의 결합에 유리하다.
- 고정 레이블 ontology에 덜 의존해, 드문 형태의 객체나 비정형 장애물에 대한 회복력이 상대적으로 높다.

## Connections
- [[Tesla]]의 자율주행 스택에서 [[HydraNet]]와 함께 사용되어 객체 인식/차선 인식의 한계를 보완한다.
- [[AutonomousVehicle]]의 [[Planning]] 및 [[Control]] 안정성 향상에 기여한다.
- [[NeuralRadianceField|NeRF]] 기반 장면 정합 검증 파이프라인과 함께 사용되는 경우가 있다.
