---
title: "Rubin NVL72 Agentic Inference: 67x better Performance per Dollar"
origin: lilys_ai
lilys_project_id: 11421783
lilys_project_url: "https://lilys.ai/digest/11421783"
lilys_created_at: "2026-09-20T04:20:22.671Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13489811"
sources:
  - id: "12331611"
    url: "https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference"
    title: "Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar"
    status: "done"
---

# Rubin NVL72 Agentic Inference: 67x better Performance per Dollar

## LilysAI note

> Vera Rubin NVL72의 에이전트 추론 성능은? **블랙웰(Blackwell) 대비 최대 67배 향상된 달러당 성능**을 제공하며, 이는 AI 추론 비용을 획기적으로 절감하고 데이터센터의 수익성을 극대화할 수 있음을 의미합니다.

## 1. Vera Rubin NVL72 에이전트 추론: 달러당 67배 향상된 성능

Vera Rubin NVL72는 에이전트 추론에서 블랙웰 대비 최대 67배 향상된 달러당 성능을 제공하여 AI 추론 비용을 획기적으로 절감하고 데이터센터의 수익성을 극대화한다.

### 1.1. 루빈 플랫폼의 혁신적인 공동 설계 및 성능
1. **루빈 플랫폼의 구성**
   1. 루빈은 에이전트 시대를 위해 6가지 제품이 공동 설계된 최초의 플랫폼이다.
   2. 구성 요소는 루빈 GPU, 베라 CPU, NVLink 6 스위치, ConnectX-9, BlueField-4, Spectrum-6이다.
2. **초기 성능 결과**
   1. 사전 출시 소프트웨어에서도 루빈의 에이전트 추론 결과는 극단적인 공동 설계의 필요성을 입증한다.
   2. GTC 2026에서 젠슨 황은 루빈 NVL72가 블랙웰 대비 메가와트당 3배의 성능을 달성했다고 발표했지만, 실제 사전 출시 소프트웨어 테스트에서는 메가와트당 최대 7배 더 나은 토큰 처리량을 보였다.
3. **수익성 증대**
   1. 초기 소프트웨어 빌드에서도 루빈은 블랙웰 플랫폼보다 기가와트당 2배 이상의 수익을 창출할 수 있다.
   2. 루빈 소프트웨어 스택과 커널 라이브러리가 성숙하고 개발자 커뮤니티가 루빈 최적화 경험을 쌓으면 이 격차는 더욱 확대될 것으로 예상된다.

### 1.2. AgentX 벤치마크의 신뢰성 및 활용
1. **AgentX 벤치마크의 표준화**
   1. AgentX는 업계 표준 에이전트 추론 벤치마크 시나리오를 사용하여 성능을 평가한다.
   2. 이 벤치마크는 수천 개의 칩으로 구성된 실제 에이전트 트래픽을 재현한다.
   3. 따라서 추론 제공업체와 하이퍼스케일 AI 연구소는 AgentX 결과를 통해 어떤 칩이 어떤 시나리오에서 가장 효율적인지 판단할 수 있다.
2. **광범위한 검증 및 지원**
   1. AgentX 벤치마크는 Google Cloud, Microsoft Azure, Oracle, Meta 등 주요 컴퓨팅 구매자들로부터 널리 재현, 검증 및/또는 지원받았다.
   2. 또한 vLLM, LMCache, SGLang, PyTorch, Huggingface와 같은 ML 커뮤니티와 OpenAI, MiniMax, ZAI, Qwen, Moonshot Kimi 등 주요 연구소의 지지를 받고 있다.
3. **향후 협력 계획**
   1. InferenceX GitHub 저장소는 TPUv7, NVIDIA, AMD를 포함하며 곧 SambaNova 및 Trainium도 포함할 예정이다.
   2. AgentX 시나리오가 실제 에이전트 추론 워크로드와 매우 유사하기 때문에 AMD는 MI455X UALoE72와의 협력을 약속했다.

## 2. 에이전트 워크로드의 특징
에이전트 워크로드는 다중 턴, 긴 컨텍스트, 높은 접두사 재사용, 서브 에이전트 버스트의 네 가지 주요 요소로 특징지어진다.

