# AI/ML Learning Review Source — 2026-05-11 Day 19

- Lesson source: `/home/ubuntu/work/ai/learning/logs/2026-05-11-day19.md`
- Follow-up answer source: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-11_09-26-55.md`

---

## Lesson

# Day 19 - AI/ML 기초 학습

- Date: 2026-05-11
- Progress: 19/30
- Level: beginner-intermediate
- Milestone: 시퀀스 모델과 어텐션
- Milestone goal: 순서가 있는 데이터를 다루는 모델과 attention의 등장 배경을 이해한다.

## Today's 3 concepts

1. 시퀀스 데이터와 autoregressive 관점
2. RNN의 recurrent state
3. BPTT와 장기 의존성 문제

---

## 1. 시퀀스 데이터와 autoregressive 관점

### 한 줄 직관

시퀀스(sequence)는 “순서가 중요한 데이터”이고, autoregressive 관점은 “지금까지 본 내용을 바탕으로 다음 것을 하나씩 예측한다”는 생각입니다.

### 개념 정의

시퀀스 데이터(sequence data)는 데이터의 순서가 의미를 가지는 데이터입니다. 문장, 음성, 주가, 센서 기록, 클릭 로그처럼 “앞에 무엇이 있었는가”가 뒤의 의미를 바꿉니다.

예를 들어 `나는 밥을` 다음에는 `먹었다`가 자연스럽지만, `먹었다 나는 밥을`처럼 순서를 바꾸면 어색합니다. 단어는 같아도 순서가 달라지면 의미와 자연스러움이 달라집니다.

시퀀스에서 각 위치를 time step이라고 부릅니다. 꼭 시간이 흐르는 데이터가 아니어도 됩니다. 문장에서 첫 번째 단어, 두 번째 단어, 세 번째 단어도 time step으로 볼 수 있습니다.

Autoregressive는 어려워 보이는 말이지만 핵심은 단순합니다.

> 이전까지의 출력 또는 입력을 context로 삼아 다음 값을 예측하는 방식

LLM이 문장을 생성할 때도 이 방식을 많이 씁니다. 예를 들어 모델이 `오늘 날씨가`를 보고 다음 token으로 `좋다`를 예측하고, 그다음에는 `오늘 날씨가 좋다` 전체를 context로 삼아 다음 token을 예측합니다.

### 왜 이런 개념이 필요한가

이미지 분류처럼 입력 전체를 한 번에 보고 답을 내는 문제도 있지만, 많은 AI 문제는 순서가 중요합니다.

- 문장 생성: 앞 단어를 보고 다음 단어를 예측해야 합니다.
- 번역: 앞뒤 문맥을 보고 단어 의미를 결정해야 합니다.
- 음성 인식: 앞 소리와 뒤 소리의 흐름이 단어를 결정합니다.
- 주가나 센서 예측: 과거 흐름이 다음 값의 힌트가 됩니다.
- 추천 시스템: 사용자가 이전에 클릭한 순서가 다음 관심사를 바꿉니다.

즉 시퀀스 모델은 “데이터 하나하나”보다 “흐름”을 배우는 모델입니다. Autoregressive 관점은 이 흐름을 가장 기본적인 예측 문제로 바꿔 줍니다.

> 지금까지의 context가 주어졌을 때, 다음 값은 무엇인가?

이 질문 하나로 문장 생성, 코드 생성, 음악 생성, 시계열 예측 같은 문제를 다룰 수 있습니다.

### 아주 쉬운 예시

숫자 시퀀스를 생각해 봅시다.

```text
1, 2, 3, ?
```

사람은 자연스럽게 `4`를 떠올립니다. 왜냐하면 앞의 context `1, 2, 3`에서 “1씩 증가한다”는 패턴을 봤기 때문입니다.

조금 더 autoregressive하게 보면 다음과 같습니다.

```text
context: 1        → next: 2
context: 1, 2     → next: 3
context: 1, 2, 3  → next: 4
```

문장도 비슷합니다.

```text
context: 나는
next 후보: 밥을, 학교에, 오늘

