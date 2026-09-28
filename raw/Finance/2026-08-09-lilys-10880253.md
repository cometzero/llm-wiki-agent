---
title: "SpaceX 10GW in 2027 – Why It’s Real, Will Drive $500B ARR for SpaceX, and Why Microsoft Will Be the Largest Offtaker"
origin: lilys_ai
lilys_project_id: 10880253
lilys_project_url: "https://lilys.ai/digest/10880253"
lilys_created_at: "2026-08-09T01:58:27.481Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "12790354"
sources:
  - id: "11711635"
    url: "https://newsletter.semianalysis.com/p/spacex-10gw-in-2027-why-its-real"
    title: "SpaceX 10GW in 2027 – Why It’s Real, Will Drive $300B ARR for SpaceX, and Why Microsoft Will Be the Largest Offtaker"
    status: "done"
---

# SpaceX 10GW in 2027 – Why It’s Real, Will Drive $500B ARR for SpaceX, and Why Microsoft Will Be the Largest Offtaker

## LilysAI note

> SpaceX가 2027년까지 10GW 규모의 데이터센터를 구축하고 3천억 달러의 매출을 달성할 것이라는 전망은 현실성이 있는가? **마이크로소프트가 AI 모델 추론 서비스로 연간 100M/MW의 수익을 창출할 수 있게 되면서 대규모 컴퓨팅 자원 확보에 대한 수요가 폭발적으로 증가**했고, SpaceX는 **빠른 구축 속도와 유연한 계약 조건**으로 이 수요를 충족시킬 수 있기 때문에 충분히 현실성이 있습니다.

## 1. SpaceX의 2027년 10GW 데이터센터 목표와 3천억 달러 매출 달성 전망
SpaceX가 2027년까지 10GW 규모의 데이터센터를 구축하고 연간 3천억 달러의 매출을 달성하겠다는 목표는 현실성이 있으며, 이는 마이크로소프트가 주요 고객이 될 것이라는 분석이다.

### 1.1. SpaceX의 기가와트(Gigawatt) 목표와 시장의 반응
1. **일론 머스크의 발표**: 일론 머스크는 SpaceX의 첫 실적 발표에서 2027년에 6~8GW를 추가로 건설 및 공급할 계획이며, 잠재적으로 10GW 이상도 가능하다고 발표했다.
2. **막대한 투자 규모**: 500억 달러/GW를 기준으로 할 때, 이는 2027년에 3천억~5천억 달러의 자본 지출(CapEx)이 필요하다는 의미이다.
   1. 이는 AWS나 Google과 같은 하이퍼스케일러의 예상 지출과 맞먹는 엄청난 규모이다.
   2. 경쟁사보다 수익성이 훨씬 낮은 회사에게는 믿기 어려운 수치로 여겨진다.
3. **목표의 현실성**: 하지만 SemiAnalysis는 이 목표가 현실적이라고 판단하며, SpaceX가 2027년 말까지 약 10GW를 구축할 수 있을 것으로 예상한다.
   1. SpaceX가 데이터센터 건설의 일반적인 제약 사항들을 어떻게 우회하는지 분석한다.

### 1.2. AI 모델 추론 서비스의 높은 수익성
1. **대규모 컴퓨팅 자원의 희소성**: 대규모의 단기 컴퓨팅 자원은 매우 희소하며, GW당 연간 최대 500억 달러에 달하는 높은 프리미엄이 붙는다.
   1. AI 연구소들은 이러한 비용을 감당하고도 충분한 수익을 창출할 수 있다.
2. **OpenAI 및 Anthropic의 수익 잠재력**: Tokenomics 모델과 Inference Simulator 분석 결과, OpenAI와 Anthropic은 GB300 클러스터에서 API 추론 서비스를 판매할 때 GW당 연간 1천억 달러 이상의 수익을 창출할 수 있다.
   1. 이는 현재 네오클라우드 가격으로 GB300 클러스터를 1년 임대하는 비용보다 훨씬 높은 수치이다.
   2. 프론티어 모델 기업들에게 추론 토큰 서비스는 엄청나게 수익성이 높다.
3. **수익성 추정의 근거**:
   1. **비용 추정**: 보수적인 GPU 시간당 3달러의 임대료를 적용하여 GW당 연간 약 120억 달러의 비용을 추정한다.
   2. **토큰 생산량 추정**: Inference Simulator와 AgentX 벤치마크를 사용하여 프론티어급 모델 아키텍처의 토큰 생산량을 추정한다.
   3. **최종 추정**: 입력, 캐시 읽기, 캐시 쓰기, 출력 토큰 비용을 실제 워크로드 비율로 혼합하여 GW당 연간 1천억 달러를 초과하는 최종 수익을 추정한다.
