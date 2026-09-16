---
title: "LIT 핵심 참고문헌"
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.12641/references
hf_url: https://huggingface.co/papers/2609.12641
arxiv_id: "2609.12641"
arxiv_url: https://arxiv.org/abs/2609.12641
pdf_url: https://arxiv.org/pdf/2609.12641
week: "2026-W38"
ingested_at_kst: "2026-09-16 09:40 KST"
selected_reason: "LIT의 action prior, VLA/WAM, robustness benchmark 계보"
---
# LIT 핵심 참고문헌

Semantic Scholar `ARXIV:2609.12641/references` 및 본문 reference에서 고른 10편이다.

1. **[Pi0.5: A Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** (2025) — LIT가 적용한 VLA 중 하나. Mixture-of-Transformers에서 VLM/action expert의 shared self-attention conditioning을 쓴다.
2. **[MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881)** (2026) — VLM layer의 projected KV representation에 action expert가 cross-attention한다. LIT의 layerwise interface 실험 기준이다.
3. **[Fast-WAM](https://arxiv.org/abs/2603.16666)** (2026) — future-video training을 쓰지만 action-only inference를 하는 WAM. LIT가 VLA 밖 WAM으로 일반화되는지 확인한다.
4. **[ImageWAM](https://arxiv.org/abs/2606.19531)** (2026) — video generation 대신 image editing latent/denoising을 action conditioning에 사용한다. LIT의 다른 visual coupling 사례다.
5. **[LA4VLA: Learning to Act without Seeing via Language-Action Pretraining](https://arxiv.org/abs/2606.27295)** (2026) — image 없이 language-action prior를 먼저 학습한다. LIT는 여기에 terminal pose condition 및 visual interface constraint를 더한다.
6. **[Learning Action Priors for Cross-embodiment Robot Manipulation](https://arxiv.org/abs/2606.26095)** (2026) — state-action trajectory로 transferable action prior를 학습한다. LIT가 action prior를 시각 shortcut 방지와 연결하는 배경이다.
7. **[APT: Action Expert Pretraining Improves Instruction Generalization of VLA Policies](https://arxiv.org/abs/2606.12366)** (2026) — action expert pretraining이 language generalization에 미치는 효과를 본다. LIT는 pretraining 이후 visual input 경로까지 제약한다.
8. **[SpatialVLA](https://arxiv.org/abs/2501.15830)** (2025) — egocentric 3D spatial representation을 VLA에 넣는다. LIT의 terminal-pose spatial supervision과 비교할 수 있다.
9. **[CogACT](https://arxiv.org/abs/2411.19650)** (2024) — VLM representation에서 diffusion action module로의 conditioning을 연구한다. direct rich-feature conditioning의 대표 비교점이다.
10. **[LIBERO-Plus](https://arxiv.org/abs/2604.16054)** (2026) — camera/noise/layout/lighting 등 7 shift를 제공하는 VLA robustness benchmark. LIT의 핵심 OOD 근거다.
