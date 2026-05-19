# AI/ML Learning Review - Day 27 (2026-05-19)
## Source Metadata
- Lesson file: `/home/ubuntu/work/ai/learning/logs/2026-05-19-day27.md`
- State file: `/home/ubuntu/work/ai/learning/state.json`
- Follow-up answer file: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-19_09-26-19.md`

---

## Lesson

# Day 27 - AI/ML 기초 학습

- Date: 2026-05-19
- Progress: 27/30
- Level: beginner-intermediate
- Milestone: LLM 구조와 학습 파이프라인
- Milestone goal: LLM이 어떻게 학습되고 추론되는지 현대적 관점으로 정리한다.

## Today's 3 concepts

1. 추론 시 디코딩 전략
2. 컨텍스트 윈도우와 메모리 한계
3. 환각, calibration, grounding

---

## 1. 추론 시 디코딩 전략

### 한 줄 직관

LLM은 다음 단어 후보들에 점수를 매기고, 디코딩 전략(decoding strategy)은 그 후보들 중에서 “어떤 방식으로 하나를 고를지” 정하는 규칙이다.

### 개념 정의

LLM이 문장을 생성할 때는 한 번에 전체 답을 쓰는 것이 아니다. 먼저 지금까지의 prompt와 이미 생성한 단어들을 보고 “다음 token으로 무엇이 올 가능성이 높은가?”를 계산한다. 여기서 token은 단어 전체일 수도 있고, 단어 조각일 수도 있다.

모델의 마지막 출력은 보통 vocabulary 전체에 대한 점수이다. 예를 들어 vocabulary에 `사과`, `바나나`, `자동차`라는 token만 있다고 해 보자. 모델은 다음 token에 대해 다음과 같은 점수를 낼 수 있다.

- `사과`: 5.0
- `바나나`: 4.0
- `자동차`: 1.0

이 점수는 softmax를 거쳐 확률처럼 바뀐다. 그 다음 “확률이 가장 큰 것만 고를지”, “상위 몇 개 중에서 랜덤하게 고를지”, “너무 낮은 후보는 버릴지”를 정해야 한다. 이 선택 방식이 디코딩 전략이다.

### 왜 이런 개념이 필요한가

같은 LLM이라도 디코딩 전략이 다르면 답변 스타일이 크게 달라진다.

- 항상 가장 높은 확률만 고르면 답이 안정적이지만 반복적이고 재미없을 수 있다.
- 조금 랜덤하게 고르면 창의적인 답이 나오지만 틀린 말이 섞일 수 있다.
- 후보를 너무 넓게 열어 두면 엉뚱한 token이 나올 수 있다.
- 후보를 너무 좁게 제한하면 다양한 표현을 못 한다.

즉, 디코딩은 모델의 “지식”을 바꾸지는 않지만, 그 지식이 실제 답변으로 나오는 방식을 조절한다. ChatGPT 같은 서비스에서 “더 창의적으로 써 줘”, “정확하게만 답해 줘” 같은 차이가 생기는 중요한 이유 중 하나가 디코딩 설정이다.

### 아주 쉬운 예시

문장 시작이 다음과 같다고 하자.

> 나는 아침에 ____을 먹었다.

모델이 다음 token 후보를 이렇게 예측했다고 하자.

| token | 확률 |
|---|---:|
| 빵 | 0.50 |
| 밥 | 0.30 |
| 사과 | 0.15 |
| 우주선 | 0.05 |

- greedy decoding은 가장 높은 `빵`을 고른다.
- top-k에서 k=2라면 `빵`, `밥`만 남기고 둘 중에서 뽑는다.
- top-p에서 p=0.8이라면 누적 확률이 0.8이 될 때까지 `빵`과 `밥`을 남긴다. 0.50 + 0.30 = 0.80이기 때문이다.
- temperature가 높으면 `사과`나 심지어 `우주선` 같은 낮은 확률 후보가 뽑힐 가능성도 상대적으로 커진다.

### 개념 구조와 핵심 포인트

1. **모델은 먼저 logit을 낸다**  
   logit은 softmax 전의 원점수이다. 모델은 vocabulary의 모든 token에 대해 logit을 만든다.

2. **softmax가 확률 분포를 만든다**  
   logit이 큰 token일수록 확률이 커진다. 하지만 확률이 1개만 있는 것이 아니라 전체 후보에 확률이 나뉘어 있다.

3. **디코딩 전략이 실제 token을 선택한다**  
   이 단계에서 greedy decoding, beam search, temperature, top-k, top-p 같은 기법을 쓴다.

4. **선택한 token을 다시 입력에 붙인다**  
   예를 들어 `빵`을 골랐다면 다음 단계에서는 `나는 아침에 빵`까지를 보고 다시 다음 token을 예측한다. 이 과정을 반복하면 긴 답변이 만들어진다.

### 핵심 수학 포인트

핵심은 “점수 → 확률 → 선택”이다.

가장 단순하게 token A, B, C의 확률이 다음과 같다고 해 보자.

- A: 0.7
- B: 0.2
- C: 0.1

greedy decoding은 항상 A를 고른다. 확률이 가장 크기 때문이다.

반면 sampling은 확률에 따라 뽑는다. 10번 뽑으면 평균적으로 A가 7번, B가 2번, C가 1번 정도 나올 수 있다. 물론 랜덤이므로 정확히 그렇게 나오지는 않는다.

**temperature**는 softmax 전에 logit을 나누는 값이다.

- temperature가 낮으면 높은 점수 token이 더 압도적으로 커진다. 답이 보수적이고 반복적이기 쉽다.
- temperature가 높으면 점수 차이가 완만해진다. 낮은 확률 token도 나올 가능성이 커진다.

직관적으로 temperature는 “선택의 과감함”을 조절하는 손잡이라고 보면 된다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **greedy decoding**: 매 단계에서 확률이 가장 높은 token 하나를 고르는 방식.
- **beam search**: 한 가지 후보만 따라가지 않고, 여러 개의 후보 문장 경로를 동시에 유지하며 더 좋은 문장을 찾는 방식.
- **temperature**: token 확률 분포를 날카롭게 또는 부드럽게 만드는 값. 낮으면 보수적, 높으면 다양해진다.
- **top-k**: 확률이 높은 상위 k개 token만 남기고 그 안에서 선택하는 방식.
- **top-p**: 누적 확률이 p가 될 때까지의 token만 남기는 방식. nucleus sampling이라고도 부른다.

### AI에서 어디에 쓰이는가

- 챗봇 답변 생성에서 정확성과 창의성의 균형을 맞출 때 쓴다.
- 코드 생성 모델에서는 낮은 temperature를 자주 쓴다. 코드에서는 창의성보다 정확성이 중요하기 때문이다.
- 소설, 마케팅 문구, 아이디어 생성에서는 더 높은 temperature와 top-p를 쓰기도 한다.
- 번역이나 요약처럼 입력에 충실해야 하는 작업에서는 후보를 너무 넓게 열지 않는 것이 좋다.
- LLM API의 `temperature`, `top_p`, `max_tokens` 같은 옵션은 실제 제품 품질에 직접 영향을 준다.

### 헷갈리기 쉬운 포인트

- temperature가 높다고 모델이 더 똑똑해지는 것은 아니다. 단지 더 다양한 후보를 고르게 할 뿐이다.
- greedy decoding이 항상 가장 좋은 답을 보장하지는 않는다. 매 순간 좋아 보이는 선택이 전체 문장에서는 어색할 수 있다.
- beam search는 번역 같은 작업에서는 유용했지만, 대화형 LLM에서는 너무 딱딱하거나 반복적인 결과를 만들 수 있다.
- top-k와 top-p는 둘 다 후보를 자르는 방식이지만 기준이 다르다. top-k는 개수 기준이고, top-p는 누적 확률 기준이다.

---

## 2. 컨텍스트 윈도우와 메모리 한계

### 한 줄 직관

컨텍스트 윈도우(context window)는 LLM이 한 번에 읽고 참고할 수 있는 “작업 책상 크기”이고, 이 책상이 꽉 차면 앞의 내용 일부를 더 이상 직접 보지 못한다.

### 개념 정의

LLM은 대화 전체를 사람처럼 머릿속에 영구 저장해 두는 것이 아니다. 매번 답을 만들 때는 입력으로 들어온 token들을 보고 계산한다. 이때 모델이 한 번에 처리할 수 있는 최대 token 수를 context window라고 한다.

예를 들어 어떤 모델의 context window가 8,000 tokens라면, prompt, 이전 대화, 첨부 문서, 모델이 생성하는 답변까지 합쳐서 대략 그 범위 안에 있어야 한다. 이 한계를 넘으면 앞부분을 잘라내거나, 요약하거나, 검색 시스템을 붙여 필요한 부분만 가져와야 한다.

### 왜 이런 개념이 필요한가

LLM을 실제로 쓰다 보면 “아까 말했잖아”라고 했는데 모델이 기억하지 못하는 경우가 있다. 이것은 모델이 무성의해서가 아니라, 현재 입력 context 안에 그 정보가 없기 때문일 수 있다.

또한 긴 문서를 넣고 질문할 때도 context window가 중요하다. 모델이 문서 전체를 읽을 수 없다면 중요한 부분이 빠질 수 있다. 그래서 RAG(Retrieval-Augmented Generation), 요약 memory, chunking 같은 기술이 필요해진다.

컨텍스트 한계는 비용과 속도에도 영향을 준다. token이 많을수록 attention 계산량과 KV cache 메모리가 커진다. 따라서 긴 context를 무조건 많이 넣는 것이 항상 좋은 전략은 아니다.

### 아주 쉬운 예시

모델의 context window가 아주 작아서 10 tokens라고 가정해 보자.

사용자 대화가 이렇게 길어진다.

1. “내 이름은 민수야.”
2. “나는 부산에 살아.”
3. “내가 좋아하는 음식은 김밥이야.”
4. “내 이름이 뭐였지?”

전체가 10 tokens를 넘으면 시스템이 앞부분 “내 이름은 민수야”를 잘라낼 수 있다. 그러면 모델은 현재 context 안에서 이름 정보를 볼 수 없으므로 제대로 답하기 어렵다.

사람 비유로 말하면, 책상 위에 종이를 10장만 올려둘 수 있는데 15장이 오면 가장 오래된 5장을 치워야 하는 상황과 비슷하다. 치워진 종이에 이름이 적혀 있었다면, 지금 책상만 보고는 이름을 알 수 없다.

### 개념 구조와 핵심 포인트

1. **prompt length**  
   입력 prompt의 길이이다. 시스템 메시지, 사용자 질문, 이전 대화, 문서 내용이 모두 포함된다.

2. **context window**  
   모델이 한 번에 처리할 수 있는 최대 token 범위이다. 입력과 출력이 같은 window를 공유하는 경우가 많다.

3. **attention은 context 안의 token들 사이 관계를 계산한다**  
   Transformer는 각 token이 다른 token을 얼마나 참고할지 attention으로 계산한다. 그래서 context가 길수록 참고할 수 있는 정보가 많아진다.

4. **KV cache는 추론 속도를 높이지만 메모리를 쓴다**  
   LLM은 한 token씩 생성한다. 매번 처음부터 모든 계산을 다시 하면 너무 느리다. 그래서 이전 token들의 key와 value를 저장해 둔다. 이것이 KV cache이다.

5. **긴 context는 공짜가 아니다**  
   더 긴 context는 더 많은 GPU memory, 더 긴 처리 시간, 더 높은 비용을 요구한다.

### 핵심 수학 포인트

Transformer의 attention은 단순하게 말하면 token들끼리 서로 점수를 매기는 구조이다.

예를 들어 문장에 token이 4개 있다고 하자.

- T1 = 나는
- T2 = 오늘
- T3 = 김밥을
- T4 = 먹었다

각 token은 다른 token들을 참고한다. 그러면 4개 token 사이의 관계는 4 × 4 표처럼 생각할 수 있다. token이 4개면 16개의 관계 점수가 생긴다.

만약 token이 1,000개라면 단순 attention 관계는 대략 1,000 × 1,000 = 1,000,000개 규모가 된다. 실제 구현은 더 최적화되어 있지만, 길이가 늘면 계산과 메모리가 빠르게 커진다는 직관은 중요하다.

KV cache도 비슷하다. 생성된 token마다 key와 value hidden state를 저장한다. token이 많고 layer가 많고 hidden size가 클수록 cache가 커진다. 그래서 긴 대화를 유지하려면 더 많은 GPU memory가 필요하다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **context window**: 모델이 한 번에 볼 수 있는 최대 token 범위.
- **prompt length**: 현재 입력 prompt가 차지하는 token 길이.
- **KV cache**: 이전 token들의 key/value 계산 결과를 저장해 다음 token 생성 속도를 높이는 메모리 구조.

### AI에서 어디에 쓰이는가

- 긴 PDF나 보고서를 넣고 질문할 때 context window가 충분한지 확인해야 한다.
- 챗봇에서 이전 대화를 얼마나 유지할지 결정할 때 중요하다.
- RAG 시스템에서는 전체 문서를 다 넣지 않고, 검색으로 관련 chunk만 context에 넣는다.
- agent 시스템에서는 작업 기록을 모두 넣으면 context가 터질 수 있으므로 요약 memory나 external database를 쓴다.
- 추론 서버 운영에서는 KV cache 때문에 동시 사용자 수, batch size, latency가 달라진다.

### 헷갈리기 쉬운 포인트

- “모델이 학습한 지식”과 “현재 context에 들어 있는 정보”는 다르다. 학습한 지식은 parameter에 저장된 일반 패턴이고, context는 지금 당장 참고하는 입력이다.
- context window가 길다고 항상 답이 좋아지는 것은 아니다. 관련 없는 내용이 너무 많으면 모델이 중요한 부분을 놓칠 수 있다.
- KV cache는 장기 기억이 아니다. 현재 generation을 빠르게 하기 위한 임시 계산 저장소이다.
- prompt length가 길면 비용이 늘고 속도가 느려질 수 있다. 그래서 필요한 정보만 잘 넣는 prompt 설계가 중요하다.

---

## 3. 환각, calibration, grounding

### 한 줄 직관

LLM은 그럴듯한 문장을 잘 만들지만, 그 문장이 사실인지 항상 보장하지는 않는다. hallucination, calibration, grounding은 “모델 답변을 얼마나 믿을 수 있는가”를 다루는 핵심 개념이다.

### 개념 정의

**hallucination**은 모델이 사실이 아닌 내용을 그럴듯하게 만들어내는 현상이다. 한국어로는 환각이라고도 하지만, 실무에서는 hallucination이라는 영어 표현을 많이 쓴다.

**calibration**은 모델의 자신감이 실제 정답률과 얼마나 잘 맞는지를 뜻한다. 예를 들어 모델이 “90% 확실하다”고 말한 문제들을 모아 봤을 때 실제로 90% 정도 맞으면 calibration이 좋다고 말한다.

**grounding**은 답변을 외부 근거에 연결하는 것이다. 예를 들어 문서, 데이터베이스, 검색 결과, citation, tool output 같은 실제 근거를 보고 답하게 만드는 방식이다.

### 왜 이런 개념이 필요한가

LLM은 next token prediction으로 학습된다. 즉, 기본 목표는 “다음 token을 잘 맞히는 것”이지 “세상의 사실을 검증하는 것”이 아니다. 그래서 문장 흐름상 자연스러운 답을 만들 수는 있지만, 그 내용이 실제로 맞는지는 별개의 문제이다.

의료, 법률, 금융, 회사 내부 문서 검색 같은 분야에서는 틀린 답이 큰 문제가 된다. 이때 단순히 “말을 잘하는 모델”보다 “근거를 확인하고, 모르면 모른다고 말하고, 자신감 수준이 실제 정확도와 맞는 모델”이 중요하다.

### 아주 쉬운 예시

사용자가 묻는다.

> 우리 회사의 2025년 3분기 매출은 얼마야?

모델이 회사 내부 데이터에 접근하지 못하는데도 이렇게 답한다고 하자.

> 2025년 3분기 매출은 120억 원입니다.

이 답이 실제 근거 없이 만들어졌다면 hallucination이다.

반대로 grounded answer는 이렇게 말할 수 있다.

> 제공된 2025_Q3_sales.pdf의 3페이지 표에 따르면 3분기 매출은 118억 원입니다. 문서에 4분기 수치는 없습니다.

여기서는 답변이 특정 문서와 연결되어 있다. 그리고 모르는 부분은 모른다고 말한다. 이것이 grounding과 uncertainty 표현의 좋은 예이다.

calibration의 작은 숫자 예시도 보자.

모델이 10개 질문에 대해 각각 “80% 확실하다”고 말했다. 그런데 실제로 10개 중 8개를 맞혔다면 calibration이 꽤 좋다. 하지만 10개 중 3개만 맞혔다면 모델의 confidence는 과하게 높았던 것이다.

### 개념 구조와 핵심 포인트

1. **hallucination은 그럴듯함과 사실성이 다를 때 생긴다**  
   LLM은 문장 패턴을 매우 잘 배운다. 그래서 실제 근거가 없어도 자연스러운 답을 만들 수 있다.

2. **uncertainty를 표현할 수 있어야 한다**  
   모델이 모르는 것을 모른다고 말하는 능력은 실무에서 매우 중요하다. “확실하지 않습니다”는 실패가 아니라 안전한 동작일 수 있다.

3. **calibration은 confidence의 품질이다**  
   confidence가 높을 때 실제로도 자주 맞아야 한다. confidence만 높고 정답률이 낮으면 위험하다.

4. **grounding은 답변을 근거에 묶는다**  
   RAG, tool use, citation, database lookup은 모두 grounding을 강화하는 방법이다.

5. **검증 가능한 출력이 중요하다**  
   사용자가 답을 확인할 수 있도록 출처, 계산 과정, 사용한 데이터 범위를 제공하는 것이 좋다.

### 핵심 수학 포인트

calibration은 확률 예측의 문제로 볼 수 있다.

아주 단순한 예를 보자. 모델이 100개 질문에 대해 “70% 확률로 맞다”고 예측한 답변들을 모았다. calibration이 좋다면 이 100개 중 실제 정답이 약 70개여야 한다.

- 예측 confidence: 70%
- 실제 정답률: 70%
- calibration: 좋음

반대로 실제로 40개만 맞았다면:

- 예측 confidence: 70%
- 실제 정답률: 40%
- calibration: 나쁨, 과신(overconfidence)

LLM의 token 확률도 confidence처럼 보일 수 있지만, token 확률이 높다고 항상 사실 확률이 높은 것은 아니다. 예를 들어 “프랑스의 수도는 파리”는 token 확률과 사실성이 잘 맞을 수 있다. 하지만 “어떤 작은 회사의 최신 매출”처럼 학습 데이터에 없거나 오래된 정보는 token 확률이 높아도 사실이 아닐 수 있다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **hallucination**: 모델이 사실이 아닌 내용을 그럴듯하게 생성하는 현상.
- **calibration**: 모델의 confidence와 실제 정답률이 얼마나 잘 맞는지 나타내는 성질.
- **grounding**: 답변을 문서, 데이터, 검색 결과, tool output 같은 외부 근거에 연결하는 것.
- **uncertainty**: 모델이 얼마나 확실하지 않은지 나타내는 불확실성.

### AI에서 어디에 쓰이는가

- RAG 기반 문서 QA에서 답변에 citation을 붙이는 이유가 grounding 때문이다.
- 의료/법률/금융 AI에서는 hallucination을 줄이고 uncertainty를 표시하는 것이 필수에 가깝다.
- customer support 챗봇은 회사 정책 문서에 grounded되어야 한다. 정책에 없는 내용을 만들어내면 안 된다.
- agent가 tool을 사용할 때는 검색 결과, 계산 결과, DB 조회 결과를 근거로 답해야 한다.
- 모델 평가에서는 단순 정답률뿐 아니라 calibration과 hallucination rate도 함께 본다.

### 헷갈리기 쉬운 포인트

- 말투가 자신감 있어도 정답이라는 뜻은 아니다. LLM은 틀린 말도 매우 자연스럽게 말할 수 있다.
- grounding이 있다고 해서 항상 100% 안전한 것은 아니다. 검색된 문서가 틀렸거나, 모델이 문서를 잘못 읽을 수 있다.
- calibration은 “모델이 확률 숫자를 말하는 능력”만이 아니라, 그 숫자가 실제 결과와 맞는지를 보는 개념이다.
- uncertainty를 표현하는 모델이 약한 모델은 아니다. 오히려 위험한 상황에서는 모른다고 말하는 것이 더 좋은 모델 행동이다.

---

## 복습 질문 3개

1. greedy decoding, top-k, top-p는 각각 다음 token 후보를 어떤 기준으로 고르거나 제한하는가?
2. context window와 KV cache는 각각 무엇이며, 긴 대화나 긴 문서 처리에서 왜 문제가 될 수 있는가?
3. hallucination을 줄이기 위해 grounding이 필요한 이유는 무엇이고, calibration은 어떤 상황에서 중요해지는가?

## 오늘의 한 줄 요약

LLM 추론은 “다음 token을 어떻게 고를지”, “얼마나 많은 context를 볼 수 있는지”, “답을 얼마나 믿을 수 있게 만들지”가 함께 결정하는 과정이다.

---

## Follow-up Answers

# Cron Job: AI ML 복습질문 정답

**Job ID:** b2c07d928d85
**Run Time:** 2026-05-19 09:26:19
**Schedule:** 25 9 * * *

## Prompt

[IMPORTANT: You are running as a scheduled cron job. DELIVERY: Your final response will be automatically delivered to the user — do NOT use send_message or try to deliver the output yourself. Just produce your report/output as your final response and the system handles the rest. SILENT: If there is genuinely nothing new to report, respond with exactly "[SILENT]" (nothing else) to suppress delivery. Never combine [SILENT] with content — either report your findings normally, or say [SILENT] and nothing more.]

## Script Output
The following data was collected by a pre-run script. Use it as context for your analysis.

```
{
  "program_title": "AI/ML Fundamentals Daily Learning",
  "level": "beginner-intermediate",
  "teaching_style": [
    "AI/ML을 처음 공부하는 사람도 따라올 수 있게 쉬운 말로 먼저 설명하고, 어려운 용어는 바로 풀어서 설명한다",
    "각 개념마다 반드시 아주 작은 숫자 예시나 일상 비유를 넣어 직관을 먼저 만든다",
    "설명은 짧게 끊지 말고 왜 그런지까지 자세히 풀어주되, 문장 구조는 단순하게 유지한다",
    "수학적 의미는 숨기지 않되 수식보다 먼저 직관, 예시, AI에서의 사용처 순서로 설명한다",
    "각 개념마다 반드시 배워야 할 핵심 용어를 함께 학습하고, 실전 모델/논문/구현과 연결되는 관점을 유지한다"
  ],
  "date": "2026-05-19",
  "day_number": 27,
  "total_days": 30,
  "concepts_per_day": 3,
  "milestone_names": [
    "LLM 구조와 학습 파이프라인"
  ],
  "milestone_goals": [
    "LLM이 어떻게 학습되고 추론되는지 현대적 관점으로 정리한다."
  ],
  "concepts": [
    "추론 시 디코딩 전략",
    "컨텍스트 윈도우와 메모리 한계",
    "환각, calibration, grounding"
  ],
  "concept_term_map": [
    {
      "concept": "추론 시 디코딩 전략",
      "terms": [
        "greedy decoding",
        "beam search",
        "temperature",
        "top-k",
        "top-p"
      ]
    },
    {
      "concept": "컨텍스트 윈도우와 메모리 한계",
      "terms": [
        "context window",
        "prompt length",
        "KV cache"
      ]
    },
    {
      "concept": "환각, calibration, grounding",
      "terms": [
        "hallucination",
        "calibration",
        "grounding",
        "uncertainty"
      ]
    }
  ],
  "target_markdown_path": "/home/ubuntu/work/ai/learning/logs/2026-05-19-day27.md",
  "state_path": "/home/ubuntu/work/ai/learning/state.json",
  "already_completed_today": true,
  "last_completed_date": "2026-05-19",
  "last_completed_file": "/home/ubuntu/work/ai/learning/logs/2026-05-19-day27.md",
  "next_day_after_completion": 28,
  "commit_message": "docs: add AI/ML lesson for day 27 (2026-05-19)"
}
```

You are sending the daily follow-up answers for the AI/ML learning workspace at /home/ubuntu/work/ai.

The Python pre-script has already run and its stdout is injected above as JSON. Parse that JSON and use it as ground truth.

Goal:
- 10 minutes after the daily lesson, send the user the answers/explanations for today's 3 review questions.
- The answer style must be easy, detailed, and example-driven.
- Assume the user is still learning the concept for the first time.
- The tone should resemble a patient workbook explanation, not a compressed model answer.

Rules:
1. Use the injected JSON from the pre-script.
2. Read `last_completed_file` from that JSON. This should be today's lesson markdown when `already_completed_today` is true.
3. If `last_completed_file` is missing, unreadable, or `last_completed_date` does not match `date`, send a short Korean message that today's lesson file is not ready yet and stop.
4. Otherwise, read the markdown lesson file and extract the section `## 복습 질문 3개`.
5. For each of the 3 review questions, provide all of the following in Korean:
   - the original question as a numbered heading
   - `정답`
   - `설명`
   - a very small example or intuitive case
   - `실전 연결` explaining where it matters in ML/DL/LLM
