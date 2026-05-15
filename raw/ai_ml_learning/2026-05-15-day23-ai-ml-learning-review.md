# AI/ML Learning Review - Day 23 (2026-05-15)
## Source Metadata
- Lesson source: /home/ubuntu/work/ai/learning/logs/2026-05-15-day23.md
- Follow-up answer source: /home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-15_09-26-07.md

---

## Lesson

# Day 23 - AI/ML 기초 학습

- Date: 2026-05-15
- Progress: 23/30
- Level: beginner-intermediate
- Milestone: Transformer 심화 기초
- Milestone goal: Transformer의 각 블록이 왜 필요한지 구조적으로 이해한다.

## Today's 3 concepts

1. Residual connection과 gradient path
2. LayerNorm의 역할
3. Position-wise FFN

---

## 1. Residual connection과 gradient path

### 한 줄 직관

Residual connection은 “블록이 새로 계산한 내용만 더하고, 원래 정보는 그대로 지나가게 해 주는 지름길”이다. 그래서 모델이 깊어져도 정보와 gradient가 길을 잃지 않는다.

### 개념 정의

Residual connection은 어떤 neural network block의 출력에 입력을 그대로 더하는 구조다.

가장 단순한 형태는 다음과 같다.

\[
y = x + F(x)
\]

여기서 `x`는 블록에 들어온 hidden state이고, `F(x)`는 attention block이나 feed-forward network가 새로 계산한 변화량이다. `x`가 그대로 더해지는 길을 skip path라고 부른다. 말 그대로 복잡한 계산을 “건너뛰는 길”이다.

Transformer에서는 보통 attention이나 FFN이 만든 결과를 원래 hidden state에 더한다. 그래서 각 블록은 완전히 새로운 표현을 처음부터 만들기보다, 기존 표현을 조금씩 수정하는 방식으로 작동한다.

### 왜 이런 개념이 필요한가

깊은 neural network를 학습할 때 가장 큰 문제 중 하나는 gradient가 아주 많은 층을 거치며 약해지거나 불안정해지는 것이다. Gradient는 loss를 줄이기 위해 각 weight를 어느 방향으로 바꿔야 하는지 알려 주는 신호다.

예를 들어 50층짜리 모델이 있다고 하자. 맨 마지막에서 계산된 loss 정보가 첫 번째 층까지 돌아가야 한다. 그런데 모든 층을 반드시 복잡한 계산 경로로만 통과해야 한다면, 중간중간에서 신호가 작아지거나 왜곡될 수 있다. 그러면 앞쪽 층은 “내가 어떻게 바뀌어야 loss가 줄어드는지”를 잘 받지 못한다.

Residual connection은 여기서 지름길을 만든다. 블록 내부의 복잡한 계산 `F(x)`를 지나가는 길도 있지만, 입력 `x`가 그대로 출력으로 가는 skip path도 있다. 이 덕분에 gradient도 더 직접적인 길을 타고 앞쪽으로 돌아갈 수 있다.

실전적으로는 residual connection 덕분에 모델을 훨씬 깊게 쌓을 수 있다. Transformer, ResNet, GPT 계열 모델이 깊은 layer를 많이 가질 수 있는 핵심 이유 중 하나다.

### 아주 쉬운 예시

친구에게 문장을 고쳐 달라고 했다고 생각해 보자.

원래 문장:

> 오늘 날씨가 좋다.

친구가 문장을 완전히 새로 쓰는 대신, 수정할 부분만 더한다고 하자.

수정량:

> “정말”을 추가하자.

그러면 최종 문장은 다음처럼 된다.

> 오늘 날씨가 정말 좋다.

Residual connection은 이 방식과 비슷하다. 원래 정보 `x`를 버리지 않고, 블록이 계산한 수정량 `F(x)`만 더한다.

숫자로 보면 더 쉽다.

- 입력 `x = 10`
- 블록이 계산한 변화량 `F(x) = 2`
- 출력 `y = x + F(x) = 10 + 2 = 12`

만약 블록이 아직 학습 초기라서 똑똑하지 않다면 `F(x)`가 거의 0일 수도 있다.

- 입력 `x = 10`
- 변화량 `F(x) = 0`
- 출력 `y = 10 + 0 = 10`

이 경우에도 원래 정보는 망가지지 않고 그대로 지나간다. 그래서 모델은 처음부터 모든 것을 완벽히 새로 만들 필요가 없다. “필요한 만큼만 수정하기”를 배우면 된다.

### 개념 구조와 핵심 포인트

Residual connection의 핵심은 세 가지다.

1. **원래 정보를 보존한다**  
   입력 hidden state가 그대로 다음 단계로 전달된다. 따라서 block이 실수하더라도 원래 정보가 완전히 사라지지 않는다.

2. **각 block을 ‘변화량 학습’ 문제로 바꾼다**  
   블록은 전체 출력을 새로 만드는 대신 `F(x)`라는 보정값을 학습한다. 예를 들어 “이 token 표현에 문맥 정보를 조금 더해라” 같은 역할을 한다.

