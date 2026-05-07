---
title: "AI/ML Learning Review Day 15 (2026-05-07)"
type: source
tags: [ai-ml-learning, review]
date: 2026-05-07
lesson_source_file: /home/ubuntu/work/ai/learning/logs/2026-05-07-day15.md
follow_up_answer_file: /home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-07_09-26-24.md
---

# AI/ML Learning Review Day 15 (2026-05-07)

이 원본 문서는 당일 AI/ML 학습 lesson과, 가능한 경우 10분 뒤 생성된 복습 질문 정답을 함께 보존하기 위해 동기화되었습니다.

## Lesson Source

- Source file: `/home/ubuntu/work/ai/learning/logs/2026-05-07-day15.md`
- Completed date: `2026-05-07`
- Program: AI/ML Fundamentals Daily Learning

---

# Day 15 - AI/ML 기초 학습

- Date: 2026-05-07
- Progress: 15/30
- Level: beginner-intermediate
- Milestone: 신경망과 표현학습
- Milestone goal: 딥러닝이 다층 표현을 학습한다는 의미를 이해한다.

## Today's 3 concepts

1. 표현학습과 latent representation
2. 초기화와 학습 안정성
3. vanishing/exploding gradient

---

## 1. 표현학습과 latent representation

### 한 줄 직관

표현학습(representation learning)은 모델이 원본 데이터를 그대로 외우는 것이 아니라, 문제를 풀기 좋은 숫자 표현을 스스로 만들어 가는 과정이다.

사람이 강아지 사진을 볼 때 픽셀 하나하나를 따로 외우지 않고 “눈이 있다”, “귀가 접혀 있다”, “털 질감이 있다”, “전체 모양이 강아지 같다”처럼 중요한 특징을 잡아내는 것과 비슷하다. 딥러닝 모델도 입력을 여러 layer에 통과시키면서 점점 더 유용한 내부 표현을 만든다.

### 개념 정의

표현학습(representation learning)은 데이터에서 사람이 직접 정한 feature만 쓰는 대신, 모델이 학습 과정에서 필요한 feature 또는 representation을 자동으로 배우는 방식이다.

여기서 representation은 “데이터를 모델이 이해하고 계산할 수 있게 바꾼 숫자 형태”라고 생각하면 된다. 예를 들어 문장 “고양이가 잔다”는 컴퓨터에게 바로 의미가 통하지 않는다. 그래서 각 단어를 embedding vector로 바꾸고, 여러 layer를 지나며 문장 전체의 의미를 담은 hidden state로 바꾼다. 이 hidden state가 일종의 learned representation이다.

latent representation에서 latent는 “겉으로 직접 보이지 않는”이라는 뜻이다. 즉 latent representation은 입력 데이터 안에 숨어 있는 의미나 구조를 모델 내부의 숫자 공간에 담은 것이다. 사용자는 보통 이 숫자를 직접 보지 않지만, 모델은 그 숫자를 이용해서 분류, 생성, 검색, 번역 같은 일을 한다.

### 왜 이런 개념이 필요한가

전통적인 머신러닝에서는 사람이 feature를 많이 설계했다. 예를 들어 스팸 메일 분류 모델을 만든다면 사람이 다음과 같은 feature를 직접 만들 수 있다.

```text
- '무료'라는 단어가 들어 있는가?
- 느낌표가 몇 개 있는가?
- 링크가 몇 개 있는가?
- 보낸 사람이 처음 보는 주소인가?
```

이 방식은 간단한 문제에는 잘 작동하지만, 이미지, 음성, 자연어처럼 복잡한 데이터에서는 사람이 모든 좋은 feature를 직접 만들기 어렵다. 고양이 사진을 분류하려고 “수염의 곡률”, “귀의 각도”, “눈 주변 패턴”을 전부 손으로 규칙화하는 것은 거의 불가능하다.

딥러닝의 강점은 여기서 나온다. 모델은 입력에서 바로 정답으로 가는 것이 아니라, 중간 layer들을 통해 점점 더 좋은 representation을 만든다.

```text
원본 픽셀 → 선/색 변화 → 작은 모양 → 얼굴 일부 → 고양이 같은 전체 패턴 → 예측
```

LLM도 마찬가지다. 처음에는 token ID라는 단순한 숫자로 시작하지만, embedding layer와 attention layer를 지나면서 “이 단어가 문장에서 어떤 역할을 하는지”, “앞의 문장과 어떤 관계인지”, “다음에 어떤 말이 자연스러운지”를 담은 representation이 만들어진다.

### 아주 쉬운 예시

아주 작은 숫자 예시를 보자. 과일을 구분하는 모델이 있다고 하자. 원본 데이터가 다음 두 숫자라고 해 보자.

```text
사과 A: 단맛 8, 신맛 3
레몬 B: 단맛 2, 신맛 9
```

사람은 이 두 숫자를 보고 “사과는 달고 신맛은 약하다”, “레몬은 덜 달고 시다”라고 이해한다. 모델도 비슷하게 두 숫자를 그대로 쓰는 대신, 내부적으로 다음과 같은 새 표현을 만들 수 있다.

```text
과일 A의 latent representation: [달콤한 정도 0.9, 상큼한 정도 0.3]
과일 B의 latent representation: [달콤한 정도 0.2, 상큼한 정도 0.95]
```

여기서 중요한 점은 “달콤한 정도”, “상큼한 정도”라는 이름을 사람이 꼭 붙여 준 것은 아닐 수 있다는 것이다. 실제 딥러닝 모델의 latent space에서는 각 축이 사람이 보기 좋게 이름 붙여지지 않는 경우가 많다. 그래도 비슷한 데이터는 비슷한 위치에 모이고, 다른 데이터는 멀어지는 식으로 문제를 풀기 좋은 구조가 생긴다.

