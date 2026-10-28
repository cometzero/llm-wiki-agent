---
title: "Status-Guided Action Denoising"
type: concept
tags: [VLA, flow-matching, recovery, task-status]
sources: [echo-2610-31569-paper-ko, echo-2610-31569-analysis, echo-2610-31569-learning]
last_updated: 2026-10-28
---

# Status-Guided Action Denoising

[[Echo]]는 task status를 사후 monitor로만 읽지 않고 [[FlowMatching]]의 continuous action update가 cleaner status estimate에 조건화되도록 한다. 핵심은 status target의 의미, action과 signal 사이의 attention topology, group별 noise schedule을 함께 설계하는 것이다.

## Mechanism

1. Action과 같은 horizon H의 stop SS·failure FS column을 joint target H×(da+2)에 더한다.
2. 내부적으로 action/SS/FS는 각각 H개 token을 가지므로 generated sequence는 3H다.
3. Group별 projection·MLP를 분리하고 action↔signal은 허용하되 direct SS↔FS는 막는다.
4. Noise=1/clean=0 convention에서 τsignal=max(0,(τaction−c)/(1−c))로 signal을 먼저 clean하게 한다. Endpoint 뒤 signal은 고정하고 action update를 계속한다.
5. Failure trajectory에서는 action loss를 끄고 boundary-derived signal target을 학습한다. Correction action은 recovery demonstration에서 온다.

## 왜 Status Probe와 다른가?

원문 Flower ablation에서 signal→action attention을 제거하면 status Frame F1은 92.18→90.78로 유지되지만 completion score는 8.33→5.00으로 하락한다. 즉 status를 읽을 수 있다는 것과 status가 action을 유용하게 바꾼다는 것은 서로 다른 주장이다. 이는 저자 setup의 증거이지 모든 VLA에 대한 보편적 인과 법칙이 아니다.

## Boundary

- Low SS/high FS는 recoverable state이며 FS=높음만으로 stopping하지 않는다.
- Signal은 calibrated safety probability가 아니다. Independent constraints·stale-observation handling·fallback이 따로 필요하다.
- Frame-level annotation을 없앤 것이 아니라 fine-grained progress annotation을 segment-level supervision으로 대체한 것이다.
- [[FailureRecovery]]·external planner와 결합할 수 있지만 결합 성능을 별도로 검증해야 한다.

## Sources

- [[echo-2610-31569-paper-ko]]
- [[echo-2610-31569-analysis]]
- [[echo-2610-31569-learning]]
