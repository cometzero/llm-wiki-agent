---
title: "Curse of Dimensionality"
type: concept
tags: [machine-learning, representation, optimization]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Definition
[[CurseOfDimensionality]]는 차원이 증가할수록 데이터 공간이 급격히 희소해져, 이웃 기반 추정, 거리 비교, 밀도 추정이 어렵고 일반화 성능이 악화되는 현상을 뜻한다.

## 주요 문제
- 데이터가 고차원에서 고르게 채워지지 않아 유사도/거리 기반 방법이 약해짐
- nearest neighbor, clustering, density estimation이 불안정
- 훈련 데이터에 과적합되기 쉬워짐
- 모델이 실제 분포보다 표본 노이즈에 민감

## 대응 전략
- [[DimensionalityReduction]]: 유효한 표현으로 축소
- [[RepresentationLearning]]: 의미 있는 잠재 표현 학습
- [[Regularization]]: 복잡도 제어로 과적합 완화

## Source Alignment
- Day03 source는 특히 embedding 차원을 무조건 키우는 접근의 한계를 경고하며, 데이터 수와 정규화/표현 학습이 동반되어야 함을 강조한다.

## Related Concepts
- [[Tensor]]
- [[TensorShape]]
- [[Regularization]]
- [[CurseOfDimensionality]]
- [[RepresentationLearning]]
- [[MachineLearning]]

## Possible Conflicts
- No explicit contradiction found with existing wiki pages.