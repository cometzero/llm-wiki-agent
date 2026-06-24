---
title: "Redundancy-Aware Reward"
type: concept
tags: [RL, reward-design, policy-efficiency, physical-steps]
sources: [policytrim-2606-22540, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

Phase 2 [[PolicyTrim]]에서 사용되는 reward 설계. **task 성공([[SuccessRate]])을 유지하면서 불필요한 [[PhysicalSteps]]를 줄이도록** 설계된 reward다.

## Design Principles

1. **Success preservation**: task 완료 보상은 반드시 유지
2. **Step penalty**: 불필요한 action step마다 penalty 부여
3. **Shortcuts 방지**: 단순 shortcut(임시로 빠르게 보이는 해법)이 아니라 재현 가능한 짧은 trajectory를 선호하도록 reward shaping
4. **Safety guard**: collision/contact/constraint penalty를 함께 포함하여 safety margin 유지

## Effect

- [[PhysicalSteps]] 51.4% 감소
- [[SuccessRate]] 유지

## Safety-Critical Extension (Autonomous Driving)

autonomous driving 적용 시 reward에 포함해야 할 요소:
- jerk, acceleration constraints
- lane rule compliance
- collision risk penalty
- comfort metric (승객 편익)

## Connections
- [[PolicyTrim]] — 두 단계 RL 프레임워크의 phase 2
- [[HorizonSuccessReward]] — phase 1 reward
- [[PhysicalSteps]] — reward의 대상
- [[IntrinsicPolicyEfficiency]] — 최적화 대상 지표
