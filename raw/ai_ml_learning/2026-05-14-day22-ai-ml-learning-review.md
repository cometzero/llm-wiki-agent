# AI/ML Learning Review - Day 22 (2026-05-14)
## Source Metadata
- Lesson source: /home/ubuntu/work/ai/learning/logs/2026-05-14-day22.md
- Follow-up answer source: /home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-14_09-26-04.md

---

## Lesson

# Day 22 - AI/ML 기초 학습

- Date: 2026-05-14
- Progress: 22/30
- Level: beginner-intermediate
- Milestone: Transformer 심화 기초
- Milestone goal: Transformer의 각 블록이 왜 필요한지 구조적으로 이해한다.

## Today's 3 concepts

1. Transformer 블록의 전체 흐름
2. 멀티헤드 어텐션의 의미
3. 포지셔널 인코딩

---

## 1. Transformer 블록의 전체 흐름

### 한 줄 직관

Transformer block은 각 token이 “주변 문맥을 보고, 자기 생각을 정리하고, 안정적으로 다음 layer로 넘기는” 작은 처리 공장입니다.

### 개념 정의

**Transformer block**은 Transformer 모델에서 반복해서 쌓이는 기본 단위입니다. GPT, BERT, T5 같은 모델은 대부분 “embedding을 만든 뒤 Transformer block을 여러 층 쌓고, 마지막에 예측한다”는 큰 흐름을 가집니다.

하나의 Transformer block은 보통 다음 부품들로 이루어집니다.

1. **attention sublayer**: token들이 서로를 보면서 필요한 문맥 정보를 가져오는 부분입니다.
2. **FFN(Feed-Forward Network)**: 각 token의 표현을 따로 더 깊게 가공하는 작은 신경망입니다.
3. **residual connection**: 원래 입력을 출력에 더해서 정보가 너무 쉽게 사라지지 않게 하는 연결입니다.
4. **LayerNorm**: vector 값의 크기와 분포를 안정적으로 맞춰 학습을 편하게 만드는 정규화(normalization)입니다.

Transformer block을 아주 단순하게 말하면 다음 순서입니다.

```text
입력 token 표현
→ attention으로 문맥 섞기
→ FFN으로 각 token 표현 가공하기
→ 다음 block으로 넘기기
```

여기서 token 표현은 보통 **hidden state**라고 부릅니다. hidden state는 모델 내부에서 token 하나를 나타내는 숫자 vector입니다. 처음에는 단어 embedding에 가까웠던 표현이, block을 지날수록 문맥과 의미가 섞인 표현으로 바뀝니다.

### 왜 이런 개념이 필요한가

문장 이해는 한 번의 계산으로 끝나기 어렵습니다. 예를 들어 다음 문장을 봅시다.

```text
철수가 민수에게 빌린 책을 어제 도서관에서 반납했다.
```

이 문장을 이해하려면 여러 관계를 봐야 합니다.

- `반납했다`는 무엇을 반납했는가? → `책`
- 책은 누구에게 빌렸는가? → `민수`
- 누가 반납했는가? → `철수`
- 언제, 어디서 반납했는가? → `어제`, `도서관`

attention은 이런 token 사이의 관계를 직접 볼 수 있게 해 줍니다. 하지만 attention만으로는 충분하지 않습니다. attention은 주로 “어떤 token의 정보를 얼마나 가져올까?”를 정하는 장치입니다. 가져온 정보를 바탕으로 각 token의 표현을 더 복잡하게 바꾸려면 FFN이 필요합니다.

예를 들어 `반납했다` token이 attention을 통해 `책`, `철수`, `도서관` 정보를 가져왔다고 합시다. 그 다음에는 “책을 반납했다”라는 의미, “도서관에서 한 행동”이라는 의미, “완료된 사건”이라는 의미를 내부 표현 안에서 더 정리해야 합니다. 이 가공을 FFN이 도와줍니다.

그리고 Transformer는 block을 아주 많이 쌓습니다. 작은 모델은 몇 개, 큰 LLM은 수십 개 이상의 block을 쌓습니다. 이때 각 block이 안정적으로 학습되지 않으면 gradient가 너무 커지거나 작아지고, 앞 layer의 정보가 사라질 수 있습니다. 그래서 residual connection과 LayerNorm이 함께 들어갑니다.

즉 Transformer block은 단순히 attention 하나가 아니라, “문맥 혼합 + 표현 가공 + 안정적 학습”을 한 묶음으로 만든 구조입니다.

### 아주 쉬운 예시

문장 세 token이 있다고 합시다.

```text
[나는, 사과를, 먹었다]
```

각 token의 hidden state를 아주 단순하게 숫자 하나로 표현해 보겠습니다.

```text
나는: 1
사과를: 10
먹었다: 5
```

`먹었다` token은 “무엇을 먹었는가?”를 이해하기 위해 `사과를`을 많이 봐야 합니다. attention 결과로 `먹었다`가 다음 비율로 정보를 가져왔다고 합시다.

```text
나는: 0.2
사과를: 0.6
먹었다: 0.2
```

그러면 attention output은 다음처럼 됩니다.

```text
0.2×1 + 0.6×10 + 0.2×5 = 0.2 + 6 + 1 = 7.2
```

이제 `먹었다`의 표현에는 `사과를` 정보가 많이 섞였습니다. 하지만 여기서 끝이 아닙니다. FFN은 이 `7.2` 같은 표현을 다시 가공합니다.

아주 단순한 FFN을 다음처럼 생각해 봅시다.

```text
FFN(x) = 2x + 1
```

그러면:

```text
FFN(7.2) = 2×7.2 + 1 = 15.4
```

실제 FFN은 이렇게 단순한 1차식이 아니라 여러 차원의 vector에 linear layer와 activation function을 적용합니다. 하지만 직관은 같습니다. attention이 “필요한 정보를 가져오기”라면, FFN은 “가져온 정보를 내 안에서 다시 해석하고 가공하기”입니다.

일상 비유로는 학생의 공부 과정과 비슷합니다.

1. 친구들에게 질문해서 필요한 정보를 듣습니다. → attention
2. 들은 정보를 자기 노트에 정리합니다. → FFN
3. 원래 알고 있던 내용도 잃지 않게 같이 남깁니다. → residual connection
4. 노트의 형식을 맞춰 다음 공부가 편하게 합니다. → LayerNorm

### 개념 구조와 핵심 포인트

Transformer block의 대표적인 구조는 크게 두 가지 방식으로 설명됩니다. 실제 모델마다 LayerNorm 위치가 조금 다를 수 있지만, 핵심 흐름은 비슷합니다.

#### 1. Attention sublayer

입력 hidden state를 `X`라고 합시다. 문장 길이가 4이고 hidden dimension이 8이면 shape는 다음처럼 볼 수 있습니다.

```text
X shape: 4 × 8
```

각 행은 token 하나의 hidden state입니다. attention sublayer는 각 token이 다른 token들을 얼마나 볼지 계산하고, value들을 섞어서 새 문맥 표현을 만듭니다.

