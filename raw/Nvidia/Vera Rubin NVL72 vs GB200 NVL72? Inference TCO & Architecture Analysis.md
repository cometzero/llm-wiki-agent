---
title: "Vera Rubin NVL72 vs GB200 NVL72? Inference TCO & Architecture Analysis"
origin: lilys_ai
lilys_project_id: 10666463
lilys_project_url: "https://lilys.ai/digest/10666463"
lilys_created_at: "2026-07-23T09:45:00.322Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "12495078"
sources:
  - id: "11471830"
    url: "https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference"
    title: "Vera Rubin NVL72 vs GB200 NVL72? Inference TCO & Architecture Analysis"
    status: "done"
---

# Vera Rubin NVL72 vs GB200 NVL72? Inference TCO & Architecture Analysis

## LilysAI note

> Vera Rubin NVL72와 GB200 NVL72의 추론 성능 및 아키텍처 분석 결과는? **Vera Rubin NVL72**는 GB200 NVL72 대비 **전력 효율(MW당 성능)과 총 소유 비용(TCO당 성능) 면에서 훨씬 뛰어난 성능**을 보여주며, 특히 높은 상호작용성(interactivity)을 요구하는 워크로드에서 압도적인 우위를 점합니다.

## 1. Vera Rubin NVL72와 GB200 NVL72의 추론 성능 및 아키텍처 분석
Vera Rubin NVL72는 Nvidia의 2세대 랙 스케일 Oberon 아키텍처로, 극단적인 공동 설계를 통해 추론 성능을 크게 향상시켰다.

### 1.1. Vera Rubin NVL72의 초기 성능 및 소프트웨어 지원
1. **초기 성능 결과**
    1. Vera Rubin NVL72는 DeepSeek R1 실행 시 GB200 NVL72 대비 MW당 성능 5.4배, 달러당 성능 5배를 달성했다.
    2. 이 격차는 2025년 GB200 NVL72의 초기 가동 시점과 비교하면 더욱 커진다.
    3. Vera Rubin은 아직 초기 가동 단계이므로, 소프트웨어 성숙에 따라 성능 격차가 더욱 확대될 것으로 예상된다.
2. **소프트웨어 스택 및 커널 재사용**
    1. Nvidia는 CUDA 13.4와 함께 Rubin(SM_107) 소프트웨어 스택의 첫 공개 버전을 출시했다.
    2. PyTorch, vLLM, OpenAI Triton 컴파일러에 Rubin PR이 업스트림되었다.
    3. Blackwell은 Hopper WGMMA 커널을 재사용할 수 없었지만, Rubin은 Blackwell 커널을 재사용할 수 있어 소프트웨어 가동 프로세스가 훨씬 원활하다.
    4. 최고 성능(SOL)을 위해서는 엔지니어가 커널을 튜닝하고 다시 작성해야 하지만, 출시 시간을 중시하는 경우 Blackwell 커널을 재사용할 수 있다.
3. **Feynman 아키텍처와의 전환**
    1. Nvidia는 GitHub를 통해 Feynman이 SM_140임을 공개했다.
    2. Blackwell에서 Rubin으로의 전환과 달리, Rubin에서 Feynman으로의 전환은 커널 측면에서 훨씬 더 복잡할 것으로 예상된다.
<img alt="Vera Rubin – Extreme Co-Design: An Evolution from Grace Blackwell Oberon" src="https://substackcdn.com/image/fetch/$s_!NB4l!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7257cc0c-a57b-4aa2-b03b-1ead3d930e8c_4800x2700.png">
<figcaption>Vera Rubin – 극단적인 공동 설계: Grace Blackwell Oberon의 진화</figcaption>

### 1.2. 성능 측정 및 분석 방법
1. **초기 측정 데이터 출처 및 검증**
    1. VR NVL72에 대한 초기 측정 지표는 CoreWeave에서 수집되었다.
    2. SemiAnalysis는 이 데이터를 독립적으로 검증하지 않았다.
    3. Nvidia는 2026년 3분기까지 InferenceX에 검증 가능한 수치를 제출할 예정이다.
    4. Google은 몇 달 내로 TPUv7 결과를 제출할 예정이며, AMD는 MI455X UALoE72를 제출할 예정이다.
2. **분석 범위**
    1. 이 글에서는 Nvidia의 Rubin 주장을 여러 기준선과 비교하여 Rubin이 Blackwell보다 명확하게 우위에 있는 부분과 격차가 좁은 부분을 분석한다.
    2. Rubin의 총 소유 비용(TCO) 추정치를 사용하여 TCO당 성능을 분석한다.
    3. TCO는 자본 지출, 운영 지출 및 기타 비용을 고려하는 AI TCO 모델에서 가져온다.
    4. 데이터센터 모델의 전력 추정치를 사용하여 와트당 성능도 고려한다.