6. The overall format should resemble this pattern:
   - first line: `[AI/ML 오늘의 복습 정답 Day XX/YY]`
   - one short intro line
   - then for each question:
     - `### 1. ...질문...`
     - `**정답**`
     - short direct answer paragraph or bullets
     - `**설명**`
     - a fuller explanation with concept meaning and why it matters
     - `**예시**`
     - one small intuitive example
     - `**실전 연결**`
     - one short paragraph connecting to actual ML/DL/LLM practice
7. Keep the tone at beginner-intermediate AI/ML level, but make the wording easy enough for a newcomer to follow.
8. Prefer natural English technical terms where appropriate (`gradient`, `loss function`, `tensor shape`, `cosine similarity`, etc.), but explain them in easy Korean when first used.
9. Keep the response mobile-friendly Korean text only. Do not use markdown tables.
10. Do not give one-line answers. Each answer should feel complete and beginner-friendly.
11. End with one short line: `기준 파일: <path>`.

Do not modify any files. Do not update state. Do not run git. Just read the lesson file and send the follow-up answer message.

## Response

[AI/ML 오늘의 복습 정답 Day 27/30]

오늘은 LLM이 답을 만들 때 “어떻게 고르고, 얼마나 기억하고, 얼마나 믿을 수 있게 만들지”를 복습합니다.