```text
Attention output shape: 4 × 8
```

입력도 token 4개, 출력도 token 4개입니다. 단, 각 token의 내용은 문맥이 섞인 표현으로 바뀝니다.

#### 2. Residual connection

attention output만 쓰면 원래 입력 정보가 일부 사라질 수 있습니다. 그래서 보통 원래 `X`를 더합니다.

```text
X_after_attention = X + Attention(X)
```

이렇게 하면 block이 “새 정보”를 추가하면서도 “원래 정보”를 유지하기 쉽습니다. gradient도 더 잘 흐릅니다.

#### 3. LayerNorm

LayerNorm은 각 token vector의 값들이 너무 크거나 작아지지 않도록 정리합니다. 여기서 중요한 것은 어렵게 외우는 것이 아니라, “layer를 많이 쌓아도 학습이 안정되도록 숫자의 스케일을 맞춘다”는 점입니다.

#### 4. FFN

FFN은 각 token에 독립적으로 적용됩니다. attention은 token들 사이를 섞지만, FFN은 각 token의 hidden state를 더 풍부하게 변환합니다.

보통 FFN은 다음처럼 생겼습니다.

```text
FFN(x) = Linear → activation → Linear
```

예를 들어 hidden dimension이 8이면 내부에서 잠깐 32차원으로 넓혔다가 다시 8차원으로 줄일 수 있습니다.

```text
8차원 → 32차원 → 8차원
```

이렇게 넓혔다 줄이는 과정은 모델이 더 다양한 feature 조합을 만들 수 있게 해 줍니다.

#### 5. 여러 block을 쌓는 이유

한 block은 한 번의 문맥 혼합과 표현 가공을 합니다. 여러 block을 쌓으면 다음처럼 점점 더 복잡한 정보를 만들 수 있습니다.

```text
초기 embedding: token 자체의 기본 의미
1~2번째 block: 가까운 단어 관계, 간단한 문법 관계
중간 block: 문장 구조, 의미 관계, 지시 대상
깊은 block: 다음 token 예측이나 분류에 필요한 고수준 단서
```

물론 실제 모델 내부가 항상 이렇게 깔끔하게 나뉘는 것은 아닙니다. 하지만 여러 block을 쌓으면 단순한 단어 의미에서 복잡한 문맥 표현으로 점진적으로 바뀐다는 관점은 매우 중요합니다.

### 핵심 수학 포인트

Transformer block 전체를 간단한 식으로 쓰면 다음처럼 볼 수 있습니다. 모델마다 순서는 조금 다르지만, 직관용으로 충분합니다.

```text
H1 = X + Attention(X)
H2 = H1 + FFN(H1)
```

여기에 LayerNorm이 앞이나 뒤에 들어갑니다.

```text
H1 = X + Attention(LayerNorm(X))        # pre-norm 방식 예시
H2 = H1 + FFN(LayerNorm(H1))
```

여기서 중요한 수학 포인트는 세 가지입니다.

1. **입력과 출력 shape가 유지됩니다.**

   문장 길이가 `n`, hidden dimension이 `d`라면:

   ```text
   X shape: n × d
   block output shape: n × d
   ```

   shape가 유지되기 때문에 같은 block 구조를 여러 번 반복해서 쌓을 수 있습니다.

2. **attention은 token 방향으로 정보를 섞습니다.**

   예를 들어 문장 길이 3이면 attention weight는 3×3이 될 수 있습니다.

   ```text
   각 행: 한 token이 다른 token들을 얼마나 보는지
   각 열: 참고 대상 token
   ```

   즉 attention은 token 간 관계를 다룹니다.

3. **FFN은 feature 방향으로 정보를 가공합니다.**

   FFN은 각 token별로 같은 작은 신경망을 적용합니다. token끼리 직접 섞는 역할은 attention이 하고, FFN은 한 token의 vector 안에 들어 있는 feature들을 비선형적으로 조합합니다.

아주 작은 숫자로 보면 다음과 같습니다.

```text
x = [1, 2]
Attention(x)가 만든 새 정보 = [0.5, 1.0]
Residual 후 = [1, 2] + [0.5, 1.0] = [1.5, 3.0]
```

원래 정보 `[1, 2]`가 완전히 사라지지 않고 새 정보가 더해졌습니다. 이것이 residual connection의 핵심입니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **transformer block**: Transformer에서 반복해서 쌓는 기본 처리 단위입니다. attention, FFN, residual connection, LayerNorm을 포함합니다.
- **attention sublayer**: token들이 서로를 참고해 문맥 정보를 섞는 부분입니다.
- **FFN(Feed-Forward Network)**: 각 token의 hidden state를 독립적으로 가공하는 작은 신경망입니다.
- **hidden state**: 모델 내부에서 token을 나타내는 vector 표현입니다. layer를 지날수록 문맥 정보가 더 많이 섞입니다.
- **residual connection**: 입력을 출력에 더해 원래 정보를 보존하고 gradient 흐름을 돕는 연결입니다.
- **LayerNorm**: 각 token vector의 숫자 스케일을 안정적으로 맞추는 normalization 기법입니다.
- **sublayer**: block 안의 작은 구성요소입니다. attention sublayer와 FFN sublayer처럼 부릅니다.

### AI에서 어디에 쓰이는가

Transformer block은 현대 LLM의 기본 단위입니다. GPT 계열 모델은 causal self-attention이 들어간 Transformer block을 여러 층 쌓고, 다음 token을 예측합니다. BERT는 양방향 self-attention이 들어간 block을 쌓고, 문장 이해나 token 분류에 사용합니다. Vision Transformer는 이미지 patch를 token처럼 보고 Transformer block을 적용합니다.

실전에서 이 구조를 이해하면 다음을 더 잘 볼 수 있습니다.

1. **모델 크기의 의미**  
   “24-layer Transformer”라고 하면 Transformer block이 24개 쌓였다는 뜻입니다. layer가 많을수록 더 깊은 표현을 만들 수 있지만, 계산량과 메모리도 커집니다.

2. **hidden state 분석**  
   모델 내부를 분석할 때 “몇 번째 layer의 hidden state를 볼 것인가?”라는 질문이 자주 나옵니다. block을 지날수록 표현이 달라지기 때문입니다.

3. **fine-tuning과 LoRA 이해**  
   LoRA 같은 parameter-efficient fine-tuning은 Transformer block 안의 attention이나 FFN의 일부 weight에 작은 학습 가능한 변화를 추가합니다. 그래서 block 구조를 알아야 fine-tuning이 어디를 바꾸는지 이해할 수 있습니다.

4. **성능 병목 이해**  
   긴 sequence에서는 attention 계산이 무겁고, 큰 hidden dimension에서는 FFN 계산도 큽니다. LLM 추론 속도를 이해하려면 attention과 FFN이 각각 어떤 비용을 만드는지 알아야 합니다.

### 헷갈리기 쉬운 포인트

