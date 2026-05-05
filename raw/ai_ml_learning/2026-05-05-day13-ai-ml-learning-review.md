# Day 13 - AI/ML 기초 학습

- Date: 2026-05-05
- Progress: 13/30
- Level: beginner-intermediate
- Milestone: 신경망과 표현학습
- Milestone goal: 딥러닝이 다층 표현을 학습한다는 의미를 이해한다.

## Today's 3 concepts

1. 퍼셉트론과 선형결합
2. 다층퍼셉트론과 비선형성
3. 활성화함수의 역할

---

## 1. 퍼셉트론과 선형결합

### 한 줄 직관

퍼셉트론(perceptron)은 여러 입력을 중요도에 따라 더한 뒤, 그 합이 기준을 넘는지 보고 간단한 결정을 내리는 가장 기본적인 인공 뉴런입니다.

### 개념 정의

퍼셉트론(perceptron)은 신경망의 아주 초기 형태이자, 오늘날 neural network의 한 뉴런을 이해하는 출발점입니다. 핵심 아이디어는 단순합니다.

1. 여러 입력값을 받습니다.
2. 각 입력에 가중치(weight)를 곱합니다.
3. 전부 더해서 weighted sum을 만듭니다.
4. 이 값이 threshold를 넘으면 1, 넘지 못하면 0처럼 출력합니다.

예를 들어 어떤 모델이 “이 이메일이 스팸인가?”를 판단한다고 해봅시다. 입력은 다음처럼 만들 수 있습니다.

- `x1 = 광고 단어가 많은가?`
- `x2 = 모르는 발신자인가?`
- `x3 = 링크가 많은가?`

모델은 각각을 똑같이 보지 않습니다. “광고 단어”가 더 중요할 수도 있고, “링크 수”가 더 중요할 수도 있습니다. 이 중요도가 weight입니다.

수식으로는 보통 이렇게 씁니다.

```text
z = w1*x1 + w2*x2 + w3*x3 + b
```

여기서 `z`가 weighted sum이고, `b`는 bias입니다. bias는 판단 기준을 조금 왼쪽이나 오른쪽으로 움직이는 값이라고 보면 됩니다.

### 왜 이런 개념이 필요한가

머신러닝 모델은 결국 입력에서 규칙을 찾아야 합니다. 그런데 입력이 여러 개일 때, “어떤 입력이 더 중요한가?”를 배워야 합니다. 퍼셉트론은 이 과정을 가장 단순한 형태로 보여줍니다.

사람이 시험 합격 여부를 판단한다고 생각해봅시다.

- 출석: 20점 비중
- 과제: 30점 비중
- 시험: 50점 비중

각 항목을 그냥 더하는 것이 아니라, 중요도를 반영해서 더합니다. 이것이 weighted sum의 직관입니다.

딥러닝에서도 마찬가지입니다. 이미지 모델은 픽셀을 보고, 언어 모델은 token embedding을 보고, 추천 모델은 사용자 행동을 봅니다. 이 많은 입력을 그대로 두면 판단하기 어렵기 때문에, 모델은 weight를 통해 “무엇을 얼마나 반영할지”를 배웁니다.

### 아주 쉬운 예시

아주 작은 숫자로 보겠습니다. 어떤 퍼셉트론이 “공부한 학생이 시험에 통과할지”를 예측한다고 합시다.

입력은 2개입니다.

- `x1 = 공부 시간`: 2시간
- `x2 = 전날 수면`: 1이면 충분히 잠, 0이면 부족

weight와 bias는 다음과 같다고 합시다.

- `w1 = 0.6`
- `w2 = 1.0`
- `b = -2.0`

학생 A는 2시간 공부했고 충분히 잤습니다.

```text
z = 0.6*2 + 1.0*1 - 2.0
  = 1.2 + 1.0 - 2.0
  = 0.2
```

만약 threshold를 0으로 두고, `z >= 0`이면 통과라고 하면 학생 A는 통과입니다.

학생 B는 2시간 공부했지만 잠을 못 잤습니다.

```text
z = 0.6*2 + 1.0*0 - 2.0
  = 1.2 + 0 - 2.0
  = -0.8
```

학생 B는 기준을 넘지 못합니다.

이 예시는 단순하지만 중요한 사실을 보여줍니다. 같은 공부 시간이라도 수면이라는 다른 입력이 함께 판단에 영향을 줍니다. 퍼셉트론은 여러 신호를 weight로 조합해서 하나의 판단 점수로 바꿉니다.

### 개념 구조와 핵심 포인트

퍼셉트론의 구조는 다음 순서로 이해하면 됩니다.

1. **input**: 모델이 보는 값입니다. 예: 공부 시간, 픽셀값, 단어 embedding 등.
2. **weight**: 각 input의 중요도입니다. 큰 weight는 해당 입력을 더 강하게 반영합니다.
3. **weighted sum**: input과 weight를 곱해서 모두 더한 값입니다.
4. **bias**: 판단 기준을 조절하는 추가 값입니다.
5. **threshold 또는 activation**: weighted sum을 최종 출력으로 바꾸는 단계입니다.