### 1. greedy decoding, top-k, top-p는 각각 다음 token 후보를 어떤 기준으로 고르거나 제한하는가?

**정답**

- **greedy decoding**은 매 순간 확률이 가장 높은 token 하나만 고릅니다.
- **top-k**는 확률이 높은 상위 k개 token만 남기고, 그 안에서 선택합니다.
- **top-p**는 확률이 높은 순서대로 더했을 때 누적 확률이 p에 도달할 때까지의 token만 남기고, 그 안에서 선택합니다.

즉, greedy는 “1등만 선택”, top-k는 “상위 몇 개만 후보로 유지”, top-p는 “확률 덩어리가 일정 수준이 될 때까지만 후보로 유지”하는 방식입니다.

**설명**

LLM은 답을 한 번에 완성하지 않습니다. 먼저 지금까지의 prompt와 이미 생성한 token을 보고, 다음 token 후보들에 점수를 매깁니다. 여기서 token은 단어일 수도 있고 단어 조각일 수도 있습니다.

예를 들어 다음 단어 후보가 있다고 해 봅시다.

- 빵: 0.50
- 밥: 0.30
- 사과: 0.15
- 우주선: 0.05

**greedy decoding**은 가장 확률이 높은 `빵`을 바로 고릅니다. 안정적이지만 답이 단조롭거나 반복적일 수 있습니다.

