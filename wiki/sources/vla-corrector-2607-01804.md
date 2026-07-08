---
title: "VLA-Corrector 분석: Action chunk를 adaptive closed-loop로 바꾸기"
type: source
tags: [huggingface-weekly, vla, robotics]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/vla-corrector-adaptive-action-horizon-2607-01804/analysis.md
source_hash: 9c3532435f97fb21326b4c97a0b95021c9b28f5e6faf894537a0dd164555716d
---

## Summary
VLA-Corrector 분석 문서다. Action chunking의 open-loop blind spot을 Latent-space Vision Monitor(LVM), event-triggered truncation, Online Gradient Guidance(OGG)로 완화하는 방법과 MetaWorld/LIBERO/real robot 결과를 정리한다.

## Key Claims
- Action chunking은 policy call을 줄이지만 stale action이 누적되는 open-loop blind spot을 만든다.
- VLA-Corrector는 frozen VLA backbone에 external monitor와 OGG를 붙여 adaptive action horizon을 만든다.
- π0.5 MetaWorld average success 48.70→64.35, real robot average success 55.6→73.3으로 향상된다.

## Key Quotes
> "VLA-Corrector는 action chunking의 latency 이점은 유지하면서, latent visual dynamics monitor로 stale chunk를 중단하고 OGG로 recovery action을 유도한다." — 한 문장 결론
> "Action grounding을 실행 중 visual dynamics consistency로 검증한다." — Action grounding 분석

## Connections
- [[VLACorrector]] — action-chunked VLA용 detect-and-correct framework
- [[ActionChunking]] — policy-call frequency를 줄이는 chunk mechanism
- [[LatentSpaceVisionMonitor]] — expected/actual latent visual dynamics 비교 monitor
- [[OnlineGradientGuidance]] — recovery replan을 guide하는 inference-time gradient method
- [[AdaptiveActionHorizon]] — event-triggered로 바뀌는 horizon

## Contradictions
- 없음.
