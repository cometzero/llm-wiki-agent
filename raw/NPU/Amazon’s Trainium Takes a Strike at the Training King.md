---
title: Amazon’s Trainium Takes a Strike at the Training King
origin: lilys_ai
lilys_project_id: 11899159
lilys_project_url: https://lilys.ai/digest/11899159
lilys_created_at: '2026-10-25T13:40:39.248Z'
lilys_collection: AI
source_type: webPage
lilys_note_id: '15793600'
sources:
- id: '21104152'
  source_type: webPage
  url: https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at
  title: Amazon’s Trainium Takes a Strike at the Training King
  status: ready
---

# Amazon’s Trainium Takes a Strike at the Training King

## LilysAI note

> 아마존 트레이니움(Trainium)이 엔비디아 GPU에 대항할 수 있는 핵심 강점은 무엇인가요? 추론에 강했던 트레이니움이 이제 **네이티브 PyTorch 지원**과 **업계 최고 수준의 프로파일러**를 통해 학습 분야에서도 강력한 경쟁력을 갖추게 되었습니다.

## 1. 아마존 트레이니움(Trainium)의 훈련 시장 진출[^1]
아마존 트레이니움은 추론 분야에서 강점을 보였지만, 이제 네이티브 PyTorch 지원과 뛰어난 프로파일러를 통해 훈련 시장에서도 강력한 경쟁력을 갖추게 되었다.

### 1.1. 트레이니움의 과거와 현재[^2]
1. **추론 분야에서의 강점**[^3]
    1. 트레이니움은 이미 추론 영역에서 성능을 입증했다.[^4]
    2. Anthropic은 Trainium2 및 Trainium3에서 프로덕션 추론 및 RL 롤아웃을 실행하고 있다.[^5]
2. **훈련 분야에서의 약점 및 변화**[^6]
    1. 과거에는 모델 아키텍처 변경 속도가 느린 추론에 적합했지만, 연구 훈련에는 최적의 솔루션이 아니었다.[^7]
    2. 훈련 과정에서는 연구자들이 다양한 실험과 모델 아키텍처의 변형을 반복하며 광범위한 API 표면을 다루는 스택이 필요했다.[^8]
    3. 과거에는 이러한 요구사항을 충족하지 못했다.[^9]
3. **네이티브 PyTorch 훈련 경험으로의 전환**[^10]
    1. AWS Neuron 팀은 이러한 단점을 개선하기 위해 적극적으로 노력하고 있으며, 가장 큰 변화는 네이티브 PyTorch 훈련 경험을 제공하는 것이다.[^11]
    2. 과거에는 훈련 루프에 `xm.step()`을 추가하고 XLA 스타일의 실행 모델과 씨름해야 했지만, 이제는 이러한 방식에서 벗어났다.[^12]
    3. 트레이니움은 이제 PyTorch 사용자들이 기대하는 방식으로, 즉 eager 모드에서 `torch.compile` 및 표준 API를 사용하여 PyTorch를 실행한다.[^13]
4. **SemiAnalysis 팀의 경험**[^14]
    1. SemiAnalysis 엔지니어링 팀은 지난 몇 주 동안 Trainium3 랙을 사용해 보았으며, 전반적인 방향성이 훌륭하다고 평가했다.[^15]
    2. 아직 완벽하지 않고 몇 가지 버그가 있었지만, CUDA 생태계의 성숙도에는 미치지 못하더라도 올바른 방향으로 나아가고 있다고 판단했다.[^16]
    3. AWS 팀은 에이전트 코딩(agentic coding)의 도움을 받아 빠르게 발전하고 있다.[^17]
5. **자동화된 품질 관리**[^18]
    1. 다른 가속기 회사들과 달리, 트레이니움은 자동화된 품질 관리를 위해 최대 80,000개의 물리적 코어를 할당하여 안정적인 CI(Continuous Integration) 환경을 구축했다.[^18]

### 1.2. Trainium3 TorchTitan 및 Neuron Explorer 프로파일러 경험[^19]
1. **TorchTitan 및 TorchNeuron 스택 경험**[^20]
    1. 이 글에서는 Trainium3 TorchTitan 및 TorchNeuron 스택에 대한 경험을 다룬다.[^20]
2. **Neuron Explorer 프로파일러의 우수성**[^19]
    1. 트레이니움의 Neuron Explorer 프로파일러는 Nvidia와 AMD의 프로파일러보다 훨씬 뛰어나다.[^20]
    2. 트레이니움 프로파일러가 "GPU 불가능(GPU Impossible)"한 이유를 보여주는 여러 데모를 만들었다.[^21]

<img alt="Nafea Bshara, VP at AWS In Trainium Profiler Showcasing Trainium’s Finegrain Profiler." src="https://substackcdn.com/image/fetch/$s_!hGVA!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F680cf6ed-4bdd-4d53-9c2c-569ac56bb93c_1452x790.png">
<figcaption>AWS의 Nafea Bshara 부사장이 Trainium 프로파일러에서 Trainium의 세밀한 프로파일러를 시연하는 모습. 출처: SemiAnalysis</figcaption>

## 2. PyTorch 경험 개선 및 생태계 확장[^22]
아마존은 소프트웨어 전략을 크게 수정하여 Trainium3의 채택을 의미 있게 확대하고 있으며, PyTorch 생태계와의 통합을 강화하고 있다.

### 2.1. 네이티브 PyTorch 경험으로의 전환[^23]
1. **소프트웨어 전략의 주요 변화**[^24]
    1. 아마존은 소프트웨어 전략을 크게 수정했으며, 이는 Trainium3 채택을 의미 있게 확대할 것으로 예상된다.[^25]
    2. TorchNeuron은 PyTorch/XLA 프로젝트를 통해 Trainium을 PyTorch에 억지로 연결하는 대신, 네이티브 PyTorch 경험을 제공한다.[^26]
    3. 새로운 백엔드는 프론티어 랩 커널 엔지니어가 아닌 모든 사용자를 대상으로 한다.[^27]
    4. AWS는 심지어 Google의 네이티브 Torch on TPU 노력의 리더를 고용하여 Trainium용 네이티브 Torch 작업을 진행하고 있다.[^28]
    5. 그는 XLA, xprof, Cloud TPU 등을 포함하여 Google에서 TPU 소프트웨어 개발을 처음부터 이끌었던 인물이다.[^29]
2. **기존 접근 방식의 문제점**[^30]
    1. 기존 접근 방식은 CUDA 사용자에게 Trainium을 이질적으로 느끼게 했다.[^31]
    2. PyTorch/XLA는 지연 텐서 그래프 캡처에 의존했으며, 네이티브 eager 모드를 지원하지 않았다.[^32]
    3. 또한 PyTorch의 네이티브 분산 API(torch.distributed.*)나 네이티브 병렬 처리 API(DTensor, SimpleFSDP, DDP)를 지원하지 않았다.[^33]
    4. 사용자들은 `torch_xla.experimental.spmd_fsdp` 및 `torch_xla.distributed.spmd`와 같은 외부 XLA SPMD API에 의존해야 했다.[^34]
    5. CUDA에서 네이티브 PyTorch에 익숙한 연구자들에게 Trainium으로 전환하는 것은 훈련 루프를 다시 배우는 것을 의미했다.[^35]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!NSYi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb846e38-260b-4211-9146-390bebf520bc_1446x1012.png">
<figcaption>출처: AWS</figcaption>

3. **PyTorch/XLA의 불편함**[^36]
    1. GPU 코드베이스를 XLA 마커를 추가하여 변환하는 어려움은 PyTorch/XLA를 사용했던 모든 사용자에게 큰 단점이었다.[^36]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!IzTF!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73ccd20a-b8b7-435f-8802-4960c36062d9_1126x668.png">
<figcaption>출처: AWS</figcaption>

4. **간소화된 전환**[^37]
    1. 높은 수준에서 필요한 유일한 변경 사항은 `.to("cuda")`를 `.to("neuron")`으로 바꾸는 것이며, 이론적으로 대부분의 PyTorch ATen 연산자는 별다른 문제 없이 작동할 것이다.[^38]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!OoTS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85a8b8ec-1992-4b58-bb84-dc655d291eaf_526x329.png">
<figcaption>출처: AWS</figcaption>

    1. 이론적으로 PyTorch의 `torch.accelerator` 하드웨어 독립적 API를 사용하면 bf16 autocast와 같은 코드 라인은 변경할 필요가 없다.[^39]
    2. 하지만 PyTorch의 일부 API와 일부 연구 코드베이스는 아직 `torch.accelerator` 네임스페이스로 마이그레이션되지 않고 `torch.cuda.*` 네임스페이스를 직접 호출하는 경우가 있다.[^39]
5. **BF16 훈련 경험 우선순위**[^40]
    1. 대부분의 학계 및 연구자들은 BF16을 주로 사용하므로, Trainium Torch는 BF16 훈련 경험이 완벽해질 때까지 TorchAO MXFP8을 지원하지 않을 예정이다.[^41]
    2. MXFP8 훈련을 수행하는 대부분의 사용자는 대규모 훈련을 위해 맞춤형 커널을 작성할 수 있는 Tier 1 랩이기 때문에 이러한 우선순위 설정에 동의한다.[^42]

