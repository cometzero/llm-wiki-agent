# AI/ML Learning Review - Day 26 (2026-05-18)

## Source Metadata
- Lesson file: `/home/ubuntu/work/ai/learning/logs/2026-05-18-day26.md`
- State file: `/home/ubuntu/work/ai/learning/state.json`
- Follow-up answer file: `/home/ubuntu/.hermes/cron/output/b2c07d928d85/2026-05-18_09-26-45.md`

---

## Lesson

# Day 26 - AI/ML 기초 학습

- Date: 2026-05-18
- Progress: 26/30
- Level: beginner-intermediate
- Milestone: LLM 구조와 학습 파이프라인
- Milestone goal: LLM이 어떻게 학습되고 추론되는지 현대적 관점으로 정리한다.

## Today's 3 concepts

1. 스케일링 법칙과 모델 크기
2. Instruction tuning과 SFT
3. RLHF와 preference optimization

---

## 1. 스케일링 법칙과 모델 크기

### 한 줄 직관

LLM은 보통 **모델을 더 크게 만들고, 데이터를 더 많이 보여 주고, 계산을 더 많이 쓰면 성능이 예측 가능한 방식으로 좋아지는 경향**이 있는데, 이 관계를 정리한 것이 scaling law입니다.

### 개념 정의

스케일링 법칙(scaling law)은 모델의 성능, 특히 language model의 loss가 **모델 크기(parameter count), 학습 데이터 양(data scaling), 계산량(compute budget)**에 따라 어떻게 변하는지 관찰하고 수식으로 정리한 경험 법칙입니다.

여기서 parameter count는 모델 안에 들어 있는 조절 가능한 숫자의 개수입니다. 예를 들어 아주 작은 신경망에 가중치(weight)가 6개, bias가 2개 있다면 parameter count는 8개입니다. 실제 LLM은 이 숫자가 수십억, 수천억 개까지 갑니다.

compute budget은 학습에 쓸 수 있는 계산 자원입니다. 쉽게 말하면 “GPU를 얼마나 오래, 얼마나 많이 돌릴 수 있는가”입니다. 같은 모델이라도 GPU 1장을 하루 쓰는 것과 GPU 1,000장을 몇 주 쓰는 것은 가능한 학습 규모가 완전히 다릅니다.

### 왜 이런 개념이 필요한가

LLM을 만들 때 가장 비싼 결정은 “얼마나 큰 모델을 만들 것인가?”입니다. 모델이 크면 더 많은 패턴을 저장하고 표현할 수 있지만, 학습 비용과 추론 비용이 커집니다. 반대로 너무 작은 모델은 비용은 낮지만 성능이 부족할 수 있습니다.

Scaling law는 이 결정을 감으로만 하지 않게 도와줍니다. 예를 들어 “모델을 2배 키우는 것이 나을까, 데이터를 2배 늘리는 것이 나을까?” 같은 질문에 방향을 줍니다. 현대 LLM 개발에서는 모델 크기, 데이터 양, 학습 토큰 수, GPU 예산을 함께 맞춰야 하므로 scaling law는 연구와 제품 개발 모두에서 중요합니다.

또한 scaling law는 “큰 모델이 왜 갑자기 좋아 보이는가?”를 이해하는 출발점이 됩니다. 모델이 커지면 단순히 암기량만 늘어나는 것이 아니라, 더 넓은 hidden state 공간에서 문맥의 미묘한 차이를 표현할 수 있습니다. attention layer도 더 많은 head와 차원을 사용해 단어 사이 관계를 더 다양하게 볼 수 있습니다.

### 아주 쉬운 예시

학생이 영어 단어를 배우는 상황을 생각해 봅시다.

- 학생 A는 작은 노트 1권만 가지고 있습니다.
- 학생 B는 큰 노트 10권을 가지고 있습니다.
- 두 학생 모두 예문을 100개만 봅니다.

큰 노트를 가진 학생 B가 더 많이 적을 수는 있지만, 예문이 100개뿐이면 배울 수 있는 패턴에 한계가 있습니다. 이번에는 예문을 10,000개로 늘리면 어떨까요? 큰 노트를 가진 학생 B는 다양한 표현을 많이 정리할 수 있어서 성능이 크게 좋아질 수 있습니다.

LLM도 비슷합니다.

아주 단순한 숫자 예시로 보면:

- 모델 A: parameter 1백만 개, 데이터 1억 token
- 모델 B: parameter 1천만 개, 데이터 1억 token
- 모델 C: parameter 1천만 개, 데이터 10억 token

B는 A보다 표현할 공간이 크기 때문에 더 복잡한 패턴을 배울 수 있습니다. 하지만 데이터가 그대로이면 큰 모델을 충분히 활용하지 못할 수 있습니다. C처럼 데이터도 함께 늘어야 큰 모델의 장점이 제대로 살아납니다.

### 개념 구조와 핵심 포인트

Scaling law를 볼 때는 보통 세 가지 축을 함께 봅니다.

1. **parameter count**  
   모델 안의 학습 가능한 숫자 개수입니다. Transformer에서는 embedding matrix, attention의 query/key/value projection, feed-forward layer의 weight 등이 모두 parameter입니다.

