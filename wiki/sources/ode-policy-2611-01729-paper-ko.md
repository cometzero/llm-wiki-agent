---
title: "ODE Policy 한국어 기술 해설"
type: "source"
tags: ["VLA", "robotics", "ODE", "hf-weekly", "independent-synopsis"]
sources: ["ode-policy-2611-01729-paper-ko"]
date: "2026-11-11"
last_updated: "2026-11-11"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W46/ode-policy-2611-01729/paper-ko.md"
source_hash: "b0bfdd2e2e0271bd"
---

## Summary
Action 값 대신 commanded-action vector field를 학습하고 physical time에 적분하는 numerical-action interface를 해설한다. 원문 arXiv non-exclusive license로 전문 번역/원본 그림 재배포는 하지 않고 독자적인 한국어 해설과 도식을 제공한다.

## Key Claims
- Short chunk의 integrated path loss로 derivative label 없이 field를 학습한다.
- Contractive perturbation과 seamless chunking, optional diversity head를 조합한다.
- π0.5의 1 epoch 96.0% vs 75.5% 비교에서 후자는 random-init FM expert다.

## Connections
- [[ODEPolicy]] — 연구와 구현 interface.
- [[ActionDynamicsPolicy]] — physical-time command integration.
- [[OSWAM]] — generation step 최적화와 action parameterization 변경의 대조.

## Contradictions
- 기존 corpus와 직접적인 모순은 확인되지 않았다. 효율·안정성의 보편적 우위로 확장하지 않는다.

## Provenance
- 수동 deterministic materialization: NVIDIA ingest HTTP 410, bounded Codex fallback에서 CLI 없음.
- 전체 번역이 아닌 독자 기술 해설; 저자 benchmark 결과와 교육 실행 증거를 분리한다.
