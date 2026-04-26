# 2026-04-26 AI/ML Learning Day 04

- Date: 2026-04-26
- Day: 04/30
- Level: beginner-intermediate
- Theme: 미분과 최적화의 핵심

## 학습 내용

### 오늘의 3가지 개념
1. 미분과 변화율
2. 편미분과 그래디언트
3. 연쇄법칙과 계산 그래프

### 핵심 요약

#### 1) 미분과 변화율
- derivative는 입력이 아주 조금 변할 때 출력이 얼마나 변하는지를 나타내는 국소적 rate of change다.
- 한 점에서의 미분값은 접선의 기울기(slope)이자 출력 sensitivity를 요약한다.
- 핵심은 작은 변화에 대해 1차 근사(first-order approximation)를 만들 수 있다는 점이다.
- optimizer는 parameter를 조금 움직였을 때 loss가 줄어드는지 늘어나는지를 derivative로 판단한다.
- learning rate와 local linearization의 관계를 이해하는 출발점이다.

#### 2) 편미분과 그래디언트
- 여러 변수의 함수에서는 한 변수만 바꿔 본 변화율이 partial derivative다.
- gradient는 모든 편미분을 모은 벡터로, loss가 각 parameter에 얼마나 민감한지 한 번에 보여준다.
- gradient는 함수가 가장 빠르게 증가하는 방향을 가리키고, gradient descent는 보통 그 반대 방향으로 이동한다.
- directional derivative와 Jacobian은 gradient 개념을 더 넓은 함수 형태로 확장할 때 중요하다.
- 딥러닝의 weight update, exploding/vanishing gradient 해석과 직접 연결된다.

#### 3) 연쇄법칙과 계산 그래프
- chain rule은 합성함수의 미분이 각 단계의 local gradient를 따라 곱셈 형태로 전달된다는 규칙이다.
- computational graph는 복잡한 모델을 작은 연산 노드의 연결로 분해한 표현이다.
- forward pass는 값을 계산하고, backward pass는 gradient를 출력에서 입력 방향으로 전파한다.
- backpropagation은 계산 그래프 위에서 chain rule을 체계적으로 실행하는 알고리즘이다.
- large model 학습이 가능한 이유를 설명하는 핵심 구조다.

## 복습 질문
1. derivative와 rate of change는 어떤 관계이며, 왜 1차 근사가 최적화의 출발점이 될까?
2. gradient가 “가장 빠른 증가 방향”이라는 말은 directional derivative 식과 어떻게 연결될까?
3. backpropagation을 계산 그래프와 chain rule 관점에서 설명하면 어떤 단계들로 나뉠까?

## 복습 정답과 설명

### 1. derivative와 rate of change는 어떤 관계이며, 왜 1차 근사가 최적화의 출발점이 될까?
**정답**
- derivative는 함수의 한 점에서 측정한 국소적 rate of change다.
- 1차 근사는 derivative를 이용해 아주 가까운 구간에서 함수를 선형적으로 근사하는 방식이다.
- 최적화는 이 선형 근사를 이용해 어느 방향으로 움직이면 loss가 줄어드는지 결정한다.

**설명**
rate of change는 넓은 의미의 변화율이고, derivative는 그중에서도 무한히 작은 변화에 대한 순간 변화율이다. 평균 변화율이 두 점 사이의 전체 기울기라면 derivative는 한 점에서의 접선 기울기에 해당한다. 최적화에서 중요한 이유는 복잡한 loss function도 아주 작은 범위에서는 선형 함수처럼 근사할 수 있기 때문이다. 즉 local slope만 알면 현재 위치 근처에서 loss가 증가하는지 감소하는지를 판단할 수 있고, 이것이 gradient-based optimization의 출발점이 된다.

### 2. gradient가 “가장 빠른 증가 방향”이라는 말은 directional derivative 식과 어떻게 연결될까?
**정답**
- directional derivative는 특정 방향으로 움직일 때의 변화율이고, 식으로는 ∇f(x)^T v 로 쓴다.
- v가 단위벡터일 때 이 값이 가장 커지는 방향이 gradient ∇f(x) 방향이다.
- 따라서 gradient는 가장 빠른 증가 방향, -gradient는 가장 빠른 감소 방향이 된다.

**설명**
directional derivative 식은 gradient를 단순한 편미분 모음이 아니라 고차원 공간에서의 최적 방향 벡터로 이해하게 해준다. ∇f(x)^T v 는 dot product이므로 gradient 크기와 방향 정렬 정도를 함께 반영한다. v가 gradient와 같은 방향이면 변화율이 최대, 직교하면 거의 0, 반대 방향이면 감소 방향이 된다. 이 수학적 해석이 gradient descent의 update direction 의미를 정확히 설명한다.

### 3. backpropagation을 계산 그래프와 chain rule 관점에서 설명하면 어떤 단계들로 나뉠까?
**정답**
- 1) forward pass: 각 노드의 연산값을 계산한다.
- 2) loss 계산: 최종 출력으로부터 loss를 만든다.
- 3) backward 시작: 출력 쪽 gradient를 설정한다.
- 4) local gradient 계산: 각 노드가 자기 입력에 대한 미분값을 구한다.
- 5) chain rule 적용: upstream gradient와 local gradient를 곱해 이전 노드로 전달한다.
- 6) parameter gradient 축적: 각 weight, bias에 대한 gradient를 모은다.
- 7) optimizer update: 계산된 gradient로 parameter를 갱신한다.

**설명**
핵심은 큰 함수를 직접 미분하지 않고, 작은 연산들의 연결로 분해해서 미분한다는 것이다. 계산 그래프에서는 각 노드가 자기 local gradient만 정확히 알면 된다. backward pass에서는 위쪽에서 내려온 upstream gradient와 현재 노드의 local gradient를 곱해 gradient를 이전 단계로 전달한다. 이 과정을 반복하면 최종 loss가 모든 중간값과 parameter에 대해 어떻게 변하는지 계산된다. autograd는 이 과정을 자동화한 시스템이며, vanishing gradient나 exploding gradient 같은 문제도 결국 이 gradient flow의 품질 문제로 볼 수 있다.

## 한 줄 정리
미분은 변화율을 읽는 도구이고, gradient는 다변수 loss의 민감도 벡터이며, chain rule과 계산 그래프는 그 gradient를 실제 대규모 모델 학습에서 계산 가능하게 만드는 핵심 구조다.
