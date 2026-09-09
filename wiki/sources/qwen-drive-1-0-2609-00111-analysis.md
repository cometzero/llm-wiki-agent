---
title: "Qwen-Drive-1.0 분석: shared VLM에서 BEV와 trajectory planning까지"
type: source
tags: [autonomous-driving, vision-language-model, bev, trajectory, closed-loop]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/qwen-drive-1-0-2609-00111/analysis.md
source_hash: d62dd1e800b232a3
---

## Summary
이 분석은 Qwen-Drive-1.0을 perception-action과 numerical action generation을 결합한 autonomous-driving VLM으로 해석한다. VLM text answer를 직접 control로 parse하지 않고 cached representation을 Planning Expert에 전달해 trajectory를 생성하는 것이 핵심 action-grounding interface다.

## Key Claims
- BEV head는 auxiliary output이면서 shared VLM representation의 geometry를 검사하는 interface다.
- ADE 같은 open-loop metric과 PDMS/NC/TTC 같은 pseudo-closed-loop metric은 다른 failure mode를 측정한다.
- real deployment에는 calibration, uncertainty, timing watchdog, safety shield, fallback planner가 필요하다.

## Connections
- Driving VLM의 language reasoning과 continuous trajectory generation 사이의 interface 설계를 다룬다.

## Contradictions
- Shared representation 성능은 explanation text가 planner action을 causal하게 결정한다는 증거와는 다르다.
