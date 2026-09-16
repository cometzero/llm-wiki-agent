---
title: "DriveZero 핵심 참고문헌"
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.06055/references
hf_url: https://huggingface.co/papers/2609.06055
arxiv_id: "2609.06055"
arxiv_url: https://arxiv.org/abs/2609.06055
pdf_url: https://arxiv.org/pdf/2609.06055
week: "2026-W37"
ingested_at_kst: "2026-09-16 09:40 KST"
selected_reason: "DriveZero의 RL, simulation, camera-planning 계보를 정리"
---
# DriveZero 핵심 참고문헌

Semantic Scholar `ARXIV:2609.06055/references`와 본문 인용에서 골랐다.

1. **[Qwen-Drive-1.0](https://arxiv.org/abs/2609.00111)** (2026) — 자율주행 vision-language foundation model. DriveZero와 달리 language/vision foundation-model 축을 강화하며, DriveZero의 camera planner를 VLM reasoning과 비교하는 기준이다.
2. **[Pictura: Perspective-View Self-Play at Scale for Driving](https://arxiv.org/abs/2607.26005)** (2026) — driving self-play를 대규모로 다룬다. DriveZero의 mixed-agent interactive world와 “자기 행동이 만든 state에서 학습”이라는 동기가 맞닿아 있다.
3. **[World Engine: Towards the Era of Post-Training for Autonomous Driving](https://arxiv.org/abs/2606.19836)** (2026) — post-training을 driving policy의 핵심 단계로 본다. DriveZero는 world-model rollout 대신 log-initialized simulator에서 PPO teacher를 학습한다.
4. **[Scaling Self-Play for End-to-End Driving](https://arxiv.org/abs/2606.19641)** (2026) — self-play 규모가 driving behavior를 만들 수 있음을 보이는 직접적인 선행 맥락이다.
5. **[TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations](https://arxiv.org/abs/2606.17386)** (2026) — expert demonstration 없는 E2E driving이라는 문제 설정을 공유한다. DriveZero의 차별점은 VFM distillation과 privileged RL teacher→camera student 분리다.
6. **[Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives](https://arxiv.org/abs/2605.19771)** (2026) — 사람 로그가 놓친 hard case를 보완하려는 접근. DriveZero는 hard negative를 별도 정답으로 만들기보다 interactive rollout로 새로운 행동 분포를 만든다.
7. **[DriveFine](https://arxiv.org/abs/2602.14577)** (2026) — robust diffusion VLA planner. action generation과 safety/precision을 다루는 비교 대상이며, DriveZero의 proposal trajectory decoder와는 생성 형식이 다르다.
8. **[PlannerRFT](https://arxiv.org/abs/2601.12901)** (2026) — diffusion planner를 closed-loop RL로 fine-tune한다. DriveZero는 imitation-pretrained camera policy가 아니라 structured teacher를 scratch RL로 만든다는 점에서 다르다.
9. **[SimScale](https://arxiv.org/abs/2511.23369)** (2025) — real-world simulation scale로 driving data를 확장한다. DriveZero-Scale의 237K OOD simulation scene에 직접 연결된다.
10. **[Depth Anything 3](https://arxiv.org/abs/2511.10647)** (2025) — visual-space/depth representation 계보. DriveVFM이 geometric cue를 얻기 위해 사용하는 Depth Anything V2와 같은 representation-learning 축이다.
