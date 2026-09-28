---
title: "AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?"
origin: lilys_ai
lilys_project_id: 11085621
lilys_project_url: "https://lilys.ai/digest/11085621"
lilys_created_at: "2026-08-24T11:47:18.060Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13053110"
sources:
  - id: "11943454"
    url: "https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat"
    title: "AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?"
    status: "done"
---

# AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?

## LilysAI note

LilysAI MCP가 이 문서를 시간 제한 S3 pre-signed URL로 반환했습니다. 보안상 URL과 temporary credential material을 제거했습니다. 본문이 필요하면 LilysAI에서 이 노트를 다시 가져와야 합니다.
> AgentX 벤치마크가 제시하는 **에이전트 추론 워크로드**의 핵심은 무엇인가요? 기존의 고정된 시퀀스 길이 벤치마크와 달리, AgentX는 **다중 턴, 긴 컨텍스트, 높은 접두사 재사용, 서브 에이전트 버스트** 등 실제 에이전트 워크로드의 복잡성을 반영하여 AI 하드웨어 및 소프트웨어 성능을 보다 정확하게 측정합니다. 이는 실제 프로덕션 환경에서의 AI 성능 최적화에 필수적인 기준점을 제공합니다.

## 1. AgentX 1.0: 에이전트 추론 벤치마크의 새로운 기준
AgentX 1.0은 기존의 고정된 시퀀스 길이 벤치마크의 한계를 극복하고, 실제 프로덕션 환경의 복잡한 에이전트 추론 워크로드를 정확하게 측정하기 위해 개발된 세계 최초의 오픈소스 멀티턴 에이전트 코딩 추론 벤치마크이다.

### 1.1. 에이전트 워크로드의 부상과 기존 벤치마크의 한계
1. **에이전트 워크로드의 급증**
    1. 2025년 11월 Claude Code의 변곡점 이후, 장문 컨텍스트, 멀티턴 에이전트 워크로드가 빠르게 성장했다.
    2. 현재 이러한 워크로드는 프로덕션 추론 트래픽의 대부분을 차지한다.
    3. 2026년 4월, OpenAI의 엔터프라이즈 에이전트 지출이 ChatGPT 지출을 넘어섰다.
2. **기존 성능 측정 방식의 비현실성**
    1. 과거에는 대부분 고정된 시퀀스 길이의 프리필(prefill) 및 디코드(decode) 워크로드 기반으로 성능을 측정했다.
    2. 그러나 이러한 방식은 실제 워크로드를 측정하는 데 정확하지 않다.
    3. 실제 환경은 멀티턴, 긴 컨텍스트, 높은 프리필 재사용, 서브 에이전트 버스트, KVCache 오프로드, 수많은 도구 호출 등을 포함한다.
3. **AgentX 1.0의 목표**
    1. AgentX 1.0은 100만 컨텍스트 길이의 멀티턴 에이전트 코딩 추론 벤치마크로, Apache 2.0 라이선스 하에 완전히 오픈소스로 공개되었다.
    2. 이 벤치마크는 AI 하드웨어 및 소프트웨어 성능을 측정하는 올바른 방법을 제시하는 것을 목표로 한다.

### 1.2. AgentX 1.0의 특징 및 개발 배경
1. **데이터셋 구축 및 공개**
    1. AgentX 데이터셋 구축에 300만 달러 이상이 투자되었다.
    2. InferenceXv3는 기존의 "고정 시퀀스 길이" 시나리오(8k1k, 1k1k, 1k8k) 외에 새로운 현실적인 시나리오인 AgentX를 구현한다.
    3. 이는 이전의 8k 입력 및 1k 출력 토큰의 단일 턴 트래픽 대신 에이전트 코딩 트래픽을 사용하여 벤치마크 시나리오를 개선한다.
2. **광범위한 하드웨어 지원**
    1. 전체 매트릭스는 MI355X, GB300 NVL72, GB200 NVL72, B300, B200, MI325, MI300X, H200, RTX Pro 서버 등 1,000개 이상의 칩에 걸쳐 약 2MW의 연속 컴퓨팅 파워로 실행된다.
    2. Rubin은 이달 말, TPU 및 Mi455X UALoE72는 올해 말에 출시될 예정이다.
3. **산업에 미치는 영향**
    1. AgentX가 초기 몇 달 동안 가장 가치 있게 생산한 것은 초기 결과가 아니라 벤치마크가 이미 미치고 있는 엄청난 산업적 영향이다.
    2. vLLM, SGLang, TensorRT-LLM, ATOM, AITER, Dynamo, LMCache, Mooncake 등에서 실제 프로덕션 에이전트 워크로드를 최적화하기 위한 70개 이상의 업스트림 PR이 AgentX를 북극성 벤치마크 프록시로 사용한다.
    3. 이러한 최적화 개선 사항의 대부분은 프로덕션 트래픽으로 이전 가능하다.

<img alt="Claude Code is the Inflection Point" src="https://substackcdn.com/image/fetch/$s_!D9-B!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8cee19d-ed2f-480d-b175-aed1ea7dbe4c_624x341.png">
<figcaption>Claude Code는 변곡점이다.</figcaption>

### 1.3. AgentX의 오픈소스 원칙 및 향후 계획
1. **완전한 오픈소스 스택**
    1. InferenceX는 오픈소스 원칙을 핵심으로 삼으며, 오픈 프론트엔드, 쉽게 소비 가능한 REST API를 통해 제공되는 공개 데이터베이스, 공개 GitHub Actions CI 출처, 로그, 모든 지점에서의 정확성 검증을 포함한다.
    2. 벤치마크 구성은 주로 recipes.vllm.ai 및 SGLang 쿡북을 업스트림 이미지에서 추적하여 실제 고객이 경험하는 성능을 측정한다.
2. **빠른 업데이트와 지속적인 개선**
    1. 3~4주 내에 AgentX 업데이트 기사가 발표될 예정이며, 에이전트 워크로드에 대한 추가 최적화와 AMD 및 Nvidia의 업데이트된 성능 결과가 포함될 것이다.
    2. 에이전트 워크로드의 프로필이 빠르게 변화하고 있으므로, InferenceX는 관련 워크로드를 신속하게 벤치마킹할 것이다.

## 2. 에이전트 워크로드의 특징 및 벤치마킹의 차이점
에이전트 워크로드는 멀티턴, 긴 컨텍스트, 높은 접두사 재사용, 서브 에이전트 버스트라는 네 가지 주요 특징을 가지며, 이는 기존의 고정 시퀀스 길이 벤치마크와 근본적으로 다른 시스템적 접근을 요구한다.

### 2.1. 에이전트 워크로드의 네 가지 핵심 요소
1. **멀티턴 (Multi-turn)**
    1. 챗봇 시나리오의 몇 번의 상호작용과 달리, 에이전트 세션은 수십 또는 수백 번의 사용자/어시스턴트 상호작용을 포함한다.
    2. 이는 멀티턴, 긴 컨텍스트, 높은 프리필 재사용, 서브 에이전트 버스트 및 수많은 도구 호출을 특징으로 한다.
2. **긴 컨텍스트 (Long context)**
    1. 시스템 프롬프트, 도구 정의 및 많은 턴으로 인해 컨텍스트가 빠르게 누적된다.
3. **높은 접두사 재사용 (High prefix reuse)**
    1. 대화가 선형적으로 진행되므로 (일반적으로 턴 n-1의 출력이 턴 n에 연결됨), 대부분의 컨텍스트는 재계산 대신 KV 캐시에서 제공될 수 있다.
    2. 턴 수가 증가함에 따라 캐시된 입력과 캐시되지 않은 입력의 비율은 일반적으로 1에 가까워진다.
4. **서브 에이전트 버스트 (Sub-agent bursts)**
    1. 세션은 새로운 컨텍스트를 가진 여러 단기 서브 에이전트를 시작하여 버스트성 KVCache 패턴을 생성한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!t24X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72b64a02-8a1f-4a19-929c-85c0ed4803cd_2048x909.png" width="1456" height="646" caption="Source: DeepSeek, SemiAnalysis">
<figcaption>에이전트 워크로드의 특징</figcaption>

### 2.2. 에이전트 워크로드 벤치마킹의 시스템적 특성
1. **기존 벤치마크와의 근본적인 차이**
    1. 위에서 언급된 특성들을 고려할 때, 이러한 워크로드 벤치마킹은 기존의 고정 시퀀스 길이 벤치마크와 근본적으로 다르다.
    2. 즉, 에이전트 추론은 본질적으로 시스템 문제이다.
2. **KV 텐서의 효율적인 전송 및 라우팅**
    1. 접두사 재사용률이 매우 높기 때문에, KV 텐서는 노드/랭크 간에 효율적으로 전송되어야 한다 (NIXL, MORI-IO, Mooncake).
    2. 또한, 캐시 적중률을 최대화하기 위해 적절한 접두사가 있는 노드/랭크로 다른 대화를 라우팅해야 한다 (LLM-d, Dynamo, vLLM/SGLang 라우터).
3. **HBM 용량 및 메모리 오프로딩**
    1. 긴 컨텍스트 대화는 KV 캐시를 위한 HBM 용량을 압박하며, KV 텐서를 다른 메모리 계층(DRAM, SSD)으로 효율적으로 오프로드해야 한다 (Mooncake Store, LMCache, vLLM Simple Offloading, SGLang HiCache).

