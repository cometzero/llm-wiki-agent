---
title: "ShieldVLA: VLA를 위한 실행가능성 인지 안전 정렬"
type: source
tags: [vla, safety-alignment, hamilton-jacobi, robotics]
date: 2026-09-23
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W39/shieldvla-safety-alignment-2609-13231/paper-ko.md
source_hash: 4ea93cef3e216e2a
---

## Summary
ShieldVLA는 VLM rubric이 만든 visual safety margin을 HJ reachability safety critic으로 학습하고, feasible state에서는 task reward를, infeasible state에서는 safety value를 높이는 gradient를 적용하는 VLA fine-tuning 방법이다. deployment에서 VLM scorer를 제거하며, 다섯 closed-loop navigation/manipulation benchmark에서 SafeVLA 대비 평균 CSC 57% 감소와 SR +0.13을 보고한다.

## Key Claims
- Safety를 soft expected-cost penalty가 아니라 recoverable feasible-set 판단으로 다룬다.
- Per-frame VLM rubric은 sparse collision signal보다 contact 이전 위험을 제공하려 한다.
- Learned critic은 visual shift, rubric quality, replay coverage에 한계가 있어 formal system safety guarantee가 아니다.

## Connections
- [[ShieldVLA]] — 안전 정렬 방법.
- [[VLA]] — action-policy 계열.

## Contradictions
- VLM-based semantic safety score는 물리 ground truth 또는 real-road guarantee와 동일하지 않다.
