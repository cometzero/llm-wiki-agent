---
title: "WorldLeague 핵심 참고문헌 9편"
source_url: "https://arxiv.org/html/2611.30989v1"
hf_url: "https://huggingface.co/papers/2611.30989"
arxiv_id: "2611.30989"
arxiv_url: "https://arxiv.org/abs/2611.30989"
pdf_url: "https://arxiv.org/pdf/2611.30989"
week: "2026-W48"
ingested_at_kst: "2026-11-25 09:43:23 KST"
selected_reason: "Current-week HF rank 4, 88 votes in pre-run snapshot; VLM/VLA/WAM closed-loop goal-achievement benchmark; independent exact ID/title duplicate searches found no raw/wiki analysis. Benchmark taxonomy rather than a driving policy."
license: "CC BY 4.0"
authors: ["Xinyang Zhou", "Qi Li", "Xinchao Wang"]
translation_scope: "Independently worded Korean analysis / educational material with source attribution"
---

# WorldLeague 참고문헌 지도

## 확보 경로와 범위

Semantic Scholar references endpoint는 HTTP 200으로 62개 record를 반환했습니다. 원문 HTML bibliography는 63개이며 API 결과와 원문이 일치하는 완전한 목록이라고 가정하지 않았습니다. 아래 9편은 원문 bibliography 번호와 직접 대조해 골랐습니다. 요약은 선택 논문의 관계 중심 해설이며 해당 9편의 새 전문 번역이나 별도 재현은 아닙니다. Author initials는 원문 그대로 보존합니다.

## [1] SayCan — Do As I Can, Not As I Say

