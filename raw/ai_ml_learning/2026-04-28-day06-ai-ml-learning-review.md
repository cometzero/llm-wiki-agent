# AI/ML Learning Review — 2026-04-28 Day 06

## Lesson Source

Source file: `/home/ubuntu/work/ai/learning/logs/2026-04-28-day06.md`

# Day 06 - AI/ML 기초 학습

- Date: 2026-04-28
- Progress: 6/30
- Level: beginner-intermediate
- Milestone: 미분과 최적화의 핵심
- Milestone goal: 학습이 왜 최적화 문제인지 이해하고 gradient 기반 학습의 기초를 다진다.

## Today's 3 concepts

1. 확률적 경사하강법과 미니배치
2. 학습률, 수렴, 불안정성
3. Momentum, Adam 같은 옵티마이저

---

## 1. 확률적 경사하강법과 미니배치

### 한 줄 직관

모든 문제를 한 번에 다 보고 고치면 정확하지만 느리고, 몇 문제만 뽑아서 대략 방향을 잡아 조금씩 고치는 방법이 확률적 경사하강법(SGD)과 mini-batch 학습이다.

### 개념 정의

신경망 학습은 보통 loss를 줄이는 과정이다. loss는 모델의 예측이 정답과 얼마나 다른지를 숫자로 나타낸 값이다. 예를 들어 정답이 10인데 모델이 7이라고 예측하면 오차가 있고, 이 오차를 loss로 계산한다.

경사하강법(gradient descent)은 loss가 줄어드는 방향으로 parameter를 조금씩 움직이는 방법이다. 여기서 parameter는 모델 안의 weight와 bias 같은 조절 가능한 숫자들이다.

전체 데이터셋을 모두 사용해서 gradient를 계산하면 batch gradient descent라고 볼 수 있다. 반대로 데이터 1개 또는 일부만 사용해서 gradient를 대략 추정하고 업데이트하는 방법을 확률적 경사하강법(SGD, Stochastic Gradient Descent)이라고 한다. 실제 딥러닝에서는 데이터 1개만 쓰기보다 보통 16개, 32개, 128개처럼 작은 묶음인 mini-batch를 사용한다.

즉, mini-batch SGD는 “전체 데이터의 평균 gradient를 매번 정확히 계산하지 않고, 작은 묶음으로 그럴듯한 방향을 추정해서 빠르게 여러 번 업데이트하는 방법”이다.

### 왜 이런 개념이 필요한가

AI 모델은 데이터가 매우 많다. 이미지 모델은 수백만 장의 이미지로 학습할 수 있고, LLM은 엄청난 양의 text token으로 학습한다. 매번 전체 데이터를 다 보고 gradient를 계산하면 한 번 업데이트하는 데 너무 오래 걸린다.

예를 들어 데이터가 1,000,000개 있다고 하자. 전체 데이터를 모두 보고 한 번 업데이트하면 업데이트 1번이 매우 비싸다. 하지만 mini-batch size를 100으로 하면 100개만 보고 한 번 업데이트할 수 있다. 한 번의 방향은 조금 덜 정확하지만, 훨씬 자주 움직일 수 있다.

또 하나 중요한 이유는 약간의 randomness가 학습에 도움이 될 때가 있다는 점이다. 전체 데이터를 기준으로 너무 매끈하게만 움직이면 어떤 지점에 갇힐 수 있다. mini-batch의 작은 흔들림은 모델이 더 좋은 지점을 찾도록 도와줄 때가 있다. 물론 흔들림이 너무 크면 학습이 불안정해질 수 있다.

### 아주 쉬운 예시

학생이 수학 문제집 1,000문제를 풀고 있다고 하자.

- 방법 A: 1,000문제를 전부 채점한 뒤, 약한 단원을 한 번에 분석해서 공부법을 바꾼다.
- 방법 B: 20문제씩 풀고 채점한 뒤, 바로 공부 방향을 조금씩 수정한다.

방법 A는 전체 판단은 정확하지만 느리다. 방법 B는 판단이 조금 흔들릴 수 있지만 빠르게 피드백을 받을 수 있다.

숫자로 보면 더 쉽다. 어떤 모델의 parameter가 하나만 있고, 우리가 loss를 줄이려고 한다고 하자. 전체 데이터 4개의 gradient가 다음과 같다고 해보자.

- 데이터 1의 gradient: 2
- 데이터 2의 gradient: 4
- 데이터 3의 gradient: 6
- 데이터 4의 gradient: 8

전체 평균 gradient는 (2 + 4 + 6 + 8) / 4 = 5이다. 전체 데이터를 쓰면 parameter를 gradient 5 방향 기준으로 업데이트한다.

그런데 mini-batch로 데이터 1, 2만 뽑으면 평균 gradient는 (2 + 4) / 2 = 3이다. 데이터 3, 4만 뽑으면 평균 gradient는 (6 + 8) / 2 = 7이다. 둘 다 전체 평균 5와 정확히 같지는 않지만, 여러 mini-batch를 반복해서 보면 평균적으로는 전체 방향을 따라가게 된다.

