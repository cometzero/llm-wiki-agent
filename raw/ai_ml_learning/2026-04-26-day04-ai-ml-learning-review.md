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

---

## 1) 미분과 변화율

### 한 줄 직관
미분은 **입력을 아주 조금 바꿨을 때 출력이 얼마나 변하는지**를 알려주는 도구다.

### 쉬운 설명
자동차 속도계를 떠올리면 쉽다. 속도는 “시간이 조금 지났을 때 위치가 얼마나 변하는가”를 보는 값이다. 미분도 비슷하다. 함수에서 입력을 아주 조금 움직였을 때 출력이 얼마나 변하는지 보는 것이다.

예를 들어 `y = x^2`를 생각해보자.
- x가 1에서 2로 가면 y는 1에서 4로 변한다.
- x가 2에서 3으로 가면 y는 4에서 9로 변한다.

즉 같은 1만큼 움직여도 출력 변화량은 점점 커진다. 미분은 이런 **순간적인 변화율**을 한 점에서 읽어내는 도구다.

### 핵심 포인트
- derivative는 local rate of change다.
- 한 점에서의 미분값은 접선의 기울기라고 볼 수 있다.
- 부호는 증가/감소 방향을 알려준다.
- 절댓값 크기는 얼마나 가파른지 알려준다.
- 최적화는 이 변화율 정보를 이용해 loss를 줄이는 방향을 찾는다.

### AI 연결
모델을 학습할 때는 “파라미터를 조금 바꾸면 loss가 줄어드나, 늘어나나?”를 알아야 한다. 이때 가장 기본이 되는 정보가 derivative다. learning rate를 너무 크게 잡으면 이 local slope 정보만 믿고 크게 움직이다가 오히려 튈 수 있고, 너무 작게 잡으면 학습이 느려진다.

---

## 2) 편미분과 그래디언트

### 한 줄 직관
변수가 여러 개일 때는 **각 방향으로 따로 본 변화율**이 편미분이고, 그것들을 한데 모은 벡터가 gradient다.

### 쉬운 설명
함수가 `f(x, y)`처럼 두 변수에 의해 결정된다고 해보자. 그러면
- x만 조금 바꿨을 때 출력이 얼마나 변하는가?
- y만 조금 바꿨을 때 출력이 얼마나 변하는가?

를 각각 볼 수 있다. 이것이 편미분(partial derivative)이다.

그리고
- x 방향 변화율
- y 방향 변화율
- z 방향 변화율
- ...

을 한 번에 모아 놓은 것이 gradient다.

즉 gradient는 “이 함수가 각 방향으로 얼마나 민감한지”를 한 벡터에 담아 놓은 것이다.

### 핵심 포인트
- partial derivative는 여러 변수 중 하나만 움직였을 때의 변화율이다.
- gradient는 모든 편미분을 모은 벡터다.
- gradient는 함수가 가장 빠르게 증가하는 방향을 가리킨다.
- gradient descent는 보통 그 반대 방향으로 이동한다.
- 딥러닝에서는 모든 weight, bias에 대해 gradient를 계산한다.

### 아주 쉬운 예시
산을 생각해보자.
지금 내가 서 있는 위치에서
- 동쪽으로 한 걸음 갔을 때 얼마나 올라가는지
- 북쪽으로 한 걸음 갔을 때 얼마나 올라가는지

를 따로 측정할 수 있다. 이것이 편미분이다.

이 정보를 모두 합치면 “어느 방향으로 가면 가장 가파르게 올라가는지” 알 수 있는데, 그것이 gradient다. 반대로 가장 빨리 내려가고 싶다면 gradient 반대 방향으로 가면 된다.

### AI 연결
신경망 학습은 사실 엄청나게 큰 산에서 내려가는 문제와 비슷하다. loss surface 위에서 현재 파라미터 위치가 있고, gradient는 “어느 방향으로 움직이면 loss가 가장 빨리 증가하는가”를 알려준다. 그래서 optimizer는 그 반대 방향으로 조금 이동해서 loss를 줄인다.

---

## 3) 연쇄법칙과 계산 그래프

### 한 줄 직관
복잡한 모델도 잘게 쪼개서 보면 작은 연산들의 연결이고, 연쇄법칙은 그 연결을 따라 gradient를 뒤로 전달하는 규칙이다.

### 쉬운 설명
함수 `y = f(g(x))`를 생각해보자.
이 함수는 사실 두 단계다.
1. 먼저 `g(x)` 계산
2. 그 결과를 다시 `f()`에 넣어 `y` 계산

그렇다면 x가 바뀔 때 y가 얼마나 바뀌는지는
- `g` 단계가 얼마나 민감한지
- `f` 단계가 얼마나 민감한지