- 원문 식별 정보: [1] M. Ahn, A. Brohan, N. Brown, Y. Chebotar, O. Cortes, B. David, C. Finn, C. Fu, K. Gopalakrishnan, K. Hausman, et al. (2022) Do as i can, not as i say: grounding language in robotic affordances . arXiv preprint arXiv:2204.01691 .
- 링크: [2204.01691](https://arxiv.org/abs/2204.01691)

언어가 제안한 skill과 robot affordance를 함께 고려해 수행 가능한 행동을 고르는 접근입니다. WorldLeague의 2.2는 action interface가 agent의 책임을 정한다는 맥락에서 인용합니다. Whole skill 선택과 motion target/parameter 선택을 같은 control 능력으로 평가하지 않도록 비교해야 합니다.

## [2] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- 원문 식별 정보: [2] M. Assran, A. Bardes, D. Fan, Q. Garrido, R. Howes, M. Muckley, A. Rizvi, C. Roberts, K. Sinha, A. Zholus, et al. (2025) V-jepa 2: self-supervised video models enable understanding, prediction and planning . arXiv preprint arXiv:2506.09985 .
- 링크: [2506.09985](https://arxiv.org/abs/2506.09985)

Video의 latent prediction을 understanding·planning으로 연결하는 연구입니다. WorldLeague는 V-JEPA 2-AC 같은 action-conditioned planner를 geometry/recovery에 적용하는 것을 future work로 제안합니다. 실제 WorldLeague에서 이 planner의 개선을 이미 측정했다는 뜻은 아닙니다.

## [9] Show-Harness: Just a VLM Agent Can Play Robots

- 원문 식별 정보: [9] Y. Chen, Z. Bai, Z. Cao, W. Zeng, K. Q. Lin, Y. Lin, G. Liang, K. Y. Ma, Q. Huang, and M. Z. Shou (2026) Show-harness: just a vlm agent can play robots . arXiv preprint arXiv:2609.10522 .
- 링크: [2609.10522](https://arxiv.org/abs/2609.10522)

VLM이 고른 motion command를 embodiment-specific interpreter로 변환하는 harness입니다. WorldHarness의 직접적인 기반이며 R1 mobile base·trunk·arm·gripper와 execution receipt를 연결합니다. Harness의 자동 recovery나 skill 범위가 agent에게 남기는 결정을 바꾼다는 점이 핵심입니다.

## [15] ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop

- 원문 식별 정보: [15] Y. Hong, J. Liu, H. Yin, M. Li, L. Guibas, L. Fei-Fei, J. Wu, and Y. Choi (2026) ESI-bench: towards embodied spatial intelligence that closes the perception-action loop . arXiv preprint arXiv:2605.18746 .
- 링크: [2605.18746](https://arxiv.org/abs/2605.18746)

물리적 interaction으로 공간 질문의 증거를 수집하는 평가입니다. WorldLeague의 47개 scene record가 이 계보를 따르지만 평가 goal은 물리적 달성으로 바뀝니다. 같은 scene에서 QA 정답과 실제 outcome이 다를 수 있다는 비교의 출발점입니다.

## [18] Inner Monologue: Embodied Reasoning through Planning with Language Models

- 원문 식별 정보: [18] W. Huang, F. Xia, T. Xiao, H. Chan, J. Liang, P. Florence, A. Zeng, J. Tompson, I. Mordatch, Y. Chebotar, et al. (2022) Inner monologue: embodied reasoning through planning with language models . arXiv preprint arXiv:2207.05608 .
- 링크: [2207.05608](https://arxiv.org/abs/2207.05608)

실행 결과 feedback을 language planning loop로 되돌려주는 접근입니다. WorldHarness의 command→receipt→새 decision 구조와 비교할 때 feedback의 유무와 feedback 이후 실제 recovery 달성을 구분하게 합니다.

## [19] π0.5: A Vision-Language-Action Model with Open-World Generalization

- 원문 식별 정보: [19] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, et al. (2025) π 0.5 \pi_{0.5} : A vision-language-action model with open-world generalization . arXiv preprint arXiv:2504.16054 .
- 링크: [2504.16054](https://arxiv.org/abs/2504.16054)

Vision/language를 native action generation으로 연결하는 generalist VLA 계열입니다. 원문에서는 R1Pro SFT deployment를 평가합니다. VLM+motion-harness와 native policy의 shared-goal 비교는 가능하지만 robot과 controller가 다르다는 confound를 유지해야 합니다.

## [20] OpenVLA: An Open-Source Vision-Language-Action Model

- 원문 식별 정보: [20] M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. Foster, G. Lam, P. Sanketi, et al. (2024) Openvla: an open-source vision-language-action model . arXiv preprint arXiv:2406.09246 .
- 링크: [2406.09246](https://arxiv.org/abs/2406.09246)

Instruction과 visual observation에서 robot action을 직접 생성하는 VLA의 대표 사례로 도입에서 인용됩니다. WorldLeague의 benchmark가 OpenVLA 자체를 주표 baseline으로 평가했다는 뜻은 아닙니다. Language explanation과 executable action의 차이를 익히는 배경입니다.

## [21] BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation

- 원문 식별 정보: [21] C. Li, R. Zhang, J. Wong, C. Gokmen, S. Srivastava, R. Martín-Martín, C. Wang, G. Levine, M. Lingelbach, J. Sun, et al. (2023) Behavior-1k: a benchmark for embodied ai with 1,000 everyday activities and realistic simulation . In Conference on Robot Learning , pp. 80–93 .
- 링크: [원 출판 기록](https://proceedings.mlr.press/v205/li23a.html)

WorldLeague가 사용하는 household layout·asset·simulation 생태계의 기반입니다. Activity별 달성을 다루는 평가에서 동일 activity 안의 memory·geometry·recovery 요구를 분해하는 평가로 이동하는 차이를 비교할 수 있습니다.

## [63] World Action Models Are Zero-Shot Policies — DreamZero

- 원문 식별 정보: [63] S. Ye, Y. Ge, K. Zheng, S. Gao, S. Yu, G. Kurian, S. Indupuru, Y. L. Tan, C. Zhu, J. Xiang, et al. (2026) World action models are zero-shot policies . arXiv preprint arXiv:2602.15922 .
- 링크: [2602.15922](https://arxiv.org/abs/2602.15922)

Future visual dynamics와 action을 연결하는 WAM 계열입니다. WorldLeague의 관련 연구는 native action chunk로 interaction하고 결과를 관측하는 접근으로 설명합니다. 예측이 그럴듯한 것과 goal 달성은 별개이며, DreamZero 자체가 주표의 Awomo/OpenWAM 결과를 의미하지는 않습니다.

## 읽는 순서

OpenVLA/π0.5로 native action을 확인하고 SayCan/Inner Monologue/Show-Harness로 agent–controller 경계를 읽습니다. BEHAVIOR-1K/ESI-Bench로 평가 단위를 비교한 뒤 DreamZero/V-JEPA 2로 prediction과 physical outcome의 차이를 정리합니다.
