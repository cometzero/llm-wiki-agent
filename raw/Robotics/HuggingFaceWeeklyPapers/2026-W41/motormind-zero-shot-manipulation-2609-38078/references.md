---
title: "MotorMind 핵심 참고 레퍼런스"
source_url: "https://arxiv.org/html/2609.38078v1"
hf_url: "https://huggingface.co/papers/2609.38078"
arxiv_id: "2609.38078"
arxiv_url: "https://arxiv.org/abs/2609.38078"
pdf_url: "https://arxiv.org/pdf/2609.38078"
week: "2026-W41"
ingested_at_kst: "2026-10-07T09:48:44.755963+09:00"
selected_reason: "범용 VLM을 mid-level robot action과 asynchronous execution feedback에 연결하는 높은 관련도·득표수의 신규 VLA/robotics 논문"
---

# MotorMind 핵심 참고 레퍼런스

Semantic Scholar `arXiv:2609.38078/references` endpoint 조회가 성공했고 full-paper bibliography와 대조해 아래 8편을 선택했습니다. 서지·식별자는 endpoint/원문에 근거합니다. 관계 요약은 선택 논문에서 인용한 맥락에 근거하며 모든 참고논문 PDF를 독립적으로 정독했다는 뜻은 아닙니다.

## 1. Code as Policies: Language Model Programs for Embodied Control

- 연도: 2022
- 링크: https://arxiv.org/abs/2209.07753
- arXiv / DOI: 2209.07753 / 10.1109/ICRA48891.2023.10160591
- 요약 및 본 논문과의 관계: program을 action API에 연결하는 language-model robot control 계열입니다. MotorMind는 전체 code 생성·revision 대신 parameterized mid-level proposal과 feedback loop를 사용하므로 latency와 control contract 비교에 중요합니다.

## 2. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

- 연도: 2023
- 링크: https://arxiv.org/abs/2307.05973
- arXiv / DOI: 2307.05973 / 10.48550/arXiv.2307.05973
- 요약 및 본 논문과의 관계: 언어 instruction을 composable 3D value map 및 motion planning에 연결하는 공간 grounding 계열입니다. MotorMind가 별도 learned grounding/planning tool dependency를 줄이려는 이유를 비교합니다.

## 3. OpenVLA: An Open-Source Vision-Language-Action Model

- 연도: 2024
- 링크: https://arxiv.org/abs/2406.09246
- arXiv / DOI: 2406.09246 / 10.48550/arXiv.2406.09246
- 요약 및 본 논문과의 관계: pretrained vision-language knowledge를 learned robot action policy로 적응시키는 공개 VLA 계열입니다. frozen generic VLM에 controller를 연결하는 MotorMind와 학습·representation 경계가 다릅니다.

## 4. π0.5: a Vision-Language-Action Model with Open-World Generalization

- 연도: 2025
- 링크: https://arxiv.org/abs/2504.16054
- arXiv / DOI: 2504.16054 / 10.48550/arXiv.2504.16054
- 요약 및 본 논문과의 관계: open-world generalization을 지향하는 learned VLA policy이며 direct baseline 및 agent의 low-level tool로 사용됩니다. backbone adaptation history와 target-domain fine-tuning 여부를 구별하는 기준입니다.

## 5. LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

- 연도: 2025
- 링크: https://arxiv.org/abs/2510.03827
- arXiv / DOI: 2510.03827 / 10.48550/arXiv.2510.03827
- 요약 및 본 논문과의 관계: memorization 밖의 instruction/object/position/task perturbation 평가를 제공합니다. MotorMind zero-shot robustness claim의 benchmark이며 canonical nominal success만으로 transfer를 평가하는 한계를 줄입니다.

## 6. Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents

- 연도: 2026
- 링크: https://arxiv.org/abs/2607.08448
- arXiv / DOI: 2607.08448 / 10.48550/arXiv.2607.08448
- 요약 및 본 논문과의 관계: frozen VLA와 primitive를 memory-guided agent로 조합합니다. MotorMind의 no learned action model interface와 비교할 수 있고 task-specific exploration memory cost를 별도로 읽어야 합니다.

## 7. Show-Harness: Just a VLM Agent Can Play Robots

- 연도: 2026
- 링크: https://arxiv.org/abs/2609.10522
- arXiv / DOI: 2609.10522 / 확인 안 됨
- 요약 및 본 논문과의 관계: 범용 VLM을 robot plugin에 연결하는 concurrent harness 연구입니다. 원문은 sequencing, motion magnitude, proactive interruption의 차이를 설명하지만 직접 성능 비교를 제공하지 않습니다.

## 8. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

- 연도: 2026
- 링크: https://arxiv.org/abs/2603.22435
- arXiv / DOI: 2603.22435 / 10.48550/arXiv.2603.22435
- 요약 및 본 논문과의 관계: coding-agent robot manipulation의 benchmarking·iterative improvement를 다룹니다. main zero-shot baseline이며 repeated program generation과 short action proposal의 execution 구조를 비교합니다.