1. **Transformer block은 attention 하나만 뜻하지 않습니다.**  
   attention은 핵심 부품이지만, FFN, residual connection, LayerNorm까지 함께 있어야 실제 block이 됩니다.

2. **FFN은 token 사이를 섞는 부분이 아닙니다.**  
   token 사이의 정보 교환은 attention이 담당합니다. FFN은 각 token의 vector를 따로 가공합니다.

3. **Residual connection은 단순한 장식이 아닙니다.**  
   깊은 모델에서 정보와 gradient가 안정적으로 흐르게 해 주는 매우 중요한 구조입니다.

4. **LayerNorm은 모델을 더 똑똑하게 만드는 지식 그 자체가 아닙니다.**  
   주된 역할은 학습 안정화입니다. 숫자 분포가 안정되어야 optimizer가 weight를 더 잘 업데이트할 수 있습니다.

5. **block을 많이 쌓는다고 무조건 좋은 것은 아닙니다.**  
   데이터, 모델 크기, optimizer, 학습 안정성, 계산 자원이 함께 맞아야 합니다. 구조만 깊게 만들면 overfitting이나 학습 불안정이 생길 수 있습니다.

---

## 2. 멀티헤드 어텐션의 의미

### 한 줄 직관

Multi-head attention은 한 사람이 한 가지 기준으로만 문장을 보는 대신, 여러 명의 독자가 동시에 다른 관점으로 문장을 읽게 하는 방식입니다.

### 개념 정의

**Multi-head attention**은 attention을 한 번만 계산하지 않고, 여러 개의 **head**로 나누어 병렬로 계산하는 구조입니다. 각 head는 같은 입력을 보지만, 서로 다른 projection matrix를 사용해서 query, key, value를 만듭니다. 그래서 서로 다른 관점의 관계를 학습할 수 있습니다.

예를 들어 문장을 읽을 때 사람도 여러 관점을 씁니다.

```text
민수가 철수에게 어제 빌린 책을 돌려주었다.
```

이 문장에서 볼 수 있는 관점은 여러 가지입니다.

- 누가 행동했는가? → `민수`
- 누구에게 했는가? → `철수에게`
- 무엇을 돌려주었는가? → `책`
- 언제 했는가? → `어제`

single-head attention이 하나의 관점으로 attention을 계산한다면, multi-head attention은 여러 관점을 동시에 계산할 수 있게 합니다.

여기서 중요한 용어가 **subspace projection**입니다. projection은 원래 vector를 다른 공간으로 변환하는 것입니다. subspace는 전체 hidden dimension 중 일부 관점이 강조된 작은 표현 공간이라고 생각하면 됩니다. 각 head는 입력 hidden state를 자기만의 Q, K, V 공간으로 projection합니다.

### 왜 이런 개념이 필요한가

언어와 이미지는 한 가지 관계만으로 설명되지 않습니다. 한 문장 안에서도 문법 관계, 의미 관계, 위치 관계, 지시 관계가 동시에 존재합니다.

예를 들어 다음 문장을 봅시다.

```text
영희는 민수에게 꽃을 주었고, 그는 웃었다.
```

`그는`이 누구를 가리키는지 이해하려면 앞 문맥을 봐야 합니다. 동시에 `주었고`의 주어는 `영희`, 받는 사람은 `민수`, 대상은 `꽃`입니다. 한 attention head가 모든 관계를 완벽히 담당하기는 어렵습니다.

Multi-head attention은 이런 문제를 구조적으로 돕습니다.

- 한 head는 주어-동사 관계를 볼 수 있습니다.
- 다른 head는 목적어-동사 관계를 볼 수 있습니다.
- 또 다른 head는 대명사와 지시 대상을 볼 수 있습니다.
- 또 다른 head는 가까운 token 중심의 지역 관계를 볼 수 있습니다.

물론 실제 학습된 head가 항상 사람이 보기 좋은 이름표대로 움직이는 것은 아닙니다. 하지만 여러 head를 병렬로 둠으로써 모델은 다양한 종류의 token interaction을 동시에 표현할 여지를 얻습니다.

또한 하나의 큰 attention을 쓰는 것보다, 여러 작은 head로 나누면 각 head가 낮은 차원의 subspace에서 더 특화된 패턴을 잡을 수 있습니다. 이것은 마치 사진 한 장을 볼 때 “색”, “모양”, “위치”, “질감”을 따로 보는 것과 비슷합니다.

### 아주 쉬운 예시

아주 작은 숫자 예시로 보겠습니다.

문장이 세 token이라고 합시다.

```text
[고양이가, 생선을, 먹었다]
```

`먹었다` token이 다른 token들을 볼 때, 두 개의 head가 있다고 해 봅시다.

#### Head 1: “무엇을 먹었는가?” 관점

```text
고양이가: 0.1
생선을:   0.8
먹었다:   0.1
```

Head 1은 `먹었다`와 가장 강하게 연결되는 목적어 `생선을`을 많이 봅니다.

#### Head 2: “누가 먹었는가?” 관점

```text
고양이가: 0.7
생선을:   0.1
먹었다:   0.2
```

Head 2는 주어 `고양이가`를 많이 봅니다.

두 head의 value output을 숫자 하나로 단순화해 봅시다.

```text
Head 1 output = 10   # 먹힌 대상 정보가 강함
Head 2 output = 3    # 행위자 정보가 강함
```

Multi-head attention은 이 결과들을 이어 붙이거나(concat) 합쳐서 다시 하나의 hidden state로 만듭니다.

```text
concat 결과: [10, 3]
```

실제 모델에서는 head output이 vector이고, 여러 head의 vector를 concatenate한 뒤 다시 linear layer로 섞습니다.

일상 비유로는 회의에서 여러 전문가가 같은 문서를 읽는 것과 같습니다.

- 문법 전문가는 문장 구조를 봅니다.
- 의미 전문가는 단어 뜻의 연결을 봅니다.
- 사실 확인 전문가는 중요한 명사와 수치를 봅니다.
- 요약 전문가는 전체 흐름을 봅니다.

마지막에는 각 전문가의 의견을 모아 하나의 결론을 만듭니다. 이것이 multi-head attention의 직관입니다.

### 개념 구조와 핵심 포인트

Multi-head attention의 흐름은 다음과 같습니다.

1. 입력 hidden state `X`가 있습니다.
2. 각 head마다 서로 다른 `W_Q`, `W_K`, `W_V`를 사용합니다.
3. 각 head가 자기만의 Q, K, V를 만듭니다.
4. 각 head가 scaled dot-product attention을 계산합니다.
5. head output들을 concatenate합니다.
6. 마지막 linear projection으로 다시 hidden dimension에 맞춥니다.

shape로 보면 더 분명합니다. 예를 들어:

```text
문장 길이 n = 4
hidden dimension d_model = 8
head 개수 h = 2
각 head dimension d_head = 4
```

입력은 다음 shape입니다.

```text
X shape: 4 × 8
```

두 head로 나누면 각 head는 대략 4차원 공간에서 attention을 계산합니다.

