---
title: "RISE 참고 문헌: driving world model과 adaptive planning"
document_type: references
source_url: https://arxiv.org/html/2608.20430
hf_url: https://huggingface.co/papers/2608.20430
arxiv_id: "2608.20430"
arxiv_url: https://arxiv.org/abs/2608.20430
pdf_url: https://arxiv.org/pdf/2608.20430
week: "2026-W35"
ingested_at_kst: "2026-08-26 09:40:11 KST"
selected_reason: "RISE의 WAM·counterfactual safety·latent planning 계보를 학습하기 위한 핵심 문헌이다."
---

# RISE 참고 레퍼런스 논문 요약

> 원문 References와 arXiv HTML에 명시된 citation을 기준으로 선택했다. Semantic Scholar references endpoint는 이번 요청에서 제목/식별자 필드를 제공하지 않아 원문 bibliography를 우선 사용했다.

1. **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** — [arXiv:2506.09985](https://arxiv.org/abs/2506.09985)
   video self-supervised representation을 understanding·prediction·planning으로 연결한다. RISE는 이 계열의 frozen V-JEPA 2 ViT-L을 encoder로 사용하므로, visual token 품질이 subsequent predictor/gate의 기반이다.

2. **World Models** — Ha & Schmidhuber, [arXiv:1803.10122](https://arxiv.org/abs/1803.10122)
   compressed latent에서 dynamics를 rollout하고 controller가 이를 사용하는 고전적 관점이다. RISE의 contribution은 world model 자체보다, rollout을 고정 길이가 아닌 selective computation으로 다룬다는 점이다.

3. **Gaia-1: A Generative World Model for Autonomous Driving** — Hu et al., [arXiv:2309.17080](https://arxiv.org/abs/2309.17080)
   driving scene를 generative world model로 모델링한 대표 출발점이다. RISE가 현실 driving future를 상상해 planning에 쓰는 맥락과 연결되지만, RISE는 planning-gain-based stopping에 초점을 둔다.

4. **Enhancing End-to-End Autonomous Driving with Latent World Model (LAW)** — Li et al., [arXiv:2406.08481](https://arxiv.org/abs/2406.08481)
   latent world model을 E2E driving planning에 넣는 baseline 계열이다. RISE의 nuScenes/NAVSIM 비교에서 fixed/latent WAM과 adaptive horizon의 차이를 파악하는 데 중요하다.

5. **DrivingGPT: Unifying Driving World Modeling and Planning with Multi-modal Autoregressive Transformers** — Chen et al., [arXiv:2412.18607](https://arxiv.org/abs/2412.18607)
   world modeling과 planning을 autoregressive Transformer로 통합한다. RISE는 이러한 shared modeling–planning 관점 위에서 planner가 받을 future prefix length를 동적으로 선택한다.

6. **DriveFuture: Future-Aware Latent World Models for Autonomous Driving** — Hong et al., [arXiv:2605.09701](https://arxiv.org/abs/2605.09701)
   future-aware latent WAM의 최신 비교 대상이다. RISE는 NAVSIM v2 EPDMS에서 DriveFuture를 포함한 baseline보다 높은 점수를 보고하며, future awareness와 compute scheduling을 분리해 본다.

7. **DriveVLA-W0: World Models Amplify Vision-Language-Action Models for Autonomous Driving** — Li et al.
   driving VLA에 world model을 결합하는 계열로 RISE의 결과 table에 baseline으로 포함된다. language-level rationale와 latent future planning을 함께 고려할 때, RISE식 scheduler가 VLA의 expensive reasoning budget을 보조할 수 있다는 연결점을 준다.

8. **NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking** — [project](https://www.nuscenes.org/nusim)
   closed-loop driving 평가에서 safety·progress·compliance를 결합한 benchmark family다. RISE의 PDMS/EPDMS는 pure open-loop trajectory error보다 action grounding의 interactive quality에 가까운 지표다.

9. **nuScenes: A Multimodal Dataset for Autonomous Driving** — Caesar et al., [arXiv:1903.11027](https://arxiv.org/abs/1903.11027)
   large-scale sensor 기반 자율주행 dataset 및 trajectory-prediction evaluation anchor다. RISE는 nuScenes selected scenes를 CounterDrive의 factual source로도 사용한다.
