---
title: "Are Open Models Catching Up?"
origin: lilys_ai
lilys_project_id: 11059017
lilys_project_url: "https://lilys.ai/digest/11059017"
lilys_created_at: "2026-08-22T09:23:27.962Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13019725"
sources:
  - id: "11913477"
    url: "https://newsletter.semianalysis.com/p/are-open-models-catching-up"
    title: "Are Open Models Catching Up?"
    status: "done"
---

# Are Open Models Catching Up?

## LilysAI note

> 오픈 모델은 클로즈드 모델을 따라잡고 있는가? **오픈소스 모델이 클로즈드 모델의 성능을 따라잡는 데 걸리는 시간이 매 세대마다 절반으로 줄어들고 있습니다.** 이는 AI 기술 발전의 가속화와 오픈소스 생태계의 성숙을 보여주며, 모델 레이어의 **상품화(commoditization)** 가능성을 시사합니다.

## 1. 오픈 모델의 발전과 클로즈드 모델과의 격차

오픈소스 AI 모델은 최근 몇 달간 눈부신 발전을 이루었으며, 클로즈드 모델과의 성능 격차를 빠르게 줄여나가고 있다.

### 1.1. 오픈소스 AI의 부상과 시장 변화
1. **오픈소스 AI의 발전**
   1. 지난 두 달은 오픈소스 AI에게 획기적인 기간이었다.
   2. 2025년 1월의 "DeepSeek 순간"이 있었지만, 당시 R1 모델은 경제적으로 가치 있는 작업에 실제로 사용되지 않았다.
   3. 반면, GLM 5.3 및 Kimi K3와 같은 모델은 Anthropic이 650억 달러 이상의 연간 반복 매출(ARR)을 달성하게 한 코딩 및 에이전트 작업의 상당 부분을 실제로 수행할 수 있다.
2. **경쟁 심화 및 토큰 소비자의 이점**
   1. 현재 토큰 소비자에게는 매우 흥미로운 시기이다.
   2. 경쟁이 심화되고 있으며, OpenAI-Anthropic 양강 체제를 넘어 토큰을 위한 경쟁이 확대되고 있다.
   3. Fireworks는 하루 40조 개 이상의 토큰을 처리하고 있으며, 이는 3월 말 OpenAI API 볼륨의 2배에 달한다.
3. **오픈 모델 성공의 영향: 상품화 우려**
   1. 오픈 모델의 성공으로 인해 주요 우려가 발생했다.
   2. 만약 오픈 모델이 클로즈드 모델에 비해 충분히 유능하고 비용이 훨씬 저렴하다면, 모델 레이어가 상품화될 가능성이 있다.
   3. 이러한 결과는 선도적인 연구소의 마진에 치명적일 수 있다.

### 1.2. 오픈 vs 클로즈드 모델 역량 격차 측정 방법
1. **벤치마크 선정의 중요성**
   1. 미래에 오픈 모델과 클로즈드 모델 간의 역량 격차가 어떻게 진행될지 예측하기 위해서는 먼저 과거를 측정해야 한다.
   2. 모든 과거 모델을 측정하기 위해 단일 벤치마크 세트를 선택하는 것은 잘못된 접근 방식이다.
   3. 모든 벤치마크는 특정 시대의 산물이기 때문이다.
   4. 새로운 벤치마크는 당시 모델 역량의 차이를 식별하기 위해 만들어진다.
   5. 벤치마크가 성공하면 모델 개발자들은 해당 벤치마크를 포화 상태에 이를 때까지 개선한다.
   6. 벤치마크가 포화 상태가 되면, 사람들은 더 이상 해당 벤치마크에 관심을 두지 않고 이 주기가 반복된다.
2. **LLM의 세 가지 시대**
   1. LLM 역사에는 지금까지 세 가지 시대가 있었다.
      1. 초기 스케일링 (Early scaling)
      2. 추론 (Reasoning)
      3. 에이전트 (Agentic)
   2. 각 시대는 모델 유틸리티의 단계적 증가를 나타내며, 단일 연속 추세를 그리기보다는 각 시대의 모델과 벤치마크를 개별적으로 평가하는 것이 더 효과적이다.
3. **오픈 vs 클로즈드 격차의 주기적 변화**
   1. 이러한 관점에서 보면, 오픈 모델과 클로즈드 모델 간의 격차는 주기적으로 움직인다는 것이 명확해진다.
   2. 각 시대의 시작에는 선도적인 연구소가 유망한 연구를 완료하고, 인상적인 모델을 훈련하며, 사용자에게 대규모로 배포하여 앞서나간다.
   3. 그 후, 다른 연구소들은 핵심적인 발전을 파악하고, 선도 연구소가 무엇을 하는지 역설계하며, 이를 자체 모델에 복제하여 격차를 좁힌다.
   4. 증류(distillation)를 고려하면 어떤 것도 영원히 비밀로 유지될 수 없다.
   5. 단지 시간이 얼마나 걸리는지의 문제이다.
