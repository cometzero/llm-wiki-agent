# 2026-04-23 AI/ML Learning Day 01

- Date: 2026-04-23
- Day: 01/30
- Level: beginner-intermediate
- Theme: 수학 표현과 확률 기초

## 학습 내용

### 오늘의 3가지 개념
1. 벡터공간과 좌표 표현
2. 행렬과 선형사상(linear map)
3. 내적(dot product), norm, 거리

### 핵심 요약

#### 1) 벡터공간과 좌표 표현
- 벡터공간(vector space)은 벡터의 덧셈과 스칼라배가 정의되는 공간이다.
- 좌표(coordinate)는 벡터 자체가 아니라, 선택한 기저(basis) 기준에서 벡터를 수치로 표현한 방식이다.
- 같은 벡터라도 basis가 바뀌면 coordinate는 달라질 수 있다.
- LLM의 token embedding, hidden state, gradient는 모두 벡터 표현으로 다룰 수 있다.

#### 2) 행렬과 선형사상(linear map)
- 행렬(matrix)은 단순한 숫자표가 아니라, 벡터를 다른 벡터로 보내는 선형사상(linear map)의 계산 표현이다.
- 선형사상은 덧셈과 스칼라배를 보존한다.
- rank는 변환이 실제로 보존하는 독립 정보의 차원 수를 뜻한다.
- dense layer, projection layer, attention의 Q/K/V projection은 모두 행렬 곱 관점으로 이해할 수 있다.

#### 3) 내적(dot product), norm, 거리
- dot product는 두 벡터의 방향성과 크기 결합을 측정한다.
- norm은 벡터의 크기를 나타내고, L1과 L2는 서로 다른 기하학적 성질을 갖는다.
- cosine similarity는 크기를 제거하고 방향 유사도에 집중한다.
- attention, embedding retrieval, regularization, gradient norm clipping에 모두 연결된다.

## 복습 질문
1. 같은 벡터라도 basis가 바뀌면 coordinate가 왜 달라질 수 있을까?
2. 행렬을 단순한 숫자표가 아니라 linear map으로 보면, rank는 무엇을 의미할까?
3. dot product, L2 norm, cosine similarity는 각각 무엇을 측정하며 attention이나 embedding search에서 어떻게 쓰일까?

## 복습 정답과 설명

### 1. 같은 벡터라도 basis가 바뀌면 coordinate가 왜 달라질 수 있을까?
**정답**
좌표(coordinate)는 벡터 자체가 아니라, 선택한 basis에 대해 그 벡터를 어떻게 분해해서 표현하느냐를 나타내는 값이기 때문이다.

**설명**
벡터는 공간 안의 대상이고, coordinate는 그 대상을 특정 기준축으로 읽어낸 숫자 표현이다. 따라서 basis가 바뀌면 같은 벡터라도 새로운 basis 조합으로 다시 써야 하므로 coordinate 값이 달라진다. 핵심은 벡터는 불변이고 coordinate는 basis-dependent라는 점이다. 이 관점이 있어야 basis change, PCA, representation learning을 자연스럽게 이해할 수 있다.

### 2. 행렬을 단순한 숫자표가 아니라 linear map으로 보면, rank는 무엇을 의미할까?
**정답**
rank는 그 linear map이 실제로 살려내는 독립적인 정보의 차원 수를 의미한다.

**설명**
행렬을 linear map으로 보면 입력 벡터를 다른 공간으로 보내는 변환으로 해석할 수 있다. 이때 rank는 출력이 실제로 펼쳐질 수 있는 공간의 차원, 즉 변환 뒤에도 유지되는 독립 방향의 수를 뜻한다. rank가 높으면 더 많은 정보를 보존하고, rank가 낮으면 어떤 방향의 정보는 눌리거나 사라진다. 따라서 rank는 이 변환이 얼마나 표현력을 유지하는지, 얼마나 압축을 일으키는지를 보여주는 양이다. LoRA, low-rank approximation, bottleneck 이해와 직접 연결된다.

### 3. dot product, L2 norm, cosine similarity는 각각 무엇을 측정하며 attention이나 embedding search에서 어떻게 쓰일까?
**정답**
- dot product: 두 벡터의 방향성과 크기가 결합된 관련도
- L2 norm: 벡터의 크기
- cosine similarity: 크기를 제거한 방향 유사도

**설명**
dot product는 방향과 크기를 함께 반영하므로 attention에서 query와 key의 관련도를 점수화할 때 쓰인다. L2 norm은 벡터의 길이를 나타내며 regularization, gradient norm clipping, 거리 계산의 기반이 된다. cosine similarity는 각 벡터를 norm으로 나눠 크기의 영향을 줄이고 방향만 비교하므로 embedding search, retrieval, semantic similarity에 자주 쓰인다. 즉 attention은 raw interaction score로 dot product를, retrieval은 의미 유사도 비교를 위해 cosine similarity를 자주 활용한다.

## 한 줄 정리
벡터공간은 표현의 대상, 행렬은 그 표현을 바꾸는 선형변환, dot product·norm·거리는 표현 사이의 관계를 수치화하는 도구다.
