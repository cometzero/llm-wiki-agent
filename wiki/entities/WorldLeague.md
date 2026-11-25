---
title: "WorldLeague"
type: entity
tags: [VLA, VLM, WAM, benchmark, physical-agency]
sources: [worldleague-2611-30989-paper-ko, worldleague-2611-30989-analysis, worldleague-2611-30989-references, worldleague-2611-30989-learning]
last_updated: 2026-11-25
---

# WorldLeague

Xinyang Zhou, Qi Li, Xinchao Wang의 arXiv:2611.30989v1(2026-11-23) benchmark. [[VisionLanguageModel]], [[VisionLanguageAction]], [[WorldActionModel]]의 physical goal achievement를 shared goal·constraint·scoring으로 비교한다. 새로운 driving policy가 아니다.

## Evaluation

60개 task는 WorldSeek(navigation/grounding), WorldShape(geometry/physics), WorldShift(memory/constrained recovery)의 여섯 dimension으로 나뉜다. [[GoalPredicateEvaluation]]은 item progress와 모든 goal·constraint를 요구하는 success를 분리한다. Eight VLM은 R1/WorldHarness, three VLA와 two WAM은 native controller/embodiment를 사용한다. Shared task는 동일 interface를 뜻하지 않는다.

Seed 0의 775 episodes에서 Fable overall I=28.58/100, 13/60 goals. QA 전부 정답 347 episodes 중 249개(71.8%)의 physical credit이 0이다. Terminal QA는 물리 결과를 고정한 뒤 수행하는 보조 지표이며 성공 판정이 아니다. T52는 초기부터 goal이 성립해 continuous policy는 제외한다.

## Evidence Boundary

대부분 system/task당 single episode이며 Sol만 추가 seed 전체 반복이다. Simulation closed-loop, robot/interface/context confound, task-equal mean과 window-pooled mean을 보존한다. Inference 동안 world가 변하지만 실차 response time·NPU throughput·formal safety를 측정한 결과는 아니다. [[ScaleVLA]]의 representation scaling이나 [[Echo]]의 status readability를 outcome success로 대체하지 않는다.

## Sources
- [[worldleague-2611-30989-paper-ko]] — CC BY 4.0 본문 기술 번역·선별 부록·원문 표.
- [[worldleague-2611-30989-analysis]] — taxonomy·I/O·metric·전이 경계.
- [[worldleague-2611-30989-references]] — 핵심 9편과 연구 관계.
- [[worldleague-2611-30989-learning]] — 실행 검증한 교육 toy 두 개.
