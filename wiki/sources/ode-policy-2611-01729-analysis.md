---
title: "ODE Policy 분석"
type: "source"
tags: ["VLA", "robotics", "ODE", "hf-weekly", "independent-synopsis"]
sources: ["ode-policy-2611-01729-analysis"]
date: "2026-11-11"
last_updated: "2026-11-11"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W46/ode-policy-2611-01729/analysis.md"
source_hash: "122e98da8a695c81"
---

## Summary
Language/image condition과 measured proprioception을 입력으로 받아 이전 desired action에서 다음 action을 적분한다. LIBERO closed-loop, LIBERO-plus OOD, 실물 조작, model-based motion tracking을 구분하며 vehicle/NPU 성능은 주장하지 않는다.

## Key Claims
- Streaming command는 chunk 안의 perception refresh를 보장하지 않는다.
- Command continuity는 bounded jerk·collision safety·global stability 증명이 아니다.
- Model-free RL·discrete gripper·camera shift·seed divergence 등 적용 한계가 남는다.

## Connections
- [[ODEPolicy]] — 연구와 구현 interface.
- [[ActionDynamicsPolicy]] — physical-time command integration.
- [[OSWAM]] — generation step 최적화와 action parameterization 변경의 대조.

## Contradictions
- 기존 corpus와 직접적인 모순은 확인되지 않았다. 효율·안정성의 보편적 우위로 확장하지 않는다.

## Provenance
- 수동 deterministic materialization: NVIDIA ingest HTTP 410, bounded Codex fallback에서 CLI 없음.
- 전체 번역이 아닌 독자 기술 해설; 저자 benchmark 결과와 교육 실행 증거를 분리한다.