3. **gradient path를 짧고 안정적으로 만든다**  
   출력 `y`가 입력 `x`를 직접 포함하므로, loss에서 나온 gradient가 `x`까지 비교적 직접 전달될 수 있다.

Transformer block을 아주 단순하게 쓰면 다음과 비슷하다.

\[
x_1 = x + Attention(x)
\]

\[
x_2 = x_1 + FFN(x_1)
\]

즉 attention도 residual connection으로 감싸고, FFN도 residual connection으로 감싼다. 이 구조 덕분에 layer가 많아져도 hidden state가 단계적으로 업데이트된다.

### 핵심 수학 포인트

가장 단순한 식은 다음이다.

\[
y = x + F(x)
\]

이 식의 중요한 의미는 출력이 입력 `x`에 직접 의존한다는 점이다. 만약 loss를 `L`이라고 하면, gradient는 대략 두 경로를 통해 `x`로 돌아간다.

1. `x`가 그대로 더해진 직접 경로
2. `F(x)` 내부 계산을 통과하는 경로

아주 작은 1D 예시로 보자.

\[
y = x + 0.5x = 1.5x
\]

여기서 `F(x) = 0.5x`다. 만약 loss가 출력 `y`에 대해 “y를 1만큼 키우는 방향이 중요하다”는 신호를 보낸다면, `x`는 직접 경로와 `F(x)` 경로를 모두 통해 신호를 받는다.

직관적으로 말하면, gradient가 지나갈 수 있는 길이 하나가 아니라 여러 개가 된다. 특히 `x`가 그대로 더해지는 길은 복잡한 weight를 통과하지 않는 길이므로 깊은 모델에서 안정성에 큰 도움이 된다.

수식을 너무 어렵게 외울 필요는 없다. 핵심은 이것이다.

> `y = x + F(x)`이면, 모델은 “원래 정보 + 필요한 수정”을 배우고, gradient도 원래 정보 쪽으로 더 쉽게 돌아간다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **residual connection**: 입력을 block의 출력에 다시 더하는 연결 구조. Transformer와 ResNet의 핵심 구조다.
- **skip path**: 복잡한 block 계산을 건너뛰어 입력이 그대로 지나가는 경로.
- **optimization path**: optimizer가 loss를 줄이기 위해 weight를 조정할 때 gradient가 전달되는 학습 경로. Residual connection은 이 경로를 더 안정적으로 만든다.
- **hidden state**: 모델 내부에서 token이나 데이터가 표현되는 벡터. Transformer에서는 각 token마다 hidden state가 있다.
- **gradient**: loss를 줄이기 위해 parameter를 어느 방향으로 바꿔야 하는지 알려 주는 신호.

### AI에서 어디에 쓰이는가

Residual connection은 거의 모든 현대 deep learning 모델에서 사용된다.

- **Transformer**: attention 결과와 FFN 결과를 각각 원래 hidden state에 더한다.
- **GPT/BERT 계열 LLM**: 수십~수백 개 layer를 쌓을 수 있게 해 준다.
- **ResNet**: 이미지 인식 모델에서 깊은 CNN을 안정적으로 학습하게 만든 대표 구조다.

LLM에서 한 token의 hidden state는 layer를 지날 때마다 조금씩 의미가 정교해진다. 예를 들어 “bank”라는 단어가 처음에는 단순한 단어 embedding이었다가, 문맥을 보며 “강둑”인지 “은행”인지 구분되는 표현으로 바뀐다. Residual connection은 이 업데이트를 “기존 표현을 보존하면서 필요한 정보를 더하는 방식”으로 만들어 준다.

### 헷갈리기 쉬운 포인트

- Residual connection은 단순히 값을 더하는 기술처럼 보이지만, 실제로는 깊은 모델 학습을 가능하게 하는 optimization 구조다.
- `F(x)`가 중요하지 않다는 뜻이 아니다. `F(x)`는 attention이나 FFN처럼 핵심 계산을 한다. 다만 원래 정보 `x`를 버리지 않게 해 준다.
- Skip path가 있다고 해서 block을 무시하는 것은 아니다. 학습이 진행되면 block은 필요한 변화량을 점점 더 잘 만든다.
- Residual connection만으로 모든 학습 문제가 해결되지는 않는다. Transformer에서는 LayerNorm, 좋은 initialization, optimizer 설정 등이 함께 중요하다.

---

## 2. LayerNorm의 역할

### 한 줄 직관

LayerNorm은 각 token의 hidden state 안에서 feature 값들의 크기와 중심을 정리해, 다음 block이 너무 크거나 너무 작은 숫자에 흔들리지 않게 해 주는 안정화 장치다.

### 개념 정의

LayerNorm은 layer normalization의 줄임말이다. Transformer에서는 보통 각 token의 hidden state 벡터를 feature 방향으로 정규화한다.

예를 들어 어떤 token 하나가 4차원 hidden state로 표현된다고 하자.

\[
x = [2, 4, 6, 8]
\]