4. **Inference Simulator의 신뢰성**:
   1. **기본 원리**: Inference Simulator는 최신 AI 가속기가 작동하는 방식에 대한 근본적인 이해를 바탕으로 구축되었다.
   2. **성능 모델**: 추론 과정에서 프론티어 모델이 작동하는 방식에 대한 루프라인 및 현실적인 성능 모델을 구축하며, 모든 작업에 대한 타이밍과 실제 트레이스 출력을 제공한다.
   3. **종합 시뮬레이션**: 실제 실리콘에서 실제 워크로드가 실행되는 과정을 엔드투엔드로 시뮬레이션한다.
   4. **검증**: 광범위한 가속기 및 워크로드에 대한 시뮬레이터의 정확성을 검증했으며, 설계 사양을 기반으로 미래 가속기의 성능을 정확하게 예측하는 능력을 지속적으로 개선하고 있다.

<img alt="Fine-grained data covering end-to-end simulated workload execution on silicon​ produces real profiler traces for analysis with standard tools such as Perfetto. Source: SemiAnalysis Inference Simulator" src="https://substackcdn.com/image/fetch/$s_!rNmG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e508607-fc09-402e-b1b1-2a3d4a4ca88e_1200x598.jpeg">
<figcaption>실리콘에서 엔드투엔드 시뮬레이션된 워크로드 실행을 다루는 세분화된 데이터는 Perfetto와 같은 표준 도구를 사용한 분석을 위해 실제 프로파일러 트레이스를 생성한다. 출처: SemiAnalysis Inference Simulator</figcaption>

<img alt="High-level projections are produced across common inference workloads and hardware platforms across the pareto frontier. Source: SemiAnlaysis Inference Simulator" src="https://substackcdn.com/image/fetch/$s_!6tVu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda1d160f-cc47-49a9-8cf9-002d41972d22_1151x675.jpeg">
<figcaption>파레토 프론티어 전반에 걸쳐 일반적인 추론 워크로드 및 하드웨어 플랫폼에 대한 높은 수준의 예측이 생성된다. 출처: SemiAnalysis Inference Simulator</figcaption>

### 1.3. 마이크로소프트의 대규모 컴퓨팅 자원 확보 동기
1. **마이크로소프트의 수익 잠재력**: OpenAI와 Anthropic 외에 마이크로소프트도 GW당 이러한 경제성을 창출할 수 있는 세 번째 회사이다.
   1. **OpenAI 모델 접근**: 마이크로소프트는 OpenAI 모델에 대한 완전한 접근 권한을 가지고 있어, 훈련 비용 없이 동일한 MW당 수익과 마진을 창출할 수 있다.
   2. **계약 조건 변경**: 2026년 4월에 재협상된 OpenAI와의 계약에서 기존의 20% 매출 공유 조항이 삭제되었다.
   3. **대규모 조달 유인**: 마이크로소프트는 가능한 한 빠르고 많이 MW를 확보할 강력한 동기를 가지고 있다.
   4. **수익성 개선 기회**: 현재 데이터센터 용량의 상당 부분이 OpenAI에 연간 약 1,400만 달러/MW로 제공되지만, 마이크로소프트는 이 수익 구성을 개선할 기회를 가지고 있다.
   5. **Azure 매출 성장 가속화**: 잠재적으로 Microsoft Azure의 매출 성장률을 현재 약 42%에서 내년에는 100% 이상으로 가속화할 수 있다.
   6. **SpaceX의 역할**: 이는 세대에 한 번 올까 말까 한 기회이며, SpaceX는 이를 충족시킬 수 있는 매우 유리한 위치에 있다.

