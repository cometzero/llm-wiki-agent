# AI/ML Learning Review — Day 17 (2026-05-09)

## Source Metadata
- Lesson file: `/home/ubuntu/work/ai/learning/logs/2026-05-09-day17.md`
- Follow-up answer file: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-09_09-25-53.md`

## Lesson

# Day 17 - AI/ML 기초 학습

- Date: 2026-05-09
- Progress: 17/30
- Level: beginner-intermediate
- Milestone: 딥러닝 학습 기법과 CNN
- Milestone goal: 실제 딥러닝 학습을 안정화하는 방법과 CNN의 구조적 아이디어를 익힌다.

## Today's 3 concepts

1. 학습 곡선 해석
2. CNN의 지역 연결성
3. 합성곱 연산의 의미

---

## 1. 학습 곡선 해석

### 한 줄 직관

학습 곡선(learning curve)은 모델이 공부를 잘하고 있는지, 외우기만 하는지, 아직 덜 배웠는지를 보여주는 “훈련 성적표의 시간 변화 그래프”입니다.

### 개념 정의

학습 곡선(learning curve)은 학습이 진행될 때 train loss와 validation loss가 어떻게 변하는지 그린 그래프입니다.

- train loss: 모델이 훈련 데이터에서 얼마나 틀렸는지 나타내는 값입니다.
- validation loss: 모델이 훈련 때 직접 보지 않은 검증 데이터에서 얼마나 틀렸는지 나타내는 값입니다.
- loss는 “틀린 정도”라고 생각하면 됩니다. 보통 낮을수록 좋습니다.

예를 들어 고양이/강아지 사진 분류 모델을 학습한다고 해봅시다. 모델은 훈련 사진을 보면서 점점 답을 맞히는 법을 배웁니다. 이때 훈련 사진에 대한 오답 정도가 train loss입니다. 반면 검증 사진은 시험 문제처럼 따로 빼둔 데이터입니다. 여기에 대한 오답 정도가 validation loss입니다.

학습 곡선을 해석한다는 것은 단순히 “loss가 내려갔다”를 보는 것이 아닙니다. train loss와 validation loss의 관계를 보면서 모델의 상태를 판단하는 것입니다.

### 왜 이런 개념이 필요한가

딥러닝 모델은 학습을 오래 한다고 항상 좋아지지 않습니다.

사람 공부로 비유하면 이렇습니다.

- 기출문제를 전혀 못 푸는 상태: 아직 덜 배운 상태입니다.
- 기출문제도 잘 풀고 새 문제도 잘 푸는 상태: 잘 일반화(generalization)한 상태입니다.
- 기출문제만 거의 외워서 잘 풀고 새 문제는 못 푸는 상태: 과적합(overfitting)입니다.

학습 곡선은 이 차이를 눈으로 보게 해줍니다. 특히 딥러닝에서는 epoch를 여러 번 돌리면서 모델이 계속 변합니다. epoch는 전체 훈련 데이터를 한 번 다 본 단위입니다. 학습 곡선을 보면 “지금 더 학습해야 하는지”, “이쯤에서 멈춰야 하는지”, “모델이 너무 단순한지”, “데이터가 부족한지”를 판단할 수 있습니다.

실전에서는 이 판단이 매우 중요합니다. LLM fine-tuning, 이미지 모델 학습, 추천 모델 학습 모두에서 train loss만 보고 계속 학습하면 모델이 훈련 데이터 문장이나 패턴을 외울 수 있습니다. 그러면 실제 사용자 입력에서는 성능이 나빠질 수 있습니다.

### 아주 쉬운 예시

아주 작은 숫자 예시를 보겠습니다.

| epoch | train loss | validation loss | 해석 |
|---:|---:|---:|---|
| 1 | 1.00 | 1.10 | 아직 많이 틀립니다. |
| 2 | 0.70 | 0.80 | 둘 다 좋아지고 있습니다. |
| 3 | 0.50 | 0.60 | 학습이 잘 진행 중입니다. |
| 4 | 0.35 | 0.58 | train은 더 좋아졌지만 validation 개선은 작습니다. |
| 5 | 0.20 | 0.75 | 훈련 데이터만 외우기 시작했을 수 있습니다. |

여기서 epoch 5는 겉으로 보면 train loss가 0.20으로 매우 좋습니다. 하지만 validation loss는 0.75로 다시 커졌습니다. 즉, 모델이 훈련 문제는 잘 맞히지만 새 문제에는 약해진 것입니다.

이럴 때는 epoch 3이나 4 근처의 모델을 선택하는 것이 더 좋을 수 있습니다. 이런 아이디어가 early stopping입니다.

### 개념 구조와 핵심 포인트

학습 곡선에서 자주 보는 패턴은 크게 세 가지입니다.

1. train loss와 validation loss가 둘 다 높다
   - 모델이 아직 충분히 배우지 못했습니다.
   - underfitting일 가능성이 있습니다.
   - 해결 방법으로는 더 오래 학습, 모델 크기 증가, 더 좋은 feature, learning rate 조정 등을 생각할 수 있습니다.

2. train loss는 낮은데 validation loss가 높다
   - 훈련 데이터에 너무 맞춰졌습니다.
   - overfitting일 가능성이 큽니다.
   - 해결 방법으로는 더 많은 데이터, regularization, dropout, data augmentation, early stopping 등을 생각할 수 있습니다.

3. train loss와 validation loss가 같이 내려가다가 validation loss가 멈추거나 올라간다
   - 처음에는 잘 배우다가 어느 시점부터 외우기 시작하는 전형적인 모습입니다.
   - validation loss가 가장 낮았던 시점의 모델을 저장하는 방식이 자주 쓰입니다.

여기서 중요한 점은 train loss 하나만 보면 안 된다는 것입니다. train loss는 모델이 “공부한 문제집”에서 얻은 점수입니다. validation loss는 “새 시험지”에서 얻은 점수입니다. 우리가 원하는 모델은 공부한 문제만 잘 푸는 모델이 아니라 새 입력에도 잘 반응하는 모델입니다.

### 핵심 수학 포인트

loss는 모델 예측값과 정답의 차이를 숫자로 만든 것입니다.

가장 단순한 예로 회귀 문제에서 정답이 10이고 모델 예측이 8이라고 해봅시다.

- 오차(error) = 예측값 - 정답 = 8 - 10 = -2
- 제곱 오차(squared error) = (-2)^2 = 4

여러 데이터에 대해 이 값을 평균내면 평균 제곱 오차(MSE, mean squared error)가 됩니다.

분류 문제에서는 cross-entropy loss가 자주 쓰입니다. 직관적으로는 “정답에 얼마나 낮은 확률을 줬는가”를 벌점으로 주는 방식입니다.

예를 들어 정답이 고양이인데 모델이 고양이 확률을 0.9로 주면 loss가 작습니다. 정답이 고양이인데 고양이 확률을 0.1로 주면 loss가 큽니다.

학습 곡선의 수학적 의미는 이 loss 값이 epoch에 따라 어떻게 바뀌는지를 보는 것입니다. optimizer는 gradient를 이용해 loss를 줄이는 방향으로 weight를 업데이트합니다. 그런데 train loss만 계속 줄이면 모델의 weight가 훈련 데이터의 세부 잡음까지 맞추도록 변할 수 있습니다. 그래서 validation loss를 함께 봐야 합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- learning curve: epoch 또는 step에 따라 loss나 accuracy가 어떻게 변하는지 나타낸 그래프입니다.
- train loss: 훈련 데이터에서 계산한 loss입니다. 모델이 본 데이터에 대한 성적입니다.
- validation loss: 검증 데이터에서 계산한 loss입니다. 모델이 보지 않은 데이터에 대한 성적입니다.
- early stopping: validation loss가 더 이상 좋아지지 않으면 학습을 일찍 멈추는 방법입니다.

### AI에서 어디에 쓰이는가

학습 곡선은 거의 모든 모델 학습에서 쓰입니다.

- 이미지 분류 CNN 학습: train accuracy는 오르는데 validation accuracy가 떨어지면 overfitting을 의심합니다.
- LLM fine-tuning: train loss만 계속 내려가도 실제 대화 품질이 나빠질 수 있습니다. 특정 답변 스타일을 과하게 외울 수 있기 때문입니다.
- embedding 모델 학습: 훈련 pair에서는 비슷한 문장끼리 잘 붙지만, 새로운 문장에서는 embedding 품질이 나빠질 수 있습니다.
- hyperparameter tuning: learning rate, batch size, 모델 크기, dropout 등을 바꿨을 때 학습 곡선 모양을 비교합니다.

실무에서는 TensorBoard, Weights & Biases, MLflow 같은 도구로 train loss와 validation loss를 계속 기록합니다. 좋은 엔지니어는 최종 숫자만 보지 않고 곡선의 모양을 봅니다.

### 헷갈리기 쉬운 포인트

- train loss가 낮다고 항상 좋은 모델은 아닙니다. 훈련 데이터를 외웠을 수도 있습니다.
- validation loss가 한두 번 튀었다고 바로 망한 것은 아닙니다. mini-batch 구성이나 데이터 난이도 때문에 조금 흔들릴 수 있습니다.
- early stopping은 “빨리 포기”가 아니라 “새 데이터 성능이 가장 좋을 때 멈추는 전략”입니다.
- loss와 accuracy는 다릅니다. accuracy가 같아도 모델이 정답에 주는 확신이 다르면 loss는 달라질 수 있습니다.

---

## 2. CNN의 지역 연결성

### 한 줄 직관

CNN의 지역 연결성(local receptive field)은 이미지를 한 번에 통째로 보지 않고, 가까운 픽셀끼리 먼저 작은 패턴을 찾는 방식입니다.

### 개념 정의

CNN(Convolutional Neural Network)은 이미지처럼 공간 구조가 있는 데이터를 잘 처리하기 위해 만든 neural network 구조입니다.

일반적인 fully connected layer는 입력의 모든 값과 출력의 모든 값이 연결됩니다. 예를 들어 28x28 이미지가 있으면 픽셀 수는 784개입니다. fully connected layer는 이 784개 픽셀 전체를 한 번에 연결해서 판단합니다.

반면 CNN은 작은 영역부터 봅니다. 예를 들어 3x3 영역을 보면서 “이 근처에 세로선이 있는가?”, “이 근처에 밝은 점이 있는가?” 같은 작은 패턴을 찾습니다. 이 작은 입력 영역을 local receptive field라고 합니다.

spatial locality는 이미지에서 가까운 픽셀들이 서로 관련이 깊다는 성질입니다. 예를 들어 고양이 귀를 이루는 픽셀들은 서로 가까이 모여 있습니다. 멀리 떨어진 배경 픽셀보다 근처 픽셀 관계가 먼저 중요합니다.

### 왜 이런 개념이 필요한가

이미지는 단순한 숫자 목록이 아닙니다. 픽셀의 위치와 이웃 관계가 매우 중요합니다.

작은 5x5 흑백 이미지를 생각해봅시다. 가운데에 세로선이 있다면 픽셀 값이 이런 모양일 수 있습니다.

```text
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
```

이 이미지를 그냥 25개의 숫자 목록으로 펴면, “가운데 열에 1이 이어져 있다”는 공간적 의미가 약해집니다. 하지만 CNN은 근처 픽셀끼리 묶어서 보므로 세로선 같은 지역 패턴을 자연스럽게 찾을 수 있습니다.

또 하나 중요한 이유는 파라미터 수입니다.

28x28 이미지 입력 784개를 hidden unit 100개에 fully connected로 연결하면 weight가 784 x 100 = 78,400개 필요합니다. 반면 3x3 kernel 하나는 weight가 9개뿐입니다. 물론 채널과 kernel 개수에 따라 늘어나지만, 기본 아이디어는 훨씬 적은 수의 weight로 지역 패턴을 반복해서 찾는 것입니다.

이 덕분에 CNN은 더 적은 데이터로도 이미지 패턴을 효율적으로 배울 수 있습니다.

### 아주 쉬운 예시

일상 비유로 생각해봅시다.

큰 벽화를 본다고 할 때, 처음부터 “이 벽화 전체가 무엇인가?”를 판단하기 어렵습니다. 대신 가까이 가서 작은 부분을 봅니다.

- 여기에는 직선이 있다.
- 저기에는 둥근 곡선이 있다.
- 이 부분은 눈처럼 보인다.
- 여러 부분을 합치면 얼굴 같다.

CNN도 비슷합니다.

- 낮은 layer: 선, 모서리, 색 변화 같은 작은 패턴을 찾습니다.
- 중간 layer: 눈, 바퀴, 질감 같은 조금 큰 패턴을 찾습니다.
- 높은 layer: 고양이 얼굴, 자동차 앞부분 같은 더 큰 구조를 찾습니다.

아주 작은 숫자 예시를 보겠습니다. 1차원으로 단순화하면 입력이 다음과 같다고 합시다.

```text
[0, 0, 1, 1, 1, 0, 0]
```

CNN이 한 번에 전체 7개를 보는 대신 크기 3짜리 창(window)을 움직이며 봅니다.

```text
[0,0,1], [0,1,1], [1,1,1], [1,1,0], [1,0,0]
```

이렇게 보면 [1,1,1]처럼 연속된 패턴이 어디 있는지 쉽게 찾을 수 있습니다. 이미지에서는 이 창이 2D로 움직인다고 생각하면 됩니다.

### 개념 구조와 핵심 포인트

CNN의 지역 연결성에는 세 가지 핵심 아이디어가 있습니다.

1. local receptive field
   - 각 neuron 또는 feature 값이 입력 전체가 아니라 작은 영역만 봅니다.
   - 예를 들어 3x3 kernel이면 한 번에 3x3 픽셀만 봅니다.

2. parameter sharing
   - 같은 kernel을 이미지 전체 위치에 반복해서 적용합니다.
   - 같은 “세로선 탐지기”를 왼쪽 위에도, 가운데에도, 오른쪽 아래에도 사용합니다.
   - 그래서 위치가 달라도 비슷한 패턴을 찾을 수 있습니다.

3. hierarchical feature learning
   - 아래 layer는 작은 패턴을 찾고, 위 layer는 작은 패턴들을 조합해 큰 패턴을 찾습니다.
   - 예를 들어 선 → 모서리 → 눈/코 → 얼굴처럼 올라갑니다.

지역 연결성은 “모든 것을 한 번에 연결하지 말자”는 제약입니다. 그런데 이 제약은 단점이 아니라 이미지에 맞는 좋은 가정입니다. 이미지에서는 가까운 픽셀끼리 먼저 관련이 크기 때문입니다.

### 핵심 수학 포인트

이미지는 tensor로 표현됩니다. 예를 들어 컬러 이미지는 보통 height x width x channels 형태입니다.

작은 예를 들어 4x4 흑백 이미지는 channels가 1개인 4x4 tensor처럼 볼 수 있습니다.

```text
1 1 0 0
1 1 0 0
0 0 1 1
0 0 1 1
```

3x3 kernel을 쓴다면 출력의 한 위치는 입력의 3x3 부분만 사용해 계산됩니다. 즉, 출력 한 칸은 입력 전체 16개를 다 보지 않고 9개만 봅니다.

fully connected layer에서는 출력 하나가 입력 16개 전체와 연결될 수 있습니다. CNN에서는 출력 하나가 입력 일부와만 연결됩니다. 이것이 수학적으로는 sparse connectivity, 즉 연결이 빽빽하지 않고 일부만 있는 구조입니다.

하지만 layer를 여러 개 쌓으면 뒤쪽 layer의 한 값이 실제로는 입력 이미지의 더 넓은 영역 정보를 포함하게 됩니다. 이것을 receptive field가 커진다고 말합니다.

예를 들어 첫 번째 convolution layer의 한 값이 3x3 영역을 본다고 합시다. 두 번째 convolution layer는 첫 번째 layer의 이웃 값들을 다시 3x3으로 봅니다. 그러면 원본 이미지 기준으로는 더 넓은 범위의 정보를 간접적으로 보게 됩니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- CNN: Convolutional Neural Network입니다. 이미지나 공간 구조 데이터에 강한 neural network입니다.
- local receptive field: 한 feature가 입력에서 직접 바라보는 작은 지역 영역입니다.
- spatial locality: 가까운 위치의 값들이 서로 관련이 크다는 성질입니다.

### AI에서 어디에 쓰이는가

CNN은 이미지 AI의 기본 구조입니다.

- 이미지 분류: 사진이 고양이인지 강아지인지 판단합니다.
- object detection: 이미지 안에서 사람, 자동차, 표지판 위치를 찾습니다.
- segmentation: 픽셀 단위로 도로, 사람, 하늘 등을 나눕니다.
- medical imaging: X-ray, MRI에서 이상 부위를 찾습니다.
- multimodal model: 이미지 encoder로 CNN 또는 CNN 계열 구조가 쓰일 수 있습니다.

최근에는 Vision Transformer(ViT)처럼 attention 기반 모델도 많이 쓰입니다. 그래도 CNN의 지역 연결성 아이디어는 여전히 중요합니다. ViT도 이미지를 patch로 나누어 처리하는데, 이것 역시 이미지를 작은 지역 단위로 본다는 관점과 연결됩니다.

LLM에서 직접 CNN을 쓰지 않더라도, “구조에 맞는 inductive bias를 모델에 넣는다”는 생각은 중요합니다. CNN은 이미지에는 가까운 픽셀이 중요하다는 bias를 넣은 모델입니다. Transformer는 sequence에서 token 사이 관계를 attention으로 학습하는 bias를 넣은 모델이라고 볼 수 있습니다.

### 헷갈리기 쉬운 포인트

- CNN이 이미지 전체를 전혀 못 보는 것은 아닙니다. 처음에는 작은 영역을 보지만 layer가 쌓이면 더 넓은 영역 정보를 통합합니다.
- local receptive field는 kernel 크기와 관련 있지만 완전히 같은 말은 아닙니다. kernel은 계산에 쓰는 weight 묶음이고, receptive field는 출력 값이 영향을 받는 입력 영역입니다.
- CNN은 위치 정보를 버리는 모델이 아닙니다. 오히려 위치와 이웃 관계를 잘 활용합니다.
- fully connected layer가 항상 나쁜 것은 아닙니다. 다만 이미지의 공간 구조를 처음부터 무시하면 비효율적일 수 있습니다.

---

## 3. 합성곱 연산의 의미

### 한 줄 직관

합성곱(convolution)은 작은 필터(kernel)를 이미지 위에 밀어가며 “이 위치에 내가 찾는 패턴이 얼마나 있는가”를 점수로 계산하는 연산입니다.

### 개념 정의

convolution은 kernel이라는 작은 숫자 표를 입력 위에 올려놓고, 겹치는 숫자끼리 곱한 뒤 모두 더하는 연산입니다. 그리고 이 작업을 위치를 바꿔가며 반복합니다.

이미지 CNN에서는 kernel이 패턴 탐지기처럼 작동합니다.

- 어떤 kernel은 세로선을 잘 찾습니다.
- 어떤 kernel은 가로선을 잘 찾습니다.
- 어떤 kernel은 밝은 부분에서 어두운 부분으로 바뀌는 경계를 찾습니다.

stride는 kernel을 한 번 계산한 뒤 몇 칸씩 이동할지 정하는 값입니다. padding은 이미지 가장자리에 0 같은 값을 덧붙여서 출력 크기를 조절하거나 가장자리 정보를 덜 잃게 하는 방법입니다.

### 왜 이런 개념이 필요한가

이미지에서 중요한 것은 “어떤 패턴이 어디에 있는가”입니다.

예를 들어 숫자 7을 인식한다고 해봅시다. 숫자 7은 위쪽 가로선과 오른쪽 아래로 내려가는 대각선 같은 패턴으로 구성됩니다. 이런 작은 선 패턴을 먼저 찾고, 그 조합을 보고 숫자 7이라고 판단하면 효율적입니다.

convolution은 이 작은 패턴 찾기를 수학적으로 구현한 것입니다. kernel 하나가 작은 패턴 탐지기가 되고, 그 kernel을 이미지 전체에 반복 적용하면 패턴이 어느 위치에 있는지 나타내는 feature map이 만들어집니다.

이 방식이 중요한 이유는 같은 패턴이 이미지 어디에 있어도 찾을 수 있기 때문입니다. 고양이 귀가 사진 왼쪽에 있든 오른쪽에 있든, 같은 kernel이 전체 이미지를 훑으면서 귀의 일부 패턴을 찾을 수 있습니다.

### 아주 쉬운 예시

3x3 입력 이미지와 2x2 kernel을 생각해봅시다.

입력:

```text
1 2 0
0 1 3
2 1 0
```

kernel:

```text
1 0
0 1
```

왼쪽 위 2x2 영역에 kernel을 올려놓습니다.

입력의 왼쪽 위 2x2:

```text
1 2
0 1
```

겹치는 숫자끼리 곱하고 더합니다.

```text
1*1 + 2*0 + 0*0 + 1*1 = 2
```

그래서 출력의 첫 번째 값은 2입니다.

이번에는 kernel을 오른쪽으로 한 칸 옮깁니다.

입력의 오른쪽 위 2x2:

```text
2 0
1 3
```

계산하면:

```text
2*1 + 0*0 + 1*0 + 3*1 = 5
```

출력 값은 5입니다. 이 값이 크다는 것은 이 kernel이 좋아하는 패턴과 해당 위치의 입력이 더 잘 맞았다는 뜻으로 볼 수 있습니다.

### 개념 구조와 핵심 포인트

convolution을 이해할 때는 네 가지를 함께 봐야 합니다.

1. kernel
   - 작은 weight 묶음입니다.
   - 처음에는 랜덤하게 시작하지만 학습을 통해 유용한 패턴 탐지기로 바뀝니다.

2. sliding
   - kernel을 입력 위에서 위치를 바꿔가며 적용합니다.
   - 같은 kernel을 여러 위치에 반복 적용하므로 parameter sharing이 일어납니다.

3. feature map
   - convolution 결과로 나오는 출력입니다.
   - 특정 패턴이 각 위치에서 얼마나 강하게 나타났는지를 담습니다.

4. channel
   - 컬러 이미지는 RGB 3개 channel을 가집니다.
   - CNN layer 중간 feature도 여러 channel을 가질 수 있습니다.
   - 각 channel은 서로 다른 종류의 특징을 담는다고 이해할 수 있습니다.

예를 들어 첫 번째 layer에서 16개의 kernel을 쓰면 출력 feature map도 보통 16개 channel을 가집니다. 각각은 다른 패턴을 찾으려 합니다.

### 핵심 수학 포인트

convolution의 한 출력 값은 작은 dot product처럼 계산됩니다.

입력 조각과 kernel을 같은 길이의 숫자 목록으로 펼쳐서 생각해봅시다.

입력 조각:

```text
[1, 2, 0, 1]
```

kernel:

```text
[1, 0, 0, 1]
```

곱해서 더하면:

```text
1*1 + 2*0 + 0*0 + 1*1 = 2
```

즉 convolution의 한 위치 계산은 “입력 조각과 kernel이 얼마나 잘 맞는지”를 dot product로 재는 것과 비슷합니다.

stride와 padding도 출력 shape에 영향을 줍니다.

예를 들어 5x5 이미지에 3x3 kernel, stride 1, padding 0을 쓰면 kernel이 가로로 3곳, 세로로 3곳에 놓일 수 있어서 출력은 3x3이 됩니다.

만약 padding 1을 추가하면 입력 가장자리에 0을 둘러서 7x7처럼 계산할 수 있고, 3x3 kernel과 stride 1을 쓰면 출력 크기를 5x5로 유지할 수 있습니다.

stride가 2이면 kernel이 한 칸씩이 아니라 두 칸씩 이동합니다. 그러면 출력 크기는 더 작아집니다. 이 때문에 stride는 공간 해상도를 줄이는 효과가 있습니다.

학습 관점에서는 kernel의 숫자들이 weight입니다. backpropagation을 통해 loss를 줄이는 방향으로 kernel 값들이 업데이트됩니다. 처음에는 의미 없는 숫자였던 kernel이 학습 후에는 edge detector나 texture detector처럼 작동할 수 있습니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- convolution: kernel을 입력 위에 이동시키며 곱하고 더해서 feature를 만드는 연산입니다.
- kernel: convolution에 쓰이는 작은 weight 묶음입니다. filter라고도 부릅니다.
- stride: kernel이 이동하는 간격입니다.
- padding: 입력 가장자리에 값을 덧붙여 출력 크기와 가장자리 정보 처리를 조절하는 방법입니다.

### AI에서 어디에 쓰이는가

convolution은 CNN의 핵심 연산입니다.

- 이미지의 edge, corner, texture를 찾습니다.
- 여러 convolution layer를 쌓아 복잡한 object feature를 만듭니다.
- 음성 처리에서는 spectrogram 같은 2D 표현에서 지역 패턴을 찾는 데 쓰일 수 있습니다.
- 시계열 데이터에서도 1D convolution으로 짧은 구간 패턴을 찾을 수 있습니다.

딥러닝 구현에서는 tensor shape를 잘 이해해야 합니다. 예를 들어 PyTorch에서는 이미지 batch가 보통 `[batch, channels, height, width]` 형태입니다. convolution layer를 지나면 height와 width는 kernel, stride, padding에 따라 바뀌고, channels는 kernel 개수에 따라 바뀝니다.

이 shape 변화는 실전에서 매우 중요합니다. CNN을 만들 때 다음 layer의 입력 크기를 맞추지 못하면 shape mismatch 오류가 납니다. 그래서 convolution은 단순한 이미지 필터가 아니라 tensor shape를 바꾸는 핵심 연산으로도 이해해야 합니다.

### 헷갈리기 쉬운 포인트

- kernel은 사람이 직접 정한 고정 필터일 수도 있지만, CNN에서는 보통 학습되는 weight입니다.
- stride가 커지면 계산량은 줄지만 세밀한 위치 정보가 줄어들 수 있습니다.
- padding은 단순히 0을 붙이는 장난이 아닙니다. 출력 크기와 가장자리 정보 보존에 큰 영향을 줍니다.
- convolution의 출력 값이 크다고 항상 “좋다”는 뜻은 아닙니다. 그 kernel이 찾는 패턴과 잘 맞았다는 뜻입니다.
- CNN에서 말하는 convolution은 수학 교과서의 엄밀한 convolution과 구현상 약간 다르게 cross-correlation 형태로 계산되는 경우가 많습니다. 하지만 딥러닝 실무에서는 보통 convolution이라고 부릅니다.

---

## 복습 질문 3개

1. train loss는 계속 내려가는데 validation loss가 다시 올라간다면, 모델에 어떤 문제가 생겼을 가능성이 큰가요?
2. CNN이 이미지에서 fully connected layer보다 효율적인 이유를 local receptive field와 spatial locality 관점에서 설명해보세요.
3. 3x3 kernel, stride, padding은 convolution 출력의 의미와 shape에 각각 어떤 영향을 주나요?

## 오늘의 한 줄 요약

학습 곡선은 모델이 잘 배우는지 감시하는 도구이고, CNN은 가까운 픽셀부터 작은 패턴을 찾으며, convolution은 kernel로 그 패턴을 위치별 점수로 계산하는 핵심 연산입니다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 17/30]

오늘은 학습 곡선 해석, CNN의 지역 연결성, convolution의 kernel/stride/padding을 차근차근 복습해볼게요.

### 1. train loss는 계속 내려가는데 validation loss가 다시 올라간다면, 모델에 어떤 문제가 생겼을 가능성이 큰가요?

**정답**

모델이 과적합(overfitting)되고 있을 가능성이 큽니다.

즉, 모델이 훈련 데이터는 점점 더 잘 맞히고 있지만, 처음 보는 검증 데이터에는 오히려 약해지고 있다는 뜻입니다.

**설명**

train loss는 모델이 학습에 사용한 훈련 데이터에서 얼마나 틀렸는지를 나타냅니다. validation loss는 모델이 직접 학습하지 않은 검증 데이터에서 얼마나 틀렸는지를 나타냅니다.

train loss가 계속 내려간다는 것은 모델이 훈련 데이터에 대해서는 점점 더 잘 맞히고 있다는 뜻입니다. 그런데 validation loss가 다시 올라간다면, 모델이 일반적인 규칙을 배우기보다 훈련 데이터의 세부 패턴이나 잡음까지 외우기 시작했을 수 있습니다.

사람 공부로 비유하면, 기출문제 답을 거의 외워서 기출문제 점수는 계속 좋아지는데, 새로운 응용문제가 나오면 오히려 틀리는 상황과 비슷합니다.

이때 중요한 핵심 용어는 early stopping입니다. early stopping은 validation loss가 가장 좋았던 시점 근처에서 학습을 멈추는 방법입니다. “빨리 포기하는 것”이 아니라, 새 데이터에 대한 성능이 가장 좋은 모델을 고르는 전략입니다.

**예시**

예를 들어 epoch마다 loss가 이렇게 변한다고 해봅시다.

epoch 1: train loss 1.0, validation loss 1.1  
epoch 2: train loss 0.7, validation loss 0.8  
epoch 3: train loss 0.5, validation loss 0.6  
epoch 4: train loss 0.3, validation loss 0.7  
epoch 5: train loss 0.1, validation loss 0.9

겉으로 보면 epoch 5의 train loss가 0.1이라 좋아 보입니다. 하지만 validation loss는 0.9로 나빠졌습니다. 이 경우 epoch 3 근처의 모델이 실제로는 더 좋은 모델일 수 있습니다.

**실전 연결**

이미지 분류 CNN, 추천 모델, LLM fine-tuning 모두에서 train loss만 보면 위험합니다. 예를 들어 LLM을 특정 데이터셋으로 fine-tuning할 때 train loss가 계속 내려가도, 실제 사용자 질문에 대한 답변 품질은 나빠질 수 있습니다. 그래서 실전에서는 train loss와 validation loss를 함께 보고, validation loss가 가장 낮은 시점의 checkpoint를 저장하는 경우가 많습니다.

### 2. CNN이 이미지에서 fully connected layer보다 효율적인 이유를 local receptive field와 spatial locality 관점에서 설명해보세요.

**정답**

CNN은 이미지 전체를 한 번에 모든 뉴런과 연결하지 않고, 가까운 픽셀들의 작은 영역을 먼저 봅니다. 이 작은 영역을 local receptive field라고 합니다.

이미지는 가까운 픽셀끼리 관련이 큰 spatial locality 성질을 가지기 때문에, CNN은 이미지 구조에 잘 맞는 방식으로 적은 파라미터로 중요한 패턴을 효율적으로 배울 수 있습니다.

**설명**

fully connected layer는 입력의 모든 값과 출력의 모든 값을 연결합니다. 예를 들어 28x28 흑백 이미지는 픽셀이 784개입니다. 이 784개를 hidden unit 100개와 전부 연결하면 weight가 78,400개 필요합니다.

반면 CNN은 처음부터 이미지 전체를 다 보지 않습니다. 3x3 kernel을 쓴다면 한 번에 3x3 픽셀, 즉 9개 픽셀만 봅니다. 이 작은 입력 영역이 local receptive field입니다.

이 방식이 잘 작동하는 이유는 이미지에는 spatial locality가 있기 때문입니다. spatial locality는 가까운 위치의 값들이 서로 관련이 크다는 뜻입니다. 고양이 귀를 이루는 픽셀들은 서로 가까이 모여 있고, 눈을 이루는 픽셀들도 가까이 모여 있습니다. 그래서 이미지에서는 멀리 떨어진 픽셀을 처음부터 모두 연결하는 것보다, 가까운 픽셀 관계를 먼저 보는 것이 자연스럽습니다.

또 CNN은 같은 kernel을 이미지의 여러 위치에 반복해서 적용합니다. 이것을 parameter sharing이라고 합니다. 같은 “세로선 탐지기”를 이미지 왼쪽 위에도 쓰고, 가운데에도 쓰고, 오른쪽 아래에도 쓰는 식입니다. 그래서 적은 수의 weight로도 이미지 전체에서 같은 패턴을 찾을 수 있습니다.

**예시**

아주 작은 1차원 예시로 생각해보겠습니다.

입력이 다음과 같다고 해봅시다.

[0, 0, 1, 1, 1, 0, 0]

CNN은 전체 7개 숫자를 한 번에 모두 보지 않고, 크기 3짜리 창으로 나누어 봅니다.

[0, 0, 1]  
[0, 1, 1]  
[1, 1, 1]  
[1, 1, 0]  
[1, 0, 0]

이렇게 보면 [1, 1, 1]처럼 연속된 패턴이 어디 있는지 찾기 쉽습니다. 이미지에서는 이 창이 2차원으로 움직이면서 선, 모서리, 질감 같은 작은 패턴을 찾는다고 생각하면 됩니다.

**실전 연결**

CNN은 이미지 분류, object detection, segmentation, 의료 이미지 분석에서 기본적으로 중요한 구조입니다. 예를 들어 자율주행에서는 도로, 차선, 표지판 같은 지역 패턴을 먼저 잘 찾아야 합니다. CNN의 local receptive field는 이런 작은 시각적 단서를 잘 잡게 해줍니다.

LLM에서 CNN을 직접 쓰지 않더라도 이 관점은 중요합니다. 모델 구조에 데이터의 성질을 반영하는 것을 inductive bias라고 합니다. CNN은 “이미지는 가까운 픽셀끼리 중요하다”는 가정을 구조에 넣은 모델입니다. Transformer는 “token들 사이의 관계가 중요하다”는 관점을 attention으로 반영한 모델이라고 볼 수 있습니다.

### 3. 3x3 kernel, stride, padding은 convolution 출력의 의미와 shape에 각각 어떤 영향을 주나요?

**정답**

3x3 kernel은 입력에서 한 번에 3x3 영역을 보며 특정 패턴이 있는지 계산합니다.

stride는 kernel이 몇 칸씩 이동할지를 정해서 출력 크기와 정보의 촘촘함에 영향을 줍니다.

padding은 입력 가장자리에 값을 덧붙여 출력 크기를 조절하고, 가장자리 정보가 너무 빨리 사라지지 않게 도와줍니다.

**설명**

convolution은 kernel이라는 작은 weight 묶음을 입력 위에 올려놓고, 겹치는 숫자끼리 곱한 뒤 모두 더하는 연산입니다. CNN에서는 이 kernel이 작은 패턴 탐지기처럼 작동합니다.

3x3 kernel은 한 번에 3x3 픽셀을 봅니다. 즉, 출력 feature map의 한 칸은 입력 이미지의 작은 3x3 영역에서 나온 점수입니다. 이 점수는 “이 위치에 kernel이 찾는 패턴이 얼마나 강하게 있는가”를 나타낸다고 볼 수 있습니다.

stride는 kernel이 움직이는 간격입니다. stride가 1이면 한 칸씩 촘촘하게 이동합니다. stride가 2이면 두 칸씩 건너뛰며 이동합니다. stride가 커질수록 출력의 height와 width는 작아지고, 계산량도 줄어듭니다. 하지만 너무 크게 잡으면 세밀한 위치 정보를 놓칠 수 있습니다.

padding은 입력의 바깥쪽에 0 같은 값을 덧붙이는 방법입니다. padding이 없으면 kernel이 가장자리 근처를 충분히 보기 어렵고, convolution을 지날수록 출력 크기가 작아집니다. padding을 주면 출력 크기를 유지하거나 가장자리 정보를 더 잘 반영할 수 있습니다.

**예시**

5x5 이미지에 3x3 kernel을 적용한다고 해봅시다.

padding이 0이고 stride가 1이면, 3x3 kernel은 가로 방향으로 3번, 세로 방향으로 3번 놓일 수 있습니다. 그래서 출력 shape는 3x3이 됩니다.

반대로 padding을 1 주면 이미지 가장자리에 0을 한 줄 둘러싸는 효과가 생깁니다. 그러면 3x3 kernel, stride 1을 써도 출력 크기를 원래와 같은 5x5로 유지할 수 있습니다.

stride를 2로 바꾸면 kernel이 한 칸씩이 아니라 두 칸씩 이동합니다. 그러면 출력 크기는 더 작아집니다. 쉽게 말해 사진을 더 듬성듬성 훑는 것과 비슷합니다.

**실전 연결**

딥러닝 구현에서는 convolution의 의미뿐 아니라 tensor shape 변화가 매우 중요합니다. 예를 들어 PyTorch에서는 이미지 batch가 보통 [batch, channels, height, width] 형태입니다. convolution layer를 지나면 height와 width는 kernel size, stride, padding에 따라 바뀌고, channels는 kernel 개수에 따라 바뀝니다.

실전 CNN 모델을 만들 때 shape를 잘못 계산하면 다음 layer에서 shape mismatch 오류가 납니다. 또한 stride를 크게 하면 계산은 빨라지지만 작은 물체나 세밀한 패턴을 놓칠 수 있고, padding을 적절히 쓰지 않으면 이미지 가장자리 정보가 약해질 수 있습니다. 그래서 kernel, stride, padding은 단순한 설정값이 아니라 모델이 이미지를 어떻게 보고, 얼마나 자세히 볼지를 결정하는 핵심 설계 요소입니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-09-day17.md
