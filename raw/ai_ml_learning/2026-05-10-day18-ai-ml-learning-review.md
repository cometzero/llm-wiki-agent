# AI/ML Learning Review — Day 18 (2026-05-10)

## Source Metadata
- Lesson file: `/home/ubuntu/work/ai/learning/logs/2026-05-10-day18.md`
- Follow-up answer file: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-10_09-26-11.md`

## Lesson

# Day 18 - AI/ML 기초 학습

- Date: 2026-05-10
- Progress: 18/30
- Level: beginner-intermediate
- Milestone: 딥러닝 학습 기법과 CNN
- Milestone goal: 실제 딥러닝 학습을 안정화하는 방법과 CNN의 구조적 아이디어를 익힌다.

## Today's 3 concepts

1. 채널, 특징맵, 필터
2. 풀링과 다운샘플링
3. Residual Network의 핵심

---

## 1. 채널, 특징맵, 필터

### 한 줄 직관

CNN은 이미지를 한 장의 납작한 그림으로 보지 않고, 여러 겹의 숫자판(channel)을 쌓아 둔 tensor로 본 뒤, 작은 탐지기(filter)를 여기저기 밀어 보면서 새로운 특징 지도(feature map)를 만든다.

### 개념 정의

이미지는 컴퓨터 안에서 숫자 배열로 표현된다. 흑백 이미지는 보통 `높이 × 너비` 모양의 숫자판 하나로 볼 수 있고, 컬러 이미지는 빨강(R), 초록(G), 파랑(B) 값을 따로 가진 숫자판 3개가 겹쳐진 형태로 볼 수 있다. 이때 각각의 겹을 **channel**이라고 한다.

CNN에서 **filter**는 작은 숫자 패턴이다. 예를 들어 `3×3` 크기의 filter는 이미지의 작은 영역을 보면서 “여기에 세로선이 있는가?”, “여기에 밝은 점이 있는가?”, “여기에 색 변화가 있는가?” 같은 단서를 찾는다. filter가 이미지 전체를 훑고 지나가면서 각 위치마다 반응값을 만들면, 그 결과로 생기는 새 숫자판이 **feature map**이다.

여러 개의 filter를 동시에 쓰면 여러 개의 feature map이 생긴다. 이 filter들의 묶음을 **filter bank**라고 부른다. 예를 들어 filter가 16개라면 출력 feature map도 보통 16개의 channel을 가진다.

### 왜 이런 개념이 필요한가

이미지는 픽셀 하나하나만 보면 의미가 약하다. 픽셀 하나가 `120`인지 `125`인지보다 중요한 것은 주변 픽셀과 함께 어떤 모양을 만드는지이다. 고양이 사진을 예로 들면, 처음 층에서는 선, 모서리, 색 변화 같은 단순한 특징을 찾고, 더 깊은 층에서는 귀 모양, 눈 주변 패턴, 털 질감처럼 더 복잡한 특징을 찾는다.

channel, feature map, filter를 이해하면 CNN이 이미지를 어떻게 “점점 더 의미 있는 표현”으로 바꾸는지 볼 수 있다. 이것은 이미지 모델뿐 아니라, 딥러닝 전체에서 중요한 생각과 연결된다. 입력 tensor가 layer를 지나며 hidden state 또는 representation으로 바뀌고, 모델은 이 표현을 이용해 loss를 줄이는 방향으로 학습한다.

LLM에서도 비슷한 관점이 있다. LLM은 이미지를 filter로 훑지는 않지만, token embedding이 여러 layer를 지나며 hidden state로 바뀐다. CNN의 feature map은 이미지 쪽 hidden representation이라고 생각할 수 있다.

### 아주 쉬운 예시

아주 작은 흑백 이미지가 있다고 하자. 숫자가 클수록 밝다고 생각한다.

```text
이미지 3×3
1 1 1
0 0 0
0 0 0
```

이 이미지는 위쪽 줄이 밝고 아래쪽은 어둡다. 여기에 “위쪽은 밝고 아래쪽은 어두운 패턴”을 찾는 `2×2` filter를 생각해 보자.

```text
filter 2×2
 1  1
