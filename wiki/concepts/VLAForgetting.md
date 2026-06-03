---
title: "VLA Forgetting"
type: concept
tags: [vla, training, forgetting]
sources: [robosemanticbench-2606-02277-references]
last_updated: 2026-06-03
---

[[VLAForgetting]]은 VLA(Vision-Language-Action) 모델 학습 중 기존 능력(특히 [[SemanticGrounding]])이 손실되는 현상이다.

## 관련 연구

- **UAM** (Jianke Zhang et al., arXiv:2605.15735) — dual-stream 관점에서의 VLA forgetting 분석
- **Actions as Language** (Asher Hancock et al.) — catastrophic forgetting 없이 VLM→VLA 변환 연구

## 해결 접근
- [[AttentionRecalibration]] — train-free attention recalibration으로 forgetting 방지
- [[LangForce]] — latent action queries로 분해