문장 embedding도 비슷하다.

```text
"강아지가 공원에서 뛴다" → [0.2, 0.8, -0.1, ...]
"개가 밖에서 논다"       → [0.25, 0.75, -0.05, ...]
"주식 시장이 하락했다"   → [-0.6, 0.1, 0.9, ...]
```

첫 두 문장은 의미가 비슷하므로 embedding space에서 가까울 가능성이 크다. 세 번째 문장은 주제가 다르므로 더 멀 가능성이 크다.

### 개념 구조와 핵심 포인트

표현학습을 이해할 때는 다음 구조를 기억하면 좋다.

1. **원본 입력(raw input)**  
   이미지 픽셀, 음성 파형, token ID, 표 데이터처럼 처음 들어오는 데이터다.

2. **feature extraction**  
   모델이 입력에서 유용한 단서(feature)를 뽑아내는 과정이다. 예전에는 사람이 feature extraction을 직접 많이 했지만, 딥러닝에서는 layer들이 이 일을 자동으로 배운다.

3. **hidden representation / latent representation**  
   모델 내부 layer의 출력이다. 입력보다 더 추상적인 의미를 담을 수 있다.

4. **latent space**  
   latent representation들이 놓이는 숫자 공간이다. 비슷한 데이터가 가까운 위치에 모이면 모델이 분류, 검색, 추천을 더 잘할 수 있다.

5. **task output**  
   마지막 layer에서 분류 확률, 다음 token 확률, 생성 이미지, 점수 같은 실제 결과가 나온다.

핵심은 “좋은 representation을 만들면 뒤의 작업이 쉬워진다”는 것이다. 예를 들어 고양이와 강아지를 구분하는 마지막 classifier가 아무리 단순해도, 앞 layer들이 이미 “동물 얼굴 구조”를 잘 표현해 두었다면 분류가 쉬워진다.

### 핵심 수학 포인트

가장 단순하게 보면 representation은 함수의 결과다.

```text
h = f(x)
```

- `x`: 원본 입력
- `f`: 모델의 앞부분 또는 어떤 layer들의 묶음
- `h`: 학습된 representation 또는 hidden state

예를 들어 입력이 2차원 벡터라고 하자.

```text
x = [단맛 8, 신맛 3]
```

모델이 이것을 다음처럼 바꿀 수 있다.

```text
h = [0.9, 0.3, 0.1]
```

여기서 차원이 2에서 3으로 늘어났다. 차원이 늘어난다고 무조건 좋은 것은 아니지만, 모델이 문제를 풀기 쉬운 방향으로 데이터를 다시 배치할 수 있다는 점이 중요하다.

딥러닝에서는 layer가 여러 개라서 다음처럼 볼 수 있다.

```text
h1 = f1(x)
h2 = f2(h1)
h3 = f3(h2)
output = g(h3)
```

각 단계의 `h1`, `h2`, `h3`가 모두 representation이다. 깊은 layer로 갈수록 보통 더 추상적인 정보를 담는다. 이미지 모델에서는 앞 layer가 edge를, 중간 layer가 texture나 부품을, 뒤 layer가 객체 전체를 담는 경향이 있다. LLM에서는 hidden state가 token의 문맥적 의미를 담는다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **representation learning**: 모델이 데이터의 유용한 숫자 표현을 스스로 배우는 것.
- **latent space**: 모델 내부 representation들이 놓이는 공간. 비슷한 의미의 데이터가 가까이 배치될 수 있다.
- **latent representation**: 입력 데이터에서 직접 보이지 않는 의미나 구조를 담은 내부 숫자 표현.
- **feature extraction**: 데이터에서 예측에 도움이 되는 단서(feature)를 뽑아내는 과정.
- **embedding**: token, 단어, 이미지 조각 등을 연속적인 vector로 바꾼 표현.
- **hidden state**: neural network의 중간 layer 출력. 특히 RNN, Transformer, LLM에서 자주 쓰인다.

### AI에서 어디에 쓰이는가

표현학습은 현대 AI 거의 전부의 핵심이다.

- **이미지 분류**: CNN이나 Vision Transformer가 픽셀을 바로 보고 끝내는 것이 아니라, 중간 representation을 통해 edge, texture, object part를 배운다.
- **LLM**: token embedding과 Transformer layer의 hidden state가 문맥 의미를 담는다. 같은 단어라도 문맥에 따라 hidden state가 달라질 수 있다. 예를 들어 “은행에 갔다”와 “강가의 은행나무”에서 “은행” 관련 표현은 다르게 형성된다.
- **검색과 추천**: 문서, 상품, 사용자를 embedding으로 바꾼 뒤 latent space에서 가까운 것을 찾는다.
- **생성 모델**: diffusion model이나 autoencoder 계열 모델은 이미지나 음성을 latent representation으로 압축한 뒤 생성에 활용한다.
- **transfer learning**: 대규모 데이터에서 배운 representation을 다른 작은 문제에 재사용한다. 예를 들어 ImageNet으로 학습한 모델의 앞부분을 가져와 의료 이미지 분류에 쓰는 식이다.

### 헷갈리기 쉬운 포인트

- **representation은 사람이 이해하기 쉬운 이름을 가진 feature와 다를 수 있다.**  
  어떤 dimension이 정확히 “귀 길이”인지 “감정 점수”인지 항상 알 수 있는 것은 아니다.

- **latent space가 실제 물리 공간은 아니다.**  
  숫자 vector들이 놓인 추상적인 공간이다. 가까움과 멂은 보통 cosine similarity, dot product, Euclidean distance 같은 방식으로 계산한다.

