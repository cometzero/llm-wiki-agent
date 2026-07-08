---
title: "VLA-Corrector 참고 레퍼런스 요약"
type: source
tags: [huggingface-weekly, vla, robotics]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/vla-corrector-adaptive-action-horizon-2607-01804/references.md
source_hash: 95929f98710dcf621027cd3cdc0bed283002fc37f7cc9e6a138445599c13b707
---

## Summary
VLA-Corrector 관련 action chunking, closed-loop verification, action draft/verify, dynamic correction, value-guided selection 논문들을 한국어로 요약한 레퍼런스 노트다.

## Key Claims
- Adaptive Action Chunking, SV-VLA, DCDP, VGAS 등은 모두 fixed chunk/open-loop execution의 취약성을 다른 방식으로 다룬다.
- VLA-Corrector는 entropy나 verifier reference action 대신 latent visual dynamics mismatch를 기반으로 interrupt/recovery한다.
- Action generation과 action evaluation/monitoring을 분리하는 흐름이 VLA robustness 연구의 주요 축이다.

## Key Quotes
> "VLA-Corrector는 verifier를 latent visual dynamics monitor로 구현하고, replan에 OGG guidance를 추가한다." — SV-VLA 비교
> "VLA-Corrector는 candidate selection보다 execution-time drift detection/recovery에 초점을 둔다." — ADV 비교

## Connections
- [[VLACorrector]] — 레퍼런스 정리의 중심 논문
- [[ActionChunking]] — 참고문헌들의 공통 문제 설정
- [[ClosedLoopRobot]] — open-loop planning을 verification으로 보완하는 방향
- [[OnlineGradientGuidance]] — VLA-Corrector의 차별점

## Contradictions
- 없음.
