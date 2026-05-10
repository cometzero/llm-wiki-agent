---
title: "Automated Code Review"
type: concept
tags: [code-quality, AI-agent, workflow]
last_updated: 2026-05-10
sources:
  - 99-가-모르는-하네스-엔지니어링-ai-에이전트-생산성을-10배-올리는-세팅법-바이브마피아-최수민님
---

## 정의

[[AutomatedCodeReview]]는 AI가 작성한 변경사항을 도구 기반으로 1차 검토하고, 사람이 최종 판단하는 하이브리드 품질 보증 방식이다. 본문에서는 [[CodeRabbit]]와 [[PR]] 자동 생성/반영 루프를 결합한 사례를 설명한다.

## 동작 요소

- 구현된 커밋 단위 생성
- PR 생성
- 리뷰 코멘트 분석 및 반영
- 사람의 최종 승인

## 장점

- 리뷰 병목 완화
- 반복적인 스타일/규칙 위반 자동 감지
- PR 단위의 문맥 유지(코드 + 코멘트)

## 한계

- 도메인 판단, 비정형 UX 의도, 제품 가치 판단은 사람 검토가 필수.
- 자동 리뷰의 결과는 참고 신호로 다루고, 최종 의사결정자는 인간이 되어야 함.

## 관련

- [[CodeReview]], [[PR]], [[HarnessEngineering]], [[AI에이전트]]