3. **VR NVL72의 BOM(Bill of Materials) 분석**
    1. VR NVL72의 구성 요소별 BOM 분석은 SemiAnalysis BOM 모델에서 제공될 예정이다.
4. **생산 가속화**
    1. Rubin Oberon NVL72는 Blackwell Oberon NVL72보다 훨씬 빠른 생산 가동 기간을 가질 것으로 예상된다.
    2. 이는 Rubin의 더 간단한 케이블 없는 컴퓨팅 트레이 설계와 Blackwell의 구리 백플레인 문제 해결 경험 덕분이다.
    3. SemiAnalysis의 Accelerator Model은 Rubin의 분기별 패키지 및 랙 수준 출하량을 추적한다.

## 2. Rubin 칩 수준 마이크로아키텍처 기능 분석
Rubin 마이크로아키텍처의 완전한 분석은 Rubin 시스템에 대한 SSH 접근 권한을 얻어 Blackwell 분석과 유사한 벤치마크를 실행할 수 있을 때까지 기다려야 한다.  그러나 몇 가지 흥미로운 점을 언급할 수 있다.

### 2.1. Rubin의 원활한 전환 및 커널 재사용
1. **Hopper에서 Blackwell로의 전환과 비교**
    1. Rubin의 가동은 Hopper에서 Blackwell로의 전환보다 훨씬 원활할 것으로 예상된다.
    2. Hopper에서 Blackwell로 전환할 때는 엔지니어들이 커널을 포팅하는 데 많은 노력을 기울여야 했다.
    3. Rubin은 DeepGEMM, FlashMLA, CUTLASS 등 모든 중요한 커널 라이브러리에서 Blackwell SM100-패밀리 커널을 실행할 수 있어 이러한 단순성이 가능하다.
    4. Hopper에서 Blackwell로 이동하는 것은 커널을 처음부터 다시 작성하는 것을 의미했으며, Hopper의 커널은 Blackwell에서 전혀 실행되지 않는다.
2. **시장 출시 시간 이점 및 커널 튜닝**
    1. Blackwell SM100 커널을 재사용하는 것은 시장 출시 시간 측면에서 명확한 이점을 제공한다.
    2. 최고 성능(SOL)을 위해서는 엔지니어가 Rubin 아키텍처에 특화된 커널을 튜닝하고 다시 작성해야 하지만, 커널 재사용은 이러한 튜닝에 집중할 시간을 벌어준다.

### 2.2. Rubin의 아키텍처 세부 사항 개선
1. **SMEM 및 TMEM 용량 증가**
    1. Rubin의 SMEM은 Blackwell의 228KiB에서 328KiB로 증가했다.
    2. 기본 SMEM 용량은 228KiB이지만, Rubin은 328KiB까지 증가할 수 있는 오버사이즈 공유 메모리 모드를 제공한다.
    3. TMEM은 Blackwell의 288KiB에서 256KiB로 증가했으며, 열 수가 512개에서 576개로 늘어났다.
    4. 추가된 열은 블록 스케일 팩터를 저장하고, 누산기용 TMEM 영역과 분리하여 블록 스케일 커널 로직을 크게 단순화한다.
2. **인라인 TMA 디스크립터 업데이트**
    1. Rubin의 TMA는 이제 인라인 디스크립터 업데이트를 지원한다.
    2. 이는 MoE(Mixture-of-Experts) 레이어와 같은 다양한 사용 사례에 유용하다.
    3. Blackwell에서는 각 전문가 전환 시 TMA 디스크립터를 메모리에 다시 작성하고 동기화해야 했다.
    4. Rubin에서는 전문가별 오프셋이 TMA 명령어에 인라인으로 전달되어 하나의 디스크립터가 모든 전문가를 커버하며, 메모리 내 재작성이 필요 없다.
    5. 이는 토큰 디스패치 중 오버헤드를 제거하고 낮은 배치 크기에서 디코딩 속도를 향상시킨다.
3. **ISA 기능 .override 한정자**
    1. 인라인 TMA 디스크립터 업데이트는 ISA 기능인 `.override` 한정자에 해당한다.
    2. TMA 명령어는 레이아웃 및 형식 메타데이터를 지정하는 `tensorMap` 객체를 필요로 한다.
    3. `.override` 한정자를 사용하면 대량 비동기 복사 명령어가 `tensorMap` 객체를 템플릿으로 재사용하면서 스트라이드와 같은 특정 메타데이터 필드를 대체할 수 있다.
    4. MoE의 경우, 전문가 가중치는 동일한 모양, 데이터 유형 및 속성을 가지므로, 전역 주소를 재정의하여 커널 작성자는 다른 전문가를 로드할 때 `tensorMap` 객체를 중복하거나 교체할 필요가 없다.
4. **BF16/FP16 지수 처리량 및 FP32 처리량**
    1. Rubin은 BF16/FP16 지수 처리량을 SM당 클럭당 두 배로 늘려, 어텐션 중 Tensor Core 작업과 소프트맥스 오버랩을 돕는다.
    2. FP32 처리량은 Blackwell Ultra와 동일하다.
