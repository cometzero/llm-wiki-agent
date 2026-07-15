---
title: "Flow-ERD: 다양한 traffic simulation을 위한 agent-type aware flow matching과 entropy-regularized distillation"
source_url: "https://api.semanticscholar.org/graph/v1/paper/arXiv:2607.06957/references"
hf_url: "https://huggingface.co/papers/2607.06957"
arxiv_id: "2607.06957"
arxiv_url: "https://arxiv.org/abs/2607.06957"
pdf_url: "https://arxiv.org/pdf/2607.06957"
week: "2026-W29"
ingested_at_kst: "2026-07-15 09:40:56 KST"
selected_reason: "자율주행 개발의 핵심 인프라인 closed-loop traffic simulation에서 realism-diversity trade-off를 직접 다루며, E2E AD/VLA policy 평가용 world/traffic simulator 관점에서 가치가 높다."
---

# 참고 레퍼런스 요약: Flow-ERD: Agent-type Aware Flow Matching with Entropy-Regularized Distillation for Diverse Traffic Simulation

> Semantic Scholar `arXiv:2607.06957/references` endpoint와 원문 References 섹션을 기준으로, 학습에 중요한 reference를 선별했다.

1. **RLFTSim: Realistic and Controllable Multi-Agent Traffic Simulation via Reinforcement Learning Fine-Tuning** (2026) — Ehsan Ahmadi, Hunter Schofield, Behzad Khamidehi, Fazel Arasteh
   - Link: https://www.semanticscholar.org/paper/35828d3fd692c9f9d5b6ebfab11f50d1d82f59d1
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
2. **RoaD: Rollouts as Demonstrations for Closed-Loop Supervised Fine-Tuning of Autonomous Driving Policies** (2025) — Guillermo Garcia-Cobo, M. Igl, Peter Karkus, Zhejun Zhang
   - Link: https://www.semanticscholar.org/paper/79aed579445e33596b3cc249f9c8fb548251f9d8
   - 관계: 자율주행 planning/trajectory generation 평가 맥락을 제공한다.
3. **MDG: Masked Denoising Generation for Multi-Agent Behavior Modeling in Traffic Environments** (2025) — Zhiyu Huang, Zewei Zhou, Tianhui Cai, Yun Zhang
   - Link: https://www.semanticscholar.org/paper/30b94e15c34e21fc06223db9150250a0ec93cf78
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
4. **DecompGAIL: Learning Realistic Traffic Behaviors with Decomposed Multi-Agent Generative Adversarial Imitation Learning** (2025) — Ke Guo, Haochen Liu, Xiaojun Wu, Chen Lv
   - Link: https://www.semanticscholar.org/paper/04e68ac568789150e2d7638fc45475f2a76b9d74
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
5. **Advancing Multi-agent Traffic Simulation via R1-Style Reinforcement Fine-Tuning** (2025) — Muleilan Pei, Shaoshuai Shi, Shaojie Shen
   - Link: https://www.semanticscholar.org/paper/cf8e1d1ff1b1d58ddda32d7bfc7d419bdb908d84
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
6. **Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion** (2025) — Xun Huang, Zhengqi Li, Guande He, Mingyuan Zhou
   - Link: https://www.semanticscholar.org/paper/a8e2e3ff1770fd83228659e9e4d16114ddb9404b
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
7. **LangTraj: Diffusion Model and Dataset for Language-Conditioned Trajectory Simulation** (2025) — Wei-Jer Chang, Wei Zhan, Masayoshi Tomizuka, M. Chandraker
   - Link: https://www.semanticscholar.org/paper/8a91c1ae9a191a07bd46975aeb03c6543e537337
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
8. **Decoupled Diffusion Sparks Adaptive Scene Generation** (2025) — Yunsong Zhou, Naisheng Ye, William Ljungbergh, Tianyu Li
   - Link: https://www.semanticscholar.org/paper/f7221f0e81ab6590ad1afcbcce88debbbf0d0cf4
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
9. **Closed-Loop Supervised Fine-Tuning of Tokenized Traffic Models** (2024) — Zhejun Zhang, Peter Karkus, M. Igl, Wenhao Ding
   - Link: https://www.semanticscholar.org/paper/8770bc87d1d4228b567d2984d604ad6506719585
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.
10. **SceneDiffuser: Efficient and Controllable Driving Simulation Initialization and Rollout** (2024) — C. Jiang, Yijing Bai, A. Cornman, Christopher Davis
   - Link: https://www.semanticscholar.org/paper/29cedccc9893548210c67083d91a578d86aaa02f
   - 관계: Flow-ERD의 traffic simulator, WOSAC, multi-agent motion generation 비교 축이다.

## 읽는 순서 제안

1. benchmark/metric 논문을 먼저 읽어 결과표의 의미를 파악한다.
2. backbone/modeling 논문을 읽어 architecture novelty를 분리한다.
3. closed-loop 또는 deployment 관련 논문을 읽어 실제 적용 리스크를 점검한다.
