---
title: "PolicyTrim"
type: concept
tags: [VLA, RL-post-training, action-chunk, deployment-efficiency]
sources: [policytrim-2606-22540, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

PolicyTrim은 VLA(Vision-Language-Action) 모델의 **intrinsic policy efficiency**를 RL post-training으로 향상시키는 2단계 프레임워크다. [[ActionChunk]] utilization을 높이고 [[PhysicalSteps]]를 줄여 deployment 속도를 개선한다.

## Key Ideas

### Phase 1: Horizon Success Reward
- VLA가 [[ActionChunk]]를 얼마나 길게 안전하게 실행할 수 있는지 측정
- chunk horizon을 늘려 성공한 rollout에 reward 부여
- [[TailDegradation]] 문제를 점진적으로 완화
- action chunk utilization **3배** 향상

### Phase 2: Redundancy-Aware Reward
- task 성공([[SuccessRate]])을 유지하면서 불필요 [[PhysicalSteps]]를 줄이는 reward 설계
- 단순 shortcut이 아니라 재현 가능한 짧은 trajectory 선호
- physical steps **51.4%** 감소

### Deployment Efficiency

```text
Total inference calls ≈ Total physical steps / Effective executable chunk length
Deployment speed ∝ fewer physical steps + longer reliable chunks
```

결과: **5.83배** 배포 속도 개선(forward pass 수 × wall-clock time 동시 감소)

## Relationship to Other Techniques

| 기법 | 타겟 | PolicyTrim과 비교 |
|---|---|---|
| [[Pruning]] | inference 속도 | 한 번의 inference를 빠르게 하지만 inference 횟수는 줄이지 않음 |
| [[Quantization]] | inference 속도 |同上 |
| PolicyTrim | inference 횟수 + [[PhysicalSteps]] | deployment efficiency 직접 최적화 |

## Safety Considerations

- reward에 collision/contact/constraint penalty 포함 필요
- dynamic perturbation에 대한 robustness 확인 필요
- autonomous driving 적용 시: jerk, acceleration, lane rule, collision risk, comfort metric reward에 포함
- 긴 [[ActionChunk]] 사용 시 monitoring/fallback controller 필수

## Connections
- [[VLA]] — 대상 모델 클래스
- [[ActionChunk]] — 핵심 조작 단위
- [[TailDegradation]] — phase 1이 해결하는 문제
- [[IntrinsicPolicyEfficiency]] — 최적화 대상 지표
- [[HorizonSuccessReward]] — phase 1 reward 설계
- [[RedundancyAwareReward]] — phase 2 reward 설계
- [[LIBERO]], [[ManiSkill]], [[MetaWorld]] — 평가 benchmark