```text
Head 1 Q/K/V shape: 4 × 4
Head 2 Q/K/V shape: 4 × 4
```

각 head output도 `4 × 4`입니다. 두 head 결과를 concatenate하면 다시 `4 × 8`이 됩니다.

```text
Head 1 output: 4 × 4
Head 2 output: 4 × 4
concat:        4 × 8
final output:  4 × 8
```

중요한 핵심 포인트는 다음입니다.

1. **head마다 다른 projection을 배웁니다.**  
   같은 입력을 보더라도 head마다 Q, K, V를 만드는 weight가 다르기 때문에 다른 관계를 볼 수 있습니다.

2. **parallel heads는 동시에 계산됩니다.**  
   head들이 순서대로 하나씩 생각하는 것이 아니라 GPU에서 병렬로 계산되도록 구현됩니다.

3. **head는 작은 attention 모델처럼 볼 수 있습니다.**  
   각 head는 자기 subspace에서 query-key-value attention을 수행합니다.

4. **마지막에 head 정보를 합칩니다.**  
   여러 관점의 결과를 concatenate한 뒤 linear layer가 다시 섞습니다. 그래서 최종 output은 한 token당 하나의 hidden state로 돌아옵니다.

5. **head 수와 head dimension은 모델 설계의 중요한 선택입니다.**  
   `d_model = h × d_head`가 되도록 설계하는 경우가 많습니다. 예를 들어 `d_model=768`, `h=12`이면 head 하나는 보통 `64`차원을 가집니다.

### 핵심 수학 포인트

Multi-head attention의 수식은 다음처럼 쓸 수 있습니다.

```text
head_i = Attention(XW_Q_i, XW_K_i, XW_V_i)
MultiHead(X) = Concat(head_1, ..., head_h) W_O
```

처음 보면 기호가 많지만, 하나씩 풀면 단순합니다.

- `X`: 입력 hidden state입니다.
- `W_Q_i`, `W_K_i`, `W_V_i`: i번째 head가 사용하는 projection weight입니다.
- `head_i`: i번째 head가 계산한 attention output입니다.
- `Concat`: 여러 head output을 옆으로 이어 붙이는 연산입니다.
- `W_O`: 이어 붙인 결과를 다시 섞는 output projection weight입니다.

아주 작은 숫자 예시를 봅시다.

입력 vector가 4차원이라고 합시다.

```text
x = [1, 2, 3, 4]
```

두 head가 각각 2차원 subspace를 본다고 아주 단순하게 생각해 보겠습니다.

```text
Head 1 projection: [1, 2]   # 앞쪽 특징을 강조
Head 2 projection: [3, 4]   # 뒤쪽 특징을 강조
```

실제 projection은 이렇게 단순히 자르는 것이 아니라 matrix multiplication으로 학습됩니다. 하지만 직관적으로 각 head가 원래 vector의 다른 방향, 다른 feature 조합을 볼 수 있다는 점이 중요합니다.

각 head가 attention을 계산한 뒤 다음 output을 만들었다고 합시다.

```text
head_1 = [0.5, 1.0]
head_2 = [2.0, 0.3]
```

concatenate하면:

```text
concat = [0.5, 1.0, 2.0, 0.3]
```

그 다음 `W_O`라는 linear layer가 이 값들을 다시 섞어 최종 hidden state를 만듭니다.

수학적으로 중요한 점은 “여러 attention matrix가 생긴다”는 것입니다. head가 8개면 attention pattern도 8개입니다. 문장 길이가 5라면 각 head마다 5×5 attention weight matrix가 생길 수 있습니다.

```text
head 1 attention weights: 5 × 5
head 2 attention weights: 5 × 5
...
head 8 attention weights: 5 × 5
```

그래서 multi-head attention은 단일 attention보다 다양한 관계 패턴을 동시에 표현할 수 있습니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **multi-head attention**: 여러 attention head를 병렬로 계산하고 결과를 합치는 Transformer의 핵심 구조입니다.
- **head**: attention을 계산하는 하나의 작은 단위입니다. 각 head는 자기 Q, K, V projection을 가집니다.
- **subspace projection**: 원래 hidden state를 특정 head가 볼 작은 표현 공간으로 변환하는 것입니다.
- **parallel heads**: 여러 head가 동시에 attention을 계산하는 구조입니다.
- **concat / concatenate**: 여러 vector를 옆으로 이어 붙이는 연산입니다.
- **output projection**: 여러 head 결과를 합친 뒤 다시 hidden dimension에 맞게 섞는 linear layer입니다.
- **d_model**: Transformer의 hidden dimension입니다.
- **d_head**: head 하나가 사용하는 차원 수입니다.

### AI에서 어디에 쓰이는가

Multi-head attention은 대부분의 Transformer 기반 모델에 들어갑니다. GPT에서는 다음 token을 예측할 때 여러 head가 이전 token들의 서로 다른 관계를 봅니다. BERT에서는 문장 전체의 양방향 관계를 여러 head가 동시에 봅니다. Vision Transformer에서는 이미지 patch들 사이의 관계를 여러 관점으로 봅니다.

실전적으로 중요한 이유는 다음과 같습니다.

1. **문맥 관계를 다양하게 잡습니다.**  
   한 head만 있으면 하나의 attention pattern에 의존하기 쉽습니다. 여러 head가 있으면 문법, 의미, 위치, 지시 관계 등 다양한 패턴을 담을 가능성이 커집니다.

2. **해석 가능성 분석의 단서가 됩니다.**  
   연구나 디버깅에서 특정 head의 attention map을 시각화하기도 합니다. 예를 들어 어떤 head가 이전 줄의 변수 선언을 보는지, 어떤 head가 문장 끝 punctuation을 보는지 관찰할 수 있습니다. 다만 attention map만으로 모델의 모든 reasoning을 설명할 수는 없습니다.

3. **모델 효율과 품질의 trade-off와 연결됩니다.**  
   head 수를 늘리면 표현력은 좋아질 수 있지만 계산량과 메모리도 늘 수 있습니다. 반대로 너무 적으면 다양한 관계를 잡기 어려울 수 있습니다.

4. **LLM 구현에서 tensor shape 이해가 중요합니다.**  
   실제 구현에서는 보통 tensor shape가 다음처럼 바뀝니다.

   ```text
   batch × sequence × d_model
   → batch × heads × sequence × d_head
   ```

   이 reshape와 transpose를 정확히 이해해야 attention 구현을 따라갈 수 있습니다.

5. **fine-tuning과 pruning에서 자주 등장합니다.**  
   어떤 연구는 중요하지 않은 attention head를 줄이는 pruning을 시도합니다. 또 어떤 fine-tuning 방법은 attention projection weight에 작은 adapter나 LoRA를 붙입니다.

### 헷갈리기 쉬운 포인트

1. **head가 사람이 정한 역할을 미리 갖는 것은 아닙니다.**  
   “이 head는 주어 담당, 저 head는 목적어 담당”처럼 사람이 직접 지정하지 않습니다. 학습 과정에서 각 head의 weight가 조정됩니다.