### 2.3. 고정 시퀀스 길이 워크로드와의 비교 및 데이터셋 구축
1. **고정 시퀀스 길이 워크로드의 한계**
    1. 고정 시퀀스 길이, 단일 턴 워크로드와는 대조적으로, 접두사 재사용이 관련이 없으며 추론 성능은 주로 기본 칩/커널 성능을 반영한다.
    2. InferenceX의 수많은 고정 시퀀스 길이 데이터가 중요하지 않다는 의미는 아니다.
    3. 실제로, 에이전트 서빙의 복잡성을 제거하면 저수준 추론 성능 최적화가 어떻게 진행되고 있는지 명확하게 보여준다.
    4. 또한 AgentX 결과에 대한 중요한 기준선을 제공한다.
2. **AgentX 데이터셋의 현실성 확보**
    1. AgentX 워크로드를 가능한 한 현실적으로 만들기 위해, SemiAnalysis의 익명 Claude Code 트레이스 393개를 초기 코퍼스로 수집하여 재생했다.
    2. 콘텐츠를 익명화하면서 원래의 접두사 재사용 패턴을 유지하기 위해, 초기 프로덕션 트레이스 코퍼스 중 하나인 Qwen-Bailian 데이터셋과 유사한 방법을 사용했다.
    3. AIPerf를 사용하여 다양한 수준의 동시 클라이언트에서 원래 요청 스케줄에 따라 트레이스를 재구성했다.
    4. AgentX 데이터셋을 가능하게 하기 위해 Anthropic과 협력하여 두 가지 Claude Code 기능을 구현했다.

## 3. 에이전트 코딩 추론 성능 평가 지표
OpenAI, Anthropic, xAI 등 선도적인 AI 연구소들은 추론 코딩 성능을 평가할 때 달러당 성능(TPOT), 첫 토큰까지의 시간(TTFT), 그리고 전반적인 종단 간 작업 완료율이라는 세 가지 주요 지표에 중점을 둔다.

### 3.1. 주요 성능 평가 지표
1. **달러당 성능 (Performance per dollar) vs. 상호작용성 (Interactivity - TPOT)**
    1. TPOT(Tokens Per Output Token)는 출력 토큰당 처리되는 토큰 수를 나타내며, 상호작용성과 관련이 있다.
    2. 이는 비용 효율성을 평가하는 중요한 지표이다.
2. **첫 토큰까지의 시간 (Time to First Token - TTFT)**
    1. 사용자가 첫 번째 토큰을 받는 데 걸리는 시간을 측정하며, 사용자 경험에 직접적인 영향을 미친다.
3. **전반적인 종단 간 작업 완료 (Overall end-to-end task completion)**
    1. 전체 작업이 완료되는 데 걸리는 시간을 평가하며, 실제 에이전트 워크로드의 효율성을 나타낸다.
4. **메가와트당 성능 (Performance per megawatt)**
    1. 지상 데이터센터 전력이 중요한 제약 조건이므로, 전력 효율성 또한 중요한 지표이다.
    2. 데이터센터 모델은 분기별 전력 수요 및 공급 추정치를 제공한다.

### 3.2. 에이전트 성능 결과 해석의 중요성
1. **전반적인 에이전트 성능 경향 파악**
    1. 이 섹션에서는 선도적인 모델 전반에 걸친 전반적인 에이전트 성능 경향을 강조한다.
2. **오픈소스 데이터 활용 권장**
    1. 독자들이 이 가이드를 통해 스스로 결과를 조사하도록 강력히 권장한다.
    2. 모든 데이터는 오픈소스이며, 커뮤니티는 실제 추론 성능의 현재 상태에 대해 자체적인 결론을 내릴 기회를 가진다.

## 4. DeepSeek V4 Pro 0813 에이전트 추론 성능
DeepSeek V4 Pro 0813은 1.6조 개의 파라미터와 490억 개의 활성 파라미터를 가진 인기 있는 오픈 웨이트 모델로, AgentX 벤치마크에서 다양한 SKU의 성능을 평가했다.

### 4.1. DeepSeek V4 Pro 0813 모델 개요 및 요청 분포
1. **모델 특징**
    1. DeepSeek V4 Pro 0813은 중국의 매우 인기 있는 선도적인 오픈 웨이트 모델이다.
    2. 약 1.6조 개의 파라미터와 490억 개의 활성 파라미터를 가지고 있다.
2. **SKU별 성능 및 요청 분포**
    1. 8월 21일 기준으로, 다음 그래프는 총 소유 비용(TCO)으로 정규화된 모든 제출물에 대한 SKU별 최고 성능을 보여준다.
    2. 모든 DeepSeek v4 실행에서 모든 요청의 ISL/OSL 분포는 다음과 같다: ISL p50=88k, p90=272k, p95=404k, p99=675k; OSL p50=413, p90=2.2k, p95=3.7k, p99=8.6k.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!JDdn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8337140-b620-476a-abd3-59d6cc447d30_2048x1256.png" width="1456" height="893">

### 4.2. 성능 지표의 균형: TPS와 TTFT
1. **TPS와 TTFT의 중요성**
    1. 일반적으로 사용자당 초당 토큰 수(TPS, 상호작용성)와 TTFT(첫 토큰까지의 시간)를 모두 고려하는 것이 중요하다.
    2. 이 두 지표는 종종 상충 관계에 있기 때문이다.
    3. 예를 들어, 위 그래프에서 일부 SKU는 괜찮은 상호작용성으로 매우 높은 처리량을 달성하지만, TTFT는 심각하게 저하된다.
2. **허용 가능한 p90 TTFT 범위**
    1. "허용 가능한" p90 TTFT는 애플리케이션에 따라 크게 달라진다.
    2. 대부분의 프로덕션 시스템에서 에이전트 워크로드를 제공하는 경우, p90 TTFT는 200-5,000ms 범위가 될 수 있다.
    3. 5-10초를 초과하는 것은 "온라인 추론"으로 간주될 수 있는 경계를 넘어서는 것이다.
    4. 지연 시간이 중요하지 않고 최대 시스템 활용이 바람직한 초고처리량 부문(배치 처리, 매우 긴 에이전트 등)에는 여전히 실용적인 애플리케이션이 존재한다.

### 4.3. AMD MI355X 성능 분석
1. **단일 노드 성능: MI355X vs. ATOM**
    1. 단일 노드 성능 측면에서 MI355X 오픈소스 성능(vLLM)은 공급업체별 ATOM(AMD의 TensorRT LLM과 동등)에 뒤처진다.
    2. AMD가 ATOM으로 빠르게 선두를 달리고 있는 것은 훌륭하지만, 이러한 개선 사항을 vLLM에 우선적으로 업스트림할 것을 권장한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!nim3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd96697d9-bf24-4093-a7db-16d27a52aa08_2048x1200.png" width="1456" height="853" caption="Source: InferenceX">

2. **분산 추론 (DI) 성능 및 개선 필요성**
    1. AMD의 분산 추론(DI) 팀은 지난 6개월 동안 8k1k 시나리오에서 큰 진전을 이루었다.
    2. 그러나 DI가 현실적인 워크로드에 대한 실행 가능한 솔루션이 되기까지는 아직 갈 길이 멀다.
3. **처리량 vs. 상호작용성 및 TTFT 문제**
    1. GPU당 처리량 대 상호작용성 측면에서 1xDEP8+1xDEP8 분산 구성은 고처리량 시나리오에서 약간의 성능 향상만 달성할 수 있으며, 저지연 시나리오에서는 실제로 성능이 더 나쁘다.
    2. 설상가상으로, 중간에서 높은 상호작용성 구성에서 처리량이 증가하더라도 p90 TTFT의 상당한 급증으로 인해 가려진다.
    3. 이러한 이유 중 하나는 동시성 64 이상에서 SGLang의 `--enable-prefill-delayer` 인수를 사용하여 프리필 승인을 연기하여 DP 랭크가 더 완전한 배치를 형성할 수 있도록 하는 것이다 (최대 30번의 순방향 패스).
    4. 또한, 이러한 지점들은 청크 프리필 크기를 8,192에서 65,536으로 증가시킨다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!hqQ7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81475383-510e-4823-9373-751b8a3722e3_2048x1202.png" width="1456" height="855">

### 4.4. AMD와 Nvidia의 성능 경쟁
1. **e2e 지연 시간: ATOM MI355X vs. B200 vLLM**
    1. 종단 간(e2e) 지연 시간 측면에서 ATOM MI355X는 B200 vLLM을 능가한다 (그러나 B300 또는 B200 SGLang은 능가하지 못한다).
    2. 문제는 중국이나 서구의 대부분의 AI 연구소는 Alibaba Corp의 작은 광고 사업부를 제외하고는 수많은 기능 누락으로 인해 ATOM을 프로덕션에서 사용하고 싶어 하지 않는다는 것이다.
    3. Alibaba의 주요 Qwen LLM 조직은 프로덕션에서 ATOM을 사용하지 않는다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!xGRQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8d915c0-c962-4277-b62c-a1b08b8e7179_1924x1262.png" width="1456" height="955" caption="Source: InferenceX">

