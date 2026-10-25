---
title: The Huawei-DeepSeek Symbiosis
origin: lilys_ai
lilys_project_id: 11875849
lilys_project_url: https://lilys.ai/digest/11875849
lilys_created_at: '2026-10-23T13:27:00.370Z'
lilys_collection: AI
source_type: webPage
lilys_note_id: '15763758'
sources:
- id: '21078599'
  source_type: webPage
  url: https://newsletter.semianalysis.com/p/huawei-deepseek
  title: The Huawei-DeepSeek Symbiosis
  status: ready
---

# The Huawei-DeepSeek Symbiosis

## LilysAI note

> 화웨이와 DeepSeek의 협력은 어떤 의미를 가지는가? 화웨이는 **하드웨어와 소프트웨어 스택**을, DeepSeek은 **워크로드와 엔지니어링 역량**을 상호 보완하며 중국 내 완전한 AI 생태계를 구축하고, 엔비디아와의 기술 격차를 줄이는 데 중요한 역할을 합니다.

## 1. 화웨이-DeepSeek 협력의 중요성[^1]
화웨이와 DeepSeek의 협력은 중국 내 완전한 AI 생태계를 구축하고 엔비디아와의 기술 격차를 줄이는 데 핵심적인 역할을 한다.

### 1.1. 상호 보완적 관계[^2]
1. **각자의 부족한 부분을 채워주는 협력 관계**[^3]
    1. 화웨이는 Pangu를 보유하고 있지만, 칩이 모델을 훈련하거나 추론할 수 있음을 증명할 선도적인 연구소가 부족하다.[^4]
    2. DeepSeek은 모델을 가지고 있지만, 필요한 컴퓨팅 자원을 확보하기 어렵다.[^4]
    3. 화웨이는 하드웨어와 네이티브 소프트웨어 스택을 제공하고, DeepSeek은 워크로드와 하드웨어를 모델에 유용하게 만드는 데 필요한 엔지니어링 역량을 제공한다.[^5]
2. **DeepSeek의 Ascend 지원 릴리스**[^6]
    1. 중국 국경절 연휴 직전, DeepSeek은 TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, DeepSelect에 대한 Ascend 지원을 발표했다.[^7]
    2. 9월 30일 DeepSeek 저장소에 Ascend 지원이 릴리스된 것은 커널 작성 언어를 통한 이러한 교환의 결과물이다.[^8]

<img alt="화웨이-DeepSeek 협력 다이어그램" src="https://substackcdn.com/image/fetch/$s_!bPeB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31b1b07c-129f-41be-a954-9806473f0d99_1764x1283.png">
<figcaption>출처: SemiAnalysis - *다이어그램은 시뮬레이션이다.*</figcaption>

### 1.2. 중국 국내 AI 생태계 구축 가속화[^9]
1. **화웨이 스택의 주요 활용 전망**[^10]
    1. 2028년 또는 2027년에는 DeepSeek이 주로 화웨이 스택을 사용할 가능성이 높다.[^10]
    2. 이는 완전한 중국 국내 생태계를 구축하려는 외부 및 내부 압력 때문이다.[^10]
2. **화웨이 생태계의 성숙도**[^11]
    1. 화웨이 생태계는 이미 성숙하고 잘 개발되어 있으며, Ascend 시대부터 강력한 기반을 가지고 있다.[^11]
    2. DeepSeek 엔지니어들은 이 기반 위에 추가적인 개발을 진행하고 있다.[^11]

### 1.3. 본 문서의 주요 내용[^12]
1. **Ascend 950PR 아키텍처 및 성능 분석**[^13]
    1. Ascend 950PR의 아키텍처를 검토하고 컴퓨팅 및 메모리 성능을 벤치마크한다.[^13]
2. **DeepSeek 소프트웨어 릴리스 탐구**[^14]
    1. TileLang의 컴파일러 기능부터 하드웨어별 커널 최적화 및 랙 스케일 통신까지 DeepSeek의 소프트웨어 릴리스를 살펴본다.[^14]
3. **DeepSeek-V4.1-Flash 실행 프로파일 분석**[^15]
    1. DeepSeek-V4.1-Flash의 실행 프로파일을 분석한다.[^15]

## 2. Ascend 950 아키텍처 및 성능[^16]
Ascend 950은 다양한 변형이 존재하며, 컴퓨팅 및 메모리 성능 벤치마크에서 높은 활용률을 보이지만 절대적인 성능은 엔비디아 H100에 비해 뒤처진다.

### 2.1. Ascend 950 아키텍처 개요[^17]
1. **CANN 및 Ascend 950 아키텍처 심층 분석**[^18]
    1. DeepSeek V4 Pro 기사에서 CANN 및 Ascend 950 아키텍처에 대해 심층적으로 다루었으며, 이후 더 흥미로운 세부 정보가 공개되었다.[^18]

<img alt="Ascend 950 아키텍처 다이어그램" src="https://substackcdn.com/image/fetch/$s_!yKZi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3363fa3-47b2-4528-bde4-0a86ba907d25_1456x926.png">
<figcaption>출처: SemiAnalysis</figcaption>

2. **Ascend 950PR/DT의 다양한 변형**[^19]
    1. 950PR/DT는 코어 수, HBM 스택 높이, 캐시 크기가 다양한 여러 변형으로 출시되었다.[^20]
    2. 일부는 가상화/시뮬레이션되거나 테스트용일 가능성이 있다.[^21]
    3. 이는 다이 및 HBM 스택의 일부만이 목표 사양을 충족하기 때문이며, 화웨이는 컴퓨팅과 메모리를 여러 SKU로 분류하고 약한 메모리를 약한 컴퓨팅과 짝지어 사용한다.[^22]
        1. 엔비디아는 컴퓨팅만 분류한다.[^22]

<img alt="Ascend 950PR/DT 변형 표" src="https://substackcdn.com/image/fetch/$s_!3Llo!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe97ec04e-772a-4f61-9984-c46af4e5720b_2047x917.png">

<img alt="Ascend 950PR/DT 변형 표" src="https://substackcdn.com/image/fetch/$s_!ntMN!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F670401d3-ae2b-44ce-8bfe-b87f7eebd4bb_2677x533.png">
<figcaption>출처: SemiAnalysis</figcaption>

3. **Ascend 910B의 변형 사례**[^23]
    1. 910B도 910B1, 910B2, 910B3, 910B4와 같은 변형이 존재한다.[^23]
    2. 다음 마이크로벤치마크에서는 28개의 큐브 코어와 128GiB HBM을 갖춘 Ascend 950PR_9579를 사용한다.[^23]

### 2.2. Ascend 950PR 컴퓨팅 및 메모리 성능 벤치마크[^24]
1. **포인터 추적 테스트 결과**[^25]
    1. 16KiB의 정수 페이로드를 읽는 포인터 추적 테스트에서, 18블록까지는 약 134ns를 유지하다가 56블록에서 182ns로 증가하고, 64블록에서 391ns로 급증한다.[^26]
    2. 이는 56개 벡터 코어를 넘어선 두 번째 웨이브와 일치하는 결과이다.[^26]

<img alt="Ascend 950PR 포인터 추적 테스트 결과" src="https://substackcdn.com/image/fetch/$s_!b4Kk!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a315507-0998-4335-841e-994ed23ddd38_2048x754.png">
<figcaption>출처: SemiAnalysis</figcaption>

2. **코어 간 주소 프로파일 분석**[^27]
    1. 각 큐브 및 벡터 코어에서 128MiB 체인 전체의 일치하는 주소에서 로드 타이밍을 기록하는 스칼라 포인터 추적 프로브를 실행한다.[^28]
    2. 각 셀의 색상은 두 코어의 주소 프로파일 간 평균 절대 차이를 나타내며, 디코딩된 다이와 일치하는 두 그룹을 생성한다.[^29]

<img alt="Ascend 950PR 코어 간 주소 프로파일" src="https://substackcdn.com/image/fetch/$s_!k-Ny!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff757e4d-1075-4230-9834-30076b620067_2048x1766.png">
<figcaption>출처: SemiAnalysis</figcaption>

3. **자원 공유 서브시스템 식별**[^30]
    1. 다른 코어가 메모리 트래픽 또는 레지스터 전용 작업을 실행하는 동안 벡터 코어의 포인터 추적 시간을 측정하여 추가적인 속도 저하를 통해 어떤 서브시스템이 자원을 공유하는지 파악한다.[^31]
    2. 이를 통해 {0,2,4} 및 {1,3,5}와 같은 그룹을 지원하는 것을 확인한다.[^31]
    3. 혼합 큐브/벡터 실행은 각 서브시스템의 하나의 큐브와 두 개의 벡터를 식별하며, 이를 해당 그룹 내에서 함께 그린다.[^32]
        1. 물리적 위치는 개략적으로 유지된다.[^32]

<img alt="Ascend 950PR 자원 공유 서브시스템 다이어그램" src="https://substackcdn.com/image/fetch/$s_!zDr8!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21a69dca-aa4a-493a-826c-5a553ab5b23c_2048x1156.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 2.3. NPU 내 CPU (AICPU)[^33]
1. **AICPU의 구성 및 역할**[^34]
    1. 각 950PR에는 가변적인 수의 Linx816 AArch64 ELF AICPU가 포함되어 있다.[^35]
    2. MIDR 숫자는 이 코어들이 Kirin 9000S/9010의 미들 코어와 동일할 가능성이 있음을 시사한다.[^36]
    3. 이 SKU의 경우, 7개의 AICPU가 구성되어 있고, 6개가 보이며, 5개가 실행 중이다.[^37]
    4. AICPU는 장치 제어 외에도 KV 메타데이터와 같은 CPU-연산자 지원을 제공할 수 있다.[^38]
    5. AICPU는 D2H 오버헤드가 대부분의 시간을 차지하는 짧은 작업에 유용하다.[^39]
