---
title: "ScaleVLA 핵심 기술 학습"
type: "source"
tags: ["VLA", "robotics", "hf-weekly", "CC-BY-4.0"]
sources: ["scalevla-2611-21607-learning"]
date: "2026-11-18"
last_updated: "2026-11-18"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W47/scalevla-2611-21607/learning.md"
source_hash: "b485a98db834d079"
---

## Summary
Frozen token feature→adapter→action DiT→numerical command의 interface를 단계적으로 설명한다. Mermaid와 실행한 Python toy 2개로 generation time, padding mask, chunk rate 및 observation age를 구분한다.

## Key Claims
- Oracle constant field의 정확한 endpoint는 learned policy의 정확성/안전성을 증명하지 않는다.
- 215.8ms의 inverse는 sequential chunk rate이고 actuator Hz가 아니다. Stale observation과 command buffer를 별도로 점검한다.
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
