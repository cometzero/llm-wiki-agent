# 2026-05-01 Day 09 AI/ML Learning Review

Source lesson: `/home/ubuntu/work/ai/learning/logs/2026-05-01-day09.md`
Follow-up answers: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-01_09-26-12.md`

---

# Lesson

# Day 09 - AI/ML 기초 학습

- Date: 2026-05-01
- Progress: 9/30
- Level: beginner-intermediate
- Milestone: 통계적 학습 이론의 직관
- Milestone goal: 모델이 데이터에 맞는 것과 일반화되는 것은 다르다는 점을 이해한다.

## Today's 3 concepts

1. 교차검증의 목적
2. 평가지표의 선택
3. 회귀와 분류의 손실 차이

---

## 1. 교차검증의 목적

### 한 줄 직관

교차검증(cross validation)은 “이 모델이 한 번 운 좋게 맞은 것인지, 여러 상황에서도 꾸준히 잘하는지”를 확인하는 연습 시험입니다.

### 개념 정의

교차검증(cross validation)은 가진 데이터를 여러 조각으로 나누고, 그 조각들을 번갈아 가며 train 데이터와 validation 데이터로 사용하는 평가 방법입니다.

보통 모델을 만들 때 데이터는 세 역할로 나뉩니다.

- train 데이터: 모델이 직접 보고 배우는 데이터
- validation 데이터: 학습 중 설정을 고를 때 확인하는 데이터
- test 데이터: 마지막에 한 번만 확인하는 최종 시험 데이터

그런데 데이터가 적으면 validation 데이터를 한 번만 나누는 것이 위험할 수 있습니다. 우연히 쉬운 validation 데이터가 걸리면 모델이 좋아 보이고, 우연히 어려운 validation 데이터가 걸리면 모델이 나빠 보일 수 있습니다.

교차검증은 이 문제를 줄이기 위해 데이터를 여러 번 다르게 나누어 봅니다. 그래서 “한 번의 운”보다 “여러 번의 평균적인 성능”을 보게 해 줍니다.

### 왜 이런 개념이 필요한가

AI 모델은 train 데이터에 너무 잘 맞을 수 있습니다. 이것을 과적합(overfitting)이라고 합니다. 예를 들어 학생이 문제집 답만 외우면, 같은 문제집에서는 100점을 받을 수 있지만 새 시험에서는 틀릴 수 있습니다.

ML에서도 비슷합니다. 모델이 train 데이터의 패턴을 배운 것이 아니라, train 데이터의 작은 잡음까지 외우면 실제 새 데이터에서 성능이 떨어집니다.

교차검증은 다음 질문에 답하려고 사용합니다.

- 이 모델은 데이터가 조금 다르게 나뉘어도 안정적인가?
- 특정 validation split에서만 잘 나온 것은 아닌가?
- hyperparameter tuning을 할 때 어떤 설정이 더 믿을 만한가?

여기서 hyperparameter는 모델이 학습으로 직접 찾는 값이 아니라 사람이 정해 주는 설정입니다. 예를 들어 learning rate, tree depth, regularization strength, batch size 같은 값입니다.

### 아주 쉬운 예시

데이터가 10개 있다고 해 봅시다.

```text
데이터 번호: 1 2 3 4 5 6 7 8 9 10
```

5-fold cross validation을 하면 데이터를 5조각(fold)으로 나눌 수 있습니다.

```text
Fold 1: 1, 2
Fold 2: 3, 4
Fold 3: 5, 6
Fold 4: 7, 8
Fold 5: 9, 10
```

이제 5번 학습합니다.

1. Fold 1을 validation으로 두고, 나머지 8개로 학습
2. Fold 2를 validation으로 두고, 나머지 8개로 학습
3. Fold 3을 validation으로 두고, 나머지 8개로 학습
4. Fold 4를 validation으로 두고, 나머지 8개로 학습
5. Fold 5를 validation으로 두고, 나머지 8개로 학습

성능이 이렇게 나왔다고 해 봅시다.

```text
Fold별 accuracy: 80%, 90%, 70%, 85%, 75%
평균: 80%
```

한 번만 봤다면 90%라고 좋아했거나, 70%라고 실망했을 수 있습니다. 하지만 5번을 보면 이 모델의 대략적인 성능은 80% 근처라고 더 차분하게 판단할 수 있습니다.

### 개념 구조와 핵심 포인트

교차검증의 핵심 구조는 다음과 같습니다.

1. 데이터를 K개의 fold로 나눈다.
2. 한 fold를 validation으로 사용한다.
3. 나머지 K-1개의 fold를 train으로 사용한다.
4. 이 과정을 K번 반복한다.
5. K개의 validation 성능을 평균 내어 모델 성능을 추정한다.

중요한 점은 모델을 K번 새로 학습한다는 것입니다. 이미 학습한 모델을 그대로 validation fold만 바꾸어 평가하는 것이 아닙니다. 매번 train fold가 달라지기 때문에 모델도 매번 새롭게 만들어집니다.

또 하나 중요한 점은 test set과 validation set을 섞으면 안 된다는 것입니다. 교차검증은 보통 train 영역 안에서 모델 선택과 hyperparameter tuning을 하기 위해 사용합니다. 최종 test set은 마지막에 한 번만 사용해야 합니다.

### 핵심 수학 포인트

교차검증은 “진짜 일반화 성능”을 직접 알 수 없기 때문에, 여러 validation 성능의 평균으로 그것을 추정합니다.

5-fold에서 validation loss가 다음과 같다고 해 봅시다.

```text
0.50, 0.40, 0.60, 0.45, 0.55
```

평균 validation loss는 다음과 같습니다.

```text
(0.50 + 0.40 + 0.60 + 0.45 + 0.55) / 5 = 0.50
```

여기서 loss는 모델의 틀림 정도입니다. loss가 낮을수록 보통 더 좋습니다.

교차검증은 평균만 보는 것이 아니라, fold마다 성능이 얼마나 흔들리는지도 봅니다. 예를 들어 두 모델이 있습니다.

```text
모델 A accuracy: 80%, 81%, 79%, 80%, 80%
모델 B accuracy: 95%, 60%, 98%, 55%, 92%
```

평균만 보면 모델 B도 좋아 보일 수 있습니다. 하지만 fold별 차이가 너무 큽니다. 이런 모델은 데이터가 조금 바뀌면 성능이 크게 흔들릴 수 있습니다. 실전에서는 평균 성능과 안정성을 같이 보는 것이 중요합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- cross validation: 데이터를 여러 방식으로 나누어 모델의 일반화 성능을 더 안정적으로 추정하는 방법
- fold: 교차검증에서 데이터를 나눈 각 조각
- K-fold cross validation: 데이터를 K개의 fold로 나누고 K번 반복 평가하는 방식
- validation set: 모델 선택이나 hyperparameter tuning에 사용하는 검증 데이터
- hyperparameter tuning: learning rate, regularization strength, tree depth처럼 사람이 정하는 설정을 바꾸며 좋은 조합을 찾는 과정
- overfitting: train 데이터에는 너무 잘 맞지만 새 데이터에는 약해지는 현상
- generalization: 모델이 처음 보는 데이터에도 잘 작동하는 능력

### AI에서 어디에 쓰이는가

전통적인 ML에서는 교차검증이 매우 자주 사용됩니다. 예를 들어 작은 tabular dataset에서 random forest, XGBoost, logistic regression의 hyperparameter를 고를 때 K-fold cross validation을 많이 씁니다.

딥러닝에서는 데이터와 모델이 크기 때문에 K번 학습하는 비용이 너무 클 수 있습니다. 큰 LLM을 5번 새로 학습하는 것은 현실적으로 거의 불가능합니다. 그래서 큰 딥러닝에서는 고정된 validation set을 두고 실험하는 경우가 많습니다.

그래도 교차검증의 생각은 여전히 중요합니다. LLM 평가에서도 하나의 benchmark 점수만 믿으면 위험합니다. 여러 dataset, 여러 task, 여러 prompt 형식에서 확인해야 합니다. 이것은 넓은 의미에서 “한 번의 평가 split에 속지 말자”는 교차검증의 정신과 같습니다.

embedding 모델을 평가할 때도 마찬가지입니다. 어떤 검색 dataset에서는 잘하지만 다른 도메인에서는 약할 수 있습니다. 그래서 여러 domain의 validation 결과를 보는 것이 중요합니다.

### 헷갈리기 쉬운 포인트

- 교차검증은 모델 성능을 올리는 마법이 아닙니다. 성능을 더 믿을 만하게 측정하는 방법입니다.
- 교차검증 결과가 좋다고 test set을 계속 봐도 된다는 뜻은 아닙니다. test set은 최종 확인용입니다.
- fold 수가 많을수록 항상 좋은 것은 아닙니다. K가 크면 학습을 더 많이 해야 해서 시간이 오래 걸립니다.
- 딥러닝에서는 계산 비용 때문에 full K-fold를 잘 안 쓰는 경우도 많습니다. 하지만 validation을 여러 관점에서 봐야 한다는 원리는 매우 중요합니다.

---

## 2. 평가지표의 선택

### 한 줄 직관

평가지표(metric)는 “무엇을 잘했다고 볼 것인가”를 정하는 기준입니다.

### 개념 정의

평가지표(metric)는 모델의 성능을 숫자로 표현하는 방법입니다. 같은 모델이라도 어떤 metric을 보느냐에 따라 좋아 보일 수도 있고 나빠 보일 수도 있습니다.

예를 들어 분류(classification) 문제에서 accuracy는 전체 중 몇 개를 맞혔는지 보는 지표입니다. 하지만 어떤 상황에서는 accuracy만 보면 큰 착각을 할 수 있습니다. 특히 한 클래스가 훨씬 많은 불균형 데이터(imbalanced data)에서는 accuracy가 매우 위험할 수 있습니다.

그래서 classification에서는 accuracy뿐 아니라 precision, recall, F1, AUROC 같은 지표를 함께 봅니다.

### 왜 이런 개념이 필요한가

모델의 목적은 문제마다 다릅니다.

스팸 메일 탐지에서는 정상 메일을 스팸으로 잘못 보내는 것이 큰 문제일 수 있습니다. 반대로 암 진단 보조 모델에서는 실제 환자를 놓치는 것이 훨씬 큰 문제일 수 있습니다.

두 문제 모두 “맞히기” 문제처럼 보이지만, 중요한 실수의 종류가 다릅니다.

- 스팸 탐지: 정상 메일을 스팸이라고 하는 실수를 줄이고 싶다.
- 질병 탐지: 아픈 사람을 건강하다고 하는 실수를 줄이고 싶다.

평가지표는 모델이 어떤 종류의 실수를 덜 하도록 선택하고 비교할지 정하는 도구입니다. 지표를 잘못 고르면 모델 개발 방향도 잘못됩니다.

### 아주 쉬운 예시

100명의 사람이 있고, 실제로 병에 걸린 사람은 5명이라고 해 봅시다.

어떤 모델이 모든 사람에게 “정상”이라고 예측했습니다.

```text
전체 100명 중 정상 95명, 환자 5명
모델 예측: 전부 정상
```

이 모델의 accuracy는 95%입니다. 왜냐하면 정상 95명은 맞혔기 때문입니다.

하지만 이 모델은 환자 5명을 한 명도 찾지 못했습니다. 질병 탐지 모델로는 매우 나쁩니다.

이때 recall을 봐야 합니다.

```text
recall = 실제 환자 중 모델이 환자라고 찾은 비율
```

실제 환자 5명 중 찾은 환자가 0명이므로 recall은 0%입니다.

accuracy 95%만 보면 좋아 보이지만, recall 0%를 보면 실제 목적에는 실패했다는 것을 알 수 있습니다.

### 개념 구조와 핵심 포인트

분류 문제에서는 예측과 정답을 4가지로 나누어 생각합니다. 예를 들어 “환자”를 positive라고 합시다.

- TP(True Positive): 실제 환자를 환자라고 맞힘
- TN(True Negative): 실제 정상인을 정상이라고 맞힘
- FP(False Positive): 실제 정상인을 환자라고 잘못 예측
- FN(False Negative): 실제 환자를 정상이라고 잘못 예측

여기서 주요 metric은 다음처럼 만들어집니다.

- accuracy: 전체 중 맞힌 비율
- precision: 모델이 positive라고 한 것 중 진짜 positive인 비율
- recall: 실제 positive 중 모델이 찾아낸 비율
- F1: precision과 recall의 균형을 보는 지표
- AUROC: threshold를 바꿔 가며 positive와 negative를 얼마나 잘 구분하는지 보는 지표

중요한 점은 “어떤 실수가 더 비싼가”입니다. FP가 더 위험한 문제도 있고, FN이 더 위험한 문제도 있습니다.

### 핵심 수학 포인트

아주 작은 숫자로 봅시다.

```text
실제 환자 4명, 실제 정상 6명
모델 결과:
TP = 3
TN = 5
FP = 1
FN = 1
```

accuracy는 전체 10명 중 맞힌 8명입니다.

```text
accuracy = (TP + TN) / 전체 = (3 + 5) / 10 = 0.8
```

precision은 모델이 환자라고 말한 4명 중 진짜 환자 3명입니다.

```text
precision = TP / (TP + FP) = 3 / (3 + 1) = 0.75
```

recall은 실제 환자 4명 중 찾아낸 3명입니다.

```text
recall = TP / (TP + FN) = 3 / (3 + 1) = 0.75
```

F1은 precision과 recall을 하나로 합친 값입니다. 단순 평균이 아니라 harmonic mean을 씁니다.

```text
F1 = 2 × precision × recall / (precision + recall)
   = 2 × 0.75 × 0.75 / (0.75 + 0.75)
   = 0.75
