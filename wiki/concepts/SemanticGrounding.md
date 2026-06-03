---
title: "Semantic Grounding"
type: concept
tags: [vla, grounding, reasoning, action]
sources: [robosemanticbench-2606-02277-ko, robosemanticbench-2606-02277-ko-analysis, robosemanticbench-2606-02277-learning]
last_updated: 2026-06-03
---

## 정의
Semantic Grounding은 [[VLA]](Vision-Language-Action) 모델에서 언어/시각 reasoning 결과가 실제 robot action(waypoint, trajectory, gripper action 등)으로 연결되는 과정이다.

## 핵심 문제
VLA 모델이 [[VQA]] 태스크에서 높은 성능을 달성해도, 그 semantic understanding이 action pathway에 제대로 전달되지 않으면 [[ShortcutBehavior]]를 보인다.

## 관련 메트릭
- **GSR (Gross Success Rate)**: 전체 grasp 성공률
- **TSR (Target Success Rate)**: semantic target 선택 성공률
- **nSG (normalized Semantic Grounding)**: random baseline 대비 semantic target 선택 성능 정규화

## 해석
- High GSR + Low TSR = Motor skill은 있으나 semantic action grounding 실패
- Benchmark는 이 두 차원을 분리해서 측정해야 motor vs semantic 병목을 정확히 진단할 수 있다.

## 관련 개념
- [[VLA]] — Semantic Grounding의 대상 모델
- [[ActionPrediction]] — grounding가 필요한 태스크
- [[ShortcutBehavior]] — grounding 실패로 인한 증상
- [[ClosedLoopControl]] — grounding가 적용되는 실행 환경
- [[CoT-VLA]] — reasoning 기반 grounding 시도

## 출처
- RoboSemanticBench (arXiv 2606.02277)
