---
title: "Data Pyramid for Embodied Manipulation"
source_url: "https://arxiv.org/html/2607.24744"
hf_url: "https://huggingface.co/papers/2607.24744"
arxiv_id: "2607.24744"
arxiv_url: "https://arxiv.org/abs/2607.24744"
pdf_url: "https://arxiv.org/pdf/2607.24744"
week: "2026-W31"
ingested_at_kst: "2026-07-29 09:40:46 KST"
selected_reason: "HF 2026-W31 후보 중 VLA/embodied manipulation 데이터 레시피를 직접 다루며, VLA for AD 학습 커리큘럼의 dataset/benchmark 및 representation transfer 축을 확장한다."
---

# Data Pyramid for Embodied Manipulation — 참고 레퍼런스 요약

> Semantic Scholar references endpoint는 이 실행 시점에 `data: []`를 반환했다. 따라서 arXiv HTML 본문과 논문이 언급한 대표 dataset/model family를 기준으로 핵심 참고문헌을 정리한다.

## 1. Open X-Embodiment / RT-X 계열

- 관계: real-robot data를 multi-institution/multi-robot scale로 모으는 대표 사례.
- 요약: 여러 robot embodiment와 task를 통합해 generalist robot policy를 학습하려는 흐름이다. Data pyramid에서 apex real-robot layer의 규모 확장을 보여준다.
- 연결: VLA가 action grounding을 얻기 위해 필요한 “실제 robot action supervision”의 대표적 기반.

## 2. DROID: Distributed Robot Interaction Dataset

- 관계: 다양한 환경에서 teleoperation으로 real-robot manipulation demonstration을 모으는 데이터셋.
- 요약: lab 밖 다양성을 높여 distribution shift를 줄이려는 시도다. 데이터 품질, diversity, collection scalability의 균형 문제를 잘 보여준다.
- 연결: 자율주행의 naturalistic driving logs와 유사하게 real-world variability가 강점이다.

## 3. ALOHA / Mobile ALOHA

- 관계: leader-follower bimanual teleoperation과 low-cost robot data collection의 대표 사례.
- 요약: 인간 조작자가 leader device로 follower robot을 제어해 고품질 manipulation trajectory를 만든다.
- 연결: real-robot data는 action label이 명확하지만 hardware-specific이므로 cross-embodiment reuse가 challenge다.

## 4. Universal Manipulation Interface (UMI)

- 관계: 논문 피라미드의 두 번째 계층인 UMI-style data의 anchor.
- 요약: robot 없이 hand-held tool/end-effector 중심으로 demonstration을 수집하고 robot으로 retarget한다.
- 연결: real-robot collection cost를 낮추면서 action-like supervision을 얻는 중간층이다.

## 5. Ego4D / EPIC-KITCHENS / human egocentric video 계열

- 관계: egocentric/exocentric human interaction data의 대표 예.
- 요약: 인간이 실제 환경에서 물체와 상호작용하는 긴 영상을 제공해 affordance, task decomposition, temporal reasoning을 학습하게 한다.
- 연결: VLA의 language reasoning과 high-level plan에는 유용하지만 executable robot action label은 별도 alignment가 필요하다.

## 6. RoboCasa / LIBERO / Meta-World 등 simulation benchmark

- 관계: simulation data 계층의 대표 source.
- 요약: task generation, state/action label, privileged supervision, closed-loop rollout evaluation을 가능하게 한다.
- 연결: failure/recovery, rare event, counterfactual interaction을 안전하게 만들 수 있지만 sim-to-real gap이 있다.

## 7. GR00T / Motus 계열 embodied foundation model

- 관계: 논문이 언급하는 hierarchical/pyramid-like data recipe의 실제 모델 사례.
- 요약: general VL, simulation, robot trajectory 등 heterogeneous data를 섞어 embodied policy를 학습한다.
- 연결: data pyramid 관점은 이런 모델들의 recipe를 비교하기 위한 공통 좌표계를 제공한다.

## 8. Vision-Language-Action Survey / VLA4AD taxonomy

- 관계: VLA model family를 이해하기 위한 taxonomy reference.
- 요약: language가 instruction, reasoning, scene description, action generator, teacher/distillation signal로 쓰이는 방식을 구분한다.
- 연결: 본 논문은 VLA architecture가 아니라 VLA를 가능하게 하는 data layer를 설명한다.

## 9. World Model / World-Action Model 논문군

- 관계: action-conditioned future prediction과 policy learning 사이의 연결고리.
- 요약: image/latent/occupancy-based future modeling은 embodied agent가 action consequence를 예측하도록 돕는다.
- 연결: data pyramid에서 simulation, real-robot trajectory, action-free video가 world-action model에 어떻게 기여하는지 설명한다.

## 10. Tactile / force-feedback manipulation datasets

- 관계: 논문이 future challenge로 강조하는 scarce modality.
- 요약: contact-rich manipulation에서는 RGB만으로 grasp stability, slip, material property를 알기 어렵다.
- 연결: 안전한 dexterous VLA에는 tactile feedback과 failure/recovery trajectory가 점점 중요해진다.