LayerNorm은 이 벡터 안의 값들의 평균과 분산을 구한 뒤, 값들을 평균 0, 표준편차 1에 가깝게 바꾼다. 그 다음 모델이 학습하는 scale과 shift를 적용한다. Scale은 다시 얼마나 키울지, shift는 얼마나 옮길지를 배우는 값이다.

중요한 점은 LayerNorm이 batch 전체를 보는 것이 아니라, 보통 “각 token의 feature들”을 본다는 것이다. 그래서 문장 길이나 batch 크기가 달라도 Transformer에서 안정적으로 쓰기 좋다.

### 왜 이런 개념이 필요한가

Neural network는 숫자를 계속 변환한다. Embedding에서 시작한 hidden state는 attention을 지나고, residual connection으로 더해지고, FFN을 지나며 계속 바뀐다. 이때 값의 크기가 너무 커지거나 너무 작아지면 학습이 불안정해진다.

예를 들어 어떤 layer에서는 hidden state 값이 `[1, 2, 1]` 정도였는데, 다음 layer에서는 `[100, -80, 120]`처럼 커졌다고 하자. 그러면 activation이 지나치게 커지고, gradient도 흔들릴 수 있다. 반대로 값이 너무 작아지면 의미 있는 차이가 사라질 수 있다.

LayerNorm은 각 단계에서 숫자의 중심과 크기를 정리해 준다. 그래서 다음 block은 “매번 너무 다른 스케일의 입력”을 받지 않고, 비교적 예측 가능한 범위의 입력을 받는다.

실전 LLM에서는 LayerNorm의 위치도 중요하다. Transformer block 안에서 LayerNorm을 attention/FFN 앞에 두는 방식을 Pre-LN이라고 하고, 뒤에 두는 방식을 Post-LN이라고 부른다. 현대 LLM에서는 깊은 모델 학습 안정성 때문에 Pre-LN 구조를 자주 쓴다.

### 아주 쉬운 예시

세 명의 학생 점수가 있다고 하자.

- A: 20점
- B: 40점
- C: 60점

이 점수만 보면 평균은 40점이다. 각 점수가 평균에서 얼마나 떨어져 있는지 보면 다음과 같다.

- A: -20
- B: 0
- C: +20

이제 “점수의 절대 크기”보다 “평균에 비해 얼마나 낮거나 높은가”를 보는 것이다.

LayerNorm도 비슷하다. 어떤 token의 hidden state가 다음과 같다고 하자.

\[
x = [2, 4, 6]
\]

1. 평균을 구한다.

\[
mean = (2 + 4 + 6) / 3 = 4
\]

2. 평균에서 얼마나 떨어졌는지 본다.

\[
[-2, 0, 2]
\]

3. 값의 퍼짐 정도를 구한다. 여기서는 표준편차가 약 `1.63`이다.

4. 각 값을 표준편차로 나눈다.

\[
[-2/1.63, 0/1.63, 2/1.63] \approx [-1.22, 0, 1.22]
\]

이제 값들이 너무 크거나 작지 않은 범위로 정리되었다. 이후 모델은 학습 가능한 scale과 shift를 사용해서 필요한 만큼 다시 조정한다.

### 개념 구조와 핵심 포인트

LayerNorm의 기본 흐름은 다음과 같다.

1. 한 token의 hidden state 벡터를 가져온다.
2. 그 벡터 안 feature 값들의 평균을 계산한다.
3. feature 값들이 평균에서 얼마나 퍼져 있는지 계산한다.
4. 평균을 빼고, 퍼짐 정도로 나누어 값의 중심과 크기를 정리한다.
5. 학습 가능한 scale과 shift를 적용한다.

Transformer에서 hidden state의 shape이 다음과 같다고 해 보자.

\[
[batch, sequence\ length, hidden\ dimension]
\]

예를 들어 `[2, 5, 768]`이라면 batch에 문장 2개가 있고, 각 문장에 token 5개가 있고, 각 token은 768차원 벡터라는 뜻이다.

LayerNorm은 보통 마지막 dimension인 hidden dimension 쪽을 정규화한다. 즉 token 하나하나마다 768개 feature의 평균과 퍼짐을 계산한다.

핵심은 “token 간 비교”가 아니라 “한 token 내부 feature들의 스케일 정리”다.

### 핵심 수학 포인트

LayerNorm의 기본 식은 다음과 비슷하다.

\[
\hat{x} = \frac{x - mean(x)}{\sqrt{variance(x) + \epsilon}}
\]

그리고 학습 가능한 scale과 shift를 적용한다.

\[
y = \gamma \hat{x} + \beta
\]

여기서:

- `mean(x)`: hidden state 벡터 안 feature 값들의 평균
- `variance(x)`: 값들이 평균에서 얼마나 퍼져 있는지 나타내는 양
- `epsilon`: 0으로 나누는 일을 막기 위한 아주 작은 숫자
- `gamma`: 모델이 학습하는 scale
- `beta`: 모델이 학습하는 shift

