# Day 07 - AI/ML 기초 학습

- Date: 2026-04-29
- Progress: 7/30
- Level: beginner-intermediate
- Milestone: 통계적 학습 이론의 직관
- Milestone goal: 모델이 데이터에 맞는 것과 일반화되는 것은 다르다는 점을 이해한다.

## Today's 3 concepts

1. 가설공간과 모델 용량
2. 훈련/검증/테스트 분리
3. 일반화와 generalization gap

---

## 1. 가설공간과 모델 용량

### 한 줄 직관

모델은 아무 답이나 만들 수 있는 것이 아니라, 자신이 표현할 수 있는 답의 후보들 안에서만 배운다. 이 후보들의 전체 범위가 가설공간(hypothesis space)이고, 그 범위가 얼마나 넓고 복잡한지를 모델 용량(capacity)이라고 생각하면 된다.

### 개념 정의

가설공간(hypothesis space)은 어떤 모델이 선택할 수 있는 모든 가능한 함수의 집합이다. 여기서 함수라는 말이 어렵게 느껴질 수 있다. 아주 단순하게 말하면, 입력을 넣었을 때 출력을 내는 규칙이다.

예를 들어 집 크기 하나만 보고 집값을 예측한다고 하자.

- 모델 A: `집값 = a × 집 크기 + b` 같은 직선만 그릴 수 있다.
- 모델 B: 직선뿐 아니라 구불구불한 곡선도 그릴 수 있다.
- 모델 C: 매우 복잡한 곡선, 여러 번 꺾이는 규칙, 많은 조건을 가진 규칙도 만들 수 있다.

이때 모델 A의 가설공간은 “가능한 모든 직선”이다. 모델 B의 가설공간은 “가능한 여러 곡선”이다. 모델 C의 가설공간은 훨씬 더 넓다.

모델 용량(capacity)은 이 가설공간이 얼마나 복잡한 패턴까지 담을 수 있는지를 말한다. 비슷한 말로 표현력(expressivity)이 있다. expressivity는 모델이 얼마나 다양한 형태의 관계를 표현할 수 있는지를 강조할 때 자주 쓴다.

또 하나 중요한 말이 inductive bias이다. inductive bias는 모델이 데이터를 보기 전부터 가지고 있는 “선호” 또는 “가정”이다. 예를 들어 선형 모델은 기본적으로 “입력과 출력의 관계가 대체로 직선적일 것이다”라는 bias를 가진다. CNN은 이미지에서 가까운 픽셀들이 서로 관련이 있을 것이라는 bias를 가진다. Transformer는 token들 사이의 관계를 attention으로 비교해 중요한 연결을 찾을 수 있다는 구조적 bias를 가진다.

### 왜 이런 개념이 필요한가

AI 모델을 고를 때 가장 중요한 질문 중 하나는 “이 모델이 너무 단순한가, 아니면 너무 복잡한가?”이다.

모델이 너무 단순하면 실제 패턴을 못 잡는다. 이를 underfitting이라고 부른다. 예를 들어 실제 집값이 위치, 층수, 학군, 면적, 교통에 따라 복잡하게 변하는데, 집 크기 하나로 직선만 그리면 중요한 정보를 놓친다.

반대로 모델이 너무 복잡하면 훈련 데이터의 우연한 잡음까지 외울 수 있다. 이를 overfitting이라고 부른다. 예를 들어 시험 문제 10개와 정답을 통째로 외운 학생은 그 10개는 다 맞힐 수 있지만, 새로운 문제를 보면 약할 수 있다.

딥러닝 모델, 특히 LLM은 capacity가 매우 크다. 수십억 개 이상의 parameter를 가진 모델은 엄청나게 많은 패턴을 표현할 수 있다. 그래서 좋은 데이터와 적절한 학습 방법이 있으면 언어, 코드, 추론 패턴을 잘 배울 수 있다. 하지만 동시에 잘못하면 훈련 데이터의 편향, 중복 문장, 개인 정보, 표면적 패턴도 외울 수 있다.

### 아주 쉬운 예시

점 3개가 있다고 하자.

| x | y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |

이 데이터는 `y = 2x`라는 직선으로 깔끔하게 설명된다. 이 경우 직선 모델도 충분하다.

그런데 점이 이렇게 바뀌었다고 하자.

| x | y |
|---|---|
| 1 | 2 |
| 2 | 100 |
| 3 | 6 |

두 번째 점 `x=2, y=100`은 이상한 값일 수 있다. 측정 실수일 수도 있고, 특별한 사건일 수도 있다. capacity가 큰 모델은 이 점까지 정확히 지나가도록 구불구불한 곡선을 만들 수 있다. 훈련 데이터에서는 오차가 0이 될 수도 있다.