- **feature extraction과 representation learning은 연결되어 있지만 완전히 같은 말은 아니다.**  
  feature extraction은 단서를 뽑는 행위이고, representation learning은 그 단서를 포함한 좋은 내부 표현을 학습하는 전체 관점이다.

- **좋은 representation은 task에 따라 달라진다.**  
  얼굴 인식에 좋은 representation이 감정 분석에 그대로 좋은 것은 아닐 수 있다.

---

## 2. 초기화와 학습 안정성

### 한 줄 직관

초기화(initialization)는 신경망이 학습을 시작할 때 weight를 어떤 값으로 놓을지 정하는 일이고, 좋은 초기화는 학습이 너무 느리거나 불안정해지는 것을 막아 준다.

운동을 시작할 때 출발 자세가 너무 기울어져 있으면 제대로 달리기 어렵다. 신경망도 마찬가지다. 처음 weight가 너무 크면 계산값과 gradient가 폭발할 수 있고, 너무 작으면 신호가 layer를 지나며 거의 사라질 수 있다.

### 개념 정의

초기화(initialization)는 학습 전 neural network의 parameter, 특히 weight와 bias의 시작값을 정하는 과정이다.

신경망은 학습 전에는 아직 아무것도 배우지 않았다. 따라서 weight는 보통 random하게 시작한다. 하지만 아무 random 값이나 쓰면 안 된다. layer가 깊어질수록 값이 계속 커지거나 작아질 수 있기 때문이다.

학습 안정성(training stability)은 학습 중 loss, activation, gradient가 지나치게 커지거나 작아지지 않고, optimizer가 의미 있는 업데이트를 계속할 수 있는 상태를 말한다.

좋은 initialization의 목표는 크게 세 가지다.

1. 각 neuron이 서로 다른 역할을 배우게 한다.
2. forward pass에서 activation 값이 너무 커지거나 작아지지 않게 한다.
3. backward pass에서 gradient가 너무 커지거나 작아지지 않게 한다.

### 왜 이런 개념이 필요한가

신경망은 같은 계산을 여러 layer에서 반복한다.

```text
입력 → layer 1 → layer 2 → layer 3 → ... → 출력
```

만약 각 layer가 값을 평균적으로 2배씩 키운다면, 10개 layer 후에는 값이 대략 `2^10 = 1024`배가 될 수 있다. 반대로 각 layer가 값을 0.5배씩 줄이면, 10개 layer 후에는 `0.5^10 ≈ 0.001`이 된다.

이 문제는 forward pass의 activation뿐 아니라 backward pass의 gradient에서도 생긴다. activation과 gradient가 너무 커지면 학습이 흔들리고, 너무 작아지면 거의 학습하지 못한다.

초기화는 이 문제를 학습 시작점에서 줄여 주는 장치다. optimizer, learning rate, normalization, activation function도 중요하지만, 시작 weight가 너무 나쁘면 첫 단계부터 학습이 불안정해질 수 있다.

### 아주 쉬운 예시

가장 단순한 선형 계산을 보자.

```text
출력 = 입력 × weight
```

입력이 `1`이고 layer를 5번 지난다고 하자.

#### 경우 1: weight가 모두 2로 시작

```text
1 → 2 → 4 → 8 → 16 → 32
```

값이 빠르게 커진다. layer가 50개라면 훨씬 심각해진다. 이런 상황은 exploding activation이나 exploding gradient로 이어질 수 있다.

#### 경우 2: weight가 모두 0.2로 시작

```text
1 → 0.2 → 0.04 → 0.008 → 0.0016 → 0.00032
```

값이 거의 0에 가까워진다. 신호가 사라지면 앞 layer들이 무엇을 배워야 하는지 알기 어렵다.

#### 경우 3: weight가 적절한 크기로 random하게 시작

```text
1 → 0.9 → 1.1 → 0.95 → 1.05 → 1.0 근처
```

실제 계산은 더 복잡하지만, 좋은 initialization은 대략 이런 목표를 가진다. layer를 지나도 신호의 크기가 너무 크게 변하지 않게 한다.

### 개념 구조와 핵심 포인트

초기화에서 중요한 구조는 다음과 같다.

1. **random initialization**  
   weight를 random하게 시작한다. 모든 neuron이 같은 값을 가지면 같은 gradient를 받아 같은 방식으로 업데이트되기 때문에 서로 다른 feature를 배울 수 없다.

2. **symmetry breaking**  
   neuron들이 서로 다른 출발점을 갖도록 만드는 것이다. 예를 들어 같은 layer의 neuron 3개가 모두 weight `0.5`로 시작하면, 같은 입력에 같은 출력을 내고 같은 gradient를 받아 계속 비슷하게 움직일 수 있다. random initialization은 이 대칭을 깨서 서로 다른 역할을 배우게 한다.

3. **scale control**  
   weight의 크기를 적절히 조절한다. 너무 큰 random 값도, 너무 작은 random 값도 문제다.

4. **activation function에 맞춘 initialization**  
   sigmoid/tanh 계열과 ReLU 계열은 값이 흐르는 방식이 다르다. 그래서 activation function에 따라 추천 initialization이 다르다.

5. **학습 안정성을 돕는 다른 장치와 함께 작동**  
   initialization만으로 모든 문제가 해결되지는 않는다. learning rate, optimizer, normalization, residual connection, gradient clipping도 함께 중요하다.

### 핵심 수학 포인트

초기화의 핵심 수학은 “layer를 지나도 값의 분산(variance)이 너무 커지거나 작아지지 않게 하자”는 생각이다.

분산(variance)은 값들이 평균에서 얼마나 퍼져 있는지를 나타낸다. 아주 쉽게 말하면 숫자들의 흔들림 크기다.

예를 들어 두 묶음을 보자.