2. **MI355X SGLang vs. B200 vLLM (2026년 8월 21일 이전)**
    1. 2026년 8월 21일 이전에는 AMD의 MI355X 강력한 SGLang 개발 팀이 종단 간(e2e) 성능에서 B200 vLLM의 달러당 성능과 일치했다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!_s4G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F360a051c-6117-4860-a704-b50198f01521_1978x1246.png" width="1456" height="917" caption="Source: InferenceX">

3. **B300 vLLM 및 B200 SGLang의 우위**
    1. 그러나 B300 vLLM과 B200 SGLang은 여전히 AMD의 MI355X를 능가한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!6j5N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ec4708c-148e-42ee-a7c5-3bf4d9cbdfaa_1938x1246.png" width="1456" height="936" caption="Source: InferenceX">

4. **Nvidia B200의 성능 역전 (2026년 8월 21일 이후)**
    1. 2026년 8월 21일 이후, Inferact 및 Nvidia의 vLLM 최적화 덕분에 Nvidia B200의 달러당 성능이 MI355X를 넘어섰다.
    2. 이는 치열한 경쟁이며, 다음 몇 주 동안의 성능 최적화를 기대한다.
    3. AgentX 업데이트 기사가 곧 발행될 예정이다.
5. **AMD의 vLLM 최적화 계획**
    1. AMD는 DeepSeekv4 vLLM 최적화 목록을 공개했으며, 성능 향상을 위한 많은 흥미로운 사항을 포함한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Y8fs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9302da60-5bc1-46e1-9392-74e912b5c200_2024x1236.png" width="1456" height="889">

### 4.5. Nvidia GB300 및 GB200 성능 분석
1. **Nvidia의 경쟁력 있는 솔루션**
    1. Nvidia의 가장 경쟁력 있는 솔루션은 GB300 Dynamo TRTLLM과 GB200 Dynamo vLLM이다.
    2. 두 구성 모두 PD 분산(disagg)에 의존하여 합리적인 상호작용성으로 높은 처리량을 달성한다.
    3. 또한, GB300 구성은 넓은 EP(DEP32) 디코드 인스턴스를 사용하여 중간 수준의 처리량에서 더 높은 처리량을 달성한다.
2. **TPS와 TTFT의 차이점**
    1. 2xDEP8+1xDEP12 GB200 지점은 TTFT에 비해 TPS 측면에서 3xDEP8+1xDEP16 GB300 지점에 훨씬 더 가깝다.
    2. 일반적으로 TTFT는 워크로드의 "급증"에 더 민감하다.
    3. GB300 지점은 훨씬 더 높은 전체 동시성을 달성하므로 더 많은 서브 에이전트 트래픽과 더 많은 콜드 프리필을 발생시킨다.
    4. 이는 해당 지점의 TTFT 차트에서 확인할 수 있다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!g7xN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96f9c9f9-eb86-4f87-8332-c85f23040836_2048x916.png" width="1456" height="651" caption="Source: InferenceX">

<img alt="" src="https://substackcdn.com/image/fetch/$s_!9DNn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff79e53f5-c8ff-4ed0-a8a3-c05b9e0b4bab_2048x1191.png" width="1456" height="847">

### 4.6. B300 vs. B200 및 KV 캐시 오프로딩
1. **TCO 정규화 성능 비교**
    1. TCO(총 소유 비용)로 정규화했을 때 B300 vLLM과 B200 vLLM의 집계 성능은 상당히 유사하다.
    2. 주요 차이점은 B300이 B200보다 HBM 용량이 50% 증가하여 추가 처리량을 "짜낼" 수 있다는 것이다.
2. **서버 메트릭 시각화를 통한 차이점 확인**
    1. 이 차이점은 AgentX에 새로 추가된 서버 메트릭 시각화를 통해 더 자세히 확인할 수 있다.
3. **B300 vLLM의 HBM 캐시 적중률**
    1. 384개의 동시 에이전트 트레이드 부하에서 vLLM 단순 오프로딩을 통한 3TB DRAM을 사용하는 B300 vLLM DEP8은 91%의 HBM 캐시 적중률과 추가 1.36%의 DRAM 캐시 적중률을 달성했다.
    2. 이는 HBM KV 캐시 작업 세트 크기가 이 구성에서 약 43M 토큰이며, 부하가 주어진 시간에 이 토큰 수를 거의 초과하지 않기 때문이다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Z3WJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7ff2d61-bdab-4c2f-96a0-ec5a52469489_2048x884.png" width="1456" height="628">

4. **B200의 HBM 및 DRAM 캐시 적중률**
    1. B200 동시성 196(다른 모든 매개변수는 동일)에서는 73%의 HBM 캐시 적중률만 보이며, 거의 20%의 오프로드 캐시 적중률로 DRAM에 더 많이 의존한다.
    2. HBM KV 캐시 작업 세트 크기는 B300의 약 절반인 22M 토큰이다.
5. **DRAM KV 오프로딩의 효과**
    1. DRAM KV 오프로딩은 일반적으로 쓰기 스루(write-through) 캐시로 구현된다.
    2. 이는 HBM 캐시에 기록된 모든 접두사가 DRAM 캐시에도 기록됨을 의미한다.
    3. 따라서 오프로딩에 사용할 수 있는 DRAM 양이 HBM KV 캐시 용량보다 훨씬 클 때(1.5-3배) 가장 효과적이다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!pmXE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61956823-2928-44ec-b00c-8bb5581b8a13_2048x892.png" width="1456" height="634">

### 4.7. H200 SGLang FP8 및 MI355X의 전반적인 성능
1. **H200 SGLang FP8의 경쟁력**
    1. H200 SGLang FP8은 낮은 동시성에서 DeepSeek v4를 제공할 수 있으며, perf/$ 관점에서 B200/MI355X SGLang과도 경쟁력이 있다.
    2. 그러나 HBM 부족으로 인해 고처리량 시나리오에서는 최신 SKU와 경쟁할 수 없다.
    3. 또한, 높은 동시성에서 DRAM KV 오프로딩에 의존하면 사용자 수가 증가함에 따라 불합리한 지연 시간이 발생한다.
2. **MI355X의 전반적인 성능 및 개선 과제**
    1. 전반적으로 MI355X는 주요 경쟁자인 B200 및 B300과 비교하여 괜찮은 성능을 보인다.
    2. 성능은 주로 텐서 병렬 처리 및 더 기본적인 커널이 배포되는 낮은 처리량/낮은 지연 시간 곡선 부분에서 가장 유사하다.
    3. AMD는 MI355X에서 DEP 커널을 최적화하여 고처리량 시나리오에서 더 경쟁력을 갖추도록 노력해야 한다. 특히 B200보다 1.5배 높은 HBM을 고려할 때 더욱 그렇다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Mcaw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba6532b3-aa46-4477-be84-8979b1cce35d_2048x1297.png" width="1456" height="922">

## 5. Kimi K3 2.8조 파라미터 모델의 에이전트 추론 성능
Kimi K3는 2.8조 개의 파라미터를 가진 대규모 오픈 웨이트 모델로, 단일 B200 서버에 적합하지 않아 분산 추론 기술이 필수적이며, AMD와 Nvidia 간의 성능 경쟁이 치열하다.

### 5.1. Kimi K3 모델 개요 및 초기 성능 문제
1. **Kimi K3 모델 특징**
    1. Kimi K3는 2.8조 개의 총 파라미터를 가진 중국의 또 다른 선도적인 오픈 웨이트 모델이다.
    2. 이는 Claude의 Mythos/Fable5 모델 아키텍처와 유사한 파라미터 범위이다.
    3. 이 모델은 오픈 웨이트 프록시 모델 아키텍처로 사용된다.
    4. Kimi K3 모델은 너무 커서 단일 B200 서버에 적합하지 않으며, 모든 가중치를 맞추기 위해 넓은 EP/넓은 TP 또는 파이프라인 병렬 처리가 필요하다.
    5. vLLM에서 추측 디코딩/DSpark는 최근까지 파이프라인 병렬 처리와 전혀 호환되지 않았기 때문에, B200은 파이프라인 병렬 처리와 추측 디코딩을 사용할 수 없어 Kimi K3에서 성능이 좋지 않았고 MI355X에 의해 압도당했다.
2. **MI355X의 초기 문제점**
    1. MI355X vLLM은 짧은 컨텍스트 단일 턴 워크로드에서는 즉시 작동했지만, 긴 컨텍스트 멀티턴 워크로드에서는 MI355X AITER 및 Triton 커널이 첫 주에 대규모 패닉을 겪었고, 업스트림 vLLM은 MI355X에서 현실적인 워크로드에 완전히 사용할 수 없었다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!W5x3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1440922-e1ea-4a74-ab62-f1263ae31ca0_2048x1473.png" width="1456" height="1047" caption="Source: SemiAnalysis InferenceX">

### 5.2. Hopper (SM90)의 Kimi K3 워크로드 처리 어려움
1. **Hopper의 성능 저하**
    1. Hopper(SM90)는 Kimi K3에 대한 AgentX 워크로드를 처리하는 데 어려움을 겪는다.
    2. Kimi가 거대한 모델이고 vLLM 유지 관리자/NVIDIA가 Kimi K3에 대한 Hopper 최적화에 집중하지 않았기 때문이다.
    3. Hopper는 높은 상호작용성에서 서비스를 제공하기 위해 K3에 대한 맞춤형 튜닝 커널과 TP32/EP32 튜닝된 형태가 필요하다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!xHtW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce2b58fc-b7b7-46c2-ae05-baa14419d233_2048x1459.png" width="1456" height="1037" caption="Source: SemiAnalysis InferenceX">

