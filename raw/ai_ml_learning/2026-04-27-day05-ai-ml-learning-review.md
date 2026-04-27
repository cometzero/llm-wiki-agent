# 2026-04-27 AI/ML Learning Day 05

- Date: 2026-04-27
- Day: 05/30
- Level: beginner-intermediate
- Theme: 미분과 최적화의 핵심
- Lesson source: /home/ubuntu/work/ai/learning/logs/2026-04-27-day05.md
- Follow-up answer source: /home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-04-27_09-26-25.md

## 학습 내용

# Day 05 - AI/ML 기초 학습

- Date: 2026-04-27
- Progress: 5/30
- Level: beginner-intermediate
- Milestone: 미분과 최적화의 핵심
- Milestone goal: 학습이 왜 최적화 문제인지 이해하고 gradient 기반 학습의 기초를 다진다.

## 오늘의 3가지 개념
1. 최적화 문제와 목적함수
2. 손실함수와 경험위험
3. 경사하강법과 step update

---

## 1) 최적화 문제와 목적함수

### 한 줄 직관
머신러닝 학습은 “수많은 후보 중에서 가장 좋은 설정을 찾는 일”이고, 그때 무엇이 좋은지 숫자로 알려주는 기준이 목적함수(objective)다.

### 개념 정의
최적화(optimization)는 어떤 목표를 가장 잘 만족하는 값을 찾는 문제다. 머신러닝에서는 보통 모델의 parameter를 조절해서 성능이 가장 좋게 만드는 값을 찾는다. 이때 “좋다”를 수치로 표현한 함수가 목적함수(objective)다. 

예를 들어 어떤 모델이 예측을 잘할수록 작은 값을 갖는 함수를 만들었다면, 우리는 그 함수를 가장 작게 만드는 parameter를 찾고 싶다. 이것을 흔히
\[
\arg\min_{\theta} J(\theta)
\]
처럼 쓴다. 여기서 \(\theta\)는 모델 parameter, \(J(\theta)\)는 목적함수, \(\arg\min\)은 “가장 작은 값을 만드는 입력 자체”를 뜻한다.

또 어떤 문제는 제약조건(constraint)이 있다. 예를 들어 parameter가 너무 커지지 않게 하거나, 확률값의 합이 1이 되게 하거나, 특정 메모리 한도를 넘지 않게 해야 할 수 있다. 그러면 “아무 값이나”가 아니라 “조건을 만족하는 값 중 가장 좋은 것”을 찾아야 한다.

### 왜 이런 개념이 필요한가
AI 모델은 학습 전에는 그냥 숫자 덩어리에 가깝다. 어떤 weight를 크게 하고 어떤 weight를 작게 해야 정답에 가까워지는지 사람이 직접 하나씩 정하기는 거의 불가능하다. 그래서 모델이 잘하는 정도를 하나의 숫자로 모으고, 그 숫자가 더 좋아지는 방향으로 자동으로 움직이게 만들어야 한다.

이 관점이 중요한 이유는 다음과 같다.
- 분류, 회귀, 추천, 번역, LLM 학습까지 대부분이 결국 최적화 문제로 표현된다.
- 모델 구조가 달라도 “무엇을 최소화하거나 최대화할 것인가”를 정해야 학습이 가능하다.
- optimizer는 목적함수를 직접 다루는 알고리즘이므로, 목적함수가 무엇인지 이해해야 optimizer의 동작도 이해된다.

쉽게 말해, 목적함수가 없으면 모델은 어디로 가야 할지 모른다. 나침반 없이 산을 걷는 것과 비슷하다.

### 아주 쉬운 예시
키와 몸무게로 칼로리 소비량을 예측하는 아주 단순한 모델이 있다고 하자.

모델을
\[
y = wx
\]
라고 두고, 데이터가 하나뿐이라고 해보자.
- 입력 \(x=2\)
- 정답 \(y=6\)

이제 \(w\) 후보를 몇 개 넣어 보자.
- \(w=1\)이면 예측은 2
- \(w=2\)이면 예측은 4
- \(w=3\)이면 예측은 6
- \(w=4\)이면 예측은 8

정답 6에 가장 잘 맞는 것은 \(w=3\)이다. 여기서 “잘 맞는다”를 숫자로 계산해 주는 함수가 목적함수다. 예를 들어 오차 제곱을 목적함수로 두면
\[
J(w)=(wx-6)^2
\]
가 된다. 

