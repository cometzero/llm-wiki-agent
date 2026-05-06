---
title: "AI/ML Learning Review Day 14 (2026-05-06)"
type: source
tags: [ai-ml-learning, review]
date: 2026-05-06
lesson_source_file: /home/ubuntu/work/ai/learning/logs/2026-05-06-day14.md
follow_up_answer_file: /home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-06_09-31-07.md
---

# AI/ML Learning Review Day 14 (2026-05-06)

이 원본 문서는 당일 AI/ML 학습 lesson과, 가능한 경우 10분 뒤 생성된 복습 질문 정답을 함께 보존하기 위해 동기화되었습니다.

## Lesson Source

- Source file: `/home/ubuntu/work/ai/learning/logs/2026-05-06-day14.md`
- Completed date: `2026-05-06`
- Program: AI/ML Fundamentals Daily Learning

---

# Day 14 - AI/ML 기초 학습

- Date: 2026-05-06
- Progress: 14/30
- Level: beginner-intermediate
- Milestone: 신경망과 표현학습
- Milestone goal: 딥러닝이 다층 표현을 학습한다는 의미를 이해한다.

## Today's 3 concepts

1. 순전파와 계산 흐름
2. 역전파와 gradient propagation
3. 파라미터, 가중치, 편향

---

## 1. 순전파와 계산 흐름

### 한 줄 직관

순전파(forward pass)는 입력 데이터가 신경망 안을 앞에서 뒤로 지나가며, 최종 예측값으로 바뀌는 계산 과정이다.

예를 들어 사진 한 장이 모델에 들어가면 처음에는 단순한 숫자 묶음이다. 이 숫자들이 여러 layer를 지나면서 “선이 있는가?”, “눈처럼 보이는가?”, “고양이 얼굴인가?” 같은 더 의미 있는 표현으로 바뀌고, 마지막에는 “고양이일 확률 0.87” 같은 출력이 나온다. 이 전체 흐름이 forward pass다.

### 개념 정의

순전파(forward pass)는 모델이 입력 `x`를 받아서 각 layer의 계산을 차례대로 적용하고, 최종 출력 `ŷ` 또는 loss 계산에 필요한 예측값을 만드는 과정이다.

가장 단순한 layer 하나를 생각하면 보통 다음 흐름을 가진다.

1. 입력값이 들어온다.
2. 입력값에 weight를 곱하고 bias를 더한다.
3. 필요하면 activation function을 적용한다.
4. 다음 layer로 결과를 보낸다.

딥러닝에서 흔히 보는 기본 계산은 다음과 같다.

```text
z = Wx + b
a = activation(z)
```

여기서 `Wx + b`는 affine transform이라고 부른다. 완전히 어려운 말처럼 보이지만, 쉽게 말하면 “입력에 weight를 곱해서 섞고, bias를 더해서 위치를 조정하는 계산”이다.

`a`는 그 layer의 출력(layer output)이다. 이 출력은 다음 layer의 입력이 된다.

### 왜 이런 개념이 필요한가

모델이 학습하기 전에 먼저 해야 하는 일은 “현재 파라미터로 예측을 해 보는 것”이다. 예측을 해야 정답과 얼마나 다른지 알 수 있고, 그래야 loss를 계산할 수 있다.

즉, 순전파는 학습의 출발점이다.

```text
입력 데이터 → 모델의 예측 → 정답과 비교 → loss 계산
```

이 중에서 “입력 데이터 → 모델의 예측” 부분이 forward pass다.

LLM에서도 마찬가지다. 사용자가 “오늘 날씨가”라고 입력하면 모델은 token embedding, attention layer, feed-forward layer 등을 지나며 다음 token의 확률을 계산한다. 예를 들어 다음 token 후보가 다음처럼 나올 수 있다.

```text
"좋다" 0.32
"흐리다" 0.21
"어떨까" 0.10
```

이 확률을 만들어 내는 계산 흐름도 forward pass다.

### 아주 쉬운 예시

입력이 하나뿐인 아주 작은 모델을 생각해 보자.

```text
입력 x = 2
weight w = 3
bias b = 1
출력 y = wx + b
```

계산하면 다음과 같다.

```text
y = 3 × 2 + 1 = 7
```

이 모델은 `2`라는 입력을 받아 `7`이라는 출력을 냈다. 이것이 가장 작은 형태의 forward pass다.

이번에는 layer가 두 개라고 해 보자.

```text
1번째 layer: h = 2x + 1
2번째 layer: y = 3h - 2
입력 x = 4
```

계산 흐름은 다음과 같다.

```text
h = 2 × 4 + 1 = 9
y = 3 × 9 - 2 = 25
```