### 5.3. AMD ATOM의 K3 성능 향상 및 vLLM 업스트림 과제
1. **AMD ATOM의 K3 성능 향상**
    1. AMD가 ATOM으로 K3 성능을 빠르게 향상시키고 있는 것은 훌륭하다.
2. **vLLM 업스트림의 중요성**
    1. 그러나 AMD는 이러한 개선 사항을 vLLM에 우선적으로 업스트림할 것을 권장한다.
    2. ATOM은 현재 AMD의 최고 성능 엔진이지만, vLLM은 업스트림 오픈소스 서빙 스택을 사용하는 고객에게 더 관련성 있는 비교 대상이다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!lDUZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80eb810f-a9ea-4f01-a41b-e19e3409ce74_2048x1459.png" width="1456" height="1037">

<img alt="" src="https://substackcdn.com/image/fetch/$s_!rIV5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73ded698-c86e-411b-8e7c-f9bb125487b7_2048x1459.png" width="1456" height="1037" caption="Source: SemiAnalysis InferenceX">

### 5.4. MI355X ATOM의 GB300 NVL72 vLLM 대비 성능
1. **MI355X ATOM의 우위**
    1. 40초에서 60초 사이의 종단 간 지연 시간 곡선 부분에서 MI355X ATOM은 달러당 성능에서 GB300 NVL72 vLLM을 능가한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!kn-R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27a3f80e-7959-4651-90eb-f498989908a3_1934x1284.png" width="1456" height="967" caption="Source: SemiAnalysis InferenceX">

## 6. MiniMax M3 모델의 에이전트 추론 성능
MiniMax M3 432B 모델에서 Nvidia는 모든 경쟁사를 압도하며 뛰어난 성능을 보여주지만, AMD는 장문 컨텍스트 멀티턴 워크로드에서 소프트웨어 성능이 저조하다.

### 6.1. MiniMax M3에서 Nvidia의 압도적인 성능
1. **Nvidia의 M3 성능 우위**
    1. Nvidia는 MiniMax M3 432B에서 모든 경쟁사를 압도한다.
2. **AMD 소프트웨어 성능의 문제점**
    1. AMD 소프트웨어 성능은 MiniMax에서 특히 장문 컨텍스트에서 매우 좋지 않다.
    2. 이는 AMD 엔지니어링 리더십이 짧은 컨텍스트 단일 턴 워크로드에만 튜닝을 장려하고 장문 컨텍스트 멀티턴 워크로드를 무시했기 때문이다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!eFzt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5396c3d-1823-4818-83de-d89cd8242451_2048x1286.png" width="1456" height="914">

### 6.2. B300 TRT-LLM의 M3 성능 및 DP-attention의 한계
1. **B300 TRT-LLM의 M3 성능**
    1. B300 TRT-LLM TP2가 M3에서 최고의 성능을 차지한다.
2. **DP-attention의 비최적성**
    1. M3에서는 DP-attention 지점이 부족한데, 이는 KV 캐시 지역성이 라우팅 제약이 되기 때문에 최적이지 않기 때문이다.
    2. 이에 대한 자세한 설명은 나중에 제공된다.
3. **GB200의 DP-attention 성능 문제**
    1. 동시성 40에서 GB200의 TP4/EP4/DPA는 일반 TP4 처리량의 0.60배에 불과하며, p90 TTFT는 3배 이상 증가한다.
    2. 동시성 32에서는 캐시의 28.8%만 적중하며, 이론적인 96.0%에 훨씬 못 미친다.
    3. 각 DP 랭크는 풀의 사적인 1/4을 소유하므로, 잘못된 랭크에 다시 착륙하는 300k 토큰 세션은 모든 것을 재계산한다.
    4. M3 프론티어에는 EP가 있는 디코드 구성이 나타나지 않는데, 이는 동시성이 모든 전문가의 부하를 균형 있게 맞출 만큼 높지 않기 때문일 가능성이 크다.

### 6.3. 랙 스케일 솔루션의 한계 및 컨텍스트 병렬 처리의 부재
1. **랙 스케일 솔루션의 성능 저하**
    1. B200/B300은 TCO로 정규화된 처리량에서 MiniMax M3에 대한 랙 스케일 솔루션을 완전히 능가한다.
    2. AgentX에서 랙 스케일 이점은 Dynamo 라우터가 병목 현상이 될 수 있기 때문에 덜 두드러진다.
    3. 이는 라우터의 작업이 활성 접두사의 수와 길이에 따라 확장되기 때문이다.
    4. 이와 관련된 최적화 및 처리량을 두 자릿수 비율로 이동시킨 몇 가지 수정 사항은 기사 후반부에서 논의된다.
    5. 또한, wideEP, wide DCP, wide TP에 대한 잘 튜닝된 커널이 없다.
    6. GB200/300은 TCO가 높기 때문에 wide ep/wide DCP가 없으면 TCO당 성능이 더 나쁘게 나타난다.
2. **Nvidia의 랙 스케일 솔루션 최적화 기대**
    1. Nvidia의 랙 스케일 솔루션에 대한 추가 최적화가 예상되며, 후속 기사에서 강조될 것이다.
3. **컨텍스트 병렬 처리의 부재**
    1. 현재 P90 ISL이 317k임에도 불구하고 컨텍스트 병렬 처리를 실행하는 제출물은 없다.
    2. 4개의 KV 헤드를 사용하면 TP8에서도 DCP가 2로 제한되며, MSA 인덱서는 자체 컨텍스트 병렬 처리가 필요하다 (vLLM PR이 열려 있음).
    3. 이 주제에 대한 자세한 내용은 컨텍스트 병렬 처리 섹션에서 논의된다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!TM89!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faec34e63-34fd-4c42-87a1-97e5c14661ed_2048x1302.png" width="1456" height="926">

### 6.4. KV 오프로딩 및 vLLM vs. TRT-LLM 성능
1. **Nvidia의 KV 오프로드 활용**
    1. Nvidia의 파레토 최적 지점은 모두 동시성 20 이상에서 KV 오프로드를 포함하지만, AMD의 파레토 최적 지점은 DRAM으로의 KV 오프로드를 사용하지 않는다.
    2. AMD는 다른 모델에서도 Nvidia보다 KV 오프로드를 덜 사용한다.
2. **AMD vLLM의 GPU-CPU 전송 비효율성**
    1. 이는 CPU KVCache 오프로드를 위한 GPU-CPU 전송이 AMD vLLM에서 매우 비효율적이기 때문이다.
    2. `hipMemcpyBatchAsync` API는 ROCm 7.14까지 누락되었다.
    3. `hipMemcpyBatchAsync`가 없으면 vLLM의 기본 Simple CPUOffloading은 더 큰 메시지 크기로 일괄 처리하는 대신 CPU에서 GPU로 직렬화된 Memcpy를 수행해야 한다.
3. **vLLM과 TRT-LLM의 성능 비교**
    1. vLLM 성능은 처리량 대 p90 상호작용성 측면에서 TRT-LLM과 매우 유사하다.
    2. 또한, vLLM은 처리량 대 p90 TTFT 측면에서 더 나은 성능을 보인다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!9ESj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68f7ad68-3886-4980-9b01-390582728e47_2048x1292.png" width="1456" height="919">

## 7. Qwen3.5 397B 모델의 에이전트 추론 성능
Qwen3.5 397B는 GatedDeltaNet을 사용하여 스토리지 요구 사항이 낮은 모델로, Nvidia가 SGLang에서 압도적인 성능을 보여주며 AMD는 경쟁력이 부족하다.

### 7.1. Qwen3.5 397B 모델 특징 및 컨텍스트 길이
1. **GatedDeltaNet 아키텍처**
    1. Qwen3.5 397B는 몇 개의 레이어마다 일반적인 어텐션 대신 GatedDeltaNet을 사용한다.
    2. GatedDeltaNet은 MIT/Nvidia Research에서 개발되었으며, 이론적으로 일반적인 어텐션의 선형 스토리지 요구 사항과 달리 상수 상태 스토리지 요구 사항을 가진다.
    3. 이는 동등한 밀집 어텐션 모델에 비해 스토리지 요구 사항이 낮다는 것을 의미한다.
    4. Nemotron 재앙과 같은 종단 간 모델 훈련 연구와 달리, Nvidia Research는 GDN 및 LatentMoE와 같은 근본적인 연구에 뛰어나며, 이는 선도적인 모델에 사용된다.
2. **모델의 최대 컨텍스트 길이 및 데이터셋 활용**
    1. 이 모델의 기본 최대 컨텍스트 길이는 262k 토큰이므로, 잘린 데이터셋을 사용한다.
    2. 이는 최대 컨텍스트 길이가 자주 도달하고 많은 압축이 발생하는 작은 모델에서의 워크로드를 시뮬레이션하며, 사용자가 이 모델을 실제로 사용하는 방식을 나타낸다.

### 7.2. Nvidia의 SGLang 성능 우위 및 AMD의 경쟁력 부족
1. **Nvidia의 압도적인 성능**
    1. Qwen3.5 397B는 SGLang 대 SGLang에서 Nvidia의 강력한 우위를 보여주며, 사용자당 90 토큰/초에서 20배 이상 더 나은 성능을 보인다.
