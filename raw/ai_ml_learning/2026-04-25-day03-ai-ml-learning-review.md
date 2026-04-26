# 2026-04-25 AI/ML Learning Day 03

- Date: 2026-04-25
- Day: 03/30
- Level: beginner-intermediate
- Theme: 수학 표현과 확률 기초

## 학습 내용

### 오늘의 3가지 개념
1. 함수 근사 관점의 머신러닝
2. 데이터 행렬과 feature representation
3. 고차원 공간과 차원의 저주

---

## 1) 함수 근사 관점의 머신러닝

### 한 줄 직관
머신러닝은 결국 **입력을 출력으로 바꾸는 좋은 함수를 찾는 문제**다.

### 쉬운 설명
예를 들어 집값 예측을 생각해보자.
입력으로는
- 평수
- 위치
- 연식
- 층수

같은 정보가 들어오고, 출력은 집값이다.

즉 우리는
`입력 → 출력`
으로 이어지는 규칙을 배우고 싶다. 이 규칙을 수학적으로 보면 하나의 함수다.

머신러닝은 이 함수를 사람이 직접 손으로 쓰는 대신, 데이터를 보고 자동으로 학습하는 과정이라고 볼 수 있다.

### 핵심 포인트
- 머신러닝은 function approximation(함수 근사) 문제로 볼 수 있다.
- hypothesis space는 모델이 선택할 수 있는 후보 함수들의 집합이다.
- loss function은 그 후보 함수가 얼마나 틀렸는지 재는 기준이다.
- 학습은 loss를 줄이는 방향으로 parameter를 조정하는 과정이다.

예를 들어
- 선형회귀
- decision tree
- neural network
- transformer

는 모두 서로 다른 hypothesis space를 가진 function approximator다.

### AI 연결
LLM도 본질적으로는 함수다.
- 이전 token들
- → 다음 token의 확률분포

를 출력하는 함수라고 볼 수 있다. 즉 next-token prediction도 함수 근사 문제의 한 종류다.

---

## 2) 데이터 행렬과 feature representation

### 한 줄 직관
데이터를 모델이 읽기 쉽게 정리한 표가 feature matrix이고, 더 잘 학습되도록 바꾼 표현이 representation이다.

### 쉬운 설명
학생 데이터가 있다고 해보자.

| 학생 | 공부시간 | 결석수 | 과제제출률 | 시험점수 |
|---|---:|---:|---:|---:|
| A | 10 | 0 | 100 | 95 |
| B | 4 | 3 | 60 | 65 |

여기서
- 한 행(row) = sample 하나
- 한 열(column) = feature 하나
- 시험점수 = label 또는 예측 대상

처럼 볼 수 있다.

이런 식으로 데이터를 행렬로 정리하면 모델이 계산하기 쉬워진다.

### 핵심 포인트
- sample: 데이터 1개
- feature: 그 데이터를 설명하는 입력 변수 또는 표현 차원
- label: 모델이 맞혀야 하는 정답
- feature matrix: sample과 feature를 정리한 입력 표
- representation: 원시 데이터를 학습하기 좋은 형태로 바꾼 표현

딥러닝에서는 단순 표를 넘어 tensor shape가 중요하다.
예를 들어:
- 이미지: `(B, C, H, W)`
- 토큰 embedding: `(B, T, D)`

shape를 제대로 읽어야 연산이 왜 그렇게 되는지 이해할 수 있다.

### AI 연결
Transformer에서 입력 token은 처음부터 완벽한 feature가 아니다. embedding, attention, MLP를 거치며 점점 더 유용한 representation으로 변한다. 즉 딥러닝은 좋은 함수를 학습할 뿐 아니라, **좋은 표현(representation)** 도 함께 학습한다.

---

## 3) 고차원 공간과 차원의 저주

### 한 줄 직관
차원이 커질수록 공간은 너무 넓어지고 데이터는 너무 성기게 퍼져서, 학습이 생각보다 훨씬 어려워진다.

### 쉬운 설명
1차원에서는 점 몇 개만 있어도 대충 구조를 볼 수 있다.
2차원도 평면에 찍어보면 감이 온다.
그런데 100차원, 1000차원이 되면 어떨까?