각 후보에서 계산하면
- \(w=1\): \((2-6)^2=16\)
- \(w=2\): \((4-6)^2=4\)
- \(w=3\): \((6-6)^2=0\)
- \(w=4\): \((8-6)^2=4\)

따라서 이 목적함수는 \(w=3\)에서 가장 작다. 이것이 “최적화 문제를 푼다”는 말의 가장 단순한 모습이다.

### 개념 구조와 핵심 포인트
- **optimization**: 좋은 해를 찾는 전체 문제 자체다.
- **objective**: 무엇이 좋은지를 숫자로 정한 함수다.
- **parameter**: 우리가 조절하는 모델 내부 숫자다.
- **constraint**: 아무 해나 허용하지 않고 지켜야 하는 조건이다.
- **argmin**: 가장 작은 objective 값을 만드는 parameter를 가리킨다.

여기서 꼭 구분해야 할 점이 있다.
1. **최솟값 자체**와 **그 값을 만드는 입력**은 다르다.  
   예를 들어 목적함수 값이 0이라는 것은 최솟값이고, 그때의 \(w=3\)이 argmin이다.
2. 목적함수가 하나라고 해서 답도 항상 하나인 것은 아니다.  
   서로 다른 parameter가 같은 objective 값을 낼 수도 있다.
3. 실제 딥러닝에서는 목적함수 표면이 매우 복잡하다.  
   언덕도 많고 골짜기도 많다. 그래서 단순 대입이 아니라 gradient 기반 방법이 필요하다.
4. 모델이 커질수록 해를 “공식으로 한 번에” 구하기보다, 조금씩 개선하는 방식이 더 현실적이다.

### 핵심 수학 포인트
최적화 문제는 보통 다음처럼 쓴다.
\[
\min_{\theta} J(\theta)
\]
또는 argmin을 써서
\[
\theta^* = \arg\min_{\theta} J(\theta)
\]
라고 쓴다. \(\theta^*\)는 최적의 parameter를 뜻한다.

여기서 중요한 수학적 생각은 아주 단순하다.
- 입력: \(\theta\)
- 출력: 목적함수 값 \(J(\theta)\)
- 목표: 출력이 작아지도록 입력을 조절

1차원에서는 이것이 그냥 숫자 하나를 조절하는 문제처럼 보인다. 하지만 실제 신경망에서는 \(\theta\)가 수천, 수백만, 수십억 개일 수 있다. 즉 목적함수는 하나의 숫자를 출력하지만, 입력은 매우 큰 벡터다.

그래서 최적화는 “고차원 공간에서 가장 낮은 지점을 찾는 문제”로 이해하면 좋다. 이 그림이 머릿속에 있어야 다음 개념인 loss, risk, gradient descent가 자연스럽게 연결된다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)
- **optimization**: 가장 좋은 해를 찾는 문제
- **objective**: 좋고 나쁨을 수치화한 함수
- **constraint**: 해가 만족해야 하는 조건
- **argmin**: objective를 가장 작게 만드는 입력

### AI에서 어디에 쓰이는가
- **linear regression**에서는 예측 오차를 가장 작게 만드는 weight를 찾는다.
- **image classifier**에서는 정답 class 확률이 높아지도록 objective를 최소화한다.
- **embedding 학습**에서는 비슷한 의미의 벡터가 가까워지도록 objective를 설계한다.
- **LLM pretraining**에서는 다음 토큰을 잘 맞히도록 huge objective를 최소화한다.
- **RL**에서는 반대로 reward를 크게 만드는 maximization 형태가 자주 나온다.

즉 AI의 거의 모든 학습은 “모델을 만드는 일”이라기보다 “좋은 objective를 정의하고 그것을 잘 최적화하는 일”에 가깝다.

### 헷갈리기 쉬운 포인트
- **objective와 loss를 같은 말로만 생각하면 안 된다.** 실무에서는 거의 비슷하게 섞어 쓰지만, loss는 데이터 한 개나 배치 하나의 오차를 말하고, objective는 loss에 regularization 같은 항까지 포함한 전체 최적화 대상인 경우가 많다.
- **argmin은 값이 아니라 위치다.** 최소값 자체와 혼동하기 쉽다.
- **constraint가 없다고 항상 좋은 것은 아니다.** 제약이 없으면 모델이 너무 큰 weight를 써서 train data만 외우는 방향으로 갈 수 있다.
- **정답이 수식으로 바로 안 나와도 학습은 가능하다.** 딥러닝은 대부분 닫힌형 해(closed-form solution) 대신 반복 최적화를 쓴다.

---

## 2) 손실함수와 경험위험

