---
title: "ODE Policy 참고문헌 지도"
type: "source"
tags: ["VLA", "robotics", "ODE", "hf-weekly", "independent-synopsis"]
sources: ["ode-policy-2611-01729-references"]
date: "2026-11-11"
last_updated: "2026-11-11"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W46/ode-policy-2611-01729/references.md"
source_hash: "e8a382c7cc87fe7d"
---

## Summary
Semantic Scholar references endpoint에서 얻은 82개 항목 중 원문과 관련된 핵심 9편을 선별한다. Neural ODE·Diffusion/Flow·π0.5·ImageWAM·SuperMimic·LIBERO/Plus의 역할을 설명한다.

## Key Claims
- Flow Matching의 generation time과 ODE Policy의 physical time을 구분한다.
- Action head 교체의 backbone과 평가 benchmark를 별도 문헌 축으로 읽는다.
- 기존 분석된 참고문헌은 이번 신규 paper selection으로 세지 않는다.

## Connections
- [[ODEPolicy]] — 연구와 구현 interface.
- [[ActionDynamicsPolicy]] — physical-time command integration.
- [[OSWAM]] — generation step 최적화와 action parameterization 변경의 대조.

## Contradictions
- 기존 corpus와 직접적인 모순은 확인되지 않았다. 효율·안정성의 보편적 우위로 확장하지 않는다.

## Provenance
- 수동 deterministic materialization: NVIDIA ingest HTTP 410, bounded Codex fallback에서 CLI 없음.
- 전체 번역이 아닌 독자 기술 해설; 저자 benchmark 결과와 교육 실행 증거를 분리한다.
