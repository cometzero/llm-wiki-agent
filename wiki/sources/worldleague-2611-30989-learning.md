---
title: "WorldLeague 핵심 기술 학습"
type: "source"
tags: ["VLA", "benchmark", "physical-agency"]
sources: ["worldleague-2611-30989-learning"]
date: "2026-11-25"
last_updated: "2026-11-25"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W48/worldleague-2611-30989/learning.md"
source_hash: "fe076380c5538bac"
source_url: "https://arxiv.org/html/2611.30989v1"
license: "CC BY 4.0"
---

## Summary
Goal predicate와 constraint 분리, task-equal weighting, history dependence, observation freshness와 stable interval을 예제 중심으로 설명한다. 최종 Markdown의 Python block 두 개를 실제 실행해 assert를 통과했다.

## Key Claims
- 교육 toy는 original benchmark 실행이 아니며 실제 robot control, contact dynamics 또는 safety certificate를 재현하지 않는다.
- [[WorldLeague]]는 [[GoalPredicateEvaluation]]으로 progress와 full success를 분리한다.

## Key Quotes
직접 인용 대신 원문 attribution 아래 한국어 기술 번역·독립 해설을 제공한다. 상세 source와 범위는 raw 문서에 명시한다.

## Connections
- [[WorldLeague]] — 이 문서의 연구 대상.
- [[GoalPredicateEvaluation]] — outcome 기반 평가의 핵심.
- [[ClosedLoopEvaluation]] — physical feedback을 사용하는 simulation 평가.
- [[VisionLanguageAction]] — native numerical policy 평가 대상.

## Contradictions
기존 VLA scaling·harness·status 연구의 개선을 부정하지 않는다. Representation 능력, command completion, terminal QA와 physical goal achievement는 평가 대상이 달라 score를 대체할 수 없다.
