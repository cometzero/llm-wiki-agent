---
title: "OpenAI Jalapeño: Better Than Nvidia Blackwell"
origin: lilys_ai
lilys_project_id: 11144230
lilys_project_url: "https://lilys.ai/digest/11144230"
lilys_created_at: "2026-08-29T03:10:10.961Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13130343"
sources:
  - id: "12009988"
    url: "https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia"
    title: "OpenAI Jalapeño: Better Than Nvidia Blackwell"
    status: "done"
---

# OpenAI Jalapeño: Better Than Nvidia Blackwell

## LilysAI note

> OpenAI가 자체 개발한 추론 칩 **'Jalapeño'**의 핵심 특징은 무엇인가요? 이 칩은 엔비디아의 최신 칩인 블랙웰(Blackwell)과 루빈(Rubin)을 능가하는 **전력 효율성(perf/W)**을 보여주며, 특정 모델에 특화되지 않은 **범용적인 AI 추론 칩**으로 설계되어 다양한 AI 워크로드에서 뛰어난 성능을 발휘합니다.

## 1. OpenAI의 Jalapeño 칩 개요 및 경쟁력
OpenAI는 LLM 추론 전용으로 설계된 자체 칩 'Jalapeño'를 발표했으며, 이는 엔비디아, AMD, 구글의 칩을 능가하는 성능을 보여준다.

### 1.1. Jalapeño 칩 개발 배경 및 특징
1. **Jalapeño 칩 개발 및 발표**
    1. OpenAI는 지난 몇 년간 LLM 추론 전용 칩인 "Jalapeño"를 조용히 개발해왔다.
    2. 이 칩은 최근 Hot Chips 행사에서 발표되었으며, 성공적인 테이프아웃(tapeout)에 대한 소문이 돌았다.
    3. OpenAI는 Broadcom과의 파트너십을 통해 2024년 중반에 설계 작업을 시작하여 약 16개월 만에 제조 테이프아웃을 완료하는 매우 빠른 ASIC 개발 주기를 보여주었다.
2. **업계 선도적인 성능**
    1. 일반적으로 1세대 칩은 경쟁력이 없지만, OpenAI는 이러한 추세를 깨고 여러 오픈 소스 모델에서 엔비디아, AMD, 구글의 모든 칩을 능가하는 업계 선도적인 성능을 달성했다.
    2. 이는 극단적인 하드웨어-소프트웨어 공동 설계를 통해 가능했다.
    3. 놀랍게도 OpenAI는 특정 모델 추론 부분에 과도하게 특화되지 않고, 모든 시나리오에서 높은 성능을 제공하는 범용 칩에 중점을 두었다.

### 1.2. 범용 추론 칩으로서의 Jalapeño
1. **OpenAI 모델에 특화되지 않은 범용성**
    1. 많은 사람들이 OpenAI 칩이 OpenAI 모델에 특화되어 있다고 말하지만, 이는 사실이 아니다.
    2. Jalapeño는 모든 종류의 모델과 워크로드를 실행할 수 있는 범용 추론 칩이다.
    3. OpenAI는 벤치마크인 InferenceX를 통해 이를 입증했으며, 심지어 Codex 프롬프트만으로 Doom을 실행하는 것을 시연하기도 했다.
2. **놀라운 개발 속도**
    1. 칩 개발 타임라인은 매우 놀랍다.
    2. 이는 AI가 칩 설계를 가속화하는 데 사용된다는 주장이 현실임을 보여준다.
    3. 빠른 개발 속도에도 불구하고, OpenAI는 많은 투자를 하고 실용적인 설계 결정을 내렸으며, 뛰어난 팀 역량을 바탕으로 이러한 성과를 달성했다.
3. **경쟁력 있는 사양**
    1. Jalapeño는 사양만으로도 즉각적인 경쟁자로 부상한다.

    <img alt="Jalapeño의 사양" src="https://substackcdn.com/image/fetch/$s_!IZvP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe346a4e5-76cb-4fd9-be95-00321116b605_1846x510.png" caption="출처: SemiAnalysis">

    2. HBM4를 사용하여 엔비디아 및 AMD의 플래그십 GPU와 비교할 만한 수준이다.

    <img alt="HBM4를 사용하는 Jalapeño의 사양" src="https://substackcdn.com/image/fetch/$s_!jhVL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F327f95f7-ab6b-44ae-9b8f-17c1ff5d296b_1712x1300.png" caption="출처: OpenAI">

### 1.3. 전력 효율성(perf/W) 및 성능 우위
1. **압도적인 전력 효율성**
    1. Jalapeño는 토큰 처리량(token throughput)을 전체 유틸리티 MW당으로 측정하는 perf/W 결과에서 다른 모든 칩을 압도한다.
    2. 이는 Multi Token Prediction(MTP) 없이 달성된 결과이며, 차트의 다른 칩들은 모두 MTP를 사용한 최적의 구성이다.

    <img alt="Jalapeño의 전력 효율성 비교" src="https://substackcdn.com/image/fetch/$s_!2a3j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19a7f45a-df8e-436e-ba04-df5d8610f3da_2048x1330.png" caption="출처: SemiAnalysis">

2. **다양한 시나리오에서의 우수성**
    1. Jalapeño는 특정 곡선 지점에 맞춰 튜닝되지 않았음에도 불구하고 거의 모든 시나리오에서 Blackwell의 perf/W를 능가한다.
    2. 낮은 지연 시간 시나리오뿐만 아니라 높은 처리량 시나리오에서도 탁월한 성능을 발휘한다.
    3. Single Token Prediction(STP) 결과와 비교하면 다른 모든 경쟁자를 압도한다.
    4. 낮은 동시성 시나리오에서 Jalapeño는 DeepSeek R1 모델에서 동시성 1일 때 사용자당 초당 700개 이상의 토큰을 처리하며 놀라운 상호작용성을 보여준다.
3. **STP 기반의 성능 및 모델 지원**
    1. 이 모든 성능은 단일 토큰 예측(STP)으로 달성되었으며, 추측 디코딩(speculative decoding)이나 프리필-디코딩 분리(prefill-decode disaggregation)는 사용되지 않았다.
    2. DeepSeek R1 외에도 Kimi-K2.5 및 GPT-OSS와 같은 다른 모델들도 사용자당 약 1,400 토큰/초로 실행되었다.
    3. 모든 모델에서 Jalapeño의 GSM8k 평가는 엔비디아 칩과 동등한 결과를 달성했음을 확인했다.