하지만 새 데이터 `x=4`가 들어왔을 때, 그 복잡한 곡선이 이상한 예측을 할 수 있다. 반면 단순한 직선 모델은 `x=2, y=100`을 완벽히 맞히지는 못하지만, 전체 흐름이 `y≈2x`라고 보고 `x=4`에서 8에 가까운 값을 예측할 수 있다.

이 예시는 capacity가 클수록 항상 좋은 것이 아니라는 점을 보여준다. 중요한 것은 “훈련 데이터에 맞는 정도”와 “새 데이터에서도 맞는 정도”의 균형이다.

### 개념 구조와 핵심 포인트

- hypothesis space는 모델이 선택할 수 있는 모든 가능한 규칙의 집합이다.
- capacity는 그 규칙 집합이 얼마나 복잡한 패턴을 표현할 수 있는지를 나타낸다.
- expressivity는 모델이 다양한 형태의 함수를 표현하는 능력이다.
- inductive bias는 모델 구조가 기본적으로 선호하는 해석 방식이다.
- capacity가 낮으면 underfitting 위험이 커진다.
- capacity가 높으면 overfitting 위험이 커진다.
- 좋은 모델은 충분히 표현력이 있으면서도, 필요 없는 잡음까지 외우지 않도록 학습된다.

딥러닝에서는 capacity가 parameter 수, layer 수, hidden dimension, attention head 수, embedding dimension 등과 관련된다. 예를 들어 hidden state의 차원이 크면 더 많은 정보를 담을 수 있지만, 데이터가 부족하면 훈련 데이터의 세부 잡음까지 담을 위험도 커진다.

### 핵심 수학 포인트

가장 단순한 경우부터 보자.

선형 모델은 보통 다음처럼 쓴다.

`ŷ = wx + b`

여기서 `x`는 입력, `ŷ`는 예측값, `w`와 `b`는 학습되는 parameter이다. 이 모델의 hypothesis space는 가능한 모든 `w`와 `b` 조합으로 만들어지는 직선들의 집합이다.

만약 모델을 이렇게 바꾸면 더 복잡해진다.

`ŷ = ax² + bx + c`

이제 직선뿐 아니라 휘어진 곡선도 만들 수 있다. 즉 hypothesis space가 더 넓어졌다. 더 넓은 hypothesis space는 더 복잡한 데이터를 맞힐 수 있지만, 훈련 데이터가 적거나 noise가 많으면 overfitting할 수 있다.

신경망에서는 이 함수가 훨씬 복잡해진다. 여러 linear layer, activation function, attention layer가 이어지면서 입력 token embedding을 hidden state로 바꾸고, 마지막에는 다음 token 확률이나 class 확률을 출력한다. 수식은 복잡해 보이지만 핵심은 같다.

“모델 구조와 parameter가 허용하는 함수들의 전체 범위가 hypothesis space이다.”

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- hypothesis space: 모델이 선택할 수 있는 가능한 함수 또는 규칙의 전체 집합
- capacity: 모델이 복잡한 패턴을 표현할 수 있는 정도
- expressivity: 모델이 다양한 형태의 관계를 표현하는 능력
- inductive bias: 모델 구조가 기본적으로 가지고 있는 가정이나 선호
- underfitting: 모델이 너무 단순해서 훈련 데이터의 패턴도 잘 못 잡는 상태
- overfitting: 모델이 훈련 데이터의 잡음까지 외워서 새 데이터에 약해지는 상태
- parameter: 학습을 통해 바뀌는 숫자 값, 예를 들어 weight와 bias

### AI에서 어디에 쓰이는가

모델 선택과 구조 설계에서 항상 쓰인다. 간단한 표 데이터 문제에서는 작은 tree model이나 linear model이 충분할 수 있다. 이미지 인식에서는 CNN이나 Vision Transformer처럼 이미지 구조를 잘 다루는 모델이 필요할 수 있다. 언어 모델에서는 Transformer가 token 사이의 관계를 attention으로 다룰 수 있어서 강력한 hypothesis space를 가진다.

LLM에서는 capacity가 매우 중요하다. 큰 모델은 긴 문맥, 코드 패턴, 문법, 세계 지식, 추론 패턴을 더 잘 표현할 가능성이 있다. 하지만 크기만 키우면 되는 것은 아니다. 데이터 품질, regularization, optimizer 설정, training loss와 validation loss 추적이 함께 중요하다.

예를 들어 훈련 loss는 계속 내려가는데 validation loss가 올라가기 시작하면, 모델이 훈련 데이터를 너무 세밀하게 맞추는 overfitting 신호일 수 있다. 이때는 데이터 증강, early stopping, weight decay, dropout, 모델 크기 조정 같은 방법을 고민한다.

### 헷갈리기 쉬운 포인트

