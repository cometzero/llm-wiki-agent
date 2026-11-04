---
title: "OSWAM 한국어 기술 번역"
type: source
tags: [hf-weekly, autonomous-driving, WAM, structured-initialization]
sources: [oswam-2610-35850-paper-ko]
date: 2026-11-04
last_updated: 2026-11-04
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W45/oswam-one-step-action-2610-35850/paper-ko.md"
source_hash: "6af6c56b979d0b08"
---

## Summary
CC BY 4.0 원문의 Abstract와 본문 절별 내용, 수식 1–12, 핵심 실험 표를 한국어로 번역했다. 선별 부록과 원본 figure 6개를 보존하고 전체 50-task 표 및 긴 baseline 표의 생략을 명시했다.

## Key Claims
- AIT는 first-frame visual context에서 structured action prior를 만들고 SIT가 scene context를 보완한다.
- Prior를 detach한 뒤 같은 action noise로 re-noise하고 한 번의 Action DiT velocity update로 refine한다.
- NAVSIM PDMS 90.3/H20 136ms, RoboTwin 평균 SR 90.00%를 저자가 보고한다. Compiled RTX 5090의 40.81ms는 robot 설정이며 driving은 52.64ms다.

## Provenance
- arXiv:2610.35850v1, https://arxiv.org/html/2610.35850v1 ; https://huggingface.co/papers/2610.35850 . 원문 CC BY 4.0 attribution과 번역/축약 범위는 raw에 보존했다. 성능은 저자 보고다.
- NVIDIA 자동 ingest는 retired model HTTP 410, bounded Codex 재시도는 CLI 부재로 실패하여 raw를 읽고 deterministic manual materialization했다. 기존 다중-source 페이지와 overview 내용은 보존한다.

## Key Quotes
- 직접 인용 대신 원문에 근거한 한국어 요약을 제공한다.

## Connections
- [[OSWAM]] — direct-policy one-step world action model
- [[StructuredActionInitialization]] — learned prior와 residual refinement
- [[FlowMatching]] — velocity/time convention
- [[SimWAM]] — driving direct-policy baseline
- [[WorldActionModel]] — world-model prior와 action generation

## Contradictions
- 기존 wiki와 직접 충돌은 찾지 못했다. One-step 충분성은 학습된 initialization과 해당 평가 범위에 한정되며, 기존 multi-step 모델이 불필요하다는 보편 명제는 아니다.