### 1.4. 성능 측정의 주의사항 및 비교 대상
1. **성능 측정의 한계점**
    1. 모든 수치는 OpenAI가 제공한 것이다.
    2. InferenceX 실행은 현장에서 직접 검증했지만, InferenceX 벤치마크 전체를 실행하거나 AgentX 결과는 확인하지 못했다.
    3. AgentX는 실제 프로덕션 워크플로우의 캐시 동작을 반영하는 긴 컨텍스트 및 다중 턴 특성 때문에 칩 성능 비교에 선호되는 스위트이다.
    4. 8k1k에서 잘 작동하는 프레임워크도 라우터, 접두사 캐시 메커니즘, 캐시 관리, 오프로드 인프라 등과 같은 구성 요소를 강조하는 AgentX에서는 성능이 저하될 수 있다.

    <img alt="AgentX - InferenceXv3: CUDA Moat가 Agentic 추론에서 유지되는가?" src="https://substackcdn.com/image/fetch/$s_!wcB4!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a2e9df4-14a4-4a66-b4a1-468ed84f7411_1672x941.png" caption="AgentX - InferenceXv3: CUDA Moat가 Agentic 추론에서 유지되는가?">

2. **블랙웰(Blackwell)과의 비교의 불완전성**
    1. Blackwell과의 비교는 다소 불완전하고 불공평하다고 생각한다.
    2. Jalapeño는 HBM4를 사용하는 Rubin과 같은 칩과 실제로 경쟁해야 한다.
    3. Vera Rubin 시스템은 현재 고객에게 출하되기 시작했지만, OpenAI는 아직 Jalapeño의 엔지니어링 샘플 외에는 아무것도 가지고 있지 않다.
    4. 따라서 성능은 Blackwell이 아닌 Rubin과 비교해야 하며, 어떤 면에서는 Jalapeño와 같은 맞춤형 칩이 Blackwell을 능가할 것으로 예상된다.
    5. Vera Rubin NVL72는 GB200 NVL72보다 5.4배 높은 perf/MW를 제공한다.

    <img alt="Vera Rubin NVL72 vs GB200 NVL72? 추론 TCO 및 아키텍처 분석" src="https://substackcdn.com/image/fetch/$s_!5z34!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccebc7c4-9306-4810-9e0c-4307a95565cc_1024x577.png" caption="Vera Rubin NVL72 vs GB200 NVL72? 추론 TCO 및 아키텍처 분석">

3. **테스트 모델의 한계**
    1. 테스트된 모델들은 최신 개방형 모델이 아니다.
    2. 엔비디아와 AMD는 AgentX를 사용하여 DeepSeek V4 Pro 및 Kimi K3와 같은 더 큰 모델에 대한 결과를 발표했다.
    3. 모델이 크고 출시가 최근일수록 새로운 칩에서 구동하기가 더 복잡하다.
    4. 하지만 OpenAI가 Jalapeño에서 작동하는 모델들도 결코 작지 않다.

## 2. Jalapeño의 성능 분석 및 아키텍처
OpenAI의 Jalapeño 칩은 전력 효율성을 최우선으로 설계되었으며, 혁신적인 아키텍처와 소프트웨어 공동 설계를 통해 엔비디아 Rubin 칩과 비교해도 뛰어난 성능을 보여준다.

### 2.1. 전력 효율성(Perf/W) 중심 설계
1. **OpenAI의 설계 목표: Perf/W**
    1. OpenAI는 perf/W(와트당 성능)를 목표로 칩을 설계한다.
    2. 그 이유는 간단하다. OpenAI는 현재 예산이나 공간이 아닌 데이터센터 전력에 의해 제한되기 때문에 MW당 토큰 수가 가장 중요하다.
    3. 2026년 Computex에서 Jensen은 perf/W, 신뢰성, 긴 수명이 미래 GPU의 핵심 기능이라고 언급했다.
    4. 그는 "1기가와트의 전력이 있다면, 와트당 처리량이 곧 수익이다"라고 말했다.
    5. 또한 칩이 더 저렴하다는 이유만으로 잘못된 아키텍처를 선택하는 것은 의미가 없다고 덧붙였다.

    <img alt="Computex 2026 기조연설" src="https://substackcdn.com/image/fetch/$s_!UzoV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69dc13f6-ffb1-4d56-8df7-b75b57280382_1980x1254.png" caption="출처: Computex 2026 기조연설">

2. **데이터센터 전력 제약의 중요성**
    1. 엔비디아는 Hot Chips 2026의 Vera 강연에서 동일한 수익 그래프를 보여주며 "오늘날 데이터센터는 전력 제한적이다"라고 강조했다.
    2. 전력은 중요하며 수익을 창출한다.
    3. 운영자는 단순히 더 많은 MW를 얻을 수 없다. GPU 추가와 전력망 용량 추가는 매우 다른 시간 척도로 발생하기 때문이다.
    4. 데이터센터 전력 엔벨로프는 유틸리티 상호 연결, 인프라, 냉각 용량, UPS/백업 발전 설계와 같은 제약 조건을 가지고 있다.
    5. 전력망 지연은 하드웨어 및 건설 일정을 반복적으로 앞지르며, BtM(behind-the-meter) 전력 용량, 즉 데이터센터 자체에 구축되고 위치한 가스 터빈 및 현장 발전기의 필요성을 증대시킨다.
    6. 이 용량은 공공 전력망에서 끌어오는 것이 아니라 유틸리티 미터 뒤에 위치한다.
    7. 이를 통해 운영자는 전력망 상호 연결 및 유틸리티 업그레이드를 기다리지 않고 시설에 전력을 공급할 수 있으며, 이는 xAI의 Colossus 2가 실제 전력망 연결이 훨씬 뒤처져 있음에도 불구하고 BtM에 크게 의존하는 이유이다.
3. **Jalapeño의 Rubin 대비 성능 우위**
    1. X 게시물에서 언급했듯이, tok/s/MW는 와트가 초당 줄(joule)이므로 줄당 토큰으로 환원된다.
    2. 이는 tok/s/MW가 시스템의 효율성과 에너지를 토큰으로 변환하는 능력을 나타낸다는 것을 의미한다.
    3. 이 면에서 Jalapeño는 Rubin과 비교해도 우위를 점한다.
    4. OpenAI의 Jalapeño는 엔비디아와 CoreWeave가 7월에 발표한 Vera Rubin의 MTP(Multi Token Prediction) 결과를 능가하는 STP(Single Token Prediction) 출력 토큰 처리량/MW를 달성한다.
    5. 또한 GB200의 2025년 MTP 결과도 훨씬 초과한다.
    6. Vera Rubin 기사에서 언급했듯이, VR은 2025년 GB200 결과와 비교되었는데, 이는 유사한 초기 가동 단계였고, 2025년 GB200과 비교하는 것이 소프트웨어 성숙도를 일정하게 유지하기 위함이었다.
    7. 이 논리에 따라 Vera Rubin의 최신 2026년 7월 결과, GB200 2025년 결과, 그리고 현재의 Jalapeño 결과를 비교한다.
    8. 이는 이들이 최고의 공개 Rubin 수치이고, OpenAI가 Rubin 이후에 칩을 테이프아웃했기 때문에 매우 유효한 비교이다.
    9. OpenAI와 Rubin 모두 아직 미성숙하므로 성능은 계속 향상될 것이다.

    <img alt="Jalapeño, Vera Rubin, GB200의 토큰 처리량/MW 비교" src="https://substackcdn.com/image/fetch/$s_!EEpe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e8f9fd2-ec7f-45fa-80b9-dc132e32c661_2048x1450.png" caption="출처: OpenAI, SemiAnalysis">