핵심은 퍼셉트론이 입력 공간을 선 하나, 평면 하나, 또는 더 높은 차원의 hyperplane으로 나눈다는 점입니다. 입력이 2개라면 선(line)으로 나눕니다. 입력이 3개라면 평면(plane)으로 나눕니다. 입력 차원이 더 높으면 hyperplane이라고 부릅니다.

그래서 단일 퍼셉트론은 “직선으로 나눌 수 있는 문제”에는 잘 맞습니다. 하지만 구불구불한 경계가 필요한 문제에는 부족합니다. 이 한계가 다음 개념인 다층퍼셉트론(MLP)으로 이어집니다.

### 핵심 수학 포인트

퍼셉트론의 중심 수학은 선형결합(linear combination)입니다.

```text
z = w1*x1 + w2*x2 + ... + wn*xn + b
```

이 식은 입력 벡터 `x`와 weight 벡터 `w`의 dot product에 bias를 더한 형태입니다.

```text
z = w · x + b
```

여기서 dot product는 두 벡터의 같은 위치끼리 곱해서 더하는 연산입니다.

예를 들어:

```text
w = [2, 3]
x = [4, 5]
w · x = 2*4 + 3*5 = 8 + 15 = 23
```

딥러닝에서는 이 계산이 엄청 많이 반복됩니다. linear layer도 기본적으로 이와 같은 계산을 여러 개 동시에 수행합니다. 입력 tensor가 들어오면 weight matrix와 곱해져 새로운 표현(hidden representation)이 됩니다.

중요한 점은 선형결합만으로는 입력을 “곧게” 섞을 수는 있지만, 복잡하게 휘어진 패턴은 만들기 어렵다는 것입니다. 그래서 딥러닝에는 여러 layer와 activation function이 필요합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **perceptron**: 입력에 weight를 곱해 더하고 기준에 따라 출력하는 기본 인공 뉴런입니다.
- **weighted sum**: 입력값에 각각의 weight를 곱한 뒤 모두 더한 값입니다.
- **threshold**: 출력이 켜질지 말지를 정하는 기준값입니다.
- **activation**: weighted sum을 최종 출력 형태로 바꾸는 단계입니다. 현대 신경망에서는 ReLU, sigmoid 같은 activation function을 많이 씁니다.
- **weight**: 입력의 중요도를 나타내는 학습 가능한 값입니다.
- **bias**: 기준선을 이동시키는 학습 가능한 값입니다.
- **linear combination**: 여러 값을 각각 배수로 곱해 더하는 방식입니다.

### AI에서 어디에 쓰이는가

퍼셉트론 자체는 단순하지만, 현대 AI의 기본 계산 단위와 깊게 연결됩니다.

- **linear layer**: LLM, 이미지 모델, 추천 모델에서 매우 자주 쓰이는 기본 층입니다. 내부 계산은 `Wx + b` 형태입니다.
- **embedding 변환**: token embedding이 다음 layer로 이동할 때 weight matrix를 통해 새로운 표현으로 바뀝니다.
- **classification head**: 모델 마지막에서 “고양이/강아지”, “긍정/부정”, “다음 token 후보” 같은 점수를 만들 때 선형결합이 쓰입니다.
- **attention 내부 계산**: query, key, value를 만들 때도 입력 hidden state에 weight matrix를 곱합니다.

즉, 퍼셉트론을 이해하면 “신경망은 입력에 weight를 곱해 새로운 신호를 만든다”는 아주 중요한 감각이 생깁니다.

### 헷갈리기 쉬운 포인트

- **퍼셉트론은 신경망 전체가 아니라 기본 단위에 가깝습니다.** 여러 퍼셉트론을 layer로 묶고 여러 layer를 쌓으면 더 복잡한 neural network가 됩니다.
- **weight는 사람이 직접 정하는 규칙이 아니라 학습으로 조정되는 값입니다.** 처음에는 랜덤에 가깝게 시작하고, loss를 줄이는 방향으로 optimizer가 업데이트합니다.
- **threshold와 activation은 비슷해 보이지만 현대 신경망에서는 더 부드럽거나 효율적인 activation function을 씁니다.** 예전 퍼셉트론은 딱 0/1로 나누는 계단 함수에 가까웠지만, 지금은 gradient 학습이 잘 되도록 ReLU, sigmoid, tanh 등을 사용합니다.
- **선형결합만으로는 복잡한 패턴을 충분히 표현하기 어렵습니다.** 그래서 다층 구조와 비선형성이 필요합니다.

---

## 2. 다층퍼셉트론과 비선형성

### 한 줄 직관

다층퍼셉트론(MLP)은 단순한 판단기 여러 개를 층층이 쌓아, 입력을 점점 더 유용한 표현으로 바꾸는 neural network입니다.

### 개념 정의

다층퍼셉트론(MLP, Multi-Layer Perceptron)은 여러 개의 layer로 구성된 신경망입니다. 보통 다음 구조를 가집니다.