2. **AMD의 경쟁력 부재**
    1. 현재 Qwen3.5 SGLang에서 AMD의 경쟁은 전혀 없다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Tgnw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc92da639-dcff-4e39-b9b5-49742677e93c_2048x1289.png" width="1456" height="916">

### 7.3. Nvidia의 TTFT 희생 및 B300 FP4의 성능
1. **Nvidia의 TTFT 희생**
    1. Nvidia는 특히 TRT-LLM의 경우 TTFT를 희생하면서 상호작용성을 과도하게 최적화하는 경향을 보인다.
    2. 위 그래프에서 모든 Nvidia SGLang 제출물은 TRT-LLM에 비해 p90 TTFT가 훨씬 낮다.
2. **B300 FP4의 성능**
    1. Qwen3.5에서 B300 FP4는 H100에 비해 달러당 성능이 12배 더 좋다.

## 8. GLM 5.3 모델의 에이전트 추론 성능
GLM 5.3은 GLM5.2 744B를 기반으로 추가 후처리된 선도적인 모델로, Nvidia가 OSS SGLang 성능에서 AMD를 크게 앞서며, 새로운 실험적 지표인 E2E 정규화된 상호작용성이 도입되었다.

### 8.1. GLM 5.3 모델 개요 및 Nvidia의 OSS SGLang 성능 우위
1. **GLM 5.3 모델 특징**
    1. GLM 5.3은 GLM5.2 744B를 기반으로 추가 후처리된 선도적인 모델이다.
2. **Nvidia의 OSS SGLang 성능 우위**
    1. OSS SGLang 성능 측면에서 Nvidia는 현실적인 에이전트 추론 성능에서 AMD를 다시 한번 능가한다.
    2. 사용자당 150 토큰/초 p90 상호작용성에서 Nvidia는 최대 5배 더 나은 비용 효율성을 보인다.
    3. 현재 AMD 소프트웨어 상태에서 사용자당 150 토큰/초에서 Nvidia의 성능 우위는 경쟁사 칩 하드웨어가 무료로 판매되더라도 (물론 데이터센터 호스팅, 전력 및 기타 운영 비용은 지불해야 함) Nvidia를 사용하는 것이 토큰당 비용이 여전히 더 저렴할 정도로 크다.
3. **AMD의 향후 성능 최적화 기대**
    1. 몇 주 안에 발표될 AgentX 업데이트 기사에서 AMD의 성능 최적화를 기대하며, 여기에는 다른 매우 흥미로운 결과도 포함될 것이다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!5PHJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff85bdb45-792c-4330-9745-674b38b03425_2048x1289.png" width="1456" height="916">

### 8.2. ATOM 성능 및 SGLang으로의 최적화 포팅 필요성
1. **ATOM의 경쟁력**
    1. ATOM을 살펴보면, AMD는 p90 E2E 정규화된 상호작용성 범위의 일부에서 GB300 NVL72 SGLang 및 심지어 TRTLLM보다 달러당 성능이 더 좋다.
    2. AMD 팀의 이러한 결과에 대한 훌륭한 노력을 인정한다.
2. **SGLang으로의 최적화 포팅 필요성**
    1. AMD가 이러한 최적화 사항을 SGLang으로 포팅하는 것을 기대한다.
    2. 또한 Nvidia가 다음 몇 주 동안 GB300 NVL72를 빠르게 최적화하는 것도 기대한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!rzqP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9337ed5b-a320-49f7-b31b-cc4b5751e0ff_2048x1290.png" width="1456" height="917" caption="Source: SemiAnalysis InferenceX">

### 8.3. E2E 정규화된 상호작용성 (E2E Normalized Interactivity) 지표
1. **새로운 실험적 지표 도입**
    1. E2E 정규화된 상호작용성이라는 실험적 지표를 소개한다.
    2. 이 지표는 TTFT와 TPS를 모두 고려하여 사용자가 응답성을 얼마나 빨리 경험하는지 평가한다.
    3. 이는 OSL/E2EL로 정의된다.
    4. E2EL이 TTFT + OSL * TPOT(실제로는 OSL - 1 토큰만 디코딩됨)와 같다는 사실을 대입하면 다음 방정식을 얻을 수 있다.
    5. 이는 효과적으로 상호작용성(1/TPOT 부분)에 TTFT에 비례하는 추가 페널티를 더한 것이다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!vo0y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e472a49-d228-4d8d-876a-6bc0d59f9d97_746x594.png" width="746" height="594" caption="Source: SemiAnalysis">

2. **지표의 실험적 특성 및 한계**
    1. 이 지표는 실험적이며 완벽하지 않다.
    2. 예를 들어, 높은 TTFT에 큰 페널티를 부과하며 PD 분산과 같은 특정 최적화의 모든 뉘앙스를 포착하지 못한다.
    3. AgentX v1.0의 모든 제출물은 일반적인 상호작용성과 TTFT를 별도로 최적화한다.
    4. 현대 에이전트 추론의 모든 뉘앙스를 반영하는 새로운 북극성 지표를 계속 개발할 것이다.

## 9. AgentX의 산업적 영향 및 에이전트 워크로드 최적화
AgentX는 오픈소스 데이터셋을 제공하는 것 외에도, 실제 에이전트 워크로드 최적화를 위한 50개 이상의 업스트림 PR을 유도하여 산업에 막대한 영향을 미쳤으며, 분산 추론 생태계의 다양한 구성 요소에 걸쳐 최적화가 이루어지고 있다.

### 9.1. AgentX의 산업적 영향 및 최적화 범위
1. **AgentX의 핵심 성과**
    1. AgentX가 초기 몇 달 동안 가장 큰 영향을 미친 결과는 오픈소스 데이터셋을 생산한 것이 아니라, AgentX 파트너들이 AgentX를 북극성으로 사용하여 실제 에이전트 워크로드를 최적화하기 위해 생성한 50개 이상의 업스트림 PR의 산업적 영향이다.
    2. AgentX의 실제 에이전트 트래픽 벤치마크는 원시 프리필 및 디코드 커널뿐만 아니라 KV 캐시 수명 주기, 하이브리드 어텐션 캐시 정확성, CPU KV 오프로드, 전송 진행 상황, 라우팅 선호도, 증분 토큰화, 요청 직렬화 및 스케줄러 장부 정리 등 전체 종단 간 토큰 생성 프로세스를 테스트한다.
    3. 이러한 모든 단계는 모든 프로덕션 에이전트 배포에 중요하다.
2. **생태계 개선 가속화**
    1. 이는 생태계가 소프트웨어 개선을 가속화하고 빛의 속도로 개선을 제공하도록 돕는 지속적인 사명의 연장선이다.
    2. 좋은 예는 SemiAnalysis와 AMD의 소프트웨어 개발 팀 간의 다년간의 협력으로, AMD의 소프트웨어 개발 원칙을 현대화하는 데 지속적인 피드백과 입력을 제공했다.
    3. 이는 AMD의 발전을 가속화하는 많은 변화를 가져왔을 뿐만 아니라, AMD 오픈소스가 에이전트 워크로드에서 일류에 더 가까워지는 데 중요한 역할을 했다.

### 9.2. 분산 추론 생태계 개요
1. **에이전트 추론의 시스템적 문제**
    1. 에이전트 추론은 단순히 칩/커널 수준의 문제가 아니라 본질적으로 시스템 전체의 문제이다.
    2. 또한, 수십만 개의 에이전트 요청을 처리하는 대규모 분산 시스템에서는 요청 스케줄링 및 KV 캐시 관리가 간단하지 않으며 실제 성능에 영향을 미친다.
    3. 예를 들어, 서브 에이전트는 버스트성 KVCache 패턴을 제공하며, 제대로 최적화되지 않으면 주 에이전트의 캐시를 부적절하게 제거한다.
2. **라우터의 역할**
    1. 다음 다이어그램은 스택을 높은 수준에서 보여준다.
    2. 맨 위에서 라우터(때로는 "프론트엔드"라고도 함)는 요청을 다른 워커로 라우팅한다.
    3. 예를 들어, 서버가 데이터 병렬 어텐션을 실행하는 경우 각 DP 랭크에 대해 별도의 KV 캐시가 있다.
    4. KV 캐시 중 하나를 스래싱하지 않기 위해, 요청은 동일한 세션/서브 에이전트의 요청이 고유 ID로 라우팅되는 일관된 해시와 같은 다른 정책에 따라 라우팅된다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!T1Z9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58ac4a3a-cc05-4ff6-9d1e-b28dc0d0f760_1814x2048.png" width="1456" height="1644" caption="Source: SemiAnalysis">

### 9.3. 분산 추론 스택의 구성 요소 및 상호작용
1. **라우터 구현의 다양성**
    1. 대부분의 라우팅 정책에서 각 라우터 구현은 크게 다르지 않다.
    2. 일부는 vLLM 라우터 및 llm-d 라우터와 같은 별도의 구성 요소이며, 다른 일부는 SGLang 모델 게이트웨이 및 ATOM Mesh와 같이 엔진에 통합되어 있다.