를 연결해서 봐야 한다. 이것이 chain rule(연쇄법칙)이다.

### 계산 그래프 직관
복잡한 수식을 작은 연산 노드로 나눠 그리면 계산 그래프가 된다.
예를 들어
- 곱셈
- 덧셈
- activation
- softmax

같은 연산을 노드로 보면, 모델 전체도 결국 그래프로 표현할 수 있다.

forward pass는 이 그래프를 따라 값을 계산하는 과정이다.
backward pass는 출력에서 시작해서 gradient를 뒤로 전달하는 과정이다.

### 핵심 포인트
- chain rule은 합성함수의 미분 규칙이다.
- computational graph는 복잡한 함수를 작은 연산들의 연결로 표현한 것이다.
- backpropagation은 계산 그래프 위에서 chain rule을 효율적으로 수행하는 알고리즘이다.
- 각 노드는 자기 local gradient만 정확히 알면 된다.
- upstream gradient와 local gradient를 곱해 이전 단계로 전달한다.

### AI 연결
Transformer 한 층도 사실은
- matmul
- scaling
- softmax
- weighted sum
- residual addition
- normalization

같은 작은 연산들의 합성이다. chain rule이 없으면 이런 큰 모델의 미분을 손으로 다 계산해야 해서 사실상 학습이 불가능하다. autograd는 이 과정을 자동으로 처리해 주는 시스템이다.

---

## 복습 질문
1. derivative와 rate of change는 어떤 관계이며, 왜 1차 근사가 최적화의 출발점이 될까?
2. gradient가 “가장 빠른 증가 방향”이라는 말은 directional derivative 식과 어떻게 연결될까?
3. backpropagation을 계산 그래프와 chain rule 관점에서 설명하면 어떤 단계들로 나뉠까?

## 복습 정답과 설명

### 1. derivative와 rate of change는 어떤 관계이며, 왜 1차 근사가 최적화의 출발점이 될까?
**정답**
- derivative는 함수의 한 점에서 측정한 local rate of change다.
- 1차 근사는 derivative를 이용해 아주 가까운 구간에서 함수를 선형처럼 근사하는 방식이다.
- 최적화는 이 근사를 이용해 어느 방향으로 움직이면 loss가 줄어드는지 판단한다.

**설명**
평균 변화율은 두 점 사이의 전체 기울기이고, derivative는 한 점에서의 순간 기울기다. 복잡한 함수도 아주 작은 범위에서는 직선처럼 근사할 수 있으므로, 현재 점에서의 derivative만 알면 근처에서 loss가 증가하는지 감소하는지 판단할 수 있다. 이것이 gradient-based optimization의 출발점이다.

### 2. gradient가 “가장 빠른 증가 방향”이라는 말은 directional derivative 식과 어떻게 연결될까?
**정답**
특정 방향 `v`로 움직일 때의 변화율은 directional derivative로 나타내며, 이 값은 `∇f(x)^T v`로 쓸 수 있다. 이 값이 가장 커지는 방향이 바로 gradient 방향이다.

**설명**
이 식은 gradient를 단순한 편미분 목록이 아니라 “최적 방향 벡터”로 해석하게 해준다. `v`가 gradient와 같은 방향이면 증가율이 가장 크고, 반대 방향이면 감소가 가장 크다. 그래서 gradient descent는 보통 `-gradient` 방향으로 이동한다.

### 3. backpropagation을 계산 그래프와 chain rule 관점에서 설명하면 어떤 단계들로 나뉠까?
**정답**
1. forward pass: 각 노드 값을 계산한다.
2. loss 계산: 최종 출력으로부터 loss를 만든다.
3. backward 시작: 출력 쪽 gradient를 설정한다.
4. local gradient 계산: 각 노드가 자기 입력에 대한 미분값을 구한다.
5. chain rule 적용: upstream gradient와 local gradient를 곱해 이전 노드로 전달한다.
6. parameter gradient 축적: weight와 bias에 대한 gradient를 모은다.
7. optimizer update: gradient를 이용해 parameter를 갱신한다.

**설명**
핵심은 큰 함수를 직접 미분하지 않고, 작은 연산의 연결로 나눠서 미분한다는 것이다. 계산 그래프에서는 각 노드가 자기 local gradient만 알면 되고, backward pass에서는 이를 chain rule로 연결해 전체 gradient를 얻는다. autograd는 이 과정을 자동화한 시스템이다.

## 한 줄 정리
미분은 변화율을 읽는 도구이고, gradient는 다변수 loss의 민감도 벡터이며, chain rule과 계산 그래프는 그 gradient를 실제 대규모 모델 학습에서 계산 가능하게 만드는 핵심 구조다.