```text
input layer → hidden layer → hidden layer → output layer
```

여기서 hidden layer는 입력과 출력 사이에 있는 중간 계산층입니다. 사람에게 직접 보이는 정답은 아니지만, 모델 내부에서 입력을 더 좋은 형태로 바꾸는 역할을 합니다.

예를 들어 고양이 이미지를 분류하는 모델을 생각해봅시다.

- 첫 layer는 밝기나 선 같은 단순한 패턴을 볼 수 있습니다.
- 다음 layer는 귀, 눈, 수염 같은 조합을 볼 수 있습니다.
- 더 깊은 layer는 “고양이답다”는 더 추상적인 표현을 만들 수 있습니다.

MLP는 꼭 이미지에만 쓰이는 것은 아닙니다. LLM의 Transformer block 안에도 feed-forward network 또는 MLP라고 부르는 부분이 있습니다. 이 부분은 각 token의 hidden state를 더 풍부한 표현으로 바꾸는 역할을 합니다.

### 왜 이런 개념이 필요한가

단일 퍼셉트론은 선형적인 경계만 만들 수 있습니다. 쉽게 말해, 데이터를 직선 하나로 나눌 수 있으면 괜찮지만, 복잡하게 섞여 있으면 어렵습니다.

일상 비유로 생각해봅시다. 어떤 사람을 “운동을 좋아하는 사람”과 “운동을 좋아하지 않는 사람”으로 나누고 싶습니다. 단순히 “운동 시간” 하나만 보면 어느 정도 나눌 수 있습니다. 하지만 실제로는 더 복잡합니다.

- 운동 시간은 적지만 스포츠 영상을 자주 보는 사람
- 운동 시간은 많지만 직업 때문에 어쩔 수 없이 하는 사람
- 헬스장은 안 가지만 등산을 좋아하는 사람

이런 패턴은 직선 하나로 나누기 어렵습니다. 여러 기준을 조합하고, 중간 판단을 만들고, 다시 조합해야 합니다. MLP는 바로 이 과정을 layer로 수행합니다.

중요한 점은 MLP가 단순히 선형결합을 여러 번 하는 것만으로는 충분하지 않다는 것입니다. 선형변환 뒤에 또 선형변환을 해도 전체적으로는 여전히 하나의 선형변환과 같습니다. 그래서 layer 사이에 nonlinearity가 반드시 필요합니다.

### 아주 쉬운 예시

입력이 하나인 아주 단순한 상황을 보겠습니다.

우리는 다음 규칙을 배우고 싶습니다.

```text
x가 -1 근처이거나 +1 근처이면 좋다.
x가 0 근처이면 별로다.
```

이 패턴은 직선 하나로 표현하기 어렵습니다. 왜냐하면 양쪽 끝은 높고 가운데는 낮아야 하기 때문입니다.

단일 퍼셉트론은 대체로 이런 식의 판단을 합니다.

```text
x가 클수록 점수가 커진다
또는 x가 작을수록 점수가 커진다
```

하지만 우리가 원하는 것은 “양쪽은 좋고 가운데는 나쁨”입니다. 이럴 때 hidden layer의 여러 뉴런이 각각 작은 역할을 맡을 수 있습니다.

- 뉴런 A: `x > 0.5`이면 반응
- 뉴런 B: `x < -0.5`이면 반응
- 마지막 output: A나 B가 반응하면 좋은 점수

작은 뉴런 여러 개가 합쳐지면, 직선 하나보다 훨씬 다양한 모양을 만들 수 있습니다. 이것이 MLP의 강점입니다.

### 개념 구조와 핵심 포인트

MLP의 기본 구조는 다음과 같습니다.

1. **input layer**: 원래 데이터를 받습니다.
2. **hidden layer**: 입력을 새로운 표현으로 바꿉니다.
3. **activation function**: 각 layer의 결과에 비선형성을 넣습니다.
4. **output layer**: 최종 예측값을 만듭니다.

핵심 포인트는 세 가지입니다.

첫째, **hidden layer는 중간 표현을 만듭니다.** 입력 데이터가 그대로는 해결하기 어려워도, hidden layer를 지나면 더 풀기 쉬운 형태가 될 수 있습니다.

둘째, **nonlinearity가 있어야 복잡한 패턴을 표현할 수 있습니다.** layer를 아무리 많이 쌓아도 activation function이 없으면 결국 하나의 큰 linear layer와 비슷해집니다.

셋째, **universal approximation이라는 중요한 이론적 성질이 있습니다.** 충분히 큰 hidden layer와 적절한 activation function을 가진 MLP는 매우 넓은 범위의 함수를 근사할 수 있습니다. 쉽게 말해, 충분한 뉴런과 데이터와 학습이 있다면 복잡한 입력-출력 관계를 꽤 잘 따라 할 수 있다는 뜻입니다.

물론 이 말이 “무조건 잘 학습된다”는 뜻은 아닙니다. 표현할 수 있는 능력과 실제로 잘 학습하는 능력은 다릅니다. 실제 학습에는 데이터, loss, optimizer, initialization, regularization 등이 모두 중요합니다.

