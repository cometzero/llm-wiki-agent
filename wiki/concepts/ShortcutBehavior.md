---
title: "Shortcut Behavior"
type: concept
tags: [vla, failure-mode, grounding, robotics]
sources: [robosemanticbench-2606-02277-ko, robosemanticbench-2606-02277-learning]
last_updated: 2026-06-03
---

## 정의
Shortcut Behavior는 [[VLA]] 모델이 진짜 [[SemanticGrounding]] 없이 색/위치/분포 편향으로 성공하는 행동 패턴이다.

## 문제
모델이 VQA 태스크에서 올바른 semantic answer를 생성해도, 그 answer가 action pathway에 전달되지 않으면 실제 행동에서 shortcut을 따른다.

## 예시 (RoboSemanticBench)
- 색상/위치 힌트에 편향되어 올바른 semantic target을 무시
- 학습 데이터의 분포 패턴을 암기하여 표면적 성공

## 감지 방법
- GSR vs TSR 불일치: High GSR + Low TSR은 motor skill만 있고 semantic selection 실패
- Counterfactual test: 색상/위치 변경 시 성능 저하 확인
- Random baseline 대비 nSG 점수로 정규화

## 관련 개념
- [[SemanticGrounding]] — shortcut behavior를 진단하려는 대상
- [[VLA]] — shortcut을 보일 수 있는 모델
- [[BenchmarkMetrics]] — shortcut 감지 위한 평가 체계

## 출처
- RoboSemanticBench (arXiv 2606.02277)
