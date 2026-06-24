---
title: "Tail Degradation"
type: concept
tags: [VLA, action-chunk, reliability, policy-efficiency]
sources: [policytrim-2606-22540, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

[[ActionChunk]] 뒤쪽(action의 시간적으로 나중인 부분) action의 신뢰도가 떨어지는 현상을 말한다. 긴 [[ActionChunk]]를 한 번에 inference할 때, 초기 몇 step은 정확한 반면 뒤로갈수록 prediction drift가 누적되어 실패율이 높아진다.

## Mechanism

```text
Inference:  [a₁, a₂, a₃, ..., aₙ]  (한 번의 forward pass)
Confidence:  高  高  中  ...  低    (뒤쪽 action으로 갈수록 감소)
```

## Relationship to [[PolicyTrim]]

- Phase 1의 **[[HorizonSuccessReward]]**가 [[TailDegradation]]을 해결하는 핵심 메커니즘
- chunk horizon을 점진적으로 늘려가며 성공 가능한 reliable horizon을 탐색
- 무조건 chunk 길이를 늘리는 것이 아니라, 성공률을 유지하는 범위에서 탐색

## Connections
- [[PolicyTrim]] — tail degradation을 완화하는 방법론
- [[ActionChunk]] — degradation이 발생하는 단위
- [[IntrinsicPolicyEfficiency]] — degradation이 저하시키는 지표