- capacity가 크다는 말은 “항상 성능이 좋다”는 뜻이 아니다.
- hypothesis space가 넓으면 좋은 답도 포함될 가능성이 크지만, 나쁜 답이나 잡음을 외우는 답도 포함될 수 있다.
- inductive bias는 나쁜 말이 아니다. 오히려 데이터가 제한적일 때 올바른 bias는 일반화에 도움을 준다.
- expressivity와 실제 성능은 다르다. 표현할 수 있어도 optimizer가 좋은 해를 찾지 못하거나 데이터가 부족하면 성능이 낮을 수 있다.

---

## 2. 훈련/검증/테스트 분리

### 한 줄 직관

모델을 공부시키는 문제지, 중간 점검용 문제지, 최종 시험지를 따로 두어야 모델이 정말 새 문제를 풀 수 있는지 알 수 있다.

### 개념 정의

머신러닝에서는 데이터를 보통 세 부분으로 나눈다.

- train set: 모델이 직접 보고 학습하는 데이터
- validation set: 학습 중 모델 선택과 설정 조정에 사용하는 데이터
- test set: 마지막에 딱 한 번, 최종 성능을 확인하는 데이터

train set은 학생이 공부하는 교재와 비슷하다. validation set은 모의고사와 비슷하다. test set은 최종 시험과 비슷하다.

중요한 점은 test set을 학습 과정에서 자주 보면 안 된다는 것이다. test set을 여러 번 보면서 모델을 고치면, 사실상 test set에 맞춘 것이 된다. 그러면 최종 시험지가 더 이상 진짜 최종 시험지가 아니다.

data leakage는 원래 학습 때 알면 안 되는 정보가 train set이나 feature 안으로 새어 들어가는 문제다. 예를 들어 내일 주가를 예측하는 모델인데 feature 안에 내일 종가와 거의 같은 정보가 들어가 있으면 모델 성능이 비정상적으로 높아진다. 하지만 실제 사용에서는 그런 정보를 알 수 없으므로 성능이 무너진다.

### 왜 이런 개념이 필요한가

우리가 알고 싶은 것은 “모델이 이미 본 데이터에서 잘하느냐”가 아니라 “처음 보는 데이터에서도 잘하느냐”이다. AI 모델은 실제 서비스에서 매번 새로운 입력을 만난다.

- 챗봇은 사용자가 처음 쓰는 문장을 받는다.
- 추천 시스템은 새로운 사용자 행동을 만난다.
- 의료 모델은 훈련 데이터에 없던 환자를 본다.
- 이미지 모델은 조명, 각도, 배경이 다른 사진을 본다.

train/validation/test 분리는 이 현실을 작게 흉내 내는 장치다. 모델에게 일부 데이터만 보여주고, 나머지 데이터로 “새 데이터에서의 성능”을 추정한다.

검증 데이터(validation set)가 필요한 이유도 중요하다. 모델을 만들 때 우리는 learning rate, batch size, layer 수, hidden dimension, dropout 비율 같은 선택을 한다. 이런 선택을 hyperparameter라고 한다. validation set은 이 선택들이 괜찮은지 중간 점검하는 데 쓴다.

### 아주 쉬운 예시

데이터가 10개 있다고 하자.