```

AUROC는 조금 다르게 생각합니다. 모델이 “환자일 확률” 같은 점수를 낸다고 합시다. threshold를 0.5로 두면 0.5 이상을 환자라고 할 수 있고, threshold를 0.3으로 낮추면 더 많은 사람을 환자라고 할 수 있습니다. AUROC는 threshold를 여러 개로 바꾸면서 모델이 positive를 negative보다 높은 점수로 잘 배치하는지를 봅니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- accuracy: 전체 예측 중 맞힌 비율
- precision: 모델이 positive라고 예측한 것 중 실제 positive의 비율
- recall: 실제 positive 중 모델이 positive로 찾아낸 비율
- F1: precision과 recall의 균형을 보는 지표
- AUROC: 여러 threshold에서 positive와 negative를 구분하는 능력을 요약한 지표
- threshold: 확률 점수를 class로 바꾸는 기준값
- TP, TN, FP, FN: 분류 결과를 네 종류로 나누는 기본 용어
- imbalanced data: class 비율이 크게 치우친 데이터

### AI에서 어디에 쓰이는가

실전 AI에서는 metric 선택이 모델 선택만큼 중요합니다.

검색 모델이나 추천 모델에서는 “사용자가 원하는 것을 위쪽에 보여 주는가”가 중요합니다. 이때는 accuracy보다 ranking metric이 더 중요할 수 있습니다.

LLM에서도 metric 선택은 쉽지 않습니다. 요약 모델을 평가할 때 단순히 단어가 겹치는지만 보면, 의미는 좋은데 표현이 다른 답을 나쁘게 평가할 수 있습니다. 반대로 표현은 비슷하지만 사실이 틀린 답을 좋게 평가할 수도 있습니다.

classification head를 붙인 transformer 모델에서는 출력 logit을 softmax로 확률처럼 바꾼 뒤, threshold를 정해 class를 결정합니다. 이때 threshold를 바꾸면 precision과 recall이 달라집니다. 그래서 모델 구조만큼이나 threshold와 metric 선택이 중요합니다.

embedding search에서도 “정답 문서가 top-1에 있는가”, “top-5 안에 있는가”, “비슷한 문서를 얼마나 위에 놓는가”처럼 문제에 맞는 metric을 고릅니다.

### 헷갈리기 쉬운 포인트

- accuracy가 높다고 항상 좋은 모델은 아닙니다. class imbalance가 있으면 특히 조심해야 합니다.
- precision과 recall은 서로 trade-off가 생기는 경우가 많습니다. threshold를 낮추면 더 많이 잡아서 recall은 오르지만 precision은 떨어질 수 있습니다.
- AUROC가 높아도 특정 threshold에서의 성능이 목적에 맞지 않을 수 있습니다.
- F1은 precision과 recall을 균형 있게 보지만, 모든 문제에 정답인 metric은 아닙니다.
- metric은 단순한 보고용 숫자가 아니라 모델 개발 방향을 정하는 나침반입니다.

---

## 3. 회귀와 분류의 손실 차이

### 한 줄 직관

회귀(regression)는 “숫자가 얼마나 떨어져 있는지”를 벌점으로 주고, 분류(classification)는 “정답 class에 얼마나 확신을 줬는지”를 벌점으로 줍니다.

### 개념 정의

손실(loss)은 모델이 얼마나 틀렸는지를 나타내는 숫자입니다. 학습 중 optimizer는 이 loss를 줄이도록 모델 파라미터를 업데이트합니다.

회귀(regression)는 연속적인 숫자를 예측하는 문제입니다. 예를 들어 집값 3억 2천만 원, 온도 22.5도, 배송 시간 3.7일 같은 값을 예측합니다.

분류(classification)는 class를 예측하는 문제입니다. 예를 들어 고양이/강아지, 스팸/정상, 긍정/부정 같은 범주를 맞힙니다.

회귀와 분류는 예측의 형태가 다르기 때문에 loss도 다르게 설계합니다.

- regression loss: 예측 숫자와 실제 숫자의 거리 중심
- classification loss: 정답 class에 준 확률 또는 점수 중심

### 왜 이런 개념이 필요한가

모델 학습은 loss가 알려 주는 방향으로 움직입니다. loss가 잘못 설계되면 모델은 엉뚱한 방향으로 열심히 학습합니다.

예를 들어 집값을 예측하는데 “class가 맞았는지”만 보는 loss를 쓰면 숫자의 차이를 제대로 반영하기 어렵습니다. 3억을 3억 1천만 원으로 예측한 것과 10억으로 예측한 것은 모두 틀렸지만, 틀린 정도가 완전히 다릅니다.

반대로 고양이/강아지 분류에서 숫자 거리만 단순히 보면, “정답 class에 확률을 높게 주는 것”이라는 분류의 핵심을 잘 다루기 어렵습니다.

loss는 gradient를 만듭니다. gradient는 파라미터를 어느 방향으로 바꿔야 loss가 줄어드는지 알려 주는 신호입니다. 그래서 loss 선택은 optimizer가 받는 학습 신호를 결정합니다.

### 아주 쉬운 예시

#### 회귀 예시

실제 온도가 20도인데 모델이 18도를 예측했다고 합시다.

```text
정답 y = 20
예측 ŷ = 18
오차 = ŷ - y = -2
```

MSE는 오차를 제곱합니다.

```text
MSE = (-2)^2 = 4
```

MAE는 오차의 절댓값을 봅니다.

```text
MAE = |-2| = 2
```

MSE는 큰 오차를 더 강하게 벌줍니다. 예를 들어 오차가 5이면 MSE는 25가 됩니다.

#### 분류 예시

정답이 “고양이”인데 모델이 이렇게 확률을 냈다고 합시다.

```text
고양이: 0.8
강아지: 0.2
```

정답 class인 고양이에 0.8이라는 높은 확률을 줬으므로 loss가 작습니다.

반대로 이렇게 예측하면 어떨까요?

```text
고양이: 0.1
강아지: 0.9
```

정답 class인 고양이에 0.1만 줬으므로 loss가 큽니다. cross entropy 또는 log loss는 정답 class에 준 확률이 낮을수록 큰 벌점을 줍니다.

### 개념 구조와 핵심 포인트

회귀의 대표 loss는 다음과 같습니다.

- MSE(Mean Squared Error): 오차를 제곱해서 평균
- MAE(Mean Absolute Error): 오차의 절댓값을 평균

분류의 대표 loss는 다음과 같습니다.

- cross entropy: 정답 분포와 모델 예측 분포의 차이를 측정하는 loss
- log loss: binary classification이나 probabilistic classification에서 자주 쓰는 이름으로, cross entropy와 밀접하게 연결됨

회귀는 보통 출력이 숫자 하나 또는 여러 개입니다.

```text
집값 예측 출력: [3.2]
좌표 예측 출력: [x, y]
```

분류는 보통 class 개수만큼 score 또는 logit을 냅니다.

```text
고양이/강아지/토끼 분류 logits: [2.1, 0.3, -1.2]
softmax 후 확률: [0.82, 0.14, 0.04]
```

여기서 logit은 softmax를 통과하기 전의 원래 점수입니다. softmax는 여러 logit을 합이 1인 확률처럼 바꾸는 함수입니다.

### 핵심 수학 포인트

#### MSE

데이터가 3개 있다고 해 봅시다.

```text
정답:  [10, 20, 30]
예측:  [12, 18, 33]
오차:  [ 2, -2,  3]
제곱:  [ 4,  4,  9]
```

MSE는 제곱 오차의 평균입니다.

```text
MSE = (4 + 4 + 9) / 3 = 17 / 3 ≈ 5.67
```

MSE는 큰 오차를 더 크게 벌합니다. 그래서 outlier에 민감할 수 있습니다.

#### MAE

같은 예시에서 절댓값 오차는 다음과 같습니다.

```text
절댓값 오차: [2, 2, 3]
MAE = (2 + 2 + 3) / 3 = 7 / 3 ≈ 2.33
```

MAE는 오차 크기를 더 직관적으로 보여 줍니다. 평균적으로 2.33 정도 틀렸다고 읽기 쉽습니다.

#### Cross entropy / log loss

정답 class가 고양이라고 합시다. 모델이 고양이에 준 확률을 p라고 하면, 간단한 형태의 loss는 다음과 같습니다.

```text
loss = -log(p)
```

p가 0.9이면 loss는 작습니다.

```text
-log(0.9) ≈ 0.105
```

p가 0.1이면 loss는 큽니다.

```text
-log(0.1) ≈ 2.303
```

즉 cross entropy는 정답 class에 높은 확률을 주도록 모델을 강하게 밀어 줍니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- MSE(Mean Squared Error): 오차를 제곱한 뒤 평균 내는 regression loss
- MAE(Mean Absolute Error): 오차의 절댓값을 평균 내는 regression loss
- cross entropy: 정답 class에 낮은 확률을 주면 큰 벌점을 주는 classification loss
- log loss: 확률 예측의 틀림 정도를 log로 벌점화하는 loss
- regression: 연속적인 숫자를 예측하는 문제
- classification: 정해진 class 중 하나 또는 여러 개를 예측하는 문제
- logit: softmax나 sigmoid에 들어가기 전의 모델 출력 점수
- softmax: 여러 class 점수를 확률처럼 합이 1이 되게 바꾸는 함수
- gradient: loss를 줄이기 위해 파라미터를 어느 방향으로 바꿀지 알려 주는 변화 신호
- optimizer: gradient를 이용해 파라미터를 업데이트하는 알고리즘

### AI에서 어디에 쓰이는가

딥러닝 학습 코드는 대부분 loss를 중심으로 돌아갑니다.

이미지 분류 모델은 보통 cross entropy loss를 씁니다. 모델은 각 class의 logit을 만들고, softmax를 통해 정답 class 확률을 높이도록 학습합니다.

언어모델(LLM)도 기본적으로 다음 token을 맞히는 classification 문제로 학습됩니다. vocabulary에 있는 수많은 token 중 다음 token이 무엇인지 맞히는 것입니다. 예를 들어 “나는 밥을” 다음에 올 token이 “먹었다”라면, 모델은 vocabulary 전체에 대한 logit을 만들고, 정답 token의 확률을 높이도록 cross entropy loss를 줄입니다.

회귀 loss도 AI에서 많이 쓰입니다. 예를 들어 object detection에서 bounding box 좌표를 예측할 때, 좌표 차이를 줄이는 regression loss가 들어갑니다. 추천 시스템에서 평점 1~5점을 예측하거나, 시계열 모델에서 다음 온도나 수요량을 예측할 때도 regression loss를 씁니다.

embedding 학습에서는 contrastive loss처럼 다른 종류의 loss도 쓰지만, 핵심은 같습니다. loss가 “무엇을 가까이 두고, 무엇을 멀리 둘지”를 정하고, gradient가 embedding 공간을 그 방향으로 바꿉니다.

### 헷갈리기 쉬운 포인트

- loss와 metric은 다릅니다. loss는 학습 중 optimizer가 줄이는 값이고, metric은 사람이 성능을 해석하기 위해 보는 값입니다. 물론 같은 값을 둘 다로 쓸 수도 있지만 역할은 구분해야 합니다.
- regression에는 보통 MSE나 MAE를 쓰고, classification에는 보통 cross entropy를 씁니다. 문제 형태가 다르면 loss도 달라져야 합니다.
- MSE는 큰 오차에 민감합니다. outlier가 많으면 MAE나 다른 robust loss를 고려할 수 있습니다.
- cross entropy는 “맞았냐 틀렸냐”만 보는 것이 아니라, 정답 class에 얼마나 높은 확률을 줬는지도 봅니다.
- LLM의 next token prediction은 겉보기에는 문장 생성이지만, 학습 관점에서는 매우 큰 classification 문제입니다.

---

## 복습 질문 3개

1. 교차검증(cross validation)은 왜 validation set을 한 번만 나누는 것보다 더 안정적인 평가를 줄 수 있을까요?
2. accuracy가 95%인 모델이 실제로는 나쁜 모델일 수 있는 상황을 하나 설명해 보세요.
3. 회귀(regression) 문제와 분류(classification) 문제에서 사용하는 loss가 왜 달라야 할까요?

## 오늘의 한 줄 요약

모델을 잘 만든다는 것은 train 데이터에만 맞추는 것이 아니라, 적절한 검증 방법과 평가지표와 loss를 선택해 새 데이터에서도 믿을 수 있게 작동하도록 만드는 것입니다.

---

# Follow-up Answers

[AI/ML 오늘의 복습 정답 Day 09/30]

오늘은 “모델이 진짜 잘하는지 어떻게 믿을 수 있게 확인할까?”에 대한 복습입니다.

### 1. 교차검증(cross validation)은 왜 validation set을 한 번만 나누는 것보다 더 안정적인 평가를 줄 수 있을까요?

**정답**

교차검증은 데이터를 여러 번 다른 방식으로 나누어 평가하기 때문에, 한 번의 운 좋은 split 또는 운 나쁜 split에 덜 흔들립니다.

즉, validation set을 한 번만 나누면 그 validation set이 우연히 너무 쉽거나 너무 어려울 수 있습니다. 하지만 cross validation은 여러 fold에서 성능을 확인하고 평균을 보기 때문에 모델의 일반화 성능을 더 안정적으로 추정할 수 있습니다.

**설명**

모델을 평가할 때 우리가 진짜 알고 싶은 것은 “이 모델이 처음 보는 새 데이터에서도 잘할까?”입니다. 이것을 generalization, 즉 일반화 능력이라고 합니다.

그런데 validation set을 딱 한 번만 나누면 문제가 생길 수 있습니다. 예를 들어 validation 데이터가 우연히 쉬운 샘플들로만 구성되면 모델 성능이 실제보다 좋아 보입니다. 반대로 우연히 어려운 샘플들만 들어가면 모델이 실제보다 나빠 보일 수 있습니다.

교차검증은 이 위험을 줄이기 위해 데이터를 여러 조각, 즉 fold로 나눕니다. 그리고 각 fold를 돌아가면서 validation set으로 사용합니다. 이렇게 하면 모델이 여러 데이터 조합에서 얼마나 꾸준히 잘하는지 볼 수 있습니다.

중요한 점은 교차검증이 모델 성능을 마법처럼 올려 주는 방법은 아니라는 것입니다. 성능을 더 믿을 만하게 측정하는 방법입니다.

**예시**

데이터가 10개 있고, 5-fold cross validation을 한다고 해 봅시다.

각 fold의 accuracy가 이렇게 나왔습니다.

```text
Fold별 accuracy: 80%, 90%, 70%, 85%, 75%
평균 accuracy: 80%
```

만약 한 번만 평가해서 90%가 나왔다면 “이 모델 정말 좋다”고 착각할 수 있습니다. 반대로 70%만 봤다면 “이 모델 별로다”라고 너무 빨리 판단할 수 있습니다.

하지만 여러 번 나누어 보니 평균은 80%입니다. 그래서 “이 모델은 대략 80% 정도의 성능을 기대할 수 있구나”라고 더 차분하고 안정적으로 판단할 수 있습니다.

**실전 연결**

전통적인 ML에서는 XGBoost, random forest, logistic regression 같은 모델의 hyperparameter tuning에 cross validation을 자주 씁니다. 예를 들어 tree depth나 regularization strength를 바꿔 가며 여러 fold에서 평균 성능이 좋은 설정을 고릅니다.

딥러닝이나 LLM에서는 모델을 여러 번 새로 학습하는 비용이 너무 커서 full K-fold를 자주 쓰지는 않습니다. 하지만 “하나의 validation 점수만 믿지 말자”는 생각은 여전히 중요합니다. LLM도 하나의 benchmark만 잘한다고 좋은 모델이라고 단정하기 어렵고, 여러 task, 여러 dataset, 여러 prompt 형식에서 평가해야 합니다.

---

### 2. accuracy가 95%인 모델이 실제로는 나쁜 모델일 수 있는 상황을 하나 설명해 보세요.

**정답**

데이터가 심하게 불균형한 상황에서는 accuracy가 95%여도 나쁜 모델일 수 있습니다.

예를 들어 100명 중 실제 환자가 5명이고 정상인이 95명인 질병 탐지 문제에서, 모델이 모든 사람을 “정상”이라고 예측하면 accuracy는 95%입니다. 하지만 환자 5명을 한 명도 찾지 못했으므로 실제로는 매우 나쁜 모델입니다.

**설명**

Accuracy는 전체 예측 중 맞힌 비율입니다. 계산하기 쉽고 직관적이지만, class imbalance가 있을 때는 위험할 수 있습니다.

Class imbalance는 한쪽 class가 다른 class보다 훨씬 많은 상황입니다. 예를 들어 정상 메일은 99개이고 스팸 메일은 1개뿐인 경우, 또는 정상 환자는 95명이고 실제 환자는 5명뿐인 경우입니다.

이런 상황에서 모델이 항상 많은 쪽 class만 예측해도 accuracy가 높게 나올 수 있습니다. 하지만 우리가 정말 찾고 싶은 소수 class를 전혀 찾지 못할 수 있습니다.

질병 탐지에서는 실제 환자를 놓치는 것, 즉 FN(False Negative)이 매우 위험합니다. 그래서 accuracy만 보면 안 되고 recall을 꼭 봐야 합니다.

Recall은 실제 positive 중 모델이 positive로 찾아낸 비율입니다. 질병 탐지에서 positive를 “환자”라고 하면, recall은 실제 환자 중 몇 명을 환자로 잡아냈는지를 의미합니다.

**예시**

100명 중 실제 환자가 5명, 정상인이 95명이라고 해 봅시다.

모델이 이렇게 예측했습니다.

```text
실제 정상: 95명
실제 환자: 5명