2. **DSA에서의 AICPU 활용**[^40]
    1. DSA의 경우, 작은 스케줄링 단계는 현재 시퀀스 길이를 읽고 인덱서 작업을 가속기 코어에 할당한다.[^41]
    2. 큐브/벡터 코어는 INT8 인덱서 점수를 계산하고 상위 2,048개 인덱스를 선택한다.[^42]
    3. 이러한 계획, 인덱스 선택 및 수집 단계는 vLLM-ascend 구현에서 AICPU에서 실행되며, 호스트 CPU에서 실행하는 것과 성능을 비교한다.[^43]

<img alt="AICPU 성능 비교 그래프" src="https://substackcdn.com/image/fetch/$s_!Bp9u!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff134f741-de67-4f8a-8ee2-e5c8b23f19f6_2048x933.png">
<figcaption>출처: SemiAnalysis</figcaption>

3. **AICPU의 제한된 활용성**[^44]
    1. AICPU는 제한된 컴퓨팅 성능으로 인해 오버헤드가 지배적인 짧은 작업과 데이터가 NPU에서 시작되고 소비되는 작업에만 적합하다.[^44]

### 2.4. 마이크로벤치마크 결과[^45]
1. **Ascend 950PR의 설계 목적**[^46]
    1. Ascend 950PR은 프리필(prefill) 및 추천(recommendation)을 위해 설계되었다.[^46]
    2. 더 큰 형제인 950DT보다 낮은 메모리 대역폭과 코어를 가진다.[^46]
2. **BF16 GEMM 성능 비교**[^47]
    1. DeepSeek의 기여가 아닌, aclnnMatmul_MatMulV3Common_MatMulV3로 해결되는 스톡 torch.matmul on ascend의 결과이다.[^48]
    2. 여러 오픈소스 모델에서 1,055개의 BF16 GEMM 형태를 비교했다.[^48]
    3. 화웨이의 최고 커널은 이론적 최대치의 99.7%에 도달하여, DeepGEMM의 99% 이상이 활용률을 극대화하는 유일한 방법이 아님을 보여준다.[^49]
    4. 화웨이 엔지니어들도 좋은 작업을 수행했다.[^50]

<img alt="BF16 GEMM 성능 비교 그래프" src="https://substackcdn.com/image/fetch/$s_!MQ5M!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda5c0a0e-1d96-4cfa-82a1-4abc4e516e56_2048x729.png">
<figcaption>출처: SemiAnalysis</figcaption>

3. **컴퓨팅 바운드 작업에서의 이점**[^51]
    1. 이점은 컴퓨팅 바운드 작업에 집중되어 있다.[^52]
    2. Ascend의 능선 아래 형태에서, 달성/가능한 중앙값 비율은 H100의 46.8%에 비해 41.5%이다.[^53]
    3. 엔비디아의 일부 결과는 전력 제한으로 인해 최대 SM 클럭에 도달하지 못했다.[^54]
        1. 700W 제한 중 약 690-698W의 중앙값 전력 소비와 1830MHz의 최대치보다 낮은 1335-1470MHz의 중앙값 샘플링 SM 클럭을 기록했다.[^54]
    4. 화웨이는 1650MHz 기준에 대해 599-600W, 1500-1550MHz를 기록했다.[^55]
4. **MXU 설계의 높은 활용률 기여**[^56]
    1. Ascend의 MXU 설계는 이러한 높은 활용률에 기여할 수 있다.[^57]
    2. Ascend는 전용 L0A/L0B 버퍼에 행렬 피연산자를 스테이징하고 L0C에 누산기를 스테이징하며, 이동, 계산 및 결과 처리가 중첩된다.[^57]
    3. 화웨이는 확장된 L0C가 더 유연한 타일링 및 재사용과 관련이 있다고 설명한다.[^58]
5. **절대 성능 비교**[^59]
    1. 950PR의 절대 성능은 A100과 MI300X 사이에 위치하며 뒤처진다.[^60]

<img alt="절대 성능 비교 그래프" src="https://substackcdn.com/image/fetch/$s_!MYoo!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00c575fd-460d-478f-b8ca-13edcaa27da6_2048x729.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 2.5. HBM 메모리 대역폭 (MemBW)[^61]
1. **HBM 메모리 대역폭 측정 결과**[^62]
    1. 950PR의 유효 대역폭과 대역폭 활용률은 작은 메시지 크기 버퍼에서 H100을 능가하며, 큰 메시지 크기에서는 H100의 대역폭 활용률과 거의 일치한다.[^63]
    2. Ascend가 복사 방법을 시작 비용이 더 많이 드는 벡터 코어 TensorMove 커널로 전환함에 따라 곡선에 하락이 나타나며, 이로 인해 약간 더 큰 복사가 갑자기 더 오래 걸린다.[^64]
    3. 매우 큰 복사의 경우, 추가 비용이 상대적으로 작아져 대역폭이 다시 증가한다.[^65]
2. **높은 FLOPs/대역폭 활용률의 한계**[^66]
    1. 높은 FLOPs 활용률과 대역폭 활용률이 반드시 높은 MFU/MBU로 이어지는 것은 아니다.[^67]
    2. 특히 FSDP를 사용하는 훈련은 중첩하기 어려운 집합체, 체크포인트 및 데이터 이동을 필요로 한다.[^68]
3. **벤치마크 칩의 사회적 구성**[^69]
    1. Jalepeno 기사에서 언급했듯이, 벤치마크에서 "칩"은 단지 사회적 구성물이다.[^70]
    2. 여러 다이를 접착하여 더 큰 "칩"을 형성할 수 있다.[^71]
    3. 따라서 와트당 성능 또는 총 소유 비용(TCO)이 최상의 비교 기준이다.[^72]
    4. 그러나 중국의 경우 전력 비용이 훨씬 저렴하다.[^73]
    5. Ascend의 TCO당 성능은 향후 기사에서 분석할 예정이다.[^74]

## 3. DeepSeek 오픈소스 및 엔지니어링 협력[^75]
화웨이의 하드웨어는 엔비디아에 비해 뒤처지지만, DeepSeek과의 협력을 통해 소프트웨어 생태계는 빠르게 발전하고 있으며, 하드웨어 아키텍처가 소프트웨어 설계에 영향을 미치고 있다.

### 3.1. DeepSeek 오픈소스 현황[^76]
1. **하드웨어와 소프트웨어의 격차**[^77]
    1. 하드웨어는 성능의 상한선을 높이지만, 소프트웨어는 그 상한선에 도달할 수 있게 한다.[^78]
    2. 화웨이의 하드웨어는 엔비디아 A100에 비해 약 5년 정도 뒤처져 있을 수 있지만, 소프트웨어는 최전선에 있다.[^79]
2. **Ascend 지원 저장소의 가용성**[^80]
    1. Ascend 지원을 받은 6개 저장소(TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, DeepSelect) 중 현재(작성 시점) TileLang만 사용 가능하다.[^81]
    2. CANN 9.2.0은 아직 릴리스되지 않았으며, DeepSeek은 CANN 9.2.0을 필요로 한다.[^82]
    3. CANN 9.2.0-beta.2는 C++20 컴파일러를 제공하지 않는다.[^82]
    4. HDK는 10월 15일에 릴리스될 예정이다.[^83]
    5. 이는 2025년 DeepSeek의 오픈소스 주간 이후에 이루어지며, 당시 일부 저장소는 엔비디아 지원만으로 릴리스되었다.[^83]
3. **협력의 목표: 효율성 및 재사용성 증대**[^84]
    1. 위 결과에서 화웨이가 이미 작업을 잘 실행할 수 있음을 알 수 있다.[^84]
    2. 이러한 공생 관계는 나머지 애플리케이션과 이를 지원하는 데 필요한 작업을 더 효율적이고 재사용 가능하게 만드는 데 중점을 둔다.[^84]

### 3.2. 상호 작용하는 엔지니어링[^85]
1. **화웨이 아키텍처의 DeepSeek 소프트웨어 영향**[^86]
    1. 화웨이의 아키텍처는 이미 DeepSeek 소프트웨어의 데이터 구성 방식에 영향을 미치고 있다.[^87]
    2. 이전 FlashMLA KV-캐시 레이아웃은 양자화된 값과 스케일링 팩터를 별도의 영역에 저장했다.[^88]
    3. Ascend에서는 토큰을 가져올 때 값과 스케일에 대해 별도의 전송이 필요했다.[^89]
    4. 새로운 구현은 이들을 함께 배치하여 메모리 전송 엔진(MTE)의 전송 요청 수를 줄인다.[^90]

<img alt="FlashMLA KV-캐시 레이아웃 변경 다이어그램" src="https://substackcdn.com/image/fetch/$s_!IPZn!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f5a9ed8-ba46-4d20-9158-41641fb98a15_1850x1170.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 3.3. 빠른 커널에서 재사용 가능한 커널 엔지니어링으로[^91]
1. **TileLang의 Ascend 백엔드 통합**[^92]
    1. Ascend 950 백엔드는 별도의 화웨이 어댑터로만 존재하는 것이 아니라, 메인 TileLang 저장소에 병합되었다.[^93]
    2. 이는 Ascend의 실행 모델에 대한 네이티브 컴파일, 스케줄링, 동기화 및 런타임 통합을 추가한다.[^94]
2. **TileLang을 통한 Ascend 커널 작성 용이성**[^95]
    1. TileLang은 Ascend 커널을 더 쉽게 작성할 수 있게 하지만, 개발자는 여전히 하드웨어를 고려해야 한다.[^96]
    2. 개발자는 계산, 타일 크기 및 데이터 저장 위치를 선택한다.[^97]
    3. 컴파일러는 큐브 코어, 벡터 코어 및 데이터 전송 간의 많은 조정을 처리한다.[^98]