입력 `4`가 첫 layer에서 `9`라는 hidden value로 바뀌고, 두 번째 layer에서 최종 출력 `25`가 되었다. 신경망은 이런 작은 계산을 매우 많이 쌓은 구조라고 볼 수 있다.

### 개념 구조와 핵심 포인트

순전파를 이해할 때 중요한 구조는 다음과 같다.

```text
input → layer 1 output → layer 2 output → ... → final output → loss
```

핵심 포인트는 세 가지다.

1. **각 layer는 입력을 새로운 표현으로 바꾼다.**  
   첫 layer는 원시 입력에 가까운 특징을 만들고, 깊은 layer는 더 추상적인 특징을 만든다.

2. **각 layer output은 다음 layer의 input이 된다.**  
   그래서 앞 layer의 계산이 뒤 layer 전체에 영향을 준다.

3. **최종 출력은 loss 계산에 사용된다.**  
   학습에서는 예측이 정답과 얼마나 다른지 loss로 측정한다. forward pass 없이는 loss도 없다.

여기서 중요한 관점은 “딥러닝은 한 번에 답을 찍는 기계가 아니라, 작은 변환을 여러 번 이어 붙여 답을 만드는 계산 흐름”이라는 점이다.

### 핵심 수학 포인트

가장 기본 형태는 다음이다.

```text
z = Wx + b
```

- `x`: 입력 vector
- `W`: weight matrix
- `b`: bias vector
- `z`: activation function을 적용하기 전의 값

예를 들어 입력이 두 개라고 하자.

```text
x = [2, 1]
W = [3, 4]
b = 1
```

그러면 출력 하나는 다음처럼 계산된다.

```text
z = 3×2 + 4×1 + 1 = 11
```

이 계산은 “입력 feature 두 개를 weight로 가중합(weighted sum)한 뒤 bias를 더한다”라고 볼 수 있다.

여기에 activation function을 붙이면 layer output이 된다.

```text
a = activation(z)
```

activation function은 모델이 단순한 직선 계산만 하지 않고, 더 복잡한 패턴을 표현하게 해 준다. 예를 들어 ReLU는 `z`가 음수이면 0으로 만들고, 양수이면 그대로 둔다.

```text
ReLU(-3) = 0
ReLU(5) = 5
```

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **forward pass**: 입력이 모델을 앞에서 뒤로 통과하며 예측값을 만드는 과정.
- **affine transform**: `Wx + b` 형태의 계산. 입력을 weight로 섞고 bias로 이동시키는 변환.
- **layer output**: 어떤 layer가 계산을 끝낸 뒤 다음 layer로 넘기는 값.
- **activation function**: affine transform 결과에 비선형성을 추가하는 함수. ReLU, sigmoid, GELU 등이 있다.
- **hidden state**: 중간 layer 안에서 만들어진 내부 표현. LLM에서는 각 token이 문맥 정보를 담은 vector로 바뀐 상태를 의미할 때가 많다.

### AI에서 어디에 쓰이는가

순전파는 거의 모든 AI 모델의 기본 실행 방식이다.

- 이미지 분류 모델은 픽셀 값을 forward pass로 처리해 class 확률을 만든다.
- 추천 모델은 사용자와 상품 embedding을 계산해 클릭 가능성을 예측한다.
- LLM은 token sequence를 여러 transformer layer에 통과시켜 다음 token 확률을 만든다.
- 학습 중에는 forward pass로 loss를 만들고, 추론(inference) 중에는 forward pass로 실제 답변이나 예측을 만든다.

실무에서 tensor shape이 중요한 이유도 forward pass 때문이다. 예를 들어 어떤 layer가 `[batch, features]` 모양을 기대하는데 `[features]`만 들어오면 계산 흐름이 끊긴다. 따라서 forward pass를 이해하면 모델이 “어떤 모양의 데이터를 받아서 어떤 모양으로 내보내는지” 추적할 수 있다.

### 헷갈리기 쉬운 포인트

- forward pass는 학습 자체가 아니라 **예측을 만드는 계산**이다. 학습은 forward pass 이후 loss를 계산하고, backward pass와 optimizer update까지 이어질 때 일어난다.
- `Wx + b`만으로 끝나는 layer도 있지만, 많은 신경망 layer는 activation function, normalization, dropout 같은 추가 연산을 포함한다.
- “깊은 layer일수록 무조건 사람이 이해하기 쉬운 개념을 담는다”라고 생각하면 안 된다. 다만 일반적으로 더 복합적이고 문맥적인 표현을 담는 경향이 있다.

---

## 2. 역전파와 gradient propagation

### 한 줄 직관

역전파(backpropagation)는 모델이 틀린 정도를 보고, “어느 weight가 얼마나 책임이 있는지”를 뒤에서 앞으로 계산해 알려 주는 과정이다.

