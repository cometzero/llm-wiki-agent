# AI/ML Learning Review Source — 2026-05-12 Day 20

- Lesson source: `/home/ubuntu/work/ai/learning/logs/2026-05-12-day20.md`
- Follow-up answer source: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-12_09-26-27.md`

---

## Lesson

# Day 20 - AI/ML 기초 학습

- Date: 2026-05-12
- Progress: 20/30
- Level: beginner-intermediate
- Milestone: 시퀀스 모델과 어텐션
- Milestone goal: 순서가 있는 데이터를 다루는 모델과 attention의 등장 배경을 이해한다.

## Today's 3 concepts

1. LSTM/GRU의 gating 메커니즘
2. 단어 임베딩과 표현 압축
3. Attention의 정보 선택 메커니즘

---

## 1. LSTM/GRU의 gating 메커니즘

### 한 줄 직관

LSTM과 GRU의 gate는 RNN이 긴 문장을 읽을 때 “무엇을 기억하고, 무엇을 잊고, 무엇을 지금 출력할지”를 조절하는 작은 스위치입니다.

### 개념 정의

이전 시간에 본 RNN은 문장을 왼쪽에서 오른쪽으로 읽으면서 hidden state라는 요약 메모리를 계속 업데이트합니다. 예를 들어 `나는 어제 친구와 영화관에 가서 ...`라는 문장을 읽으면, 모델은 지금까지 읽은 내용을 hidden state 안에 압축해서 들고 갑니다.

문제는 단순 RNN이 시간이 길어질수록 오래전 정보를 잘 잊어버린다는 점입니다. 문장 초반에 나온 중요한 단어가 문장 끝의 예측에 필요할 수 있는데, hidden state가 매 time step마다 계속 덮어써지기 때문입니다.

LSTM(Long Short-Term Memory)과 GRU(Gated Recurrent Unit)는 이 문제를 줄이기 위해 만들어진 RNN 변형입니다. 핵심 아이디어는 gate입니다. gate는 0과 1 사이의 값을 만들어 정보의 흐름을 조절합니다.

- gate 값이 `0`에 가까우면: 정보를 거의 막습니다.
- gate 값이 `1`에 가까우면: 정보를 거의 통과시킵니다.
- gate 값이 `0.3`이면: 정보의 30% 정도만 반영한다고 직관적으로 볼 수 있습니다.

LSTM은 특히 cell state라는 긴 메모리 통로를 따로 두고, 그 위에 여러 gate를 붙입니다. GRU는 LSTM보다 구조를 조금 단순하게 만들어 gate 수를 줄인 모델입니다.

### 왜 이런 개념이 필요한가

시퀀스 데이터에서는 “멀리 떨어진 정보”가 중요할 때가 많습니다.

예를 들어 문장을 봅시다.

```text
철수는 아침에 도서관에서 빌린 책을 집에 가져와서 밤늦게까지 ___
```

빈칸에는 `읽었다`가 자연스럽습니다. 그런데 `책`이라는 단어는 문장 중간에 있고, 빈칸은 훨씬 뒤에 있습니다. 모델이 `책`을 기억하지 못하면 `먹었다`, `걸었다` 같은 이상한 예측을 할 수 있습니다.

단순 RNN은 hidden state 하나에 모든 정보를 계속 섞어 넣습니다. 그래서 문장이 길어지면 중요한 정보도 점점 희미해집니다. 학습 과정에서도 gradient가 시간 방향으로 뒤로 전달되다가 너무 작아지는 vanishing gradient 문제가 생길 수 있습니다. 그러면 모델은 오래전 단어가 현재 예측에 미치는 영향을 잘 배우지 못합니다.

LSTM/GRU의 gate는 이 문제에 대한 실용적인 해결책입니다. 모델이 스스로 학습하면서 다음과 같은 결정을 내리게 합니다.

- 이 정보는 오래 유지해야 하는가?
- 방금 들어온 단어는 중요한가?
- 이전 메모리 중 일부를 지워야 하는가?
- 지금 출력에 어떤 기억을 사용할 것인가?

즉 gate는 시퀀스 모델에 “선택적 기억력”을 줍니다.

### 아주 쉬운 예시

작은 숫자 예시로 gate를 생각해 봅시다.

모델의 현재 메모리(cell state)가 다음과 같다고 합시다.

```text
기존 메모리: 10
새 정보: 4
```

만약 새 정보를 무조건 더하면 메모리는 `14`가 됩니다. 하지만 모든 새 정보가 항상 중요한 것은 아닙니다. gate가 새 정보의 중요도를 `0.25`라고 판단했다면, 새 정보 중 25%만 반영합니다.

```text
반영되는 새 정보 = 4 × 0.25 = 1
업데이트된 메모리 = 10 + 1 = 11
```

반대로 어떤 정보는 잊어야 할 수도 있습니다. 기존 메모리 유지 gate가 `0.8`이면 기존 메모리의 80%만 유지한다고 볼 수 있습니다.

```text
유지되는 기존 메모리 = 10 × 0.8 = 8
새 정보 반영 = 4 × 0.25 = 1
업데이트된 메모리 = 8 + 1 = 9
```

이 숫자는 실제 LSTM 수식의 단순화된 직관입니다. 중요한 점은 모델이 정보를 그냥 통째로 덮어쓰지 않고, gate를 통해 얼마나 남기고 얼마나 넣을지 조절한다는 것입니다.

일상 비유로는 메모장 정리와 비슷합니다. 하루 동안 들은 말을 모두 적으면 메모장이 금방 지저분해집니다. 그래서 우리는 중요한 약속은 남기고, 중요하지 않은 잡담은 지웁니다. LSTM/GRU의 gate는 모델 안에서 이 정리를 자동으로 하는 장치입니다.

### 개념 구조와 핵심 포인트

LSTM의 대표적인 구조는 다음처럼 이해할 수 있습니다.

1. **cell state**
   긴 정보를 비교적 안정적으로 흘려보내는 메모리 통로입니다. 단순 RNN의 hidden state보다 “오래 기억하는 역할”에 더 집중합니다.

2. **forget gate**
   이전 cell state에서 무엇을 버릴지 결정합니다. 예를 들어 이전 주제가 끝났다면 오래된 주제 정보를 줄일 수 있습니다.

3. **input gate**
   새로 들어온 입력 중 무엇을 cell state에 넣을지 결정합니다. 모든 단어가 똑같이 중요하지 않기 때문에 필요한 정보만 추가합니다.

4. **output gate**
   cell state 중 지금 hidden state로 내보낼 정보를 결정합니다. 즉 내부에 기억해 둔 것과 지금 밖으로 보여 줄 것을 구분합니다.

GRU는 LSTM보다 단순합니다.

1. **update gate**
   이전 hidden state를 얼마나 유지하고 새 정보를 얼마나 반영할지 결정합니다.

2. **reset gate**
   과거 정보를 얼마나 무시하고 새 후보 상태를 만들지 결정합니다.

LSTM은 cell state와 hidden state를 분리합니다. GRU는 보통 hidden state 중심으로 더 간단하게 동작합니다. 그래서 GRU는 계산이 조금 가볍고, LSTM은 더 세밀한 기억 제어가 가능한 편입니다. 다만 실제 성능은 데이터와 문제에 따라 달라집니다.

핵심은 둘 다 “순서가 긴 데이터에서 필요한 정보를 오래 보존하기 위해 gate를 사용한다”는 점입니다.

### 핵심 수학 포인트

gate는 보통 sigmoid 함수를 통과한 값입니다. sigmoid는 어떤 숫자를 받아서 0과 1 사이 값으로 바꿉니다.

```text
입력 점수: -3  → sigmoid 결과: 약 0.05  → 거의 닫힌 gate
입력 점수:  0  → sigmoid 결과: 0.5    → 반쯤 열린 gate
입력 점수:  3  → sigmoid 결과: 약 0.95  → 거의 열린 gate
```

이 gate 값은 벡터의 각 원소에 곱해집니다. 예를 들어 hidden state가 3차원 벡터라고 합시다.

```text
정보 벡터: [2, 10, -4]
gate 벡터: [1.0, 0.2, 0.0]
결과:      [2, 2, 0]
```

첫 번째 정보는 그대로 통과하고, 두 번째 정보는 20%만 남고, 세 번째 정보는 막혔습니다.

LSTM에서는 대략 다음과 같은 생각이 들어갑니다.

```text
새 cell state = forget gate × 이전 cell state + input gate × 새 후보 정보
```

수식을 정확히 외우는 것보다 먼저 이해해야 할 점은 이것입니다.

- 덧셈 경로가 있어서 오래된 정보가 비교적 안정적으로 이어질 수 있습니다.
- 곱셈 gate가 있어서 정보별로 통과량을 조절할 수 있습니다.
- 이 gate 값들도 학습되는 weight로 계산됩니다.
- loss를 줄이는 방향으로 optimizer가 weight를 바꾸면서, 어떤 정보를 기억해야 하는지 모델이 배웁니다.

tensor shape 관점에서는 batch 크기와 hidden size가 중요합니다. 예를 들어 batch size가 `2`, hidden size가 `4`이면 hidden state는 보통 `[2, 4]` 모양의 tensor가 됩니다. gate도 같은 `[2, 4]` 모양으로 만들어져 hidden state의 각 숫자를 원소별로 조절합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **LSTM(Long Short-Term Memory)**: 긴 시퀀스에서 오래 기억할 정보를 보존하기 위해 gate와 cell state를 사용하는 RNN 계열 모델입니다.
- **GRU(Gated Recurrent Unit)**: LSTM보다 단순한 gate 구조를 가진 RNN 계열 모델입니다.
- **gate**: 0과 1 사이 값으로 정보가 얼마나 지나갈지 조절하는 장치입니다.
- **cell state**: LSTM에서 긴 정보를 비교적 안정적으로 전달하는 내부 메모리 통로입니다.
- **hidden state**: 현재 time step까지의 정보를 압축한 모델의 상태 벡터입니다.
- **sigmoid**: 입력 숫자를 0과 1 사이로 바꾸는 함수로, gate 값을 만들 때 자주 쓰입니다.
- **vanishing gradient**: 시간이나 layer가 길어질 때 gradient가 너무 작아져 앞쪽 정보의 영향을 잘 배우지 못하는 문제입니다.

### AI에서 어디에 쓰이는가

LSTM과 GRU는 Transformer가 널리 쓰이기 전까지 자연어 처리와 시계열 모델링의 대표적인 방법이었습니다. 지금도 데이터가 아주 길지 않거나, 계산 자원이 제한되어 있거나, 스트리밍처럼 순서대로 들어오는 데이터를 처리할 때 사용될 수 있습니다.

활용 예시는 다음과 같습니다.

- 문장 분류: 리뷰를 읽고 긍정/부정을 판단합니다.
- 음성 인식: 시간 순서로 들어오는 음성 특징을 처리합니다.
- 시계열 예측: 온도, 전력 사용량, 센서 값, 주가 흐름을 예측합니다.
- 이상 탐지: 정상적인 순서 패턴과 다른 움직임을 찾습니다.
- 초기 seq2seq 번역 모델: encoder가 문장을 읽고 hidden state에 의미를 압축한 뒤 decoder가 번역문을 생성합니다.

LLM의 주류 구조는 Transformer지만, LSTM/GRU를 이해하면 “왜 attention이 필요해졌는가”를 더 잘 이해할 수 있습니다. LSTM/GRU도 긴 문맥을 다루려 했지만, 결국 모든 정보를 순차적으로 압축해야 했습니다. Attention은 이 압축 병목을 더 직접적으로 해결하려고 등장했습니다.

### 헷갈리기 쉬운 포인트

- **gate가 사람이 직접 정한 규칙은 아닙니다.**
  “명사는 기억하고 조사는 잊어라”처럼 사람이 코딩하는 것이 아닙니다. 모델이 loss를 줄이는 과정에서 gate를 계산하는 weight를 학습합니다.

- **cell state가 완벽한 장기 기억은 아닙니다.**
  LSTM은 단순 RNN보다 장기 의존성을 잘 다루지만, 매우 긴 문맥에서는 여전히 한계가 있습니다.

- **GRU가 항상 LSTM보다 나쁘거나 좋은 것은 아닙니다.**
  GRU는 단순해서 빠를 수 있고, LSTM은 더 세밀할 수 있습니다. 어떤 모델이 좋은지는 데이터, 크기, 학습 조건에 따라 달라집니다.

- **hidden state와 cell state를 구분해야 합니다.**
  LSTM에서 cell state는 내부 장기 메모리 통로에 가깝고, hidden state는 각 time step에서 밖으로 전달되는 요약 표현에 가깝습니다.

---

## 2. 단어 임베딩과 표현 압축

### 한 줄 직관

단어 임베딩(embedding)은 `고양이`, `강아지`, `자동차` 같은 단어를 컴퓨터가 계산할 수 있는 작은 숫자 벡터로 바꾸되, 의미가 비슷한 단어는 비슷한 위치에 놓는 방법입니다.

### 개념 정의

컴퓨터는 단어 자체를 바로 이해하지 못합니다. `고양이`라는 글자를 그대로 보면 사람은 동물을 떠올리지만, 모델 입장에서는 문자열일 뿐입니다. 그래서 단어를 숫자로 바꿔야 합니다.

가장 단순한 방법은 one-hot vector입니다. 예를 들어 단어장이 5개라고 합시다.

```text
단어장: [고양이, 강아지, 자동차, 사과, 바나나]
고양이 → [1, 0, 0, 0, 0]
강아지 → [0, 1, 0, 0, 0]
자동차 → [0, 0, 1, 0, 0]
```

이 방식은 단어를 구분하는 데는 좋지만, 의미를 담지 못합니다. `고양이`와 `강아지`는 동물이라 비슷한데, one-hot vector에서는 둘 사이의 비슷함이 보이지 않습니다. 모든 단어가 서로 완전히 다른 번호처럼 취급됩니다.

Embedding은 단어를 더 짧고 촘촘한 dense vector로 바꿉니다.

```text
고양이 → [0.8, 0.7, 0.1]
강아지 → [0.7, 0.8, 0.1]
자동차 → [0.1, 0.2, 0.9]
```

여기서 `고양이`와 `강아지`는 숫자 패턴이 비슷합니다. 반면 `자동차`는 다른 패턴입니다. 이런 식으로 embedding은 단어의 의미적 관계를 숫자 공간에 압축합니다.

### 왜 이런 개념이 필요한가

AI 모델은 숫자 tensor를 입력으로 받아 계산합니다. 따라서 자연어를 다루려면 단어, subword, token을 숫자 벡터로 바꿔야 합니다. 그런데 단순히 번호만 붙이면 의미가 사라집니다.

예를 들어 다음 두 문장을 봅시다.

```text
나는 고양이를 좋아한다.
나는 강아지를 좋아한다.
```

사람은 두 문장이 꽤 비슷하다고 느낍니다. 둘 다 반려동물을 좋아한다는 의미입니다. 하지만 one-hot에서는 `고양이`와 `강아지`가 완전히 다른 칸에 있으므로 비슷함을 직접 표현하기 어렵습니다.

Embedding은 이 문제를 해결합니다. 단어를 의미가 담긴 dense vector로 바꾸면 모델은 다음을 배울 수 있습니다.

- 비슷한 단어는 비슷한 역할을 한다.
- 문맥이 비슷한 단어는 가까운 벡터가 될 수 있다.
- 단어의 차이도 방향으로 표현될 수 있다.
- 긴 문장도 token embedding들의 sequence로 바꿔 neural network에 넣을 수 있다.

표현 압축이라는 말도 중요합니다. 단어장이 50,000개라면 one-hot vector는 50,000차원이 됩니다. 대부분이 0인 아주 긴 벡터입니다. Embedding은 이를 예를 들어 256차원, 768차원, 4096차원 같은 dense vector로 바꿉니다. 차원 수는 여전히 커 보일 수 있지만, one-hot보다 훨씬 작고 정보가 촘촘하게 들어 있습니다.

### 아주 쉬운 예시

단어를 “동물 느낌”과 “탈것 느낌” 두 숫자로 표현한다고 상상해 봅시다.

```text
             동물 느낌   탈것 느낌