### 한 줄 직관
모델이 틀릴수록 벌점을 주는 숫자가 손실함수(loss)이고, 여러 데이터에서 그 벌점을 평균낸 것이 우리가 실제로 줄이려는 경험위험(empirical risk)이다.

### 개념 정의
손실함수(loss function)는 모델의 예측이 정답과 얼마나 다른지를 숫자로 측정하는 함수다. 예측이 좋으면 loss가 작고, 예측이 나쁘면 loss가 크다.

하지만 데이터는 한 개가 아니라 여러 개다. 그래서 실제 학습에서는 한 샘플의 loss만 보는 것이 아니라, 데이터셋 전체에서 평균적으로 얼마나 틀리는지를 본다. 이 평균적인 오차 개념이 위험(risk)이다.

이론적으로는 “세상에 존재하는 모든 가능한 데이터”에 대한 평균 오차를 생각할 수 있는데, 실제로는 그 전체 분포를 모르므로 우리가 가진 train data로 대신 평균을 낸다. 이렇게 train data 위에서 계산한 평균 오차를 경험위험(empirical risk)이라고 한다. 그리고 **empirical risk minimization**, 줄여서 **ERM**은 “train data 평균 loss를 최소화하자”는 아주 기본적인 학습 원리다.

또 어떤 경우에는 직접 원하는 평가 지표를 최적화하기 어렵다. 예를 들어 0 아니면 1로만 맞고 틀림을 세는 함수는 미분이 어려울 수 있다. 그래서 학습할 때는 더 다루기 쉬운 대체 손실(surrogate loss)을 쓴다.

### 왜 이런 개념이 필요한가
모델이 좋다는 말을 하려면 “무엇을 기준으로 좋다고 할 것인가”가 필요하다. 분류 문제에서 단순 정확도만 보면 학습 중에 미세한 차이를 읽기 어렵다. 예를 들어 정답 확률이 0.49에서 0.51로 바뀌는 것과 0.01에서 0.49로 바뀌는 것은 정확도 숫자만 보면 둘 다 비슷하거나 아예 차이가 안 보일 수 있다. 하지만 학습 관점에서는 두 경우가 다르다.

loss는 이런 차이를 더 섬세하게 반영한다. 그래서 gradient를 통해 모델이 어느 방향으로 개선되어야 하는지 알려줄 수 있다.

또 데이터가 여러 개일 때 한 샘플만 잘 맞고 나머지를 못 맞히는 모델은 좋은 모델이 아니다. 그래서 평균적인 성능, 즉 risk 관점이 필요하다. 이 생각이 generalization으로 이어진다. train loss만 낮추고 새로운 데이터에서 못 맞히면 overfitting 문제가 생긴다.

### 아주 쉬운 예시
이진 분류를 생각해 보자. 정답이 1인 데이터가 3개 있고, 모델이 정답 class 확률을 다음처럼 냈다고 하자.
- 샘플 A: 0.9
- 샘플 B: 0.6
- 샘플 C: 0.2

아주 단순하게 loss를 \((예측 - 정답)^2\)로 보자.
- A: \((0.9-1)^2 = 0.01\)
- B: \((0.6-1)^2 = 0.16\)
- C: \((0.2-1)^2 = 0.64\)

개별 loss만 보면 C가 가장 큰 문제다. 
이제 평균을 내면
\[
\frac{0.01+0.16+0.64}{3} = 0.27
\]
이 값이 경험위험의 아주 단순한 예다.

즉 모델이 전체적으로 얼마나 틀리는지를 한 숫자로 볼 수 있게 된다. 학습은 이 평균을 0.27에서 0.20, 0.10처럼 계속 낮추는 과정이다.

### 개념 구조와 핵심 포인트
- **loss**는 샘플 하나 또는 배치 하나의 오차를 말한다.
- **risk**는 기대값, 즉 평균적인 오차라는 더 큰 개념이다.
- **empirical risk**는 우리가 가진 train data로 계산한 평균 오차다.
- **ERM**은 empirical risk를 최소화하는 학습 원리다.
- **surrogate loss**는 직접 최적화하기 어려운 목표 대신 사용하는, 더 부드럽고 미분 가능한 학습용 loss다.

여기서 중요한 흐름은 이렇다.
1. 샘플마다 loss를 계산한다.
2. 여러 샘플에서 평균을 낸다.
3. 그 평균이 현재 모델의 학습 상태를 대표한다.
4. optimizer는 그 평균 loss를 줄이는 방향으로 parameter를 바꾼다.