공간은 엄청 커지는데 데이터 수는 그만큼 빨리 늘지 못한다. 그래서 데이터는 고차원 공간에 듬성듬성 흩어지게 된다. 이것을 sparsity라고 부른다.

이렇게 되면
- 가까운 이웃 찾기 어려움
- 거리 비교가 덜 믿을 만해짐
- 데이터가 부족해 보이기 쉬움
- 모델이 훈련 데이터만 외우기 쉬움

같은 문제가 생긴다.

### 핵심 포인트
- high-dimensional space에서는 데이터가 sparse하게 퍼진다.
- 차원이 커질수록 “가깝다”는 개념 자체가 약해질 수 있다.
- nearest neighbor, clustering, density estimation이 어려워진다.
- overfitting 위험이 커진다.
- 그래서 dimensionality reduction, regularization, representation learning이 중요하다.

### AI 연결
embedding dimension을 무조건 키운다고 항상 좋은 것은 아니다. 차원이 커지면 표현력은 늘 수 있지만, 데이터 수와 regularization이 받쳐주지 않으면 오히려 일반화가 나빠질 수 있다. 그래서 PCA, autoencoder, 좋은 embedding 학습, norm 제어 같은 아이디어가 계속 중요하게 등장한다.

---

## 복습 질문
1. 머신러닝을 function approximation으로 볼 때 hypothesis space와 loss function은 각각 어떤 역할을 할까?
2. feature matrix에서 sample, feature, label은 어떻게 구분되며 tensor shape를 읽는 능력이 왜 중요한가?
3. high-dimensional space에서 sparsity가 커지면 거리 기반 방법과 일반화에 어떤 문제가 생길까?

## 복습 정답과 설명

### 1. 머신러닝을 function approximation으로 볼 때 hypothesis space와 loss function은 각각 어떤 역할을 할까?
**정답**
- hypothesis space: 모델이 선택할 수 있는 후보 함수들의 집합
- loss function: 그 후보 함수가 얼마나 틀렸는지 측정하는 기준

**설명**
머신러닝은 좋은 함수를 찾는 문제다. hypothesis space는 “어떤 종류의 함수를 허용할 것인가”를 정한다. loss function은 “그 함수가 얼마나 잘 맞는가”를 평가한다. 즉 hypothesis space는 탐색 범위이고, loss function은 평가 기준이다.

### 2. feature matrix에서 sample, feature, label은 어떻게 구분되며 tensor shape를 읽는 능력이 왜 중요한가?
**정답**
- sample: 데이터 1개
- feature: 그 데이터를 설명하는 입력 변수 또는 표현 차원
- label: 모델이 맞혀야 하는 정답
- tensor shape 이해는 데이터 구조와 연산 흐름을 읽는 데 필수다.

**설명**
기본 표 형태 데이터에서는 행이 sample, 열이 feature다. label은 별도로 예측 대상이다. 딥러닝에서는 입력이 표가 아니라 tensor이므로 `(B, T, D)` 같은 shape를 정확히 읽어야 attention, matmul, broadcasting이 왜 그렇게 동작하는지 이해할 수 있다. 실제 디버깅에서도 shape mismatch는 가장 흔한 문제다.

### 3. high-dimensional space에서 sparsity가 커지면 거리 기반 방법과 일반화에 어떤 문제가 생길까?
**정답**
데이터가 성기게 퍼지면 거리의 구별력이 약해지고, nearest neighbor 같은 거리 기반 방법이 불안정해지며, 충분한 데이터를 확보하기 어려워 overfitting과 일반화 저하가 쉽게 발생한다.

**설명**
차원이 커질수록 공간은 급격히 넓어진다. 하지만 데이터는 그만큼 촘촘하게 채워지지 못한다. 그래서 가까운 점과 먼 점의 차이가 줄어들고, 거리 기반 추론이 덜 믿을 만해진다. 동시에 표본 부족 문제가 심해져 모델이 훈련 데이터만 외우기 쉬워진다. 그래서 regularization, dimensionality reduction, representation learning이 중요하다.

## 한 줄 정리
머신러닝은 좋은 함수를 학습하는 문제이고, 그 함수는 적절한 representation 위에서 동작하며, 고차원 공간에서는 차원의 저주를 줄이기 위한 구조적 표현과 regularization이 매우 중요하다.