3. **TileLang의 성능 비교**[^99]
    1. 구현을 더 깊이 파고들어 CANN 및 Triton-ascend에 대한 성능을 살펴보면, 특정 경우에 CANN을 능가하거나 일치할 수 있음을 알 수 있다.[^100]
    2. 선호되는 구현은 크기에 따라 달라진다.[^100]
    3. 이는 웜 캐시(warm-cache)의 간단하고 순진한 벤치마크 결과이다.[^101]

<img alt="TileLang 성능 비교 그래프" src="https://substackcdn.com/image/fetch/$s_!nXcL!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09daeb23-5133-4316-a95c-afa2205f3165_2048x2032.png">
<figcaption>출처: SemiAnalysis</figcaption>

4. **AutoSchedule의 역할**[^102]
    1. AutoSchedule은 데이터 종속성 및 예상 실행 시간을 사용하여 어떤 작업이 중첩될 수 있는지 계획한다.[^103]
    2. 또한 사용 가능한 온칩 메모리 내에서 사용할 버퍼 슬롯 수를 선택하여 현재 타일이 처리되는 동안 다음 데이터를 로드할 수 있도록 한다.[^104]
    3. 기본 스케줄이 적합하지 않을 경우 개발자가 이러한 결정을 안내할 수 있다.[^105]

<img alt="AutoSchedule 다이어그램" src="https://substackcdn.com/image/fetch/$s_!BzCB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c33e708-9c7b-4a84-8cae-0eed766fcd77_1758x956.png">
<figcaption>출처: SemiAnalysis</figcaption>

    4. 950PR에서 AutoSchedule은 특히 작은 크기에서 단일 작업의 실행 시간을 최대 40%까지 줄여준다.[^106]

<img alt="AutoSchedule 성능 향상 그래프" src="https://substackcdn.com/image/fetch/$s_!jUIg!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7751b4a-8006-40e5-80f5-f877ccdd7edd_2048x793.png">
<figcaption>출처: SemiAnalysis</figcaption>

5. **컴파일러의 동기화 관리**[^107]
    1. 컴파일러는 또한 동기화를 삽입하여 작업이 필요한 데이터를 기다리도록 하고, 다른 종속성으로 인해 불필요한 대기를 제거한다.[^108]
    2. 조건부 분기도 확인하여 해당 분기가 실행되지 않을 수 있는 경우 작업이 완료되었다고 가정하지 않는다.[^109]
    3. 이는 프로그래머가 직접 관리해야 하는 동기화 작업을 줄여준다.[^110]

### 3.4. DeepEP[^111]
1. **화웨이의 대규모 AI 시스템 상용화**[^112]
    1. 화웨이는 Ascend 슈퍼노드를 통해 910 CloudMatrix384에서 950 SuperPod에 이르기까지 여러 랙에 걸쳐 긴밀하게 연결된 가속기 인터커넥트를 확장하여 대규모 AI 시스템 상용화에 엔비디아와 함께 참여하고 있다.[^113]
    2. 9월 30일 릴리스에서 화웨이는 950DT 슈퍼팟에서 URMA를 통한 EP16 디스패치/결합 벤치마크도 릴리스했다.[^114]
2. **화웨이 디스패치와 GB300의 비교**[^115]
    1. 화웨이의 디스패치는 세 개의 순차적인 연산자(pre/URMA/post)로 구성되는 반면, GB300은 하나의 융합된 호출이다.[^115]
    2. 화웨이의 사후 작업에는 수신 완료가 포함되며, 이는 측정에 포함되지만, GB300의 결과에는 없는 전문가별 확장이 포함된다.[^115]
3. **DeepEP-Ascend의 개발 및 통합**[^116]
    1. DeepEP-Ascend는 DeepEP V2.5를 포팅한 것으로, 동일한 파이썬 API를 사용하지만 내부적으로 URMA 및 HCCL을 호출한다.[^117]
    2. 2025년 7월, 화웨이 Ascend 팀은 deepseek-ai 아래에 DeepEP-Ascend를 제안했지만, DeepEP 유지 관리자가 거부했다.[^118]
    3. 현재 DeepEP-Ascend는 DeepSeek 자체 조직에서 배포된다.[^119]
4. **통신 및 계산 중첩의 과제**[^120]
    1. Ascend의 별도 큐브 및 벡터 실행 경로는 통신과 계산을 중첩할 기회를 제공하지만, 이러한 중첩이 무료로 이루어지는 것은 아니다.[^121]
    2. 전문가 계산은 벡터 처리 및 데이터 이동을 필요로 할 수 있으며, 통신은 공유 메모리 대역폭을 놓고 경쟁한다.[^122]
    3. 따라서 함께 실행되는 계산 속도를 늦추지 않고 얼마나 많은 통신을 숨길 수 있는지에 대한 절충점이 존재한다.[^123]
5. **자원 균형 문제 및 공동 설계**[^124]
    1. 이러한 자원 균형 문제는 DeepSeek에만 국한된 것이 아니다.[^125]
    2. 화웨이의 Kimi K3 레시피는 동시 작업을 위한 용량을 확보하기 위해 벡터 사용을 명시적으로 제한하고, 중첩되어야 하는 작업에 따라 전용 CCU와 벡터 기반 통신 중에서 선택한다.[^126]
    3. 개별 작업이 빠르다고 해서 충분한 것이 아니라, 자원 요구 사항도 서로 잘 맞아야 한다.[^127]
    4. DeepEP-Ascend의 문서에는 HBM 자원에 대한 결합 처리와 URMA 통신 간의 경합이 언급되어 있으며, 이를 줄이기 위한 화웨이 펌웨어 개선이 계획되어 있다고 한다.[^128]
    5. 이는 공동 설계의 실질적인 형태이다. 모델이 병목 현상을 드러내면 구현이 적응하고, 플랫폼 개발 우선순위는 남아있는 문제에 대응한다.[^129]

### 3.5. 모든 것이 계획대로[^130]
1. **DeepSeek 투자자 회의록 인용**[^131]
    1. 5월에 공개된 미확인 DeepSeek 투자자 회의록에서 Liang Wenfeng은 다음과 같이 말했다.[^132]
    2. "중국과 미국 간의 칩 격차에 관해서는 소프트웨어 생태계 격차가 결국 사라질 것이라고 생각한다. 그러나 하드웨어 측면에서는 두 가지 별도의 단점에 직면해 있다. 화웨이 가속기 카드 4개가 엔비디아 카드 1개와 맞먹고, 화웨이는 하드웨어를 시장에 출시하는 데 약 2년 정도 뒤처져 있다."[^133]
2. **생태계 격차의 축소**[^134]
    1. 4개월 후, 생태계 격차는 실제로 좁혀졌다.[^134]
    2. 동일한 회의록에서 TileLang과 화웨이가 생태계를 올바르게 구축하는 데 도움이 되었다고 언급되었다.[^134]

## 4. DeepSeek-V4.1-Flash 최적화 및 프로파일[^135]
DeepSeek은 화웨이 하드웨어에 최적화된 모델을 제공하며, Ascend의 독특한 아키텍처를 활용하여 효율적인 연산을 수행한다.

### 4.1. DSv4.1 Flash 최적화[^136]
1. **DeepSeek의 화웨이 지원 및 최적화**[^137]
    1. DeepSeek-화웨이 공생 관계의 또 다른 부분은 DeepSeek이 화웨이에 가중치를 제공하여 DeepSeek V4 및 V4.1과 같은 Day-0 최적화 릴리스를 지원한다는 것이다.[^137]
2. **Ascend의 어텐션 처리 방식**[^138]
    1. Ascend의 누산기 설계는 어텐션에 다른 접근 방식을 강요한다.[^139]
    2. 큐브의 L0C 버퍼는 누적된 출력을 제자리에서 재조정할 수 없으며, 재조정된 출력을 L0C로 반환하려면 비용이 많이 드는 항등 행렬 곱셈이 필요하다.[^140]
    3. 대신 DeepSeek은 실행 중인 출력 누산기를 벡터 UB에 유지하고, 재조정 및 누적에 필요할 때 L0C에서 부분 합계를 전송한다.[^141]
    4. Hopper는 누산기를 레지스터에 유지하고, Blackwell은 텐서 메모리와 레지스터 간의 로드 및 저장을 제공하여 이러한 특정 제한을 피한다.[^142]

<img alt="Ascend 어텐션 처리 방식 다이어그램" src="https://substackcdn.com/image/fetch/$s_!edJT!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3741c14f-30e9-4883-950f-4a1e32af842d_2048x664.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 4.2. DeepSeek-V4.1-Flash 프로파일[^143]
1. **DeepSeek-V4.1-Flash 프로파일 공개**[^144]
    1. 화웨이는 32개 칩으로 구성된 화웨이 Ascend 950DT 배포에서 DeepSeek-V4.1-Flash의 한 랭크와 해당 호스트 스레드의 프로파일을 공개했다.[^145]
    2. 6월에는 DeepSeek V4 Pro의 유사한 프로파일을 다루었다.[^146]
2. **프로파일의 유사성**[^147]
    1. AICPU 사용 및 일부 레이어를 다른 스트림으로 분리하는 등 많은 구성 요소가 유사하다.[^147]

<img alt="DeepSeek-V4.1-Flash 프로파일 그래프" src="https://substackcdn.com/image/fetch/$s_!Jyrn!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F780f172c-a874-4a1d-b705-b439d10e1312_2048x759.png">
<figcaption>출처: SemiAnalysis</figcaption>

