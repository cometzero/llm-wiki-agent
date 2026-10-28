---
title: "Echo 참고문헌 지도"
type: "source"
tags: ["hf-weekly", "VLA", "robotics", "task-status"]
sources: ["echo-2610-31569-references"]
date: "2026-10-28"
last_updated: "2026-10-28"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W44/echo-task-status-2610-31569/references.md"
source_hash: "5970ac9bd7631199"
---

## Summary
Semantic Scholar references 38건과 원문 bibliography 39항목을 교차 확인하여 backbone·flow-time conditioning·monitoring·correction·recovery benchmark의 핵심 8편을 정리했다. 각 요약은 Echo의 인용 문맥에 근거하며 전편 독립 재현을 뜻하지 않는다.

## Key Claims
- π0.5와 token-wise action conditioning은 joint flow policy의 배경이다.
- CycleVLA·VLA-Corrector·ProgressVLA·Robometer는 backtracking, correction, gradient guidance, external evaluation이라는 서로 다른 비교 축이다.
- LIBERO/Libero-Recover의 recovery scene protocol은 원래 standard leaderboard 및 실물 평가와 구분한다.

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
