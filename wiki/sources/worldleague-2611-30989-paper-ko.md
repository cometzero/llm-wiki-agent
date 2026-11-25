---
title: "WorldLeague 한국어 기술 번역"
type: "source"
tags: ["VLA", "benchmark", "physical-agency"]
sources: ["worldleague-2611-30989-paper-ko"]
date: "2026-11-25"
last_updated: "2026-11-25"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W48/worldleague-2611-30989/paper-ko.md"
source_hash: "119f47213fdc690a"
source_url: "https://arxiv.org/html/2611.30989v1"
license: "CC BY 4.0"
---

## Summary
60개 physical goal을 여섯 capability dimension으로 묶고 VLM/VLA/WAM의 partial progress와 constraint-aware success를 비교한다. 본문 구조와 식 1–4, 전체 표 cell rows, 부록 A–F 선별 protocol을 한국어로 보존한다.

## Key Claims
- QA 전부 정답인 347개 VLM episode 중 249개는 physical credit 0이며, Kimi T41은 item credit 100이어도 constraint 위반으로 실패한다.
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