**top-k**에서 k=2라면 `빵`, `밥`만 남깁니다. `사과`, `우주선`은 후보에서 제외됩니다. 그 다음 `빵`과 `밥` 중에서 확률에 따라 선택할 수 있습니다.

**top-p**에서 p=0.8이라면 확률이 높은 순서대로 더합니다. `빵` 0.50 + `밥` 0.30 = 0.80이므로 `빵`, `밥`까지만 남깁니다. top-k는 “개수 기준”이고, top-p는 “누적 확률 기준”이라는 점이 핵심 차이입니다.

여기에 **temperature**도 자주 같이 쓰입니다. temperature는 확률 분포를 날카롭게 또는 부드럽게 만드는 값입니다. 낮으면 높은 확률 후보가 더 강해져 보수적인 답이 나오고, 높으면 낮은 확률 후보도 나올 가능성이 커져 더 다양한 답이 나옵니다.

**예시**

문장이 이렇게 시작한다고 해 봅시다.

“오늘 점심에는 ____을 먹었다.”

모델이 다음 후보를 이렇게 봅니다.

- 김밥: 60%
- 라면: 25%
- 샐러드: 10%
- 자동차: 5%

greedy decoding은 항상 `김밥`을 고릅니다.

top-k에서 k=2라면 `김밥`, `라면`만 후보로 남깁니다.

