---
title: "OSWAM 핵심 참고문헌 9편"
type: source
tags: [hf-weekly, autonomous-driving, WAM, structured-initialization]
sources: [oswam-2610-35850-references]
date: 2026-11-04
last_updated: 2026-11-04
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W45/oswam-one-step-action-2610-35850/references.md"
source_hash: "218e2f9435c8c51a"
---

## Summary
Semantic Scholar references endpoint의 59편과 원문 59 bibliography 항목을 교차 확인해 direct-policy, distillation, backbone/flow 및 benchmark 핵심 9편을 정리했다.

## Key Claims
- Fast-WAM/SimWAM은 direct-policy 설계의 직접 선행이고 Flash-WAM/Light-WAM은 다른 efficiency trade-off다.
- Wan/LoRA/Rectified Flow는 backbone 적응과 velocity refinement의 배경이다.
- NAVSIM의 non-reactive contract와 RoboTwin의 domain randomization 범위를 구분한다. 서로 다른 두 Faster-WAM의 ID도 분리했다.

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
