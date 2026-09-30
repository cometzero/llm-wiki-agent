---
title: "D-JEPA 참고 레퍼런스"
document_type: korean-references
source_url: https://arxiv.org/html/2609.24749
hf_url: https://huggingface.co/papers/2609.24749
arxiv_id: "2609.24749"
arxiv_url: https://arxiv.org/abs/2609.24749
pdf_url: https://arxiv.org/pdf/2609.24749
week: "2026-W40"
ingested_at_kst: "2026-09-30 09:40:58 KST"
selected_reason: "latent world model, plan-aware representation, VLA action selection, driving trajectory evaluation의 연결을 추적한다."
---

# D-JEPA 참고 레퍼런스

Semantic Scholar `ARXIV:2609.24749/references`와 원문 Related Work에서 D-JEPA의 문제 정의와 implementation 축을 보여 주는 항목을 골랐다.

1. **Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control** (2026), [arXiv:2607.25337](https://arxiv.org/abs/2607.25337) — TD-JEPA는 D-JEPA가 adapt·fusion하는 predictive geometry 중 하나다. temporal distance가 planning cost가 되도록 representation을 학습한다.
2. **A Control Theory of Predictability in Latent World Models** (2026), [arXiv:2607.10362](https://arxiv.org/abs/2607.10362) — prediction error/correlation이 plan quality를 보장하지 않는다는 이론적 문제의식과 이어진다. D-JEPA는 이를 candidate outcome supervision으로 바꾼다.
3. **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** (2025), [arXiv:2506.09985](https://arxiv.org/abs/2506.09985) — action-conditioned JEPA future와 planning interface의 기반이다. D-JEPA의 physical robot transfer는 이 계열 planner 위에 ranking layer를 둔다.
4. **DINO-WM: World Models on Pre-trained Visual Features Enable Zero-shot Planning** (2025), [arXiv:2506.09930](https://arxiv.org/abs/2506.09930) — pretrained visual feature space를 world model planning에 쓰는 대표 비교축이다. D-JEPA는 서로 다른 latent scale을 ordinal rank로 통합한다.
5. **PlaNet: Learning Latent Dynamics for Planning from Pixels** (2019), [arXiv:1811.04551](https://arxiv.org/abs/1811.04551) — pixel observation에서 latent dynamics를 학습하고 planning하는 출발점이다. D-JEPA의 핵심 차이는 dynamics model 자체보다 action decision의 local ordering이다.
6. **DreamerV3: Mastering Diverse Domains through World Models** (2023), [arXiv:2301.04104](https://arxiv.org/abs/2301.04104) — imagined trajectory를 behavior learning에 이용하는 latent control baseline이다. D-JEPA는 action 후보를 실제 execution outcome으로 비교한다.
7. **TD-MPC2: Scalable, Robust World Models for Continuous Control** (2024), [arXiv:2310.16828](https://arxiv.org/abs/2310.16828) — task-oriented latent dynamics와 value-based MPC의 강한 기준선. decision-local 후보 ranking이 왜 별도 문제인지 비교하기 좋다.
8. **OpenVLA: An Open-Source Vision-Language-Action Model** (2024), [arXiv:2406.09246](https://arxiv.org/abs/2406.09246) — language, vision, robot action의 policy interface를 제공하는 대표 VLA. D-JEPA의 RoboTwin transfer를 VLA 관점에서 이해하는 데 필요하다.
9. **Drive-JEPA: Learning Driving World Model from ...** — D-JEPA 원문에서 autonomous-driving candidate trajectory source로 사용된다. 본 논문은 Drive-JEPA의 32 trajectory proposal을 생성하지 않고 score correction/re-ranking만 수행한다.