쉽게 말해 시험 문제를 틀렸을 때 “마지막 계산에서 실수했는지, 중간 공식 선택이 틀렸는지, 처음 숫자를 잘못 넣었는지” 거꾸로 추적하는 것과 비슷하다.

### 개념 정의

역전파(backpropagation)는 loss가 각 parameter에 대해 얼마나 민감하게 변하는지, 즉 gradient를 효율적으로 계산하는 알고리즘이다.

학습 흐름 전체에서 보면 다음 위치에 있다.

```text
forward pass → loss 계산 → backpropagation → optimizer update
```

forward pass는 앞에서 뒤로 예측을 만든다. 반대로 backpropagation은 loss에서 시작해 뒤 layer부터 앞 layer 방향으로 gradient를 전달한다. 그래서 gradient propagation이라는 표현을 쓴다.

여기서 gradient는 “parameter를 조금 바꾸면 loss가 어느 방향으로 얼마나 바뀌는가”를 알려 주는 신호다.

### 왜 이런 개념이 필요한가

신경망에는 parameter가 매우 많다. 작은 모델도 수천 개, LLM은 수십억 개 이상의 parameter를 가진다. 각 parameter를 하나씩 바꿔 보면서 loss가 줄어드는지 확인하면 너무 오래 걸린다.

역전파는 이 문제를 해결한다. forward pass에서 만들어진 계산 관계를 이용해, loss가 각 parameter에 미치는 영향을 효율적으로 계산한다.

중요한 이유는 단순하다.

```text
gradient가 있어야 optimizer가 parameter를 어느 방향으로 수정할지 안다.
```

예를 들어 loss가 커졌을 때 weight `w`를 줄여야 하는지, 키워야 하는지 모르면 학습할 수 없다. 역전파는 “이 weight는 loss를 키우는 쪽으로 작용했으니 조금 줄이자” 같은 정보를 제공한다.

### 아주 쉬운 예시

아주 작은 모델을 보자.

```text
예측 y = w × x
입력 x = 2
정답 target = 10
현재 weight w = 3
```

forward pass를 하면 다음과 같다.

```text
y = 3 × 2 = 6
```

정답은 10인데 예측은 6이다. 너무 작다. 그러면 `w`를 키우면 예측이 커질까?

`w = 4`로 바꾸면:

```text
y = 4 × 2 = 8
```

정답에 가까워졌다. 따라서 이 상황에서는 weight를 키우는 방향이 맞다.

역전파는 이런 판단을 감으로 하지 않고 gradient로 계산한다. loss를 간단히 다음처럼 두자.

```text
loss = (y - target)^2
```

현재는:

```text
y = 6
loss = (6 - 10)^2 = 16
```

이때 gradient는 “w를 조금 키우면 loss가 줄어드는지 늘어나는지”를 알려 준다. 계산 결과는 음수 방향의 신호가 나오고, optimizer는 보통 `w = w - learning_rate × gradient`로 업데이트한다. gradient가 음수이면 빼는 과정에서 `w`는 증가한다. 그래서 예측이 정답에 가까워진다.

숫자로 작게 보면:

```text
현재 w = 3
gradient = -16
learning_rate = 0.1
새 w = 3 - 0.1 × (-16) = 4.6
```

weight가 3에서 4.6으로 커졌다. 예측은 다음처럼 바뀐다.

```text
새 예측 = 4.6 × 2 = 9.2
```

정답 10에 더 가까워졌다.

### 개념 구조와 핵심 포인트

역전파의 핵심 구조는 다음과 같다.

```text
loss
 ↓
마지막 layer의 gradient
 ↓
중간 layer의 gradient
 ↓
첫 layer의 gradient
```

중요한 포인트는 네 가지다.

1. **loss에서 시작한다.**  
   모델이 얼마나 틀렸는지 알아야 무엇을 고칠지 알 수 있다.

2. **뒤 layer부터 앞 layer로 계산한다.**  
   마지막 layer가 예측에 직접 영향을 주고, 앞 layer는 중간 표현을 통해 간접적으로 영향을 준다.

3. **chain rule을 사용한다.**  
   여러 계산이 이어져 있을 때 전체 영향도를 작은 영향도의 곱으로 나누어 계산한다.

4. **credit assignment 문제를 해결한다.**  
   credit assignment는 “결과가 좋거나 나빴을 때, 내부의 많은 parameter 중 누구에게 얼마나 책임을 줄 것인가”의 문제다.

예를 들어 축구 경기에서 골을 먹혔다고 하자. 골키퍼만 책임이 있는 것이 아닐 수 있다. 수비 위치, 미드필더의 패스 실수, 전술 선택도 영향을 줬을 수 있다. 역전파는 신경망 안에서 이런 책임 배분을 수학적으로 해 주는 과정이다.