2. **data scaling**  
   학습에 사용한 token 수와 데이터 다양성입니다. LLM은 문장을 token 단위로 나누어 다음 token을 예측하면서 배웁니다. 데이터가 많고 다양할수록 모델은 더 많은 문맥 패턴을 봅니다.

3. **compute budget**  
   모델 크기와 데이터 양을 실제로 학습시키는 데 필요한 계산량입니다. 너무 큰 모델을 너무 적은 compute로 학습하면 충분히 수렴하지 못합니다.

핵심은 “무조건 크게”가 아니라 **균형 있게 크게**입니다. 모델만 키우고 데이터가 부족하면 overfitting이나 비효율이 생길 수 있습니다. 데이터만 늘리고 모델이 너무 작으면 그 패턴을 담을 표현력이 부족할 수 있습니다. compute가 부족하면 loss가 충분히 내려가지 않습니다.

### 핵심 수학 포인트

Scaling law에서 자주 보는 대상은 loss입니다. Language model의 loss는 보통 cross-entropy loss로 측정합니다. 직관적으로는 “모델이 다음 token을 얼마나 놀라워했는가”입니다.

아주 작은 예시를 보겠습니다.

문장: “나는 밥을 ___”  
정답 token: “먹었다”

모델이 다음 token 확률을 이렇게 냈다고 합시다.

- 먹었다: 0.50
- 마셨다: 0.20
- 잤다: 0.05
- 기타: 0.25

정답인 “먹었다”에 0.50을 주었으니 나쁘지 않습니다. 만약 더 큰 모델이 더 많은 데이터를 보고 학습해서 “먹었다”에 0.80을 준다면 loss는 더 낮아집니다. Scaling law는 모델 크기, 데이터 양, compute가 커질수록 이런 평균 loss가 어떤 속도로 줄어드는지 봅니다.

수식 형태는 논문마다 다르지만, 초보자에게 중요한 직관은 이것입니다.

- 성능 향상은 대체로 점점 느려집니다.
- parameter, data, compute 중 하나만 늘리면 한계가 옵니다.
- 좋은 학습 계획은 같은 compute budget 안에서 loss를 가장 많이 낮추는 조합을 찾는 것입니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **scaling law**: 모델 크기, 데이터 양, 계산량이 성능과 어떤 관계를 가지는지 설명하는 경험 법칙입니다.
- **parameter count**: 모델 안의 학습 가능한 숫자 개수입니다.
- **compute budget**: 학습에 쓸 수 있는 GPU 시간, 연산량, 비용의 총량입니다.
- **data scaling**: 학습 데이터의 양과 다양성을 늘리는 것입니다.
- **loss**: 모델 예측이 정답과 얼마나 다른지 나타내는 값입니다. 낮을수록 좋습니다.
- **token**: LLM이 문장을 처리하는 기본 조각입니다. 한 글자, 단어 일부, 단어 전체가 될 수 있습니다.

### AI에서 어디에 쓰이는가

Scaling law는 LLM 개발의 예산 계획에 직접 쓰입니다. GPT 계열, LLaMA 계열, Claude 계열 같은 대형 모델은 모두 모델 크기, 데이터 양, compute budget 사이의 균형을 고민합니다.

실무에서도 중요합니다. 예를 들어 회사가 자체 LLM을 만들려 할 때 “7B 모델을 오래 학습할지, 13B 모델을 짧게 학습할지, 아니면 기존 모델을 fine-tuning할지”를 결정해야 합니다. 이때 scaling law 관점이 있으면 단순히 “큰 모델이 좋다”가 아니라 비용 대비 성능을 비교할 수 있습니다.

또한 inference 비용과도 연결됩니다. parameter count가 큰 모델은 추론할 때 더 많은 메모리와 계산이 필요합니다. 제품에서는 응답 속도, 서버 비용, 사용자 수를 고려해야 하므로 무조건 가장 큰 모델을 쓰지 않습니다.

### 헷갈리기 쉬운 포인트

첫째, scaling law는 절대 법칙이 아니라 경험 법칙입니다. 데이터 품질, 모델 구조, 학습 방법이 바뀌면 결과도 달라질 수 있습니다.

둘째, 큰 모델이 항상 작은 모델보다 모든 상황에서 좋은 것은 아닙니다. 작은 task, 제한된 환경, 모바일 기기에서는 작은 모델이 더 실용적일 수 있습니다.

셋째, parameter count가 크다고 지식이 자동으로 “정확”해지는 것은 아닙니다. LLM은 다음 token 예측을 통해 패턴을 배운 모델입니다. 잘못된 데이터나 오래된 데이터가 많으면 큰 모델도 hallucination을 할 수 있습니다.

---

## 2. Instruction tuning과 SFT

### 한 줄 직관

Pretraining이 “언어를 넓게 읽고 배우는 단계”라면, instruction tuning과 SFT는 모델에게 **사람의 지시를 어떻게 따라야 하는지 예시로 가르치는 단계**입니다.

### 개념 정의

Instruction tuning은 LLM이 질문, 요청, 명령 같은 instruction을 보고 적절한 답변을 하도록 학습시키는 과정입니다. Supervised fine-tuning(SFT)은 정답 예시가 붙어 있는 데이터로 모델을 추가 학습시키는 방법입니다.