### 2.2. TCO(총 소유 비용) 및 아키텍처 설계 철학
1. **TCO(총 소유 비용) 경쟁력**
    1. perf/TCO(총 소유 비용당 성능) 측면에서 Vera Rubin과 Jalapeño는 거의 동일한 출력 토큰 수를 생성하며 대등하다.
    2. 그러나 Jalapeño의 결과는 추측 디코딩 없이 얻어진 반면, Vera Rubin의 결과는 추측 디코딩을 사용한다.
    3. 추측 디코딩은 토큰당 비용을 약 3~5배 절감시킨다.
    4. Jalapeño에 추측 디코딩이 구현되면 토큰을 훨씬 더 비용 효율적으로 제공할 수 있을 것이다.
    5. 물론 이러한 TCO 이점의 일부는 엔비디아의 높은 마진을 브로드컴의 낮은(여전히 높지만) 마진으로 교환하는 데서 비롯된다.
    6. 하지만 이것이 전부는 아니다.
    7. 예를 들어, Meta와 Microsoft의 AI ASIC 프로그램이 훨씬 더 오래 노력했음에도 불구하고 성공하지 못한 것은 비용이 방정식의 한 부분일 뿐임을 보여준다.
2. **프리필-디코딩 분리(PDD) 미사용**
    1. 아키텍처적으로 OpenAI는 별도의 칩 풀에 프리필 및 디코딩(PD)을 분리하지 않기로 결정했다.
    2. 드래프트 모델과 메인 모델은 동일한 칩과 패브릭을 공유하는데, 이는 이론적인 효율성 일부를 실용적인 운영과 교환하는 설계 철학이다.
    3. 이러한 동기는 워크로드 혼합이 시간이 지남에 따라 변하기 때문이다. 예를 들어, 모델의 세 가지 시대(지식, 추론, 에이전트)를 거치면서 입력 대 캐시 쓰기 대 캐시 읽기 대 출력 토큰의 비율이 크게 변했다.
    4. 따라서 이기종 프리필 실리콘과 디코딩 실리콘의 고정된 양을 미리 선택하면 시간이 지남에 따라 비효율성이 발생할 수 있다.
    5. OpenAI는 이 아키텍처에서 균일한 풀을 선택하고 모든 시나리오에서 칩이 잘 작동하도록 노력한다.

### 2.3. Jalapeño의 모델별 성능 및 개발 속도
1. **Kimi K2.5 모델 성능**
    1. Jalapeño는 Kimi K2.5(Cursor Composer 2.5의 기반)에서 사용자당 거의 700 토큰/초에 도달하며, 사용자당 100 토큰/초를 기록한 다음으로 성능이 좋은 칩보다 9배 이상 빠르다.

    <img alt="Kimi K2.5 모델에서 Jalapeño의 성능 비교" src="https://substackcdn.com/image/fetch/$s_!yoRC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3088f64c-9bee-46d9-a445-6818248ba573_2048x1366.png" caption="출처: OpenAI, SemiAnalysis">

2. **GPT-OSS 모델 성능**
    1. GPT-OSS에서도 Jalapeño는 압도적인 성능을 보여준다.
    2. Jalapeño의 iso-interactivity 처리량/MW는 GB200의 최고 처리량 지점보다 거의 두 배 높고, GB200의 동시성 1 지점보다 50배 이상 높다.
    3. Jalapeño의 높은 동시성 지점은 EP8을 사용한다.

    <img alt="GPT-OSS 모델에서 Jalapeño의 성능 비교" src="https://substackcdn.com/image/fetch/$s_!CW1w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f245dd7-c6b7-48a3-9215-3976633bb77f_2048x1366.png" caption="출처: OpenAI, SemiAnalysis">

3. **성능 결과에 대한 추가 고려사항**
    1. 이러한 결과는 인상적이지만, 8k1k 워크로드에 대한 것이며 AgentX 실행은 아직 없다는 점을 고려해야 한다.
    2. AgentX 기사에서 언급했듯이, 다중 턴, 긴 컨텍스트 워크로드는 라우터 및 접두사 캐시와 같은 서빙 스택의 더 많은 측면을 강조한다.
    3. 에이전트 워크로드에서 탁월한 성능을 발휘하려면 더 많은 최적화가 필요하다.

    <img alt="AgentX - InferenceXv3: CUDA Moat가 Agentic 추론에서 유지되는가?" src="https://substackcdn.com/image/fetch/$s_!wcB4!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a2e9df4-14a4-4a66-b4a1-468ed84f7411_1672x941.png" caption="AgentX - InferenceXv3: CUDA Moat가 Agentic 추론에서 유지되는가?">

### 2.4. Jalapeño의 세부 사양 및 아키텍처
1. **Jalapeño의 개발 단계 및 성능 향상**
    1. 이 모든 결과는 Jalapeño 프로그램 시작 9개월 만에 A0 스테핑에서 수집되었다.
    2. 현재 B0 스테핑이 제조 중이며, 이는 초기 A0 실리콘보다 약 25%의 와트당 성능 향상을 제공하는 최적화를 포함한다.
    3. 특히 B0 스테핑은 TSMC의 N3P에서 제조된 단일 레티클 크기 컴퓨팅 다이에서 13.4 PFLOPs의 MXFP4를 제공한다.
    4. 이는 유사한 크기와 동일한 노드에서 17.5 PFLOPs의 밀집 Rubin NVFP4를 제공하는 단일 Rubin 컴퓨팅 다이와 비교된다.
    5. Jalapeño의 TDP는 700W에 불과하며, Rubin의 900-1,150W/컴퓨팅 다이와 비교하면 더욱 인상적이다.
    6. Jalapeño가 훈련보다는 추론에 중점을 두기 때문에 FLOPs를 최대화하기 위해 TDP를 높일 필요가 없다는 점은 이해할 수 있지만, 그럼에도 불구하고 Jalapeño는 상당한 이론적 최대 FLOPs를 제공한다.
