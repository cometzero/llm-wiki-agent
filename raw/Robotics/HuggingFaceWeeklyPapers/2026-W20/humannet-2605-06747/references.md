---
title: "HumanNet: 인간 중심 비디오 학습을 100만 시간 규모로 확장하기 — references"
source_url: "https://arxiv.org/abs/2605.06747"
hf_url: "https://huggingface.co/papers/2605.06747"
arxiv_id: "2605.06747"
arxiv_url: "https://arxiv.org/abs/2605.06747"
pdf_url: "https://arxiv.org/pdf/2605.06747"
week: "2026-W20"
ingested_at_kst: "2026-05-13 09:40:08 KST"
selected_reason: "현재 주차(2026-W20) 후보 중 VLA/embodied learning 관련성이 가장 높고, 로봇 데이터 병목을 인간 중심 비디오로 우회하는 데이터 스케일링 관점이 VLA 학습 전략과 직접 연결됨."
---

# HumanNet 참고 레퍼런스 요약

Semantic Scholar references endpoint가 이 신규 arXiv 항목에 대해 아직 reference를 반환하지 않아, 원문 Related Work와 본문 citation에 명시된 주요 문헌을 중심으로 정리했다.

| Reference | 링크 | HumanNet과의 관계 |
|---|---|---|
| Ego4D | https://ego4d-data.org/ | egocentric video가 narration, forecasting, hand-object interaction 학습에 유용함을 보여준 대표 corpus |
| EPIC-KITCHENS | https://epic-kitchens.github.io/ | kitchen egocentric activity dataset; actor-centered intent와 hand-object contact의 중요성을 보여줌 |
| Ego-Exo4D | https://ego-exo4d-data.org/ | first-person과 third-person paired view가 skilled activity 이해에 중요함을 제시 |
| HOI4D | https://hoi4d.github.io/ | hand-object geometry와 dense interaction supervision을 강조하는 dataset |
| Open X-Embodiment / RT-X | https://robotics-transformer-x.github.io/ | heterogeneous robot logs를 통한 robot foundation model scaling의 대표 사례; HumanNet은 human-video side scaling으로 보완 |
| DROID | https://droid-dataset.github.io/ | real-world robot manipulation dataset; HumanNet의 “robot data는 비싸다”는 문제의식과 연결 |
| R3M | https://sites.google.com/view/robot-r3m/ | passive human video representation이 robot manipulation에 transfer될 수 있음을 보인 선행 연구 |
| EgoMimic | 원문 citation 참조 | egocentric human trace와 robot demonstration alignment를 통한 imitation learning 방향 |
| GR00T N1 | https://developer.nvidia.com/isaac/gr00t | heterogeneous robot/human data mixture를 쓰는 VLA/robot foundation model 계열 |
| LingBot-VLA | 원문 citation 참조 | HumanNet validation에서 사용한 VLA post-training architecture/protocol의 기반 |

## 읽기 우선순위

1. R3M / EgoMimic: human video가 robot policy prior가 되는 원리
2. Ego4D / Ego-Exo4D: egocentric/exocentric viewpoint 설계
3. Open X-Embodiment / DROID: robot data scale의 현실적 한계
4. GR00T / LingBot-VLA: heterogeneous data를 VLA post-training에 섞는 방법