### 핵심 수학 포인트

MLP의 한 layer는 보통 이렇게 계산합니다.

```text
h1 = activation(W1*x + b1)
h2 = activation(W2*h1 + b2)
y  = W3*h2 + b3
```

여기서 `W1`, `W2`, `W3`는 weight matrix이고, `b1`, `b2`, `b3`는 bias입니다. `h1`, `h2`는 hidden state 또는 hidden representation이라고 볼 수 있습니다.

아주 작은 숫자로 보겠습니다.

입력 `x = [1, 2]`이고, 첫 hidden layer에 뉴런이 2개 있다고 합시다.

```text
뉴런 1: z1 = 1*x1 + 1*x2 - 2 = 1 + 2 - 2 = 1
뉴런 2: z2 = 2*x1 - 1*x2 + 0 = 2 - 2 = 0
```

activation으로 ReLU를 쓰면 `ReLU(z) = max(0, z)`입니다.

```text
h1 = ReLU(1) = 1
h2 = ReLU(0) = 0
```

이제 다음 layer는 원래 입력 `[1, 2]`가 아니라 hidden representation `[1, 0]`을 봅니다. 즉, 모델은 입력을 한 번 해석한 뒤 다음 판단을 합니다.

이것이 딥러닝에서 매우 중요합니다. 깊은 모델은 원본 입력을 바로 정답에 연결하는 것이 아니라, 여러 단계의 hidden state로 바꾸며 점점 더 유용한 표현을 만듭니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **MLP**: Multi-Layer Perceptron. 여러 layer로 구성된 기본 feed-forward neural network입니다.
- **hidden layer**: input과 output 사이에서 중간 표현을 만드는 layer입니다.
- **hidden state / hidden representation**: 모델 내부에서 만들어진 중간 표현입니다.
- **nonlinearity**: 직선적인 변환만으로는 만들 수 없는 복잡한 패턴을 가능하게 하는 성질입니다.
- **activation function**: layer의 출력에 nonlinearity를 넣는 함수입니다.
- **universal approximation**: 충분한 크기의 MLP가 다양한 함수를 근사할 수 있다는 이론적 성질입니다.
- **feed-forward**: 입력이 앞에서 뒤로 한 방향으로 흐르는 구조입니다.

### AI에서 어디에 쓰이는가

MLP는 현대 AI의 핵심 부품입니다.

- **Transformer의 feed-forward network**: LLM에서 attention 다음에 자주 등장하는 MLP 블록은 token별 hidden state를 변환합니다.
- **classification model**: embedding을 받아 최종 label을 예측하는 head로 자주 쓰입니다.
- **recommendation system**: 사용자 feature와 item feature를 결합해 클릭 확률이나 구매 확률을 예측합니다.
- **tabular data model**: 표 형태 데이터에서 여러 feature를 조합하는 데 사용됩니다.
- **representation learning**: raw input을 바로 쓰지 않고, 더 유용한 hidden representation으로 바꾸는 데 쓰입니다.

LLM을 볼 때도 MLP는 단순한 부속품이 아닙니다. attention이 token들 사이의 관계를 섞는 역할을 한다면, MLP는 각 token 위치의 hidden state를 더 복잡한 특징으로 변환하는 역할을 합니다.

### 헷갈리기 쉬운 포인트

- **layer를 많이 쌓는 것만으로는 충분하지 않습니다.** activation function이 없으면 여러 linear layer는 하나의 linear layer로 합쳐질 수 있습니다.
- **universal approximation은 마법의 보장이 아닙니다.** 표현 가능하다는 말과 실제 학습이 잘 된다는 말은 다릅니다.
- **hidden layer는 사람이 직접 의미를 붙인 규칙 모음이 아닙니다.** 모델이 loss를 줄이는 과정에서 스스로 만들어낸 중간 표현입니다.
- **MLP는 오래된 개념이지만 여전히 현대 모델에 매우 중요합니다.** Transformer 안에도 MLP 계열의 feed-forward block이 핵심 구성요소로 들어갑니다.

---

## 3. 활성화함수의 역할

### 한 줄 직관

활성화함수(activation function)는 뉴런의 계산 결과를 그냥 통과시키지 않고, 꺾거나 눌러서 신경망이 복잡한 패턴을 배울 수 있게 만드는 장치입니다.

### 개념 정의

활성화함수(activation function)는 `Wx + b`처럼 선형결합으로 나온 값을 다음 layer로 보내기 전에 변환하는 함수입니다.

가장 단순한 linear layer는 다음 계산을 합니다.

```text
z = Wx + b
```

여기에 activation function을 적용하면 다음처럼 됩니다.

```text
a = activation(z)
```

대표적인 activation function은 다음과 같습니다.

- **ReLU**: `max(0, x)`
- **sigmoid**: 값을 0과 1 사이로 눌러줍니다.
- **tanh**: 값을 -1과 1 사이로 눌러줍니다.