2. **HBM 대역폭 및 FLOPs/W 비교**
    1. 다른 가속기와 직접 비교했을 때, Jalapeño는 와트당 HBM 대역폭과 와트당 FLOPs가 가장 높으며, 1,800W Rubin Max-Q 구성과 비교할 만하다.

    <img alt="Jalapeño의 HBM 대역폭 및 FLOPs/W 비교" src="https://substackcdn.com/image/fetch/$s_!4mJM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5795c45-d23b-403c-8bc4-f13d5ba6fb45_2048x394.png" caption="출처: SemiAnalysis">

3. **I/O 및 HBM4 채택**
    1. 오프패키지 I/O는 컴퓨팅 패브릭을 위한 32레인 800G SerDes를 갖춘 N3E I/O 칩렛에 의해 제공된다.
    2. 이 중 24레인(600GB/s)은 랙 내 로컬 스케일업에 사용되고, 8레인(200GB/s)은 2,048 XPU 멀티랙 도메인인 글로벌 스케일업에 사용된다.
    3. PCIe Gen 5는 x86 호스트 CPU에 연결하기 위한 시스템 I/O로 사용된다.
    4. Jalapeño는 HBM4와 함께 출시될 예정이며, 이는 엔비디아와 AMD에 이어 비교적 초기 채택자 중 하나가 될 것이며, 기존 TPU 및 Trainium 프로그램을 능가한다.
    5. Jalapeño의 핵심 아키텍처 원칙 중 하나가 HBM 대역폭을 최대한 활용하는 것이므로, 최고의 HBM이 아닌 다른 것을 선택하는 것은 그 목표에 역행할 것이다.
    6. 그 결과 패키지당 15.4TB/s의 메모리 대역폭을 제공하며, 이는 HBM3E를 사용하는 다른 모든 가속기를 능가한다.
    7. 15.4TB/s 대역폭은 HBM4가 10Gbps 핀 속도를 달성할 수 있음을 보여주며, 이는 Rubin에서 엔비디아가 HBM4에서 얻는 9.6Gbps보다 약간 우위에 있다.
    8. HBM은 삼성에서 제공될 가능성이 높다.

    <img alt="Jalapeño의 HBM 대역폭" src="https://substackcdn.com/image/fetch/$s_!ZdtW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d7d181a-2bb9-45d4-bd67-2f7e525ce6d1_1426x376.png" caption="출처: OpenAI">

4. **빠른 개발 속도와 소프트웨어 스택**
    1. OpenAI는 2025년 11월에 Jalapeño를 테이프아웃했으며, 이는 단순히 상단 다이 실리콘이 아닌 CoWoS 설계의 테이프아웃이었다.
    2. 2025년 11월 테이프아웃 후 9개월 이내, 실제 실리콘 가동 3개월 만에 OpenAI는 Jalapeño로 매우 좋은 결과를 달성했다.
    3. 팀이 소프트웨어 스택을 처음부터 시작했다는 점을 고려하면 더욱 인상적이다.
    4. 반면 Rubin의 CoWoS 테이프아웃은 한 달 빠른 2025년 10월에 완료되었지만, 우리가 본 초기 결과는 CoreWeave의 엔지니어링 샘플뿐이다.
    5. 엔비디아는 OpenAI처럼 벤치마크를 테스트하고 공개하도록 허용하지 않았는데, 이는 칩 소프트웨어가 아직 미성숙하다는 것을 나타낸다.
    6. OpenAI가 새로운 모델을 실리콘에 빠르게 적용할 수 있다는 점을 고려할 때, CUDA 해자(moat)는 잠재적으로 사라질 수 있다.
    7. 아직 최적화되지 않았음에도 불구하고 Jalapeño는 일반적으로 더 나은 수치를 제공했다.
    8. 엔비디아 하드웨어가 열등하다고 생각하지 않지만, Jalapeño의 소프트웨어 가동이 엔비디아보다 빠르게 진행되었다고 본다.
    9. 이는 하드웨어/소프트웨어 공동 설계의 힘을 보여주며, 이는 뛰어난 프론티어 AI 랩 ASIC 팀이 기존 상용 실리콘 플레이어를 능가할 수 있는 주요 영역이다.
    10. 역설적으로, 처음부터 시작하는 것이 OpenAI에게 이점이 되었을 수도 있다. 이전 버전과의 호환성이나 오래된 소프트웨어 버전에 대해 걱정할 필요 없이 깨끗한 아키텍처 결정을 내릴 수 있었기 때문이다.
5. **생산 계획 및 Rubin과의 비교**
    1. OpenAI는 Jalapeño의 엔지니어링 샘플을 보유하고 있지만, 생산은 2027년 내내 점진적으로 확대될 예정이며, 대부분의 생산량은 내년 말에 예정되어 있다.
    2. Jalapeño는 실제 대량 생산 ASIC이다.
    3. Rubin의 타임라인과 비교했을 때, Jalapeño의 개발 속도는 놀랍도록 빠르다.
    4. 앞서 보여주었듯이, Rubin이 먼저 시작했음에도 불구하고 Jalapeño의 결과는 Rubin을 능가한다.

    <img alt="Jalapeño와 Rubin의 개발 타임라인 비교" src="https://substackcdn.com/image/fetch/$s_!d3_z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb59cacc-1f16-4c6a-98a5-0f0db74dada7_2048x411.png" caption="출처: SemiAnalysis">

