---
title: "VLA-Precision 참고 레퍼런스"
document_type: korean-references
source_url: https://arxiv.org/html/2609.04355
hf_url: https://huggingface.co/papers/2609.04355
arxiv_id: "2609.04355"
arxiv_url: https://arxiv.org/abs/2609.04355
pdf_url: https://arxiv.org/pdf/2609.04355
week: "2026-W40"
ingested_at_kst: "2026-09-30 09:40:58 KST"
selected_reason: "VLA post-training, real-world RL, intervention learning, action expert/flow policy의 선행 축을 연결한다."
---

# VLA-Precision 참고 레퍼런스

Semantic Scholar endpoint는 이 논문에 대해 reference rows를 제공하지 않아, 원문 Related Work와 method에서 직접 언급한 핵심 계보를 정리했다.

1. **π0.5: A Vision-Language-Action Model with Open-World Generalization** (2025) — 본 논문의 task-specific initialization backbone이다. VLA-Precision은 Stage I에 \(\pi_{0.5}\)를 fine-tune하고 Stage II에서 action expert LoRA만 online optimize한다.
2. **HIL-SERL: Human-in-the-Loop Reinforcement Learning for Real-World Robot Control** (2024), [arXiv:2410.21845](https://arxiv.org/abs/2410.21845) — human intervention을 이용해 real-world RL을 빠르게 안정화한다. ACoB의 correction buffer와 early behavioral learning의 직접적 비교축이다.
3. **ConRFT: ... Reinforcement Fine-Tuning for Robot Policies** (2025) — offline-to-online RL과 BC constraint로 compact robot policy를 개선한다. VLA-Precision은 large VLA의 value drift와 system overhead에 초점을 확장한다.
4. **OpenVLA: An Open-Source Vision-Language-Action Model** (2024), [arXiv:2406.09246](https://arxiv.org/abs/2406.09246) — VLA의 visual-language-to-action interface를 이해할 대표 backbone 자료다.
5. **Octo: An Open-Source Generalist Robot Policy** (2024), [arXiv:2405.12213](https://arxiv.org/abs/2405.12213) — large-scale generalist robot policy와 task adaptation의 기준선. 논문은 compact-policy real-world RL 계열을 Octo representation과 대비한다.
6. **RIPT-VLA** — dynamic rollout sampling과 leave-one-out advantage로 VLA RL post-training을 시도한 simulation 축이다. VLA-Precision은 physical interaction에서 value calibration을 다룬다.
7. **VLA-RL** — trajectory-level RL과 process reward로 VLA post-training을 수행한 simulation-based 계열. real-world sim-to-real gap이 VLA-Precision의 출발 동기다.
8. **RLinf-VLA** — heterogeneous workload coordination으로 VLA RL throughput을 높이는 계열. ACoB-Stream은 simulator scale-out이 아니라 physical actor–learner의 prefix/KV/state lifecycle을 최적화한다.
9. **RL Token** — critical phase throughput을 높이고 externalized policy component를 사용한다. VLA-Precision은 auxiliary editor 대신 action expert의 trainable subspace에 improvement를 축적하려 한다.
10. **GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators** (2023), [arXiv:2309.13037](https://arxiv.org/abs/2309.13037) — real-world correction/demonstration interface의 hardware 맥락이다. 논문은 master-arm load, backlash, operator precision 문제를 대응해 isomorphic master와 keyboard mode를 설계한다.