이처럼 mini-batch gradient는 전체 gradient의 대략적인 추정치이다. 이 추정치를 stochastic estimate라고 부른다.

### 개념 구조와 핵심 포인트

1. 전체 데이터 gradient는 가장 안정적인 방향이다.  
   전체 데이터셋의 loss 평균을 기준으로 gradient를 구하면 방향이 비교적 정확하다. 하지만 계산량이 너무 크다.

2. SGD는 일부 데이터로 gradient를 추정한다.  
   stochastic이라는 말은 “확률적인, 무작위성이 있는”이라는 뜻이다. 매번 어떤 데이터가 mini-batch에 들어가느냐에 따라 gradient가 조금 달라진다.

3. mini-batch는 속도와 안정성 사이의 타협이다.  
   batch size가 너무 작으면 gradient가 많이 흔들린다. batch size가 너무 크면 한 번 업데이트가 비싸고, update 횟수가 줄어들 수 있다.

4. variance가 중요하다.  
   variance는 값들이 얼마나 흔들리는지를 나타내는 개념이다. mini-batch gradient의 variance가 크면 업데이트 방향이 매번 크게 달라져 학습이 불안정할 수 있다.

5. GPU/TPU에서는 mini-batch가 특히 중요하다.  
   딥러닝 연산은 tensor 단위로 병렬 처리된다. 예를 들어 입력 tensor shape이 `[32, 128]`이라면 batch size 32, feature 또는 token 관련 길이 128일 수 있다. mini-batch는 하드웨어를 효율적으로 쓰게 해준다.

### 핵심 수학 포인트

전체 데이터셋의 평균 loss를 다음처럼 생각할 수 있다.

\[
L(\theta) = \frac{1}{N}\sum_{i=1}^{N} L_i(\theta)
\]

여기서 \(\theta\)는 모델 parameter 전체를 뜻한다. \(L_i(\theta)\)는 i번째 데이터에 대한 loss이다.

전체 gradient는 모든 데이터의 gradient 평균이다.

\[
\nabla L(\theta) = \frac{1}{N}\sum_{i=1}^{N} \nabla L_i(\theta)
\]

mini-batch는 전체 \(N\)개 중 일부 \(B\)개만 뽑아 평균을 낸다.

\[
\nabla L_B(\theta) = \frac{1}{|B|}\sum_{i \in B} \nabla L_i(\theta)
\]

이 값은 전체 gradient와 완전히 같지는 않다. 하지만 mini-batch가 무작위로 잘 뽑혔다면, 평균적으로는 전체 gradient를 향하는 추정치가 된다. 여기서 “평균적으로 맞다”는 감각이 stochastic estimate의 핵심이다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- SGD: Stochastic Gradient Descent. 일부 데이터로 gradient를 추정해 parameter를 업데이트하는 방법.
- mini-batch: 한 번의 업데이트에 사용하는 작은 데이터 묶음. 예: 32개 문장, 128개 이미지.
- stochastic estimate: 무작위로 뽑은 일부 데이터로 전체 값을 대략 추정한 값.
- variance: 추정값이 얼마나 흔들리는지를 나타내는 정도. mini-batch gradient의 variance가 크면 학습이 더 요동친다.
- batch size: mini-batch 안에 들어가는 데이터 개수.
- epoch: 전체 데이터셋을 한 번 다 학습에 사용한 단위.

### AI에서 어디에 쓰이는가

거의 모든 딥러닝 학습에서 mini-batch 기반 최적화를 사용한다. 이미지 분류 모델, 추천 모델, 음성 인식 모델, LLM 학습 모두 mini-batch를 사용한다.

LLM을 예로 들면, 모델은 수많은 token sequence를 본다. 한 번에 전체 인터넷 text를 다 보고 업데이트할 수는 없다. 대신 여러 sequence를 mini-batch로 묶어 loss를 계산한다. 예를 들어 batch size가 8이고 sequence length가 2048이면, 입력 token tensor는 대략 `[8, 2048]` 형태가 될 수 있다. 모델은 이 묶음에서 다음 token 예측 loss를 계산하고, gradient를 구한 뒤 optimizer가 parameter를 업데이트한다.

embedding 학습에서도 마찬가지다. 단어, 문장, 상품, 사용자 등을 vector로 바꾸는 embedding model은 mini-batch 안의 예시들을 보고 비슷한 것은 가까이, 다른 것은 멀리 가도록 gradient를 계산한다.

### 헷갈리기 쉬운 포인트

- SGD가 항상 데이터 1개만 쓴다는 뜻은 아니다. 실전에서 “SGD로 학습한다”고 말해도 보통 mini-batch를 사용한다.
- mini-batch가 작을수록 무조건 좋은 것은 아니다. 너무 작으면 gradient가 많이 흔들리고 GPU를 비효율적으로 쓸 수 있다.
- mini-batch가 클수록 무조건 좋은 것도 아니다. 너무 크면 업데이트 횟수가 줄고, 일반화 성능이 나빠질 때도 있다.
- stochastic estimate는 “틀린 값”이 아니라 “일부 표본으로 계산한 대략적 추정값”이다.
- loss가 내려가다가 오르내리는 것은 mini-batch 학습에서는 자연스러운 현상일 수 있다. 중요한 것은 장기적인 추세다.

