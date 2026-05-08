# AI/ML Learning Review — Day 16 (2026-05-08)

## Source Metadata
- Lesson file: `/home/ubuntu/work/ai/learning/logs/2026-05-08-day16.md`
- Follow-up answer file: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-08_09-25-55.md`

## Lesson

# Day 16 - AI/ML 기초 학습

- Date: 2026-05-08
- Progress: 16/30
- Level: beginner-intermediate
- Milestone: 딥러닝 학습 기법과 CNN
- Milestone goal: 실제 딥러닝 학습을 안정화하는 방법과 CNN의 구조적 아이디어를 익힌다.

## Today's 3 concepts

1. 에폭, 이터레이션, 배치크기
2. BatchNorm과 내부 공변량 변화
3. Dropout과 확률적 정규화

---

## 1. 에폭, 이터레이션, 배치크기

### 한 줄 직관

딥러닝 학습은 “문제집 전체를 몇 번 풀었는가”와 “한 번에 몇 문제씩 보고 채점했는가”를 정해서, 조금씩 모델의 가중치(weight)를 고치는 과정이다.

여기서 문제집 전체를 한 번 다 보는 단위가 **epoch**, 한 번 가중치를 업데이트하는 단위가 **iteration**, 한 번에 묶어서 보는 데이터 개수가 **batch size**다.

### 개념 정의

**epoch**은 전체 training dataset을 모델이 한 번 모두 본 것을 뜻한다. 예를 들어 훈련 데이터가 이미지 1,000장이고 모델이 1,000장을 모두 한 번씩 학습에 사용했다면 1 epoch이 끝난 것이다.

**iteration**은 optimizer가 가중치를 한 번 업데이트하는 한 걸음을 뜻한다. 보통 딥러닝은 데이터 전체를 한 번에 넣지 않고 작은 묶음으로 나눈다. 이 작은 묶음을 **batch** 또는 더 정확히는 **mini-batch**라고 부른다. mini-batch 하나를 넣고 loss를 계산한 뒤 gradient를 구해서 optimizer가 한 번 업데이트하면 1 iteration이다.

**batch size**는 한 mini-batch에 들어가는 sample 수다. batch size가 32라면 한 번의 forward/backward pass에서 데이터 32개를 함께 처리한다.

**throughput**은 보통 “초당 몇 개의 sample을 처리하는가”를 뜻한다. 예를 들어 GPU가 1초에 이미지 800장을 학습에 사용한다면 throughput은 800 samples/sec라고 말할 수 있다.

### 왜 이런 개념이 필요한가

딥러닝 학습은 “데이터를 얼마나 자주 보여 줄지”와 “한 번에 얼마나 많이 보여 줄지”에 따라 학습 속도, 메모리 사용량, 성능이 크게 달라진다.

데이터 전체를 한 번에 넣으면 gradient가 안정적일 수 있지만, GPU memory가 부족할 수 있다. 반대로 데이터 1개씩만 넣으면 memory는 적게 쓰지만 gradient가 너무 흔들리고 GPU 병렬 처리 효율이 떨어질 수 있다. 그래서 실제 학습에서는 mini-batch 단위가 거의 표준이다.

LLM 학습에서도 이 개념은 매우 중요하다. 예를 들어 “batch size가 크다”는 것은 한 번의 update에 많은 token을 사용한다는 뜻이다. 많은 token으로 평균 loss를 계산하면 gradient noise가 줄어 안정적일 수 있지만, GPU memory가 많이 필요하다. 그래서 실제 대형 모델 학습에서는 batch size, sequence length, gradient accumulation을 함께 조절한다.

### 아주 쉬운 예시

훈련 데이터가 사과 사진 10장이라고 해 보자.

```text
전체 데이터 수 N = 10
batch size = 2
```

그러면 한 번에 사진 2장씩 모델에 넣는다.

```text
1번째 iteration: 사진 1, 2 → loss 계산 → weight 업데이트
2번째 iteration: 사진 3, 4 → loss 계산 → weight 업데이트
3번째 iteration: 사진 5, 6 → loss 계산 → weight 업데이트
4번째 iteration: 사진 7, 8 → loss 계산 → weight 업데이트
5번째 iteration: 사진 9, 10 → loss 계산 → weight 업데이트
```

사진 10장을 모두 봤으므로 여기까지가 **1 epoch**이다. 이 경우 1 epoch에는 5 iterations가 있다.

만약 3 epochs를 학습한다면 모델은 같은 10장 데이터 전체를 총 3번 반복해서 본다.

```text
1 epoch = 5 iterations
3 epochs = 15 iterations
```

즉 optimizer는 총 15번 weight를 업데이트한다.

### 개념 구조와 핵심 포인트

1. **dataset size**  
   전체 훈련 sample 수다. 예: 이미지 10,000장, 문장 100만 개, token 10억 개.

2. **batch size**  
   한 번에 모델에 들어가는 sample 수다. batch size가 32이면 입력 tensor의 첫 번째 차원이 보통 32가 된다. 예를 들어 이미지 batch는 `[32, 3, 224, 224]`처럼 표현될 수 있다. 여기서 32는 batch dimension이다.

3. **iteration**  
   batch 하나를 처리하고 optimizer가 한 번 update하는 단위다. forward pass로 예측을 만들고, loss를 계산하고, backward pass로 gradient를 구하고, optimizer step으로 weight를 바꾸는 과정이 한 iteration이다.

4. **epoch**  
   전체 training dataset을 한 번 다 사용한 단위다. `iterations per epoch`은 대략 `dataset size / batch size`로 계산한다.

5. **throughput**  
   학습 처리량이다. 같은 모델이라도 batch size를 키우면 GPU가 병렬 계산을 더 잘 활용해 throughput이 올라갈 수 있다. 하지만 너무 키우면 memory가 터지거나 generalization이 나빠질 수 있다.

핵심은 다음 관계다.

```text
데이터 전체 → batch 여러 개로 나눔 → batch 하나마다 iteration 1번 → 전체 batch를 다 돌면 epoch 1번
```

### 핵심 수학 포인트

가장 기본 관계는 다음과 같다.

```text
iterations per epoch = ceil(N / B)
```

- `N`: training sample 수
- `B`: batch size
- `ceil`: 나누어떨어지지 않으면 올림

예를 들어 데이터가 10개이고 batch size가 4라면:

```text
ceil(10 / 4) = 3
```

batch는 다음처럼 된다.

```text
batch 1: 4개
batch 2: 4개
batch 3: 2개
```

mini-batch loss는 보통 batch 안 sample loss의 평균이다.

```text
batch loss = (loss_1 + loss_2 + ... + loss_B) / B
```

예를 들어 batch size가 2이고 두 sample의 loss가 0.8, 0.4라면:

```text
batch loss = (0.8 + 0.4) / 2 = 0.6
```

모델은 이 평균 loss를 줄이는 방향으로 gradient를 계산한다. 즉 batch size는 “한 번의 gradient가 몇 개 sample의 평균 의견을 반영하는가”를 정한다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **epoch**: 전체 training dataset을 한 번 모두 사용한 학습 단위.
- **iteration**: optimizer가 한 번 weight를 업데이트하는 단위.
- **batch size**: 한 번에 처리하는 sample 수.
- **mini-batch**: 전체 데이터 중 일부를 묶은 작은 batch.
- **throughput**: 초당 처리 sample 수 또는 token 수. 학습 시스템의 처리량을 볼 때 중요하다.
- **optimizer step**: gradient를 이용해 weight를 실제로 바꾸는 한 번의 update.

### AI에서 어디에 쓰이는가

이미지 분류 모델, 추천 모델, Transformer, LLM 모두 mini-batch 학습을 사용한다. 예를 들어 Transformer에서 batch size가 8이고 sequence length가 512라면 한 iteration에서 대략 `8 × 512 = 4096` tokens를 처리한다. 이때 attention 계산은 sequence length와도 관련이 있기 때문에, batch size를 키우는 것은 단순히 sample 수만 늘리는 문제가 아니라 GPU memory와 계산량에도 영향을 준다.

실전에서는 batch size를 키우고 싶지만 memory가 부족한 경우가 많다. 이때 **gradient accumulation**을 쓴다. 예를 들어 실제 GPU에는 batch size 8만 들어가지만, 4번 gradient를 모은 뒤 한 번 optimizer step을 하면 효과적으로 batch size 32처럼 만들 수 있다.

### 헷갈리기 쉬운 포인트

- epoch은 update 횟수가 아니라 “전체 데이터를 몇 번 봤는가”다.
- iteration은 보통 “batch 하나를 처리하고 update 한 번”을 뜻한다.
- batch size를 키우면 항상 성능이 좋아지는 것은 아니다. gradient는 안정적일 수 있지만 memory가 늘고, 너무 큰 batch는 generalization이 나빠질 수 있다.
- throughput이 높다고 항상 최종 모델이 좋은 것은 아니다. throughput은 학습 속도 지표이고, 모델 성능은 validation loss나 accuracy 같은 지표로 따로 봐야 한다.
- 마지막 batch는 데이터 수가 딱 나누어떨어지지 않으면 더 작을 수 있다.

---

## 2. BatchNorm과 내부 공변량 변화

### 한 줄 직관

**BatchNorm(batch normalization)**은 layer 중간값들의 평균과 크기를 너무 들쭉날쭉하지 않게 맞춰서, 딥러닝 모델이 더 안정적으로 학습되도록 돕는 방법이다.

마치 여러 학생의 시험 점수가 과목마다 기준이 달라 비교하기 어려울 때, 각 과목 점수를 “평균에서 얼마나 떨어졌는지”로 바꿔 비교하기 쉽게 만드는 것과 비슷하다.

### 개념 정의

BatchNorm은 neural network의 어떤 layer 출력 또는 activation을 mini-batch 기준으로 normalize한 뒤, 다시 학습 가능한 scale과 shift를 적용하는 기법이다.

여기서 **normalization**은 숫자들의 평균과 분산을 일정한 기준으로 맞추는 것을 말한다. BatchNorm에서는 보통 mini-batch 안에서 각 feature의 평균을 0에 가깝게, variance를 1에 가깝게 만든다.

**internal covariate shift**는 원래 BatchNorm 논문에서 강조한 설명이다. 앞 layer의 weight가 계속 바뀌면 뒤 layer가 받는 입력 분포도 계속 바뀐다. 뒤 layer 입장에서는 “어제는 평균이 1인 입력을 받았는데 오늘은 평균이 10인 입력을 받는” 식으로 환경이 계속 바뀌는 셈이다. 이렇게 내부 activation 분포가 학습 중에 변하는 현상을 internal covariate shift라고 부른다.

현대적으로는 BatchNorm의 효과를 internal covariate shift 하나로만 설명하지는 않는다. 하지만 초보자에게는 “중간 숫자들의 scale을 안정시켜 gradient와 optimization을 편하게 만든다”라고 이해하면 좋다.

### 왜 이런 개념이 필요한가

딥러닝 모델은 layer가 깊어질수록 중간 activation의 값 크기가 커지거나 작아질 수 있다. 어떤 layer의 출력이 갑자기 너무 커지면 다음 layer는 큰 숫자를 받아서 activation이 포화되거나 gradient가 불안정해질 수 있다. 반대로 값이 너무 작아지면 signal이 약해질 수 있다.

예를 들어 어떤 layer가 처음에는 `[1, 2, 3]` 정도의 값을 다음 layer에 보냈는데, 학습이 진행되면서 `[100, 200, 300]` 같은 값을 보내기 시작하면 뒤 layer는 계속 바뀌는 입력 환경에 적응해야 한다. 모델은 정답을 배우기도 바쁜데, 내부 숫자 scale 변화까지 따라가야 하므로 학습이 어려워진다.

BatchNorm은 중간 activation을 normalize해서 이런 scale 문제를 줄인다. 그래서 더 큰 learning rate를 쓸 수 있거나, 학습이 더 빠르고 안정적으로 진행되는 경우가 많다. 특히 CNN에서는 BatchNorm이 오랫동안 매우 중요한 기본 구성요소였다.

### 아주 쉬운 예시

어떤 layer가 mini-batch 안에서 한 feature 값으로 다음 숫자 3개를 만들었다고 하자.

```text
x = [2, 4, 6]
```

평균은 4다.

```text
mean = (2 + 4 + 6) / 3 = 4
```

각 값에서 평균을 빼면:

```text
[-2, 0, 2]
```

분산은 대략 2.67이고, 표준편차는 대략 1.63이다. 그래서 표준편차로 나누면:

```text
normalized ≈ [-1.22, 0, 1.22]
```

처음 숫자 `[2, 4, 6]`은 평균이 4였지만, normalize 후에는 평균이 거의 0이고 크기도 적당해졌다. 이제 다음 layer는 너무 큰 값이나 너무 한쪽으로 치우친 값을 덜 받는다.

그런데 항상 평균 0, variance 1로만 고정하면 모델의 표현력이 줄어들 수 있다. 그래서 BatchNorm은 마지막에 학습 가능한 두 값 `gamma`와 `beta`를 둔다.

```text
y = gamma × normalized + beta
```

모델이 필요하면 다시 scale을 키우거나 평균을 옮길 수 있게 하는 것이다.

### 개념 구조와 핵심 포인트

BatchNorm의 흐름은 다음과 같다.

1. **mini-batch activation을 모은다**  
   예를 들어 어떤 layer의 출력 tensor가 `[batch, features]` 모양이라면, batch 안 sample들을 기준으로 feature별 평균과 variance를 계산한다.

2. **평균을 뺀다**  
   각 feature 값을 batch 평균에서 얼마나 떨어져 있는 값으로 바꾼다.

3. **표준편차로 나눈다**  
   값의 scale을 맞춘다. 너무 큰 feature와 작은 feature가 뒤섞여 있으면 optimization이 어려울 수 있기 때문이다.

4. **gamma와 beta를 적용한다**  
   normalize만 하면 표현력이 제한될 수 있으므로, 모델이 학습으로 다시 적절한 scale과 shift를 선택하게 한다.

5. **training과 inference가 다르다**  
   학습 중에는 현재 mini-batch의 평균과 variance를 사용한다. 추론(inference) 때는 batch가 1개일 수도 있고 매번 통계가 흔들리면 안 되므로, 학습 중 누적한 running mean과 running variance를 사용한다.

CNN에서는 보통 channel별로 BatchNorm을 적용한다. 예를 들어 activation이 `[batch, channels, height, width]` 모양이면, 각 channel마다 평균과 variance를 계산해서 channel scale을 안정화한다.

### 핵심 수학 포인트

BatchNorm의 기본 수식은 다음과 같다.

```text
mu_B = batch mean
sigma_B^2 = batch variance
x_hat = (x - mu_B) / sqrt(sigma_B^2 + epsilon)
y = gamma × x_hat + beta
```

- `mu_B`: mini-batch 평균
- `sigma_B^2`: mini-batch variance
- `epsilon`: 0으로 나누는 것을 막기 위한 아주 작은 수
- `gamma`: 학습 가능한 scale
- `beta`: 학습 가능한 shift

가장 중요한 직관은 이것이다.

```text
큰 값, 작은 값, 치우친 값 → 기준이 맞춰진 값 → 필요하면 gamma/beta로 다시 조정
```

수학적으로 BatchNorm은 activation의 scale을 조절한다. gradient는 layer를 거꾸로 지나가며 전달되는데, 중간 activation scale이 너무 불안정하면 gradient도 불안정해질 수 있다. BatchNorm은 이 scale 문제를 완화해 optimizer가 더 예측 가능한 환경에서 weight를 업데이트하게 돕는다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **batch normalization**: mini-batch 통계로 activation을 normalize하고 학습 가능한 scale/shift를 적용하는 기법.
- **normalization**: 숫자의 평균, variance, scale을 일정 기준에 맞추는 과정.
- **internal covariate shift**: 앞 layer 변화 때문에 뒤 layer가 받는 내부 입력 분포가 학습 중 계속 바뀌는 현상.
- **activation**: layer를 통과한 중간 출력값.
- **running mean / running variance**: inference 때 쓰기 위해 학습 중 누적해 둔 평균과 variance.
- **gamma / beta**: BatchNorm에서 normalize된 값을 다시 조정하는 학습 가능한 scale과 shift.

### AI에서 어디에 쓰이는가

BatchNorm은 CNN에서 특히 자주 쓰였다. ResNet 같은 이미지 모델에서 convolution layer 뒤에 BatchNorm을 넣으면 학습이 훨씬 안정적이고 빠르게 되는 경우가 많다.

Transformer와 LLM에서는 BatchNorm보다 **LayerNorm(layer normalization)**이 더 흔하다. 이유는 자연어 모델에서는 sequence length, batch 구성, autoregressive generation 때문에 batch 통계에 의존하는 방식이 불편할 수 있기 때문이다. 그래도 BatchNorm을 이해하면 “왜 normalization이 딥러닝 안정화에 중요한가”를 이해하는 데 큰 도움이 된다.

embedding이나 hidden state 관점에서도 normalization은 중요하다. 모델 내부의 vector 값들이 너무 커지거나 작아지면 attention score, feed-forward layer 출력, gradient scale이 불안정해질 수 있다. 그래서 현대 딥러닝은 BatchNorm, LayerNorm, RMSNorm 같은 normalization 계열 기법을 매우 많이 사용한다.

### 헷갈리기 쉬운 포인트

- BatchNorm은 입력 데이터 자체만 normalize하는 것이 아니라, 모델 중간 activation에도 적용된다.
- BatchNorm은 training과 inference 동작이 다르다. 이 차이를 모르면 모델 평가 때 결과가 이상해질 수 있다.
- BatchNorm이 항상 최고의 선택은 아니다. batch size가 너무 작으면 batch 통계가 흔들릴 수 있다.
- internal covariate shift는 BatchNorm의 역사적 설명으로 중요하지만, BatchNorm의 모든 효과를 완벽히 설명한다고 보기는 어렵다.
- BatchNorm은 regularization 효과도 약간 줄 수 있지만, 주된 목적은 학습 안정화와 optimization 개선이다.

---

## 3. Dropout과 확률적 정규화

### 한 줄 직관

**Dropout**은 학습 중에 neural network의 일부 neuron을 일부러 랜덤하게 꺼서, 모델이 특정 neuron 몇 개에만 과하게 의존하지 않도록 만드는 방법이다.

팀 프로젝트로 비유하면, 매번 같은 한 사람에게만 일을 맡기지 않고 랜덤하게 몇 명을 쉬게 하면서 나머지 팀원들도 일을 할 수 있게 훈련하는 것과 비슷하다.

### 개념 정의

Dropout은 training 중 activation의 일부를 확률적으로 0으로 만드는 **regularization** 기법이다. regularization은 모델이 training data를 너무 외워서 새로운 데이터에 약해지는 overfitting을 줄이기 위한 방법을 말한다.

예를 들어 hidden layer에 neuron이 100개 있고 dropout rate가 0.5라면, 학습 중 매 iteration마다 평균적으로 50개 neuron의 출력이 0이 된다. 어떤 neuron이 꺼질지는 매번 랜덤이다.

Dropout은 “이 feature가 없더라도 다른 feature로도 예측할 수 있게” 모델을 훈련시킨다. 그래서 여러 neuron이 서로 협력하되, 특정 조합에 지나치게 고정되지 않게 만든다.

### 왜 이런 개념이 필요한가

딥러닝 모델은 parameter가 많다. parameter가 많으면 복잡한 패턴을 잘 배울 수 있지만, training data의 우연한 노이즈까지 외울 위험도 커진다.

예를 들어 고양이와 강아지 사진을 분류하는 모델이 있다고 하자. training data의 고양이 사진 대부분이 흰 배경이고 강아지 사진 대부분이 잔디 배경이라면, 모델은 “고양이의 귀와 수염”을 배우기보다 “배경이 흰색이면 고양이”라는 쉬운 편법을 배울 수 있다. 이것이 overfitting 또는 spurious correlation 문제다.

Dropout은 학습 중 일부 activation을 랜덤하게 없애서 모델이 한두 개 단서에만 매달리지 않게 한다. 어떤 neuron이 언제 꺼질지 모르므로, 모델은 더 robust한 representation을 만들려고 한다.

LLM에서도 dropout은 embedding dropout, attention dropout, residual dropout 같은 형태로 쓰일 수 있다. 특히 작은 데이터로 fine-tuning할 때는 overfitting을 줄이는 데 도움이 될 수 있다.

### 아주 쉬운 예시

어떤 hidden layer의 출력이 다음과 같다고 하자.

```text
h = [2, 1, 3]
```

dropout rate가 0.5라면 각 값을 50% 확률로 끈다. 이번 iteration에서 랜덤 mask가 다음처럼 나왔다고 하자.

```text
mask = [1, 0, 1]
```

그러면 두 번째 neuron은 꺼진다.

단순히 곱하면:

```text
h × mask = [2, 0, 3]
```

실제 구현에서는 보통 **inverted dropout**을 사용한다. keep probability가 0.5이면 남은 값을 `1 / 0.5 = 2`배 해서 평균 크기를 유지한다.

```text
h_dropout = [2, 0, 3] / 0.5 = [4, 0, 6]
```

왜 2배를 할까? 학습 때 절반을 꺼 버리면 전체 activation 평균이 줄어들 수 있다. 남은 neuron 값을 키워 두면 inference 때 dropout을 끄더라도 activation scale이 크게 달라지지 않는다.

추론(inference) 때는 dropout을 적용하지 않는다. 모델이 실제로 예측할 때는 모든 neuron을 사용한다.

### 개념 구조와 핵심 포인트

Dropout의 구조는 다음과 같다.

1. **training 때만 랜덤 mask 생성**  
   각 neuron 또는 activation 위치마다 “살릴지, 끌지”를 랜덤하게 정한다.

2. **꺼진 activation은 0이 됨**  
   꺼진 neuron은 이번 iteration에서 다음 layer로 정보를 보내지 않는다.

3. **남은 activation은 scale 조정**  
   inverted dropout에서는 남은 값을 keep probability로 나누어 평균 scale을 맞춘다.

4. **매 iteration마다 다른 network처럼 학습**  
   매번 다른 neuron 조합이 살아남기 때문에, 모델은 하나의 고정된 network가 아니라 많은 작은 sub-network를 번갈아 학습하는 효과를 낸다.

5. **inference 때는 dropout off**  
   평가나 실제 서비스에서는 모든 neuron을 사용한다. PyTorch에서는 `model.train()`일 때 dropout이 켜지고, `model.eval()`일 때 dropout이 꺼진다.

Dropout의 중요한 효과는 **co-adaptation**을 줄이는 것이다. co-adaptation은 여러 neuron이 “나는 이 neuron이 항상 이 feature를 줄 거야”라고 지나치게 서로 의존하는 현상이라고 생각하면 된다. Dropout은 그런 의존을 깨뜨린다.

### 핵심 수학 포인트

Dropout은 랜덤 mask를 곱하는 방식으로 표현할 수 있다.

```text
m_i ~ Bernoulli(q)
h'_i = (m_i × h_i) / q
```

- `h_i`: 원래 activation
- `m_i`: 0 또는 1인 랜덤 mask
- `q`: keep probability, 즉 neuron을 살릴 확률
- `dropout rate = 1 - q`

예를 들어 dropout rate가 0.2라면 keep probability는 0.8이다.

```text
q = 0.8
평균적으로 neuron 80%는 살아 있고 20%는 꺼진다.
```

inverted dropout에서 `/ q`를 하는 이유는 activation의 기대값을 유지하기 위해서다. 아주 단순하게 activation 하나가 10이고 q가 0.5라고 하자.

```text
50% 확률로 0
50% 확률로 10 / 0.5 = 20
기대값 = 0.5 × 0 + 0.5 × 20 = 10
```

즉 평균적으로는 원래 activation 크기 10을 유지한다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **dropout**: training 중 activation 일부를 랜덤하게 0으로 만드는 regularization 기법.
- **regularization**: overfitting을 줄이고 generalization을 높이기 위한 제약 또는 학습 기법.
- **ensemble effect**: 여러 모델을 함께 쓰는 것과 비슷한 효과. Dropout은 매번 다른 sub-network를 학습하므로 약한 ensemble 효과가 있다고 볼 수 있다.
- **dropout rate**: activation을 끌 확률.
- **keep probability**: activation을 살릴 확률.
- **co-adaptation**: neuron들이 서로에게 지나치게 의존하는 현상.
- **inverted dropout**: training 때 남은 activation을 keep probability로 나누어 inference 때 별도 scale 조정이 필요 없게 하는 방식.

### AI에서 어디에 쓰이는가

Dropout은 MLP, CNN, Transformer 등 여러 neural network에서 쓰인다. 이미지 모델에서는 fully connected layer나 convolution feature에 적용할 수 있고, Transformer에서는 attention weight나 feed-forward output, residual connection 주변에 쓰일 수 있다.

LLM pretraining에서는 모델 크기, 데이터 크기, architecture에 따라 dropout을 적게 쓰거나 아예 줄이는 경우도 있다. 큰 데이터로 매우 오래 학습하는 대형 모델에서는 dropout보다 data scale, weight decay, learning rate schedule 같은 요소가 더 중요할 때도 있다. 하지만 작은 dataset으로 fine-tuning할 때는 dropout이 overfitting을 줄이는 실용적인 도구가 될 수 있다.

hidden state 관점에서 보면 Dropout은 일부 hidden feature를 랜덤하게 제거한다. 그래서 모델은 “이 feature 하나가 없으면 망하는 representation”이 아니라, 여러 feature가 나눠서 정보를 담는 representation을 만들도록 압박받는다.

### 헷갈리기 쉬운 포인트

- Dropout은 training 때만 적용하고 inference 때는 꺼야 한다.
- dropout rate가 높을수록 항상 좋은 것은 아니다. 너무 많이 끄면 모델이 충분히 배우지 못한다.
- Dropout은 overfitting을 줄이는 방법이지, underfitting을 해결하는 방법은 아니다.
- BatchNorm과 Dropout을 함께 쓸 때는 위치와 상황에 따라 효과가 달라질 수 있다. BatchNorm은 batch 통계를 쓰고 Dropout은 activation을 랜덤하게 바꾸므로 조합이 항상 단순하지 않다.
- Dropout의 ensemble effect는 진짜로 독립 모델 여러 개를 학습해서 평균내는 것과 완전히 같지는 않다. 다만 매번 다른 sub-network를 학습한다는 직관이 도움이 된다.

---

## 복습 질문 3개

1. 데이터가 100개이고 batch size가 20이면 1 epoch에는 몇 iterations가 있을까? 그리고 5 epochs를 학습하면 optimizer step은 총 몇 번일까?
2. BatchNorm에서 training 때는 mini-batch 평균과 variance를 쓰지만 inference 때는 running mean과 running variance를 쓰는 이유는 무엇일까?
3. Dropout은 왜 training 때 일부 neuron을 랜덤하게 끄고, inference 때는 끄지 않을까?

## 오늘의 한 줄 요약

딥러닝을 안정적으로 학습하려면 데이터를 어떤 단위로 반복할지(epoch, iteration, batch size), 중간 activation scale을 어떻게 안정화할지(BatchNorm), overfitting을 어떻게 줄일지(Dropout)를 함께 이해해야 한다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 16/30]

오늘은 딥러닝 학습 단위, BatchNorm, Dropout을 실제 학습 상황에 연결해서 다시 확인해 볼게요.

### 1. 데이터가 100개이고 batch size가 20이면 1 epoch에는 몇 iterations가 있을까? 그리고 5 epochs를 학습하면 optimizer step은 총 몇 번일까?

**정답**

1 epoch에는 **5 iterations**가 있습니다.

5 epochs를 학습하면 optimizer step은 총 **25번** 일어납니다.

계산은 이렇게 됩니다.

```text
iterations per epoch = 데이터 개수 / batch size
                     = 100 / 20
                     = 5

