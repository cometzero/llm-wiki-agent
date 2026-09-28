---
title: "Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading"
origin: lilys_ai
lilys_project_id: 11421788
lilys_project_url: "https://lilys.ai/digest/11421788"
lilys_created_at: "2026-09-20T04:20:45.991Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13489817"
sources:
  - id: "12331622"
    url: "https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign"
    title: "Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading"
    status: "done"
---

# Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading

## LilysAI note

> Engram 모델 아키텍처의 핵심은 무엇인가? **Engram**은 표준 토큰 임베딩을 확장하여 반복되는 패턴을 직접 검색함으로써, HBM 용량 요구량을 줄이고 DRAM/SSD로의 효율적인 **파라미터 오프로딩**을 가능하게 합니다. 이는 모델 품질을 유지하면서도 더 적은 고대역폭 메모리로 AI 모델을 운영할 수 있게 합니다.

## 1. Engram 모델 아키텍처: 효율적인 DRAM/SSD 오프로딩을 위한 공동 설계

Engram 모델 아키텍처는 표준 토큰 임베딩을 확장하여 반복되는 패턴을 직접 검색함으로써 HBM 용량 요구량을 줄이고 DRAM/SSD로의 효율적인 파라미터 오프로딩을 가능하게 한다.

### 1.1. Engram 모델 아키텍처의 핵심 및 이점
1. **Engram의 확장된 토큰 임베딩**
    1. Engram은 표준 토큰 임베딩을 학습된 다중 토큰 조회로 확장한다.
    2. 반복되는 로컬 패턴은 벡터를 직접 검색하여 어텐션 및 피드포워드 레이어를 통한 재구축 필요성을 줄인다.
2. **HBM 용량 최적화**
    1. Engram 모델 아키텍처 최적화를 통해 동일한 품질의 모델에 필요한 HBM 용량을 줄일 수 있다.
    2. 이는 HBM에 대한 엄청난 수요가 없을 것이라는 의미는 아니지만, 모델 아키텍처가 제약 조건에 맞춰 계속 혁신할 것임을 시사한다.
3. **파라미터 오프로딩을 위한 공동 설계**
    1. 이 모델 아키텍처 설계는 파라미터 오프로딩을 위해 자연스럽게 공동 설계되었다.
    2. 각 토큰은 은닉 상태가 아닌 토큰 ID에 따라 주소가 결정되는 몇 개의 임베딩 행에 접근한다.
    3. 런타임은 이전 레이어가 계산되는 동안 호스트 DRAM에서 해당 행을 미리 가져와 전체 가중치 행렬을 전송하지 않고도 테이블을 HBM 외부에 유지할 수 있다.

### 1.2. Engram의 오프로딩 이점 및 DeepSeek-V4.1-Flash 적용 사례
1. **HBM 용량 확보 및 계층화된 메모리 활용**
    <img alt="HBM, DRAM, NAND 공급 및 수요 추정치를 보여주는 차트" src="https://substackcdn.com/image/fetch/$s_!EPnh!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa5373b8-e5c4-4254-b899-1195ac27e1a7_2048x769.png" caption="출처: SemiAnalysis">
    1. 오프로딩은 모델 가중치와 KV 캐시를 위해 HBM을 확보하여 더 큰 배치 또는 더 많은 동시 세션을 지원할 수 있다.
    2. DRAM이 다음 제약이 될 경우, NVMe는 또 다른 계층을 제공한다.
    3. 추천 시스템은 이미 자주 또는 최근에 접근한 임베딩 행을 더 빠른 메모리에 캐시하고, 덜 사용되는 행은 SSD로 백업한다.
    4. NVIDIA 로드맵이 Rubin Ultra의 HBM 용량을 1024GB에서 약 200GB로 대폭 줄여야 했기 때문에, Engram과 같은 모델 아키텍처 최적화가 유용할 수 있다.