왜 `gamma`와 `beta`가 필요할까? 정규화만 하면 모든 값이 무조건 평균 0, 표준편차 1에 가깝게 묶인다. 하지만 모델 입장에서는 어떤 feature는 더 크게 유지해야 할 수도 있고, 어떤 feature는 약간 이동해야 할 수도 있다. 그래서 정규화한 뒤에도 모델이 필요한 스케일과 위치를 다시 배울 수 있게 한다.

즉 LayerNorm은 값을 강제로 똑같이 만드는 장치가 아니라, “안정적인 기준으로 정리한 뒤 필요한 조정은 다시 배우게 하는 장치”다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **layer normalization**: 한 layer의 hidden state에서 feature 방향으로 값을 정규화하는 방법.
- **feature normalization**: feature 값들의 중심과 크기를 정리하는 과정.
- **stability**: 학습 중 숫자 크기, gradient, loss 변화가 지나치게 흔들리지 않는 안정성.
- **mean**: 평균. 값들의 중심 위치를 나타낸다.
- **variance**: 값들이 평균 주변에 얼마나 퍼져 있는지 나타낸다.
- **scale / shift**: LayerNorm 후 값을 다시 키우거나 옮기기 위해 학습되는 조정값.
- **Pre-LN / Post-LN**: LayerNorm을 block 계산 앞에 두는지 뒤에 두는지에 따른 Transformer 구조 구분.

### AI에서 어디에 쓰이는가

LayerNorm은 Transformer에서 거의 필수 구성 요소다.

- **LLM 학습 안정화**: GPT, BERT, T5 같은 모델에서 hidden state 값이 layer를 지날 때 너무 불안정해지지 않도록 돕는다.
- **긴 sequence 처리**: 문장 길이나 batch 크기가 달라도 token별로 정규화하기 때문에 NLP 모델에 잘 맞는다.
- **Residual connection과 함께 사용**: residual addition으로 값이 계속 더해지면 스케일이 변할 수 있는데, LayerNorm이 이를 정리해 준다.
- **Optimizer가 학습하기 쉬운 지형 만들기**: 입력 스케일이 너무 들쭉날쭉하면 optimizer가 적절한 step size를 잡기 어렵다. LayerNorm은 이 문제를 줄인다.

실제 LLM에서 LayerNorm이 없으면 loss가 불안정하게 튀거나, 깊은 layer를 가진 모델이 제대로 학습되지 않을 수 있다.

### 헷갈리기 쉬운 포인트

- LayerNorm은 “값을 작게 만드는 것”이 목적이 아니다. 값의 중심과 스케일을 정리해 안정적으로 만드는 것이 목적이다.
- LayerNorm은 BatchNorm과 다르다. BatchNorm은 batch 방향 통계를 많이 사용하지만, LayerNorm은 보통 각 token의 feature 방향을 본다.
- 정규화 후에도 `gamma`, `beta` 때문에 모델은 필요한 표현 크기를 다시 배울 수 있다.
- LayerNorm이 의미 정보를 없애는 것은 아니다. 오히려 숫자 스케일 문제 때문에 의미 학습이 방해받는 일을 줄여 준다.

---

## 3. Position-wise FFN

### 한 줄 직관

Position-wise FFN은 attention이 섞어 온 문맥 정보를 각 token 자리마다 따로 가공하는 작은 MLP block이다.

### 개념 정의

Position-wise FFN은 Transformer block 안에 들어 있는 feed-forward network다. 여기서 position-wise라는 말은 “각 token position에 같은 FFN을 독립적으로 적용한다”는 뜻이다.

Transformer block에는 크게 두 종류의 계산이 있다.

1. **Attention**: token들이 서로를 보면서 정보를 섞는다.
2. **Position-wise FFN**: 각 token의 hidden state를 개별적으로 깊게 변환한다.

FFN은 보통 두 개의 linear layer와 activation function으로 구성된다.

\[
FFN(x) = W_2 \sigma(W_1x + b_1) + b_2
\]

여기서 `x`는 token 하나의 hidden state다. `W_1`은 hidden dimension을 더 큰 intermediate dimension으로 확장하고, `W_2`는 다시 원래 hidden dimension으로 줄인다.

예를 들어 LLM에서 hidden dimension이 768이라면 FFN 내부에서는 3072처럼 더 큰 차원으로 확장했다가 다시 768로 줄이는 경우가 많다.

### 왜 이런 개념이 필요한가

Attention은 token 사이의 관계를 잘 다룬다. 예를 들어 “그는 사과를 먹었다. 그것은 빨갰다.”라는 문장에서 “그것”이 “사과”를 가리킨다는 정보를 attention이 섞어 줄 수 있다.

하지만 token 사이 정보를 섞는 것만으로는 충분하지 않다. 섞어 온 정보를 바탕으로 각 token의 표현을 더 복잡하게 변환해야 한다. 예를 들어 어떤 token hidden state 안에는 품사, 의미, 문맥, 위치, 문장 역할 같은 여러 feature가 섞여 있다. FFN은 이 feature들을 조합해서 더 유용한 representation으로 바꾼다.

