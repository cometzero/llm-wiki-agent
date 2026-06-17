---
title: "APT"
type: entity
tags: [vla, robotics, action-expert]
sources: [apt-action-expert-pretraining-2606-12366]
last_updated: 2026-06-17
---

## Overview
APT(Action Expert PreTraining)는 continuous action expert 기반 [[VisionLanguageAction]] policy의 OOD instruction generalization을 개선하기 위한 two-stage training method다.

## Key Facts
- Stage 1: language 없이 visual tokens로 action expert를 VA prior로 pretrain한다.
- Stage 2: gated fusion으로 language tokens를 주입해 language-conditioned likelihood를 학습한다.
- 핵심 raw/source: [[apt-action-expert-pretraining-2606-12366]].

## Connections
- [[ActionExpertPretraining]] — APT의 핵심 학습 절차.
- [[ActionGrounding]] — instruction이 continuous action expert에 실제로 반영되는지의 문제.
- [[OpenVLA]], [[GR00T-N1]] — 관련 VLA architecture comparison anchor.
