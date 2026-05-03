---
title: "2026-05-03 AI/ML Learning Day 11"
type: source
tags:
  - diary
  - ai-ml-learning
  - classic-ml
  - svm
  - knn
  - decision-tree
source_file: raw/ai_ml_learning/2026-05-03-day11-ai-ml-learning-review.md
sources:
  - 2026-05-03-day11-ai-ml-learning-review
date: 2026-05-03
last_updated: 2026-05-03
---

## Summary
Day 11은 고전 ML의 세 가지 분류 모델을 복습한다: [[SupportVectorMachine]], [[KNN]], [[DecisionTree]]. 공통 목표는 “새 데이터에서 신뢰성 있게 분류 규칙을 세우는 것”이다.

Day 11은 먼저 [[Margin]]를 키워 일반화에 강한 경계를 선택하는 SVM 직관을 다루고, 다음으로 "가장 가까운 이웃"을 보는 [[KNN]]의 거리 기반 추론을 다룬다. 마지막으로 [[DecisionTree]]의 분할 규칙을 평가하는 지표로 [[InformationGain]], [[Entropy]], [[GiniImpurity]]를 이어서 설명한다.

실제 활용 연결로는 [[Embedding]] 공간의 분류, [[RAG]] 검색, 추천 시스템, 그리고 트리 기반 앙상블(RandomForest, GradientBoosting, XGBoost, LightGBM, CatBoost)까지 다뤄진다.

## Key Claims
- [[SupportVectorMachine]]은 분류 경계( decision boundary )를 여러 후보 중 [[MaximumMargin]]가 최대가 되도록 선택하고, 경계에 가장 영향력 큰 점은 SupportVector이다.
- [[KNN]]은 훈련 데이터를 저장해 두고, 새 샘플 주변의 Distance 기반 LocalNeighborhood을 찾아 다수결/가중합으로 예측한다. 즉, 학습은 거의 없고 예측 시 계산이 집중된다.
- K의 크기는 편향-분산을 바꾸는 핵심 하이퍼파라미터로, 작으면 노이즈에 민감하고 크면 지역 패턴을 잃는다.
- [[DecisionTree]]는 질문형 분기(node/branch)로 학습하며, 분기 선택은 [[InformationGain]]이 큰 규칙(불확실성 감소가 큰 split)을 우선한다.
- [[Entropy]]는 섞임/불확실성 측정이며, [[GiniImpurity]]는 동일 목적의 대체 지표다. 둘 다 순수한 노드(한 클래스 집중도)로 갈수록 작아진다.
- 깊은 트리는 훈련 데이터 노이즈를 과도하게 외우기 쉬워서 [[Overfitting]]이 생길 수 있으므로 MaxDepth, 최소 분할 조건, Pruning으로 통제가 필요하다.
- 이 세 모델은 [[Margin]], Distance 기반 유사도, 분할 기반 불확실성 감소라는 서로 다른 축으로도 “일반화”와 “규칙의 해석가능성”을 강조한다.

## Key Quotes
> "SVM은 가장 여유 있게 나누는 선" — 경계 주변 여백을 크게 만드는 아이디어

> "KNN은 가장 가까운 K개가 말해주는 말을 따른다" — 사례 기반 추론의 핵심

> "information gain은 어떤 질문을 던졌을 때 불확실성이 얼마나 줄었는지" — 분할 품질 기준의 본질

## Connections
- [[SupportVectorMachine]]: [[Margin]], SupportVector, KernelTrick, [[Hyperplane]], [[DecisionBoundary]]
- [[KNN]]: DistanceMetric, EuclideanDistance, [[CosineSimilarity]], FeatureScaling, LazyLearning, LocalNeighborhood
- [[DecisionTree]]: [[Entropy]], [[InformationGain]], [[GiniImpurity]], Pruning, [[Overfitting]], RootNode, [[LeafNode]]
- [[Classification]]: 세 모델 모두 클래스 판별 관점에서 연결됨
- [[Embedding]]: LLM/문서/이미지의 벡터공간에서 분류·검색·비유사도 측정 이해에 적용
- [[RAG]]: 질문 임베딩에서 유사 문서 탐색은 KNN 직관과 거리 기반 설계와 직접 연결
- RandomForest, GradientBoosting, XGBoost, LightGBM, CatBoost: [[DecisionTree]]를 앙상블로 확장한 트리 기반 기법
- [[Generalization]]: [[MaximumMargin]], 적절한 K, 적절한 분할 규칙이 과적합/노이즈 민감도를 조절

## Contradictions
- 기존 위키 내용과 정면 충돌하는 진술은 확인되지 않았다.

## Today's 3 Concepts

### 1) [[SupportVectorMachine]]과 [[MaximumMargin]]
- 분류 경계를 여러 후보에서 고를 때, 클래스 경계에서 가장 멀리 떨어진 경계(최대 마진 경계)를 고름
- 결정에 큰 영향을 주는 점은 SupportVector
- kernel trick으로 비선형 경계도 고차원 분리 아이디어로 처리

### 2) [[KNN]] 거리 기반 추론
- 최근접 이웃 K개를 찾아 이웃 라벨의 합의로 예측
- 회귀면 평균값, 분류면 다수결(또는 가중치 다수결)
- 거리 척도(유클리디안, 코사인)가 예측 성능을 좌우
- feature scale이 큰 값이 거리 지배 가능하므로 스케일링 필요

### 3) [[DecisionTree]]와 [[InformationGain]]
- 질문을 던지는 방식으로 데이터를 분할
- split 전후 불확실성 감소량이 큰 split을 우선
- 노드(questions), branch(조건 경로), leaf(최종 예측) 구조
- 깊이 과대화는 [[Overfitting]] 유발, pruning과 깊이/최소크기 제약 필요

## 복습 질문 3개

1. SVM에서 [[MaximumMargin]]을 크게 만들면 왜 새 데이터에 더 견고한가요?
2. [[KNN]]에서 K가 너무 작거나 너무 클 때 각각 생기는 문제가 무엇인가요?
3. [[DecisionTree]]에서 [[InformationGain]]이 크다는 것은 split 전후로 무엇이 많이 줄었다는 뜻인가요?

## 오늘의 한 줄 요약
SVM은 여유 있는 경계로 분리하고, [[KNN]]은 가까운 이웃을 따라가며, [[DecisionTree]]는 불확실성을 줄이는 질문을 찾아 분류한다.

## 복습 질문 정답

### 1. SVM에서 Margin을 크게 만들면 새 데이터에 더 강해질 수 있는 이유

Margin이 크면 decision boundary가 양 클래스에서 멀리 떨어져 있어 작은 측정 오차나 노이즈가 생겨도 분류가 바뀌기 어렵다. 즉, training point를 외우는 대신 여유 공간이 넓은 경계로 일반화 여지를 확보한다.

### 2. KNN에서 K를 너무 작거나 너무 크게 잡으면 생기는 문제

- 너무 작으면 이웃 하나/소수의 노이즈에 과민해져 분류가 흔들림
- 너무 크면 먼 점까지 포함해 local pattern이 희석되어 둔한 예측이 된다.

### 3. DecisionTree에서 Information Gain이 크다는 의미

split 전보다 split 후의 [[Entropy]](또는 불확실성) 감소량이 크다는 뜻이다. 즉, 노드 내 클래스 섞임이 크게 정리되어 예측이 쉬워진다.