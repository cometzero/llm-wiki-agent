# AI/ML Learning Review - Day 21 (2026-05-13)
## Source Metadata
- Lesson source: /home/ubuntu/work/ai/learning/logs/2026-05-13-day21.md
- Follow-up answer source: /home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-13_09-26-24.md

---

## Lesson

# Day 21 - AI/ML 기초 학습

- Date: 2026-05-13
- Progress: 21/30
- Level: beginner-intermediate
- Milestone: 시퀀스 모델과 어텐션
- Milestone goal: 순서가 있는 데이터를 다루는 모델과 attention의 등장 배경을 이해한다.

## Today's 3 concepts

1. Query, Key, Value의 역할 분리
2. Scaled Dot-Product Attention
3. Self-Attention의 표현력

---

## 1. Query, Key, Value의 역할 분리

### 한 줄 직관

Query, Key, Value는 attention에서 “내가 찾는 것”, “각 정보가 가진 이름표”, “실제로 가져올 내용”을 서로 나누어 생각하는 방식입니다.

### 개념 정의

attention은 많은 정보 중에서 지금 필요한 정보를 더 많이 가져오는 메커니즘입니다. 그런데 “필요한 정보”를 고르려면 적어도 세 가지가 필요합니다.

1. 지금 내가 무엇을 찾고 있는지
2. 각 후보 정보가 어떤 특징을 가지고 있는지
3. 선택한 뒤 실제로 가져올 내용이 무엇인지

이 세 역할을 attention에서는 각각 다음처럼 부릅니다.

- **query**: 지금 찾고 싶은 것, 또는 현재 위치의 질문
- **key**: 각 후보 정보가 가진 검색용 특징, 또는 이름표
- **value**: key로 선택된 뒤 실제로 섞어 가져올 내용

예를 들어 도서관에서 책을 찾는 상황을 생각해 봅시다.

- query: “딥러닝 attention을 쉽게 설명한 책을 찾고 싶다”
- key: 각 책의 제목, 태그, 분류번호, 주제어
- value: 실제 책 내용

우리는 query와 key를 비교해서 어떤 책이 관련 있는지 판단합니다. 관련성이 높으면 그 책의 value, 즉 실제 내용을 더 많이 읽습니다.

AI 모델에서도 비슷합니다. 문장 안의 각 token은 embedding vector로 표현됩니다. attention layer는 이 embedding에서 query vector, key vector, value vector를 각각 만들어 냅니다. 그리고 query와 key의 잘 맞는 정도를 계산한 뒤, 그 결과로 value들을 가중합(weighted sum)합니다.

### 왜 이런 개념이 필요한가

RNN처럼 순서대로 읽는 모델은 이전 정보가 hidden state 하나에 압축되어 들어갑니다. 문장이 길어지면 어떤 단어가 어떤 단어와 연결되는지 직접 고르기 어렵습니다.

예를 들어 다음 문장을 봅시다.

```text
철수가 민수에게 빌린 책을 어제 도서관에서 반납했다.
```

여기서 `반납했다`를 이해하려면 `책`이 중요합니다. `철수`, `민수`, `어제`, `도서관`도 정보이지만, 동사 `반납했다`와 특히 강하게 연결되는 것은 `책`입니다.

attention은 각 위치가 문장 안의 다른 위치를 직접 바라볼 수 있게 합니다. 그런데 “어떤 위치가 무엇을 기준으로 다른 위치를 볼 것인가?”를 명확히 해야 합니다. 그래서 query, key, value를 분리합니다.

이 분리가 중요한 이유는 다음과 같습니다.

- query는 현재 token이 필요한 정보를 표현합니다.
- key는 다른 token들이 자신을 찾을 수 있게 내놓는 검색용 특징입니다.
- value는 실제로 다음 표현을 만들 때 가져올 내용입니다.

만약 key와 value가 항상 완전히 같은 역할이라면, “검색 기준”과 “전달할 내용”을 분리해서 학습할 수 없습니다. 하지만 실제 언어에서는 어떤 단어가 검색될 때 중요한 특징과, 검색된 뒤 전달해야 할 의미가 다를 수 있습니다.

예를 들어 `은행`이라는 단어는 문맥에 따라 금융기관일 수도 있고 강가의 둑일 수도 있습니다. key는 “나를 어떤 문맥에서 찾아야 하는가”를 나타내고, value는 “선택되었을 때 어떤 정보를 전달할 것인가”를 나타냅니다. 모델은 학습을 통해 이 둘을 다르게 조정할 수 있습니다.

### 아주 쉬운 예시

아주 작은 숫자 예시를 보겠습니다.

현재 token이 `먹었다`라고 합시다. 이 token은 “무엇을 먹었는가?”를 찾고 싶습니다. 그래서 query를 아주 단순하게 숫자 하나로 표현해 보겠습니다.

```text
query: 2
```

문장 안에 후보 token 세 개가 있습니다.

```text
사과    key: 2, value: 10
어제    key: 0, value: 3
친구와  key: 1, value: 5
```

여기서 key는 “먹었다와 얼마나 관련될 수 있는가”를 나타내는 검색용 숫자라고 생각해 봅시다. query와 key를 곱해서 관련 점수, 즉 **compatibility score**를 만들면 다음과 같습니다.

```text
사과:   query 2 × key 2 = 4
어제:   query 2 × key 0 = 0
친구와: query 2 × key 1 = 2
```

점수가 가장 큰 것은 `사과`입니다. 그러면 모델은 `사과`의 value를 가장 많이 가져오게 됩니다.

여기서 중요한 점은 `key`와 `value`가 다르다는 것입니다.

- key는 찾기 위한 표지입니다. `사과`가 먹는 대상일 가능성이 높다는 검색 특징입니다.
- value는 실제로 가져와서 새 표현에 섞을 정보입니다. 여기서는 단순히 `10`이라고 했지만, 실제 모델에서는 여러 차원의 vector입니다.

비유하면 스마트폰 사진 앱에서 검색하는 것과 비슷합니다.

- query: “강아지 사진 찾아줘”
- key: 각 사진의 태그나 이미지 특징
- value: 실제 사진 데이터

검색은 key로 하지만, 결과로 보는 것은 value입니다.

### 개념 구조와 핵심 포인트

QKV 구조는 보통 하나의 입력 embedding에서 시작합니다. 어떤 token의 embedding이 `x`라고 하면, 모델은 학습 가능한 linear layer를 사용해서 세 vector를 만듭니다.

