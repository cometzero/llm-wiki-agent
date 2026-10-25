---
title: 'Inside GLM-5.3: How Sparse Attention Affects DRAM Memory TAM'
origin: lilys_ai
lilys_project_id: 11568519
lilys_project_url: https://lilys.ai/digest/11568519
lilys_created_at: '2026-10-01T14:50:50.256Z'
lilys_collection: ''
source_type: webPage
lilys_note_id: '13680887'
sources:
- id: '115664'
  source_type: webPage
  url: https://newsletter.semianalysis.com/p/sparse-savings-persistent-demand-inside-glm53
  title: How GLM5.3 Sparse Attention Affects HBM Memory Usage
  status: ready
---

# Inside GLM-5.3: How Sparse Attention Affects DRAM Memory TAM

## LilysAI note

> GLM5.3의 **희소 어텐션(Sparse Attention)**은 HBM 메모리 사용에 어떤 영향을 미치는가? 희소 어텐션은 SDPA 연산 시 메모리 및 대역폭 요구량을 줄이지만, 전체 메모리 용량 사용량은 줄이지 못하며, **HiSparse와 같은 시스템 최적화**를 통해 이러한 한계를 극복할 수 있습니다.

## 1. GLM5.3 희소 어텐션의 HBM 메모리 사용 영향[^1]