2. **multi-head attention은 여러 모델을 따로 돌리는 것이 아닙니다.**  
   하나의 layer 안에서 여러 head를 병렬로 계산하는 구조입니다.

3. **head 수가 많을수록 무조건 좋은 것은 아닙니다.**  
   전체 hidden dimension이 고정되어 있으면 head 수가 늘 때 head 하나의 dimension은 작아질 수 있습니다. 너무 작은 head는 충분한 정보를 담기 어려울 수 있습니다.

4. **subspace projection은 단순히 vector를 자르는 것보다 일반적입니다.**  
   실제로는 학습 가능한 matrix multiplication입니다. 모델이 어떤 feature 조합을 볼지 스스로 학습합니다.

5. **attention head의 시각화는 도움이 되지만 완전한 설명은 아닙니다.**  
   attention weight가 높다고 해서 그 token이 최종 예측의 유일한 원인이라는 뜻은 아닙니다. FFN, residual connection, 여러 layer의 상호작용도 함께 영향을 줍니다.

---

## 3. 포지셔널 인코딩

### 한 줄 직관

Positional encoding은 Transformer에게 “이 token이 문장 안에서 몇 번째에 있는지” 알려 주는 위치 표식입니다.

### 개념 정의

Transformer의 self-attention은 기본적으로 token들 사이의 관련성을 계산합니다. 그런데 attention만 보면 token들의 순서를 자연스럽게 알기 어렵습니다. 입력 token들이 동시에 들어오고, attention은 모든 token 쌍을 비교하기 때문입니다.

그래서 Transformer에는 **positional encoding** 또는 position embedding이 필요합니다. 이것은 각 token embedding에 위치 정보를 더하거나 결합해서, 모델이 token의 순서를 구분할 수 있게 하는 방법입니다.

예를 들어 다음 두 문장은 같은 단어를 쓰지만 의미가 다릅니다.

```text
개가 사람을 물었다.
사람이 개를 물었다.
```

단어 종류만 보면 `개`, `사람`, `물었다`가 모두 등장합니다. 하지만 순서가 바뀌면 의미가 완전히 달라집니다. Transformer가 이런 차이를 이해하려면 “누가 앞에 있고, 누가 뒤에 있는지”를 알아야 합니다.

대표적인 방법 중 하나가 **sinusoidal encoding**입니다. 이는 sine과 cosine 함수를 이용해 위치마다 다른 vector를 만드는 방식입니다. 원래 Transformer 논문에서 사용된 방식입니다.

### 왜 이런 개념이 필요한가

RNN은 token을 순서대로 처리합니다. 첫 번째 token을 보고, 그 다음 두 번째 token을 보고, 그 다음 세 번째 token을 봅니다. 그래서 구조 자체에 순서가 들어 있습니다.

하지만 Transformer는 병렬 계산을 위해 token들을 한꺼번에 처리합니다. 이 점은 GPU 학습에 매우 유리하지만, 순서를 따로 알려 주지 않으면 문제가 생깁니다.

아주 단순하게 말하면, positional encoding이 없으면 Transformer는 다음 두 입력을 비슷하게 볼 위험이 있습니다.

```text
[나는, 밥을, 먹었다]
[밥을, 나는, 먹었다]
```

물론 실제로는 token embedding과 attention 계산 때문에 완전히 같게만 처리된다고 단순화할 수는 없지만, 핵심은 self-attention만으로는 “몇 번째 token인가”라는 정보를 명시적으로 제공하지 않는다는 점입니다.

AI에서 순서는 매우 중요합니다.

- 자연어에서는 주어, 목적어, 동사의 위치가 의미를 바꿉니다.
- 코드에서는 괄호와 들여쓰기, 변수 선언 위치가 중요합니다.
- 음성에서는 frame의 시간 순서가 중요합니다.
- 이미지에서도 patch의 위치가 중요합니다. 같은 patch라도 왼쪽 위에 있는지 오른쪽 아래에 있는지에 따라 의미가 달라집니다.

따라서 positional encoding은 “attention이 무엇을 볼지”와 별개로 “각 정보가 어디에 있었는지”를 알려 주는 필수 장치입니다.

### 아주 쉬운 예시

token embedding을 숫자 하나로 아주 단순화해 보겠습니다.

```text
나는 embedding = 5
밥을 embedding = 8
먹었다 embedding = 3
```

위치 정보도 숫자 하나로 단순화해 보겠습니다.

```text
1번째 위치 encoding = 0.1
2번째 위치 encoding = 0.2
3번째 위치 encoding = 0.3
```

그러면 입력 표현은 token embedding에 position information을 더해서 만들 수 있습니다.

```text
나는:   5 + 0.1 = 5.1
밥을:   8 + 0.2 = 8.2
먹었다: 3 + 0.3 = 3.3
```

이제 같은 `밥을`이라는 token이라도 위치가 바뀌면 입력 표현이 달라집니다.

```text
밥을이 1번째면: 8 + 0.1 = 8.1
밥을이 2번째면: 8 + 0.2 = 8.2
```

실제 모델에서는 embedding이 숫자 하나가 아니라 수백~수천 차원의 vector입니다. position encoding도 같은 차원의 vector입니다.

```text
token embedding shape: d_model
positional encoding shape: d_model
입력 hidden state = token embedding + positional encoding
```

예를 들어 `d_model = 4`라면:

```text
사과 token embedding       = [0.2, 0.7, 0.1, 0.5]
2번째 위치 encoding       = [0.0, 0.1, 0.3, 0.2]
최종 입력 representation  = [0.2, 0.8, 0.4, 0.7]
```

이렇게 하면 모델은 “사과라는 단어의 의미”와 “2번째 위치에 있다는 정보”를 함께 받습니다.

일상 비유로는 택배 상자에 붙은 주소 라벨과 비슷합니다. 상자 내용물이 token embedding이라면, 주소 라벨은 positional encoding입니다. 같은 물건이라도 어디로 가야 하는지 라벨이 없으면 제대로 처리하기 어렵습니다.

### 개념 구조와 핵심 포인트

Positional encoding의 핵심은 각 위치마다 고유한 vector를 준비해서 token embedding과 결합하는 것입니다.

가장 기본 흐름은 다음과 같습니다.

```text
token id
→ token embedding
→ positional encoding 더하기
→ Transformer block 입력
```

#### 1. Absolute position information

가장 단순한 방식은 각 위치에 번호를 붙이는 것입니다.

```text
0번째 token, 1번째 token, 2번째 token, ...
```

각 위치 번호에 해당하는 vector를 만들어 token embedding에 더합니다. 이것을 absolute position 방식이라고 볼 수 있습니다. “이 token은 전체 sequence에서 몇 번째인가?”를 알려 줍니다.

#### 2. Sinusoidal encoding

원래 Transformer 논문에서는 sine과 cosine 함수를 사용했습니다. 위치마다 서로 다른 파형 값을 만들고, 차원마다 다른 주기를 사용합니다.

