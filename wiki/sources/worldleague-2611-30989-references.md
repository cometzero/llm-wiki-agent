---
title: "WorldLeague 핵심 참고문헌 9편"
type: "source"
tags: ["VLA", "benchmark", "physical-agency"]
sources: ["worldleague-2611-30989-references"]
date: "2026-11-25"
last_updated: "2026-11-25"
source_file: "raw/Robotics/HuggingFaceWeeklyPapers/2026-W48/worldleague-2611-30989/references.md"
source_hash: "11265b04d9c229e0"
source_url: "https://arxiv.org/html/2611.30989v1"
license: "CC BY 4.0"
---

## Summary
원문 bibliography 63개와 Semantic Scholar references 62개를 구분해 핵심 9편을 선택했다. SayCan, V-JEPA 2, Show-Harness, ESI-Bench, Inner Monologue, π0.5, OpenVLA, BEHAVIOR-1K, DreamZero를 action interface와 평가 단위 관점에서 연결한다.

## Key Claims
- V-JEPA 2-AC 적용과 generator 기반 online RL은 future work다. 인용된 OpenVLA/DreamZero가 원문 주표 baseline이라는 뜻은 아니다.
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