-1 -1
```

왼쪽 위 `2×2` 영역은 다음과 같다.

```text
1 1
0 0
```

각 위치를 곱해서 더하면 다음과 같다.

```text
1×1 + 1×1 + 0×(-1) + 0×(-1) = 2
```

반응값이 `2`로 크다. 즉 이 위치에는 filter가 찾는 패턴이 꽤 잘 맞는다. 반대로 아래쪽 영역처럼 모두 어두운 곳을 보면 반응값이 작아진다.

이렇게 filter가 위치마다 만든 반응값을 모아 놓은 것이 feature map이다. feature map의 값이 크다는 것은 “그 위치에 이 filter가 찾는 특징이 강하게 있다”는 뜻에 가깝다.

### 개념 구조와 핵심 포인트

- **입력 channel**: 원본 데이터가 가진 겹이다. RGB 이미지는 보통 3 channel이다.
- **filter**: 작은 패턴 탐지기다. 보통 `3×3`, `5×5` 같은 작은 공간을 본다.
- **channel 전체를 함께 본다**: RGB 이미지에 `3×3` filter를 적용할 때 실제 filter는 `3×3×3` 모양이다. 공간은 `3×3`이고, 색 channel 3개를 모두 본다.
- **feature map**: filter가 이미지 전체를 훑으며 만든 반응값의 지도다.
- **filter bank**: 여러 filter의 묶음이다. filter가 32개면 출력 feature map channel도 보통 32개가 된다.
- **깊은 층으로 갈수록 의미가 추상화된다**: 처음 feature map은 선이나 모서리처럼 단순한 특징을 담고, 뒤쪽 feature map은 부품이나 객체 일부처럼 더 큰 의미를 담을 수 있다.

예를 들어 tensor shape가 다음처럼 변할 수 있다.

```text
입력 이미지: 32 × 32 × 3
Conv layer의 filter 개수: 16개
출력 feature map: 32 × 32 × 16   # padding을 사용했다고 가정
```

여기서 `16`은 “16개의 다른 특징 탐지 결과”라고 볼 수 있다.

### 핵심 수학 포인트

CNN의 convolution은 아주 단순하게 말하면 “작은 영역과 filter의 숫자를 곱해서 더하는 연산”이다.

가장 간단한 2D 흑백 예시는 다음처럼 쓸 수 있다.

```text
출력값 = 입력 작은 영역과 filter를 위치별로 곱한 뒤 모두 더한 값 + bias
```

수식 느낌으로 쓰면 다음과 같다.

```text
y[i, j] = Σ 입력[i+u, j+v] × filter[u, v] + bias
```

컬러 이미지나 여러 channel이 있는 경우에는 channel 방향으로도 더한다.

```text
출력값 = 모든 channel의 작은 영역 × filter 값을 전부 더한 값
```

중요한 점은 filter의 숫자들이 사람이 직접 정한 규칙이 아니라, 학습되는 parameter라는 것이다. 처음에는 랜덤에 가깝지만, loss를 줄이도록 gradient와 optimizer가 filter 값을 조금씩 바꾼다. 그래서 어떤 filter는 세로선을 잘 찾게 되고, 어떤 filter는 색 변화나 질감을 잘 찾게 된다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **channel**: tensor의 겹 또는 축이다. RGB 이미지에서는 R, G, B 3개 channel이 있다.
- **feature map**: filter가 입력을 훑으며 만든 반응값 지도다. 특정 특징이 어디에 강한지 보여 준다.
- **filter**: 작은 학습 가능한 숫자 패턴이다. CNN에서는 local pattern detector처럼 작동한다.
- **filter bank**: 여러 filter의 묶음이다. 출력 channel 수와 직접 연결된다.
- **convolution**: filter를 입력 위에 이동시키며 곱하고 더해 feature map을 만드는 연산이다.
- **activation**: filter 반응값에 ReLU 같은 비선형 함수를 적용한 결과를 말하기도 한다.

### AI에서 어디에 쓰이는가

- 이미지 분류 모델에서 고양이, 자동차, 글자 같은 객체를 알아보는 데 쓰인다.
- object detection 모델에서 물체의 위치와 종류를 찾는 데 쓰인다.
- segmentation 모델에서 픽셀 단위로 “도로”, “사람”, “건물” 같은 label을 붙이는 데 쓰인다.
- vision transformer 이전의 대표적인 이미지 모델들은 거의 모두 convolution, channel, feature map 개념을 중심으로 만들어졌다.
- 요즘 멀티모달 모델에서도 이미지 encoder 쪽에는 CNN 또는 CNN에서 발전한 구조가 들어가거나, CNN의 feature map 사고방식이 patch embedding 이해에 도움을 준다.

### 헷갈리기 쉬운 포인트

- channel은 반드시 RGB만 뜻하지 않는다. 중간 layer에서는 `64 channel`, `256 channel`처럼 사람이 해석하기 어려운 특징 channel이 생긴다.
- feature map은 원본 이미지가 아니다. 모델이 특정 filter 관점에서 다시 표현한 숫자 지도다.
- filter 하나가 feature map 하나를 만든다고 생각하면 처음에는 쉽다. 실제 구현에서는 batch, stride, padding, channel 축이 함께 있어서 tensor shape를 조심해야 한다.
- filter는 사람이 “이것은 고양이 귀 filter”라고 정해 넣는 것이 아니다. 데이터와 loss를 통해 자동으로 학습된다.

---

## 2. 풀링과 다운샘플링

### 한 줄 직관

Pooling은 큰 그림에서 중요한 정보만 남기고 해상도를 줄이는 방법이고, downsampling은 데이터의 크기를 줄이는 전체 아이디어다.

### 개념 정의

**downsampling**은 feature map의 높이와 너비를 줄이는 것을 말한다. 예를 들어 `32×32` feature map을 `16×16`으로 줄이면 공간 크기가 절반이 된다. 전체 원소 수는 `1024`개에서 `256`개로 줄어든다.

**pooling**은 downsampling을 하는 대표적인 방법이다. 특히 **max pooling**은 작은 구역 안에서 가장 큰 값만 남긴다. 예를 들어 `2×2` 영역마다 가장 큰 값 하나를 뽑으면 높이와 너비가 각각 절반으로 줄어든다.

이때 중요한 직관은 “조금 위치가 바뀌어도 비슷하게 보자”이다. 고양이 귀가 왼쪽으로 1픽셀 움직였다고 해서 완전히 다른 물체가 되는 것은 아니다. pooling은 이런 작은 위치 변화에 덜 민감한 표현을 만드는 데 도움을 준다. 이것을 **translation invariance** 또는 더 약하게는 작은 이동에 대한 robustness라고 설명한다.

### 왜 이런 개념이 필요한가

CNN에서 feature map을 계속 같은 크기로 유지하면 계산량이 커진다. 예를 들어 `128×128×64` feature map은 원소가 1,048,576개다. 이것을 계속 유지한 채 깊은 layer를 쌓으면 메모리와 연산량이 부담된다.

또한 이미지 인식에서는 모든 픽셀 위치를 완벽히 외우는 것보다, 중요한 특징이 대략 어디에 있는지를 아는 것이 더 유용할 때가 많다. 예를 들어 숫자 `7`이 이미지 중앙에서 오른쪽으로 조금 이동해도 여전히 `7`이다. pooling은 이런 작은 위치 변화에 대해 모델이 너무 예민하게 반응하지 않게 도와준다.

다만 downsampling은 정보를 버리는 과정이기도 하다. 너무 빨리, 너무 많이 줄이면 작은 물체나 세밀한 경계 정보가 사라질 수 있다. 그래서 segmentation처럼 정확한 위치가 중요한 작업에서는 pooling을 조심해서 쓰고, skip connection이나 upsampling으로 위치 정보를 보완한다.

### 아주 쉬운 예시

`4×4` feature map이 있다고 하자.

```text
1 3 2 0
4 6 1 2
0 1 5 2
2 2 1 3
```

`2×2 max pooling`을 적용한다. 즉 `2×2` 구역마다 가장 큰 값 하나만 남긴다.

왼쪽 위 구역:

```text
1 3
4 6
```

가장 큰 값은 `6`이다.

오른쪽 위 구역:

```text
2 0
1 2
```

가장 큰 값은 `2`이다.

왼쪽 아래 구역:

```text
0 1
2 2
```

가장 큰 값은 `2`이다.

오른쪽 아래 구역:

```text
5 2
1 3
```

가장 큰 값은 `5`이다.

그래서 출력은 다음과 같다.

```text
6 2
2 5
```

입력은 `4×4`였고 출력은 `2×2`가 되었다. 정보는 줄었지만, 각 구역에서 강하게 나타난 특징은 남았다.

### 개념 구조와 핵심 포인트

- **pooling window**: 값을 모아 볼 작은 구역이다. 예: `2×2`.
- **stride**: window를 몇 칸씩 이동할지 정한다. `2×2 max pooling`에서 stride가 2이면 겹치지 않고 이동한다.
- **max pooling**: 구역 안의 최대값만 남긴다. “강한 특징이 있었는가?”를 보존하는 느낌이다.
- **average pooling**: 구역 안의 평균값을 남긴다. “전체적으로 어느 정도 반응했는가?”를 보존하는 느낌이다.
- **downsampling**: pooling뿐 아니라 stride가 큰 convolution으로도 할 수 있다.
- **translation invariance**: 입력이 조금 이동해도 출력이 크게 바뀌지 않는 성질이다. 엄밀히는 완전한 invariance라기보다 작은 이동에 둔감해지는 효과로 이해하면 좋다.

shape 예시는 다음과 같다.

```text
입력 feature map: 32 × 32 × 64
2×2 max pooling, stride 2
출력 feature map: 16 × 16 × 64
```

여기서 channel 수 `64`는 그대로이고, 공간 크기만 줄어든다.

### 핵심 수학 포인트

max pooling은 각 구역에서 최대값을 고르는 연산이다.

```text
출력값 = max(구역 안의 값들)
```

예를 들어 `2×2` 구역이 다음과 같다면,

```text
2 9
4 1
```

출력은 `9`이다.

downsampling 비율도 중요하다. 높이와 너비를 각각 절반으로 줄이면 원소 수는 4분의 1이 된다.

```text
32 × 32 = 1024
16 × 16 = 256
```

이것은 계산량을 크게 줄인다. 하지만 gradient 관점에서는 max pooling에서 선택된 최대값 위치로만 gradient가 주로 전달된다. 예를 들어 위 구역에서 `9`가 선택되었다면, backward pass에서 그 구역의 대표 책임은 `9` 위치가 갖는다. 그래서 pooling은 학습과 gradient 흐름에도 영향을 준다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **pooling**: 작은 구역의 값을 하나로 요약하는 연산이다.
- **max pooling**: 구역에서 가장 큰 값만 남기는 pooling이다.
- **average pooling**: 구역의 평균을 남기는 pooling이다.
- **downsampling**: 공간 크기나 sequence 길이 등 데이터 해상도를 줄이는 과정이다.
- **stride**: filter나 pooling window가 이동하는 간격이다.
- **translation invariance**: 입력이 조금 이동해도 모델 출력이 크게 달라지지 않는 성질이다.

### AI에서 어디에 쓰이는가

- 이미지 분류 CNN에서 feature map 크기를 줄여 계산량을 낮춘다.
- 고양이 귀, 자동차 바퀴처럼 위치가 조금 달라져도 같은 특징으로 보게 만든다.
- object detection에서는 너무 강한 downsampling이 작은 물체 탐지를 어렵게 할 수 있어 feature pyramid 같은 구조로 보완한다.
- segmentation에서는 위치 정보가 중요하므로 downsampling 후 upsampling, skip connection을 함께 사용한다.
- Transformer에서도 직접적인 max pooling은 덜 쓰지만, 긴 sequence를 줄이거나 patch를 합치는 방식은 downsampling과 비슷한 목적을 갖는다. 예를 들어 vision transformer 계열에서 patch merging은 공간 정보를 줄이며 더 큰 단위의 표현을 만든다.

### 헷갈리기 쉬운 포인트

- pooling과 downsampling은 같은 말이 아니다. pooling은 downsampling의 한 방법이다.
- max pooling은 “가장 중요한 정보만 완벽히 남긴다”가 아니다. 최대값만 남기므로 평균적인 정보나 정확한 위치 정보는 사라질 수 있다.
- translation invariance는 입력이 어디로 움직여도 완전히 같은 결과가 나온다는 뜻으로 과하게 이해하면 안 된다. 작은 위치 변화에 덜 민감해진다는 직관이 더 안전하다.
- 해상도를 줄이면 계산은 쉬워지지만, 작은 물체나 경계선처럼 세밀한 정보는 잃을 수 있다.

---

## 3. Residual Network의 핵심

### 한 줄 직관

Residual Network, 즉 ResNet은 깊은 neural network가 “전부 새로 배우기”보다 “기존 입력에 필요한 변화만 더하기”를 배우게 해서 학습을 훨씬 쉽게 만든 구조다.

### 개념 정의

일반적인 layer 블록은 입력 `x`를 받아 어떤 변환 `F(x)`를 만든다. ResNet의 핵심인 **skip connection**은 입력 `x`를 몇 개 layer 뒤로 그대로 건너뛰어 보내고, 나중에 변환 결과와 더한다.

```text
일반 블록: 출력 = F(x)
Residual 블록: 출력 = x + F(x)
```

여기서 `x`를 그대로 보내는 경로를 **identity mapping**이라고 한다. identity mapping은 “입력을 바꾸지 않고 그대로 통과시키는 함수”라는 뜻이다. 예를 들어 입력이 `5`이면 출력도 `5`인 함수가 identity mapping이다.

ResNet은 “정답 표현을 직접 배워라”가 아니라 “입력에서 무엇을 얼마나 바꾸면 좋은지, 즉 residual을 배워라”라고 시킨다. residual은 쉽게 말해 차이 또는 수정량이다.

### 왜 이런 개념이 필요한가

딥러닝에서는 layer를 깊게 쌓으면 더 복잡한 패턴을 표현할 수 있다. 하지만 무작정 깊게 만들면 학습이 어려워진다. gradient가 앞쪽 layer까지 잘 전달되지 않거나, 깊은 모델이 오히려 얕은 모델보다 학습 loss도 잘 못 줄이는 문제가 생길 수 있다.

직관적으로 보면, 50층짜리 모델이 20층짜리 모델보다 항상 잘해야 할 것 같지만 실제로는 그렇지 않았다. 뒤에 30층을 더 붙였을 때, 그 30층이 아무것도 하지 않고 그냥 통과만 해도 최소한 20층 모델 수준은 유지할 수 있어야 한다. 그런데 일반 layer는 “아무것도 하지 않기”조차 배우기 어려울 수 있다.

ResNet은 skip connection을 넣어서 “필요 없으면 그냥 지나가라”는 길을 만들어 준다. 그래서 매우 깊은 모델도 안정적으로 학습할 수 있게 되었다.

### 아주 쉬운 예시

입력 숫자 `x = 10`이 있고, 우리가 원하는 출력도 `10`이라고 하자. 즉 이 블록은 사실 아무것도 바꾸지 않는 것이 최선이다.

일반 블록에서는 layer가 직접 다음을 배워야 한다.

```text
F(10) = 10
```

반면 residual 블록에서는 다음처럼 된다.

```text
출력 = x + F(x)
원하는 출력 = 10
x = 10
따라서 F(x)는 0만 배우면 됨
```

즉 residual 블록은 `F(10) = 0`을 배우면 된다. “입력을 그대로 유지하기”가 쉬워진다.

또 다른 예로 원하는 출력이 `12`라면,

```text
x = 10
출력 = x + F(x) = 12
F(x) = 2
```

블록은 전체 값 `12`를 처음부터 만들기보다, “기존 값에 +2만 더하면 된다”를 배우면 된다. 이것이 residual learning의 핵심 직관이다.

### 개념 구조와 핵심 포인트

- **ResNet**: residual block을 많이 쌓은 neural network 구조다.
- **skip connection**: 입력을 몇 개 layer 뒤로 건너뛰어 전달하는 연결이다.
- **identity mapping**: 입력을 그대로 출력하는 경로다. `output = x`인 함수로 이해하면 된다.
- **residual function**: `F(x)`처럼 입력에 더할 변화량을 만드는 함수다.
- **출력 구조**: 보통 `y = x + F(x)` 형태다.
- **shape가 맞아야 더할 수 있다**: `x`와 `F(x)`를 더하려면 tensor shape가 같아야 한다. 다르면 `1×1 convolution` 같은 projection을 사용해 channel 수나 크기를 맞춘다.
- **깊은 모델 학습 안정화**: gradient가 skip path를 통해 앞쪽 layer까지 더 쉽게 흐를 수 있다.

CNN에서 residual block은 보통 다음과 같은 느낌이다.

```text
입력 x
  ├─ Conv → ReLU → Conv → F(x)
  └─ 그대로 이동 ───────────────┐
