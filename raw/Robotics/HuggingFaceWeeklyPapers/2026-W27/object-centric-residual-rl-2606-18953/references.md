---
    title: "Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — references"
    source_url: "https://arxiv.org/abs/2606.18953"
    hf_url: "https://huggingface.co/papers/2606.18953"
    arxiv_id: "2606.18953"
    arxiv_url: "https://arxiv.org/abs/2606.18953"
    pdf_url: "https://arxiv.org/pdf/2606.18953"
    week: "2026-W27"
    category: "raw/Robotics/HuggingFaceWeeklyPapers"
    ingested_at_kst: "2026-07-01 09:40:38 KST"
    selected_reason: "Vision-Language-Action 정책의 real-world robustness와 zero-shot sim-to-real residual RL을 직접 다루는 신규 VLA 논문."
    ---

# Object-Centric Residual RL 참고 레퍼런스 정리

Semantic Scholar references endpoint와 논문 본문에서 확인한 주요 연결 논문입니다.

- **π*0.6: a VLA That Learns From Experience** (2025) — Physical Intelligence, A. Amin, Raichelle J. Aniceto, Ashwin Balakrishna. https://www.semanticscholar.org/paper/319e005858f32a7b1eddb05a62b1652ca8ea4611
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from
- **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** (2025) — Wenli Xiao, Haotian Lin, Andy Peng, Haoru Xue. https://www.semanticscholar.org/paper/14c584af2fda0b9b5851b1e8573c4e2dd2c8fd0b
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: Supervised fine-tuning (SFT) has become the de facto post-training strategy for large vision-language-action (VLA) models, but its reliance on costly human demonstrations limits scalability and generalization. We propose Probe, Learn, Distill (PLD), a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection. In Stage 1, we train lightwe
- **Residual Off-Policy RL for Finetuning Behavior Cloning Policies** (2025) — Lars Ankile, Zhenyu Jiang, Rocky Duan, Guanya Shi. https://www.semanticscholar.org/paper/c61186e5ffe02954118d97bf845e1d1af431c34d
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: Recent advances in behavior cloning (BC) have enabled impressive visuomotor control policies. However, these approaches are limited by the quality of human demonstrations, the manual effort required for data collection, and the diminishing returns from offline data. In comparison, reinforcement learning (RL) trains an agent through autonomous interaction with the environment and has shown remarkable success in variou
- **π0.5: a Vision-Language-Action Model with Open-World Generalization** (2025) — Physical Intelligence, Kevin Black, Noah Brown, James Darpinian. https://www.semanticscholar.org/paper/1e2a82ef5e0325a26ca0344c4f8c256c52fae7ec
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $\pi_{0.5}$, a new model based on $\pi_{0}$ that uses co-training on heterogeneous tasks to enable broad 
- **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** (2025) — Nvidia, Johan Bjorck, Fernando Castañeda, Nikita Cherniadev. https://www.semanticscholar.org/paper/731c50b0d6af4c1cb8d95f506541681ea487973b
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: General-purpose robots need a versatile body and an intelligent mind. Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world. A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world variability, and rapidly learn new tasks.
- **Refined Policy Distillation: From VLA Generalists to RL Experts** (2025) — T. Jülg, Wolfram Burgard, Florian Walter. https://www.semanticscholar.org/paper/887ffb482d574cc053213f14da7a80006170e72d
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a c
- **SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model** (2025) — Delin Qu, Haoming Song, Qizhi Chen, Yuanqi Yao. https://www.semanticscholar.org/paper/10301766e5686bda76722ef2af1362213b934cc0
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adapti
- **π0: A Vision-Language-Action Flow Model for General Robot Control** (2024) — Kevin Black, Noah Brown, Danny Driess, A. Esmail. https://www.semanticscholar.org/paper/7e7e59d2e247d99954081080ddd5aae93d10b9e0
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: Robot learning holds tremendous promise to unlock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the deepest questions in artificial intelligence. However, bringing robot learning to the level of generality required for effective real-world systems faces major obstacles in terms of data, generalization, and robustness. In this paper, we discuss how generalist robot
- **SAM 2: Segment Anything in Images and Videos** (2024) — Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu. https://www.semanticscholar.org/paper/92a09cdfc19f3f582d89c28c1b4f386299cc69e1
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: We present Segment Anything Model 2 (SAM 2), a foundation model towards solving promptable visual segmentation in images and videos. We build a data engine, which improves model and data via user interaction, to collect the largest video segmentation dataset to date. Our model is a simple transformer architecture with streaming memory for real-time video processing. SAM 2 trained on our data provides strong performan
- **From Imitation to Refinement - Residual Rl for Precise Assembly** (2024) — Lars Ankile, A. Simeonov, Idan Shenfeld, M. Torné. https://www.semanticscholar.org/paper/d8f75adfc48528833a6fc5fa0dcc6e856016a243
  - 관계: 이 논문이 VLA backbone, residual RL, sim-to-real transfer, pose/segmentation 기반 deployment를 구성할 때 직접 참조하는 배경 작업입니다.
  - 요약: Recent advances in Behavior Cloning (BC) have made it easy to teach robots new tasks. However, we find that the ease of teaching comes at the cost of unreliable performance that saturates with increasing data for tasks requiring precision. The performance saturation can be attributed to two critical factors: (a) distribution shift resulting from the use of offline data and (b) the lack of closed-loop corrective contr

## 읽는 순서
1. OpenVLA / π0 / π0.5 / GR00T-N1: base VLA family 이해.
2. Residual RL / ResFiT / ResiP: imitation policy refinement 이해.
3. SAM2 / FoundationPose: object-centric observation을 현실에서 얻는 perception stack 이해.
