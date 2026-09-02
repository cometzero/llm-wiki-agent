---
title: "PonderPounce 참고 문헌: VLA memory·demonstration conditioning·slow-fast control"
document_type: references
source_url: https://arxiv.org/html/2608.24115
hf_url: https://huggingface.co/papers/2608.24115
arxiv_id: "2608.24115"
arxiv_url: https://arxiv.org/abs/2608.24115
pdf_url: https://arxiv.org/pdf/2608.24115
week: "2026-W36"
ingested_at_kst: "2026-09-02 09:40:54 KST"
selected_reason: "PonderPounce의 contextual memory와 action-interface design을 이해하는 핵심 reference를 정리한다."
---

# PonderPounce 참고 레퍼런스 논문 요약

> Semantic Scholar `ARXIV:2608.24115/references` endpoint와 원문 reference를 바탕으로, memory representation·context-to-control·benchmark 축에서 10개를 골랐다.

1. **RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies** — [arXiv:2603.04639](https://arxiv.org/abs/2603.04639)
   - Counting, Permanence, Reference, Imitation으로 robot policy memory를 분해하는 PonderPounce의 main benchmark다. 단순 current-frame policy의 큰 gap과 simulator-derived reasoning label의 성격을 해석하는 출발점이다.

2. **RoboTTT: Context Scaling for Robot Policies** — [arXiv:2607.15275](https://arxiv.org/abs/2607.15275)
   - VLA history를 fast weight로 압축하는 test-time-training 계열이다. PonderPounce가 transformer causal context에 history를 두는 것과 달리 parameter update로 context를 보존한다.

3. **MEM: Multi-Scale Embodied Memory for Vision Language Action Models** — [arXiv:2603.03596](https://arxiv.org/abs/2603.03596)
   - short video와 recursive language memory를 결합하는 VLA memory 방법이다. Native MLLM context를 별도 external memory 없이 쓰려는 PonderPounce의 직접 비교 배경이다.

4. **MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation** — [arXiv:2508.19236](https://arxiv.org/abs/2508.19236)
   - observation VLM summary/cognitive token을 external memory bank에서 retrieve/fuse한다. PonderPounce도 cognition token을 쓰지만, bank/retrieval을 두지 않고 append-only MLLM context에 history를 유지한다.

5. **SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos** — [arXiv:2606.02745](https://arxiv.org/abs/2606.02745)
   - cross-embodiment demonstration video를 future visual trace/latent plan으로 grounding한다. PonderPounce의 RoboCasa-DC comparison과 demonstration conditioning 문제를 연결한다.

6. **Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference** — [arXiv:2605.02739](https://arxiv.org/abs/2605.02739)
   - slow VLM reasoning과 fast action policy 사이의 latent interface 효율을 다룬다. PonderPounce의 continuous cognition+age channel을 latency 관점에서 비교할 기준이다.

7. **Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System** — [arXiv:2604.24921](https://arxiv.org/abs/2604.24921)
   - 비동기 coarse-to-fine VLA learning을 연구한다. PonderPounce의 독립 clock과 latest-ready scheduling이 single-system synchronous control보다 필요한 이유를 이해하게 한다.

8. **StreamVLA: Breaking the Reason-Act Cycle via Completion-State Gating** — [arXiv:2602.01100](https://arxiv.org/abs/2602.01100)
   - reasoning/action cycle을 completion-state gating으로 조절한다. PonderPounce의 transition gate와 fresh cognition delivery를 설계할 때 관련되는 streaming control 축이다.

9. **Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation** — [arXiv:2512.20188](https://arxiv.org/abs/2512.20188)
   - whole-body robot에서 slow semantic policy와 fast motor policy를 분리하는 선행 계열이다. PonderPounce는 persistent episode context와 recurrent continuous routing을 강조한다.

10. **Running VLAs at Real-time Speed** — [arXiv:2510.26742](https://arxiv.org/abs/2510.26742)
    - VLA deployment latency를 시스템 차원에서 다루는 reference다. PonderPounce의 p50 숫자는 batch-1 kernel profile이므로 complete control-loop deadline/throughput으로 확대 해석하지 않아야 한다.
