---
title: "Echo 분석"
type: "source"
tags: ["hf-weekly", "VLA", "robotics", "task-status"]
sources: ["echo-2610-31569-analysis"]
date: "2026-10-28"
last_updated: "2026-10-28"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W44/echo-task-status-2610-31569/analysis.md"
source_hash: "c08fa0a3207a88b1"
---

## Summary
Numerical-action VLA에서 status readability와 action influence를 구분한다. Data semantics, attention topology, async flow-time schedule이 함께 recovery action grounding을 만든다는 관점과 AD/NPU 전이의 미검증 경계를 정리했다.

## Key Claims
- Action-supervision budget은 baseline과 같지만 Echo에는 status용 failure data가 추가된다.
- Signal→action attention 제거 시 status Frame F1은 유지되지만 task score가 크게 떨어진다.
- 0–10 completion score, episode-first Macro-F1, frame-weighted simulation accuracy 및 3초 outcome window를 구별해야 한다. Vehicle safety·NPU latency 증거는 없다.

## Provenance
- 원문: https://arxiv.org/html/2610.31569 ; HF: https://huggingface.co/papers/2610.31569 . 원문 CC BY 4.0, 한국어 번역/편집 attribution은 raw에 보존한다. 성능은 저자 보고다.
- NVIDIA ingest HTTP 410와 bounded Codex fallback의 executable 부재로 새 raw를 읽고 deterministic manual materialization했다. 기존 다중-source 페이지는 수정하지 않는다.

## Key Quotes
- 직접 인용은 생략하고 출처가 명시된 한국어 요약을 제공한다.

## Connections
- [[Echo]] — status/action joint denoising VLA
- [[StatusGuidedActionDenoising]] — supervision·attention·schedule interface
- [[FlowMatching]] — continuous action generation
- [[FailureRecovery]] — corrective behavior와 termination 구분

## Contradictions
- 직접 충돌은 찾지 못했다. 실물 recovery padding의 SS supervision과 simulation recipe는 서로 다른 setup이며 일반화된 단일 rule이 아니다.