### 2.1. 에이전트 워크로드의 4가지 주요 특징
1. **다중 턴 (Multi-turn)**
   1. 챗봇 시나리오와 달리 사용자-어시스턴트 간 수십 또는 수백 번의 상호작용이 포함된다.
   2. 이러한 워크로드는 긴 컨텍스트와 높은 접두사 재사용을 서브 에이전트 버스트 및 수많은 도구 호출과 결합한다.
2. **긴 컨텍스트 (Long context)**
   1. 시스템 프롬프트, 도구 정의 및 많은 수의 턴으로 인해 컨텍스트가 빠르게 축적된다.
3. **높은 접두사 재사용 (High prefix reuse)**
   1. 대화가 선형적으로 진행되므로, 이전 턴의 출력이 다음 턴에 연결되어 대부분의 컨텍스트를 KV 캐시에서 제공할 수 있다.
   2. 턴 수가 증가함에 따라 캐시된 입력의 비율이 캐시되지 않은 입력에 비해 1에 가까워지는 경향이 있다.
4. **서브 에이전트 버스트 (Sub-agent bursts)**
   1. 세션은 새로운 컨텍스트로 여러 개의 단기 서브 에이전트를 시작하여 버스트성 KV-캐시 패턴을 생성한다.

<img alt="에이전트 워크로드의 4가지 주요 특징을 시각적으로 설명하는 다이어그램. 다중 턴, 긴 컨텍스트, 높은 접두사 재사용, 서브 에이전트 버스트가 각각의 아이콘과 간략한 설명으로 표현되어 있다." src="https://substackcdn.com/image/fetch/$s_!qQ6y!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a6ce1d1-5754-4021-88ca-812789d36bd9_2048x909.png" caption="에이전트 워크로드의 4가지 주요 특징">

## 3. Vera Rubin의 TCO(총 소유 비용) 대비 놀라운 성능
Vera Rubin은 TCO 대비 성능 면에서 GB300을 크게 능가하며, 특히 에이전트 워크로드에서 훨씬 더 많은 토큰을 더 저렴한 비용으로 생성할 수 있다.

### 3.1. TCO 대비 성능 평가의 중요성
1. **평가 기준**
   1. AI 가속기 성능을 평가하는 가장 중요한 기준 중 하나는 TCO(총 소유 비용) 대비 성능이다.
   2. Y축은 1달러 TCO당 총 토큰 수를 나타내며, 이는 추론 제공업체가 컴퓨팅에 지출하는 1달러당 생성할 수 있는 토큰 수를 의미한다.
   3. 이는 시나리오의 총 처리량을 총 서비스 비용(칩당 시간당 비용 * 사용된 칩 수)으로 정규화하여 계산된다.
2. **TCO 산정 방식**
   1. InferenceX는 SemiAnalysis AI 클라우드 TCO 모델에서 파생된 여러 TCO 수치를 제공한다.
   2. 기본 시나리오는 다음과 같다.
      1. **대규모 하이퍼스케일러 볼륨 소유**: 서버 및 네트워킹 자본 지출, 코로케이션, 전력, 자본 비용을 포함한 하드웨어 소유 및 운영 비용을 모델링한다.
      2. **3년 약정 임대**: SemiAnalysis 임대 가격 조사를 기반으로 클라우드 제공업체에 지불하는 3년 약정 예약의 GPU 시간당 시장 가격이다.
3. **사용자 맞춤형 비용 계산**
   1. 사용자는 계산기에서 컴퓨팅 비용을 편집하여 실제 지불하는 비용에 맞출 수 있다.
   2. 온디맨드 시장 임대료 및 단기 임대 약정과 같은 추가 수치는 월별 시장 조사를 통해 얻은 AI 클라우드 TCO 모델에서 확인할 수 있다.

### 3.2. Vera Rubin과 GB300의 TCO 대비 성능 비교
1. **GB300 대비 상당한 개선**
   1. Vera Rubin은 달러당 성능 면에서 GB300보다 크게 향상되었다.
   2. 170 TPS에서 Vera Rubin NVL72는 소유 비용 가정 하에 GB300 Dynamo TRTLLM의 TCO당 총 처리량의 약 67배를 제공한다.
   3. 대부분의 제공업체가 실제로 이 모델을 서비스할 60-100 TPS 범위에서는 Vera Rubin이 최신 GB300 TRTLLM 구성 대비 TCO당 처리량에서 1.4배에서 3배를 달성한다.
