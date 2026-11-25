---
title: "WorldLeague 분석"
type: "source"
tags: ["VLA", "benchmark", "physical-agency"]
sources: ["worldleague-2611-30989-analysis"]
date: "2026-11-25"
last_updated: "2026-11-25"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W48/worldleague-2611-30989/analysis.md"
source_hash: "ed185799018506e1"
source_url: "https://arxiv.org/html/2611.30989v1"
license: "CC BY 4.0"
---

## Summary
Physical agency는 설명·command completion과 달리 timestamped world outcome으로 평가해야 한다. Native control과 VLM harness는 shared goal을 쓰지만 robot·interface·context가 달라 system-level 비교로 해석한다.

## Key Claims
- Simulation closed-loop benchmark이며 real vehicle, NPU profiling, formal safety evidence가 아니다. 대부분 single episode이고 Sol만 full second-seed suite를 수행한다.
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
