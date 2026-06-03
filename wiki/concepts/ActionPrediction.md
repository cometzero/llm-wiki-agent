---
title: "Action Prediction"
type: concept
tags: [robotics, vla, imitation-learning, trajectory]
sources: [robosemanticbench-2606-02277-ko, robosemanticbench-2606-02277-learning, reflectdrive-2-2605-04647-analysis]
last_updated: 2026-06-03
---

## 정의
Action Prediction은 [[VLA]] 모델이 vision/language 입력을 받아 executable action(waypoint, trajectory, gripper command 등)으로 변환하는 태스크이다.

## 관련 태스크
- Action token prediction
- Trajectory prediction
- Imitation learning
- End-to-end policy learning

## Benchmark
- RoboSemanticBench: VLA의 action prediction에서 [[SemanticGrounding]] 병목 진단
- NAVSIM: 자율주행 trajectory planning evaluation

## 관련 모델
- [[OpenVLA]]
- [[GR00T]]
- [[Pi0]]
- [[CoT-VLA]]

## 관련 개념
- [[VLA]] — action prediction을 수행하는 모델 클래스
- [[SemanticGrounding]] — action prediction의 핵심 병목
- [[ClosedLoopControl]] — action prediction이 적용되는 실시간 환경
- [[BenchmarkMetrics]] — action prediction 평가 체계

## 출처
- RoboSemanticBench (arXiv 2606.02277)
- ReflectDrive-2 (arXiv 2605.04647)
