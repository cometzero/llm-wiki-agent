---
title: "Act with Intent (INDI) 참고문헌 학습 메모"
document_type: references
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.23478/references
hf_url: https://huggingface.co/papers/2608.23478
arxiv_id: "2608.23478"
arxiv_url: https://arxiv.org/abs/2608.23478
pdf_url: https://arxiv.org/pdf/2608.23478
week: "2026-W36"
ingested_at_kst: "2026-09-09 09:40:43 KST"
selected_reason: "INDI의 VLA backbone, behavior intent, representation-transfer 문헌을 연결한다."
---

# Act with Intent (INDI) 참고 레퍼런스 논문 요약

> Semantic Scholar `ARXIV:2608.23478/references` endpoint는 67개 reference를 반환했다. 아래는 원문의 related work와 method를 이해하는 데 중요한 논문을 선별한 학습 메모다.

1. **LUCID: Learning Embodiment-Agnostic Intent Models from Unstructured Human Videos for Scalable Dexterous Robot Skill Acquisition** (2026), [arXiv:2606.11628](https://arxiv.org/abs/2606.11628)
   Unstructured human video에서 embodiment-agnostic intent representation을 학습해 robot skill acquisition으로 옮긴다. INDI와 마찬가지로 action surface가 아니라 intent를 다루지만, INDI는 frozen teacher의 executed-segment interpretation을 VLA decoder에 직접 distill한다.

2. **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** (2025), [project](https://research.nvidia.com/labs/gear/gr00t-n1/)
   Vision-language-action robot foundation model 계열의 backbone이다. INDI는 GR00T-N1.7을 main student로 써 intent objective가 backbone-independent supervision으로 작동할 수 있는지를 보인다.

3. **π0: A Vision-Language-Action Flow Model for General Robot Control** (2024), [arXiv:2410.24164](https://arxiv.org/abs/2410.24164)
   VLM과 continuous action flow model을 결합한 general robot-control architecture다. INDI의 comparison/extension target이며, language-conditioned action model에 latent intent supervision을 넣는 효과를 비교할 기준이다.

4. **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** (2023), [arXiv:2307.15818](https://arxiv.org/abs/2307.15818)
   web-scale vision-language knowledge를 robot action으로 transfer하는 대표 VLA다. INDI의 문제는 이런 policy가 instruction을 알아도 execution의 local objective/progress를 충분히 표현하는가에 있다.

5. **Open X-Embodiment / RT-X** (2023), [project](https://robotics-transformer-x.github.io/)
   여러 robot embodiment/dataset을 모은 generalist robot learning data effort다. Intent target이 embodiment-specific motor coordinates보다 더 transfer-friendly한지 시험할 data background를 제공한다.

6. **RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots** (2024), [arXiv:2406.02523](https://arxiv.org/abs/2406.02523)
   kitchen manipulation을 대규모로 제공하는 benchmark다. INDI의 24-task RoboCasa Kitchen 결과를 해석할 때 macro average와 data scale·task distribution을 함께 봐야 한다.

7. **SimplerEnv: A Framework for Bridging Simulated and Real Robot Learning** (2024), [arXiv:2405.03107](https://arxiv.org/abs/2405.03107)
   simulation benchmark evaluation을 real robot relevance와 연결하려는 framework다. INDI의 SimplerEnv-Bridge success는 useful하지만 real-world table-top trial을 대체하지는 않는다.

8. **R3M: A Universal Visual Representation for Robot Manipulation** (2022), [arXiv:2203.12601](https://arxiv.org/abs/2203.12601)
   robot manipulation의 transferable visual representation 학습을 다룬다. INDI의 frozen visual encoder endpoint target은 action policy가 visual outcome representation을 가지게 하는 auxiliary grounding과 관련된다.

9. **Behavior Cloning and Imitation Learning literature**
   Demonstrated action을 직접 map하는 VLA baseline의 근간이다. INDI는 BC를 버리기보다 action loss 위에 intent/visual/text grounding objective를 추가한다는 점을 기억해야 한다.

10. **Representation distillation / privileged-information learning**
    Training에서만 rich evidence를 teacher가 보고 deployment student가 compressed target을 복구하는 일반 패턴이다. INDI의 핵심 위험은 privileged future execution이 reusable intent가 아니라 train-distribution shortcut으로 증류될 가능성이다.

## 비교 질문

- RT-2/π0/GR00T 계열 action representation에 intent bottleneck을 넣으면 backbone별 gain이 유지되는가?
- LUCID 같은 human-video intent prior와 INDI의 teacher-generated intent는 data cost·embodiment transfer에서 어떤 차이가 있는가?
- RoboCasa success를 safety, recovery, force/contact metric으로 확장하면 intent supervision의 효과가 남는가?
