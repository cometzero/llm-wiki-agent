---
title: "NVIDIA OmniDreams: Closed-loop 자율주행 시뮬레이션을 위한 실시간 생성형 World Model — references"
source_url: "https://huggingface.co/papers/2606.03159"
hf_url: "https://huggingface.co/papers/2606.03159"
arxiv_id: "2606.03159"
arxiv_url: "https://arxiv.org/abs/2606.03159"
pdf_url: "https://arxiv.org/pdf/2606.03159"
week: "2026-W23"
ingested_at_kst: "2026-06-10 09:40:00 KST"
selected_reason: "이전 주(2026-W23) 후보 중 자율주행/E2E/closed-loop simulation 관련성이 가장 높고, VLA 대비 WAM(world-action model) 관점을 직접 제시한다."
---

# OmniDreams 참고 레퍼런스 정리

Semantic Scholar endpoint에는 구조화된 references가 충분히 노출되지 않아, PDF reference/related-work section과 본문 citation을 기준으로 핵심 관련 연구를 정리했다.

- **Cosmos / Cosmos-Predict 2.5** — NVIDIA의 physical AI/world model 기반. OmniDreams의 visual prior와 diffusion backbone 출발점.
- **Alpamayo 1 / Alpamayo 1.5** — NVIDIA 자율주행 policy/VLA baseline. OmniDreams closed-loop integration과 WAM 비교의 기준.
- **AlpaSim** — policy action과 simulator state update를 관리하는 orchestrator. OmniDreams를 reactive environment로 연결한다.
- **Diffusion Forcing (Chen et al., 2024)** — bidirectional diffusion/video model을 causal autoregressive generation으로 바꾸기 위한 training method.
- **Self Forcing (Huang et al., 2025)** — teacher forcing과 inference self-rollout mismatch를 줄이기 위한 distillation/training framework.
- **Distribution Matching Distillation (Yin et al., 2024)** — generated video distribution을 real data manifold로 맞추는 holistic objective.
- **NuRec simulator / reconstruction-based neural simulator** — closed-loop 비교 대상. photorealistic reconstruction은 강하지만 novel dynamic scenario 일반화가 제한적이다.
- **DriveDreamer / Drive-WM 계열** — 자율주행 world model 연구의 전형적 배경. OmniDreams는 real-time closed-loop 조건을 더 강하게 목표로 한다.
- **Waymo / CARLA / nuPlan style closed-loop evaluation** — 자율주행 policy 검증에서 open-loop metric 한계를 보완하는 평가 패러다임.
- **World Action Model (WAM) in robotics** — VLA와 대비되는 policy architecture 관점. OmniDreams는 AV에서도 WAM이 경쟁력 있음을 제시한다.

## 읽기 우선순위

1. Cosmos / Cosmos-Predict 2.5 — backbone과 physical AI world model 관점.
2. Diffusion Forcing + Self Forcing — autoregressive video generation 안정화.
3. NuRec / reconstruction-based simulator — 비교 대상의 한계 이해.
4. Alpamayo / WAM vs VLA — 자율주행 policy architecture 논쟁.