5. **Tensor Core의 블록 스케일 팩터 형식 확장**
    1. Blackwell NVFP4/MXFP4 Tensor Core는 UE4M3/UE8M0 블록 스케일 팩터 형식만 허용했지만, Rubin Tensor Core는 이제 UE5M3 8비트 블록 스케일 팩터도 허용한다.
    2. 이 추가 블록 스케일 형식은 더 넓은 범위로 인해 특정 경우에 더 많은 유연성과 더 적은 양자화 오류를 허용한다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!eSOM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e1122cc-b6a4-4d16-868f-5eb30f436322_1476x602.png">
<figcaption>출처: NVIDIA PTX</figcaption>

### 2.3. NVLink 통신 및 Tensor Core 개선
1. **SM 구동 NVLink 통신 지연 시간 개선**
    1. Rubin은 카운트된 쓰기를 사용하여 SM 구동 NVLink 통신 지연 시간을 개선했다.
    2. 이는 구리 백플레인을 통해 GPU 간에 데이터를 전송하는 데 필요한 메시지 수를 줄여준다.
    3. Blackwell NVLink 지연 시간은 TPU 및 Trainium보다 몇 배 더 높았기 때문에 이는 매우 중요한 개선 사항이다.
2. **FP8 및 FP4 처리량 두 배 증가**
    1. Rubin의 Tensor Core는 Blackwell에 비해 FP8 및 FP4 처리량을 두 배로 제공한다.
    2. 이는 k 차원을 두 배로 늘린 것이 주요 원인이며, 이론적으로 GEMM 실행에 필요한 클럭 사이클 수가 절반으로 줄어든다.
    3. Blackwell Ultra의 K=96/3xFP4 명령어는 여전히 존재하지만, 새로운 K=128 변형도 추가되었다.

### 2.4. 세분화된 오버랩 및 메모리 대역폭 향상
1. **세분화된 오버랩 기능**
    1. Blackwell의 PDL은 그리드 수준에서 오버랩을 허용하여, 종속 그리드가 이전 커널의 모든 스레드 블록이 완료될 때까지 기다려야 시작할 수 있었다.
    2. 이는 커널 간의 램프 다운 및 램프 업 시간을 일부 숨길 수 있었지만, 최신 메가커널 작성자들이 추구하는 매우 세분화된 오버랩에는 미치지 못했다.
    3. Rubin에서는 종속 커널이 이전 커널과 스레드 블록 수준에서 동기화할 수 있도록 하여 더 세분화된 오버랩이 가능하다.
2. **글로벌 메모리 대역폭 증가**
    1. Rubin은 3D 스택 HBM4 메모리를 사용하여 Blackwell Ultra보다 2.8배 높은 글로벌 메모리 대역폭을 제공한다.
    2. Rubin이 메모리 시스템 지연 시간 측면에서 Blackwell보다 개선될 가능성은 낮다.
    3. SemiAnalysis의 Accelerator & HBM Model은 Rubin에 사용된 메모리 용량 추정치 및 공급업체에 대한 완전한 분석을 제공한다.

### 2.5. 활성화에 대한 2:4 희소성 지원
1. **2:4 희소성 작동 방식**
    1. Rubin은 활성화에 대한 2:4 희소성 지원을 추가한다.
    2. 4개의 값 그룹마다 2개는 유지되고 2개는 0으로 처리된다.
    3. 패턴이 규칙적이므로 Tensor Core는 유지되는 슬롯을 알고 나머지를 건너뛰며, MMA를 두 배 빠른 속도로 실행한다.
    4. 작은 메타데이터 필드가 유지된 슬롯을 추적한다.
2. **Ampere의 2:4 희소성과의 차이점**
    1. Nvidia는 Ampere에서 가중치에 2:4 희소성을 적용했지만, 모델 가지치기 및 재훈련이 필요했기 때문에 아무도 사용하지 않았다.
    2. Rubin은 런타임에 활성화에 적용하므로 재훈련이 필요 없다.
3. **어텐션 및 MLP 활성화에 적용**
    1. 어텐션에서 QK^T는 밀집하게 실행된 다음, 점수는 Tensor Memory에서 나올 때 압축된다.
    2. 소프트맥스는 유지된 값만 처리하고, V에 대한 다음 GEMM은 희소하게 실행된다.
    3. 출력은 밀집 상태로 유지되므로 모델의 다른 부분은 변경되지 않는다.
    4. 이는 MLP 활성화에도 적용된다.
4. **정확도 데이터 및 현재 사용 현황**
    1. Nvidia는 정확도 데이터를 공개하지 않았으며, 소프트맥스 전에 어텐션 점수의 절반을 버리는 것이 항상 이득이 되는 것은 아니다.
    2. CoreWeave의 DeepSeek R1 결과도 이를 사용하지 않는 것으로 보이며, 이는 Rubin의 또 다른 기능이지만 아직 튜닝된 커널이 없는 상태이다.