2. **P90 상호작용성 비교**
   1. Vera Rubin은 GB300 Dynamo TRTLLM보다 약 61% 높은 최대 P90 상호작용성(276.24 대 171.53 P90 TPS)을 달성한다.
   2. 하지만 오픈소스 SGLang 스택을 사용하면 GB300도 Vera Rubin과 유사한 상호작용성을 달성할 수 있다.

<img alt="Vera Rubin NVL72와 GB300 Dynamo TRTLLM의 TCO당 총 처리량(Total Tokens per $1 TCO)을 비교하는 그래프. Vera Rubin이 GB300보다 훨씬 높은 처리량을 보여준다." src="https://substackcdn.com/image/fetch/$s_!zMPG!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac2da106-c1f2-4c85-ab6c-858908f06c05_2048x1322.png" caption="Vera Rubin NVL72와 GB300 Dynamo TRTLLM의 TCO당 총 처리량 비교">

<img alt="Vera Rubin NVL72와 GB300 Dynamo TRTLLM의 P90 상호작용성(P90 Interactivity)을 비교하는 그래프. Vera Rubin이 GB300보다 높은 상호작용성을 보여준다." src="https://substackcdn.com/image/fetch/$s_!TOW-!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed0a77f0-77a8-4240-885d-6fd85b30f2b5_2048x1322.png" caption="Vera Rubin NVL72와 GB300 Dynamo TRTLLM의 P90 상호작용성 비교">

### 3.3. 3년 임대 비용 및 단일 노드 비교
1. **3년 임대 비용 기준 성능**
   1. 2026년 7월 기준, Rubin의 3년 임대 비용은 칩당 시간당 8.5달러 이상, Blackwell Ultra NVL72는 칩당 시간당 5달러였음에도 불구하고, 업그레이드는 여전히 정당화된다.
   2. 80 TPS P90 상호작용성에서 Vera Rubin은 동일한 임대 TCO로 62% 더 많은 총 토큰을 생산할 수 있다.
   3. 더 높은 상호작용성 영역에서는 Vera Rubin이 3년 임대 TCO당 최대 16배 더 많은 토큰을 달성한다.
   4. 이는 VR NVL72를 구매하거나 임대할 여유가 있다면, 더 저렴한 토큰을 생성하고 더 많은 수익을 창출할 수 있음을 의미한다.

<img alt="Vera Rubin NVL72와 GB300 Dynamo TRTLLM의 3년 임대 TCO당 총 처리량(Total Tokens per 3 Year Rental TCO)을 비교하는 그래프. Vera Rubin이 GB300보다 훨씬 높은 처리량을 보여준다." src="https://substackcdn.com/image/fetch/$s_!Jj6x!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F850c28c6-035d-45cb-821c-27991c92ac36_2048x1331.png" caption="Vera Rubin NVL72와 GB300 Dynamo TRTLLM의 3년 임대 TCO당 총 처리량 비교">

2. **단일 노드 Blackwell 및 MI355X 대비 성능**
   1. 단일 노드 Blackwell 및 MI355X와 비교하면 TCO당 성능 격차는 전체 곡선에서 더욱 커진다.
   2. 80 TPS P90 SLA(실제 모델에 매우 현실적인 수치)에서 추론 제공업체는 소유 TCO 수치를 사용할 때 B300보다 USD당 10배 더 많은 토큰을 서비스할 수 있다.

<img alt="Vera Rubin NVL72와 단일 노드 Blackwell 및 MI355X의 TCO당 총 처리량(Total Tokens per $1 TCO)을 비교하는 그래프. Vera Rubin이 다른 GPU보다 훨씬 높은 처리량을 보여준다." src="https://substackcdn.com/image/fetch/$s_!dcXL!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b1f8c1b-fc2b-4d2f-8cf8-6c1527e5dd43_2048x1312.png" caption="Vera Rubin NVL72와 단일 노드 Blackwell 및 MI355X의 TCO당 총 처리량 비교">

3. **P90 종단 간 지연 시간 이점**
   1. Vera Rubin은 P90 종단 간 지연 시간에서도 이점을 제공한다.
   2. 소유 가정 하에 TCO 1달러당 6천만 토큰에서 Vera Rubin은 약 20초의 P90 종단 간 지연 시간을 달성하는 반면, 최신 vLLM 서빙 스택을 실행하는 B200/B300은 60초가 걸린다.
   3. TCO 1달러당 1억 6천만 토큰에서는 P90 종단 간 지연 시간 격차가 약 6배로 벌어져 Vera Rubin은 20초, B200/B300은 120초가 된다.