2. **DeepSeek-V4.1-Flash의 Engram 구성 및 오프로딩 실험**
    1. DeepSeek-V4.1-Flash 구성은 Engram에 약 189GiB의 메모리를 사용한다.
    2. 이를 메모리 매핑(mmap) 파일로 대체하고 SSD 오프로딩을 통한 서비스 성능을 측정한다.
    3. 보고서 후반부에서는 Engram 오프로딩 실험과 DeepSeekv4.1 Flash와 같은 Engram 모델에 대한 공식 InferenceX 에이전트 추론 서비스 결과를 6가지 NVIDIA GPU SKU 및 MI355X에서 보여줄 예정이다.
    4. 예상대로, CUDA Moat은 여전히 매우 인기 있는 DeepSeekV4.1 Flash 모델에서 MI355X를 능가한다.
    5. 고용량 HBM SKU에서도 Engram을 DRAM으로 오프로딩하는 것이 HBM에 Engram을 유지하는 것보다 대부분의 파레토에서 더 나은 성능을 가져올 수 있음을 보여준다.
3. **InferenceX 벤치마크의 광범위한 채택 및 지원**
    1. 이 벤치마크는 Google Cloud, Microsoft Azure, Oracle, Meta 등 거의 모든 주요 컴퓨팅 구매자에 의해 널리 재현, 검증 및/또는 지원되었다.
    2. 또한 vLLM, LMCache, SGLang, PyTorch, Huggingface를 포함한 ML 커뮤니티와 OpenAI, MiniMax, ZAI, Qwen, Moonshot Kimi 등 주요 연구소의 지원을 받고 있다.
    3. 오픈 소스 벤치마크 및 데이터가 유용하다고 생각되면 InferenceX GitHub 저장소에 별표를 표시해야 한다.
    4. InferenceX는 TPUv7, Jalapeño, Nvidia Rubin NVL72, AMD, 그리고 곧 SambaNova 및 Trainium을 포함하는 세계 유일의 추론 벤치마크이다.
    5. AgentX 시나리오가 실제 에이전트 추론 워크로드에 얼마나 현실적인지 때문에 AMD는 MI455X UALoE72에서도 협력하기로 약속했다.

## 2. Engram의 성능 이점 및 메모리 활용 분석
Engram은 MoE(Mixture-of-Experts) 모델의 성능을 향상시키고, 특정 n-그램을 효과적으로 기억하며, 제거 시 모델 성능에 상당한 영향을 미친다.

### 2.1. Engram의 성능 향상 및 DeepSeek 재현 결과
1. **DeepSeek Engram 모델 재현 및 U-자형 스케일링 관찰**
    1. DeepSeek은 원래 논문의 두 가지 훈련된 Engram 모델을 공개하지 않았다.
    2. 공개된 코드와 훈련 하이퍼파라미터를 사용하여 fineweb-edu에서 설정을 재현했으며, 실행당 약 6E18 FLOPs로 추정된다.
    3. 동일한 U-자형 스케일링을 관찰했다.
    <img alt="Engram 모델의 U-자형 스케일링을 보여주는 그래프" src="https://substackcdn.com/image/fetch/$s_!XE1Q!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ec98796-a8c4-4cf8-9065-e9397c59fca1_1034x752.png" caption="출처: SemiAnalysis">
2. **순수 MoE 대비 Engram의 성능 개선**
    1. Engram은 순수 MoE(Mixture-of-Experts) 기준선보다 성능을 향상시켰다.
    2. DeepSeek의 결과도 재현했는데, Engram을 사용한 초기 레이어 표현이 후기 레이어 표현과 유사하다는 것을 확인했다.
    <img alt="Engram을 사용한 초기 레이어 표현과 후기 레이어 표현의 유사성을 보여주는 그래프" src="https://substackcdn.com/image/fetch/$s_!uRQK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27447880-e621-4b06-8f26-79773780be2f_2272x1348.png" caption="출처: SemiAnalysis">