## 3. Rubin SM107 Tensor Core의 룩업 테이블 가중치 압축 해제
Rubin은 룩업 테이블에서 가중치 피연산자를 압축 해제하는 Tensor Core MMA 모드인 LUT B를 추가한다.

### 3.1. LUT B 작동 방식
1. **B 피연산자 압축**
    1. 이 모드에서 B 피연산자는 인덱스의 압축된 행렬이다.
    2. 표준 추론 GEMM에서 B 피연산자는 가중치를 보유한다.
    3. 가중치 값은 Tensor Memory의 룩업 테이블에 저장된다.
    4. Tensor Core는 각 인덱스를 읽고 MMA 내부에서 가중치 값을 재구성한다.
    5. 별도의 역양자화 과정은 없다.
    6. 룩업 후 곱셈은 FP8로 실행된다.
2. **3비트 인덱스 및 룩업 테이블**
    1. LUT B에서 각 가중치 위치는 완전한 숫자 값 대신 3비트 인덱스를 저장한다.
    2. 이 인덱스는 해당 가중치의 8x64 블록이 공유하는 룩업 테이블에서 8개의 E4M3 값 중 하나를 선택한다.
    3. 예를 들어, 저장된 인덱스가 5이면 Tensor Core는 해당 블록의 룩업 테이블에서 5번 항목을 가중치로 사용한다.
    4. 룩업은 MMA 내부에서 발생하므로 커널은 별도의 압축 해제된 가중치 행렬을 구성할 필요가 없다.

### 3.2. 룩업 테이블의 유연성 및 정확도
1. **비균일 간격 및 비대칭 코드북**
    1. 룩업 테이블(LUT)은 기존의 균일하거나 부동 소수점 그리드의 간격을 따를 필요가 없다.
    2. 따라서 양자화 알고리즘은 밀집된 가중치 클러스터 주변에 더 많은 값을 배치하거나, 긴 꼬리에 대해 불균일한 간격을 사용하거나, 양수 및 음수 가중치가 다른 분포를 가질 때 비대칭 코드북을 선택할 수 있다.
2. **비트당 정확도 향상 가능성**
    1. 이러한 유연성은 저장된 비트당 더 나은 정확도를 가능하게 한다.
    2. Rubin LUT B는 FP4보다 개별 코드가 적지만, 특정 가중치 그룹에 필요한 위치에 코드를 배치할 수 있다.
    3. 그러나 MXFP4 또는 NVFP4보다 자동으로 더 정확한 것은 아니다.
    4. 하나의 코드북이 512개의 가중치에 걸쳐 공유되는 반면, NVFP4는 16개의 훨씬 작은 그룹에 걸쳐 스케일을 조정한다.
    5. 결과는 코드북 피팅 알고리즘, 보정 데이터, 양자화 인식 훈련 및 민감한 레이어가 더 높은 정밀도를 유지하는지 여부에 따라 달라진다.

### 3.3. 비트당 가중치 및 메모리 절약
1. **비트당 가중치 계산**
    1. 각 인덱스는 3비트이고 룩업 테이블은 8개의 항목을 가진다.
    2. 각 항목은 1바이트이며, 참조 커널에서는 E4M3 8비트 부동 소수점이다.
    3. 이는 가중치당 3.125비트(인덱스 3비트 + 512개 가중치에 걸쳐 분산된 코드북 64비트)를 초래한다.
    4. 코드북은 인덱스와 함께 HBM에 저장되므로, 가중치당 3.125비트가 전체 저장 공간이다.
2. **가중치 정지 패턴 및 제한 사항**
    1. 명령어는 압축된 가중치를 컬렉터 버퍼로 로드한다.
    2. Tensor Core는 이를 유지하고 활성화 타일 실행 전반에 걸쳐 재사용할 수 있다.
    3. 이는 가중치 정지 패턴이다.
    4. 이 모드는 B 행렬의 전치를 지원하지 않는다는 제한도 있다.

### 3.4. LUT B와 다른 압축 방식 비교
1. **블록 스케일 형식과의 차이점**
    1. 블록 스케일 형식인 NVFP4 및 MXFP도 MMA 내부에서 압축 해제를 수행한다.
    2. 그러나 이들은 코드북이 아닌 블록당 하나의 균일한 스케일을 적용한다.
2. **AWQ와의 차이점**
    1. AWQ와 같은 소프트웨어 방식은 행렬 곱셈 전에 별도의 역양자화 단계를 실행하여 낮은 비트 수를 달성한다.
    2. Rubin은 MMA 내부에서 비균일 코드북을 재구성하는 최초의 NVIDIA Tensor Core 입력 형식이다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!eWMD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff60b0243-309e-4ed7-a03d-0977dc045cb9_2856x782.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 3.5. HBM 용량 및 디코딩 처리량에 미치는 영향
