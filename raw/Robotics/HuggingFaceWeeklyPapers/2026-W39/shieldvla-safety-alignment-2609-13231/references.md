---
title: "ShieldVLA 참고 레퍼런스"
document_type: korean-references
source_url: https://arxiv.org/html/2609.13231
hf_url: https://huggingface.co/papers/2609.13231
arxiv_id: "2609.13231"
arxiv_url: https://arxiv.org/abs/2609.13231
pdf_url: https://arxiv.org/pdf/2609.13231
week: "2026-W39"
ingested_at_kst: "2026-09-23 09:40:29 KST"
selected_reason: "VLA safety alignment의 핵심 선행 연구를 추적한다."
---

# ShieldVLA 참고 레퍼런스

Semantic Scholar `ARXIV:2609.13231/references`와 원문 References에서 안전 critic·VLM scorer·VLA backbone 연결에 중요한 항목을 골랐다.

1. **SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning** (2025), [arXiv:2503.03480](https://arxiv.org/abs/2503.03480) — ShieldVLA의 직접 baseline이다. constrained/Lagrangian learning으로 VLA safety를 다루며, ShieldVLA는 soft expected-cost trade-off 대신 HJ feasibility gate를 주장한다.
2. **OpenVLA: An Open-Source Vision-Language-Action Model** (2024), [arXiv:2406.09246](https://arxiv.org/abs/2406.09246) — visual-language input을 robot action으로 map하는 open VLA backbone 계열의 대표 자료다. ShieldVLA의 safety layer가 얹히는 policy interface를 이해하는 데 필요하다.
3. **Octo: An Open-Source Generalist Robot Policy** (2024), [arXiv:2405.12213](https://arxiv.org/abs/2405.12213) — diverse robot data에서 일반 정책을 학습하는 baseline. 안전 critic이 여러 morphology/task로 옮겨질 수 있는지 볼 때 비교 기준이 된다.
4. **Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success** (2025), [arXiv:2502.19645](https://arxiv.org/abs/2502.19645) — VLA post-training의 speed/success trade-off를 다룬다. ShieldVLA가 VLM scoring을 deployment에서 제거해 latency 증가를 피하려는 동기를 보완한다.
5. **Generalizing Safety Beyond Collision-Avoidance via Latent-Space Reachability Analysis** (2025), [arXiv:2502.00935](https://arxiv.org/abs/2502.00935) — collision 하나를 넘어 reachability-based safety set을 다룬다. ShieldVLA의 HJ value/feasible-set 해석을 넓히는 관련 축이다.
6. **A Physics-Informed Machine Learning Framework for Safe and Optimal Control of Autonomous Systems** (2025), [arXiv:2502.11057](https://arxiv.org/abs/2502.11057) — physics-informed 안전/최적 control의 관점. learned critic을 물리 constraint와 결합할 때 참고할 수 있다.
7. **Semi-Supervised Safe Visuomotor Policy Synthesis using Barrier Certificates** (2024), [arXiv:2409.12616](https://arxiv.org/abs/2409.12616) — vision 기반 policy에 barrier-certificate safety signal을 부여한다. HJ critic과 달리 barrier formulation을 사용하므로 safety interface의 대안이다.
8. **Qwen3-VL Technical Report** (2025), [arXiv:2511.21631](https://arxiv.org/abs/2511.21631) — ShieldVLA의 rubric scorer처럼 VLM을 scene evaluator로 사용할 때 model capability/limitation을 확인할 기반 문서다.
9. **Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training** (2025), [arXiv:2509.21500](https://arxiv.org/abs/2509.21500) — rubric을 structured score로 설계하는 방법론적 유사점이 있다. ShieldVLA의 visual safety rubric이 왜 항목별 score를 요구하는지 이해하는 데 연결된다.