3. **실행 순서 및 커널 작업**[^148]
    1. 실행 순서는 40개의 타겟 모델 레이어, 타겟 LM 헤드, 3개의 DSpark 드래프터 블록, 드래프트 LM 헤드, 그리고 5번의 샘플링 라운드이다.[^149]
    2. 주요 계산은 스트림 19에서 실행되고, 드래프터는 스트림 173에서 실행된다.[^150]
    3. DSv4 Pro 트레이스에서 계산과 통신을 융합했던 V2 MC² 커널이 이번에는 V3로 다시 나타난다.[^150]
    4. 이것이 각 단계에서 43개의 전문가 디스패치에 비해 4개의 AI CPU가 시작한 HCCL 작업만 나타나는 이유이다.[^151]
    5. 이들은 타겟 및 드래프트 어휘 헤드의 hcom_allGather 및 hcom_alltoallv이다.[^152]
        1. 숨겨진 상태를 수집하고, LM-헤드 GEMM을 실행한 다음, 로짓을 교환한다.[^152]

<img alt="DeepSeek-V4.1-Flash 실행 순서 다이어그램" src="https://substackcdn.com/image/fetch/$s_!Xwin!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac3e578f-23de-4c3c-88b7-e625782f67ca_2048x831.png">
<figcaption>출처: SemiAnalysis</figcaption>

<img alt="DeepSeek-V4.1-Flash 실행 순서 다이어그램 (확대)" src="https://substackcdn.com/image/fetch/$s_!As98!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f8f988c-ff82-4a1f-b1b4-e5d6bba6b3ad_2048x843.png">
<figcaption>출처: SemiAnalysis</figcaption>

4. **드래프터 블록 및 마르코프 헤드**[^153]
    1. 드래프터 블록은 드래프트 위치에 대한 기본 로짓을 생성하기 위해 한 번 실행된다.[^154]
    2. 후속 마르코프 헤드는 샘플링 및 임베딩 피드백을 통해 토큰 종속성을 모델링한다.[^155]
    3. 각 제안에 대해 트랜스포머 블록을 다시 실행하지 않는다.[^156]
    4. 각 단계의 끝은 MoE 및 어텐션에서 작은 투영 및 샘플링 작업의 직렬 체인으로 변경된다.[^157]
5. **추측 디코딩 (Speculative Decoding)**[^158]
    1. 추측 디코딩은 드래프트 토큰을 예측하고 단일 패스를 사용하여 이를 검증하는 무손실 방법으로, 가중치 로딩을 상각한다.[^159]
    2. 위 디코딩 단계 다이어그램에서 DSpark 토큰 드래프팅이 검증 단계보다 얼마나 빠른지 확인할 수 있다.[^160]

<img alt="추측 디코딩 성능 비교 그래프" src="https://substackcdn.com/image/fetch/$s_!1b9M!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F344fe07e-5770-415f-a19d-20302d364b1f_2048x831.png">
<figcaption>출처: SemiAnalysis</figcaption>

6. **Engram 사용 및 오프로딩**[^161]
    1. DSv4.1 Flash는 Qwen 및 Meituan Longcat에 이어 Engram을 사용하는 첫 번째 DeepSeek 모델이다.[^162]
    2. Engram은 토큰 ID를 입력으로 받기 때문에, 가져오기(fetch)를 비동기적으로 수행하고 레이어 0의 계산과 중첩할 수 있다.[^163]
    3. 이를 통해 성능 손실 없이 DRAM으로 오프로딩할 수 있지만, PCIe 4.0 SSD로 오프로딩하면 성능이 저하된다.[^164]

<img alt="Engram 오프로딩 성능 그래프" src="https://substackcdn.com/image/fetch/$s_!Mglv!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4941eee2-8e0e-4af5-a669-0c30d969f0a8_2048x688.png">
<figcaption>출처: SemiAnalysis</figcaption>

7. **커널 지속 시간 요약 및 자원 활용**[^165]
    1. 안정 상태(steady-state) 창에서 커널 지속 시간을 요약하면, 스트림 19는 창의 88.8%를 차지하지만, 다른 스트림이 중첩되어 총 장치 시간의 72.6%를 기여한다.[^166]
    2. 중간에 상당한 MIX_AIV 및 AI_VECTOR_CORE 대역은 디스패치/결합뿐만 아니라 양자화도 포함한다.[^167]
    3. Ascend는 MIX_AIC, MIX_AIV, AI_CORE 및 AI_VECTOR_CORE를 통해 별도로 스케줄링된 큐브 및 벡터 경로를 노출한다.[^168]
    4. 각 이벤트에는 작업 유형이 있으므로 지속 시간 계산은 파티션이다.[^169]
    5. 혼합 유형은 여전히 단일 물리적 단위를 넘어서는 작업을 포함하며, 그 이름이 경과된 커널 지속 시간을 측정된 큐브 전용 또는 벡터 전용 활용률로 바꾸지는 않는다.[^170]

<img alt="커널 지속 시간 요약 그래프" src="https://substackcdn.com/image/fetch/$s_!vK8L!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F382a08c7-e8fa-4db1-9653-c8982c5ff491_2048x747.png">
<figcaption>출처: SemiAnalysis</figcaption>

8. **큐브 처리량 개선 시나리오**[^171]
    1. 다른 장치 작업은 변경하지 않고 큐브 처리량을 두 배로 늘리는 1차 시나리오는 1.32배의 단계 개선을 제공한다.[^172]
    2. 이는 측정된 스트림 중첩을 일정하게 유지하고 유휴 시간을 변경하지 않는다.[^173]
    3. 이는 새로운 실리콘에 대한 예측이 아닌 구성 시나리오이다.[^174]
        1. 혼합 작업 유형은 배타적인 활용률 측정이 아니며, 대역폭, 종속성 및 스케줄링이 결과에 영향을 미칠 수 있다.[^174]
9. **양자화 융합의 기회**[^175]
    1. 양자화 융합은 반복되는 생산자-소비자 경계와 융합된 통신도 수행하는 벡터 버킷의 큰 비중으로 인해 여전히 기회로 남아있다.[^175]

## 5. 생태계 격차 및 과제[^176]
화웨이와 DeepSeek의 협력은 DeepSeek에게는 매우 효과적일 수 있지만, 다른 사용자들에게 Ascend를 보편적으로 사용 가능하게 만드는 데는 여전히 과제가 남아있다.

### 5.1. DeepSeek에 편중된 협력의 한계[^177]
1. **DeepSeek에게만 효과적인 협력 가능성**[^178]
    1. 이 파트너십은 DeepSeek에게는 매우 효과적일 수 있지만, 다른 모든 사람에게 Ascend를 동등하게 사용 가능하게 만들지는 못할 수 있다.[^178]
2. **DeepSeek의 엔지니어링 부담**[^179]
    1. DeepSeek의 경우, 컴파일러 구축, 커널 유지 관리 및 공급업체별 동작 디버깅은 모델 연구 및 제품 개발과 경쟁한다.[^179]
    2. 이는 일시적인 부담일 수 있다.[^179]

### 5.2. 일반 사용자에게 Ascend 사용 시 문제점[^180]
1. **하드웨어 구성 불일치 문제**[^181]
    1. 다른 사용자들에게는 하드웨어 구성이 DeepSeek의 구성과 일치하지 않을 때 문제가 발생할 수 있다.[^181]
2. **vLLM-Ascend의 x86 호스트 지원 문제**[^182]
    1. 대부분의 최적화는 슈퍼노드에서 이루어졌으며, vLLM-Ascend_0.26.0rc1 기준으로 x86 호스트에서 Ascend와 작업할 때 여러 문제가 존재한다.[^182]
    1. x86 호스트에서 DeepGEMM 지원이 없다.[^183]
    2. vLLM-Ascend에 하드코딩된 ARM 헤더를 포함하는 `memfabric_hybrid`에 대한 종속성으로 인해 시작이 차단된다.[^184]
        1. vLLM-Ascend는 즉시 작동하지 않는다.[^184]
    3. vLLM-Ascend에서 비ARM CPU에 대한 CPU 바인딩이 건너뛴다.[^185]
    4. NPU + x86 CI가 없으며, 일부 레시피에는 패치가 필요하다.[^186]