두 용어는 자주 함께 쓰입니다. 보통 instruction tuning을 실제로 구현할 때 “instruction과 좋은 answer 쌍”을 만들고, 그 answer를 따라 하도록 supervised fine-tuning을 합니다. 그래서 “Instruction tuning을 SFT로 한다”라고 말할 수 있습니다.

예를 들어 데이터 하나는 이렇게 생겼습니다.

- instruction: “이 문장을 더 공손하게 바꿔줘: 빨리 보내.”
- answer: “가능하시다면 빠르게 보내 주시면 감사하겠습니다.”

모델은 이 쌍을 보고, 지시가 들어오면 어떤 스타일과 형식으로 답해야 하는지 배웁니다.

### 왜 이런 개념이 필요한가

기본 pretraining만 한 language model은 다음 token을 잘 예측할 수 있지만, 사용자의 의도를 친절하게 따르는 assistant가 되지는 않습니다. 예를 들어 사용자가 “파이썬 리스트 정렬 방법을 알려줘”라고 했을 때, pretrained model은 관련 글처럼 이어 쓸 수는 있지만, 반드시 단계별 답변을 해 주거나 코드 예시를 깔끔하게 제시한다고 보장하기 어렵습니다.

Instruction tuning은 모델의 행동 양식을 바꿉니다. 단순히 문장을 이어 쓰는 모델에서, 요청을 이해하고 답변 형식을 맞추는 모델로 바뀌게 합니다.

이 과정은 hidden state와도 연결됩니다. 모델은 instruction token들을 attention으로 읽고, “이 요청은 번역이다”, “이 요청은 요약이다”, “이 요청은 코드 작성이다” 같은 패턴을 내부 표현(hidden states)에 담습니다. SFT는 이런 내부 표현이 좋은 답변 token으로 이어지도록 gradient를 통해 parameter를 조정합니다.

### 아주 쉬운 예시

요리 초보에게 “계란 요리해 봐”라고만 하면 결과가 들쭉날쭉할 수 있습니다. 하지만 좋은 예시를 여러 개 보여 주면 달라집니다.

예시 1:

- 요청: “계란 프라이 만드는 법 알려줘.”
- 좋은 답변: “1. 팬을 달굽니다. 2. 기름을 두릅니다. 3. 계란을 깨 넣습니다. 4. 원하는 익힘 정도까지 익힙니다.”

예시 2:

- 요청: “계란 삶는 법을 짧게 설명해줘.”
- 좋은 답변: “물에 계란을 넣고 끓인 뒤, 반숙은 약 7분, 완숙은 약 10분 삶으면 됩니다.”

이런 예시를 많이 보면 초보는 “아, 요청이 길면 단계별로, 짧게 하라면 짧게 답해야 하는구나”를 배웁니다. LLM의 instruction tuning도 비슷합니다.

아주 작은 숫자 예시로 보면, SFT 데이터가 3개만 있다고 해 봅시다.

1. 번역 요청 → 번역 답변
2. 요약 요청 → 요약 답변
3. 코드 요청 → 코드 답변

처음에는 모델이 “요약해줘”라는 요청 뒤에 엉뚱한 긴 글을 만들 수 있습니다. SFT 후에는 “요약해줘” 뒤에 짧고 핵심적인 답변이 나올 확률이 올라갑니다.

### 개념 구조와 핵심 포인트

Instruction tuning 데이터는 보통 다음 구조를 가집니다.

1. **instruction**  
   사용자가 원하는 작업입니다. 예: “다음 글을 세 줄로 요약해줘.”

2. **input 또는 context**  
   작업에 필요한 자료입니다. 예: 요약할 긴 글, 번역할 문장, 코드 오류 메시지.

3. **response 또는 answer**  
   모델이 따라 배워야 할 좋은 답변입니다.

SFT에서는 이 response token들이 정답 역할을 합니다. 모델은 앞의 instruction과 context를 보고 다음 answer token을 맞히도록 학습합니다.

핵심 포인트는 세 가지입니다.

- 데이터 품질이 매우 중요합니다. 나쁜 답변을 정답으로 주면 모델도 나쁜 스타일을 배웁니다.
- 다양한 instruction이 필요합니다. 요약만 배운 모델은 코딩, 추론, 대화 스타일을 잘 못 배울 수 있습니다.
- SFT는 모델에게 “무엇을 아는가”보다 “어떻게 답할 것인가”를 강하게 가르칩니다.

### 핵심 수학 포인트

SFT도 기본적으로 next-token prediction loss를 사용합니다. 다만 pretraining과 다른 점은 아무 웹문장이나 이어 쓰는 것이 아니라, instruction에 대한 좋은 response를 이어 쓰도록 학습한다는 점입니다.

작은 예시를 봅시다.

입력:

“질문: 2+3은? 답:”

정답 response token:

“5”

모델이 다음 token 확률을 이렇게 냈다고 합시다.

- “5”: 0.40
- “6”: 0.20
- “23”: 0.10
- 기타: 0.30

정답 “5”의 확률이 0.40이면 loss가 생깁니다. optimizer는 gradient를 이용해 parameter를 조금 바꾸고, 다음에는 “5”의 확률을 더 높이도록 합니다. 이 과정을 수많은 instruction-answer 쌍에 대해 반복합니다.

Tensor shape 관점으로 아주 단순화하면, 모델은 token id들의 배열을 입력으로 받습니다.