activation function이 필요한 이유는 neural network에 nonlinearity를 넣기 위해서입니다. 이것이 없으면 여러 layer를 쌓아도 복잡한 모양을 만들기 어렵습니다.

### 왜 이런 개념이 필요한가

딥러닝의 목표는 단순한 직선 관계만 배우는 것이 아닙니다. 실제 데이터는 대부분 복잡합니다.

예를 들어 집값을 예측한다고 합시다.

- 면적이 넓으면 대체로 비싸집니다.
- 하지만 너무 외진 곳이면 가격이 낮을 수 있습니다.
- 지하철역과의 거리가 가까우면 좋지만, 너무 시끄러운 위치는 오히려 불리할 수 있습니다.

이런 관계는 단순히 “입력에 weight를 곱해서 더하기”만으로는 부족합니다. 중간중간 꺾임이 필요합니다. activation function은 이 꺾임을 만들어줍니다.

일상 비유로는 수도꼭지를 생각할 수 있습니다. 입력 압력이 조금 들어와도 아예 물이 안 나오게 할 수도 있고, 어느 정도 이상이면 물이 나오게 할 수도 있습니다. ReLU는 특히 이런 느낌과 비슷합니다. 0보다 작으면 꺼지고, 0보다 크면 그대로 통과합니다.

### 아주 쉬운 예시

ReLU를 작은 숫자로 보겠습니다.

```text
ReLU(x) = max(0, x)
```

입력이 다음과 같다면:

```text
x = [-2, -1, 0, 3]
```

ReLU를 적용하면:

```text
ReLU(x) = [0, 0, 0, 3]
```

즉, 음수 신호는 끄고, 양수 신호는 살립니다.

이번에는 sigmoid를 보겠습니다. sigmoid는 값을 0과 1 사이로 바꿉니다.

```text
sigmoid(-5) ≈ 0.01
sigmoid(0)  = 0.5
sigmoid(5)  ≈ 0.99
```

그래서 sigmoid는 “확률처럼 해석하고 싶은 값”에 자주 등장합니다. 예를 들어 binary classification에서 “스팸일 확률”을 0과 1 사이 값으로 만들 때 사용할 수 있습니다.

하지만 sigmoid에는 saturation 문제가 있습니다. 입력이 너무 크거나 너무 작으면 출력이 거의 1이나 0에 붙어버립니다. 이 구간에서는 값이 조금 변해도 출력이 거의 변하지 않아서 gradient가 작아질 수 있습니다. 그러면 학습이 느려질 수 있습니다.

### 개념 구조와 핵심 포인트

activation function의 역할은 크게 네 가지입니다.

1. **nonlinearity를 넣습니다.** 신경망이 직선적인 관계를 넘어 복잡한 패턴을 표현할 수 있게 합니다.
2. **신호를 선택적으로 통과시킵니다.** ReLU는 음수 신호를 0으로 만들고 양수 신호만 통과시킵니다.
3. **출력 범위를 조절합니다.** sigmoid는 0~1, tanh는 -1~1 범위로 값을 눌러줍니다.
4. **gradient 흐름에 영향을 줍니다.** 학습은 gradient를 이용해 weight를 바꾸므로, activation function이 gradient를 너무 작게 만들면 학습이 어려워질 수 있습니다.

각 activation의 느낌은 다음과 같습니다.

- **ReLU**: 단순하고 빠르며 deep neural network에서 널리 쓰입니다.
- **sigmoid**: 0~1 범위가 필요할 때 유용하지만 saturation에 주의해야 합니다.
- **tanh**: -1~1 범위로 중심이 0에 가까워 sigmoid보다 나은 경우가 있지만, 역시 saturation 문제가 있습니다.

현대 LLM에서는 ReLU만 쓰는 것이 아니라 GELU, SwiGLU 같은 activation 변형도 많이 씁니다. 하지만 처음에는 ReLU, sigmoid, tanh를 이해하는 것이 가장 좋은 출발점입니다.

### 핵심 수학 포인트

activation function은 각 원소에 독립적으로 적용되는 경우가 많습니다. 예를 들어 vector가 있습니다.

```text
z = [-2, 0.5, 3]
```

ReLU를 적용하면 각 원소마다 따로 계산합니다.

```text
a = [ReLU(-2), ReLU(0.5), ReLU(3)]
  = [0, 0.5, 3]
```

수학적으로 중요한 점은 activation function의 기울기입니다. 학습에서는 loss를 줄이기 위해 gradient를 뒤로 전달합니다. 이때 activation function의 기울기가 너무 작으면 앞쪽 layer까지 학습 신호가 잘 전달되지 않습니다.

sigmoid를 예로 들면, 입력이 0 근처일 때는 출력이 잘 변합니다. 하지만 입력이 10처럼 너무 크면 출력은 거의 1입니다. 11이 되어도 여전히 거의 1입니다. 출력 변화가 작다는 것은 gradient도 작다는 뜻이고, 이것이 saturation 문제입니다.

