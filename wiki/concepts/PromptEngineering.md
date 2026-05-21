---
title: "Prompt Engineering"
type: concept
tags: [llm, prompt, instruction, interaction]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Prompt Engineering

## 정의

Prompt engineering은 [[LLM]]에 넣는 입력 문장, 지시문, 예시, 출력 형식, 제약 조건을 설계하는 작업이다.

## 왜 중요한가

[[LLM]]은 버튼처럼 하나의 정답만 내는 프로그램이 아니다. 입력된 token들을 바탕으로 다음 token의 확률분포를 계산하고 생성한다. 입력 prompt가 바뀌면:
- 내부 hidden state가 바뀐다
- [[Attention]]이 보는 문맥이 바뀐다
- 최종 출력이 바뀐다

## Prompt 구성 요소

1. **Role**: "너는 친절한 AI 튜터다"
2. **Task**: "이 문서를 요약하라"
3. **Context**: 참고 배경 정보나 문서
4. **Constraints**: "근거 없는 내용은 말하지 마라"
5. **Examples**: [[FewShotPrompting]]
6. **Output format**: JSON, Markdown, bullet list
7. **Evaluation hint**: 좋은 답변의 기준

## [[PromptSensitivity]]

Prompt의 작은 변화에도 출력이 달라질 수 있다:
- "간단히 설명해 줘" vs "초보자에게 자세히 설명해 줘"
- 같은 의미처럼 보여도 다른 신호가 될 수 있다

## 한계

Prompt engineering은 만능이 아니다:
- 모델이 모르는 최신 정보를 알아낼 수 없다 → [[RAG]] 필요
- [[ContextWindow]]보다 긴 문서를 완벽히 기억하게 할 수 없다
- 정확한 계산은 [[ToolUse]]가 더 안전할 수 있다

## 연관 개념

- [[RAG]] — 보완 관계
- [[ContextWindow]] — 입력 제한
- [[ToolUse]] — 보완 관계
- [[InstructionDesign]] — 하위 개념
- [[FewShotPrompting]] — 기법 중 하나
- [[SystemPrompt]] — 역할/규칙 설정

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