```text
q = xW_Q
k = xW_K
v = xW_V
```

여기서 `W_Q`, `W_K`, `W_V`는 학습되는 weight matrix입니다. 같은 입력 `x`라도 서로 다른 weight를 통과하기 때문에 query, key, value가 다르게 만들어집니다.

핵심 포인트는 다음과 같습니다.

1. **query는 현재 위치의 질문입니다.**  
   예를 들어 `먹었다` 위치의 query는 “먹은 대상이 어디 있지?” 같은 정보를 담을 수 있습니다.

2. **key는 각 위치의 검색용 특징입니다.**  
   `사과`의 key는 “나는 먹을 수 있는 대상이다”라는 방향의 특징을 담을 수 있습니다. 물론 모델이 실제로 이런 문장으로 생각하는 것은 아니지만, vector 공간에서 그런 구분이 학습됩니다.

3. **value는 실제로 전달되는 내용입니다.**  
   attention weight가 정해지면 value들이 섞입니다. 최종 출력은 key가 아니라 value의 조합입니다.

4. **compatibility score는 query와 key가 얼마나 잘 맞는지 나타냅니다.**  
   보통 dot product로 계산합니다. 두 vector가 비슷한 방향을 가리키면 점수가 커집니다.

5. **QKV는 token interaction의 기본 부품입니다.**  
   Transformer에서 각 token은 자기 query로 다른 token들의 key를 훑어보고, 필요한 value를 가져와 자신의 표현을 업데이트합니다.

Tensor shape 관점으로도 간단히 보면 좋습니다. 예를 들어 문장 길이가 4이고 embedding 차원이 8이면 입력은 대략 다음 shape를 가질 수 있습니다.

```text
X shape: 4 × 8
Q shape: 4 × d_k
K shape: 4 × d_k
V shape: 4 × d_v
```

각 token마다 query, key, value가 하나씩 생깁니다. 그래서 길이 4인 문장에서는 query 4개, key 4개, value 4개가 생깁니다.

### 핵심 수학 포인트

가장 기본적인 수학은 query와 key의 dot product입니다.

두 vector가 있다고 합시다.

```text
q = [1, 2]
k = [3, 1]
```

dot product는 같은 위치끼리 곱해서 더합니다.

```text
q · k = 1×3 + 2×1 = 5
```

이 값이 compatibility score입니다. 직관적으로는 두 vector가 얼마나 같은 방향을 보고 있는지 나타냅니다.

아주 단순하게 생각하면 다음과 같습니다.

- q와 k가 비슷한 특징을 강조하면 점수가 큽니다.
- q와 k가 별로 관련 없으면 점수가 작습니다.
- 점수가 크면 해당 value를 더 많이 가져옵니다.

실제 attention에서는 한 query가 모든 key와 점수를 계산합니다.

```text
scores = qK^T
```

여기서 `K^T`는 key matrix를 transpose한 것입니다. transpose는 행과 열을 바꾸는 연산입니다. 왜 바꾸냐면 query와 모든 key의 dot product를 한 번에 계산하기 위해서입니다.

작은 예를 들어 보겠습니다.

```text
q = [1, 0]
key_1 = [1, 0]
key_2 = [0, 1]
key_3 = [1, 1]
```

점수는 다음과 같습니다.

```text
q · key_1 = 1
q · key_2 = 0
q · key_3 = 1
```

이 query는 첫 번째 특징을 보는 query입니다. 그래서 첫 번째 특징이 있는 key_1과 key_3에 높은 점수를 줍니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **query**: 현재 위치가 찾고 싶은 정보의 기준입니다. “내 질문”이라고 생각하면 쉽습니다.
- **key**: 각 위치가 가진 검색용 특징입니다. query와 비교되어 선택될지 말지가 결정됩니다.
- **value**: 선택된 뒤 실제로 가져와서 섞는 내용입니다. 최종 attention output은 value들의 조합입니다.
- **compatibility score**: query와 key가 얼마나 잘 맞는지 나타내는 점수입니다. 보통 dot product로 계산합니다.
- **dot product**: 두 vector의 같은 위치 원소를 곱해서 더하는 연산입니다. attention에서는 관련성 점수 계산에 자주 쓰입니다.
- **embedding**: token을 숫자 vector로 바꾼 표현입니다. QKV는 보통 embedding에서 만들어집니다.

### AI에서 어디에 쓰이는가

QKV는 Transformer 계열 모델의 핵심입니다. BERT, GPT, T5, Vision Transformer 같은 모델이 모두 attention 구조를 사용하고, 그 중심에 query, key, value가 있습니다.

LLM에서는 어떤 단어를 생성할 때 이전 token들 중 어떤 정보를 참고할지 결정해야 합니다. 예를 들어 모델이 다음 문장을 이어 쓴다고 합시다.

```text
프랑스의 수도는
```

`수도` 위치의 query는 나라 이름과 관련된 정보를 찾을 수 있습니다. `프랑스` token의 key는 그 정보와 잘 맞을 수 있고, value는 “프랑스라는 나라에 대한 의미 정보”를 전달합니다. 그러면 모델은 다음 token으로 `파리`를 예측할 가능성을 높입니다.

실전 구현에서는 QKV가 대량의 tensor 연산으로 계산됩니다. 모델이 커질수록 attention 계산은 많은 메모리와 연산량을 사용합니다. 그래서 FlashAttention 같은 최적화 기법도 결국 QKV attention을 더 빠르고 메모리 효율적으로 계산하려는 시도입니다.

### 헷갈리기 쉬운 포인트

1. **query, key, value는 사람이 직접 정한 태그가 아닙니다.**  
   모델 안의 weight matrix가 학습하면서 만들어 내는 vector입니다.

2. **key와 value는 같은 token에서 나오지만 역할이 다릅니다.**  
   key는 “검색될 때 쓰는 특징”이고, value는 “선택된 뒤 전달되는 내용”입니다.

3. **attention이 value를 고르는 기준은 query-key 점수입니다.**  
   최종 출력은 value들의 weighted sum이지만, weight를 만드는 것은 query와 key입니다.

4. **compatibility score가 곧 최종 확률은 아닙니다.**  
   score는 softmax를 거쳐 attention weight가 됩니다. score가 크면 weight도 대체로 커지지만, 전체 후보들과 함께 비교된 뒤 결정됩니다.