- input shape 예: `[batch_size, sequence_length]`
- 예: 한 번에 2개 예시를 넣고, 각 예시 길이가 8 token이면 `[2, 8]`

모델은 각 위치마다 vocabulary 전체에 대한 점수(logits)를 냅니다.

- logits shape 예: `[batch_size, sequence_length, vocab_size]`

SFT loss는 answer 부분의 token들이 정답과 맞는지 계산합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **instruction tuning**: 모델이 사람의 지시를 잘 따르도록 instruction-response 예시로 학습시키는 과정입니다.
- **supervised fine-tuning**: 정답 label 또는 정답 answer가 있는 데이터로 추가 학습하는 방법입니다.
- **instruction-following**: 사용자의 요청 의도, 형식, 제약을 따라 답하는 능력입니다.
- **prompt**: 모델에게 주는 입력 문장입니다.
- **response**: 모델이 생성해야 하는 답변입니다.
- **fine-tuning**: 이미 학습된 모델을 특정 목적에 맞게 조금 더 학습시키는 과정입니다.

### AI에서 어디에 쓰이는가

Instruction tuning과 SFT는 챗봇, 코딩 assistant, 검색 요약 모델, 고객지원 bot, 교육용 tutor 등에 거의 필수로 쓰입니다. 사용자가 “표로 정리해줘”, “초등학생도 이해하게 설명해줘”, “이 코드의 버그를 찾아줘”라고 했을 때, 모델은 단순히 다음 단어를 예측하는 것 이상으로 요청의 형식을 따라야 합니다.

실제 LLM pipeline에서는 보통 다음 흐름이 있습니다.

1. 대규모 텍스트로 pretraining
2. instruction 데이터로 SFT
3. 필요하면 preference data로 RLHF 또는 preference optimization

SFT는 이 중에서 “assistant처럼 말하는 능력”을 만드는 첫 번째 큰 단계입니다.

### 헷갈리기 쉬운 포인트

첫째, SFT가 새로운 지식을 무한히 추가하는 만능 방법은 아닙니다. SFT는 행동과 형식을 크게 바꾸지만, 아주 많은 새 지식을 넣으려면 데이터 설계가 중요하고 때로는 retrieval이나 continued pretraining이 더 적합합니다.

둘째, instruction tuning 데이터가 많기만 하면 좋은 것이 아닙니다. 같은 형식의 낮은 품질 답변이 많으면 모델은 그 나쁜 습관을 배웁니다.

셋째, SFT만으로 사람의 선호를 완벽히 맞추기는 어렵습니다. 답변이 정답처럼 보이더라도 너무 장황하거나, 무례하거나, 위험할 수 있습니다. 그래서 다음 단계로 RLHF나 preference optimization이 사용됩니다.

---

## 3. RLHF와 preference optimization

### 한 줄 직관

SFT가 “좋은 답변 예시를 따라 하게 만드는 학습”이라면, RLHF와 preference optimization은 **여러 답변 중 사람이 더 좋아하는 답변을 더 자주 만들도록 조정하는 학습**입니다.

### 개념 정의

RLHF(Reinforcement Learning from Human Feedback)는 사람의 피드백을 이용해 모델의 답변 정책(policy)을 개선하는 방법입니다. 보통 사람에게 여러 답변을 보여 주고 어느 쪽이 더 좋은지 고르게 한 뒤, 그 preference data로 reward model을 학습합니다. 이후 policy optimization을 통해 LLM이 더 높은 reward를 받는 답변을 만들도록 조정합니다.

Preference optimization은 더 넓은 표현입니다. 사람이 선호한 답변과 덜 선호한 답변의 차이를 이용해 모델을 개선하는 여러 방법을 포함합니다. 요즘은 PPO 기반 RLHF뿐 아니라 DPO(Direct Preference Optimization)처럼 reward model을 별도로 두지 않는 방법도 많이 이야기합니다.

### 왜 이런 개념이 필요한가

SFT는 “정답 예시 하나”를 따라 하도록 학습합니다. 하지만 실제 대화에서는 좋은 답변이 하나만 있는 경우가 드뭅니다.

예를 들어 사용자가 “gradient descent를 설명해줘”라고 했을 때 가능한 답변은 많습니다.

- 답변 A: 짧고 정확하지만 너무 딱딱함
- 답변 B: 비유와 예시가 있어 초보자에게 쉬움
- 답변 C: 수식은 맞지만 너무 어려움
- 답변 D: 그럴듯하지만 일부 틀림

사람은 보통 B를 더 좋아할 수 있습니다. RLHF와 preference optimization은 이런 “사람이 실제로 선호하는 답변의 특징”을 모델에 반영합니다.

LLM은 token을 하나씩 선택하는 policy처럼 볼 수 있습니다. 같은 prompt에서 다음 token 후보가 여러 개 있을 때, 어떤 token을 더 높은 확률로 선택할지 정하는 것이 policy입니다. Preference optimization은 이 policy가 더 도움이 되고, 안전하고, 사용자의 의도에 맞는 방향으로 움직이게 합니다.

### 아주 쉬운 예시

친구에게 카페 추천 답변을 두 개 만들었다고 해 봅시다.

질문: “근처에서 조용한 카페 추천해줘.”

답변 A: “카페 가세요.”