쉽게 말해 attention이 “누구의 정보를 볼지”를 결정한다면, FFN은 “그 정보를 보고 내 token 표현을 어떻게 가공할지”를 담당한다.

### 아주 쉬운 예시

음식 재료로 비유해 보자.

Attention은 여러 재료를 한 그릇에 모아 주는 과정과 비슷하다.

- 토마토 정보
- 치즈 정보
- 빵 정보

이 정보들이 한 token의 hidden state 안에 섞여 들어왔다고 하자. 그런데 재료를 모으기만 하면 요리가 완성되지 않는다. 이제 자르고, 굽고, 양념해야 한다. 이 가공 과정이 FFN에 가깝다.

숫자로 아주 작게 보자.

어떤 token의 hidden state가 2차원이라고 하자.

\[
x = [1, 2]
\]

첫 번째 linear layer가 이것을 3차원으로 확장한다고 하자.

\[
[1, 2] \rightarrow [3, -1, 4]
\]

activation function이 음수 값을 약하게 만들거나 0으로 만든다고 하자. ReLU라면 음수는 0이 된다.

\[
[3, -1, 4] \rightarrow [3, 0, 4]
\]

두 번째 linear layer가 다시 2차원으로 줄인다.

\[
[3, 0, 4] \rightarrow [5, 1]
\]

즉 FFN은 token 하나의 hidden state를 “확장 → 비선형 변환 → 축소”하면서 더 풍부한 feature 조합을 만든다.

### 개념 구조와 핵심 포인트

Position-wise FFN의 핵심 구조는 다음이다.

1. 입력: 각 token의 hidden state
2. 첫 번째 linear layer: hidden dimension을 더 큰 차원으로 확장
3. activation function: 단순한 직선 변환만으로는 못 하는 비선형 패턴을 표현
4. 두 번째 linear layer: 다시 원래 hidden dimension으로 축소
5. residual connection과 함께 출력에 더해짐

Shape 관점에서 보면 다음과 같다.

- 입력 hidden states: `[sequence length, d_model]`
- 예: token 3개, hidden dimension 4라면 `[3, 4]`

Position-wise FFN은 각 행, 즉 각 token에 같은 MLP를 적용한다.

- token 1의 4차원 벡터 → FFN → 새 4차원 벡터
- token 2의 4차원 벡터 → 같은 FFN → 새 4차원 벡터
- token 3의 4차원 벡터 → 같은 FFN → 새 4차원 벡터

중요한 점은 FFN 자체는 token들을 서로 섞지 않는다는 것이다. Token 간 정보 교환은 attention이 주로 담당한다. FFN은 각 token 내부 feature를 변환한다.

그래서 Transformer block은 다음처럼 역할이 나뉜다.

- Attention: token 간 정보 mixing
- FFN: token별 feature transformation
- Residual connection: 원래 정보 보존과 gradient path 제공
- LayerNorm: 값의 scale 안정화

### 핵심 수학 포인트

Position-wise FFN의 기본 식은 다음이다.

\[
FFN(x) = W_2 \sigma(W_1x + b_1) + b_2
\]

여기서:

- `x`: token 하나의 hidden state 벡터
- `W_1`: 첫 번째 linear layer의 weight
- `b_1`: 첫 번째 bias
- `σ`: activation function. 예: ReLU, GELU, SwiGLU 계열
- `W_2`: 두 번째 linear layer의 weight
- `b_2`: 두 번째 bias

가장 중요한 수학적 의미는 “linear transformation만 두 번 하는 것이 아니라, 중간에 activation을 넣어서 비선형 변환을 만든다”는 점이다.

만약 activation이 없다면 linear layer 두 개를 이어 붙여도 결국 하나의 더 큰 linear layer와 비슷하게 합쳐질 수 있다. 그러면 복잡한 패턴을 표현하기 어렵다. Activation이 들어가면 feature 사이의 조건부 관계를 더 잘 표현할 수 있다.

예를 들어 어떤 feature가 “이 token은 동사일 가능성”이고, 다른 feature가 “앞에 주어가 있음”이라면, FFN은 이런 feature 조합을 보고 “이 token의 문법적 역할을 더 강하게 표현하자” 같은 변환을 배울 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **feed-forward network**: 입력이 한 방향으로 linear layer와 activation을 지나 출력으로 가는 network. Transformer의 FFN block을 가리킬 때 자주 쓴다.
- **point-wise transformation**: 각 position/token에 독립적으로 적용되는 변환. Position-wise FFN과 거의 같은 맥락에서 이해하면 된다.
- **MLP block**: multi-layer perceptron block. 여러 linear layer와 activation으로 구성된 작은 network.
- **linear layer**: 벡터에 weight matrix를 곱하고 bias를 더하는 layer.
- **activation function**: 모델이 비선형 패턴을 표현할 수 있게 해 주는 함수. 예: ReLU, GELU.
- **d_model**: Transformer에서 hidden state의 기본 차원 수.
- **intermediate dimension**: FFN 내부에서 잠시 확장되는 더 큰 차원.