### 2.2. Engram이 기억하는 내용 및 오프로딩 시 고려사항
1. **Engram이 기억하는 n-그램 유형**
    1. 원래 Engram 논문처럼 Engram의 게이트 점수를 조사하여 DeepSeek-V4.1-Flash가 가장 많이 활용하는 n-그램을 확인할 수 있다.
    2. 게이트 스캔 결과 이름, 코드 조각, 관계형 구문 및 상용구(boilerplate)가 발견되었다.
    3. 이러한 예시는 게이트 강도보다는 흥미로움을 우선시한다.
    4. 예상치 못한 결과 중 하나는 `Wright : Ace Attorney`였다.
    <img alt="Engram이 기억하는 n-그램 예시를 보여주는 표" src="https://substackcdn.com/image/fetch/$s_!GcHc!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0160b80e-a48a-4e36-9895-494f7ce158ba_1290x1080.png" caption="출처: SemiAnalysis">
2. **학습된 메모리의 최적화 및 오프로딩 시 주의사항**
    1. 이러한 예시는 학습된 메모리가 훈련 목표를 최적화하며, 어떤 사실이 저장될 가치가 있는지에 대한 판단이 아님을 시사한다.
    2. 라이선스, 참고 문헌 조각, API 스캐폴딩 및 웹사이트 구성 요소는 예측 지름길을 제공할 수 있으므로, 추가 Engram 용량의 가치는 데이터 준비 후 무엇이 남는지에 따라 달라질 수 있다.
    3. 이는 테이블 용량이 "낭비"된다는 것을 보여주지 않는다. 평가 코퍼스 스캔은 훈련 노출이나 각 범주가 차지하는 용량을 확립하지 않는다.
    4. 오프로딩의 경우, 강한 게이트가 캐시-핫 행을 식별하지는 않는다.
    5. 낮은 게이트도 자동으로 읽기 횟수를 줄이지는 않는다. 게이트를 계산하려면 검색된 키가 필요하며, 이는 융합 커널의 성능 이점을 상쇄한다.
    6. 읽기를 건너뛰려면 검색 전에 별도의 유용성 예측기가 필요하다.

### 2.3. Engram 제거 시 모델 성능 변화
1. **Engram 제거 시 벤치마크 성능 저하**
    1. 원래 논문의 추론 시간 제거 실험에서 사실 지식 벤치마크는 원래 성능의 29~44%만 유지했고, 독해는 81~93%를 유지했다.
    2. 이는 훈련-추론 불일치 때문이다.
    3. 결과적인 성능 저하는 Engram에 대한 훈련된 모델의 의존성을 측정하는 것이지, Engram 유무에 따라 훈련된 모델 간의 성능 차이를 측정하는 것이 아니다.
    4. 제거 실험에서 Engram을 억제하면 모든 평가 도메인, 특히 백과사전 텍스트와 여러 코드 코퍼스에서 토큰 가능성이 악화된다.
    5. 놀랍게도 GSM8K 정확도는 측정된 실행 간 변동 범위 내에 머물렀고, Engram을 제거해도 효과가 없었다.
2. **Engram 제거가 MoE 모델에 미치는 영향**
    1. Engram은 변경되지 않은 MoE 옆에 있는 분리 가능한 사전이 아니다. Engram을 제거하면 다운스트림 기능과 전문가 선택이 변경된다.
    2. CRUXEval(모델이 코드와 입력에서 함수의 출력을 예측하는 작은 Python 함수 코드 추론 벤치마크)에서 토큰을 고정하는 교사 강제 실험을 통해 재라우팅이 해로운지 또는 보상하는지 테스트하고 참조 답변을 채점했다.
    3. Engram을 제거하면 답변 손실이 0.2848에서 0.3093 bits/token으로 증가했다.
    4. 제거된 모델이 원래 Engram-on 전문가 선택을 사용하도록 강제하면 0.3375 bits/token으로 더욱 악화되었다.
    <img alt="Engram 제거가 답변 손실에 미치는 영향을 보여주는 그래프" src="https://substackcdn.com/image/fetch/$s_!2mjE!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe728edcc-e684-41c7-99f3-3de66b76d1ff_2048x841.png" caption="출처: SemiAnalysis">
