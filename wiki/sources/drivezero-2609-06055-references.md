---
title: "DriveZero 핵심 참고문헌"
type: source
tags: [autonomous-driving, literature-map, reinforcement-learning]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W37/drivezero-end-to-end-driving-2609-06055/references.md
source_hash: c4de19d89c46d469
---

## Summary
DriveZero reference map은 driving self-play, post-training, simulation scaling, no-expert-demonstration policy, diffusion/RL planner, visual depth representation을 연결한다. 특히 Qwen-Drive, PlannerRFT, SimScale은 DriveZero의 foundation representation·closed-loop policy optimization·OOD data scaling 비교축을 제공한다.

## Key Claims
- RL/self-play 계열은 offline imitation의 covariate shift를 interactive experience로 다룬다.
- SimScale은 camera student의 OOD scaling data와 연결된다.
- driving VLM과 numerical planner는 언어 reasoning과 executable trajectory를 구별해야 한다.

## Connections
- [[DriveZero]] — reference context.
- [[ClosedLoopReinforcementLearning]] — policy optimization lineage.

## Contradictions
- Reference summary는 각 cited method의 reproduction 또는 성능 재검증을 수행하지 않는다.
