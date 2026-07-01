---
title: "Zero-Shot Sim-to-Real Transfer"
type: concept
tags: [robotics, sim-to-real, transfer-learning]
sources: [object-centric-residual-rl-vla-enhancement-2606-18953]
last_updated: 2026-07-01
---

## Definition
Simulation 환경에서만 학습한 policy를 별도 adaptation 없이 직접 real robot에 배포하는 것을 의미한다.

## This Paper's Approach
[[ObjectCentricResidualRL]]는 residual policy가 다음 조건을 만족할 때 zero-shot transfer가 가능하다고 본다:

```
s_t^real = s_t^sim + η_t,  η_t ~ P_η
```

Reality observation이 simulation observation에 noise가 더해진 형태로 근사될 수 있으면 transfer 가능.

이를 위해 training에서:
1. **Position noise**: mm 단위 perturbation
2. **Orientation noise**: small random rotation
3. **Pose dropout**: pose confidence가 낮은 step에서 pose component dropout

## Comparison with Other Approaches
| Approach | Problem |
|----------|---------|
| Privileged-state method | Deployment 시 distillation 필요, teacher-to-student loss |
| Image-based method | Visual domain gap에 취약 |
| Real-world RL | 비용과 safety risk 큼 |
| Object-centric (ours) | Pose는 sim/reality에서 recoverable → zero-shot 가능 |

## Connections
- [[ObjectCentricResidualRL]] — 적용 framework
- [[SimToRealGap]] — 해결 대상 문제
- [[ResidualRL]] — policy 구조
