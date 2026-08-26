---
title: "RISE 분석: 자율주행 WAM의 selective rollout"
type: source
tags: [autonomous-driving, world-action-model, analysis, closed-loop]
date: 2026-08-26
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W35/rise-adaptive-imagination-2608-20430/analysis.md
source_hash: d904f56e4b3d952b
---

## Summary
이 분석은 RISE를 language-action VLA가 아니라 latent-based World Action Model로 위치시킨다. front-camera observation에서 numerical ego trajectory를 생성하며, open-loop nuScenes와 closed-loop NAVSIM 결과, deployment latency와 calibration risk를 분리해 해석한다.

## Key Claims
- planning gain은 visual-future fidelity가 아니라 final trajectory quality에 정렬된 continuation criterion이다.
- NAVSIM closed-loop PDMS/EPDMS는 logged trajectory error보다 action grounding의 상호작용 품질에 가까운 검증이다.
- gate calibration failure와 synthetic counterfactual artifact는 safety-critical limitation이다.

## Connections
- VLA의 high-level reasoning과 결합 가능한 low-level future-aware planning substrate다.

## Contradictions
- 없음. 실제 vehicle 안전성은 simulator 결과만으로 일반화할 수 없다.