1. **HBM 용량 절감**
    1. 낮은 비트 전송률은 가중치에 필요한 HBM 용량을 줄인다.
    2. 또한 GPU가 각 가중치에 대해 읽는 바이트 수를 줄인다.
2. **디코딩 처리량 향상**
    1. 낮은 배치 크기에서는 가중치 대역폭이 디코딩 단계를 제한한다.
    2. 가중치당 바이트 수가 적으면 디코딩 처리량이 증가한다.
3. **정확도 유지 및 전력 효율성**
    1. 비균일 코드북은 동일한 비트 수에서 균일한 반올림보다 정확도를 더 잘 유지한다.
    2. 이 기능은 플롭당 메모리 시스템을 통해 이동해야 하는 비트 수가 적기 때문에 전력 효율성에도 영향을 미칠 것으로 예상된다.

### 3.6. Kimi K3 2.8T 모델 예시를 통한 HBM 용량 비교
1. **MXFP4 형식의 HBM 용량**
    1. Kimi K3 2.8T를 예로 들면, 가중치당 약 4.5비트에서 MXFP4는 약 1,487.5GB(1.4875TB)를 저장한다.
2. **Rubin 룩업 테이블 형식의 HBM 용량**
    1. 가중치당 3.125비트에서 Rubin 룩업 테이블 형식은 약 1,094GB(1.09TB)를 저장한다.
3. **용량 차이**
    1. 두 형식 간의 차이는 약 393.5GB이다.
4. **저장 공간 범위**
    1. 이 수치는 원시 가중치 페이로드만 포함하며, KV 캐시, 활성화 및 병렬 복제는 제외한다.
5. **Rubin 패키지 필요 수**
    1. Rubin 패키지당 288GB의 HBM4를 기준으로, 가중치만으로 NVFP4에서는 약 6개의 패키지가 필요하고, 새로운 Rubin 형식에서는 약 4개의 패키지가 필요하다.

## 4. Feynman 아키텍처 미리보기
Blackwell(SM100)/Blackwell Ultra에서 Rubin(SM107)으로의 도약은 마이크로아키텍처 측면에서 상대적으로 작으므로, Rubin은 Blackwell의 개선 아키텍처로 볼 수 있다.  반면, Feynman(sm_140)은 완전히 새로운 아키텍처 패밀리이다.

### 4.1. Feynman으로의 전환 복잡성
1. **커널 재작성 필요성**
    1. 이는 Rubin에서 Feynman으로 많은 커널을 다시 작성해야 함을 의미하며, Hopper WGMMA에서 Blackwell tcgen05로 전환할 때와 유사하다.
    2. SemiAnalysis의 Accelerator & HBM Model은 Feynman의 분기별 볼륨 추정치에 대한 완전한 분석을 제공한다.
2. **3D 스태킹 기술**
    1. Feynman의 3D 스태킹은 AMD가 MI300X와 CDNA3에서 3D 스태킹을 해온 것과 유사할 것이다.

### 4.2. Feynman의 새로운 기능: 희소성 인식 데이터 이동 연산
1. **희소성 인식 데이터 이동 연산**
    1. Feynman 아키텍처의 새로운 기능 중 하나는 희소성 인식 데이터 이동 연산을 포함한다는 것이다.
    2. 이는 희소 GEMM에서 불필요한 로드, 저장 및 FMA를 피함으로써 성능을 향상시키는 데 사용될 수 있다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!SOmE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a0880df-bf99-4b05-b28e-a82003b23ea1_1698x782.png">

## 5. CoreWeave VR NVL72 결과의 미묘한 차이
CoreWeave는 Vera Rubin NVL72 추론 결과를 전력 사용량(MW)당 성능(초당 토큰) 단위로 게시했다.  SemiAnalysis는 이 데이터의 미묘한 차이를 분석하고, 2026년 7월 InferenceX 결과를 기준선으로 사용하여 Blackwell의 성능과 비교한다.

### 5.1. CoreWeave-Nvidia 차트의 주요 주장 및 측정 방식
1. **주요 주장**
    1. CoreWeave-Nvidia 차트의 첫 번째 주목할 만한 주장은 VR NVL72가 약 150 tok/s/user의 동일한 상호작용성에서 GB200 NVL72보다 메가와트당 토큰 처리량이 10배 더 우수하다는 것이다.
    2. 이는 오늘날 최신 모델의 "고속 모드"보다 약 50% 빠르다.
2. **차트의 세 가지 특징**
    1. 벤치마크는 단일 턴, 8k 입력 및 1k 출력이다.
    2. Y축은 총 처리량이 아닌 메가와트당 출력 토큰 처리량이다.
    3. 전력 수치는 출력 토큰만 계산되었음에도 불구하고 프리필 및 디코딩 GPU를 모두 포함한다.
    4. InferenceX는 디코딩 GPU 와트만 기준으로 출력 처리량을 측정하므로, 비교를 위해 데이터를 CoreWeave의 방식에 맞게 재정규화했다.

