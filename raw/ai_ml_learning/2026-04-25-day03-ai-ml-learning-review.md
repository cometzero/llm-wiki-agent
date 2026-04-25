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

### 핵심 요약

#### 1) 함수 근사 관점의 머신러닝
- 머신러닝은 입력을 출력으로 대응시키는 함수를 학습하는 문제로 볼 수 있다.
- hypothesis space는 모델이 탐색할 수 있는 함수들의 집합이다.
- loss function은 후보 함수가 얼마나 틀렸는지를 재는 기준이다.
- classification, regression, sequence modeling, next-token prediction을 하나의 틀로 묶어준다.

#### 2) 데이터 행렬과 feature representation
- feature matrix에서는 row가 sample, column이 feature를 뜻한다.
- label은 맞혀야 하는 정답이며 입력과 구분된다.
- 딥러닝에서는 행렬을 넘어 tensor와 tensor shape 이해가 중요하다.
- representation은 원시 데이터를 모델이 학습하기 쉬운 좌표계로 바꾸는 관점과 연결된다.

#### 3) 고차원 공간과 차원의 저주
- 현대 ML 데이터는 대부분 high-dimensional space에 놓여 있다.
- 차원이 커질수록 데이터는 sparse하게 퍼지고 거리 개념이 약해진다.
- nearest neighbor, density estimation, nonparametric method가 어려워진다.
- representation learning, regularization, dimensionality reduction이 중요해진다.

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
머신러닝은 결국 입력 x를 출력 y로 보내는 함수 f를 찾는 문제다. hypothesis space는 어떤 종류의 함수를 허용할지를 정한다. 선형모델, decision tree, neural network, transformer는 각각 다른 hypothesis space를 이룬다. loss function은 그 공간 안에서 어떤 함수가 더 좋은지 판별하는 기준이다. 회귀에서는 MSE, 분류에서는 cross-entropy 같은 식이다. 요약하면 hypothesis space는 어디를 탐색할지, loss function은 그 안에서 무엇을 최소화할지를 정한다.

### 2. feature matrix에서 sample, feature, label은 어떻게 구분되며 tensor shape를 읽는 능력이 왜 중요한가?
**정답**
- sample: 데이터 1개
- feature: 그 데이터를 설명하는 입력 변수 또는 표현 차원
- label: 모델이 맞혀야 하는 정답
- tensor shape를 읽는 능력은 데이터 구조와 연산 흐름을 이해하고 디버깅하는 데 필수다.

**설명**
기본 tabular setting에서 X ∈ R^{n×d}일 때 n은 sample 수, d는 feature 수다. sample은 개별 데이터 포인트이고, feature는 각 데이터를 설명하는 입력 축이다. label은 분류의 class index나 회귀의 연속값처럼 정답 역할을 한다. 딥러닝에서는 이미지가 (B, C, H, W), 토큰 embedding이 (B, T, D)처럼 tensor로 표현되므로 shape를 이해해야 matrix multiplication, broadcasting, attention score 계산이 왜 그렇게 동작하는지 파악할 수 있다. 실제 모델 디버깅에서도 shape mismatch는 가장 흔한 문제 중 하나다.

### 3. high-dimensional space에서 sparsity가 커지면 거리 기반 방법과 일반화에 어떤 문제가 생길까?
**정답**
데이터가 고차원 공간에 성기게 퍼지면 거리의 구별력이 약해지고, nearest neighbor 같은 거리 기반 방법이 불안정해지며, 충분한 데이터를 확보하기 어려워 overfitting과 일반화 저하가 쉽게 발생한다.

**설명**
차원이 커질수록 공간의 부피는 급격히 커지지만 데이터 수는 그렇게 빨리 늘지 못하므로, 데이터는 매우 sparse하게 분포한다. 이때 가까운 점과 먼 점의 차이가 줄어들어 거리의 의미가 약해지고, nearest neighbor, clustering, density estimation이 불안정해진다. 동시에 충분히 촘촘한 표본을 확보하기 어려워 모델이 훈련 데이터를 외우는 방향으로 가기 쉬워져 overfitting 위험이 커진다. 그래서 representation learning, regularization, dimensionality reduction이 중요한 대응 전략이 된다.

## 한 줄 정리
머신러닝은 좋은 함수를 학습하는 문제이고, 그 함수는 적절한 representation 위에서 동작하며, 고차원 공간에서는 차원의 저주를 피하기 위한 구조적 표현과 regularization이 매우 중요하다.
