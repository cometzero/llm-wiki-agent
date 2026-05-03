---
title: "KNN"
type: concept
tags:
  - nearest-neighbor
  - instance-based-learning
  - distance-metric
  - retrieval
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[KNN]](K-Nearest Neighbors)은 새 샘플의 라벨을 예측할 때, 훈련 데이터에서 가장 가까운 K개의 이웃을 찾아 라벨을 종합하는 지도학습 분류/회귀 방법이다.

## Core Mechanism
- 학습 단계에서 복잡한 파라미터 최적화가 거의 없음
- 예측 시점에 거리 계산이 핵심
- 보통은 분류에서 다수결, 회귀에서 평균

## Key Terms
- DistanceMetric
- EuclideanDistance
- [[CosineSimilarity]]
- LocalNeighborhood
- FeatureScaling
- LazyLearning

## Trade-offs
- K가 작을수록 노이즈에 민감
- K가 클수록 지역 패턴이 희석
- 거리 척도(예: 코사인 vs 유클리디안)와 스케일링이 성능을 좌우

## Practical Links
- [[RAG]] 검색에서 임베딩 유사 문서 탐색은 KNN 직관에 매우 가깝다.
- 추천 시스템의 유사 사용자/아이템 접근법과 닮은 구조
- [[Embedding]], [[CurseOfDimensionality]]를 함께 이해하면 고차원에서의 성능 한계를 설명하기 쉽다.