직관적으로는 여러 개의 시계를 동시에 보는 것과 비슷합니다.

- 어떤 시계는 빠르게 반복됩니다.
- 어떤 시계는 천천히 반복됩니다.
- 여러 시계 값을 함께 보면 위치를 구분하기 쉬워집니다.

예를 들어 위치가 1, 2, 3으로 바뀔 때 각 차원의 값이 조금씩 다르게 변합니다. 모델은 이 패턴을 이용해 위치와 거리 정보를 배울 수 있습니다.

#### 3. Learned position embedding

많은 실제 모델은 위치 embedding을 학습 가능한 parameter로 둡니다. 즉 “1번째 위치 vector”, “2번째 위치 vector”를 모델이 학습 중에 직접 조정합니다.

```text
position 0 embedding: 학습됨
position 1 embedding: 학습됨
position 2 embedding: 학습됨
```

GPT 계열의 여러 모델은 learned position embedding 또는 더 발전된 위치 방식들을 사용합니다.

#### 4. Relative position과 RoPE 계열

최근 LLM에서는 단순히 “몇 번째인가”보다 “두 token 사이의 상대적 거리”가 중요하다는 관점도 많이 씁니다. 예를 들어 `현재 token에서 3칸 앞` 같은 정보입니다. RoPE(Rotary Positional Embedding)는 이런 상대적 위치 정보를 attention 계산에 잘 반영하기 위해 널리 쓰이는 방식입니다.

오늘의 핵심은 세부 방식보다 다음 한 문장입니다.

> Transformer는 순서를 자동으로 아는 구조가 아니므로, position information을 별도로 넣어 주어야 한다.

### 핵심 수학 포인트

가장 기본적인 positional encoding 결합은 덧셈입니다.

```text
input_i = token_embedding_i + positional_encoding_i
```

여기서 `i`는 token의 위치입니다.

예를 들어 3개 token, hidden dimension 2라고 합시다.

```text
Token embeddings:
나는   [1.0, 0.0]
밥을   [0.0, 1.0]
먹었다 [1.0, 1.0]

Position encodings:
pos 0 [0.1, 0.0]
pos 1 [0.0, 0.1]
pos 2 [0.1, 0.1]
```

더하면:

```text
나는(pos 0)   [1.0, 0.0] + [0.1, 0.0] = [1.1, 0.0]
밥을(pos 1)   [0.0, 1.0] + [0.0, 0.1] = [0.0, 1.1]
먹었다(pos 2) [1.0, 1.0] + [0.1, 0.1] = [1.1, 1.1]
```

중요한 점은 token embedding과 positional encoding의 차원이 같아야 더할 수 있다는 것입니다.

```text
token embedding shape: n × d_model
position encoding shape: n × d_model
더한 결과 shape: n × d_model
```

Sinusoidal encoding은 보통 다음 성질을 갖습니다.

- 위치마다 다른 vector가 생깁니다.
- 가까운 위치는 어느 정도 비슷한 패턴을 가질 수 있습니다.
- 먼 위치는 다른 패턴을 가집니다.
- 학습하지 않아도 긴 위치에 대해 계산할 수 있습니다.

정확한 sine/cosine 공식 자체를 지금 외우는 것보다, “위치를 숫자 vector로 바꿔 embedding에 더한다”는 구조를 먼저 이해하는 것이 중요합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **positional encoding**: token의 위치 정보를 vector로 만들어 Transformer 입력에 넣는 방법입니다.
- **position information**: token이 sequence 안에서 어디에 있는지에 대한 정보입니다.
- **sinusoidal encoding**: sine과 cosine 함수를 사용해 위치 vector를 만드는 방식입니다.
- **position embedding**: 위치마다 embedding vector를 두는 방식입니다. learned position embedding은 이 vector들을 학습합니다.
- **absolute position**: sequence 안에서 몇 번째 위치인지 나타내는 정보입니다.
- **relative position**: 두 token 사이의 거리나 상대적 위치를 나타내는 정보입니다.
- **RoPE(Rotary Positional Embedding)**: attention 계산에 회전 방식으로 위치 정보를 넣는 대표적인 현대적 방법입니다.

### AI에서 어디에 쓰이는가

Positional encoding은 Transformer가 순서 있는 데이터를 다룰 때 거의 항상 필요합니다.

1. **LLM의 문장 생성**  
   GPT 같은 모델은 이전 token들을 보고 다음 token을 예측합니다. 이때 token의 순서를 모르면 `나는 밥을 먹었다`와 `밥을 나는 먹었다`를 제대로 구분하기 어렵습니다.

2. **문서 이해와 긴 context**  
   긴 문서에서는 앞에서 나온 정보와 뒤에서 나온 정보의 위치가 중요합니다. “위에서 언급한 회사”, “다음 절에서 설명할 방법” 같은 표현은 위치와 순서에 의존합니다.

3. **코드 모델**  
   코드에서는 줄의 순서, 괄호 위치, 변수 선언과 사용 위치가 매우 중요합니다. positional information이 약하면 코드 구조를 이해하기 어렵습니다.

4. **Vision Transformer**  
   이미지를 patch로 나누면 patch들도 token처럼 처리됩니다. 하지만 patch의 위치를 알려 주지 않으면, 하늘 patch가 위에 있는지 아래에 있는지 모델이 알기 어렵습니다. 그래서 이미지 모델도 position embedding을 사용합니다.

5. **음성, 시계열, 로봇 데이터**  
   시간 순서가 중요한 데이터에서는 위치 정보가 곧 시간 정보가 됩니다. 어떤 신호가 먼저 왔고 나중에 왔는지가 예측에 큰 영향을 줍니다.

실전 LLM에서는 context length와 positional encoding 방식이 깊게 연결됩니다. 예를 들어 어떤 모델이 4,096 token까지 학습되었다면, 그보다 훨씬 긴 context를 넣을 때 position 처리 방식이 성능에 큰 영향을 줄 수 있습니다. 그래서 RoPE scaling, ALiBi, relative position 같은 기술들이 긴 context 모델에서 중요하게 다뤄집니다.

### 헷갈리기 쉬운 포인트

1. **Self-Attention은 순서를 자동으로 완벽히 알지 못합니다.**  
   attention은 token들 사이의 관련성을 계산하지만, 순서 정보는 positional encoding 같은 방식으로 넣어 주어야 합니다.

2. **Positional encoding은 단어 뜻 자체가 아닙니다.**  
   token embedding이 단어 의미를 담는다면, positional encoding은 위치 정보를 담습니다. 둘을 더해서 의미와 위치를 함께 제공합니다.

3. **위치 번호를 그냥 1, 2, 3으로 넣는 것과는 다릅니다.**  
   실제 모델은 위치를 scalar 하나가 아니라 hidden dimension과 같은 vector로 표현합니다. 그래야 token embedding과 자연스럽게 결합됩니다.

4. **Sinusoidal encoding만 쓰는 것은 아닙니다.**  
   learned position embedding, relative position, RoPE 등 다양한 방식이 있습니다. 모델 구조와 목적에 따라 선택이 달라집니다.