---

## 2. 학습률, 수렴, 불안정성

### 한 줄 직관

학습률(learning rate)은 모델이 한 번에 얼마나 크게 움직일지 정하는 보폭이고, 보폭이 적당하면 수렴(convergence)하지만 너무 크면 튕기거나 발산(divergence)할 수 있다.

### 개념 정의

학습률(learning rate)은 gradient를 따라 parameter를 업데이트할 때 이동 크기를 조절하는 숫자이다. 가장 기본적인 업데이트 식은 다음 감각이다.

“새 parameter = 현재 parameter - learning rate × gradient”

gradient는 loss가 커지는 방향을 가리킨다. loss를 줄이려면 그 반대 방향으로 움직여야 하므로 빼기 기호가 붙는다. learning rate는 그 방향으로 얼마나 크게 움직일지를 정한다.

수렴(convergence)은 학습이 진행되면서 loss가 점점 줄고 parameter가 어느 정도 안정적인 좋은 지점에 가까워지는 상태이다. 발산(divergence)은 업데이트가 너무 커서 loss가 줄지 않고 오히려 커지거나 숫자가 폭주하는 상태이다. 진동(oscillation)은 최솟값 근처를 지나치게 크게 왔다 갔다 하는 현상이다.

### 왜 이런 개념이 필요한가

learning rate는 딥러닝 학습에서 가장 중요한 hyperparameter 중 하나다. hyperparameter는 모델이 학습으로 자동으로 찾는 값이 아니라, 사람이 학습 전에 정해야 하는 설정값이다.

learning rate가 너무 작으면 학습이 매우 느리다. 하루 종일 걸어도 목적지에 거의 도착하지 못하는 것과 비슷하다. learning rate가 너무 크면 좋은 지점을 지나쳐 반대편으로 튀고, 다시 지나쳐 또 튀면서 loss가 줄지 않는다.

실전에서는 같은 모델이라도 learning rate 하나 때문에 결과가 크게 달라질 수 있다. LLM fine-tuning에서도 learning rate가 너무 크면 기존에 잘하던 언어 능력이 망가질 수 있다. 반대로 너무 작으면 새 데이터에서 거의 배우지 못한다.

### 아주 쉬운 예시

아주 단순한 loss를 생각해보자.

\[
L(w) = (w - 3)^2
\]

이 loss는 \(w = 3\)일 때 0이 되어 가장 작다. 지금 \(w = 0\)이라고 하자. 이때 gradient는 \(2(w - 3) = -6\)이다.

업데이트는 다음과 같다.

\[
w_{new} = w - \eta \times gradient
\]

여기서 \(\eta\)가 learning rate이다.

1. learning rate = 0.1이면  
   \(w_{new} = 0 - 0.1 \times (-6) = 0.6\)  
   0에서 3 쪽으로 적당히 이동했다.

2. learning rate = 0.5이면  
   \(w_{new} = 0 - 0.5 \times (-6) = 3\)  
   한 번에 최적점에 도착했다. 이 장난감 예시에서는 운이 매우 좋다.

3. learning rate = 1.2이면  
   \(w_{new} = 0 - 1.2 \times (-6) = 7.2\)  
   최적점 3을 훨씬 지나쳤다. 다음에는 반대 방향으로 크게 움직이며 튈 수 있다.

산을 내려가는 비유로 보면, gradient는 “가장 가파르게 올라가는 방향”을 알려준다. 우리는 내려가야 하므로 반대로 간다. learning rate는 한 걸음의 크기이다. 한 걸음이 너무 크면 계곡 바닥을 지나 반대편 언덕으로 올라가 버린다.

### 개념 구조와 핵심 포인트

1. learning rate는 update 크기를 정한다.  
   gradient 방향이 맞아도 learning rate가 부적절하면 학습이 실패할 수 있다.

2. convergence는 loss가 안정적으로 줄어드는 상태다.  
   완전히 매번 감소해야만 수렴은 아니다. mini-batch 학습에서는 흔들리지만 전체 추세가 내려갈 수 있다.

3. divergence는 학습이 폭주하는 상태다.  
   loss가 계속 커지거나 NaN이 나오는 경우가 있다. NaN은 “숫자가 아님”을 뜻하며, 계산이 망가졌다는 강한 신호다.

4. oscillation은 최적점 주변을 왔다 갔다 하는 상태다.  
   learning rate가 조금 크거나, loss surface가 한 방향으로는 가파르고 다른 방향으로는 완만할 때 자주 생긴다.

5. learning rate schedule을 자주 쓴다.  
   처음에는 조금 크게 움직여 빠르게 배우고, 나중에는 작게 움직여 세밀하게 조정한다. 이를 learning rate decay, cosine schedule, warmup 같은 방식으로 구현한다.

### 핵심 수학 포인트

가장 기본적인 gradient descent update는 다음이다.

\[
\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)
\]

