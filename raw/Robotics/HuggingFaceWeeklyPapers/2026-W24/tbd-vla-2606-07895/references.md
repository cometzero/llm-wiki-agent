---
title: "TBD-VLA: 시간 블록 Diffusion 기반 Vision-Language-Action 모델 — references"
source_url: "https://huggingface.co/papers/2606.07895"
hf_url: "https://huggingface.co/papers/2606.07895"
arxiv_id: "2606.07895"
arxiv_url: "https://arxiv.org/abs/2606.07895"
pdf_url: "https://arxiv.org/pdf/2606.07895"
week: "2026-W24"
ingested_at_kst: "2026-06-10 09:40:00 KST"
selected_reason: "현재 주(2026-W24) 후보 중 VLA/action grounding 관련성이 가장 높고, discrete VLA의 latency와 temporal dependency 문제를 직접 다루는 논문이다."
---

# TBD-VLA 참고 레퍼런스 정리

Semantic Scholar references endpoint와 논문 reference section을 함께 확인해 중요한 관련 연구를 골랐다.

- **Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance** ([arXiv:2603.25661](https://arxiv.org/abs/2603.25661)) — TBD-VLA와 가장 가까운 speed-oriented discrete diffusion VLA 계열. TBD-VLA는 단순 speedup을 넘어 temporal block 구조를 명시화한다.
- **Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in VLA Policies** ([arXiv:2511.01718](https://arxiv.org/abs/2511.01718)) — action decoding을 discrete diffusion으로 바꾼 직접 선행연구. TBD-VLA는 여기에 block-level temporal autoregression을 추가한다.
- **Qwen3-VL Technical Report** ([arXiv:2511.21631](https://arxiv.org/abs/2511.21631)) — TBD-VLA의 VLM backbone. action token decoding 능력은 이 backbone의 multimodal representation에 의존한다.
- **LIBERO-Plus: In-depth Robustness Analysis of VLA Models** ([arXiv:2510.13626](https://arxiv.org/abs/2510.13626)) — TBD-VLA robustness 평가에 사용되는 perturbation benchmark.
- **InternVLA-M1: A Spatially Guided VLA Framework** ([arXiv:2510.13778](https://arxiv.org/abs/2510.13778)) — spatial grounding을 VLA action으로 연결하는 관련 연구. TBD-VLA의 temporal action grounding과 보완적이다.
- **VLA-0: Building State-of-the-Art VLAs with Zero Modification** ([arXiv:2510.13054](https://arxiv.org/abs/2510.13054)) — VLM 자체를 거의 수정하지 않고 VLA policy로 쓰려는 흐름. TBD-VLA도 VLM-native action decoding을 지향한다.
- **LLaDA-VLA: Vision Language Diffusion Action Models** ([arXiv:2509.06932](https://arxiv.org/abs/2509.06932)) — language diffusion model을 VLA action generation에 적용하는 계열.
- **OpenVLA: An Open-Source Vision-Language-Action Model** — 대표적인 autoregressive discrete VLA baseline. TBD-VLA는 OpenVLA식 token generation의 latency 한계를 겨냥한다.
- **π0.5: A VLA Model with Open-World Generalization** — continuous action expert 기반 강력 baseline. TBD-VLA의 real-world 비교 대상이다.
- **FAST: Efficient Action Tokenization for VLA Models** — action token 수 자체를 줄이는 approach. TBD-VLA는 token compression 대신 block diffusion decoding을 선택한다.

## 읽기 우선순위

1. **Discrete Diffusion VLA / Fast-dVLA** — TBD-VLA의 직접 기술 배경.
2. **Qwen3-VL** — VLM backbone이 action token decoding에 어떤 representation을 제공하는지 이해.
3. **OpenVLA / VLA-0 / π0.5** — discrete-token VLA와 continuous-action-expert VLA의 대비.
4. **LIBERO-Plus / SimplerEnv** — robustness와 sim-to-real 평가 방식 이해.
