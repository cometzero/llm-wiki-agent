---
title: "Latest Ready"
type: concept
tags: [control, serving, scheduling, latency]
sources: [ponderpounce-2608-24115-learning]
last_updated: 2026-09-02
---

[[LatestReady]] is a scheduling rule for asynchronous embodied systems: choose the newest cognition or intermediate result that is ready before the control deadline. It is stricter than "most recent" because freshness alone is insufficient if the result arrives too late to be useful.

This matters in [[PonderPounce]] because the controller must select a cognition carrier that is both recent and on time. The same rule generalizes to other [[RealTimeControl]] systems that separate slow reasoning from fast execution.

## Related Concepts
- [[InferencePlanning]]
- [[TemporalDecay]]
- [[RealTimeControl]]
- [[DualSystemArchitecture]]
