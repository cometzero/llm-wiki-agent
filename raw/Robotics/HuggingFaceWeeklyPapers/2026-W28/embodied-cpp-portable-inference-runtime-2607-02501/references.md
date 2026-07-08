---
title: "Embodied.cpp 참고 레퍼런스 요약"
source_url: "https://arxiv.org/html/2607.02501"
hf_url: "https://huggingface.co/papers/2607.02501"
arxiv_id: "2607.02501"
arxiv_url: "https://arxiv.org/abs/2607.02501"
pdf_url: "https://arxiv.org/pdf/2607.02501"
week: "2026-W28"
ingested_at_kst: "2026-07-08 09:40:16 KST"
selected_reason: "Semantic Scholar references와 본문 citation에서 Embodied.cpp의 runtime/deployment 맥락을 이해하는 핵심 선행 연구를 정리."
---

# Embodied.cpp 참고 레퍼런스 요약

Semantic Scholar `paper/arXiv:2607.02501/references`와 arXiv HTML 본문 citation을 기반으로 핵심 레퍼런스를 추렸다.

## 1. Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving (arXiv:2606.20537)

- 링크: <https://arxiv.org/abs/2606.20537>
- 관계: Embodied.cpp가 latency-first batch-1 physical-AI serving을 강조하는 배경이 되는 runtime 계열 연구.
- 요약: KV cache만 재사용하는 LLM serving과 달리, recurrent state, convolution state, MTP state, metadata까지 포함한 complete restorable state를 graph-bound capsule로 저장/복원한다. Robot policy와 physical AI serving처럼 branching, reset, interrupt가 잦은 on-device setting에서 sub-millisecond restore와 큰 TTFT speedup을 보고한다.

## 2. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation (arXiv:2606.17598)

- 링크: <https://arxiv.org/abs/2606.17598>
- 관계: Embodied.cpp가 지원해야 하는 VLA family 중 adaptive multimodal sensing의 예시.
- 요약: RGB만 사용하는 VLA의 한계를 넘어 temperature, audio, radar 같은 sensor를 tool처럼 호출하고, sensor measurement를 grounded sensor image로 변환해 VLA backbone과 결합한다. Runtime 입장에서는 새로운 sensor modality와 grounded intermediate representation을 지원해야 하므로 extensible embodied I/O의 필요성을 보여준다.

## 3. LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies (arXiv:2606.15768)

- 링크: <https://arxiv.org/abs/2606.15768>
- 관계: Embodied.cpp의 WAM 지원 필요성을 보여주는 latent-space WAM 사례.
- 요약: Pixel-space video rollout 대신 compact latent visual subgoal을 예측해 action generation에 제공한다. LIBERO, RoboTwin, real-world manipulation에서 높은 success와 낮은 latency를 보이며, runtime은 action head뿐 아니라 latent future prediction branch도 schedule해야 함을 시사한다.

## 4. DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model (arXiv:2606.12105)

- 링크: <https://arxiv.org/abs/2606.12105>
- 관계: multi-rate execution이 필요한 대표적 asynchronous VLA.
- 요약: VLA가 모든 modality를 하나의 synchronous clock으로 처리하는 문제를 지적하고, modality별 latent buffer를 sensor rate에 맞게 refresh한다. 100Hz reactive control을 보고하며, Embodied.cpp가 perception/backbone/action head refresh policy를 분리해야 하는 이유를 강화한다.

## 5. World Action Models: The Next Frontier in Embodied AI (arXiv:2605.12090)

- 링크: <https://arxiv.org/abs/2605.12090>
- 관계: Embodied.cpp가 VLA뿐 아니라 WAM을 first-class로 다루는 이론적 배경.
- 요약: WAM을 future state modeling과 action generation을 결합하는 embodied foundation model paradigm으로 정의하고, cascaded/joint WAM taxonomy, data ecosystem, evaluation protocol을 정리한다. Embodied.cpp의 VLA/WAM architecture taxonomy와 직접 연결된다.

## 6. Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078)

- 링크: <https://arxiv.org/abs/2605.00078>
- 관계: future-aware reasoning을 latent query로 넣는 deployable WAM/VLA hybrid 사례.
- 요약: Future observation embedding을 posterior branch로 사용해 latent reasoning space를 학습하고, inference에서는 posterior를 버려 visual rollout 없이 future-aware action을 생성한다. Runtime 입장에서는 training-only branch와 deployable prior branch의 경계를 명확히 관리해야 한다.

## 7. Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning (arXiv:2604.02318)

- 링크: <https://arxiv.org/abs/2604.02318>
- 관계: embodied/navigation agent에서 spatial memory, history-aware planning, reflective correction이 runtime state로 등장하는 사례.
- 요약: 3D semantic map, revisiting penalty, LLM reflective correction을 결합해 VLN agent의 inefficiency를 줄인다. 자율주행/로봇 navigation에서는 policy 호출뿐 아니라 persistent memory와 planner state도 runtime object가 된다.

## 8. H2O: Heterogeneity-Aware Hierarchical Orchestration for Memory-Efficient On-Device LLM Inference

- 링크: <https://doi.org/10.1109/TMC.2025.3628498>
- 관계: on-device memory 및 heterogeneous inference orchestration 배경.
- 요약: 모델 weight가 KV cache보다 memory bottleneck이 되는 경우를 분석하고, hierarchical weight orchestration, zero-copy I/O–compute parallelism, heterogeneity-aware inference planning으로 memory와 latency를 개선한다. Embodied.cpp의 heterogeneous device 지원과 NPU/edge 관점에 참고가 된다.

## 9. vla.cpp

- 링크: 본문 citation 기준, VLA를 C++ runtime으로 배포하는 가장 가까운 선행 시스템.
- 관계: Embodied.cpp의 직접적인 predecessor.
- 요약: 여러 VLA architecture를 하나의 portable C++ inference runtime으로 가져오지만, 논문 설명에 따르면 VLA-centric이며 WAM과 modular multi-component optimization은 제한적이다. Embodied.cpp는 여기서 VLA+WAM, robot+simulator, heterogeneous hardware 지원으로 범위를 확장한다.

## 10. π0 / π0.5, OpenVLA, RT-2

- 링크: 각 VLA foundation model 논문.
- 관계: Embodied.cpp가 target으로 삼는 VLA 모델 family.
- 요약: VLA의 핵심 흐름은 pretrained VLM semantics를 robot action generation으로 연결하는 것이다. 그러나 실제 deployment에서는 action token/continuous action head/action chunk의 형식 차이가 runtime complexity로 나타난다. Embodied.cpp의 head plugin과 sequence builder가 필요한 이유다.