4. **격차 해소 시간 단축 추세**
   1. 이 질문에 답하기 위해, 각 시대의 모든 관련 모델을 가져와 선별된 벤치마크 세트를 실행하여 복합 역량 점수를 얻었다.
   2. 그 결과는 명확한 추세를 보여준다.
      1. 각 세대마다 오픈소스 모델이 해당 시대의 첫 번째 클로즈드소스 모델을 따라잡는 데 걸리는 시간이 절반으로 줄어들고 있다.

<img alt="오픈 모델이 클로즈드 모델을 따라잡는 데 걸리는 시간" src="https://substackcdn.com/image/fetch/$s_!5AMx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F071b0427-31a2-42ce-9aae-7af849932fa_3200x1800.png">
<figcaption>오픈 모델이 클로즈드 모델을 따라잡는 데 걸리는 시간</figcaption>

### 1.3. 측정 방법론 및 고려 사항
1. **모델 및 벤치마크 선정 개요**
   1. 각 시대별로 선정된 모델과 벤치마크는 다음과 같다.

<img alt="각 시대별 모델 및 벤치마크" src="https://substackcdn.com/image/fetch/$s_!3Ysi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F398dbca6-c628-4a13-b22d-df1362c02434_2048x1280.png">
<figcaption>각 시대별 모델 및 벤치마크</figcaption>

2. **모델 선정의 주관성 및 보수적 접근**
   1. 특정 시점의 최첨단(SOTA) 클로즈드 모델과 오픈 모델을 선정하는 것은 주관적일 수 있다.
   2. 하지만, 선정된 모델들은 AI 전문가들 사이에서 일반적인 합의를 반영한다.
   3. 논쟁의 여지가 있는 경우(예: 현재 Fable 5 vs GPT 5.6)에는 보수적으로 두 모델 모두를 테스트했다.
3. **벤치마크 선정 기준**
   1. 벤치마크는 개인적인 선호와 인기를 조합하여 선정했다.
   2. Humanity's Last Exam(HLE)은 많은 문제가 있지만, 추론 시대의 결정적인 벤치마크 중 하나였으며 대체할 만한 것이 없었다.
   3. SWE-bench Pro 역시 인기가 많고 문제가 있지만, DeepSWE로 유사하게 근사화될 수 있다.
4. **벤치마크 점수 측정 및 환경 설정**
   1. 대부분의 벤치마크 점수는 Prime Intellect의 평가 스택(특히 환경 허브 및 Prime-RL에 포함된 evals harness)을 사용하여 직접 실행했다.
   2. 나머지는 Artificial Analysis 및 Datacurve의 DeepSWE 리더보드에서 얻은 결과이다.
   3. 오픈 모델은 출시 당시와 동일한 방식으로 서비스되었다.
      1. vLLM 버전
      2. 당시 사용되던 하드웨어
      3. 모델 카드에 명시된 샘플링 설정
   4. 클로즈드 모델의 경우, 고정된 API 버전을 대상으로 실행했다.
   5. 자체 측정값과 타사 값이 함께 표시된 차트에서는 동일한 규칙 세트를 적용했다.

## 2. LLM 시대별 오픈 모델과 클로즈드 모델의 격차 변화

LLM은 초기 스케일링, 추론, 에이전트 시대를 거치며 발전했으며, 각 시대마다 오픈 모델이 클로즈드 모델을 따라잡는 시간이 점진적으로 단축되었다.

### 2.1. 1시대: 초기 스케일링 (2022-2024)
1. **Llama-2의 등장과 초기 격차**
   1. 2023년 6월, ChatGPT가 세상을 뒤흔들고 있을 때, Meta의 FAIR 팀은 Llama-2-70B를 성공적으로 출시했다.
   2. 이는 최첨단에 근접한 최초의 오픈 모델이었다.
2. **1시대 벤치마크 및 GPT-3.5 Turbo와의 비교**
   1. 당시 SOTA를 정의하는 데 도움이 된 네 가지 벤치마크는 다음과 같다.
      1. GSM8K
      2. HumanEval
      3. TriviaQA
      4. MMLU-Pro

