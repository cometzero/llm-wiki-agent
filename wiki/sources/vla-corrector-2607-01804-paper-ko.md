---
title: "VLA-Corrector: Adaptive Action Horizon을 위한 경량 Detect-and-Correct 추론"
type: source
tags: [huggingface-weekly, vla, robotics]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/vla-corrector-adaptive-action-horizon-2607-01804/paper-ko.md
source_hash: 488f61eb3a2ac68254f9c27a2ad715f15ed4217f90aad8bee5ff15f644b836ae
---

## Summary
VLA-Corrector 원문의 한국어 기술 번역이다. Abstract, Introduction, 수식 기반 방법론, MetaWorld/LIBERO/AgileX PiPER 실험, ablation과 결론을 보존한다.

## Key Claims
- LVM은 predicted visual feature evolution과 actual visual feature evolution을 비교해 persistent deviation을 감지한다.
- OGG는 flow-matching velocity를 corrective latent direction으로 guide하여 smoother corrective replanning을 만든다.
- Disturbance recovery real robot task에서 40.0%→68.3%로 큰 향상을 보인다.

## Key Quotes
> "Current chunk가 reliable할 때는 long-horizon execution을 유지하고, execution drift가 시작되면 short-horizon corrective replanning을 호출한다." — Abstract 번역
> "핵심은 더 나은 fixed horizon을 고르는 것이 아니라, current chunk를 언제 더 이상 신뢰하지 말아야 하는지 결정하는 것이다." — Introduction 번역

## Connections
- [[VLACorrector]] — 번역 대상 VLA framework
- [[OpenLoopBlindSpot]] — fixed horizon action chunk가 fresh observation을 무시하는 구간
- [[SuccessPerCall]] — 성공률과 policy-call 효율을 함께 보는 metric
- [[ClosedLoopRobot]] — real robot feedback execution 관점

## Contradictions
- 없음.