- \(\theta_t\): t번째 step의 parameter
- \(\eta\): learning rate
- \(\nabla L(\theta_t)\): 현재 parameter에서의 gradient

1D에서는 단순히 숫자 하나가 움직인다. 여러 parameter가 있는 모델에서는 \(\theta\)가 아주 긴 vector처럼 생각된다. 예를 들어 작은 neural network도 수천 개의 weight를 가질 수 있고, LLM은 수십억 개 이상의 parameter를 가진다. gradient도 parameter와 같은 shape을 가진다. weight matrix가 `[768, 3072]` shape이면 해당 weight에 대한 gradient도 `[768, 3072]` shape이다.

learning rate는 이 모든 parameter update에 곱해지는 기본 보폭이다. 그래서 작은 숫자처럼 보여도 모델 전체 움직임을 크게 좌우한다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- learning rate: gradient 방향으로 parameter를 얼마나 크게 업데이트할지 정하는 값.
- convergence: loss가 줄고 parameter가 안정적인 좋은 지점으로 가까워지는 현상.
- divergence: update가 불안정해 loss가 커지거나 숫자가 폭주하는 현상.
- oscillation: 최적점 주변을 지나치게 크게 왔다 갔다 하는 현상.
- learning rate schedule: 학습 중 learning rate를 바꾸는 규칙.
- warmup: 학습 초반 learning rate를 작은 값에서 서서히 키우는 방법. 큰 모델 학습에서 안정성을 위해 자주 쓴다.

### AI에서 어디에 쓰이는가

모델 학습, fine-tuning, embedding training, reinforcement learning 등 거의 모든 최적화 과정에서 learning rate가 중요하다.

LLM fine-tuning에서는 특히 조심해야 한다. 이미 사전학습된 모델은 많은 언어 지식을 parameter 안에 담고 있다. learning rate가 너무 크면 새 데이터 몇 개에 과하게 맞추면서 원래 능력을 망가뜨릴 수 있다. 이를 catastrophic forgetting과 연결해서 설명하기도 한다. 반대로 learning rate가 너무 작으면 fine-tuning 데이터의 스타일이나 작업 형식을 거의 배우지 못한다.

attention layer나 feed-forward layer의 weight도 모두 gradient로 업데이트된다. 학습이 안정적이면 hidden states가 점점 task에 맞는 표현을 만들도록 parameter가 조정된다. 학습이 불안정하면 loss가 튀고, embedding 공간이나 hidden representation도 일관되게 좋아지지 않는다.

### 헷갈리기 쉬운 포인트

- loss가 한 step에서 올랐다고 무조건 실패는 아니다. mini-batch 때문에 잠깐 오를 수 있다.
- learning rate가 작으면 항상 안전하다고 생각하기 쉽지만, 너무 작으면 사실상 학습이 거의 안 된다.
- learning rate가 크면 빨리 배우는 것이 아니라, 일정 수준을 넘으면 아예 못 배울 수 있다.
- convergence는 “정확도 100%”가 아니라 “최적화가 안정적으로 좋은 방향으로 가는 상태”에 가깝다.
- divergence는 코드 버그 때문일 수도 있지만, learning rate, gradient explosion, 잘못된 normalization, data 문제 때문일 수도 있다.

---

## 3. Momentum, Adam 같은 옵티마이저

### 한 줄 직관

Momentum과 Adam은 단순히 현재 gradient만 보고 움직이지 않고, 이전 움직임의 흐름과 gradient 크기 정보를 이용해 더 안정적이고 빠르게 학습하려는 optimizer이다.

### 개념 정의

옵티마이저(optimizer)는 gradient를 이용해 parameter를 어떻게 업데이트할지 정하는 알고리즘이다. 가장 기본은 SGD이다. SGD는 현재 mini-batch에서 계산한 gradient를 보고 바로 움직인다.

Momentum은 이전 gradient들의 누적 방향을 기억해서 관성처럼 움직이는 방법이다. 공이 경사면을 굴러 내려갈 때, 매 순간의 기울기뿐 아니라 이전에 굴러오던 속도도 영향을 주는 것과 비슷하다.

Adam은 Adaptive Moment Estimation의 줄임말이다. Adam은 크게 두 가지 정보를 추적한다.

1. first moment: gradient의 이동 평균. 쉽게 말해 “최근 gradient 방향의 평균적인 흐름”이다.
2. second moment: gradient 제곱의 이동 평균. 쉽게 말해 “최근 gradient 크기가 얼마나 컸는지”를 보는 정보이다.

Adam은 이 정보를 이용해 parameter마다 update 크기를 다르게 조절한다. 그래서 adaptive learning rate를 사용하는 optimizer라고 말한다.

### 왜 이런 개념이 필요한가

딥러닝의 loss surface는 단순한 그릇 모양이 아니다. 어떤 방향은 매우 가파르고, 어떤 방향은 매우 완만하다. 어떤 parameter는 gradient가 크게 나오고, 어떤 parameter는 작게 나온다. SGD만 사용하면 한쪽 방향으로는 너무 흔들리고, 다른 방향으로는 너무 느리게 갈 수 있다.

