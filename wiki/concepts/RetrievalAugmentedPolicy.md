---
title: "Retrieval-Augmented Policy"
type: concept
tags: [vla, retrieval, robotics]
sources: [retrieve-dont-retrain-2606-15631]
last_updated: 2026-06-17
---

## Definition
Retrieval-augmented policy는 현재 observation/instruction에 맞는 과거 demonstration, trajectory, memory item을 검색하고 이를 action generation의 조건으로 사용하는 policy family다.

## Current State
[[ReCAP]]은 새 task adaptation을 parameter update가 아니라 retrieval pool update로 처리한다. 이 접근은 [[WorldActionModel]]과 결합될 때 retrieved trajectory가 coarse task progression을 주고, model은 target embodiment residual을 생성한다.

## Open Questions
- Retrieval false positive가 [[ActionGrounding]]과 safety에 미치는 영향.
- Large memory에서 latency와 relevance를 동시에 만족하는 방법.
- 자율주행 VLA에서 retrieved trajectory를 waypoint/BEV/occupancy planner prior로 바꾸는 방법.

## Related
- [[VisionLanguageAction]]
- [[WorldActionModel]]
- [[retrieve-dont-retrain-2606-15631]]