### 2.2. Trainium Torch 생태계 확장[^43]
1. **PyTorch 생태계 라이브러리 지원**[^44]
    1. PyTorch는 핵심 PyTorch뿐만 아니라 Hugging Face Transformers, PEFT, diffusers, TRL, Accelerate, TorchTitan 등 전체 라이브러리 생태계 때문에 인기가 많다.[^45]
    2. Trainium Torch가 Hugging Face Accelerate를 포함한 많은 라이브러리를 이미 지원하고 있다는 점은 놀랍다.[^46]
    3. Trainium은 TorchTitan이라는 인기 있는 오픈 소스 훈련 코드베이스를 지원하며, 많은 Tier 2 랩에서 이를 내부 훈련 코드베이스의 기반으로 사용하고 있다.[^47]
    4. Trainium의 새로운 PyTorch 경험은 이 또한 완벽하게 지원한다.[^48]
2. **vLLM/SGLang 생태계와의 협력**[^49]
    1. Google이 Inferact/RadixArk와 성공적으로 협력하여 TPUs를 vLLM/SGLang 생태계에 통합하고, Meta를 프로덕션 TPU 고객으로 확보한 사례를 보았다.[^50]
    2. TPUs를 vLLM/SGLang 생태계에 통합함으로써, TPUs는 Muse Spark Open에 대한 즉각적인 지원과 인기 있는 향후 모델에 대한 즉각적인 TPU 지원 약속을 자동으로 얻을 수 있었다.[^51]
    3. 에이전트 코딩의 증가로 엔진 코드 자체의 중요성이 줄어들었지만, vLLM/SGLang이 제공하는 것은 생태계이다.[^52]
    4. 어떤 오픈 소스 모델이든, 출시 당일부터 전 세계 ML 커뮤니티는 vLLM/SGLang을 추론을 위한 핵심 엔진으로 신뢰한다.[^53]
    5. 다른 어떤 엔진도 이러한 영향력을 가지고 있지 않다.[^54]
3. **Trainium의 vLLM/SGLang 커뮤니티 투자**[^55]
    1. Trainium은 TorchTPU 접근 방식과 유사하게, 네이티브 PyTorch(TorchNeuron) 기반의 SGLang에서 Trainium에 대한 하드웨어 접근 및 조기 액세스를 통해 vLLM/SGLang 커뮤니티에 빠르게 투자하고 있다.[^56]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!iP2W!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23423dd8-6352-4943-af4d-c303ca5ad2af_1492x1384.png">
<figcaption>출처: SemiAnalysis</figcaption>

## 3. TorchTitan 경험 및 성능 분석[^57]
TorchTitan을 통한 Trainium의 훈련 경험은 전반적으로 긍정적이었지만, 컴파일 시간과 같은 개선이 필요한 부분도 있었다.

### 3.1. TorchTitan을 이용한 훈련 경험[^58]
1. **오픈 소스 사전 훈련 프레임워크 테스트**[^59]
    1. TorchTitan은 가장 인기 있는 오픈 소스 사전 훈련 프레임워크 중 하나이며, Trainium의 지원을 테스트하여 연구자가 Trainium으로 복잡한 모델을 훈련할 때의 사용자 경험을 평가했다.[^60]
    2. 특히, 16개의 Trainium2 칩(총 64개의 LNC=2 논리 코어)과 64개의 물리적 칩을 가진 랙 스케일 Trainium3 UltraServer에서 Qwen3-32B를 훈련했다.[^61]
2. **전반적인 사용자 경험 평가**[^62]
    1. 전반적으로 사용자 경험은 좋았지만, 아마존 팀이 이미 해결 로드맵에 포함시킨 몇 가지 미흡한 점이 있었다.[^63]
    2. ML 연구에서는 빛의 속도로 최적화된 스택보다는 적절한 성능과 모델 아키텍처 수정에 대한 광범위한 지원이 중요하므로, 연구자들이 스택과 씨름하지 않고 반복 작업을 수행할 수 있어야 한다.[^64]

### 3.2. 훈련 처리량 및 MFU 측정[^65]
1. **Neuron 공식 TorchTitan 이미지 사용**[^66]
    1. Neuron의 공식 TorchTitan 이미지를 사용하여 문제없이 훈련을 시작할 수 있었다.[^66]
2. **Eager 모드 성능**[^67]
    1. eager 모드에서 평균 11,099 토큰/초의 훈련 처리량과 23.89%의 MFU(Model FLOPs Utilization)를 기록했다.[^67]
3. **컴파일 모드 성능**[^68]
    1. 컴파일 모드에서는 14,156 토큰/초의 처리량과 30.47%의 MFU를 기록하여, eager 모드보다 1.28배 향상된 처리량을 보였다.[^69]
    2. 모델 아키텍처를 약간 변경해도 잘 작동했다.[^70]
4. **최신 모델 아키텍처 훈련 레시피 지원**[^71]
    1. Neuron은 더 현대적인 모델 아키텍처를 위한 훈련 레시피도 제공하며, gpt-oss 20B 훈련 레시피를 테스트했다.[^72]
    2. Neuron은 TorchTitan의 실험적인 트레이너 모듈인 GraphTrainer와의 통합을 통해 gpt-oss 훈련을 지원한다.[^73]
    3. 특히, Neuron은 SimpleFSDP의 Trainium 호환 구성, PyTorch 계산 그래프 캡처를 위한 컴파일 백엔드, 그리고 어텐션 및 MoE(Mixture-of-Experts) 연산을 위한 맞춤형 NKI 커널을 추가한다.[^74]
    4. 사용자 경험 측면에서 레시피는 별다른 문제 없이 작동했으며, 모든 것이 순조롭게 진행되었다.[^75]

### 3.3. TokenSwitch 구현 및 컴파일 시간 문제[^76]
1. **TokenSwitch 미구현 문제**[^77]
    1. 아직 업스트림 API를 사용하여 구현되지 않은 한 가지는 TokenSwitch였다.[^78]
    2. MoE 시대에는 추론 및 훈련 모두에서 MoE 결합 및 MoE 디스패치가 가장 중요한 통신 연산 중 하나이며, 통신량의 60-70%를 차지한다. TokenSwitch는 이를 위한 PyTorch의 핵심 API이다.[^79]
    3. Trainium은 아직 이를 지원하지 않으며, 대신 NeuronEPTokenDispatcher라는 맞춤형 TorchTitan 클래스에 의존한다.[^80]
    4. 이를 TokenSwitch API로 옮기는 것은 간단한 수정으로 보이며, AWS 팀은 Meta PyTorch 팀과 협력하여 TokenSwitch ABC가 Trainium도 지원할 수 있도록 수정하겠다고 약속했다.[^81]
2. **긴 컴파일 시간 문제**[^82]
    1. 다소 실망스러웠던 부분은 Neuron 컴파일러가 컴파일하는 데 오랜 시간이 걸려 첫 단계에서 긴 대기 시간이 발생했다는 점이다.[^83]
    2. 구체적으로, 첫 단계는 eager 모드에서 184.6초(컴파일 모드에서 255.7초)가 걸렸는데, 이는 첫 단계를 제외한 평균 단계 시간보다 30-55배 더 길다.[^84]
    3. gpt-oss의 경우, 이 훈련 실행은 27분 17초라는 엄청나게 긴 컴파일 시간을 기록하여, 특히 새로운 모델 아키텍처를 실험하는 연구자들에게는 최악의 사용자 경험을 제공한다.[^85]
    4. 이러한 이유는 과거에 Trainium 컴파일러 스택이 주로 추론에 초점을 맞췄기 때문이다. 추론에서는 컴파일이 오프라인으로 수행되고 이미지당 한 번 캐시되므로 컴파일 시간이 중요하지 않지만, 훈련에서는 중요하다.[^86]
    5. 당시 추론에는 올바른 결정이었지만, 모델 아키텍처를 반복하는 연구자들에게는 상당한 마찰 지점이다.[^87]

### 3.4. 컴파일 시간 개선 계획[^88]
1. **Neuron 팀의 문제 해결 노력**[^89]
    1. Neuron 팀은 이 문제를 직접 해결하고 있다.[^89]
2. **향후 TorchNeuron 릴리스의 개선 사항**[^90]
    1. 향후 TorchNeuron 릴리스에는 광범위한 사전 컴파일된 NKI 커널과 빠른 컴파일을 위해 재설계된 컴파일 스택을 갖춘 새로운 컴파일러 백엔드가 도입될 예정이다.[^91]
    2. 이는 eager 및 컴파일 모드 모두에서 첫 단계까지의 시간을 최대 2자리 수까지 줄이는 것을 목표로 하며, 성능 저하는 최소화하거나 없을 것이다.[^91]
    3. 이러한 목표를 달성한다면 컴파일 시간은 더 이상 문제가 되지 않을 것이다.[^92]

## 4. 훈련 MatMul 성능 및 FlexAttention API 지원[^93]
Trainium3는 다양한 행렬 곱셈 형태에서 GB300보다 높은 MFU를 달성했으며, FlexAttention API 지원을 통해 연구자들에게 유연성과 사용 편의성을 제공한다.

### 4.1. 훈련 MatMul 성능[^94]
1. **실험 훈련의 중요성**[^95]
    1. 실험 훈련에서 가장 중요한 것 중 하나는 ML 연구자들이 다양한 시도를 하기 때문에 광범위한 형태에서 적절한 성능을 확보하는 것이다.[^95]
