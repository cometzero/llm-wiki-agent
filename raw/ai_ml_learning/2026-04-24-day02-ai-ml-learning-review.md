# 2026-04-24 AI/ML Learning Day 02

- Date: 2026-04-24
- Day: 02/30
- Level: beginner-intermediate
- Theme: 수학 표현과 확률 기초

## 학습 내용

### 오늘의 3가지 개념
1. 확률변수와 확률분포
2. 기댓값, 분산, 공분산
3. 조건부확률과 베이즈 정리

### 핵심 요약

#### 1) 확률변수와 확률분포
- 확률변수(random variable)는 불확실한 결과를 숫자로 대응시키는 함수다.
- distribution은 그 확률변수가 어떤 값을 어떤 비중으로 가질지 기술한다.
- 이산형에서는 PMF, 연속형에서는 PDF, 누적 관점에서는 CDF를 사용한다.
- likelihood, sampling, generative modeling의 출발점이 된다.

#### 2) 기댓값, 분산, 공분산
- expectation은 분포의 평균적 위치를, variance는 평균 주변의 퍼짐을 나타낸다.
- covariance는 두 확률변수가 함께 어떻게 변하는지를 측정한다.
- correlation은 covariance를 스케일 정규화한 값이다.
- normalization, PCA, Gaussian modeling, feature analysis에 직접 연결된다.

#### 3) 조건부확률과 베이즈 정리
- conditional probability는 추가 정보가 주어졌을 때 확률이 어떻게 바뀌는지 다룬다.
- Bayes theorem은 prior를 data를 통해 posterior로 업데이트하는 규칙이다.
- prior, likelihood, posterior를 구분하는 것이 핵심이다.
- classification, calibration, diagnosis, spam filtering에 널리 쓰인다.

## 복습 질문
1. PMF, PDF, CDF는 각각 어떤 상황에서 쓰이며 서로 어떤 관계를 가질까?
2. variance와 covariance는 각각 무엇을 측정하며, correlation은 왜 따로 쓰는가?
3. Bayes theorem에서 prior, likelihood, posterior의 역할을 분류 문제 관점에서 설명해볼 수 있을까?

## 복습 정답과 설명

### 1. PMF, PDF, CDF는 각각 어떤 상황에서 쓰이며 서로 어떤 관계를 가질까?
**정답**
- PMF: 이산(discrete) 확률변수에서 각 값의 확률을 나타낼 때 사용한다.
- PDF: 연속(continuous) 확률변수에서 확률의 밀도(density)를 나타낼 때 사용한다.
- CDF: 이산/연속 모두에서 어떤 값 이하일 누적확률을 나타낼 때 사용한다.

**설명**
PMF는 주사위처럼 값이 딱딱 떨어지는 이산형 변수에서 각 점의 확률 질량(probability mass)을 준다. PDF는 연속형 변수에서 특정 점의 확률이 아니라 구간에 대한 확률을 계산하기 위한 밀도 함수다. CDF는 누적확률 함수로, x 이하의 확률을 직접 보여준다. 관계는 이산형에서는 PMF를 누적하면 CDF가 되고, 연속형에서는 PDF를 적분하면 CDF가 된다. 충분히 매끄러운 경우 CDF를 미분하면 PDF를 얻을 수 있다.

### 2. variance와 covariance는 각각 무엇을 측정하며, correlation은 왜 따로 쓰는가?
**정답**
- variance: 한 확률변수가 평균 주변에서 얼마나 퍼져 있는지 측정한다.
- covariance: 두 확률변수가 함께 어떻게 변하는지 측정한다.
- correlation: covariance를 스케일 정규화해 단위가 다른 변수도 비교 가능하게 만든다.

**설명**
variance는 하나의 변수만 보고 퍼짐 정도를 측정한다. covariance는 두 변수가 함께 증가하는지, 반대로 움직이는지 같은 공동 변화 패턴을 보여준다. 하지만 covariance는 단위와 스케일의 영향을 크게 받기 때문에 변수 간 관계 강도를 직접 비교하기 어렵다. correlation은 covariance를 각 변수의 표준편차로 나눠 정규화한 값이므로 -1에서 1 사이에서 해석할 수 있고, 서로 다른 단위나 크기를 가진 변수끼리도 관계의 강도를 공정하게 비교할 수 있다.

### 3. Bayes theorem에서 prior, likelihood, posterior의 역할을 분류 문제 관점에서 설명해볼 수 있을까?
**정답**
- prior: 데이터를 보기 전, 클래스가 원래 얼마나 그럴듯한지에 대한 사전 확률
- likelihood: 특정 클래스라고 가정했을 때 지금 같은 입력을 볼 가능성
- posterior: 실제 입력을 본 뒤 그 입력이 해당 클래스일 확률

**설명**
분류 문제에서 우리가 궁극적으로 알고 싶은 것은 P(y|x), 즉 입력 x가 주어졌을 때 클래스 y일 확률이다. 이것이 posterior다. Bayes theorem은 posterior를 P(x|y)P(y)에 비례하는 값으로 표현한다. 여기서 prior P(y)는 데이터를 보기 전의 기본 믿음이고, likelihood P(x|y)는 해당 클래스가 주어졌을 때 지금 같은 데이터를 볼 가능성이다. posterior는 이 둘을 결합해 업데이트된 최종 판단이다. Naive Bayes는 이 구조를 직접 사용하고, 현대 딥러닝 분류도 넓게 보면 조건부 class distribution을 학습하는 문제로 이해할 수 있다.

## 한 줄 정리
확률변수와 distribution이 불확실성을 표현하고, expectation·variance·covariance가 그 구조를 요약하며, conditional probability와 Bayes theorem이 새로운 정보에 따라 믿음을 업데이트한다.