<img alt="1시대 벤치마크 점수" src="https://substackcdn.com/image/fetch/$s_!PJUJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb674a44-63d5-4960-a9b7-4f602ab8f8b3_2048x1152.png">
<figcaption>1시대 벤치마크 점수</figcaption>

   2. 이 벤치마크들은 당시 최첨단 모델의 역량을 대표한다.
      1. 간단한 객관식 문제
      2. 단어 문제
      3. 단일 함수 범위의 프로그래밍 문제
   3. Llama-2와 GPT-3.5 Turbo의 비교 결과는 다음과 같다.

<img alt="Llama-2와 GPT-3.5 Turbo의 벤치마크 점수 비교" src="https://substackcdn.com/image/fetch/$s_!TTkE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99e69460-de7f-48db-b750-b6ce87fde19b_2048x1152.png">
<figcaption>Llama-2와 GPT-3.5 Turbo의 벤치마크 점수 비교</figcaption>

3. **점수 정규화 및 초기 격차**
   1. 벤치마크 난이도 차이를 고려하여 점수를 정규화했다.
   2. 각 시대의 최고 점수는 100으로 설정하고, 다른 모든 모델은 이에 상대적으로 점수가 매겨진다.
   3. 복합 점수는 네 가지 벤치마크의 동일 가중치 평균을 나타낸다.
      1. GPT-3.5 Turbo (최첨단): 75.7점
      2. Llama-2-70B: 39.9점
   4. 이는 상당한 격차를 보여준다.
4. **격차 해소 과정 및 GPT-4o의 등장**
   1. 이러한 초기 지연은 시대의 나머지 스토리를 만든다.

<img alt="1시대 모델 성능 추이" src="https://substackcdn.com/image/fetch/$s_!0OZy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F232b9c60-4520-4ad7-b333-41398cff3f0c_2048x1152.png">
<figcaption>1시대 모델 성능 추이</figcaption>

   2. 2023년 12월에 출시된 Mixtral-8x7B는 GPT-4 역량에 대한 모멘텀을 만들었지만, GPT-4 Turbo와 GPT-4o가 다시 앞서나갔다.
   3. 2024년 7월 Llama-3.1-405B가 출시되어서야 오픈 모델이 GPT-3.5 Turbo와의 격차를 좁혔고, 복합 점수 86점을 기록했다.
   4. 마지막 최첨단 모델인 GPT-4o는 2024년 12월 DeepSeek V3에 의해 역량이 따라잡혔으며, 각각 95.5점과 94.1점을 기록했다.
   5. Qwen2.5-72B는 405B 파라미터 수의 6분의 1에 불과한 규모로 18조 개의 토큰으로 사전 훈련되었음에도 GPT-4o에 근접한 성능을 보였다.
5. **격차 해소의 첫 사례 및 OpenAI의 전략 변화**
   1. 이것이 격차가 좁혀진 첫 번째 사례이다.
   2. 이 시대 동안 최첨단 모델은 GPT-4의 역량을 크게 넘어서지 못했는데, 이는 주로 우선순위 때문이었다.
   3. Turbo와 4o는 GPT-4를 더 저렴하고 빠르게 만드는 데 중점을 두었지, 더 똑똑하게 만드는 데 중점을 두지 않았다.
   4. 한편, OpenAI는 다른 종류의 모델을 개발하고 있었다.
   5. 프로세스-보상 논문과 Noam Brown의 영입은 추론(reasoning)에 초점을 맞추고 있음을 시사했으며, 2024년 중반까지 모든 주요 연구소는 테스트 시간 컴퓨팅 연구를 발표했다.
   6. 405B 출시 7주 후인 2024년 9월 12일, OpenAI는 o1-preview를 출시하여 새로운 혁신 시대를 열었다.

### 2.2. 2시대: 추론 (2024-2025)
1. **o1의 등장과 벤치마크의 변화**
   1. o1은 벤치마크 선택과 격차를 재설정했다.
   2. 1시대의 초등 수준 평가는 o1의 모든 능력을 테스트하기에 더 이상 충분히 어렵지 않았다.
   3. 초등학교 수학 문제는 AIME로 대체되었다.
   4. Scale AI는 세계에서 가장 난해한 박사 수준의 객관식 문제들을 수집하여 도발적으로 '인류의 마지막 시험(Humanity's Last Exam)'이라고 명명했다.

<img alt="2시대 벤치마크" src="https://substackcdn.com/image/fetch/$s_!_TZT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7676e5dd-379e-49d4-ba17-25652fc3e5ad_2048x1152.png">
<figcaption>2시대 벤치마크</figcaption>