5. **긴 context 성능은 position 처리와 강하게 연결됩니다.**  
   모델이 학습 때 본 위치 범위를 넘어가면 위치 정보를 해석하는 방식이 달라질 수 있습니다. 그래서 context extension은 단순히 입력 길이 제한만 늘리는 문제가 아닙니다.

---

## 복습 질문 3개

1. Transformer block 안에서 attention sublayer와 FFN은 각각 어떤 역할을 하나요?
2. Multi-head attention에서 여러 head를 쓰면 single-head attention보다 어떤 점이 좋아질 수 있나요?
3. Transformer에 positional encoding이 없다면 문장 순서를 이해할 때 어떤 문제가 생길 수 있나요?

## 오늘의 한 줄 요약

Transformer block은 attention으로 token 사이의 문맥을 섞고, FFN으로 각 token 표현을 가공하며, multi-head attention은 여러 관점의 관계를 동시에 보고, positional encoding은 그 모든 계산에 순서 정보를 넣어 줍니다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 22/30]

오늘은 Transformer block, multi-head attention, positional encoding이 왜 필요한지 차근차근 복습해 볼게요.

### 1. Transformer block 안에서 attention sublayer와 FFN은 각각 어떤 역할을 하나요?

**정답**

attention sublayer는 token들이 서로를 참고해서 문맥 정보를 섞는 역할을 합니다.

FFN, 즉 Feed-Forward Network는 attention으로 섞인 각 token의 표현을 더 깊게 가공하는 역할을 합니다.

짧게 말하면:

- attention sublayer: “다른 token들 중 무엇을 봐야 할까?”
- FFN: “가져온 정보를 내 token 표현 안에서 어떻게 해석하고 정리할까?”

입니다.

**설명**

Transformer block은 하나의 큰 처리 단위입니다. 이 안에는 보통 attention sublayer, FFN, residual connection, LayerNorm이 들어갑니다.

먼저 attention sublayer는 token 사이의 관계를 봅니다. 예를 들어 `나는 사과를 먹었다`라는 문장에서 `먹었다`라는 token은 “무엇을 먹었는가?”를 알기 위해 `사과를`이라는 token을 강하게 참고해야 합니다. 이런 식으로 attention은 각 token이 다른 token들을 얼마나 볼지 정하고, 필요한 정보를 가져옵니다.

하지만 정보를 가져오는 것만으로는 충분하지 않습니다. 가져온 정보를 바탕으로 token의 내부 표현을 더 유용하게 바꿔야 합니다. 이 일을 FFN이 합니다.

FFN은 각 token에 따로 적용되는 작은 신경망입니다. attention이 token들 사이의 정보를 섞는다면, FFN은 한 token의 vector 안에 있는 feature들을 조합하고 변환합니다. 여기서 feature는 모델이 내부적으로 쓰는 특징 정보라고 보면 됩니다.

예를 들어 `먹었다`가 attention을 통해 `사과를`, `나는` 정보를 가져왔다면, FFN은 그 정보를 바탕으로 “누가 무엇을 먹은 사건인가”에 더 적합한 hidden state로 바꿔 줍니다. hidden state는 모델 내부에서 token을 나타내는 숫자 vector입니다.

즉 attention은 문맥을 가져오고, FFN은 그 문맥을 이용해 표현을 다듬습니다.

**예시**

아주 작게 숫자로 생각해 볼게요.

문장이 다음과 같다고 합시다.

```text
[나는, 사과를, 먹었다]
```

`먹었다` token이 attention을 통해 다른 token들을 이렇게 참고했다고 해봅시다.

```text
나는: 0.2
사과를: 0.6
먹었다: 0.2
```

이 말은 `먹었다`가 `사과를`을 가장 많이 참고했다는 뜻입니다. 그래서 `먹었다`의 표현에는 “사과를 먹었다”라는 문맥이 섞입니다.

그 다음 FFN은 이 섞인 정보를 다시 가공합니다.

일상 비유로 보면:

- attention: 친구들에게 물어봐서 필요한 정보를 듣기
- FFN: 들은 정보를 자기 노트에 정리하기

입니다.

친구에게 정보를 듣기만 하고 정리하지 않으면 내 지식이 되기 어렵습니다. 마찬가지로 Transformer도 attention으로 정보를 가져온 뒤 FFN으로 표현을 정리해야 합니다.

**실전 연결**

LLM에서 Transformer block은 수십 개 이상 쌓입니다. GPT 같은 모델은 각 block에서 attention으로 이전 token들의 문맥을 보고, FFN으로 각 token 표현을 가공한 뒤 다음 token을 예측합니다.

실전 구현에서는 attention과 FFN이 계산량의 큰 부분을 차지합니다. 긴 문장을 처리할 때는 attention 비용이 커지고, hidden dimension이 큰 모델에서는 FFN 비용도 매우 커집니다. 그래서 LLM 최적화, fine-tuning, LoRA, 모델 압축을 이해하려면 attention sublayer와 FFN의 역할을 구분할 수 있어야 합니다.

### 2. Multi-head attention에서 여러 head를 쓰면 single-head attention보다 어떤 점이 좋아질 수 있나요?

**정답**

Multi-head attention은 여러 attention head가 동시에 서로 다른 관점으로 token 관계를 볼 수 있게 합니다.

Single-head attention은 하나의 attention pattern만 만들지만, multi-head attention은 여러 pattern을 병렬로 만들 수 있습니다.

그래서 문장 안의 다양한 관계, 예를 들어 주어-동사 관계, 목적어-동사 관계, 위치 관계, 대명사 지시 관계 등을 더 풍부하게 잡을 수 있습니다.

**설명**

Multi-head attention에서 head는 attention을 계산하는 하나의 작은 단위입니다. 각 head는 같은 입력을 보지만, 서로 다른 projection matrix를 사용합니다.

여기서 projection은 vector를 다른 표현 공간으로 바꾸는 일입니다. subspace projection은 전체 hidden state를 head가 볼 수 있는 작은 관점의 공간으로 바꾸는 것이라고 생각하면 됩니다.

사람이 문장을 읽을 때도 한 가지 기준만 보지 않습니다.

예를 들어:

```text
민수가 철수에게 책을 돌려주었다.
```

이 문장을 이해하려면 여러 질문을 해야 합니다.

- 누가 돌려주었는가? → 민수
- 누구에게 돌려주었는가? → 철수
- 무엇을 돌려주었는가? → 책
- 어떤 행동인가? → 돌려주었다

Single-head attention은 이 모든 관계를 하나의 attention 방식으로 처리해야 합니다. 반면 multi-head attention은 여러 head가 각각 다른 관계에 집중할 수 있는 여지를 줍니다.

중요한 점은 사람이 미리 “1번 head는 주어 담당, 2번 head는 목적어 담당”이라고 정해 주는 것은 아니라는 점입니다. 모델이 학습 과정에서 각 head의 weight를 조정하면서 서로 다른 패턴을 학습할 수 있습니다.

