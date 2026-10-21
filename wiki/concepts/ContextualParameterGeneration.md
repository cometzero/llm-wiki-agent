---
title: "Contextual Parameter Generation"
type: concept
tags: [hypernetwork, VLA, low-rank-adaptation]
sources: ["morphact-2610-20019-paper-ko", "morphact-2610-20019-analysis", "morphact-2610-20019-references", "morphact-2610-20019-learning"]
last_updated: 2026-10-21
---

# Contextual Parameter Generation

고정 task adapter 대신 현재 context에서 effective weight update를 생성하는 방식입니다.

[[MorphAct]]에서는 observation마다 vision-side update를 먼저 만들고, 수정된 representation으로 action-side update를 생성한다. [[LoRA]]의 A/B factor는 생성 출력이며 generator parameter 자체와 구분한다. action objective의 gradient는 native action condition과 action-weight generator의 두 경로로 upstream에 전달된다.

## Lifecycle
동일 context의 factor와 adapted condition은 solver step 사이에 재사용하고, 새로운 observation에서 교체한다. test-time gradient optimization이나 fixed task-ID adapter와 다르다.

## Limits
finite manipulation success나 local gradient conflict는 general safety guarantee가 아니다. latency/memory, batch별 cache isolation, observation age 및 independent safety fallback을 별도로 검증해야 한다.

## Sources
- [[morphact-2610-20019-paper-ko]]
- [[morphact-2610-20019-analysis]]
- [[morphact-2610-20019-references]]
- [[morphact-2610-20019-learning]]