5. **QKV는 NLP에만 쓰이지 않습니다.**  
   이미지 patch, 음성 frame, 단백질 sequence, 추천 시스템의 item 표현 등 다양한 데이터에서 쓰입니다.

---

## 2. Scaled Dot-Product Attention

### 한 줄 직관

Scaled Dot-Product Attention은 query와 key의 dot product로 관련성을 계산하고, 너무 큰 점수가 되지 않도록 scale한 뒤, softmax로 비율을 만들고, 그 비율만큼 value를 섞는 방법입니다.

### 개념 정의

Scaled Dot-Product Attention은 Transformer에서 가장 기본이 되는 attention 계산 방식입니다. 한 문장으로 쓰면 다음과 같습니다.

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

처음 보면 복잡해 보이지만, 실제 순서는 단순합니다.

1. query와 key를 dot product해서 관련성 점수를 구합니다.
2. 점수를 `sqrt(d_k)`로 나누어 너무 커지지 않게 조절합니다.
3. softmax를 적용해서 합이 1인 attention weight로 바꿉니다.
4. attention weight만큼 value들을 섞어 output을 만듭니다.

여기서 `d_k`는 key vector의 차원 수입니다. 예를 들어 key가 `[0.2, 0.5, -0.1, 0.7]`처럼 숫자 4개짜리 vector이면 `d_k = 4`입니다. `sqrt(d_k)`는 `d_k`의 square root, 즉 제곱근입니다. `d_k = 4`이면 `sqrt(d_k) = 2`입니다.

### 왜 이런 개념이 필요한가

attention의 목표는 “많은 정보 중 무엇을 얼마나 볼 것인가”를 정하는 것입니다. 이때 단순히 query와 key의 dot product만 쓰면 문제가 생길 수 있습니다.

vector 차원이 커지면 dot product 값도 커지기 쉽습니다. 예를 들어 각 원소가 대충 1 근처라고 하면:

```text
차원 2: 1×1 + 1×1 = 2
차원 8: 1×1 + ... + 1×1 = 8
차원 64: 1을 64번 더해서 64
```

점수가 너무 커지면 softmax가 한 후보에 거의 모든 weight를 몰아줄 수 있습니다. 그러면 attention이 너무 날카로워지고, 학습 초기에 gradient가 불안정해질 수 있습니다.

softmax는 큰 숫자 차이를 더 크게 느끼게 만드는 성질이 있습니다. 예를 들어 점수 `[1, 2]`는 부드러운 차이지만, 점수 `[10, 20]`은 거의 두 번째만 고르는 결과가 됩니다. dot product가 차원 때문에 커지면, 모델이 아직 제대로 배우기 전부터 “무조건 하나만 봐!”처럼 행동할 수 있습니다.

그래서 `sqrt(d_k)`로 나눕니다. 이 scaling은 점수의 크기를 적당히 줄여 softmax가 너무 극단적으로 변하지 않게 도와줍니다.

### 아주 쉬운 예시

후보가 두 개 있다고 합시다.

```text
score A = 2
score B = 4
```

softmax를 적용하면 B가 더 큰 weight를 받습니다. 정확한 값은 대략 다음과 비슷합니다.

```text
A weight ≈ 0.12
B weight ≈ 0.88
```

B가 꽤 많이 선택됩니다.

그런데 점수가 차원 때문에 커져서 다음처럼 되었다고 해 봅시다.

```text
score A = 20
score B = 40
```

차이는 여전히 “B가 A보다 2배 크다”처럼 보일 수 있지만, softmax는 거의 B만 선택합니다.

```text
A weight ≈ 거의 0
B weight ≈ 거의 1
```

이렇게 되면 모델이 다양한 정보를 섞기 어렵습니다.

이제 scaling을 해 봅시다. key 차원이 `d_k = 4`라면 `sqrt(d_k) = 2`입니다.

```text
scaled score A = 20 / 2 = 10
scaled score B = 40 / 2 = 20
```

아직 크지만 줄었습니다. 실제 모델에서는 `d_k`가 64면 `sqrt(64)=8`이므로, 큰 dot product를 더 의미 있게 낮춥니다.

value를 섞는 예시도 보겠습니다.

```text
attention weight: [0.25, 0.75]
value A: 10
value B: 20
```

출력은 weighted sum입니다.

```text
output = 0.25×10 + 0.75×20
       = 2.5 + 15
       = 17.5
```

즉 attention output은 하나를 딱 고르는 것이 아니라, 여러 value를 비율대로 섞은 결과입니다.

일상 비유로는 요리 레시피와 비슷합니다. 국물 맛을 만들 때 소금 25%, 간장 75%처럼 재료를 섞는다고 생각할 수 있습니다. attention weight는 각 재료를 얼마나 넣을지 정하는 비율입니다. value는 실제 재료입니다.

### 개념 구조와 핵심 포인트

Scaled Dot-Product Attention의 전체 흐름은 다음과 같습니다.

1. **점수 계산: `QK^T`**  
   모든 query와 모든 key의 dot product를 계산합니다. 문장 길이가 4이면, 각 token이 다른 4개 token을 얼마나 볼지에 대한 4×4 점수 matrix가 생길 수 있습니다.

2. **scale: `/ sqrt(d_k)`**  
   key 차원이 커질 때 dot product가 너무 커지는 문제를 줄입니다. softmax가 너무 극단적으로 되는 것을 완화합니다.

3. **softmax**  
   각 query 기준으로 후보 key들에 대한 점수를 확률처럼 해석 가능한 weight로 바꿉니다. 모든 weight의 합은 1입니다.

4. **value와 곱하기: `weights V`**  
   weight만큼 value vector들을 섞습니다. 최종 결과는 각 token의 새 표현입니다.

작은 shape 예시를 들어 보겠습니다.

```text
문장 길이: 3
key/query 차원 d_k: 2
value 차원 d_v: 4

Q shape: 3 × 2
K shape: 3 × 2
V shape: 3 × 4
QK^T shape: 3 × 3
attention weight shape: 3 × 3
output shape: 3 × 4
```

`3 × 3` attention weight matrix는 “각 token이 세 token을 각각 얼마나 보는지”를 담습니다. 예를 들어 두 번째 token의 attention weight가 다음과 같을 수 있습니다.

```text
[0.1, 0.7, 0.2]
```

이 뜻은 두 번째 token이 새 표현을 만들 때:

- 첫 번째 token의 value를 10%
- 자기 자신의 value를 70%
- 세 번째 token의 value를 20%

섞는다는 뜻입니다.

### 핵심 수학 포인트

핵심 공식은 다음입니다.

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

각 부분을 하나씩 해석해 보겠습니다.

#### 1. `QK^T`: 관련성 점수 matrix

하나의 query `q`와 하나의 key `k`에 대해:

```text
score = q · k
```

여러 query와 key를 한 번에 계산하면 matrix가 됩니다.

예를 들어 query가 2개, key가 3개라면 score matrix는 2×3입니다.

```text
각 행: 한 query가 모든 key를 본 점수
각 열: 특정 key가 얼마나 선택되는지에 해당
```

#### 2. `/ sqrt(d_k)`: scale

`d_k`가 64이면 `sqrt(d_k)=8`입니다. 점수를 8로 나누면 softmax에 들어가는 값이 너무 커지지 않습니다.

간단한 예를 봅시다.

```text
raw scores: [8, 16]
d_k = 16, sqrt(d_k) = 4
scaled scores: [2, 4]
```

원래 `[8, 16]`은 softmax에서 매우 극단적인 차이를 만들 수 있습니다. `[2, 4]`로 줄이면 여전히 두 번째가 더 중요하지만, 학습하기에 더 부드러운 분포가 됩니다.

#### 3. `softmax`: 합이 1인 weight 만들기

softmax는 여러 점수를 받아 양수 weight로 바꾸고, 전체 합이 1이 되게 합니다.

예를 들어 softmax 결과가 다음과 같다면:

```text
[0.2, 0.3, 0.5]
```

세 값은 모두 0 이상이고 합은 1입니다.

```text
0.2 + 0.3 + 0.5 = 1.0
```

이제 이 값들을 attention weight라고 부릅니다.

#### 4. `weights V`: value weighted sum

attention weight와 value를 곱해 섞습니다.

```text
weights = [0.2, 0.3, 0.5]
values = [10, 20, 40]

output = 0.2×10 + 0.3×20 + 0.5×40
       = 2 + 6 + 20
       = 28
```

실제 모델에서는 value가 숫자 하나가 아니라 vector입니다. 예를 들어 value가 `[의미1, 의미2, 의미3, ...]` 같은 여러 차원으로 되어 있고, weighted sum도 각 차원별로 계산됩니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **scaled dot-product attention**: dot product attention에 `sqrt(d_k)` scaling을 추가한 Transformer의 기본 attention 방식입니다.
- **softmax**: 여러 점수를 합이 1인 양수 weight로 바꾸는 함수입니다. attention에서는 “얼마나 볼지”를 나타내는 비율을 만듭니다.
- **attention weight**: 각 value를 얼마나 섞을지 정하는 weight입니다. softmax 결과입니다.
- **weighted sum**: 각 항목에 weight를 곱해 더하는 방식입니다. attention output은 value들의 weighted sum입니다.
- **d_k**: key/query vector의 차원 수입니다. scaling에 사용됩니다.
- **sqrt**: square root, 제곱근입니다. `sqrt(64)=8`입니다.

### AI에서 어디에 쓰이는가

Scaled Dot-Product Attention은 Transformer의 기본 연산입니다. GPT 계열 LLM은 다음 token을 예측할 때 이전 token들의 value를 attention weight로 섞습니다. BERT는 문장 전체를 보면서 각 token의 문맥적 표현을 만듭니다. Vision Transformer는 이미지를 작은 patch로 나누고, patch들끼리 attention을 계산합니다.

실전에서 이 개념이 중요한 이유는 다음과 같습니다.

1. **모델의 문맥 이해 능력과 직접 연결됩니다.**  
   attention weight가 어떤 token에 높게 걸리는지 보면 모델이 어떤 정보를 참고했는지 어느 정도 해석할 수 있습니다. 완전한 설명은 아니지만, 모델 내부 동작을 이해하는 실마리가 됩니다.

2. **연산량과 메모리 사용량에 큰 영향을 줍니다.**  
   문장 길이가 `n`이면 attention score matrix는 대략 `n × n`입니다. 문장이 1,000 token이면 1,000×1,000 = 1,000,000개의 점수가 필요합니다. 그래서 긴 context를 다루는 LLM에서는 attention 최적화가 매우 중요합니다.

3. **학습 안정성과 관련됩니다.**  
   scaling이 없으면 softmax가 너무 극단적이 되어 gradient 흐름이 나빠질 수 있습니다. gradient는 loss를 줄이기 위해 weight를 어떻게 바꿀지 알려 주는 신호입니다. attention weight가 너무 한쪽으로 굳어지면, 다양한 후보에서 배우는 신호가 약해질 수 있습니다.

4. **구현에서 tensor shape 이해가 필수입니다.**  
   실제 PyTorch나 TensorFlow 구현에서는 `Q`, `K`, `V`의 shape가 맞아야 합니다. shape가 어긋나면 matrix multiplication이 실패합니다.

### 헷갈리기 쉬운 포인트

1. **scale은 attention weight를 직접 나누는 것이 아닙니다.**  
   softmax 전에 score를 나눕니다. 순서는 `score → scale → softmax → value 혼합`입니다.

2. **softmax output은 확률처럼 보이지만 반드시 인간이 해석하는 확률은 아닙니다.**  
   합이 1인 weight라서 비율로 볼 수 있지만, “모델이 70% 확률로 이 단어를 믿는다”처럼 너무 단순하게 해석하면 안 됩니다.

3. **attention은 하나를 고르는 hard selection이 아닙니다.**  
   보통 여러 value를 부드럽게 섞습니다. weight가 `[0, 1, 0]`처럼 극단적이면 하나만 고르는 것처럼 보일 수 있지만, 일반적으로는 soft mixing입니다.

4. **dot product score가 크다고 항상 좋은 것은 아닙니다.**  
   너무 큰 score는 softmax를 지나면서 한쪽으로 몰릴 수 있습니다. scaling이 필요한 이유입니다.

5. **`d_k`와 문장 길이를 혼동하지 않아야 합니다.**  
   `d_k`는 key vector의 차원 수이고, 문장 길이는 token 개수입니다. 둘은 다른 개념입니다.

---

## 3. Self-Attention의 표현력

### 한 줄 직관

Self-Attention은 문장 안의 각 token이 같은 문장 안의 다른 token들을 직접 참고해서, 자기 표현을 문맥에 맞게 다시 만드는 방법입니다.