```text
A = [0.9, 1.0, 1.1]  → 평균 근처에 모여 있음
B = [-10, 1, 12]     → 많이 퍼져 있음
```

B가 A보다 variance가 크다. 신경망에서는 layer를 지날 때 activation의 variance가 계속 커지거나 작아지면 학습이 불안정해질 수 있다.

대표적인 초기화 방법은 다음과 같다.

#### Xavier initialization

Xavier initialization은 주로 tanh나 sigmoid 계열 activation에서 많이 설명된다. 핵심 아이디어는 입력으로 들어오는 연결 수(`fan_in`)와 출력으로 나가는 연결 수(`fan_out`)를 고려해 weight 크기를 정하는 것이다.

간단한 형태로 생각하면 weight의 scale을 다음과 비슷하게 잡는다.

```text
scale ≈ sqrt(2 / (fan_in + fan_out))
```

예를 들어 어떤 layer가 입력 4개, 출력 4개라면 다음과 같다.

```text
fan_in = 4
fan_out = 4
scale ≈ sqrt(2 / 8) = sqrt(0.25) = 0.5
```

즉 weight를 너무 큰 범위에서 뽑지 않고, 적당한 크기 근처에서 시작하게 한다.

#### He initialization

He initialization은 ReLU 계열 activation에서 자주 쓰인다. ReLU는 음수 입력을 0으로 만들기 때문에 신호의 일부가 사라진다. 그래서 이를 고려해 weight scale을 조금 다르게 잡는다.

단순화하면 다음 아이디어다.

```text
scale ≈ sqrt(2 / fan_in)
```

예를 들어 입력 연결 수가 8개라면:

```text
fan_in = 8
scale ≈ sqrt(2 / 8) = sqrt(0.25) = 0.5
```

입력 연결 수가 100개라면:

```text
scale ≈ sqrt(2 / 100) ≈ 0.14
```

입력이 많을수록 각 weight를 조금 작게 시작해야 전체 합이 너무 커지지 않는다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **initialization**: 학습 시작 전 parameter의 초기값을 정하는 과정.
- **Xavier initialization**: `fan_in`과 `fan_out`을 고려해 weight scale을 정하는 초기화 방식. Glorot initialization이라고도 부른다.
- **He initialization**: ReLU 계열 activation에 잘 맞도록 설계된 초기화 방식.
- **symmetry breaking**: neuron들이 같은 역할만 반복하지 않도록 random 시작점으로 대칭을 깨는 것.
- **fan_in**: 한 neuron으로 들어오는 입력 연결 수.
- **fan_out**: 한 layer 또는 neuron에서 다음으로 나가는 출력 연결 수.
- **training stability**: 학습 중 activation, gradient, loss가 지나치게 불안정하지 않은 상태.

### AI에서 어디에 쓰이는가

초기화는 거의 모든 neural network 학습에 필요하다.

- **MLP/CNN 학습**: weight initialization이 나쁘면 loss가 처음부터 NaN이 되거나 거의 줄지 않을 수 있다.
- **Transformer/LLM 학습**: 모델이 매우 깊기 때문에 initialization과 residual connection, normalization의 조합이 중요하다.
- **fine-tuning**: 이미 학습된 모델을 가져오는 경우에는 대부분 pre-trained weight가 초기값이 된다. 이때 새로 붙이는 classification head나 adapter layer는 여전히 적절히 초기화해야 한다.
- **실전 debugging**: loss가 갑자기 폭발하거나 gradient가 0에 가까우면 learning rate만 볼 것이 아니라 initialization, activation, normalization도 함께 확인해야 한다.

### 헷갈리기 쉬운 포인트

- **모든 weight를 0으로 초기화하면 안 된다.**  
  linear regression처럼 단순한 모델에서는 0 초기화가 가능할 때도 있지만, neural network의 같은 layer neuron들을 모두 0으로 시작하면 symmetry breaking이 되지 않는다.

- **random이면 다 좋은 것이 아니다.**  
  random initialization은 필요하지만, scale이 중요하다. 너무 큰 random 값은 폭발을 만들고, 너무 작은 random 값은 신호를 죽인다.

- **Xavier와 He를 외우기만 하면 부족하다.**  
  왜 필요한지 이해해야 한다. 핵심은 “layer를 지나도 activation과 gradient의 크기가 적당히 유지되게 하자”이다.

- **초기화는 학습 안정성의 전부가 아니다.**  
  initialization은 출발점을 좋게 만드는 것이고, 이후의 안정성은 optimizer, learning rate schedule, normalization, residual connection, gradient clipping 등과 함께 결정된다.

---

## 3. vanishing/exploding gradient

### 한 줄 직관

vanishing gradient는 gradient가 앞 layer로 갈수록 너무 작아져 학습 신호가 사라지는 문제이고, exploding gradient는 gradient가 너무 커져 업데이트가 불안정해지는 문제다.

선생님이 맨 뒤 학생에게 전달한 말이 학생들을 거치며 점점 작아져 앞자리에는 거의 안 들리면 vanishing gradient와 비슷하다. 반대로 말이 전달될수록 과장되어 마지막에는 소리 지르는 수준이 되면 exploding gradient와 비슷하다.

### 개념 정의

gradient는 loss를 줄이기 위해 parameter를 어느 방향으로 얼마나 바꿔야 하는지 알려 주는 신호다.

신경망 학습에서는 먼저 forward pass로 예측과 loss를 계산하고, backward pass로 각 parameter의 gradient를 계산한다.

```text
입력 → 여러 layer → 예측 → loss
loss에서 시작한 gradient → 뒤 layer → 중간 layer → 앞 layer
```

**vanishing gradient**는 이 gradient가 앞쪽 layer로 전달될수록 너무 작아져서 거의 0이 되는 문제다. gradient가 거의 0이면 parameter update도 거의 0이므로 앞 layer가 잘 배우지 못한다.

