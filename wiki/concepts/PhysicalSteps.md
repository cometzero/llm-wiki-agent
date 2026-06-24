---
title: "Physical Steps"
type: concept
tags: [VLA, deployment, robot-control, action-chunk]
sources: [policytrim-2606-22540, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

실제 robot/environment에서 수행되는 action step 수. [[VLA]] policy가 environment와 상호작용한 횟수를 의미하며, deployment 속도와 directly 연관되는 핵심 지표다.

## Relationship to [[ActionChunk]]

```text
Total inference calls = Total physical steps / Effective executable chunk length
```

동일한 task를 완료하더라도:
- 짧은 [[ActionChunk]]를 사용하면 → 많은 inference call 필요 → 느린 deployment
- 긴 reliable [[ActionChunk]]를 사용하면 → 적은 inference call → 빠른 deployment

## [[PolicyTrim]]에서의 역할

- Phase 1: reliable chunk horizon 확보
- Phase 2: [[RedundancyAwareReward]]로 physical steps 직접 감소
- 결과: 51.4% physical steps 감소, 5.83× deployment speedup

## Connections
- [[PolicyTrim]] — physical steps를 줄이는 방법론
- [[ActionChunk]] — inference call 수를 결정하는 단위
- [[IntrinsicPolicyEfficiency]] — physical steps는 efficiency의 핵심 구성 요소
- [[VLA]] — deployment 대상 모델