3. **메모리 기능과 전문가 선택의 상호작용**
    1. 재라우팅은 누락된 메모리를 부분적으로 보상한다.
    2. 메모리 기능과 전문가 선택은 "메모리가 사실을 저장하고 전문가가 추론한다"는 깔끔한 구분 없이 함께 작동한다.
    3. 동일한 CRUXeval에서, 어느 단계에서든 Engram을 제거하면 정확도가 감소하고 생성된 토큰이 증가했으며, 전체적으로 제거하면 가장 큰 변화가 발생했다.
    <img alt="Engram 제거가 정확도 및 생성된 토큰에 미치는 영향을 보여주는 그래프" src="https://substackcdn.com/image/fetch/$s_!kkAk!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F477584e8-1f01-4e67-90b4-a8f60d3b3b09_2048x666.png" caption="출처: SemiAnalysis">
    4. 프리필(prefill)을 위해 Engram을 유지하는 것이 디코드(decode)를 위해 유지하는 것보다 더 정확한 답변을 제공하는데, 이는 디코드 워커로 전송되는 의미론적으로 더 풍부한 KV 캐시 덕분에 성능 손실의 일부를 완화할 수 있기 때문이다.

## 3. 에이전트 추론 서비스 성능 및 Engram 오프로딩의 효과
Engram의 대규모 테이블은 각 조회가 작지만, DRAM 오프로딩을 통해 HBM 사용량을 줄이고 성능을 향상시킬 수 있으며, SSD 오프로딩은 현재 최적화되지 않아 성능 이점이 적다.

### 3.1. Engram의 조회 특성 및 AMD vLLM의 성능 문제
1. **Engram 테이블의 조회 특성**
    1. Engram의 테이블은 크지만, 각 조회는 작다.
    2. DeepSeek-V4.1-Flash는 두 Engram 레이어 각각에서 24개의 행을 요청하며, 모델 전체에서 처리된 토큰 위치당 약 12.4KiB, 4개의 GPU로 분할 시 GPU당 3.1KiB이다.
2. **MI355X의 성능 및 AMD vLLM의 문제점**
    1. 모델 출시 7일차 현재, MI355X는 B200에 비해 달러당 성능이 2-4배 낮으며, MI355X의 낮은 총 소유 비용(TCO)을 고려해도 마찬가지이다.
    2. 총 소유 비용 분석은 AI 클라우드 TCO 모델과 100개 이상의 GPU 클라우드 및 GPU 클라우드 고객에 대한 월별 시장 조사를 기반으로 한다.
    3. DeepSeekv4.1 Flash 출시 당일, NVIDIA vLLM은 H100, H200, B200, B300, GB200, GB300 등 6개 SKU 모두에서 문제없이 작동했다. 이는 NVIDIA 및 Interact 팀의 놀라운 노력 덕분이다.
    4. 이에 비해 AMD vLLM은 DeepSeekv4.1 Flash 출시 당일 작동하지 않았다.
    <img alt="NVIDIA vLLM과 AMD vLLM의 DeepSeekv4.1 Flash 지원 현황 비교" src="https://substackcdn.com/image/fetch/$s_!8jLf!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd87f68d4-6472-4aa2-8b98-fda4cf16e148_1918x1254.png" caption="출처: vLLM AMD">
    5. AMD의 vLLM 문서는 vllm/vllm-openai-rocm:deepseekv41-flash-0909 사용을 지시하지만, 모델 출시 0시간부터 23시간까지 AMD는 이미지를 공개적으로 출시하지 않았다.
    6. AMD는 "속도가 해자"라고 주장하지만, 23시간이 지나도 출시하지 않았다.
    7. 앞으로 AMD 팀이 0시간 모델 출시에 대한 더 나은 프로세스를 갖기를 바란다.
    <img alt="AMD vLLM의 DeepSeekv4.1 Flash 이미지 출시 지연을 보여주는 차트" src="https://substackcdn.com/image/fetch/$s_!4J-t!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe40700af-36e7-41c7-82c7-b5eed85bec19_1700x1162.png" caption="출처: vLLM, AMD, DockerHub">