### 5.2. CoreWeave의 추론 최적화
1. **적용된 최적화**
    1. CoreWeave는 기준선 GB200 NVL72 및 Rubin NVL72 성능 결과 모두에 다음 추론 최적화를 적용했다고 주장한다.
    2. NVFP4 정밀도
    3. 추측 디코딩(MTP 사용)
    4. 분산 서빙(Dynamo 사용)
    5. 광범위한 전문가 병렬 처리
    6. TensorRT-LLM을 통해
2. **초기 성능 이점**
    1. 위 결과는 Rubin이 Blackwell에 비해 강력한 성능 향상을 가지고 시장에 출시됨을 시사한다.

### 5.3. CoreWeave 결과의 미묘한 차이점
1. **기준선 비교 시점**
    1. CoreWeave는 Rubin을 2025년 GB200 NVL72 기준선과 비교하고 있다.
    2. GB200 NVL72 수명 주기의 초기 단계 성능과 비교하는 것은 Rubin 성능도 초기 단계에서 크게 향상될 것으로 예상되므로 어느 정도 공정하다.
    3. SemiAnalysis는 2025년 GB200 NVL72 초기 성능 결과와 2026년 GB200 NVL72 성능, 그리고 현재 비교할 만한 GPU인 GB300 NVL72를 모두 사용한다.
    4. 2026년 초 GB300 NVL72 성능과 Rubin의 유사한 초기 수명 주기 성능을 직접 비교할 것이다.
2. **사용된 모델의 선택**
    1. CoreWeave는 현재 널리 사용되지 않는 DeepSeek R1 671B 모델을 사용했다.
    2. GLM5.2, Kimi K2.5, Qwen3.5 또는 DeepSeek V4와 같은 최신 모델을 사용했으면 더 좋았을 것이다.
    3. Kimi K3 또는 Qwen3.8과 같은 곧 출시될 모델은 InferenceX에서 더 나은 비교를 제공할 것이다.
    4. AMD가 MI455X UALoE72 성능 측정에 2026년 여름에 GPTOSS 120B를 사용하는 것보다는 낫다.
    5. Nvidia가 2026년 3분기에 InferenceX를 통해 더 현대적인 모델 아키텍처로 Rubin을 벤치마킹하면 이러한 불확실성이 해소될 것으로 예상된다.
3. **DeepSeek R1 671B 모델 선택의 영향**
    1. CoreWeave가 DeepSeek R1 671B를 선택한 것은 이론적으로 Rubin이 아닌 Blackwell 기준선에 더 유리하다.
    2. Rubin의 주요 장점은 더 높은 HBM 용량, 더 높은 CPU DRAM 용량 및 더 큰 HBM 대역폭에 있다.
    3. 이는 Rubin이 Fable 5, Gemini Pro, Kimi K3 및 Qwen3.8 2.4T와 같은 수조 개의 매개변수 모델에 더 최적화되어 있음을 의미한다.
4. **단일 턴 벤치마크의 한계**
    1. CoreWeave는 단일 턴 8k/1k 입력/출력 토큰만 사용했다.
    2. 이론적으로 Agentic Coding과 같은 다중 턴 장문 컨텍스트 워크로드는 Rubin의 더 높은 HBM 용량과 대역폭 덕분에 더 잘 수행될 수 있지만, 이는 간단한 단일 턴 벤치마크에서는 포착되지 않는다.
    3. Weka, LMCache, vLLM/SGLang 커뮤니티, Nvidia, AMD 등과 협력하여 개발 중인 AgentX 벤치마크 시나리오는 현실적인 에이전트 워크로드를 제공하여 추론 성능을 벤치마킹할 것이다.
5. **사전 생산 랙에서의 테스트**
    1. CoreWeave의 테스트는 스케일 아웃 패브릭이 없는 사전 생산 랙(Dell 엔지니어링 샘플 랙)에서 수행되었다.
    2. 이러한 결과는 NVL72 스케일 업 백플레인을 사용하는 광범위한 EP 및 PD 분리를 사용하고 잘 작동함을 증명하므로 가치가 있다.
    3. 이 백플레인은 GB200 NVL72 Oberon의 가동 중에 많은 신뢰성 문제에 직면했다.

## 6. Rubin 대 Blackwell 메가와트당 성능
Nvidia가 제시한 주요 지표는 "시스템의 모든 GPU를 포함한 총 유틸리티 메가와트당 출력 토큰 수"였다.  동일한 기준으로 비교하기 위해 SemiAnalysis는 InferenceX 벤치마크 데이터를 동일한 총 GPU 기준으로 재정규화했다.

### 6.1. VR NVL72와 GB200 및 GB300 벤치마크 비교
1. **비교 기준선**
    1. VR NVL72를 SemiAnalysis의 공식 GB200 및 GB300 2026년 7월 벤치마크와 CoreWeave의 2025년 GB200 기준선과 비교한다.
