---
title: "Coding LLM Benchmarks"
type: concept
tags: [Benchmark, LLM, Software Engineering, Code Agents]
last_updated: 2026-05-10
sources: [the-coding-assistant-breakdown-more-tokens-please]
---

## Definition

[[Coding LLM Benchmarks]]는 코딩 도메인에서 대형 언어모델의 성능을 측정하는 비교 체계를 의미한다. 본 개념은 공개 정량 지표(MMLU, GSM8K, SWE-bench 등)와 도구-기반 작업 성능을 모두 포함하지만, 단일 숫자로 AI 도구 전체 능력을 대변할 수 없다는 점을 강조한다.

## Why It Is Different

코딩 벤치는 세 요소에 의해 크게 바뀐다.

- [[Tasks]]: 실제로 주는 문제의 구조와 모호성
- [[Evaluation Method]]: 점수 산출 방식(자동 채점, 휴먼 심사, 루브릭)
- [[Harness]]: 툴/컨텍스트/세션 정책(실행 가능성, 데이터 노출, 테스트 가시성)

## Risk Areas

- 작업 정의가 과소하거나 과도하게 좁을 경우, 잘못된 정답률이 생김.
- 평가가 단일 테스트 패턴에 과적합되어 "점수 상승"이 실제 업무 효율과 불일치.
- 작업 설명과 테스트 간 불일치로 인한 오탐/오판 가능성.
- [[BenchmarkContamination]]과 데이터 누수의 영향이 커질 수 있음.

## Core Example Set

- [[SWE-bench]], [[SWE-bench Verified]], [[SWE-bench Pro]]: PR 기반 코딩 작업의 대표군.
- [[HumanEval]], [[GPQA]], [[HLE]], [[MMLU]]: 정적 정답형 대표성의 한계가 큼.
- [[GDPval]], [[OSWorld]], [[Tau-bench]]: 멀티툴·비코딩 작업과의 경계 확장형 벤치로 이동 중인 흐름.

## Practical Guidance

코딩 모델의 실사용 비교는 동일 벤치 숫자만으로 판단하지 않고, 모델별 장점을 결합한 [[HybridLLMCodingWorkflow]](예: 초기 설계는 Opus 계열, 정밀 구현은 Codex 계열)로 운영 지표를 측정해야 한다.

## Related Links

- [[TokenEconomy]]
- [[Evaluation]
- [[ToolUse]
- [[ClaudeOpus47]]
- [[GPT-5.5]]
- [[OpenAI]], [[Anthropic]], [[DeepSeek]]