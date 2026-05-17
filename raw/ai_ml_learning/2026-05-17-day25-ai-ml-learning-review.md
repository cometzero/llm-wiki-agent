# AI/ML Learning Review - 2026-05-17 Day 25
- Lesson source: `/home/ubuntu/work/ai/learning/logs/2026-05-17-day25.md`
- Follow-up answer source: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-17_09-26-00.md`

---

## Daily Lesson

# Day 25 - AI/ML 기초 학습

- Date: 2026-05-17
- Progress: 25/30
- Level: beginner-intermediate
- Milestone: LLM 구조와 학습 파이프라인
- Milestone goal: LLM이 어떻게 학습되고 추론되는지 현대적 관점으로 정리한다.

## Today's 3 concepts

1. 언어모델과 next-token prediction
2. 토큰화와 subword 분해
3. 사전학습 objective

---

## 1. 언어모델과 next-token prediction

### 한 줄 직관

Language model은 “지금까지 나온 말”을 보고 “다음에 올 가능성이 높은 token”을 맞히는 모델이다. GPT 같은 LLM은 이 아주 단순해 보이는 문제를 엄청나게 큰 데이터와 모델로 반복해서 풀면서 언어 패턴, 지식, 추론 습관을 배운다.

### 개념 정의

**Language model**은 문장이나 코드처럼 순서가 있는 token sequence에 확률을 붙이는 모델이다. 쉽게 말하면 “이 문장이 얼마나 자연스러운가?” 또는 “이 다음에는 무엇이 올 가능성이 높은가?”를 숫자로 표현하는 모델이다.

LLM에서 가장 대표적인 학습 방식은 **next-token prediction**이다. 현재까지의 token들을 입력으로 받고, 바로 다음 token의 확률분포(probability distribution)를 예측한다.

예를 들어 문장이 다음처럼 시작한다고 하자.

> 나는 아침에 커피를

모델은 다음 token 후보들에 대해 이런 확률을 낼 수 있다.

| 다음 token 후보 | 모델이 예측한 확률 |
|---|---:|
| 마셨다 | 0.70 |
| 먹었다 | 0.20 |
| 달렸다 | 0.05 |
| 파란색 | 0.05 |

이때 모델은 “정답 하나만 바로 말하는 기계”가 아니라, vocabulary 안의 모든 token에 대해 가능성을 나누어 주는 기계다. 실제 생성에서는 이 확률분포에서 가장 높은 token을 고르거나, 약간의 randomness를 넣어 token을 뽑는다.

Next-token prediction을 왼쪽에서 오른쪽으로 계속 반복하는 방식을 **autoregressive objective**라고 부른다. Autoregressive는 “이전 결과를 다음 입력처럼 사용하면서 하나씩 이어 간다”는 뜻에 가깝다.

### 왜 이런 개념이 필요한가

LLM은 처음부터 “질문에 답하기”, “요약하기”, “코드 작성하기” 같은 작업을 직접 배우는 것이 아니다. 먼저 거대한 텍스트에서 next-token prediction을 한다. 그런데 이 문제가 단순해 보여도 매우 강력하다.

문장 “서울은 대한민국의 ___”에서 다음 token을 잘 맞히려면 모델은 지식이 필요하다. “수도”가 자연스럽다는 것을 알아야 한다.

문장 “A가 B보다 크고 B가 C보다 크면, A는 C보다 ___”에서 다음 token을 잘 맞히려면 간단한 추론 패턴이 필요하다. “크다”가 자연스럽다는 것을 알아야 한다.

코드에서 `for i in range(3):` 다음 줄을 예측하려면 들여쓰기, 변수 사용, Python 문법을 알아야 한다.

즉 next-token prediction은 겉으로는 “다음 단어 맞히기”지만, 잘하려면 문법, 의미, 세계 지식, 스타일, 코드 구조, 대화 흐름을 모두 어느 정도 내부 표현(hidden state)에 담아야 한다. 그래서 LLM 학습의 출발점이 된다.

### 아주 쉬운 예시

Vocabulary가 아주 작다고 해 보자. 모델이 고를 수 있는 다음 token이 딱 4개뿐이다.

| token id | token |
|---:|---|
| 0 | 밥 |
| 1 | 물 |
| 2 | 먹었다 |
| 3 | 마셨다 |

입력이 다음과 같다고 하자.

> 나는 밥을

정답 다음 token은 “먹었다”다. 모델이 처음에는 이런 확률을 냈다고 하자.

| token | 확률 |
|---|---:|
| 밥 | 0.10 |
| 물 | 0.10 |
| 먹었다 | 0.30 |
| 마셨다 | 0.50 |

모델은 “마셨다”를 더 높게 보고 있다. 하지만 정답은 “먹었다”이므로 loss가 크다. 학습은 이 loss를 줄이는 방향으로 모델 파라미터를 조금씩 고친다.

학습이 진행된 뒤에는 확률이 이렇게 바뀔 수 있다.

| token | 확률 |
|---|---:|
| 밥 | 0.03 |
| 물 | 0.02 |
| 먹었다 | 0.90 |
| 마셨다 | 0.05 |

이제 모델은 “나는 밥을” 다음에는 “먹었다”가 훨씬 자연스럽다고 배운 것이다.

실제 LLM에서는 후보 token이 4개가 아니라 수만 개이고, 입력 token도 몇 개가 아니라 수천 개 이상일 수 있다. 하지만 기본 아이디어는 같다. “지금까지의 token들 → 다음 token 확률분포”다.

### 개념 구조와 핵심 포인트

Next-token prediction의 흐름은 보통 다음과 같다.

1. 문장을 token으로 나눈다.  
   예: “나는 밥을 먹었다” → `[나는, 밥을, 먹었다]`

2. 각 token을 token id로 바꾼다.  
   예: `[나는, 밥을, 먹었다]` → `[17, 42, 91]`

3. Token id를 embedding vector로 바꾼다.  
   Embedding은 token을 숫자 벡터로 표현한 것이다. 예를 들어 “밥을”이라는 token이 `[0.2, -0.1, 0.7]` 같은 벡터로 바뀐다.

4. Transformer block이 각 위치의 hidden state를 만든다.  
   Hidden state는 “이 위치 token이 문맥 안에서 어떤 의미를 가지는지”를 담은 벡터다. Attention은 앞의 token들을 참고해서 hidden state를 업데이트한다.

5. 마지막 hidden state를 vocabulary 크기의 점수(logits)로 바꾼다.  
   Vocabulary가 50,000개면 다음 token 후보 50,000개 각각에 대한 점수가 나온다.

6. Softmax로 점수를 확률로 바꾼다.

7. 정답 token과 비교해서 loss를 계산한다.

8. Gradient와 optimizer를 이용해 파라미터를 업데이트한다.

중요한 점은 “문장 전체를 한 번에 이해해서 완성된 답을 내는 것”처럼 보이는 LLM도, 생성 단계에서는 사실 token을 하나씩 이어 붙인다는 것이다. `안녕`을 만들고, 다음에 `하세요`를 만들고, 다음에 `!`를 만드는 식이다.

### 핵심 수학 포인트

수학적으로 language model은 다음 확률을 배운다.

\[
P(x_t \mid x_1, x_2, \dots, x_{t-1})
\]

이 식은 “앞의 token들 \(x_1\)부터 \(x_{t-1}\)까지를 봤을 때, 현재 token \(x_t\)가 나올 확률”이라는 뜻이다.

문장 전체의 확률은 다음처럼 쪼갤 수 있다.

\[
P(x_1, x_2, x_3) = P(x_1)P(x_2 \mid x_1)P(x_3 \mid x_1, x_2)
\]

예를 들어 세 token 문장이 `[나는, 밥을, 먹었다]`라고 하자.

- `P(나는) = 0.01`
- `P(밥을 | 나는) = 0.20`
- `P(먹었다 | 나는, 밥을) = 0.80`

그러면 전체 문장 확률은 대략 다음처럼 계산된다.

\[
0.01 \times 0.20 \times 0.80 = 0.0016
\]

학습에서는 정답 token의 확률을 높이고 싶다. 정답 확률이 높을수록 loss가 작아진다. 대표적으로 cross-entropy loss를 사용한다.

정답 token 확률이 0.80이면 loss는 대략 다음과 같다.

\[
-\log(0.80) \approx 0.22
\]

정답 token 확률이 0.10이면 loss는 다음처럼 커진다.

\[
-\log(0.10) \approx 2.30
\]

즉 모델이 정답에 낮은 확률을 주면 loss가 커지고, optimizer는 gradient를 따라 파라미터를 고쳐 다음에는 정답 확률이 올라가게 만든다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **language model**: token sequence에 확률을 붙이거나 다음 token을 예측하는 모델.
- **next-token prediction**: 앞의 token들을 보고 다음 token을 맞히는 학습 문제.
- **autoregressive objective**: 이전 token들을 조건으로 다음 token을 하나씩 예측하는 objective. GPT 계열 모델의 기본 방식이다.
- **vocabulary**: 모델이 알고 있는 token 목록 전체.
- **logits**: softmax를 적용하기 전의 원시 점수. 각 vocabulary token마다 하나의 logit이 나온다.
- **softmax**: 여러 점수를 합이 1인 확률분포로 바꾸는 함수.
- **cross-entropy loss**: 정답 token에 모델이 얼마나 낮은 확률을 줬는지 벌점으로 계산하는 loss.
- **hidden state**: 각 token 위치가 문맥을 반영해 가지는 내부 벡터 표현.

### AI에서 어디에 쓰이는가

Next-token prediction은 GPT, LLaMA, Mistral, Claude류 decoder-only LLM의 기본 사전학습 방식이다. 모델은 웹 문서, 책, 코드, 대화 데이터에서 “다음 token 맞히기”를 반복하며 언어의 통계적 패턴을 배운다.

실제 사용에서도 같은 원리가 이어진다. 사용자가 “오늘 날씨를 알려줘”라고 입력하면, 모델은 내부적으로 다음 response token을 하나씩 예측한다. 첫 token을 만들고, 그 token을 다시 입력 뒤에 붙여 다음 token을 만들고, 이 과정을 종료 token이 나올 때까지 반복한다.

또한 next-token prediction은 attention mask와도 연결된다. GPT는 현재 위치에서 미래 token을 보면 안 되기 때문에 causal mask를 사용한다. 그래야 학습 상황이 실제 생성 상황과 같아진다.

### 헷갈리기 쉬운 포인트

- **“다음 단어”와 “다음 token”은 다르다.**  
  LLM은 보통 단어(word)가 아니라 token 단위로 예측한다. 한 단어가 여러 token으로 쪼개질 수도 있고, 공백이나 문장부호가 token에 포함될 수도 있다.

- **모델은 하나의 정답만 외우는 것이 아니다.**  
  모델은 vocabulary 전체에 대한 확률분포를 낸다. “커피를” 다음에는 “마셨다”도 가능하고 “샀다”도 가능하다. 어떤 문맥에서는 둘 다 자연스러울 수 있다.

- **Next-token prediction이 너무 단순해서 약한 학습이라고 생각하기 쉽다.**  
  하지만 큰 데이터에서 이 문제를 잘 풀려면 문법, 의미, 지식, 추론 패턴이 필요하다. 단순한 objective가 큰 규모와 만나면 매우 강력해진다.

- **생성은 한 번에 문단 전체를 쓰는 것이 아니다.**  
  사용자는 완성된 문장을 한 번에 받는 것처럼 느끼지만, 모델은 실제로 token을 순서대로 생성한다.

---

## 2. 토큰화와 subword 분해

### 한 줄 직관

Tokenization은 사람이 읽는 글을 모델이 처리할 수 있는 작은 조각 token으로 나누는 과정이다. Subword 분해는 “처음 보는 단어도 너무 당황하지 않게” 단어보다 작은 의미 있는 조각으로 쪼개는 방법이다.

### 개념 정의

**Tokenization**은 텍스트를 모델 입력 단위인 token으로 나누는 과정이다. 컴퓨터는 “나는 밥을 먹었다”라는 글자를 그대로 이해하지 못한다. 먼저 텍스트를 token으로 나누고, 각 token을 숫자 id로 바꿔야 한다.

예를 들어 아주 단순한 tokenizer는 문장을 띄어쓰기 기준으로 나눌 수 있다.

> 나는 밥을 먹었다 → `[나는, 밥을, 먹었다]`

하지만 실제 LLM은 보통 단어 단위만 쓰지 않는다. 대신 **subword** 단위를 많이 쓴다. Subword는 단어보다 작을 수도 있고, 자주 등장하는 짧은 단어 하나와 같을 수도 있는 조각이다.

예를 들어 영어 단어 `unhappiness`는 다음처럼 쪼갤 수 있다.

> `unhappiness` → `[un, happiness]` 또는 `[un, happy, ness]`

한국어에서도 긴 표현이나 어미 변화가 많기 때문에 subword가 유용하다.

> `먹었습니다` → `[먹, 었, 습니다]`처럼 쪼개질 수 있다.  
> 실제 tokenizer마다 결과는 다르지만, 핵심은 “자주 쓰이는 조각을 vocabulary에 넣고 조합한다”는 것이다.

대표적인 subword tokenizer 학습 방식 중 하나가 **BPE(Byte Pair Encoding)**이다. BPE는 처음에는 아주 작은 단위에서 시작해, 자주 붙어 나오는 조각들을 반복적으로 합치면서 vocabulary를 만든다.

### 왜 이런 개념이 필요한가

모델은 숫자 tensor만 처리할 수 있다. 텍스트를 neural network에 넣으려면 반드시 token id sequence로 바꿔야 한다.

그런데 token을 어떻게 나누느냐는 모델 성능과 비용에 큰 영향을 준다.

첫째, 단어 단위 tokenization은 모르는 단어 문제를 만든다. 예를 들어 vocabulary에 `초거대언어모델`이라는 단어가 없으면 모델은 이 단어를 처리하기 어렵다. 하지만 subword를 쓰면 `초`, `거대`, `언어`, `모델` 같은 조각으로 나누어 어느 정도 의미를 이어갈 수 있다.

둘째, 글자 단위 tokenization은 너무 길어진다. “Transformer”를 글자 단위로 나누면 `[T, r, a, n, s, f, o, r, m, e, r]`처럼 11개 token이 된다. Sequence length가 길어지면 attention 계산 비용이 커진다. 특히 self-attention은 대략 sequence length의 제곱에 가까운 비용이 들기 때문에 token 수가 중요하다.

셋째, vocabulary가 너무 크면 output layer가 커진다. Next-token prediction에서는 vocabulary의 모든 token에 대해 logit을 계산한다. Vocabulary가 50,000개면 각 위치마다 50,000개 점수를 만든다. Vocabulary가 커질수록 모델의 embedding matrix와 출력 계산도 커진다.

그래서 좋은 tokenizer는 균형을 잡아야 한다. 너무 잘게 쪼개면 sequence가 길어지고, 너무 크게 묶으면 모르는 단어와 큰 vocabulary 문제가 생긴다.

### 아주 쉬운 예시

문장 하나를 보자.

> 나는 딥러닝을 공부한다

방법 A: 띄어쓰기 단위로 tokenization

| 순서 | token |
|---:|---|
| 1 | 나는 |
| 2 | 딥러닝을 |
| 3 | 공부한다 |

이 방법은 보기에는 쉽다. 그런데 vocabulary에 `딥러닝을`이 없고 `딥러닝`만 있다면 문제가 생긴다.

방법 B: subword tokenization

| 순서 | token |
|---:|---|
| 1 | 나는 |
| 2 | 딥 |
| 3 | 러닝 |
| 4 | 을 |
| 5 | 공부 |
| 6 | 한다 |

이렇게 나누면 token 수는 3개에서 6개로 늘었다. 하지만 `딥러닝을`이라는 정확한 단어가 vocabulary에 없어도 `딥`, `러닝`, `을` 조각으로 표현할 수 있다.

이제 token들을 id로 바꿔 보자.

| token | token id |
|---|---:|
| 나는 | 17 |
| 딥 | 821 |
| 러닝 | 1204 |
| 을 | 9 |
| 공부 | 330 |
| 한다 | 88 |

모델 입력은 결국 다음 숫자 sequence가 된다.

\[
[17, 821, 1204, 9, 330, 88]
\]

Batch에 문장 2개를 넣는다면 tensor shape는 예를 들어 `[batch_size, seq_len] = [2, 6]`이 될 수 있다. 그다음 embedding layer를 지나면 `[2, 6, hidden_dim]` 모양의 embedding tensor가 된다. Hidden dim이 4인 작은 장난감 예시라면 shape는 `[2, 6, 4]`다.

### 개념 구조와 핵심 포인트

Tokenization의 전체 구조는 다음과 같다.

1. **텍스트 정리(normalization)**  
   공백, 대소문자, 특수문자 처리 방식 등을 정한다. 모든 tokenizer가 같은 normalization을 쓰지는 않는다.

2. **Pre-tokenization**  
   대략적인 단위로 먼저 나눌 수 있다. 예를 들어 공백이나 문장부호 주변에서 자를 수 있다.

3. **Subword 분해**  
   BPE, WordPiece, SentencePiece 같은 알고리즘이 자주 쓰이는 조각을 기준으로 token을 만든다.

4. **Token id 변환**  
   Vocabulary에서 각 token의 id를 찾는다.

5. **Special token 추가**  
   모델에 따라 시작, 끝, padding, mask 같은 special token을 붙인다. 예: `<bos>`, `<eos>`, `<pad>`, `[MASK]`

6. **Embedding lookup**  
   Token id를 embedding matrix의 row index로 사용해 벡터를 꺼낸다.

BPE의 직관은 “자주 붙어 나오는 두 조각을 하나로 합친다”이다. 아주 작은 예시를 보자.

처음 조각들이 다음처럼 있다고 하자.

- `l o w`
- `l o w e r`
- `n e w e r`

여기서 `l` 다음에 `o`가 자주 나오면 `lo`로 합친다. 그다음 `lo` 다음에 `w`가 자주 나오면 `low`로 합친다. 이런 식으로 자주 등장하는 조합은 하나의 token이 되고, 드문 조합은 여러 subword로 남는다.

핵심 포인트는 tokenizer가 모델의 “입구”라는 것이다. 같은 문장이라도 tokenizer가 다르면 token 수, id, embedding lookup 결과가 달라진다. 그래서 LLM을 사용할 때는 반드시 그 모델이 학습할 때 사용한 tokenizer를 함께 써야 한다.

### 핵심 수학 포인트

Tokenization 자체는 neural network의 미분 가능한 계산은 아니다. 텍스트를 정해진 규칙으로 token id로 바꾸는 전처리 단계다. 하지만 tokenization 결과는 이후 tensor 계산 전체를 결정한다.

예를 들어 문장 하나가 token id 5개로 바뀌었다고 하자.

\[
[10, 25, 7, 91, 3]
\]

Embedding matrix \(E\)가 있다고 하자. Vocabulary size가 100이고 hidden dim이 4라면 embedding matrix shape는 다음과 같다.

\[
E \in \mathbb{R}^{100 \times 4}
\]

Token id 25는 embedding matrix의 25번째 row를 꺼내는 것과 같다.

\[
E[25] = [0.2, -0.4, 0.1, 0.8]
\]

문장에 token이 5개면 embedding 결과는 다음 shape가 된다.

\[
[seq\_len, hidden\_dim] = [5, 4]
\]

Batch size가 2라면 전체 입력 embedding tensor shape는 다음과 같다.

\[
[batch\_size, seq\_len, hidden\_dim] = [2, 5, 4]
\]

Tokenization이 더 잘게 나뉘어 seq_len이 5에서 10으로 늘면 attention 계산량도 늘어난다. Self-attention은 각 token이 다른 token과 관계를 계산하므로, 대략 비교 쌍이 \(seq\_len \times seq\_len\)개 생긴다.

- seq_len = 5이면 비교 쌍은 25개
- seq_len = 10이면 비교 쌍은 100개

Token 수가 2배가 되면 attention score matrix는 4배 커질 수 있다. 그래서 tokenizer는 단순한 전처리가 아니라 모델 속도, 메모리, context length 효율에 직접 영향을 준다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **tokenization**: 텍스트를 token sequence로 나누는 과정.
- **token**: 모델이 처리하는 텍스트의 기본 조각. 단어일 수도, subword일 수도, 문장부호일 수도 있다.
- **BPE(Byte Pair Encoding)**: 자주 함께 등장하는 조각들을 반복적으로 합쳐 subword vocabulary를 만드는 방법.
- **subword**: 단어보다 작거나 비슷한 크기의 token 조각. 모르는 단어 처리에 유용하다.
- **vocabulary**: tokenizer와 모델이 사용하는 token 목록. 각 token은 고유한 id를 가진다.
- **token id**: token을 나타내는 정수 번호.
- **embedding lookup**: token id를 이용해 embedding matrix에서 해당 token vector를 꺼내는 과정.
- **special token**: `<pad>`, `<eos>`, `[MASK]`처럼 모델 제어를 위해 쓰는 특별한 token.

### AI에서 어디에 쓰이는가

모든 LLM 입력은 tokenizer를 거친다. 사용자가 입력한 prompt도, 모델이 생성한 답변도, 학습 데이터의 문서도 모두 token 단위로 처리된다.

Tokenization은 다음 영역에 직접 영향을 준다.

- **Context length**: 같은 글이라도 token이 많이 나오면 context window를 더 빨리 사용한다.
- **비용과 속도**: token 수가 많을수록 attention 계산과 generation 시간이 늘어난다.
- **다국어 성능**: 한국어, 일본어, 중국어처럼 공백 기준 단어 분리가 단순하지 않은 언어에서는 tokenizer 품질이 중요하다.
- **Rare word 처리**: 신조어, 이름, 코드 변수명, URL 같은 드문 문자열을 subword로 나눠 처리할 수 있다.
- **Embedding 학습**: 각 token id는 embedding vector를 가진다. Tokenizer가 어떻게 나누는지에 따라 모델이 배우는 기본 단위가 달라진다.

예를 들어 코드 모델은 `get_user_name` 같은 identifier를 여러 조각으로 나누어 `get`, `_`, `user`, `_`, `name`처럼 처리할 수 있다. 이렇게 하면 처음 보는 변수명도 익숙한 조각 조합으로 이해할 수 있다.

### 헷갈리기 쉬운 포인트

- **Token은 단어와 같지 않다.**  
  “안녕하세요”가 하나의 token일 수도 있고 여러 token일 수도 있다. 모델과 tokenizer에 따라 다르다.

- **Tokenizer는 모델마다 다를 수 있다.**  
  GPT 계열, LLaMA 계열, BERT 계열은 tokenizer 방식과 vocabulary가 다를 수 있다. 모델 A의 token id 100이 모델 B에서도 같은 의미라는 보장은 없다.

- **Subword가 항상 의미 단위로 예쁘게 나뉘는 것은 아니다.**  
  BPE는 언어학적으로 완벽한 형태소 분석기가 아니다. 자주 등장하는 문자열 패턴을 기준으로 합치기 때문에 사람이 보기에는 어색한 조각이 나올 수 있다.

- **Vocabulary가 크면 무조건 좋은 것이 아니다.**  
  Vocabulary가 크면 드문 단어를 한 token으로 표현할 수 있지만, embedding matrix와 output logits 계산이 커진다. 반대로 vocabulary가 작으면 token sequence가 길어진다.

- **Tokenization은 보통 gradient로 학습되는 부분이 아니다.**  
  일반적인 LLM 학습에서 tokenizer는 먼저 만들어 두고 고정한다. 모델 파라미터는 학습되지만 tokenization 규칙 자체는 그대로인 경우가 많다.

---

## 3. 사전학습 objective

### 한 줄 직관

Pretraining objective는 모델에게 “처음에 어떤 문제를 풀면서 기본기를 배울지” 정해 주는 학습 과제다. LLM은 사람이 일일이 정답을 붙인 데이터가 아니라, 텍스트 자체에서 만든 정답으로 먼저 거대한 연습을 한다.

### 개념 정의

**Pretraining**은 모델을 특정 서비스나 과제에 바로 맞추기 전에, 큰 데이터로 기본 표현 능력을 먼저 학습시키는 단계다. 사람으로 비유하면 시험 문제를 풀기 전에 책을 많이 읽고 언어 감각과 배경지식을 쌓는 과정에 가깝다.

이때 모델이 풀 문제를 **objective**라고 부른다. Objective는 “무엇을 잘하면 loss가 작아지는가?”를 정하는 규칙이다.

LLM에서 중요한 점은 pretraining이 대부분 **self-supervised learning**이라는 것이다. Self-supervised learning은 사람이 별도로 라벨을 달지 않아도 데이터 안에서 정답을 만들 수 있는 학습 방식이다.

예를 들어 문장이 다음과 같다고 하자.

> 고양이는 소파 위에서 잔다

Causal LM objective에서는 앞부분을 보고 다음 token을 맞힌다.

> 고양이는 소파 위에서 ___ → 정답: 잔다

Masked LM objective에서는 문장 중간 일부를 가리고 맞힌다.

> 고양이는 [MASK] 위에서 잔다 → 정답: 소파

둘 다 사람이 새로 라벨을 만든 것이 아니다. 원래 문장 자체가 정답을 제공한다.

### 왜 이런 개념이 필요한가

현대 AI 모델은 큰 neural network다. 파라미터가 수십억 개 이상이면, 작은 라벨 데이터만으로는 좋은 표현을 배우기 어렵다. 모든 질문-답변, 모든 번역, 모든 요약, 모든 코드 예제를 사람이 직접 라벨링하는 것도 불가능에 가깝다.

Pretraining objective는 이 문제를 해결한다. 인터넷 문서, 책, 코드, 위키, 논문 같은 대규모 원문에서 자동으로 학습 문제를 만들 수 있기 때문이다.

예를 들어 next-token prediction은 모든 문장을 훈련 문제로 바꾼다.

문장:

> 나는 오늘 학교에 갔다

이 문장은 여러 개의 학습 문제로 바뀐다.

1. `나는` 다음은? → `오늘`
2. `나는 오늘` 다음은? → `학교에`
3. `나는 오늘 학교에` 다음은? → `갔다`

문장 하나에서 여러 training example이 생긴다. 데이터가 많을수록 모델은 다양한 문맥에서 loss를 줄이는 법을 배운다.

Pretraining을 잘하면 모델은 downstream task, 즉 나중에 맡길 실제 작업에 더 잘 적응한다. 질문 답변, 요약, 번역, 코드 생성, classification, 검색용 embedding 등 많은 작업이 좋은 pretraining representation 위에서 성능을 얻는다.

### 아주 쉬운 예시

아주 작은 corpus가 있다고 하자.

1. 나는 밥을 먹었다
2. 나는 물을 마셨다

Causal LM objective로 학습 문제를 만들면 다음과 같다.

| 입력 | 정답 다음 token |
|---|---|
| 나는 | 밥을 |
| 나는 밥을 | 먹었다 |
| 나는 | 물을 |
| 나는 물을 | 마셨다 |

모델이 처음에는 `나는 밥을` 다음에 `마셨다`를 0.60, `먹었다`를 0.40으로 예측했다고 하자. 정답은 `먹었다`이므로 loss가 생긴다. Gradient는 `먹었다`의 logit을 올리고 `마셨다`의 logit을 상대적으로 낮추는 방향으로 파라미터를 바꾼다.

Masked LM objective로는 이렇게 만들 수 있다.

| 가린 문장 | 정답 token |
|---|---|
| 나는 [MASK] 먹었다 | 밥을 |
| 나는 물을 [MASK] | 마셨다 |

이 방식에서는 모델이 왼쪽과 오른쪽 문맥을 둘 다 볼 수 있다. “나는 [MASK] 먹었다”에서는 뒤의 “먹었다”를 보고 `[MASK]`가 “밥을”일 가능성이 높다고 추론할 수 있다.

같은 텍스트라도 objective가 다르면 모델이 보는 정보와 배우는 행동이 달라진다.

### 개념 구조와 핵심 포인트

Pretraining objective를 이해할 때는 세 가지를 구분하면 좋다.

1. **데이터(data)**  
   모델이 읽는 원문이다. 예: 웹 문서, 책, 코드, 뉴스, 논문.

2. **Objective**  
   원문으로부터 어떤 학습 문제를 만들지 정하는 규칙이다. 예: 다음 token 맞히기, 가린 token 맞히기.

3. **Loss**  
   모델 예측이 정답과 얼마나 다른지 숫자로 재는 함수다. 예: cross-entropy loss.

대표 objective 두 가지를 비교해 보자.

#### Causal LM

Causal LM은 왼쪽 문맥만 보고 다음 token을 예측한다. GPT 계열 모델이 대표적이다.

> 입력: `나는 오늘`  
> 정답: `학교에`

이 objective는 생성(generation)에 자연스럽다. 실제로 답변을 만들 때도 앞에서 만든 token들을 보고 다음 token을 계속 만들어야 하기 때문이다.

Causal LM에서는 causal mask가 중요하다. 학습 중 현재 위치가 미래 token을 보면 정답을 훔쳐보는 셈이 되기 때문이다.

#### Masked LM

Masked LM은 문장 일부를 `[MASK]`로 가리고, 주변 문맥을 보고 원래 token을 맞힌다. BERT가 대표적이다.

> 입력: `나는 [MASK]에 갔다`  
> 정답: `학교`

이 objective는 문장 이해(understanding)에 강하다. 왼쪽과 오른쪽 문맥을 모두 사용해 token의 의미를 파악하기 때문이다. 그래서 classification, 문장 pair 판단, 검색 reranking 같은 작업에 많이 쓰였다.

하지만 Masked LM은 그대로 autoregressive generation을 하기에 자연스럽지는 않다. 생성은 미래 token이 아직 없는데, masked LM은 양쪽 문맥을 보는 방식으로 학습되기 때문이다.

### 핵심 수학 포인트

Objective는 결국 loss를 최소화하는 문제로 바뀐다.

\[
\min_\theta L(\theta)
\]

여기서 \(\theta\)는 모델 파라미터다. Embedding matrix, attention weight, MLP weight 같은 모든 학습 가능한 숫자들이 포함된다.

Causal LM의 loss는 각 위치에서 정답 다음 token의 negative log probability를 더한 형태로 볼 수 있다.

\[
L = -\sum_t \log P_\theta(x_t \mid x_{<t})
\]

쉬운 숫자 예시를 보자. 세 위치의 정답 token 확률이 다음과 같다고 하자.

| 위치 | 정답 token 확률 |
|---:|---:|
| 1 | 0.50 |
| 2 | 0.25 |
| 3 | 0.80 |

각 위치 loss는 대략 다음과 같다.

- \(-\log(0.50) \approx 0.69\)
- \(-\log(0.25) \approx 1.39\)
- \(-\log(0.80) \approx 0.22\)

전체 loss를 평균내면 대략 다음과 같다.

\[
(0.69 + 1.39 + 0.22) / 3 \approx 0.77
\]

학습의 목표는 이 평균 loss를 낮추는 것이다. Loss가 낮아진다는 말은 정답 token에 더 높은 확률을 준다는 뜻이다.

Masked LM도 비슷하게 cross-entropy loss를 사용하지만, loss를 모든 위치가 아니라 mask된 위치에 대해서만 계산하는 경우가 많다.

예:

> `나는 [MASK] 먹었다` → 정답: `밥을`

모델이 `밥을` 확률을 0.70으로 주면 loss는 \(-\log(0.70) \approx 0.36\)이다. `물을`에 0.70을 주고 `밥을`에 0.10만 주면 loss는 \(-\log(0.10) \approx 2.30\)으로 커진다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **pretraining**: 큰 데이터로 모델의 기본 언어/표현 능력을 먼저 학습시키는 단계.
- **objective**: 모델이 어떤 문제를 풀도록 학습할지 정하는 목표 규칙.
- **self-supervised learning**: 데이터 자체에서 정답을 만들어 학습하는 방식. 사람이 별도 라벨을 많이 달지 않아도 된다.
- **causal LM**: 과거 token만 보고 현재 또는 다음 token을 예측하는 language model 방식. GPT 계열과 잘 맞는다.
- **masked LM**: 일부 token을 `[MASK]`로 가리고 주변 문맥으로 맞히는 방식. BERT 계열과 연결된다.
- **loss**: 모델 예측이 정답과 얼마나 다른지 나타내는 숫자.
- **gradient**: loss를 줄이려면 파라미터를 어느 방향으로 바꾸어야 하는지 알려 주는 정보.
- **optimizer**: gradient를 사용해 실제로 파라미터를 업데이트하는 알고리즘. AdamW가 LLM 학습에서 자주 쓰인다.
- **downstream task**: pretraining 이후 모델을 적용하는 실제 작업. 예: 요약, 번역, classification, 질의응답.

### AI에서 어디에 쓰이는가

Pretraining objective는 모델의 성격을 크게 결정한다.

- GPT류 모델은 causal LM objective로 학습되어 자연스러운 text generation에 강하다.
- BERT류 모델은 masked LM objective로 학습되어 문장 이해, classification, 검색 관련 작업에 강하게 쓰였다.
- T5 같은 encoder-decoder 모델은 text-to-text 방식 objective를 사용해 여러 문제를 “입력 텍스트 → 출력 텍스트” 형식으로 통일했다.

현대 LLM pipeline에서는 보통 다음 순서가 등장한다.

1. **Pretraining**: 대규모 텍스트로 기본 language model 능력을 만든다.
2. **Instruction tuning**: 지시문과 답변 데이터로 “사용자 요청에 답하는 방식”을 배운다.
3. **Preference optimization / RLHF류 학습**: 사람이 선호하는 답변 스타일, 안전성, 유용성을 더 맞춘다.

이 중 pretraining은 가장 큰 기반이다. Pretraining objective가 어떤 문제를 풀게 했는지에 따라 모델이 정보를 보는 방식, 생성 방식, attention mask, loss 계산 위치, fine-tuning 전략이 달라진다.

### 헷갈리기 쉬운 포인트

- **Pretraining은 supervised learning과 완전히 반대말이 아니다.**  
  Self-supervised learning도 정답이 있다. 다만 정답을 사람이 따로 붙이는 것이 아니라 원문에서 자동으로 만든다.

- **Objective와 loss는 비슷해 보이지만 구분하면 좋다.**  
  Objective는 “어떤 문제를 풀 것인가”이고, loss는 “그 문제를 얼마나 못 풀었는지 숫자로 재는 방법”이다.

- **Causal LM은 미래를 보면 안 된다.**  
  GPT가 학습 중 미래 token을 볼 수 있으면 next-token prediction이 의미 없어지고 실제 생성 상황과 맞지 않는다.

- **Masked LM은 생성형 챗봇과 바로 같은 방식이 아니다.**  
  BERT는 `[MASK]`를 채우는 이해 중심 objective로 유명하다. GPT처럼 왼쪽에서 오른쪽으로 긴 답변을 생성하는 구조와는 다르다.

- **Pretraining만으로 모든 것이 끝나지는 않는다.**  
  Base model은 next-token prediction을 잘하지만, 사용자의 지시를 친절하게 따르도록 만들려면 instruction tuning이나 preference optimization이 추가로 필요하다.

---

## 복습 질문 3개

1. Language model이 next-token prediction을 잘하려면 왜 단순히 단어 빈도만 외우는 것보다 더 많은 문맥 이해가 필요할까?
2. Subword tokenization은 모르는 단어 문제를 어떻게 줄여 주며, 대신 어떤 비용을 늘릴 수 있을까?
3. Causal LM objective와 masked LM objective는 모델이 볼 수 있는 문맥이 어떻게 다르고, 각각 어떤 AI 작업에 더 자연스럽게 연결될까?

## 오늘의 한 줄 요약

LLM의 기본 출발점은 텍스트를 token으로 바꾸고, 큰 데이터에서 self-supervised objective로 다음 token이나 가린 token을 맞히며, loss를 줄이는 과정 속에서 language model의 내부 표현을 배우는 것이다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 25/30]

오늘은 LLM의 기본 출발점인 next-token prediction, tokenization, pretraining objective를 복습합니다.

### 1. Language model이 next-token prediction을 잘하려면 왜 단순히 단어 빈도만 외우는 것보다 더 많은 문맥 이해가 필요할까?

**정답**

Language model이 next-token prediction을 잘하려면 단어가 자주 나오는지만 아는 것으로는 부족합니다.

다음 token은 앞 문맥에 따라 완전히 달라지기 때문입니다. 모델은 문법, 의미, 앞뒤 관계, 세계 지식, 대화 흐름, 코드 구조 같은 정보를 함께 이해해야 합니다.

즉, next-token prediction은 겉으로는 “다음 token 맞히기”이지만, 실제로는 문맥을 바탕으로 가장 자연스러운 후보에 높은 확률을 주는 문제입니다.

**설명**

**Language model**은 지금까지 나온 token들을 보고 다음 token의 확률분포를 예측하는 모델입니다. 여기서 **next-token prediction**은 “앞의 token들을 봤을 때 다음 token이 무엇일까?”를 맞히는 학습 방식입니다.

단순한 단어 빈도만 외운 모델이라면 “먹었다”라는 단어가 자주 나오니까 아무 곳에나 “먹었다”를 높게 줄 수 있습니다. 하지만 실제 문장은 그렇게 단순하지 않습니다.

예를 들어 “나는 물을 ___” 뒤에는 “마셨다”가 자연스럽고, “나는 밥을 ___” 뒤에는 “먹었다”가 자연스럽습니다. “먹었다”와 “마셨다”가 각각 얼마나 자주 나오는지도 중요하지만, 더 중요한 것은 앞에 나온 대상이 “물”인지 “밥”인지입니다.

또 “서울은 대한민국의 ___”에서 “수도”를 맞히려면 단어 빈도뿐 아니라 사실 지식이 필요합니다. “A가 B보다 크고 B가 C보다 크면 A는 C보다 ___”에서 “크다”를 맞히려면 간단한 논리 관계도 필요합니다.

그래서 LLM은 next-token prediction을 반복하면서 단어 빈도만 외우는 것이 아니라, 문맥 속 의미를 담는 **hidden state**, 즉 내부 벡터 표현을 배우게 됩니다. 이 hidden state 안에는 “이 token이 지금 문장 안에서 어떤 의미인지”에 대한 정보가 들어갑니다.

**예시**

아주 작은 예를 들어 보겠습니다.

문장 A:

> 나는 커피를 ___

문장 B:

> 나는 운동장을 ___

두 문장 모두 “나는”으로 시작하지만 다음에 자연스러운 말은 다릅니다.

문장 A에서는:

> 마셨다

가 자연스럽습니다.

문장 B에서는:

> 달렸다

또는

> 걸었다

가 더 자연스럽습니다.

만약 모델이 단어 빈도만 외웠다면 “마셨다”가 자주 나온다는 이유로 문장 B에도 “나는 운동장을 마셨다”처럼 이상한 예측을 할 수 있습니다. 하지만 좋은 language model은 “커피”는 마시는 대상이고, “운동장”은 걷거나 달리는 장소라는 문맥 차이를 반영합니다.

**실전 연결**

GPT, LLaMA, Mistral 같은 decoder-only LLM은 기본적으로 **autoregressive objective**, 즉 이전 token들을 보고 다음 token을 하나씩 예측하는 방식으로 학습됩니다. 이 과정에서 모델은 단순한 빈도표가 아니라 문맥을 압축한 내부 표현을 배웁니다. 그래서 실제 서비스에서 질문 답변, 요약, 코드 생성, 번역을 할 때도 “지금까지의 prompt와 생성된 답변”을 바탕으로 다음 token을 계속 선택할 수 있습니다.

### 2. Subword tokenization은 모르는 단어 문제를 어떻게 줄여 주며, 대신 어떤 비용을 늘릴 수 있을까?

**정답**

Subword tokenization은 처음 보는 단어나 드문 단어를 더 작은 조각으로 나누어 처리함으로써 모르는 단어 문제를 줄여 줍니다.

예를 들어 vocabulary에 “초거대언어모델”이라는 단어 전체가 없어도, “초”, “거대”, “언어”, “모델” 같은 subword 조각이 있다면 모델은 그 단어를 완전히 모르는 것으로 처리하지 않아도 됩니다.

하지만 대신 token 수가 늘어날 수 있습니다. Token 수가 늘어나면 sequence length가 길어지고, attention 계산량, 메모리 사용량, 생성 시간이 늘어날 수 있습니다.

**설명**

**Tokenization**은 사람이 읽는 텍스트를 모델이 처리할 수 있는 token sequence로 나누는 과정입니다. 모델은 글자를 그대로 이해하는 것이 아니라, token을 정수 id로 바꾸고, 그 id를 embedding vector로 변환해서 사용합니다.

문제는 단어 단위로만 tokenization을 하면 vocabulary에 없는 단어가 자주 생긴다는 점입니다. 특히 한국어처럼 조사와 어미 변화가 많거나, 신조어, 이름, 코드 변수명, URL이 자주 나오는 경우에는 “모르는 단어” 문제가 더 커집니다.

**Subword**는 단어보다 작거나 비슷한 크기의 조각입니다. Subword tokenization을 쓰면 단어 전체가 vocabulary에 없어도, 익숙한 조각들의 조합으로 표현할 수 있습니다.

대표적인 방식 중 하나가 **BPE(Byte Pair Encoding)**입니다. BPE는 자주 붙어 나오는 글자나 조각을 반복적으로 합쳐 vocabulary를 만듭니다. 자주 나오는 표현은 하나의 token이 될 수 있고, 드문 표현은 여러 subword로 쪼개집니다.

하지만 장점만 있는 것은 아닙니다. 단어 하나가 여러 token으로 쪼개지면 전체 token 수가 늘어납니다. LLM에서 token 수가 늘어난다는 것은 단순히 입력이 길어진다는 뜻이 아닙니다. Transformer의 self-attention은 각 token이 다른 token들과 관계를 계산하기 때문에, sequence length가 길어질수록 계산량이 빠르게 늘어납니다.

예를 들어 token 수가 5개일 때는 token 간 비교가 대략 25개이고, token 수가 10개가 되면 대략 100개가 됩니다. Token 수가 2배가 되었는데 attention score matrix는 4배 커질 수 있습니다.

**예시**

문장을 하나 보겠습니다.

> 나는 딥러닝을 공부한다

띄어쓰기 기준으로 나누면:

> 나는 / 딥러닝을 / 공부한다

이렇게 3개 token처럼 보일 수 있습니다.

그런데 vocabulary에 “딥러닝을”이라는 token이 없다면 문제가 됩니다. 대신 subword tokenization을 쓰면 다음처럼 나눌 수 있습니다.

> 나는 / 딥 / 러닝 / 을 / 공부 / 한다

이 경우 “딥러닝을”이라는 단어 전체를 몰라도 “딥”, “러닝”, “을”이라는 조각으로 처리할 수 있습니다.

하지만 token 수는 3개에서 6개로 늘었습니다. 즉, 모르는 단어 문제는 줄었지만 모델이 처리해야 할 sequence length는 길어진 것입니다.

**실전 연결**

실제 LLM을 사용할 때 tokenizer는 모델의 입력 비용과 성능에 직접 영향을 줍니다. 같은 한국어 문장이라도 tokenizer가 잘게 쪼개면 더 많은 token을 사용하고, context window를 더 빨리 채웁니다. API 비용이 token 수 기준으로 계산되는 경우도 많기 때문에 tokenization은 실전에서 매우 중요합니다. 또한 모델을 사용할 때는 반드시 그 모델이 학습할 때 사용한 tokenizer를 함께 써야 합니다. tokenizer가 달라지면 token id, embedding lookup, 입력 tensor shape가 모두 달라지기 때문입니다.

### 3. Causal LM objective와 masked LM objective는 모델이 볼 수 있는 문맥이 어떻게 다르고, 각각 어떤 AI 작업에 더 자연스럽게 연결될까?

**정답**

Causal LM objective는 왼쪽 문맥, 즉 이전 token들만 보고 다음 token을 예측합니다. 그래서 GPT 같은 생성형 language model과 잘 맞습니다.

Masked LM objective는 문장 중간 일부를 가리고, 왼쪽과 오른쪽 문맥을 모두 사용해서 가려진 token을 맞힙니다. 그래서 BERT 같은 문장 이해 중심 모델과 잘 맞습니다.

간단히 말하면, Causal LM은 “앞에서부터 이어 쓰기”에 자연스럽고, Masked LM은 “빈칸 채우기와 문장 이해”에 자연스럽습니다.

**설명**

**Pretraining objective**는 모델이 사전학습 때 어떤 문제를 풀면서 기본기를 배울지 정하는 규칙입니다. LLM은 보통 사람이 직접 라벨을 붙인 데이터만으로 학습하지 않습니다. 대신 원래 텍스트 자체에서 정답을 만들어 학습합니다. 이것을 **self-supervised learning**이라고 합니다.

Causal LM objective는 다음 token을 맞히는 방식입니다. 모델은 현재 위치에서 미래 token을 보면 안 됩니다. 예를 들어:

> 나는 오늘 ___

이 입력에서 정답이 “학교에”라면, 모델은 “나는 오늘”까지만 보고 “학교에”를 예측해야 합니다.

이때 미래 token을 보면 정답을 훔쳐보는 것이 됩니다. 그래서 GPT 계열 모델은 **causal mask**를 사용합니다. Causal mask는 attention에서 미래 위치를 보지 못하게 막는 장치입니다.

반면 masked LM objective는 문장 일부를 `[MASK]`로 가리고, 그 빈칸을 맞히는 방식입니다. 예를 들어:

> 나는 [MASK]에 갔다

정답이 “학교”라면, 모델은 왼쪽의 “나는”과 오른쪽의 “에 갔다”를 모두 볼 수 있습니다. 즉, 양방향 문맥을 활용합니다.

이 차이 때문에 두 objective는 잘 맞는 작업도 달라집니다.

Causal LM은 실제 생성 상황과 비슷합니다. 챗봇이 답변을 만들 때는 아직 미래 문장이 존재하지 않습니다. 앞에서 만든 token들을 보고 다음 token을 하나씩 만들어야 합니다. 그래서 GPT류 모델은 글쓰기, 대화, 코드 생성, 요약 생성 같은 작업에 자연스럽습니다.

Masked LM은 문장 전체를 보고 중간 의미를 파악하는 데 강합니다. 그래서 문장 classification, 감정 분석, 문장 pair 판단, 검색 reranking 같은 이해 중심 작업에 잘 맞습니다. BERT가 대표적인 masked LM 계열 모델입니다.

**예시**

같은 문장을 두 objective로 바꿔 보겠습니다.

원문:

> 고양이는 소파 위에서 잔다

Causal LM 방식:

> 고양이는 소파 위에서 ___  
> 정답: 잔다

여기서 모델은 “고양이는 소파 위에서”까지만 보고 다음 token을 맞힙니다.

Masked LM 방식:

> 고양이는 [MASK] 위에서 잔다  
> 정답: 소파

여기서 모델은 앞의 “고양이는”도 보고, 뒤의 “위에서 잔다”도 봅니다. 그래서 “[MASK]”에 들어갈 말이 “소파”일 가능성이 높다고 판단할 수 있습니다.

두 방식 모두 원래 문장 자체에서 정답을 만들기 때문에 self-supervised learning입니다. 하지만 모델이 볼 수 있는 정보가 다르기 때문에 배우는 능력의 방향도 달라집니다.

**실전 연결**

GPT류 LLM은 causal LM objective로 사전학습되기 때문에 실제 서비스에서 답변을 왼쪽에서 오른쪽으로 자연스럽게 생성합니다. 사용자가 prompt를 주면 모델은 첫 token을 만들고, 그 token을 다시 문맥에 붙여 다음 token을 예측합니다. 반면 BERT류 모델은 masked LM objective로 학습되어 문장 전체의 의미를 파악하는 데 강하게 쓰였습니다. 예를 들어 리뷰가 긍정인지 부정인지 분류하거나, 두 문장이 같은 의미인지 판단하거나, 검색 결과를 재정렬하는 작업에 잘 연결됩니다. 따라서 objective는 단순한 학습 설정이 아니라 모델의 구조, attention mask, loss 계산 방식, 그리고 나중에 잘하는 AI 작업까지 결정하는 중요한 선택입니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-17-day25.md