top-p에서 p=0.85라면 `김밥` 60% + `라면` 25% = 85%이므로 역시 `김밥`, `라면`까지만 남깁니다.

만약 temperature를 높이면 `샐러드`가 나올 가능성도 조금 커집니다. 하지만 너무 높이면 문맥에 맞지 않는 이상한 단어가 나올 위험도 커집니다.

**실전 연결**

LLM API를 사용할 때 `temperature`, `top_p`, `max_tokens` 같은 설정은 답변 품질에 직접 영향을 줍니다. 코드 생성이나 사실 기반 QA처럼 정확성이 중요한 작업에서는 낮은 temperature와 보수적인 decoding이 유리합니다. 반대로 브레인스토밍, 광고 문구, 소설 초안처럼 다양한 아이디어가 필요한 작업에서는 top-p나 temperature를 조금 높여 더 다양한 출력을 만들 수 있습니다.

---

### 2. context window와 KV cache는 각각 무엇이며, 긴 대화나 긴 문서 처리에서 왜 문제가 될 수 있는가?

**정답**

**context window**는 LLM이 한 번에 읽고 참고할 수 있는 최대 token 범위입니다.

**KV cache**는 LLM이 다음 token을 빠르게 생성하기 위해 이전 token들의 key/value 계산 결과를 저장해 두는 임시 메모리입니다.