답변 B: “조용한 곳을 원하면 큰길가보다 골목 안 카페를 먼저 찾아보세요. 리뷰에서 ‘공부하기 좋다’, ‘좌석 간격이 넓다’ 같은 표현이 있는 곳을 고르면 실패 확률이 낮습니다.”

대부분의 사람은 B를 더 좋아할 것입니다. 왜냐하면 구체적이고, 조건을 반영하고, 실제 행동에 도움이 되기 때문입니다.

Preference data는 이런 형태입니다.

- prompt: “근처에서 조용한 카페 추천해줘.”
- chosen: 답변 B
- rejected: 답변 A

아주 작은 숫자 예시를 보겠습니다.

Reward model이 답변에 점수를 준다고 합시다.

- 답변 A reward: 0.2
- 답변 B reward: 0.9

Policy optimization은 앞으로 비슷한 prompt가 들어왔을 때 A 같은 답변의 확률은 낮추고, B 같은 답변의 확률은 높이는 방향으로 모델을 조정합니다.

### 개념 구조와 핵심 포인트

전형적인 RLHF 흐름은 다음과 같습니다.

1. **SFT model 준비**  
   먼저 instruction-following이 어느 정도 되는 모델을 만듭니다.

2. **preference data 수집**  
   같은 prompt에 대해 여러 답변을 만들고, 사람이 더 좋은 답변을 고릅니다.

3. **reward model 학습**  
   prompt와 답변을 입력하면 “사람이 좋아할 점수”를 예측하는 모델을 학습합니다.

4. **policy optimization**  
   LLM이 reward model에서 높은 점수를 받는 답변을 더 자주 만들도록 학습합니다.

핵심 포인트는 “정답 하나를 외우는 것”이 아니라 “선호의 방향을 배우는 것”입니다. 사람은 정확성, 친절함, 간결함, 안전성, 형식 준수 등을 종합해서 선호를 판단합니다. RLHF는 이 복합적인 기준을 모델 행동에 넣으려는 시도입니다.

### 핵심 수학 포인트

가장 단순하게 보면 preference data는 비교 데이터입니다.

같은 prompt x에 대해:

- chosen answer: y_good
- rejected answer: y_bad

목표는 모델이 y_good을 y_bad보다 더 선호하도록 만드는 것입니다.

Reward model 방식에서는 다음처럼 생각할 수 있습니다.

- reward_model(x, y_good) = 2.0
- reward_model(x, y_bad) = 0.5

그러면 policy optimization은 모델이 y_good 스타일의 답변을 만들 확률을 높이려 합니다.

다만 한 가지 주의가 필요합니다. Reward만 무작정 높이면 모델이 reward model의 허점을 이용할 수 있습니다. 예를 들어 reward model이 “긴 답변”을 좋게 평가하는 경향이 있으면, 모델이 필요 이상으로 장황해질 수 있습니다. 그래서 실제 RLHF에서는 기존 SFT model에서 너무 멀어지지 않도록 KL penalty 같은 제약을 둡니다. 초보자 관점에서는 “보상을 높이되, 원래의 자연스러운 언어 능력을 망가뜨리지 않게 잡아주는 안전벨트”라고 이해하면 됩니다.

DPO 같은 preference optimization 방법은 이 과정을 더 직접적으로 만듭니다. 별도의 reward model을 훈련하고 RL을 돌리는 대신, chosen 답변의 확률은 높이고 rejected 답변의 확률은 낮추도록 loss를 설계합니다.

### 배워야 할 용어 (영문 term 중심, 필요 시 한국어 설명 보조)

- **RLHF**: Reinforcement Learning from Human Feedback. 사람 피드백을 이용해 모델 행동을 개선하는 방법입니다.
- **reward model**: 답변이 사람에게 얼마나 좋게 평가될지 점수로 예측하는 모델입니다.
- **preference data**: 같은 prompt에 대한 여러 답변 중 어떤 답변이 더 좋은지 비교한 데이터입니다.
- **policy optimization**: 모델의 답변 선택 방식(policy)을 더 좋은 보상을 받는 방향으로 조정하는 과정입니다.
- **chosen / rejected**: preference data에서 더 선호된 답변과 덜 선호된 답변입니다.
- **DPO**: Direct Preference Optimization. preference data를 이용해 chosen 답변 확률은 높이고 rejected 답변 확률은 낮추는 방식의 대표적인 방법입니다.

### AI에서 어디에 쓰이는가

RLHF와 preference optimization은 현대 assistant형 LLM의 사용자 경험을 크게 바꿉니다. 같은 지식을 가진 모델이라도, 답변이 친절한지, 사용자의 조건을 잘 지키는지, 위험한 요청을 안전하게 다루는지, 불필요하게 공격적이지 않은지는 별도의 alignment 학습이 필요합니다.

챗봇 제품에서는 특히 중요합니다. 사용자는 단순히 “문법적으로 이어지는 글”을 원하는 것이 아니라 “내 요청을 이해하고, 도움이 되고, 안전하며, 읽기 쉬운 답변”을 원합니다. Preference optimization은 이런 품질 기준을 모델에 반영합니다.

또한 코드 생성 모델에서도 중요합니다. 두 코드 답변이 모두 실행될 수 있어도, 하나는 설명이 좋고 edge case를 다루며, 다른 하나는 위험한 하드코딩을 할 수 있습니다. 사람이나 자동 평가가 더 나은 답변을 고르면, 모델은 그 선호를 배웁니다.

