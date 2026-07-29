---
title: "WorldDiT: A Unified Diffusion Architecture for World and Action Modeling"
source_url: "https://arxiv.org/html/2607.23909"
hf_url: "https://huggingface.co/papers/2607.23909"
arxiv_id: "2607.23909"
arxiv_url: "https://arxiv.org/abs/2607.23909"
pdf_url: "https://arxiv.org/pdf/2607.23909"
week: "2026-W31"
ingested_at_kst: "2026-07-29 09:40:46 KST"
selected_reason: "VLM action backbone 없이 continuous action chunk와 future RGB patch prediction을 같은 DiT로 학습하는 compact world-action modeling 논문으로, VLA/World Model track과 배포 지연·파라미터 효율성 관점에 적합하다."
---

# WorldDiT — 참고 레퍼런스 논문 요약

Semantic Scholar references endpoint에서 확인된 reference 및 논문 Table 1에 등장하는 관련 연구 중 핵심 10개를 정리한다.

## 1. Paris 2.0: A Decentralized Diffusion Model for Video Generation (2026, arXiv:2605.26064)

- 관계: WorldDiT discussion에서 action/RGB target을 shared flow interface로 다루는 방향과 연결되는 diffusion 기반 생성 모델.
- 요약: decentralized diffusion/video generation 구조를 다루며, WorldDiT 저자 중 일부와 연구 방향이 이어진다.
- WorldDiT와의 차이: Paris는 video generation 중심이고, WorldDiT는 robot action chunk + future RGB patch를 control policy로 연결한다.

## 2. MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation (2026)

- 관계: Table 1의 large pretrained VLM action backbone category 상위권 baseline.
- 요약: diffusion 기반 VLA로 multimodal instruction과 action/generation을 통합하려는 접근.
- 차이: MMaDA-VLA는 대형 VLM/VLA backbone 계열이고, WorldDiT는 compact DiT로 action/world modeling을 결합한다.

## 3. VLANeXt: Recipes for Building Strong VLA Models (2026)

- 관계: 강한 VLA recipe baseline.
- 요약: VLA 모델 구축에서 data, architecture, training recipe를 체계화하는 연구.
- 차이: WorldDiT는 VLA recipe 전반보다 “large VLM 없이도 가능한 compact world-action diffusion baseline”에 초점을 둔다.

## 4. ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models (2026)

- 관계: explicit reasoning/action CoT를 쓰는 VLA baseline.
- 요약: action generation 전에 action chain-of-thought를 통해 motion reasoning을 보강한다.
- 차이: WorldDiT는 explicit language reasoning이 아니라 continuous flow 기반 action chunk generation이다.

## 5. Unified Diffusion VLA (2025, arXiv:2511.01718)

- 관계: discrete denoising diffusion process로 VLA를 구성하는 diffusion VLA 계열.
- 요약: action을 discrete diffusion formulation으로 decoding한다.
- 차이: WorldDiT는 continuous action chunk와 normalized RGB patch를 같은 flow matching target으로 묶는다.

## 6. VLA-0: Building State-of-the-Art VLAs with Zero Modification (2025, arXiv:2510.13054)

- 관계: large pretrained VLA/VLM backbone을 활용하는 state-of-the-art VLA baseline.
- 요약: 기존 pretrained model을 최대한 수정 없이 action policy로 활용하려는 방향.
- 차이: WorldDiT는 pretrained VLM action backbone 의존도를 줄이고 compact backbone의 Pareto efficiency를 보인다.

## 7. VLA-Adapter: An Effective Paradigm for Tiny-Scale VLA Model (2025, arXiv:2509.09372)

- 관계: 작은 규모 VLA를 만들기 위한 adapter 방식.
- 요약: tiny-scale 모델에 adapter를 붙여 VLA capability를 확보하려 한다.
- 차이: WorldDiT는 adapter보다 unified diffusion backbone과 auxiliary world prediction에 초점을 둔다.

## 8. Discrete Diffusion VLA (2025, arXiv:2508.20072)

- 관계: diffusion을 action decoding에 쓰는 또 다른 계열.
- 요약: discrete action token 또는 action representation에 denoising diffusion을 적용한다.
- 차이: WorldDiT는 continuous robot action과 RGB patch를 모두 flow-matching target으로 통일한다.

## 9. MemoryVLA (2025, arXiv:2508.19236)

- 관계: VLA에서 perceptual-cognitive memory를 강조하는 baseline.
- 요약: long-horizon manipulation을 위해 memory mechanism으로 scene/task state를 유지한다.
- 차이: WorldDiT는 memory보다 receding-horizon action chunk와 world supervision에 집중한다.

## 10. Diffusion Policy / DiT Policy / LIBERO benchmark

- 관계: WorldDiT의 직접적인 action diffusion 및 simulation evaluation 배경.
- 요약: Diffusion Policy는 continuous action sequence를 denoising diffusion으로 생성하는 대표 robot policy다. LIBERO는 language-conditioned manipulation suite로 VLA policy 평가에 널리 쓰인다.
- 차이: WorldDiT는 pure action diffusion에 future RGB patch prediction objective를 추가해 world-action coupling을 시도한다.