긴 대화나 긴 문서에서는 context window가 꽉 차서 앞부분 정보가 잘릴 수 있고, KV cache가 커져서 GPU memory 사용량과 비용, latency가 증가할 수 있습니다.

**설명**

LLM은 사람처럼 모든 대화를 영구적으로 기억하는 것이 아닙니다. 답을 만들 때 현재 입력으로 들어온 내용, 즉 context 안에 있는 token들을 보고 답합니다.

**context window**는 모델이 한 번에 볼 수 있는 작업 공간입니다. 예를 들어 context window가 8,000 tokens인 모델이라면, 시스템 지시문, 사용자 질문, 이전 대화, 첨부 문서, 그리고 모델이 앞으로 생성할 답변까지 이 범위 안에 들어가야 합니다.

만약 대화가 너무 길어지면 앞부분이 잘릴 수 있습니다. 사용자가 초반에 “내 이름은 민수야”라고 말했더라도, 그 내용이 현재 context에서 빠져 있다면 모델은 이름을 알기 어렵습니다.

**KV cache**는 추론 속도와 관련이 있습니다. Transformer 기반 LLM은 token을 하나씩 생성합니다. 매번 이전 모든 token을 처음부터 다시 계산하면 너무 느립니다. 그래서 이전 token들의 key와 value 정보를 저장해 둡니다. 이 저장 공간이 KV cache입니다.