고양이          0.9        0.0
강아지          0.9        0.0
자동차          0.0        0.9
버스            0.0        0.8
사과            0.1        0.0
```

이건 실제 embedding보다 훨씬 단순한 예시입니다. 하지만 직관은 좋습니다.

`고양이`와 `강아지`는 `[0.9, 0.0]`으로 비슷합니다. `자동차`와 `버스`도 비슷합니다. 반면 `고양이`와 `자동차`는 매우 다릅니다.

작은 거리 계산을 해 봅시다.

```text
고양이 [0.9, 0.0]
강아지 [0.8, 0.1]
차이   [0.1, -0.1]
```

두 숫자의 차이가 작으므로 둘은 가깝다고 볼 수 있습니다.

반면:

```text
고양이 [0.9, 0.0]
자동차 [0.0, 0.9]
차이   [0.9, -0.9]
```

차이가 큽니다. 그래서 멀다고 볼 수 있습니다.

일상 비유로는 지도와 비슷합니다. 지도에서 서울과 인천은 가깝고, 서울과 뉴욕은 멉니다. Embedding space에서는 단어들이 의미 지도 위에 놓입니다. `고양이`와 `강아지`는 가까운 동네에 있고, `자동차`는 다른 동네에 있는 식입니다.

### 개념 구조와 핵심 포인트

Embedding을 구현 관점에서 보면 보통 embedding table이 있습니다. 단어장 크기가 `V`, embedding 차원이 `D`라면 embedding table의 모양은 `[V, D]`입니다.

예를 들어 단어장이 5개이고 embedding 차원이 3이면 table은 `[5, 3]`입니다.

```text
단어 id 0(고양이): [0.8, 0.7, 0.1]
단어 id 1(강아지): [0.7, 0.8, 0.1]
단어 id 2(자동차): [0.1, 0.2, 0.9]
단어 id 3(사과):   [0.2, 0.1, 0.3]
단어 id 4(바나나): [0.2, 0.1, 0.4]
```

문장 `고양이 좋아`가 token id `[0, 4]`처럼 바뀌었다면, 모델은 embedding table에서 0번 행과 4번 행을 꺼냅니다. 그러면 문장은 `[sequence length, embedding dimension]` 모양의 tensor가 됩니다.

batch까지 포함하면 모양은 보통 다음처럼 생각할 수 있습니다.

```text
input token ids shape: [batch_size, sequence_length]
embedding output shape: [batch_size, sequence_length, embedding_dim]
```

예를 들어 batch size가 `2`, 문장 길이가 `4`, embedding dim이 `3`이면 embedding 결과는 `[2, 4, 3]` 모양입니다. 즉 문장 2개, 각 문장에 token 4개, 각 token은 숫자 3개짜리 벡터입니다.

핵심 포인트는 다음과 같습니다.

1. **Embedding은 lookup입니다.**
   복잡한 계산으로 매번 단어 벡터를 만드는 것이 아니라, token id에 해당하는 행을 table에서 꺼냅니다.

2. **Embedding 값은 학습됩니다.**
   처음에는 랜덤 숫자일 수 있습니다. 학습하면서 loss를 줄이는 방향으로 embedding vector가 조금씩 바뀝니다.

3. **의미는 사용 문맥에서 생깁니다.**
   비슷한 문맥에 자주 등장하는 단어는 비슷한 벡터를 갖도록 학습될 수 있습니다.

4. **압축은 손실과 선택을 포함합니다.**
   모든 단어 정보를 완벽히 담는 것이 아니라, 모델 과제에 유용한 특징을 제한된 차원 안에 담습니다.

### 핵심 수학 포인트

Embedding의 가장 기본 수학은 “큰 one-hot vector에 embedding matrix를 곱하면 해당 행을 고르는 것과 같다”입니다.

단어장이 3개이고 embedding 차원이 2라고 합시다.

```text
Embedding matrix E:
고양이: [0.8, 0.6]
강아지: [0.7, 0.7]
자동차: [0.1, 0.9]
```

`강아지`의 one-hot vector는 `[0, 1, 0]`입니다. 이 벡터에 matrix `E`를 곱하면 두 번째 행인 `[0.7, 0.7]`이 나옵니다. 실제 구현에서는 굳이 one-hot을 만들지 않고 id로 바로 행을 가져옵니다. 더 빠르고 메모리를 아끼기 위해서입니다.

의미적 유사도는 벡터 사이의 거리나 cosine similarity로 볼 수 있습니다. Cosine similarity는 두 벡터가 얼마나 비슷한 방향을 보는지 측정합니다.

아주 단순하게 생각해 봅시다.

```text
고양이: [1, 0]
강아지: [0.9, 0.1]
자동차: [0, 1]
```

`고양이`와 `강아지`는 거의 같은 방향입니다. `고양이`와 `자동차`는 수직에 가깝습니다. 그래서 `고양이`와 `강아지`의 semantic similarity가 더 높다고 말할 수 있습니다.

학습에서는 embedding vector도 모델의 parameter입니다. 예를 들어 `고양이`가 들어간 문장에서 정답 label을 잘 못 맞히면 loss가 커집니다. Backpropagation은 그 loss를 줄이기 위해 embedding table의 `고양이` 행도 조금 수정합니다. 이렇게 많은 문장을 학습하면서 단어 벡터들이 점점 유용한 위치로 이동합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **embedding**: 단어나 token 같은 discrete한 대상을 neural network가 계산할 수 있는 dense vector로 바꾸는 표현입니다.
- **dense vector**: 대부분의 값이 0이 아닌 촘촘한 숫자 벡터입니다. one-hot vector와 대비됩니다.
- **semantic similarity**: 의미적 유사도입니다. 의미가 비슷한 단어들이 embedding space에서 가까운지 보는 개념입니다.
- **one-hot vector**: 한 칸만 1이고 나머지는 0인 벡터입니다. 단어 구분은 쉽지만 의미 관계를 담기 어렵습니다.
- **embedding table**: token id별 embedding vector를 저장한 matrix입니다.
- **token**: 모델이 처리하는 텍스트 단위입니다. 단어일 수도 있고 subword일 수도 있습니다.
- **cosine similarity**: 두 벡터의 방향이 얼마나 비슷한지 보는 유사도 측정 방법입니다.

### AI에서 어디에 쓰이는가

Embedding은 자연어 처리와 LLM의 입구입니다. 텍스트 모델은 글자를 그대로 계산하지 않고 token id를 embedding vector로 바꾼 뒤 neural network에 넣습니다.

사용 예시는 매우 넓습니다.

- LLM 입력: token id를 embedding으로 바꿔 Transformer에 넣습니다.
- 검색 시스템: 문서와 질문을 embedding으로 바꾼 뒤 비슷한 문서를 찾습니다.
- 추천 시스템: 사용자, 상품, 영상, 음악을 embedding으로 표현해 취향이 가까운 항목을 찾습니다.
- 이미지-텍스트 모델: 이미지와 문장을 같은 embedding space에 놓고 서로 맞는지 비교합니다.
- 분류 모델: 문장의 단어 embedding들을 모아 감정, 주제, 의도 등을 예측합니다.

RAG(Retrieval-Augmented Generation)에서도 embedding이 중요합니다. 질문과 문서를 각각 vector로 바꾼 뒤, semantic similarity가 높은 문서를 찾아 LLM에 context로 넣습니다. 사용자가 `환불 규정 알려줘`라고 물었을 때, 문서에 `반품 정책`이라고 쓰여 있어도 embedding이 의미적 유사성을 잡으면 관련 문서를 찾을 수 있습니다.

### 헷갈리기 쉬운 포인트

- **Embedding이 단어의 사전적 의미를 사람이 직접 넣은 것은 아닙니다.**
  대부분은 학습 데이터와 목표 task를 통해 자동으로 만들어집니다.

- **차원이 작다고 항상 나쁜 것은 아닙니다.**
  너무 작으면 표현력이 부족할 수 있지만, 너무 크면 계산량과 과적합 문제가 생길 수 있습니다. 적절한 embedding dimension은 문제에 따라 다릅니다.

- **가까운 vector가 항상 사람이 생각하는 의미와 완벽히 맞지는 않습니다.**
  모델은 학습 데이터의 패턴을 반영합니다. 데이터 편향도 embedding에 들어갈 수 있습니다.

- **Embedding은 context를 모르는 고정 표현일 수도 있고, context를 반영한 표현일 수도 있습니다.**
  Word2Vec 같은 전통적 embedding은 단어마다 비교적 고정된 vector를 가집니다. Transformer의 layer를 거친 표현은 문맥에 따라 `bank`가 은행인지 강둑인지 다르게 표현될 수 있습니다.

---

## 3. Attention의 정보 선택 메커니즘

### 한 줄 직관

Attention은 모델이 긴 입력을 볼 때 모든 정보를 똑같이 보지 않고, 지금 필요한 부분에 더 큰 가중치를 주어 읽는 방법입니다.

### 개념 정의

Attention은 “현재 출력이나 현재 token을 이해하는 데 입력의 어느 부분을 더 참고해야 하는가?”를 계산하는 메커니즘입니다.

RNN 계열 seq2seq 모델에서는 encoder가 입력 문장을 읽고 마지막 hidden state 하나에 전체 문장의 의미를 압축했습니다. 짧은 문장은 괜찮을 수 있지만 긴 문장은 문제가 됩니다. 한 벡터에 모든 정보를 담아야 하므로 중요한 세부 정보가 사라질 수 있습니다.

Attention은 이 병목을 줄입니다. 입력 sequence의 각 위치에 대한 hidden state를 모두 보관해 두고, decoder가 단어를 생성할 때마다 그중 필요한 위치를 골라 참고합니다.

예를 들어 영어 문장 `I love cats`를 한국어로 번역한다고 합시다. `고양이`를 생성하는 순간에는 `cats`에 가장 집중해야 합니다. `사랑한다`를 생성하는 순간에는 `love`에 더 집중해야 합니다. Attention은 이런 alignment, 즉 출력 위치와 입력 위치 사이의 대응 관계를 가중치로 표현합니다.

### 왜 이런 개념이 필요한가

긴 문장이나 긴 문맥에서는 “전체를 하나의 벡터로 압축”하는 방식이 너무 힘듭니다. 예를 들어 다음 문장을 번역한다고 합시다.

```text
The small black cat that my sister found near the school yesterday was sleeping.
```

마지막에 `sleeping`을 번역할 때 주어가 무엇인지 알아야 합니다. 주어는 문장 앞쪽의 `cat`입니다. 중간에 `my sister`, `school`, `yesterday` 같은 정보가 끼어 있습니다. 모델이 마지막 hidden state 하나만 보고 번역하면 어떤 정보가 중요한지 놓칠 수 있습니다.

Attention은 매번 필요한 부분을 다시 볼 수 있게 합니다.

- 출력 단어를 만들 때 입력 단어별 중요도를 계산합니다.
- 중요한 단어에는 큰 weight를 줍니다.
- 덜 중요한 단어에는 작은 weight를 줍니다.
- 이 weight로 입력 hidden states를 섞어 context vector를 만듭니다.

이 방식은 정보 선택을 학습 가능한 연산으로 만듭니다. 사람이 “여기 봐”라고 표시하지 않아도, loss를 줄이는 과정에서 모델은 어떤 입력 위치를 참고해야 하는지 배웁니다.

### 아주 쉬운 예시

문장 번역 예시를 아주 작게 보겠습니다.

```text
입력: I / love / cats
출력하려는 단어: 고양이
```

`고양이`를 만들 때 각 입력 단어에 대한 attention weight가 다음과 같다고 합시다.

```text
I     → 0.05
love  → 0.10
cats  → 0.85
합계  → 1.00
```

모델은 `cats`를 가장 많이 참고합니다. 그래서 `고양이`라는 출력을 만들 가능성이 커집니다.

반대로 `사랑한다`를 만들 때는 다음처럼 될 수 있습니다.

```text
I     → 0.05
love  → 0.90
cats  → 0.05
합계  → 1.00
```

이번에는 `love`가 중요합니다.

숫자로 context vector를 만들어 봅시다. 입력 hidden state가 1차원 숫자라고 아주 단순화하겠습니다.

```text
I의 hidden state:     2
love의 hidden state: 10
cats의 hidden state: 20
```

`고양이`를 출력할 때 attention weight가 `[0.05, 0.10, 0.85]`라면:

```text
context vector = 0.05×2 + 0.10×10 + 0.85×20
               = 0.1 + 1.0 + 17.0
               = 18.1
