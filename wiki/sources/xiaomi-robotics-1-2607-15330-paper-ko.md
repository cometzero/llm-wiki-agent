---
title: "Xiaomi-Robotics-1 한국어 기술 번역"
type: source
tags: [robotics, vla, translation, scaling, action-grounding]
date: 2026-07-22
last_updated: 2026-07-22
source_url: "https://arxiv.org/html/2607.15330"
hf_url: "https://huggingface.co/papers/2607.15330"
arxiv_url: "https://arxiv.org/abs/2607.15330"
pdf_url: "https://arxiv.org/pdf/2607.15330"
week: "2026-W30"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W30/xiaomi-robotics-1-scaling-vla-2607-15330/paper-ko.md
source_hash: 0ec67d35e44f6cba
---

## Summary

이 소스는 Xiaomi-Robotics-1 원문의 Abstract, Introduction, Model/Training, Experiments, Related Work, Conclusion과 주요 figure caption을 한국어로 기술 번역한 문서다. 핵심 내용은 100K+ 시간 UMI trajectory를 [[StateTransitionCaptioning]]으로 라벨링하고, [[Qwen3-VL]] + [[DiT]]/[[DiffusionTransformer]] action generator를 pre-training한 뒤 cross-embodiment post-training으로 실제 로봇 instruction following에 맞춘다는 것이다.

## Key Claims
- [[Xiaomi-Robotics-1]]은 robot VLA에서도 data/model scaling이 실제 out-of-the-box manipulation 성능으로 이전될 수 있음을 보여준다.
- State-transition caption은 task label보다 action grounding에 가까운 supervision을 제공한다.
- [[RoboCasa365]] 및 [[RoboDojo]] 결과는 simulation generalization 측면의 성능 이전을 뒷받침한다.

## Key Quotes
> "로봇 VLA도 scale한다" — 번역본의 핵심 해석.

> "state transition description은 action learning에 풍부하고 정확한 conditioning 신호를 제공한다" — pre-training recipe 해석.

## Connections
- [[Xiaomi-Robotics-1]] — 대상 모델.
- [[StateTransitionCaptioning]] — 핵심 데이터 라벨링 방식.
- [[ActionChunking]] — 모델 출력 표현.
- [[CrossEmbodimentLearning]] — post-training 목표.
- [[RoboCasa365]] / [[RoboDojo]] — 평가 benchmark.

## Contradictions
- 기존 wiki 내용과 직접적인 충돌은 확인되지 않았다.