2. **DeepSeek R1의 역할과 초기 격차 축소**
   1. o1의 출시는 기술계에서 매우 중요하게 여겨졌다.
   2. 많은 사람들은 이날을 "우리가 AGI를 확실히 얻을 것이라고 알게 된 날"로 간주한다.
   3. 그러나 Llama-2-70B와 GPT-4의 격차와 달리, 2시대에는 오픈 모델과 클로즈드 모델 간의 격차가 훨씬 작게 시작되었다.
   4. 그 원인은 DeepSeek R1이라는 잘 알려지지 않은 모델이었다.

<img alt="o1-preview와 DeepSeek R1의 벤치마크 점수 비교" src="https://substackcdn.com/image/fetch/$s_!iZRt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F891cbf92-d756-4015-ba25-936c5fe533e6_2048x1152.png">
<figcaption>o1-preview와 DeepSeek R1의 벤치마크 점수 비교</figcaption>

   5. 이전 시대 시작 시점의 35.8점과 비교하여 12.1점의 격차를 보였다.
   6. 시장은 이에 반응하여 급락했다.
   7. 다행히 AI 자본 지출(capex) 시장은 빠르게 회복되었고, R1에 의해 확립된 "우리가 돌아왔다"는 오픈 모델 모멘텀은 Meta의 Llama-4 Maverick에 의해 곧 꺾였다.

<img alt="2시대 모델 성능 추이" src="https://substackcdn.com/image/fetch/$s_!XxAm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F700c6b14-aaea-4e05-ac7e-edb6480d5fca_2048x1152.png">
<figcaption>2시대 모델 성능 추이</figcaption>

3. **격차 해소 및 Anthropic의 전략**
   1. Gemini 2.5 Pro와 o3는 추론 최첨단을 계속해서 밀어붙였고, R1-0528 체크포인트는 2025년 5월에 78점을 기록하며 초기 격차를 해소했다.
   2. 12.1점의 격차를 좁히는 데 8.5개월이 걸렸다.

<img alt="2시대 모델 성능 추이 (격차 해소)" src="https://substackcdn.com/image/fetch/$s_!clCp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd00db9e-d73b-4e72-82ac-b7eab611446d_2048x1152.png">
<figcaption>2시대 모델 성능 추이 (격차 해소)</figcaption>

   3. 이 차트에서 Anthropic은 눈에 띄게 부재하다.
   4. 그들의 모델 카드에는 다른 모델들과 마찬가지로 이러한 벤치마크가 보고되었지만, 이 시대에는 리더보드 상단을 위해 경쟁하지 않았다.
   5. OpenAI와 Google이 왕관을 주고받는 동안, Anthropic은 Claude를 기본 코딩 에이전트로 만들고 있었다.
   6. 이는 다음 시대의 조건을 설정했다. 이제 중요한 벤치마크는 터미널에서 실행된다.

### 2.3. 3시대: 에이전트 (2025-현재)
1. **Claude Code의 성공과 에이전트 시대의 시작**
   1. Claude Code 이전에도 에이전트들은 주목받는 순간들이 있었지만(예: 2024년 3월 Cognition의 Devin 바이럴 데모), Anthropic은 모델과 하네스 제품을 성공적으로 결합한 최초의 회사였다.
   2. 이는 큰 성과를 거두었다.
   3. 2025년 5월 Claude Code의 일반 출시 이후, Anthropic은 650억 달러 이상의 ARR을 추가했다.
2. **에이전트 시대의 새로운 벤치마크**
   1. 에이전트와 함께 또 다른 새로운 벤치마크 세트가 등장했다.
   2. 복잡한 수학 문제는 더 이상 모델 역량을 테스트하는 최고의 방법이 아니었다.
   3. 대신, 사람들은 모델이 코드를 얼마나 잘 작성하고, 웹 검색을 수행하며, 일반적으로 인간처럼 컴퓨터를 사용하는지 알고 싶어 했다.

<img alt="3시대 벤치마크" src="https://substackcdn.com/image/fetch/$s_!Kxyi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe082580f-2b7d-4877-a6bd-b712eeec3e0c_2048x1280.png">
<figcaption>3시대 벤치마크</figcaption>

3. **에이전트 작업에 특화된 벤치마크**
   1. Terminal-Bench 2.1, BrowseComp-Plus, 𝜏³-banking, DeepSWE는 오늘날 에이전트가 사용되는 장기적인 작업(소프트웨어 엔지니어링, 심층 연구, 지식 작업)을 다룬다.
   2. 암기 효과를 제한하기 위해 의도적으로 최신 벤치마크를 선택했다.