<img alt="Vera Rubin NVL72와 B200/B300의 TCO당 총 토큰 수에 따른 P90 종단 간 지연 시간(P90 End-to-End Latency)을 비교하는 그래프. Vera Rubin이 B200/B300보다 훨씬 낮은 지연 시간을 보여준다." src="https://substackcdn.com/image/fetch/$s_!-Tct!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe968ae77-746d-4a8a-9642-b3e25b255896_2048x1325.png" caption="Vera Rubin NVL72와 B200/B300의 TCO당 총 토큰 수에 따른 P90 종단 간 지연 시간 비교">

4. **H200 대비 압도적인 성능**
   1. 에이전트 워크로드에서 Vera Rubin은 H200을 TI-84 계산기만큼 경쟁력 없게 만든다.
   2. 80 TPS의 P90 상호작용성 목표에서 Rubin은 달러당 18배 더 많은 토큰을 제공한다.
   3. 120 P90 TPS에서는 이 이점이 39배로 확대된다.
   4. Rubin의 이점은 오프라인 배치 추론보다는 훈련에 더 크며, 이는 대규모 연구소들이 Hopper를 점차 전환하는 이유이다.

<img alt="Vera Rubin NVL72와 H200의 TCO당 총 처리량(Total Tokens per $1 TCO)을 비교하는 그래프. Vera Rubin이 H200보다 훨씬 높은 처리량을 보여준다." src="https://substackcdn.com/image/fetch/$s_!NSQ8!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96d8a330-0716-4e39-85a5-d74ab3f273ad_2048x1317.png" caption="Vera Rubin NVL72와 H200의 TCO당 총 처리량 비교">

<img alt="텍사스 인스트루먼트 TI-84 Plus 그래프 계산기 교사용 10개 팩 이미지." src="https://substackcdn.com/image/fetch/$s_!IDZJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f2c6be2-d0ea-4e25-a145-3df3b49c2faa_2000x2000.png" caption="텍사스 인스트루먼트 TI-84 Plus 그래프 계산기">

## 4. Vera Rubin의 와트당 성능 및 Jensen의 과소평가
Vera Rubin은 와트당 성능에서도 탁월하며, Jensen Huang이 GTC에서 발표한 수치보다 실제 성능이 훨씬 뛰어나다.

### 4.1. 와트당 성능의 중요성 및 Jensen의 과소평가
1. **전력 효율성의 중요성**
   1. 전력 공급 데이터센터의 가용성은 칩 배포를 제한하는 요인이므로 전력 효율성이 매우 중요하다.
   2. 기가와트당 더 많은 토큰을 생성할 수 있다면, 기가와트당 더 많은 수익과 이익을 창출할 수 있다.
2. **Jensen의 성능 과소평가**
   1. GTC 2026에서 Jensen은 루빈이 블랙웰 대비 메가와트당 3배의 성능을 달성했다고 발표했지만, 실제 사전 출시 소프트웨어 테스트에서는 메가와트당 최대 7배 더 나은 토큰 처리량을 보였다.
   2. Jensen은 GTC에서 성능 주장을 과소평가하는 경향이 있다.
   3. GTC 2024에서 GB200 NVL72가 Hopper보다 30배 빠를 것이라고 주장했지만, 실제 테스트에서는 98배 더 나은 성능을 보였다.

<img alt="NVIDIA GTC 2026에서 Jensen Huang이 발표한 Rubin과 Blackwell의 성능 비교 그래프. Rubin이 Blackwell보다 메가와트당 3배 더 나은 성능을 보여준다고 명시되어 있다." src="https://substackcdn.com/image/fetch/$s_!DFuy!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffca74ac6-8331-4bd3-abb8-7058f4141ec8_2048x1131.png" caption="NVIDIA GTC 2026에서 Jensen Huang이 발표한 Rubin 성능 과소평가">

### 4.2. P90 상호작용성 및 전력 예산 내 트래픽 처리
1. **P90 상호작용성의 의미**
   1. P90 상호작용성은 P90 전체 응답 인터토큰 지연 시간의 역수를 사용하여 개별 응답의 스트리밍 속도를 나타낸다.