2. **Nvidia 차트의 배수**
    1. Nvidia 차트의 눈에 띄는 배수는 모두 2025년 기준선에서 비롯된다.
    2. 벤치마크 데이터를 비교할 때는 동일한 기간의 수치를 사용하는 것이 더 유용하므로, 2026년 7월 GB200 및 GB300 벤치마크가 더 적절한 비교 대상이다.

### 6.2. 데이터센터 PUE 및 파레토 곡선
1. **데이터센터 PUE**
    1. Vera Rubin은 칠러 없이 맞춤형 데이터센터에서 45도 섭씨 냉각수 온도로 작동할 수 있으므로 데이터센터 PUE가 더 낮을 수 있다.
    2. 그러나 대부분의 데이터센터는 다양한 시스템을 수용하도록 설계되었으므로, 비교를 위해 DLC 냉각 칩에 동일한 PUE를 사용한다.
2. **파레토 곡선**
    1. 다음 파레토 곡선은 총 GPU 메가와트당 출력 처리량을 상호작용성과 비교하여 나타낸다.
    2. 각 선은 해당 레시피의 한계가 끝나는 지점에서 멈춘다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!FNvZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ee917ba-0028-459d-a335-ce66c295df01_2048x1293.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 6.3. 표 형식 데이터 및 상호작용성 범위
1. **표 형식 데이터**
    1. 다음은 동일한 데이터를 표 형식으로 제공한다.
    2. "불가능"이라고 표시된 셀은 해당 레시피의 한계를 넘어 해당 속도로 워크로드를 처리할 수 없음을 의미한다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!moMr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a17747e-8857-443b-a4ab-218b517f1fdf_2048x593.png">
<figcaption>출처: SemiAnalysis</figcaption>
2. **막대 그래프**
    1. 다음은 100~300 tok/s/user 범위에서 동일한 데이터를 막대 그래프로 나타낸다.
    2. 네 가지 레시피 모두 250 tok/s/user까지 데이터가 있으며, Rubin과 GB300만 300 tok/s/user에 도달한다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!46dJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa06afa4a-0f30-436d-959f-bcebe37606b4_2048x691.png">
<img alt="" src="https://substackcdn.com/image/fetch/$s_!F2Sw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe07c6e89-f1a9-4b63-9ae2-dc951c74f6bf_1536x52.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 6.4. Rubin과 Blackwell의 성능 비교 분석
1. **Rubin 대 2026년 7월 GB300 NVL72 기준선**
    1. Rubin의 우위는 낮은 상호작용성에서 가장 작고, 상호작용성 곡선의 중간을 거치면서 계속 커진다.
    2. Rubin은 100 tok/s/user까지 Blackwell보다 거의 2배의 처리량을 보이며, 200 tok/s/user 부근에서 격차가 약 4배로 확대되어 정점에 달한다.
    3. 그 후 격차는 다시 좁아지기 시작한다.
    4. 300 tok/s/user에서 GB300보다 5.4배의 성능 향상은 Rubin이 더 앞서나가는 것이 아니다.
    5. 오히려 GB300이 한계의 마지막, 겨우 실행 가능한 지점을 실행하여 비율이 급증하는 것이다.
    6. GB200은 300 tok/s/user에 전혀 도달할 수 없다.
    7. Blackwell의 GPU당 처리량은 높은 상호작용성에서 배치 크기가 줄어들면서 빠르게 감소하는 반면, Rubin은 여전히 한계의 더 평평한 부분에 있다.
2. **Rubin 대 2025년 GB200 NVL72 기준선**
    1. 2025년 GB200 NVL72 기준선과 Rubin을 비교하는 것은 다르며, 곡선 중간에서 가장 큰 우위를 보인다.
    2. 낮은 속도에서는 격차가 3배 미만으로 시작하지만, 150 tok/s/user(Nvidia가 차트에서 강조하는 지점)에서 약 10배로 증가한 후, 200 tok/s/user 부근에서 6배로 다시 감소한다.
    3. 해당 라인의 데이터는 정확하지만, 언급했듯이 1년 된 소프트웨어 스택을 사용하며, 오늘날 실행할 GB200이 아니다.
3. **상호작용성 범위의 최상단**
    1. 상호작용성 범위의 최상단에서는 Blackwell 곡선이 급격히 떨어진다.
    2. 350 tok/s/user에서는 GB200과 GB300 모두 워크로드를 전혀 처리할 수 없으며, Rubin만이 실제 곡선을 제공하여 300 tok/s/user에서 96,446 tok/s/MW, 350 tok/s/user에서 70,703 tok/s/MW를 제공한다.
    3. Rubin은 Blackwell보다 훨씬 더 많은 "고속 모드"를 제공할 것이다.

## 7. Rubin 대 Blackwell TCO당 성능
메가와트당 성능은 전력 대비 성능만 계산한다.  백만 출력 토큰당 비용은 하드웨어의 총 소유 비용(TCO)에 IT 자본 비용, 전기 및 데이터센터 비용을 포함한다.