```

결과가 `cats`의 hidden state인 20에 가깝습니다. 즉 context vector가 `cats` 정보를 많이 담게 됩니다.

일상 비유로는 시험 문제를 풀 때 교과서 전체를 다 똑같이 읽지 않고, 문제와 관련된 문단에 형광펜을 치는 것과 비슷합니다. Attention weight는 모델이 친 형광펜의 진하기라고 볼 수 있습니다.

### 개념 구조와 핵심 포인트

전통적인 encoder-decoder attention에서는 다음 흐름으로 생각할 수 있습니다.

1. **Encoder hidden states 저장**
   입력 문장의 각 token마다 hidden state를 만듭니다. 예를 들어 입력 길이가 3이면 hidden state도 3개입니다.

2. **현재 decoder state와 입력 위치들의 관련도 계산**
   지금 출력하려는 상황과 각 입력 위치가 얼마나 관련 있는지 score를 계산합니다.

3. **softmax로 attention weight 만들기**
   score들을 0과 1 사이 값으로 바꾸고, 전체 합이 1이 되게 만듭니다. 이렇게 해야 “어디를 얼마나 볼지”를 비율처럼 해석할 수 있습니다.

4. **weighted sum으로 context vector 만들기**
   각 hidden state에 attention weight를 곱해 더합니다. 중요한 위치의 정보가 context vector에 더 많이 들어갑니다.

5. **context vector를 사용해 출력 예측**
   decoder는 이 context vector와 자기 상태를 이용해 다음 단어의 확률을 계산합니다.

Transformer의 self-attention도 같은 큰 아이디어를 사용합니다. 다만 encoder-decoder 번역 상황만이 아니라, 같은 문장 안의 token들이 서로를 참고합니다. 예를 들어 `그는 사과를 먹었다. 그것은 달았다.`에서 `그것`이 `사과`를 참고해야 할 수 있습니다. Self-attention은 각 token이 문장 안의 다른 token들을 얼마나 볼지 계산합니다.

핵심 포인트는 다음과 같습니다.

- Attention은 정보 선택을 weight로 표현합니다.
- Weight의 합은 보통 1입니다.
- Context vector는 관련 정보의 weighted sum입니다.
- Alignment는 입력 위치와 출력 위치 사이의 대응 관계입니다.
- Attention은 긴 문맥에서 압축 병목을 줄입니다.

### 핵심 수학 포인트

가장 단순한 attention 수학은 세 단계입니다.

1. 관련도 score를 계산합니다.
2. softmax로 weight를 만듭니다.
3. weight를 이용해 value들을 weighted sum합니다.

작은 숫자 예시를 봅시다.

```text
score: [1, 2, 5]
```

가장 큰 score는 세 번째 위치입니다. softmax를 적용하면 대략 다음처럼 됩니다.

```text
attention weight: [0.02, 0.05, 0.93]
```

세 번째 위치에 거의 집중합니다.

value가 1차원이라고 단순화하면:

```text
value: [3, 10, 20]
context vector = 0.02×3 + 0.05×10 + 0.93×20
               = 0.06 + 0.50 + 18.60
               = 19.16
