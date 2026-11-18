---
title: "ScaleVLA 핵심 참고문헌 9편"
source_url: "https://arxiv.org/html/2611.21607v1"
hf_url: "https://huggingface.co/papers/2611.21607"
arxiv_id: "2611.21607"
arxiv_url: "https://arxiv.org/abs/2611.21607v1"
pdf_url: "https://arxiv.org/pdf/2611.21607v1"
week: "2026-W47"
ingested_at_kst: "2026-11-18 09:48:21 KST"
selected_reason: "Current-week new VLA paper: frozen frontier representation, numerical action, generalization and deployment latency"
license: "CC BY 4.0"
authors: "Ruixi Yu et al. (12 authors; see metadata.json)"
document_role: "references"
---

# ScaleVLA 핵심 참고문헌 9편

## 수집 및 검증 방식

2026-11-18 KST에 Semantic Scholar `arXiv:2611.21607/references?fields=title,authors,year,externalIds,url&limit=1000`를 호출했으나 **HTTP 404 / Paper not found**였습니다. 빈 응답을 참고문헌이 없다는 의미로 해석하지 않고, arXiv v1 HTML의 bibliography **101개**에서 다음 9개를 선별했습니다. 원문 bibliography의 번호/제목/identifier를 기준으로 연결했습니다. 아래 요약은 각 연구가 ScaleVLA에서 맡는 역할에 대한 한국어 설명이며, 이 job에서 9편 모두를 full deep-read하거나 결과를 독립 재현한 것은 아닙니다. 전체 추출 서지는 `metadata.json`의 `bibliography`에 보존합니다.

원문 서지: https://arxiv.org/html/2611.21607v1#bib

## 1. GR00T N1 — Action expert 구조의 출발점

- 원문 번호 **[4]**, Johan Bjorck, Fernando Castañeda et al., *GR00T N1: An Open Foundation Model for Generalist Humanoid Robots*, 2025.
- arXiv: **2503.14734**, https://arxiv.org/abs/2503.14734
- VLM의 의미 representation과 continuous action expert를 연결하는 foundation-policy 설계를 읽을 출발점입니다. ScaleVLA는 GR00T-inspired action-expert interface를 쓰되 비교에서 pretrained robot-action expert를 가져오지 않습니다.
- 구분: 실제 head architecture는 원문 [58]의 **GR00T N1.7**을 따른다고 명시합니다. N1 원 논문과 N1.7 release를 같은 version으로 취급하지 않습니다. N1.7 code/model reference: https://github.com/NVIDIA/Isaac-GR00T

## 2. π0 — Continuous flow-based VLA

- 원문 번호 **[5]**, Kevin Black, Noah Brown, Danny Driess et al., *π0: A Vision-Language-Action Flow Model for General Robot Control*, 2024.
- arXiv: **2410.24164**, https://arxiv.org/abs/2410.24164
- Language/vision conditioning을 continuous action generation과 연결하는 flow-based policy 계보입니다. ScaleVLA의 noise→action vector field를 이해하는 데 유용합니다.
- 관계: 둘 다 continuous action에 grounding하지만 ScaleVLA의 핵심 비교는 frozen backbone 규모이며 일반적인 multi-robot pretrained policy 전체를 같은 조건으로 다시 학습한 비교는 아닙니다.

## 3. Diffusion Policy — Action chunk를 generative object로 보기

- 원문 번호 **[13]**, Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song, *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*, RSS 2023.
- DOI: **10.15607/RSS.2023.XIX.026**, https://doi.org/10.15607/RSS.2023.XIX.026
- 하나의 action을 point estimate로 예측하는 대신 future action sequence를 generative model로 표현하는 배경입니다. Multi-modal action distribution과 receding-horizon execution을 이해하는 데 도움이 됩니다.
- 관계: ScaleVLA는 flow matching과 4 integration step을 사용하므로 원래 diffusion noise schedule이나 sampler를 그대로 쓴다고 생각하면 안 됩니다. DexJoCo published DP-T 결과와 본 연구의 backbone-controlled 결과도 구분합니다.

## 4. Knowledge Insulating VLA — Action learning과 VLM knowledge 보존

- 원문 번호 **[18]**, Danny Driess, Jost Tobias Springenberg, Brian Ichter, Lili Yu et al., *Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better*, 2025.
- arXiv: **2505.23705**, https://arxiv.org/abs/2505.23705
- Action expert gradient가 foundation knowledge에 어떻게 작용하는지, policy adaptation과 pretrained VLM capability를 어떻게 분리할지 묻는 관련 연구입니다.
- 관계: ScaleVLA는 backbone을 freeze해 action-side만 학습하고 feature cache를 재사용합니다. Knowledge insulation과 frozen feature transfer를 개념적으로 비교할 수 있지만 두 training recipe가 동일하다는 뜻은 아닙니다.