6. **Jalapeño 아키텍처의 특징**
    1. Jalapeño 칩의 매트릭스 엔진은 TPU와 유사하게 MXFP 숫자 형식과 가중치 고정 시스톨릭 배열을 사용한다.
    2. 그러나 TPU와 직접 비교했을 때, 더 작은 형태/차원을 지원하여 더 큰 시스톨릭 배열에서 어색한 형태의 행렬 곱셈으로 인해 발생하는 이상한 성능 저하를 방지한다.
    3. 또한 64비트 스칼라 코어와 FP32/INT32 벡터 코어를 갖추고 있다.
    4. OpenAI는 트레이 수준에서 이중화를 투자했으며, 코어 및 채널 수준에서 수율 확보 기능을 내장했다.
    5. AI 지원 칩 설계가 SIMD 영역을 8%, 매트릭스 엔진 영역을 10% 감소시켰다고 주장한다.
    6. 정확한 공정/전압/온도(PVT) 조건은 명확히 밝히지 않았지만, AI 지원 블록이 초기 블록보다 타이밍과 전력을 개선했다고 언급했다.
    7. Jalapeño 아키텍처 설계는 KVCache 및 가중치의 메모리 이동과 고정된 지연 시간 및 오버헤드를 제거하는 데 중점을 둔다.
    8. 이는 다른 가속기와 비교하여 작은 배치 또는 형태에서도 원시 최대 FLOPs/대역폭에 더 가까워질 수 있도록 한다.
    9. 코어와 HBM은 슬라이스로 나뉘며, 각 코어 슬라이스는 자체 HBM 슬라이스에 대한 낮은 지연 시간 로컬 뷰를 갖는다.
    10. 슬라이스 간 동기화는 고대역폭 전용 집합 네트워크에서 발생한다.
    11. 이러한 최소한의 메모리 계층 구조는 Jalapeño에게 GPU에 비해 큰 잠재적 이점을 제공한다. GPU에서는 메모리 액세스가 복잡한 메모리 시스템을 통과해야 하므로 큰 지연 시간이 발생하고, 이는 더 큰 형태에서 상쇄되거나 숨겨져야 한다.
    12. 이러한 선택은 가중치와 KV의 신중한 배치로 코어 간 동기화를 텐서 병렬 통신과 같이 제한적이고 알려진 고대역폭 통신으로 제한할 수 있기 때문에 가능하다.

    <img alt="Jalapeño의 아키텍처 다이어그램" src="https://substackcdn.com/image/fetch/$s_!VVEK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F871631ee-8f0d-4fb6-869c-a6fb298e800e_2048x832.png" caption="출처: OpenAI">

7. **단순화된 NoC 및 메모리 서브시스템**
    1. 일반적인 통신 및 스케일업 네트워크 액세스에 사용되는 추가적인 일반 NoC(Network-on-Chip)도 있다.
    2. 일반적으로 OpenAI는 단순화된 NoC 및 메모리 서브시스템을 통해 엔비디아 및 구글에 비해 엄청난 전력을 절약하고 큰 성능 향상을 얻는다.

    <img alt="Jalapeño의 NoC 및 메모리 서브시스템" src="https://substackcdn.com/image/fetch/$s_!-R_1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f93df86-2ea2-4904-8fd1-e0e5eff4b410_1638x854.png" caption="출처: OpenAI">

8. **코어 아키텍처 및 성능 최적화 전략**
    1. 코어 수준에서 OpenAI는 L1 캐시를 갖춘 OoO(Out-of-Order) 코어를 설명한다.
    2. 이는 다른 가속기에서 볼 수 있는 패턴과 크게 다르다. 다른 가속기들은 일반적으로 비동기 DMA 지원과 함께 소프트웨어 관리 스크래치패드를 사용한다.
    3. 여기서 주장하는 바는 Jalapeño가 시작 지연 시간, 장벽 지연 시간, 메모리 시스템 지연 시간과 같은 고정된 오버헤드를 피할 수 있게 하여, 코어당 더 많은 작업을 통해 상쇄되거나 숨겨져야 하는 다른 가속기(예: GPU)에 비해 작은 배치 또는 형태에서도 원시 최대 대역폭/FLOPs에 더 가까워질 수 있도록 한다는 것이다.
    4. 단점은 Jalapeño가 메모리 요청의 적시 도착을 보장하기 위해 우수한 프리페칭에 의존한다는 것이다. 이는 예측하기 어렵고 추론하기 더 어렵다.
    5. 그러나 상세한 추적에 접근할 수 있는 좋은 하네스에 Codex가 있다면, 주어진 형태에 대한 최상의 프리페칭을 가진 최적의 커널을 찾는 데 인간의 개입이 거의 필요하지 않을 것이다.
    6. OpenAI가 DeepSeek R1, Kimi K2.5, GPT-OSS를 그렇게 빠르게 가동시킨 것이 바로 이 방법이라고 생각한다.
    7. 코어는 또한 "작은" 매트릭스 차원을 지원한다. 이는(얼마나 작은지에 따라) 다양한 모델 및 배치 차원에 걸쳐 더 일반적이며, 매트릭스 차원 정렬, 패딩 오버헤드 및 타일링 비효율성에 덜 민감하게 만든다.
    8. 예를 들어, TPU, Trainium 및 Etched 칩은 매우 큰 시스톨릭 배열을 가지고 있어 타일링 비효율성을 피하기 위해 큰 배치 또는 정확히 나눌 수 있는 모델 차원이 필요할 수 있다.
    9. Jalapeño를 통해 OpenAI는 파레토 곡선의 모든 영역에서 가능한 한 루프라인 성능에 가깝게 도달하기 위해 시스템의 고정된 지연 시간을 제거하는 데 중점을 두었다.
    10. 이론적으로 이는 여러 작동 지점에서 GPU에 비해 이점을 제공할 수 있다.
        1. 낮은 지연 시간/작은 배치 추론에서 훨씬 더 나은 상한 성능을 제공한다. GPU에서는 시작 지연 시간, 장벽 지연 시간, 메모리 시스템 지연 시간과 같은 많은 고정된 오버헤드에 의해 제한된다.
        2. 큰 배치 또는 긴 컨텍스트에서도 하드웨어 루프라인에 더 가까워질 수 있는 잠재력을 제공한다.
    11. 이는 이론적으로 상한 성능을 사용할 수 있더라도 실제 커널에 대해 해당 성능을 실현하기가 더 어려울 수 있다는 단점이 있다.
    12. 따라서 접근 방식은 다음과 같다.
        1. 모든 워크로드 형태에서 가장 높은 상한 성능을 목표로 설계한다.
        2. Codex가 상한을 달성하는 커널을 찾는 지루한 작업을 수행하도록 한다.
    13. OpenAI 팀이 Jalapeño에서 InferenceX 워크로드를 매우 빠르게 가동시킨 것을 보면, 이 접근 방식에 대해 낙관적이다.
    14. Jalapeño가 성공한다면, 이는 프로그래밍 모델과 완벽하고 보편적인 컴파일러에 대한 업계의 집착이 프론티어 AI 모델에 의해 무효화된다는 강력한 신호가 될 것이다.

## 3. Jalapeño의 소프트웨어 및 시스템 아키텍처
OpenAI의 Jalapeño 칩은 Codex와 Gluon을 활용한 혁신적인 소프트웨어 스택을 통해 빠른 개발 속도와 높은 성능을 달성하며, 데이터센터 운영 효율성을 극대화하기 위한 시스템 아키텍처를 채택하고 있다.

