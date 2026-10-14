---
title: "GroundingPI"
type: entity
tags: [robotics, vla, visual-grounding, foundation-model]
sources: [groundingpi-2609-39601]
last_updated: 2026-10-14
---

# GroundingPI

Qize Yu 외의 *GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives* (arXiv:2609.39601)이다. MoonViT-V2→projector→Qwen3-4B와 shared coordinate vocabulary를 통해 precise language-conditioned perception을 학습한다. 전체 multimodal parameter는 약 4.844B다.

## 핵심 결과와 범위

- 34 benchmark·11 capability·44 baseline 비교의 Grounding Avg 73.68%; 이는 uniform benchmark dominance가 아니다.
- nuScenes front image+ego history→6 cumulative metric waypoint, mean open-loop L2 0.296 m. Vehicle closed-loop/control safety는 평가하지 않았다.
- Manipulation은 normalized depth 8개의 feature→common resampler→fixed flow-matching Action DiT다. Four OOD conditions와 limited-demonstration efficiency에서 전이를 보인다.
- Dense grounding은 broad marginal value를 보이지만 OCR catalyst, architecture cause, integrated System-1/2 deployment는 hypothesis다. Robot experiment는 simulation이고 physical vehicle/robot deployment는 없다.

## 문서

- [[groundingpi-2609-39601-paper-ko]] — 핵심 본문과 주요 부록 기술 번역.
- [[groundingpi-2609-39601-analysis]] — taxonomy·action interface·evaluation·deployment 경계.
- [[groundingpi-2609-39601-references]] — 9개 핵심 문헌 지도.
- [[groundingpi-2609-39601-learning]] — token/metric convention·GRPO·flow matching 학습.

## 관련 연결

- [[PreciseGroundingTransfer]] — perception-native foundation의 transfer 원리.
- [[VisionLanguageAction]] / [[AutonomousDrivingVLA]] — executable numerical action learner로 adaptation.
- [[StarVLA]] / [[FlowMatching]] — matched backbone-to-action interface.
- [[PerturBot]] / [[MotorMind]] — 각각 training evidence와 runtime execution을 다루는 상보적 연구.

## 출처

https://arxiv.org/html/2609.39601v1
