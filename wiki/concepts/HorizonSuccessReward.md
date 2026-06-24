---
title: "Horizon Success Reward"
type: concept
tags: [RL, reward-design, action-chunk, policy-efficiency]
sources: [policytrim-2606-22540, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

Phase 1 [[PolicyTrim]]에서 사용되는 reward 설계. **chunk horizon을 늘려 성공한 rollout에 보상**을 부여하여 policy가 더 긴 [[ActionChunk]]의 reliable horizon을 탐색하도록 유도한다.

## Mechanism

```text
chunk horizon h로 rollout 실행
  → 성공 시 reward + bonus(h)  (h가 길수록 높은 보상)
  → 실패 시 reward 0 또는 penalty
```

## Goal

- [[ActionChunk]] utilization 3배 향상
- [[TailDegradation]]을 점진적으로 완화
- 더 긴 reliable chunk를 신뢰할 수 있는 policy 학습

## Relation to Phase 2

Horizon Success Reward → 긴 reliable chunk 확보 → [[RedundancyAwareReward]]로 불필요 [[PhysicalSteps]] 절감

## Connections
- [[PolicyTrim]] — 두 단계 RL 프레임워크의 phase 1
- [[TailDegradation]] — 해결 대상
- [[ActionChunk]] — reward의 대상 단위
- [[RedundancyAwareReward]] — phase 2 reward