### 1.4. 마이크로소프트가 SpaceX와 계약할 가능성
1. **3GW 계약의 현실성**: 마이크로소프트가 SpaceX와 GW당 500억 달러에 3GW를 계약하는 것이 터무니없이 들릴 수 있지만, 두 가지 이유로 가능하다고 본다.
   1. **마이크로소프트의 데이터센터 확장 준비**: 마이크로소프트는 이미 대규모 데이터센터 확장을 준비하고 있다.
      1. 현재까지 10GW 규모의 계약을 체결했으며, 이는 총 계약 가치 3천억 달러 이상에 해당한다(GPU 비용 제외).
      2. 더 많은 계약이 체결될 것으로 예상된다.
      3. **주의사항**: 이 계약들은 2027년 말과 2028년 용량에 기여하므로, 단기적인 공급 부족을 채워야 한다.
   2. **낮은 재무 위험**: Anthropic 및 Google과의 SpaceX 계약과 유사하게 90일 취소 정책이 있어 재무제표 위험이 전혀 없다.
      1. 이러한 수익 기회를 고려할 때, Amy Hood(마이크로소프트 CFO)가 승인하기 매우 쉽다.

### 1.5. SpaceX의 자금 조달 방안
1. **자금 조달의 필요성**: 일론 머스크는 선도적인 하이퍼스케일러와 같은 재무제표 없이 어떻게 그렇게 많은 자본 지출을 감당할 수 있을까?
2. **두 가지 주요 방안**: 다음 두 가지 항목의 조합을 예상한다.
   1. **Nvidia의 지원**: Nvidia의 벤더 파이낸싱 형태로 초기 현금 비용을 낮출 수 있다.
      1. 일론 머스크가 실적 발표에서 Nvidia 독점 계약을 선언한 이유가 여기에 있을 가능성이 높다.
      2. Accelerator Model에 따르면, xAI/SpaceX는 TPU 및 AMD와 같은 대안을 적극적으로 평가했지만, 재정적 이유로 이들을 포기하고 Nvidia에 집중했을 가능성이 크다.
   2. **운영 현금 흐름을 통한 자금 조달**: 업계 최고 수준의 가격 책정과 가장 빠른 구축 기간을 통해 운영 현금 흐름으로 자금을 조달할 것이다.
      1. SpaceX는 3~5개월의 리드 타임으로 대규모 컴퓨팅 자원을 제공하는 타의 추종을 불허하는 서비스를 제공하며, 이에 따라 GW당 연간 3천만~5천만 달러로 가격을 책정할 것이다.
      2. 이는 1년 이내에 자본 지출을 회수할 수 있게 한다.

### 1.6. SpaceX의 2027년 말까지 3천억 달러 ARR 달성 경로
1. **ARR 목표**: SpaceX는 2027년 말까지 연간 반복 매출(ARR) 3천억 달러를 달성할 수 있는 경로를 가지고 있다.
2. **수익화 가정**: 이는 2027년 증분 컴퓨팅 자원의 50%만 수익화된다고 가정한다.
   1. 나머지 50%는 Grok 및 Cursor 팀의 훈련용으로 사용되며, 추론 매출은 모델링되지 않았다.

## 2. 마이크로소프트의 10GW 확보와 연간 1억 달러/MW 기회
마이크로소프트는 1억 달러/MW의 수익 기회를 포착하기 위해 10GW 규모의 데이터센터를 확보하고 있다.

### 2.1. 마이크로소프트의 데이터센터 활동 재개
1. **활동 중단 및 재개**: 2024년 12월, SemiAnalysis는 마이크로소프트의 리스 활동이 극적으로 중단되었음을 처음으로 지적했다.
   1. 현재 마이크로소프트는 다시 활동을 시작했다.
2. **모델 추적**: SemiAnalysis의 모델은 분기별 리스 활동, 네오클라우드 계약, 자체 구축 건설 시작, 대규모 구속력 있는 PPA(전력 구매 계약) 및 ESA(에너지 서비스 계약)를 추적한다.
3. **계약 현황**: 마이크로소프트는 이러한 모든 분야에서 10GW 이상의 계약을 체결했으며, 이는 약 3천억 달러의 새로운 구속력 있는 약정에 해당한다.

<img alt="The SemiAnalysis diagram illustrates Microsoft's projected growth in energy contracts and construction activities for the years 2025 and 2026. AI-generated content may be incorrect." src="https://substackcdn.com/image/fetch/$s_!HzYG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2151a0ea-4cb2-4d92-bca2-629635199d33_1248x666.png">
<figcaption>SemiAnalysis 다이어그램은 2025년과 2026년 마이크로소프트의 에너지 계약 및 건설 활동의 예상 성장을 보여준다. 출처: SemiAnalysis Datacenter Model</figcaption>