### 개념 정의

Self-Attention에서 “self”는 query, key, value가 모두 같은 입력 sequence에서 나온다는 뜻입니다. 즉 한 문장의 token들이 서로를 바라보며 정보를 주고받습니다.

예를 들어 다음 문장을 봅시다.

```text
그는 사과를 먹었다.
```

`먹었다`라는 token은 `사과`를 참고해야 자연스럽습니다. `그는`은 누가 행동했는지를 알려 줍니다. Self-Attention은 각 token이 문장 안의 다른 token들과 연결되어 자신의 새 표현을 만들 수 있게 합니다.

RNN에서는 정보가 순서대로 흘러갑니다. 앞 단어에서 뒤 단어로 한 단계씩 전달됩니다. 반면 Self-Attention에서는 한 layer 안에서 멀리 떨어진 token도 직접 연결될 수 있습니다. 문장 첫 단어와 마지막 단어가 멀리 떨어져 있어도 attention weight가 높으면 바로 정보를 주고받을 수 있습니다.

이것을 **token interaction**이라고 볼 수 있습니다. token interaction은 token들 사이의 상호작용입니다. Self-Attention은 token interaction을 강하게 만들어 줍니다.

최종적으로 각 token의 표현은 여러 token의 value가 섞인 결과가 됩니다. 이것을 **context mixing**이라고 생각할 수 있습니다. 즉 자기 혼자만의 embedding이 아니라, 문맥이 섞인 embedding이 됩니다.

### 왜 이런 개념이 필요한가

같은 단어라도 문맥에 따라 의미가 달라집니다.

```text
나는 은행에서 돈을 찾았다.
나는 강가의 은행에 앉았다.
```

첫 번째 `은행`은 bank입니다. 두 번째 `은행`은 river bank에 가깝습니다. 단어 자체만 보면 둘 다 `은행`이지만, 주변 단어가 의미를 결정합니다.

전통적인 단어 embedding은 같은 단어에 같은 vector를 줄 수 있습니다. 하지만 실제 언어 이해에서는 문맥이 필요합니다. Self-Attention은 각 token이 주변 token들을 참고해 자신의 표현을 문맥에 맞게 바꿉니다.

예를 들어 첫 번째 문장에서 `은행` token은 `돈`, `찾았다`와 강하게 interaction할 수 있습니다. 두 번째 문장에서는 `강가`, `앉았다`와 더 강하게 interaction할 수 있습니다. 그러면 같은 `은행`이라도 layer를 지난 뒤의 hidden state는 서로 달라집니다.

LLM이 문장을 자연스럽게 이해하고 생성하려면 이런 문맥 혼합 능력이 꼭 필요합니다. 다음 단어를 예측할 때 단어 하나만 보는 것이 아니라, 앞에서 나온 여러 단서가 함께 필요하기 때문입니다.

### 아주 쉬운 예시

문장이 세 token으로 되어 있다고 합시다.

```text
[나는, 사과를, 먹었다]
```

`먹었다` token이 새 표현을 만들 때 attention weight가 다음과 같다고 해 봅시다.

```text
나는:   0.2
사과를: 0.6
먹었다: 0.2
```

value를 아주 단순한 숫자로 표현해 보겠습니다.

```text
나는 value = 1
사과를 value = 10
먹었다 value = 5
```

그러면 `먹었다`의 새 표현은 다음처럼 계산됩니다.

```text
new representation of 먹었다
= 0.2×1 + 0.6×10 + 0.2×5
= 0.2 + 6 + 1
= 7.2
```

이 숫자 `7.2`는 단순 예시일 뿐입니다. 핵심은 `먹었다`의 표현이 자기 자신만으로 만들어진 것이 아니라, `나는`, `사과를`, `먹었다`의 정보가 섞여 만들어졌다는 점입니다. 특히 `사과를`의 weight가 크기 때문에 “무엇을 먹었는지” 정보가 많이 반영됩니다.

이번에는 다른 문장입니다.

```text
[나는, 물을, 마셨다]
```

`마셨다` token은 `물을`을 강하게 볼 것입니다. 이런 방식으로 Self-Attention은 동사와 목적어, 주어와 동사, 대명사와 지칭 대상 같은 관계를 학습할 수 있습니다.

일상 비유로는 회의와 비슷합니다. 한 사람이 결론을 말할 때 자기 생각만 말하는 것이 아니라, 회의에 참여한 다른 사람들의 의견을 듣고 자신의 말을 조정합니다. Self-Attention에서 각 token은 작은 회의 참가자처럼 다른 token들의 정보를 듣고 자기 표현을 업데이트합니다.

### 개념 구조와 핵심 포인트

Self-Attention의 구조는 다음 흐름으로 이해할 수 있습니다.

1. **각 token을 embedding으로 바꿉니다.**  
   예를 들어 `[나는, 사과를, 먹었다]`가 각각 vector가 됩니다.

2. **각 embedding에서 Q, K, V를 만듭니다.**  
   같은 문장 안의 모든 token이 query, key, value를 가집니다.

3. **각 token의 query가 모든 token의 key와 점수를 계산합니다.**  
   `먹었다`의 query는 `나는`, `사과를`, `먹었다`의 key를 모두 비교할 수 있습니다.

4. **softmax로 attention weight를 만듭니다.**  
   어떤 token을 얼마나 참고할지 비율이 됩니다.

5. **value들을 weighted sum해서 새 hidden state를 만듭니다.**  
   이 새 hidden state는 문맥이 섞인 표현입니다.

Self-Attention의 표현력이 강한 이유는 token들 사이의 관계를 직접 만들 수 있기 때문입니다.

- 가까운 token뿐 아니라 먼 token도 볼 수 있습니다.
- 한 token이 여러 token을 동시에 참고할 수 있습니다.
- layer를 여러 개 쌓으면 더 복잡한 관계를 단계적으로 만들 수 있습니다.
- multi-head attention을 쓰면 서로 다른 관점의 관계를 동시에 볼 수 있습니다.

예를 들어 한 head는 문법적 관계를 볼 수 있고, 다른 head는 의미적 관계를 볼 수 있습니다. 실제로 head가 항상 사람이 이해하기 쉬운 역할로 깔끔하게 나뉘는 것은 아니지만, 구조적으로는 여러 종류의 interaction을 학습할 여지를 줍니다.