### 헷갈리기 쉬운 포인트

첫째, RLHF는 모델에게 완전히 새로운 사실을 주입하는 과정이라기보다, 답변 행동을 사람 선호에 맞추는 과정에 가깝습니다.

둘째, reward model이 항상 완벽한 사람 판단은 아닙니다. 사람이 만든 preference data도 편향될 수 있고, reward model도 그 편향을 배울 수 있습니다.

셋째, preference optimization은 “무조건 사용자가 원하는 대로 다 해 주는 것”이 아닙니다. 안전성, 정직성, 정책 준수도 선호 기준에 포함될 수 있습니다.

넷째, SFT와 RLHF는 경쟁 관계가 아니라 보통 순서대로 이어지는 관계입니다. 먼저 SFT로 기본 assistant 행동을 만들고, 그다음 preference optimization으로 더 선호되는 행동을 강화합니다.

---

## 복습 질문 3개

1. Scaling law에서 parameter count, data scaling, compute budget을 함께 봐야 하는 이유는 무엇인가요?
2. Instruction tuning과 SFT는 pretrained language model의 어떤 행동을 바꾸는 데 도움이 되나요?
3. RLHF에서 preference data와 reward model은 각각 어떤 역할을 하나요?

## 오늘의 한 줄 요약

현대 LLM은 scaling law로 크기와 학습 예산을 설계하고, SFT로 instruction-following을 배우며, RLHF와 preference optimization으로 사람이 더 선호하는 assistant 행동에 가까워집니다.

---

## Follow-up Review Answers

# Cron Job: AI ML 복습질문 정답

**Job ID:** b2c07d928d85
**Run Time:** 2026-05-18 09:26:45
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
  "date": "2026-05-18",
  "day_number": 26,
  "total_days": 30,
  "concepts_per_day": 3,
  "milestone_names": [
    "LLM 구조와 학습 파이프라인"
  ],
  "milestone_goals": [
    "LLM이 어떻게 학습되고 추론되는지 현대적 관점으로 정리한다."
  ],
  "concepts": [
    "스케일링 법칙과 모델 크기",
    "Instruction tuning과 SFT",
    "RLHF와 preference optimization"
  ],
  "concept_term_map": [
    {
      "concept": "스케일링 법칙과 모델 크기",
      "terms": [
        "scaling law",
        "parameter count",
        "compute budget",
        "data scaling"
      ]
    },
    {
      "concept": "Instruction tuning과 SFT",
      "terms": [
        "instruction tuning",
        "supervised fine-tuning",
        "instruction-following"
      ]
    },
    {
      "concept": "RLHF와 preference optimization",
      "terms": [
        "RLHF",
        "reward model",
        "preference data",
        "policy optimization"
      ]
    }
  ],
  "target_markdown_path": "/home/ubuntu/work/ai/learning/logs/2026-05-18-day26.md",
  "state_path": "/home/ubuntu/work/ai/learning/state.json",
  "already_completed_today": true,
  "last_completed_date": "2026-05-18",
  "last_completed_file": "/home/ubuntu/work/ai/learning/logs/2026-05-18-day26.md",
  "next_day_after_completion": 27,
  "commit_message": "docs: add AI/ML lesson for day 26 (2026-05-18)"
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

[AI/ML 오늘의 복습 정답 Day 26/30]

오늘은 LLM 학습 파이프라인에서 중요한 세 가지 질문을 차근차근 복습해 볼게요.

### 1. Scaling law에서 parameter count, data scaling, compute budget을 함께 봐야 하는 이유는 무엇인가요?

**정답**

Scaling law에서는 **모델 크기(parameter count), 데이터 양(data scaling), 계산 예산(compute budget)**을 함께 봐야 합니다.

이유는 세 가지가 서로 따로 움직이지 않기 때문입니다.

- 모델만 크게 만들고 데이터가 적으면, 큰 모델을 충분히 활용하지 못합니다.
- 데이터만 많이 늘리고 모델이 너무 작으면, 많은 패턴을 담을 공간이 부족합니다.
- 모델과 데이터가 충분해도 compute budget이 부족하면, 학습을 끝까지 제대로 시키기 어렵습니다.

즉, 좋은 LLM 학습은 “무조건 크게”가 아니라 **모델 크기, 데이터 양, 계산량을 균형 있게 맞추는 일**입니다.

**설명**

Parameter count는 모델 안에 있는 학습 가능한 숫자의 개수입니다. 쉽게 말해 모델이 패턴을 저장하고 표현할 수 있는 “공간”에 가깝습니다. Parameter가 많으면 더 복잡한 문맥과 표현을 배울 가능성이 커집니다.

Data scaling은 학습에 사용하는 token 수와 데이터 다양성을 늘리는 것입니다. LLM은 많은 문장을 보면서 “이 문맥 다음에는 어떤 token이 올 가능성이 높은가?”를 배웁니다. 그래서 데이터가 적으면 아무리 큰 모델이라도 세상의 다양한 표현을 충분히 배우기 어렵습니다.

Compute budget은 GPU 시간, 연산량, 비용 같은 학습 자원입니다. 큰 모델과 많은 데이터를 준비해도 계산 자원이 부족하면 학습을 충분히 반복하지 못하고, loss function, 즉 예측이 정답과 얼마나 다른지를 나타내는 값이 충분히 내려가지 않을 수 있습니다.