```

context vector는 세 번째 value인 20에 매우 가깝습니다.

Transformer에서는 query, key, value라는 용어가 중요합니다.

- **query**: 지금 내가 찾고 싶은 정보의 힌트입니다.
- **key**: 각 token이 “나는 이런 정보를 가지고 있다”고 내놓는 검색용 표지입니다.
- **value**: 실제로 가져올 정보입니다.

비유하면 도서관 검색입니다.

```text
query: “고양이에 대한 정보가 필요해”
key: 각 책의 제목/태그
value: 책의 실제 내용
```

query와 key의 유사도를 계산해 attention score를 만들고, 그 score로 value를 섞어 context vector를 만듭니다.

tensor shape를 단순하게 보면, sequence length가 `4`, hidden size가 `8`이면 각 token은 8차원 벡터입니다. Self-attention은 각 token이 다른 4개 token을 얼마나 볼지 계산하므로 attention weight는 대략 `[4, 4]` 모양으로 볼 수 있습니다. batch와 head까지 포함하면 실제 shape는 더 커지지만, 기본 직관은 “각 위치가 각 위치를 보는 표”입니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **attention**: 현재 처리에 필요한 입력 위치나 token에 더 큰 weight를 주어 정보를 선택하는 메커니즘입니다.
- **alignment**: 입력의 어느 부분이 출력의 어느 부분과 대응되는지를 나타내는 관계입니다.
- **context vector**: attention weight로 여러 hidden state 또는 value를 섞어 만든 현재 상황용 요약 벡터입니다.
- **attention weight**: 각 위치를 얼마나 참고할지 나타내는 0과 1 사이의 값입니다. 보통 합이 1입니다.
- **softmax**: 여러 score를 확률처럼 해석 가능한 weight로 바꾸는 함수입니다.
- **query**: 현재 필요한 정보를 찾기 위한 벡터입니다.
- **key**: 각 token이 query와 비교되기 위해 가진 벡터입니다.
- **value**: attention weight를 곱해 실제로 가져오는 정보 벡터입니다.
- **self-attention**: 같은 sequence 안의 token들이 서로를 참고하는 attention입니다.

### AI에서 어디에 쓰이는가

Attention은 현대 LLM과 Transformer의 핵심입니다. GPT 계열 모델, BERT 계열 모델, 번역 모델, 코드 모델, multimodal 모델에서 모두 중요한 역할을 합니다.

활용 예시는 다음과 같습니다.

- 기계 번역: 출력 단어마다 입력 문장의 관련 단어를 참고합니다.
- 문서 요약: 요약 문장을 만들 때 원문에서 중요한 문장을 더 봅니다.
- 질문 답변: 질문과 관련된 문서 위치에 집중합니다.
- LLM next token prediction: 다음 token을 예측할 때 이전 token들 중 관련 있는 token을 참고합니다.
- 이미지 모델: 이미지 patch들 사이의 관계를 attention으로 계산합니다.
- 멀티모달 모델: 텍스트 token이 이미지 patch를 참고하거나, 이미지 정보가 텍스트 정보와 연결됩니다.

실전적으로 attention은 모델의 성능뿐 아니라 계산량에도 큰 영향을 줍니다. Self-attention은 sequence length가 길어질수록 모든 token 쌍을 비교해야 하므로 계산량과 메모리 사용량이 빠르게 커집니다. 그래서 긴 context를 다루는 LLM에서는 efficient attention, KV cache, sliding window 같은 기술도 중요해집니다.

### 헷갈리기 쉬운 포인트

- **Attention weight가 곧 완벽한 설명은 아닙니다.**
  어떤 token에 높은 weight가 있다고 해서 모델의 모든 의사결정 이유가 그 token 하나라고 단정할 수는 없습니다. 해석 도구로 참고할 수 있지만 조심해야 합니다.

- **Attention은 memory를 없애는 것이 아니라 참고 방식을 바꾸는 것입니다.**
  RNN처럼 하나의 hidden state에 모든 것을 압축하기보다, 여러 위치의 표현을 필요할 때 다시 참고합니다.

- **Context vector는 단순 평균이 아닙니다.**
  모든 hidden state를 똑같이 더하는 것이 아니라 attention weight로 가중합을 만듭니다.

- **Alignment는 사람이 주는 정답표가 아닐 수 있습니다.**
  많은 경우 모델이 학습 중에 스스로 유용한 alignment를 찾습니다.

- **Transformer의 attention은 RNN attention보다 더 일반화된 형태입니다.**
  번역 decoder가 encoder를 보는 attention에서 시작해, 이제는 token들이 서로를 보는 self-attention이 LLM의 기본 구조가 되었습니다.

---

## 복습 질문 3개

1. LSTM에서 gate는 왜 0과 1 사이 값을 사용하며, 이 값이 정보 흐름을 어떻게 조절하나요?
2. One-hot vector와 embedding의 가장 큰 차이는 무엇이고, embedding이 semantic similarity를 표현하는 데 왜 더 유리한가요?
3. Attention에서 attention weight와 context vector는 각각 어떤 역할을 하며, 긴 문장을 다룰 때 왜 도움이 되나요?

## 오늘의 한 줄 요약

LSTM/GRU는 gate로 오래 기억할 정보를 고르고, embedding은 단어를 의미 있는 dense vector로 압축하며, attention은 지금 필요한 정보에 집중해 긴 시퀀스의 압축 병목을 줄입니다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 20/30]

오늘은 LSTM/GRU의 gate, embedding, attention을 “정보를 어떻게 기억하고, 표현하고, 골라 보는가”라는 관점에서 다시 정리해 볼게요.

### 1. LSTM에서 gate는 왜 0과 1 사이 값을 사용하며, 이 값이 정보 흐름을 어떻게 조절하나요?

**정답**

LSTM에서 gate가 0과 1 사이 값을 사용하는 이유는 정보를 “얼마나 통과시킬지” 비율처럼 조절하기 위해서입니다.

- gate 값이 0에 가까우면 정보가 거의 막힙니다.
- gate 값이 1에 가까우면 정보가 거의 그대로 지나갑니다.
- gate 값이 0.3이면 정보의 약 30%만 반영한다고 직관적으로 볼 수 있습니다.

즉, gate는 LSTM 안에서 “이전 정보를 얼마나 기억할지”, “새 정보를 얼마나 넣을지”, “현재 출력에 어떤 정보를 보여 줄지”를 조절하는 스위치 역할을 합니다.

**설명**

일반 RNN은 문장을 순서대로 읽으면서 hidden state 하나에 지금까지의 정보를 계속 압축합니다. 그런데 문장이 길어지면 앞쪽에 나온 중요한 정보가 뒤쪽으로 갈수록 희미해질 수 있습니다.

예를 들어 문장 앞에 나온 `책`이라는 단어가 나중에 `읽었다`를 예측하는 데 중요할 수 있습니다. 하지만 단순 RNN은 중간에 많은 단어를 지나면서 그 정보를 잊어버릴 수 있습니다.

LSTM은 이 문제를 줄이기 위해 cell state라는 긴 메모리 통로를 둡니다. 그리고 이 메모리 통로 위에 gate를 사용합니다.

대표적으로 LSTM에는 다음과 같은 gate들이 있습니다.

- forget gate: 이전 cell state에서 무엇을 잊을지 결정합니다.
- input gate: 새로 들어온 정보 중 무엇을 저장할지 결정합니다.
- output gate: 내부 기억 중 현재 hidden state로 무엇을 내보낼지 결정합니다.

이 gate 값들은 보통 sigmoid 함수를 통해 만들어집니다. sigmoid는 어떤 숫자든 0과 1 사이 값으로 바꾸는 함수입니다. 그래서 gate는 “완전히 닫힘”과 “완전히 열림” 사이의 부드러운 조절 장치가 됩니다.

중요한 점은 gate를 사람이 직접 정하지 않는다는 것입니다. 모델이 학습하면서 loss function, 즉 예측이 얼마나 틀렸는지를 나타내는 값이 줄어드는 방향으로 gate를 계산하는 weight를 배웁니다.

**예시**

아주 작게 생각해 볼게요.

기존 cell state에 들어 있는 정보가 10이고, 새 정보가 4라고 합시다.

만약 input gate 값이 0.25라면 새 정보 전체를 넣지 않고 25%만 넣습니다.

```text
새 정보: 4
input gate: 0.25