### 2.2. 1억 달러/MW 수익 기회 포착을 위한 컴퓨팅 수요
1. **컴퓨팅 자원 부족**: 마이크로소프트가 이러한 활동을 재개한 주요 이유는 연간 1억 달러/MW의 수익 기회를 포착하기 위한 컴퓨팅 자원의 절박한 필요성 때문이다.
2. **OpenAI와의 대규모 계약**: 2025년 10월, 마이크로소프트는 OpenAI와 2,500억 달러 규모의 계약을 체결했으며, 이는 Tokenomics Model에서 총 약 7GW로 추정된다.
   1. 이 대규모 IaaS(Infrastructure-as-a-Service) 계약으로 인해 마이크로소프트는 다른 사용 사례에 대한 컴퓨팅 자원이 매우 부족해졌다.
   2. 마이크로소프트는 OpenAI 모델에 대한 접근 권한을 API 비즈니스인 Foundry나 Copilot과 같은 애플리케이션에 활용하지 못했다.
3. **최고 마진 서비스**: 이러한 서비스들이 MW당 가장 높은 마진과 수익을 제공한다.

<img alt="AI Value Capture - The Shift To Model Labs" src="https://substackcdn.com/image/fetch/$s_!Yyjb!,w_1300,h_650,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1d0c080-fbf0-4274-a129-4bfea496225e_2752x1536.png">
<figcaption>AI 가치 포착 - 모델 연구소로의 전환</figcaption>

### 2.3. AI 산업의 빠른 변화와 추론 마진의 중요성
1. **AI 산업의 속도**: AI 산업에서는 하루가 다른 산업의 1년처럼 느껴질 정도로 모델 출시, 소프트웨어 혁신, 하드웨어 개선이 빠르게 이루어진다.
2. **추론 마진의 인식**: 지난 몇 달 동안, API 가격으로 프론티어 토큰을 제공하는 것이 실제로 매우 높은 마진을 가진 사업이라는 인식이 정교한 투자자들 사이에서 합의되었다.
   1. **SemiAnalysis의 선도적 분석**: SemiAnalysis는 1월에 Tokenomics Model 구독자들에게 추론 총마진이 60% 이상이라는 점을 처음으로 알렸다.
   2. **Opus 4.8의 높은 마진**: 6월에는 Opus 4.8이 85% 이상의 마진을 가진다는 심층 분석을 발표했으며, 이는 Anthropic 분석 시 모든 사람이 인용하는 기본 수치가 되었다.
3. **마진 추정의 복잡성**: 이러한 마진 추정치를 얻기 위해 유출된 재무 정보, InferenceX 데이터, 최신 가속기 마이크로벤치마크, 오픈 소스 연구소의 논문, 블로그, 트윗 등을 신중하게 종합해야 했다.
   1. **DeepSeek 사례**: DeepSeek 투자자 통화에서 GPU 회수 기간이 10개월이라고 언급한 것과 같은 새로운 데이터 포인트는 SemiAnalysis의 추정치가 정확한 범위 내에 있음을 확인시켜 준다.
   2. **세분화된 정보의 필요성**: 단일 회사 전체의 추론 총마진 수치보다는, 전체 처리량 대 지연 시간 파레토 프론티어에 걸쳐 모든 (모델, 가속기) 조합에 대한 총마진을 아는 것이 중요하다.
      1. 예를 들어, Trainium3에서 Opus 5 Fast를 제공하는 것과 TPUv7에서 Fable 5를 제공하는 것의 총마진은 얼마인가?

### 2.4. Inference Simulator를 통한 정확한 수익 예측
1. **Inference Simulator의 역할**: SemiAnalysis는 Inference Simulator를 통해 이러한 질문에 답하며, 이는 컨설팅 고객에게 독점적으로 제공된다.
2. **비용 및 수익 예측**: AI Cloud TCO 모델은 이미 비용 측면을 해결하지만, 수익 측면은 역사적으로 알 수 없었다.
   1. **시뮬레이션 프레임워크**: 이를 해결하기 위해 실제 모델 실행을 가상 하드웨어에서 시뮬레이션하는 프레임워크를 개발했으며, 이는 다양한 가속기 및 작업 유형을 다루는 미세 조정된 성능 모델에 의해 지원된다.
   2. **다양한 구성 시뮬레이션**: 모든 모델을 가능한 모든 서비스 구성에서 시뮬레이션된 XPU에서 실행하며, 실제 및 이상적인 서비스 조건을 혼합한다.
   3. **정확한 성능 추정**: 이를 통해 모델 아키텍처에 대한 충분한 정보를 바탕으로 소프트웨어, 하드웨어 및 워크로드의 모든 조합에 대한 성능을 정확하게 추정할 수 있다.
