---
title: "Verifiability"
type: concept
tags:
  - 신뢰성
  - 테스트
  - 엔지니어링 거버넌스
  - 릴리즈 품질
last_updated: 2026-05-03
---

## Summary
[[Verifiability]]는 AI가 만든 변경사항의 정확성과 안전성을 사람이 코드 전부를 읽지 않고도 판단할 수 있게 만드는 성질이다. 

## Core Principle
- 입력/출력, 성공/실패 케이스, 성능/안전 제약이 명확할수록 검증이 쉬워진다.
- 스트레스 테스트, E2E 시나리오, 회귀 체크포인트를 통해 실행 기반 신뢰도를 확보한다.

## Practical Signals
- 체크포인트 테스트 통과율
- 핵심 경계 조건 동작 일관성
- 예외 처리 및 롤백 시나리오 동작성

## Connections
- [[TestDrivenDevelopment]]
- [[VibeCoding]]
- [[LeafNode]]
- [[AIPM]]
- [[Claude]]

## Notes
- 본 개념은 코드 이해의 완전성보다 결과의 재현 가능성과 예측 가능성을 중시한다.