3. **AMD의 성능 개선에도 불구하고 NVIDIA와의 격차**
    1. 결국 "0일차" 이미지 지원을 위해 공개적으로 출시했을 때, 성능 면에서 H200보다 달러당 성능이 최대 14.8배, B200/B300보다 최대 42배 낮았다.
    2. CUDA MOAT의 힘은 NVIDIA가 vLLM 및 SGLang 및 Tokenspeed 유지 관리자 대부분을 포함하는 6백만 개발자 커뮤니티 생태계와의 협력에 있으며, 이는 CUDA가 0일차에 최적화된다는 것을 의미한다.
    3. 전반적으로 AMD는 상당한 개선을 이루었지만, 달러당 성능은 여전히 B200보다 2-4배 낮다.

### 3.2. AgentX Engram DRAM 오프로딩을 통한 성능 향상
1. **HBM 및 DRAM 오프로드의 작동 방식**
    1. HBM 및 DRAM 오프로드는 동일한 GPU 커널을 사용하여 행을 선택하고 역양자화한다.
    2. HBM의 경우 GPU 메모리를 읽고, UVA(Unified Virtual Addressing)의 경우 고정된 호스트 메모리를 직접 읽는다.
    3. 둘 다 전체 디코드 그래프를 지원한다.
    4. 테이블을 HBM으로 이동하면 희소 조회만 가속화되고 디코더 계산 및 통신은 변경되지 않아 전반적인 이점이 거의 없으며 KV 캐시에 사용할 수 있는 메모리를 소비한다.
2. **Engram DRAM 오프로딩의 이점**
    1. Engram을 DRAM으로 오프로딩하는 또 다른 이점은 복제본당 HBM GPU를 적게 사용하여 통신 오버헤드를 줄일 수 있다는 것이다.
    2. 예를 들어, B300에서 Engram 오프로딩을 활성화하면 TP4에서 TP2로 전환할 수 있어 파레토 곡선을 최대 1.6배 향상시킨다.
    <img alt="Engram DRAM 오프로딩이 B300에서 TP4에서 TP2로 전환하여 파레토 곡선을 향상시키는 것을 보여주는 그래프" src="https://substackcdn.com/image/fetch/$s_!NpaA!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa66eaf4d-e1c6-4967-bee8-5c3b995ef41d_1922x1214.png" caption="출처: SemiAnalysis InferenceX">
3. **HBM 대역폭의 중요성 및 최적화된 DRAM 오프로드**
    1. 동일 모델 품질에서 Engram을 호스트 DRAM으로 오프로드할 수 있으므로 더 적은 HBM이 필요하다.
    2. 따라서 HBM 대역폭이 HBM 용량보다 훨씬 더 중요하다.
    3. 메모리 대역폭이 가장 중요한 추론 워크로드의 경우, 4-hi HBM이 최고의 $/대역폭을 제공하므로 토큰당 비용이 가장 낮다.
    4. 중국이 점점 더 혁신적인 모델 아키텍처 혁신을 계속한다면, 곧 0Hi HBM 스택도 가능할 수 있다.
    5. 또한 B300 및 week-0 스택에서 Engram 테이블을 HBM으로 다시 이동해도 결과가 개선되지 않고 실행 간 변동 범위 내에 머물렀다.
    6. 이는 비동기 및 오버랩과 같은 DRAM 오프로드 최적화 작업의 결과이다.