### 핵심 수학 포인트

가장 쉬운 1D 예로 시작하자.

```text
y = w × x
loss = (y - target)^2
```

우리가 알고 싶은 것은 다음이다.

```text
w를 조금 바꾸면 loss가 얼마나 바뀌는가?
```

이것을 `d loss / d w`라고 쓴다. 어려워 보이지만 의미는 “loss의 w에 대한 변화율”이다.

계산이 두 단계로 이어져 있다.

```text
w → y → loss
```

그래서 전체 영향은 다음처럼 나눠서 생각할 수 있다.

```text
w가 y에 주는 영향 × y가 loss에 주는 영향
```

이것이 chain rule의 직관이다.

신경망에서는 이 구조가 훨씬 길어진다.

```text
W1 → hidden state → W2 → output → loss
```

역전파는 이 긴 흐름을 따라 gradient를 뒤에서 앞으로 전달한다. 그래서 gradient flow가 좋아야 학습이 잘 된다.

만약 gradient가 앞 layer로 갈수록 너무 작아지면 vanishing gradient 문제가 생긴다. 반대로 너무 커지면 exploding gradient 문제가 생긴다. Transformer, residual connection, normalization 같은 구조는 gradient flow를 안정적으로 만드는 데도 중요하다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **backpropagation**: loss에서 시작해 각 parameter의 gradient를 뒤에서 앞으로 계산하는 알고리즘.
- **gradient flow**: gradient가 layer들을 거쳐 전달되는 흐름. 너무 약해지거나 커지면 학습이 어려워진다.
- **gradient propagation**: gradient가 computational path를 따라 전달되는 과정.
- **credit assignment**: 최종 loss에 대해 각 parameter나 layer가 얼마나 책임이 있는지 배분하는 문제.
- **chain rule**: 여러 함수가 이어져 있을 때 전체 변화율을 단계별 변화율의 곱으로 계산하는 규칙.
- **optimizer**: gradient를 이용해 parameter를 실제로 업데이트하는 방법. SGD, Adam 등이 있다.

### AI에서 어디에 쓰이는가

역전파는 딥러닝 학습의 핵심이다.

- CNN은 이미지 분류 loss를 줄이기 위해 filter weight를 backpropagation으로 학습한다.
- Transformer는 다음 token 예측 loss를 줄이기 위해 attention weight, feed-forward layer weight, embedding matrix를 업데이트한다.
- embedding 모델은 비슷한 문장은 가까워지고 다른 문장은 멀어지도록 gradient를 통해 vector 표현을 조정한다.
- fine-tuning에서는 이미 학습된 모델의 parameter를 특정 데이터셋에 맞게 조금씩 수정한다.

LLM 학습을 예로 들면, 모델이 다음 token을 틀리게 예측했을 때 loss가 생긴다. backpropagation은 이 loss를 attention layer, feed-forward layer, embedding layer까지 전달한다. 그러면 optimizer는 다음번에 더 알맞은 token 확률이 나오도록 parameter를 바꾼다.

### 헷갈리기 쉬운 포인트

- backpropagation 자체가 parameter를 업데이트하는 것은 아니다. gradient를 계산하는 과정이다. 실제 업데이트는 optimizer가 한다.
- gradient는 “정답”이 아니라 “현재 위치에서 loss를 줄이기 위한 국소적인 방향 신호”다. 그래서 learning rate, optimizer, 데이터 품질이 함께 중요하다.
- gradient가 있다고 항상 학습이 잘 되는 것은 아니다. gradient가 너무 작거나 크거나, loss landscape가 복잡하거나, 데이터가 부족하면 학습이 어려울 수 있다.
- forward pass와 backward pass는 서로 반대 방향이지만, 완전히 별개의 일이 아니다. backward pass는 forward pass에서 만들어진 중간값들을 이용한다.

---

## 3. 파라미터, 가중치, 편향

### 한 줄 직관

파라미터(parameter)는 모델이 학습하면서 조정하는 숫자이고, weight와 bias는 그 대표적인 종류다.

사람이 요리할 때 소금 양, 불 세기, 조리 시간을 조절하듯이, 모델은 weight와 bias라는 숫자를 조절하면서 더 좋은 예측을 하도록 배운다.

### 개념 정의

parameter는 모델 내부에 저장되어 있고 학습 중에 바뀌는 값이다. 신경망에서는 보통 weight와 bias가 가장 기본적인 parameter다.

- **weight**는 입력 feature가 출력에 얼마나 강하게 영향을 주는지 정하는 값이다.
- **bias**는 입력과 별개로 출력의 기본 위치를 조정하는 값이다.

가장 단순한 선형 모델은 다음과 같다.

```text
y = wx + b
```

여기서 `w`와 `b`가 parameter다. 학습은 좋은 `w`와 `b`를 찾는 과정이라고 볼 수 있다.

