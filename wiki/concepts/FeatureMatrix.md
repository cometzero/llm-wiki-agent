---
title: "Feature Matrix"
type: concept
tags: [data-representation, machine-learning]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Definition
[[FeatureMatrix]]는 샘플(sample)과 feature로 구성된 입력 데이터를 행렬 형태로 정리한 것이다.

## 구성
- 각 행(row): 하나의 샘플
- 각 열(column): 하나의 feature
- 따로 분리되는 타깃: label(목표값)

## 핵심 의미
- 정형 데이터의 기본 정렬 규칙을 제공한다.
- 딥러닝에서 단순 2D 표를 넘어 시퀀스·채널·배치의 [[Tensor]] 구조로 확장된다.
- [[TensorShape]] 해석은 연산 흐름 디버깅과 모델 구현에서 필수이다.

## Source Notes
- Source Day03은 학생 성적 예시로 행·열 의미를 설명하고, 실제로는 `(B, C, H, W)`나 `(B, T, D)` 같은 텐서 표현으로 일반화됨을 강조한다.

## Related Concepts
- [[Tensor]]
- [[TensorShape]]
- [[RepresentationLearning]]
- [[FeatureAnalysis]]
- [[MachineLearning]]

## Possible Conflicts
- No explicit contradiction found with existing wiki pages.