2. **추론 엔진 및 KV 캐시 관리자**
    1. 요청이 라우팅되면 vLLM, SGLang 등과 같은 추론 엔진의 스케줄러에 의해 처리된다.
    2. 엔진은 실제로 추론을 수행하고 API를 통해 결과를 반환하는 역할을 한다.
    3. 또한, 각 엔진은 엔진의 내부 KV 캐시를 외부 KV 캐시 관리자에 연결하기 위한 인터페이스를 가지고 있다.
    4. 이를 통해 다양한 KV 캐시 관리자가 다양한 추론 엔진과 통합될 수 있는 "플러그형" 생태계가 가능하다.
3. **Mooncake와 vLLM의 통합 예시**
    1. 현재 AgentX 결과에 사용되는 간단한 배포는 동일한 노드에서 Mooncake와 vLLM을 함께 실행한다.
    2. 각 vLLM 워커는 Mooncake Store 클라이언트를 내장하고 호스트 DRAM의 일부를 외부 KV-캐시 풀에 기여한다.
    3. vLLM은 MooncakeStoreConnector 인터페이스를 통해 이 풀에 연결하여 재사용 가능한 KV 블록을 GPU 메모리로 로드하고 새로 계산된 블록을 호스트 메모리로 다시 저장한다.
    4. Mooncake Store는 배치 및 제거를 포함한 외부 캐시를 관리하며, Mooncake Transfer Engine은 GPU와 CPU 메모리 간의 실제 데이터 이동을 수행한다.
4. **다중 KV 관리 및 전송 경로**
    1. 다른 KV 캐시 관리자는 메모리 계층 또는 머신 간(예: 프리필 및 디코드 워커 간)에 바이트를 물리적으로 이동하기 위해 다른 전송 엔진을 사용할 수 있다.
    2. 예를 들어, Mooncake Store는 Mooncake Transfer Engine을 사용하여 GPU 메모리, 호스트 DRAM 및 원격 노드 간에 KV 블록을 이동한다.
    3. 배포는 Mooncake Store를 사용하여 재사용 가능한 KV 블록을 호스트 DRAM으로 오프로드하는 동시에 NIXL을 사용하여 요청별 KV를 프리필 GPU에서 디코드 GPU로 직접 전송할 수 있다.
    4. Mooncake TE는 Mooncake Store 경로의 이동을 처리하고, NIXL은 UCX 및 GPUDirect RDMA가 지원되는 경우 별도의 프리필-디코드 경로를 처리한다.
    5. 따라서 여러 KV 관리 및 전송 경로가 동일한 추론 엔진 내에서 공존할 수 있다.
5. **분산 시스템 플랫폼**
    1. 생태계는 추론 엔진, 라우터, KV-캐시 관리자, 데이터 전송 라이브러리 및 클러스터 컨트롤러를 포함한 많은 독립적인 구성 요소로 구성된다.
    2. Nvidia Dynamo, llm-d 및 AMD Infera와 같은 플랫폼은 이러한 구성 요소의 선택된 조합을 완전한 소프트웨어 배포판으로 "패키징"한다.
    3. 이들은 호환 가능한 컨테이너 이미지, 커넥터, 배포 매니페스트 및 오케스트레이션 로직을 게시하여 구성 요소가 하나의 시스템으로 배포 및 작동될 수 있도록 한다.
    4. 결과 제품은 일반적으로 단일 모놀리식 서비스가 아니라 조정된 컨테이너 모음이다 (예: Dynamo, llm-d 및 Infera는 일반적으로 k8s에 배포되고 대규모 분산 시스템을 조정한다).

<img alt="" src="https://substackcdn.com/image/fetch/$s_!ZyoZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf5c4776-221b-43b4-b2fd-d46e46f1ab38_1772x960.png" width="1456" height="789" caption="Source: RedHat / llm-d">

## 10. 컨텍스트 병렬 처리 (Context Parallelism)
컨텍스트 병렬 처리는 긴 컨텍스트 워크로드에서 효율성을 높이기 위해 쿼리 토큰을 GPU에 분할하는 기술로, 프리필 컨텍스트 병렬 처리(PCP)와 디코드 컨텍스트 병렬 처리(DCP)의 두 가지 형태로 나뉜다.

### 10.1. 컨텍스트 병렬 처리의 필요성 및 유형
1. **긴 컨텍스트 워크로드의 병렬 처리 이점**
    1. 긴 컨텍스트는 고정된 8k 프롬프트가 강력하게 활용할 수 없는 병렬 처리 기술에 이점을 제공한다.
    2. 8k에서는 분할할 것이 거의 없고 TTFT가 이미 짧기 때문이다.
    3. 또한, TP 및 DP 어텐션과 같은 병렬 처리 전략은 더 긴 컨텍스트 길이에서 최적이지 않다.
    4. TP는 각 랭크에 전체 KV가 복제될 수 있기 때문이다.
    5. DP 어텐션의 경우 KV가 공유되지만, 긴 컨텍스트 워크로드는 가능한 컨텍스트 길이의 분산이 더 높기 때문에 더 긴 컨텍스트에서 지연될 수 있다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!8e51!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e2801db-53ff-4029-8b55-01b3c1a7037d_1632x1140.png" width="1456" height="1017" caption="Source: SemiAnalysis">

2. **컨텍스트 병렬 처리의 두 가지 형태**
    1. **PCP (Prefill Context Parallelism)**
        1. 각 랭크는 쿼리 청크(KV 링 전달)를 프리필한다.
        2. 프리필은 컴퓨팅 바운드 경향이 있으므로, 이는 FLOP를 병렬화하여 한 랭크에서 거대한 프롬프트 프리필 스파이크 없이 더 빠른 프리필을 초래한다.
    2. **DCP (Decode Context Parallelism)**
        1. 각 랭크는 KV 샤드를 스캔하고, 부분 어텐션은 플래시 디코드 스타일로 병합된다.
        2. 디코드는 메모리 대역폭 바운드이므로, 병렬 KV 읽기는 더 빠른 토큰/초를 초래할 수 있다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!o8e4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9544ced-f418-44e0-8910-0cbc63fa26ec_2048x768.png" width="1456" height="546">

<img alt="" src="https://substackcdn.com/image/fetch/$s_!jsOJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F512c3a96-2ab4-452f-be6a-4fa60900575c_2048x651.png" width="1456" height="463">

### 10.2. CUDA Moat와 AMD 구현의 과제
1. **Nvidia Research의 역할**
    1. 이 병렬 처리 기술은 부분적으로 Nvidia Research에 의해 개발되었다.
    2. Nvidia Research는 이러한 근본적인 연구에 뛰어나지만, 종단 간 훈련 연구에서는 현재 작은 Qwen3.8 27B 모델에도 크게 뒤처지는 끔찍한 Nemotron3 Ultra 모델로 미국을 당황시키고 있다.
2. **AMD 구현의 최적화 부족**
    1. DCP/PCP는 AMD의 DCP/PCP 구현이 아직 최적화되지 않았기 때문에 CUDA Moat의 일부를 형성한다.
    2. vLLM 지원 매트릭스에서 모든 AMD 백엔드는 지원되지 않는다.
3. **향후 변경 사항**
    1. 다음 몇 섹션에서 언급된 변경 사항 중 일부는 DCP/PCP에 중점을 둔다.

## 11. vLLM 에이전트 최적화
vLLM은 AgentX의 현실적인 리플레이어를 북극성으로 삼아 하이브리드 어텐션 접두사 캐싱 개선, CPU KV 오프로드 지원 확장, 오프로드 경로 비용 절감, 비동기 조회 및 정확성 수정 등 다양한 에이전트 워크로드 최적화를 구현했다.

### 11.1. vLLM의 하이브리드 어텐션 접두사 캐싱 개선
1. **AgentX를 통한 최적화**
    1. Inferact, Red Hat, NVIDIA 및 AMD의 vLLM 유지 관리자와 협력하여 AgentX의 현실적인 리플레이어를 북극성으로 사용했으며, 그 결과 수정 사항은 대부분 프로덕션에 매우 이전 가능한 업스트림에 적용되었다.
    2. 몇 가지 예시는 다음과 같다.
2. **하이브리드 어텐션 접두사 캐싱 개선**
    1. vLLM은 하이브리드 어텐션 접두사 캐싱을 개선하여 단기 슬라이딩 윈도우 할당이 유용한 장문 컨텍스트 체크포인트를 제거하지 않도록 했다.
    2. 선택적 보존은 희소한 리플레이 경계를 보존했으며, 14개의 동시 요청과 최대 100만 토큰의 컨텍스트에서 95% 이상의 접두사 캐시 적중률을 보고했다.
    3. 동일한 도달 가능성 정책이 Mooncake에 적용되었으며, 도달할 수 없는 슬라이딩 윈도우 조회는 제거되었다.
    4. 이전 후속 작업에서는 재사용할 수 없는 슬라이딩 윈도우 블록의 오프로드를 중단하고 추측적 선행 블록을 보존된 접두사에 유지했다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!CVRv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf1a505d-b8c3-45f9-b03c-a8798fba54c0_2048x632.png" width="1456" height="449" caption="Source: SemiAnalysis and vLLM GitHub PR for Agentic Workloads">

