---
    title: "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System — Korean technical translation"
    source_url: "https://arxiv.org/abs/2606.18112"
    hf_url: "https://huggingface.co/papers/2606.18112"
    arxiv_id: "2606.18112"
    arxiv_url: "https://arxiv.org/abs/2606.18112"
    pdf_url: "https://arxiv.org/pdf/2606.18112"
    week: "2026-W27"
    category: "raw/Robotics/HuggingFaceWeeklyPapers"
    ingested_at_kst: "2026-07-01 09:40:38 KST"
    selected_reason: "2026-W27 후보 중 자율주행·navigation·VLM/VLA 접점이 가장 직접적이며, NAVSIM closed-loop autonomous driving까지 평가한 Qwen3-VL 기반 scalable navigation model."
    ---

# Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System — 한국어 기술 번역

> 원문: arXiv:2606.18112 / Hugging Face Weekly 2026-W27  
> 번역 범위: Abstract, Introduction, Navigation Model, Agentic Navigation, Data, Deployment/Evaluation, Autonomous Driving, Ablation, Real-world Deployment, Conclusion을 깊게 번역·재구성했습니다. 부록·세부 수치표 전체는 본문 핵심과 관련되는 부분만 요약했습니다.

## Abstract 번역

Agentic navigation system에는 inference time에 관측 전략을 외부에서 다시 설정할 수 있는 base navigation model이 필요하다. Instruction following, object search, target tracking, autonomous driving은 같은 perception-planning backbone을 공유하지만, visual stream을 소비하는 방식은 근본적으로 다르다. 저자들은 Qwen3-VL 위에 구축한 scalable navigation model인 **Qwen-RobotNav**를 제안한다. 핵심은 두 축의 parameterised interface다. 첫째, task mode가 navigation behaviour를 선택하고, 둘째 token budget, per-camera weight 같은 controllable observation parameter가 visual history encoding을 제어한다. 모든 parameter를 training time에 randomization하기 때문에 Qwen3-VL backbone을 바꾸지 않고도 inference-time configuration에 견고하다.

Qwen-RobotNav는 15.6M samples로 학습된다. Trajectory-only training만 사용하면 모델이 reactive action-sequence mapper로 붕괴하는데, vision-language data를 함께 학습해 이를 방지한다. Parameterised interface 덕분에 upper-level planner가 long-horizon goal을 sub-task로 분해하고, episode 중 task mode와 context strategy를 동적으로 바꿔 같은 모델 호출을 반복적으로 조합할 수 있다. 실험에서는 VLN-CE RxR 76.5% success rate, EVT-Bench 90.0% tracking rate, NAVSIM 91.4 PDMS를 보고하며, embodied QA에서도 이전 SOTA 대비 10.8% 향상을 보인다.

## 1. Introduction 번역

Embodied navigation은 instruction following, point-goal navigation, object search, target tracking, autonomous driving처럼 매우 다양한 task family를 포함한다. 이들은 모두 egocentric perception을 executable motion으로 바꾼다는 점에서는 같지만, 필요한 memory horizon과 observation fidelity가 다르다. 예를 들어 language instruction following은 과거 landmark와 procedural milestone을 다시 참조해야 하므로 episode-level memory가 중요하다. 반면 active tracking은 현재 target의 motion과 occlusion에 민감해 최신 frame을 고해상도로 처리해야 한다. Autonomous driving은 multi-camera traffic scene, route command, safety constraint를 동시에 만족해야 하므로 camera-wise attention과 trajectory planning이 중요하다.

기존 방식은 task별 architecture/head를 두거나, 고정된 observation context를 사용한다. 저자들은 이를 **context modeling problem**으로 재정의한다. 즉, backbone은 유지하되 task mode, token allocation, camera weight, temporal decay, frame sampling을 prompt와 parameter로 조절하면 여러 navigation task를 하나의 model로 다룰 수 있다는 주장이다. 이는 VLA for AD 관점에서 중요하다. 자율주행 end-to-end model도 결국 route instruction, traffic semantics, multi-view observation, trajectory output을 연결해야 하며, Qwen-RobotNav는 이 연결을 VLM backbone + waypoint action head로 구현한다.

## 2. Navigation Model

### 2.1 Model Architecture

Qwen-RobotNav는 Qwen3-VL architecture를 상속하고 trajectory regression을 위한 lightweight action head를 붙인다. Vision encoder는 SigLIP-2 ViT 기반이며 native dynamic-resolution과 2D-RoPE를 지원한다. LLM backbone은 visual token과 text prompt를 함께 받아 spatial-language reasoning을 수행한다. 마지막 hidden state `E^A`는 4-layer MLP action head로 전달되어 `K=8`개의 waypoint를 예측한다. 각 waypoint는 `(x_k, y_k, θ_k)`의 3 DoF로 표현되므로 총 24차원 출력이다.

### 2.2 Task-Adaptive Observation Encoding

