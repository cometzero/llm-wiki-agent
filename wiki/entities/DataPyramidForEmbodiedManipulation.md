---
title: "Data Pyramid for Embodied Manipulation"
type: entity
tags:
  - robotics
  - embodied-manipulation
  - data-recipe
  - vla
sources:
  - data-pyramid-for-embodied-manipulation-2607-24744
last_updated: 2026-07-29
---

## 개요

**Data Pyramid for Embodied Manipulation**은 [[VisionLanguageAction]] 학습에서 데이터 혼합을 5개 레이어로 정렬하는 실무 프레임이다.
상위로 갈수록 로봇 실행 정렬 신호는 약해지고, 표현 다양성은 커진다.

## 핵심 계층

1. [[RealRobotData]] — 실행성능 정렬 신호가 가장 강함
2. [[UMI]] — object/end-effector 중심 수집으로 비용 대비 실행 전이성 개선
3. [[EgocentricVideo]]/[[ExocentricVideo]] — 인간 상호작용 prior 강화
4. [[Simulation]] — 폐루프/대량 데이터 생성, counterfactual 보강
5. [[VisionLanguageModel]]/일반 멀티모달 — semantic breadth 제공

## 주장

- VLA 파이프라인에서 실사용 성능은 `web-scale`보다 실행 정렬이 더 중요하다.
- [[CrossEmbodimentAlignment]]는 저비용 수집축(UMI)과 실실행축(real-robot) 사이의 교량을 얼마나 잘 만드는지가 핵심이다.
- 실패 대응을 위한 [[FailureRecoveryTrajectory]]가 없으면 안정성을 과대평가하기 쉽다.

## 연결

- [[Xiaomi-Robotics-1]] — 데이터 확장 전략의 대표 실무 사례
- [[WorldActionModel]] — 예측/회복 설계 축
- [[VisionLanguageAction]] — semantic→execution 전이의 최종 작업축
- [[VisionLanguageModel]] — 고밀도 의미론 prior
- [[Sim-to-Real Transfer]] — 시뮬레이션에서 실제로 넘어가는 지점
