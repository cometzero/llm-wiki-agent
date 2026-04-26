# 2026-04-23 AI/ML Learning Day 01

- Date: 2026-04-23
- Day: 01/30
- Level: beginner-intermediate
- Theme: 수학 표현과 확률 기초

## 학습 내용

### 오늘의 3가지 개념
1. 벡터공간과 좌표 표현
2. 행렬과 선형사상(linear map)
3. 내적(dot product), norm, 거리

---

## 1) 벡터공간과 좌표 표현

### 한 줄 직관
벡터는 **숫자 여러 개로 어떤 대상을 표현하는 방법**이고, 좌표는 그 벡터를 **어떤 기준으로 적었는지**를 보여주는 숫자표다.

### 쉬운 설명
AI 모델 안에서는 대부분의 데이터가 숫자로 바뀐다. 이미지, 단어, 문장, 음성도 결국은 숫자 묶음으로 표현된다. 이 숫자 묶음의 가장 기본 형태가 벡터다.

예를 들어 사람 한 명을 아주 단순하게
- 키 175
- 몸무게 70
- 나이 30

으로 적는다면, 이 사람을 `[175, 70, 30]` 같은 벡터로 표현할 수 있다.

LLM에서도 비슷하다.
- `cat` → `[0.2, -0.5, 1.3, 0.7, ...]`
- `dog` → `[0.3, -0.4, 1.1, 0.8, ...]`

이런 표현을 embedding이라고 부른다.

### 핵심 포인트
- 벡터는 어떤 대상을 숫자로 표현한 결과다.
- 벡터공간(vector space)은 벡터들이 놓이는 공간이다.
- 좌표(coordinate)는 벡터 자체가 아니라, **basis(기저)** 기준으로 적은 숫자다.
- 같은 벡터라도 basis가 바뀌면 coordinate는 달라질 수 있다.

예를 들어 서울역이라는 같은 장소도
- 위도/경도
- 도로명 주소
- 지하철 노선 기준

으로 다르게 표현할 수 있다. 벡터도 마찬가지다. 벡터 자체는 같아도, 어떤 기준축으로 보느냐에 따라 좌표 숫자는 달라진다.

### AI 연결
LLM 안에서 token embedding, hidden state, gradient는 모두 벡터다. Transformer는 이 벡터들을 layer마다 바꾸고, 다시 비교하고, 또 변환한다. 즉 AI 모델은 내부적으로 **벡터를 계속 바꾸고 비교하는 시스템**이라고 볼 수 있다.

---

## 2) 행렬과 선형사상(linear map)

### 한 줄 직관
행렬은 **입력 벡터를 다른 벡터로 바꾸는 변환기**라고 생각하면 된다.

### 쉬운 설명
행렬은 겉으로 보면 숫자표다.

```text
[ 1  2 ]
[ 3  4 ]
```

하지만 AI/ML에서는 이것을 단순 숫자표보다 **변환 도구**로 보는 것이 훨씬 중요하다.

예를 들어 입력 벡터 `x = [1, 2]`가 있고,

```text
W = [ 2  0 ]
    [ 0  3 ]
```

이라면 `Wx = [2, 6]`이 된다.

이것은
- 첫 번째 방향은 2배
- 두 번째 방향은 3배

로 바꾸었다는 뜻이다.

### 핵심 포인트
- 행렬(matrix)은 벡터를 다른 벡터로 보내는 선형사상(linear map)의 계산 표현이다.
- 선형사상은 덧셈과 스칼라배 구조를 보존한다.
- rank는 변환 후에도 살아남는 독립 정보의 수를 뜻한다.

예를 들어 2차원 점들이 어떤 행렬을 거친 뒤 모두 한 직선 위로 눌려버리면, 원래 2차원 정보가 1차원으로 줄어든 것이므로 rank는 1이라고 볼 수 있다.

### AI 연결
신경망의 dense layer는 보통

`y = W x + b`

형태다. Transformer에서도
- `Q = XWq`
- `K = XWk`
- `V = XWv`

처럼 행렬 곱이 계속 등장한다. 즉 행렬은 신경망 안에서 **표현을 바꾸는 핵심 기계**다.

또 LoRA에서 말하는 low-rank도 이 rank 개념과 직접 연결된다.

---

## 3) 내적(dot product), norm, 거리

