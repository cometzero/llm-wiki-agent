---
title: "Feedback Loop"
type: concept
tags: [ai-ml, mlops, system-design, continuous-improvement]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[FeedbackLoop]]는 사용자의 반응, 실패 사례, [[Evaluation]] 결과를 다시 데이터와 모델 개선으로 연결하는 순환 구조이다. 이 loop가 있어야 시스템이 시간이 지나며 좋아질 수 있다.

## Key Concepts

### Feedback Sources
- 사용자의 "도움 됨/도움 안 됨" 클릭
- 상담원의 틀린 답변 표시
- [[Evaluation]]에서의 실패 사례
- 버그 리포트, 고객 불만

### How Feedback is Used
- 실패 사례를 eval set에 추가
- 데이터 정리 및 재수집
- Prompt 수정
- Retrieval 개선
- Fine-tuning 데이터 보강

### Importance
- "모델을 한 번 학습하고 끝"이 아니라 "계속 평가하고, 실패 사례를 모으고, 다시 개선하는" 구조
-.eval 100문제 중 70개 맞히던 시스템이 78개로 개선 = 8문제 향상 = 다음 설계 결정의 근거

### Caution
- [[FeedbackLoop]]는 "사용자 데이터를 무조건 학습에 넣는다"가 아님
- 개인정보, 동의, 품질 검수, 안전성 기준 필요
- 잘못된 feedback을 그대로 넣으면 모델이 오히려 나빠질 수 있음

## Connections
- [[Evaluation]] — 피드백 수집의 기준
- [[DataPipeline]] — 피드백 데이터 재처리
- [[TrainingStack]] — 개선된 모델 재학습
- [[Serving]] — 개선된 모델 배포

## Practical Notes

하루에 질문 100개 중 20개에서 "도움 안 됨" 클릭 → 20개 모아 분석 → 모델이 약한 주제 발견 → 다음 버전에서 12개 개선 = 실제 제품 품질 향상.
