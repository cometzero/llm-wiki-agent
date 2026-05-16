# AI/ML Learning Review - 2026-05-16 Day 24

- Lesson source: `/home/ubuntu/work/ai/learning/logs/2026-05-16-day24.md`
- Follow-up answer source: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-16_09-25-50.md`

---

## Daily Lesson

# Day 24 - AI/ML 기초 학습

- Date: 2026-05-16
- Progress: 24/30
- Level: beginner-intermediate
- Milestone: Transformer 심화 기초
- Milestone goal: Transformer의 각 블록이 왜 필요한지 구조적으로 이해한다.

## Today's 3 concepts

1. Causal mask와 padding mask
2. 인코더-디코더 attention
3. Transformer의 병렬성과 계산비용

---

## 1. Causal mask와 padding mask

### 한 줄 직관

Mask는 attention에게 “여기는 보지 마”라고 알려 주는 가림막이다. Causal mask는 미래 token을 못 보게 막고, padding mask는 의미 없는 padding token을 못 보게 막는다.

### 개념 정의

Attention은 문장 안의 각 token이 다른 token들을 얼마나 참고할지 정하는 계산이다. 그런데 모든 token을 항상 다 보면 안 되는 경우가 있다.

대표적으로 두 가지 상황이 있다.

1. **Causal mask**  
   GPT처럼 다음 단어를 예측하는 decoder-only language model에서는 현재 위치가 미래 단어를 보면 안 된다. 예를 들어 “나는 밥을”까지 보고 다음 단어를 맞혀야 하는데, 정답인 “먹었다”를 미리 보면 학습 문제가 너무 쉬워지고 실제 생성 상황과 맞지 않는다. Causal mask는 각 token이 자기 자신과 과거 token만 보게 만든다.

2. **Padding mask**  
   여러 문장을 한 batch로 묶을 때 길이가 짧은 문장 뒤에 `<pad>` 같은 가짜 token을 붙인다. 이 token은 실제 단어가 아니다. Padding mask는 attention이 이 가짜 token을 참고하지 못하게 만든다.

둘을 합쳐서 넓게 **attention masking**이라고 부른다. Masking은 attention score에 아주 작은 값이 아니라 보통 `-inf`에 가까운 큰 음수 값을 더해, softmax를 지난 뒤 해당 위치의 attention weight가 거의 0이 되게 한다.

### 왜 이런 개념이 필요한가

Attention은 기본적으로 “모든 token이 모든 token을 본다”는 강력한 구조다. 이 장점 때문에 Transformer는 문장 전체 문맥을 잘 사용할 수 있다. 하지만 상황에 따라 보지 말아야 할 정보도 생긴다.

첫째, language model 학습에서는 미래 정보를 막아야 한다. 모델이 “오늘 날씨가 매우” 다음 단어를 맞히는 중인데, 뒤에 이미 “좋다”가 있는 것을 attention으로 볼 수 있다면, 모델은 언어를 이해한 것이 아니라 답안지를 훔쳐본 것이다. 이런 모델은 실제 생성할 때 성능이 무너진다. 실제 생성에서는 미래 단어가 아직 없기 때문이다.

둘째, padding token은 정보가 아니다. Batch 안에서 문장 길이를 맞추기 위한 빈칸일 뿐이다. Attention이 padding token을 참고하면 hidden state가 불필요한 가짜 정보에 흔들린다. 특히 짧은 문장과 긴 문장을 함께 학습할 때 padding mask가 없으면, 짧은 문장의 실제 token들이 많은 `<pad>`를 문맥처럼 보게 될 수 있다.

즉 mask는 Transformer가 “볼 수 있는 정보의 범위”를 정하는 규칙이다. 모델의 정직한 학습, 안정적인 batch 처리, 올바른 tensor shape 관리를 위해 꼭 필요하다.

### 아주 쉬운 예시

문장 하나를 생각해 보자.

> 나는 밥을 먹었다

Token을 4개로 나누면 다음과 같다.

1. 나는
2. 밥을
3. 먹었다
4. `<pad>`

원래 문장은 3개 token인데, batch 길이를 4로 맞추려고 마지막에 `<pad>`를 붙였다고 하자.

#### Causal mask 예시

GPT가 3번째 token “먹었다”의 hidden state를 계산한다고 하자. 이 위치는 다음처럼 볼 수 있다.

- “나는” 볼 수 있음
- “밥을” 볼 수 있음
- “먹었다” 자기 자신 볼 수 있음
- 미래 token은 볼 수 없음

만약 문장이 더 길어서 4번째 실제 token이 “그리고”였다면, 3번째 token은 4번째 token을 보면 안 된다.

작은 attention 허용 표로 보면 다음과 같다. `O`는 볼 수 있음, `X`는 볼 수 없음이다.

| Query token | Key 1: 나는 | Key 2: 밥을 | Key 3: 먹었다 |
|---|---:|---:|---:|
| 나는 | O | X | X |
| 밥을 | O | O | X |
| 먹었다 | O | O | O |

이 삼각형 모양의 mask가 causal mask다. 보통 아래쪽 삼각형은 열어 두고, 오른쪽 위 미래 영역은 막는다.

#### Padding mask 예시

이번에는 `<pad>`가 있는 경우다.

| Query token | 나는 | 밥을 | 먹었다 | `<pad>` |
|---|---:|---:|---:|---:|
| 나는 | O | O | O | X |
| 밥을 | O | O | O | X |
| 먹었다 | O | O | O | X |

모든 실제 token은 `<pad>`를 보면 안 된다. `<pad>`는 단어가 아니라 길이를 맞추기 위한 빈칸이기 때문이다.

숫자로도 볼 수 있다. 어떤 query가 key 3개에 대해 attention score를 다음처럼 만들었다고 하자.

\[
[2, 1, 5]
\]

그런데 세 번째 key가 `<pad>`라면 mask를 적용해서 다음처럼 만든다.

\[
[2, 1, -\infty]
\]

softmax를 적용하면 세 번째 위치의 attention weight는 거의 0이 된다.

\[
softmax([2, 1, -\infty]) \approx [0.73, 0.27, 0.00]
\]

즉 attention은 세 번째 padding 위치를 사실상 무시한다.

### 개념 구조와 핵심 포인트

Masking은 attention 계산의 중간 단계에 들어간다. Self-attention의 기본 흐름은 다음과 같다.

1. 각 token hidden state에서 query, key, value를 만든다.
2. Query와 key를 곱해 attention score를 만든다.
3. Mask를 score에 적용한다.
4. Softmax로 attention weight를 만든다.
5. Attention weight로 value를 가중합한다.

수식으로는 보통 이렇게 쓴다.

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}} + mask\right)V
\]

여기서 `mask`는 볼 수 있는 위치에는 0, 볼 수 없는 위치에는 `-inf`에 가까운 큰 음수 값을 넣는다. 볼 수 있는 위치에 0을 더하면 score가 그대로 유지된다. 볼 수 없는 위치에 큰 음수를 더하면 softmax 결과가 0에 가까워진다.

핵심 포인트는 다음과 같다.

1. **Causal mask는 시간 순서를 지킨다**  
   다음 token 예측 모델에서 미래 token을 보는 것을 막는다.

2. **Padding mask는 가짜 token을 제거한다**  
   Batch 처리를 위해 넣은 `<pad>`가 문맥 정보처럼 쓰이지 않게 한다.

3. **Mask는 attention weight를 직접 0에 가깝게 만든다**  
   단순히 “나중에 무시하자”가 아니라 softmax 전에 score를 조정한다.

4. **Tensor shape가 중요하다**  
   실제 구현에서는 attention score shape가 보통 `[batch, heads, query_length, key_length]`가 된다. Mask도 이 shape에 맞게 broadcasting될 수 있어야 한다.

### 핵심 수학 포인트

Attention score는 보통 다음 형태다.

\[
S = \frac{QK^T}{\sqrt{d_k}}
\]

여기서 `S[i, j]`는 i번째 query token이 j번째 key token을 얼마나 볼지에 대한 점수다. Mask는 이 score matrix에 더해진다.

간단한 3-token causal mask를 보자.

\[
mask =
\begin{bmatrix}
0 & -\infty & -\infty \\
0 & 0 & -\infty \\
0 & 0 & 0
\end{bmatrix}
\]

첫 번째 token은 자기 자신만 볼 수 있다. 두 번째 token은 첫 번째와 두 번째를 볼 수 있다. 세 번째 token은 첫 번째, 두 번째, 세 번째를 볼 수 있다.

왜 `-inf`를 쓰는지 softmax와 연결해서 보면 쉽다. Softmax는 큰 값을 큰 확률로, 작은 값을 작은 확률로 바꾼다.

\[
softmax([3, 1, -\infty]) = [약\ 0.88, 약\ 0.12, 0]
\]

`-inf` 위치는 지수 함수 `exp(-inf)`가 0이 되므로 attention weight가 0이 된다. 실제 컴퓨터에서는 진짜 `-inf` 대신 `-1e9` 같은 매우 큰 음수를 쓰기도 한다. Mixed precision 학습에서는 dtype에 따라 너무 큰 음수가 overflow 문제를 만들 수 있어, framework가 제공하는 mask 기능을 쓰는 것이 안전하다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **causal mask**: 현재 token이 미래 token을 보지 못하게 하는 mask. Autoregressive language model에서 핵심이다.
- **padding mask**: `<pad>`처럼 실제 의미가 없는 token을 attention에서 제외하는 mask.
- **attention masking**: attention score에 mask를 적용해 특정 위치의 attention weight를 0에 가깝게 만드는 전체 기법.
- **attention score**: softmax 전에 query와 key로 계산한 점수.
- **attention weight**: softmax 후 value를 얼마나 섞을지 결정하는 비율.
- **autoregressive**: 이전 token들을 바탕으로 다음 token을 하나씩 예측하거나 생성하는 방식.
- **broadcasting**: tensor shape가 완전히 같지 않아도 특정 차원을 자동으로 맞춰 연산하는 규칙.

### AI에서 어디에 쓰이는가

Causal mask는 GPT 계열 모델의 핵심이다. GPT는 “지금까지 생성된 token만 보고 다음 token을 예측”해야 한다. 학습 때도 이 조건을 지켜야 실제 생성과 학습 상황이 일치한다. 그래서 decoder-only Transformer에서는 causal mask가 거의 항상 들어간다.

Padding mask는 BERT, T5, GPT 등 batch 학습을 하는 거의 모든 NLP 모델에서 필요하다. 문장 길이는 제각각인데 GPU는 보통 같은 shape의 tensor를 한 번에 처리해야 한다. 그래서 padding을 넣고, padding mask로 가짜 위치를 제거한다.

실전 구현에서는 mask 실수가 모델 성능을 크게 망칠 수 있다. 예를 들어 causal mask가 빠지면 validation loss는 비정상적으로 좋아 보일 수 있다. 모델이 미래 정답을 보고 있기 때문이다. 반대로 padding mask가 빠지면 짧은 문장에서 attention이 `<pad>`에 분산되어 실제 단어 표현이 흐려질 수 있다.

### 헷갈리기 쉬운 포인트

- Causal mask와 padding mask는 목적이 다르다. Causal mask는 미래 차단, padding mask는 가짜 token 차단이다.
- Mask는 보통 value를 직접 지우는 것이 아니라 softmax 전 attention score를 조정한다.
- Encoder에서는 보통 causal mask를 쓰지 않는다. BERT encoder는 양방향 문맥을 보기 때문에 미래 token도 볼 수 있다. 단, padding mask는 여전히 필요하다.
- Decoder에서는 causal mask와 padding mask가 함께 쓰일 수 있다.
- `<pad>` token 자체 embedding이 있더라도, attention에서 그것을 의미 있는 문맥처럼 쓰면 안 된다.

---

## 2. 인코더-디코더 attention

### 한 줄 직관

인코더-디코더 attention은 decoder가 답을 만들 때 encoder가 읽어 둔 입력 문장을 다시 찾아보는 장치다. 번역으로 비유하면, 번역문을 한 단어씩 쓰면서 원문에서 필요한 부분을 계속 확인하는 것이다.

### 개념 정의

Transformer에는 크게 encoder와 decoder가 있다.

- **Encoder**는 입력을 읽고 각 token의 문맥 표현, 즉 hidden state를 만든다.
- **Decoder**는 지금까지 만든 출력 token을 바탕으로 다음 출력 token을 생성한다.

인코더-디코더 attention은 decoder 안에 있는 attention이다. Decoder의 현재 hidden state가 query가 되고, encoder가 만든 hidden state들이 key와 value가 된다. 그래서 이 attention을 **encoder-decoder attention** 또는 **cross attention**이라고 부른다.

Self-attention은 같은 sequence 안에서 서로를 보는 attention이다. 반면 cross attention은 한쪽 sequence가 다른 sequence를 본다. 번역에서는 출력 문장 쪽 decoder가 입력 문장 쪽 encoder output을 본다.

여기서 encoder output을 종종 **memory**라고 부른다. Decoder 입장에서는 encoder가 읽어 둔 입력 정보가 “참고할 수 있는 기억장소”처럼 작동하기 때문이다.

### 왜 이런 개념이 필요한가

기계번역을 생각해 보자.

입력: `I love cats`  
출력: `나는 고양이를 좋아한다`

Decoder가 “고양이를”이라는 단어를 만들 때는 입력의 `cats`를 강하게 참고해야 한다. “좋아한다”를 만들 때는 `love`를 참고해야 한다. 만약 decoder가 encoder output을 다시 볼 수 없다면, 입력 문장의 세부 정보를 놓치기 쉽다.

옛날 sequence-to-sequence 모델에서는 입력 문장 전체를 하나의 벡터에 압축하기도 했다. 짧은 문장은 괜찮지만 긴 문장은 정보가 많이 사라진다. Cross attention은 이 문제를 완화한다. Decoder가 매 출력 step마다 encoder의 모든 token 표현을 다시 훑어보며 필요한 부분에 attention을 줄 수 있기 때문이다.

즉 encoder-decoder attention은 “입력과 출력 사이의 연결 통로”다. Encoder가 입력을 이해하고, decoder가 출력을 만들며, cross attention이 둘을 연결한다.

### 아주 쉬운 예시

영어를 한국어로 번역하는 작은 예시를 보자.

입력 token:

1. I
2. love
3. cats

출력 token을 만들고 있다고 하자.

1. 나는
2. 고양이를
3. 좋아한다

Decoder가 두 번째 출력 token “고양이를”를 만들 때 encoder output을 본다. Attention weight가 다음처럼 나왔다고 하자.

| Encoder token | I | love | cats |
|---|---:|---:|---:|
| Attention weight for “고양이를” | 0.05 | 0.10 | 0.85 |

이 말은 decoder가 “고양이를”를 만들 때 `cats` 정보를 가장 많이 참고했다는 뜻이다.

세 번째 출력 token “좋아한다”를 만들 때는 다를 수 있다.

| Encoder token | I | love | cats |
|---|---:|---:|---:|
| Attention weight for “좋아한다” | 0.05 | 0.90 | 0.05 |

이번에는 `love`를 많이 본다. 이렇게 decoder는 출력 위치마다 입력의 다른 부분을 참고한다.

숫자로 더 작게 보면 다음과 같다. Encoder memory가 세 개의 값이라고 하자.

- `I`의 value = 1
- `love`의 value = 10
- `cats`의 value = 100

“고양이를” 위치의 attention weight가 `[0.05, 0.10, 0.85]`라면, decoder가 가져오는 context는 대략 다음과 같다.

\[
0.05\times1 + 0.10\times10 + 0.85\times100 = 86.05
\]

큰 값 100, 즉 `cats`의 정보가 대부분 반영된다. 실제 모델에서는 value가 숫자 하나가 아니라 hidden dimension을 가진 벡터다.

### 개념 구조와 핵심 포인트

Encoder-decoder attention의 구조는 self-attention과 거의 같다. 다른 점은 Q, K, V가 어디서 오느냐이다.

#### Self-attention

같은 sequence에서 Q, K, V를 모두 만든다.

\[
Q = XW_Q, \quad K = XW_K, \quad V = XW_V
\]

예를 들어 decoder self-attention에서는 decoder의 현재 출력 token hidden states에서 Q, K, V를 모두 만든다.

#### Encoder-decoder attention / Cross attention

Decoder hidden states에서 query를 만들고, encoder hidden states에서 key와 value를 만든다.

\[
Q = H_{dec}W_Q
\]

\[
K = H_{enc}W_K, \quad V = H_{enc}W_V
\]

그리고 attention은 다음처럼 계산된다.

\[
softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

여기서 `H_enc`는 encoder가 입력 문장을 읽고 만든 hidden states다. 이 `H_enc`를 memory라고 부르기도 한다.

핵심 포인트는 다음과 같다.

1. **Query는 decoder에서 온다**  
   Decoder는 “지금 내가 만들려는 출력에 필요한 입력 정보가 무엇인가?”를 묻는다.

2. **Key와 value는 encoder에서 온다**  
   Encoder는 입력 문장의 각 token에 대한 문맥 정보를 제공한다.

3. **출력 token마다 보는 입력 위치가 달라질 수 있다**  
   번역, 요약, 음성인식 등에서 alignment처럼 작동한다.

4. **Encoder output은 decoder에게 memory 역할을 한다**  
   Decoder는 생성 중에 이 memory를 반복해서 조회한다.

5. **Decoder self-attention과 cross attention은 역할이 다르다**  
   Decoder self-attention은 지금까지 생성한 출력 문맥을 보고, cross attention은 원본 입력을 본다.

### 핵심 수학 포인트

Shape로 보면 cross attention이 더 명확해진다.

예를 들어 batch는 생략하고 다음처럼 두자.

- 입력 문장 길이 `source_length = 3`
- 출력 문장 길이 `target_length = 2`
- hidden dimension `d_model = 4`

Encoder hidden states shape:

\[
H_{enc}: [3, 4]
\]

Decoder hidden states shape:

\[
H_{dec}: [2, 4]
\]

Cross attention에서는 다음을 만든다.

\[
Q: [2, d_k]
\]

\[
K: [3, d_k]
\]

\[
V: [3, d_v]
\]

그 다음 `QK^T`를 계산하면 shape는 다음과 같다.

\[
[2, d_k] \times [d_k, 3] = [2, 3]
\]

이 `[2, 3]` matrix는 “출력 token 2개가 입력 token 3개를 각각 얼마나 볼지”를 나타낸다.

예를 들어 attention weight matrix가 다음과 같다고 하자.

\[
\begin{bmatrix}
0.80 & 0.15 & 0.05 \\
0.05 & 0.10 & 0.85
\end{bmatrix}
\]

첫 번째 출력 token은 첫 번째 입력 token을 많이 보고, 두 번째 출력 token은 세 번째 입력 token을 많이 본다. 이 구조 덕분에 decoder는 출력 위치별로 필요한 입력 정보를 골라 가져올 수 있다.

중요한 점은 cross attention에서도 softmax와 gradient가 모두 학습에 연결된다는 것이다. Loss는 최종 출력 token 예측에서 계산되고, gradient는 decoder뿐 아니라 cross attention을 통해 encoder 쪽 parameter에도 전달된다. 그래서 encoder는 decoder가 잘 활용할 수 있는 memory를 만들도록 학습된다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **encoder-decoder attention**: decoder가 encoder output을 참고하는 attention.
- **cross attention**: 서로 다른 sequence 또는 서로 다른 정보원 사이에서 Q와 K,V를 연결하는 attention.
- **memory**: decoder가 참고하는 encoder hidden states. 입력 문장에 대한 저장된 문맥 정보라고 볼 수 있다.
- **source sequence**: encoder에 들어가는 입력 sequence. 번역에서는 원문이다.
- **target sequence**: decoder가 생성하는 출력 sequence. 번역에서는 번역문이다.
- **alignment**: 출력 token이 입력의 어느 부분과 대응되는지에 가까운 관계. Attention weight가 이를 어느 정도 보여 줄 수 있다.
- **context vector**: attention weight로 value들을 가중합해 만든, 현재 query에 필요한 요약 벡터.

### AI에서 어디에 쓰이는가

Encoder-decoder attention은 입력을 보고 출력을 만들어야 하는 task에서 중요하다.

- **Machine translation**: 원문을 보고 번역문을 생성한다.
- **Summarization**: 긴 문서를 읽고 요약문을 만든다.
- **Question answering**: 문서나 passage를 읽고 답변을 만든다.
- **Speech recognition**: 음성 feature를 encoder가 읽고, decoder가 text를 생성한다.
- **Image captioning**: 이미지 encoder output을 decoder가 보고 문장을 생성한다.

T5, original Transformer, BART 같은 encoder-decoder 모델은 이 cross attention 구조를 핵심으로 사용한다. GPT 같은 decoder-only 모델에는 전통적인 encoder-decoder attention block이 없다. 대신 prompt 전체를 하나의 sequence로 넣고 causal self-attention으로 처리한다. 다만 multimodal 모델에서는 text decoder가 image encoder output을 cross attention으로 보는 구조가 자주 등장한다.

실전에서 cross attention은 “조건부 생성”을 가능하게 한다. 단순히 아무 문장이나 생성하는 것이 아니라, 주어진 입력에 맞는 출력을 생성하게 해 준다. 입력에 충실한 번역, 문서 기반 답변, 이미지 설명 생성이 모두 여기에 연결된다.

### 헷갈리기 쉬운 포인트

- Cross attention은 self-attention과 계산식이 비슷하지만 Q, K, V의 출처가 다르다.
- Encoder output을 memory라고 부른다고 해서 RNN의 hidden memory처럼 하나의 벡터만 의미하는 것은 아니다. 보통 입력 token별 hidden states 전체를 뜻한다.
- Attention weight가 항상 사람이 해석하는 “정확한 이유”를 보여 주는 것은 아니다. 하지만 입력-출력 연결을 이해하는 데 유용한 힌트를 줄 수 있다.
- Decoder self-attention은 causal mask가 필요하지만, cross attention은 보통 encoder의 모든 입력 token을 볼 수 있다. 단, encoder 쪽 padding token은 padding mask로 막아야 한다.
- GPT류 decoder-only 모델과 T5류 encoder-decoder 모델은 입력을 처리하는 방식이 다르다.

---

## 3. Transformer의 병렬성과 계산비용

### 한 줄 직관

Transformer는 문장 안의 token들을 한꺼번에 계산할 수 있어 학습이 빠르지만, 모든 token 쌍을 서로 비교하기 때문에 문장이 길어질수록 attention 계산비용이 빠르게 커진다.

### 개념 정의

Transformer의 큰 장점 중 하나는 **parallelization**이다. RNN은 보통 첫 번째 token을 처리한 뒤 두 번째 token, 그 다음 세 번째 token처럼 순서대로 진행해야 한다. 반면 Transformer self-attention은 한 layer 안에서 모든 token의 query, key, value를 동시에 만들고, token들 사이의 관계도 matrix 연산으로 한꺼번에 계산할 수 있다.

하지만 이 장점에는 비용이 있다. Self-attention은 sequence 안의 모든 token 쌍을 비교한다. Token 수가 `n`이면 대략 `n × n`개의 attention score가 필요하다. 이 때문에 attention의 계산량과 memory 사용량은 sequence length에 대해 대략 **quadratic complexity**, 즉 제곱으로 증가한다.

예를 들어 token 수가 10에서 20으로 2배가 되면, token 쌍은 100개에서 400개로 4배가 된다. Token 수가 1,000에서 2,000으로 2배가 되면 attention score matrix는 1,000,000개에서 4,000,000개로 늘어난다.

### 왜 이런 개념이 필요한가

Transformer가 현대 AI의 핵심이 된 이유 중 하나는 GPU와 잘 맞기 때문이다. GPU는 많은 작은 계산을 병렬로 처리하는 데 강하다. Transformer는 attention과 linear layer를 큰 matrix multiplication으로 표현할 수 있어서 GPU에서 효율적으로 학습된다.

RNN은 순서 의존성이 강하다. 100번째 token의 hidden state를 계산하려면 99번째 token의 hidden state가 먼저 필요하다. 그래서 긴 sequence를 처리할 때 병렬화가 어렵다. Transformer는 positional encoding으로 위치 정보를 더하고, self-attention으로 모든 위치를 동시에 계산한다. 이 덕분에 긴 문장도 학습 단계에서는 훨씬 병렬화하기 쉽다.

하지만 긴 context를 다루려면 attention 비용이 문제가 된다. LLM에서 context length를 4K에서 32K, 128K로 늘리고 싶을 때 가장 먼저 부딪히는 장벽 중 하나가 attention memory다. 모든 token 쌍을 저장하고 계산해야 하기 때문이다.

즉 Transformer는 “병렬화 덕분에 학습이 강력해졌지만, 긴 sequence에서는 제곱 비용이 병목이 된다”는 trade-off를 가진다.

### 아주 쉬운 예시

학생들이 서로 한 번씩 인사해야 하는 상황을 생각해 보자.

- 학생이 3명이면 가능한 쌍은 대략 3 × 3 = 9개다.
- 학생이 4명이면 4 × 4 = 16개다.
- 학생이 10명이면 10 × 10 = 100개다.

Self-attention도 비슷하다. 각 token이 모든 token을 본다.

문장:

> 나는 오늘 학교에 갔다

Token이 4개라고 하자.

1. 나는
2. 오늘
3. 학교에
4. 갔다

각 token이 4개 token을 모두 본다면 attention score는 4 × 4 = 16개가 필요하다.

만약 token이 8개로 늘어나면 score는 8 × 8 = 64개가 된다. Token 수는 2배인데 score 수는 4배다.

작은 표로 보면 다음과 같다.

| Sequence length n | Attention score 개수 n² |
|---:|---:|
| 4 | 16 |
| 8 | 64 |
| 16 | 256 |
| 32 | 1,024 |

이게 quadratic complexity의 직관이다. 길이가 조금만 늘어도 attention matrix는 훨씬 빠르게 커진다.

### 개념 구조와 핵심 포인트

Transformer의 계산을 크게 나누면 다음과 같다.

1. **Embedding lookup**  
   Token id를 embedding vector로 바꾼다. Shape는 보통 `[batch, sequence_length, d_model]`이다.

2. **Q, K, V projection**  
   각 token hidden state에 linear layer를 적용해 query, key, value를 만든다. 이 부분은 token별로 동시에 계산하기 쉽다.

3. **Attention score 계산**  
   `QK^T`를 계산한다. 이때 sequence length가 `n`이면 attention score matrix는 `[n, n]`이 된다.

4. **Softmax와 value 가중합**  
   각 query token마다 모든 key token에 대한 weight를 만들고, value를 섞는다.

5. **FFN**  
   각 token 위치에 같은 feed-forward network를 적용한다. 이 부분도 token별로 병렬화하기 좋다.

핵심 포인트는 다음과 같다.

1. **Transformer는 layer 안에서 token들을 병렬 처리할 수 있다**  
   학습 시 teacher forcing을 사용하면 target token들도 한 번에 넣고 causal mask로 미래만 가리면 된다.

2. **Attention은 token 쌍 비교 때문에 n² 비용이 든다**  
   `n`이 sequence length일 때 attention score matrix가 `[n, n]`이다.

3. **FFN 비용도 크지만 sequence length에는 보통 선형적으로 증가한다**  
   각 token에 독립적으로 적용되므로 token 수가 2배면 FFN 계산도 대략 2배다. 반면 attention score는 4배가 된다.

4. **긴 context LLM의 핵심 병목은 attention memory다**  
   Attention score 또는 attention 관련 중간값을 저장해야 backward pass에서 gradient를 계산할 수 있다.

5. **Inference에서는 상황이 조금 다르다**  
   생성할 때는 token을 하나씩 만든다. 이때 과거 K,V를 저장하는 KV cache를 쓰면 매번 과거 전체를 다시 계산하지 않아도 된다. 하지만 context가 길수록 cache memory는 커진다.

### 핵심 수학 포인트

Self-attention의 대표 수식은 다음이다.

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

여기서 sequence length를 `n`, key/query dimension을 `d_k`라고 하자.

- `Q` shape: `[n, d_k]`
- `K` shape: `[n, d_k]`
- `QK^T` shape: `[n, n]`

`QK^T`를 계산하려면 각 query token이 각 key token과 dot product를 해야 한다. Dot product 하나는 대략 `d_k`번의 곱셈/덧셈이 필요하다. 이런 비교가 `n²`개 있으므로 attention score 계산은 대략 다음 규모가 된다.

\[
O(n^2 d_k)
\]

Big-O notation에서 핵심은 세부 상수보다 “무엇이 커질 때 얼마나 빨리 비용이 늘어나는가”다. 여기서는 sequence length `n`이 커지면 비용이 제곱으로 늘어난다는 점이 중요하다.

작은 숫자로 보자.

- `n = 4`, `d_k = 2`이면 dot product 비교는 16개, 각 비교는 2차원이다.
- `n = 8`, `d_k = 2`이면 비교는 64개다.

`d_k`는 그대로인데 `n`만 2배가 되었더니 비교 수가 4배가 되었다.

Memory도 비슷하게 생각할 수 있다. Attention weight matrix만 보아도 head 하나당 `[n, n]`을 가진다. Multi-head attention에서 head가 8개면 `[8, n, n]` 규모가 된다. Batch까지 포함하면 `[batch, heads, n, n]`이다.

예를 들어 batch 2, head 8, sequence length 1,000이면 attention weight 원소 수는 다음과 같다.

\[
2 \times 8 \times 1000 \times 1000 = 16,000,000
\]

원소 하나가 float16으로 2 bytes라면 attention weight만 단순 계산으로 약 32MB다. 실제 학습에서는 여러 layer, gradient 저장, Q/K/V, activation까지 필요하므로 훨씬 커진다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **parallelization**: 여러 계산을 동시에 처리하는 것. Transformer는 GPU에서 병렬화가 잘 된다.
- **quadratic complexity**: 입력 길이 `n`에 대해 비용이 `n²`처럼 증가하는 성질.
- **sequence length**: 모델에 들어가는 token 개수. Context length라고도 자주 연결된다.
- **matrix multiplication**: 행렬곱. Transformer 계산 대부분은 큰 matrix multiplication으로 표현된다.
- **Big-O notation**: 입력 크기가 커질 때 계산량이 어떻게 증가하는지 표현하는 표기. 예: `O(n²)`.
- **KV cache**: autoregressive inference에서 과거 token들의 key/value를 저장해 재사용하는 cache.
- **memory bottleneck**: 계산 자체보다 GPU memory 사용량이 먼저 한계가 되는 상황.

### AI에서 어디에 쓰이는가

Transformer의 병렬성은 대규모 LLM 학습의 핵심이다. 수많은 token을 GPU/TPU에서 matrix operation으로 한꺼번에 처리할 수 있기 때문에 GPT, BERT, T5 같은 모델이 대규모 데이터로 학습될 수 있었다.

하지만 quadratic complexity는 긴 문서, 긴 대화, 코드 전체 repository 분석, 장문 RAG, long-context reasoning에서 큰 문제로 나타난다. Context length를 늘리면 더 많은 정보를 넣을 수 있지만, attention 비용과 memory가 급격히 증가한다.

그래서 실전에서는 여러 해결책이 나온다.

- **FlashAttention**: attention을 더 memory-efficient하게 계산하는 구현 기법.
- **Sparse attention**: 모든 token 쌍을 보지 않고 일부 중요한 위치만 보는 방식.
- **Sliding window attention**: 가까운 주변 token 위주로 보는 방식.
- **Linear attention**: attention 비용을 sequence length에 대해 더 낮추려는 여러 연구 방향.
- **Chunking / retrieval**: 긴 문서를 한 번에 모두 넣지 않고 필요한 부분만 찾아 넣는 방식.

LLM을 사용할 때 “context length가 길면 무조건 좋다”라고만 생각하면 안 된다. 길어질수록 비용, latency, memory, attention 품질 문제가 함께 커진다. 좋은 시스템은 긴 context를 무작정 넣기보다 필요한 정보를 잘 고르고, 모델이 처리하기 좋은 형태로 구성한다.

### 헷갈리기 쉬운 포인트

- Transformer가 병렬화된다는 말은 “생성 inference에서 모든 token을 한 번에 만든다”는 뜻이 아니다. 학습에서는 정답 sequence를 알고 있으므로 한꺼번에 계산할 수 있지만, autoregressive 생성에서는 다음 token을 하나씩 만든다.
- Causal mask가 있어도 학습 중에는 matrix 계산을 한꺼번에 할 수 있다. Mask가 미래 정보를 가릴 뿐, 계산 자체는 병렬로 수행된다.
- Attention만 비용이 드는 것은 아니다. FFN도 LLM 계산량에서 매우 큰 부분을 차지한다. 다만 sequence length가 길어질 때 attention의 n² memory가 특히 문제가 된다.
- Sequence length와 hidden dimension은 다른 개념이다. Sequence length는 token 개수이고, hidden dimension은 각 token을 표현하는 벡터 크기다.
- Long context 모델은 단순히 n² 문제만 해결하면 끝나는 것이 아니다. 긴 입력에서 중요한 정보를 찾고 유지하는 모델 행동 문제도 함께 있다.

---

## 복습 질문 3개

1. Causal mask와 padding mask는 각각 어떤 정보를 보지 못하게 막는가?
2. Encoder-decoder attention에서 query는 어디서 오고, key와 value는 어디서 오는가?
3. Transformer self-attention에서 sequence length가 2배가 되면 attention score 개수는 왜 보통 4배가 되는가?

## 오늘의 한 줄 요약

Transformer는 mask로 “봐도 되는 정보”를 정하고, cross attention으로 입력과 출력을 연결하며, 병렬 계산으로 강력해졌지만 긴 sequence에서는 attention의 제곱 비용을 반드시 고려해야 한다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 24/30]

오늘은 Transformer에서 “무엇을 볼 수 있게 할 것인가”와 “얼마나 비싸게 계산되는가”를 중심으로 복습해 볼게요.

### 1. Causal mask와 padding mask는 각각 어떤 정보를 보지 못하게 막는가?

**정답**

Causal mask는 현재 token이 미래 token을 보지 못하게 막습니다.

Padding mask는 `<pad>`처럼 실제 의미가 없는 padding token을 보지 못하게 막습니다.

둘 다 attention에서 “이 위치는 참고하지 마”라고 알려 주는 attention masking입니다.

**설명**

Transformer의 attention은 기본적으로 한 token이 다른 token들을 얼마나 참고할지 계산합니다. 그런데 모든 token을 항상 다 보면 문제가 생길 수 있습니다.

Causal mask는 GPT 같은 autoregressive language model에서 중요합니다. Autoregressive는 “이전 token들을 보고 다음 token을 하나씩 예측하는 방식”입니다. 예를 들어 모델이 “나는 밥을”까지 보고 다음 단어를 맞혀야 하는데, 뒤에 있는 정답 “먹었다”를 미리 보면 안 됩니다. 그것은 시험 중에 답안지를 보는 것과 같습니다.

그래서 causal mask는 현재 위치에서 자기 자신과 과거 token만 보게 하고, 미래 token은 가립니다.

Padding mask는 목적이 다릅니다. 여러 문장을 batch로 묶을 때 문장 길이를 맞추려고 짧은 문장 뒤에 `<pad>`를 붙입니다. 하지만 `<pad>`는 실제 단어가 아닙니다. 단지 tensor shape를 맞추기 위한 빈칸입니다. Attention이 이 빈칸을 문맥처럼 참고하면 모델의 표현이 흐려질 수 있습니다.

즉 정리하면 다음과 같습니다.

Causal mask: 미래 정보 차단

Padding mask: 가짜 token 차단

**예시**

문장이 있다고 해 봅시다.

“나는 밥을 먹었다”

GPT가 “밥을” 위치에서 다음 표현을 계산하는 중이라면, 뒤의 “먹었다”를 보면 안 됩니다. 이때 causal mask가 “먹었다”를 가립니다.

반대로 batch 길이를 맞추려고 이렇게 만들었다고 해 봅시다.

“나는 밥을 먹었다 `<pad>`”

여기서 `<pad>`는 단어가 아닙니다. Padding mask는 실제 token들이 `<pad>`를 참고하지 못하게 막습니다.

**실전 연결**

LLM 학습에서 causal mask가 빠지면 validation loss가 비정상적으로 좋아질 수 있습니다. 모델이 미래 정답을 몰래 보고 있기 때문입니다. 하지만 실제 생성할 때는 미래 token이 없으므로 성능이 무너집니다.

Padding mask가 빠지면 짧은 문장을 학습할 때 모델이 `<pad>`를 의미 있는 문맥처럼 참고할 수 있습니다. 그래서 BERT, GPT, T5처럼 batch 학습을 하는 거의 모든 Transformer 모델에서 padding mask 처리가 중요합니다.

### 2. Encoder-decoder attention에서 query는 어디서 오고, key와 value는 어디서 오는가?

**정답**

Encoder-decoder attention에서 query는 decoder hidden state에서 옵니다.

Key와 value는 encoder hidden state에서 옵니다.

즉 decoder가 “지금 출력 token을 만들기 위해 입력의 어느 부분을 봐야 하지?”라고 묻고, encoder가 읽어 둔 입력 정보가 key와 value로 답을 제공합니다.

**설명**

Encoder-decoder attention은 cross attention이라고도 부릅니다. Cross attention은 서로 다른 정보원 사이를 연결하는 attention입니다.

Self-attention에서는 query, key, value가 모두 같은 sequence에서 나옵니다. 예를 들어 문장 안의 token들이 서로를 보는 구조입니다.

하지만 encoder-decoder attention은 다릅니다.

Decoder는 출력 문장을 만들고 있습니다. 예를 들어 번역에서 “나는 고양이를 좋아한다”를 생성 중입니다. 이때 decoder는 원문 “I love cats”를 참고해야 합니다.

그래서 decoder hidden state가 query가 됩니다. Query는 쉽게 말해 “내가 지금 찾고 싶은 정보”입니다.

Encoder hidden state는 key와 value가 됩니다. Key는 “어떤 정보가 어디에 있는지 찾기 위한 단서”이고, value는 “실제로 가져올 내용”이라고 생각하면 됩니다.

Encoder output을 memory라고 부르기도 합니다. Decoder 입장에서는 encoder가 입력 문장을 읽고 저장해 둔 기억장소처럼 작동하기 때문입니다.

**예시**

영어 문장을 한국어로 번역한다고 해 봅시다.

입력: “I love cats”

출력: “나는 고양이를 좋아한다”

Decoder가 “고양이를”를 만들 차례라면 입력의 “cats”를 많이 참고해야 합니다.

이때 decoder의 현재 상태가 query입니다.

Encoder가 만들어 둔 “I”, “love”, “cats”의 hidden states가 key와 value입니다.

Attention weight가 다음처럼 나올 수 있습니다.

“I”: 0.05

“love”: 0.10

“cats”: 0.85

이 말은 decoder가 “고양이를”를 만들 때 “cats” 정보를 가장 많이 참고했다는 뜻입니다.

**실전 연결**

Encoder-decoder attention은 입력을 보고 출력을 만들어야 하는 task에서 핵심입니다.

예를 들어 machine translation에서는 원문을 보고 번역문을 만듭니다. Summarization에서는 긴 문서를 보고 요약문을 만듭니다. Question answering에서는 문서를 읽고 답을 생성합니다.

T5, BART, original Transformer 같은 encoder-decoder 모델은 이 cross attention 구조를 사용합니다. 반면 GPT 같은 decoder-only 모델은 전통적인 encoder-decoder attention block이 없고, prompt 전체를 하나의 sequence로 넣은 뒤 causal self-attention으로 처리합니다.

### 3. Transformer self-attention에서 sequence length가 2배가 되면 attention score 개수는 왜 보통 4배가 되는가?

**정답**

Self-attention에서는 각 token이 모든 token을 보기 때문에 attention score 개수가 대략 sequence length × sequence length, 즉 n²개가 됩니다.

그래서 sequence length가 n에서 2n으로 늘어나면 attention score는 n²에서 (2n)² = 4n²가 됩니다.

즉 길이는 2배지만 attention score 개수는 보통 4배가 됩니다.

**설명**

Sequence length는 모델에 들어가는 token 개수입니다. 예를 들어 문장이 4개의 token으로 나뉘면 sequence length는 4입니다.

Self-attention에서는 각 token이 다른 모든 token과 관계를 계산합니다. 이 관계 점수를 attention score라고 합니다.

Token이 4개라면 다음처럼 생각할 수 있습니다.

1번 token이 1, 2, 3, 4번을 봅니다.

2번 token도 1, 2, 3, 4번을 봅니다.

3번 token도 1, 2, 3, 4번을 봅니다.

4번 token도 1, 2, 3, 4번을 봅니다.

그래서 총 4 × 4 = 16개의 attention score가 필요합니다.

만약 token이 8개가 되면 각 token이 8개를 봅니다. 그러면 8 × 8 = 64개가 됩니다.

4에서 8로 sequence length는 2배가 되었지만, attention score는 16에서 64로 4배가 되었습니다.

이런 성질을 quadratic complexity라고 합니다. 한국어로는 “제곱 복잡도”라고 볼 수 있습니다. 입력 길이 n이 커질 때 비용이 n²처럼 늘어난다는 뜻입니다.

**예시**

학생들이 서로 인사하는 상황으로 생각해 봅시다.

학생이 3명이면 각 학생이 3명을 확인해서 대략 3 × 3 = 9번의 관계가 생깁니다.

학생이 6명이면 6 × 6 = 36번의 관계가 생깁니다.

학생 수는 2배가 되었지만, 관계 수는 9에서 36으로 4배가 되었습니다.

Self-attention도 비슷합니다. Token이 많아질수록 “누가 누구를 볼지”의 조합이 빠르게 늘어납니다.

**실전 연결**

이 성질은 LLM에서 긴 context를 다룰 때 매우 중요합니다.

Context length를 4K에서 8K로 늘리면 단순히 비용이 2배만 늘어나는 것이 아니라 attention score 관점에서는 약 4배로 커질 수 있습니다. 그래서 긴 문서, 긴 대화, 코드 repository 분석, 장문 RAG를 처리할 때 GPU memory와 latency가 큰 문제가 됩니다.

이 문제를 줄이기 위해 FlashAttention, sparse attention, sliding window attention, chunking, retrieval 같은 방법들이 사용됩니다. 즉 실전에서는 긴 입력을 무조건 한 번에 많이 넣기보다, 필요한 정보를 잘 고르고 효율적으로 attention을 계산하는 것이 중요합니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-16-day24.md