[^1]: The Huawei-DeepSeek Symbiosis — "The Huawei-DeepSeek Symbiosis Oct 22, 2026 Huawei Ascend 950PR Deep dive & µbenchmarks, DSv4.1 Flash Analysis, DeepSeek support for Ascend, AICPU, Tilelang Ascend Right before China’s national day holidays, DeepSeek released Ascend support for TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, and D…"
[^2]: The Huawei-DeepSeek Symbiosis — "Right before China’s national day holidays, DeepSeek released Ascend support for TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, and DeepSelect. Neither can do this alone. Although they have Pangu, Huawei has no frontier lab to prove their chip can train or infer models, DeepSeek has models but c…"
[^3]: The Huawei-DeepSeek Symbiosis — "Neither can do this alone. Although they have Pangu, Huawei has no frontier lab to prove their chip can train or infer models, DeepSeek has models but cannot buy the compute it needs. Each supplies exactly what the other lacks: Huawei provides the hardware and native software stack; DeepSeek brings …"
[^4]: The Huawei-DeepSeek Symbiosis — "Although they have Pangu, Huawei has no frontier lab to prove their chip can train or infer models, DeepSeek has models but cannot buy the compute it needs."
[^5]: The Huawei-DeepSeek Symbiosis — "Each supplies exactly what the other lacks: Huawei provides the hardware and native software stack; DeepSeek brings the workloads and engineering needed to make that hardware useful for its models."
[^6]: The Huawei-DeepSeek Symbiosis — "Right before China’s national day holidays, DeepSeek released Ascend support for TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, and DeepSelect. September 30’s release of Ascend support in DeepSeek repositories is an artifact of this trade, where the exchange runs through the kernel-authoring lan…"
[^7]: The Huawei-DeepSeek Symbiosis — "Right before China’s national day holidays, DeepSeek released Ascend support for TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, and DeepSelect."
[^8]: The Huawei-DeepSeek Symbiosis — "September 30’s release of Ascend support in DeepSeek repositories is an artifact of this trade, where the exchange runs through the kernel-authoring language."
[^9]: The Huawei-DeepSeek Symbiosis — "In 2028 or even 2027, DeepSeek will likely be primarily using Huawei’s stack, especially with the external and internal pressure to build a fully domestic chinese ecosystem. As we show here and in future articles, the Huawei ecosystem is already mature and well developed, with strong foundations fro…"
[^10]: The Huawei-DeepSeek Symbiosis — "In 2028 or even 2027, DeepSeek will likely be primarily using Huawei’s stack, especially with the external and internal pressure to build a fully domestic chinese ecosystem."
[^11]: The Huawei-DeepSeek Symbiosis — "As we show here and in future articles, the Huawei ecosystem is already mature and well developed, with strong foundations from the Ascend time and DeepSeek engineers building further ontop."
[^12]: The Huawei-DeepSeek Symbiosis — "In this article, we’ll first examine Ascend 950PR’s architecture and benchmark its compute and memory performance. We then explore DeepSeek’s software releases, from TileLang’s compiler capabilities to hardware-specific kernel optimizations and rack-scale communication. Finally, we analyze DeepSeek-…"
[^13]: The Huawei-DeepSeek Symbiosis — "In this article, we’ll first examine Ascend 950PR’s architecture and benchmark its compute and memory performance."
[^14]: The Huawei-DeepSeek Symbiosis — "We then explore DeepSeek’s software releases, from TileLang’s compiler capabilities to hardware-specific kernel optimizations and rack-scale communication."
[^15]: The Huawei-DeepSeek Symbiosis — "Finally, we analyze DeepSeek-V4.1-Flash’s execution profile."
[^16]: The Huawei-DeepSeek Symbiosis — "Ascend 950 We deep-dived into CANN and the Ascend 950 architecture in our DeepSeek V4 Pro article. Since then, more interesting details have been revealed. https://substackcdn.com/image/fetch/$s_!yKZi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazon…"
[^17]: The Huawei-DeepSeek Symbiosis — "Ascend 950 We deep-dived into CANN and the Ascend 950 architecture in our DeepSeek V4 Pro article. Since then, more interesting details have been revealed. https://substackcdn.com/image/fetch/$s_!yKZi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazon…"
[^18]: The Huawei-DeepSeek Symbiosis — "We deep-dived into CANN and the Ascend 950 architecture in our DeepSeek V4 Pro article. Since then, more interesting details have been revealed."
[^19]: The Huawei-DeepSeek Symbiosis — "Starting from the chip, many variants of 950PR/DT have appeared with varying core counts, HBM stack height, and cache sizes. Some are likely either virtualised/simulated, or for testing only. This is because only a fraction of dies and HBM stacks meet the target spec, due to both outright defects an…"
[^20]: The Huawei-DeepSeek Symbiosis — "Starting from the chip, many variants of 950PR/DT have appeared with varying core counts, HBM stack height, and cache sizes."
[^21]: The Huawei-DeepSeek Symbiosis — "Some are likely either virtualised/simulated, or for testing only."
[^22]: The Huawei-DeepSeek Symbiosis — "This is because only a fraction of dies and HBM stacks meet the target spec, due to both outright defects and parametric shortfalls in power and performance, so Huawei bins both compute and memory into multiple SKUs and pairs weaker memory with weaker compute, rather than binning only compute as Nvi…"
[^23]: The Huawei-DeepSeek Symbiosis — "This isn’t new, 910B also has variants such as 910B1, 910B2, 910B3, 910B4. For the following microbenchmarks, we use an Ascend 950PR_9579, with 28 cube cores and 128 GiB HBM."
[^24]: The Huawei-DeepSeek Symbiosis — "Running point chases reading 16 KiB of integer payload per launch, it stays near 134ns through 18 blocks, rises to 182ns at 56, then jumps to 391ns at 64. This is consistent with a second wave beyond 56 Vector cores. https://substackcdn.com/image/fetch/$s_!b4Kk!,w_1456,c_limit,f_webp,q_auto:good,fl_…"
[^25]: The Huawei-DeepSeek Symbiosis — "Running point chases reading 16 KiB of integer payload per launch, it stays near 134ns through 18 blocks, rises to 182ns at 56, then jumps to 391ns at 64. This is consistent with a second wave beyond 56 Vector cores. https://substackcdn.com/image/fetch/$s_!b4Kk!,w_1456,c_limit,f_webp,q_auto:good,fl_…"
[^26]: The Huawei-DeepSeek Symbiosis — "Running point chases reading 16 KiB of integer payload per launch, it stays near 134ns through 18 blocks, rises to 182ns at 56, then jumps to 391ns at 64. This is consistent with a second wave beyond 56 Vector cores."
[^27]: The Huawei-DeepSeek Symbiosis — "Then by running a scalar pointer-chase probe separately on every Cube and Vector core, recording load timings at matching addresses throughout a 128 MiB chain, we get the following graph. Each cell’s color represents the mean absolute difference between two cores' address profiles, producing two gro…"
[^28]: The Huawei-DeepSeek Symbiosis — "Then by running a scalar pointer-chase probe separately on every Cube and Vector core, recording load timings at matching addresses throughout a 128 MiB chain, we get the following graph."
[^29]: The Huawei-DeepSeek Symbiosis — "Each cell’s color represents the mean absolute difference between two cores' address profiles, producing two groups that match the decoded dies."
[^30]: The Huawei-DeepSeek Symbiosis — "Going further, by timing a Vector core’s pointer chase while another core runs either memory traffic or register-only work; the extra slowdown reveals which subsystems share resources, supporting groups such as {0,2,4} and {1,3,5}. Mixed Cube/Vector launches identify each subsystem’s one Cube and tw…"
[^31]: The Huawei-DeepSeek Symbiosis — "Going further, by timing a Vector core’s pointer chase while another core runs either memory traffic or register-only work; the extra slowdown reveals which subsystems share resources, supporting groups such as {0,2,4} and {1,3,5}."
[^32]: The Huawei-DeepSeek Symbiosis — "Mixed Cube/Vector launches identify each subsystem’s one Cube and two Vectors, which we draw together within those groups, with physical positions remaining schematic."
[^33]: The Huawei-DeepSeek Symbiosis — "CPU within the NPU Each 950PR comes with a variable number of Linx816 AArch64 ELF AICPUs. The MIDR numbers imply these cores are likely the same as the middle cores in the Kirin 9000S/9010. These AICPU cores have instruction set: For this SKU, there are 7 configured, 6 visible, and 5 executing AICPU…"
[^34]: The Huawei-DeepSeek Symbiosis — "Each 950PR comes with a variable number of Linx816 AArch64 ELF AICPUs. The MIDR numbers imply these cores are likely the same as the middle cores in the Kirin 9000S/9010. These AICPU cores have instruction set: For this SKU, there are 7 configured, 6 visible, and 5 executing AICPU cores. Other than …"
[^35]: The Huawei-DeepSeek Symbiosis — "Each 950PR comes with a variable number of Linx816 AArch64 ELF AICPUs."
[^36]: The Huawei-DeepSeek Symbiosis — "The MIDR numbers imply these cores are likely the same as the middle cores in the Kirin 9000S/9010. These AICPU cores have instruction set:"
[^37]: The Huawei-DeepSeek Symbiosis — "For this SKU, there are 7 configured, 6 visible, and 5 executing AICPU cores."
[^38]: The Huawei-DeepSeek Symbiosis — "Other than device control it can provide CPU-operator support, such as KV metadata."
[^39]: The Huawei-DeepSeek Symbiosis — "The AICPU helps out for short work where D2H overhead take up most of the time."
[^40]: The Huawei-DeepSeek Symbiosis — "For DSA, a small scheduling step reads the current sequence lengths and assigns indexer work to accelerator cores. Cube/Vector cores then compute INT8 indexer scores and select the top 2,048 indices. These planning, index selection, and gather steps are ran on AICPUs in vLLM-ascend implementation, a…"
[^41]: The Huawei-DeepSeek Symbiosis — "For DSA, a small scheduling step reads the current sequence lengths and assigns indexer work to accelerator cores."
[^42]: The Huawei-DeepSeek Symbiosis — "Cube/Vector cores then compute INT8 indexer scores and select the top 2,048 indices."
[^43]: The Huawei-DeepSeek Symbiosis — "These planning, index selection, and gather steps are ran on AICPUs in vLLM-ascend implementation, and we compare their performance to running on the host CPU."
[^44]: The Huawei-DeepSeek Symbiosis — "Due to their limited compute performance, AICPU is only good for short work where overhead dominates, and work where data starts and is consumed at the NPU."
[^45]: The Huawei-DeepSeek Symbiosis — "Microbenchmarks Ascend 950PR is designed for prefill and recommendation. It gets lower memory bandwidth and core than its bigger brother the 950DT. The results below are not from DeepSeek’s contributions but from stock torch.matmul on ascend resolving to aclnnMatmul_MatMulV3Common_MatMulV3. We compa…"
[^46]: The Huawei-DeepSeek Symbiosis — "Ascend 950PR is designed for prefill and recommendation. It gets lower memory bandwidth and core than its bigger brother the 950DT."
[^47]: The Huawei-DeepSeek Symbiosis — "The results below are not from DeepSeek’s contributions but from stock torch.matmul on ascend resolving to aclnnMatmul_MatMulV3Common_MatMulV3. We compared 1,055 BF16 GEMM shapes from several open-sourced models. Huawei’s best kernels hits 99.7% of the ceiling, showing DeepSeek’s 99+% from DeepGEMM …"
[^48]: The Huawei-DeepSeek Symbiosis — "The results below are not from DeepSeek’s contributions but from stock torch.matmul on ascend resolving to aclnnMatmul_MatMulV3Common_MatMulV3. We compared 1,055 BF16 GEMM shapes from several open-sourced models."
[^49]: The Huawei-DeepSeek Symbiosis — "Huawei’s best kernels hits 99.7% of the ceiling, showing DeepSeek’s 99+% from DeepGEMM isn’t the only way to maximize utilization."
[^50]: The Huawei-DeepSeek Symbiosis — "Huawei engineers did good work too."
[^51]: The Huawei-DeepSeek Symbiosis — "The advantage is concentrated in compute-bound work. On the shapes below Ascend’s ridge, its median achieved/attainable fraction is 41.5% versus H100’s 46.8%. Some of Nvidia’s results were power-limited and did not hit maximum SM clock: median power around 690-698 W out of a 700 W limit, and median …"
[^52]: The Huawei-DeepSeek Symbiosis — "The advantage is concentrated in compute-bound work."
[^53]: The Huawei-DeepSeek Symbiosis — "On the shapes below Ascend’s ridge, its median achieved/attainable fraction is 41.5% versus H100’s 46.8%."
[^54]: The Huawei-DeepSeek Symbiosis — "Some of Nvidia’s results were power-limited and did not hit maximum SM clock: median power around 690-698 W out of a 700 W limit, and median sampled SM clocks at 1335-1470 MHz, below the max of 1830 MHz."
[^55]: The Huawei-DeepSeek Symbiosis — "Huawei approximated 599-600 W, at 1500-1550 MHz against its 1650 MHz reference."
[^56]: The Huawei-DeepSeek Symbiosis — "Ascend’s MXU design may contribute to some of this high utilization, Ascend stages matrix operands in dedicated L0A/L0B buffers and accumulators in L0C, with overlapping movement, computation and result handling. Huawei associates the enlarged L0C with more flexible tiling and reuse."
[^57]: The Huawei-DeepSeek Symbiosis — "Ascend’s MXU design may contribute to some of this high utilization, Ascend stages matrix operands in dedicated L0A/L0B buffers and accumulators in L0C, with overlapping movement, computation and result handling."
[^58]: The Huawei-DeepSeek Symbiosis — "Huawei associates the enlarged L0C with more flexible tiling and reuse."
[^59]: The Huawei-DeepSeek Symbiosis — "But of course, 950PR’s falls behind on absolute values, sitting somewhere between A100 and MI300X. https://substackcdn.com/image/fetch/$s_!MYoo!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00c575fd-460d-478f-b8ca-13edc…"
[^60]: The Huawei-DeepSeek Symbiosis — "But of course, 950PR’s falls behind on absolute values, sitting somewhere between A100 and MI300X."
[^61]: The Huawei-DeepSeek Symbiosis — "MemBW Measuring HBM memory bandwidth, we see 950PR’s effective bandwidth and bandwidth utilization surpassing H100 at small message size per buffers, and nearly matching H100 in bandwidth utilization at large message sizes. A dip appears in the curve as Ascend switches copy methods to a Vector-core …"
[^62]: The Huawei-DeepSeek Symbiosis — "Measuring HBM memory bandwidth, we see 950PR’s effective bandwidth and bandwidth utilization surpassing H100 at small message size per buffers, and nearly matching H100 in bandwidth utilization at large message sizes. A dip appears in the curve as Ascend switches copy methods to a Vector-core Tensor…"
[^63]: The Huawei-DeepSeek Symbiosis — "Measuring HBM memory bandwidth, we see 950PR’s effective bandwidth and bandwidth utilization surpassing H100 at small message size per buffers, and nearly matching H100 in bandwidth utilization at large message sizes."
[^64]: The Huawei-DeepSeek Symbiosis — "A dip appears in the curve as Ascend switches copy methods to a Vector-core TensorMove kernel that has more startup cost, so a slightly larger copy suddenly takes longer."
[^65]: The Huawei-DeepSeek Symbiosis — "For very large copies, that extra cost becomes relatively small, so bandwidth rises again."
[^66]: The Huawei-DeepSeek Symbiosis — "Note that high FLOPs utilization and bandwidth utilization does not necessarily translate to high MFU/MBU. Training, especially with FSDP, requires collectives, checkpointing, and data moving that can be hard to overlap."
[^67]: The Huawei-DeepSeek Symbiosis — "Note that high FLOPs utilization and bandwidth utilization does not necessarily translate to high MFU/MBU."
[^68]: The Huawei-DeepSeek Symbiosis — "Training, especially with FSDP, requires collectives, checkpointing, and data moving that can be hard to overlap."
[^69]: The Huawei-DeepSeek Symbiosis — "As we mentioned in our Jalepeno article, a “chip” in benchmarks is just a social construct. Multiple dies can be glue to form a bigger “chip”. Thus performance per watt or TCO is the best comparison. But for China, watts are far cheaper. We’ll analyze Ascend’s perf per TCO in a future article."
[^70]: The Huawei-DeepSeek Symbiosis — "As we mentioned in our Jalepeno article, a “chip” in benchmarks is just a social construct."
[^71]: The Huawei-DeepSeek Symbiosis — "Multiple dies can be glue to form a bigger “chip”."
[^72]: The Huawei-DeepSeek Symbiosis — "Thus performance per watt or TCO is the best comparison."
[^73]: The Huawei-DeepSeek Symbiosis — "But for China, watts are far cheaper."
[^74]: The Huawei-DeepSeek Symbiosis — "We’ll analyze Ascend’s perf per TCO in a future article."
[^75]: The Huawei-DeepSeek Symbiosis — "Hardware raises the ceiling, but software lets you reach that ceiling. Although Huawei’s hardware may be beyond ~5 years behind(compared to A100), the software is right at the frontier. DeepSeek Open Source For the 6 repos that received ascend support(TileLang, DeepGEMM, DeepEP, TileKernels, FlashML…"
[^76]: The Huawei-DeepSeek Symbiosis — "Hardware raises the ceiling, but software lets you reach that ceiling. Although Huawei’s hardware may be beyond ~5 years behind(compared to A100), the software is right at the frontier. DeepSeek Open Source For the 6 repos that received ascend support(TileLang, DeepGEMM, DeepEP, TileKernels, FlashML…"
[^77]: The Huawei-DeepSeek Symbiosis — "Hardware raises the ceiling, but software lets you reach that ceiling. Although Huawei’s hardware may be beyond ~5 years behind(compared to A100), the software is right at the frontier."
[^78]: The Huawei-DeepSeek Symbiosis — "Hardware raises the ceiling, but software lets you reach that ceiling."
[^79]: The Huawei-DeepSeek Symbiosis — "Although Huawei’s hardware may be beyond ~5 years behind(compared to A100), the software is right at the frontier."
[^80]: The Huawei-DeepSeek Symbiosis — "For the 6 repos that received ascend support(TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, DeepSelect), only TileLang is usable as of writing, and CANN 9.2.0 has not been released. Deepseek requires CANN 9.2.0 which was released after time of writing, and a C++20 compiler is required which CANN…"
[^81]: The Huawei-DeepSeek Symbiosis — "For the 6 repos that received ascend support(TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, DeepSelect), only TileLang is usable as of writing, and CANN 9.2.0 has not been released."
[^82]: The Huawei-DeepSeek Symbiosis — "Deepseek requires CANN 9.2.0 which was released after time of writing, and a C++20 compiler is required which CANN 9.2.0-beta.2 does not provide."
[^83]: The Huawei-DeepSeek Symbiosis — "The HDK will be released on Oct 15. This comes after DeepSeek’s open source week in 2025, where some of these repositories were released with Nvidia support only."
[^84]: The Huawei-DeepSeek Symbiosis — "From the results above, we can see Huawei can already execute operations well; the symbiosis is about making the rest of the application & the work required to support it more efficient and reusable."
[^85]: The Huawei-DeepSeek Symbiosis — "Engineering runs both ways Huawei’s architecture is already influencing how DeepSeek’s software organizes data. Earlier FlashMLA KV-cache layouts stored quantized values and their scaling factors in separate regions. On Ascend, fetching a token then required separate transfers for its values and sca…"
[^86]: The Huawei-DeepSeek Symbiosis — "Huawei’s architecture is already influencing how DeepSeek’s software organizes data. Earlier FlashMLA KV-cache layouts stored quantized values and their scaling factors in separate regions. On Ascend, fetching a token then required separate transfers for its values and scales. The new implementation…"
[^87]: The Huawei-DeepSeek Symbiosis — "Huawei’s architecture is already influencing how DeepSeek’s software organizes data."
[^88]: The Huawei-DeepSeek Symbiosis — "Earlier FlashMLA KV-cache layouts stored quantized values and their scaling factors in separate regions."
[^89]: The Huawei-DeepSeek Symbiosis — "On Ascend, fetching a token then required separate transfers for its values and scales."
[^90]: The Huawei-DeepSeek Symbiosis — "The new implementation places them together, reducing the number of transfer requests by the memory transfer engine(MTE)."
[^91]: The Huawei-DeepSeek Symbiosis — "From fast kernels to reusable kernel engineering Ascend 950 backend is merged into the main TileLang repository, rather than existing only in a separate Huawei adapter. It adds native compilation, scheduling, synchronization and runtime integration for Ascend’s execution model. TileLang makes Ascend…"
[^92]: The Huawei-DeepSeek Symbiosis — "Ascend 950 backend is merged into the main TileLang repository, rather than existing only in a separate Huawei adapter. It adds native compilation, scheduling, synchronization and runtime integration for Ascend’s execution model."
[^93]: The Huawei-DeepSeek Symbiosis — "Ascend 950 backend is merged into the main TileLang repository, rather than existing only in a separate Huawei adapter."
[^94]: The Huawei-DeepSeek Symbiosis — "It adds native compilation, scheduling, synchronization and runtime integration for Ascend’s execution model."
[^95]: The Huawei-DeepSeek Symbiosis — "TileLang makes Ascend kernels easier to write, but developers still need to account for the hardware. They choose the calculations, tile sizes and where data is stored. The compiler handles much of the coordination between Cube cores, Vector cores and data transfers."
[^96]: The Huawei-DeepSeek Symbiosis — "TileLang makes Ascend kernels easier to write, but developers still need to account for the hardware."
[^97]: The Huawei-DeepSeek Symbiosis — "They choose the calculations, tile sizes and where data is stored."
[^98]: The Huawei-DeepSeek Symbiosis — "The compiler handles much of the coordination between Cube cores, Vector cores and data transfers."
[^99]: The Huawei-DeepSeek Symbiosis — "Digging below the implementation and looking at its performance against CANN and Triton-ascend, it can match and beat CANN at certain cases; the preferred implementation changes with size. This is a warm-cache simple and naive benchmark."
[^100]: The Huawei-DeepSeek Symbiosis — "Digging below the implementation and looking at its performance against CANN and Triton-ascend, it can match and beat CANN at certain cases; the preferred implementation changes with size."
[^101]: The Huawei-DeepSeek Symbiosis — "This is a warm-cache simple and naive benchmark."
[^102]: The Huawei-DeepSeek Symbiosis — "AutoSchedule uses data dependencies and estimated execution times to plan which operations can overlap. It also chooses how many buffer slots to use within the available on-chip memory, allowing upcoming data to load while the current tile is being processed. Developers can guide these decisions whe…"
[^103]: The Huawei-DeepSeek Symbiosis — "AutoSchedule uses data dependencies and estimated execution times to plan which operations can overlap."
[^104]: The Huawei-DeepSeek Symbiosis — "It also chooses how many buffer slots to use within the available on-chip memory, allowing upcoming data to load while the current tile is being processed."
[^105]: The Huawei-DeepSeek Symbiosis — "Developers can guide these decisions when the default schedule is not suitable."
[^106]: The Huawei-DeepSeek Symbiosis — "On 950PR, AutoSchedule helps especially for smaller sizes, reducing execution time by up to 40% for a single operation."
[^107]: The Huawei-DeepSeek Symbiosis — "The compiler also inserts synchronization so operations wait for the data they need, while removing waits that other dependencies make unnecessary. It checks conditional branches too, so it does not assume an operation has completed when that branch might never execute. This reduces the synchronizat…"
[^108]: The Huawei-DeepSeek Symbiosis — "The compiler also inserts synchronization so operations wait for the data they need, while removing waits that other dependencies make unnecessary."
[^109]: The Huawei-DeepSeek Symbiosis — "It checks conditional branches too, so it does not assume an operation has completed when that branch might never execute."
[^110]: The Huawei-DeepSeek Symbiosis — "This reduces the synchronization work programmers must manage themselves."
[^111]: The Huawei-DeepSeek Symbiosis — "DeepEP Huawei has joined NVIDIA in commercializing large scale-up AI systems, with its Ascend supernodes extending tightly coupled accelerator interconnects across multiple racks from the 910 CloudMatrix384 to the 950 SuperPod,enabling wideEP scale-out. In the 30th September release, Huawei also rel…"
[^112]: The Huawei-DeepSeek Symbiosis — "Huawei has joined NVIDIA in commercializing large scale-up AI systems, with its Ascend supernodes extending tightly coupled accelerator interconnects across multiple racks from the 910 CloudMatrix384 to the 950 SuperPod,enabling wideEP scale-out. In the 30th September release, Huawei also released E…"
[^113]: The Huawei-DeepSeek Symbiosis — "Huawei has joined NVIDIA in commercializing large scale-up AI systems, with its Ascend supernodes extending tightly coupled accelerator interconnects across multiple racks from the 910 CloudMatrix384 to the 950 SuperPod,enabling wideEP scale-out."
[^114]: The Huawei-DeepSeek Symbiosis — "In the 30th September release, Huawei also released EP16 dispatch/combine benchmarks over URMA in the 950DT superpod."
[^115]: The Huawei-DeepSeek Symbiosis — "Huawei’s dispatch is three sequential operators (pre/URMA/post) whereas GB300 is one fused call, and their post work includes receive completion, which our measurement includes, but also includes expansion by expert which GB300’s results don’t."
[^116]: The Huawei-DeepSeek Symbiosis — "DeepEP-Ascend is a port of DeepEP V2.5, with the same python API but calls URMA and HCCL underneath. In July 2025, Huawei’s Ascend team proposed DeepEP-Ascend under deepseek-ai, but a DeepEP maintainer declined. Today, DeepEP-Ascend is distributed under DeepSeek’s own organization."
[^117]: The Huawei-DeepSeek Symbiosis — "DeepEP-Ascend is a port of DeepEP V2.5, with the same python API but calls URMA and HCCL underneath."
[^118]: The Huawei-DeepSeek Symbiosis — "In July 2025, Huawei’s Ascend team proposed DeepEP-Ascend under deepseek-ai, but a DeepEP maintainer declined."
[^119]: The Huawei-DeepSeek Symbiosis — "Today, DeepEP-Ascend is distributed under DeepSeek’s own organization."
[^120]: The Huawei-DeepSeek Symbiosis — "Ascend’s separate Cube and Vector execution paths create opportunities to overlap communication and computation, but do not make that overlap free. Expert computation can also require vector processing and data movement, while communication competes for shared memory bandwidth. Therefore there’s a t…"
[^121]: The Huawei-DeepSeek Symbiosis — "Ascend’s separate Cube and Vector execution paths create opportunities to overlap communication and computation, but do not make that overlap free."
[^122]: The Huawei-DeepSeek Symbiosis — "Expert computation can also require vector processing and data movement, while communication competes for shared memory bandwidth."
[^123]: The Huawei-DeepSeek Symbiosis — "Therefore there’s a tradeoff on how much communication can be hidden without slowing the computation that runs alongside."
[^124]: The Huawei-DeepSeek Symbiosis — "This resource-balancing problem is not unique to DeepSeek. Huawei’s Kimi K3 recipe explicitly restricts vector use to leave capacity for concurrent work, and chooses between dedicated CCU and Vector-based communication according to what must overlap. Faster individual operations are not enough: thei…"
[^125]: The Huawei-DeepSeek Symbiosis — "This resource-balancing problem is not unique to DeepSeek."
[^126]: The Huawei-DeepSeek Symbiosis — "Huawei’s Kimi K3 recipe explicitly restricts vector use to leave capacity for concurrent work, and chooses between dedicated CCU and Vector-based communication according to what must overlap."
[^127]: The Huawei-DeepSeek Symbiosis — "Faster individual operations are not enough: their resource demands must also fit together."
[^128]: The Huawei-DeepSeek Symbiosis — "DeepEP-Ascend’s documentation identifies contention between combine processing and URMA communication for HBM resources, and says Huawei firmware improvements are planned to reduce it."
[^129]: The Huawei-DeepSeek Symbiosis — "This is the practical form of co-design: the model exposes a bottleneck, the implementation adapts, and the platform’s development priorities respond to what remains."
[^130]: The Huawei-DeepSeek Symbiosis — "All planned In May’s unverified DeepSeek investor meeting transcript, Liang Wenfeng said: “So, when it comes to the chip gap between China and the US, I think the software ecosystem gap will eventually disappear. But on the hardware side, we face two separate disadvantages: it takes four Huawei acce…"
[^131]: The Huawei-DeepSeek Symbiosis — "In May’s unverified DeepSeek investor meeting transcript, Liang Wenfeng said: “So, when it comes to the chip gap between China and the US, I think the software ecosystem gap will eventually disappear. But on the hardware side, we face two separate disadvantages: it takes four Huawei accelerator card…"
[^132]: The Huawei-DeepSeek Symbiosis — "In May’s unverified DeepSeek investor meeting transcript, Liang Wenfeng said:"
[^133]: The Huawei-DeepSeek Symbiosis — "“So, when it comes to the chip gap between China and the US, I think the software ecosystem gap will eventually disappear. But on the hardware side, we face two separate disadvantages: it takes four Huawei accelerator cards to match one NVIDIA card, and Huawei is also roughly two years behind in bri…"
[^134]: The Huawei-DeepSeek Symbiosis — "4 months later, the ecosystem gap did indeed narrow. The same transcript mentioned TileLang and helping Huawei get the ecosystem right."
[^135]: The Huawei-DeepSeek Symbiosis — "DSv4.1 Flash Optimizations Another part of the DeepSeek-Huawei symbiosis is that DeepSeek provides Huawei with weights, supporting Day-0 optimized releases, such as DeepSeek V4 and V4.1. Ascend’s accumulator design forces a different approach to attention. The Cube’s L0C buffer cannot rescale accumu…"
[^136]: The Huawei-DeepSeek Symbiosis — "DSv4.1 Flash Optimizations Another part of the DeepSeek-Huawei symbiosis is that DeepSeek provides Huawei with weights, supporting Day-0 optimized releases, such as DeepSeek V4 and V4.1. Ascend’s accumulator design forces a different approach to attention. The Cube’s L0C buffer cannot rescale accumu…"
[^137]: The Huawei-DeepSeek Symbiosis — "Another part of the DeepSeek-Huawei symbiosis is that DeepSeek provides Huawei with weights, supporting Day-0 optimized releases, such as DeepSeek V4 and V4.1."
[^138]: The Huawei-DeepSeek Symbiosis — "Ascend’s accumulator design forces a different approach to attention. The Cube’s L0C buffer cannot rescale accumulated outputs in place, while returning a rescaled output to L0C would require an expensive identity-matrix multiplication. DeepSeek instead keeps the running output accumulator in Vector…"
[^139]: The Huawei-DeepSeek Symbiosis — "Ascend’s accumulator design forces a different approach to attention."
[^140]: The Huawei-DeepSeek Symbiosis — "The Cube’s L0C buffer cannot rescale accumulated outputs in place, while returning a rescaled output to L0C would require an expensive identity-matrix multiplication."
[^141]: The Huawei-DeepSeek Symbiosis — "DeepSeek instead keeps the running output accumulator in Vector UB, transferring partial sums from L0C when needed for rescaling and accumulation."
[^142]: The Huawei-DeepSeek Symbiosis — "Hopper holds its accumulator in registers, while Blackwell provides loads and stores between tensor memory and registers, avoiding this particular restriction"
[^143]: The Huawei-DeepSeek Symbiosis — "Profile Huawei also released a profile of one rank of DeepSeek-V4.1-Flash on a Huawei Ascend 950DT deployment of 32 chips, together with its host threads. In June, we covered a similar profile, that of DeepSeek V4 Pro’s. https://substackcdn.com/image/fetch/$s_!PeCS!,w_140,h_140,c_fill,f_webp,q_auto:…"
[^144]: The Huawei-DeepSeek Symbiosis — "Huawei also released a profile of one rank of DeepSeek-V4.1-Flash on a Huawei Ascend 950DT deployment of 32 chips, together with its host threads. In June, we covered a similar profile, that of DeepSeek V4 Pro’s."
[^145]: The Huawei-DeepSeek Symbiosis — "Huawei also released a profile of one rank of DeepSeek-V4.1-Flash on a Huawei Ascend 950DT deployment of 32 chips, together with its host threads."
[^146]: The Huawei-DeepSeek Symbiosis — "In June, we covered a similar profile, that of DeepSeek V4 Pro’s."
[^147]: The Huawei-DeepSeek Symbiosis — "Many components are similar, like the use of AICPU and separation of some layers to different streams."
[^148]: The Huawei-DeepSeek Symbiosis — "The execution order is 40 target-model layers, the target LM head, 3 DSpark drafter blocks, the draft LM head, and 5 sampling rounds. The main compute runs on Stream 19; the drafter’s run on Stream 173. The V2 MC² kernels that fused computation and communication from the DSv4 Pro trace shows up agai…"
[^149]: The Huawei-DeepSeek Symbiosis — "The execution order is 40 target-model layers, the target LM head, 3 DSpark drafter blocks, the draft LM head, and 5 sampling rounds."
[^150]: The Huawei-DeepSeek Symbiosis — "The main compute runs on Stream 19; the drafter’s run on Stream 173. The V2 MC² kernels that fused computation and communication from the DSv4 Pro trace shows up again, as V3 this time."
[^151]: The Huawei-DeepSeek Symbiosis — "This is why only 4 AI CPU-launched HCCL operations appear per step, against 43 expert dispatches."
[^152]: The Huawei-DeepSeek Symbiosis — "These are the target and draft vocabulary heads’ hcom_allGather and hcom_alltoallv: gather hidden states, run the LM-head GEMM, then exchange logits."
[^153]: The Huawei-DeepSeek Symbiosis — "The drafter blocks run once to produce base logits for the draft positions. The subsequent Markov head models token dependencies through sampling and embedding feedback. It does not rerun the transformer blocks for each proposal. The end of each step changes from MoE and attention to a serial chain …"
[^154]: The Huawei-DeepSeek Symbiosis — "The drafter blocks run once to produce base logits for the draft positions."
[^155]: The Huawei-DeepSeek Symbiosis — "The subsequent Markov head models token dependencies through sampling and embedding feedback."
[^156]: The Huawei-DeepSeek Symbiosis — "It does not rerun the transformer blocks for each proposal."
[^157]: The Huawei-DeepSeek Symbiosis — "The end of each step changes from MoE and attention to a serial chain of small projections and sampling operations."
[^158]: The Huawei-DeepSeek Symbiosis — "As mentioned and explained in previous articles, speculative decoding is a lossless method to predict draft tokens and use a single pass to verify them, amortizing weight loading. In the decode step diagram above, we can see how much faster DSpark token drafting is compared to the verification step.…"
[^159]: The Huawei-DeepSeek Symbiosis — "As mentioned and explained in previous articles, speculative decoding is a lossless method to predict draft tokens and use a single pass to verify them, amortizing weight loading."
[^160]: The Huawei-DeepSeek Symbiosis — "In the decode step diagram above, we can see how much faster DSpark token drafting is compared to the verification step."
[^161]: The Huawei-DeepSeek Symbiosis — "DSv4.1 Flash is also the first DeepSeek model to use Engram, but after Qwen and Meituan Longcat. https://substackcdn.com/image/fetch/$s_!LKos!,w_140,h_140,c_fill,f_webp,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32927bec-0019-418f-9…"
[^162]: The Huawei-DeepSeek Symbiosis — "DSv4.1 Flash is also the first DeepSeek model to use Engram, but after Qwen and Meituan Longcat."
[^163]: The Huawei-DeepSeek Symbiosis — "Because Engram takes token IDs as input, the fetch can be done async and overlapped with layer 0’s compute."
[^164]: The Huawei-DeepSeek Symbiosis — "This allows offloading to DRAM without performance loss vis-a-vis HBM, but offloading to a PCIe 4.0 SSD degrades performance."
[^165]: The Huawei-DeepSeek Symbiosis — "Summarizing kernel durations in the steady-state window, Stream 19 is occupied for 88.8% of the window but contributes 72.6% of summed device time because other streams overlap it. In the middle, the substantial MIX_AIV and AI_VECTOR_CORE bands contain dispatch/combine as well as quantization. Ascen…"
[^166]: The Huawei-DeepSeek Symbiosis — "Summarizing kernel durations in the steady-state window, Stream 19 is occupied for 88.8% of the window but contributes 72.6% of summed device time because other streams overlap it."
[^167]: The Huawei-DeepSeek Symbiosis — "In the middle, the substantial MIX_AIV and AI_VECTOR_CORE bands contain dispatch/combine as well as quantization."
[^168]: The Huawei-DeepSeek Symbiosis — "Ascend exposes separately scheduled cube and vector paths through MIX_AIC, MIX_AIV, AI_CORE, and AI_VECTOR_CORE."
[^169]: The Huawei-DeepSeek Symbiosis — "Each event has a task type, so the duration accounting is a partition."
[^170]: The Huawei-DeepSeek Symbiosis — "Mixed types still involve work beyond a single physical unit; their names do not turn elapsed kernel duration into measured cube-only or vector-only utilization."
[^171]: The Huawei-DeepSeek Symbiosis — "A first-order scenario doubling cube throughput while leaving other device work unchanged gives a 1.32× step improvement. It holds measured stream overlap constant and leaves idle unchanged. This is a composition scenario, not a prediction for new silicon: mixed task types are not exclusive utilizat…"
[^172]: The Huawei-DeepSeek Symbiosis — "A first-order scenario doubling cube throughput while leaving other device work unchanged gives a 1.32× step improvement."
[^173]: The Huawei-DeepSeek Symbiosis — "It holds measured stream overlap constant and leaves idle unchanged."
[^174]: The Huawei-DeepSeek Symbiosis — "This is a composition scenario, not a prediction for new silicon: mixed task types are not exclusive utilization measurements, and bandwidth, dependencies, and scheduling can change the result."
[^175]: The Huawei-DeepSeek Symbiosis — "Quantization fusion likewise remains an opportunity, its attraction is the repeated producer-to-consumer boundary and its large share of the vector bucket that also carries fused communication."
[^176]: The Huawei-DeepSeek Symbiosis — "Ecosystem gaps One issue however is the partnership could work extremely well for DeepSeek without making Ascend equally usable for everyone else. For DeepSeek, building compilers, maintaining kernels and debugging vendor-specific behavior competes with model research and product development, albeit…"
[^177]: The Huawei-DeepSeek Symbiosis — "One issue however is the partnership could work extremely well for DeepSeek without making Ascend equally usable for everyone else. For DeepSeek, building compilers, maintaining kernels and debugging vendor-specific behavior competes with model research and product development, albeit temporarily."
[^178]: The Huawei-DeepSeek Symbiosis — "One issue however is the partnership could work extremely well for DeepSeek without making Ascend equally usable for everyone else."
[^179]: The Huawei-DeepSeek Symbiosis — "For DeepSeek, building compilers, maintaining kernels and debugging vendor-specific behavior competes with model research and product development, albeit temporarily."
[^180]: The Huawei-DeepSeek Symbiosis — "For everyone else, there may be issues when hardware configurations doesn’t align with DeepSeek’s. Most optimizations were on supernodes, and as of vLLM-Ascend_0.26.0rc1 many issues exist working with Ascend on x86 hosts: No DeepGEMM support on x86 hosts Dependency on memfabric_hybrid containing har…"
[^181]: The Huawei-DeepSeek Symbiosis — "For everyone else, there may be issues when hardware configurations doesn’t align with DeepSeek’s."
[^182]: The Huawei-DeepSeek Symbiosis — "Most optimizations were on supernodes, and as of vLLM-Ascend_0.26.0rc1 many issues exist working with Ascend on x86 hosts:"
[^183]: The Huawei-DeepSeek Symbiosis — "No DeepGEMM support on x86 hosts"
[^184]: The Huawei-DeepSeek Symbiosis — "Dependency on memfabric_hybrid containing hardcoded ARM headers for vLLM-Ascend, blocking startup; vLLM-Ascend doesn’t work out of the box."
[^185]: The Huawei-DeepSeek Symbiosis — "CPU-binding skipped for non-ARM CPUs on vLLM-Ascend"
[^186]: The Huawei-DeepSeek Symbiosis — "No NPU + x86 CI, patches needed for some recipes"
