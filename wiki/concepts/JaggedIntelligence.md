---
title: "Jagged Intelligence"
type: concept
tags: [llm-behavior, reliability, distribution-shift, verification]
sources: [그만-알아야할만-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필요-인스터스]
last_updated: 2026-05-10
---

## 정의

[[JaggedIntelligence]]는 [[LLM]] 성능이 과제별로 심하게 들쭉날쭉한 특성을 설명하는 비공식 용어이다. 즉, 어떤 과제에서는 천재적이지만 인접 과제에서는 비상식적으로 오답을 낼 수 있는 상태.

## 핵심 내용

- [[Reinforcement Learning]] 기반으로 학습된 모델은 보상 함수가 잘 설계된 영역에서 매우 강력하다.
- 그러나 비가시성/비정형/맥락 미스매치 구간에서는 급격한 실패를 보일 수 있다.
- [[AndrejKapassi]] 인터뷰는 제로데이 취약점 탐지, 대규모 코드 작업 같은 고난도 작업에서도 운전 실수성 사례를 비유로 제시한다.

## 연결

- [[ContextWindow]], [[DistributionShift]], [[Validation]], [[Verifiability]], [[AI에이전트]]
- [[Understanding]] 중심의 인간 감독과 [[Thinking]] 자동화 분리는 이런 실패 완화의 기반이다.