중요한 점은 Self-Attention output이 고정된 단어 의미가 아니라는 것입니다. layer를 지날수록 token representation은 문맥에 맞게 바뀝니다.

```text
초기 embedding: 단어 자체의 기본 의미가 강함
중간 hidden state: 주변 문맥이 섞임
깊은 layer의 hidden state: 문장 전체 역할, 추론 단서, 다음 token 예측에 필요한 정보가 더 많이 반영됨
```

### 핵심 수학 포인트

Self-Attention도 기본 공식은 Scaled Dot-Product Attention과 같습니다.

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

다만 Self-Attention에서는 `Q`, `K`, `V`가 모두 같은 입력 `X`에서 만들어집니다.

```text
Q = XW_Q
K = XW_K
V = XW_V
```

여기서 `X`는 문장 전체 token embedding matrix입니다. 예를 들어 문장 길이가 3이고 embedding 차원이 4라면:

```text
X shape: 3 × 4
```

각 token의 embedding이 한 행(row)입니다. 여기에 세 weight matrix를 곱해서 Q, K, V를 만듭니다.

Self-Attention의 중요한 수학적 결과는 attention weight matrix입니다.

문장 길이가 3이면 attention weight는 3×3입니다.

```text
          보는 대상
          나는  사과를  먹었다
보는 token
나는      0.5   0.2    0.3
사과를    0.1   0.7    0.2
먹었다    0.2   0.6    0.2
```

각 행은 합이 1입니다. 예를 들어 `먹었다` 행은 다음과 같습니다.

```text
0.2 + 0.6 + 0.2 = 1.0
```

이 행은 `먹었다`가 새 표현을 만들 때 각 token의 value를 얼마나 섞는지 나타냅니다.

여기서 중요한 것은 출력도 sequence 형태를 유지한다는 점입니다.

```text
입력 X: token 3개의 표현
출력 O: token 3개의 새 표현
```

Self-Attention은 문장 전체를 하나의 vector로 바로 압축하는 것이 아니라, 각 token의 표현을 문맥에 맞게 업데이트합니다. 그래서 다음 layer에서 다시 더 복잡한 관계를 만들 수 있습니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **self-attention**: 같은 sequence 안의 token들이 서로를 참고해 새 표현을 만드는 attention 방식입니다.
- **token interaction**: token들 사이의 상호작용입니다. Self-Attention은 각 token이 다른 token의 정보를 직접 참고하게 만듭니다.
- **context mixing**: 여러 token의 정보가 attention weight에 따라 섞여 문맥적 표현이 되는 과정입니다.
- **hidden state**: layer를 지난 뒤의 내부 표현입니다. Transformer에서는 각 token의 hidden state가 layer마다 업데이트됩니다.
- **contextual embedding**: 문맥에 따라 달라지는 embedding입니다. 같은 단어라도 주변 단어가 다르면 표현이 달라집니다.
- **multi-head attention**: attention을 여러 head로 나누어 서로 다른 관점의 관계를 동시에 학습하게 하는 구조입니다.

### AI에서 어디에 쓰이는가

Self-Attention은 현대 LLM의 핵심입니다. GPT는 이전 token들을 self-attention으로 참고해서 다음 token을 예측합니다. BERT는 문장 안의 양쪽 문맥을 함께 보며 각 token의 의미를 파악합니다. 번역 모델은 원문 내부 관계와 번역문 내부 관계를 self-attention으로 다룹니다.

실전에서 Self-Attention의 표현력은 다음과 같은 문제를 해결하는 데 중요합니다.

1. **긴 거리 의존성(long-range dependency)**  
   문장 앞에 나온 주어가 문장 뒤의 동사와 연결될 수 있습니다. RNN은 여러 단계를 거쳐야 하지만, self-attention은 직접 연결할 수 있습니다.

2. **대명사 해석**  
   `민수는 철수에게 책을 줬다. 그는 고마워했다.`에서 `그`가 누구인지 문맥으로 판단해야 합니다. Attention은 관련 token들을 참고해 표현을 조정할 수 있습니다.

3. **동음이의어 처리**  
   `은행`처럼 같은 단어가 다른 의미를 가질 때 주변 token과의 interaction으로 의미를 구분할 수 있습니다.

4. **코드 이해**  
   코드 모델에서는 변수 사용 위치가 멀리 떨어져 있을 수 있습니다. Self-Attention은 변수 선언과 사용 부분을 연결하는 데 도움이 됩니다.

5. **이미지와 멀티모달 모델**  
   Vision Transformer에서는 이미지 patch들 사이의 관계를 self-attention으로 학습합니다. 멀티모달 모델에서는 텍스트 token과 이미지 patch 표현이 서로 연결되기도 합니다.

또한 Self-Attention은 병렬화에 유리합니다. RNN은 순서대로 hidden state를 계산해야 해서 이전 step이 끝나야 다음 step을 계산하기 쉽습니다. 반면 Transformer의 self-attention은 한 layer 안에서 여러 token의 계산을 matrix multiplication으로 동시에 처리할 수 있습니다. 이 점이 대규모 GPU 학습에서 매우 중요했습니다.

### 헷갈리기 쉬운 포인트

1. **Self-Attention은 자기 자신만 본다는 뜻이 아닙니다.**  
   “self”는 같은 sequence 내부에서 attention을 한다는 뜻입니다. 각 token은 자기 자신뿐 아니라 같은 문장 안의 다른 token도 봅니다.

2. **Self-Attention만으로 순서를 자동으로 아는 것은 아닙니다.**  
   attention은 기본적으로 token들 사이의 관계를 계산하지만, 순서 정보는 positional encoding 또는 position embedding 같은 장치로 넣어 주어야 합니다.

3. **attention weight가 높다고 항상 인간이 생각하는 중요한 단어라는 뜻은 아닙니다.**  
   attention은 모델 내부 계산의 일부입니다. 해석에 도움이 될 수 있지만, 완전한 설명으로 받아들이면 위험합니다.

4. **Self-Attention output은 단어 하나의 고정 의미가 아닙니다.**  
   주변 문맥이 섞인 hidden state입니다. 같은 단어라도 문장이 다르면 output vector가 달라집니다.

5. **표현력이 좋다는 것이 항상 계산이 싸다는 뜻은 아닙니다.**  
   문장 길이가 길어지면 attention matrix가 `n × n`으로 커집니다. 긴 context에서는 메모리와 속도가 큰 문제가 됩니다.