2. **Trainium3 벤치마크**[^96]
    1. PyTorch `nn.functional.linear` API에서 단일 Trainium3 논리 코어(LNC=2)의 행렬 곱셈 성능을 벤치마킹하고, GB300 및 B200과 비교했다.[^97]
    2. 주요 오픈 가중치 모델의 투영 연산 행렬 형태를 조사했으며, 다양한 배치 크기 시나리오를 나타내기 위해 M 차원을 1, 128, 2048로 설정했다.[^98]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!bRyu!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b02cad9-f642-4bae-be70-4b2141f6a983_1980x1260.png">
<figcaption>출처: SemiAnalysis</figcaption>

3. **벤치마크 결과**[^99]
    1. 벤치마크에서 Trainium3는 행렬 곱셈이 1 GFLOP의 연산을 수행하는 중간 범위부터 GB300보다 눈에 띄게 높은 MFU를 달성했다.[^100]
    2. GB300과 B200이 Trainium3를 능가하기 시작한 것은 100 GFLOP 이후였으며, Trainium3는 1 TFLOP 이후 다시 우위를 점했다.[^101]

### 4.2. FlexAttention API 지원[^102]
1. **FlexAttention API의 중요성**[^103]
    1. FlexAttention은 PyTorch를 사용하여 다양한 어텐션 변형을 구현할 수 있는 고수준 API로, 역방향 자동 생성 및 합리적인 성능을 제공한다.[^104]
    2. FlexAttention 지원이 잘 되어 있다는 것은 하드웨어의 유연성과 연구자들에게 제공되는 사용 편의성을 보여준다.[^105]
    3. Trainium3에서 FlexAttention 벤치마크 스위트를 실행하여 FlexAttention 지원을 확인했다.[^106]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!GgbZ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd03ecc2c-c3cf-4424-a366-5a9d2bd037a6_1600x680.png">
<figcaption>출처: SemiAnalysis</figcaption>

2. **FlexAttention 벤치마크 결과**[^107]
    1. Trainium3는 96개의 테스트 케이스 중 89개를 통과하여 93%의 통과율을 기록했다.[^108]
    2. 실패한 7개 케이스는 모두 큰 배치 크기(4)와 시퀀스 길이(8192)에서 발생했으며, 수치 오류가 아닌 컴파일 시간이 예산을 초과하여 실패했다.[^109]
    3. 이러한 문제는 TorchNeuron의 향후 버전에서 수정될 예정이다.[^110]
3. **맞춤형 어텐션 변형 구현**[^111]
    1. 또한 Trainium3에서 FlexAttention 벤치마크 스위트에 없는 맞춤형 어텐션 변형을 구현해 보았으며, Nvidia GPU와 수치가 일치했다.[^112]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!BJnh!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8cb4895-1a44-461d-838a-f13de37d3a8e_1600x680.png">
<figcaption>출처: SemiAnalysis</figcaption>

## 5. 자동화된 품질 보증 및 Neuron Explorer 프로파일러의 우수성[^113]
Trainium은 자동화된 품질 보증에 막대한 투자를 하고 있으며, Neuron Explorer 프로파일러는 업계 최고 수준의 정밀하고 시각적인 분석 기능을 제공한다.

### 5.1. 자동화된 품질 보증[^114]
1. **SemiAnalysis의 역할**[^115]
    1. SemiAnalysis는 전 세계 ML 커뮤니티에서 "CI Karen"으로 알려져 있으며, 모든 하드웨어 공급업체에 높은 기준을 설정하고 AI 칩 회사의 고위 경영진이 엔지니어들에게 자동화된 품질 관리를 위한 충분한 리소스와 CI 플릿을 제공하도록 노력한다.[^115]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!aaSF!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ece87e1-1fd3-4bae-bd17-9fe9e28190e1_1040x598.png">
<figcaption>출처: SemiAnalysis</figcaption>

2. **AMD와의 협력 사례**[^116]
    1. 최근 9개월간 AMD 고위 경영진과의 노력 끝에, 엔지니어들이 게이팅 테스트 그룹에서 93%의 패리티를 달성할 수 있는 충분히 안정적인 노드를 확보했다.[^117]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!jjqT!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78c1bfee-bc21-46e5-bb7f-1abfe8ac31fe_2048x1065.png">
<figcaption>출처: vLLM Dashboard</figcaption>

3. **추론과 훈련의 차이점**[^118]
    1. 추론은 좁은 문제이다. 소수의 프로덕션 모델을 서비스하는 랩은 주로 고정된 아키텍처와 소수의 핵심 커널을 필요로 한다.[^119]
    2. 훈련은 일반성 문제이다. 수천 개의 연산자 각각에 역방향 패스가 필요하며, 연구 코드베이스는 때때로 실수로 더 높은 정밀도로 연산자를 실행하기도 하는데, 이 또한 지원되어야 한다.[^120]
4. **AWS의 광범위한 테스트 노력**[^121]
    1. Trainium이 광범위한 모델 아키텍처에서 작동하고 eager 모드와 컴파일 모드를 모두 잘 수행할 수 있도록, AWS는 다양한 정규화, MLP, MoE 레이아웃 및 어텐션 유형을 포함하는 10만 개 이상의 Hugging Face 모델 목록을 수집했다.[^122]
    2. AWS는 충돌 여부뿐만 아니라 성능, CPU 폴백을 사용하는 연산자, 그래프 중단 지점, 그리고 가장 중요하게는 CPU 및 Nvidia 기준선에 대한 수치 정확도를 테스트한다.[^123]
    3. 텐서 수준 패리티와 손실 곡선 발산도 테스트한다.[^124]
    4. 시험을 10분 안에 끝내는 것은 쉽지만, 0점을 받는다면 아무리 빨리 끝내도 소용없다.[^125]
    5. 훈련 스택도 마찬가지이다. 적절한 MFU%를 얻는 것은 쉽지만, 수치 문제를 일으키지 않으면서 적절한 MFU%를 얻는 것은 어렵다.[^126]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!4yzy!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb0a6c55-273d-4f78-9819-694f30224206_717x649.png">
<figcaption>출처: AWS</figcaption>

5. **AWS의 투명한 품질 관리**[^127]
    1. 통과율이 아직 100%는 아니지만, 중요한 것은 발전 궤적이다.[^128]
    2. AWS는 에이전트 스웜(agent swarms)을 통해 남은 실패를 체계적으로 수정하며 빠르게 발전하고 있다.[^129]
    3. AWS의 내부 요약 테이블(고위 경영진이 보는)이 격차를 투명하게 보여주고 숨기지 않는다는 점은 강점이라고 생각한다.[^130]
    4. SemiAnalysis와 업스트림 유지 관리자들이 다른 하드웨어 공급업체에서 품질 관리 문화를 개선하려고 시도했을 때, 고위 경영진이 실제 패리티 통과율을 알게 되면 진정으로 충격을 받는 것을 경험했다.[^131]
    5. 특히 한 공급업체에서는 중간 관리층의 필터링이 너무 심해서 CI 수치가 고위 경영진에게 도달했을 때는 99.99%로 표시되었지만, 당시 실제 게이팅 패리티 통과율은 5% 미만이었다.[^132]

### 5.2. Neuron Explorer - Nvidia 및 AMD 프로파일러보다 우수[^133]
1. **업계 최고 수준의 프로파일러**[^134]
    1. Trainium의 프로파일러는 단연 업계를 선도하며 SOTA(State-Of-The-Art) 수준이다.[^135]
    2. 초기 인상을 공유하며, 향후 Trainium 커널 관련 글에서 전체 사용자 경험을 공유할 예정이다.[^136]
2. **Anthropic 성능 엔지니어들의 평가**[^137]
    1. Trainium의 프로파일러는 Anthropic의 모든 성능 엔지니어들에게 사랑받고 있다.[^138]
    2. Anthropic의 성능 책임자(전 Jane and Finch Street 출신)는 Trainium에서의 성능 분석이 Nvidia GPU(및 당연히 AMD GPU)에서의 성능 분석보다 훨씬 낫다고 공개적으로 말했다.[^139]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!qA-i!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea535417-4c21-49ed-b9f9-c3c80eb222af_2048x822.png">
<figcaption>출처: Tristan Hume on Twitter</figcaption>

3. **프로파일링 설정의 어려움과 사용자 경험**[^140]
    1. Tristan Hume의 의견에 동의한다. 프로파일링 설정이 다소 혼란스러웠지만(불가능하지는 않음), 초기 어려움을 극복한 후에는 프로파일링 경험이 놀라웠다.[^141]
    2. 여러 환경 변수를 설정하고, 다른 파일 유형으로 저장하며, 다양한 명령어를 사용하여 프로파일 추적을 캡처하고 봐야 한다.[^142]
    3. 이는 커널 프로파일링 설정일 뿐이며, PyTorch 프로파일링 설정도 비슷하지만 약간의 차이가 있어 더욱 혼란스럽다.[^143]
    4. Codex의 도움을 받아(Claude는 Trainium 커널 작성을 거부했기 때문에), 최선의 작업 설정은 다음과 같다.[^144]
        1. 영구 Neuron Explorer 서버를 시작한다.[^145]
        2. `neuron-explorer capture` 명령으로 커널을 프로파일링한다.[^146]
        3. 프로파일 추적을 웹 요청으로 Neuron Explorer 서버에 아티팩트로 업로드한다.[^147]
4. **문서화 개선 요청**[^148]
    1. AWS에 워크플로우에 대한 문서가 더 명확해져서, 어떤 환경 변수를 어떤 이유로 설정해야 하는지, 각 파일 유형이 어떤 목적을 가지는지 설명해 달라고 피드백을 공유했다.[^148]
