---
title: "ScaleVLA 한국어 기술 번역"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "CC-BY-4.0"]
sources: ["scalevla-2611-21607-paper-ko"]
date: "2026-11-18"
last_updated: "2026-11-18"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W47/scalevla-2611-21607/paper-ko.md"
source_hash: "a1c4e2d7e1a1a47c"
---

## Summary
CC BY 4.0 원문 v1의 본문·수식 1·모든 표 1–9·그림 1–5와 주요 부록 조건을 한국어로 보존한다. Related Work 인용 열거 및 전체 서지 prose는 축약하고 전체 서지 추출은 metadata에 분리한다.

## Key Claims
- 552B frozen causal-encoder feature를 scratch action DiT에 연결한다. Decoder/explicit CoT는 실행하지 않는다.
- LIBERO-PRO 평균 45.1%, 실물 ID 9/10·OOD 8/15는 저자 보고 manipulation 결과다. 차량/NPU safety 결과가 아니다.
- 원문 https://arxiv.org/html/2611.21607v1 ; HF https://huggingface.co/papers/2611.21607

## Connections
- [[ScaleVLA]] — paper entity 및 실험 경계.
- [[FrontierVLMFeatureTransfer]] — frozen representation의 numerical action grounding.
- [[ODEPolicy]] — physical-time dynamics와 generation flow의 구분.
- [[GroundingPI]] — perceptual foundation의 action transfer와 비교.

## Contradictions
- 기존 wiki와 직접 모순은 확인하지 못했다. More capacity는 universal OOD dominance나 formal safety를 뜻하지 않는다.

## Provenance
- NVIDIA 자동 ingest HTTP 410 뒤 단 한 번의 bounded Codex fallback에서도 CLI를 찾지 못해 수동 deterministic materialization을 수행했다.
- Full nested source_file 및 최종 raw-byte SHA-256 prefix를 고정했다. 원문 benchmark 수치, 해설, 교육 toy 실행을 구분한다.