`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

아주 단순하게 나누면 다음과 같다.

- train set: 1~6번 데이터
- validation set: 7~8번 데이터
- test set: 9~10번 데이터

모델은 1~6번을 보면서 parameter를 학습한다. 예를 들어 loss를 줄이기 위해 gradient를 계산하고 optimizer가 weight를 조금씩 바꾼다.

그다음 7~8번으로 중간 점검한다. “learning rate를 0.1로 했더니 validation loss가 높네. 0.01로 바꿔보자.” 같은 판단을 한다.

마지막으로 모든 선택이 끝난 뒤 9~10번으로 최종 확인한다. 이때 test set 점수가 진짜 보고서에 쓸 성능에 가깝다.

만약 9~10번을 계속 보면서 모델을 고쳤다면 어떻게 될까? 모델은 9~10번에 은근히 맞춰진다. 그러면 test 성능은 실제 새 데이터 성능보다 좋게 보일 수 있다.

### 개념 구조와 핵심 포인트

- train set은 parameter를 직접 학습하는 데 사용된다.
- validation set은 hyperparameter 선택, early stopping, 모델 비교에 사용된다.
- test set은 최종 성능 추정에 사용된다.
- test set은 최대한 마지막까지 건드리지 않는 것이 좋다.
- data leakage가 생기면 성능이 실제보다 과장된다.
- 데이터 분리는 문제의 시간 구조, 사용자 구조, 그룹 구조를 고려해야 한다.

예를 들어 시간 순서가 중요한 예측에서는 랜덤 분리가 위험할 수 있다. 내일을 예측하는 모델인데 미래 데이터가 train set에 섞이면 leakage가 생긴다. 이런 경우에는 과거 데이터를 train으로, 이후 데이터를 validation/test로 두는 time-based split이 더 자연스럽다.

사용자별 추천 모델에서도 같은 사용자의 기록이 train과 test에 동시에 들어가면, 모델이 사용자를 어느 정도 외워서 성능이 높게 보일 수 있다. “새 사용자에게 잘하는가”를 보고 싶다면 user 단위로 분리해야 한다.

### 핵심 수학 포인트

머신러닝 학습은 보통 train set에서 평균 loss를 줄이는 문제로 볼 수 있다.

`train loss = train 데이터에서의 평균 오차`

예를 들어 train 데이터 3개의 오차가 각각 1, 2, 3이면 train loss는 평균인 2이다.

validation loss도 같은 방식으로 계산하지만, 모델이 직접 학습한 데이터가 아니라 validation set에서 계산한다.

- train loss가 낮다: 모델이 공부한 문제를 잘 푼다.
- validation loss가 낮다: 공부하지 않은 모의고사 문제도 잘 푼다.
- test loss가 낮다: 최종적으로 새 데이터에 대해 잘할 가능성이 높다.

딥러닝 구현에서는 보통 training loop 안에서 mini-batch 단위로 train loss를 계산하고, `loss.backward()`로 gradient를 구한 다음 optimizer가 parameter를 업데이트한다. 하지만 validation 단계에서는 parameter를 업데이트하지 않는다. validation은 “채점만 하는 단계”이다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- train set: 모델이 직접 학습하는 데이터
- validation set: 모델 선택과 hyperparameter 조정에 쓰는 중간 점검 데이터
- test set: 최종 성능 평가에 쓰는 데이터
- data leakage: 학습 때 알면 안 되는 정보가 데이터 안에 새어 들어가는 문제
- hyperparameter: 학습으로 자동 결정되지 않고 사람이 설정하는 값, 예를 들어 learning rate나 batch size
- early stopping: validation 성능이 나빠지기 시작하면 학습을 멈추는 방법
- split: 데이터를 목적에 따라 나누는 것

### AI에서 어디에 쓰이는가

모든 실전 ML 프로젝트에서 쓰인다. Kaggle 대회, 논문 실험, 사내 모델 배포, LLM fine-tuning까지 거의 항상 필요하다.

LLM fine-tuning을 예로 들어보자. train set에는 모델이 실제로 학습할 instruction-response 쌍이 들어간다. validation set에는 학습 중 성능을 확인할 held-out instruction이 들어간다. test set에는 최종 보고용 또는 배포 전 평가용 문제가 들어간다.

만약 같은 질문의 살짝 바꾼 버전이 train과 test에 동시에 들어가면, 모델이 진짜로 이해한 것이 아니라 문장을 외운 것처럼 보일 수 있다. LLM 평가에서 benchmark contamination이라는 문제가 바로 이와 관련된다. 평가 문제나 정답이 사전학습 데이터에 이미 들어 있었다면, 모델의 benchmark 점수가 실제 reasoning 능력을 과장할 수 있다.

### 헷갈리기 쉬운 포인트

- validation set과 test set은 둘 다 “학습에 직접 쓰지 않는 데이터”지만 역할이 다르다.
- validation set은 여러 번 봐도 되지만, 그만큼 validation set에도 맞춰질 수 있다.
- test set은 최종 평가용이므로 자주 보면 안 된다.
- 랜덤 분리가 항상 정답은 아니다. 시간, 사용자, 문서, 환자, 제품처럼 묶음 구조가 있으면 split 방식이 달라져야 한다.
- data leakage는 성능을 좋게 만드는 것이 아니라, 성능을 좋게 보이게 만드는 문제다.

---

## 3. 일반화와 generalization gap

### 한 줄 직관

진짜 좋은 모델은 연습문제만 잘 푸는 모델이 아니라, 처음 보는 문제에서도 비슷하게 잘 푸는 모델이다. 이 능력을 일반화(generalization)라고 한다.

### 개념 정의

generalization은 모델이 학습에 사용하지 않은 새 데이터, 즉 out-of-sample 데이터에서도 잘 작동하는 능력이다. out-of-sample은 말 그대로 “표본 밖”이라는 뜻이다. 여기서는 train set 밖의 데이터라고 이해하면 된다.

generalization gap은 train 성능과 validation/test 성능 사이의 차이다.

예를 들어 정확도(accuracy)를 본다고 하자.

- train accuracy: 98%
- test accuracy: 80%

이 경우 차이는 18%p이다. 이 차이를 generalization gap이라고 부를 수 있다. train에서는 매우 잘하지만 test에서는 많이 떨어지므로 overfitting을 의심할 수 있다.

loss로 볼 때는 이렇게 볼 수 있다.

- train loss: 0.1
- validation loss: 0.6

validation loss가 train loss보다 훨씬 높다. 이 역시 generalization gap이 큰 상황이다.

### 왜 이런 개념이 필요한가

머신러닝의 목표는 과거 데이터를 외우는 것이 아니다. 미래의 새 입력에 대해 좋은 예측을 하는 것이다. 그래서 일반화는 ML의 중심 목표라고 할 수 있다.

훈련 데이터는 세상의 일부 샘플일 뿐이다. 예를 들어 고양이 사진 분류 모델을 만든다고 하자. train set에는 밝은 방에서 찍은 고양이가 많고, test에는 어두운 곳의 고양이가 많을 수 있다. 모델이 밝은 배경을 고양이의 특징으로 잘못 배웠다면 새 사진에서 실패한다.

LLM도 마찬가지다. 모델이 특정 benchmark의 문장 패턴만 외웠다면 점수는 높아도 실제 사용자 질문에는 약할 수 있다. 반대로 일반화가 좋은 모델은 처음 보는 표현, 다른 주제, 약간 다른 형식의 질문에도 안정적으로 답한다.

### 아주 쉬운 예시

학생 A와 학생 B가 있다고 하자.

- 학생 A는 기출문제 100개와 정답을 통째로 외웠다.
- 학생 B는 기출문제를 풀면서 원리를 이해했다.

기출문제 그대로 시험이 나오면 학생 A가 100점을 받을 수 있다. 하지만 숫자만 조금 바뀐 새 문제가 나오면 A는 흔들릴 수 있다. 학생 B는 처음 보는 문제라도 원리를 적용할 가능성이 높다.

모델도 똑같다.

작은 숫자로 보자.

| 데이터 | train에서 맞힌 개수 | test에서 맞힌 개수 |
|---|---:|---:|
| 모델 A | 100개 중 99개 | 100개 중 70개 |
| 모델 B | 100개 중 90개 | 100개 중 88개 |

모델 A는 train 성능만 보면 좋아 보인다. 하지만 test에서 크게 떨어진다. 모델 B는 train 성능은 조금 낮지만 test에서도 거의 유지된다. 실전에서는 모델 B가 더 좋은 모델일 가능성이 크다.

### 개념 구조와 핵심 포인트

- generalization은 새 데이터에서의 성능이다.
- out-of-sample은 모델이 학습에 직접 보지 않은 데이터다.
- generalization gap은 train 성능과 validation/test 성능의 차이다.
- gap이 크면 overfitting 가능성이 있다.
- gap이 작고 성능도 높으면 좋은 신호다.
- gap이 작지만 train/test 성능이 둘 다 낮으면 underfitting일 수 있다.

중요한 것은 gap만 보면 안 된다는 점이다. 예를 들어 train accuracy 55%, test accuracy 54%이면 gap은 작다. 하지만 둘 다 낮으므로 모델이 패턴을 못 배운 것이다. 좋은 일반화는 “train과 test가 비슷하다”만이 아니라 “새 데이터 성능 자체가 충분히 좋다”까지 포함한다.

### 핵심 수학 포인트

가장 간단하게는 다음 차이로 생각할 수 있다.

`generalization gap = test error - train error`

또는 정확도를 쓴다면 방향이 반대가 된다.

`accuracy gap = train accuracy - test accuracy`

예를 들어 train error가 5%, test error가 15%이면 generalization gap은 10%p이다.

loss 기준으로는 다음처럼 볼 수 있다.

`gap = validation loss - train loss`

train loss가 0.2이고 validation loss가 0.5이면 gap은 0.3이다. 이 숫자가 커질수록 모델이 train set에 비해 새 데이터에서 더 못한다는 뜻이다.

딥러닝 학습 곡선을 보면 일반화 문제를 직관적으로 볼 수 있다.

- 초반: train loss와 validation loss가 함께 내려간다.
- 어느 순간 이후: train loss는 계속 내려가는데 validation loss가 멈추거나 올라간다.
- 이 지점 이후에는 모델이 train 데이터에 더 특화되고 있을 수 있다.

이때 early stopping을 쓰면 validation 성능이 가장 좋았던 시점의 모델을 저장할 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- generalization: 학습하지 않은 새 데이터에서도 잘 작동하는 능력
- generalization gap: train 성능과 validation/test 성능 사이의 차이
- out-of-sample: train set 밖의 새 데이터
- train error: train set에서의 오차
- test error: test set에서의 오차
- overfitting: train 성능은 좋지만 새 데이터 성능이 떨어지는 상태
- regularization: overfitting을 줄이기 위해 모델을 너무 복잡하게 맞추지 못하게 하는 방법들

### AI에서 어디에 쓰이는가

모델 평가, 논문 읽기, 서비스 배포에서 핵심 기준으로 쓰인다. 논문에서 “우리 모델이 benchmark에서 성능이 좋다”고 말할 때도 실제로는 그 benchmark가 out-of-sample 성능을 얼마나 잘 대표하는지가 중요하다.

LLM에서는 generalization이 특히 어렵고 중요하다. 사용자의 질문은 무한히 다양하다. train 데이터에 있던 문장과 정확히 같은 문장이 들어오는 경우보다, 비슷하지만 다른 문맥의 질문이 들어오는 경우가 훨씬 많다. 그래서 LLM은 단순 memorization보다 패턴, 구조, 의미, reasoning 절차를 배워야 한다.

embedding에서도 일반화가 중요하다. 예를 들어 “강아지”와 “개”가 비슷한 embedding 공간에 놓이면, 모델은 정확히 같은 단어를 보지 않아도 의미가 비슷한 입력을 비슷하게 처리할 수 있다. attention도 문장 안에서 어떤 token이 중요한지 문맥마다 다르게 찾으면서 일반화에 도움을 준다.

### 헷갈리기 쉬운 포인트

- train 성능이 높다고 generalization이 좋은 것은 아니다.
- test 성능을 계속 보면서 고치면 test set도 사실상 validation set처럼 되어 버린다.
- generalization gap이 작아도 전체 성능이 낮으면 좋은 모델이 아니다.
- 데이터 분포가 바뀌면 기존 test 성능이 실제 서비스 성능을 잘 대표하지 못할 수 있다. 이를 distribution shift라고 한다.
- 큰 모델은 generalization을 잘할 수도 있지만, 데이터와 평가가 부실하면 단순 memorization처럼 보이는 성능을 낼 수도 있다.

---

## 복습 질문 3개

1. hypothesis space와 capacity는 각각 무엇을 의미하며, capacity가 너무 작거나 너무 크면 어떤 문제가 생길까?
2. train set, validation set, test set은 각각 어떤 역할을 하며, test set을 자주 보면 왜 문제가 될까?
3. train accuracy가 99%이고 test accuracy가 75%라면 generalization gap 관점에서 어떤 해석을 할 수 있을까?

## 오늘의 한 줄 요약

모델의 진짜 실력은 훈련 데이터를 얼마나 잘 외웠는지가 아니라, 적절한 capacity와 올바른 데이터 분리를 바탕으로 처음 보는 데이터에 얼마나 잘 일반화되는지로 판단한다.

---

## 복습 질문 정답

[AI/ML 오늘의 복습 정답 Day 07/30]

오늘은 “모델이 훈련 데이터에 잘 맞는 것”과 “처음 보는 데이터에도 잘하는 것”이 왜 다른지 복습해볼게요.

### 1. hypothesis space와 capacity는 각각 무엇을 의미하며, capacity가 너무 작거나 너무 크면 어떤 문제가 생길까?

**정답**

hypothesis space는 모델이 선택할 수 있는 가능한 규칙, 즉 가능한 함수들의 전체 집합입니다.

capacity는 그 hypothesis space 안에서 모델이 얼마나 복잡한 패턴까지 표현할 수 있는지를 뜻합니다.

capacity가 너무 작으면 모델이 실제 패턴을 충분히 배우지 못해 underfitting이 생길 수 있습니다. 반대로 capacity가 너무 크면 훈련 데이터의 우연한 잡음까지 외워서 overfitting이 생길 수 있습니다.

**설명**

머신러닝 모델은 아무 규칙이나 만들 수 있는 것이 아닙니다. 모델 구조가 허용하는 범위 안에서만 답을 찾습니다.

예를 들어 선형 회귀 모델은 기본적으로 직선 형태의 규칙을 찾습니다. 이 모델의 hypothesis space는 “가능한 모든 직선”입니다. 반면 깊은 neural network는 훨씬 더 복잡한 곡선, 조건, 패턴을 표현할 수 있습니다. 그래서 hypothesis space가 훨씬 넓습니다.

capacity는 이 표현 능력의 크기라고 보면 됩니다. capacity가 낮은 모델은 단순해서 안정적일 수 있지만, 복잡한 문제를 못 풀 수 있습니다. 예를 들어 이미지 분류 문제를 아주 단순한 직선 모델로 풀면, 고양이와 강아지의 복잡한 차이를 잘 잡기 어렵습니다.

반대로 capacity가 높은 모델은 많은 패턴을 배울 수 있지만, 데이터가 적거나 noise가 많으면 위험합니다. 훈련 데이터 안의 우연한 예외, 오타, 특이한 샘플까지 “중요한 패턴”처럼 외울 수 있기 때문입니다.

그래서 좋은 모델은 무조건 큰 모델이 아니라, 문제의 복잡도와 데이터 양에 맞는 적절한 capacity를 가진 모델입니다.

**예시**

점 3개가 있다고 해봅시다.

x=1일 때 y=2  
x=2일 때 y=4  
x=3일 때 y=6

이 데이터는 `y = 2x`라는 단순한 직선으로 잘 설명됩니다. 이때는 직선 모델만으로도 충분합니다.

그런데 가운데 값이 갑자기 이렇게 바뀌었다고 해봅시다.

x=1일 때 y=2  
x=2일 때 y=100  
x=3일 때 y=6

capacity가 큰 모델은 이 세 점을 모두 정확히 지나가는 이상한 곡선을 만들 수 있습니다. 훈련 데이터에서는 완벽해 보일 수 있습니다. 하지만 x=4가 들어왔을 때 말도 안 되는 값을 예측할 수 있습니다.

즉, 너무 복잡한 모델은 “진짜 규칙”이 아니라 “훈련 데이터의 특이한 점”까지 외울 수 있습니다.

**실전 연결**

딥러닝과 LLM에서는 capacity가 매우 중요합니다. parameter 수, layer 수, hidden dimension, attention head 수가 커질수록 모델은 더 많은 패턴을 표현할 수 있습니다. 하지만 데이터 품질이 낮거나 평가가 부실하면 큰 모델은 좋은 일반화 대신 단순 memorization, 즉 외우기에 가까운 행동을 할 수 있습니다. 그래서 실제 학습에서는 training loss와 validation loss를 함께 보고, overfitting이 보이면 regularization, dropout, early stopping, 데이터 정제, 모델 크기 조정 등을 사용합니다.

### 2. train set, validation set, test set은 각각 어떤 역할을 하며, test set을 자주 보면 왜 문제가 될까?

**정답**

train set은 모델이 직접 보고 학습하는 데이터입니다.

validation set은 학습 중에 모델 선택이나 hyperparameter 조정에 사용하는 중간 점검용 데이터입니다.

test set은 모든 학습과 선택이 끝난 뒤, 최종 성능을 평가하기 위해 사용하는 데이터입니다.

test set을 자주 보면 모델이나 사람이 test set에 맞춰 결정을 하게 됩니다. 그러면 test set이 더 이상 “처음 보는 데이터” 역할을 하지 못하고, 최종 성능이 실제보다 좋게 보일 수 있습니다.

**설명**

train set, validation set, test set은 각각 학생의 공부 과정에 비유할 수 있습니다.

train set은 교재나 연습문제입니다. 모델은 이 데이터를 보면서 parameter를 바꿉니다. 딥러닝에서는 loss function을 계산하고, gradient를 구한 뒤, optimizer가 weight를 조금씩 업데이트합니다.

validation set은 모의고사입니다. 모델이 직접 학습하지는 않지만, 학습 중간에 “이 설정이 괜찮은가?”를 확인하는 데 씁니다. 예를 들어 learning rate를 0.1로 할지 0.01로 할지, layer를 몇 개로 할지, dropout을 얼마나 줄지 같은 결정을 validation 성능을 보고 조정합니다.

test set은 최종 시험입니다. 모든 모델 선택과 튜닝이 끝난 뒤 마지막에 사용해야 합니다. 이 데이터는 모델의 진짜 새 데이터 성능을 추정하기 위한 기준입니다.

문제는 test set을 여러 번 보면, 사람이든 모델이든 test set에 맞춰지기 시작한다는 것입니다. 예를 들어 test 점수를 보고 “이 모델은 별로네, 구조를 바꿔보자”를 반복하면, 사실상 test set을 validation set처럼 쓰는 것입니다. 그러면 최종 test 성능은 실제 새 데이터 성능보다 과장될 수 있습니다.

이와 관련된 중요한 문제로 data leakage가 있습니다. data leakage는 학습 때 알면 안 되는 정보가 train set이나 feature 안에 들어가는 상황입니다. 예를 들어 내일 주가를 예측하는 모델에 내일 종가와 거의 같은 정보가 feature로 들어가 있다면, 모델은 성능이 매우 좋아 보일 수 있습니다. 하지만 실제 서비스에서는 그 정보를 미리 알 수 없기 때문에 성능이 무너집니다.

**예시**

데이터가 10개 있다고 해봅시다.

1번부터 6번까지는 train set  
7번부터 8번까지는 validation set  
9번부터 10번까지는 test set

모델은 1~6번 데이터를 보면서 공부합니다.  
그다음 7~8번으로 중간 점검을 합니다. 예를 들어 “learning rate가 너무 큰가?”, “모델이 너무 복잡한가?”를 확인합니다.  
마지막으로 9~10번으로 최종 시험을 봅니다.

그런데 9~10번 점수를 계속 확인하면서 모델을 바꾸면 어떻게 될까요? 이제 9~10번은 순수한 최종 시험이 아닙니다. 모델 개발 과정에 영향을 준 데이터가 됩니다. 그래서 실제로 완전히 새로운 11번, 12번 데이터가 왔을 때는 성능이 떨어질 수 있습니다.

**실전 연결**

실제 ML/DL 프로젝트에서는 데이터 분리가 성능 평가의 신뢰도를 결정합니다. LLM fine-tuning에서도 train set은 instruction-response 데이터를 학습하는 데 쓰고, validation set은 학습 중 성능 확인과 early stopping에 쓰며, test set은 최종 보고나 배포 전 평가에 씁니다. 특히 LLM에서는 benchmark contamination도 중요합니다. 평가 문제나 정답이 이미 사전학습 데이터에 들어 있었다면, 모델이 진짜 reasoning을 한 것이 아니라 본 적 있는 답을 재현했을 수 있습니다. 그래서 test set을 깨끗하게 유지하는 것이 매우 중요합니다.

### 3. train accuracy가 99%이고 test accuracy가 75%라면 generalization gap 관점에서 어떤 해석을 할 수 있을까?

**정답**

train accuracy가 99%이고 test accuracy가 75%라면 accuracy 기준 generalization gap은 24%p입니다.

계산하면 `99% - 75% = 24%p`입니다.

이 gap은 꽤 큰 편이므로, 모델이 훈련 데이터에는 매우 잘 맞지만 처음 보는 데이터에는 성능이 많이 떨어진다고 해석할 수 있습니다. 즉 overfitting 가능성을 의심해야 합니다.

**설명**

generalization은 모델이 학습하지 않은 새 데이터에서도 잘 작동하는 능력입니다. 머신러닝의 진짜 목표는 train set을 외우는 것이 아니라, 앞으로 들어올 새 입력에 대해 좋은 예측을 하는 것입니다.

train accuracy는 모델이 공부한 문제를 얼마나 잘 맞히는지를 보여줍니다. test accuracy는 모델이 처음 보는 문제를 얼마나 잘 맞히는지를 보여줍니다.

train accuracy가 99%라는 것은 모델이 훈련 데이터는 거의 완벽하게 맞힌다는 뜻입니다. 하지만 test accuracy가 75%라면, 새로운 데이터에서는 성능이 꽤 떨어집니다. 이 차이인 24%p가 generalization gap입니다.

이런 상황에서는 모델이 훈련 데이터의 핵심 패턴만 배운 것이 아니라, 훈련 데이터에만 있는 세부 특징이나 noise까지 외웠을 수 있습니다. 그래서 train set에서는 뛰어나지만, test set에서는 약해지는 것입니다.

다만 여기서 한 가지 조심할 점이 있습니다. gap이 크다고 해서 무조건 원인이 하나로 정해지는 것은 아닙니다. overfitting이 대표적인 의심 원인이지만, train/test 데이터 분포가 다를 수도 있습니다. 예를 들어 train 데이터는 밝은 곳에서 찍은 고양이 사진이고, test 데이터는 어두운 곳에서 찍은 고양이 사진이라면 distribution shift, 즉 데이터 분포 변화도 원인일 수 있습니다.

**예시**

학생 두 명을 생각해봅시다.

학생 A는 연습문제 100개 중 99개를 맞힙니다. 그런데 처음 보는 시험 문제에서는 100개 중 75개만 맞힙니다.

이 학생은 연습문제에는 매우 강하지만, 새 문제에는 실력이 많이 떨어집니다. 원리를 깊게 이해했다기보다 연습문제의 형태를 많이 외웠을 가능성이 있습니다.

모델도 비슷합니다. train accuracy 99%, test accuracy 75%인 모델은 “공부한 데이터”에는 매우 강하지만, “새 데이터”에는 약합니다. 실전에서는 train 점수보다 test 점수가 더 중요하기 때문에 이 모델을 그대로 신뢰하기는 어렵습니다.

**실전 연결**

딥러닝 학습에서는 이런 상황을 training curve로 자주 확인합니다. train accuracy는 계속 올라가는데 validation accuracy나 test accuracy가 어느 순간부터 멈추거나 떨어진다면 overfitting 신호일 수 있습니다. 이때는 모델 capacity를 줄이거나, 더 많은 데이터를 모으거나, data augmentation을 하거나, dropout, weight decay 같은 regularization을 사용할 수 있습니다. LLM에서도 마찬가지입니다. 특정 benchmark나 fine-tuning 데이터에는 높은 점수를 내지만 실제 사용자 질문에서 약하다면, 모델이 일반화한 것이 아니라 특정 데이터 패턴에 과하게 맞춰졌을 가능성을 확인해야 합니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-04-29-day07.md