### 11.2. CPU KV 오프로드 지원 확장 및 비용 절감
1. **하이브리드 모델을 위한 CPU KV 오프로드**
    1. 고동시성 에이전트를 위한 에이전트 워크로드는 오프로딩이 필요하다.
    2. AgentX의 영향 덕분에 vLLM에는 하이브리드 모델에 대한 CPU KV 오프로드를 허용하는 작업 스트림이 이미 존재한다.
    3. 이는 균일한 전체 어텐션 모델에만 해당되지 않는다.
    4. 이 구분은 중요하다. 왜냐하면 균일한 모델은 토큰당 하나의 KV 레이아웃을 가지므로, 커넥터는 단일 블록 지오메트리로 저장할 내용을 설명할 수 있기 때문이다.
    5. 하이브리드 모델은 여러 캐시 그룹을 동시에 가지며, 각 그룹은 다른 모양과 다른 수명 주기를 가지므로, 하나의 균일한 레이아웃을 가정하는 커넥터는 주어진 블록이 어떤 그룹에 속하는지 표현할 수 없다.
    6. 따라서 오프로드는 가장 긴 세션이 필요한 모델에 사용할 수 없었다.
    7. 일반 SimpleCPU 커넥터가 먼저 나왔고, ROCm에서 활성화되었으며, DeepSeek-V4 하이브리드 어텐션으로 확장되어 HBM에 더 이상 맞지 않는 접두사를 재계산하는 것에 비해 81.7% 더 높은 출력 처리량과 46.6% 더 낮은 평균 종단 간 지연 시간을 보고했다.
2. **Mooncake의 하이브리드 메모리 할당 지원**
    1. Mooncake도 동등한 하이브리드 메모리 할당 지원을 얻었다.
    2. 동일한 레이아웃 문제가 분산 서빙에서 다시 나타나는데, 여기서 보류 중인 변경 사항은 Kimi-K3의 conv+ssm 순환 상태를 MoRI-IO를 통해 어텐션 KV와 함께 1P1D 프리필/디코드 분할로 전송한다.
    3. 이것이 없으면 디코드 측은 초기화되지 않은 순환 상태에서 시작한다.
    4. 순환 상태 슬롯은 기존 원격 블록 ID 채널을 사용하므로, 분산 라우터는 모델별 변경이 필요 없으며, MI355X, 교차 노드 RDMA를 통한 레그당 TP8, 양쪽 레그에서 DSpark 추측 디코딩으로 종단 간 경로가 실행되었다.
3. **오프로드 경로 비용 절감**
    1. 현실적인 워크로드를 프로파일링할 때 vLLM 유지 관리자는 오프로드 중에 비용이 저장 경로로 이동하며, 너무 많이 너무 자주 쓰기 작업을 수행한다는 것을 발견했다.
    2. 세 가지 새로운 수정 사항이 이 문제를 해결했다.
        1. 동일한 전송이 이미 진행 중인 동안 저장 작업이 건너뛰어지므로, 접두사를 공유하는 동시 세션은 각 세션당 한 번이 아니라 한 번만 비용을 지불한다.
        2. 저장 작업은 새로 생성된 KV 범위만 포함하므로, 기록을 확장하는 세션은 매 턴마다 전체 접두사를 다시 쓰는 대신 델타를 기록한다.
        3. 마지막으로, 저장 작업은 동일한 블록이 여전히 HBM에 있는지 여부에 더 이상 의존하지 않으므로, 제거가 발생하더라도 이미 예약된 작업이 폐기되지 않는다.
4. **비동기 조회 및 CPU/전송 오버헤드 제거**
    1. 조회 경로는 별도로 튜닝되었다. 왜냐하면 데이터가 실제로 이동할 때뿐만 아니라 모든 스케줄링 결정에서 조회가 발생하기 때문이다.
    2. 스케줄러 경로에서 조회를 비동기식으로 만들면 커넥터가 단계의 중요 경로에서 벗어나므로, 단계는 더 이상 작업을 승인하기 전에 CPU 측 캐시 쿼리를 기다리지 않는다.
    3. 컴팩트한 제로 복사 조회 키, 병렬 수신 측 로딩 및 사전 구축된 Mooncake 키 문자열은 남아있는 CPU 및 전송 오버헤드를 제거했다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!E7LD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c2cfea4-a217-47ad-934b-dbd226bb248c_2048x837.png" width="1456" height="595" caption="Source: SemiAnalysis and vLLM GitHub PR for Agentic Workloads">

### 11.3. 정확성 및 계정 수정, ROCm 측 최적화
1. **하이브리드 상태의 정확성 및 계정 수정**
    1. 장기 실행되는 하이브리드 상태는 고정된 형태의 요청에서는 거의 발생하지 않는 정확성 및 계정 수정 문제를 야기했다.
    2. vLLM은 하이브리드 캐시 그룹당 캐시 이벤트를 발생시키고, 분산 컨텍스트 저장소를 올바르게 스트라이드하며, 분산 컨텍스트 및 프리필에서 조회 접두사를 올바르게 계산한다.
    3. 관련 컨텍스트 병렬 계정 변경은 캐시 소유권을 샤딩된 토큰 범위와 정렬한다.
    4. 추측 상태는 이제 병합된 Mooncake 그룹과 SimpleCPU 코디네이터를 통해 전파되어 반복되는 턴 캐시가 EAGLE 상태를 조용히 잃는 것을 방지한다.
2. **ROCm 측 에이전트 워크로드 최적화**
    1. vLLM에서 에이전트 워크로드를 최적화하는 ROCm 측 작업은 캐시 계층 아래에서 계속되며, 여기서 남은 비용은 요청당이 아니라 계층당이다.
    2. 접두사가 살아남아 제때 도착하면 남은 것은 디코드 단계 자체이며, 세션당 수천 번 실행되는 디코드 단계는 피할 수 있는 모든 복사 및 일치하지 않는 커널에 대한 비용을 지불한다.
    3. 세 가지 공개된 변경 사항이 해당 계층을 공격한다.
        1. Kimi-K3 변경 사항은 KDA 디코드 결과를 계층 출력 버퍼에 직접 기록하여 KDA 계층당 하나의 장치 복사를 제거한다. 이 절약은 개별적으로는 작지만 디코딩된 모든 토큰의 모든 계층에 대해 반복된다.
        2. 두 번째 변경 사항은 일반 경로 대신 AITER 희소-MLA 디코드 커널을 선택했으며, 실질적으로 낮은 토큰 간 지연 시간으로 5.22% 더 높은 AgentX 출력 처리량을 보고했다.
        3. 세 번째는 측정 형태가 얼마나 중요한지 보여주는 유용한 예시이다. 동반 변경 사항은 튜닝된 AITER GEMM을 통해 전체 그래프 어텐션 프로젝션을 라우팅했으며, 낮은 동시성에서 고정 시퀀스에서 2.3%의 이득을 달성했다. 이는 커널 수준 변경이 균일한 형태에서 깨끗한 이득을 보여줄 수 있지만, 에이전트 트레이스에서는 트레이스가 도입하는 캐시 및 스케줄링 분산에 의해 압도될 수 있음을 보여준다. 보류 중인 변경 사항은 해당 형태 민감도를 디스패치 기준 자체로 전환한다. DeepSeek V4 C4A 선택기의 ROCm top-k 병목 현상을 gfx950의 하이브리드 AITER/네이티브 경로로 대체하여 짧고 중간 컨텍스트는 AITER를 통해 라우팅하고 긴 컨텍스트는 그래프 안전 튜닝된 네이티브 폴백을 통해 라우팅한다. 이는 84개 형태 매트릭스에서 1.21배에서 1.76배의 종단 간 선택기 속도 향상과 1.2배에서 2.9배의 디코드 커널 기하 평균을 보고한다.

## 12. SGLang 에이전트 최적화
SGLang은 AgentX 팀과의 협력을 통해 슬라이딩 윈도우 메모리 관리, HiCache 오프로딩 메커니즘, 가변 길이 트래픽 처리, DP 캐시 선호도, 추측 디코딩 및 이기종 프리필/디코드 토폴로지 지원 등 다양한 에이전트 워크로드 최적화를 구현하여 프로덕션 추론 성능을 크게 향상시켰다.

### 12.1. SGLang의 슬라이딩 윈도우 메모리 관리 개선
1. **AgentX 팀과의 협력**
    1. AgentX 팀은 RadixArk, Meta, Nvidia 및 AMD의 SGLang 유지 관리자와 긴밀히 협력하여 SGLang을 사용하여 실행되는 에이전트 워크로드에 대한 최적화를 추진했으며, 그 결과 프로덕션 추론 성능이 크게 향상되었다.
    2. 이러한 최적화에 대해 더 자세히 논의한다.
2. **슬라이딩 윈도우 메모리 관리 문제 해결**
    1. 할당자 측면에서 SGLang의 슬라이딩 윈도우 작업이 vLLM의 보존 정책과 동일한 충돌을 어떻게 해결하는지 설명한다.
    2. 윈도우 페이지와 접두사 페이지는 하나의 풀에서 가져오며, 윈도우는 더 탐욕스러운 소비자이다.
    3. 접두사는 가만히 있는 동안 윈도우는 계속해서 바뀌므로, 압력 하에서 일시적인 할당이 영구적인 할당을 대체한다.
    4. 세 가지 설계 개선 사항이 다른 각도에서 이 문제를 해결한다.
        1. 하나는 페이지가 윈도우를 떠날 때 제거 압력이 페이지를 찾을 때까지 기다리지 않고 선제적으로 페이지를 해제하므로, 죽은 윈도우 상태는 더 이상 사용할 수 없는 페이지에 대한 경쟁을 중단한다.
        2. 다른 하나는 컴퓨팅 잠금을 단일 윈도우로 제한하여, 진행 중인 요청이 한 번에 얼마나 많은 풀을 고정할 수 있는지 제한한다.
        3. 세 번째는 유용성이 다한 오래된 전체-KV 항목을 제거한다.
