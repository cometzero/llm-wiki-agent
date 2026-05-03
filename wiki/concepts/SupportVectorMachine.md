---
title: "Support Vector Machine"
type: concept
tags:
  - classic-ml
  - svm
  - classification
  - margin
  - kernel-method
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[SupportVectorMachine]] (SVM)는 클래스를 분리하는 [[DecisionBoundary]]를 학습하는 지도학습 분류 모델이다. 핵심은 가능한 boundary 중 [[MaximumMargin]](최대 마진)를 최대화하는 것이다.

## Core Mechanism
- 선형 판별: \(w \cdot x + b = 0\) 형태의 경계에서 거리 최대화
- 경계 근처의 핵심 샘플은 SupportVector
- 마진이 클수록 작은 입력 변화에 덜 흔들리는 편을 기대
- 비선형 데이터는 KernelTrick으로 고차원에서 선형 분리를 유도

## Key Terms
- [[DecisionBoundary]]
- [[Hyperplane]]
- [[Margin]]
- SoftMargin
- KernelTrick
- [[Norm]]

## Notes for practice
- SVM은 "항상 직선"만 그리는 모델이 아니다.
- 마진이 크다고 항상 좋은 것은 아니며, 실제로는 소프트 마진/오류 허용이 필요할 수 있다.
- 텍스트/문서 임베딩의 분리도 해석에 직관적 기반을 준다.

## Relations
- Distance 기반 분류 직관은 [[KNN]]과 다르지만 거리/거리의 의미 공간을 공유한다.
- [[Classification]]의 기하학 해석으로, [[Generalization]] 이해에 유용하다.