모델 예측: 전부 정상
```

이 경우 정상 95명은 맞혔으므로 accuracy는 95%입니다.

```text
accuracy = 95 / 100 = 95%
```

하지만 실제 환자 5명은 모두 놓쳤습니다.

```text
recall = 찾은 환자 수 / 실제 환자 수
recall = 0 / 5 = 0%
```

즉 accuracy는 95%로 좋아 보이지만, recall은 0%입니다. 질병 탐지 모델로는 실패한 모델입니다.

**실전 연결**

실전 ML에서는 metric 선택이 모델의 개발 방향을 정합니다. 암 진단 보조 모델, 사기 거래 탐지, 보안 침입 탐지처럼 드문 사건을 찾는 문제에서는 accuracy만 보면 위험합니다.

이런 문제에서는 precision, recall, F1, AUROC 등을 함께 봐야 합니다. 특히 실제 positive를 놓치면 큰 문제가 되는 경우에는 recall이 중요합니다.

LLM이나 검색 시스템에서도 비슷합니다. 단순히 “전체적으로 몇 개를 맞혔는가”보다, 중요한 답을 놓치지 않는지, 위험한 답을 얼마나 줄이는지, 관련 문서를 top-k 안에 잘 올리는지가 더 중요할 수 있습니다. 그래서 metric은 단순한 숫자가 아니라 “무엇을 좋은 모델이라고 볼 것인가”를 정하는 기준입니다.

---

### 3. 회귀(regression) 문제와 분류(classification) 문제에서 사용하는 loss가 왜 달라야 할까요?

**정답**

회귀와 분류는 예측하려는 대상의 형태가 다르기 때문에 loss도 달라야 합니다.

회귀는 연속적인 숫자를 예측하는 문제이므로, 예측값과 정답 숫자가 얼마나 떨어져 있는지를 벌점으로 줍니다. 그래서 MSE나 MAE 같은 loss를 씁니다.

분류는 정해진 class 중 하나를 맞히는 문제이므로, 정답 class에 얼마나 높은 확률을 주었는지를 벌점으로 봅니다. 그래서 cross entropy 또는 log loss를 씁니다.

**설명**

Loss는 모델이 얼마나 틀렸는지를 나타내는 숫자입니다. 학습 중 optimizer는 이 loss를 줄이는 방향으로 모델 파라미터를 업데이트합니다.

그래서 loss는 단순한 평가 숫자가 아닙니다. 모델이 어떤 방향으로 배울지를 정하는 학습 신호입니다.

회귀 문제에서는 “얼마나 떨어졌는가”가 중요합니다. 예를 들어 실제 집값이 3억 원인데 모델이 3억 1천만 원이라고 예측한 것과 10억 원이라고 예측한 것은 둘 다 틀렸지만, 틀린 정도가 완전히 다릅니다. 그래서 숫자 거리 기반의 loss가 필요합니다.

분류 문제에서는 숫자 거리보다 “정답 class에 확률을 얼마나 주었는가”가 중요합니다. 예를 들어 정답이 고양이인데 모델이 고양이에 0.9의 확률을 주면 잘한 것입니다. 반대로 고양이에 0.1만 주고 강아지에 0.9를 주면 크게 틀린 것입니다.

이 차이 때문에 회귀에는 MSE, MAE를 쓰고, 분류에는 cross entropy나 log loss를 주로 씁니다.

**예시**

회귀 예시를 먼저 봅시다.

실제 온도가 20도인데 모델이 18도를 예측했습니다.

```text
정답: 20
예측: 18
오차: -2
```

MSE는 오차를 제곱합니다.

```text
MSE = (-2)^2 = 4
```

MAE는 오차의 절댓값을 봅니다.

```text
MAE = |-2| = 2
```

즉 회귀 loss는 “숫자가 얼마나 떨어졌는가”를 봅니다.

이번에는 분류 예시입니다.

정답이 고양이인데 모델이 이렇게 예측했습니다.

```text
고양이: 0.8
강아지: 0.2
```

정답 class인 고양이에 높은 확률을 줬으므로 loss가 작습니다.

반대로 이렇게 예측하면 loss가 큽니다.

```text
고양이: 0.1
강아지: 0.9
```

정답인 고양이에 낮은 확률을 주었기 때문입니다. Cross entropy는 이런 경우 큰 벌점을 줍니다.

**실전 연결**

딥러닝에서는 loss function 선택이 매우 중요합니다. 이미지 분류 모델은 보통 class별 logit을 출력하고, softmax로 확률처럼 바꾼 뒤 cross entropy loss를 줄이도록 학습합니다.

LLM도 기본적으로 다음 token을 맞히는 거대한 classification 문제로 학습됩니다. vocabulary 안에 있는 수많은 token 중 다음 token이 무엇인지 맞히는 방식입니다. 그래서 LLM 학습에서도 cross entropy loss가 핵심적으로 사용됩니다.

반대로 object detection에서 bounding box 좌표를 예측하거나, 시계열 모델에서 다음 온도나 수요량을 예측하거나, 추천 시스템에서 평점을 예측하는 경우에는 숫자 차이가 중요합니다. 이런 경우에는 MSE, MAE 또는 변형된 regression loss를 사용합니다.

결국 loss는 모델에게 “무엇을 틀렸다고 볼 것인가”를 알려 주는 기준입니다. 문제 형태가 다르면 틀림의 의미도 다르기 때문에, loss도 달라져야 합니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-01-day09.md
