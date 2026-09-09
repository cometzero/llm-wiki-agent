---
title: "Act with Intent (INDI) 분석: 행동 목적을 latent action decoder로 증류"
type: source
tags: [vision-language-action, representation-transfer, teacher-supervision, robotics]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/act-with-intent-indi-2608-23478/analysis.md
source_hash: 1b53542e8b215660
---

## Summary
이 분석은 INDI를 implicit representation transfer 계열 VLA로 위치시킨다. Executed video를 본 teacher의 privileged evidence를 deployment student에 leak하지 않고, objective/progress-aware latent target으로 distill하는 것이 central design이다.

## Key Claims
- Intent intervention은 latent가 actual policy behavior에 사용되는지 보는 비교적 강한 causal diagnostic이다.
- Simulation/real robot success는 closed-loop evidence지만 finite task/trial/teacher-target bias를 포함한다.
- Safety-critical deployment에는 latent intent 외에도 uncertainty, rule/constraint check, recovery와 shield가 필요하다.

## Connections
- Future supervision, representation transfer, continuous robot action grounding의 차이를 정리한다.

## Contradictions
- Higher task success는 teacher interpretation의 correctness나 action safety를 보장하지 않는다.