3. **Tokenomics Model의 확장**: 이 시뮬레이터 덕분에 Tokenomics Model은 이제 모든 관련 칩에서 주요 OpenAI/Anthropic 모델을 실행하는 MW당 높은 수준의 수익 수치를 포함한다.
   1. **워크로드 형태의 중요성**: 워크로드 형태는 매우 중요한 요소이며, SemiAnalysis는 자체 사용에서 수집된 100만 달러 이상의 에이전트 트레이스를 실제 상호작용 및 TTFT(Time To First Token) 수준을 충족하면서 시뮬레이션한다.
   2. **Fable 5 on GB200 vs GB300**: Fable 5를 GB200과 GB300에서 서비스하는 것에 대한 수치를 예시로 제공한다.
4. **마이크로소프트의 기회**: 이것이 바로 마이크로소프트의 MW당 1억 달러 기회이다.
   1. 최근 Codex 수요 급증과 OpenAI ARR 가속화를 고려할 때, 마이크로소프트는 OpenAI 모델을 서비스하여 유사한 속도로 컴퓨팅 자원을 수익화할 수 있을 것으로 예상된다.

## 3. SpaceX의 놀라운 데이터센터 구축 속도
SpaceX는 다른 어떤 회사보다 빠르게 데이터센터를 구축할 수 있는 능력을 입증했으며, 이는 2027년까지 10GW+ 목표 달성을 가능하게 한다.

### 3.1. 일론 머스크의 상업적 통찰력
1. **가치 기반 가격 책정**: Meta Compute 기사에서 설명했듯이, 일론 머스크는 AI 연구소의 마진이 극적으로 급증했음을 이해하고, 이에 따라 일반적인 "원가 가산" 방식이 아닌 "가치 기반 가격 책정"을 GPU 클러스터에 도입했다.

### 3.2. SpaceX의 데이터센터 구축 속도 증거
1. **빠른 구축 속도**: 일론 머스크는 다른 어떤 회사보다 빠르게 데이터센터를 구축해야 하며, SemiAnalysis는 그가 그렇게 할 수 있다고 믿는다.
2. **과거 사례**:
   1. **Colossus 1**: 300MW 규모의 Colossus 1을 122일 만에 구축했다.
   2. **Colossus 2**: 200MW 규모의 Colossus 2를 6개월 만에 구축했다.
   3. **현장 발전소 건설**: 허가를 피하기 위해 국경 너머 1km 떨어진 곳에 현장 발전소를 건설하기로 결정했다.
3. **최근 속도 증명**:
   1. **Southaven 발전소 확장**: 2026년 2월 27개 터빈(약 495MW)에서 2026년 7월 69개 터빈(1.7GW)으로 확장되었다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!9EM4!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e0d5106-157f-46bc-9c20-afe0c6d3ef25_1603x1247.png">
<img alt="" src="https://substackcdn.com/image/fetch/$s_!riXP!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea3b3b74-c0f5-479b-b0c7-0328ddb461f2_821x872.png">
<figcaption>출처: SemiAnalysis Datacenter Industry Model; Southaven 발전소, 2026년 2월 ~ 2026년 7월</figcaption>

### 3.3. SpaceX의 독특한 데이터센터 구축 전략
1. **"MiniHard"의 빠른 건설**: 2026년 3월 수직 건설을 시작한 "MiniHard"는 약 5개월 만에 450-500MW에 도달할 것으로 예상된다.
2. **다른 접근 방식**: 일론 머스크가 다른 회사보다 더 잘 짓는다는 의미는 아니며, 단지 다른 전략을 적용하고 있을 뿐이다.
3. **공급망 제약 우회**:
   1. **스위치기어 및 대형 전력 변압기**: 2년 이상 품절된 스위치기어 및 대형 전력 변압기 대신, 중국에서 전력 모듈을 구매하고, 발전소에서 저전압 변압기로 중전압 전력을 직접 공급하여 대형 전력 변압기를 건너뛴다.
      1. 저전압 변압기는 훨씬 더 널리 구할 수 있다.
   2. **속도 대 효율성**: SpaceX는 속도 대 효율성 트레이드오프를 관리하는 데 가장 뛰어난 전기 엔지니어들을 보유하고 있다.
      1. 대부분의 데이터센터 운영자는 효율성과 품질을 최적화하여 15~20년 장기 계약을 체결하지만, SpaceX는 속도를 최우선으로 한다.
   3. **가치 증명**: 컴퓨팅 제약과 매우 높은 AI 토큰 마진 시대에, 3개월 내에 사용 가능하고 90일 취소 정책이 있는 500MW 클러스터는 세계에서 가장 희소하고 가치 있는 자산 중 하나이다.
      1. 일반적인 "품질" 지표는 중요하지 않다.
      2. **사례**: 세계에서 가장 수직 통합된 인프라 회사인 Google조차 SpaceX와 계약을 체결했다는 것이 이를 증명한다.