Scaling law의 핵심은 이 세 요소가 성능과 비용을 함께 결정한다는 점입니다. 모델이 커질수록 보통 성능은 좋아질 수 있지만, 그만큼 더 많은 데이터와 계산량이 필요합니다. 그래서 LLM 개발에서는 “7B 모델을 오래 학습할까?”, “13B 모델을 짧게 학습할까?”, “데이터를 더 모을까?” 같은 결정을 scaling law 관점에서 합니다.

**예시**

학생이 영어 공부를 한다고 생각해 봅시다.

- parameter count: 학생의 노트 크기
- data scaling: 학생이 보는 예문 수
- compute budget: 공부할 수 있는 시간

큰 노트 10권이 있어도 예문을 10개만 보면 많이 배울 수 없습니다. 반대로 예문이 10,000개 있어도 노트가 너무 작으면 중요한 패턴을 다 정리하기 어렵습니다. 또 노트와 예문이 충분해도 공부 시간이 10분뿐이면 제대로 익히기 어렵습니다.

LLM도 비슷합니다.  
모델이 크고, 데이터가 충분하고, 학습 계산량도 충분해야 좋은 성능이 나올 가능성이 커집니다.

**실전 연결**

실제 LLM을 만들거나 fine-tuning할 때 이 관점은 예산 계획에 바로 연결됩니다. 회사나 연구팀은 GPU 비용이 제한되어 있기 때문에 가장 큰 모델을 무조건 선택할 수 없습니다. 같은 compute budget 안에서 모델 크기, 학습 token 수, 데이터 품질을 어떻게 배분해야 loss를 가장 잘 낮출 수 있는지 판단해야 합니다. 그래서 scaling law는 GPT, LLaMA 같은 대형 모델뿐 아니라 작은 사내 모델을 만들 때도 중요한 기준이 됩니다.

### 2. Instruction tuning과 SFT는 pretrained language model의 어떤 행동을 바꾸는 데 도움이 되나요?

**정답**

Instruction tuning과 SFT는 pretrained language model이 단순히 문장을 이어 쓰는 행동에서 벗어나, **사용자의 지시를 이해하고 그 지시에 맞는 답변을 하도록** 바꾸는 데 도움이 됩니다.

즉, 모델이 다음과 같은 행동을 더 잘 하게 만듭니다.

- 질문에 직접 답하기
- 요청한 형식 지키기
- 요약, 번역, 설명, 코드 작성 같은 작업 구분하기
- 친절하고 assistant다운 답변 만들기
- instruction-following, 즉 사용자의 지시를 따르는 능력 높이기

**설명**

Pretraining만 한 language model은 많은 텍스트를 읽고 다음 token을 예측하는 능력을 배운 모델입니다. 그래서 언어 패턴은 잘 알지만, 반드시 “사용자에게 도움이 되는 답변”을 하도록 훈련된 것은 아닙니다.

예를 들어 사용자가 “이 문장을 세 줄로 요약해줘”라고 했을 때, pretrained model은 관련된 글을 자연스럽게 이어 쓸 수는 있습니다. 하지만 정말로 세 줄로 요약할지, 핵심만 뽑을지, 사용자 요청을 깔끔하게 따를지는 보장되지 않습니다.

Instruction tuning은 모델에게 instruction-response 예시를 많이 보여 주는 과정입니다. 여기서 instruction은 “무엇을 해 달라”는 요청이고, response는 그 요청에 대한 좋은 답변입니다.

SFT, 즉 supervised fine-tuning은 정답 answer가 붙어 있는 데이터로 모델을 추가 학습시키는 방법입니다. LLM에서는 보통 instruction과 좋은 answer 쌍을 이용해서 SFT를 합니다.

작동 방식은 기본적으로 next-token prediction입니다. 예를 들어 입력이 “질문: 2+3은? 답:”이라면, 정답 token “5”가 나오도록 모델의 parameter를 조정합니다. 이때 gradient는 loss를 줄이는 방향으로 모델 내부 숫자를 조금씩 바꾸는 신호입니다.

결국 SFT는 모델에게 “이런 요청이 오면 이런 식으로 답해야 한다”는 행동 패턴을 가르칩니다.

**예시**

아주 작은 예를 들어 보겠습니다.

SFT 데이터가 다음처럼 3개 있다고 해 봅시다.

1. “이 문장을 영어로 번역해줘.” → 영어 번역 답변
2. “이 글을 한 문장으로 요약해줘.” → 짧은 요약 답변
3. “이 파이썬 오류를 설명해줘.” → 오류 원인과 해결책 답변

처음 모델은 “요약해줘”라는 요청에도 긴 글을 계속 이어 쓸 수 있습니다. 하지만 이런 예시를 많이 보고 학습하면, “요약”이라는 instruction이 들어왔을 때 짧고 핵심적인 답변을 만들 확률이 높아집니다.

일상 비유로 보면, 글을 잘 읽는 사람에게 “상담원처럼 답하는 법”, “선생님처럼 설명하는 법”, “요청한 형식을 지키는 법”을 예시로 훈련시키는 것과 비슷합니다.

**실전 연결**