5. **프로파일러의 뛰어난 사용자 경험**[^149]
    1. 설정이 완료되면 프로파일러 사용자 경험은 훌륭하다.[^150]
    2. Neuron Explorer는 하드웨어와 함께 설계되었다.[^151]
    3. 특히 하드웨어 단위를 다른 행으로 분리하여 버블을 한눈에 볼 수 있도록 하는 타임라인이 마음에 든다.[^152]
    4. 대조적으로, GPU 프로그래머는 공식 Nsight 도구가 이를 지원하지 않기 때문에 SM(Streaming Multiprocessor) 내 프로파일링을 위해 자체 설정을 해야 한다.[^153]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Fvcw!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b780b6a-3587-41be-ac01-c268c4624261_1001x609.png">
<figcaption>출처: SemiAnalysis</figcaption>

6. **의존성 시각화 기능**[^154]
    1. 뷰어가 의존성을 시각화하는 방식도 마음에 든다.[^155]
    2. 블록을 선택하면 해당 블록의 의존성 및 종속성이 다른 색상으로 강조 표시되어, 작업 중복 여부(예: 계산이 메모리 로딩과 충분히 중복되는지)를 파악하는 데 도움이 된다.[^156]
    3. 아래 이미지는 선택된 흰색 블록이 다음을 나타낸다.[^157]
        1. 빨간색 블록에 흐름 의존적이다.[^158]
        2. 주황색 블록에 순서 의존적이다.[^159]
        3. 파란색 블록의 흐름 의존성이다.[^160]
        4. 보라색 블록의 출력 의존성이다.[^161]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!lX4e!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c749837-cde0-4015-8def-23186b72fc97_647x166.png">
<figcaption>Neuron Explorer 의존성 시각화. 출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!MAqa!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd333f32c-4e37-489c-8281-b741310499d3_2048x924.png">
<figcaption>Neuron Explorer 코드 편집기 매핑. 출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!aTZQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc19ace2d-f4ea-4fa5-8dcb-14dc63db54cf_1172x486.png">
<figcaption>Neuron Explorer: 이벤트에 마우스를 올렸을 때의 이벤트 정보. 출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!KtJu!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F178ccf7f-c5f1-4763-8cea-921827276215_656x538.png">
<figcaption>Neuron Explorer 메모리 뱅크 활용 시각화. 출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!VY_y!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa75e0579-f42c-49ba-96f5-336140a1fa4e_604x292.png">
<figcaption>Neuron Explorer 마이크로초 단위 메모리 처리량 시각화. 출처: SemiAnalysis</figcaption>

### 5.3. Trainium 프로파일러 데모 - 픽셀 아트[^162]
1. **Neuron Explorer의 추가 기능**[^163]
    1. Neuron Explorer는 코드 편집기 매핑, MFU 추정, 메모리 사용량 등 더 많은 기능을 제공하며, 프로파일러의 정밀도 덕분에 픽셀 아트까지 만들 수 있다.[^164]
    2. 아래 이미지는 모두 실제 Trainium 하드웨어에서 실행된 프로파일 추적에서 가져온 것이며, 가짜 프로파일 보고서가 아니다.[^165]
2. **픽셀 아트 생성 영감 및 방법**[^166]
    1. Daniel Liu(Anthropic 성능 엔지니어)의 Bad Apple 게시물에서 영감을 받아 이미지를 생성하기 위한 자체 에이전트 코딩 SKILL.md를 만들었다.[^167]
    2. 아직 프레임별로 비디오를 자동으로 생성하는 데는 시간이 없었지만, 앞으로는 이를 오픈 소스로 공개할 예정이다.[^168]
    3. 주로 물리적 코어당 16개의 DMA 엔진을 사용하여 DMA 엔진을 활성화하여 영역을 "색칠"하고, 음영 처리된 영역의 너비는 각 DMA 엔진이 이동하는 데이터 양에 따라 결정된다.[^169]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!qsps!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc99913b4-6db5-45df-b4e8-4e1db122f915_2048x929.png">
<figcaption>SemiAnalysis 로고 시각화. 출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!OgDQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d1da3ef-a722-4275-9249-897009a7470a_1258x802.png">
<figcaption>제프 베조스(looksmaxxing 전) 시각화. 출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!nRxA!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5811851d-661c-400e-85cf-ce78ca4f93aa_2064x1118.png">
<figcaption>딜런 파텔(looksmaxxing 전) 시각화. 출처: SemiAnalysis</figcaption>

3. **Nvidia에 대한 제안**[^170]
    1. AWS는 Nvidia의 파트너이므로, Jensen은 Nvidia 엔지니어들에게 AWS Trainium 팀과 만나 정확하고 세밀한 프로파일링에 필요한 하드웨어 기능에 대해 논의하도록 지시해야 한다.[^171]
    2. 이를 통해 Nvidia는 Feynman 또는 Feynman-Next GPU에 이 기능을 추가하는 방법을 배울 수 있을 것이다.[^171]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!9bPt!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45749adc-f952-40a7-a175-f4a5cd3e21d0_2048x1193.png">
<figcaption>Trainium3에서 Jensen 시각화. 출처: SemiAnalysis</figcaption>

### 5.4. Nvidia Nsight Compute 및 QuACK 프로파일러와의 비교[^172]
1. **Nvidia Nsight Compute의 설계**[^173]
    1. Nvidia의 커널 내 프로파일러인 Nsight Compute는 다른 설계를 사용한다.[^174]
    2. 이벤트 기반 타임라인 뷰어보다는 집계된 메트릭과 성능 속성에 대한 자세한 정보를 제공한다.[^175]
2. **Tri Dao의 QuACK 프로파일러**[^176]
    1. 가장 유사한 것은 Tri Dao의 QuACK 커널 내 프로파일러로, Nvidia의 In-Kernel Event Tracing API를 사용한다.[^177]
    2. QuACK은 Perfetto가 그에 따라 시각화되도록 맞춤형 설계가 필요하지만, AWS가 Neuron Explorer에서 이를 잘 통합된 핵심 경험으로 만들었다는 점은 훌륭하다.[^178]

<img alt="" src="https://substackcdn.com/image/fetch/$s_!oHdF!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F922100d3-ea70-4104-99e9-f2e6e069e6e1_2048x795.png">
<figcaption>QuACK의 커널 내 프로파일러: QuACK GEMM 커널 시각화. 출처: QuACK</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!24XK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3cbed7a-998a-454c-a7ad-485c0e8bb312_2048x1280.png">
<figcaption>FlashAttention 4 워크로드 분석의 Nsight Compute 뷰. 출처: Nvidia Nsight</figcaption>