context: 나는 밥을
next 후보: 먹었다, 샀다, 만들었다
```

`나는`만 봤을 때보다 `나는 밥을`까지 봤을 때 다음 단어를 더 정확히 예측할 수 있습니다. 이 “지금까지의 정보”가 context입니다.

### 개념 구조와 핵심 포인트

시퀀스 데이터는 보통 다음처럼 표현합니다.

```text
x1, x2, x3, ..., xt
```

여기서 `x1`은 첫 번째 time step의 입력, `x2`는 두 번째 time step의 입력입니다. 문장이라면 각 `x`는 단어 또는 token이 될 수 있고, 실제 모델 안에서는 embedding vector로 바뀝니다.

예를 들어 문장 `나는 밥을 먹었다`를 token 단위로 보면 다음과 같습니다.

```text
time step 1: 나는
time step 2: 밥을
time step 3: 먹었다
```

모델 내부에서는 각 token이 숫자 벡터인 embedding으로 변환됩니다.

```text
나는   → [0.2, -0.1, 0.7]
밥을   → [0.5,  0.3, 0.1]
먹었다 → [0.4, -0.2, 0.6]
```

실전에서는 embedding 차원이 3이 아니라 768, 4096, 8192처럼 훨씬 큽니다. 하지만 핵심은 같습니다. 단어를 숫자 벡터로 바꾼 뒤, 그 벡터들의 순서를 모델이 처리합니다.

Autoregressive 모델은 다음 확률을 배웁니다.

```text
P(다음 token | 지금까지의 context)
```

즉 “context가 주어졌을 때 다음 token의 확률 분포”를 예측합니다. 예를 들어 `나는 밥을` 다음에 대해 모델은 이런 확률을 낼 수 있습니다.

```text
먹었다: 0.70
샀다:   0.15
봤다:   0.03
그리고: 0.01
기타:   0.11
```

그다음 실제 정답이 `먹었다`였다면 loss는 `먹었다`의 확률이 높을수록 작아지고, 낮을수록 커집니다. 학습은 이 loss를 줄이는 방향으로 진행됩니다.

### 핵심 수학 포인트

시퀀스 전체의 확률은 “각 time step에서 다음 값을 맞히는 확률”의 곱으로 나눠 볼 수 있습니다.

문장 token이 `x1, x2, x3`라고 하면 autoregressive 관점에서는 다음처럼 봅니다.

```text
P(x1, x2, x3) = P(x1) × P(x2 | x1) × P(x3 | x1, x2)
```

말로 풀면 이렇습니다.

1. 첫 token `x1`이 나올 확률
2. `x1`을 본 뒤 `x2`가 나올 확률
3. `x1, x2`를 본 뒤 `x3`가 나올 확률

아주 작은 예시를 봅시다.

```text
P(나는) = 0.10
P(밥을 | 나는) = 0.30
P(먹었다 | 나는, 밥을) = 0.70
```

그러면 `나는 밥을 먹었다`라는 짧은 문장의 확률은 단순화해서 다음처럼 계산할 수 있습니다.

```text
0.10 × 0.30 × 0.70 = 0.021
```

실제 학습에서는 곱셈을 그대로 쓰기보다 log probability를 더하고, 정답 token의 확률을 높이도록 cross-entropy loss를 줄입니다. 하지만 초반에는 이렇게 이해하면 충분합니다.

> 시퀀스 학습은 “각 위치에서 다음 것을 맞히는 훈련”으로 볼 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- sequence: 순서가 중요한 데이터입니다. 문장, 음성, 시계열 데이터가 대표적입니다.
- time step: 시퀀스 안의 한 위치입니다. 문장에서는 각 token 위치, 시계열에서는 각 시간 지점입니다.
- autoregressive: 이전 context를 이용해 다음 값을 하나씩 예측하는 방식입니다.
- context: 현재 예측에 사용되는 앞선 정보입니다. LLM에서는 보통 지금까지 입력된 token들이 context입니다.

### AI에서 어디에 쓰이는가

Autoregressive 관점은 LLM의 핵심적인 생성 방식과 직접 연결됩니다. ChatGPT 같은 모델은 한 번에 긴 답변 전체를 “통째로” 뱉는 것이 아니라, 내부적으로는 다음 token을 반복해서 예측합니다.

예를 들어 다음과 같은 과정입니다.

```text
입력: 머신러닝은
예측: 데이터를
새 context: 머신러닝은 데이터를
예측: 통해
새 context: 머신러닝은 데이터를 통해
예측: 패턴을
...
```

코드 생성 모델도 비슷합니다. `for i in range(`까지 보면 다음에 숫자나 변수, 닫는 괄호가 올 가능성을 계산합니다.

또한 autoregressive 관점은 loss 설계에도 중요합니다. 모델은 각 time step에서 정답 token에 높은 확률을 주도록 학습됩니다. 그래서 데이터셋을 만들 때도 보통 입력 token을 한 칸 밀어서 target token을 만듭니다.

### 헷갈리기 쉬운 포인트

- Autoregressive는 “무조건 RNN”이라는 뜻이 아닙니다. RNN도 autoregressive하게 쓸 수 있고, Transformer decoder도 autoregressive하게 쓸 수 있습니다.
- 시퀀스는 꼭 시간 데이터만 뜻하지 않습니다. 문장, DNA 염기서열, 코드, 음악도 sequence입니다.
- context가 길수록 항상 좋은 것은 아닙니다. 긴 context를 잘 활용하려면 모델 구조와 학습이 뒷받침되어야 합니다.
- 다음 token을 예측한다고 해서 모델이 “진짜 의미를 사람처럼 이해한다”고 단정할 수는 없습니다. 다만 매우 많은 next-token prediction을 통해 복잡한 패턴과 개념을 학습할 수 있습니다.

---

## 2. RNN의 recurrent state

### 한 줄 직관

RNN은 시퀀스를 왼쪽에서 오른쪽으로 읽으면서, 지금까지 본 내용을 hidden state라는 작은 메모리에 계속 업데이트하는 모델입니다.

### 개념 정의

RNN(Recurrent Neural Network)은 순서가 있는 데이터를 처리하기 위한 neural network 구조입니다. 핵심은 recurrence, 즉 “이전 상태를 다시 사용한다”는 점입니다.

일반적인 feedforward network는 입력을 한 번 넣고 출력이 나오면 끝입니다. 하지만 RNN은 매 time step마다 다음 두 가지를 함께 봅니다.

1. 현재 입력 `xt`
2. 이전까지의 요약 정보인 hidden state `h(t-1)`

그리고 새로운 hidden state `ht`를 만듭니다.

```text
현재 입력 xt + 이전 hidden state h(t-1) → 새로운 hidden state ht
```

이 hidden state는 “지금까지 읽은 내용을 요약한 메모리”라고 생각하면 됩니다.

### 왜 이런 개념이 필요한가

시퀀스에서는 현재 입력만 보면 부족한 경우가 많습니다.

예를 들어 문장을 봅시다.

```text
나는 어제 너무 배가 고파서 김밥을
```

마지막 단어 다음을 예측하려면 바로 앞의 `김밥을`도 중요하지만, 앞쪽의 `배가 고파서`도 중요합니다. 사람은 앞에서 읽은 내용을 머릿속에 기억합니다. RNN의 hidden state는 이런 기억 역할을 하려고 만든 장치입니다.

숫자 예측에서도 마찬가지입니다.

```text
2, 4, 6, ?
```

현재 `6`만 보면 다음이 무엇인지 확실하지 않습니다. 하지만 이전 값 `2, 4`까지 기억하면 “2씩 증가한다”는 패턴을 알 수 있습니다. RNN은 이전 정보가 hidden state에 담기기를 기대합니다.

### 아주 쉬운 예시

아주 단순한 RNN을 손으로 상상해 봅시다. 입력 숫자를 하나씩 읽고, hidden state에 지금까지의 합을 저장한다고 합시다.

```text
sequence: 1, 2, 3
처음 hidden state h0 = 0
```

각 time step에서 state update를 이렇게 한다고 해봅시다.

```text
새 hidden state = 이전 hidden state + 현재 입력
```

그러면 다음과 같습니다.

```text
time step 1: x1 = 1, h0 = 0 → h1 = 0 + 1 = 1
time step 2: x2 = 2, h1 = 1 → h2 = 1 + 2 = 3
time step 3: x3 = 3, h2 = 3 → h3 = 3 + 3 = 6
```

마지막 hidden state `h3 = 6`은 지금까지 본 숫자의 합을 담고 있습니다.

실제 RNN은 단순히 합만 저장하지 않습니다. weight matrix, bias, activation function을 사용해서 더 복잡한 정보를 hidden state에 담습니다. 하지만 직관은 같습니다.

> 매 time step마다 hidden state를 업데이트해서 과거 정보를 다음 step으로 넘긴다.

### 개념 구조와 핵심 포인트

RNN의 기본 구조는 다음과 같습니다.

```text
x1 → [RNN cell] → h1
x2 → [RNN cell] → h2
x3 → [RNN cell] → h3
```

그런데 각 RNN cell은 따로 떨어져 있지 않습니다. 같은 파라미터를 공유합니다. 즉 time step 1에서도, 2에서도, 3에서도 같은 규칙으로 state update를 합니다.

기본 RNN의 state update는 보통 다음처럼 씁니다.

```text
ht = tanh(Wx xt + Wh h(t-1) + b)
```

처음 보면 복잡하지만 하나씩 보면 어렵지 않습니다.

- `xt`: 현재 time step의 입력 vector입니다.
- `h(t-1)`: 이전 hidden state입니다.
- `Wx`: 현재 입력을 hidden state 공간으로 바꾸는 weight입니다.
- `Wh`: 이전 hidden state를 새 hidden state에 반영하는 weight입니다.
- `b`: bias입니다.
- `tanh`: 값을 너무 커지지 않게 -1에서 1 사이로 눌러 주는 activation function입니다.

Tensor shape로 감을 잡아 봅시다.

```text
batch_size = 2
sequence_length = 4
embedding_dim = 3
hidden_dim = 5
```

입력 tensor는 보통 다음 shape를 가질 수 있습니다.

```text
X shape: [2, 4, 3]
```

뜻은 이렇습니다.

- 2개 문장을 한 번에 처리합니다.
- 각 문장은 4개 time step을 가집니다.
- 각 token embedding은 3차원입니다.

RNN은 각 time step을 처리하며 hidden state를 만듭니다.

```text
hidden state shape: [2, 5]
```

즉 각 문장마다 5차원짜리 메모리를 유지하는 것입니다.

### 핵심 수학 포인트

가장 중요한 수학 포인트는 같은 함수를 반복 적용한다는 것입니다.

```text
h1 = f(x1, h0)
h2 = f(x2, h1)
h3 = f(x3, h2)
```

여기서 `f`가 RNN cell입니다. 같은 `f`를 반복해서 쓰기 때문에 recurrent하다고 부릅니다.

아주 작은 1D 예시로 보겠습니다. 실제 RNN은 vector지만, 먼저 숫자 하나짜리 hidden state로 이해해도 됩니다.

```text
ht = tanh(0.5 × xt + 0.8 × h(t-1))
```

입력이 `x1 = 1`, `x2 = 2`이고 `h0 = 0`이라고 합시다.

```text
h1 = tanh(0.5 × 1 + 0.8 × 0)
   = tanh(0.5)
   ≈ 0.46

h2 = tanh(0.5 × 2 + 0.8 × 0.46)
   = tanh(1.0 + 0.368)
   = tanh(1.368)
   ≈ 0.88
```

여기서 `h2`는 `x2`만 반영한 값이 아닙니다. `h1`을 통해 `x1`의 정보도 반영되어 있습니다.

이 점이 RNN의 핵심입니다.

> 현재 hidden state는 현재 입력과 과거 hidden state가 섞인 결과다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- RNN: Recurrent Neural Network입니다. 이전 state를 다음 step에 넘기며 시퀀스를 처리하는 neural network입니다.
- hidden state: 지금까지 본 정보를 요약한 내부 memory vector입니다.
- recurrence: 같은 구조나 규칙이 반복되며 이전 결과를 다시 사용하는 성질입니다.
- state update: 현재 입력과 이전 state로 새로운 state를 계산하는 과정입니다.

### AI에서 어디에 쓰이는가

RNN은 Transformer가 널리 쓰이기 전까지 NLP, 음성, 시계열 모델링에서 매우 중요한 기본 구조였습니다.

예전에는 다음과 같은 문제에 많이 쓰였습니다.

- 문장 감정 분류: 문장을 순서대로 읽고 마지막 hidden state로 긍정/부정을 분류합니다.
- 기계 번역: encoder RNN이 원문을 읽고, decoder RNN이 번역문을 생성합니다.
- 음성 인식: 소리 특징을 시간 순서대로 처리합니다.
- 시계열 예측: 과거 센서 값으로 다음 값을 예측합니다.

현대 LLM의 중심은 Transformer지만, RNN의 hidden state 개념은 여전히 중요합니다. 왜냐하면 hidden state는 “과거 정보를 압축해서 다음 계산에 넘긴다”는 생각을 보여주기 때문입니다. Attention을 이해할 때도 RNN의 한계를 먼저 이해하면 “왜 attention이 등장했는가”가 훨씬 잘 보입니다.

### 헷갈리기 쉬운 포인트

- hidden state는 사람이 직접 의미를 정해 넣은 메모리가 아닙니다. 학습 과정에서 loss를 줄이도록 자동으로 형성되는 vector입니다.
- hidden state가 있다고 해서 모든 과거를 완벽히 기억하는 것은 아닙니다. 차원이 제한되어 있고, 업데이트를 반복하면서 오래된 정보가 약해질 수 있습니다.
- RNN은 time step을 순서대로 처리하기 때문에 긴 문장을 병렬 처리하기 어렵습니다. Transformer가 강력해진 이유 중 하나가 이 병렬화 문제를 크게 개선했기 때문입니다.
- 마지막 hidden state만 사용하면 앞부분 정보가 충분히 보존되지 않을 수 있습니다. 이 문제가 attention의 필요성과 연결됩니다.

---

## 3. BPTT와 장기 의존성 문제

### 한 줄 직관

BPTT는 RNN을 시간 방향으로 길게 펼쳐서 학습시키는 방법이고, 장기 의존성 문제는 멀리 떨어진 중요한 정보가 학습 중에 잘 전달되지 않는 문제입니다.

### 개념 정의

BPTT(Backpropagation Through Time)는 RNN을 학습시키기 위해 사용하는 backpropagation 방식입니다.

일반 neural network는 layer가 여러 개 쌓여 있고, loss에서 시작한 gradient가 뒤에서 앞으로 이동하며 weight를 업데이트합니다. RNN은 시간 step마다 같은 cell이 반복됩니다. 그래서 학습할 때는 RNN을 시간 방향으로 펼친 것처럼 생각합니다.

예를 들어 3개의 time step이 있다면 다음처럼 펼쳐 봅니다.

```text
x1 → RNN cell → h1 →
x2 → RNN cell → h2 →
x3 → RNN cell → h3 → loss
```

BPTT는 loss에서 시작한 gradient를 `h3 → h2 → h1` 방향으로 거슬러 보내며, 각 time step에 영향을 준 weight를 업데이트합니다.

장기 의존성(long-term dependency)은 시퀀스에서 멀리 떨어진 정보가 현재 예측에 중요한 경우를 말합니다.

예를 들어 문장 앞에서 나온 주어가 문장 끝의 동사 선택에 영향을 주거나, 긴 대화의 초반 조건이 후반 답변에 영향을 주는 경우입니다.

### 왜 이런 개념이 필요한가

RNN이 좋은 모델이 되려면 과거 정보를 hidden state에 담는 것뿐 아니라, 학습 중에 “어떤 과거 정보가 중요했는지”를 잘 배워야 합니다.

그런데 긴 시퀀스에서는 문제가 생깁니다.

- 앞쪽 time step이 뒤쪽 loss에 영향을 주려면 gradient가 먼 길을 거슬러 가야 합니다.
- 이 과정에서 gradient가 점점 작아지면 앞쪽 정보는 거의 학습되지 않습니다.
- 반대로 gradient가 너무 커지면 학습이 불안정해질 수 있습니다.

이 때문에 RNN은 짧은 문맥은 잘 처리해도 긴 문맥을 다루는 데 어려움을 겪을 수 있습니다. 이 한계를 해결하려고 LSTM, GRU, attention, Transformer 같은 구조가 중요해졌습니다.

### 아주 쉬운 예시

긴 문장을 봅시다.

```text
철수는 아침에 집을 나서기 전에 가방 안에 노트북을 넣었고,
버스를 타고 학교에 도착한 뒤 강의실에 앉아서 과제를 하려고 했다.
철수가 꺼내야 할 것은 무엇인가?
```

정답은 `노트북`입니다. 그런데 `노트북`이라는 단어는 질문보다 훨씬 앞에 나왔습니다. 모델이 마지막 질문에 답하려면 앞쪽 정보를 오래 기억해야 합니다.

숫자 예시로도 볼 수 있습니다.

```text
첫 숫자가 1이면 마지막에 A를 출력하고,
첫 숫자가 0이면 마지막에 B를 출력하라.

입력: 1, 7, 3, 8, 2, 9, ?
정답: A
```

마지막 예측에 정말 중요한 정보는 바로 앞의 `9`가 아니라 맨 앞의 `1`입니다. 이런 것이 long-term dependency입니다.

RNN이 hidden state를 계속 업데이트하면서 맨 앞의 `1` 정보를 잃어버리면 마지막에 `A`를 맞히기 어렵습니다.

### 개념 구조와 핵심 포인트

BPTT는 RNN을 다음처럼 시간 방향으로 펼친 뒤 backpropagation을 한다고 생각하면 됩니다.

```text
forward:
h1 = f(x1, h0)
h2 = f(x2, h1)
h3 = f(x3, h2)
loss = L(h3, 정답)

backward:
loss → h3 → h2 → h1 → parameters
```

여기서 중요한 점은 `h1`이 `h2`에 영향을 주고, `h2`가 `h3`에 영향을 주고, `h3`가 loss에 영향을 준다는 것입니다. 그래서 loss를 줄이려면 gradient가 이 연결을 따라 뒤로 흐릅니다.

하지만 time step이 3개가 아니라 100개라면 어떨까요?

```text
loss → h100 → h99 → h98 → ... → h1
```

gradient가 너무 긴 경로를 지나야 합니다. 이때 gradient가 계속 작아지는 현상을 gradient decay 또는 vanishing gradient라고 부릅니다.

간단한 비유로 생각해 봅시다. 친구 100명을 거쳐 메시지를 전달한다고 합시다. 한 사람을 거칠 때마다 메시지의 90%만 정확히 전달된다면, 100명을 지나면 처음 메시지는 거의 사라집니다. gradient도 비슷하게 여러 step을 지나며 작아질 수 있습니다.

### 핵심 수학 포인트

핵심은 “작은 값을 여러 번 곱하면 매우 작아진다”입니다.

예를 들어 gradient가 한 time step을 거슬러 갈 때마다 `0.5`배가 된다고 합시다.

```text
1 step 전: 0.5
2 step 전: 0.5 × 0.5 = 0.25
3 step 전: 0.5 × 0.5 × 0.5 = 0.125
10 step 전: 0.5^10 ≈ 0.00098
```

10 step만 지나도 gradient가 거의 0에 가까워집니다. 그러면 앞쪽 time step의 weight가 “내가 loss에 영향을 줬구나”라는 신호를 거의 받지 못합니다. 이게 gradient decay입니다.

반대로 매 step마다 `1.5`배가 되면 어떨까요?

```text
1.5^10 ≈ 57.7
```

이번에는 gradient가 너무 커져서 업데이트가 폭주할 수 있습니다. 이를 exploding gradient라고 부릅니다. 오늘의 핵심은 gradient가 작아지는 쪽인 gradient decay지만, 두 문제는 함께 자주 등장합니다.

RNN의 state update에는 반복 곱셈이 숨어 있습니다. 정확한 식을 깊게 들어가지 않아도, backpropagation이 여러 time step을 지나면서 비슷한 weight와 activation의 영향을 반복해서 받는다는 점이 중요합니다.

> 긴 시퀀스에서는 gradient가 앞쪽까지 안정적으로 전달되어야 오래된 정보를 학습할 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- BPTT: Backpropagation Through Time입니다. RNN을 time step 방향으로 펼쳐서 gradient를 거슬러 보내는 학습 방법입니다.
- long-term dependency: 멀리 떨어진 과거 정보가 현재 예측에 중요한 관계입니다.
- gradient decay: gradient가 time step을 거슬러 갈수록 작아져 학습 신호가 약해지는 현상입니다. vanishing gradient라고도 자주 부릅니다.

### AI에서 어디에 쓰이는가

BPTT와 장기 의존성 문제는 시퀀스 모델 역사에서 매우 중요합니다.

RNN은 이론적으로 과거 정보를 hidden state에 담을 수 있지만, 실제 학습에서는 긴 문맥을 잘 배우기 어렵습니다. 그래서 다음과 같은 모델들이 등장했습니다.

- LSTM: gate를 사용해 중요한 정보를 더 오래 보존하려고 만든 RNN 변형입니다.
- GRU: LSTM보다 단순한 gate 구조로 정보를 조절합니다.
- Attention: 필요한 과거 위치를 직접 참고할 수 있게 만든 방식입니다.
- Transformer: attention을 중심으로 긴 context를 더 효과적으로 다루고 병렬화도 가능하게 만든 구조입니다.

LLM을 이해할 때도 이 흐름이 중요합니다. Transformer가 그냥 갑자기 나온 것이 아니라, RNN이 긴 문맥과 병렬 처리에서 어려움을 겪었고, attention이 그 문제를 해결하는 방향으로 발전했기 때문입니다.

실전 모델 학습에서는 gradient 문제를 줄이기 위해 다음 방법들도 씁니다.

- gradient clipping: gradient가 너무 커질 때 일정 크기로 자릅니다.
- residual connection: gradient가 더 쉽게 흐를 수 있는 우회 경로를 만듭니다.
- normalization: 값의 scale을 안정적으로 유지합니다.
- attention mechanism: 멀리 있는 정보에 직접 접근하게 합니다.

### 헷갈리기 쉬운 포인트

- BPTT는 새로운 optimizer 이름이 아닙니다. RNN에 backpropagation을 적용하는 방식입니다. 실제 weight 업데이트는 SGD, Adam 같은 optimizer가 담당합니다.
- long-term dependency는 단순히 “문장이 길다”는 뜻이 아닙니다. 멀리 있는 정보가 현재 예측에 실제로 중요할 때를 말합니다.
- gradient decay가 있으면 모델이 앞쪽 정보를 절대 못 쓰는 것은 아닙니다. 하지만 학습이 어려워지고, 긴 의존성을 안정적으로 배우기 힘들어집니다.
- LSTM/GRU가 문제를 완전히 끝낸 것은 아닙니다. 긴 context와 병렬화 문제 때문에 attention과 Transformer가 더 널리 쓰이게 되었습니다.

---

## 복습 질문 3개

1. Autoregressive 모델이 `P(다음 token | context)`를 예측한다는 말은 어떤 뜻인가요? 아주 짧은 문장 예시로 설명해 보세요.
2. RNN의 hidden state는 왜 필요한가요? 현재 입력만 보는 모델과 비교해서 설명해 보세요.
3. BPTT에서 gradient가 긴 time step을 거슬러 갈 때 왜 long-term dependency를 배우기 어려워질 수 있나요?

## 오늘의 한 줄 요약

시퀀스 모델은 순서와 context를 다루기 위해 등장했고, RNN은 hidden state로 과거를 요약하지만 BPTT의 gradient decay 때문에 긴 의존성을 배우기 어려워 attention과 Transformer의 필요성이 커졌습니다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 19/30]

오늘은 시퀀스 데이터, RNN, BPTT가 서로 어떻게 이어지는지 차근차근 확인해 볼게요.

### 1. Autoregressive 모델이 `P(다음 token | context)`를 예측한다는 말은 어떤 뜻인가요? 아주 짧은 문장 예시로 설명해 보세요.

**정답**

Autoregressive 모델이 `P(다음 token | context)`를 예측한다는 말은, “지금까지 나온 내용인 context를 보고 다음 token이 무엇일 확률이 높은지 계산한다”는 뜻입니다.

즉 모델은 문장 전체를 한 번에 완성하는 것이 아니라, 앞에 있는 단어들을 바탕으로 다음 단어를 하나씩 예측합니다.

예를 들어 context가 `나는 밥을`이라면 모델은 다음 token 후보에 대해 이런 확률을 낼 수 있습니다.

```text
먹었다: 0.70
샀다: 0.15
봤다: 0.05
기타: 0.10
```

이 경우 모델은 `먹었다`가 가장 자연스럽다고 판단한 것입니다.

**설명**

여기서 `context`는 지금까지 모델이 본 정보입니다. 문장 생성에서는 보통 앞에 나온 token들이 context가 됩니다.

`P(다음 token | context)`는 말로 풀면 다음과 같습니다.

```text
context가 주어졌을 때,
다음 token이 무엇일 확률이 가장 높은가?
```

여기서 `|` 기호는 “~가 주어졌을 때”라는 뜻입니다. 그래서 `P(다음 token | context)`는 “context를 알고 있을 때 다음 token의 확률”이라고 읽으면 됩니다.

Autoregressive 방식의 중요한 특징은 “하나를 예측하고, 그 예측 결과를 다시 context에 붙여서 다음 것을 예측한다”는 점입니다.

예를 들어 모델이 다음처럼 문장을 만든다고 해봅시다.

```text
처음 context: 오늘 날씨가
예측 token: 좋다

새 context: 오늘 날씨가 좋다
예측 token: 그래서

새 context: 오늘 날씨가 좋다 그래서
예측 token: 산책을
```

이런 식으로 한 token씩 이어 붙이면서 긴 문장을 생성합니다.

또 중요한 점은 모델이 단순히 정답 하나만 고르는 것이 아니라, 가능한 token들에 대해 확률 분포를 만든다는 것입니다. 그중 가장 확률이 높은 token을 고를 수도 있고, 약간의 randomness를 넣어서 더 다양한 답변을 만들 수도 있습니다.

**예시**

아주 짧은 문장으로 보면 더 쉽습니다.

```text
context: 나는 사과를
다음 token 후보:
먹었다: 0.65
던졌다: 0.10
읽었다: 0.01
샀다: 0.20
기타: 0.04
```

`나는 사과를` 다음에는 보통 `먹었다`나 `샀다`가 자연스럽습니다. 반대로 `읽었다`는 사과와 잘 어울리지 않기 때문에 확률이 낮습니다.

즉 autoregressive 모델은 “앞 문맥을 보고 다음에 올 말을 확률적으로 고르는 모델”이라고 이해할 수 있습니다.

**실전 연결**

LLM, 즉 Large Language Model은 대부분 이런 next-token prediction 방식으로 학습하고 생성합니다. ChatGPT 같은 모델도 내부적으로는 긴 답변을 한 번에 통째로 만드는 것이 아니라, 지금까지의 context를 보고 다음 token을 예측하는 과정을 반복합니다. 코드 생성 모델도 마찬가지입니다. 예를 들어 `for i in range(`까지 보면 다음에 숫자, 변수, 닫는 괄호 등이 올 확률을 계산합니다. 그래서 autoregressive 관점은 LLM의 학습 방식과 생성 방식을 이해하는 핵심 출발점입니다.

### 2. RNN의 hidden state는 왜 필요한가요? 현재 입력만 보는 모델과 비교해서 설명해 보세요.

**정답**

RNN의 hidden state는 “지금까지 본 정보를 요약해서 기억하기 위해” 필요합니다.

현재 입력만 보는 모델은 매 순간 들어온 입력 하나만 보고 판단합니다. 반면 RNN은 현재 입력뿐 아니라 이전 hidden state도 함께 사용합니다.

즉 RNN은 다음처럼 생각합니다.

```text
현재 입력 + 이전까지의 기억 → 새로운 기억
```

이때 이전까지의 기억 역할을 하는 것이 hidden state입니다.

**설명**

시퀀스 데이터에서는 현재 입력만 봐서는 충분하지 않은 경우가 많습니다. 문장, 음성, 주가, 센서 데이터처럼 순서가 중요한 데이터에서는 앞에서 무슨 일이 있었는지가 뒤의 의미를 바꿉니다.

예를 들어 문장을 봅시다.

```text
나는 어제 너무 배가 고파서 김밥을
```

여기서 다음 단어를 예측하려면 현재 단어 `김밥을`도 중요하지만, 앞에 나온 `배가 고파서`라는 정보도 중요합니다. 사람은 문장을 읽을 때 앞부분을 어느 정도 기억합니다. RNN의 hidden state는 이 기억을 흉내 내려는 장치입니다.

현재 입력만 보는 모델이라면 각 time step을 거의 따로따로 처리합니다. 예를 들어 마지막에 `김밥을`만 보면 다음이 `먹었다`인지, `샀다`인지, `버렸다`인지 판단하기 어렵습니다. 하지만 앞에서 `배가 고파서`를 봤다면 `먹었다`가 더 자연스럽다는 것을 알 수 있습니다.

RNN은 매 time step마다 hidden state를 업데이트합니다.

```text
h1 = f(x1, h0)
h2 = f(x2, h1)
h3 = f(x3, h2)
```

여기서 `x1`, `x2`, `x3`는 각 time step의 입력이고, `h1`, `h2`, `h3`가 hidden state입니다. `h2`는 `x2`만 담은 것이 아니라 `h1`을 통해 `x1`의 정보도 어느 정도 담고 있습니다. 그래서 뒤로 갈수록 hidden state는 “지금까지 읽은 내용의 요약본”처럼 작동합니다.

**예시**

아주 작은 숫자 예시로 보겠습니다.

```text
sequence: 2, 4, 6, ?
```

현재 입력만 보는 모델이 마지막 숫자 `6`만 본다면, 다음 숫자가 무엇인지 확실히 알기 어렵습니다. `6` 다음에는 `7`일 수도 있고, `12`일 수도 있고, 다른 숫자일 수도 있습니다.

하지만 앞의 흐름 `2, 4, 6`을 기억한다면 “2씩 증가하는구나”라고 볼 수 있습니다. 그러면 다음 값은 `8`일 가능성이 높습니다.

RNN의 hidden state는 이런 흐름을 저장하려고 합니다.

아주 단순화해서 hidden state가 지금까지의 합을 저장한다고 해봅시다.

```text
처음 hidden state h0 = 0

x1 = 1 → h1 = 0 + 1 = 1
x2 = 2 → h2 = 1 + 2 = 3
x3 = 3 → h3 = 3 + 3 = 6
```

이 예시에서 마지막 hidden state `h3 = 6`은 지금까지 본 입력 `1, 2, 3`의 정보를 담고 있습니다. 실제 RNN은 단순한 합보다 훨씬 복잡한 정보를 vector 형태로 저장하지만, 핵심 아이디어는 같습니다.

**실전 연결**

RNN의 hidden state는 NLP, 음성 인식, 시계열 예측에서 오래전부터 중요하게 쓰였습니다. 예를 들어 문장 감정 분류에서는 문장을 앞에서부터 읽으면서 hidden state에 정보를 쌓고, 마지막 hidden state를 사용해 긍정/부정을 판단할 수 있습니다. 다만 hidden state 하나에 모든 과거 정보를 압축해야 하므로 긴 문장에서는 앞부분 정보가 약해질 수 있습니다. 이 한계가 나중에 attention과 Transformer가 등장하는 중요한 이유가 됩니다.

### 3. BPTT에서 gradient가 긴 time step을 거슬러 갈 때 왜 long-term dependency를 배우기 어려워질 수 있나요?

**정답**

BPTT에서는 loss에서 시작한 gradient가 뒤쪽 time step에서 앞쪽 time step으로 거슬러 이동합니다. 그런데 시퀀스가 길면 gradient가 많은 단계를 지나야 합니다.

이 과정에서 gradient가 계속 작아지면, 앞쪽 time step은 “내가 최종 loss에 어떤 영향을 줬는지”에 대한 학습 신호를 거의 받지 못합니다. 그래서 멀리 떨어진 과거 정보가 현재 예측에 중요한 long-term dependency를 배우기 어려워집니다.

이 현상을 gradient decay 또는 vanishing gradient라고 부릅니다.

**설명**

BPTT는 Backpropagation Through Time의 줄임말입니다. RNN을 시간 방향으로 펼쳐 놓고 backpropagation을 하는 방식입니다.

예를 들어 RNN이 3개의 time step을 처리했다고 해봅시다.

```text
x1 → h1
x2 → h2
x3 → h3 → loss
```

학습할 때는 loss에서 시작한 gradient가 뒤로 흐릅니다.

```text
loss → h3 → h2 → h1
```

이렇게 해야 모델이 “x1, x2, x3 중 무엇이 loss에 영향을 줬는지”를 배울 수 있습니다.

문제는 time step이 아주 길 때입니다.

```text
loss → h100 → h99 → h98 → ... → h1
```

gradient가 100단계를 거슬러 가야 한다면, 중간중간에서 계속 작아질 수 있습니다. gradient는 “weight를 어느 방향으로 얼마나 고쳐야 하는지 알려주는 신호”입니다. 이 신호가 너무 작아지면 앞쪽 time step은 거의 학습되지 않습니다.

long-term dependency는 멀리 떨어진 정보가 현재 예측에 중요한 경우입니다. 예를 들어 문장 맨 앞에 나온 정보가 문장 끝의 답을 결정하는 경우입니다. 그런데 gradient가 맨 앞까지 제대로 전달되지 않으면, 모델은 그 앞쪽 정보가 중요하다는 사실을 배우기 어렵습니다.

수학적으로는 작은 값을 여러 번 곱하면 빠르게 작아지는 현상과 관련이 있습니다.

예를 들어 gradient가 한 step을 지날 때마다 `0.5`배가 된다고 해봅시다.

```text
1 step 전: 0.5
2 step 전: 0.25
3 step 전: 0.125
10 step 전: 약 0.00098
```

처음에는 작아 보이지 않지만, 여러 번 반복되면 거의 0에 가까워집니다. 그러면 앞쪽 정보는 학습 신호를 거의 받지 못합니다.

**예시**

다음 문장을 봅시다.

```text
철수는 아침에 가방 안에 노트북을 넣었다.
그 뒤 버스를 타고 학교에 갔다.
강의실에 앉아 과제를 하려고 했다.
철수가 꺼내야 할 것은 무엇인가?
```

정답은 `노트북`입니다. 하지만 `노트북`이라는 중요한 단어는 질문보다 훨씬 앞에 있습니다.

RNN이 이 문제를 잘 풀려면, 앞쪽의 `노트북` 정보를 마지막 질문까지 잘 보존해야 합니다. 그리고 학습할 때도 마지막 loss에서 나온 gradient가 앞쪽의 `노트북`이 등장한 time step까지 잘 전달되어야 합니다.

그런데 gradient가 중간에 너무 작아지면 모델은 “아, 앞에 나온 노트북이 마지막 답에 중요했구나”를 충분히 배우지 못합니다. 그래서 마지막 근처의 단어만 보고 엉뚱한 답을 할 수 있습니다.

**실전 연결**

이 문제는 RNN 계열 모델의 큰 한계였습니다. 그래서 LSTM과 GRU는 gate 구조를 사용해 중요한 정보를 더 오래 보존하려고 했습니다. 이후 attention은 더 직접적인 해결 방향을 제시했습니다. Attention은 모든 정보를 하나의 hidden state에 압축하지 않고, 필요한 과거 위치를 직접 참고할 수 있게 해줍니다. Transformer는 이 attention을 중심으로 만든 구조이고, 현대 LLM의 핵심 기반입니다. 따라서 BPTT와 long-term dependency 문제를 이해하면 “왜 attention과 Transformer가 중요해졌는가”를 훨씬 자연스럽게 이해할 수 있습니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-11-day19.md
