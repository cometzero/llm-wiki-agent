---
title: "Echo 핵심 기술 학습"
type: "source"
tags: ["hf-weekly", "VLA", "robotics", "task-status"]
sources: ["echo-2610-31569-learning"]
date: "2026-10-28"
last_updated: "2026-10-28"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W44/echo-task-status-2610-31569/learning.md"
source_hash: "a6bae00881a2e913"
---

## Summary
Stop/failure 상태 의미, 네 data type의 target/loss mask, asynchronous flow schedule과 velocity 부호를 단계적으로 설명한다. Pure-Python 교육 예제 두 개를 실행했으며 실제 VLA 구현·로봇 제어 코드가 아님을 명시한다.

## Key Claims
- Loss mask와 attention mask는 서로 다르며 failure chunk의 unknown FS를 0 label로 학습하면 안 된다.
- 원문 flow convention은 τ=1 noise, τ=0 clean이므로 inference의 time step은 감소한다.
- 실물과 simulation의 H·τclean·recovery SS target rule을 별도 관리한다. Learned status와 independent safety fallback을 분리한다.

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