### AI에서 어디에 쓰이는가

Position-wise FFN은 Transformer block의 절반 정도를 차지할 만큼 중요하다. 많은 LLM에서 parameter 수의 상당 부분이 attention보다 FFN에 들어가기도 한다.

실제 사용처는 다음과 같다.

- **LLM의 token representation 가공**: attention이 가져온 문맥 정보를 token별로 해석하고 변환한다.
- **feature 조합 학습**: hidden state 안의 여러 feature를 조합해 더 유용한 representation을 만든다.
- **모델 용량 증가**: FFN의 intermediate dimension을 크게 하면 모델이 더 다양한 패턴을 표현할 수 있다.
- **Transformer block의 핵심 연산**: GPT, BERT, T5, LLaMA 같은 모델은 모두 attention과 FFN을 반복해서 쌓는다.

예를 들어 번역 모델에서 attention이 원문 단어와 목표 문장 단어 사이의 관계를 찾는다면, FFN은 그 정보를 바탕으로 현재 token이 어떤 의미와 문법 형태를 가져야 하는지 더 구체적으로 가공한다.

### 헷갈리기 쉬운 포인트

- Position-wise FFN은 sequence 전체를 한꺼번에 섞는 layer가 아니다. 각 token position에 같은 network를 따로 적용한다.
- Token 간 정보 교환은 주로 attention이 한다. FFN은 token 내부 feature 변환에 더 가깝다.
- FFN은 단순한 부가 장치가 아니다. Transformer의 표현력과 parameter 규모에서 매우 큰 비중을 차지한다.
- “feed-forward”라는 말은 recurrent network처럼 시간 순환이 없고, 입력에서 출력으로 한 방향 계산이 진행된다는 뜻이다.

---

## 복습 질문 3개

1. Residual connection에서 `y = x + F(x)` 구조가 깊은 모델의 gradient 전달에 왜 도움이 될까?
2. LayerNorm은 Transformer hidden state의 어떤 방향을 정규화하며, BatchNorm과 어떤 점에서 다르게 이해해야 할까?
3. Attention과 Position-wise FFN은 Transformer block 안에서 각각 어떤 역할을 나누어 맡을까?

## 오늘의 한 줄 요약

Transformer block은 residual connection으로 정보를 보존하고 gradient path를 안정화하며, LayerNorm으로 hidden state의 스케일을 정리하고, Position-wise FFN으로 각 token의 feature를 깊게 가공한다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 23/30]

오늘은 Transformer block 안에서 “깊게 쌓아도 잘 학습되게 만드는 장치들”을 복습해 볼게요.

### 1. Residual connection에서 `y = x + F(x)` 구조가 깊은 모델의 gradient 전달에 왜 도움이 될까?

**정답**

`y = x + F(x)` 구조는 입력 `x`가 복잡한 block 계산을 거치지 않고도 출력으로 직접 이어지는 길을 만든다.  
이 직접 경로를 `skip path`라고 한다.

그래서 학습할 때 loss function에서 나온 `gradient`, 즉 “어느 방향으로 parameter를 고쳐야 loss가 줄어드는지 알려 주는 신호”가 앞쪽 layer까지 더 쉽게 돌아갈 수 있다.

즉 residual connection은 깊은 모델에서 gradient가 중간에 약해지거나 꼬이는 문제를 줄여 주고, 모델을 더 안정적으로 학습하게 해 준다.

**설명**

깊은 neural network에서는 layer가 많다. 예를 들어 Transformer layer가 48개 있다고 해 보자. 마지막 layer에서 계산된 loss 정보가 첫 번째 layer까지 거꾸로 전달되어야 한다.

그런데 모든 gradient가 매번 복잡한 attention, FFN, activation, weight matrix를 통과해야 한다면 신호가 점점 약해질 수 있다. 이것을 직관적으로는 “학습 신호가 멀리까지 잘 도착하지 못한다”고 볼 수 있다.

Residual connection은 이 문제를 완화한다.

식으로 보면:

`y = x + F(x)`

여기서 `F(x)`는 attention block이나 FFN이 계산한 변화량이다. 중요한 점은 출력 `y` 안에 원래 입력 `x`가 그대로 들어 있다는 것이다.

그래서 모델은 매 layer마다 완전히 새로운 표현을 처음부터 만들 필요가 없다. 대신 “원래 표현에 무엇을 조금 더할까?”를 배우면 된다.

이 구조는 두 가지 면에서 좋다.

첫째, 원래 정보가 보존된다.  
block이 아직 잘 학습되지 않아 `F(x)`가 별로 좋은 값을 만들지 못해도, `x`는 그대로 다음 layer로 넘어갈 수 있다.

둘째, gradient가 지나갈 길이 더 단순해진다.  
복잡한 `F(x)` 경로뿐 아니라, `x`가 직접 더해진 경로를 통해 gradient가 더 쉽게 앞쪽으로 전달된다.

그래서 residual connection은 단순한 “더하기”가 아니라, 깊은 모델의 optimization path, 즉 학습 경로를 안정적으로 만들어 주는 핵심 구조다.