Navigation은 partial observability 아래의 sequential decision-making이다. Qwen-RobotNav는 visual history를 고정 길이로 자르는 대신, task-specific context parameter로 token allocation을 결정한다. Temporal decay `γ`, token budget `B`, camera weight `w_c`, frame sampling mode가 서로 결합되어 최근 frame 중심인지, long-history 중심인지, 특정 camera 중심인지가 정해진다. 이 설계는 autonomous driving에서 front/side/rear camera importance를 달리 주거나, VLN에서 과거 landmark memory를 길게 보존하는 식으로 확장된다.

### 2.3 Viewpoint and Temporal Identification

Visual token만으로는 어떤 token이 “front camera step 12”인지 “left camera step 3”인지 알기 어렵다. 논문은 natural-language viewpoint tag와 timestep tag를 visual token 사이에 삽입한다. Learned embedding이 아니라 언어 tag를 쓰는 점이 특징이다. 이는 Qwen3-VL의 language reasoning 능력을 그대로 활용하면서 camera/time identity를 모델에게 명시적으로 알려준다.

### 2.4 Embodiment-Aware Prompt Design

Indoor mobile robot, quadruped, autonomous vehicle은 같은 waypoint라도 dynamics와 safety constraint가 다르다. Qwen-RobotNav는 별도 learned embedding이나 head 대신 system prompt preamble로 embodiment를 표현한다. 예: “Imagine you are a robot programmed for navigation tasks” 또는 autonomous driving 환경을 암시하는 preamble. 이는 cross-embodiment transfer를 위한 단순하지만 강한 interface다.

### 2.5 Action Planning

Action head는 LLM final hidden state를 waypoint trajectory로 mapping한다. 출력은 per-dataset scale factor로 `[-1, 1]`에 정규화된 `(x, y, θ)` waypoint sequence다. Training objective는 다음과 같다.

```text
L = L_traj + λ L_VL
L_traj = || W_hat - W* ||_2^2
```

`L_traj`는 navigation trajectory sample에만 적용되고, `L_VL`은 vision-language alignment를 유지한다. 이 결합이 중요한 이유는 trajectory-only 학습이 model을 language reasoning 없는 reactive mapper로 만들 수 있기 때문이다.

## 3. Qwen-RobotNav for Agentic Navigation

Qwen-RobotNav는 standalone navigation benchmark model일 뿐 아니라, upper-level planner가 부르는 navigation module로 설계된다. Planner는 long-horizon instruction을 sub-goal로 나누고 각 sub-goal에 대해 task mode, token budget, temporal decay, camera weights를 지정한다. Navigation call의 결과는 raw frame stream 전체가 아니라 trajectory evidence와 context-compressed summary로 planner에 반환된다. 이 구조는 VLA/agentic driving system에서 slow planner와 fast trajectory module을 연결하는 dual-system interface로 읽을 수 있다.

## 4. Data

Training corpus는 navigation trajectory data와 vision-language data를 합쳐 15.6M samples이다. 포함 범위는 instruction following, point-goal navigation, object-goal navigation, target tracking, autonomous driving이다. Autonomous driving은 별도 capability라기보다 cross-embodiment trajectory supervision source로 포함된다. 모델은 complex dynamic traffic, drivable area, route compliance, time-to-collision 같은 safety-critical 요소를 포함하는 future trajectory를 학습한다.

논문은 video generator로 synthetic egocentric navigation data도 만든다. LLM이 video prompt와 navigation instruction을 생성하고, text-to-video model이 first-person video를 합성한다. 이후 VLM quality filter와 monocular depth/pose estimator, kinematic filter를 거쳐 물리적으로 말이 되는 trajectory만 남긴다. 이는 실제 robot/vehicle data가 부족한 long-tail navigation scene을 보강하는 방식이다.

## 5. Deployment and Evaluation

Qwen-RobotNav는 cloud deployment와 edge deployment를 모두 평가한다. Edge case에서는 Jetson Thor에서 FP8 quantization과 TensorRT acceleration을 사용한다. 이는 자율주행/VLA 관점에서 latency와 on-device feasibility가 핵심임을 보여준다.

평가는 VLN-CE, OVON, EVT-Bench, embodied QA, NAVSIM을 포함한다. Autonomous driving 평가는 NAVSIM navtest의 closed-loop metrics를 사용하며 Navigation Compliance, Drivable Area Compliance, Time-to-Collision, Comfort, Ego Progress, PDMS를 보고한다. 특히 PDMS 91.4는 human 94.8에 근접하는 수치로 제시된다. 단, NAVSIM은 closed-loop planner metric이지만 실제 도로 배포와는 차이가 있으므로 safety validation은 별도 필요하다.

## 6. Figures / Tables 번역 메모

