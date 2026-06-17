---
title: "APT: Action Expert Pretraining으로 VLA의 Instruction Generalization 개선하기 — references"
source_url: "https://arxiv.org/abs/2606.12366"
hf_url: "https://huggingface.co/papers/2606.12366"
arxiv_id: "2606.12366"
arxiv_url: "https://arxiv.org/abs/2606.12366"
pdf_url: "https://arxiv.org/pdf/2606.12366"
week: "2026-W25"
ingested_at_kst: "2026-06-17 09:40:19 KST"
selected_reason: "현재 주(2026-W25) 후보 중 VLA/VLM/action expert 구조를 직접 다루며, continuous action expert가 언어 불균형 때문에 OOD instruction generalization에 실패하는 원인을 Bayesian factorization과 two-stage pretraining으로 분석한다."
---

# APT: Action Expert Pretraining으로 VLA의 Instruction Generalization 개선하기 참고 레퍼런스 정리

Semantic Scholar references endpoint와 arXiv HTML bibliography를 먼저 시도했다. 신생 arXiv 항목이라 Semantic Scholar가 비어 있거나 404인 경우, 원문 reference/context와 논문 내 언급을 기준으로 핵심 레퍼런스를 선별했다.

## 핵심 레퍼런스 5–10개

### π0 / π0.5

- 관계: continuous action expert 기반 generalist robot policy 계열. APT가 적용 가능한 대표 architecture family다.
- 이 논문을 읽을 때의 역할: π0 / π0.5은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### GR00T-style architecture

- 관계: NVIDIA 계열 VLA stack. APT는 π 계열뿐 아니라 GR00T-style에도 적용 가능하다고 주장한다.
- 이 논문을 읽을 때의 역할: GR00T-style architecture은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### OpenVLA

- 관계: discrete action token 기반 VLA baseline. continuous expert와 대비되는 language co-training 장점을 보여주는 reference 축이다.
- 이 논문을 읽을 때의 역할: OpenVLA은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### LIBERO / LIBERO-Plus

- 관계: simulation manipulation benchmark. unseen instruction 및 compositional generalization 평가에 사용된다.
- 이 논문을 읽을 때의 역할: LIBERO / LIBERO-Plus은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### Visual shortcut learning

- 관계: 언어 지시보다 visual cue에 의존하는 failure mode. APT의 핵심 문제 정의다.
- 이 논문을 읽을 때의 역할: Visual shortcut learning은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### Bayesian policy factorization

- 관계: π(a|v,l)를 VA prior와 language-conditioned likelihood로 나누는 이론적 틀.
- 이 논문을 읽을 때의 역할: Bayesian policy factorization은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### Diffusion action expert

- 관계: continuous action sequence 생성을 위한 action module. APT의 Stage 1 pretraining 대상이다.
- 이 논문을 읽을 때의 역할: Diffusion action expert은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

### Gated multimodal fusion

- 관계: VLM feature와 action expert feature를 layer-wise gate로 결합하는 설계. visuomotor prior 보존과 language conditioning의 균형을 만든다.
- 이 논문을 읽을 때의 역할: Gated multimodal fusion은/는 본 논문의 baseline, backbone, benchmark 또는 문제 정의를 이해하기 위한 anchor다.

## Semantic Scholar에서 확인된 references 샘플

- **${\pi}_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities** (2026) — Physical Intelligence, Bo Ai, A. Amin, Raichelle J. Aniceto. citations=38. arXiv:2604.15483
  - 요약: We present a new robotic foundation model, called ${\pi}_{0.7}$, that can enable strong out-of-the-box performance in a wide range of scenarios. ${\pi}_{0.7}$ can follow diverse language instructions in unseen environments, including multi-stage tasks with various kitchen appliances, provide zero-shot cross-embodiment generalization, for example en
- **CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation** (2026) — Max Fu, Justin Yu, Karim El-Refai, Ethan Kou. citations=10. arXiv:2603.22435
  - 요약: "Code-as-Policy"considers how executable code can complement data-intensive Vision-Language-Action (VLA) methods, yet their effectiveness as autonomous controllers for embodied manipulation remains underexplored. We present CaP-X, an open-access framework for systematically studying Code-as-Policy agents in robot manipulation. At its core is CaP-Gy
- **Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking** (2026) — David Emukpere, Romain Deffayet, J. Renders. citations=1. arXiv:2602.24143 / DOI:10.48550/arXiv.2602.24143
  - 요약: Vision-language action (VLA) policies often report strong manipulation benchmark performance with relatively few demonstrations, but it remains unclear whether this reflects robust language-to-object grounding or reliance on object--location correlations that do not transfer beyond the training distribution. We present a controlled multi-object pic
- **When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs** (2026) — Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu. citations=6. arXiv:2602.17659 / DOI:10.48550/arXiv.2602.17659
  - 요약: Vision-Language-Action models (VLAs) promise to ground language instructions in robot control, yet in practice often fail to faithfully follow language. When presented with instructions that lack strong scene-specific supervision, VLAs suffer from counterfactual failures: they act based on vision shortcuts induced by dataset biases, repeatedly exec
