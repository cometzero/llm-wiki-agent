---
    title: "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System — references"
    source_url: "https://arxiv.org/abs/2606.18112"
    hf_url: "https://huggingface.co/papers/2606.18112"
    arxiv_id: "2606.18112"
    arxiv_url: "https://arxiv.org/abs/2606.18112"
    pdf_url: "https://arxiv.org/pdf/2606.18112"
    week: "2026-W27"
    category: "raw/Robotics/HuggingFaceWeeklyPapers"
    ingested_at_kst: "2026-07-01 09:40:38 KST"
    selected_reason: "2026-W27 후보 중 자율주행·navigation·VLM/VLA 접점이 가장 직접적이며, NAVSIM closed-loop autonomous driving까지 평가한 Qwen3-VL 기반 scalable navigation model."
    ---

# Qwen-RobotNav 참고 레퍼런스 정리

Semantic Scholar references endpoint와 논문 본문 맥락에서 추출한 주요 연결 논문입니다.

- **AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning** (2026) — Hang Yin, Yinan Liang, Jiazhao Zhang, Jiahang Liu. https://www.semanticscholar.org/paper/ac8b13fe74185db968be794e74e0999ca2851ca5
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Lifelong embodied navigation in dynamic environments requires robots to form persistent scene understanding from fragmentary observations, which remains difficult for existing methods that rely on explicit maps or scene graphs and struggle to generalize beyond structured settings. We propose AllDayNav, a lifelong self-learning navigation framework that implicitly encodes scene dynamics into the billion-scale paramete
- **Planning-aligned Token Compression for Long-Context Autonomous Driving** (2026) — Zhixuan Liang, Yuxiao Chen, Yurong You, Peter Karkus. https://www.semanticscholar.org/paper/96dc7510ae1cab59cdb2dfc087a32d725c00438d
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Monolithic vision-action models represent an emerging paradigm in autonomous driving. However, this architecture produces token sequences that quickly exceed real-time computational budgets when encoding extended temporal context for complex interactions. While approaches like linear transformers and external memory try to make the context lightweight, token compression is most compatible with the architecture as it 
- **GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation** (2026) — Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jian Dong. https://www.semanticscholar.org/paper/797b5845ba4d5ea8c72d406186cd07b693a77258
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Embodied navigation connects intelligent agents with the physical world and is fundamental for general robotic intelligence. Limited availability and quality of navigation data have constrained Vision-and-Language Navigation (VLN) systems'generalization and long-horizon capabilities. To address this, we curate diverse 3D scenes and develop an automated pipeline for large-scale navigation data, resulting in the GN-Mat
- **Memory Centric Power Allocation for Multi-Agent Embodied Question Answering** (2026) — Chengyang Li, Shuai Wang, Kejiang Ye, Weijie Yuan. https://www.semanticscholar.org/paper/b39b7e5152a059fe06f720b2f3ded2350090f471
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: This paper considers multi-agent embodied question answering (MA-EQA), which aims to query robot teams on what they have seen over a long horizon. In contrast to existing edge resource management methods that emphasize sensing, communication, or computation performance metrics, MA-EQA emphasizes the memory qualities. To cope with this paradigm shift, we propose a quality of memory (QoM) model based on generative adve
- **Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting** (2026) — Zi-Xiang Xia, Jing Xu, C. Cui, Yuanhong Yu. https://www.semanticscholar.org/paper/bcaa9e780fd21ee325511ea708a479d7526124ac
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Training embodied AI agents depends critically on the visual fidelity of simulation environments and the ability to model dynamic humans. Current simulators rely on mesh-based rasterization with limited visual realism, and their support for dynamic human avatars, where available, is constrained to mesh representations, hindering agent generalization to human-populated real-world scenarios. We present Habitat-GS, a na
- **FAST-EQA: Efficient Embodied Question Answering with Global and Local Region Relevancy** (2026) — Haochen Zhang, Nirav Savaliya, Faizan Siddiqui, Enna Sachdeva. https://www.semanticscholar.org/paper/6f29b0a65e4f822380390b63087d2da6bc96ef2a
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Embodied Question Answering (EQA) combines visual scene understanding, goal-directed exploration, spatial and temporal reasoning under partial observability. A central challenge is to confine physical search to question-relevant subspaces while maintaining a compact, actionable memory of observations. Furthermore, for real-world deployment, fast inference time during exploration is crucial. We introduce FAST-EQA, a q
- **ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation** (2026) — Zedong Chu, Shichao Xie, Xiaolong Wu, Yanfen Shen. https://www.semanticscholar.org/paper/a06d27aa66483cca708e0e924438b62d415172e8
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Embodied navigation has long been fragmented by task-specific architectures. We introduce ABot-N0, a unified Vision-Language-Action (VLA) foundation model that achieves a ``Grand Unification''across 5 core tasks: Point-Goal, Object-Goal, Instruction-Following, POI-Goal, and Person-Following. ABot-N0 utilizes a hierarchical ``Brain-Action''architecture, pairing an LLM-based Cognitive Brain for semantic reasoning with 
- **VLN-MME: Diagnosing MLLMs as Language-guided Visual Navigation agents** (2025) — Xunyi Zhao, G. Zhou, Qi Wu. https://www.semanticscholar.org/paper/1ba6a97335a6ebde13617cd8a4d2233dac542fd9
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities across a wide range of vision-language tasks. However, their performance as embodied agents, which requires multi-round dialogue spatial reasoning and sequential action prediction, needs further exploration. Our work investigates this potential in the context of Vision-and-Language Navigation (VLN) by introducing a unified and extensib
- **ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving** (2025) — Qihang Peng, Xuesong Chen, Chen Yang, Shaoshuai Shi. https://www.semanticscholar.org/paper/049b9036c5c702b2eb694603ba0dd0510f2c37d6
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Autonomous driving requires generating safe and reliable trajectories from complex multimodal inputs. Traditional modular pipelines separate perception, prediction, and planning, while recent end-to-end (E2E) systems learn them jointly. Vision-language models (VLMs) further enrich this paradigm by introducing cross-modal priors and commonsense reasoning, yet current VLM-based planners face three key challenges: (i) a
- **AstraNav-World: World Model for Foresight Control and Consistency** (2025) — Junjun Hu, Jintao Chen, Haochen Bai, Minghua Luo. https://www.semanticscholar.org/paper/e3d3a9a51b8d8384d748ddab4b04be2a641b6574
  - 관계: Qwen-RobotNav가 navigation foundation model·VLN·autonomous driving trajectory planning·agentic navigation 평가 축과 직접 비교하거나 배경으로 삼는 작업입니다.
  - 요약: Embodied navigation in open, dynamic environments demands accurate foresight of how the world will evolve and how actions will unfold over time. We propose AstraNav-World, an end-to-end world model that jointly reasons about future visual states and action sequences within a unified probabilistic framework. Our framework integrates a diffusion-based video generator with a vision-language policy, enabling synchronized

## 읽는 순서
1. VLN/embodied navigation foundation model 계열: ABot-N0, GN0, VLNVerse.
2. Autonomous driving trajectory/planning 계열: Planning-aligned token compression, ColaVLA.
3. Agentic navigation/EQA 계열: FAST-EQA, memory-centric EQA.