즉 loss는 개별 벌점이고, empirical risk는 그 벌점의 평균 성적표라고 생각하면 된다.

### 핵심 수학 포인트
데이터가 \((x_i, y_i)\)로 \(N\)개 있다고 하자. 모델이 \(f_\theta(x_i)\)를 예측하면, 샘플별 loss는 보통
\[
\ell(f_\theta(x_i), y_i)
\]
처럼 쓴다.

경험위험(empirical risk)은
\[
\hat{R}(\theta)=\frac{1}{N}\sum_{i=1}^{N} \ell(f_\theta(x_i), y_i)
\]
이다.

여기서 포인트는 아주 중요하다.
- \(\ell\)은 “한 개 샘플”의 오차다.
- \(\hat{R}(\theta)\)는 “전체 데이터 평균”이다.
- 학습은 보통 \(\hat{R}(\theta)\)를 최소화하는 것이다.

실전에서는 이 평균에 regularization 항이 더해져서
\[
J(\theta)=\hat{R}(\theta)+\lambda \Omega(\theta)
\]
형태가 되기도 한다. 이때 \(\Omega(\theta)\)는 weight가 지나치게 커지지 않게 막는 penalty다. 그래서 objective와 empirical risk가 완전히 같은 말이 아닐 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)
- **loss**: 예측 하나가 얼마나 틀렸는지 재는 함수
- **risk**: 평균적인 오차라는 더 큰 개념
- **empirical risk minimization**: train data 평균 loss를 줄이는 학습 원리
- **surrogate loss**: 직접 최적화하기 어려운 목표 대신 쓰는 학습용 loss

### AI에서 어디에 쓰이는가
- **회귀(regression)**에서는 MSE loss를 자주 쓴다.
- **분류(classification)**에서는 cross-entropy loss가 대표적이다.
- **LLM**에서는 다음 토큰 예측의 cross-entropy가 핵심 training loss다.
- **contrastive learning**에서는 positive pair는 가깝게, negative pair는 멀게 만드는 surrogate loss를 설계한다.
- **reinforcement learning**에서도 policy loss, value loss처럼 여러 loss를 묶어 objective를 만든다.

특히 LLM에서는 attention, hidden state, embedding이 아무리 복잡해도 마지막에는 “정답 토큰 확률을 얼마나 잘 올렸는가”가 loss로 요약된다. 그래서 loss는 모델 내부의 수많은 연산을 학습 신호 하나로 묶는 중심 역할을 한다.

### 헷갈리기 쉬운 포인트
- **loss가 낮다고 무조건 실제 성능이 좋지는 않다.** train loss만 계속 낮고 validation 성능이 나쁘면 overfitting일 수 있다.
- **accuracy와 loss는 다르다.** accuracy가 같아도 loss는 다를 수 있다. 정답 확률 0.51과 0.99는 둘 다 맞았지만 학습 신호는 크게 다르다.
- **surrogate loss는 가짜가 아니라 실용적인 대리 목표다.** 최종 평가 지표를 더 잘 학습하게 만들기 위해 쓰는 경우가 많다.
- **empirical risk는 전체 세상의 진짜 평균 오차가 아니다.** 우리가 가진 샘플 기준 평균이므로 데이터 편향의 영향을 받을 수 있다.

---

## 3) 경사하강법과 step update

### 한 줄 직관
지금 서 있는 곳의 기울기(gradient)를 보고, 아래로 내려가는 쪽으로 조금 이동하는 가장 기본적인 학습 방법이 경사하강법(gradient descent)이다.

### 개념 정의
경사하강법(gradient descent)은 목적함수를 줄이기 위해 parameter를 반복적으로 업데이트하는 방법이다. 핵심 아이디어는 간단하다. gradient는 함수가 가장 빠르게 증가하는 방향을 가리키므로, 그 반대 방향으로 가면 함수값을 줄일 가능성이 높다.

업데이트 규칙(update rule)은 보통 다음처럼 쓴다.
\[
\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)
\]
여기서
- \(\theta_t\): 현재 parameter
- \(\nabla J(\theta_t)\): 현재 위치의 gradient
- \(\eta\): step size 또는 learning rate

즉 “현재 위치 - (얼마나 내려가야 하는지)”의 구조다.

### 왜 이런 개념이 필요한가
딥러닝 모델은 parameter가 너무 많아서, 목적함수의 최솟값을 한 번에 계산하는 공식이 없는 경우가 대부분이다. 그래서 조금씩 개선해 나가는 반복적 방법이 필요하다.