반영되는 새 정보 = 4 × 0.25 = 1
```

그리고 forget gate 값이 0.8이라면 기존 정보의 80%만 유지합니다.

```text
기존 정보: 10
forget gate: 0.8

유지되는 기존 정보 = 10 × 0.8 = 8
```

그러면 새 cell state는 직관적으로 이렇게 볼 수 있습니다.

```text
새 cell state = 유지된 기존 정보 + 반영된 새 정보
              = 8 + 1
              = 9
```

즉 LSTM은 정보를 무조건 덮어쓰지 않고, “조금 잊고, 조금 추가하는” 방식으로 기억을 관리합니다.

**실전 연결**

LSTM/GRU의 gate는 문장 분류, 음성 인식, 시계열 예측, 센서 데이터 분석처럼 순서가 중요한 데이터에서 중요합니다. 예를 들어 전력 사용량 예측에서는 몇 시간 전의 패턴이 현재 예측에 영향을 줄 수 있습니다. gate가 있으면 모델은 오래 기억해야 할 패턴과 버려도 되는 잡음을 구분하는 법을 배울 수 있습니다.

LLM의 주류 구조는 Transformer지만, LSTM/GRU를 이해하면 attention이 왜 등장했는지도 더 잘 이해할 수 있습니다. LSTM은 gate로 기억을 개선했지만, 여전히 순차적으로 정보를 압축해야 했습니다. Attention은 필요한 정보를 더 직접적으로 다시 참고하는 방식으로 이 한계를 줄였습니다.

### 2. One-hot vector와 embedding의 가장 큰 차이는 무엇이고, embedding이 semantic similarity를 표현하는 데 왜 더 유리한가요?

**정답**

One-hot vector와 embedding의 가장 큰 차이는 의미 관계를 담을 수 있는지입니다.

One-hot vector는 단어를 구분하기 위한 표현입니다. 한 칸만 1이고 나머지는 모두 0입니다. 그래서 `고양이`와 `강아지`가 의미적으로 비슷하다는 정보를 거의 표현하지 못합니다.

Embedding은 단어를 dense vector, 즉 대부분의 값이 0이 아닌 촘촘한 숫자 벡터로 바꿉니다. 학습을 통해 의미가 비슷한 단어들이 embedding space에서 가까운 위치에 놓일 수 있습니다. 그래서 semantic similarity, 즉 의미적 유사도를 표현하는 데 더 유리합니다.

**설명**

컴퓨터는 `고양이`, `강아지`, `자동차` 같은 단어를 그대로 이해하지 못합니다. 그래서 단어를 숫자로 바꿔야 합니다.

가장 단순한 방식이 one-hot vector입니다.

```text
단어장: [고양이, 강아지, 자동차]