출력 y = x + F(x)
```

이 구조는 이미지 모델뿐 아니라 Transformer 계열에서도 매우 중요하다. Transformer layer에도 attention 결과나 feed-forward 결과를 원래 hidden state에 더하는 residual connection이 들어간다.

### 핵심 수학 포인트

Residual block의 핵심 식은 단순하다.

```text
y = x + F(x)
```

여기서 `F(x)`는 convolution, normalization, activation 같은 layer들이 만든 변환이다. 중요한 점은 gradient 흐름이다.

아주 단순하게 `y = x + F(x)`라고 하면, 출력 `y`가 입력 `x`에 의존하는 길이 두 개 있다.

1. `x`가 그대로 더해지는 길
2. `F(x)`를 거쳐 오는 길

그래서 backward pass에서 gradient도 두 길로 전달될 수 있다. 아주 직관적으로 말하면, skip connection은 gradient가 지나갈 수 있는 “직통 도로”를 만든다.

조금 더 수학적으로는 `y`를 `x`에 대해 미분할 때, `x`가 그대로 더해진 부분에서 `1`이 생긴다.

```text
변화량 관점: y가 x를 그대로 포함하므로, x의 변화가 y에 직접 반영된다.
```

이것은 깊은 layer를 많이 지나며 gradient가 약해지는 문제를 줄이는 데 도움을 준다. 그래서 optimizer가 앞쪽 layer의 parameter도 더 안정적으로 업데이트할 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **ResNet**: Residual Network의 줄임말이다. skip connection을 활용해 매우 깊은 CNN을 학습시킨 대표 구조다.
- **skip connection**: layer 몇 개를 건너뛰어 입력을 뒤쪽으로 직접 보내는 연결이다.
- **identity mapping**: 입력을 그대로 출력하는 함수 또는 경로다.
- **residual**: 목표값과 현재 입력 사이의 차이, 또는 추가로 배워야 할 변화량이다.
- **deep supervision**: 깊은 모델의 중간 또는 깊은 layer에도 학습 신호를 잘 전달하려는 아이디어다. ResNet 자체가 항상 auxiliary loss를 쓰는 deep supervision은 아니지만, skip connection은 깊은 layer 학습 신호 전달을 쉽게 만든다는 점에서 관련된 관점으로 이해할 수 있다.
- **projection shortcut**: `x`와 `F(x)`의 shape가 다를 때, `x`를 `1×1 convolution` 등으로 바꿔 더할 수 있게 만드는 skip path다.

### AI에서 어디에 쓰이는가

- ResNet-50, ResNet-101 같은 이미지 분류 모델의 핵심 구조다.
- object detection, segmentation, pose estimation 모델의 backbone으로 오랫동안 사용되었다.
- Transformer에서도 residual connection은 필수에 가깝다. attention layer의 출력은 원래 hidden state에 더해지고, feed-forward layer의 출력도 다시 더해진다.
- LLM 학습에서도 residual stream이라는 표현이 자주 나온다. 여러 layer가 같은 hidden state 흐름에 정보를 조금씩 더해 가는 구조로 볼 수 있다.
- 깊은 모델에서 loss와 gradient가 안정적으로 전달되게 하므로, optimizer가 더 깊은 parameter들을 학습하기 쉬워진다.

### 헷갈리기 쉬운 포인트

- skip connection은 layer를 아예 무시한다는 뜻이 아니다. 필요하면 `F(x)`가 중요한 변화를 만들고, 필요 없으면 거의 0에 가까운 변화를 만들 수 있게 해 준다.
- `x + F(x)`를 하려면 shape가 맞아야 한다. channel 수나 공간 크기가 다르면 projection이 필요하다.
- ResNet은 단순히 “깊게 쌓은 CNN”이 아니다. 깊게 쌓아도 학습되게 만든 구조적 아이디어가 핵심이다.
- deep supervision과 skip connection은 같은 말이 아니다. deep supervision은 보통 중간 layer에 auxiliary loss를 붙이는 방법을 말한다. 다만 둘 다 깊은 모델에 학습 신호를 잘 전달하려는 문제의식과 연결된다.

---

## 복습 질문 3개

1. RGB 이미지의 channel 수는 몇 개이며, CNN의 중간 feature map에서 channel 수가 64라는 말은 어떤 뜻일까?
2. `2×2 max pooling`은 왜 계산량을 줄이고 작은 위치 변화에 덜 민감한 표현을 만드는 데 도움이 될까?
3. ResNet의 `y = x + F(x)` 구조에서 `F(x)`가 0에 가까워지면 블록은 어떤 역할을 하게 될까?

## 오늘의 한 줄 요약

CNN은 filter로 feature map을 만들고 pooling으로 중요한 정보만 남기며, ResNet은 skip connection으로 깊은 모델이 필요한 변화만 배우게 해서 학습을 안정화한다.

---

## Follow-up Review Answers

[AI/ML 오늘의 복습 정답 Day 18/30]

오늘은 CNN의 feature map 구조, pooling의 역할, ResNet의 skip connection을 천천히 정리해 볼게요.

### 1. RGB 이미지의 channel 수는 몇 개이며, CNN의 중간 feature map에서 channel 수가 64라는 말은 어떤 뜻일까?

**정답**

RGB 이미지의 channel 수는 3개입니다.

RGB는 각각 다음 3개의 색 정보를 뜻합니다.

- R: Red, 빨강
- G: Green, 초록
- B: Blue, 파랑

그리고 CNN의 중간 feature map에서 channel 수가 64라는 말은, 모델이 그 시점에서 64종류의 특징 지도를 만들었다는 뜻입니다.

즉, 원본 이미지의 RGB 3개 channel이 그대로 유지된다는 뜻이 아니라, 여러 filter가 이미지를 분석한 결과로 “64개의 서로 다른 특징 반응”이 생겼다는 뜻입니다.

**설명**

처음 이미지는 보통 사람이 이해하기 쉬운 색 channel을 가집니다. 예를 들어 컬러 사진 하나는 컴퓨터 안에서 보통 다음과 같은 tensor shape로 표현됩니다.

```text
높이 × 너비 × 3
```

여기서 마지막 `3`이 RGB channel입니다.

하지만 CNN의 중간 layer로 들어가면 channel의 의미가 달라집니다. 이때 channel은 더 이상 “빨강, 초록, 파랑”처럼 사람이 바로 이름 붙일 수 있는 색 정보가 아닐 수 있습니다.

CNN은 filter라는 작은 패턴 탐지기를 사용합니다. 어떤 filter는 세로선에 강하게 반응할 수 있고, 어떤 filter는 모서리, 질감, 색 변화, 특정 부분 모양에 강하게 반응할 수 있습니다.

filter가 64개 있다면, 각 filter가 하나씩 feature map을 만듭니다. 그래서 출력 channel 수가 64가 됩니다.

쉽게 말하면 다음과 같습니다.

```text
입력: 이미지 1장, RGB 3 channel
CNN layer 통과
출력: 64개의 특징 지도
```

여기서 `64 channel`은 “64개의 관점으로 이미지를 다시 본 결과”라고 이해하면 좋습니다.

**예시**

예를 들어 고양이 사진이 있다고 해볼게요.

처음 입력은 다음처럼 생겼습니다.

```text
32 × 32 × 3
```

이것은 32×32 크기의 컬러 이미지이고, RGB 3개 channel이 있다는 뜻입니다.

이 이미지에 filter 64개를 가진 convolution layer를 적용하면 출력은 보통 다음처럼 될 수 있습니다.

```text
32 × 32 × 64
```

이때 64개의 channel은 대략 이런 식의 특징을 담을 수 있습니다.

- 1번 channel: 밝은 세로선에 반응
- 2번 channel: 어두운 가로선에 반응
- 3번 channel: 털 같은 질감에 반응
- 4번 channel: 둥근 모서리에 반응
- ...
- 64번 channel: 또 다른 패턴에 반응

물론 실제로 사람이 각 channel을 정확히 “이건 귀 channel이다”라고 해석하기는 어렵습니다. 하지만 기본 직관은 “각 channel은 어떤 특징에 대한 반응 지도”라고 보면 됩니다.

**실전 연결**

이미지 분류, object detection, segmentation 모델에서 channel 수는 모델의 표현 능력과 직접 연결됩니다. channel 수가 많을수록 모델은 더 다양한 특징을 동시에 저장할 수 있습니다. 예를 들어 ResNet, EfficientNet 같은 CNN backbone에서는 layer가 깊어질수록 channel 수가 64, 128, 256, 512처럼 커지는 경우가 많습니다. 이는 단순한 픽셀 정보에서 출발해 점점 더 복잡한 visual representation, 즉 이미지 표현을 만들기 위한 구조입니다.

### 2. `2×2 max pooling`은 왜 계산량을 줄이고 작은 위치 변화에 덜 민감한 표현을 만드는 데 도움이 될까?

**정답**

`2×2 max pooling`은 2×2 영역 안에서 가장 큰 값 하나만 남깁니다.

그래서 feature map의 높이와 너비가 보통 절반으로 줄어듭니다. 높이와 너비가 각각 절반이 되면 전체 위치 수는 4분의 1로 줄어듭니다. 따라서 다음 layer가 처리해야 할 숫자 개수가 줄어 계산량이 감소합니다.

또한 2×2 영역 안에서 특징이 정확히 어느 위치에 있든 가장 큰 값만 남기기 때문에, 특징이 아주 조금 이동해도 비슷한 출력이 나올 수 있습니다. 그래서 작은 위치 변화에 덜 민감한 표현을 만드는 데 도움이 됩니다.

**설명**

max pooling은 “작은 구역 안에서 가장 강한 특징만 대표로 남기는 연산”입니다.

예를 들어 어떤 feature map의 값이 크다는 것은 보통 “이 위치에 어떤 특징이 강하게 있다”는 뜻입니다. max pooling은 그 작은 구역 안에서 가장 큰 반응만 선택합니다.

`2×2 max pooling`은 보통 이런 식으로 작동합니다.

```text
2×2 구역 → 숫자 1개
```

예를 들어 입력 feature map이 `32 × 32`라면, `2×2 max pooling` 후에는 보통 `16 × 16`이 됩니다.

원소 수를 비교하면 다음과 같습니다.

```text
32 × 32 = 1024개
16 × 16 = 256개
```

즉, 공간 위치 수가 1024개에서 256개로 줄어듭니다. 4분의 1이 된 것입니다. 그래서 다음 convolution layer가 계산해야 할 양도 줄어듭니다.

또 하나 중요한 점은 작은 위치 변화에 대한 둔감함입니다.

예를 들어 고양이 귀를 찾는 filter가 있다고 해볼게요. 고양이 귀가 이미지에서 오른쪽으로 1픽셀 움직였다고 해서 고양이가 아닌 것은 아닙니다. 하지만 픽셀 단위로 너무 예민한 모델은 이런 작은 이동에도 feature map이 크게 달라질 수 있습니다.

max pooling은 작은 구역 안에서 가장 큰 값만 남기기 때문에, 특징이 구역 안에서 조금 움직여도 여전히 비슷한 대표값이 남을 수 있습니다. 이것이 translation invariance, 즉 “입력이 조금 이동해도 출력이 크게 달라지지 않는 성질”과 연결됩니다.

다만 완벽한 translation invariance는 아닙니다. 정확히는 작은 이동에 조금 더 robust, 즉 덜 예민해지는 효과라고 이해하는 것이 안전합니다.

**예시**

다음과 같은 `2×2` 구역이 있다고 해볼게요.

```text
1 8
2 3
```

max pooling을 하면 가장 큰 값인 `8`만 남습니다.

```text
출력: 8
```

이번에는 특징 위치가 조금 움직여서 값이 이렇게 바뀌었다고 해봅시다.

```text
8 1
2 3
```

여전히 max pooling 결과는 `8`입니다.

```text
출력: 8
```

즉, 강한 특징이 2×2 구역 안에서 오른쪽 위에 있든 왼쪽 위에 있든, 대표값은 똑같이 남을 수 있습니다. 그래서 작은 위치 변화에 덜 민감해집니다.

조금 더 큰 예시는 다음과 같습니다.

```text
입력 feature map: 4 × 4
2×2 max pooling 적용
출력 feature map: 2 × 2
```

크기는 줄었지만, 각 구역에서 가장 강한 특징은 남습니다.

**실전 연결**

CNN 이미지 분류 모델에서는 pooling이 계산량을 줄이는 데 매우 중요합니다. 큰 이미지를 계속 큰 feature map으로 처리하면 memory와 연산량이 빠르게 증가합니다. pooling이나 stride convolution으로 downsampling을 하면 모델이 더 깊어질 수 있습니다. 하지만 segmentation이나 object detection처럼 위치가 중요한 작업에서는 너무 많이 downsampling하면 작은 물체나 경계 정보가 사라질 수 있습니다. 그래서 U-Net, Feature Pyramid Network 같은 구조에서는 downsampling으로 얻은 큰 의미 정보와 skip connection으로 보존한 위치 정보를 함께 사용합니다.

### 3. ResNet의 `y = x + F(x)` 구조에서 `F(x)`가 0에 가까워지면 블록은 어떤 역할을 하게 될까?

**정답**

`F(x)`가 0에 가까워지면 ResNet 블록의 출력은 거의 `x`와 같아집니다.

식으로 보면 다음과 같습니다.

```text
y = x + F(x)
```

만약 `F(x) ≈ 0`이라면,

```text
y ≈ x
```

즉, 블록은 입력을 거의 그대로 통과시키는 identity mapping 역할을 하게 됩니다.

쉽게 말하면 “이 layer들은 지금 굳이 바꿀 것이 없으니, 입력을 거의 그대로 보내자”라는 동작을 하게 됩니다.

**설명**

ResNet의 핵심은 skip connection입니다. skip connection은 입력 `x`를 몇 개 layer 뒤로 그대로 보내고, 그 결과를 `F(x)`와 더합니다.

일반적인 block은 입력 `x`를 받아서 완전히 새로운 출력 `F(x)`를 만들어야 합니다.

```text
일반 block:
y = F(x)
```

반면 ResNet block은 다음처럼 작동합니다.

```text
Residual block:
y = x + F(x)
```

여기서 `F(x)`는 “입력을 얼마나 바꿀지”를 나타내는 변화량이라고 볼 수 있습니다. 이것을 residual이라고 합니다.

중요한 점은, 어떤 layer가 꼭 복잡한 변환을 해야 하는 것은 아니라는 점입니다. 깊은 모델에서는 어떤 block은 입력을 크게 바꿀 필요가 없을 수도 있습니다. 이때 일반 layer는 “입력을 그대로 출력하는 함수”를 직접 배워야 합니다. 생각보다 이것이 쉽지 않을 수 있습니다.

하지만 ResNet에서는 상황이 쉬워집니다.

원래 입력 `x`가 이미 skip connection을 통해 더해지기 때문에, block이 아무 변화도 주고 싶지 않다면 `F(x)`를 0에 가깝게 만들면 됩니다.

즉, ResNet block은 다음 두 가지를 모두 쉽게 할 수 있습니다.

- 필요하면 `F(x)`를 크게 만들어 입력을 바꾼다.
- 필요 없으면 `F(x)`를 0에 가깝게 만들어 입력을 그대로 보낸다.

이 구조 덕분에 아주 깊은 neural network도 학습이 쉬워집니다. gradient, 즉 loss function을 줄이기 위해 parameter를 어떻게 바꿔야 하는지 알려주는 신호도 skip connection을 통해 더 잘 흐를 수 있습니다.

**예시**

입력값이 `x = 10`이라고 해볼게요.

ResNet block의 식은 다음과 같습니다.

```text
y = x + F(x)
```

만약 이 block이 아무것도 바꾸지 않는 것이 가장 좋다면, 원하는 출력도 `10`입니다.

```text
원하는 출력 y = 10
입력 x = 10
```

그러면 `F(x)`는 얼마가 되면 될까요?

```text
10 = 10 + F(x)
F(x) = 0
```

즉, block은 `F(x) = 0`만 배우면 됩니다.

반대로 원하는 출력이 `12`라면,

```text
12 = 10 + F(x)
F(x) = 2
```

이 경우 block은 전체 출력 `12`를 처음부터 새로 만드는 것이 아니라, “기존 입력에 +2만 더하자”를 배우면 됩니다.

이것이 residual learning의 직관입니다. 전체 답을 새로 만드는 것보다 수정량만 배우는 것이 더 쉬울 때가 많습니다.

**실전 연결**

ResNet은 ResNet-50, ResNet-101 같은 이미지 모델의 핵심 구조입니다. 이 아이디어는 CNN에만 머물지 않고 Transformer와 LLM에도 매우 중요하게 이어집니다. Transformer layer에서도 attention 결과를 원래 hidden state에 더하고, feed-forward network 결과도 다시 더합니다. 이것도 residual connection입니다. LLM에서 여러 layer가 residual stream 위에 정보를 조금씩 더해 가는 구조를 이해하려면, `y = x + F(x)`라는 ResNet의 직관이 큰 도움이 됩니다. 깊은 모델이 안정적으로 학습되기 위해서는 gradient가 앞쪽 layer까지 잘 전달되어야 하는데, skip connection은 이 흐름을 도와주는 핵심 장치입니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-10-day18.md