ReLU는 양수 구간에서 기울기가 1이라 gradient가 비교적 잘 흐릅니다. 그래서 깊은 신경망에서 오랫동안 많이 쓰였습니다. 다만 음수 구간에서는 기울기가 0이므로, 어떤 뉴런이 계속 음수만 내면 학습이 멈춘 듯한 상태가 될 수 있습니다. 이를 dead ReLU 문제라고 부르기도 합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **activation function**: linear layer의 출력에 적용해 nonlinearity를 넣는 함수입니다.
- **ReLU**: Rectified Linear Unit. `max(0, x)`로 계산하는 대표 activation입니다.
- **sigmoid**: 값을 0과 1 사이로 바꾸는 S자 모양 함수입니다.
- **tanh**: 값을 -1과 1 사이로 바꾸는 함수입니다.
- **saturation**: 입력이 너무 크거나 작아서 출력이 거의 변하지 않는 상태입니다.
- **gradient**: loss를 줄이기 위해 weight를 어느 방향으로 바꿔야 하는지 알려주는 변화율입니다.
- **dead ReLU**: ReLU 뉴런이 계속 음수 입력을 받아 출력과 gradient가 0에 가까워지는 문제입니다.

### AI에서 어디에 쓰이는가

activation function은 거의 모든 deep learning model에서 핵심적으로 쓰입니다.

- **이미지 모델**: CNN이나 vision model에서 feature를 단계적으로 추출할 때 사용됩니다.
- **LLM의 MLP block**: Transformer 내부 feed-forward network에서 GELU, SwiGLU 같은 activation이 hidden state를 변환합니다.
- **classification**: sigmoid는 binary classification에서 확률 출력으로 자주 사용됩니다.
- **representation learning**: activation이 없으면 embedding이나 hidden state가 충분히 복잡한 표현으로 바뀌기 어렵습니다.
- **gradient 기반 학습**: activation function의 모양은 gradient 흐름과 학습 안정성에 직접 영향을 줍니다.

실전에서는 activation function 선택이 모델 성능과 학습 속도에 영향을 줄 수 있습니다. 특히 깊은 모델에서는 gradient가 잘 흐르는지가 중요합니다. 그래서 단순히 “어떤 함수가 예쁘게 생겼나”가 아니라, “학습이 잘 되는가”라는 관점에서 activation을 봐야 합니다.

### 헷갈리기 쉬운 포인트

- **activation function은 단순한 장식이 아닙니다.** 없으면 deep network가 복잡한 패턴을 표현하기 어렵습니다.
- **sigmoid는 항상 좋은 확률 함수가 아닙니다.** 출력이 0~1이라 편리하지만, 중간 layer에서 많이 쓰면 saturation 때문에 학습이 느려질 수 있습니다.
- **ReLU도 완벽하지 않습니다.** 음수 구간에서 gradient가 0이라 dead ReLU 문제가 생길 수 있습니다.
- **activation과 최종 출력 함수는 구분해야 합니다.** hidden layer에서는 ReLU/GELU 등을 쓰고, 마지막 classification에서는 sigmoid나 softmax를 쓰는 식으로 목적이 다를 수 있습니다.

---

## 복습 질문 3개

1. 퍼셉트론에서 weighted sum과 threshold는 각각 어떤 역할을 하나요?
2. MLP에서 activation function이 없다면 여러 layer를 쌓아도 왜 한계가 생기나요?
3. sigmoid의 saturation 문제는 gradient 기반 학습에서 왜 문제가 될 수 있나요?

## 오늘의 한 줄 요약

신경망은 input을 weight로 선형결합하고 activation function으로 비선형성을 넣으며, 여러 hidden layer를 통해 점점 더 유용한 표현을 학습합니다.

---

# Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 13/30]

오늘은 퍼셉트론, MLP, 활성화함수가 왜 신경망의 기본 뼈대가 되는지 차근차근 복습해볼게요.

### 1. 퍼셉트론에서 weighted sum과 threshold는 각각 어떤 역할을 하나요?

**정답**

weighted sum은 여러 입력값을 각각의 중요도인 weight와 곱한 뒤 모두 더해서 하나의 판단 점수를 만드는 역할을 합니다.

threshold는 그 판단 점수가 기준을 넘었는지 확인해서 최종 출력을 결정하는 기준선 역할을 합니다.

쉽게 말하면:

- weighted sum: “여러 증거를 중요도에 따라 합산한 점수”
- threshold: “이 점수가 충분히 높은지 판단하는 기준”

입니다.

**설명**

퍼셉트론(perceptron)은 가장 기본적인 인공 뉴런입니다. 퍼셉트론은 입력을 그냥 더하지 않습니다. 각 입력이 얼마나 중요한지 나타내는 weight를 곱한 뒤 더합니다. 이것을 weighted sum이라고 합니다.

예를 들어 스팸 메일을 판단한다고 하면, 모델은 다음과 같은 신호를 볼 수 있습니다.

- 광고 단어가 많은가?
- 모르는 사람이 보냈는가?
- 링크가 많은가?