Momentum은 자주 같은 방향으로 나오는 gradient를 누적해서 그 방향으로 더 빠르게 가게 해준다. 동시에 mini-batch noise 때문에 좌우로 흔들리는 움직임은 어느 정도 줄여준다.

Adam은 여기서 한 단계 더 나아가 parameter별로 update 크기를 조절한다. gradient가 계속 큰 parameter는 너무 크게 움직이지 않도록 나누어 주고, gradient가 작은 parameter도 적절히 움직일 수 있게 돕는다. 그래서 많은 딥러닝 실험에서 Adam 또는 AdamW가 기본 선택처럼 쓰인다.

### 아주 쉬운 예시

좁고 긴 골짜기를 내려간다고 생각해보자. 골짜기 바닥은 앞으로 길게 이어져 있는데, 좌우 벽은 가파르다.

SGD는 현재 발밑 기울기만 보고 움직인다. 그러면 좌우 벽 때문에 왼쪽, 오른쪽으로 많이 튀면서 천천히 앞으로 갈 수 있다.

Momentum은 “최근에 계속 앞으로 가는 경향이 있었네”를 기억한다. 그래서 좌우 흔들림은 평균적으로 줄이고, 앞으로 가는 속도는 키운다.

숫자로 간단히 보자. 최근 gradient가 다음과 같다고 하자.

- step 1 gradient: 5
- step 2 gradient: 5
- step 3 gradient: 5

계속 같은 방향이면 Momentum은 “이 방향은 믿을 만하다”고 보고 움직임을 누적한다. 반대로 gradient가 다음처럼 왔다 갔다 한다고 하자.

- step 1 gradient: 5
- step 2 gradient: -5
- step 3 gradient: 5

이 경우 평균적으로는 흔들림이 크다. Momentum의 누적 평균은 이런 빠른 방향 전환을 어느 정도 부드럽게 만든다.

Adam의 작은 예시도 보자. 어떤 parameter A는 gradient가 자주 10처럼 크게 나오고, parameter B는 gradient가 자주 0.1처럼 작게 나온다고 하자. 같은 learning rate를 그대로 곱하면 A는 너무 크게 움직이고 B는 거의 움직이지 않을 수 있다. Adam은 gradient 제곱 평균, 즉 second moment를 이용해 “A는 gradient가 크니 update를 조심하고, B는 상대적으로 작으니 적절히 보정하자”는 식으로 parameter별 update를 조절한다.

### 개념 구조와 핵심 포인트

1. optimizer는 parameter update 규칙이다.  
   gradient를 계산하는 것과 gradient를 어떻게 사용할지는 다른 문제다. optimizer는 후자를 담당한다.

2. SGD는 단순하고 강력하지만 흔들릴 수 있다.  
   현재 mini-batch gradient만 사용하므로 noise가 그대로 반영된다.

3. Momentum은 방향의 누적 흐름을 본다.  
   같은 방향으로 반복되는 gradient는 강화하고, 빠르게 바뀌는 흔들림은 줄이는 효과가 있다.

4. Adam은 방향 평균과 크기 평균을 함께 본다.  
   first moment는 gradient의 평균 방향, second moment는 gradient 제곱의 평균 크기이다.

5. AdamW는 실전 LLM 학습에서 자주 나온다.  
   AdamW는 Adam에 weight decay를 더 올바르게 적용한 변형으로, Transformer 계열 모델 학습과 fine-tuning에서 널리 사용된다.

### 핵심 수학 포인트

Momentum의 핵심은 velocity라는 누적 값을 두는 것이다.

\[
v_t = \beta v_{t-1} + (1 - \beta) g_t
\]

\[
\theta_{t+1} = \theta_t - \eta v_t
\]

- \(g_t\): 현재 step의 gradient
- \(v_t\): 누적된 이동 방향, velocity
- \(\beta\): 이전 흐름을 얼마나 유지할지 정하는 값. 보통 0.9 같은 값을 쓴다.

Adam은 first moment와 second moment를 추적한다.

\[
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t
\]

\[
v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
\]

여기서 \(m_t\)는 first moment, \(v_t\)는 second moment이다. 이름이 Momentum의 velocity와 겹쳐 보일 수 있으니 문맥을 보고 이해해야 한다.

Adam의 update는 직관적으로 다음과 같다.

\[
\theta_{t+1} \approx \theta_t - \eta \frac{m_t}{\sqrt{v_t} + \epsilon}
\]

분모에 second moment의 제곱근이 들어가기 때문에, gradient 크기가 큰 parameter는 update가 너무 커지지 않도록 조절된다. \(\epsilon\)은 0으로 나누는 문제를 막기 위한 아주 작은 숫자이다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- momentum: 이전 gradient 흐름을 누적해 update에 반영하는 방법.
- Adam: first moment와 second moment를 이용하는 adaptive optimizer.
- adaptive learning rate: parameter마다 update 크기를 다르게 조절하는 방식.
- first moment: gradient의 이동 평균. 평균적인 방향 정보.
- second moment: gradient 제곱의 이동 평균. 평균적인 크기 정보.
- optimizer: gradient를 사용해 parameter를 업데이트하는 알고리즘.
- AdamW: Adam에서 weight decay 처리를 개선한 optimizer. LLM 학습에서 자주 사용된다.