## 5. OpenVLA — Action-token 계열과의 비교 기준

- 원문 번호 **[36]**, Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti et al., *OpenVLA: An Open-Source Vision-Language-Action Model*, CoRL.
- 원문 bibliography의 primary venue URL: https://proceedings.mlr.press/v270/kim25c.html
- Pretrained visual/language model의 robot adaptation, action tokenization, 공개 policy의 출발점입니다. ScaleVLA related work는 DINOv2/SigLIP feature와 token action 계열의 사례로 연결합니다.
- 관계: ScaleVLA Table 2의 OpenVLA는 published result입니다. 동일 backbone/data/budget controlled comparison의 한 행이 아닙니다. Numerical flow head와 autoregressive action token의 generation contract를 비교해 읽습니다.

## 6. Flow Matching for Generative Modeling — Loss의 수학적 배경

- 원문 번호 **[46]**, Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matthew Le, *Flow Matching for Generative Modeling*, ICLR 2023.
- Primary paper: https://openreview.net/pdf?id=PqvMRDCJT9t
- Probability path를 따라가는 vector field를 regress하고 적분해 sample을 생성하는 수학적 배경입니다. ScaleVLA의 식 (1)은 noise에서 demonstrated action으로 가는 straight path velocity를 condition부로 학습합니다.
- 관계: Generation flow time과 robot physical execution time은 다릅니다. 네 integration update가 네 physical robot command를 의미하지 않습니다.

## 7. LIBERO — Language-conditioned task/knowledge transfer 평가

- 원문 번호 **[47]**, Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone, *LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning*, NeurIPS Datasets and Benchmarks 2023.
- arXiv: **2306.03310**, https://arxiv.org/abs/2306.03310
- Language-conditioned manipulation을 Spatial/Object/Goal/Long의 서로 다른 요구로 나누어 평가합니다.
- 관계: ScaleVLA는 각 suite 10 task/50 initial states와 four-suite mean을 사용하고 Goal/Long에서 demonstration-budget sweep을 합니다. 원 benchmark의 lifelong-learning 모든 protocol을 수행했다는 뜻은 아닙니다.

## 8. RoboCasa — OOD kitchen generalization

- 원문 번호 **[54]**, Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, Yuke Zhu, *RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots*, RSS 2024.
- Primary paper: https://robocasa.ai/assets/robocasa_rss24.pdf
- Everyday kitchen scene/task의 다양성을 통해 policy generalization을 평가하는 simulation 기반입니다.
- 관계: ScaleVLA는 24 task, task당 50 episode, generated demonstration 30/100개에서 OOD kitchen SR을 측정합니다. RoboCasa timing은 별도 backend/configuration으로 수행하므로 성공률과 timing 경로의 equivalence를 자동 가정하지 않습니다.

## 9. LIBERO-PRO — Memorization 밖 perturbation 검증

- 원문 번호 **[100]**, Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang, Duanfeng Chu, Pan Zhou, Lichao Sun, *LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization*, 2025.
- arXiv: **2510.03827**, https://arxiv.org/abs/2510.03827
- 익숙한 task 성공이 환경/object 변화 아래에도 유지되는지 점검하는 benchmark입니다.
- 관계: ScaleVLA는 LIBERO-trained policy를 retraining 없이 3 perturbation setting에서 평가합니다. 평균 45.1%는 원래 LIBERO 96.1%와 다른 평가이며, Object-Env에서는 최상위가 아닙니다. OOD task SR은 safety certificate가 아닙니다.

## 읽기 순서

Diffusion Policy → Flow Matching → π0/GR00T → OpenVLA/Knowledge Insulation → LIBERO/LIBERO-PRO/RoboCasa → ScaleVLA Table 7/9 및 Appendix B/C 순으로 읽으면 **action representation, foundation knowledge, measurement protocol**을 분리하기 쉽습니다.

## 보조 taxonomy anchor — 선별 참고문헌 9편과 별개

2026-11-18에 확인한 WorldBench의 VA/VLA taxonomy를 적용하되 ScaleVLA는 manipulation 연구라는 범위를 유지합니다. Numerical action generation과 representation transfer의 관점에서 읽고, vehicle closed-loop 검증으로 확대하지 않습니다.

- https://worldbench.github.io/vla4ad
- https://raw.githubusercontent.com/worldbench/awesome-vla-for-ad/main/README.md
