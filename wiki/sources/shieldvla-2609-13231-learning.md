---
title: "ShieldVLA 핵심 기술 학습 자료"
type: source
tags: [vla, safety, learning-guide, hamilton-jacobi]
date: 2026-09-23
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W39/shieldvla-safety-alignment-2609-13231/learning.md
source_hash: dfb5a3b732e6bde6
---

## Summary
학습 자료는 rubric score, HJ reachability critic, feasibility gate, deployment fallback을 단계별로 설명한다. 자율주행 전이에는 camera-only scorer 대신 BEV·occupancy·map·rule·uncertainty를 포함해야 한다고 명시한다.

## Key Claims
- VLM scorer는 action controller가 아니라 training-side safety signal 생산자다.
- threshold calibration은 success, cumulative safety cost, intervention rate를 함께 봐야 한다.

## Connections
- [[ShieldVLA]] — 학습 대상.

## Contradictions
- 긍정 safety value는 단순 collision-free 판정과 동의어가 아니다.