<img alt="3시대 모델 성능 추이" src="https://substackcdn.com/image/fetch/$s_!NxrI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02ce4e10-36e6-4db4-ab09-99beac72cdff_2048x1152.png">
<figcaption>3시대 모델 성능 추이</figcaption>

4. **Opus 4.5와 GPT-5.2의 비교 및 Anthropic의 강점**
   1. 대부분의 AI 전문가들은 모델의 신뢰성 때문에 Opus 4.5를 에이전트 시대의 공식적인 시작으로 간주한다.
   2. 흥미롭게도, GPT-5.2(당시 OpenAI의 주력 모델)는 벤치마크 스위트에서 더 나은 성능을 보였지만, 이는 더 나은 사용자 경험으로 이어지지 않았다.
   3. 이제는 완전한 에이전트 제품(모델 + 하네스)이 중요했으며, Anthropic은 일반적인 에이전트 작업에 뛰어난 하네스를 반복적으로 개발하는 데 집중했다.
   4. 반면 Codex는 상대적으로 미숙했으며, OpenAI는 웹 브라우저와 같은 부수적인 작업들을 동시에 추구하고 있었다.
5. **모델 출시 속도 가속화**
   1. 두 선도 연구소 간의 모델 출시 간격도 단축되었다.
   2. OpenAI와 Anthropic은 이 시대 동안 평균 51일마다 모델을 출시하여 양강 체제를 구축했다.
   3. 이는 1시대의 평균 213일, 2시대의 평균 120일과 비교할 때 엄청난 속도 향상이다.

<img alt="시대별 모델 출시 간격" src="https://substackcdn.com/image/fetch/$s_!volS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F021545e4-9386-4738-8dff-ba1cebd218c4_3200x1800.png">
<figcaption>시대별 모델 출시 간격</figcaption>

6. **격차 해소 속도 및 일관된 추세**
   1. 최첨단 모델에 의해 창출된 경제적 가치가 엄청나게 폭발했음에도 불구하고, 3시대의 격차는 이전 두 시대보다 더 빠르게 좁혀졌다.
   2. Kimi K2.6은 4.8개월 만에 56.3점을 기록하며 Opus 4.5를 넘어섰고, GLM-5.2는 6개월 만에 72.4점을 기록하며 GPT-5.2를 넘어섰다.
   3. 각 후속 시대마다 격차 해소 시간이 절반으로 줄어드는 추세는 놀랍도록 일관적이다.

<img alt="시대별 격차 해소 시간" src="https://substackcdn.com/image/fetch/$s_!H-n0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb272b3ef-7f89-4f4a-a44d-9be5a279da5c_2048x1152.png">
<figcaption>시대별 격차 해소 시간</figcaption>

## 3. 미래 전망 및 고려 사항

오픈 모델과 클로즈드 모델의 미래에 대한 분석은 벤치마크의 한계와 안전성 테스트의 영향을 고려해야 한다.

### 3.1. 벤치마크의 한계와 실제 사용 경험
1. **벤치마크의 불완전성**
   1. 벤치마크가 모든 것을 말해주지는 않는다는 점을 인정해야 한다.
   2. Kimi K3가 선별된 복합 벤치마크에서 Fable 5보다 높은 점수를 받을 수 있지만, SemiAnalysis에서는 여전히 일상 업무에 Fable을 선호한다.
   3. 이는 부분적으로 Anthropic이 Claude Code 및 Claude Tag와 같은 제품을 통해 모델을 더 잘 상품화했기 때문이기도 하지만, 벤치마크가 실제 작업에 대한 완벽한 대리 지표가 아니기 때문이기도 하다.
2. **공개 벤치마크의 문제점**
   1. 특히 공개 벤치마크의 경우 이러한 경향이 두드러진다.
   2. 모델 개발자들은 벤치마크 작업을 밀접하게 모방하는 여러 RL 환경을 생성하여 쉽게 벤치마크 점수를 올릴 수 있다.

### 3.2. 안전성 테스트가 격차 해소 시간에 미치는 영향
1. **안전성 테스트로 인한 격차 해소 시간 지연 가능성**
   1. 3시대의 격차 해소 시간이 Anthropic과 OpenAI가 Moonshot 및 Zhipu보다 안전성 테스트에 더 많은 시간을 할애했기 때문에 인위적으로 낮게 평가될 수 있다고 주장할 수 있다.
2. **과거 사례를 통한 반박**
   1. 그러나 이는 새로운 현상이 아니다.
   2. 예를 들어, GPT-4는 출시 218일 전에 훈련을 마쳤다.
   3. Mythos가 2월 중순에 훈련을 마쳤다고 가정하더라도, Fable 출시까지는 여전히 114일의 지연이 있었다.