### 3.1. Jalapeño의 소프트웨어 스택
1. **Codex를 활용한 커널 개발**
    1. OpenAI는 Jalapeño 커널을 어셈블리처럼 작성한다.
    2. 각 커널은 수천 줄에 달하는 수동 튜닝된 코드를 가지며, 정확성 검사와 맞춤형 새니타이저의 지원을 받는다.
    3. 초기 커널 작업은 완전 자동화보다는 인간 개입 방식이었지만, OpenAI가 기업 고객에게 제공할 계획인 확장된 내부 버전의 Codex를 사용하면서 변화했다.
    4. 내부 서빙 엔진은 "Teacup"이라고 불린다.
    5. 흥미롭게도 OpenAI는 InferenceX로 DeepSeek을 벤치마킹하기 전까지 MLA 커널의 내부 구현이 없었다.
    6. OpenAI의 커널 엔지니어링 팀의 개입 없이 Codex가 기능적이고 효율적인 커널을 그렇게 빠르게 작성할 수 있는 능력은 소프트웨어 파이프라인의 개발 능력을 보여준다.
2. **Gluon 프로그래밍 언어**
    1. OpenAI는 Gluon으로 Jalapeño를 프로그래밍한다.
    2. Gluon은 OpenAI의 커널 프로그래밍 언어이다.
    3. Triton 위에 구축된 Gluon은 Triton의 SPMD(Single Program Multiple Data) 프로그래밍 모델을 유지하면서도 저수준 프로그래밍 추상화를 노출한다.
    4. 예를 들어, 엔비디아 GPU의 경우 MMA 명령어, TMA 명령어, mbarrier 메커니즘 등 PTX 명령어에 매핑되는 API를 제공한다.
    5. Gluon이 제공하는 가장 독특한 추상화는 레이아웃이다.
    6. 일반적으로 레이아웃은 하드웨어 리소스(예: 워프 9의 5번째 레지스터)와 텐서 요소(예: 6행 7열의 텐서 요소) 간의 매핑을 정의한다.
    7. Gluon의 레이아웃 추상화는 OpenAI가 발명한 레이아웃 대수학의 한 유형인 선형 레이아웃(Linear Layouts)을 기반으로 한다.
    8. 선형 레이아웃은 레이아웃이 무엇인지 수학적으로 형식화하고 레이아웃에 대한 연산을 수행하는 도구를 제공한다.
    9. 이를 통해 증명 가능한 정확한 레이아웃 변환 및 최적의 메모리 스위즐링과 같은 많은 기능을 사용할 수 있다.
    10. Jalapeño의 프로그래밍 모델 측면에서 각 Gluon 프로그램은 영구 스레드에 매핑된다.
    11. 이는 Jalapeño가 영구 커널 프로그래밍 패턴에 적합하다는 것을 시사한다. 이 패턴에서는 각 프로그램이 여러 타일에서 실행되며, 하드웨어 스케줄러가 아닌 프로그래머가 작업을 할당한다.
    12. OpenAI는 레이아웃을 명시적으로 인코딩하는 추상화인 TensorInfo를 언급했다.
    13. 이는 선형 레이아웃으로 구동될 Jalapeño용으로 설계된 레이아웃 세트일 가능성이 높다.
    14. 마지막으로, 각 코어는 데이터 프리페칭 및 분리된 비순차 실행(out-of-order) 장치를 제공한다.
    15. 예를 들어, 사용자는 세마포어 뒤에 잠긴 프리페치된 데이터에 대한 대기를 프로그래밍할 수 있다.
3. **CUDA 해자(Moat)에 대한 위협**
    1. 아이러니하게도 현재 엔비디아 GPU에서 실행되는 GPT 5.6 Sol과 같은 OpenAI 모델은 CUDA 해자에 실제 위협이 되는 칩을 설계하는 데 사용되었다.
    2. 엔비디아 자체 GPU가 잠재적인 후계자를 실시간으로 도입하는 데 도움을 주고 있는 것이다.
4. **Jalapeño의 빠른 개발 속도**
    1. 시간 경과에 따른 비교를 통해 Jalapeño의 개발 속도를 확인할 수 있다. 2주도 안 되는 기간에 특정 상호작용성에서 2배 이상의 처리량 개선을 달성했다.

    <img alt="Jalapeño의 개발 속도에 따른 처리량 개선" src="https://substackcdn.com/image/fetch/$s_!LMc_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb38d958b-6d53-4ebe-b92f-c2cb58de05c2_2048x1485.png" caption="출처: OpenAI, SemiAnalysis">

    2. 커널 성능이 향상되었을 뿐만 아니라, 8일 만에 Jalapeño 팀은 이전 TP8 구성에서 확장하여 TP32를 활성화하고 단일 시스템을 넘어 대규모 모델에서 전체 랙 규모 구성을 실행했다.
    3. 이는 정말 인상적인 개발 속도이다.

    <img alt="Jalapeño의 TP32 활성화 및 랙 규모 구성" src="https://substackcdn.com/image/fetch/$s_!hCdt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa18d5611-f7c1-4e34-8919-99b1c683054f_2048x1485.png" caption="출처: OpenAI, SemiAnalysis">

5. **시뮬레이터 및 데모**
    1. 실제 하드웨어 실행에 앞서 성능을 검증하기 위해 OpenAI는 측정된 하드웨어와 5% 이내의 정확도를 가진 시뮬레이터 "chilisim"을 보유하고 있으며, 고정 폭 추적 버스를 사용한다.
    2. A0에서의 추적은 제한적이었지만, B0에서는 A0 실리콘의 실제 실행 입력으로 인해 크게 개선되었다.
    3. 엔지니어들은 내부 모델인 "Raiku" 또는 "5.3 Codex Spark"를 1.2ms TPOT로 실행하는 Codex CLI를 시연했다.
    4. 팀은 또한 칩에서 직접 실행되는 Codex로 작성된 데모를 선보였다. 36 FPS의 Doom, FP32 유체 역학 시뮬레이션, "Liquid Light" 마우스 드래그 시각화 등이 있다.

    <img alt="Codex로 작성된 Jalapeño 칩 데모" src="https://substackcdn.com/image/fetch/$s_!U08h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd410878f-5f19-40bd-ad2c-d92ad45d65a9_1252x1232.png" caption="출처: SemiAnalysis">

6. **모델 측면의 접근 방식**
    1. 모델 측면에서 OpenAI의 내부 메가커널 접근 방식인 "기가커널"은 CPU 오버헤드와 시작 시간을 줄이기 위해 온디바이스에서 루프를 도는 단일 메가커널을 중심으로 구축된다.
    2. 팀은 또한 테스트 시간 컴퓨팅 전략에 더 집중하고 있으며, 특히 100만 롤아웃을 일관되게 사용하는 방법에 관심을 가지고 있다.