2. **전력 예산 내 트래픽 처리 능력**
   1. 고정된 상호작용성 목표에서 곡선이 높을수록 동일한 전력 예산 내에서 더 많은 총 트래픽을 처리할 수 있음을 의미한다.
   2. 첫 토큰에 대한 초기 대기 시간과 전체 응답 시간은 이전 지연 시간 분석에서 별도의 고려 사항으로 남아 있다.

<img alt="Vera Rubin NVL72와 GB300, MI355X의 P90 상호작용성(P90 Interactivity)에 따른 메가와트당 총 토큰 처리량(Total Tokens per MW)을 비교하는 그래프. Vera Rubin이 다른 GPU보다 훨씬 높은 처리량을 보여준다." src="https://substackcdn.com/image/fetch/$s_!jmPd!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F424235b9-f3a9-4875-8b91-d0875b715e7f_2048x1279.png" caption="SemiAnalysis InferenceX">

### 4.3. DeepSeek V4 Pro 워크로드에서의 와트당 성능 비교
1. **DeepSeek V4 Pro 워크로드에서의 이점**
   1. DeepSeek V4 Pro 에이전트 워크로드에서 Vera Rubin은 아래 비교된 목표에서 GB300 및 MI355X보다 훨씬 더 많은 총 토큰 처리량을 메가와트당 제공한다.
   2. 이 이점의 크기는 상호작용성 목표와 비교에 사용된 서빙 엔진에 따라 달라진다.
2. **100 TPS에서의 성능 비교**
   1. 100 TPS에서 Rubin은 약 5,940만 총 토큰/초/MW를 제공하는 반면, GB300 Dynamo SGLang은 2,850만, GB300 Dynamo TRTLLM은 2,110만을 제공한다.
   2. 이는 이 목표에서 더 강력한 GB300 엔진 대비 2.09배의 이점이다.
   3. MI355X SGLang은 201만 토큰/초/MW에 도달하여 Rubin이 이 특정 워크로드 및 스냅샷에서 29.5배 앞선다.
   4. SGLang은 이 목표에서 측정된 MI355X 엔진 중 가장 강력하다.
   5. 100 TPS에서의 더 넓은 하드웨어 비교에서 B200 SGLang은 695만, B300 vLLM은 556만, H200 Dynamo SGLang은 226만 토큰/초/MW를 기록한다.
   6. H200은 FP8을 사용하고, 이 비교의 다른 구성은 FP4를 사용한다.
3. **처리량 변화에 따른 이점**
   1. 아래 표는 곡선 전체에서 이점이 어떻게 변하는지 보여주며, 처리량은 유틸리티 MW당 백만 총 토큰/초 단위이다.
   2. 값은 보간된 것으로, 동일한 속도 목표에서 엔진을 비교하기 위해 측정된 벤치마크 지점 사이에서 추정된 값이다.
   3. N/A는 목표가 해당 엔진의 측정 범위를 벗어남을 의미한다.

<img alt="다양한 TPS 목표에서 Vera Rubin, GB300, MI355X, B200, B300, H200의 메가와트당 총 토큰 처리량(Million Total Tok/s per Utility MW)을 비교하는 표. Vera Rubin이 대부분의 목표에서 가장 높은 수치를 보여준다." src="https://substackcdn.com/image/fetch/$s_!aPaK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13c07f83-d722-466e-bf23-49788022a6d3_1600x900.png" caption="SemiAnalysis InferenceX 미리보기">

   4. 150 TPS에서 Rubin은 거의 3,700만 토큰/초/MW를 유지하며, GB300 SGLang 대비 약 7.2배의 이점을 가진다.
   5. 이 이점은 속도 요구 사항이 더 높아짐에 따라 좁아져 200 TPS에서는 2.72배에 이른다.
   6. 가장 강력한 GB300 엔진도 목표에 따라 달라진다. TRTLLM은 75 TPS에서, SGLang은 여기에 표시된 더 높은 목표에서 선두를 차지한다.
   7. 이 차이는 이전에 논의된 작동 지점 근처에서 특히 중요하다.
   8. 정확히 170 TPS에서 Rubin은 GB300 TRTLLM(곡선이 가장 빠른 측정 끝점에 가까움)의 MW당 총 처리량의 62.9배를 제공한다.
   9. 동일한 목표에서 GB300 SGLang 대비 승수는 5.56배이다.
   10. 따라서 높은 상호작용성 이점을 인용할 때 엔진 레이블이 필수적이다.

