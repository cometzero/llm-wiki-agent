---
title: "Echo 한국어 기술 번역"
type: "source"
tags: ["hf-weekly", "VLA", "robotics", "task-status"]
sources: ["echo-2610-31569-paper-ko"]
date: "2026-10-28"
last_updated: "2026-10-28"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W44/echo-task-status-2610-31569/paper-ko.md"
source_hash: "9056983e348ffe0a"
---

## Summary
CC BY 4.0 원문 본문 1–5절·수식 1–14와 주요 실험 표를 번역하고 부록의 재현 조건을 선별 번역했다. Stop/failure signal과 action을 jointly denoise하며 signal을 먼저 clean하게 만들어 continuous action generation을 안내한다.

## Key Claims
- SS와 FS를 H×(da+2) joint target으로 구성하지만 Transformer 내부 generated token은 3H다.
- Failure action은 imitation하지 않고 segment boundary·recovery position으로 signal supervision을 만든다. Frame-level progress label은 없어도 subtask/recovery boundary는 필요하다.
- 실물 5개 task score 개선과 LIBERO-Recovery 32.67→34.76% SR(+2.09 pp)을 보고한다. Simulation status accuracy는 terminal-failure detection 평가가 아니다.

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