### AI에서 어디에 쓰이는가

Transformer, CNN, diffusion model, 추천 모델 등 많은 딥러닝 모델에서 optimizer 선택은 성능과 안정성에 직접 영향을 준다.

LLM 사전학습이나 fine-tuning에서는 AdamW가 매우 자주 쓰인다. attention layer, feed-forward layer, embedding table의 모든 parameter가 optimizer에 의해 업데이트된다. gradient는 backpropagation으로 계산되지만, 실제로 parameter를 얼마나 바꿀지는 optimizer가 결정한다.

embedding model에서도 Adam 계열 optimizer가 흔하다. 예를 들어 문장 embedding을 학습할 때, 비슷한 문장 pair는 vector가 가까워지도록, 다른 문장은 멀어지도록 loss를 만든다. optimizer는 그 loss의 gradient를 사용해 embedding space를 조금씩 정리한다.

실전에서는 optimizer와 learning rate schedule을 함께 생각한다. Adam을 쓴다고 learning rate 고민이 사라지는 것은 아니다. Adam은 update를 자동으로 보정해주지만, 기본 learning rate가 너무 크면 여전히 불안정해질 수 있다.

### 헷갈리기 쉬운 포인트

- Adam이 항상 SGD보다 좋은 것은 아니다. 문제, 데이터, regularization, generalization 목표에 따라 SGD가 더 나을 때도 있다.
- adaptive learning rate는 “learning rate를 아예 안 정해도 된다”는 뜻이 아니다. 기본 learning rate는 여전히 중요하다.
- Momentum은 gradient를 무작정 크게 만드는 것이 아니라, 일관된 방향을 누적하고 흔들림을 완화하는 역할을 한다.
- first moment와 second moment는 어려운 확률 용어처럼 보이지만, 여기서는 각각 “gradient 평균”과 “gradient 제곱 평균”으로 먼저 이해하면 충분하다.
- optimizer는 loss를 직접 정하지 않는다. loss는 목표를 정의하고, optimizer는 그 목표를 줄이는 방향으로 parameter를 업데이트한다.

---

## 복습 질문 3개

1. mini-batch gradient는 전체 데이터 gradient와 항상 같지 않은데도 왜 학습에 사용할 수 있을까?
2. learning rate가 너무 클 때 나타날 수 있는 divergence와 oscillation은 각각 어떤 느낌의 현상인가?
3. Adam에서 first moment와 second moment는 각각 어떤 정보를 기억하며, 왜 parameter별 update 조절에 도움이 될까?

## 오늘의 한 줄 요약

딥러닝 학습은 mini-batch로 gradient를 추정하고, learning rate로 보폭을 정하며, Momentum이나 Adam 같은 optimizer로 더 빠르고 안정적으로 loss를 줄여가는 최적화 과정이다.

---

## Follow-up Review Answers

