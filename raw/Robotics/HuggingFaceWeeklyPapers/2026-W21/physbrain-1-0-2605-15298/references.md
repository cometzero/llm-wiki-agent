---
title: "PhysBrain 1.0 기술 보고서: 인간 egocentric video에서 물리 상식 supervision을 추출해 VLA로 전이하기 — references"
source_url: "https://arxiv.org/abs/2605.15298"
hf_url: "https://huggingface.co/papers/2605.15298"
arxiv_id: "2605.15298"
arxiv_url: "https://arxiv.org/abs/2605.15298"
pdf_url: "https://arxiv.org/pdf/2605.15298"
week: "2026-W21"
ingested_at_kst: "2026-05-20 09:40:06 KST"
selected_reason: "현재 주(2026-W21) 후보 중 VLA 정책의 physical commonsense, human egocentric video 기반 supervision, capability-preserving VLA adaptation을 다뤄 VLA/embodied action grounding 학습에 직접적으로 중요함."
---

# 참고 레퍼런스 논문 요약

## 1. OpenVLA

- 링크/식별자: arXiv / VLA policy
- 관계: VLM을 robot policy로 전이하는 대표 baseline. PhysBrain은 단순 robot trajectory imitation보다 physical commonsense pretraining 후 adaptation을 강조한다.

## 2. π0 / Pi0

- 링크/식별자: Physical Intelligence VLA policy
- 관계: generalist robot action generation 계열의 강력한 baseline. PhysBrain은 human-derived physics prior가 policy 성능과 out-of-domain robustness를 끌어올릴 수 있음을 비교한다.

## 3. GR00T N1 / GR00T N1.6

- 링크/식별자: NVIDIA robotics foundation model
- 관계: 대규모 embodied policy baseline. PhysBrain 결과표에서 강한 비교군으로 등장하며, human video 기반 physical supervision의 경쟁력을 판단하는 기준이다.

## 4. Ego4D

- 링크/식별자: CVPR 2022
- 관계: human first-person interaction video source. PhysBrain은 이 영상들을 generic caption이 아니라 structured physical meta-information으로 변환한다.

## 5. EgoDex

- 링크/식별자: arXiv:2505.11709
- 관계: egocentric video에서 dexterous manipulation을 학습하는 연구. PhysBrain의 egocentric-to-robot transfer 맥락과 가깝다.

## 6. EPIC-KITCHENS

- 링크/식별자: ECCV/IJCV
- 관계: human activity video source. PhysBrain은 action label을 넘어 depth/spatial/action execution QA로 재주석한다.

## 7. VGGT

- 링크/식별자: CVPR 2025
- 관계: camera parameter/depth-related cues를 추정하는 foundation model 계열. PhysBrain의 camera motion filtering 및 depth-aware augmentation에 연결된다.

## 8. SimplerEnv

- 링크/식별자: CoRL 2024
- 관계: VLA/robot policy simulation benchmark. PhysBrain의 out-of-domain 성능 주장의 핵심 평가장이다.

## 9. LIBERO

- 링크/식별자: NeurIPS 2023
- 관계: long-horizon manipulation benchmark. PhysBrain의 embodied control transfer를 평가하는 주요 benchmark다.

## 10. RoboCasa / RoboCasa-GR1

- 링크/식별자: RSS 2024 / robotics benchmark
- 관계: 다양한 가정형 manipulation task를 제공하며, PhysBrain의 VLA adaptation 성능 비교에 쓰인다.
