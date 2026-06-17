---
title: "APT: Action Expert Pretraining으로 VLA의 Instruction Generalization 개선하기"
type: source
tags: [vla, robotics, action-expert, instruction-generalization, language-grounding]
sources: []
date: 2026-06-17
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W25/apt-action-expert-pretraining-2606-12366/paper-ko.md
source_hash: 5aeed1267e9f8390
---

## Summary
APT는 VLA policy를 language-agnostic Vision-Action prior와 language-conditioned likelihood로 factorization하고, action expert를 먼저 VA prior로 pretrain한 뒤 gated language fusion을 적용해 OOD instruction generalization을 개선한다.

## Key Claims
- Continuous action expert는 VLA data의 language imbalance 때문에 visual shortcut을 학습하기 쉽다.
- Stage 1 VA prior pretraining과 Stage 2 gated fusion은 π-style 및 GR00T-style VLA 구조 모두에 적용된다.
- LIBERO/LIBERO-Plus와 real robot task에서 unseen/compositional instruction generalization 향상을 보고한다.

## Connections
- [[apt-action-expert-pretraining-2606-12366-analysis]]
- [[ActionExpertPretraining]]
- [[APT]]
- [[VisionLanguageAction]]
- [[ActionGrounding]]

## Contradictions
- 없음 — 기존 [[VisionLanguageAction]], [[ActionGrounding]], [[WorldActionModel]] 흐름을 보완한다.
