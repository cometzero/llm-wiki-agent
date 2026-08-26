---
title: "EXIMO 참고 문헌: VLM 계획·VLA 조작·residual RL"
document_type: references
source_url: https://arxiv.org/html/2608.19891
hf_url: https://huggingface.co/papers/2608.19891
arxiv_id: "2608.19891"
arxiv_url: https://arxiv.org/abs/2608.19891
pdf_url: https://arxiv.org/pdf/2608.19891
week: "2026-W34"
ingested_at_kst: "2026-08-26 09:40:11 KST"
selected_reason: "EXIMO의 high-level language planning, VLA behaviour cloning, residual-RL 계보를 정리한다."
---

# EXIMO 참고 레퍼런스 논문 요약

> 원문 References를 기준으로 VLM–VLA hierarchy와 adaptation에 직접 연결되는 문헌을 골랐다. Semantic Scholar references endpoint는 이번 요청에서 usable title metadata를 반환하지 않아 원문 bibliography를 우선했다.

1. **Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)** — Ahn et al., [arXiv:2204.01691](https://arxiv.org/abs/2204.01691)  
   language model이 제안한 skill을 affordance/value로 거르는 고전적 high-level planning 구조다. EXIMO와 같이 language planning과 physical execution을 분리하지만, EXIMO는 orchestrated rollout을 VLA weight로 증류한다.

2. **RT-1: Robotics Transformer for Real-World Control at Scale** — Brohan et al., [arXiv:2212.06817](https://arxiv.org/abs/2212.06817)  
   large-scale robot demonstration에서 vision-language-action control을 학습한 대표 모델이다. EXIMO가 전제하는 behaviour-cloned VLA motor prior의 배경을 제공한다.

3. **PaLM-E: An Embodied Multimodal Language Model** — Driess et al., [arXiv:2303.03378](https://arxiv.org/abs/2303.03378)  
   language model에 visual/embodied observation을 넣어 planning과 generalization을 넓힌다. EXIMO의 VLM orchestration이 활용하는 broad semantic world knowledge의 선행 사례다.

4. **ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation** — Aldaco et al., [arXiv:2405.02292](https://arxiv.org/abs/2405.02292)  
   low-cost bimanual teleoperation platform과 data collection setting을 제공한다. EXIMO의 ALOHA simulation task와 base policy training context를 이해하는 데 필요하다.

5. **Open X-Embodiment: Robotic Learning Datasets and RT-X Models** — [arXiv:2310.08864](https://arxiv.org/abs/2310.08864)  
   여러 robot embodiment와 task의 demonstration을 결합해 generalist robot policy를 학습한다. EXIMO가 large heterogeneous prior 위에서 new task post-training을 다루는 이유를 보여준다.

6. **Maximum a Posteriori Policy Optimisation (MPO)** — Abdolmaleki et al., [arXiv:1806.06920](https://arxiv.org/abs/1806.06920)  
   off-policy continuous-control RL의 중요한 계열이다. EXIMO의 online optimization을 BC policy의 sample-efficient refinement로 읽을 때 RL background가 된다.

7. **Residual Reinforcement Learning for Robot Control** — Johannink et al., [arXiv:1812.03201](https://arxiv.org/abs/1812.03201)  
   existing controller action 위에 learned residual을 얹어 prior와 adaptation을 결합한다. EXIMO의 residual off-policy RL은 VLA base policy를 보존하며 correction을 학습하는 핵심 설계와 연결된다.

8. **Gemini Robotics On-Device** — Google DeepMind, [project](https://deepmind.google/models/gemini-robotics/)  
   EXIMO가 initial VLA로 쓰는 GROD 계열의 기반이다. PaliGemma visual-language backbone과 diffusion action head라는 implementation choice가 VLM planner와의 instruction interface를 가능하게 한다.

9. **From Imitation to Refinement: Residual RL for Precise Assembly** — Ankile et al., ICRA 2025  
   imitation policy 뒤 residual refinement를 적용하는 관련 접근이다. EXIMO는 이를 VLM-orchestrated exploration과 SFT preceding stage까지 확장한다.
