---
title: "Failure/Recovery Trajectory"
type: concept
tags:
  - closed-loop
  - robustness
  - robotics
sources:
  - data-pyramid-for-embodied-manipulation-2607-24744
last_updated: 2026-07-29
---

## 정의

**Failure/Recovery Trajectory**는 정책이 실패 상태를 인식하고 복구 동작으로 전환하는 행동 시퀀스를 포함한 trajectory를 뜻한다.

## 왜 중요한가

[[VisionLanguageAction]] 정책이 성공 데모만 학습할 경우, 편차 발생 시 복구 전략이 없어 `closed-loop`에서 급격히 성능이 무너질 수 있다.

- 실행 중 예기치 못한 외란 감지
- 복구 전환(action re-plan)
- 정상 상태 복귀

## 역할

- [[ClosedLoopEvaluation]]에서 오차 누적을 줄인다.
- [[CrossEmbodimentLearning]]에서 embodiment 간 비선형 실패 패턴에 대한 일반화 강화.
- [[Simulation]]에서 counterfactual 생성 시나리오 구축의 핵심 데이터 단위.

## 연결

- [[RealRobotData]]
- [[WorldActionModel]]
- [[TactileSensing]]
- [[Failure Mode Analysis]]