문제는 context가 길수록 저장해야 할 token도 많아진다는 점입니다. token 수가 많고, 모델 layer가 많고, hidden size가 클수록 KV cache는 더 커집니다. 그래서 긴 문서를 넣거나 긴 대화를 유지하면 GPU memory를 많이 쓰고, 여러 사용자를 동시에 처리하기 어려워질 수 있습니다.

**예시**

책상 비유로 생각하면 쉽습니다.

context window는 책상 크기입니다. 책상 위에 종이를 10장만 올릴 수 있는데, 문서가 20장이라면 10장은 책상 밖으로 밀려납니다. 모델은 지금 책상 위에 있는 10장만 보고 답할 수 있습니다.

KV cache는 책상 위 종이마다 붙여 둔 빠른 참고용 메모지입니다. 종이가 많아질수록 메모지도 많아집니다. 그래서 다시 읽는 속도는 빨라질 수 있지만, 책상 공간과 정리 비용은 점점 커집니다.

작은 숫자로 보면, token이 4개일 때 attention 관계는 대략 4 × 4 = 16개처럼 생각할 수 있습니다. token이 1,000개라면 1,000 × 1,000 = 1,000,000개 규모의 관계를 다루는 느낌이 됩니다. 실제 구현은 최적화되어 있지만, 길이가 늘수록 계산과 메모리가 빠르게 커진다는 직관은 중요합니다.