총 optimizer step 수 = iterations per epoch × epochs
                    = 5 × 5
                    = 25
```

**설명**

**epoch**은 전체 training dataset을 모델이 한 번 모두 본 단위입니다.  
즉 데이터가 100개라면, 모델이 이 100개를 전부 한 번 학습에 사용했을 때 1 epoch이 끝납니다.

**batch size**는 한 번에 모델에 넣는 데이터 개수입니다.  
batch size가 20이라는 말은, 데이터 100개를 한 번에 다 넣지 않고 20개씩 나눠서 넣는다는 뜻입니다.

**iteration**은 batch 하나를 처리하고, loss function으로 오차를 계산한 뒤, gradient를 이용해 optimizer가 weight를 한 번 업데이트하는 단위입니다.

따라서 데이터 100개를 20개씩 나누면 batch가 5개 생깁니다.

```text
batch 1: 데이터 20개
batch 2: 데이터 20개
batch 3: 데이터 20개
batch 4: 데이터 20개
batch 5: 데이터 20개
```

batch 하나마다 optimizer step이 한 번 일어나므로, 1 epoch에는 5번의 update가 있습니다.

그리고 5 epochs는 이 전체 과정을 5번 반복하는 것이므로,

```text
1 epoch에 5번 update
5 epochs면 5 × 5 = 25번 update
```

가 됩니다.

**예시**

문제집에 문제가 100개 있다고 생각해 봅시다.  
한 번에 20문제씩 풀고 채점한다고 하면, 문제집 전체를 다 풀려면 5묶음이 필요합니다.

```text
20문제씩 5번 풀면 총 100문제
```

문제집 전체를 한 번 다 푼 것이 1 epoch입니다.  
이 문제집을 총 5번 반복해서 풀면, 채점하고 고치는 과정은 총 25번 일어납니다.

**실전 연결**

실제 딥러닝 학습 로그에서 `epoch`, `step`, `iteration`은 매우 자주 나옵니다. 예를 들어 LLM fine-tuning을 할 때 “현재 3 epoch 중 2 epoch 진행 중, global step 1200” 같은 로그를 보게 됩니다. 이때 step은 보통 optimizer update 횟수와 연결됩니다. batch size를 바꾸면 1 epoch 안의 iteration 수가 달라지고, 이는 학습 시간, GPU memory 사용량, gradient 안정성에 직접 영향을 줍니다.

---

### 2. BatchNorm에서 training 때는 mini-batch 평균과 variance를 쓰지만 inference 때는 running mean과 running variance를 쓰는 이유는 무엇일까?

**정답**

training 때는 모델이 학습 중이므로 현재 mini-batch의 평균과 variance를 사용해 activation을 normalize합니다.

하지만 inference 때는 예측 결과가 안정적이어야 하므로, 매번 들어오는 batch의 통계에 의존하지 않고 학습 중 누적해 둔 **running mean**과 **running variance**를 사용합니다.

즉 핵심은 이것입니다.

```text
training: 현재 batch 통계 사용
inference: 학습 중 누적한 안정적인 통계 사용
```

**설명**

**BatchNorm(batch normalization)**은 layer 중간의 activation 값을 너무 크거나 작지 않게 맞춰 주는 방법입니다. 여기서 activation은 neural network의 중간 layer가 만들어 낸 출력값이라고 생각하면 됩니다.

학습 중에는 여러 sample이 mini-batch로 들어옵니다. BatchNorm은 이 mini-batch 안에서 평균과 variance를 계산합니다.

예를 들어 어떤 feature 값이 batch 안에서 다음과 같다면,

```text
[2, 4, 6]
```

평균은 4입니다. BatchNorm은 각 값을 평균에서 얼마나 떨어져 있는지로 바꾸고, scale도 적당히 맞춥니다. 이렇게 하면 뒤 layer가 너무 들쭉날쭉한 숫자를 받지 않아 학습이 안정됩니다.

그런데 inference, 즉 실제 예측 상황에서는 문제가 생길 수 있습니다.

예를 들어 서비스에 이미지를 한 장씩 넣어 예측한다고 해 봅시다. batch size가 1이면 평균과 variance를 제대로 계산하기 어렵습니다. 또 어떤 batch에는 밝은 이미지가 많고, 어떤 batch에는 어두운 이미지가 많다면 batch 통계가 계속 흔들릴 수 있습니다. 그러면 같은 입력도 주변 batch 구성에 따라 예측이 달라질 위험이 있습니다.

그래서 inference 때는 현재 batch의 평균과 variance를 쓰지 않습니다. 대신 training 중에 조금씩 누적해 둔 running mean과 running variance를 사용합니다. 이 값들은 “학습 데이터 전체에서 대략 이 feature는 평균과 분산이 이 정도였다”라는 안정적인 기준 역할을 합니다.

**예시**

학생 시험 점수를 정규화한다고 생각해 봅시다.

training 때는 매번 한 반의 학생 점수를 보고 평균과 분산을 계산합니다.

```text
이번 mini-batch 학생 점수: [60, 70, 80]
평균: 70
```

학습 중에는 이런 식으로 현재 묶음의 통계를 써도 괜찮습니다. 오히려 이 통계를 이용해서 모델이 안정적으로 배우게 됩니다.

하지만 실제 평가 때 학생 한 명만 들어왔다고 해 봅시다.

```text
학생 점수: [75]
```

한 명만 가지고 평균과 분산을 계산하면 기준이 너무 불안정합니다. 그래서 학습 중 여러 반을 보며 누적해 둔 평균, 예를 들어 “전체적으로 평균은 68 정도였다” 같은 값을 사용하는 것이 더 안정적입니다.

**실전 연결**

CNN 모델에서 BatchNorm은 ResNet 같은 구조에 자주 들어갑니다. 이때 PyTorch에서는 `model.train()` 상태에서는 mini-batch 통계를 사용하고, `model.eval()` 상태에서는 running mean과 running variance를 사용합니다. 만약 평가할 때 `model.eval()`을 호출하지 않으면 BatchNorm이 계속 training 방식으로 동작해서 validation accuracy나 inference 결과가 이상해질 수 있습니다. 실제 모델 평가와 배포에서 매우 중요한 포인트입니다.

---

### 3. Dropout은 왜 training 때 일부 neuron을 랜덤하게 끄고, inference 때는 끄지 않을까?

**정답**

Dropout은 training 때 일부 neuron을 랜덤하게 꺼서 모델이 특정 neuron이나 feature에 지나치게 의존하지 않도록 만듭니다. 이것은 overfitting을 줄이기 위한 regularization 방법입니다.

하지만 inference 때는 실제 예측을 해야 하므로 neuron을 끄지 않고 전체 network를 사용합니다. 그래야 모델이 학습한 모든 정보를 활용해 안정적으로 예측할 수 있습니다.

정리하면 다음과 같습니다.

```text
training: 일부 neuron을 랜덤하게 끔 → 과의존 방지, overfitting 완화
inference: neuron을 끄지 않음 → 전체 모델로 안정적인 예측
```

**설명**

**Dropout**은 training 중에 activation 일부를 확률적으로 0으로 만드는 기법입니다. 어떤 neuron이 꺼질지는 매 iteration마다 랜덤하게 정해집니다.

이 방법의 목적은 모델이 한두 개의 강한 단서에만 의존하지 않게 하는 것입니다.

예를 들어 고양이와 강아지를 분류하는 모델이 있다고 해 봅시다. 만약 훈련 데이터에서 고양이 사진은 대부분 흰 배경이고, 강아지 사진은 대부분 잔디 배경이라면 모델은 동물의 모양보다 배경색을 외울 수 있습니다. 이런 식으로 training data의 우연한 특징까지 외우는 것을 **overfitting**이라고 합니다.

Dropout은 학습 중 일부 neuron을 랜덤하게 꺼 버립니다. 그러면 모델 입장에서는 “항상 이 neuron이 중요한 정보를 줄 거야”라고 믿을 수 없습니다. 따라서 여러 feature를 나눠서 사용하고, 더 robust한 representation을 만들도록 학습됩니다.

하지만 inference 때도 neuron을 랜덤하게 꺼 버리면 예측이 매번 흔들릴 수 있습니다. 같은 사진을 넣었는데 어떤 때는 고양이, 어떤 때는 강아지처럼 결과가 달라질 수 있습니다. 실제 서비스에서는 안정적인 예측이 필요하므로 inference 때는 Dropout을 끕니다.

**예시**

어떤 hidden layer의 출력이 다음과 같다고 해 봅시다.

```text
h = [2, 1, 3]
```

training 때 dropout rate가 0.5라면, 각 neuron은 50% 확률로 꺼질 수 있습니다. 이번 iteration에서 mask가 이렇게 나왔다고 해 봅시다.

```text
mask = [1, 0, 1]
```

그러면 두 번째 neuron이 꺼집니다.

```text
h × mask = [2, 0, 3]
```

이번 학습에서는 두 번째 정보 없이도 정답을 맞히도록 훈련됩니다. 다음 iteration에서는 또 다른 neuron이 꺼질 수 있습니다. 이렇게 모델은 매번 조금 다른 작은 network처럼 학습합니다.

하지만 inference 때는 다음처럼 모든 neuron을 사용합니다.

```text
h = [2, 1, 3]
```

실제 예측에서는 모델이 가진 정보를 최대한 활용해야 하기 때문입니다.

**실전 연결**

Dropout은 MLP, CNN, Transformer에서 overfitting을 줄이는 데 사용됩니다. LLM에서는 attention dropout, residual dropout, embedding dropout 같은 형태로 쓰일 수 있습니다. 특히 작은 dataset으로 fine-tuning할 때 모델이 데이터를 너무 외우는 것을 막는 데 도움이 됩니다. PyTorch에서는 `model.train()`일 때 Dropout이 켜지고, `model.eval()`일 때 Dropout이 꺼집니다. 따라서 평가나 추론 전에 `model.eval()`을 호출하는 것은 BatchNorm뿐 아니라 Dropout 때문에도 중요합니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-08-day16.md