**예시**

아주 작은 숫자로 보자.

입력 hidden state가:

`x = 10`

block이 계산한 변화량이:

`F(x) = 2`

이면 출력은:

`y = x + F(x) = 10 + 2 = 12`

이때 모델은 10을 버리고 12를 새로 만든 것이 아니다.  
원래 값 10을 유지하면서 필요한 수정값 2를 더한 것이다.

만약 학습 초기에 block이 아직 별로 똑똑하지 않아서:

`F(x) = 0`

이라면:

`y = 10 + 0 = 10`

이 된다.

즉 block이 아무것도 잘 못 해도 원래 정보는 망가지지 않고 지나간다. 이것이 “지름길”의 힘이다.

**실전 연결**

GPT, BERT, LLaMA 같은 LLM은 Transformer layer를 수십 개에서 수백 개까지 쌓는다. 이런 깊은 모델에서 residual connection이 없으면 앞쪽 layer가 gradient를 제대로 받기 어려워 학습이 불안정해질 수 있다.

실제로 Transformer에서는 attention 결과도 원래 hidden state에 더하고, FFN 결과도 다시 원래 hidden state에 더한다. 그래서 각 layer는 token 표현을 조금씩 수정하면서 더 깊고 정교한 의미 표현을 만들어 간다.

---

### 2. LayerNorm은 Transformer hidden state의 어떤 방향을 정규화하며, BatchNorm과 어떤 점에서 다르게 이해해야 할까?

**정답**

LayerNorm은 Transformer에서 보통 각 token의 hidden state 안에 있는 `feature direction`, 즉 hidden dimension 방향을 정규화한다.

예를 들어 hidden state의 shape이:

`[batch, sequence length, hidden dimension]`

이라면 LayerNorm은 보통 마지막 차원인 `hidden dimension` 안의 값들을 정리한다.

BatchNorm은 batch에 있는 여러 데이터의 통계를 많이 사용하지만, LayerNorm은 각 token 하나의 feature 값들을 기준으로 평균과 분산을 계산한다는 점에서 다르게 이해해야 한다.

**설명**

Transformer에서 한 token은 하나의 벡터로 표현된다. 이 벡터를 hidden state라고 한다.

예를 들어 “사과”라는 token이 4차원 hidden state로 표현된다고 해 보자.

`[2, 4, 6, 8]`

LayerNorm은 이 네 개 feature 값의 평균과 퍼짐을 계산한다. 그리고 값들을 평균 0, 표준편차 1에 가까운 형태로 정리한다.

쉽게 말하면, hidden state 안의 숫자들이 너무 커지거나 너무 작아지지 않도록 중심과 크기를 맞춰 주는 것이다.

왜 이것이 필요할까?

Transformer block에서는 attention 결과가 더해지고, FFN 결과가 더해지고, residual connection도 반복된다. 그러다 보면 hidden state 값의 크기가 layer마다 계속 변할 수 있다.

어떤 layer에서는 값이:

`[1, 2, 1]`

정도였는데, 다음 layer에서는:

`[100, -80, 120]`

처럼 커질 수도 있다.

이렇게 숫자 scale이 크게 흔들리면 optimizer가 안정적으로 학습하기 어렵다. Gradient도 불안정해지고, loss가 튈 수 있다.

LayerNorm은 이런 숫자 scale을 정리해서 다음 block이 더 예측 가능한 입력을 받게 해 준다.

BatchNorm과의 차이도 중요하다.

BatchNorm은 보통 batch 안의 여러 sample을 모아서 평균과 분산을 계산한다. 이미지 모델의 CNN에서 자주 쓰였다.

반면 LayerNorm은 batch 크기에 크게 의존하지 않는다. 각 token의 hidden state 내부 feature들을 보고 정규화한다.

그래서 문장 길이가 다르거나 batch size가 작아도 Transformer에서는 LayerNorm이 안정적으로 잘 맞는다.

**예시**

한 token의 hidden state가 다음과 같다고 하자.

`x = [2, 4, 6]`

먼저 평균을 구한다.

`mean = (2 + 4 + 6) / 3 = 4`

각 값에서 평균을 빼면:

`[-2, 0, 2]`

이 된다.

이제 값들이 평균 4를 기준으로 얼마나 낮거나 높은지 보인다.

그 다음 퍼짐 정도, 즉 표준편차로 나누면 값들이 대략:

`[-1.22, 0, 1.22]`

처럼 정리된다.

이 과정은 “절대 점수”보다 “평균에 비해 얼마나 큰가/작은가”를 보는 것과 비슷하다.

학생 점수로 비유하면, 20점, 40점, 60점이 있을 때 단순히 점수만 보는 것이 아니라 평균 40점에서 얼마나 떨어져 있는지를 보는 것이다.

**실전 연결**

LLM에서는 LayerNorm이 거의 필수다. GPT 계열 모델, BERT, T5, LLaMA 같은 Transformer 모델들은 hidden state 값이 layer를 지날 때 지나치게 흔들리지 않도록 LayerNorm을 사용한다.