3. **포크형 맹점 및 ROCm 링 캐시 수정**
    1. 선제적 해제에는 포크형 맹점이 있다.
    2. 공유 접두사에서 분기하는 요청은 여전히 재사용 가능한 전체-KV를 보유할 수 있지만, 분기 지점의 윈도우 상태는 이미 해제되었으므로, 저렴한 절반이 없으면 전체 접두사가 재계산된다.
    3. 공개된 작업은 포크가 윈도우를 다시 빌드하는 대신 상속하도록 해당 분기 지점에서 SWA 상태를 보존한다.
    4. 이와 함께 ROCm 링 캐시 수정은 용량 변경이 아니라 정확성 변경이다.
    5. 링 버퍼는 구성상 슬롯을 재사용하며, 이전 내용이 여전히 참조되는 슬롯을 재사용하면 느린 출력이 아니라 잘못된 출력이 발생한다.
    6. 이 중 어느 것도 윈도우가 접두사를 겹치지 않고 풀이 경쟁하지 않는 단일 8k 프롬프트에서는 보이지 않는다.
    7. 멀티턴 하이브리드 세션에서는 이러한 변경 사항이 다음 턴에서 값비싼 전체 어텐션 기록이 여전히 존재하는지 여부를 결정한다.

### 12.2. HiCache 오프로딩 및 가변 길이 트래픽 처리
1. **HiCache 오프로딩 메커니즘**
    1. HiCache는 SGLang의 일류 인트리 오프로딩 메커니즘이다.
    2. vLLM의 커넥터와 동일한 하이브리드 문제에 직면했으며, 비대칭 방식으로 해결했다.
    3. 전체 어텐션 캐시를 오프로드하고 돌아오는 길에 짧은 슬라이딩 윈도우 꼬리를 재구성한다.
    4. 값비싼 절반만 버스를 통해 이동할 가치가 있으며, 저렴한 절반은 가져오는 것보다 더 빨리 재구축될 수 있다.
    5. AMD에서는 단계별 쓰기 백(staged write-back)이 엔진이 작동하는 동안 이동을 차단하지 않도록 한다.
    6. 순환 상태는 남은 간격이었다. 왜냐하면 윈도우 꼬리처럼 인접 토큰에서 재구축될 수 없기 때문이다.
    7. FlashInfer GDN 체크포인트는 접두사 재사용에 참여할 수 있도록 했고, 92.4%의 캐시 적중률로 처리량을 47,771에서 53,004 토큰/초/GPU로 증가시켰다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!VyzT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F078ad449-7657-4468-9ff9-3480a7999d89_2048x720.png" width="1456" height="512" caption="Source: SemiAnalysis">

2. **가변 길이 트래픽 처리**
    1. 두 가지 추가 변경 사항은 가변 길이 트래픽이 커널 파이프라인에 미치는 영향을 해결한다.
    2. AgentX 현실적인 세션은 지속적으로 변화하는 컨텍스트 길이로 도착하는 경향이 있으며, 이는 프로덕션 트래픽에서 관찰되는 유사한 패턴이다.
    3. 길이에 특화된 순진한 런타임은 거의 모든 요청에 대해 새로운 커널을 컴파일한다.
    4. SGLang 유지 관리자는 컨텍스트 길이를 런타임 스칼라로 전달하여 하나의 컴파일로 축소하는 대신 이 문제를 해결했으며, 컴파일을 제거하여 AgentX 동시성 384 출력 처리량을 26.75% 증가시키고 평균 TTFT를 36.25% 감소시켰다.
    5. 같은 맥락에서, 단계별 장치-호스트 시퀀스 길이 동기화를 제거하면 호스트가 장치가 이미 가지고 있는 길이를 알고 싶어 하기 때문에 발생하는 디코드 버블이 제거된다.
3. **어텐션 커널 내 가변 길이 문제**
    1. 가변 길이는 어텐션 커널 자체 내에서도 문제가 된다.
    2. GB300에서 혼합 컨텍스트 디코드 배치는 꼬리 세금을 지불한다.
    3. 일치하는 프로필은 9.8ms 디코드 단계 델타 중 8.4ms를 어텐션에 기인했으며, 가장 긴 요청이 영구 커널의 공유 웨이브를 지연시킨다.
    4. 공개된 작업은 TRTLLM MHA 디코드 배치를 KV 길이로 정렬된 그룹으로 분할하여 짧은 요청이 가장 긴 요청을 기다리지 않도록 한다.
4. **스케줄러 수준의 디코드 지연 해결**
    1. 디코드는 스케줄러에서 커널 내부에서뿐만 아니라 한 단계 위에서도 지연될 수 있다.
    2. DP 어텐션 하에서 모든 랭크는 동일한 MoE 집합에 참여하면서 어텐션 작업을 로컬로 스케줄링하므로, 청크 프리필 연속 스트림을 공급받는 랭크는 프리필 우선 결정을 계속 이기면서 피어 랭크의 실행 중인 배치는 대기 상태로 유지된다 (AgentX 실행에서 관찰됨).
    3. 프리필 후 구성 가능한 디코드 간격은 프리필 사이에 디코드 라운드를 강제한다.
    4. AgentX DSv4 Pro에서 출력 처리량은 141% 증가하고 p99 토큰 간 지연 시간은 97.3% 감소했지만, 중간 TTFT는 36.5초에서 59초로 증가하여 첫 토큰 대기 시간과 스트림 부드러움 간의 균형을 맞춘다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!mne_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47ce130f-13f2-4732-8431-17e26184b8c3_1846x806.png" width="1456" height="636" caption="Source: SemiAnalysis">

### 12.3. DP 캐시 선호도 및 추측 디코딩 최적화
1. **DP 캐시 선호도 추가**
    1. 요청이 서브 에이전트 시작과 같이 재사용 가능한 기록을 가지고 있지 않은 경우, 어떤 워커든 잘 작동하며 로드 밸런싱이 유일한 질문이다.
    2. 요청이 MB의 캐시된 접두사를 가지고 있는 경우, 해당 접두사를 보유하지 않은 유휴 워커로 보내는 것은 비용이 많이 드는 선택이며, 라우터는 상태가 이미 어디에 있는지 알아야 한다.
    3. SGLang은 DP 캐시 선호도를 추가하여 세션이 캐시를 보유하는 랭크에 고정되도록 했다.
    4. 이 PR에서는 DP 인식 프리필 및 디코드 라우팅이 모두 구현되어 분산 배포의 양쪽 절반이 일관되게 결정을 내리고, 선호도가 하나의 핫 워커로 퇴화하지 않도록 캐시 균형을 라우팅 신호로 사용한다.
    5. 라우터는 전달받은 정보에만 따라 행동할 수 있으므로, 하이브리드 캐시 이벤트도 라딕스 캐시 인식 및 슬라이딩 윈도우 인식이 된다.
2. **추측 디코딩 최적화**
    1. 추측 디코딩은 특별한 주의를 받는다. 왜냐하면 MTP는 주 캐시가 살아남는 모든 것을 살아남아야 하는 두 번째, 더 작은 요청당 상태를 추가하기 때문이다.
    2. SGLang은 분산 서빙에서 드래프트 윈도우 전송을 수정하여 상태가 프리필-디코드 경계를 손상 없이 통과하도록 했고, 고동시성 온라인 디코딩을 위한 오버랩 스케줄링을 추가했으며, 노옵(no-op) EAGLE 정규화를 제거하고 EAGLE 프리필 중에 호스트 동기화를 피했다.
    3. 공개된 리소스 임대 스케줄링 작업과 데이터 병렬 그래프 메타데이터 수정은 동일한 노력을 계속하며, 요청이 단순히 완료될 때까지 실행되는 것이 아니라 철회되고 재개될 수 있을 때 오버랩을 안전하게 만드는 것이다.

### 12.4. 이기종 프리필/디코드 토폴로지 및 정확성 문제 해결
1. **접두사 인식 스테이징의 필요성**
    1. 이기종 프리필 및 디코드 토폴로지에서는 접두사 인식 스테이징이 필요하며, 여기서 접두사 캐싱과 분산이 제대로 상호작용하지 않는다.
    2. 양쪽이 동일하게 샤딩되지 않으면, 하나의 논리적 요청에 대한 KV는 몇 개의 큰 연속 영역이 아니라 수천 개의 작은 스트라이드 조각이 되며, 각 조각은 자체 전송 디스크립터가 된다.
    3. 이동되는 바이트는 변경되지 않지만, 디스크립터당 오버헤드가 폭발적으로 증가하며, 이는 중요한 긴 프롬프트에서 최악의 방식으로 발생한다.
    4. 수정된 멀티풀 매핑과 청크 NIXL 바운스 경로는 이러한 조각을 제한된 재사용 가능한 아레나를 통해 통합하여, 추가 스테이징 복사를 수십 배 적은 디스크립터와 교환한다.
    5. AgentX 진단은 동시성 5에서 요청 중요 KV p99를 26.74초에서 125ms로