### 한 줄 직관
벡터끼리 얼마나 비슷한지, 얼마나 큰지, 얼마나 떨어져 있는지를 재는 도구가 바로 dot product, norm, 거리다.

### 쉬운 설명
두 벡터가 있다고 하자.
- `A = [1, 2]`
- `B = [3, 4]`

#### dot product
같은 자리끼리 곱해서 더한다.

`A · B = 1×3 + 2×4 = 11`

보통 값이 크면 두 벡터가 비슷한 방향을 본다고 해석할 수 있다. 다만 방향뿐 아니라 크기 영향도 함께 들어간다.

#### norm
벡터 `v = [3, 4]`의 L2 norm은

`||v||2 = sqrt(3^2 + 4^2) = 5`

즉 벡터의 길이, 크기를 뜻한다.

#### cosine similarity
- `A = [1, 1]`
- `B = [10, 10]`

은 크기는 다르지만 방향은 같다. 그래서 cosine similarity는 매우 높게 나온다. 즉 cosine similarity는 크기를 지우고 **방향 유사도**에 집중한다.

### 핵심 포인트
- dot product: 방향 + 크기를 함께 반영한 관련도
- norm: 벡터의 크기
- cosine similarity: 방향 유사도
- 거리(distance): 두 벡터가 얼마나 다른지

### AI 연결
Transformer attention에서는 Query와 Key의 dot product를 계산한다.

`score = Q · K`

이 값이 크면 관련도가 높다고 본다.

Embedding search에서는 cosine similarity를 많이 쓴다. 예를 들어
- `고양이가 소파에 앉아 있다`
- `cat is sitting on a sofa`

같은 문장은 방향이 비슷한 벡터가 되기 쉽기 때문이다.

norm은 regularization, gradient clipping, 벡터 크기 안정화에 연결된다.

---

## 복습 질문
1. 같은 벡터라도 basis가 바뀌면 coordinate가 왜 달라질 수 있을까?
2. 행렬을 단순한 숫자표가 아니라 linear map으로 보면, rank는 무엇을 의미할까?
3. dot product, L2 norm, cosine similarity는 각각 무엇을 측정하며 attention이나 embedding search에서 어떻게 쓰일까?

## 복습 정답과 설명

### 1. 같은 벡터라도 basis가 바뀌면 coordinate가 왜 달라질 수 있을까?
**정답**
좌표는 벡터 자체가 아니라, 선택한 basis 기준으로 그 벡터를 어떻게 적었는지를 나타내는 값이기 때문이다.

**설명**
벡터는 공간 안의 대상이고, coordinate는 그 대상을 특정 기준축으로 읽어낸 숫자 표현이다. 따라서 basis가 바뀌면 같은 벡터라도 새로운 basis 조합으로 다시 적어야 하므로 coordinate 값이 달라진다. 핵심은 **벡터는 불변이고 coordinate는 basis-dependent**라는 점이다.

### 2. 행렬을 단순한 숫자표가 아니라 linear map으로 보면, rank는 무엇을 의미할까?
**정답**
rank는 그 변환이 실제로 살려내는 독립 정보의 차원 수를 의미한다.

**설명**
행렬을 linear map으로 보면 입력을 다른 공간으로 보내는 규칙으로 이해할 수 있다. 이때 rank는 출력이 실제로 펼쳐질 수 있는 공간의 차원, 즉 변환 뒤에도 유지되는 독립 방향의 수를 뜻한다. rank가 낮으면 일부 정보는 눌리거나 사라진다. 그래서 rank는 변환의 정보 보존 정도를 보여주는 지표다.

### 3. dot product, L2 norm, cosine similarity는 각각 무엇을 측정하며 attention이나 embedding search에서 어떻게 쓰일까?
**정답**
- dot product: 두 벡터의 방향성과 크기가 결합된 관련도
- L2 norm: 벡터의 크기
- cosine similarity: 크기를 제거한 방향 유사도

**설명**
dot product는 attention에서 query와 key의 관련도를 점수화할 때 쓰인다. L2 norm은 regularization, gradient clipping, 거리 계산의 기반이 된다. cosine similarity는 embedding search나 retrieval에서 의미 유사도를 비교할 때 자주 쓴다.

## 한 줄 정리
벡터는 AI 내부의 데이터 표현이고, 행렬은 그 표현을 바꾸는 변환기이며, dot product·norm·cosine similarity는 표현끼리의 관계를 재는 도구다.