- **VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model** (2026) — Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren. citations=21. arXiv:2602.10098 / DOI:10.48550/arXiv.2602.10098
  - 요약: Pretraining Vision-Language-Action (VLA) policies on internet-scale video is appealing, yet current latent-action objectives often learn the wrong thing: they remain anchored to pixel variation rather than action-relevant state transitions, making them vulnerable to appearance bias, nuisance motion, and information leakage. We introduce VLA-JEPA, a
- **Causal World Modeling for Robot Control** (2026) — Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang. citations=88. arXiv:2601.21998 / DOI:10.48550/arXiv.2601.21998
  - 요약: This work highlights that video world modeling, alongside vision-language pre-training, establishes a fresh and independent foundation for robot learning. Intuitively, video world models provide the ability to imagine the near future by understanding the causality between actions and visual dynamics. Inspired by this, we introduce LingBot-VA, an au
- **A Pragmatic VLA Foundation Model** (2026) — Wei Wu, Fan Lu, Yunnan Wang, Shuai Yang. citations=38. arXiv:2601.18692 / DOI:10.48550/arXiv.2601.18692
  - 요약: Offering great potential in robotic manipulation, a capable Vision-Language-Action (VLA) foundation model is expected to faithfully generalize across tasks and platforms while ensuring cost efficiency (e.g., data and GPU hours required for adaptation). To this end, we develop LingBot-VLA with around 20,000 hours of real-world data from 9 popular du
- **LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries** (2026) — Shijie Lian, Bin Yu, Xiaopeng Lin, L. T. Yang. citations=12. arXiv:2601.15197 / DOI:10.48550/arXiv.2601.15197
  - 요약: Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable fro

## arXiv HTML bibliography 추출 샘플

- [1] S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, et al. (2025) Qwen3-vl technical report . arXiv preprint arXiv:2511.21631 . Cited by: Appendix A , Appendix A , Appendix C , §2 , §3.1 , §3.3 .
- [2] L. Beyer, A. Steiner, A. S. Pinto, A. Kolesnikov, X. Wang, D. Salz, M. Neumann, I. Alabdulmohsin, M. Tschannen, E. Bugliarello, et al. (2024) Paligemma: a versatile 3b vlm for transfer . arXiv preprint arXiv:2407.07726 . Cited by: Appendix C , §2 , §3.1 .
- [3] J. Bjorck, F. Castañeda, N. Cherniadev, X. Da, R. Ding, L. Fan, Y. Fang, D. Fox, F. Hu, S. Huang, et al. (2025) Gr00t n1: an open foundation model for generalist humanoid robots . arXiv preprint arXiv:2503.14734 . Cited by: §1 , §1 , §1 , §2 , §3.1 , §3.1 , §4.1.4 .
- [4] J. Bjorck, F. Castañeda, N. Cherniadev, X. Da, R. Ding, L. Fan, Y. Fang, D. Fox, F. Hu, S. Huang, et al. (2025) GR00T n1.5: an improved open foundation model for generalist humanoid robots . Cited by: §1 , §1 , §2 , §2 , §3.1 , §4.1.4 .
- [5] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, et al. (2024) π 0 \pi_{0} : A vision-language-action flow model for general robot control . arXiv preprint arXiv:2410.24164 . Cited by: Appendix C , Table 4 , Table 5 , §1 , §1 , §1 , §2 , §3.1 , §3.1 , §4.1.2 , Table 1 , §4.1.4 .
- [6] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, et al. (2023) RT-1: robotics transformer for real-world control at scale . Robotics: Science and Systems (RSS) . Cited by: §2 .
- [7] Q. Bu, J. Cai, L. Chen, X. Cui, Y. Ding, S. Feng, S. Gao, X. He, X. Hu, X. Huang, et al. (2025) Agibot world colosseo: a large-scale manipulation platform for scalable and intelligent embodied systems . arXiv preprint arXiv:2503.06669 . Cited by: 2nd item , §2 .
- [8] Q. Bu, H. Li, L. Chen, J. Cai, J. Zeng, H. Cui, M. Yao, and Y. Qiao (2024) Towards synergistic, generalized, and efficient dual-system for robotic manipulation . arXiv preprint arXiv:2410.08001 . Cited by: §2 .
- [9] Q. Bu, Y. Yang, J. Cai, S. Gao, G. Ren, M. Yao, P. Luo, and H. Li (2025) Univla: learning to act anywhere with task-centric latent actions . arXiv preprint arXiv:2505.06111 . Cited by: Appendix C , Table 4 , Table 5 .
- [10] J. Cen, C. Yu, H. Yuan, Y. Jiang, S. Huang, J. Guo, X. Li, Y. Song, H. Luo, F. Wang, et al. (2025) WorldVLA: towards autoregressive action world model . arXiv preprint arXiv:2506.21539 . Cited by: Appendix C , Table 4 , §2 .
