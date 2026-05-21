---
title: "Tool Use"
type: concept
tags: [llm, agent, external, capability]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Tool Use

## 정의

Tool use는 [[LLM]]이 검색, 계산기, 코드 실행, API 호출 같은 외부 도구를 사용하게 하는 방식이다.

## 왜 필요한가

[[PromptEngineering]]의 한계를 보완:
- **정확한 계산**: Calculator tool이나 코드 실행
- **실시간 정보**: 웹 검색
- **외부 시스템**: API 호출으로 데이터 조회
- **작업 수행**: 파일 쓰기,メール送信など

## [[RAG]]과의 비교

| 구분 | [[RAG]] | [[ToolUse]] |
|------|---------|--------------|
| 목적 | 문서 기반 답변 | 구체적 작업 수행 |
| 방식 | 검색 + 생성 | 함수 호출 |
| 예시 | FAQ 검색 | 계산, 검색, 코드 실행 |

## AI Agent와의 관계

Tool use는 [[AI에이전트]]의 핵심 능력:
- 계획 수립 → tool 선택 → 실행 → 결과 반영

## 연관 개념

- [[PromptEngineering]] — 도구 사용 지시 설계
- [[RAG]] — 문서 검색 도구
- [[AI에이전트]] — tool use를 활용하는 시스템

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