---

## 복습 질문 3개

1. query, key, value를 도서관 검색에 비유하면 각각 무엇에 해당하나요?
2. Scaled Dot-Product Attention에서 dot product score를 `sqrt(d_k)`로 나누는 이유는 무엇인가요?
3. Self-Attention이 같은 단어의 의미를 문맥에 따라 다르게 표현할 수 있는 이유는 무엇인가요?

## 오늘의 한 줄 요약

Attention은 query로 필요한 정보를 찾고, key로 관련성을 계산하고, value를 attention weight만큼 섞어서 각 token의 문맥적 표현을 만드는 메커니즘이며, Self-Attention은 이 과정을 같은 sequence 내부에서 수행해 Transformer의 강한 표현력을 만듭니다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 21/30]

오늘은 Transformer attention의 핵심인 QKV, scaling, self-attention을 복습해 볼게요.

### 1. query, key, value를 도서관 검색에 비유하면 각각 무엇에 해당하나요?

**정답**

도서관 검색에 비유하면 다음과 같습니다.

- **query**: 내가 찾고 싶은 것, 즉 “어떤 책을 찾고 싶다”라는 검색 질문
- **key**: 각 책이 가진 제목, 태그, 분류번호, 주제어 같은 검색용 정보
- **value**: 검색 결과로 실제로 읽게 되는 책의 내용

즉 query와 key를 비교해서 어떤 책이 관련 있는지 판단하고, 관련성이 높은 책의 value를 더 많이 가져옵니다.

**설명**

attention에서 query, key, value는 각각 역할이 다릅니다.

query는 현재 위치가 “무엇을 찾고 있는지”를 나타냅니다. 예를 들어 문장 안에서 `먹었다`라는 단어는 “무엇을 먹었지?”라는 정보를 찾고 싶을 수 있습니다.

key는 각 token이 가진 “검색용 특징”입니다. `사과`라는 token의 key는 “나는 먹을 수 있는 대상일 수 있다” 같은 방향의 특징을 담을 수 있습니다. 물론 모델이 실제 문장으로 생각하는 것은 아니고, vector 공간에서 그런 관계가 학습됩니다.

value는 선택된 뒤 실제로 가져와서 섞는 정보입니다. attention의 최종 출력은 key가 아니라 value들의 weighted sum입니다. weighted sum은 각각의 값에 비율을 곱해서 더하는 방식입니다.

중요한 점은 key와 value가 같은 token에서 나오더라도 역할이 다르다는 것입니다. key는 “나를 찾을 때 쓰는 표지”이고, value는 “선택되었을 때 전달할 내용”입니다.

**예시**

사진 앱에서 검색한다고 생각해 봅시다.

내가 검색창에 이렇게 입력합니다.

`강아지 사진 찾아줘`

이때:

- query: “강아지 사진 찾아줘”
- key: 각 사진에 붙은 태그, 이미지 특징, 분류 정보
- value: 실제 사진 데이터

검색은 key를 보고 합니다. 하지만 내가 최종적으로 보는 것은 key 자체가 아니라 실제 사진, 즉 value입니다.

아주 작은 숫자로 보면 이렇게 볼 수 있습니다.

`먹었다`의 query가 2라고 해 봅시다.

- 사과: key 2, value 10
- 어제: key 0, value 3
- 친구와: key 1, value 5

query와 key를 곱하면:

- 사과: 2 × 2 = 4
- 어제: 2 × 0 = 0
- 친구와: 2 × 1 = 2

점수가 가장 큰 것은 `사과`입니다. 그래서 모델은 `사과`의 value를 가장 많이 가져옵니다.

**실전 연결**

QKV는 GPT, BERT, T5, Vision Transformer 같은 Transformer 모델의 기본 부품입니다. LLM이 다음 단어를 예측할 때, 현재 token의 query가 이전 token들의 key를 보고 어떤 정보를 참고할지 정합니다. 그런 다음 선택된 token들의 value를 섞어서 새 hidden state를 만듭니다. hidden state는 모델 내부에서 token을 표현하는 vector입니다. 그래서 QKV를 이해하면 “LLM이 문맥에서 필요한 정보를 어떻게 찾아오는가”를 이해하는 데 큰 도움이 됩니다.

### 2. Scaled Dot-Product Attention에서 dot product score를 `sqrt(d_k)`로 나누는 이유는 무엇인가요?

**정답**

dot product score를 `sqrt(d_k)`로 나누는 이유는 score가 너무 커지는 것을 막기 위해서입니다.

key/query vector의 차원 수인 `d_k`가 커지면 dot product 값도 커지기 쉽습니다. score가 너무 커지면 softmax 결과가 한쪽으로 지나치게 몰릴 수 있습니다. 그래서 `sqrt(d_k)`로 나누어 score 크기를 적당히 줄이고, attention weight가 너무 극단적이 되지 않게 만듭니다.

**설명**

Scaled Dot-Product Attention의 공식은 다음과 같습니다.

`Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V`

순서는 이렇게 이해하면 됩니다.

1. query와 key를 dot product해서 관련성 score를 구합니다.
2. 그 score를 `sqrt(d_k)`로 나눕니다.
3. softmax로 attention weight를 만듭니다.
4. attention weight만큼 value를 섞습니다.

여기서 dot product는 두 vector의 같은 위치 숫자를 곱해서 더하는 연산입니다. 예를 들어 `[1, 2]`와 `[3, 1]`의 dot product는 `1×3 + 2×1 = 5`입니다.

문제는 vector 차원이 커질수록 dot product 값도 커지기 쉽다는 점입니다. 차원이 2이면 숫자 2개를 곱해서 더하지만, 차원이 64이면 숫자 64개를 곱해서 더합니다. 그래서 별다른 조절이 없으면 score가 커질 가능성이 높습니다.

softmax는 여러 score를 받아서 합이 1인 비율로 바꾸는 함수입니다. attention에서는 이 비율을 attention weight라고 부릅니다. 그런데 softmax에 들어가는 숫자 차이가 너무 크면 결과가 거의 하나의 후보에만 몰립니다.

예를 들어 score가 `[1, 2]`이면 두 번째가 더 크지만 그래도 어느 정도 부드러운 차이입니다. 하지만 `[10, 20]`이면 softmax는 거의 두 번째만 선택하는 식으로 변합니다.