**exploding gradient**는 gradient가 전달되면서 너무 커지는 문제다. gradient가 너무 크면 parameter update가 과격해지고, loss가 튀거나 NaN이 될 수 있다.

**deep network instability**는 깊은 신경망에서 이런 gradient 문제, activation scale 문제, optimizer 불안정 등이 겹쳐 학습이 흔들리는 현상을 넓게 말한다.

### 왜 이런 개념이 필요한가

딥러닝은 layer가 깊다. Transformer나 큰 CNN은 수십, 수백 layer를 가질 수 있다. 깊은 모델이 잘 학습되려면 마지막 loss에서 나온 학습 신호가 앞쪽 layer까지 잘 전달되어야 한다.

하지만 backward pass에서는 여러 미분값이 곱해진다. 단순하게 말하면, 어떤 layer를 지날 때마다 gradient가 `0.5`배가 된다면 깊어질수록 빠르게 작아진다.

```text
1 → 0.5 → 0.25 → 0.125 → 0.0625 → ...
```

반대로 매번 `2`배가 되면 빠르게 커진다.

```text
1 → 2 → 4 → 8 → 16 → ...
```

이런 문제가 있으면 깊은 모델은 이론적으로 표현력이 좋아도 실제로는 학습하기 어렵다. 그래서 현대 딥러닝 구조에는 initialization, ReLU 계열 activation, normalization, residual connection, gradient clipping 같은 장치가 들어간다.

### 아주 쉬운 예시

가장 단순한 1D 예시를 보자. 모델이 여러 layer를 지나며 다음처럼 계산한다고 하자.

```text
h1 = 0.5 × x
h2 = 0.5 × h1
h3 = 0.5 × h2
h4 = 0.5 × h3
```

입력 `x = 1`이면 forward 값은 다음과 같다.

```text
h1 = 0.5
h2 = 0.25
h3 = 0.125
h4 = 0.0625
```

backward에서도 비슷하게 gradient가 곱해질 수 있다. 마지막에서 gradient가 `1`로 시작한다고 하면 앞쪽으로 갈수록:

```text
grad at h4 = 1
grad at h3 = 1 × 0.5 = 0.5
grad at h2 = 0.5 × 0.5 = 0.25
grad at h1 = 0.25 × 0.5 = 0.125
grad at x  = 0.125 × 0.5 = 0.0625
```

layer가 4개라서 아직 작아 보이지만, 50개라면 `0.5^50`은 거의 0에 가깝다. 앞쪽 layer는 “어떻게 고쳐야 하는지” 신호를 거의 못 받는다.

이번에는 각 layer가 `2`를 곱한다고 하자.

```text
grad: 1 → 2 → 4 → 8 → 16 → 32 ...
```

layer가 많아지면 gradient가 너무 커진다. optimizer가 parameter를 한 번에 너무 크게 바꿔서 loss가 오히려 증가하거나 계산이 터질 수 있다.

### 개념 구조와 핵심 포인트

vanishing/exploding gradient를 이해하는 구조는 다음과 같다.

1. **loss가 학습 신호의 출발점이다.**  
   모델이 틀린 정도를 loss로 계산한다.

2. **gradient는 parameter update 방향을 알려 준다.**  
   gradient descent에서는 대략 다음처럼 업데이트한다.

   ```text
   new_weight = old_weight - learning_rate × gradient
   ```

3. **깊은 네트워크에서는 gradient가 여러 layer를 거슬러 간다.**  
   이때 각 layer의 local gradient들이 곱해진다.

4. **작은 값들이 계속 곱해지면 vanishing gradient가 된다.**  
   예: `0.9^100 ≈ 0.000026`

5. **큰 값들이 계속 곱해지면 exploding gradient가 된다.**  
   예: `1.1^100 ≈ 13780` 정도로 커진다.

6. **해결책은 신호가 적당한 크기로 흐르게 만드는 것이다.**  
   initialization, activation, normalization, residual connection, gradient clipping 등이 이 목표를 돕는다.

### 핵심 수학 포인트

처음에는 1D로 이해하면 충분하다. 어떤 함수가 여러 단계로 이어져 있다고 하자.

```text
y = f3(f2(f1(x)))
```

`x`가 조금 변할 때 `y`가 얼마나 변하는지 알고 싶으면 각 단계의 변화율을 곱한다.

```text
전체 변화율 = f3의 변화율 × f2의 변화율 × f1의 변화율
```

이것이 chain rule의 핵심이다. chain rule은 “연결된 계산의 전체 변화량은 각 단계의 변화량을 곱해서 구한다”는 규칙이다.

신경망의 backward pass도 이 원리를 따른다. 어려운 수식으로 쓰면 복잡해 보이지만, 핵심은 매우 단순하다.

```text
앞 layer gradient = 뒤에서 온 gradient × 현재 layer의 local gradient
```

예를 들어 local gradient가 계속 `0.3`이면:

```text
1 × 0.3 × 0.3 × 0.3 × 0.3 = 0.0081
```

금방 작아진다. sigmoid activation이 깊은 네트워크에서 문제를 만들었던 이유도 여기에 있다. sigmoid는 입력이 매우 크거나 작으면 출력이 0이나 1 근처에서 거의 변하지 않는다. 이 구간에서는 local gradient가 매우 작다. 작은 gradient가 여러 번 곱해지면 앞 layer는 학습 신호를 거의 받지 못한다.

ReLU는 양수 구간에서 gradient가 1이라 vanishing gradient를 줄이는 데 도움이 된다. 하지만 ReLU도 음수 구간에서는 gradient가 0이므로 모든 문제가 사라지는 것은 아니다.