이 세 가지가 모두 똑같이 중요하지는 않습니다. 어떤 신호는 더 중요하고, 어떤 신호는 덜 중요합니다. 그래서 weight가 필요합니다.

weighted sum은 보통 이런 형태입니다.

```text
z = w1*x1 + w2*x2 + w3*x3 + b
```

여기서 `z`가 판단 점수입니다. 이 점수가 threshold를 넘으면 “예”, 넘지 못하면 “아니오”처럼 결정할 수 있습니다.

threshold는 문지방 같은 역할을 합니다. 점수가 문지방보다 높으면 통과하고, 낮으면 통과하지 못합니다.

**예시**

학생이 시험에 통과할지 판단한다고 해봅시다.

입력은 두 개입니다.

```text
x1 = 공부 시간
x2 = 충분히 잤는가
```

weight와 bias가 다음과 같다고 해봅시다.

```text
w1 = 0.6
w2 = 1.0
b = -2.0
```

학생이 2시간 공부했고 충분히 잤다면:

```text
z = 0.6*2 + 1.0*1 - 2.0
  = 1.2 + 1.0 - 2.0
  = 0.2
```

threshold를 0으로 두면 `z = 0.2`는 0보다 크므로 통과입니다.

반대로 2시간 공부했지만 잠을 못 잤다면:

```text
z = 0.6*2 + 1.0*0 - 2.0
  = 1.2 + 0 - 2.0
  = -0.8
```

이 경우 threshold 0을 넘지 못하므로 통과하지 못합니다.

즉, weighted sum은 여러 조건을 하나의 점수로 만들고, threshold는 그 점수를 보고 결정을 내립니다.

**실전 연결**

딥러닝의 linear layer는 기본적으로 `Wx + b` 계산을 합니다. 이것은 퍼셉트론의 weighted sum과 같은 핵심 구조입니다. LLM에서도 token embedding이 여러 layer를 지나며 weight matrix와 곱해지고, 새로운 hidden state로 바뀝니다. 즉, 퍼셉트론의 weighted sum을 이해하면 neural network 내부에서 “입력이 weight를 통해 새로운 표현으로 변환된다”는 핵심 감각을 잡을 수 있습니다.

### 2. MLP에서 activation function이 없다면 여러 layer를 쌓아도 왜 한계가 생기나요?

**정답**

activation function이 없으면 여러 layer를 쌓아도 전체 계산은 결국 하나의 큰 linear transformation, 즉 하나의 선형변환과 비슷해집니다.

그래서 layer가 많아 보여도 복잡하게 휘어진 패턴이나 비선형적인 관계를 잘 표현하지 못합니다.

즉, MLP가 강력해지려면 layer 사이에 activation function을 넣어서 nonlinearity, 즉 비선형성을 만들어야 합니다.

**설명**

MLP, 즉 Multi-Layer Perceptron은 여러 layer를 쌓은 신경망입니다. 구조는 보통 이렇게 생겼습니다.

```text
input layer → hidden layer → hidden layer → output layer
```

여기서 hidden layer는 입력을 중간 표현으로 바꾸는 역할을 합니다. 하지만 중요한 조건이 있습니다. 각 layer 사이에 activation function이 있어야 합니다.

왜냐하면 linear layer만 계속 쌓으면 다음과 같은 일이 생기기 때문입니다.

```text
첫 번째 layer: h = W1*x + b1
두 번째 layer: y = W2*h + b2
```

이 둘을 합치면 결국:

```text
y = W2*(W1*x + b1) + b2
```

형태가 됩니다. 복잡해 보이지만 전체적으로는 여전히 `x`에 어떤 큰 weight를 곱하고 bias를 더한 선형변환입니다.

쉽게 말해, 직선으로 한 번 나누는 일을 여러 번 반복해도 activation이 없으면 결국 더 복잡한 곡선 경계를 만들기 어렵습니다.

activation function은 중간에 “꺾임”을 넣습니다. ReLU 같은 함수는 음수는 0으로 만들고 양수는 그대로 통과시킵니다. 이런 꺾임 덕분에 모델은 단순한 직선이 아니라 여러 조각으로 이루어진 복잡한 패턴을 표현할 수 있습니다.

**예시**

아주 단순한 문제를 생각해봅시다.

우리가 원하는 규칙은 다음과 같습니다.

```text
x가 -1 근처이면 좋다.
x가 0 근처이면 별로다.
x가 +1 근처이면 좋다.
```

이 패턴은 가운데는 낮고 양쪽은 높은 모양입니다. 직선 하나로는 표현하기 어렵습니다.

단일 선형모델은 보통 이런 식으로만 판단할 수 있습니다.

```text
x가 커질수록 점수가 커진다
또는
x가 작아질수록 점수가 커진다
```

하지만 우리가 원하는 것은 “양쪽 끝은 좋고 가운데는 나쁨”입니다.

이때 hidden layer와 activation function이 있으면 뉴런들이 역할을 나눌 수 있습니다.