또한 여러 head는 parallel heads, 즉 병렬로 계산됩니다. 순서대로 하나씩 실행하는 것이 아니라 GPU에서 동시에 처리되도록 구현됩니다. 그래서 다양한 관점을 계산하면서도 효율적인 병렬 처리가 가능합니다.

**예시**

문장이 다음과 같다고 해봅시다.

```text
[고양이가, 생선을, 먹었다]
```

`먹었다`라는 token이 문장을 이해하려면 두 가지 정보를 모두 알아야 합니다.

첫 번째 head는 “무엇을 먹었는가?”에 집중할 수 있습니다.

```text
고양이가: 0.1
생선을: 0.8
먹었다: 0.1
```

이 head는 `생선을`을 많이 봅니다.

두 번째 head는 “누가 먹었는가?”에 집중할 수 있습니다.

```text
고양이가: 0.7
생선을: 0.1
먹었다: 0.2
```

이 head는 `고양이가`를 많이 봅니다.

두 head의 결과를 합치면 `먹었다`라는 token은 “고양이가 먹었다”와 “생선을 먹었다”라는 정보를 함께 가질 수 있습니다.

일상 비유로는 여러 명의 독자가 같은 글을 읽는 것과 비슷합니다.

- 한 사람은 문법을 봅니다.
- 한 사람은 의미를 봅니다.
- 한 사람은 대명사가 누구를 가리키는지 봅니다.
- 한 사람은 중요한 명사들을 봅니다.

마지막에는 이 의견들을 합쳐 더 풍부한 이해를 만듭니다.

**실전 연결**

실제 LLM에서는 multi-head attention이 핵심 구조입니다. GPT, BERT, T5, Vision Transformer 같은 모델 대부분이 여러 head를 사용합니다.

구현 관점에서는 tensor shape가 자주 다음처럼 바뀝니다.

```text
batch × sequence × d_model
→ batch × heads × sequence × d_head
```

이 구조를 이해하면 attention 코드를 읽을 때 왜 reshape, transpose, concat이 필요한지 알 수 있습니다.

또 연구나 디버깅에서는 특정 attention head가 어떤 token을 보는지 attention map으로 시각화하기도 합니다. 다만 attention weight가 높다고 해서 그 token이 최종 답의 유일한 원인이라는 뜻은 아닙니다. FFN, residual connection, 여러 layer의 상호작용도 함께 영향을 줍니다.

### 3. Transformer에 positional encoding이 없다면 문장 순서를 이해할 때 어떤 문제가 생길 수 있나요?

**정답**

Positional encoding이 없으면 Transformer는 token이 문장 안에서 몇 번째에 있는지 알기 어렵습니다.

그 결과 같은 단어들이 들어 있어도 순서가 다른 문장을 제대로 구분하지 못할 수 있습니다.

예를 들어:

```text
개가 사람을 물었다.
사람이 개를 물었다.
```

두 문장은 같은 단어를 사용하지만 의미는 완전히 다릅니다. Positional encoding은 이런 순서 차이를 모델에게 알려 주는 장치입니다.

**설명**

Transformer의 self-attention은 token들 사이의 관련성을 계산합니다. 하지만 기본 attention 구조만 보면 token들을 순서대로 하나씩 읽는 것이 아니라, 한꺼번에 비교합니다.

RNN은 첫 번째 token, 두 번째 token, 세 번째 token을 순서대로 처리하기 때문에 구조 자체에 순서 정보가 들어 있습니다. 반면 Transformer는 병렬 계산을 잘하기 위해 token들을 동시에 처리합니다. 이 장점 덕분에 빠르게 학습할 수 있지만, 순서를 따로 알려 주는 장치가 필요합니다.

그 장치가 positional encoding입니다.

Positional encoding은 token embedding에 위치 정보를 더합니다. token embedding은 단어의 의미를 담은 vector이고, positional encoding은 그 token이 몇 번째 위치에 있는지를 담은 vector입니다.

기본적인 결합은 다음처럼 생각할 수 있습니다.

```text
input_i = token_embedding_i + positional_encoding_i
```

여기서 `i`는 token의 위치입니다.

즉 모델은 “이 단어가 무엇인가?”와 “이 단어가 어디에 있는가?”를 함께 받습니다.

대표적인 방법 중 하나가 sinusoidal encoding입니다. 이는 sine과 cosine 함수를 사용해 위치마다 다른 vector를 만드는 방식입니다. 또 많은 실제 모델은 learned position embedding처럼 위치 vector 자체를 학습하기도 합니다. 최근 LLM에서는 RoPE 같은 상대적 위치 방식도 많이 사용합니다.

하지만 오늘의 핵심은 하나입니다.

Transformer는 순서를 자동으로 완벽히 아는 구조가 아니기 때문에 position information을 따로 넣어야 합니다.

**예시**

아주 작은 숫자로 생각해 볼게요.

token embedding이 다음과 같다고 합시다.

```text
나는 embedding = 5
밥을 embedding = 8
먹었다 embedding = 3
```

위치 정보는 이렇게 단순화해 보겠습니다.

```text
1번째 위치 encoding = 0.1
2번째 위치 encoding = 0.2
3번째 위치 encoding = 0.3
```

그러면 입력은 다음처럼 됩니다.

```text
나는: 5 + 0.1 = 5.1
밥을: 8 + 0.2 = 8.2
먹었다: 3 + 0.3 = 3.3
```

이제 같은 `밥을`이라는 token도 위치가 바뀌면 표현이 달라집니다.

```text
밥을이 1번째면: 8 + 0.1 = 8.1
밥을이 2번째면: 8 + 0.2 = 8.2
```

이 작은 차이 덕분에 모델은 같은 단어라도 어디에 등장했는지 구분할 수 있습니다.

일상 비유로는 택배 상자와 주소 라벨을 생각하면 좋습니다. token embedding이 상자 안의 물건이라면, positional encoding은 주소 라벨입니다. 물건이 무엇인지도 중요하지만, 어디에 놓여야 하는지도 중요합니다.

**실전 연결**

LLM에서 positional encoding은 문장 생성과 긴 context 처리에 매우 중요합니다. GPT 같은 모델은 이전 token들을 보고 다음 token을 예측하는데, 순서 정보를 모르면 문장의 흐름을 제대로 이해하기 어렵습니다.

코드 모델에서도 위치 정보는 중요합니다. 변수 선언이 먼저 나오고 사용이 나중에 나오는지, 괄호가 어디서 열리고 닫히는지, 줄의 순서가 어떻게 되는지가 모두 의미에 영향을 줍니다.

또 긴 context 모델에서는 positional encoding 방식이 성능에 큰 영향을 줍니다. 예를 들어 모델이 4,096 token 길이로 학습되었는데 훨씬 긴 문서를 넣으면, 위치 정보를 어떻게 해석하느냐가 중요해집니다. 그래서 RoPE scaling, relative position, ALiBi 같은 기술들이 긴 문맥 LLM에서 자주 등장합니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-14-day22.md