고양이 → [1, 0, 0]
강아지 → [0, 1, 0]
자동차 → [0, 0, 1]
```

이 방식은 단어를 서로 구분하는 데는 좋습니다. 하지만 문제가 있습니다. `고양이`와 `강아지`는 둘 다 동물이고 반려동물이라는 점에서 비슷합니다. 그런데 one-hot vector에서는 둘이 완전히 다른 칸에 있습니다. 벡터만 보면 `고양이`와 `강아지`가 `고양이`와 `자동차`보다 더 비슷하다는 사실을 알기 어렵습니다.

Embedding은 이 문제를 해결하기 위해 단어를 더 짧고 의미 있는 숫자 벡터로 바꿉니다.

```text
고양이 → [0.8, 0.7, 0.1]
강아지 → [0.7, 0.8, 0.1]
자동차 → [0.1, 0.2, 0.9]
```

여기서 `고양이`와 `강아지`는 숫자 패턴이 비슷합니다. 반면 `자동차`는 다른 패턴입니다.

이런 벡터들은 학습 과정에서 만들어집니다. 모델이 많은 문장을 보면서 “비슷한 문맥에 자주 등장하는 단어들은 비슷한 역할을 한다”는 패턴을 배웁니다. 그래서 embedding vector들은 점점 의미적으로 유용한 위치로 이동합니다.

또 embedding은 표현 압축의 역할도 합니다. 단어장이 50,000개라면 one-hot vector는 50,000차원이 필요합니다. 하지만 embedding은 예를 들어 256차원이나 768차원 같은 더 작은 dense vector로 단어를 표현할 수 있습니다. 정보가 더 촘촘하게 들어가는 것입니다.

**예시**

아주 단순하게 단어를 두 숫자로 표현한다고 해볼게요.

첫 번째 숫자는 “동물 느낌”, 두 번째 숫자는 “탈것 느낌”이라고 생각해 봅시다.

```text
고양이 → [0.9, 0.0]
강아지 → [0.8, 0.1]
자동차 → [0.0, 0.9]
버스   → [0.0, 0.8]
```

`고양이`와 `강아지`는 둘 다 첫 번째 숫자가 큽니다. 그래서 비슷합니다.

```text
고양이 [0.9, 0.0]
강아지 [0.8, 0.1]
```

두 벡터는 방향과 값이 비슷합니다.

반면 `고양이`와 `자동차`는 다릅니다.

```text
고양이 [0.9, 0.0]
자동차 [0.0, 0.9]
```

두 벡터는 서로 다른 방향을 가리킵니다.

실제로는 이런 유사도를 cosine similarity로 많이 봅니다. Cosine similarity는 두 벡터가 얼마나 비슷한 방향을 향하는지 측정하는 방법입니다. 방향이 비슷하면 의미도 비슷할 가능성이 높다고 보는 것입니다.

**실전 연결**

Embedding은 NLP와 LLM의 입구입니다. LLM은 글자를 그대로 계산하지 않고, 먼저 token을 숫자 id로 바꾼 뒤 embedding table에서 해당 token의 vector를 꺼냅니다. 그다음 Transformer layer들이 이 embedding을 처리합니다.

또 RAG에서도 embedding은 매우 중요합니다. 사용자가 `환불 규정 알려줘`라고 물었을 때, 문서에는 `반품 정책`이라고 쓰여 있을 수 있습니다. 단어가 완전히 같지 않아도 embedding이 의미적 유사성을 잘 잡으면 관련 문서를 찾을 수 있습니다. 검색, 추천 시스템, 문장 분류, 이미지-텍스트 모델에서도 embedding은 핵심적인 표현 방식입니다.

### 3. Attention에서 attention weight와 context vector는 각각 어떤 역할을 하며, 긴 문장을 다룰 때 왜 도움이 되나요?

**정답**

Attention weight는 입력의 각 위치를 얼마나 참고할지 나타내는 중요도입니다. 보통 0과 1 사이 값이며, 전체 합은 1이 됩니다.

Context vector는 attention weight를 이용해 여러 hidden state 또는 value vector를 가중합한 결과입니다. 즉, 현재 예측에 필요한 정보들을 중요도에 따라 섞어 만든 요약 벡터입니다.

긴 문장을 다룰 때 attention이 도움이 되는 이유는 전체 문장을 하나의 벡터에 억지로 압축하지 않고, 필요한 순간마다 중요한 위치를 다시 참고할 수 있기 때문입니다.

**설명**

기존 RNN 기반 seq2seq 모델에서는 encoder가 입력 문장을 읽고 마지막 hidden state 하나에 전체 의미를 압축했습니다. 짧은 문장은 어느 정도 괜찮지만, 긴 문장은 문제가 생깁니다.

예를 들어 이런 문장이 있다고 해봅시다.

```text
The small black cat that my sister found near the school yesterday was sleeping.
```

마지막의 `was sleeping`을 이해하려면 주어가 무엇인지 알아야 합니다. 주어는 앞쪽의 `cat`입니다. 그런데 중간에 `my sister`, `school`, `yesterday` 같은 정보가 끼어 있습니다. 전체 문장을 하나의 벡터에만 담으면 `cat` 정보가 약해질 수 있습니다.

Attention은 이 문제를 줄입니다. 입력 sequence의 각 token에 대한 hidden state를 보관해 두고, 출력할 때마다 어디를 볼지 새로 계산합니다.

예를 들어 번역에서 `고양이`라는 단어를 출력해야 하는 순간에는 입력의 `cats`에 높은 attention weight를 줍니다. `사랑한다`를 출력해야 하는 순간에는 `love`에 높은 attention weight를 줍니다.

이때 attention weight는 “어디를 얼마나 볼지”를 나타냅니다. Context vector는 그렇게 선택한 정보들을 모은 현재 상황용 요약입니다.

핵심 흐름은 이렇습니다.

1. 각 입력 위치와 현재 출력 상황의 관련도 score를 계산합니다.
2. softmax를 사용해 score를 attention weight로 바꿉니다.
3. 각 hidden state 또는 value에 attention weight를 곱합니다.
4. 모두 더해서 context vector를 만듭니다.
5. 이 context vector를 이용해 다음 출력을 예측합니다.

여기서 softmax는 여러 점수를 합이 1인 비율처럼 바꿔 주는 함수입니다. 그래서 attention weight를 “중요도 분배”처럼 해석할 수 있습니다.

**예시**

입력 문장이 다음과 같다고 해봅시다.

```text
입력: I / love / cats
출력하려는 단어: 고양이
```

이때 attention weight가 이렇게 나왔다고 합시다.

```text
I     → 0.05
love  → 0.10
cats  → 0.85
```

합은 1입니다.

모델은 `고양이`를 만들 때 `cats`를 가장 많이 참고합니다. 그래서 context vector에는 `cats` 정보가 가장 많이 들어갑니다.

숫자로 아주 단순화해 볼게요. 각 단어의 hidden state가 1차원 숫자라고 합시다.

```text
I의 hidden state:     2
love의 hidden state: 10
cats의 hidden state: 20
```

attention weight가 `[0.05, 0.10, 0.85]`라면 context vector는 이렇게 계산됩니다.

```text
context vector = 0.05×2 + 0.10×10 + 0.85×20
               = 0.1 + 1.0 + 17.0
               = 18.1
