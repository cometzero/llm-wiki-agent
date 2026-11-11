---
title: "ODE Policy 핵심 기술 학습"
type: "source"
tags: ["VLA", "robotics", "ODE", "hf-weekly", "independent-synopsis"]
sources: ["ode-policy-2611-01729-learning"]
date: "2026-11-11"
last_updated: "2026-11-11"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W46/ode-policy-2611-01729/learning.md"
source_hash: "99f163b31dc78fa2"
---

## Summary
Physical time과 generation time, desired action과 measured state, path supervision과 derivative supervision을 예제로 구분한다. 두 toy Python block은 실행 검증했지만 학습된 policy 또는 실제 robot의 재현 실험은 아니다.

## Key Claims
- Toy integration에서 RK4/Euler 오차와 chunk boundary의 carried command를 확인한다.
- Route balance와 전체 success rate는 서로 다른 지표다.
- Sensor-to-actuator latency와 head-only generation cost를 분리해야 한다.

## Connections
- [[ODEPolicy]] — 연구와 구현 interface.
- [[ActionDynamicsPolicy]] — physical-time command integration.
- [[OSWAM]] — generation step 최적화와 action parameterization 변경의 대조.

## Contradictions
- 기존 corpus와 직접적인 모순은 확인되지 않았다. 효율·안정성의 보편적 우위로 확장하지 않는다.

## Provenance
- 수동 deterministic materialization: NVIDIA ingest HTTP 410, bounded Codex fallback에서 CLI 없음.
- 전체 번역이 아닌 독자 기술 해설; 저자 benchmark 결과와 교육 실행 증거를 분리한다.