[^1]: Amazon’s Trainium Takes a Strike at the Training King — "Amazon’s Trainium Takes a Strike at the Training King Oct 24, 2026 Trainium Best for Inference? But now good for Training too, Native Trainium PyTorch, High Quality CI, TorchTitan, GPU Impossible Profiler Trainium has already proven itself in the realm of inference. Anthropic is running production i…"
[^2]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium has already proven itself in the realm of inference. Anthropic is running production inference and RL rollouts on Trainium2 and Trainium3. Historically, Trainium has been great for inference but not the best fit for research training. In inference, the model architecture changes at a much s…"
[^3]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium has already proven itself in the realm of inference. Anthropic is running production inference and RL rollouts on Trainium2 and Trainium3. Historically, Trainium has been great for inference but not the best fit for research training."
[^4]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium has already proven itself in the realm of inference."
[^5]: Amazon’s Trainium Takes a Strike at the Training King — "Anthropic is running production inference and RL rollouts on Trainium2 and Trainium3. Historically, Trainium has been great for inference but not the best fit for research training."
[^6]: Amazon’s Trainium Takes a Strike at the Training King — "Anthropic is running production inference and RL rollouts on Trainium2 and Trainium3. Historically, Trainium has been great for inference but not the best fit for research training. In inference, the model architecture changes at a much slower pace compared to training, where researchers iterate on …"
[^7]: Amazon’s Trainium Takes a Strike at the Training King — "Anthropic is running production inference and RL rollouts on Trainium2 and Trainium3. Historically, Trainium has been great for inference but not the best fit for research training. In inference, the model architecture changes at a much slower pace compared to training, where researchers iterate on …"
[^8]: Amazon’s Trainium Takes a Strike at the Training King — "In inference, the model architecture changes at a much slower pace compared to training, where researchers iterate on many different experiments and ablations of model architecture and need a stack that covers a broad API surface."
[^9]: Amazon’s Trainium Takes a Strike at the Training King — "In the past, that is where Trainium fell short."
[^10]: Amazon’s Trainium Takes a Strike at the Training King — "The AWS Neuron team is aggressively working to change this pitfall with the biggest shift being moving towards a first-class, native PyTorch training experience. Gone are the days of sprinkling xm.step() through your training loop and wrestling with a bespoke XLA-style execution model. Trainium now …"
[^11]: Amazon’s Trainium Takes a Strike at the Training King — "The AWS Neuron team is aggressively working to change this pitfall with the biggest shift being moving towards a first-class, native PyTorch training experience."
[^12]: Amazon’s Trainium Takes a Strike at the Training King — "Gone are the days of sprinkling xm.step() through your training loop and wrestling with a bespoke XLA-style execution model."
[^13]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium now runs PyTorch the way PyTorch users expect, in eager mode, with torch.compile and the standard APIs."
[^14]: Amazon’s Trainium Takes a Strike at the Training King — "The SemiAnalysis engineering team has been trying out the Trainium3 racks for the past couple of weeks and has found the experience to be great – we love the overall direction of where it is heading. To be clear, it isn’t perfect yet, and we have personally run into a couple of bugs ourselves. It’s …"
[^15]: Amazon’s Trainium Takes a Strike at the Training King — "The SemiAnalysis engineering team has been trying out the Trainium3 racks for the past couple of weeks and has found the experience to be great – we love the overall direction of where it is heading."
[^16]: Amazon’s Trainium Takes a Strike at the Training King — "To be clear, it isn’t perfect yet, and we have personally run into a couple of bugs ourselves. It’s nowhere close to the maturity of the CUDA ecosystem, but the direction is right."
[^17]: Amazon’s Trainium Takes a Strike at the Training King — "Their team is making rapid progress with the help of agentic coding."
[^18]: Amazon’s Trainium Takes a Strike at the Training King — "Furthermore, unlike other accelerator companies, where we had to fight tooth and nail to get their engineers a reasonably stable CI fleet, Trainium uses up to 80,000 physical cores allocated towards automated quality control."
[^19]: Amazon’s Trainium Takes a Strike at the Training King — "In this article, we walk through our experience on the Trainium3 TorchTitan and TorchNeuron stack, along with our experience of Trainium’s Neuron Explorer profiler, which is way better than both Nvidia’s and AMD’s profilers. We created a bunch of demos to show how Trainium’s profiler is “GPU Impossi…"
[^20]: Amazon’s Trainium Takes a Strike at the Training King — "In this article, we walk through our experience on the Trainium3 TorchTitan and TorchNeuron stack, along with our experience of Trainium’s Neuron Explorer profiler, which is way better than both Nvidia’s and AMD’s profilers."
[^21]: Amazon’s Trainium Takes a Strike at the Training King — "We created a bunch of demos to show how Trainium’s profiler is “GPU Impossible.”"
[^22]: Amazon’s Trainium Takes a Strike at the Training King — "Moving Towards a First-Class PyTorch Experience Amazon has made a major course correction to its software strategy, and we believe it will meaningfully broaden Trainium3 adoption. TorchNeuron represents a native PyTorch experience instead of duct-taping Trainium onto PyTorch through the PyTorch/XLA …"
[^23]: Amazon’s Trainium Takes a Strike at the Training King — "Moving Towards a First-Class PyTorch Experience Amazon has made a major course correction to its software strategy, and we believe it will meaningfully broaden Trainium3 adoption. TorchNeuron represents a native PyTorch experience instead of duct-taping Trainium onto PyTorch through the PyTorch/XLA …"
[^24]: Amazon’s Trainium Takes a Strike at the Training King — "Amazon has made a major course correction to its software strategy, and we believe it will meaningfully broaden Trainium3 adoption. TorchNeuron represents a native PyTorch experience instead of duct-taping Trainium onto PyTorch through the PyTorch/XLA project. The new backend is aimed at everyone wh…"
[^25]: Amazon’s Trainium Takes a Strike at the Training King — "Amazon has made a major course correction to its software strategy, and we believe it will meaningfully broaden Trainium3 adoption."
[^26]: Amazon’s Trainium Takes a Strike at the Training King — "TorchNeuron represents a native PyTorch experience instead of duct-taping Trainium onto PyTorch through the PyTorch/XLA project."
[^27]: Amazon’s Trainium Takes a Strike at the Training King — "The new backend is aimed at everyone who isn’t a frontier-lab kernel engineer."
[^28]: Amazon’s Trainium Takes a Strike at the Training King — "AWS has even hired the lead of Google’s native Torch on TPU effort to work on native Torch for Trainium."
[^29]: Amazon’s Trainium Takes a Strike at the Training King — "He was the TPU SW lead from the start of the program at Google, including XLA, xprof, Cloud TPU, etc."
[^30]: Amazon’s Trainium Takes a Strike at the Training King — "The old approach made Trainium feel foreign to anyone coming from CUDA. PyTorch/XLA relied on lazy tensor graph capture and had no first-class eager mode. It also didn’t support PyTorch’s native distributed APIs (torch.distributed.*) or its native parallelism APIs (DTensor, SimpleFSDP, DDP). Users h…"
[^31]: Amazon’s Trainium Takes a Strike at the Training King — "The old approach made Trainium feel foreign to anyone coming from CUDA."
[^32]: Amazon’s Trainium Takes a Strike at the Training King — "PyTorch/XLA relied on lazy tensor graph capture and had no first-class eager mode."
[^33]: Amazon’s Trainium Takes a Strike at the Training King — "It also didn’t support PyTorch’s native distributed APIs (torch.distributed.*) or its native parallelism APIs (DTensor, SimpleFSDP, DDP)."
[^34]: Amazon’s Trainium Takes a Strike at the Training King — "Users had to rely on out-of-tree XLA SPMD APIs such as torch_xla.experimental.spmd_fsdp and torch_xla.distributed.spmd."
[^35]: Amazon’s Trainium Takes a Strike at the Training King — "For researchers who are used to native PyTorch on CUDA, switching to Trainium meant relearning how to write a training loop."
[^36]: Amazon’s Trainium Takes a Strike at the Training King — "The pain of converting GPU research codebases by adding XLA markers everywhere was a massive turnoff to anyone who used PyTorch/XLA before."
[^37]: Amazon’s Trainium Takes a Strike at the Training King — "At a high level, the only change needed is replacing .to(”cuda”) with .to(”neuron”), and in theory the vast majority of the PyTorch ATen operators will work decently well out of the box. https://substackcdn.com/image/fetch/$s_!OoTS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%…"
[^38]: Amazon’s Trainium Takes a Strike at the Training King — "At a high level, the only change needed is replacing .to(”cuda”) with .to(”neuron”), and in theory the vast majority of the PyTorch ATen operators will work decently well out of the box."
[^39]: Amazon’s Trainium Takes a Strike at the Training King — "In theory, with PyTorch’s torch.accelerator hardware-agnostic API, lines of code like bf16 autocast won’t even need to be changed, though some APIs in PyTorch and some research codebases still haven’t migrated to the torch.accelerator namespace and still directly call the torch.cuda.* namespace."
[^40]: Amazon’s Trainium Takes a Strike at the Training King — "As most academics and researchers across robotics, biotech, world models, and self-driving mainly use BF16, Trainium Torch will not support TorchAO MXFP8 on day 0 until they have made the BF16 training experience great. We don’t disagree with this sequence, as most people doing MXFP8 training are bi…"
[^41]: Amazon’s Trainium Takes a Strike at the Training King — "As most academics and researchers across robotics, biotech, world models, and self-driving mainly use BF16, Trainium Torch will not support TorchAO MXFP8 on day 0 until they have made the BF16 training experience great."
[^42]: Amazon’s Trainium Takes a Strike at the Training King — "We don’t disagree with this sequence, as most people doing MXFP8 training are big Tier 1 labs that have enough kernel engineers to write custom kernels for the big training run."
[^43]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium Torch Ecosystem PyTorch is popular not only because of core PyTorch but also because of the entire ecosystem of libraries, including Hugging Face Transformers, PEFT, diffusers, TRL, Accelerate, TorchTitan, etc. We are amazed to see that Trainium Torch already supports a ton of these librari…"
[^44]: Amazon’s Trainium Takes a Strike at the Training King — "PyTorch is popular not only because of core PyTorch but also because of the entire ecosystem of libraries, including Hugging Face Transformers, PEFT, diffusers, TRL, Accelerate, TorchTitan, etc. We are amazed to see that Trainium Torch already supports a ton of these libraries in the ecosystem, incl…"
[^45]: Amazon’s Trainium Takes a Strike at the Training King — "PyTorch is popular not only because of core PyTorch but also because of the entire ecosystem of libraries, including Hugging Face Transformers, PEFT, diffusers, TRL, Accelerate, TorchTitan, etc."
[^46]: Amazon’s Trainium Takes a Strike at the Training King — "We are amazed to see that Trainium Torch already supports a ton of these libraries in the ecosystem, including Hugging Face Accelerate, which an insane number of layers of indirection."
[^47]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium supports one of the most popular clean open-source training codebases called TorchTitan with many Tier 2 labs forking it to serve as the foundation of their internal training codebase."
[^48]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium’s new PyTorch experience fully supports that too."
[^49]: Amazon’s Trainium Takes a Strike at the Training King — "We saw how Google was able to successfully partner with Inferact/RadixArk to bring TPUs into the vLLM/SGLang ecosystem, and also land Meta as a production TPU customer. Furthermore, by bringing TPUs into the vLLM/SGLang ecosystem, TPUs were already able to automatically get day 0 support for Muse Sp…"
[^50]: Amazon’s Trainium Takes a Strike at the Training King — "We saw how Google was able to successfully partner with Inferact/RadixArk to bring TPUs into the vLLM/SGLang ecosystem, and also land Meta as a production TPU customer."
[^51]: Amazon’s Trainium Takes a Strike at the Training King — "Furthermore, by bringing TPUs into the vLLM/SGLang ecosystem, TPUs were already able to automatically get day 0 support for Muse Spark Open and commitments for day 0 TPU support for popular upcoming models."
[^52]: Amazon’s Trainium Takes a Strike at the Training King — "While it is true that the increase in agentic coding has made the engine code itself less important, what vLLM/SGLang brings to the table is the ecosystem."
[^53]: Amazon’s Trainium Takes a Strike at the Training King — "No matter the open source model, on day 0, the global ML community trusts vLLM/SGLang as the go-to engine for inference."
[^54]: Amazon’s Trainium Takes a Strike at the Training King — "No vibe-coded engine has that reach."
[^55]: Amazon’s Trainium Takes a Strike at the Training King — "We are starting to see Trainium rapidly invest in the vLLM/SGLang community with hardware access and early access to Trainium on SGLang built on native PyTorch (TorchNeuron), similar to the TorchTPU approach. https://substackcdn.com/image/fetch/$s_!iP2W!,w_1456,c_limit,f_webp,q_auto:good,fl_progress…"
[^56]: Amazon’s Trainium Takes a Strike at the Training King — "We are starting to see Trainium rapidly invest in the vLLM/SGLang community with hardware access and early access to Trainium on SGLang built on native PyTorch (TorchNeuron), similar to the TorchTPU approach."
[^57]: Amazon’s Trainium Takes a Strike at the Training King — "TorchTitan Experience TorchTitan is one of the most popular open-source pre-training frameworks, and we tested Neuron’s support to gauge the user experience of a researcher training a non-trivial model with Trainium. Specifically, we trained a Qwen3-32B on 16 Trainium2 chips, 64 LNC=2 logical cores …"
[^58]: Amazon’s Trainium Takes a Strike at the Training King — "TorchTitan Experience TorchTitan is one of the most popular open-source pre-training frameworks, and we tested Neuron’s support to gauge the user experience of a researcher training a non-trivial model with Trainium. Specifically, we trained a Qwen3-32B on 16 Trainium2 chips, 64 LNC=2 logical cores …"
[^59]: Amazon’s Trainium Takes a Strike at the Training King — "TorchTitan is one of the most popular open-source pre-training frameworks, and we tested Neuron’s support to gauge the user experience of a researcher training a non-trivial model with Trainium. Specifically, we trained a Qwen3-32B on 16 Trainium2 chips, 64 LNC=2 logical cores in total, and we also …"
[^60]: Amazon’s Trainium Takes a Strike at the Training King — "TorchTitan is one of the most popular open-source pre-training frameworks, and we tested Neuron’s support to gauge the user experience of a researcher training a non-trivial model with Trainium."
[^61]: Amazon’s Trainium Takes a Strike at the Training King — "Specifically, we trained a Qwen3-32B on 16 Trainium2 chips, 64 LNC=2 logical cores in total, and we also tried doing it on a rack-scale Trainium3 UltraServer with 64 physical chips."
[^62]: Amazon’s Trainium Takes a Strike at the Training King — "Overall, we liked the user experience, though there were some rough edges that the Amazon team already has on its roadmap to fix. While we will provide the Trainium2 MFU below for completeness, the part to focus on is that for ML research ablations, what matters most isn’t a speed-of-light-optimized…"
[^63]: Amazon’s Trainium Takes a Strike at the Training King — "Overall, we liked the user experience, though there were some rough edges that the Amazon team already has on its roadmap to fix."
[^64]: Amazon’s Trainium Takes a Strike at the Training King — "While we will provide the Trainium2 MFU below for completeness, the part to focus on is that for ML research ablations, what matters most isn’t a speed-of-light-optimized stack but decent performance and broad support across model architecture modifications, so researchers can iterate without fighti…"
[^65]: Amazon’s Trainium Takes a Strike at the Training King — "With Neuron’s official TorchTitan image, we were able to launch the run without any issues. We measured 11,099 tokens per second in average training throughput on eager mode, at 23.89% MFU. For compiled mode, we saw 14,156 tokens per second and 30.47% MFU, a 1.28x throughput improvement over eager m…"
[^66]: Amazon’s Trainium Takes a Strike at the Training King — "With Neuron’s official TorchTitan image, we were able to launch the run without any issues."
[^67]: Amazon’s Trainium Takes a Strike at the Training King — "We measured 11,099 tokens per second in average training throughput on eager mode, at 23.89% MFU."
[^68]: Amazon’s Trainium Takes a Strike at the Training King — "For compiled mode, we saw 14,156 tokens per second and 30.47% MFU, a 1.28x throughput improvement over eager mode. We tried changing the model architecture slightly in the modeling code and it worked great also."
[^69]: Amazon’s Trainium Takes a Strike at the Training King — "For compiled mode, we saw 14,156 tokens per second and 30.47% MFU, a 1.28x throughput improvement over eager mode."
[^70]: Amazon’s Trainium Takes a Strike at the Training King — "We tried changing the model architecture slightly in the modeling code and it worked great also."
[^71]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron also offers training recipes for more modern model architectures, so we tested its gpt-oss 20B training recipe. Neuron supports gpt-oss training through integration with GraphTrainer, TorchTitan’s experimental trainer module. Specifically, Neuron adds Trainium-compatible configurations of Sim…"
[^72]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron also offers training recipes for more modern model architectures, so we tested its gpt-oss 20B training recipe."
[^73]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron supports gpt-oss training through integration with GraphTrainer, TorchTitan’s experimental trainer module."
[^74]: Amazon’s Trainium Takes a Strike at the Training King — "Specifically, Neuron adds Trainium-compatible configurations of SimpleFSDP, a compilation backend for PyTorch computation graph capture, and custom NKI kernels for attention and MoE operations."
[^75]: Amazon’s Trainium Takes a Strike at the Training King — "In terms of user experience, the recipe worked out of the box, and everything went well."
[^76]: Amazon’s Trainium Takes a Strike at the Training King — "One thing that was not yet implemented using the upstream APIs was TokenSwitch. In the age of MoE, for inference and training, MoE combine and MoE dispatch are among the most important comms ops and take anywhere from 60-70% of the communication volume, and TokenSwitch is PyTorch’s first-class API f…"
[^77]: Amazon’s Trainium Takes a Strike at the Training King — "One thing that was not yet implemented using the upstream APIs was TokenSwitch. In the age of MoE, for inference and training, MoE combine and MoE dispatch are among the most important comms ops and take anywhere from 60-70% of the communication volume, and TokenSwitch is PyTorch’s first-class API f…"
[^78]: Amazon’s Trainium Takes a Strike at the Training King — "One thing that was not yet implemented using the upstream APIs was TokenSwitch."
[^79]: Amazon’s Trainium Takes a Strike at the Training King — "In the age of MoE, for inference and training, MoE combine and MoE dispatch are among the most important comms ops and take anywhere from 60-70% of the communication volume, and TokenSwitch is PyTorch’s first-class API for them."
[^80]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium doesn’t support it yet and instead relies on a custom TorchTitan class called NeuronEPTokenDispatcher."
[^81]: Amazon’s Trainium Takes a Strike at the Training King — "Moving it onto the TokenSwitch API looks like a simple fix, and the AWS team has committed to collaborating with the Meta PyTorch team to modify the TokenSwitch ABC such that it can support Trainium too."
[^82]: Amazon’s Trainium Takes a Strike at the Training King — "The part where it was slightly disappointing was the Neuron compiler took a long time to compile, leading to a long wait in the first step. Concretely, the first step took 184.6 seconds for eager mode (255.7 seconds for compiled mode), which is 30-55x longer than the average step time, excluding the…"
[^83]: Amazon’s Trainium Takes a Strike at the Training King — "The part where it was slightly disappointing was the Neuron compiler took a long time to compile, leading to a long wait in the first step."
[^84]: Amazon’s Trainium Takes a Strike at the Training King — "Concretely, the first step took 184.6 seconds for eager mode (255.7 seconds for compiled mode), which is 30-55x longer than the average step time, excluding the first step."
[^85]: Amazon’s Trainium Takes a Strike at the Training King — "For gpt-oss, this training run came at a ridiculously high compilation time of 27 minutes and 17 seconds, which leads to a terrible user experience, especially for researchers who experiment with new model architectures."
[^86]: Amazon’s Trainium Takes a Strike at the Training King — "The reason for this is that historically the Trainium compiler stack has mainly been focused on inference, where compile time doesn’t matter because compilation is done offline and cached once per image and doesn’t affect production inference, whereas in training it does."
[^87]: Amazon’s Trainium Takes a Strike at the Training King — "While this is the right call for inference at the time, for researchers iterating on model architecture, that’s a meaningful friction point."
[^88]: Amazon’s Trainium Takes a Strike at the Training King — "The Neuron team is already addressing this directly. Upcoming TorchNeuron releases introduce a new compiler backend with a broad set of precompiled NKI kernels and a compile stack re-architected for fast compilation, targeting up to a 2 orders of magnitude reduction in time-to-first-step for both ea…"
[^89]: Amazon’s Trainium Takes a Strike at the Training King — "The Neuron team is already addressing this directly."
[^90]: Amazon’s Trainium Takes a Strike at the Training King — "Upcoming TorchNeuron releases introduce a new compiler backend with a broad set of precompiled NKI kernels and a compile stack re-architected for fast compilation, targeting up to a 2 orders of magnitude reduction in time-to-first-step for both eager and compiled modes, with minimal or no performanc…"
[^91]: Amazon’s Trainium Takes a Strike at the Training King — "Upcoming TorchNeuron releases introduce a new compiler backend with a broad set of precompiled NKI kernels and a compile stack re-architected for fast compilation, targeting up to a 2 orders of magnitude reduction in time-to-first-step for both eager and compiled modes, with minimal or no performanc…"
[^92]: Amazon’s Trainium Takes a Strike at the Training King — "If they deliver on that, compilation time stops being a conversation."
[^93]: Amazon’s Trainium Takes a Strike at the Training King — "Training MatMul Performance One of the most important things for experimental training is to have decent performance across a broad range of shapes as ML researchers try lots of different things. We benchmarked a single Trainium3 logical core (LNC=2) on the PyTorch nn.functional.linear API to unders…"
[^94]: Amazon’s Trainium Takes a Strike at the Training King — "Training MatMul Performance One of the most important things for experimental training is to have decent performance across a broad range of shapes as ML researchers try lots of different things. We benchmarked a single Trainium3 logical core (LNC=2) on the PyTorch nn.functional.linear API to unders…"
[^95]: Amazon’s Trainium Takes a Strike at the Training King — "One of the most important things for experimental training is to have decent performance across a broad range of shapes as ML researchers try lots of different things."
[^96]: Amazon’s Trainium Takes a Strike at the Training King — "We benchmarked a single Trainium3 logical core (LNC=2) on the PyTorch nn.functional.linear API to understand its matrix multiplication performance, and we compared it with GB300 and B200 for reference. We swept through the matrix shapes of projection operations in major open weight models, and we se…"
[^97]: Amazon’s Trainium Takes a Strike at the Training King — "We benchmarked a single Trainium3 logical core (LNC=2) on the PyTorch nn.functional.linear API to understand its matrix multiplication performance, and we compared it with GB300 and B200 for reference."
[^98]: Amazon’s Trainium Takes a Strike at the Training King — "We swept through the matrix shapes of projection operations in major open weight models, and we set the M dimension to 1, 128, and 2048 to represent different batch size scenarios."
[^99]: Amazon’s Trainium Takes a Strike at the Training King — "In our benchmark, Trainium3 achieved a visibly higher MFU than GB300, starting from the mid-range, where the matrix multiplication performs 1 GFLOP of computation. It was only after 100 GFLOP that GB300 and B200 started outperforming Trainium3, and Trainium3 won again after 1 TFLOP."
[^100]: Amazon’s Trainium Takes a Strike at the Training King — "In our benchmark, Trainium3 achieved a visibly higher MFU than GB300, starting from the mid-range, where the matrix multiplication performs 1 GFLOP of computation."
[^101]: Amazon’s Trainium Takes a Strike at the Training King — "It was only after 100 GFLOP that GB300 and B200 started outperforming Trainium3, and Trainium3 won again after 1 TFLOP."
[^102]: Amazon’s Trainium Takes a Strike at the Training King — "FlexAttention API FlexAttention is a high-level API that allows implementing different attention variants using PyTorch, while offering backward pass auto-generation and reasonable performance. Good FlexAttention support shows a hardware’s flexibility and ease-of-use to researchers. We ran the FlexA…"
[^103]: Amazon’s Trainium Takes a Strike at the Training King — "FlexAttention is a high-level API that allows implementing different attention variants using PyTorch, while offering backward pass auto-generation and reasonable performance. Good FlexAttention support shows a hardware’s flexibility and ease-of-use to researchers. We ran the FlexAttention benchmark…"
[^104]: Amazon’s Trainium Takes a Strike at the Training King — "FlexAttention is a high-level API that allows implementing different attention variants using PyTorch, while offering backward pass auto-generation and reasonable performance."
[^105]: Amazon’s Trainium Takes a Strike at the Training King — "Good FlexAttention support shows a hardware’s flexibility and ease-of-use to researchers."
[^106]: Amazon’s Trainium Takes a Strike at the Training King — "We ran the FlexAttention benchmark suite on Trainium3 to see its FlexAttention support."
[^107]: Amazon’s Trainium Takes a Strike at the Training King — "Overall, Trainium3 passed 89 out of 96 test cases, a 93% pass rate. All 7 failed cases were at large batch size (4) and sequence length (8192), and all failed due to compilation exceeding the time budget rather than numerical errors. These issues will be fixed in later versions of TorchNeuron."
[^108]: Amazon’s Trainium Takes a Strike at the Training King — "Overall, Trainium3 passed 89 out of 96 test cases, a 93% pass rate."
[^109]: Amazon’s Trainium Takes a Strike at the Training King — "All 7 failed cases were at large batch size (4) and sequence length (8192), and all failed due to compilation exceeding the time budget rather than numerical errors."
[^110]: Amazon’s Trainium Takes a Strike at the Training King — "These issues will be fixed in later versions of TorchNeuron."
[^111]: Amazon’s Trainium Takes a Strike at the Training King — "Additionally, we tried implementing custom attention variants not in the FlexAttention benchmark suite for Trainium3, and it matched the numerics of Nvidia GPUs. https://substackcdn.com/image/fetch/$s_!BJnh!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.…"
[^112]: Amazon’s Trainium Takes a Strike at the Training King — "Additionally, we tried implementing custom attention variants not in the FlexAttention benchmark suite for Trainium3, and it matched the numerics of Nvidia GPUs."
[^113]: Amazon’s Trainium Takes a Strike at the Training King — "Automated Quality Assurance SemiAnalysis is known in the global ML community to be the “CI Karen,” setting a high bar across all hardware vendors and doing whatever it takes to get senior leadership of AI chip companies to actually provide their engineers with enough resources and CI fleet to mainta…"
[^114]: Amazon’s Trainium Takes a Strike at the Training King — "Automated Quality Assurance SemiAnalysis is known in the global ML community to be the “CI Karen,” setting a high bar across all hardware vendors and doing whatever it takes to get senior leadership of AI chip companies to actually provide their engineers with enough resources and CI fleet to mainta…"
[^115]: Amazon’s Trainium Takes a Strike at the Training King — "SemiAnalysis is known in the global ML community to be the “CI Karen,” setting a high bar across all hardware vendors and doing whatever it takes to get senior leadership of AI chip companies to actually provide their engineers with enough resources and CI fleet to maintain a high bar of automated q…"
[^116]: Amazon’s Trainium Takes a Strike at the Training King — "One recent achievement, which took over 9 months of fighting with AMD senior leadership, was getting their engineers enough stable nodes to achieve 93% parity on gating test groups. https://substackcdn.com/image/fetch/$s_!jjqT!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsub…"
[^117]: Amazon’s Trainium Takes a Strike at the Training King — "One recent achievement, which took over 9 months of fighting with AMD senior leadership, was getting their engineers enough stable nodes to achieve 93% parity on gating test groups."
[^118]: Amazon’s Trainium Takes a Strike at the Training King — "Inference is a narrow problem. A lab serving a handful of production models needs a forward pass, mostly fixed architectures, and a small set of hot kernels. Training is a generality problem. Each of the thousands of operators needs a backward pass, and research codebases sometimes accidentally run …"
[^119]: Amazon’s Trainium Takes a Strike at the Training King — "Inference is a narrow problem. A lab serving a handful of production models needs a forward pass, mostly fixed architectures, and a small set of hot kernels."
[^120]: Amazon’s Trainium Takes a Strike at the Training King — "Training is a generality problem. Each of the thousands of operators needs a backward pass, and research codebases sometimes accidentally run operators in higher precision, which must also be supported."
[^121]: Amazon’s Trainium Takes a Strike at the Training King — "To ensure that Trainium works across a wide range of model architectures and can do eager mode and compile mode well, AWS collected a giant list of top 100k+ Hugging Face models that spread across a whole range of different normalization, MLP, MoE layouts and attention types. Not only do they test t…"
[^122]: Amazon’s Trainium Takes a Strike at the Training King — "To ensure that Trainium works across a wide range of model architectures and can do eager mode and compile mode well, AWS collected a giant list of top 100k+ Hugging Face models that spread across a whole range of different normalization, MLP, MoE layouts and attention types."
[^123]: Amazon’s Trainium Takes a Strike at the Training King — "Not only do they test that it doesn’t crash, but they also test performance, which ops use CPU fallbacks and don’t have native support yet, where graph breaks are and most importantly, they test numerics against CPU and Nvidia baselines."
[^124]: Amazon’s Trainium Takes a Strike at the Training King — "They test tensor level parity and loss curve divergence also."
[^125]: Amazon’s Trainium Takes a Strike at the Training King — "It is easy to finish an exam within 10 minutes, but it doesn’t matter how fast you finish an exam if you get a 0% on it."
[^126]: Amazon’s Trainium Takes a Strike at the Training King — "Same thing with training stacks. It is easy to get decent MFU%, but it is hard to get decent MFU% while not introducing numeric issues."
[^127]: Amazon’s Trainium Takes a Strike at the Training King — "Although the pass rates aren’t at 100% yet, what matters is the trajectory. AWS is climbing rapidly, with agent swarms systematically fixing the remaining failures. We think it’s a strength that AWS’s internal summary table, the one senior leadership sees, shows gaps transparently rather than hiding…"
[^128]: Amazon’s Trainium Takes a Strike at the Training King — "Although the pass rates aren’t at 100% yet, what matters is the trajectory."
[^129]: Amazon’s Trainium Takes a Strike at the Training King — "AWS is climbing rapidly, with agent swarms systematically fixing the remaining failures."
[^130]: Amazon’s Trainium Takes a Strike at the Training King — "We think it’s a strength that AWS’s internal summary table, the one senior leadership sees, shows gaps transparently rather than hiding them."
[^131]: Amazon’s Trainium Takes a Strike at the Training King — "We say this from experience. When SemiAnalysis and upstream maintainers have tried to fix quality control culture at other hardware vendors, we’ve found that senior leadership is genuinely shocked when shown the real parity pass rates."
[^132]: Amazon’s Trainium Takes a Strike at the Training King — "At one vendor in particular, there was so much middle management filtering that by the time CI numbers reached senior leadership, they showed 99.99%, while the actual gating parity pass rate at the time was below 5%."
[^133]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron Explorer - Better than Nvidia and AMD Profilers Trainium’s profiler is by far leading the industry and is SOTA status. Here we share our initial impressions and plan on sharing our full user experience in a future Trainium kernel article. Trainium’s profiler is loved by all the performance en…"
[^134]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium’s profiler is by far leading the industry and is SOTA status. Here we share our initial impressions and plan on sharing our full user experience in a future Trainium kernel article."
[^135]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium’s profiler is by far leading the industry and is SOTA status."
[^136]: Amazon’s Trainium Takes a Strike at the Training King — "Here we share our initial impressions and plan on sharing our full user experience in a future Trainium kernel article."
[^137]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium’s profiler is loved by all the performance engineers at Anthropic. Anthropic’s head of performance (who is ex-Jane and Finch Street) has publicly said that performance analysis on Trainium is way better than performance analysis on Nvidia GPUs (and obviously better than on AMD GPUs)."
[^138]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium’s profiler is loved by all the performance engineers at Anthropic."
[^139]: Amazon’s Trainium Takes a Strike at the Training King — "Anthropic’s head of performance (who is ex-Jane and Finch Street) has publicly said that performance analysis on Trainium is way better than performance analysis on Nvidia GPUs (and obviously better than on AMD GPUs)."
[^140]: Amazon’s Trainium Takes a Strike at the Training King — "We agree with Tristan Hume. In our experience, the profiling experience was amazing, after getting over the initial hump of the profiling setup being slightly confusing (but not impossible). There are multiple environment variables to set, different file types to save, and various commands to captur…"
[^141]: Amazon’s Trainium Takes a Strike at the Training King — "We agree with Tristan Hume. In our experience, the profiling experience was amazing, after getting over the initial hump of the profiling setup being slightly confusing (but not impossible)."
[^142]: Amazon’s Trainium Takes a Strike at the Training King — "There are multiple environment variables to set, different file types to save, and various commands to capture and view the profile traces."
[^143]: Amazon’s Trainium Takes a Strike at the Training King — "This is only the kernel profiling setup, and the PyTorch profiling setup is similar but with slight differences, making things even more confusing."
[^144]: Amazon’s Trainium Takes a Strike at the Training King — "With the help of Codex (since Claude refuses to write Trainium kernels), our best effort working setup is as follows:"
[^145]: Amazon’s Trainium Takes a Strike at the Training King — "Launch a persistent Neuron Explorer server"
[^146]: Amazon’s Trainium Takes a Strike at the Training King — "Profile the kernel with neuron-explorer capture command"
[^147]: Amazon’s Trainium Takes a Strike at the Training King — "Upload the profile trace as an artifact to the Neuron Explorer server as a web request"
[^148]: Amazon’s Trainium Takes a Strike at the Training King — "We shared feedback with AWS that we wished the documentation could be clearer on the workflow, explaining what environment variables need to be set for what reasons, and what purpose each file type serves."
[^149]: Amazon’s Trainium Takes a Strike at the Training King — "Once the setup is done, the profiler user experience is great. Neuron Explorer is co-designed with the hardware. We particularly like the timeline separating hardware units in different rows, so that bubbles are visible at a glance. In contrast, GPU programmers have to roll their own setup for intra…"
[^150]: Amazon’s Trainium Takes a Strike at the Training King — "Once the setup is done, the profiler user experience is great."
[^151]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron Explorer is co-designed with the hardware."
[^152]: Amazon’s Trainium Takes a Strike at the Training King — "We particularly like the timeline separating hardware units in different rows, so that bubbles are visible at a glance."
[^153]: Amazon’s Trainium Takes a Strike at the Training King — "In contrast, GPU programmers have to roll their own setup for intra-SM profiling as the official Nsight tools don’t support that."
[^154]: Amazon’s Trainium Takes a Strike at the Training King — "We also like how the viewer visualizes dependencies. When a block is selected, its dependencies and dependents light up in different colors, which helps us reason about work overlapping, e.g. whether computation sufficiently overlaps with memory loading. The image below shows that the selected white…"
[^155]: Amazon’s Trainium Takes a Strike at the Training King — "We also like how the viewer visualizes dependencies."
[^156]: Amazon’s Trainium Takes a Strike at the Training King — "When a block is selected, its dependencies and dependents light up in different colors, which helps us reason about work overlapping, e.g. whether computation sufficiently overlaps with memory loading."
[^157]: Amazon’s Trainium Takes a Strike at the Training King — "The image below shows that the selected white block is:"
[^158]: Amazon’s Trainium Takes a Strike at the Training King — "Flow-dependent on the red block"
[^159]: Amazon’s Trainium Takes a Strike at the Training King — "Order-dependent on the orange block"
[^160]: Amazon’s Trainium Takes a Strike at the Training King — "A flow dependency of the blue block"
[^161]: Amazon’s Trainium Takes a Strike at the Training King — "An output dependency of the purple block"
[^162]: Amazon’s Trainium Takes a Strike at the Training King — "Trainium Profiler Demo - Pixel Art Neuron Explorer has many more features, including code editor mapping, MFU estimation, memory usage, and even creating pixel art due to how precise the profiler is. The images below are all from profiler traces of running on actual Trainium hardware, not fake profi…"
[^163]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron Explorer has many more features, including code editor mapping, MFU estimation, memory usage, and even creating pixel art due to how precise the profiler is. The images below are all from profiler traces of running on actual Trainium hardware, not fake profile reports."
[^164]: Amazon’s Trainium Takes a Strike at the Training King — "Neuron Explorer has many more features, including code editor mapping, MFU estimation, memory usage, and even creating pixel art due to how precise the profiler is."
[^165]: Amazon’s Trainium Takes a Strike at the Training King — "The images below are all from profiler traces of running on actual Trainium hardware, not fake profile reports."
[^166]: Amazon’s Trainium Takes a Strike at the Training King — "We were mainly inspired by the Bad Apple post from Daniel Liu (Anthropic Performance Engineer) and have created our own agentic coding SKILL.md for creating images. We did not have the time yet to create one to automatically generate videos frame by frame but will in the future and open source this …"
[^167]: Amazon’s Trainium Takes a Strike at the Training King — "We were mainly inspired by the Bad Apple post from Daniel Liu (Anthropic Performance Engineer) and have created our own agentic coding SKILL.md for creating images."
[^168]: Amazon’s Trainium Takes a Strike at the Training King — "We did not have the time yet to create one to automatically generate videos frame by frame but will in the future and open source this SKILL.md for everyone to use."
[^169]: Amazon’s Trainium Takes a Strike at the Training King — "We mainly generate this pixel art by using the 16 DMA engines per physical core by “coloring in” regions by turning the DMA engines active, and the width of the shaded area is determined by how much data we have each DMA engine move."
[^170]: Amazon’s Trainium Takes a Strike at the Training King — "Since AWS is a partner of Nvidia, Jensen should tell his engineers to book a meeting with the AWS Trainium team on the hardware features needed to do accurate fine-grained profiling such that Nvidia can learn how to add this capability to Feynman or Feynman-Next GPUs. https://substackcdn.com/image/f…"
[^171]: Amazon’s Trainium Takes a Strike at the Training King — "Since AWS is a partner of Nvidia, Jensen should tell his engineers to book a meeting with the AWS Trainium team on the hardware features needed to do accurate fine-grained profiling such that Nvidia can learn how to add this capability to Feynman or Feynman-Next GPUs."
[^172]: Amazon’s Trainium Takes a Strike at the Training King — "Nvidia’s intra-kernel profiler Nsight Compute employs a different design. It offers aggregate metrics and detailed information on performance properties, rather than an event-based timeline viewer. The closest thing we found was Tri Dao’s QuACK intra-kernel profiler, which uses Nvidia’s In-Kernel Ev…"
[^173]: Amazon’s Trainium Takes a Strike at the Training King — "Nvidia’s intra-kernel profiler Nsight Compute employs a different design. It offers aggregate metrics and detailed information on performance properties, rather than an event-based timeline viewer."
[^174]: Amazon’s Trainium Takes a Strike at the Training King — "Nvidia’s intra-kernel profiler Nsight Compute employs a different design."
[^175]: Amazon’s Trainium Takes a Strike at the Training King — "It offers aggregate metrics and detailed information on performance properties, rather than an event-based timeline viewer."
[^176]: Amazon’s Trainium Takes a Strike at the Training King — "The closest thing we found was Tri Dao’s QuACK intra-kernel profiler, which uses Nvidia’s In-Kernel Event Tracing API. While QuACK requires custom design to make Perfetto visualize accordingly, it’s great to see that AWS made this a well-integrated, first-class experience in Neuron Explorer."
[^177]: Amazon’s Trainium Takes a Strike at the Training King — "The closest thing we found was Tri Dao’s QuACK intra-kernel profiler, which uses Nvidia’s In-Kernel Event Tracing API."
[^178]: Amazon’s Trainium Takes a Strike at the Training King — "While QuACK requires custom design to make Perfetto visualize accordingly, it’s great to see that AWS made this a well-integrated, first-class experience in Neuron Explorer."