경사하강법이 중요한 이유는 다음과 같다.
- 목적함수가 복잡해도 local slope만 알면 다음 이동을 정할 수 있다.
- backpropagation이 계산한 gradient를 실제 parameter 변경으로 연결해 준다.
- Adam, RMSProp, momentum 같은 복잡한 optimizer도 결국 gradient descent의 확장판이다.

쉽게 말하면, gradient가 “어느 쪽이 오르막인가”를 알려주고, gradient descent가 “그럼 어느 쪽으로 얼마나 움직일까”를 결정한다.

### 아주 쉬운 예시
가장 단순하게
\[
J(w)=(w-3)^2
\]
를 최소화한다고 하자. 최솟값은 눈으로 보면 \(w=3\)이다. 하지만 지금은 그 답을 모른다고 가정하고 경사하강법으로 찾아 보자.

미분하면
\[
\frac{dJ}{dw}=2(w-3)
\]
이다.

초기값을 \(w=0\), step size를 \(\eta=0.5\)로 두면
1. 현재 gradient: \(2(0-3)=-6\)
2. update: \(w \leftarrow 0 - 0.5(-6)=3\)

한 번에 최적점에 도착했다.

이번에는 step size를 \(\eta=0.1\)로 두자.
- 시작: \(w=0\)
- gradient: -6 → 새 \(w=0.6\)
- gradient: \(2(0.6-3)=-4.8\) → 새 \(w=1.08\)
- gradient: \(2(1.08-3)=-3.84\) → 새 \(w=1.464\)

조금씩 3에 가까워진다. 이 예시가 보여주는 핵심은 아주 명확하다.
- 방향은 gradient가 정한다.
- 얼마나 멀리 갈지는 step size가 정한다.

### 개념 구조와 핵심 포인트
- **gradient descent**: gradient 반대 방향으로 움직이는 반복 최적화 방법
- **descent direction**: objective를 줄이는 방향. 가장 기본형에서는 \(-\nabla J\)다.
- **step size**: 한 번에 얼마나 이동할지 정하는 크기다.
- **update rule**: 현재 parameter를 다음 parameter로 바꾸는 공식이다.

이 구조를 실제 학습 흐름으로 보면
1. forward pass로 예측을 만든다.
2. loss를 계산한다.
3. backward pass로 gradient를 계산한다.
4. optimizer가 update rule에 따라 parameter를 바꾼다.
5. 이 과정을 수천~수백만 번 반복한다.

딥러닝 프레임워크에서 `optimizer.step()`은 바로 이 과정을 코드로 실행하는 부분이다.

### 핵심 수학 포인트
작은 이동 \(\Delta \theta\)에 대해 목적함수는 1차 근사로
\[
J(\theta + \Delta \theta) \approx J(\theta) + \nabla J(\theta)^\top \Delta \theta
\]
라고 볼 수 있다.

이제 \(\Delta \theta = -\eta \nabla J(\theta)\)를 넣으면
\[
J(\theta + \Delta \theta) \approx J(\theta) - \eta \|\nabla J(\theta)\|^2
\]
가 된다. 여기서 \(\|\nabla J(\theta)\|^2\)는 gradient 크기의 제곱이다. \(\eta > 0\)가 너무 크지만 않다면, 이 식은 목적함수가 줄어드는 방향이라는 직관을 준다.

즉 gradient의 반대 방향을 택하는 이유는 단순 암기가 아니라, 1차 근사에서 실제로 감소가 보이기 때문이다.

또 learning rate가 너무 크면 한 번에 너무 멀리 가서 골짜기를 지나쳐 버릴 수 있고, 너무 작으면 학습이 매우 느려진다. 그래서 step size 조절은 실전에서 매우 중요하다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)
- **gradient descent**: gradient 반대 방향으로 이동하며 objective를 줄이는 방법
- **step size**: 한 번 update할 때 이동 크기, learning rate와 거의 같은 의미로 자주 사용
- **update rule**: parameter를 어떻게 바꾸는지 적은 공식
- **descent direction**: objective를 낮추는 방향

### AI에서 어디에 쓰이는가
- **신경망 학습 전체**가 거의 이 틀 위에서 돌아간다.
- **SGD, mini-batch SGD, Adam**은 모두 gradient descent의 변형이다.
- **embedding layer**도 gradient를 받아 벡터가 조금씩 수정된다.
- **attention block**의 query, key, value projection weight도 update rule로 바뀐다.
- **LLM finetuning**에서는 enormous parameter 중 실제 학습 대상 전체 또는 LoRA adapter만 gradient descent 계열 optimizer로 업데이트한다.