**실전 연결**

긴 PDF 질문답변, 회사 내부 문서 검색, 장기 대화 챗봇, agent 시스템에서 context window 관리는 매우 중요합니다. 모든 문서를 prompt에 다 넣는 방식은 비용도 크고 성능도 불안정할 수 있습니다. 그래서 실무에서는 RAG, chunking, 요약 memory, external database를 사용합니다. 필요한 부분만 검색해서 context에 넣고, 오래된 대화는 요약해서 유지하는 방식이 많이 쓰입니다.

---

### 3. hallucination을 줄이기 위해 grounding이 필요한 이유는 무엇이고, calibration은 어떤 상황에서 중요해지는가?

**정답**

**hallucination**은 LLM이 사실이 아닌 내용을 그럴듯하게 만들어내는 현상입니다.

이를 줄이기 위해 **grounding**이 필요합니다. grounding은 답변을 문서, 검색 결과, 데이터베이스, tool output 같은 실제 근거에 연결하는 것입니다.

**calibration**은 모델의 confidence, 즉 자신감이 실제 정답률과 얼마나 잘 맞는지를 뜻합니다. 의료, 법률, 금융, 회사 정책 안내처럼 틀린 답이 큰 피해를 줄 수 있는 상황에서 특히 중요합니다.

**설명**

LLM은 기본적으로 “다음 token을 잘 예측하는 모델”입니다. 다시 말해, 문장 흐름상 자연스러운 다음 말을 잘 고르도록 학습되었습니다. 하지만 자연스러운 문장과 사실인 문장은 다를 수 있습니다.

예를 들어 모델이 “이 회사의 2025년 3분기 매출은 120억 원입니다”라고 자신 있게 말할 수 있습니다. 하지만 실제 회사 데이터나 보고서를 본 적이 없다면 이 답은 근거 없는 생성일 수 있습니다. 이것이 hallucination입니다.

**grounding**은 이런 문제를 줄이기 위한 방법입니다. 모델이 그냥 기억이나 추측으로 답하는 것이 아니라, 실제 문서나 검색 결과를 보고 답하게 만듭니다. 예를 들어 “2025_Q3_sales.pdf 3페이지 표에 따르면 매출은 118억 원입니다”처럼 답하면 사용자가 근거를 확인할 수 있습니다.

**calibration**은 모델이 얼마나 자신 있어 하는지와 실제로 얼마나 맞는지가 일치하는지를 봅니다. 모델이 “90% 확실합니다”라고 말한 답들이 실제로도 90% 정도 맞으면 calibration이 좋습니다. 하지만 90% 확실하다고 했는데 실제로는 50%만 맞으면 모델이 과신하고 있는 것입니다.

중요한 점은 말투가 자신감 있어도 답이 맞다는 뜻은 아니라는 것입니다. LLM은 틀린 말도 매우 자연스럽게 말할 수 있습니다. 그래서 근거를 붙이고, 모르는 것은 모른다고 말하고, 불확실성을 표현하는 능력이 중요합니다.

**예시**

사용자가 이렇게 묻습니다.

“우리 회사의 올해 1분기 영업이익은 얼마야?”

모델이 내부 문서에 접근하지 못하는데도 이렇게 말합니다.

“올해 1분기 영업이익은 35억 원입니다.”

이 답은 그럴듯하지만 근거가 없다면 hallucination일 수 있습니다.

grounding이 된 답은 이렇게 됩니다.

“제공된 `2026_Q1_report.pdf`의 5페이지 손익계산서에 따르면, 1분기 영업이익은 32억 원입니다. 다만 이 문서에는 2분기 수치는 포함되어 있지 않습니다.”

여기서는 출처가 있고, 문서에 없는 내용은 없다고 말합니다.

calibration 예시도 보겠습니다.

모델이 10개 질문에 대해 전부 “80% 확실합니다”라고 했습니다. 실제로 10개 중 8개를 맞혔다면 calibration이 좋습니다. 하지만 10개 중 3개만 맞혔다면 모델의 confidence는 실제보다 너무 높았던 것입니다.

**실전 연결**

RAG 기반 문서 QA에서는 grounding이 핵심입니다. 회사 정책 챗봇은 반드시 최신 정책 문서에 근거해서 답해야 하고, 없는 정책을 만들어내면 안 됩니다. 의료나 법률 AI에서는 hallucination이 실제 피해로 이어질 수 있으므로, citation, database lookup, tool use, uncertainty 표현이 중요합니다. 모델 평가에서도 단순 accuracy만 보는 것이 아니라 hallucination rate와 calibration을 함께 확인해야 더 안전한 시스템을 만들 수 있습니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-19-day27.md