```text
뉴런 A: x가 0.5보다 크면 반응
뉴런 B: x가 -0.5보다 작으면 반응
출력층: A나 B가 반응하면 좋은 점수
```

이렇게 여러 뉴런과 activation이 함께 작동하면 단순한 직선보다 훨씬 다양한 모양을 만들 수 있습니다.

**실전 연결**

LLM의 Transformer block 안에도 MLP 또는 feed-forward network가 들어갑니다. attention이 token 사이의 관계를 섞는 역할을 한다면, MLP는 각 token의 hidden state를 더 풍부한 표현으로 바꿉니다. 이때 activation function이 없으면 표현력이 크게 제한됩니다. 그래서 실제 LLM에서는 ReLU뿐 아니라 GELU, SwiGLU 같은 activation이 사용됩니다. activation은 단순한 부품이 아니라 모델이 복잡한 언어 패턴을 배우게 하는 핵심 장치입니다.

### 3. sigmoid의 saturation 문제는 gradient 기반 학습에서 왜 문제가 될 수 있나요?

**정답**

sigmoid의 saturation 문제는 입력값이 너무 크거나 너무 작을 때 출력이 거의 1이나 0에 붙어서 잘 변하지 않는 현상입니다.

출력이 거의 변하지 않으면 gradient, 즉 loss를 줄이기 위해 weight를 어느 방향으로 얼마나 바꿔야 하는지 알려주는 변화율도 매우 작아질 수 있습니다.

gradient가 작아지면 앞쪽 layer까지 학습 신호가 잘 전달되지 않아 학습이 느려지거나 어려워집니다.

**설명**

sigmoid는 값을 0과 1 사이로 바꿔주는 activation function입니다.

```text
sigmoid(-5) ≈ 0.01
sigmoid(0)  = 0.5
sigmoid(5)  ≈ 0.99
```

이 성질 때문에 sigmoid는 “확률처럼 해석하고 싶은 값”을 만들 때 유용합니다. 예를 들어 binary classification에서 “스팸일 확률”을 0과 1 사이로 표현할 수 있습니다.

하지만 중간 layer에서 sigmoid를 많이 쓰면 문제가 생길 수 있습니다.

입력이 아주 큰 양수이면 sigmoid 출력은 거의 1입니다. 예를 들어 입력이 5여도 0.99에 가깝고, 입력이 10이어도 거의 1입니다. 즉, 입력이 더 커져도 출력이 거의 변하지 않습니다.

입력이 아주 작은 음수일 때도 마찬가지입니다. 출력이 거의 0에 붙습니다.

이렇게 출력이 0이나 1 근처에 붙어서 변화가 거의 없는 상태를 saturation이라고 합니다.

gradient 기반 학습에서는 gradient가 중요합니다. gradient는 “loss function을 줄이려면 weight를 어느 방향으로 바꿔야 하는가”를 알려주는 신호입니다. 그런데 sigmoid가 saturation 상태에 들어가면 출력 변화가 작아지고, 그에 따라 gradient도 작아집니다.

gradient가 너무 작으면 optimizer가 weight를 조금밖에 업데이트하지 못합니다. 특히 깊은 신경망에서는 뒤쪽 layer에서 시작된 gradient가 앞쪽 layer로 전달되면서 점점 작아질 수 있습니다. 이것이 vanishing gradient 문제와 연결됩니다.

**예시**

온도 조절 다이얼을 생각해봅시다.

다이얼이 중간에 있을 때는 조금만 돌려도 온도가 잘 바뀝니다. 이것은 sigmoid 입력이 0 근처일 때와 비슷합니다. 출력이 민감하게 변합니다.

그런데 다이얼이 이미 최대치에 거의 붙어 있다면, 조금 더 돌려도 온도가 거의 변하지 않습니다. 이것이 sigmoid saturation과 비슷합니다.

숫자로 보면:

```text
sigmoid(0) = 0.5
sigmoid(1) ≈ 0.73
```

0에서 1로 바뀌면 출력이 꽤 변합니다.

하지만:

```text
sigmoid(10) ≈ 0.99995
sigmoid(11) ≈ 0.99998
```

10에서 11로 바뀌어도 출력은 거의 그대로입니다.

출력이 거의 그대로라는 것은 gradient도 작다는 뜻입니다. 그러면 모델이 “어떻게 고쳐야 하는지”를 배우기 어려워집니다.

**실전 연결**

딥러닝 모델은 보통 backpropagation으로 gradient를 뒤로 전달하면서 학습합니다. activation function이 gradient를 너무 작게 만들면 앞쪽 layer의 weight가 잘 업데이트되지 않습니다. 그래서 깊은 모델의 hidden layer에서는 sigmoid보다 ReLU, GELU, SwiGLU 같은 activation을 더 많이 사용합니다. 다만 sigmoid는 여전히 binary classification의 마지막 출력처럼 0~1 확률이 필요한 곳에서는 중요하게 쓰입니다. 핵심은 “sigmoid가 나쁘다”가 아니라, 어디에 쓰느냐가 중요하다는 점입니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-05-day13.md