### 3.2. 프리필-디코딩 분리(PDD) 미사용 이유
1. **PDD의 매력과 한계**
    1. OpenAI가 이 칩에서 프리필-디코딩 분리(PDD)를 사용하지 않는다는 점은 놀라웠다. 엔비디아와 AMD GPU 성능은 균일한 하드웨어에서도 PDD로부터 상당한 이점을 얻기 때문이다.
    2. PDD는 워크로드가 고정되어 있을 때 매력적으로 보인다.
    3. 프리필과 디코딩은 하드웨어를 다르게 스트레스 주기 때문에 각 단계를 별도로 튜닝된 풀에 할당하면 선택된 입력/출력 비율에서 효율성을 향상시킬 수 있다.
    4. 그러나 실제 트래픽은 그 비율을 유지하지 않는다.
    5. 입력 및 출력 시퀀스 길이, 동시성, 캐시 적중률, 추측 수용률, 지연 시간 목표는 하루 종일 변동한다.
    6. 장치가 프리필 및 디코딩 풀로 나뉘면, 프리필 수요가 너무 많으면 요청이 대기하는 동안 디코딩 칩이 유휴 상태가 된다.
    7. 그러나 디코딩 수요가 너무 많으면 그 반대가 된다.
    8. 운영자는 이상적인 비율이 항상 변하는 시스템에서 올바른 분할을 지속적으로 예측하고, 양쪽에 예비 용량을 프로비저닝하고, 시스템의 균형을 재조정해야 한다.
    9. 통합 시스템에서는 특정 단계에서 일부 리소스가 충분히 활용되지 않을 수 있지만, 모든 장치는 다음 요청을 처리할 수 있다.
    10. 분리된 시스템에서는 단순히 잘못된 풀에 속해 있기 때문에 전체 칩이 유휴 상태로 있을 수 있다.
    11. 로컬 활용도는 더 좋아 보이지만, 글로벌 활용도는 나쁠 수 있다.

    <img alt="프리필-디코딩 분리(PDD)의 비효율성" src="https://substackcdn.com/image/fetch/$s_!uPh7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92d363ab-c391-4b9a-9f67-516dac22f534_1364x938.png" caption="출처: SemiAnalysis">

2. **PDD로 인한 지역성(Locality) 손실**
    1. 분리는 또한 지역성을 깨뜨린다.
    2. 프리필 워커는 디코딩 워커가 즉시 필요로 하는 큰 KV 캐시를 생성하므로, 시스템은 생성이 계속되기 전에 해당 상태를 네트워크를 통해 전송해야 한다.
    3. 이는 대역폭 소비, 동기화, 대기열 및 또 다른 장애 도메인을 추가한다.
    4. KV 캐시가 증가하기 때문에 입력 시퀀스 길이에 따라 비용도 증가한다.
    5. 그러나 KV 이동을 피하는 것은 주로 전력 및 지연 시간 최적화이다. 일부 KV를 이동할 의향이 있다면 일부 전력 및 요청당 지연 시간을 희생하면서 하드웨어 활용도를 높일 수 있다.

    <img alt="프리필-디코딩 분리(PDD)로 인한 KV 캐시 이동" src="https://substackcdn.com/image/fetch/$s_!q86J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5789e0ea-2d0d-4924-b338-f0559c7e7ee9_1928x1292.png">

3. **유연한 시스템의 이점**
    1. 대체 가능한(fungible) 플릿은 지연 시간에 민감한 요청과 처리량 중심의 배치 간에 용량을 전환하는 반면, 고정된 분할은 트래픽 혼합이 변경될 때마다 하드웨어를 유휴 상태로 둔다.
    2. 또한 컨텍스트 길이는 어텐션(attention) 작업과 FFN(Feed-Forward Network) 작업 간의 균형을 변화시켜, 어떤 고정된 하드웨어 비율도 설계 지점 근처에서만 효율적이게 만든다.

    <img alt="유연한 시스템과 고정된 분할 시스템의 비교" src="https://substackcdn.com/image/fetch/$s_!l0lN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f3a37f8-0996-4dea-9631-02ade61d7fae_1358x938.png" caption="출처: SemiAnalysis">

4. **추측 디코딩(Speculative Decoding)과의 관계**
    1. 동일한 제약 조건이 추측 디코딩에도 적용된다.
    2. 드래프트 모델은 검증자에게 후보 토큰을 극도로 낮은 지연 시간으로 공급해야 한다.
    3. 두 모델을 특화된 풀로 분리하면 긴밀하게 결합된 디코딩 루프가 분산 프로토콜로 변환된다.
    4. 추가적인 통신 및 조정은 드래프팅으로 절약된 지연 시간을 소모할 수 있다.
    5. 두 모델을 동일한 장치와 낮은 지연 시간 패브릭에 유지하면 추측을 가치 있게 만드는 지역성이 보존된다.

    <img alt="추측 디코딩과 지역성" src="https://substackcdn.com/image/fetch/$s_!n0nI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2eb19374-5a08-4d82-84a3-9875b3fc0f5b_1980x1220.png" caption="출처: SemiAnalysis">

    6. 그러나 분리는 수요가 충분히 크고 안정적이며 예측 가능할 때, 특히 기존 GPU가 좋은 처리량에 도달하기 위해 대규모 단계별 배치가 필요할 때 여전히 승리할 수 있다.
    7. 하지만 이는 공짜 점심이 아니다.

### 3.3. Jalapeño 랙 시스템 아키텍처
1. **랙 유닛 구성**
    1. 랙 유닛 수준에서 Jalapeño 시스템은 CPU 호스트 랙과 ASIC 랙으로 구성된다.
    2. 호스트 랙에는 "Katsu"라고 불리는 16개의 호스트 CPU 트레이가 있으며, 각각은 "Vindaloo"라고 불리는 16개의 ASIC 트레이에 해당한다.
    3. 각 호스트에는 1.5TB DRAM, 2x E1.S, 2x M.2 SSD를 갖춘 2개의 Turin급 AMD EPYC CPU가 장착되어 있다.
    4. 각 트레이는 또한 400G(2x200G) 프론트엔드 네트워킹 사양을 갖추고 있다.
    5. 각 Katsu 트레이는 랙 전면을 가로지르는 8개의 외부 PCIe DAC 케이블을 통해 각 Vindaloo 트레이에 연결된다.
    6. 시스템 수준 설계는 Celestica와 협력하여 이루어졌다.