4. **가스 터빈 공급 확보**:
   1. **GEV 백로그**: GEV 터빈은 5년 이상 백로그되어 있지만, 다른 많은 옵션이 있다.
   2. **다양한 공급업체**: SemiAnalysis의 에너지 모델은 데이터센터에 대규모 주문을 확보한 30개 이상의 가스 발전 장비 제조업체를 추적한다.
   3. **새로운 공급업체와의 협력**: 충분히 노력하고 새로운 공급업체와 협력할 의지가 있다면 충분한 가용 용량이 있다.
   4. **중고 시장 활용**: 터빈의 중고 시장 거래량이 급증하고 있다.
      1. 예를 들어, 원래 Oracle의 뉴멕시코 부지로 예정되었던 모든 터빈이 시장에 나와 있다.
      2. 중고 시장 가격은 매우 높지만, 일론 머스크는 지불할 수 있다.
5. **인력 제약 극복**:
   1. **병렬화 및 사전 조립**: 가능한 한 많은 작업을 병렬화하고, 시운전 프로세스를 줄이며, 가능한 한 많이 사전 조립한다.
   2. **Colossus 2 사례**: Colossus 2의 일일 최대 건설 인력은 약 3천 명으로, 다른 기가와트 규모 데이터센터 건설 현장보다 훨씬 적다.
   3. **일론 머스크의 역사**: 일론 머스크는 Tesla와 SpaceX의 역사에서 볼 수 있듯이, 업계 표준보다 적은 인력으로 많은 성과를 달성한 오랜 역사를 가지고 있다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Vpm4!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b39afad-99d2-46eb-85c4-937afa2ef699_1099x1050.png">
<img alt="" src="https://substackcdn.com/image/fetch/$s_!nLUB!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9227934-69eb-44b1-a31c-e27ad0089597_1093x1033.png">
<figcaption>출처: SemiAnalysis Datacenter Industry Model; MiniHard, 2026년 3월 ~ 2026년 7월</figcaption>

### 3.4. 10GW+ 구축의 가능성 및 전략
1. **추가 건설 시간**: 2027년까지 많은 데이터센터 쉘을 구축할 충분한 시간이 있다.
   1. MiniHard는 일론 머스크의 첫 진정한 그린필드(신규 부지) 프로젝트였으므로, 다음 프로젝트에서는 더 나은 성과를 낼 수 있을 것이다.
2. **개조(Retrofit) 옵션**: Colossus 1과 2는 개조를 통해 놀랍도록 빠르게 구축되었다.

<img alt="xAI's Colossus 2 - First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise" src="https://substackcdn.com/image/fetch/$s_!4HLZ!,w_1300,h_650,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb21d4c51-8f25-4cd4-b0fd-fe3303381090_1536x1024.png">
<figcaption>xAI의 Colossus 2 - 세계 최초의 기가와트 데이터센터, 독특한 RL 방법론, 자본 조달</figcaption>

3. **Colossus 1의 역사적 의미**: xAI의 Colossus 1에 대해 많은 글이 쓰였다.
   1. 멤피스 건설은 역사에 남을 만한 일이다.
   2. 122일 만에 처음부터 구축된 가장 큰 AI 훈련 클러스터이다.
   3. 약 20만 개의 H100/H200과 약 3만 개의 GB200 NVL72를 갖춘, 현재까지 가장 큰 완전 운영 단일 일관성 클러스터이다(Google 제외).
4. **10GW+ 구축의 과제**: 1년에 10GW 이상을 구축하는 것은 다른 이야기이다.
   1. **부지 확보**: SpaceX는 쉬운 허가와 가스 접근이 가능한 적합한 부지를 전국적으로 찾아야 할 것이다.
   2. **충분한 옵션**: 하지만 상당한 확장을 지원할 수 있는 충분한 옵션이 있다고 믿는다.
   3. **현장 가스 발전**: 이는 자연스럽게 현장 가스 발전에 크게 의존할 것이다.