즉 경사하강법은 “모델이 학습한다”는 말을 가장 구체적으로 풀어쓴 형태다. hidden state가 어떻게 나오든, loss가 계산된 뒤에는 결국 parameter update가 일어나야 모델이 달라진다.

### 헷갈리기 쉬운 포인트
- **gradient가 0이라고 항상 최솟값은 아니다.** 평평한 지점이나 local maximum일 수도 있다.
- **step size를 크게 하면 무조건 빨라지는 것이 아니다.** 너무 크면 loss가 오히려 발산할 수 있다.
- **gradient descent와 backpropagation은 같은 것이 아니다.** backpropagation은 gradient를 계산하는 방법이고, gradient descent는 그 gradient로 parameter를 업데이트하는 방법이다.
- **한 번 update했다고 끝나는 것이 아니다.** 실제 학습은 매우 많은 step의 반복이다.

---

## 복습 질문 3개
1. objective와 argmin은 각각 무엇을 뜻하며, 왜 머신러닝 학습을 최적화 문제로 볼 수 있을까?
2. loss와 empirical risk의 차이는 무엇이고, ERM은 왜 train data 평균 오차를 중심으로 설명될까?
3. gradient descent update rule에서 gradient와 step size는 각각 어떤 역할을 하나?

## 오늘의 한 줄 요약
머신러닝 학습은 목적함수(objective)를 가장 좋게 만드는 parameter를 찾는 최적화 문제이고, 실제로는 데이터 평균 loss인 경험위험을 줄이기 위해 gradient descent update를 반복하는 과정이다.

---

## 복습 정답과 해설

[AI/ML 오늘의 복습 정답 Day 05/30]
오늘 배운 3가지 핵심 개념을 복습 질문에 맞춰 쉬운 말로 다시 풀어볼게요.

### 1. objective와 argmin은 각각 무엇을 뜻하며, 왜 머신러닝 학습을 최적화 문제로 볼 수 있을까?

**정답**

objective는 모델이 얼마나 잘하고 있는지를 숫자로 나타내는 기준 함수입니다.  
argmin은 그 objective 값을 가장 작게 만드는 parameter 값 자체를 뜻합니다.  

머신러닝 학습을 최적화 문제로 보는 이유는, 결국 우리가 하는 일이 모델의 parameter를 조절해서 objective가 가장 좋아지게 만드는 값을 찾는 일이기 때문입니다.

**설명**

먼저 objective부터 보면, 이것은 “무엇이 좋은 모델인가?”를 숫자로 정한 규칙입니다.  
예를 들어 예측이 틀릴수록 큰 벌점을 주고, 잘 맞을수록 작은 값을 주는 함수를 만들 수 있습니다. 그러면 학습의 목표는 아주 자연스럽게 “이 숫자를 가능한 한 작게 만들자”가 됩니다.

argmin은 여기서 한 단계 더 구체적인 말입니다.  
많은 초보자가 헷갈리는 부분인데, 최소값과 argmin은 다릅니다.

- 최소값: objective가 가장 작아졌을 때의 함수값
- argmin: 그 가장 작은 값을 만들어낸 parameter 위치

예를 들어 objective 값이 0이 가장 작은 값이고, 그때의 parameter가 w=3이라면:
- 최소값은 0
- argmin은 w=3

머신러닝 학습이 왜 최적화 문제냐고 하면, 학습은 그냥 “모델을 돌린다”가 아니라 “수많은 가능한 parameter 후보 중에서 가장 좋은 것을 찾는다”는 과정이기 때문입니다.  
선형회귀든, 이미지 분류든, LLM이든, 결국은 내부 weight를 바꿔 가면서 어떤 기준 숫자(objective)를 더 좋게 만드는 방향으로 움직입니다.

즉 핵심은 이겁니다.

- 모델에는 조절할 숫자(parameter)가 있다
- 그 숫자가 좋고 나쁨을 판단하는 함수가 있다
- 학습은 그 함수를 가장 좋게 만드는 parameter를 찾는 과정이다

그래서 머신러닝은 본질적으로 최적화 문제라고 부릅니다.

**예시**

아주 작은 예시로 모델이 y = wx 라고 해볼게요.  
입력이 x=2이고 정답이 y=6이라고 합시다.

이때 w를 여러 개 넣어 보면:

- w=1이면 예측 2
- w=2이면 예측 4
- w=3이면 예측 6
- w=4이면 예측 8

오차를 재는 objective를 J(w)=(2w-6)^2 라고 두면:

- J(1)=16
- J(2)=4
- J(3)=0
- J(4)=4

여기서 objective는 J(w)이고, argmin은 w=3입니다.  
즉 “가장 좋은 w를 찾는 문제”가 바로 최적화 문제입니다.

**실전 연결**

실전 ML/DL에서는 이 생각이 그대로 이어집니다.  
분류 모델은 cross-entropy 같은 objective를 줄이도록 학습하고, 회귀 모델은 MSE를 줄이도록 학습합니다. LLM도 다음 토큰을 더 잘 맞히도록 training objective를 최소화합니다. 모델 구조가 아무리 복잡해도, 마지막에는 “어떤 숫자를 좋게 만들 것인가”와 “그 숫자를 가장 좋게 만드는 parameter는 무엇인가”의 문제로 정리됩니다.

### 2. loss와 empirical risk의 차이는 무엇이고, ERM은 왜 train data 평균 오차를 중심으로 설명될까?

**정답**

loss는 보통 개별 샘플 하나 또는 한 배치에서의 오차를 말합니다.  
empirical risk는 train data 전체에 대해 loss를 평균낸 값입니다.  

ERM(empirical risk minimization)은 우리가 실제로는 세상의 모든 데이터를 알 수 없기 때문에, 현재 가진 train data에서 평균 오차를 작게 만드는 방식으로 학습을 설명하는 원리입니다.

**설명**

loss는 아주 로컬한 개념입니다.  
한 개의 입력에 대해 모델이 얼마나 틀렸는지를 점수처럼 계산합니다. 예측이 맞으면 작고, 틀리면 큽니다.

그런데 실제 학습에서는 데이터가 하나가 아닙니다.  
샘플이 수십 개, 수천 개, 수백만 개가 있을 수 있습니다. 그러면 한 샘플의 loss만 보고 모델이 좋다고 말할 수 없습니다. 어떤 샘플은 잘 맞고, 어떤 샘플은 크게 틀릴 수 있기 때문입니다.

그래서 여러 샘플의 loss를 모아서 평균적인 오차를 봐야 합니다. 이 평균적인 관점이 risk입니다.  
그리고 우리가 실제로 손에 쥐고 있는 train data 위에서 계산한 평균 오차가 empirical risk입니다.

쉽게 정리하면:

- loss: 한 문제의 틀린 정도
- empirical risk: 여러 문제의 평균 성적

ERM은 “train data에서 평균 loss를 줄이자”는 학습 원리입니다.  
왜 굳이 train data 평균 오차를 중심으로 설명하느냐 하면, 현실에서는 데이터가 생성되는 진짜 전체 분포를 직접 다 볼 수 없기 때문입니다. 세상에 존재할 모든 입력을 다 모아 평균을 계산하는 것은 불가능합니다. 그래서 지금 가진 샘플(train set)을 대표 표본처럼 사용해서 평균을 냅니다.

즉 ERM은 완벽한 답이라기보다, 현실적인 학습 원칙입니다.  
우리가 가진 데이터를 기준으로 가장 잘하는 모델을 찾자는 것입니다.

여기서 중요한 감각이 하나 더 있습니다.  
loss는 학습 신호를 더 섬세하게 줍니다. accuracy는 맞았는지 틀렸는지만 보여주는 경우가 많지만, loss는 “얼마나 자신 있게 틀렸는지”, “조금 나아졌는지”까지 반영할 수 있습니다. 그래서 optimizer가 더 부드럽게 학습 방향을 잡을 수 있습니다.

**예시**

정답이 모두 1인 샘플 3개가 있다고 해볼게요.  
모델이 정답 class 확률을 이렇게 냈다고 합시다.

- A: 0.9
- B: 0.6
- C: 0.2

아주 단순하게 loss를 (예측-정답)^2 로 두면:

- A의 loss = (0.9-1)^2 = 0.01
- B의 loss = (0.6-1)^2 = 0.16
- C의 loss = (0.2-1)^2 = 0.64

여기서 각 샘플의 값은 loss입니다.  
그리고 empirical risk는 이 셋의 평균입니다.

(0.01 + 0.16 + 0.64) / 3 = 0.27

즉:
- A, B, C 각각의 점수는 loss
- 전체 평균 0.27은 empirical risk

이제 학습은 이 평균 0.27을 더 낮추는 방향으로 진행됩니다.

**실전 연결**