특히 깊은 LLM에서는 LayerNorm 위치도 중요하다. Attention이나 FFN 앞에 LayerNorm을 두는 구조를 `Pre-LN`이라고 하고, 뒤에 두는 구조를 `Post-LN`이라고 한다. 현대 LLM에서는 깊은 모델의 학습 안정성 때문에 Pre-LN 구조를 많이 사용한다.

즉 LayerNorm은 단순히 숫자를 예쁘게 만드는 장치가 아니라, 깊은 Transformer가 안정적으로 학습되도록 돕는 핵심 안정화 장치다.

---

### 3. Attention과 Position-wise FFN은 Transformer block 안에서 각각 어떤 역할을 나누어 맡을까?

**정답**

Attention은 token들 사이에서 정보를 섞는 역할을 한다.  
즉 “이 token이 문장 안의 어떤 다른 token을 참고해야 하는가?”를 담당한다.

Position-wise FFN은 각 token의 hidden state를 개별적으로 가공하는 역할을 한다.  
즉 attention이 가져온 문맥 정보를 바탕으로 “이 token 표현을 어떻게 더 유용하게 바꿀까?”를 담당한다.

간단히 말하면:

Attention = token 간 정보 교환  
Position-wise FFN = token별 feature 변환

**설명**

Transformer block 안에는 크게 두 가지 중요한 계산이 있다.

첫 번째는 attention이다.

Attention은 token들이 서로를 보게 만든다. 예를 들어 문장이 있다고 하자.

“철수는 사과를 먹었다. 그것은 빨갰다.”

여기서 “그것”이라는 token은 혼자 보면 의미가 불명확하다. 하지만 attention을 통해 앞의 “사과”를 참고하면 “그것”이 사과를 가리킨다는 정보를 얻을 수 있다.

즉 attention은 문장 안에서 token들이 서로 관계를 맺고 정보를 주고받게 한다.

두 번째는 Position-wise FFN이다.

Attention이 여러 token의 정보를 섞어 왔다고 해서 일이 끝나는 것은 아니다. 섞어 온 정보를 각 token 내부에서 더 깊게 가공해야 한다.

Position-wise FFN은 각 token의 hidden state에 같은 작은 MLP block을 적용한다. 여기서 MLP는 linear layer와 activation function으로 이루어진 작은 neural network라고 보면 된다.

FFN의 기본 구조는 보통 다음과 같다.

`확장 → activation → 축소`

예를 들어 hidden dimension이 768이면, FFN 안에서 잠시 3072 같은 더 큰 차원으로 확장했다가 다시 768로 줄일 수 있다.

이 과정에서 token의 feature들이 더 복잡하게 조합된다.

중요한 점은 Position-wise FFN이 token끼리 직접 섞는 역할은 아니라는 것이다. Token 간 정보 mixing은 주로 attention이 한다. FFN은 각 token position에 독립적으로 적용되며, token 내부 feature를 더 풍부하게 변환한다.

**예시**

요리로 비유해 보자.

Attention은 여러 재료를 한 그릇에 모아 주는 과정과 비슷하다.

예를 들어 한 token이 다음 정보들을 attention으로 가져왔다고 하자.

토마토 정보  
치즈 정보  
빵 정보

하지만 재료를 모았다고 바로 요리가 완성되지는 않는다. 이제 자르고, 굽고, 간을 해야 한다.

이 가공 과정이 Position-wise FFN과 비슷하다.

숫자로 보면 더 작게 이해할 수 있다.

어떤 token의 hidden state가:

`x = [1, 2]`

라고 하자.

FFN의 첫 번째 linear layer가 이것을 3차원으로 확장한다.

`[1, 2] → [3, -1, 4]`

activation function이 음수 값을 0으로 만든다고 하자. ReLU라면:

`[3, -1, 4] → [3, 0, 4]`

그 다음 두 번째 linear layer가 다시 2차원으로 줄인다.

`[3, 0, 4] → [5, 1]`

즉 FFN은 token 하나의 표현을 더 넓게 펼쳐 보고, 중요한 패턴을 살린 뒤, 다시 원래 크기의 표현으로 정리한다.

**실전 연결**

실제 LLM에서 attention과 FFN은 서로 보완적인 역할을 한다.

Attention은 문맥을 가져온다. 예를 들어 어떤 단어가 문장 안에서 누구와 관련 있는지, 어떤 앞 단어를 참고해야 하는지를 찾는다.

FFN은 그 문맥 정보를 바탕으로 각 token의 representation을 가공한다. 품사, 의미, 문장 역할, 추론에 필요한 feature들이 hidden state 안에서 더 유용하게 조합되도록 돕는다.

또한 많은 Transformer 모델에서 parameter 수의 큰 부분은 attention보다 FFN에 들어가기도 한다. 그래서 FFN은 단순한 부가 장치가 아니라, LLM의 표현력과 모델 용량을 크게 담당하는 핵심 block이다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-15-day23.md
