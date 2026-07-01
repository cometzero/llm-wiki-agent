---
title: "Self-Improvement Loop"
type: concept
tags: [robotics, training, vla]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
Self-improvement loop은 residual-corrected rollout을 [[VLA]] supervised fine-tuning (SFT) 데이터으로 재사용하여 base model을 iterative로 개선하는 기법이다.

## Process
1. Base VLA + residual로 rollout 실행
2. 성공한 trajectory 수집
3. 이 데이터를 base VLA SFT에 추가
4. 개선된 base VLA로 다시 residual 학습

## Connections
- [[ObjectCentricResidualRL]] — implementation
- [[VLA]] — base policy improvement
- [[SupervisedFineTuning]] — training method