Instruction tuning과 SFT는 챗봇, 코딩 assistant, 고객지원 bot, 학습 도우미 LLM을 만들 때 거의 필수적인 단계입니다. Pretraining이 언어 지식을 넓게 배우는 단계라면, SFT는 그 모델을 실제 제품에서 쓸 수 있는 assistant로 바꾸는 단계입니다. 사용자가 “표로 정리해줘”, “초보자도 이해하게 설명해줘”, “코드만 보여줘”라고 했을 때 이런 형식과 의도를 따르는 능력이 바로 instruction tuning과 SFT에서 강화됩니다.

### 3. RLHF에서 preference data와 reward model은 각각 어떤 역할을 하나요?

**정답**

RLHF에서 **preference data**는 사람이 여러 답변 중 어떤 답변을 더 좋아하는지 비교한 데이터입니다.

**Reward model**은 그 preference data를 바탕으로, 어떤 답변이 사람에게 더 좋게 평가될지를 점수로 예측하는 모델입니다.

정리하면 다음과 같습니다.

- preference data: “A 답변보다 B 답변이 더 좋다”는 사람의 선택 기록
- reward model: 답변을 보고 “이 답변은 사람이 좋아할 가능성이 높다/낮다”를 점수화하는 모델
- policy optimization: LLM이 reward model에서 높은 점수를 받는 답변을 더 자주 만들도록 조정하는 과정

**설명**

SFT는 좋은 답변 예시 하나를 정답처럼 따라 하게 만듭니다. 하지만 실제 대화에서는 좋은 답변이 하나만 있는 경우가 많지 않습니다.

예를 들어 “gradient descent를 설명해줘”라는 질문에 답변이 여러 개 있을 수 있습니다.

- 답변 A: 짧지만 너무 딱딱함
- 답변 B: 쉬운 비유와 예시가 있음
- 답변 C: 수식은 맞지만 초보자에게 너무 어려움
- 답변 D: 그럴듯하지만 일부 틀림

사람은 보통 정확하면서도 이해하기 쉬운 답변을 더 선호합니다. RLHF는 이런 사람의 선호를 모델에 반영하려는 방법입니다.

Preference data는 보통 같은 prompt에 대해 여러 답변을 만들고, 사람이 더 나은 답변을 고르는 방식으로 만들어집니다.

예를 들어:

- prompt: “근처에서 조용한 카페 추천해줘.”
- chosen: “리뷰에서 ‘공부하기 좋다’, ‘조용하다’ 같은 표현이 있는 골목 카페를 찾아보세요.”
- rejected: “카페 가세요.”

여기서 chosen은 사람이 더 선호한 답변이고, rejected는 덜 선호한 답변입니다.

Reward model은 이런 비교 데이터를 학습해서 답변에 점수를 줍니다. 예를 들어 좋은 답변에는 0.9, 부족한 답변에는 0.2처럼 점수를 줄 수 있습니다. 이후 policy optimization은 LLM이 높은 reward를 받을 만한 답변을 더 자주 생성하도록 조정합니다.

다만 reward만 무작정 높이면 문제가 생길 수 있습니다. 예를 들어 reward model이 긴 답변을 좋아한다고 잘못 배우면, 모델이 필요 이상으로 장황하게 답할 수 있습니다. 그래서 실제 RLHF에서는 기존 SFT model에서 너무 멀어지지 않도록 KL penalty 같은 제약을 두기도 합니다. 이것은 “보상은 높이되, 원래의 자연스러운 언어 능력은 망가뜨리지 않게 하는 안전벨트”라고 이해하면 됩니다.

**예시**

아주 작은 숫자 예시를 보겠습니다.

질문: “초보자에게 loss function을 설명해줘.”

모델이 두 답변을 만들었습니다.

- 답변 A: “Loss는 objective입니다.”
- 답변 B: “Loss function은 모델의 예측이 정답과 얼마나 다른지 숫자로 나타내는 기준입니다. 낮을수록 모델이 더 잘 맞힌 것입니다.”

사람은 B를 더 좋아할 가능성이 큽니다. 이유는 더 친절하고, 용어를 풀어서 설명하고, 초보자에게 도움이 되기 때문입니다.

이 데이터는 이렇게 저장될 수 있습니다.

- chosen: 답변 B
- rejected: 답변 A

Reward model은 이 패턴을 배워서 앞으로 B처럼 친절하고 구체적인 답변에 더 높은 점수를 주도록 학습됩니다. 그런 다음 LLM은 비슷한 상황에서 B 같은 답변을 만들 확률을 높이도록 조정됩니다.

**실전 연결**

RLHF와 preference optimization은 현대 assistant형 LLM의 품질을 크게 좌우합니다. 같은 지식을 가진 모델이라도 어떤 모델은 무례하거나 장황하고, 어떤 모델은 친절하고 안전하며 요청 형식을 잘 지킵니다. 이 차이는 단순 pretraining만으로 해결되기 어렵고, 사람의 선호를 반영하는 alignment 학습이 필요합니다. 실제 챗봇, 코드 생성 모델, 고객지원 AI에서는 정확성뿐 아니라 친절함, 안전성, 간결함, 형식 준수까지 중요하기 때문에 preference data와 reward model이 매우 중요한 역할을 합니다.

기준 파일: /home/ubuntu/work/ai/learning/logs/2026-05-18-day26.md
