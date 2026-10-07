---
title: "PerturBot 분석: 성공률과 Evidence Use를 분리하기"
type: source
tags: [huggingface-weekly, robotics, vla, analysis]
sources: [perturbot-2610-04616]
date: 2026-10-07
last_updated: 2026-10-07
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W41/perturbot-grounded-vla-2610-04616/analysis.md
source_hash: 566fa15bfc5f23f9
arxiv_id: "2610.04616"
---

## Summary
successful demonstration의 visual·lexical·motor cue가 task evidence를 대체하는 modality shortcut을 다룬다. label-valid V/C/R training data intervention과 null/causal paired action response의 GroundFscore를 결합하며 inference architecture는 유지한다. taxonomy, I/O와 action grounding, training, offline/closed-loop 평가, safety/latency와 AD 전이 boundary를 분리했다. robotics 결과와 자율주행에 대한 분석자 유추를 명확히 구별한다.

## Key Claims
- taxonomy, I/O와 action grounding, training, offline/closed-loop 평가, safety/latency와 AD 전이 boundary를 분리했다. robotics 결과와 자율주행에 대한 분석자 유추를 명확히 구별한다.
- R relabeling은 unrecorded recovery를 생성하지 않는다. GF는 paired expert delta와 valid edits에 의존하는 diagnostic이며 formal safety certificate가 아니다. abstract/full-text metric 명칭 차이를 보존했다.
- 원문과 분석자 deployment 유추를 분리하며 독립 reproduction은 수행하지 않았다.

## Key Quotes
- 긴 원문 인용 대신 raw 번역과 원문 링크를 참조한다.

## Connections
- [[PerturBot]] — 연구 방법과 나머지 세 deliverable을 잇는 중심 페이지.
- [[VisionLanguageModel]] — visual/language decision과 executable action의 연결.
- [[VisionActionShortcut]] — successful-demo cue와 task evidence의 분리.
- [[MotorMind]] — runtime harness와 training-data evidence intervention의 상보적 관계.

## Contradictions and Boundaries
- R relabeling은 unrecorded recovery를 생성하지 않는다. GF는 paired expert delta와 valid edits에 의존하는 diagnostic이며 formal safety certificate가 아니다. abstract/full-text metric 명칭 차이를 보존했다.
- 본 논문은 robotics 연구로 vehicle closed-loop 성능을 직접 입증하지 않는다.

## Source
https://arxiv.org/html/2610.04616v1