### 4.4. 동적 전력 전환 (DSX MaxLPS) 통합
1. **DSX MaxLPS의 특징**
   1. Rubin의 또 다른 특징은 동적 전력 전환인 "DSX MaxLPS"의 일류 통합이다.
   2. 이는 최대 TDP에 10-20%의 초과 구독 계수를 더하여 프로비저닝하는 대신, GPU 클러스터 운영자가 추론 워크로드 및 향후 워크로드에 대한 프록시의 전력 프로파일을 분석하여 실제 전력을 기반으로 동일한 데이터센터 전력 공간에 더 많은 GPU를 장착할 수 있음을 의미한다.
2. **전력 효율성 향상**
   1. 추론 워크로드, 특히 중간에서 빠른 속도에서는 GPU가 전력 소모 한도를 모두 사용하지 않으므로, 데이터센터 전체에 전력을 스마트하게 조절하면 더 많은 GPU를 장착할 수 있다.
   2. InferenceX에 곧 통합될 PowerX는 기가와트당 처리량에 대한 더욱 세밀한 측정을 가능하게 할 것이다.

## 5. 기가와트당 연간 수익 및 이익
Vera Rubin은 고정된 전력 예산 내에서 더 많은 토큰을 처리할 뿐만 아니라, GB300 대비 훨씬 높은 연간 수익과 이익을 창출하여 투자 가치를 극대화한다.

### 5.1. DeepSeek V4 Pro 모델을 통한 수익성 분석
1. **모델 선정 배경**
   1. 작성 시점에는 DeepSeek V4 Pro 1.6T가 DeepSeek V4.1 Flash로 대체되었지만, 그 크기 때문에 O(1-3T) 매개변수 LLM의 대리 역할을 할 수 있다.
   2. DeepSeek V4 Pro는 MIT 라이선스로 출시되었으므로 라이선스 비용이 없다.
2. **Rubin의 수익 창출 능력**
   1. 고정된 전력 예산에서 Rubin의 이점은 단순히 더 많은 토큰을 처리할 수 있다는 것 이상이다.
   2. 이는 운영자에게 추가 유틸리티 전력을 확보하지 않고도 수요를 수익화할 수 있는 더 많은 용량을 제공한다.
   3. 75 TPS 상호작용성, 60% 활용률, 모델 라이선스 비용이 없는 경우, Vera Rubin은 연간 1,595억 달러의 수익과 1,499억 달러의 모델링된 이익을 기가와트당 창출한다.
   4. 이 연간 수익 비교에서 가장 강력한 GB300 구성인 Dynamo SGLang은 각각 1,149억 달러와 1,053억 달러를 창출한다.
   5. 따라서 Rubin은 동일한 전력 할당에서 약 39% 더 많은 수익과 42% 더 많은 모델링된 이익을 제공한다.

<img alt="Vera Rubin NVL72와 GB300 Dynamo SGLang의 기가와트당 연간 수익 및 이익을 비교하는 그래프. Vera Rubin이 GB300보다 훨씬 높은 수익과 이익을 보여준다." src="https://substackcdn.com/image/fetch/$s_!lAYo!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05f44b34-7b40-409d-ad6a-015be7cdadbe_2048x1336.png" caption="SemiAnalysis InferenceX">

### 5.2. 추가 이익 및 가격 경쟁력 확보
1. **추가 연간 이익**
   1. 절대적인 차이는 기가와트당 약 446억 달러의 추가 연간 모델링된 이익이며, 선형 확장을 가정할 때 10 MW 규모에서는 약 4억 4,600만 달러에 해당한다.
   2. 이 두 구성에 대한 기가와트당 연간 비용이 유사하므로, 대부분의 증분 수익은 모델의 이익 측정으로 이어진다.
2. **가격 경쟁력 확보**
   1. 동일한 이점은 가격 경쟁력을 위한 여유 공간도 제공한다.
   2. 워크로드 혼합, 처리량 및 청구 가능한 활용률을 일정하게 유지하면 Rubin은 표시된 가격에서 GB300 Dynamo SGLang의 기가와트당 수익과 일치하면서 캐시된 입력, 캐시되지 않은 입력 및 출력 토큰 전반에 걸쳐 약 28% 더 저렴하게 청구할 수 있다.
   3. 따라서 운영자는 효율성 이득을 추가 이익으로 유지하거나 모델의 수요 탄력성에 따라 가격 경쟁에 활용할 수 있다.
