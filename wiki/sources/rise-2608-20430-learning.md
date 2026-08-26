---
title: "RISE 학습 노트: selective imagination과 자율주행 WAM"
type: source
tags: [autonomous-driving, world-action-model, learning]
date: 2026-08-26
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W35/rise-adaptive-imagination-2608-20430/learning.md
source_hash: c5c1cc9a44eebfc8
---

## Summary
이 학습 노트는 observation encoding, latent rollout, risk/gain evaluation, Roll/Stop gating, diffusion trajectory planning의 흐름과 stopping-time 표현을 설명한다. 또한 open-loop와 closed-loop evaluation, gate calibration 및 deployment safety checklist를 제시한다.

## Key Claims
- adaptive imagination은 prefix마다 additional rollout utility를 재평가한다.
- action grounding은 future latent에서 ego trajectory로 이어지는 numerical planning chain이다.
- production deployment에는 uncertainty-aware fallback과 device-level latency measurement가 필요하다.

## Connections
- autonomous-driving world-model study material이다.

## Contradictions
- 없음.