- 그림 1: `figures/figure-01.png` — 
- 그림 2: `figures/figure-02.png` — Figure 1: Benchmark summary. Across instruction following, object search, target tracking, embodied question answering, and autonomous driving, Qwen-RobotNav-4B and Qwen-RobotNav-8B achieve state-of-the-art or competitive performance against specialist and navigation foundation model baselines. Trophy icons mark the best result in each benchmark group.
- 그림 3: `figures/figure-03.png` — Figure 2: Qwen-RobotNav architecture. Top: In the agentic navigation system, an upper planner LLM decomposes long-horizon goals into sub-goals and controls Qwen-RobotNav through task-adaptive context parameters such as token budget B B , temporal decay γ \gamma , camera weights w c w_{c} , and frame sampling mode. Bottom: Qwen-RobotNav receives multi-view RGB observations, an embodied prompt, and a navigation instruction; allocates visual tokens across cameras and timesteps; inserts natural-lang
- 그림 5: `figures/figure-05.png` — Figure 3: Visualization of task-adaptive observation encoding. (a) Normalized temporal weights ω t = exp ⁡ ( γ ⋅ t / ( T ′ − 1 ) ) \omega_{t}=\exp(\gamma\cdot t/(T^{\prime}{-}1)) for varying decay factors γ \gamma when T ′ > 1 T^{\prime}{>}1 ; annotations show the newest-to-oldest weight ratio. (b) Resulting per-timestep token budget (summed across all cameras) under a fixed total budget B = 3072 B{=}3072 with camera weights w c = [ 2.0 , 1.0 , 0.5 , 1.0 ] w_{c}{=}[2.0,1.0,0.5,1.0] for front, ri
- 그림 6: `figures/figure-06.png` — Figure 4: Qwen-RobotNav for agentic navigation. An upper-level planner decomposes a long-horizon task into sub-goals and dispatches either auxiliary vision-tool calls or Qwen-RobotNav navigation calls. Each navigation call is parameterized by a sub-goal instruction ℒ i \mathcal{L}_{i} , a task mode τ i \tau_{i} , and an observation configuration Φ i \Phi_{i} . Qwen-RobotNav uses the selected task mode and configuration to predict waypoints 𝒲 i \mathcal{W}_{i} , which are executed in the environm
- 그림 7: `figures/figure-07.png` — Figure 5: Training data distribution. Left: Per-dataset sample counts across all navigation trajectory and vision-language sources. Right: Aggregated distribution over task categories, totalling 15.6M training samples.
- 그림 8: `figures/figure-08.png` — Figure 6: Visualization of the three coordinate-based point-goal navigation categories. Direct Approach (348K) targets near-straight paths along canonical egocentric directions. Short Range (174K) introduces local obstacle avoidance within cluttered indoor geometry. Long Range (400K) requires multi-room path search over extended horizons, navigating around walls and furniture.
- 그림 9: `figures/figure-09.png` — Figure 7: Object-goal navigation data generation pipeline. (1) The top-down occupancy map is binarised into a navigability mask. (2) Morphological dilation and erosion expand navigable regions and remove thin noise. (3) Skeletonisation extracts the medial-axis graph of the navigable space. (4) An exploration trajectory is generated by traversing the skeleton with backtracking at dead ends. (5) A VLM annotates the goal object at the terminal viewpoint, producing open-vocabulary goal specification
- 그림 10: `figures/figure-10.png` — Figure 8: Autogenerated navigation data pipeline. Right: A large language model first generates paired video prompts and navigation instructions; a text-to-video model then synthesises first-person egocentric videos, which are filtered by a vision-language model for quality before a monocular depth-and-pose estimator extracts 2-D trajectories; a final kinematic filter removes physically implausible samples. Left: Two example outputs covering instruction following (top) and target tracking (botto
- 그림 11: `figures/figure-11.png` — Figure 9: Visual comparison between original Habitat simulator renders (top) and Qwen-Image-Edit ( wu2025qwenimage ) (bottom).
- 그림 12: `figures/figure-12.png` — Figure 10: Visualization of structured multi-perspective reasoning along a complete navigation trajectory. Given the instruction “ Enter the open space, then go through the door on the right. Wait just past the black doormat ,” the agent executes eight sequential steps (numbered on the floor plan). At each step, a four-component reasoning chain is produced: History summarises the journey so far, Scene Analysis describes the current multi-view observations, Instruction Progress tracks completed a

## 7. Conclusion 번역

Qwen-RobotNav는 multi-task navigation의 핵심을 architecture explosion이 아니라 context modeling으로 본다. 다양한 navigation task는 perception-planning backbone을 공유하지만 observation stream을 소비하는 방식이 다르므로, parameterised context interface가 필요하다. Qwen3-VL 기반 backbone, task-adaptive observation encoding, language identity tags, waypoint action head, 15.6M mixed corpus가 결합되어 instruction following부터 autonomous driving까지 하나의 모델로 다룬다. VLA for autonomous driving 관점에서는 VLM reasoning을 직접 executable waypoint trajectory로 grounding하는 중요한 사례다.

## 번역상 생략·주의

- 부록의 모든 세부 hyperparameter와 표 전체는 요약했습니다.
- arXiv HTML에서 추출 가능한 그림 파일은 `figures/`에 저장했습니다. 일부 arXiv LaTeXML 표/알고리즘은 이미지가 아니라 텍스트 캡션으로만 보존됩니다.
- “VLA”라는 명칭을 직접 쓰는 robot manipulation 논문과 달리, 이 논문은 navigation foundation model이지만 VLM-to-trajectory action grounding과 autonomous driving closed-loop evaluation이 있어 이번 주제에 포함했습니다.