2. **ASIC 랙 구성**
    1. ASIC 랙은 16개의 Vindaloo 트레이와 8개의 스케일업 스위치 트레이(로컬용 6개 + 글로벌용 2개)로 구성되며, 이들은 "Chana"라고 불린다.
    2. 각 Vindaloo 트레이는 8개의 Jalapeño ASIC으로 구성되어 랙당 총 128개의 Jalapeño ASIC을 이룬다.
    3. ASIC은 엔비디아의 Oberon과 마찬가지로 구리 케이블 백플레인을 통해 Chana 스위치 트레이에 연결된다.
    4. 스케일업 토폴로지는 랙 내 128개 ASIC을 연결하는 로컬 도메인과 최대 16개 랙 또는 2,048개 ASIC을 연결하는 글로벌 도메인으로 나뉜다.
    5. 사이드카 호스트 랙에 대한 전력 공급은 약 50kW(생산 시 31kW)가 필요하며, ASIC 랙은 130kW를 소비하여 총 2개 랙 시스템은 약 160kW를 소비한다.
    6. 이는 전력 소비 측면에서 기본적으로 이중 폭 GB300 랙과 유사하다.

    <img alt="Jalapeño 랙 시스템 아키텍처" src="https://substackcdn.com/image/fetch/$s_!uzLk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F596ca531-3bde-44fa-8d1b-34d04b8cc6b8_1304x1382.png" caption="출처: SemiAnalysis, OpenAI">

3. **스케일업 네트워크 구성**
    1. OpenAI는 단일 스케일업 네트워크 내에서 최대 2,048개의 Jalapeño XPU를 연결할 수 있다.
    2. 스케일업 네트워크는 두 개의 도메인으로 구성된다.
        1. 랙 내에서 128개의 XPU를 백플레인을 통해 연결하는 로컬 도메인
        2. 구리 및 광학 인터커넥트의 하이브리드를 사용하여 16개 랙에 걸쳐 2,048개의 XPU를 연결하는 글로벌 도메인
    3. 각 랙은 8개의 Chana 스위치 트레이로 구성된다.
    4. 중앙의 6개 Chana 스위치는 로컬 도메인용이며, 각각 102.4T Tomahawk 6 스위치 ASIC을 포함한다.
    5. 로컬 스위치 상단과 하단의 2개 Chana 스위치는 글로벌 도메인용이며, 이는 2개의 102.4T Tomahawk 6 스위치로 구성되어 스위치 트레이당 최대 204.8T를 이룰 수 있다고 생각한다.
    6. 로컬 도메인에서 128개의 Jalapeño 칩 각각은 XPU당 4.8Tb/s의 단방향 대역폭을 가지며, 6개의 102.4Tb/s Tomahawk 6 ASIC에 올투올(all-to-all) 방식으로 연결된다.
    7. 이는 XPU당 48개의 차동 쌍(DP) 수컷 및 암컷 커넥터 쌍에 해당하며, 로컬 스케일업에 사용되는 랙당 총 6,144개의 DP 수동 구리 케이블에 해당한다.
    8. 글로벌 도메인의 경우, 16개 랙의 총 2,048개 XPU는 구리 백플레인, 전기 204.8T TH6 스위치, 1.6T 트랜시버 및 광 회로 스위치의 조합을 통해 연결된다.
    9. 각 XPU는 글로벌 링크에 대해 1.6Tb/s의 단방향 대역폭을 가지며, 이는 XPU와 글로벌 스위치 간의 백플레인에 대해 XPU당 16개의 차동 쌍(DP) 수컷 및 암컷 커넥터 쌍에 해당한다.
    10. 각 글로벌 스위치 트레이(각각 2개의 ASIC)에서 나가는 대역폭은 백플레인과 전면 패널 광학 장치로 분할된다.
    11. 로컬 도메인과 글로벌 도메인 사이에서 랙당 백플레인 커넥터 수는 XPU당 64개의 DP와 랙당 총 8,192개의 DP 수동 구리 케이블에 달한다.
4. **글로벌 도메인 아키텍처**
    1. 글로벌 도메인은 8개의 레일로 구성된 레일 전용 아키텍처를 채택한다.
    2. OpenAI는 각 랙에 설치된 광 회로 스위치(OCS)를 통해 글로벌 도메인의 광학 링크를 라우팅한다고 생각한다.
    3. 각 XPU에 대해 1.6Tb/s의 글로벌 대역폭은 구리 백플레인을 통해 글로벌 스위치 트레이로 이동한다.
    4. 그런 다음 1.6T 트랜시버를 통해 전면 패널을 통해 스위치를 빠져나와 랙을 빠져나가기 전에 수동 광 스위치로 이동한다.
    5. 이는 128개 XPU로 구성된 16개 랙을 결합하여 스케일업 월드 크기를 2,048개 XPU로 확장한다.

    <img alt="Jalapeño의 글로벌 스케일업 네트워크" src="https://substackcdn.com/image/fetch/$s_!mFHS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae9b26b8-471a-43b2-a60c-cd99ce2b9b07_3480x1342.png" caption="출처: SemiAnalysis">

5. **향후 계획 및 배포**
    1. 스케일업 네트워킹은 전체 시스템 비용의 약 10%에 불과하므로, 이러한 유연성은 미래의 10~20조 매개변수 모델 또는 200~400만 토큰 컨텍스트 창에 대한 귀중한 선택권을 제공한다.
    2. 배포 측면에서 OpenAI는 네오클라우드와 협력하고 있으며, 1월까지 데이터센터 파트너와 함께 신뢰성 데이터를 수집하고 도크-투-랙(dock-to-rack) 출시 시간을 최적화하고 있다.

### 3.4. Jalapeño의 미래와 시장 영향
1. **Jalapeño의 다음 목표**
    1. Jalapeño의 첫 번째 생산 토큰이 곧 출시될 예정이다.
    2. 다음 목표는 100MW이며, 주요 장애물은 대부분 하드웨어 관련이다.
    3. 즉, 얼마나 많이 생산할 수 있는지, 데이터센터를 얼마나 잘 배포하고 운영할 수 있는지, 모니터링 및 복원력을 어떻게 처리하는지 등이다.
    4. 소프트웨어는 이미 입증되었으며, 내부 모델을 통해 모든 소프트웨어 선점은 쉽게 따라잡을 수 있다.
2. **NVIDIA, AMD, Cerebras에 대한 영향**
    1. 유료 콘텐츠에서는 향후 몇 년 동안 엔비디아, AMD, Cerebras 및 OpenAI와 계약을 체결한 다른 칩 회사에 대한 영향을 논의할 예정이다.
    2. 또한 가속기 모델에서 차세대 칩의 생산량, 단위 및 타임라인을 다룬다.