Source output file: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-04-28_09-26-41.md`

[AI/ML 오늘의 복습 정답 Day 06/30]

오늘은 mini-batch SGD, learning rate, Adam optimizer를 “학습이 어떻게 loss를 줄이는가”라는 관점에서 다시 정리해볼게요.

### 1. mini-batch gradient는 전체 데이터 gradient와 항상 같지 않은데도 왜 학습에 사용할 수 있을까?

**정답**

mini-batch gradient는 전체 데이터 gradient의 정확한 값은 아니지만, 무작위로 잘 뽑은 일부 데이터로 계산한 “대략적인 추정치”이기 때문에 학습에 사용할 수 있습니다.

즉, 한 번의 mini-batch gradient는 조금 틀릴 수 있지만, 여러 mini-batch를 반복해서 보면 평균적으로는 전체 데이터가 알려주는 방향과 비슷한 방향을 가리키게 됩니다. 이것을 stochastic estimate, 즉 확률적 추정치라고 볼 수 있습니다.

**설명**

전체 데이터 gradient는 모든 데이터를 다 보고 계산한 가장 안정적인 방향입니다. 하지만 데이터가 많으면 매번 전체 데이터를 다 사용하는 것은 너무 느립니다.

예를 들어 데이터가 100만 개라면, 매 update마다 100만 개를 전부 보고 gradient를 계산하는 것은 매우 비쌉니다. 그래서 실제 딥러닝에서는 32개, 64개, 128개처럼 작은 묶음인 mini-batch를 사용합니다.

mini-batch gradient는 전체 데이터의 일부만 보고 계산하므로 매번 방향이 조금 흔들립니다. 이 흔들림을 variance라고 합니다. variance는 추정값이 얼마나 요동치는지를 뜻합니다.

하지만 중요한 점은 mini-batch가 무작위로 잘 뽑혔다면, 한 번 한 번은 조금 다르더라도 장기적으로는 전체 gradient의 방향을 따라간다는 것입니다. 그래서 완벽히 정확하지 않아도 학습에 쓸 수 있습니다.

오히려 이 작은 randomness가 도움이 될 때도 있습니다. 모델이 너무 매끄럽게 한 방향으로만 가다가 좋지 않은 지점에 갇히는 것을 어느 정도 피하게 해줄 수 있기 때문입니다.

**예시**

전체 데이터 4개의 gradient가 다음과 같다고 해볼게요.

- 데이터 1: 2
- 데이터 2: 4
- 데이터 3: 6
- 데이터 4: 8

전체 평균 gradient는 5입니다.

그런데 mini-batch로 데이터 1, 2만 뽑으면 평균은 3입니다.  
데이터 3, 4만 뽑으면 평균은 7입니다.

3도 7도 전체 평균 5와 정확히 같지는 않습니다. 하지만 여러 mini-batch를 계속 사용하면 어떤 때는 작게, 어떤 때는 크게 나오면서 전체적으로는 5 근처의 방향을 따라가게 됩니다.

일상 비유로는 문제집 1,000문제를 전부 채점하고 공부 방향을 정하는 대신, 20문제씩 풀고 바로 피드백을 받는 것과 비슷합니다. 20문제만 보면 판단이 완벽하지는 않지만, 빠르게 여러 번 방향을 고칠 수 있습니다.

**실전 연결**

LLM이나 이미지 모델은 데이터가 너무 많아서 전체 데이터를 한 번에 보고 update할 수 없습니다. 그래서 학습할 때 token sequence나 이미지들을 mini-batch로 묶어 loss를 계산하고, 그 loss에서 gradient를 구해 parameter를 업데이트합니다.

예를 들어 LLM fine-tuning에서 batch size가 8이고 sequence length가 2048이면, 입력은 대략 `[8, 2048]` 같은 tensor shape을 가질 수 있습니다. 모델은 이 작은 묶음에서 다음 token 예측 loss를 계산하고, 그 mini-batch gradient를 이용해 조금씩 학습합니다.

---

### 2. learning rate가 너무 클 때 나타날 수 있는 divergence와 oscillation은 각각 어떤 느낌의 현상인가?

**정답**

learning rate가 너무 크면 모델이 한 번에 너무 크게 움직입니다.

divergence는 loss가 줄지 않고 오히려 커지거나 숫자가 폭주하는 현상입니다. 쉽게 말해 학습이 완전히 엉뚱한 방향으로 망가지는 느낌입니다.

oscillation은 최적점 근처까지는 왔지만, 한 걸음이 너무 커서 좋은 지점을 지나치며 좌우로 계속 왔다 갔다 하는 현상입니다. 즉, 목적지 주변에서 멈추지 못하고 계속 튀는 느낌입니다.

**설명**

learning rate는 parameter를 한 번 update할 때 얼마나 크게 움직일지 정하는 값입니다. 기본적인 감각은 다음과 같습니다.

현재 parameter에서 gradient를 구하고, loss가 줄어드는 방향으로 이동합니다. 이때 learning rate는 그 이동의 보폭입니다.

보폭이 적당하면 loss가 점점 줄어들고 convergence, 즉 수렴이 일어납니다. 수렴은 모델이 점점 안정적인 좋은 지점에 가까워지는 상태입니다.

하지만 learning rate가 너무 크면 문제가 생깁니다.

첫 번째는 oscillation입니다. loss가 가장 작은 지점 근처로 가기는 하지만, 한 번의 update가 너무 커서 그 지점을 지나쳐버립니다. 다음 step에서는 반대 방향으로 또 지나칩니다. 그래서 왼쪽, 오른쪽으로 계속 흔들립니다.

두 번째는 divergence입니다. 이 경우는 더 심합니다. update가 너무 커서 loss가 점점 커지고, parameter 값이 이상하게 커지며, 심하면 NaN이 나오기도 합니다. NaN은 “Not a Number”, 즉 계산이 망가져 숫자로 표현할 수 없는 상태입니다.

**예시**

아주 단순한 loss를 생각해봅시다.

목표는 parameter `w`를 3에 가깝게 만드는 것입니다. 현재 `w = 0`이라고 해볼게요.

learning rate가 적당하면 `w`는 0에서 3 쪽으로 조금씩 이동합니다.

예를 들어 한 걸음 후에 `w = 0.6`, 그다음 `w = 1.1`, 그다음 `w = 1.5`처럼 점점 3에 가까워질 수 있습니다.

그런데 learning rate가 너무 크면 한 번에 `w = 7.2`처럼 3을 훨씬 지나칠 수 있습니다. 다음에는 다시 반대쪽으로 크게 움직여 `w = -2` 근처로 갈 수도 있습니다. 이렇게 3 주변을 계속 크게 왔다 갔다 하면 oscillation입니다.

더 심하면 `w`가 7, -20, 100, -500처럼 점점 더 멀어질 수 있습니다. 이때 loss도 점점 커집니다. 이런 상태가 divergence입니다.

산을 내려가는 비유로 보면, learning rate는 한 걸음의 크기입니다. 한 걸음이 너무 크면 계곡 바닥에 멈추지 못하고 반대편 언덕으로 튀어 올라갑니다. 계속 더 크게 튀면 아예 산 아래로 내려가는 데 실패합니다.

**실전 연결**

딥러닝 학습에서 learning rate는 가장 중요한 hyperparameter 중 하나입니다. hyperparameter는 모델이 자동으로 배우는 값이 아니라, 사람이 학습 전에 정해야 하는 설정값입니다.

LLM fine-tuning에서는 특히 learning rate가 중요합니다. 너무 크면 이미 사전학습된 언어 능력이 망가질 수 있습니다. 예를 들어 모델이 원래 문장을 잘 생성하던 능력을 잃고, fine-tuning 데이터의 이상한 패턴에 과하게 맞춰질 수 있습니다.

반대로 learning rate가 너무 작으면 안정적이긴 하지만 거의 배우지 못합니다. 그래서 실전에서는 warmup, learning rate decay, cosine schedule 같은 learning rate schedule을 함께 사용해서 초반에는 조심스럽게 시작하고, 이후에는 적절한 크기로 학습하게 만듭니다.

---

### 3. Adam에서 first moment와 second moment는 각각 어떤 정보를 기억하며, 왜 parameter별 update 조절에 도움이 될까?

**정답**

Adam에서 first moment는 gradient의 이동 평균, 즉 최근 gradient들이 평균적으로 어느 방향을 가리키는지를 기억합니다.

second moment는 gradient 제곱의 이동 평균, 즉 최근 gradient의 크기가 얼마나 컸는지를 기억합니다.

Adam은 이 두 정보를 이용해서 parameter마다 update 크기를 다르게 조절합니다. 그래서 gradient가 자주 크게 나오는 parameter는 너무 크게 움직이지 않게 하고, gradient가 작게 나오는 parameter도 적절히 움직일 수 있게 도와줍니다.

**설명**

Adam은 Adaptive Moment Estimation의 줄임말입니다. 이름 그대로 moment, 즉 gradient에 대한 통계적 정보를 추정해서 update에 사용합니다.

여기서 first moment는 어렵게 생각하지 않아도 됩니다. 처음에는 “gradient의 평균 방향”이라고 이해하면 충분합니다.

예를 들어 최근 gradient가 계속 비슷한 방향으로 나오면, Adam은 “이 방향은 꽤 일관성이 있구나”라고 판단할 수 있습니다. 이것은 Momentum과 비슷한 역할을 합니다. 매 step의 noisy한 gradient 하나만 믿지 않고, 최근 흐름을 부드럽게 반영합니다.

second moment는 gradient를 제곱한 값의 평균입니다. gradient를 제곱하면 방향의 plus/minus보다는 크기 정보가 중요해집니다. 즉, 어떤 parameter에서 gradient가 계속 크게 나오는지, 작게 나오는지를 보는 데 도움이 됩니다.

Adam은 update할 때 first moment를 사용해 방향을 잡고, second moment를 사용해 크기를 조절합니다. 그래서 모든 parameter에 똑같은 방식으로 learning rate를 적용하는 것이 아니라, parameter별 상황에 맞게 adaptive learning rate를 적용합니다.

이것이 Adam이 많은 딥러닝 실험에서 안정적이고 빠르게 동작하는 이유 중 하나입니다.

**예시**

두 개의 parameter A와 B가 있다고 해봅시다.

- parameter A의 gradient는 자주 10 정도로 큽니다.
- parameter B의 gradient는 자주 0.1 정도로 작습니다.

그냥 같은 learning rate를 곱하면 A는 너무 크게 움직일 수 있고, B는 거의 움직이지 않을 수 있습니다.

Adam은 second moment를 통해 “A는 gradient가 계속 크구나”를 압니다. 그래서 A의 update가 너무 커지지 않게 조절합니다.

반대로 B는 gradient가 작다는 것도 파악합니다. 그래서 B가 완전히 무시되지 않도록 parameter별 update 크기를 조정할 수 있습니다.

일상 비유로는 여러 학생에게 같은 공부량을 무조건 주는 것이 아니라, 각 학생의 상태를 보고 조절하는 것과 비슷합니다. 어떤 학생은 이미 변화가 너무 크니 조금 안정시키고, 어떤 학생은 변화가 너무 작으니 조금 더 밀어주는 식입니다.

**실전 연결**

Transformer, LLM, diffusion model, 추천 모델 등 많은 딥러닝 모델에서 Adam 또는 AdamW가 자주 사용됩니다.

LLM 학습에서는 attention layer, feed-forward layer, embedding table 등 수많은 parameter가 있습니다. 각 parameter마다 gradient의 크기와 패턴이 다를 수 있습니다. Adam은 first moment와 second moment를 이용해 이 parameter들을 조금 더 안정적으로 업데이트합니다.

특히 AdamW는 LLM fine-tuning에서 매우 흔하게 등장합니다. Adam의 adaptive update 장점에 weight decay 처리를 더 실전적으로 적용한 optimizer입니다. 다만 Adam을 쓴다고 learning rate 고민이 사라지는 것은 아닙니다. Adam도 기본 learning rate가 너무 크면 여전히 loss가 튀거나 학습이 불안정해질 수 있습니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-04-28-day06.md