신경망이 커지면 `w`는 하나의 숫자가 아니라 matrix가 되고, `b`도 vector가 된다. LLM에서는 embedding matrix, attention projection matrix, feed-forward layer matrix 등이 모두 parameter다.

### 왜 이런 개념이 필요한가

모델이 데이터를 보고 배운다는 말은, 사실 parameter 값을 데이터에 맞게 바꾼다는 뜻이다.

처음 모델은 보통 random initialization으로 시작한다. 즉 weight와 bias가 처음에는 거의 무작위 값이다. 그래서 처음 예측은 엉망일 수 있다. 하지만 많은 데이터를 보면서 loss를 계산하고 gradient를 이용해 parameter를 조금씩 바꾸면, 점점 더 좋은 예측을 하게 된다.

중요한 관점은 다음이다.

```text
모델 구조는 계산의 틀이고, parameter는 그 틀 안에서 학습되는 내용이다.
```

예를 들어 같은 Transformer 구조라도 parameter 값이 다르면 번역 모델이 될 수도 있고, 코딩 모델이 될 수도 있고, 대화 모델이 될 수도 있다.

### 아주 쉬운 예시

집값을 예측하는 아주 작은 모델을 생각해 보자.

```text
예측 집값 = w × 집 크기 + b
```

집 크기를 아주 단순하게 `x = 10`이라고 하고, 현재 parameter가 다음과 같다고 하자.

```text
w = 2
b = 5
```

그러면 예측은 다음과 같다.

```text
y = 2 × 10 + 5 = 25
```

그런데 실제 집값이 30이라면 예측이 5만큼 낮다. 모델은 학습을 통해 `w`를 조금 키우거나 `b`를 키워서 예측을 올릴 수 있다.

예를 들어 `w = 2.4`, `b = 6`이 되면:

```text
y = 2.4 × 10 + 6 = 30
```

정답에 맞아진다.

여기서 `w`는 “집 크기가 예측에 주는 영향의 세기”이고, `b`는 “집 크기가 0이어도 기본적으로 더해지는 기준값”처럼 볼 수 있다.

### 개념 구조와 핵심 포인트

parameter를 이해할 때는 다음 구분이 중요하다.

```text
모델이 학습으로 바꾸는 값: parameter
사용자가 정하거나 실험 설정으로 두는 값: hyperparameter
```

예를 들어 weight와 bias는 parameter다. 반면 learning rate, batch size, layer 수, hidden dimension 같은 것은 보통 hyperparameter다.

weight와 bias의 역할은 다음처럼 볼 수 있다.

1. **weight는 방향과 중요도를 정한다.**  
   입력 feature 중 어떤 것을 더 중요하게 볼지 정한다.

2. **bias는 기준점을 이동시킨다.**  
   입력이 0에 가까워도 출력이 어느 정도 값을 가질 수 있게 한다.

3. **parameter space는 가능한 parameter 조합 전체 공간이다.**  
   `w`와 `b`가 하나씩만 있으면 parameter space는 2차원 평면처럼 생각할 수 있다. 신경망 parameter가 1억 개라면 1억 차원의 매우 큰 공간에서 좋은 위치를 찾는 셈이다.

4. **학습은 parameter space에서 loss가 낮은 지점을 찾는 과정이다.**  
   optimizer는 gradient를 따라 조금씩 이동하며 더 좋은 parameter 조합을 찾는다.

### 핵심 수학 포인트

가장 작은 모델은 다음이다.

```text
y = wx + b
```

여기서 `w`가 바뀌면 선의 기울기가 바뀐다. `b`가 바뀌면 선이 위아래로 이동한다.

작은 숫자로 보자.

```text
y = 2x + 1
```

입력 `x = 3`이면:

```text
y = 2×3 + 1 = 7
```

만약 weight가 4로 커지면:

```text
y = 4×3 + 1 = 13
```

같은 입력인데 출력이 훨씬 커졌다. 즉 weight는 입력의 영향력을 조절한다.

이번에는 bias만 바꿔 보자.

```text
y = 2x + 5
x = 3
```

그러면:

```text
y = 2×3 + 5 = 11
```

기울기는 그대로지만 전체 출력이 위로 올라갔다. 즉 bias는 기준선을 이동시킨다.

다변수에서는 weight가 vector나 matrix가 된다.

```text
z = W x + b
```