실전에서는 거의 모든 딥러닝 학습이 이 구조를 따릅니다.  
이미지 분류에서는 batch마다 cross-entropy loss를 계산하고, optimizer는 그 평균 loss를 줄이도록 weight를 바꿉니다. LLM도 문장 속 각 토큰 예측의 loss를 쌓아서 평균 내고, 그 값을 줄이도록 학습합니다. 또 추천 시스템, 음성 모델, 임베딩 학습도 결국 train data 평균 오차를 줄이는 식으로 돌아갑니다. 다만 실전에서는 empirical risk에 regularization 같은 항을 더해 objective를 만들기도 해서, loss와 전체 objective가 완전히 같은 말은 아닐 수 있습니다.

### 3. gradient descent update rule에서 gradient와 step size는 각각 어떤 역할을 하나?

**정답**

gradient는 현재 위치에서 objective가 가장 가파르게 증가하는 방향과 크기를 알려줍니다.  
그래서 gradient descent에서는 그 반대 방향으로 움직여 objective를 줄이려 합니다.  

step size는 그 방향으로 한 번에 얼마나 멀리 이동할지를 정합니다.  
즉 gradient는 방향과 기울기 정보를 주고, step size는 이동 거리의 크기를 정합니다.

**설명**

gradient descent의 기본 update rule은 보통 이렇게 씁니다.

θ_(t+1) = θ_t - η∇J(θ_t)

여기서 핵심 역할을 나눠 보면 아주 분명합니다.

1. gradient
gradient는 “지금 이 자리에서 어느 쪽이 오르막인지”를 알려줍니다.  
함수가 가장 빨리 커지는 방향을 가리키기 때문에, 우리는 그 반대 방향으로 가면 내려갈 가능성이 높습니다. 그래서 식에서 마이너스가 붙습니다.

2. step size
step size(또는 learning rate)는 “얼마나 크게 움직일 것인가”를 정합니다.  
같은 gradient를 보더라도 step size가 크면 한 번에 멀리 가고, 작으면 조금만 갑니다.

비유하면:
- gradient는 내리막이 어느 방향인지 알려주는 화살표
- step size는 그 방향으로 한 걸음인지, 세 걸음인지 정하는 값

둘 다 중요합니다.  
방향만 맞고 너무 크게 가면 목표 지점을 지나쳐 버릴 수 있습니다.  
반대로 방향은 맞아도 너무 조금씩 가면 학습이 너무 느려집니다.

또 gradient의 크기 자체도 의미가 있습니다.  
기울기가 가파르면 “여기는 아직 많이 틀려 있다”는 신호가 될 수 있고, 기울기가 작으면 “평평해지거나 최적점 근처일 수 있다”는 신호가 될 수 있습니다. 물론 gradient가 0이라고 무조건 최솟값은 아니라는 점은 주의해야 합니다.

정리하면:

- gradient: 어디로 가야 줄어드는지 알려줌
- step size: 얼마나 크게 갈지 정함
- update rule: 이 둘을 이용해 parameter를 실제로 바꿈

이것이 바로 “모델이 학습한다”는 말의 가장 구체적인 모습입니다.

**예시**

아주 간단하게 J(w)=(w-3)^2 를 최소화한다고 해볼게요.

이 함수를 미분하면 gradient는:

dJ/dw = 2(w-3)

초기값을 w=0으로 두겠습니다.

먼저 현재 gradient를 계산하면:
- 2(0-3) = -6

이 말은 지금 위치에서 objective가 증가하는 방향이 왼쪽 쪽이라는 뜻이고,  
우리는 반대 방향으로 가야 하니 오른쪽으로 이동하게 됩니다.

step size가 0.1이면:
- w ← 0 - 0.1(-6) = 0.6

즉 조금 이동합니다.

step size가 0.5이면:
- w ← 0 - 0.5(-6) = 3

이번에는 한 번에 최적점까지 갑니다.

이 예시에서 보이는 점은 아주 중요합니다.

- gradient가 없으면 어느 방향으로 가야 할지 모른다
- step size가 없으면 얼마나 움직일지 정할 수 없다

**실전 연결**

실전 딥러닝에서는 backpropagation이 gradient를 계산하고, optimizer가 그 gradient를 사용해 parameter를 update합니다. SGD, Momentum, Adam 같은 optimizer도 기본적으로는 gradient 정보를 이용해 step을 정하는 방식입니다. LLM 학습에서도 attention weight, embedding, projection matrix 같은 수많은 parameter가 이런 update rule 계열로 조금씩 바뀝니다. 즉 gradient와 step size는 “모델이 오답에서 정답 쪽으로 조금씩 이동하게 만드는 엔진”이라고 보면 됩니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-04-27-day05.md
