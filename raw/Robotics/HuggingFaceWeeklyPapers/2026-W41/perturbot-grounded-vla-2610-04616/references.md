---
title: "PerturBot 핵심 참고 레퍼런스"
source_url: "https://arxiv.org/html/2610.04616v1"
hf_url: "https://huggingface.co/papers/2610.04616"
arxiv_id: "2610.04616"
arxiv_url: "https://arxiv.org/abs/2610.04616"
pdf_url: "https://arxiv.org/pdf/2610.04616"
week: "2026-W41"
ingested_at_kst: "2026-10-07T09:48:44.759073+09:00"
selected_reason: "current-week VLA의 evidence grounding·shortcut robustness와 unchanged-inference training을 다루어 deployment reliability 학습에 적합"
---

# PerturBot 핵심 참고 레퍼런스

Semantic Scholar `arXiv:2610.04616/references` endpoint 조회가 성공했고 full-paper bibliography와 대조해 아래 8편을 선택했습니다. 서지·식별자는 endpoint/원문에 근거합니다. 관계 요약은 선택 논문에서 인용한 맥락에 근거하며 모든 참고논문 PDF를 독립적으로 정독했다는 뜻은 아닙니다.

## 1. Shortcut learning in deep neural networks

- 연도: 2020
- 링크: https://arxiv.org/abs/2004.07780
- arXiv / DOI: 2004.07780 / 10.1038/s42256-020-00257-z
- 요약 및 본 논문과의 관계: 학습 분포에서 쉬운 predictive cue를 사용하는 모델이 distribution shift에서 실패할 수 있다는 기본 틀입니다. 세 modality shortcut을 이해하는 출발점입니다.

## 2. Object-Aware Regularization for Addressing Causal Confusion in Imitation Learning

- 연도: 2021
- 링크: https://arxiv.org/abs/2110.14118
- arXiv / DOI: 2110.14118 / 확인 안 됨
- 요약 및 본 논문과의 관계: imitation으로 expert action을 맞추어도 원인이 아닌 correlation을 사용할 수 있다는 문제를 다룹니다. successful demo만으로 intended evidence를 식별하기 어려운 rationale에 연결됩니다.

## 3. Fighting Copycat Agents in Behavioral Cloning from Observation Histories

- 연도: 2020
- 링크: https://arxiv.org/abs/2010.14876
- arXiv / DOI: 2010.14876 / 확인 안 됨
- 요약 및 본 논문과의 관계: observation history의 familiar past action에 의존하는 behavioral-cloning 문제를 다룹니다. PerturBot의 motor inertia와 outcome-sensitive branch coverage를 비교합니다.

## 4. π0.5: a Vision-Language-Action Model with Open-World Generalization

- 연도: 2025
- 링크: https://arxiv.org/abs/2504.16054
- arXiv / DOI: 2504.16054 / 10.48550/arXiv.2504.16054
- 요약 및 본 논문과의 관계: flow-matching 기반 continuous action VLA 계열입니다. PerturBot이 새로운 action decoder가 아니라 기존 policy loss와 inference를 보존하는 data intervention임을 이해하는 baseline입니다.

## 5. RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

- 연도: 2025
- 링크: https://arxiv.org/abs/2506.18088
- arXiv / DOI: 2506.18088 / 10.48550/arXiv.2506.18088
- 요약 및 본 논문과의 관계: strong domain randomization을 가진 bimanual manipulation data generator/benchmark입니다. Full과 Clean2Random, broader skill와 noun-lock-in probe의 평가 기반입니다.

## 6. PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training

- 연도: 2025
- 링크: https://arxiv.org/abs/2503.06486
- arXiv / DOI: 2503.06486 / 10.48550/arXiv.2503.06486
- 요약 및 본 논문과의 관계: perturbative visual training으로 multimodal hallucination을 줄이는 선행 연구입니다. PerturBot은 이를 executable action과 valid demonstration supervision으로 확장하고 GF는 stability/sensitivity를 함께 요구합니다.

## 7. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

- 연도: 2026
- 링크: https://arxiv.org/abs/2609.12641
- arXiv / DOI: 2609.12641 / 확인 안 됨
- 요약 및 본 논문과의 관계: LIT는 pose-grounded latent interface로 vision-action shortcut을 완화합니다. PerturBot의 data/evaluation intervention과 다른 representation-level 접근이며 기존 wiki 분석과 이어집니다.

## 8. When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

- 연도: 2026
- 링크: https://arxiv.org/abs/2602.17659
- arXiv / DOI: 2602.17659 / 10.48550/arXiv.2602.17659
- 요약 및 본 논문과의 관계: VLA가 instruction보다 vision prior를 따르는 counterfactual failure를 평가·완화하는 연구입니다. salient cue를 피하면서 changed instruction에도 적절히 반응해야 한다는 논점을 연결합니다.