exploding gradient는 update 식으로 보면 더 직관적이다.

```text
new_weight = old_weight - learning_rate × gradient
```

learning rate가 `0.01`이어도 gradient가 `10000`이면 update 크기는 `100`이 된다. weight가 한 번에 너무 크게 움직인다. 그래서 RNN 학습이나 큰 모델 학습에서는 gradient clipping을 사용해 gradient 크기를 제한하기도 한다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **vanishing gradient**: gradient가 앞 layer로 갈수록 너무 작아져 학습이 거의 안 되는 문제.
- **exploding gradient**: gradient가 너무 커져 parameter update가 불안정해지는 문제.
- **deep network instability**: 깊은 모델에서 gradient, activation, loss 등이 불안정해지는 넓은 현상.
- **gradient propagation**: gradient가 backward pass를 통해 layer들을 거슬러 전달되는 과정.
- **chain rule**: 여러 단계로 연결된 함수의 변화율을 각 단계 변화율의 곱으로 계산하는 규칙.
- **gradient clipping**: gradient가 너무 커질 때 일정 크기 이상으로 커지지 않게 제한하는 방법.
- **residual connection**: layer 입력을 출력 쪽에 더해 주는 구조. gradient가 더 잘 흐르도록 도와 깊은 네트워크 학습에 중요하다.

### AI에서 어디에 쓰이는가

이 문제는 깊은 모델을 실제로 학습할 때 매우 중요하다.

- **RNN/LSTM**: 오래된 순차 데이터 모델에서는 긴 sequence에서 gradient가 사라지거나 폭발하는 문제가 컸다. LSTM과 GRU는 장기 의존성을 더 잘 학습하기 위해 설계되었다.
- **CNN/ResNet**: ResNet의 residual connection은 매우 깊은 CNN을 학습 가능하게 만든 핵심 아이디어다.
- **Transformer/LLM**: Transformer는 residual connection과 LayerNorm을 적극적으로 사용한다. 이것들은 attention이 좋아서만이 아니라, 깊은 네트워크에서 학습 신호가 안정적으로 흐르도록 돕기 때문에 중요하다.
- **실전 학습 모니터링**: loss가 갑자기 NaN이 되거나 gradient norm이 급격히 커지면 exploding gradient를 의심한다. 반대로 loss가 거의 줄지 않고 gradient가 0에 가까우면 vanishing gradient나 activation saturation을 의심한다.
- **optimizer 설정**: learning rate, warmup, gradient clipping, weight initialization은 모두 gradient 안정성과 연결된다.

### 헷갈리기 쉬운 포인트

- **vanishing gradient는 loss가 작은 것과 다르다.**  
  loss가 작아서 gradient가 작은 것은 좋은 상황일 수 있다. 하지만 모델이 아직 틀리는데 앞 layer gradient가 거의 0이면 학습 문제가 된다.

- **exploding gradient는 단순히 gradient가 크다는 뜻만은 아니다.**  
  중요한 것은 update가 불안정해져 loss가 튀거나 계산이 NaN이 되는 것이다.

- **깊은 모델은 무조건 gradient 문제가 생기는 것은 아니다.**  
  좋은 initialization, activation, normalization, residual connection 덕분에 현대 모델은 훨씬 깊어질 수 있었다.

- **gradient clipping은 exploding gradient를 줄이지만 원인 전체를 해결하지는 않는다.**  
  clipping은 안전장치에 가깝다. learning rate, architecture, initialization도 함께 봐야 한다.

- **attention이 있다고 gradient 문제가 자동으로 사라지지는 않는다.**  
  Transformer도 깊어지면 안정화 장치가 필요하다. residual connection, LayerNorm, initialization이 함께 중요하다.

---

## 복습 질문 3개

1. representation learning이 사람이 직접 feature를 만드는 방식보다 이미지나 자연어 문제에서 유리한 이유는 무엇인가?
2. 모든 weight를 같은 값, 특히 0으로 초기화하면 neural network에서 어떤 문제가 생기는가?
3. vanishing gradient와 exploding gradient를 `0.5를 계속 곱하는 경우`와 `2를 계속 곱하는 경우`로 설명해 보라.

## 오늘의 한 줄 요약

딥러닝은 좋은 latent representation을 여러 layer에서 만들어 가는 모델이며, 이 표현을 제대로 배우려면 initialization과 gradient 흐름이 안정적이어야 한다.

---

## Follow-up Review Answers

