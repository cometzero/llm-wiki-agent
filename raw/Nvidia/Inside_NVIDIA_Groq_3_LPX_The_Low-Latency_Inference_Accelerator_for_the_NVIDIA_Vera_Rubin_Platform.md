[NVIDIA Groq 3 LPX](https://www.nvidia.com/en-us/data-center/lpx/)는 [NVIDIA Vera Rubin platform](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)을 위한 새로운 rack-scale inference accelerator로, agentic 시스템이 요구하는 low-latency와 large-context 워크로드를 겨냥해 설계되었습니다. [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)와 함께 co-design된 LPX는 빠르고 예측 가능한 token generation에 최적화된 엔진으로 [AI factory](https://www.nvidia.com/en-us/glossary/ai-factory/)를 보강합니다. 반면 Vera Rubin NVL72는 여전히 유연하고 범용적인 워크호스 역할을 유지하면서 학습과 inference에서 높은 throughput을 제공하며, prefill과 decode 전반(장문 맥락 처리, decode attention, 대규모 동시성 serving 포함)에서 성능을 담당합니다.  

이 조합이 중요한 이유는, agentic 미래에서는 더 높은 형태의 inference가 필요하기 때문입니다. 사용자당 초당 token 생성 속도가 1,000 tokens/sec 수준에 접근하면, 모델은 단순 대화형 상호작용을 넘어 thinking-speed 상호작용에 가까워집니다. 이 속도에서는 AI가 reasoning, simulation, response를 연속적으로 수행할 수 있어, turn-based chat보다 실시간 협업에 가까운 사용자 경험이 가능해집니다.  

이러한 전환은 [multi-agent](https://www.nvidia.com/en-us/glossary/ai-agents/) 환경의 상한도 함께 끌어올립니다. 개별 agent는 강력할 수 있지만, 협업하는 agent 집단은 훨씬 더 큰 성과를 낼 수 있습니다. 이는 인간 사회가 집단 지성으로 능력을 배가시키는 것과 유사합니다.  

이처럼 떠오르는 워크로드를 뒷받침하려면 높은 throughput과 낮은 latency를 동시에 만족하는 인프라가 필요합니다. Vera Rubin NVL72와 LPX의 조합은 바로 이러한 heterogeneous architecture를 가능하게 하여, AI factory 수준의 대규모 성능과 계속 실행되는 agentic 시스템 및 차세대 AI 애플리케이션을 구동하는 데 필요한 빠른 token generation을 한 구조 안에서 제공합니다.  

## NVIDIA Groq 3 LPX 소개[](#introducing_nvidia_groq_3_lpx )

Vera Rubin과 LPX는 Rubin GPU와 LPU의 극한 성능을 결합해 최대 35배 높은 inference throughput per megawatt, 그리고 1조 파라미터급 모델 기준 최대 10배 이상의 revenue opportunity를 제공합니다. NVIDIA [MGX ETL rack architecture](https://www.nvidia.com/en-us/data-center/products/mgx/)에 통합되고 넓은 Vera Rubin platform과 정합된 LPX는 데이터 센터가 하나의 공통 인프라 설계 안에서 Vera Rubin NVL72와 함께 전용 low-latency inference 경로를 배치할 수 있게 합니다.  

이 시스템은 256개의 상호 연결된 NVIDIA Groq 3 LPU accelerator를 중심으로 구성됩니다. 아키텍처는 결정론적 실행, 칩 내 SRAM 대역폭 극대화, 그리고 긴밀히 조율된 scale-up 통신을 강조해 동시 접속 수가 증가하고 request shape가 변해도 interactive inference의 응답성이 유지되도록 설계되었습니다.  

Vera Rubin NVL72와 함께 배치될 경우 LPX는 decode loop에서 FFN과 MoE expert 실행 같은 latency-sensitive 부분을 가속하고, Rubin GPU가 prefill과 decode attention을 계속 처리합니다. 두 하드웨어가 결합하면 AI factory throughput을 희생하지 않고도 interactive responsiveness를 개선하는 heterogeneous serving path를 형성합니다.  

![NVIDIA Groq 3 LPX의 랙 규모 시스템. 사이드 표에는 256개 Groq 3 LP30 칩, 40 PB/s 칩 내 SRAM 대역폭, 640 TB/s 스케일업 대역폭, 총 128 GB SRAM 용량, FP8 compute 315 PFLOPS 등 핵심 사양이 정리되어 있다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/Groq-3-LPX.webp)  

*그림 1. NVIDIA Groq 3 LPX 랙 규모 시스템*

랙 단위 규모에서 LPX가 제공하는 사양은 다음과 같습니다.

<table><tbody><tr><td><strong>사양(Specification)</strong></td><td><strong>NVIDIA Groq 3 LPX</strong></td></tr><tr><td>AI inference compute</td><td>315 PFLOPS</td></tr><tr><td>총 SRAM 용량</td><td>128 GB</td></tr><tr><td>칩 내 SRAM 대역폭</td><td>40 PB/s</td></tr><tr><td>스케일업 밀도</td><td>256 chips</td></tr><tr><td>스케일업 대역폭</td><td>640 TB/s</td></tr></tbody></table>

*표 1. NVIDIA Groq 3 LPX 사양*

Vera Rubin NVL72와 LPX는 AI factory를 위한 더욱 이질적(hybrid)인 inference architecture를 만듭니다. 즉, 높은 aggregate token 생산량과 반응형 interactive AI 경험을 동시에 지원합니다.  

### NVIDIA Groq 3 LPX compute tray 내부[](#inside_the_nvidia_groq_3_lpx_compute_tray)

LPX rack-scale accelerator에는 32개의 liquid-cooled 1U compute tray가 들어 있으며, 각 tray는 대규모 low-latency inference를 위해 설계되었습니다. 각 tray는 8개의 LPU accelerator, host processor, fabric expansion logic을 통합해 케이블이 없는(cableless) 구조로 구성되어 있어 rack-scale 배포가 단순화되며 compute와 communication이 긴밀히 결합됩니다.  

LPU chip-to-chip (C2C) 링크는 tray 내 직접 통신, tray 간 LPU C2C spine 통신, rack 간 통신을 지원합니다. interactive inference는 단순 계산량만이 아니라, 장치 간 데이터 이동 효율, 작업 협업 방식, 요청이 확산되며 생기는 지연 편차(가변 지연)를 얼마나 줄이느냐도 성능에 큰 영향을 주기 때문에 이 연결성이 중요합니다.  

![케이블이 없는 liquid-cooled 1U NVIDIA Groq 3 LPX compute tray. 8개의 Groq 3 LPU 모듈이 tray 내 Fabric Expansion Logic, DRAM, Host CPU, BlueField-4 DPU, backplane, front panel과 연결된 구조를 보여준다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/LPX02-Groq3LPX_Compute_Tray.webp)  

*그림 2. NVIDIA Groq 3 LPX compute tray와 모듈*

각 tray가 제공하는 자원은 다음과 같습니다.

<table><tbody><tr><td><strong>자원(Resource)</strong></td><td><strong>tray당</strong></td></tr><tr><td>LP30 chips</td><td>8</td></tr><tr><td>칩 내 SRAM</td><td>4 GB</td></tr><tr><td>SRAM 대역폭</td><td>1.2 PB/s</td></tr><tr><td>fabric expansion logic을 통한 DRAM</td><td>최대 256 GB</td></tr><tr><td>host CPU를 통한 DRAM</td><td>최대 128 GB</td></tr><tr><td>AI inference compute (FP8)</td><td>9.6 PFLOPS</td></tr><tr><td>스케일업 대역폭</td><td>20 TB/s</td></tr></tbody></table>

*표 2. NVIDIA Groq 3 LPX compute tray 사양*

시스템 관점에서 LPX는 coordination overhead와 jitter가 사용자에게 바로 드러나는 inference 환경을 대상으로 설계되었습니다. 이는 오프라인 또는 throughput 중심 serving에서 interactive generation 중심 serving으로 이동하는 AI application이 늘어나는 현재 특히 중요합니다. LPX가 어떤 방식으로 이런 영역에 최적화되는지 이해하려면, 이 시스템의 핵심 프로세서인 NVIDIA Groq 3 LPU의 아키텍처를 봐야 합니다.  

### NVIDIA Groq 3 LPU의 첫 번째 아키텍처 관찰: Vera Rubin Platform의 일곱 번째 칩[](#first_look_at_the_architecture_of_the_nvidia_groq_3_lpu—the_seventh_chip_of_the_vera_rubin_platform)

LPX의 핵심은 NVIDIA Groq 3 LPU입니다. 이 칩은 compute, memory, communication을 compiler가 통제하는 방식으로 결합해 빠르고 예측 가능한 token generation을 만들도록 설계되었습니다. LPU 아키텍처는 또한 정확히 동일한 목표로, 높은 peak arithmetic throughput만 최적화하기보다 deterministic execution, 칩 내 높은 메모리 대역폭, 명시적 데이터 이동을 강조합니다. 이러한 특성은 decode-dominant이면서 latency-sensitive한 inference 환경에서 특히 중요합니다.  

![NVIDIA Groq 3 LPU의 단순화된 구조도. compute, memory, control, chip-to-chip 통신 블록을 보여주며 tensor-first compute, 높은 SRAM 대역폭, 직접 chip-to-chip interconnect를 강조한다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/Groq-3-Architecture.webp)  

*그림 3. NVIDIA Groq 3 LPU 칩 아키텍처*

#### Tensor-first compute와 explicit data movement

Compute와 communication은 LPU에서 320-byte vector를 작업 단위로 묶어 구성됩니다. 산술 연산, 메모리 접근, 장치 간 전송 모두 이 고정 크기 벡터 단위를 사용해 scheduling과 동기화를 단순화합니다.  

특화된 실행 모듈은 다음과 같은 연산 유형을 분리해 처리합니다.

+   **Matrix execution modules (MXM)**: 텐서 연산용 dense multiply-accumulate를 제공하며, 고정된 데이터 타입으로 예측 가능한 throughput을 유지합니다.
+   **Vector execution modules (VXM)**: pointwise arithmetic, type conversion, activation function을 처리하며 lane당 여러 ALU로 구성된 mesh 방식으로 동작합니다.
+   **Switch execution modules (SXM)**: 순열, 회전, 분배, 전치(transposition) 등 구조화된 데이터 이동을 수행합니다.

LPU는 데이터 이동을 explicit하고 programmable하게 만들어 하드웨어 휴리스틱에 의존하지 않고 memory access, compute, communication을 겹쳐 동작(overlap)할 수 있게 합니다.  

#### MEM가 극한의 on-chip 메모리 대역폭을 제공하는 방식

LPU의 핵심 요소는 MEM 블록입니다. MEM는 flat하고 SRAM-first한 구조로, 500 MB의 고속 on-chip SRAM을 inference의 주된 working storage로 사용합니다. 하드웨어가 관리하는 cache에 의존하지 않고, compiler와 runtime이 active working set(가중치, activation, KV state 포함)을 on-chip memory로 배치해 데이터를 명시적으로 이동시킵니다. 이 방식은 예측 불가능한 stall을 줄이고 latency-sensitive한 데이터는 compute에 최대한 근접한 위치에 유지해 낮고 안정적인 latency를 만들어 냅니다.  

on-chip SRAM 용량은 유한하므로, 더 큰 모델은 layer-wise partitioning 같은 병렬 실행 전략으로 여러 LPU accelerator에 분산됩니다. 이때 전체 시스템은 훨씬 더 큰 유효 작업 집합을 제공합니다. 이 설계에서는 peak arithmetic throughput보다 compute를 꾸준히 feed할 수 있느냐가 성능을 좌우하므로, LPX는 LPU당 150 TB/s의 on-chip memory bandwidth와 높은 C2C scale-up 대역폭을 결합합니다.  

#### 예측 가능한 통신을 갖춘 C2C 스케일링

여러 장치로 inference를 확장하기 위해 LPU는 deterministic한 데이터 교환을 위해 high-radix, high-speed C2C 링크를 탑재합니다. 각 LPU는 96개의 C2C 링크(각 112 Gbps)를 통해 연결되며, LPX 전체 scale-up 토폴로지를 단순화하고 총 I/O 양방향 대역폭 2.5 TB/s와 예측 가능한 통신 타이밍을 제공합니다. 분산된 inference 파이프라인에서 통신 오버헤드는 큰 latency 원인이 될 수 있어, 이는 특히 중요합니다.  

#### deterministic하고 compiler가 오케스트레이션하는 실행

LPU는 Groq의 spatial execution model을 기반으로, compiler가 계산, 데이터 이동, 동기화를 명시적으로 스케줄합니다. 실행 시점에 dynamic hardware scheduler에 맡기지 않고, 하드웨어 수준의 plesiosynchronous chip-to-chip protocol로 자연적인 clock drift를 상쇄해 수백 개 LPU를 단일 조정된 시스템처럼 동작시킵니다. 데이터 도착 시점이 예측 가능하고 주기적으로 software sync를 수행하면 개발자는 타이밍을 더 직접적으로 reasoning할 수 있으며, compute와 network 동작 모두 determinism이 높아집니다.  

이 실행 모델은 다음을 가능하게 합니다.

+   메모리와 compute의 정밀한 협조
+   명시적 instruction timing 제어
+   가변 워크로드에서 줄어든 execution jitter  

실시간 inference에서 이 deterministic 특성은 소량 배치 환경에서도 time-to-first-token과 per-token latency를 안정적으로 유지하는 데 기여합니다.  

## interactive inference로의 전환[](#the_shift_toward_interactive_inference)

AI inference는 넓은 성능 스펙트럼을 가집니다. 한쪽에는 배치 문서 처리, moderation, embedding, media pipeline처럼 throughput-optimized 서비스가 있고, 이들은 GPU당 토큰, watt당 토큰, 비용 효율을 최대로 하는 것이 목적입니다. 이러한 워크로드는 일반적으로 large-scale shared service(예: free-tier/background AI)에서 높은 이용률이 더 중요합니다.  

다른 한쪽에는 coding assistants, chatbots, voice assistants, copilots, interactive agents처럼 latency-optimized 서비스가 있습니다. 이쪽은 지연이 사용자에게 바로 체감되므로 time-to-first-token, tokens per second per user, tail latency가 핵심 지표가 됩니다. 현대의 AI 플랫폼은 두 영역을 동시에 지원해야 하는 경우가 많아, 큰 처리량을 처리하는 backends와 반응형 interactive 경험을 동시에 운영합니다. 이 분기점 때문에 heterogeneous inference architecture의 중요성이 커집니다.  

### interactive inference가 어려운 이유[](#what_makes_interactive_inference_harder)

표 3에서 보듯, 더 긴 출력과 커지는 context window는 워크로드를 decode 중심으로 이동시켜 token이 순차적으로 생성되기 시작하고, 사용자에게는 응답성이 직접적으로 노출됩니다. 이를 통해 low-latency interactive inference의 중요성이 커지는 동시에 효율적 제공은 어려워지고 있습니다.  

<table><tbody><tr><td><strong>요인</strong></td><td><strong>중요한 이유</strong></td></tr><tr><td><strong>제품 속성으로서의 low-latency</strong></td><td>interactive 응용에서 responsiveness는 더 이상 인프라 지표가 아니라, 사용자가 제품을 평가하는 요소 자체가 됩니다.</td></tr><tr><td><strong>더 긴 reasoning output</strong></td><td>모델이 더 긴 output을 생성하고 multi-step chains of thought를 수행할수록, 요청의 비중이 순차적 token generation이 많은 decode 구간으로 이동합니다.</td></tr><tr><td><strong>Prefix caching</strong></td><td>공유 프롬프트 상태 재사용은 prefill 비용을 줄여주지만, 요청별 decode 작업의 상대 비중을 높여 해당 부분을 더 빨리 서비스해야 합니다.</td></tr><tr><td><strong>긴 context</strong></td><td>context가 길어질수록 Transformer self-attention이 데이터 이동과 memory bandwidth 제약을 점점 더 많이 받게 됩니다.</td></tr></tbody></table>

*표 3. 전통적 serving 방식이 low-latency inference에 덜 효과적인 네 가지 요인*

동시에, 긴 context는 memory bandwidth와 데이터 이동 압력을 높이고, 동시 사용자 수 증가로 throughput 중심 시스템이 의존하던 배치 효율이 떨어집니다. 결과적으로 aggregate throughput 최적화 시스템이 각 요청마다 빠르고 예측 가능한 token 생성이 필요한 워크로드에 항상 최적은 아닙니다.  

이 어려움은 agentic AI에서 더 커집니다. agentic AI는 inference, retrieval, tool use, reasoning을 반복 순환하기 때문입니다. 각 단계마다 지연이 누적되며, 안정적인 per-token 성능과 좋은 tail-latency 동작이 인터랙티브 사용자 경험에서 필수입니다.  

### agentic inference 시대, 새로운 아키텍처가 필요한 이유[](#the_era_of_agentic_inference_requires_a_new_architecture)

inference는 하나의 균일한 workload가 아닙니다. 한 요청 안에서도 prefill과 decode가 서로 다른 하드웨어 요구를 만들고, batch size, context length, 모델 구조가 바뀌면 그 요구도 이동합니다. self-attention이나 sparse MoE 같은 일부 단계는 memory bandwidth와 데이터 이동에 매우 민감해지고, 반대로 dense projection과 feed-forward layer는 충분한 parallelism이 있으면 throughput-optimized hardware에서 효율적으로 확장됩니다. interactive decode에서는 배치 크기가 작은 경우가 많아 stall, contention, jitter에 훨씬 민감해집니다.  

전체 파이프라인을 하나의 regime에만 맞추면 항상 타협이 발생합니다. 대량 배치에서 peak throughput 중심으로 튜닝된 하드웨어는 지연 민감 경로에 적합하지 않을 수 있고, 반대로 latency 최적화 하드웨어는 가장 compute-heavy 단계에서 효율이 떨어질 수 있습니다.  

그림 4에서 보듯 heterogeneous system은 두 방식을 결합해 low-latency interactive performance와 높은 AI factory throughput를 동시에 가져옵니다. 결국 두 엔진 구조가 됩니다. GPU는 context-heavy prefill 및 decode attention에서 높은 출력을 내고, LPUs는 FFN/MoE 같은 latency-sensitive decode 구성요소를 가속합니다. 두 엔진을 함께 쓰면 AI factory throughput을 희생하지 않고 상호작용성을 높일 수 있습니다.  

![개념도: throughput-optimized hardware, low-latency hardware, 그리고 heterogeneous 조합이 AI factory throughput과 interactive responsiveness 간 trade-off에서 차지하는 영역을 보여준다.](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201600%20937%22%3E%3C/svg%3E)  

*그림 4. Heterogeneous inference는 Pareto frontier를 확장한다*

## Vera Rubin NVL72과 LPX의 결합[](#vera_rubin_nvl72_meets_lpx)

현대 inference는 계주(running relay race)와 유사합니다. 같은 하드웨어가 무거운 context 구간을 처리한다고 해서 다음 token 생성 구간의 스프린트까지 모두 맡을 필요는 없습니다. Rubin GPU는 학습과 inference 모두에서 유연하고 범용적인 workhorse입니다. 긴 context prefill부터 decode attention, 대규모 동시 추론까지 다양한 모델 크기와 배치 regime에서 높은 throughput을 제공합니다.  

LPX는 빠르고 latency-sensitive한 token 생성을 위한 특화 경로를 추가합니다. 두 하드웨어를 함께 쓰면 system-scale 효율을 유지하면서도 interactive responsiveness를 높이는 heterogeneous inference design이 완성됩니다.  

![NVIDIA Rubin GPU와 Groq 3 LPU 비교도. Rubin의 높은 FLOPS와 대용량 HBM memory, 그리고 Groq 3 LPU의 low-latency inference에 최적화된 고대역폭 on-chip SRAM을 대비한다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/LPX05-Rubin_GPU_and_Groq_3_LPU.webp)  

*그림 5. 극한 FLOPS를 제공하는 Rubin GPU와 bandwidth 중심의 Groq 3 LPU 결합*

### Decode 단계: 반복적인 multi-engine 루프[](#decode_phase_a_repeated_multi-engine_loop)

prefill 단계는 대용량 입력을 수집해 KV cache를 구성하는 작업이 주가 되며, 이는 높은 parallel compute와 큰 memory capacity를 활용하는 workload입니다. Vera Rubin NVL72는 특히 long-context workload와 context가 크고 변동이 큰 MoE 모델에서 이 단계를 효율적으로 처리합니다.  

decode는 구조가 다릅니다. decode는 반복적인 token-by-token loop이며, loop의 서로 다른 구간이 서로 다른 병목을 만듭니다. Vera Rubin platform architecture에서 LPX를 함께 사용하면 decode를 two-engine loop로 보는 것이 적합합니다. GPU는 accumulated KV cache 전체 context에 대한 attention처럼 throughput과 큰 memory capacity의 이점을 살리는 작업을 담당하고, LPX는 sparse MoE expert feed-forward network(FFN)와 다른 pointwise 연산 같은 latency-sensitive 연산을 가속합니다. 이 분할은 종종 decode phase disaggregation 또는 attention–FFN disaggregation(AFD)이라 불리며, decode 내부에서 attention과 FFN을 분리해 각 토큰마다 중간 활성값(intermediate activation)을 교환합니다. 결과적으로 각 엔진이 최적화된 부분만 처리해 loop를 더 효율적으로 실행합니다. 이 AFD loop는 Pareto frontier의 고부가가치 operating region을 확장합니다.  

![decode를 두 엔진 루프로 표현한 도식: Rubin GPU가 KV cache 기반 attention을 처리하고 LPUs가 feed-forward/MoE layer를 수행한다. 각 토큰마다 intermediate activation(임시 텐서 상태)을 교환해 latency와 throughput을 개선한다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/Decode-Loop.webp)  

*그림 6. AFD decode 동작 설명*

rack 규모 이상으로 확대될 때 LPX는 하나의 정밀하게 조정된 compute 단위로 동작하도록 설계되어 coordination overhead를 줄이고 jitter를 낮춥니다. 이는 small delay가 많은 model call과 검증 루프를 통해 누적되는 decode-heavy, agentic workflow에서 특히 유용합니다.  

### NVIDIA Dynamo가 heterogeneous decode를 운영 가능한 형태로 만드는 방식[](#nvidia_dynamo_makes_heterogeneous_decode_operational)

heterogeneous decode를 실서비스로 구현하려면 요청을 분류하고 latency 목표에 따라 라우팅하며, 오버헤드가 낮은 방식으로 intermediate activation을 이동시키고, 버스트성·가변 트래픽에서 tail latency를 안정적으로 유지하는 소프트웨어가 필요합니다. [NVIDIA Dynamo](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/)는 이 오케스트레이션 레이어를 담당하며, 이기종 백엔드 간의 disaggregated serving과 disaggregated decode를 조율합니다.  

실제 동작에서는 Dynamo가 prefill을 GPU 워커로 라우팅해 대규모 context를 처리하고 KV cache를 생성합니다. decode 단계에서는 Dynamo가 AFD loop를 오케스트레이션해 GPU가 accumulated KV cache에 대한 attention을 수행하고, 중간 활성값(intermediate activation)을 LPUs로 넘겨 FFN/MoE를 실행한 뒤, 결과를 다시 GPU로 반환해 token 생성을 계속 진행합니다. 이 구조는 AI factory throughput을 유지하면서 tail latency가 더 예측 가능한 단일 serving path를 구현합니다.  

![NVIDIA Dynamo가 두 랙 간 heterogeneous inference를 조정하는 도식. VR NVL72 GPU가 prefill로 대규모 context를 처리해 KV cache를 만든 뒤, decode에서는 GPU가 KV cache attention을 수행하고 LPX가 FFN/MoE를 실행한다. 양측은 반복 루프에서 중간 decode activation을 교환해 토큰을 생성한다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/LPX07-NVIDIA_Dynamo_Orchestrates_Disagg_Compute.webp)  

**그림 7. Dynamo의 heterogeneous compute 오케스트레이션**

KV-aware routing, 저오버헤드 전송, latency target 기반 스케줄링을 통해 Dynamo는 interactive session이 긴 대기열에 묶이지 않도록 하고, tenant 간 jitter를 줄이며, 동시성 및 요청 형태 변화에도 tail latency를 안정적으로 유지합니다. 결과적으로 고확장 환경에서 반응형 사용자 경험을 유지하면서도 높은 AI factory throughput을 지속하는 production-ready heterogeneous serving 모델이 완성됩니다.  

### LPX로 speculative decoding 가속하기[](#accelerating_speculative_decoding_with_lpx)

[Speculative decoding](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)은 LLM inference latency를 줄이기 위해 점차 중요해진 기법입니다. 이 방식은 작은 draft model이 여러 후보 토큰을 미리 생성하고, 더 큰 target model이 이를 병렬로 검증해 일치하면 한 번에 여러 토큰을 확정합니다. 따라서 유효 토큰당 처리량이 크게 늘고 응답 지연이 줄어듭니다.  

LPX는 이 아키텍처에서 draft-generation 엔진으로 적합합니다. LPU의 deterministic execution model과 극도의 높은 on-chip SRAM bandwidth가 매우 빠른 draft token 생성을 가능하게 해, draft model이 verifier보다 앞서 실행될 수 있습니다. 동시에 Rubin 같은 GPU는 prefill, attention 처리, token verification 같은 대형 모델 작업에서 높은 효율을 유지합니다.  

두 장치를 결합하면 장점이 극대화됩니다.

+   LPX는 low-latency 아키텍처로 draft token을 신속하게 생성합니다.
+   Rubin GPU는 throughput이 높은 compute와 큰 memory capacity를 활용해 토큰을 효율적으로 검증·확정합니다.

이렇게 분리하면 speculative decoding을 동일 하드웨어에서 draft와 verifier를 함께 돌리는 대신, 서로 다른 processor에서 나눠 수행할 수 있습니다. 그 결과 draft 생성 속도는 빨라지면서도 GPU 기반 검증 효율은 유지됩니다.  

![Speculative decoding 동작 도식: LPX에서 실행된 draft 모델이 생성한 토큰을 GPU target 모델이 검증한다. 검증이 통과한 여러 토큰을 한 단계에서 반영해 추론 지연을 낮춘다.](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201600%20743%22%3E%3C/svg%3E)  

*그림 8. GPU 검증과 LPU draft 생성으로 수행하는 speculative decoding*

## 지능형 agentic 스웜을 여는 길[](#unlocking_intelligent_agentic_swarms)

AI 사용 사례가 단순한 chat, 배치 추론에서 multi-step agentic workflow로 진화하면서 responsiveness 자체가 필수 요건이 됩니다. 오프라인 추론이나 기본 assistant는 종종 aggregate throughput에 더 초점을 둘 수 있지만, interactive application, deep research, agentic pipeline은 고토큰량과 촘촘한 feedback loop를 결합합니다. 이때 latency는 여러 model call과 tool interaction을 거치며 누적됩니다.  

이 시나리오에서 heterogeneous inference의 가치가 분명해집니다. 긴 context 처리용 고처리량 엔진과 decode FFN용 저지연 엔진을 결합하면 AI factory output을 희생하지 않고 사용자 interactivity를 높일 수 있습니다.  

![AI가 오프라인 추론과 단순 챗봇에서 reasoning workflow, 코딩 어시스턴트, 자율 멀티에이전트 시스템으로 발전함에 따라 interactivity가 올라갈수록 compute 요구량이 커지는 추세를 보여준다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/Agentic-Scaling.webp)  

*그림 9. AI 워크로드별 compute 및 interactivity 요구량 비교: agentic swarm을 위해 높은 throughput과 low-latency가 모두 필요함을 강조*

### Pareto frontier에서 새로운 AI 경험 범주를 여는 방법[](#unlocking_a_new_category_of_ai_experiences_on_the_pareto_frontier)

성능과 비용 간의 tradeoff를 가시화하는 실용적인 방법 중 하나가 [Pareto frontier](https://blogs.nvidia.com/blog/revenue-potential-ai-factories/)입니다. 여기서 가로축은 사용자 interactivity를 나타내는 tokens per second per user(TPS per user), 세로축은 AI factory throughput인 tokens per second per megawatt(TPS per MW)입니다.  

그림 10에서 보듯 서로 다른 AI 서비스는 이 곡선의 서로 다른 위치에서 동작합니다. throughput-first 서비스(예: 많은 free-tier, background workload)는 대부분 효율과 높은 utilization을 우선하며, 종종 작은 모델과 짧은 context window를 사용합니다. 반면 premium AI 서비스는 높은 모델 역량과 사용자에게 직접 체감되는 응답성을 요구합니다. 특히 long-context reasoning과 agentic workflow에서 그러합니다. 그림 10의 premium tier는 400K input context window를 가진 2-trillion-parameter MoE 모델이 사용자당 약 400 TPS 수준으로 동작하는 구간으로 설명됩니다.  

![AI factory 효율(TPS/MW)과 interactivity(사용자당 TPS)를 비교한 차트. 사용자당 400 TPS 구간에서 Vera Rubin NVL72+Groq 3 LPX 조합이 Grace Blackwell NVL72 대비 35배 높은 throughput을 유지함을 보여준다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/Pareto.webp)  

*그림 10. Vera Rubin NVL72와 Groq 3 LPX가 여는 새로운 AI 경험 카테고리*

단일 homogeneous 플랫폼으로 premium operating point를 달성하려 하면, 서로 다른 성능 regime이 같은 serving pipeline 안에 섞여 있어 responsiveness와 전체 AI factory throughput 간 반드시 tradeoff가 생깁니다. heterogeneous architecture는 상호 보완적인 실행 경로를 결합해 이 한계를 확장시키고, 높은 factory output을 유지한 채 반응형, 저지연 상호작용을 제공합니다. 그림 10에서도 보듯 Vera Rubin NVL72와 LPX 조합은 사용자당 400 TPS 구간에서 NVIDIA GB200 NVL72 대비 최대 35배 높은 TPS per MW를 유지하여, interactive AI 서비스에서 새로운 premium 성능 구간을 만듭니다.  

이 전환은 직접적인 경제적 효과를 가집니다. 높은 responsiveness는 AI factory가 제공 가능한 premium 경험 범위를 넓히고 단위 인프라 가치를 올립니다. Vera Rubin 플랫폼에서는 AI factory가 GB200 NVL72 대비 최대 5배의 revenue per megawatt를 확보할 수 있고, agentic coding, 멀티에이전트 같은 가장 latency-sensitive하고 가치가 높은 interactive 워크로드에서는 Vera Rubin NVL72+LPX 조합으로 최대 10배까지 수익 기회를 확대할 수 있습니다.  

![연간 수익을 서비스 등급(Free, Medium, High, Premium, Ultra)별로 추정한 막대그래프. Blackwell, Rubin, Rubin+LPX를 비교했을 때 Rubin+LPX는 Premium/Ultra 구간에서 수익이 높다. 오른쪽 콜아웃은 총 연수익이 Blackwell에서 Rubin, Rubin+LPX 순으로 증가하며 10배 확장되는 흐름을 요약한다.](https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/LPX11-Rubin_plus_LPX_Boosts_Revenues_10X.webp)  

*그림 11. NVIDIA Vera Rubin NVL72와 LPX가 제공하는 10배 수익 기회*

## NVIDIA Groq 3 LPX가 개발자에게 제공하는 것[](#what_nvidia_groq_3_lpx_enables_for_developers)

개발자들이 요구하는 시스템은 점점 세 축을 동시에 충족해야 합니다.

+   **Responsiveness:** interactive experience와 agent loop에서 낮고 예측 가능한 latency.
+   **Capability:** 높은 모델 품질, 깊은 reasoning, 긴 context 이해력.
+   **Scale:** 많은 동시 사용자/agent를 처리할 수 있는 고처리량과 비용 효율성.

LPX는 AI factory가 처리할 수 있는 workload 범위를 넓힙니다. coding assistants, tool-calling loop가 짧고 촘촘한 agentic workflow, 음성 상호작용, 실시간 번역처럼 responsiveness가 사용자 경험을 좌우하는 영역에서는 low-latency path를 사용합니다. 반면 batch serving, long-context throughput run처럼 GPU를 지속적으로 가동해 효율을 높이는 throughput-first workload는 Rubin GPU에 남겨둡니다. 운영 철학의 전환이 핵심입니다. 더는 하나의 단일 지표만 최적화하지 말고, 실제 운영에서 마주치는 여러 operating point를 함께 최적화해야 합니다.  

## 더 알아보기[](#learn_more)

NVIDIA Groq 3 LPX와 Vera Rubin의 아키텍처를 더 깊게 보려면 [Vera Rubin platform](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/), [LPX](https://www.nvidia.com/en-us/data-center/lpx/), [AFD](https://www.nvidia.com/en-us/on-demand/session/other25-dynamoday09/), [Dynamo](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/)에 대한 NVIDIA 공식 제품 페이지와 technical blog를 시작점으로 확인하세요. 텐서 스트리밍 프로세서와 AI를 위한 software-defined silicon design에 대한 기초 연구도 함께 보면, 대규모에서의 heterogeneous, low-latency inference를 구현하는 하드웨어와 시스템 아키텍처, orchestration software를 더 깊이 이해할 수 있습니다. 이후 [NVIDIA Developer Forum](https://forums.developer.nvidia.com/)의 inference 및 배포 관련 스레드에 참여해, 유사한 시스템을 구축 중인 다른 팀과 경험을 공유하는 것도 권장됩니다.  

### 참고 자료[](#resources)

+   [NVIDIA LPX page](https://www.nvidia.com/en-us/data-center/lpx/)
+   **Press Release:** [NVIDIA Vera Rubin Opens Agentic AI Frontier](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)
+   **Tech Blog:** [Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/) 
+   **Tech Blog:** [NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer](https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/)
+   **Tech Blog:** [Announcing NVIDIA Dynamo 1.0: Scaling MultiNode Inference in Production](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/)
+   **Video:** [The Future of AI Inference – Explainer on Attention-FFN Disaggregation AFD (starting at 18:00)](https://www.nvidia.com/en-us/on-demand/session/other25-dynamoday09/)
+   **Tech Blog:** [NVIDIA Vera CPU Delivers High Performance, Bandwidth, and Efficiency for AI Factories](https://developer.nvidia.com/blog/nvidia-vera-cpu-delivers-high-performance-bandwidth-and-efficiency-for-ai-factories)
+   **Research Paper:** [Think Fast: A Tensor Streaming Processor (TSP) for Accelerating Deep Learning Workloads](https://ieeexplore.ieee.org/document/9138986)
+   **Research Paper:** [A Software-defined Tensor Streaming Multiprocessor for Large-scale Machine Learning](https://dl.acm.org/doi/pdf/10.1145/3470496.3527405)
+   **Video:** [Enabling PyTorch’s Thousand Ops for Software First Silicon Design](https://www.youtube.com/watch?v=wzgaGdcrPW0)

### 감사 인사[](#acknowledgments)

*Thanks to Amr Elmeleegy, Andrew Bitar, Andrew Ling, Graham Steele, Itay Neeman, Jamie Li, Omar Kilani, Santosh Raghavan, and Stuart Pitts, along with many other NVIDIA product leaders, engineers, and architects who contributed to this post.*
