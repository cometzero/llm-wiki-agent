---
title: "ScaleVLA 분석"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "CC-BY-4.0"]
sources: ["scalevla-2611-21607-analysis"]
date: "2026-11-18"
last_updated: "2026-11-18"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W47/scalevla-2611-21607/analysis.md"
source_hash: "a50faf983b14117b"
---

## Summary
Numerical Action Generator와 representation-transfer 관점으로 frontier backbone scaling을 분석한다. Action grounding, evaluation protocol, hardware 및 observation freshness의 경계를 분리한다.

## Key Claims
- 10 demonstration의 Goal 87.8%는 fixed 5k budget 및 full-data normalization 조건이다. Convergence 후 순수 data-budget 비교가 아니다.
- MoE family, pretraining, readout, token 수, GPU allocation이 달라 pure parameter-count causal law로 해석하지 않는다.
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