```

결과인 18.1은 `cats`의 hidden state인 20에 가깝습니다. 즉 context vector가 `cats` 정보를 강하게 담고 있습니다.

일상 비유로는 시험 공부와 비슷합니다. 문제를 풀 때 교과서 전체를 똑같이 읽지 않고, 문제와 관련된 문단에 더 집중합니다. Attention weight는 형광펜의 진하기이고, context vector는 형광펜 친 내용을 모아 현재 문제 풀이에 맞게 정리한 요약이라고 볼 수 있습니다.

**실전 연결**

Attention은 Transformer와 LLM의 핵심입니다. GPT 계열 모델은 다음 token을 예측할 때 이전 token들 중 어떤 token을 더 참고할지 self-attention으로 계산합니다. Self-attention은 같은 sequence 안의 token들이 서로를 보는 방식입니다.

예를 들어 `그것은 맛있었다`라는 문장에서 `그것`이 앞의 `사과`를 가리키는지, `케이크`를 가리키는지 문맥을 봐야 합니다. Attention은 이런 관계를 학습하는 데 도움을 줍니다.

기계 번역, 문서 요약, 질문 답변, 코드 생성, 이미지-텍스트 모델에서도 attention은 중요합니다. 특히 긴 문장을 처리할 때 attention은 하나의 hidden state에 모든 정보를 몰아넣는 압축 병목을 줄여 줍니다. 다만 sequence length가 길어질수록 token끼리 비교해야 하는 양이 많아져 계산량과 메모리 사용량이 커지므로, 긴 context를 다루는 LLM에서는 efficient attention, KV cache 같은 기술도 함께 중요해집니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-12-day20.md
