---
title: "Tesla's Shift to End-To-End Deep Learning: Full Breakdown"
type: source
tags: [Tesla, EndToEndAutonomy, EndToEndDeepLearning, OccupancyNetwork, HydraNet, MonteCarloTreeSearch, OccupancyGrid, FSD]
date: 2026-05-10
sources:
  - tesla-s-shift-to-end-to-end-deep-learning-full-breakdown
last_updated: 2026-05-10
source_file: raw/Robotics/LilysAI/tesla-s-shift-to-end-to-end-deep-learning-full-breakdown.md
source_hash: 1d89541f559e6e1c
---

## Summary
이 문서는 [[Tesla]] 자율주행이 모듈형 구조에서 단일 최적화 목표 기반의 [[EndToEndDeepLearning]]로 이동한 연혁을 정리한다. 핵심은 [[Perception|인지(Perception)]]와 [[Planning|계획(Planning)]]을 별도 블록으로 학습하던 방식에서, 하나의 [[Objective Function|단일 목표 함수]]로 동시에 조정하는 [[EndToEndAutonomy]]로 전환한 것이다.

2021년에는 [[HydraNet]] 기반 다중 작업 학습으로 객체/차선/도로요소 감지 체계를 구성했고, [[Planning|Planning]]은 신경망과 전통 알고리즘이 결합된 방식으로 동작했다. 2022년에는 [[OccupancyNetwork]]와 [[OccupancyFlow]]가 추가되어 3D 공간 점유 맵(= [[OccupancyGrid]])을 중심으로 인지 품질을 개선했으나, 여전히 [[Planning]] 단계에서 수동 규칙이 존재했다.

이후 FSD v12에서 [[Tesla]]는 [[Planning]]도 딥러닝으로 통합해 [[EndToEndDeepLearning]]으로 재구성한다. 이 과정에서 두 블록의 출력 품질뿐 아니라, 전체 시스템 성능을 함께 최적화할 수 있게 되며, 수동 규칙 기반의 휴리스틱 제어(예: 정지 신호 대기 시간/속도 패턴) 제거를 목표로 한다.

문서의 마지막에서는 종단간 학습의 핵심 차이를 비교하고, [[BlackBox|검은 상자]] 우려를 줄이기 위해 기존 모듈(예: [[OccupancyNetwork]], [[HydraNet]])의 시각화 가능성과 단계적 미세조정이 결합될 수 있음을 제시한다.

## Key Claims
- 2021년 [[Tesla]] 자율주행은 모듈형 구성에서 [[HydraNet]]가 [[Perception]]을 담당하고, 별도 [[Planning]]·제어 경로가 별개로 동작했다.
- [[HydraNet]]는 다중 작업 헤드 구조로, 객체/차선/신호 관련 인지 신호를 공유 인코더에서 처리해 효율적으로 계산한다.
- 2022년 [[Tesla]]는 [[OccupancyNetwork]]를 도입해 2D 객체 박스 중심 표현을 보완했고, 공간의 점유 상태를 [[Voxel]] 단위로 예측해 동적/복잡 장면 처리력을 높였다.
- 2022년 [[Planning]]은 [[MonteCarloTreeSearch]]와 신경망 점수를 결합해 후보 궤적을 생성·평가했으며, 비용 함수는 충돌 위험·승차감·개입 빈도·인간유사성 요소를 함께 고려했다.
- 2022년 기준, [[Tesla]]의 [[Planning]]에는 수동 규칙 기반 요소(예: 불법 횡단보도 대응, 정지 신호 대기 정책 등)가 포함되어 있었다.
- FSD v12 전환 시점에서 [[Tesla]]는 [[Perception]]과 [[Planning]]을 단일 신경망 학습 체계로 묶어 [[EndToEndDeepLearning]]으로 개선했고, 이때 두 블록은 서로의 목표를 공유하며 함께 개선된다.
- 완전한 [[EndToEndDeepLearning]]에서는 [[EndToEndAutonomy]] 최적화가 각 블록 독립 최적화가 아니라 전체 파이프라인의 연동 성능을 중심으로 수행된다.
- “비종단간 완전 딥러닝”은 각각의 모듈이 깊은 신경망으로 학습되더라도, 공동 손실 함수로 조정되지 않으면 전체 시스템 최적화에는 한계가 있다.
- [[OccupancyNetwork]]와 [[HydraNet]]는 FSD v12에서도 소거되지 않고, 시각화·진단 가능한 입력/중간출력 구성요소로 활용될 수 있다.
- 종단간 전환의 위험요인으로 지적된 [[BlackBox]] 성격은, 내부 모듈별 진단 지표를 유지하고 미세조정 단계에서 조기 분해가 가능하다는 점으로 완화할 수 있다.

## Key Quotes
> "종단간 학습은 복잡한 학습 시스템 전체에 경사 기반 학습을 적용하여 훈련하는 것을 의미한다. 종단간 학습 시스템은 모든 모듈이 미분 가능하도록 특별히 설계된다."  
> [tesla-s-shift-to-end-to-end-deep-learning-full-breakdown]

> "두 개의 딥러닝 블록이 있더라도 종단간 작업이 필요하다. 블록 자체가 아니라 훈련 및 최적화 방식이 다르면 결국 시스템 목표 정합이 깨진다."  
> [tesla-s-shift-to-end-to-end-deep-learning-full-breakdown]

> "테슬라는 FSD v12에서 Planning 시스템을 딥러닝으로 전환하고, Perception과 Planning 블록을 단일 목표 함수로 함께 학습시켜 최적화한다."  
> [tesla-s-shift-to-end-to-end-deep-learning-full-breakdown]

## Connections
- [[Tesla]] — 본 소스의 대상 시스템 주체.
- [[EndToEndAutonomy]] — 모듈형에서 통합형 제어로 이동한 아키텍처 방향.
- [[EndToEndDeepLearning]] — 본 문서의 핵심 전환 프레임.
- [[HydraNet]] — 2021 인지 기반 핵심 backbone.
- [[OccupancyNetwork]] — 2022 인지 품질 개선의 핵심 요소.
- [[OccupancyFlow]] — 점유 셀의 시공간적 이동 예측을 담당.
- [[OccupancyGrid]] — 3D 점유 표현의 기초 공간 구조.
- [[MonteCarloTreeSearch]] — 2022 [[Planning]]에서 후보 평가에 사용된 탐색 기법.
- [[EndToEnd]] — 시스템 통합 학습 관점의 설계 원리.
- [[Tesla Occupancy Networks: A look at How They Work|Tesla's Occupancy Networks: A look at How They Work]] — 기존 3D 점유 기반 전개와 본 소스의 연속성.
- [[Ashok Elluswamy: Building Foundational Models for Robotics at Tesla|Ashok Elluswamy: Building Foundational Models for Robotics at Tesla]] — 모듈식 손실을 피하는 종단간 기반 확장 논리와 정합.

## Contradictions
- 일부 기존 Tesla 관련 소스는 운영 단계별로 모듈 분리의 디버깅·안전성 장점을 강조한다. 본 소스는 장기적으로 동일한 수치적 목표 하에서 [[Planning]] 자체를 학습시키는 통합 접근이 더 본질적 최적화를 가능하게 한다고 본다. 이는 실무 운영 관점에서 "단계별 해석성"과 "통합 학습 정합성"의 우선순위가 다르다는 점에서 **방향성의 충돌**이 아닌 **적용 단계의 트레이드오프**로 정리한다.