![A diagram illustrating how sparse attention, while reducing memory and bandwidth for SDPA operations, fails to reduce overall HBM memory capacity usage, and how system optimizations like HiSparse bridge this gap by offloading KV cache entries from HBM to DRAM.](https://resource.lilys.ai/images/genimg_48341d56513a3b22.png)

GLM5.3의 희소 어텐션은 SDPA 연산 시 메모리 및 대역폭 요구량을 줄이지만, 전체 메모리 용량 사용량은 줄이지 못하며, HiSparse와 같은 시스템 최적화를 통해 이러한 한계를 극복할 수 있다.

### 1.1. 희소 어텐션의 메모리 사용 한계 및 HiSparse의 역할[^2]

1. **희소 어텐션의 메모리 효율성 한계**[^3]
   1. 희소 어텐션은 가장 관련성이 높은 상위 K개 토큰에만 집중하여, 핵심 SDPA(Scaled Dot-Product Attention) 연산 중 메모리 소비와 대역폭 요구 사항을 줄인다.[^4]
   2. 그러나 이러한 효율성 개선이 실제 전체 메모리 절약으로 이어지지 않는다.[^5]
   3. 상위 K개 토큰을 선택하는 작업은 일반적으로 전체 컨텍스트가 HBM에 있어야 하므로, 희소 어텐션은 메모리 용량 병목 현상을 해결하지 못한다.[^6]

<img src="https://substackcdn.com/image/fetch/$s_!1i4c!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cd044d2-888a-4569-97ea-5354b07e4f62_1600x900.png">

희소 어텐션 처리량은 메모리 용량에 의해 병목 현상이 발생한다. 출처: HiSparse

2. **HiSparse를 통한 한계 극복**[^7]
   1. SGLang 팀은 이러한 한계를 극복하기 위해 KV 캐시 항목을 장치 HBM에서 호스트 DRAM으로 사전에 오프로드하는 계층적 메모리 시스템인 HiSparse를 설계했다.[^8]
   2. HiSparse는 LRU(Least Recently Used) 캐시처럼 작동하며, 상위 K개 선택 캐시 미스 발생 시 DRAM에서 HBM으로 토큰을 로드하고, LRU 제거 정책에 따라 HBM에서 DRAM으로 토큰을 오프로드한다.[^9]
   3. 캐시 미스 지연 시간을 줄이기 위해 HiSparse는 이전 작업인 HiCache에서 도입된 계층별 오버래핑(layer-wise overlapping)을 통해 N-1 계층 실행과 N 계층의 KV 캐시 로딩을 중첩시킨다.[^10]
   4. HiSparse를 통해 SGLang은 상위 K개 캐시 미스 I/O 오버헤드를 대가로 높은 동시성 및 긴 컨텍스트 시나리오에서 처리량을 크게 향상시킨다.[^11]
3. **희소 어텐션과 시스템 최적화의 관계**[^12]
   1. 희소 어텐션은 SDPA 연산에서 KV 캐시 메모리 및 대역폭 요구 사항을 줄이지만, 전체 메모리 용량 사용량을 줄이지는 못한다.[^13]
   2. HiSparse는 시스템 최적화를 통해 희소 어텐션의 메모리 용량 한계를 극복할 수 있음을 보여주므로, 희소 어텐션 메모리 프로파일만으로는 시스템 KV 캐시 효율성의 전체 그림을 충분히 설명할 수 없다.[^14]
   3. 희소 어텐션 모델 서비스에 대한 보다 전체적인 그림을 제공하기 위해 Z.ai의 GLM-5 모델 시리즈 설계와 실제 서비스 방식을 설명한다.[^15]

## 2. GLM5.3 에이전트 추론 서비스[^16]

GLM5.3 에이전트 추론 서비스는 InferenceX 벤치마크를 통해 GB300 및 GB200과 MI355X ATOM 간의 비용 효율성과 성능을 비교하며, 특히 에이전트 워크로드에서 캐시 재사용의 중요성을 강조한다.

### 2.1. InferenceX 벤치마크를 통한 비용 및 성능 분석[^17]

1. **GB300의 비용 효율성**[^18]
   1. 실시간 벤치마크 보드 InferenceX에서 GB300은 초당 150토큰의 응답 속도로 가장 낮은 모델링 서비스 비용을 제공한다.[^19]
   2. GB300은 GPU당 더 많은 토큰을 처리하며, 시간당 비용이 높음에도 불구하고 비용 효율성 면에서 GB200보다 앞선다.[^20]
   3. GB300 결과는 Dynamo-TRT-LLM을 사용하고, GB200 결과는 Dynamo-SGLang을 사용한다.[^21]
2. **벤치마크 측정 기준**[^22]
   1. GLM-5.3의 서비스 영향을 설명하기 위해 9월 28일 AgentX 스냅샷 결과를 사용한다.[^23]
   2. 비용은 하이퍼스케일러 규모에서 인프라를 소유하고 운영하는 InferenceX 모델을 사용하여 추정한다.[^23]
   3. 총 토큰에는 입력 및 생성된 출력, 그리고 턴(turn) 간 재사용되는 캐시된 입력 기록이 포함된다.[^24]
   4. 스트리밍 속도는 p90 상호작용을 사용하여 측정하며, 첫 토큰까지의 시간은 별도로 평가한다.[^25]
3. **GB200과 MI355X ATOM의 비용 비교**[^26]
   1. 초당 150토큰에서 GB200은 백만 총 토큰당 약 $0.044의 비용이 들며, MI355X ATOM의 $0.049에 비해 약 12% 낮은 비용을 보인다.[^27]
   2. 이 값들은 정확히 초당 150토큰에서의 별도 테스트가 아닌, 측정된 곡선에서 추정된 값이다.[^28]
   3. 이 비교를 위해 하이퍼스케일러 규모에서 인프라를 소유하고 운영하는 InferenceX의 추정 비용을 사용한다.[^29]
   4. 총 토큰에는 입력 및 생성된 출력, 그리고 캐시에서 재사용된 입력 기록이 포함된다.[^30]

<img src="https://substackcdn.com/image/fetch/$s_!YLxK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd794226-78c0-4143-8b48-f632a507f676_2700x1900.png">

출처: InferenceX | SemiAnalysis

### 2.2. GPU별 성능 및 비용 효율성 비교[^31]

1. **GB300과 GB200의 처리량 및 비용 상충 관계**[^32]
   1. Dynamo-SGLang 결과 중 GB300은 GPU당 초당 약 13950 총 토큰을 처리하여 GB200의 11873 총 토큰 대비 17.5%의 처리량 우위를 보인다.[^32]
   2. 그러나 GB300의 시간당 GPU 비용은 $2.31인 반면 GB200은 $1.86으로, GB300의 높은 시간당 비용이 처리량 우위를 상쇄한다.[^32]
2. **AMD와 GB200의 비용 비교**[^33]
   1. AMD와 비교했을 때, ATOM은 초당 100토큰에서 GB200보다 약 13% 저렴하다.[^34]
   2. GB200은 초당 125토큰에서 약 5% 저렴하고, 초당 150토큰에서 약 12% 저렴하다.[^35]
   3. 이 세 가지 목표에서 어느 시스템도 일관된 비용 우위를 보이지 않는다.[^35]
3. **에이전트 워크로드에서의 비용 분석**[^36]
   1. 생성된 출력만 고려할 때, GB200은 초당 150토큰의 응답 속도에서 백만 출력 토큰당 $5.92의 비용이 들며, 이는 MI355X ATOM의 $6.68보다 약 11% 저렴하다.[^37]
   2. 이 지표는 에이전트가 긴 입력 기록을 반복적으로 재사용하면서 상대적으로 적은 새 텍스트를 생성하는 에이전트 워크로드에서 비용을 분석하는 데 유용하다.[^38]

<img src="https://substackcdn.com/image/fetch/$s_!YLxK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd794226-78c0-4143-8b48-f632a507f676_2700x1900.png">

출처: InferenceX | SemiAnalysis

4. **첫 토큰까지의 시간(TTFT)을 고려한 비교**[^39]
   1. 초당 150토큰 목표 전후의 GB200 측정값은 p90 TTFT가 약 14~19초인 반면, MI355X ATOM은 약 1.1~1.2초이다.[^40]
   2. 일부 GB200의 최저 비용 실행은 첫 토큰까지 훨씬 더 긴 대기 시간을 가진다.[^41]
   3. 따라서 실제로 테스트되었고 p90 TTFT가 최대 2초 이내로 초당 150토큰 이상을 달성한 구성만을 사용하여 두 번째 비교를 수행한다.[^42]
   4. 아래 차트는 MI355X ATOM이 백만 총 토큰당 $0.0607, B200 Dynamo-SGLang이 $0.0666임을 보여준다.[^43]
   5. 2초 첫 토큰 제한을 적용하면 ATOM이 약 9% 더 저렴하다.[^44]
   6. 제한을 10초로 완화하면 Dynamo-TRT-LLM을 사용하는 GB300이 $0.0451로 적격이 되며, ATOM의 $0.0607보다 약 26% 저렴하다.[^45]

<img src="https://substackcdn.com/image/fetch/$s_!591h!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2a4b342-0525-4274-af86-3e6d5e9f7fa8_2700x1800.png">

출처: InferenceX | SemiAnalysis

## 3. GLM5.3의 최적화 및 아키텍처[^46]

GLM5.3은 메모리 요구 사항을 줄이기 위한 최적화, TileRT를 통한 저지연 추론, DeepSeek Sparse Attention(DSA)의 라이트닝 인덱서와 희소 MLA를 활용하여 효율성을 높인다.

### 3.1. GLM5.3의 메모리 최적화[^47]

1. **KV 압축 및 희소 어텐션**[^48]
   1. GLM 5.2/5.3 모델의 어텐션 아키텍처는 메모리 요구 사항을 줄이며, 장기 실행 에이전트는 이전 대화 기록을 유지해야 한다.[^49]
   2. GLM은 두 가지 방법으로 이 기록 처리 비용을 줄인다.
      1. KV 압축: 토큰당 캐시된 상태를 줄인다.[^50]
      2. 희소 어텐션: 각 어텐션 연산이 읽는 상태의 양을 줄인다.[^50]
   3. 그런 다음 서비스 엔진은 캐시를 저장할 위치와 효율적으로 검색할 방법을 결정한다.[^51]
2. **GPU 및 호스트 메모리 재사용**[^52]
   1. B200 결과는 GPU 메모리 외부에서 얼마나 많은 재사용이 일어날 수 있는지를 보여준다.[^53]
   2. 동시 요청 수가 8개에서 16개로 증가하면 GPU 메모리에서 재사용되는 프롬프트 토큰의 비율이 90.3%에서 54.8%로 감소한다.[^54]
   3. 이 재사용의 상당 부분이 호스트 메모리로 이동하여 6.0%에서 40.3%로 증가한다.[^55]
   4. GPU 캐시 감소의 대부분은 호스트 메모리 재사용으로 상쇄되어 모든 동시성 수준에서 전체 캐시 적중률을 95% 이상으로 유지한다.[^56]
3. **서비스 엔진 실행 최적화**[^57]
   1. 캐시 관리 외에도 서비스 엔진이 프리필(prefill) 및 디코딩을 실행하는 방식의 변경도 성능을 변화시킬 수 있다.[^58]
   2. 두 가지 GLM-5.2 연구가 이를 보여준다.[^59]
      1. vLLM은 첫 번째 디코딩 단계를 일관된 CUDA 그래프 실행 경로에 유지하여 NVFP4 연구에서 평균 TPOT(출력 토큰당 시간)를 약 40ms에서 22ms로 줄였다.[^60]
      2. 다른 8 MI355X 장기 컨텍스트 워크로드에서 ATOM 엔진은 파이프라인 단계에 걸쳐 프리필을 청크(chunk)로 처리하여 총 처리량을 98% 높이고 중앙값 TTFT를 28.6초에서 8.7초로 줄였다.[^61]

### 3.2. TileRT를 통한 저지연 LLM 추론[^62]

1. **TileRT의 특징**[^63]
   1. GLM5.3의 TileRT는 AMD MI355X를 먼저 지원했다.[^64]
   2. TileRT는 디코딩을 단일 영구 커널로 컴파일하여 시작 오버헤드를 줄이고 계산, 메모리 접근 및 통신을 중첩시키는 저지연 LLM 추론 엔진이다.[^65]
   3. TileRT는 최대 배치 처리량보다는 사용자당 더 빠른 토큰 생성을 우선시하며, vLLM은 프리필을 처리한다.[^66]

<img src="https://substackcdn.com/image/fetch/$s_!IlqS!,w_140,h_140,c_fill,f_webp,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F735bcccf-dfa2-41ea-85f6-131b781511cc_1376x768.png">

NVIDIA GPU에서 초고속 상호작용? - TileRT InferenceX

2. **AgentX에서의 성능 향상**[^67]
   1. AgentX에서 FP8 TileRT MI355X는 최고의 FP4 MI335X 구성보다 2배의 P90 상호작용을 달성한다.[^68]
   2. GB300 NVL72와 비교하여 상호작용에서 40% 향상을 가져온다.[^69]
   3. 이러한 서비스 지표는 이전에는 특수 하드웨어가 필요했다.[^70]

<img src="https://substackcdn.com/image/fetch/$s_!3tYc!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22959305-42e4-48ef-afb2-913f9474f339_1582x1450.png">

출처: SemiAnalysis

3. **향후 개발 여지**[^71]
   1. 그러나 TTFT는 최적화되지 않았으며, KV 전송 최적화, FP4 지원, 더 큰 배치 크기 등 개발 여지가 남아있다.[^71]

### 3.3. DeepSeek Sparse Attention (DSA)[^72]

1. **GLM-5 모델의 DSA 적용**[^73]
   1. GLM-5(및 GLM-5.x 모델)는 총 744B, 활성 매개변수 40B의 Mixture-of-Experts 모델이다.[^74]
   2. 모든 토큰에 대해 1개의 공유 전문가를 가지며 256개 전문가 중 8개를 통해 라우팅되어 희소성(sparsity)이 32이다.[^75]
   3. 이 모델은 DeepSeek V3.2에서 소개된 DeepSeek Sparse Attention(DSA)을 특징으로 한다.[^76]
2. **DSA의 두 가지 구성 요소**[^77]
   1. **라이트닝 인덱서(Lightning Indexer)**: 상위 K개 토큰을 선택한다.[^77]
   2. **희소 다중 잠재 어텐션(Sparse Multi-Latent Attention, MLA)**.[^77]

### 3.4. 라이트닝 인덱서[^78]

1. **라이트닝 인덱서의 기능**[^79]
   1. 라이트닝 인덱서는 경량 어텐션 메커니즘과 기능적으로 유사하다.[^80]
   2. 쿼리와 키는 더 낮은 차원으로 투영되며, 인덱서 쿼리는 멀티 헤드이고 인덱서 키는 싱글 헤드이다.[^81]
   3. 상위 K개 토큰 선택을 위해 쿼리-키 관계 점수(로짓)만 필요하므로, 인덱서는 값 임베딩이나 정규화된 로짓을 위한 소프트맥스 연산이 필요 없다.[^82]
   4. 대신 쿼리-키 내적을 계산한 후 ReLU 비선형성을 적용한다.[^83]
   5. 인덱서는 모든 쿼리 헤드에 걸쳐 로짓의 가중 합으로 각 토큰의 인덱서 점수를 계산하며, 이를 사용하여 상위 K개 토큰을 선택한다.[^84]
   6. 이는 인덱서가 여러 헤드를 가짐에도 불구하고 토큰 선택이 여러 어텐션 헤드에 걸쳐 공유됨을 의미한다.[^85]
   7. 상위 K개 토큰을 선택할 때, K개 미만의 토큰에 집중하는 쿼리는 밀집 어텐션으로 유지하고, 그렇지 않으면 상위 K개를 선택한다.[^86]

<img src="https://substackcdn.com/image/fetch/$s_!-FZf!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3abe0c5-92c8-4912-ad2b-1b5ba3753580_1404x682.png">

라이트닝 인덱서의 개념적 예시. 출처: SemiAnalysis

<img src="https://substackcdn.com/image/fetch/$s_!n_SD!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F375d0869-c668-4145-bf66-3b019701c834_2048x2048.png">

인덱서 점수는 모든 인덱서 쿼리 헤드의 가중 합이다. 출처: SemiAnalysis

### 3.5. 희소 MLA (Multi-Latent Attention)[^87]

1. **MLA의 두 가지 모드**[^88]
   1. MLA는 MHA(Multi-Head Attention) 모드와 MQA(Multi-Query Attention) 모드의 두 가지 모드로 작동한다.[^89]
   2. 두 모드 모두 장단점이 있다.
      1. MHA 모드: FLOPs는 낮지만 메모리 비용이 42배 높다.[^90]
      2. MQA 모드: 메모리 비용은 낮지만 FLOPs가 최대 3.4배 높다.[^90]
2. **DSA의 MQA 모드 활용**[^91]
   1. DSA는 희소 어텐션이 더 적은 토큰에 집중하므로 높은 FLOP 사용량을 완화할 수 있어 MQA 모드를 사용한다.[^91]
3. **시퀀스 길이에 따른 효율성 변화**[^92]
   1. 실제로는 MHA 모드가 MQA 모드보다 효율적인 시퀀스 길이 임계값이 존재한다.[^93]
   2. 짧은 시퀀스 길이에서는 메모리 로딩 시간이 지배적이지 않아 FLOPs가 낮은 MHA 모드가 유리할 수 있다.[^94]
   3. vLLM은 이 기능을 구현하여 데이터 병렬의 경우 시퀀스 길이 2K에서 약 5K까지, 텐서 병렬의 경우 2K에서 약 77K까지 MHA 모드를 구성한다.[^95]
   4. 최소 2K는 상위 K가 2048이기 때문이며, 2K 미만의 어텐션은 밀집 어텐션이다.[^96]

### 3.6. MLA 수정 사항[^97]

1. **GLM-5와 DeepSeek V3.2의 MLA 차이점**[^98]
   1. GLM-5와 DeepSeek V3.2의 MLA 차원 구성을 비교하면, 가장 눈에 띄는 차이점은 **쿼리 헤드 수**와 **쿼리 키 헤드 차원**이다.[^99]

<img src="https://substackcdn.com/image/fetch/$s_!qpBS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0857f2d-5a6a-45a5-accd-3ec332737582_1258x204.png">

출처: SemiAnalysis

2. **H800 루프라인에 따른 쿼리 헤드 수 결정**[^100]
   1. GLM-5 기술 보고서는 DeepSeek이 H800의 루프라인에 따라 쿼리 헤드 수를 선택했다고 언급한다.[^101]
   2. 이는 디코딩 중 MLA의 SDPA 산술 강도가 H800의 릿지 포인트(ridge point)에 대략적으로 위치한다는 것을 의미한다.[^101]
   3. 다음 가정을 따른다.[^102]
      1. `L`: 시퀀스 길이[^103]
      2. `d`: 헤드 차원[^104]
      3. `r`: RoPE 차원[^105]
      4. `H`: 헤드 수[^106]
      5. `b`: 매개변수당 바이트 수[^107]
   4. MQA 모드에서 FLOPs는 다음과 같다.[^108]
   5. 로드된 메모리는 다음과 같다.[^109]
   6. 따라서 산술 강도는 다음과 같다.[^110]
   7. DeepSeek V3.2 구성(`d` = 512, `r` = 64, `b` = 2)을 대입하면 다음과 같다.[^111]
   8. H800의 실제 산술 강도는 258.2 FLOP/B이며(DeepSeek에 따르면 실제 최고 865 TFLOP/s, 3.35 TB/s 대역폭), 공식에 대입하면 `H` ~= 128이 나온다.[^112]
3. **GLM-5의 하드웨어 최적화**[^113]
   1. GLM-5가 쿼리 헤드 수가 절반인 H = 64를 가진다는 사실은 GLM-5가 다른 하드웨어에 최적화되었음을 시사한다.[^114]
   2. GLM-5의 구성(`d` = 512, `r` = 64, `b` = 2, `H` = 64)을 대입하면 산술 강도는 120.8 FLOP/B가 나온다.[^115]
   3. 따라서 GLM-5는 약 128 FLOP/B인 Moore Threads MTT S4000에 최적화되었을 것으로 추정된다.[^116]
   4. Moore Threads와 Z.ai의 협력(예: GLM-5.3-Flash 출시 당일 지원)이 이 이론을 뒷받침한다.[^117]
4. **QK NoPE 차원 증가**[^118]
   1. GLM-5는 QK NoPE 차원을 128에서 192로 증가시켰는데, 이는 iso-FLOP 및 iso-매개변수 제약 조건에서 이 구성이 더 우수하다는 연구 결과에 따른 것이다.[^119]
   2. 이는 SDPA 헤드 차원을 192에서 256으로 증가시키지만, 헤드 수 감소를 고려하면 여전히 33%의 FLOP 감소 효과가 있다.[^120]

### 3.7. IndexShare[^121]

1. **IndexShare의 도입 배경 및 기능**[^122]
   1. 컨텍스트가 길어질수록 인덱서의 지연 시간 비용이 무시할 수 없게 된다.[^123]
   2. 이 비용을 완화하기 위해 Z.ai는 GLM-5.2에서 IndexShare(일명 IndexCache)를 제안했으며, 이는 4개의 DSA 계층이 하나의 인덱서를 공유하는 방식이다.[^124]

<img src="https://substackcdn.com/image/fetch/$s_!gPFQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1afc9d13-969e-449a-91d1-cd3b310c779a_944x654.png">

30B DSA 모델의 다양한 컨텍스트 길이에 따른 지연 시간 비용. 출처: IndexCache

2. **IndexShare의 훈련 및 추론 복잡성**[^125]
   1. IndexShare는 훈련 및 추론에 복잡성을 추가한다.[^126]
   2. 표준 DSA 훈련은 두 단계로 이루어진다.
      1. 밀집 웜업(dense warm-up) 단계: 인덱서를 제외한 모든 모델 가중치가 고정되고 어텐션 계산이 밀집 방식으로 이루어진다.[^127]
      2. 희소 적응(sparse adaptation) 단계: 전체 모델이 희소 어텐션으로 훈련된다.[^127]

<img src="https://substackcdn.com/image/fetch/$s_!0XK_!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88c2f29b-e00a-4240-92a0-2a1c30c7ee15_1258x264.png">

출처: SemiAnalysis

3. 훈련 목표 측면에서 인덱서는 KL 발산 목표를 사용하여 어텐션 헤드 점수의 합과 정렬되도록 훈련된다.[^128]
4. IndexShare는 훈련 목표를 공유 계층에 걸쳐 어텐션 점수의 평균 분포와 인덱서 로짓 분포를 정렬하는 방식으로 조정한다.[^129]
5. 추론의 경우, 일반적으로 인덱서는 어텐션 캐시 KV처럼 키를 캐시한다.[^130]
6. 여러 계층이 하나의 인덱서를 공유하므로, 공유 계층에서 상위 K 선택 정보를 재사용하기 위해 전체 계층에서 상위 K 인덱스를 추가로 캐시해야 한다.[^131]
7. **IndexShare의 성능 향상**[^132]
   1. 이 설계는 인덱서 캐시를 75% 줄이고, 인덱서 FLOPs를 75% 줄이며, 다양한 컨텍스트 길이와 프리필/디코딩에서 처리량을 1.5배에서 1.8배 향상시킨다.[^132]

<img src="https://substackcdn.com/image/fetch/$s_!J1l1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff70d8106-0784-4721-b55f-e2285ce91f6d_2048x629.png">

기준선 대비 GLM-5.2 구성(빨간색) (30B DSA 모델). 출처: IndexCache

## 4. GLM-5의 후처리 설계 및 RL 훈련 알고리즘[^133]

GLM-5의 후처리 파이프라인은 SFT와 세 가지 RL 훈련 단계, 그리고 교차 단계 증류를 포함하며, 동기 및 비동기 RL 단계에 따라 다른 알고리즘과 최적화 기법을 적용한다.

### 4.1. GLM-5 후처리 파이프라인[^134]

1. **파이프라인 구성**[^135]
   1. 사전 훈련 및 중간 훈련 후, GLM-5의 후처리 파이프라인은 지도 미세 조정(SFT)으로 시작하여, **세 가지 RL 훈련 단계**(추론 RL, 에이전트 RL, 일반 RL)를 거치고, **온-정책 교차 단계 증류**로 마무리된다.[^135]
   2. 이 증류는 추론 및 일반 RL을 SFT 체크포인트로 다시 증류한다.[^135]

<img src="https://substackcdn.com/image/fetch/$s_!-nRK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2665b55-e60e-4d73-ac0f-68b93e205460_2048x1432.png">

GLM-5 후처리 파이프라인. 출처: SemiAnalysis

2. **파이프라인 세부 사항**[^136]
   1. **추론 RL 모델 훈련**: 추론 RL 모델은 전적으로 온-정책(on-policy)으로 훈련되며, 이는 동기적으로 훈련됨을 의미한다.[^137]
      1. 동기 RL 훈련은 시스템 효율성은 낮지만 RL 훈련 안정성은 높다.[^138]
   2. **온-정책 교차 단계 증류**: 이는 다중 교사 온-정책 증류(MOPD)와 유사하며, 학생 모델이 여러 교사 모델에 대해 온-정책 증류로 RL 훈련된다.[^139]
      1. MOPD의 목표는 전문가 교사 모델을 하나의 모델로 병합하는 것이지만, GLM-5는 모델이 새로운 기능을 학습할 때 발생하는 기존 기능 손실을 복구하는 데 더 중점을 두는 것으로 보인다.[^140]
      2. 이 가정에 따르면, Z.ai가 세 가지 RL 체크포인트 모두를 사용하지 않고 추론 및 일반 RL 체크포인트만 교사로 사용하는 이유는 불분명하다.[^141]
3. **GLM-5.2의 변경 사항**[^142]
   1. 발표 블로그 게시물에 따르면, GLM-5.2는 온-정책 교차 단계 증류를 Z.ai가 병렬 OPD 훈련이라고 명명한 표준 MOPD 파이프라인으로 대체했을 수 있다.[^143]
   2. Z.ai는 이 방식의 규모와 훈련 효율성을 강조하며, 10개 이상의 전문가 모델을 약 이틀 만에 최종 모델로 병합했다고 밝혔다.[^144]

### 4.2. RL 훈련 알고리즘[^145]

1. **동기 및 비동기 RL 단계별 알고리즘**[^146]
   1. Z.ai는 동기 및 비동기 RL 단계에 따라 다른 RL 알고리즘을 채택한다.[^146]
2. **동기 RL 단계의 GRPO 기반 알고리즘**[^147]
   1. 동기 RL 단계에서는 GRPO(Group Relative Policy Optimization) 기반 RL 알고리즘에 현대적인 적응을 적용한다.[^148]
   2. 주요 적응 사항은 다음과 같다.
      1. **KL 정규화 항 제거**: 시스템 효율성을 개선하고 더 적극적인 기울기 업데이트를 허용한다.[^149]
      2. **IcePop**: 훈련-추론 불일치 비율을 기반으로 토큰 수준 마스킹을 적용한다.[^150]
      3. **Clip-Higher**: 탐색을 장려하기 위해 중요도 샘플링 비율에 더 높은 최대 임계값을 사용한다.[^151]
3. **비동기 RL 단계의 REINFORCE 유사 알고리즘**[^152]
   1. 대조적으로, Z.ai는 비동기 RL 단계에 REINFORCE와 유사한 RL 알고리즘을 사용하며, 직접 양면 중요도 샘플링(DIS)과 IcePop과 유사한 클리핑 메커니즘을 추가한다.[^153]
   2. 아래는 두 RL 단계의 토큰 수준 목표를 비교한 것이다.[^154]

<img src="https://substackcdn.com/image/fetch/$s_!gNw1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feab874c6-4338-4a58-b394-8de2794966dd_2048x472.png">

두 RL 단계의 토큰 수준 목표. 출처: SemiAnalysis

4. **중요도 샘플링(IS) 비율 비교**[^155]
   1. IS 비율은 현재 정책과 행동 정책 하에서 각 샘플링된 행동의 확률을 비교하여, 각 행동이 훈련 목표에 기여하는 정도를 조절한다.[^156]
   2. 동기 RL 단계는 행동 정책으로 이전 반복의 트레이너 정책을 활용하는 반면, 비동기 RL 단계는 추론 정책을 활용한다.[^157]
   3. 비동기 훈련 설정에서는 롤아웃 중에 정책 업데이트가 여러 번 발생하므로, IS 비율을 계산하기 위해 그 사이의 모든 체크포인트 버전이 필요하다.[^158]
   4. 그러나 이는 높은 메모리 및 지연 시간 오버헤드로 인해 실현 불가능하다.[^159]
   5. 결과적으로 Z.ai는 수치적 안정성 문제의 대가로 효율성과 단순성을 위해 추론 정책을 사용한다.[^160]

<img src="https://substackcdn.com/image/fetch/$s_!VIZ-!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb5823b7-0ac8-4326-af4f-5e3b3829f100_1654x484.png">

두 RL 단계의 IS 비율. 출처: SemiAnalysis

5. **어드밴티지 계산의 주요 차이점**[^161]
   1. RL 훈련, 교차 증류 및 장기 RL 훈련에서 어드밴티지 계산의 주요 차이점을 강조한다.[^162]
   2. RL 훈련은 GRPO 표준 그룹 정규화 어드밴티지를 사용하고, 교차 증류는 역 KL 발산을 사용한다.[^163]

<img src="https://substackcdn.com/image/fetch/$s_!7JkY!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F855b6009-e0d8-4e01-bab5-d6abfdd5849b_2048x479.png">

어드밴티지 계산 비교. 출처: SemiAnalysis

### 4.3. 단일 롤아웃 비동기 최적화 (SAO)[^164]

1. **SAO 도입 배경**[^165]
   1. 장기 작업은 매우 긴 궤적을 생성하며, GRPO 컨텍스트에서 궤적 길이의 높은 분산은 불안정한 훈련 신호를 생성하여 더 긴 궤적으로 편향될 수 있다.[^166]
   2. 더욱이 RL 롤아웃 워크로드는 종단 간 지연 시간에 민감하므로, 장기 작업의 경우 지연 롤아웃의 꼬리 지연 시간이 악화된다.[^167]
2. **SAO의 해결책**[^168]
   1. 이 문제를 완화하기 위해 Z.ai는 GLM-5.2에서 장기 RL 훈련을 위한 단일 롤아웃 비동기 최적화(SAO)를 도입했다.[^169]
   2. SAO는 그룹 정규화 어드밴티지를 PPO(Proximal Policy Optimization)에서 영감을 받은 수정된 GAE(Generalized Advantage Estimation)로 대체한다.[^169]
   3. GAE는 어드밴티지를 계산하기 위해 단일 롤아웃만 필요하다.[^170]
   4. 이는 프롬프트당 여러 롤아웃을 수행할 필요성을 제거하여 GRPO의 단점을 완화한다.[^171]

<img src="https://substackcdn.com/image/fetch/$s_!1MnE!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29bbbf45-36e4-470f-be0c-092db886317d_1255x669.png">

생성기 노드가 트레이너 노드에게 롤아웃 완료를 기다리도록 요청한다. 출처: SAO

3. **SAO의 GAE 적응**[^172]
   1. GAE는 값 모델에 의해 추정된 값(RL 용어로 현재 상태의 예상 수익)으로 계산된다.[^173]
   2. 구체적으로, 값 모델은 롤아웃을 입력으로 받아 모든 토큰에 대한 값 추정치를 생성한다.[^174]
   3. SAO는 관찰 토큰(즉, 도구 호출 결과)을 최적화에서 제거하여 GAE를 에이전트 RL 훈련에 적용한다.[^175]
   4. 이전 GLM-5에서는 토큰을 건너뛰는 것으로 충분했지만, SAO에서는 관찰 토큰을 우회하도록 어드밴티지 추정 공식을 수정한다.[^176]
   5. 벨만 목표 및 어블레이션에 대한 더 많은 직관은 SAO 논문 및 부록 A.1을 참조한다.[^177]
4. **값 모델 훈련 기술**[^178]
   1. SAO에서 값 모델은 정책 모델과 동시에 훈련되는 별도의 LLM이다.[^179]
   2. 이는 약한 값 모델로 인해 훈련 초기 단계에서 어드밴티지 계산의 높은 분산에 취약하다.[^180]
   3. 이를 해결하기 위해 SAO는 값 모델 훈련을 위한 여러 기술을 제안한다.[^181]
      1. **두 시간 척도 업데이트 규칙(Two Time-scale Update Rule)**: 정책 모델보다 두 배 자주 값 모델을 업데이트한다. 이는 모든 정책 훈련 단계에서 각 데이터 배치에 대해 두 번 훈련함을 의미한다.[^182]
      2. **어텐션 매개변수 고정(Attention Parameter Freezing)**: 훈련 안정성을 개선하기 위해 값 모델의 전체 어텐션 계층을 고정한다.[^183]
      3. **사전 훈련 스케일링(Scaling Pre-training)**: 값 모델을 초기화하기 위해 값 모델 사전 훈련 코퍼스를 스케일링하여, 훈련 초기 단계에서 값 모델이 값을 견고하게 추정할 수 있도록 한다. Z.ai는 사전 훈련 코퍼스의 스케일링 정보를 공개하지 않았다.[^184]

<img src="https://substackcdn.com/image/fetch/$s_!YbQd!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb83b1151-c583-4cb6-bd89-a247fb7f4f92_335x597.png">

출처: SemiAnalysis

5. **SAO의 장점**[^185]
   1. 계산 오버헤드와 메모리 사용량 두 배 증가를 대가로 SAO는 그룹별 샘플링을 값 모델로 대체하여 GRPO의 지연 시간 문제를 완화한다.[^185]

## 5. GLM-5의 후처리 인프라[^186]

GLM-5는 slime 프레임워크를 기반으로 다중 작업 롤아웃 오케스트레이터를 통해 효율적인 RL 훈련을 지원하며, IndexShare를 통해 동적 교사 모델 전환 및 프리페칭 기능을 제공한다.

### 5.1. slime 기반 후처리 인프라[^187]

1. **slime 프레임워크 활용**[^188]
   1. Z.ai는 모든 GLM-5 모델 전반에 걸쳐 최고의 오픈 소스 RL 훈련 프레임워크 중 하나인 slime을 후처리 인프라로 사용한다.[^189]
   2. slime의 설계 및 기능에 대한 자세한 내용은 slime GitHub 리포지토리를 참조하며, 여기서는 두 가지 주요 기능을 강조한다.[^190]
2. **서버 기반 다중 작업 롤아웃 오케스트레이터**[^191]
   1. RL 롤아웃의 성능 특성은 작업에 따라 크게 다르며, 각 작업에는 다른 도구와 보상 함수가 필요하다.[^192]
   2. 시스템 효율성을 보장하기 위해 Z.ai는 서버 기반 다중 작업 롤아웃 오케스트레이터를 설계했다.[^193]
   3. 각 작업은 독립적인 마이크로서비스 서버 역할을 하여 롤아웃 및 보상 로직을 제어한다.[^194]
   4. 오케스트레이터는 작업별 롤아웃 비율과 생성 속도를 제어하여 전체 성능의 균형을 맞춘다.[^195]
   5. 중앙 집중화는 또한 작업 전반에 걸친 동적 비율 조정, 세분화된 진행 상황 모니터링 등을 가능하게 한다.[^196]
   6. Z.ai는 GLM-5 훈련 시 오케스트레이터가 1000개의 동시 롤아웃을 지원한다고 주장한다.[^197]

<img src="https://substackcdn.com/image/fetch/$s_!u9lu!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F749e2de3-ef84-4776-864e-846243d30d9e_2048x1039.png">

다중 작업 롤아웃 오케스트레이터의 아키텍처 다이어그램. 출처: SemiAnalysis

### 5.2. 동적 교사 모델 전환 및 프리페칭[^198]

1. **GLM-5.3의 로컬 저장소 활용**[^199]
   1. GLM-5.3 발표 블로그 게시물에서 Z.ai는 호스트 메모리 외에 로컬 저장소를 캐시 계층으로 사용하여 MOPD를 위한 동적 교사 모델 전환 및 프리페칭을 가능하게 한다고 주장한다.[^199]
2. **slime PR#1538의 구현**[^200]
   1. slime PR#1538은 TensorBackuper 클래스를 도입하여 교사 가중치를 CPU 메모리에 고정된 PyTorch 텐서로 저장함으로써 교사 전환을 구현한다.[^201]
   2. 롤아웃이 교사로 라우팅되면 TensorBackuper 객체가 교사 모델을 GPU 메모리로 다시 복사하여 순방향 패스를 수행한다.[^202]
   3. 그러나 이는 CPU 기반 가중치 스와핑이며, 저장소 기반 구현은 아직 확인되지 않았다.[^203]

[^1]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "How GLM5.3 Sparse Attention Affects HBM Memory Usage Sep 29, 2026 GLM-5.3, KV Cache Offloading, HiSparse, AgentX TileRT, InferenceX DeepSeek Sparse Attention, IndexShare, Single-rollout Asynchronous Optimization, Cybersecurity How does sparse attention affect the TAM of memory, including HBM and NAN…"
[^2]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "How does sparse attention affect the TAM of memory, including HBM and NAND? Sparse attention selects top-k most relevant tokens to attend to, reducing the memory consumption and bandwidth requirements during the core Scaled Dot-Product Attention (SDPA) operation. However, the efficiency improvement …"
[^3]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "How does sparse attention affect the TAM of memory, including HBM and NAND? Sparse attention selects top-k most relevant tokens to attend to, reducing the memory consumption and bandwidth requirements during the core Scaled Dot-Product Attention (SDPA) operation. However, the efficiency improvement …"
[^4]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Sparse attention selects top-k most relevant tokens to attend to, reducing the memory consumption and bandwidth requirements during the core Scaled Dot-Product Attention (SDPA) operation."
[^5]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, the efficiency improvement doesn’t directly translate to overall memory savings in practice."
[^6]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Concretely, the top-k selection operation typically requires the full context to be in HBM, so sparse attention doesn’t eliminate the memory capacity bottleneck."
[^7]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To overcome this limitation, the SGLang team designed HiSparse, a hierarchical memory system that proactively offloads KV cache entries from device HBM to host DRAM. HiSparse behaves like an LRU (Least Recently Used) cache, where it loads tokens from DRAM to HBM upon top-k selection cache miss, and …"
[^8]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To overcome this limitation, the SGLang team designed HiSparse, a hierarchical memory system that proactively offloads KV cache entries from device HBM to host DRAM."
[^9]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "HiSparse behaves like an LRU (Least Recently Used) cache, where it loads tokens from DRAM to HBM upon top-k selection cache miss, and it offloads tokens from HBM to DRAM based on the LRU eviction policy."
[^10]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To reduce the cache miss latency, HiSparse overlaps KV cache loading of layer N with the execution of layer N-1 (layer-wise overlapping), introduced in HiSparse’s prior work HiCache."
[^11]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "With HiSparse, SGLang greatly boosts throughput at high concurrency and long context scenarios, at the cost of top-k cache miss I/O overhead."
[^12]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Sparse attention reduces KV cache memory and bandwidth requirements at the SDPA operation, but it does not reduce the overall memory capacity usage. In addition, HiSparse shows that system optimizations can overcome sparse attention’s memory capacity limitations, so sparse attention memory profile a…"
[^13]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Sparse attention reduces KV cache memory and bandwidth requirements at the SDPA operation, but it does not reduce the overall memory capacity usage."
[^14]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In addition, HiSparse shows that system optimizations can overcome sparse attention’s memory capacity limitations, so sparse attention memory profile alone cannot sufficiently portray the full picture of system KV cache efficiency."
[^15]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To provide a more holistic picture of serving sparse attention models, here we explain the design of Z.ai’s GLM-5 model series, and how they are served in practice."
[^16]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GLM5.3 Agentic Inference Serving In our realtime benchmark board InferenceX, GB300 delivers the lowest modeled serving cost in our comparison at a response speed of 150 tokens per second. GB300 handles more tokens per GPU, and its higher hourly cost still leaves it ahead of GB200 on cost efficiency.…"
[^17]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In our realtime benchmark board InferenceX, GB300 delivers the lowest modeled serving cost in our comparison at a response speed of 150 tokens per second. GB300 handles more tokens per GPU, and its higher hourly cost still leaves it ahead of GB200 on cost efficiency. The GB300 result uses Dynamo-TRT…"
[^18]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In our realtime benchmark board InferenceX, GB300 delivers the lowest modeled serving cost in our comparison at a response speed of 150 tokens per second. GB300 handles more tokens per GPU, and its higher hourly cost still leaves it ahead of GB200 on cost efficiency. The GB300 result uses Dynamo-TRT…"
[^19]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In our realtime benchmark board InferenceX, GB300 delivers the lowest modeled serving cost in our comparison at a response speed of 150 tokens per second."
[^20]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GB300 handles more tokens per GPU, and its higher hourly cost still leaves it ahead of GB200 on cost efficiency."
[^21]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The GB300 result uses Dynamo-TRT-LLM, while the GB200 result uses Dynamo-SGLang."
[^22]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "We use the September 28 AgentX snapshot results to help illustrate the serving implications of GLM-5.3. We estimate costs using InferenceX’s model of owning and operating infrastructure at hyperscaler scale. Total tokens include input and generated output, including cached input history reused acros…"
[^23]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "We use the September 28 AgentX snapshot results to help illustrate the serving implications of GLM-5.3. We estimate costs using InferenceX’s model of owning and operating infrastructure at hyperscaler scale."
[^24]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Total tokens include input and generated output, including cached input history reused across turns."
[^25]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Streaming speed is measured using p90 interactivity; time to first token is evaluated separately."
[^26]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "At 150 tokens per second, GB200 costs approximately $0.044 per million total tokens, compared with $0.049 for MI355X running ATOM. That is about 12% lower cost at the same streaming-speed target. These values are estimated from the measured curves, rather than from a separate test at exactly 150 tok…"
[^27]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "At 150 tokens per second, GB200 costs approximately $0.044 per million total tokens, compared with $0.049 for MI355X running ATOM. That is about 12% lower cost at the same streaming-speed target."
[^28]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "These values are estimated from the measured curves, rather than from a separate test at exactly 150 tokens per second."
[^29]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For this comparison, we use InferenceX’s estimated cost of owning and operating the infrastructure at hyperscaler scale."
[^30]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Total tokens include input and generated output, including input history reused from cache."
[^31]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Among the Dynamo-SGLang results, GB300 serves roughly 13950 total tokens per second per GPU here, a 17.5% throughput advantage versus 11873 total tokens for GB200. However, we assume $2.31 per GB300 GPU hour versus $1.86 for GB200. The higher hourly cost more than offsets GB300’s throughput lead at …"
[^32]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Among the Dynamo-SGLang results, GB300 serves roughly 13950 total tokens per second per GPU here, a 17.5% throughput advantage versus 11873 total tokens for GB200. However, we assume $2.31 per GB300 GPU hour versus $1.86 for GB200. The higher hourly cost more than offsets GB300’s throughput lead at …"
[^33]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In comparison with AMD, ATOM costs about 13% less than GB200 at 100 tokens per second. GB200 costs about 5% less at 125 and 12% less at 150. Across these three targets, neither system has a uniform cost advantage."
[^34]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In comparison with AMD, ATOM costs about 13% less than GB200 at 100 tokens per second."
[^35]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GB200 costs about 5% less at 125 and 12% less at 150. Across these three targets, neither system has a uniform cost advantage."
[^36]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Counting only generated output, GB200 costs $5.92 per million output tokens at a response speed of 150 tokens per second, which is about 11% less than $6.68 for MI355X ATOM. This metric is useful to analyze cost under agentic workloads, where agents repeatedly reuse long input histories while genera…"
[^37]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Counting only generated output, GB200 costs $5.92 per million output tokens at a response speed of 150 tokens per second, which is about 11% less than $6.68 for MI355X ATOM."
[^38]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "This metric is useful to analyze cost under agentic workloads, where agents repeatedly reuse long input histories while generating relatively little new text."
[^39]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The GB200 measurements on either side of the 150-token-per-second target have p90 TTFT (time to first token) of roughly 14–19 seconds, compared with about 1.1–1.2 seconds for MI355X ATOM. Some of the GB200 lowest-cost runs have much longer waits for the first token. We therefore make a second compar…"
[^40]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The GB200 measurements on either side of the 150-token-per-second target have p90 TTFT (time to first token) of roughly 14–19 seconds, compared with about 1.1–1.2 seconds for MI355X ATOM."
[^41]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Some of the GB200 lowest-cost runs have much longer waits for the first token."
[^42]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "We therefore make a second comparison using only configurations that were actually tested and achieved at least 150 tokens per second with p90 TTFT at most two seconds."
[^43]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The chart below shows MI355X with ATOM at $0.0607 per million total tokens versus $0.0666 for B200 with Dynamo-SGLang."
[^44]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "ATOM costs about 9% less with the two-second first-token limit."
[^45]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "If the limit is relaxed to ten seconds, GB300 with Dynamo-TRT-LLM becomes eligible at $0.0451, about 26% below ATOM’s $0.0607."
[^46]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Optimizations In GLM’s 5.2 / 5.3 model, its attention architecture reduces memory demands, and long running agents still need to retain earlier conversation history. GLM reduces the cost of handling this history in two ways: KV compression reduces the cached state stored per token, and sparse attent…"
[^47]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Optimizations In GLM’s 5.2 / 5.3 model, its attention architecture reduces memory demands, and long running agents still need to retain earlier conversation history. GLM reduces the cost of handling this history in two ways: KV compression reduces the cached state stored per token, and sparse attent…"
[^48]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In GLM’s 5.2 / 5.3 model, its attention architecture reduces memory demands, and long running agents still need to retain earlier conversation history. GLM reduces the cost of handling this history in two ways: KV compression reduces the cached state stored per token, and sparse attention reduces ho…"
[^49]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In GLM’s 5.2 / 5.3 model, its attention architecture reduces memory demands, and long running agents still need to retain earlier conversation history."
[^50]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GLM reduces the cost of handling this history in two ways: KV compression reduces the cached state stored per token, and sparse attention reduces how much of that state each attention operation reads."
[^51]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Then the serving engine would determine where to store the cache and how to retrieve it efficiently."
[^52]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "These B200 results show how much reuse can happen outside of GPU memory. When concurrency increases from 8 to 16 requests, the share of prompt tokens reused from GPU memory falls from 90.3% to 54.8%. Much of that reuse shifts to host memory, which rose from 6.0% to 40.3%. Much of the decline in GPU …"
[^53]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "These B200 results show how much reuse can happen outside of GPU memory."
[^54]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "When concurrency increases from 8 to 16 requests, the share of prompt tokens reused from GPU memory falls from 90.3% to 54.8%."
[^55]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Much of that reuse shifts to host memory, which rose from 6.0% to 40.3%."
[^56]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Much of the decline in GPU cache is offset by reuse from host memory, keeping the overall cache hit rate above 95% at all concurrency levels."
[^57]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Beyond cache management, changes to how the serving engine executes prefill and decoding can also change performance. Two separate GLM-5.2 studies illustrate this: vLLM keeping the first decoding step on a consistent CUDA graph execution path reduced average TPOT (time per output token) from about 4…"
[^58]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Beyond cache management, changes to how the serving engine executes prefill and decoding can also change performance."
[^59]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Two separate GLM-5.2 studies illustrate this:"
[^60]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "vLLM keeping the first decoding step on a consistent CUDA graph execution path reduced average TPOT (time per output token) from about 40 ms to 22 ms in an NVFP4 study."
[^61]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "On a different 8 MI355X long context workload, ATOM engine processing prefill in chunks across pipeline stages delivered 98% higher total throughput and reduced median TTFT from 28.6 to 8.7 seconds."
[^62]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "TileRT For GLM5.3 on TileRT, AMD MI355X was supported first. TileRT is a low-latency LLM inference engine for that compiles decoding into a single persistent kernel, reducing launch overhead and overlapping computation, memory access, and communication. It prioritizes faster token generation per use…"
[^63]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For GLM5.3 on TileRT, AMD MI355X was supported first. TileRT is a low-latency LLM inference engine for that compiles decoding into a single persistent kernel, reducing launch overhead and overlapping computation, memory access, and communication. It prioritizes faster token generation per user, rath…"
[^64]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For GLM5.3 on TileRT, AMD MI355X was supported first."
[^65]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "TileRT is a low-latency LLM inference engine for that compiles decoding into a single persistent kernel, reducing launch overhead and overlapping computation, memory access, and communication."
[^66]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "It prioritizes faster token generation per user, rather than maximum batched throughput, while vLLM handle prefill."
[^67]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "On AgentX, FP8 TileRT MI355X achieves 2x the P90 interactivity than the best FP4 MI335X config. Comparing to GB300 NVL72, it brings a 40% uplift in interactivity. These are serving metrics that used to require specialized hardware."
[^68]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "On AgentX, FP8 TileRT MI355X achieves 2x the P90 interactivity than the best FP4 MI335X config."
[^69]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Comparing to GB300 NVL72, it brings a 40% uplift in interactivity."
[^70]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "These are serving metrics that used to require specialized hardware."
[^71]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, TTFT is suboptimal and there is still room for development, such as optimizing KV transfer, FP4 support, and larger batch sizes."
[^72]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "DeepSeek Sparse Attention GLM-5 (and GLM-5.x models) is a 744B total, 40B active-parameter mixture-of-experts model. For every token, it has 1 shared expert and is routed through 8 out of 256 experts, which is sparsity 32. It features DeepSeek Sparse Attention, which we will discuss in this section.…"
[^73]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GLM-5 (and GLM-5.x models) is a 744B total, 40B active-parameter mixture-of-experts model. For every token, it has 1 shared expert and is routed through 8 out of 256 experts, which is sparsity 32. It features DeepSeek Sparse Attention, which we will discuss in this section."
[^74]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GLM-5 (and GLM-5.x models) is a 744B total, 40B active-parameter mixture-of-experts model."
[^75]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For every token, it has 1 shared expert and is routed through 8 out of 256 experts, which is sparsity 32. It features DeepSeek Sparse Attention, which we will discuss in this section."
[^76]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For every token, it has 1 shared expert and is routed through 8 out of 256 experts, which is sparsity 32. It features DeepSeek Sparse Attention, which we will discuss in this section. DeepSeek Sparse Attention (DSA), introduced in DeepSeek V3.2, consists of two components: A lightning indexer that s…"
[^77]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "DeepSeek Sparse Attention (DSA), introduced in DeepSeek V3.2, consists of two components: A lightning indexer that selects top K tokens, and a sparse Multi-Latent Attention (MLA)."
[^78]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Lightning Indexer A lightning indexer is functionally similar to a lightweight attention mechanism. Queries and keys are down-projected to lower dimensions, with indexer queries being multi-headed and indexer keys single-headed. Since we only need a query and key relation score (logits) for selectin…"
[^79]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "A lightning indexer is functionally similar to a lightweight attention mechanism. Queries and keys are down-projected to lower dimensions, with indexer queries being multi-headed and indexer keys single-headed. Since we only need a query and key relation score (logits) for selecting top K tokens, th…"
[^80]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "A lightning indexer is functionally similar to a lightweight attention mechanism."
[^81]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Queries and keys are down-projected to lower dimensions, with indexer queries being multi-headed and indexer keys single-headed."
[^82]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Since we only need a query and key relation score (logits) for selecting top K tokens, the indexer doesn’t need value embeddings or the softmax operation for normalized logits."
[^83]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Instead, it computes a query-key dot product, followed by a ReLU non-linearity."
[^84]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The indexer then computes each token’s indexer score as a weighted sum of logits across all query heads, which we use to select the top K tokens with."
[^85]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "This means despite the indexer having multiple heads, token selection is shared across multiple attention heads."
[^86]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "When selecting top K tokens, we keep queries that attend to less than K tokens as dense attention, and we select top K otherwise."
[^87]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Sparse MLA As we explained in our Kimi K3 article, MLA operates in two modes: Multi-Head Attention (MHA) mode and Multi-Query Attention (MQA) mode. Both come with trade-offs: MHA mode has lower FLOPs but 42x higher memory cost, MQA mode has lower memory cost but up to 3.4x higher FLOPs. DSA uses MQA…"
[^88]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "As we explained in our Kimi K3 article, MLA operates in two modes: Multi-Head Attention (MHA) mode and Multi-Query Attention (MQA) mode. Both come with trade-offs: MHA mode has lower FLOPs but 42x higher memory cost, MQA mode has lower memory cost but up to 3.4x higher FLOPs."
[^89]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "As we explained in our Kimi K3 article, MLA operates in two modes: Multi-Head Attention (MHA) mode and Multi-Query Attention (MQA) mode."
[^90]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Both come with trade-offs: MHA mode has lower FLOPs but 42x higher memory cost, MQA mode has lower memory cost but up to 3.4x higher FLOPs."
[^91]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "DSA uses MQA mode, since sparse attention attends to less tokens,mitigating the higher FLOP usage."
[^92]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, in practice, there is a sequence length threshold where under it, MHA mode is actually more efficient that MQA mode. The intuition is that at shorter sequence length, the memory loading time isn’t as dominating, and MHA mode may have an edge for being lower FLOPs. vLLM implements this featu…"
[^93]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, in practice, there is a sequence length threshold where under it, MHA mode is actually more efficient that MQA mode."
[^94]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The intuition is that at shorter sequence length, the memory loading time isn’t as dominating, and MHA mode may have an edge for being lower FLOPs."
[^95]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "vLLM implements this feature, and configures MHA mode for sequence length 2K to about 5K for data parallel, and 2K to about 77K for tensor parallel."
[^96]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The 2K minimum is due to top K being 2048, and as mentioned above, attention below 2K is dense."
[^97]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "MLA Modifications Comparing the MLA dimension configurations of GLM-5 and DeepSeek V3.2, we see that the most notable differences are the number of query heads and the query key head dimension. https://substackcdn.com/image/fetch/$s_!qpBS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https…"
[^98]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Comparing the MLA dimension configurations of GLM-5 and DeepSeek V3.2, we see that the most notable differences are the number of query heads and the query key head dimension. https://substackcdn.com/image/fetch/$s_!qpBS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-…"
[^99]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Comparing the MLA dimension configurations of GLM-5 and DeepSeek V3.2, we see that the most notable differences are the number of query heads and the query key head dimension."
[^100]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GLM-5 tech report mentions DeepSeek chose the number of query heads according to the roofline of H800. This is likely referring to the fact that MLA’s SDPA arithmetic intensity during decode is roughly at the ridge point of H800. Derivation as follows. Assume L: Sequence length d: Head dimension r: …"
[^101]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GLM-5 tech report mentions DeepSeek chose the number of query heads according to the roofline of H800. This is likely referring to the fact that MLA’s SDPA arithmetic intensity during decode is roughly at the ridge point of H800. Derivation as follows."
[^102]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Assume"
[^103]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "L: Sequence length"
[^104]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "d: Head dimension"
[^105]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "r: RoPE dimension"
[^106]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "H: Number of heads"
[^107]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "b: Number of bytes per parameter"
[^108]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In MQA mode, the FLOPs are"
[^109]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "and the memory loaded is"
[^110]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "So the arithmetic intensity is"
[^111]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "If we plug in the DeepSeek V3.2 configuration d = 512, r = 64, b = 2), we get"
[^112]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "H800’s practical arithmetic intensity is 258.2 FLOP/B (Practical peak 865 TFLOP/s, 3.35 TB/s bandwidth, according to DeepSeek), and plugging in the formula gives us H ~= 128."
[^113]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The fact that GLM-5 has H = 64, half the number of query heads, implies that GLM-5 may be designed for different hardware. If we plug in GLM-5’s configuration (d = 512, r = 64, b = 2, H = 64), we get an arithmetic intensity of 120.8 FLOP/B. Thus, we suspect GLM-5 is optimized for Moore Threads MTT S…"
[^114]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The fact that GLM-5 has H = 64, half the number of query heads, implies that GLM-5 may be designed for different hardware."
[^115]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "If we plug in GLM-5’s configuration (d = 512, r = 64, b = 2, H = 64), we get an arithmetic intensity of 120.8 FLOP/B."
[^116]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Thus, we suspect GLM-5 is optimized for Moore Threads MTT S4000, which is about 128 FLOP/B."
[^117]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Moore Threads’ collaboration with Z.ai, such as GLM-5.3-Flash day 0 support, corroborates our theory."
[^118]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Separately, GLM-5 increases the QK NoPE dimension from 128 to 192, as ablations show the configuration is superior under iso-FLOP and iso-parameter constraints. This increases the SDPA head dimension from 192 to 256, which is still a 33% FLOP reduction after considering the head number reduction."
[^119]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Separately, GLM-5 increases the QK NoPE dimension from 128 to 192, as ablations show the configuration is superior under iso-FLOP and iso-parameter constraints."
[^120]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "This increases the SDPA head dimension from 192 to 256, which is still a 33% FLOP reduction after considering the head number reduction."
[^121]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "IndexShare The latency cost of the indexer becomes non-negligible as context grows. To mitigate the cost, Z.ai proposes IndexShare (aka IndexCache) in GLM-5.2, where every 4 DSA layers share one indexer. https://substackcdn.com/image/fetch/$s_!gPFQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:s…"
[^122]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The latency cost of the indexer becomes non-negligible as context grows. To mitigate the cost, Z.ai proposes IndexShare (aka IndexCache) in GLM-5.2, where every 4 DSA layers share one indexer."
[^123]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The latency cost of the indexer becomes non-negligible as context grows."
[^124]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To mitigate the cost, Z.ai proposes IndexShare (aka IndexCache) in GLM-5.2, where every 4 DSA layers share one indexer."
[^125]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "IndexShare introduces complications in training and inference. Standard DSA training involves two stages: A dense warm-up stage where all model weights except the indexer are frozen and attention computation is dense, and then a sparse adaptation stage where the full model is trained with sparse att…"
[^126]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "IndexShare introduces complications in training and inference."
[^127]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Standard DSA training involves two stages: A dense warm-up stage where all model weights except the indexer are frozen and attention computation is dense, and then a sparse adaptation stage where the full model is trained with sparse attention."
[^128]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In terms of training objective, the indexer is trained to align with the sum of attention head scores, using a KL divergence objective."
[^129]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "IndexShare adapts the training objective to aligning the indexer logit distribution with the average distribution of attention scores across shared layers."
[^130]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For inference, typically the indexer caches keys, like attention caches KV."
[^131]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Since multiple layers share one indexer, we need to additionally cache the top K indices at the full layer, in order to reuse the top K selection information at shared layers."
[^132]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "This design reduces indexer cache by 75%, reduces indexer FLOPs by 75%, and boosts throughput by 1.5x to 1.8x at different context lengths and prefill/decode."
[^133]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Post-Training Design Pipeline After pre-training and mid-training, GLM-5’s post-training pipeline starts with supervised fine-tuning (SFT), continues with three RL training stages (reasoning RL, agentic RL, and general RL), and ends with an on-policy cross-stage distillation, distilling reasoning an…"
[^134]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Pipeline After pre-training and mid-training, GLM-5’s post-training pipeline starts with supervised fine-tuning (SFT), continues with three RL training stages (reasoning RL, agentic RL, and general RL), and ends with an on-policy cross-stage distillation, distilling reasoning and general RL back int…"
[^135]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "After pre-training and mid-training, GLM-5’s post-training pipeline starts with supervised fine-tuning (SFT), continues with three RL training stages (reasoning RL, agentic RL, and general RL), and ends with an on-policy cross-stage distillation, distilling reasoning and general RL back into the SFT…"
[^136]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Here we highlight two details. First, the tech report states that the reasoning RL model is trained entirely on-policy, implying that it is trained synchronously. Synchronous RL training is low system efficiency but has higher RL training stability. Second, on-policy cross-stage distillation is simi…"
[^137]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "First, the tech report states that the reasoning RL model is trained entirely on-policy, implying that it is trained synchronously."
[^138]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Synchronous RL training is low system efficiency but has higher RL training stability."
[^139]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Second, on-policy cross-stage distillation is similar to Multi-teacher On-Policy Distillation (MOPD), where a student model is RL trained with on-policy distillation over multiple teacher models."
[^140]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, unlike MOPD, whose goal is to merge expert teacher models into one model, GLM-5 here seems to be more about recovering old capability loss when the model learns new capabilities."
[^141]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Following this assumption, we are not sure why the Z.ai only uses reasoning and general RL checkpoints as teachers, instead of using all three RL checkpoints."
[^142]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Based on the announcement blog post, GLM-5.2 may have replaced the on-policy cross-stage distillation with a standard MOPD pipeline, which Z.ai named parallel OPD training. Z.ai touted its scale and training efficiency: they merged more than ten expert models into a final model by training for about…"
[^143]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Based on the announcement blog post, GLM-5.2 may have replaced the on-policy cross-stage distillation with a standard MOPD pipeline, which Z.ai named parallel OPD training."
[^144]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Z.ai touted its scale and training efficiency: they merged more than ten expert models into a final model by training for about two days."
[^145]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "RL Training Algorithm Z.ai adopts different RL algorithms for synchronous and asynchronous RL stages. Here we compare the major differences in the RL objectives. In the synchronous RL stage, Z.ai adopts Group Relative Policy Optimization (GRPO)-based RL algorithm with modern adaptations, including: …"
[^146]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Z.ai adopts different RL algorithms for synchronous and asynchronous RL stages. Here we compare the major differences in the RL objectives."
[^147]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In the synchronous RL stage, Z.ai adopts Group Relative Policy Optimization (GRPO)-based RL algorithm with modern adaptations, including: Remove KL regularization term to improve system efficiency and allow more aggressive gradient updates IcePop: Apply token-level masking based on the training-infe…"
[^148]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In the synchronous RL stage, Z.ai adopts Group Relative Policy Optimization (GRPO)-based RL algorithm with modern adaptations, including:"
[^149]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Remove KL regularization term to improve system efficiency and allow more aggressive gradient updates"
[^150]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "IcePop: Apply token-level masking based on the training-inference mismatch ratio"
[^151]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Clip-Higher: Use a higher max threshold for importance sampling ratio to encourage exploration"
[^152]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In contrast, Z.ai employs a REINFORCE-like RL algorithm for asynchronous RL stage, adding Direct Double-Sided Importance Sampling (DIS), an IcePop-like clipping mechanism. Below we compare the token-level objectives for the two RL stages:"
[^153]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In contrast, Z.ai employs a REINFORCE-like RL algorithm for asynchronous RL stage, adding Direct Double-Sided Importance Sampling (DIS), an IcePop-like clipping mechanism."
[^154]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Below we compare the token-level objectives for the two RL stages:"
[^155]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The importance sampling (IS) ratio compares the probability of each sampled action under the current policy and the behavior policy, scaling each action’s contribution to the training objective. For IS ratio, the synchronous RL stage utilizes the trainer policy of the previous iteration for the beha…"
[^156]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The importance sampling (IS) ratio compares the probability of each sampled action under the current policy and the behavior policy, scaling each action’s contribution to the training objective."
[^157]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "For IS ratio, the synchronous RL stage utilizes the trainer policy of the previous iteration for the behavior policy, whereas the asynchronous RL stage utilizes the inference policy for that."
[^158]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In an asynchronous training setting, policy updates happen multiple times during rollouts, so we will need every checkpoint version in between to calculate the IS ratio."
[^159]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, this is infeasible due to the high memory and latency overhead."
[^160]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "As a result, Z.ai opts for using inference policy for efficiency and simplicity, at the cost of numeric stability challenges."
[^161]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Finally, we highlight the major differences in advantage calculation in RL training, cross-distillation, and long-horizon RL training. RL training employs the GRPO standard group-normalized advantage, and cross-distillation uses the reverse KL divergence. https://substackcdn.com/image/fetch/$s_!7JkY…"
[^162]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Finally, we highlight the major differences in advantage calculation in RL training, cross-distillation, and long-horizon RL training."
[^163]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "RL training employs the GRPO standard group-normalized advantage, and cross-distillation uses the reverse KL divergence."
[^164]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Single-Rollout Asynchronous Optimization Long horizon tasks produce extremely long trajectories, and in the context of GRPO, the high variance in trajectory length produces unstable training signals that may skew towards longer trajectories. What’s worse, since RL rollout workload is sensitive to en…"
[^165]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Long horizon tasks produce extremely long trajectories, and in the context of GRPO, the high variance in trajectory length produces unstable training signals that may skew towards longer trajectories. What’s worse, since RL rollout workload is sensitive to end-to-end latency, the tail-latency of a s…"
[^166]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Long horizon tasks produce extremely long trajectories, and in the context of GRPO, the high variance in trajectory length produces unstable training signals that may skew towards longer trajectories."
[^167]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "What’s worse, since RL rollout workload is sensitive to end-to-end latency, the tail-latency of a straggler rollout worsens for long horizon tasks."
[^168]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To mitigate this issue, Z.ai introduced Single-rollout Asynchronous Optimization (SAO) for long-horizon RL training in GLM-5.2. SAO replaces group-normalized advantage with a modified Generalized Advantage Estimation (GAE), inspired by Proximal Policy Optimization (PPO). GAE only needs a single roll…"
[^169]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To mitigate this issue, Z.ai introduced Single-rollout Asynchronous Optimization (SAO) for long-horizon RL training in GLM-5.2. SAO replaces group-normalized advantage with a modified Generalized Advantage Estimation (GAE), inspired by Proximal Policy Optimization (PPO)."
[^170]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GAE only needs a single rollout to compute the advantage."
[^171]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "This removes the need to do multiple rollouts per prompt, mitigating GRPO’s short-come."
[^172]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GAE is computed with values (In RL terms, expected returns of the current state), estimated by a value model. Concretely, the value model takes the rollout as input and produces a value estimation for every token. SAO adapts GAE to agentic RL training by removing the observation tokens, i.e. tool ca…"
[^173]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "GAE is computed with values (In RL terms, expected returns of the current state), estimated by a value model."
[^174]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Concretely, the value model takes the rollout as input and produces a value estimation for every token."
[^175]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "SAO adapts GAE to agentic RL training by removing the observation tokens, i.e. tool call results, from the optimization."
[^176]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Previously in GLM-5, skipping the tokens is sufficient; in SAO, we modify the advantage estimation formula to bypass the observation tokens."
[^177]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "We refer readers to the SAO paper and its appendix A.1 for more intuition on the Bellman target and the ablations."
[^178]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In SAO, the value model is a separate LLM concurrently trained with the policy model. This means early stages of training are susceptible to high variance of advantage calculations, due to a weak value model. To combat this, SAO proposes multiple techniques for training value models: Two Time-scale …"
[^179]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In SAO, the value model is a separate LLM concurrently trained with the policy model."
[^180]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "This means early stages of training are susceptible to high variance of advantage calculations, due to a weak value model."
[^181]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To combat this, SAO proposes multiple techniques for training value models:"
[^182]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Two Time-scale Update Rule: Updating the value model twice as frequently as the policy model. This means training on each data batch twice at every policy training step"
[^183]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Attention Parameter Freezing: Freezing the value model’s full attention layers to improve training stability"
[^184]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Scaling Pre-training: Scaling the value model pre-training corpus to initialize the value model, so that the value model can robustly estimate values in the early stages of training. Unfortunately, Z.ai didn’t disclose the scaling information of pre-training corpus"
[^185]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "At the cost of computational overhead and doubling memory footprint, SAO replaces group-wise sampling with a value model, mitigating the latency issues of GRPO."
[^186]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Post-Training Infrastructure Z.ai uses slime, one of the best open-source RL training frameworks, as the post-training infrastructure throughout all GLM-5 models. We refer readers to the slime GitHub repo to learn more about its design and features, and here we highlight two features. Performance ch…"
[^187]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Z.ai uses slime, one of the best open-source RL training frameworks, as the post-training infrastructure throughout all GLM-5 models. We refer readers to the slime GitHub repo to learn more about its design and features, and here we highlight two features. Performance characteristics of RL rollouts …"
[^188]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Z.ai uses slime, one of the best open-source RL training frameworks, as the post-training infrastructure throughout all GLM-5 models. We refer readers to the slime GitHub repo to learn more about its design and features, and here we highlight two features."
[^189]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Z.ai uses slime, one of the best open-source RL training frameworks, as the post-training infrastructure throughout all GLM-5 models."
[^190]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "We refer readers to the slime GitHub repo to learn more about its design and features, and here we highlight two features."
[^191]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Performance characteristics of RL rollouts are highly task-dependent, and each task comes with different tools and reward functions. To ensure system efficiency, Z.ai designed a server-based multi-task rollout orchestrator. Each task acts as an independent microservice server, controlling rollout an…"
[^192]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Performance characteristics of RL rollouts are highly task-dependent, and each task comes with different tools and reward functions."
[^193]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "To ensure system efficiency, Z.ai designed a server-based multi-task rollout orchestrator."
[^194]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Each task acts as an independent microservice server, controlling rollout and reward logic."
[^195]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "The orchestrator balances the overall performance, controlling the per-task rollout ratio and generation speed."
[^196]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Centralization also allows dynamic ratio adjustments across tasks, fine-grained progress monitoring, and many more."
[^197]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "Z.ai claims the orchestrator supports 1000 concurrent rollouts when training GLM-5."
[^198]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In the GLM-5.3 announcement, Z.ai claims to use local storage as a cache layer in addition to host memory, which enables dynamic teacher model switching and prefetching for MOPD. slime PR#1538 implements teacher switching by introducing a TensorBackuper class, which stores teacher weights as PyTorch…"
[^199]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "In the GLM-5.3 announcement, Z.ai claims to use local storage as a cache layer in addition to host memory, which enables dynamic teacher model switching and prefetching for MOPD."
[^200]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "slime PR#1538 implements teacher switching by introducing a TensorBackuper class, which stores teacher weights as PyTorch tensors pinned to CPU memory. When a rollout is routed to a teacher, a TensorBackuper object copies the teacher model back to GPU memory to perform a forward pass (implementation…"
[^201]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "slime PR#1538 implements teacher switching by introducing a TensorBackuper class, which stores teacher weights as PyTorch tensors pinned to CPU memory."
[^202]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "When a rollout is routed to a teacher, a TensorBackuper object copies the teacher model back to GPU memory to perform a forward pass (implementation here)."
[^203]: How GLM5.3 Sparse Attention Affects HBM Memory Usage — "However, this is CPU-backed weight swapping, and we have yet to see storage-backed implementation."