이렇게 되면 모델이 다양한 token에서 정보를 섞기 어렵고, 학습 초기에 gradient 흐름도 불안정해질 수 있습니다. gradient는 loss function을 줄이기 위해 모델 weight를 어떻게 바꾸면 좋을지 알려 주는 신호입니다. attention weight가 너무 한쪽으로 굳어지면 여러 후보에서 배우는 신호가 약해질 수 있습니다.

**예시**

두 후보 A, B가 있다고 해 봅시다.

처음 score가 다음과 같습니다.

- A score = 2
- B score = 4

softmax를 적용하면 B가 더 큰 attention weight를 받습니다. 대략 B를 더 많이 보지만, A도 조금은 참고합니다.

그런데 차원이 커져서 dot product score가 다음처럼 커졌다고 해 봅시다.

- A score = 20
- B score = 40

겉으로 보면 여전히 B가 A보다 2배 큰 것처럼 보입니다. 하지만 softmax 입장에서는 차이가 너무 큽니다. 그래서 B에 거의 모든 weight가 몰릴 수 있습니다.

이때 `d_k = 64`라면 `sqrt(d_k) = 8`입니다. score를 8로 나누면:

- A scaled score = 20 / 8 = 2.5
- B scaled score = 40 / 8 = 5

여전히 B가 더 중요하지만, softmax가 덜 극단적으로 반응하게 됩니다. 즉 scaling은 “중요한 차이는 남기되, 너무 과격하게 몰리지 않게 하는 장치”라고 볼 수 있습니다.

**실전 연결**

이 scaling은 Transformer 학습 안정성과 직접 연결됩니다. GPT 같은 LLM은 수많은 token 사이에서 attention score를 계산합니다. 만약 score가 너무 커져 softmax가 한 token에만 몰리면, 모델이 다양한 문맥 정보를 섞기 어려워집니다. 특히 큰 모델에서는 tensor shape와 차원이 커지기 때문에 이런 안정화 장치가 중요합니다. 실제 구현에서도 attention score를 구한 뒤 softmax 전에 `sqrt(d_k)`로 나누는 순서가 매우 중요합니다.

### 3. Self-Attention이 같은 단어의 의미를 문맥에 따라 다르게 표현할 수 있는 이유는 무엇인가요?

**정답**

Self-Attention은 각 token이 같은 문장 안의 다른 token들을 참고해서 자기 표현을 다시 만들기 때문에, 같은 단어라도 주변 문맥에 따라 다른 표현을 가질 수 있습니다.

즉 단어 하나만 따로 보는 것이 아니라, 관련 있는 주변 token들의 value를 attention weight만큼 섞어서 새 hidden state를 만듭니다. 그래서 같은 `은행`이라는 단어도 `돈`, `계좌`와 함께 있으면 금융기관에 가까운 표현이 되고, `강가`, `앉았다`와 함께 있으면 강둑에 가까운 표현이 될 수 있습니다.

**설명**

Self-Attention에서 “self”는 같은 sequence 안에서 attention을 한다는 뜻입니다. 자기 자신만 본다는 뜻이 아닙니다. 문장 안의 각 token이 자기 자신뿐 아니라 같은 문장 안의 다른 token들도 볼 수 있습니다.

예를 들어 다음 두 문장을 봅시다.

`나는 은행에서 돈을 찾았다.`  
`나는 강가의 은행에 앉았다.`

두 문장 모두 `은행`이라는 단어가 들어 있습니다. 하지만 의미는 다릅니다.

첫 번째 문장에서 `은행`은 `돈`, `찾았다`와 연결됩니다. 이 문맥에서는 bank, 즉 금융기관입니다.

두 번째 문장에서 `은행`은 `강가`, `앉았다`와 연결됩니다. 이 문맥에서는 river bank, 즉 강둑에 가까운 의미입니다.

Self-Attention은 이런 차이를 token interaction으로 처리합니다. token interaction은 token들 사이의 상호작용입니다. 각 token의 query가 다른 token들의 key와 비교되고, 그 결과로 attention weight가 만들어집니다. 그런 다음 value들이 섞여서 새 표현이 됩니다. 이 과정을 context mixing이라고 볼 수 있습니다. context mixing은 주변 문맥 정보가 섞여서 문맥적 표현이 되는 과정입니다.

그래서 Self-Attention의 출력은 단어의 고정된 의미가 아닙니다. layer를 지난 뒤의 hidden state는 주변 단어들이 반영된 contextual embedding이 됩니다. contextual embedding은 문맥에 따라 달라지는 embedding입니다.

**예시**

문장이 세 token이라고 해 봅시다.

`[나는, 사과를, 먹었다]`

`먹었다` token이 새 표현을 만들 때 attention weight가 다음과 같다고 해 봅시다.

- 나는: 0.2
- 사과를: 0.6
- 먹었다: 0.2

그리고 value를 아주 단순한 숫자로 표현하면:

- 나는 value = 1
- 사과를 value = 10
- 먹었다 value = 5

그러면 `먹었다`의 새 표현은 다음처럼 됩니다.

`0.2×1 + 0.6×10 + 0.2×5 = 7.2`

이 숫자 자체가 중요한 것은 아닙니다. 핵심은 `먹었다`의 표현이 자기 자신만으로 만들어진 것이 아니라 `나는`, `사과를`, `먹었다`의 정보가 섞여 만들어졌다는 점입니다.

특히 `사과를`의 weight가 0.6으로 크기 때문에, `먹었다`는 “무엇을 먹었는가”라는 문맥 정보를 많이 반영하게 됩니다.

비슷하게 `은행`이라는 단어도 주변에 `돈`이 있으면 그 정보를 많이 섞고, 주변에 `강가`가 있으면 그 정보를 많이 섞을 수 있습니다.

**실전 연결**

Self-Attention은 LLM이 문맥을 이해하는 핵심 원리입니다. GPT는 이전 token들을 self-attention으로 참고해서 다음 token을 예측합니다. BERT는 문장 양쪽의 문맥을 함께 보며 각 token의 의미를 만듭니다. 이 구조 덕분에 모델은 대명사 해석, 동음이의어 구분, 긴 거리 의존성 처리, 코드에서 변수 선언과 사용 위치 연결 같은 일을 더 잘할 수 있습니다. 또한 여러 layer를 쌓으면 단순한 단어 관계를 넘어서 문장 전체의 의미와 추론 단서까지 표현할 수 있습니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-13-day21.md
