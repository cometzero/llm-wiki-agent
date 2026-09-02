---
title: "Episode Context Engine"
type: concept
tags: [robotics, memory, inference-planning, context]
sources: [ponderpounce-2608-24115-paper-ko]
last_updated: 2026-09-02
---

[[EpisodeContextEngine]]은 로봇 에피소드 동안 관측, 시연, 중간 추론, subgoal, prior cognition을 누적해 downstream controller가 사용할 수 있는 context representation으로 만드는 메커니즘이다. 핵심은 단순 저장이 아니라, 현재 control step에서 활용 가능한 형식으로 context를 유지하고 갱신하는 것이다.

## Characteristics
- append-only 혹은 bounded-update context 유지
- subgoal, reasoning, memory carrier 등의 intermediate state 포함
- control path와 분리된 비동기 갱신 가능
- stale context를 구분하기 위한 age signal과 결합 가능

## Related
- [[PersistentMemory]]
- [[PlannerState]]
- [[InferencePlanning]]
- [[TemporalDecay]]
- [[DualSystemArchitecture]]