예를 들어 입력 feature가 `[공부시간, 수면시간]` 두 개라면, weight는 각각의 feature가 예측에 얼마나 영향을 주는지 나타낸다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **parameter**: 학습 중 optimizer가 업데이트하는 모델 내부 숫자.
- **weight**: 입력 feature를 얼마나 강하게 반영할지 정하는 parameter.
- **bias**: 출력의 기준 위치를 조정하는 parameter.
- **parameter space**: 가능한 모든 parameter 조합이 이루는 공간.
- **trainable parameter**: gradient를 통해 학습되는 parameter.
- **frozen parameter**: fine-tuning 등에서 일부러 업데이트하지 않도록 고정한 parameter.
- **hyperparameter**: 학습으로 자동 업데이트되지 않고 사람이 정하는 설정값. learning rate, batch size 등이 있다.

### AI에서 어디에 쓰이는가

parameter는 모델의 “기억”과 “능력”이 저장되는 곳이라고 볼 수 있다.

- embedding matrix의 parameter는 token이나 item을 vector로 바꾸는 방법을 담는다.
- attention layer의 weight는 어떤 token 정보에서 query, key, value를 만들지 정한다.
- feed-forward layer의 weight와 bias는 hidden state를 더 풍부한 표현으로 변환한다.
- classifier head의 weight는 hidden state를 class 확률로 바꾼다.

LLM이 문법, 사실 지식, 코딩 패턴, 문체를 어느 정도 흉내 낼 수 있는 이유도 학습 과정에서 parameter에 통계적 패턴이 저장되었기 때문이다. 물론 parameter가 데이터베이스처럼 문장을 그대로 저장한다는 뜻은 아니다. 더 정확히는 많은 예시에서 반복되는 관계와 패턴이 숫자 형태로 압축되어 있는 것이다.

### 헷갈리기 쉬운 포인트

- parameter와 hyperparameter를 혼동하기 쉽다. weight와 bias는 학습으로 바뀌는 parameter이고, learning rate는 사람이 정하는 hyperparameter다.
- bias는 “편견”이라는 일상적 의미로 이해하면 혼란스럽다. 여기서는 출력의 기준점을 이동시키는 숫자다.
- parameter 수가 많다고 항상 좋은 모델은 아니다. 데이터, 구조, 학습 방법, regularization, 계산 자원도 함께 중요하다.
- 모델이 배운다는 말은 사람이 규칙을 직접 넣는다는 뜻이 아니라, parameter가 loss를 줄이는 방향으로 조정된다는 뜻이다.

---

## 복습 질문 3개

1. forward pass에서 `z = Wx + b` 계산이 하는 역할은 무엇이고, layer output은 다음 layer와 어떤 관계를 가지나요?
2. backpropagation은 parameter를 직접 업데이트하는 과정인가요, 아니면 gradient를 계산하는 과정인가요? optimizer와의 차이를 설명해 보세요.
3. `y = wx + b`에서 weight와 bias가 각각 바뀌면 출력은 어떻게 달라지나요? 작은 숫자 예시로 설명해 보세요.

## 오늘의 한 줄 요약

딥러닝 학습은 forward pass로 예측과 loss를 만들고, backpropagation으로 각 parameter의 책임을 계산한 뒤, optimizer가 weight와 bias를 조금씩 조정해 더 좋은 표현을 만드는 과정이다.

---

## Follow-up Review Answers