### 7.1. TCO 모델 및 비용 분석
1. **TCO 모델**
    1. SemiAnalysis의 TCO 모델은 서버 세대별 자본 비용과 운영 비용을 포괄적으로 분석한다.
2. **TCO당 성능 계산**
    1. 각 SKU의 총 TCO를 동일하게 재정규화된 출력 처리량으로 나누므로, 수치가 낮을수록 좋다.
3. **Rubin의 GPU당 TCO**
    1. Rubin은 Blackwell보다 GPU당 TCO가 더 높다.
    2. 운영자 소유 시나리오(임대 가격 아님)에서 Rubin은 GPU 시간당 3.57달러, GB200은 1.84달러, GB300은 2.36달러이다.
4. **Rubin의 토큰당 달러 우위**
    1. 아래 차트와 표는 Rubin의 토큰당 달러 우위가 메가와트당 우위보다 약간 작게 나타남을 보여줄 것이다.

### 7.2. TCO당 성능 분석 기준선
1. **2025년 GB200 기준선**
    1. 메가와트당 분석과 마찬가지로, 2025년 GB200 기준선은 Rubin의 성능에서 가장 큰 이득을 보여준다.
2. **2026년 7월 GB200 및 GB300 기준선**
    1. 그러나 오늘날 용량을 구매하는 사람에게는 2026년 7월 GB200 및 GB300 수치가 비교를 위한 더 관련성 있는 기준선이다.

### 7.3. 파레토 곡선 및 표 형식 데이터
1. **파레토 곡선**
    1. 다음 파레토 곡선은 백만 출력 토큰당 비용을 상호작용성과 비교하여 나타낸다.
    2. 각 선은 해당 레시피의 한계가 끝나는 지점에서 멈춘다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!elXn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70c45703-725b-4176-aaef-86a34ca5e60d_2048x1293.png">
<figcaption>출처: SemiAnalysis</figcaption>
2. **표 형식 데이터**
    1. 다음은 동일한 데이터를 표 형식으로 제공하며, 각 상호작용성에서 Rubin이 몇 배 더 저렴한지를 보여주는 비율을 포함한다.
    2. 다시 한번, "불가능"으로 표시된 셀은 해당 레시피의 한계가 도달할 수 없는 속도이다.
3. **막대 그래프**
    1. 아래 차트는 100~300 tok/s/user 범위에서 한계를 막대 그래프로 나타낸다.
    2. 네 가지 레시피 모두 250 tok/s/user까지 데이터가 있으며, Rubin과 GB300만 300 tok/s/user에 도달한다.
<img alt="" src="https://substackcdn.com/image/fetch/$s_!IeUT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20a9279d-57af-43bb-a36b-3f850e18f43b_2048x651.png">
<img alt="" src="https://substackcdn.com/image/fetch/$s_!Te82!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1c63d4b-cf07-4f15-a990-e340a68cf9ff_1534x52.png">
<figcaption>출처: SemiAnalysis</figcaption>

### 7.4. Rubin과 Blackwell의 TCO당 성능 비교 분석
1. **Rubin 대 2026년 7월 GB200 및 GB300**
    1. 2026년 7월 GB200 및 GB300과 비교할 때, Rubin은 모든 상호작용성에서 더 저렴하며, 상호작용성이 높아질수록 격차가 커진다.
    2. 100 tok/s/user까지 GB200보다 약 1.5배 저렴하게 시작하며, 200 tok/s/user에서 250 tok/s/user까지 3배로 개선된다.
    3. 300 tok/s/user에서 GB300보다 5배 우위는 메가와트당 관점과 동일하며, GB300은 겨우 토큰을 처리할 수 있고 GB200은 이 상호작용성 수준에서 전혀 처리할 수 없다.
2. **Rubin 대 2025년 GB200 NVL72 기준선**
    1. 2025년 GB200 NVL72 기준선은 다시 한번 더 극적인 결과를 보여주며, 곡선 중간에서 정점에 달한다.
    2. Rubin은 낮은 속도에서 2배 이상 저렴하게 시작하며, 150 tok/s/user에서 거의 8배로 정점에 달한 후, 200 tok/s/user까지 5배로 다시 감소한다.
    3. 메가와트당 버전과 동일한 의견으로, 2025년 GB200 기준선은 1년 된 소프트웨어 스택을 측정하며, 오늘날 실행할 GB200이 아니다.
3. **상호작용성 범위의 최상단**
    1. 범위의 최상단에서는 상황이 동일하다.
    2. GB200은 250 tok/s/user를 넘는 작동 지점이 없고, GB300은 300 tok/s/user를 넘는 작동 지점이 없으므로, 350 tok/s/user에서는 Rubin만이 작동할 수 있으며, 백만 출력 토큰당 4.18달러의 비용을 제공한다.
