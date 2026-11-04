---
title: "OSWAM 핵심 기술 학습"
type: source
tags: [hf-weekly, autonomous-driving, WAM, structured-initialization]
sources: [oswam-2610-35850-learning]
date: 2026-11-04
last_updated: 2026-11-04
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W45/oswam-one-step-action-2610-35850/learning.md"
source_hash: "2373ba2c4095d75e"
---

## Summary
AIT/SIT, flow 부호, same-noise re-noising, teacher/student information boundary 및 RoPE timeline을 예제 중심으로 설명한다. 두 Python 예제는 residual-target algebra와 timeline/latency 산술을 검증하며 모델 재현은 아니다.

## Key Claims
- One-step은 Action DiT의 denoising 횟수이며 Video DiT 계산까지 없어지는 것은 아니다.
- Loss target (a_init-a_gt)/sigma와 update a_init-sigma*v의 부호·scale이 맞아야 한다.
- Stop-gradient, teacher freeze, same epsilon, indirect future leakage, observation freshness를 구현 시 검증해야 한다.

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
