---
title: "GPT-5.5"
type: entity
tags: [OpenAI, LLM, Coding Assistant, Reasoning]
last_updated: 2026-05-10
source: [the-coding-assistant-breakdown-more-tokens-please]
---

## Profile

[[GPT-5.5]]는 [[OpenAI]]가 제시한 코딩 중심 고성능 추론 모델군으로, 복잡한 추론과 구조 분석이 필요한 작업에서 강점이 있다고 요약된다.

## Key Characteristics

- 가격(공개 기준): 입력 100만 토큰당 5달러, 출력 100만 토큰당 30달러.
- 추론 수준 옵션이 다양하며, 비용-품질 조합을 위해 `xhigh`, `high`, `low`, `non-reasoning` 계열이 언급된다.
- [[OpenAI]]는 [[GPT-5.5 Pro]]를 별도 제품군으로 취급하며 연구/장기 추론 중심 사용을 강조한 것으로 제시된다.
- [[TokenEconomy]] 관점에서 같은 문제를 덜 토큰으로 처리할 수 있는 경향을 보여, 총 비용에서 상대적 경쟁력이 생길 수 있음.

## Role in Workflows

- 긴 사유가 필요한 리팩터링, 버그 추적, 코드 구조 이해 및 설득형 설명 생성에서 상대적 우세로 제시됨.
- 실무에서는 [[Claude]] 계열과 조합해 초기 의도 확정/스캐폴딩-정교한 구현 분할 전략에 투입되는 하이브리드 편성에서 쓰임.

## Connections

- [[OpenAI]]
- [[OpenAI API]]
- [[Codex]]
- [[ClaudeOpus47]]
- [[SWE-bench]], [[SWE-bench Verified]]
- [[TokenEconomy]], [[Token Efficiency]

## Notes

[[DeepSeek V4]], [[Claude Opus 4.7]]과 비교 시 모델 본체 성능보다 작업 맥락과 토큰 정책이 더 큰 분기점이 될 수 있다고 본문에서 정리된다.