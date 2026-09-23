---
title: "ShieldVLA 분석"
type: source
tags: [vla, safety, closed-loop, analysis]
date: 2026-09-23
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W39/shieldvla-safety-alignment-2609-13231/analysis.md
source_hash: c04d0c3aeb3570b3
---

## Summary
분석 문서는 ShieldVLA를 VLM semantic scoring과 HJ safety critic을 결합한 explicit action-guidance layer로 위치시킨다. SR과 CSC를 함께 보는 closed-loop evidence는 유용하지만 robotic benchmark 결과를 자율주행 rare-event safety로 확대 해석하지 않아야 한다.

## Key Claims
- \(Q^s>\delta\)인 영역만 task-reward update를 받고, 나머지는 safety gradient를 받는다.
- language는 action text보다는 safety rubric의 scene semantics를 만드는 간접 interface다.

## Connections
- [[ShieldVLA]] — 방법 분석 대상.
- [[VLA]] — action-policy 맥락.

## Contradictions
- safety critic score는 physical certification을 대체하지 않는다.
