---
title: "AutoResearch"
type: concept
tags: [automation, research-ops, llm]
last_updated: 2026-04-21
sources: [andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai]
---

## Definition
[[AutoResearch]]는 인간의 매뉴얼 개입을 최소화하고 에이전트가 연구 목표(목표·제약·평가지표)를 따라 반복 실험·튜닝·평가를 수행하도록 설계한 자율 연구 운영 패턴이다.

## Core Mechanism
- 연구자가 매크로 수준의 목표와 검증 규칙을 제공
- 에이전트가 아이디어 생성, 실험 제출, 성능 평가를 자동 실행
- 발견-검증 분리(discovery cheap, verification costly/expensive) 아키텍처

## Evidence in Source
- [[AndrejKarpathy]]는 GPT 계열 튜닝에서 자율 루프가 놓쳤던 하이퍼파라미터 조정 아이디어를 찾아냈다고 설명한다.
- 소규모 탐색 결과를 대규모 모델에 외삽하는 방식과, 작업자 풀을 통한 분산 검증 구조를 제안한다.

## Risks / Limits
- 검증 불가한 주관적 영역에서는 적용 한계 존재.
- 지표 과적합(overfitting to metrics) 방지를 위한 메타 지표 설계가 필요.

## Related
- [[LLMAgents]]
- [[Speciation]]
- [[program MD]]
- [[오픈소스AI]]