- Answer cron output: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-07_09-26-24.md`

[AI/ML 오늘의 복습 정답 Day 15/30]

오늘은 딥러닝이 “좋은 내부 표현을 배우는 과정”과, 그 학습이 안정적으로 일어나기 위해 필요한 초기화와 gradient 흐름을 다시 정리해 볼게요.

### 1. representation learning이 사람이 직접 feature를 만드는 방식보다 이미지나 자연어 문제에서 유리한 이유는 무엇인가?

**정답**

representation learning이 유리한 이유는 이미지나 자연어 데이터가 너무 복잡해서 사람이 좋은 feature를 전부 직접 설계하기 어렵기 때문입니다.

딥러닝 모델은 raw input, 즉 원본 입력에서 출발해서 여러 layer를 지나며 문제를 풀기 좋은 숫자 표현을 스스로 배웁니다. 이때 만들어지는 내부 표현을 latent representation이라고 합니다.

사람이 “이 feature가 중요하다”라고 하나하나 정해 주는 대신, 모델이 학습을 통해 useful feature를 자동으로 찾는 것이 핵심입니다.

**설명**

전통적인 머신러닝에서는 사람이 feature extraction을 직접 많이 했습니다. feature extraction은 데이터에서 예측에 도움이 되는 단서를 뽑는 과정입니다.

예를 들어 스팸 메일 분류라면 사람이 이런 feature를 만들 수 있습니다.

- “무료”라는 단어가 있는가?
- 링크가 몇 개인가?
- 느낌표가 많은가?

이 정도 문제는 사람이 규칙을 어느 정도 만들 수 있습니다.

하지만 이미지나 자연어는 훨씬 복잡합니다. 고양이 사진을 분류한다고 할 때, 사람이 직접 “귀의 각도”, “수염의 방향”, “털의 질감”, “눈 주변 패턴”을 모두 수식이나 규칙으로 만들기는 어렵습니다.

자연어도 마찬가지입니다. 같은 단어라도 문맥에 따라 의미가 바뀝니다. 예를 들어 “은행에 갔다”의 은행과 “강가의 은행나무”의 은행은 다릅니다. 이런 문맥적 의미를 사람이 feature로 전부 직접 설계하기는 매우 어렵습니다.

representation learning은 이 문제를 모델에게 맡깁니다. 모델은 여러 layer를 지나면서 처음에는 단순한 정보를 보고, 점점 더 추상적인 정보를 배웁니다.

이미지에서는 대략 이런 흐름이 생길 수 있습니다.

원본 픽셀 → 선과 색 변화 → 작은 모양 → 얼굴 일부 → 고양이 같은 전체 패턴 → 예측

즉, 좋은 latent representation을 만들면 마지막 classifier가 훨씬 쉽게 정답을 맞힐 수 있습니다.

**예시**

아주 작은 예로 과일 분류를 생각해 볼게요.

입력이 이렇게 있다고 합시다.

- 사과: 단맛 8, 신맛 3
- 레몬: 단맛 2, 신맛 9

사람은 이 숫자를 보고 “사과는 달고, 레몬은 시다”라고 이해합니다.

모델도 학습하면서 내부적으로 이런 표현을 만들 수 있습니다.

- 사과의 latent representation: [달콤함 0.9, 상큼함 0.3]
- 레몬의 latent representation: [달콤함 0.2, 상큼함 0.95]

실제 모델 안에서는 각 숫자 축에 “달콤함” 같은 예쁜 이름이 붙어 있지 않을 수 있습니다. 하지만 비슷한 과일은 latent space에서 가까이 모이고, 다른 과일은 멀어지도록 학습될 수 있습니다.

**실전 연결**

LLM에서는 token이 embedding vector로 바뀌고, Transformer layer를 지나며 문맥을 반영한 hidden state가 됩니다. 이 hidden state가 바로 중요한 learned representation입니다. 검색 시스템에서는 문서와 질문을 embedding으로 바꾼 뒤 latent space에서 가까운 문서를 찾습니다. 이미지 모델, 추천 시스템, 생성 모델, fine-tuning 모두 결국 “좋은 representation을 어떻게 만들고 활용할 것인가”와 깊게 연결됩니다.

### 2. 모든 weight를 같은 값, 특히 0으로 초기화하면 neural network에서 어떤 문제가 생기는가?

**정답**

모든 weight를 같은 값, 특히 0으로 초기화하면 같은 layer 안의 neuron들이 서로 똑같은 계산을 하게 됩니다.

그러면 같은 출력을 만들고, 같은 gradient를 받고, 같은 방식으로 업데이트됩니다. 결과적으로 여러 neuron이 있어도 서로 다른 feature를 배우지 못합니다.

이 문제를 symmetry breaking이 되지 않는다고 말합니다. symmetry breaking은 neuron들이 서로 다른 역할을 배울 수 있도록 대칭을 깨는 것입니다.

**설명**

neural network에서 여러 neuron을 두는 이유는 각 neuron이 서로 다른 특징을 배우게 하기 위해서입니다.

예를 들어 이미지 분류 모델에서 어떤 neuron은 “세로선”에 민감하고, 다른 neuron은 “둥근 모양”에 민감하고, 또 다른 neuron은 “털 질감”에 민감해질 수 있습니다.

그런데 모든 weight가 같은 값으로 시작하면 문제가 생깁니다.

같은 layer에 neuron 3개가 있고, 모두 weight가 0이라고 해 봅시다. 같은 입력이 들어오면 세 neuron은 같은 계산을 합니다. 그래서 출력도 같습니다. backward pass에서 gradient도 같아집니다. optimizer가 update를 해도 세 neuron은 계속 같은 방향으로 움직입니다.

즉 neuron이 3개 있어도 실제로는 거의 neuron 1개를 복사해 놓은 것처럼 작동할 수 있습니다.

그래서 neural network에서는 보통 weight를 random initialization으로 시작합니다. random이라고 해서 아무렇게나 큰 값을 넣는다는 뜻은 아닙니다. 서로 조금씩 다른 출발점을 주되, 값의 크기는 너무 크거나 작지 않게 조절해야 합니다.

이때 Xavier initialization이나 He initialization 같은 방법이 쓰입니다.

- Xavier initialization: 주로 tanh, sigmoid 계열에서 자주 설명되는 초기화 방식
- He initialization: ReLU 계열 activation에 잘 맞는 초기화 방식

핵심 목표는 두 가지입니다.

첫째, neuron들이 서로 다른 역할을 배우게 한다.

둘째, layer를 지나며 activation과 gradient가 너무 커지거나 작아지지 않게 한다.

**예시**

아주 단순한 예를 들어 볼게요.

입력이 2이고, neuron 3개가 모두 같은 weight 0으로 시작한다고 합시다.

- neuron A: 2 × 0 = 0
- neuron B: 2 × 0 = 0
- neuron C: 2 × 0 = 0

출력이 모두 같습니다. 학습 중에 gradient도 모두 같다면 update 후에도 비슷합니다.

반대로 weight를 조금씩 다르게 시작하면 상황이 달라집니다.

- neuron A weight: 0.1
- neuron B weight: -0.2
- neuron C weight: 0.05

그러면 같은 입력 2가 들어와도 출력이 달라집니다.

- neuron A: 2 × 0.1 = 0.2
- neuron B: 2 × -0.2 = -0.4
- neuron C: 2 × 0.05 = 0.1

이제 각 neuron은 조금씩 다른 신호를 만들고, 학습하면서 서로 다른 feature를 배울 가능성이 생깁니다.

**실전 연결**

실제로 MLP, CNN, Transformer, LLM의 새 layer를 학습할 때 initialization은 매우 중요합니다. pre-trained model을 fine-tuning할 때도 기존 weight는 이미 학습된 값이지만, 새로 붙이는 classification head나 adapter layer는 적절히 초기화해야 합니다. loss가 처음부터 줄지 않거나, gradient가 거의 0이거나, 값이 NaN으로 터진다면 learning rate뿐 아니라 initialization도 함께 확인해야 합니다.

### 3. vanishing gradient와 exploding gradient를 `0.5를 계속 곱하는 경우`와 `2를 계속 곱하는 경우`로 설명해 보라.

**정답**

vanishing gradient는 gradient가 layer를 거슬러 올라가며 계속 작아지는 문제입니다. 예를 들어 gradient에 0.5를 계속 곱하면 값이 빠르게 0에 가까워집니다.

exploding gradient는 반대로 gradient가 계속 커지는 문제입니다. 예를 들어 gradient에 2를 계속 곱하면 값이 빠르게 커져서 학습이 불안정해집니다.

즉,

- 0.5를 계속 곱함 → gradient가 사라짐 → vanishing gradient
- 2를 계속 곱함 → gradient가 폭발함 → exploding gradient

입니다.

**설명**

gradient는 loss function을 줄이기 위해 parameter를 어느 방향으로 얼마나 바꿔야 하는지 알려 주는 신호입니다. 쉽게 말해 “이 weight를 이렇게 고치면 loss가 줄어든다”라고 알려 주는 학습 신호입니다.

신경망은 forward pass로 예측과 loss를 계산한 뒤, backward pass로 gradient를 계산합니다.

입력 → 여러 layer → 예측 → loss

그다음 gradient는 반대로 흐릅니다.

loss → 뒤 layer → 중간 layer → 앞 layer

깊은 neural network에서는 gradient가 여러 layer를 지나야 합니다. 이때 chain rule이 사용됩니다. chain rule은 연결된 함수의 변화율을 각 단계 변화율의 곱으로 계산하는 규칙입니다.

그래서 backward pass에서는 작은 값들이 여러 번 곱해지거나, 큰 값들이 여러 번 곱해질 수 있습니다.

만약 local gradient가 계속 0.5라면 다음처럼 됩니다.

1 → 0.5 → 0.25 → 0.125 → 0.0625 → ...

처음에는 작아지는 정도가 괜찮아 보이지만, layer가 50개, 100개가 되면 거의 0에 가까워집니다. 그러면 앞쪽 layer는 학습 신호를 거의 받지 못합니다. 이것이 vanishing gradient입니다.

반대로 local gradient가 계속 2라면 다음처럼 됩니다.

1 → 2 → 4 → 8 → 16 → 32 → ...

layer가 많아질수록 gradient가 매우 커집니다. 그러면 update 식에서 문제가 생깁니다.

new_weight = old_weight - learning_rate × gradient

learning rate가 작아도 gradient가 너무 크면 weight가 한 번에 너무 많이 바뀝니다. 그러면 loss가 튀거나, 학습이 발산하거나, 계산 결과가 NaN이 될 수 있습니다. 이것이 exploding gradient입니다.

**예시**

마지막 layer에서 시작한 gradient가 1이라고 해 봅시다.

먼저 0.5를 계속 곱하는 경우입니다.

- 시작: 1
- 한 layer 뒤: 1 × 0.5 = 0.5
- 두 layer 뒤: 0.5 × 0.5 = 0.25
- 세 layer 뒤: 0.25 × 0.5 = 0.125
- 네 layer 뒤: 0.125 × 0.5 = 0.0625

layer가 더 많아지면 앞쪽 layer가 받는 gradient는 거의 0이 됩니다. 앞쪽 layer는 “어떻게 바뀌어야 하는지” 신호를 못 받습니다.

이번에는 2를 계속 곱하는 경우입니다.

- 시작: 1
- 한 layer 뒤: 1 × 2 = 2
- 두 layer 뒤: 2 × 2 = 4
- 세 layer 뒤: 4 × 2 = 8
- 네 layer 뒤: 8 × 2 = 16

layer가 더 많아지면 gradient가 너무 커집니다. optimizer가 weight를 너무 과격하게 바꾸면서 학습이 흔들립니다.

일상 비유로 보면, vanishing gradient는 뒤에서 전달한 말이 앞사람에게 갈수록 점점 작아져 거의 안 들리는 상황입니다. exploding gradient는 반대로 말이 전달될수록 점점 과장되어 마지막에는 소리 지르는 수준이 되는 상황입니다.

**실전 연결**

vanishing/exploding gradient는 깊은 CNN, RNN, Transformer, LLM 학습에서 매우 중요한 문제입니다. 현대 모델은 이를 줄이기 위해 He initialization, Xavier initialization, ReLU 계열 activation, LayerNorm, residual connection, gradient clipping 같은 장치를 사용합니다. LLM에서 residual connection과 normalization이 중요한 이유도 단순히 성능 때문만이 아니라, 깊은 layer를 지나도 gradient와 activation이 안정적으로 흐르게 하기 위해서입니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-07-day15.md