### 3.3. SSD 오프로딩의 한계 및 비효율성
1. **B200에서 SSD 오프로딩 구현 및 작동 방식**
    1. B200에서 최적화되지 않은 vLLM 포크를 생성하고 Engram 테이블을 로컬 SSD의 메모리 매핑 파일에 저장했다.
    2. 파일 백업을 통해 다른 애플리케이션에 RAM이 필요할 때 OS가 테이블 페이지를 회수할 수 있다.
    3. 이미 메모리에 캐시된 페이지는 SSD를 다시 읽지 않고도 서비스될 수 있다.
    4. 또한 GDS를 켤 수 없었다는 점에 유의해야 한다.
    5. 최적화되지 않은 SSD 구현은 행이 GPU에 도달하는 방식을 변경한다.
    6. 행 ID를 CPU로 복사하고, 중복을 제거하고, 요청된 행을 고정된 버퍼로 수집하고, 해당 행을 GPU로 다시 복사하고 역양자화한다.
    7. 이 작업은 GPU 실행 그래프의 세그먼트 사이에 실행된다.
    8. 네이티브 UVA는 GPU에서 직접 행 선택 및 역양자화를 수행하여 CPU 왕복을 피한다.
2. **SSD 오프로딩의 성능 저하 원인**
    1. 웜 파일 시스템 캐시는 물리적 SSD 읽기를 제거하지만, 조정, 행 수집 및 전송은 남긴다.
    2. 이것이 RAM에 이미 캐시된 파일이 고정된 DRAM 테이블보다 성능이 떨어질 수 있는 이유이다.
    3. 비교는 전체 서비스 경로를 측정하며, 이러한 각 작업에 소요된 시간을 분리하지 않는다.
3. **DRAM 대비 SSD 오프로딩의 비효율성**
    1. B200 DRAM은 달러당 총 토큰 및 P90 상호작용성 측면에서 측정된 두 SSD 서비스 곡선 모두를 지배한다.
    2. 사용자당 약 125 토큰/초에서 DRAM은 달러당 1억 2천 1백만 총 토큰을 제공하는 반면, SSD는 5천 2백만 토큰을 제공한다.
    <img alt="B200에서 DRAM과 SSD 오프로딩의 달러당 총 토큰 및 P90 상호작용성 비교 그래프" src="https://substackcdn.com/image/fetch/$s_!JLpv!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fcfe5b9-1ec1-44e2-9c21-be862536931c_1698x1504.png" caption="출처: SemiAnalysis InferenceX">
    3. 프로덕션 서비스의 경우, SSD 오프로딩은 트레이드오프할 가치가 없을 가능성이 높다.
    4. 측정된 B200 구성에서 SSD 오프로딩은 두 가지 측정치 모두에서 손실을 보였다. 관찰된 모든 SSD 지점은 더 높은 P90 상호작용성과 달러당 더 많은 총 토큰을 제공하는 DRAM 대안을 가지고 있다.
    5. 더 저렴한 스토리지가 자동으로 더 저렴한 추론 서비스를 생산하지는 않는다.
    6. Engram을 SSD로 이동해도 동일한 4개의 비싼 GPU와 나머지 서버는 그대로 유지된다.
    7. RAM 회수는 더 저렴한 서버 구성이나 추가 유용한 용량을 가능하게 할 때만 경제적 이점을 창출한다.
    8. 현재 최적화되지 않은 경로는 어떠한 이점도 제공하지 않으며, 테이블 페이지가 상주할 때 파일 시스템 캐시는 여전히 RAM을 소비한다.

## 4. 메커니즘
DeepSeekv4.1 Flash, LongCat, Qwen3.8 Flash Next의 n-그램 메커니즘 및 특정 구현을 살펴볼 예정이다.

### 4.1. n-그램 구현 메커니즘
1. **DeepSeekv4.1 Flash, LongCat, Qwen3.8 Flash Next의 n-그램 메커니즘 및 특정 구현**
    1. 다음으로 DeepSeekv4.1 Flash, LongCat, Qwen3.8 Flash Next의 n-그램 메커니즘 및 특정 구현을 살펴볼 예정이다.