- Answer cron output: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-06_09-31-07.md`

[AI/ML 오늘의 복습 정답 Day 14/30]

오늘은 신경망 학습의 핵심 흐름인 forward pass, backpropagation, parameter를 차근차근 복습해 볼게요.

### 1. forward pass에서 `z = Wx + b` 계산이 하는 역할은 무엇이고, layer output은 다음 layer와 어떤 관계를 가지나요?

**정답**

`z = Wx + b`는 한 layer가 입력 `x`를 받아서 weight `W`로 섞고, bias `b`로 기준 위치를 조정하는 계산입니다.

이 계산을 affine transform이라고 부릅니다.

그 뒤 activation function을 적용하면 보통 그 layer의 출력, 즉 layer output이 됩니다.

이 layer output은 다음 layer의 input으로 들어갑니다.

즉 흐름은 이렇게 이어집니다.

```text
input → layer 1 output → layer 2 input → layer 2 output → ... → final output
```

**설명**

forward pass는 입력 데이터가 모델 안을 앞에서 뒤로 통과하면서 예측값으로 바뀌는 과정입니다.

예를 들어 이미지 모델에 고양이 사진이 들어간다고 해 볼게요. 처음 입력은 픽셀 숫자들입니다. 첫 layer는 단순한 선이나 색 변화 같은 특징을 만들 수 있고, 다음 layer는 눈, 귀, 털 같은 더 복잡한 특징을 만들 수 있습니다. 더 깊은 layer에서는 “고양이 얼굴 같다”는 식의 표현이 만들어질 수 있습니다.

이때 각 layer는 그냥 데이터를 그대로 넘기는 것이 아니라, 자기 parameter인 weight와 bias를 사용해서 입력을 새롭게 변환합니다.

`z = Wx + b`에서:

- `x`는 현재 layer에 들어온 입력입니다.
- `W`는 입력 feature들을 얼마나 중요하게 섞을지 정하는 weight입니다.
- `b`는 결과값의 기준 위치를 조정하는 bias입니다.
- `z`는 activation function을 적용하기 전의 중간값입니다.

그 다음 ReLU, sigmoid, GELU 같은 activation function을 적용하면 layer output이 됩니다. 이 output은 다음 layer 입장에서는 다시 input이 됩니다.

그래서 신경망은 “한 번에 답을 찍는 구조”라기보다, 작은 변환을 여러 번 이어 붙여서 점점 더 유용한 표현을 만드는 계산 흐름이라고 이해하면 좋습니다.

**예시**

아주 작은 숫자 예시로 보겠습니다.

```text
입력 x = 2
weight W = 3
bias b = 1
z = Wx + b
```

계산하면:

```text
z = 3 × 2 + 1 = 7
```

여기서 activation function이 없다고 단순화하면, 이 layer의 output은 `7`입니다.

만약 다음 layer가 다음과 같다면:

```text
다음 layer: y = 2 × z + 1
```

이전 layer output인 `7`이 다음 layer input으로 들어갑니다.

```text
y = 2 × 7 + 1 = 15
```

즉 첫 layer의 output `7`은 다음 layer가 계산을 시작하는 재료가 됩니다.

**실전 연결**

실제 딥러닝 구현에서는 forward pass를 이해해야 tensor shape을 추적할 수 있습니다. 예를 들어 어떤 layer가 `[batch, features]` 형태의 입력을 기대하는데 다른 모양의 tensor가 들어오면 에러가 납니다. LLM에서도 token embedding이 여러 Transformer layer를 지나며 hidden state로 바뀌고, 마지막에는 다음 token 확률이 나옵니다. 이 전체 계산 흐름이 forward pass입니다.

### 2. backpropagation은 parameter를 직접 업데이트하는 과정인가요, 아니면 gradient를 계산하는 과정인가요? optimizer와의 차이를 설명해 보세요.

**정답**

backpropagation은 parameter를 직접 업데이트하는 과정이 아니라, 각 parameter에 대한 gradient를 계산하는 과정입니다.

실제로 parameter 값을 바꾸는 것은 optimizer입니다.

정리하면 다음과 같습니다.

```text
forward pass → loss 계산 → backpropagation으로 gradient 계산 → optimizer가 parameter 업데이트
```

backpropagation은 “어느 parameter가 loss에 얼마나 영향을 주었는가”를 계산합니다.

optimizer는 그 gradient를 보고 “parameter를 어느 방향으로 얼마나 움직일지” 결정해 실제로 값을 바꿉니다.

**설명**

신경망 학습의 목표는 loss function 값을 줄이는 것입니다. loss function은 모델의 예측이 정답과 얼마나 다른지 나타내는 함수입니다.

예를 들어 모델이 정답을 `10`이라고 맞혀야 하는데 `6`이라고 예측했다면 loss가 생깁니다. 이제 모델은 어떤 weight와 bias를 어떻게 바꿔야 다음에는 더 잘 맞힐지 알아야 합니다.

여기서 backpropagation이 등장합니다.

backpropagation은 loss에서 시작해서 뒤쪽 layer부터 앞쪽 layer 방향으로 gradient를 계산합니다. gradient는 “parameter를 조금 바꾸면 loss가 어느 방향으로 얼마나 변하는가”를 알려주는 신호입니다.

하지만 backpropagation은 여기까지만 합니다.

즉 “이 weight는 loss를 줄이려면 조금 키우는 게 좋다”, “저 bias는 조금 줄이는 게 좋다” 같은 방향 정보를 계산합니다. 실제로 값을 바꾸는 일은 optimizer가 합니다.

대표적인 optimizer에는 SGD, Adam 등이 있습니다.

예를 들어 optimizer는 보통 이런 형태로 parameter를 업데이트합니다.

```text
새 parameter = 기존 parameter - learning_rate × gradient
```

여기서 learning rate는 한 번에 얼마나 크게 움직일지 정하는 값입니다. learning rate는 학습으로 자동으로 바뀌는 parameter가 아니라, 사람이 정하는 hyperparameter입니다.

**예시**

아주 작은 모델을 보겠습니다.

```text
예측 y = w × x
입력 x = 2
현재 weight w = 3
정답 target = 10
```

forward pass를 하면:

```text
y = 3 × 2 = 6
```

정답은 `10`인데 예측은 `6`입니다. 예측이 너무 작습니다. 이 경우에는 `w`를 키우면 예측이 커집니다.

backpropagation은 이 상황에서 gradient를 계산합니다. 예를 들어 gradient가 `-16`이라고 해 보겠습니다.

```text
현재 w = 3
gradient = -16
learning_rate = 0.1
```

optimizer가 업데이트하면:

```text
새 w = 3 - 0.1 × (-16)
새 w = 4.6
```

weight가 `3`에서 `4.6`으로 커졌습니다.

새 예측은:

```text
y = 4.6 × 2 = 9.2
```

정답 `10`에 더 가까워졌습니다.

여기서 역할을 나누면:

- backpropagation: gradient `-16`을 계산
- optimizer: gradient를 이용해 `w`를 `3`에서 `4.6`으로 변경

입니다.

**실전 연결**

LLM 학습에서도 같은 일이 일어납니다. 모델이 다음 token을 틀리게 예측하면 loss가 생깁니다. backpropagation은 그 loss가 embedding layer, attention layer, feed-forward layer의 각 parameter에 얼마나 책임이 있는지 계산합니다. 그 다음 Adam 같은 optimizer가 parameter를 조금씩 업데이트합니다. fine-tuning에서도 핵심은 같습니다. 이미 학습된 parameter를 특정 데이터에 맞게 gradient와 optimizer로 조정하는 과정입니다.

### 3. `y = wx + b`에서 weight와 bias가 각각 바뀌면 출력은 어떻게 달라지나요? 작은 숫자 예시로 설명해 보세요.

**정답**

`y = wx + b`에서 weight `w`가 바뀌면 입력 `x`가 출력에 미치는 영향의 세기가 바뀝니다.

bias `b`가 바뀌면 입력과 별개로 출력의 기본 기준값이 위아래로 이동합니다.

쉽게 말하면:

- weight는 입력을 얼마나 강하게 반영할지 정합니다.
- bias는 전체 출력의 기준 위치를 조정합니다.

**설명**

`y = wx + b`는 가장 단순한 선형 모델입니다.

여기서 `w`와 `b`는 parameter입니다. parameter는 모델이 학습하면서 바꾸는 내부 숫자입니다.

weight `w`는 입력 `x` 앞에 곱해지는 값입니다. 그래서 `w`가 커지면 같은 입력이라도 출력이 더 크게 변합니다. 반대로 `w`가 작아지면 입력이 출력에 주는 영향이 약해집니다.

bias `b`는 마지막에 더해지는 값입니다. 입력 `x`가 어떤 값이든, 전체 출력에 일정하게 더해집니다. 그래서 bias는 출력의 기본 위치를 이동시키는 역할을 합니다.

비유하면 weight는 “입력의 볼륨 조절기”에 가깝고, bias는 “기본 시작점 조절기”에 가깝습니다.

집값 예측을 생각해 볼 수 있습니다.

```text
예측 집값 = w × 집 크기 + b
```

여기서 weight는 집 크기가 집값에 얼마나 큰 영향을 주는지 나타냅니다. bias는 집 크기 외에도 기본적으로 반영되는 기준 가격처럼 생각할 수 있습니다.

**예시**

먼저 기본 모델을 보겠습니다.

```text
y = 2x + 1
x = 3
```

계산하면:

```text
y = 2 × 3 + 1 = 7
```

이번에는 weight만 바꿔 보겠습니다.

```text
y = 4x + 1
x = 3
```

계산하면:

```text
y = 4 × 3 + 1 = 13
```

입력 `x = 3`은 그대로인데 출력이 `7`에서 `13`으로 커졌습니다. weight가 커졌기 때문에 입력의 영향력이 더 강해진 것입니다.

이번에는 bias만 바꿔 보겠습니다.

```text
y = 2x + 5
x = 3
```

계산하면:

```text
y = 2 × 3 + 5 = 11
```

weight는 여전히 `2`라서 입력을 반영하는 세기는 그대로입니다. 하지만 bias가 `1`에서 `5`로 커졌기 때문에 전체 출력이 위로 올라갔습니다.

정리하면:

```text
기본: y = 2×3 + 1 = 7
weight 변경: y = 4×3 + 1 = 13
bias 변경: y = 2×3 + 5 = 11
```

weight는 입력의 영향력을 바꾸고, bias는 출력의 기준점을 이동시킵니다.

**실전 연결**

신경망에서는 weight와 bias가 하나의 숫자가 아니라 matrix와 vector 형태로 많이 존재합니다. LLM에서는 embedding matrix, attention projection matrix, feed-forward layer의 weight와 bias가 모두 parameter입니다. 모델이 학습한다는 것은 결국 이 많은 parameter들이 loss를 줄이는 방향으로 조금씩 조정된다는 뜻입니다. 그래서 weight와 bias를 이해하면 “AI가 데이터를 보고 배운다”는 말을 더 구체적으로 이해할 수 있습니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-06-day14.md
