---
title: "Feedback Loop"
type: concept
tags: [ai-ml, system-design, continuous-improvement]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Feedback loop는 사용자 반응과 실패 사례를 다시 개선 과정에 반영하는 순환 구조이다. AI 시스템은 "일회성 프로젝트"가 아니라 "계속 돌아가는 개선 루프"이다.

## How It Works
1. 사용자가 답변에 대해 "도움 됨/안 됨" 피드백 제공
2. "안 됨" 사례를 모아 분석
3. 데이터, prompt, 검색 방식, 모델, 평가 기준 개선
4. 개선된 버전으로 다시 배포
5. 새로운 피드백 수집 (순환)

## Why It Matters
- 데이터가 바뀌고, 사용자 질문이 바뀌고, 제품 목표가 바뀌면 모델도 평가도 업데이트되어야 함
- 배포 후 실제 문제가 드러나며, monitoring과 feedback loop가 없으면 개선이 어려움
- 같은 실패가 반복되는 것을 방지

## Example: Customer Service Chatbot
1. 고객 문의 1만 건 수집
2. 개인정보 제거, 자주 묻는 질문 분류
3. FAQ 문서 embedding 생성
4. 사용자 질문 시 관련 문서 검색
5. LLM이 검색된 문서로 답변
6. 사용자 "도움 됨/안 됨" 피드백 수집
7. "안 됨" 사례 → 프롬프트/검색/문서/모델 개선

## Connections
- [[DataPipeline]] — feedback이 데이터로 다시流入
- [[Evaluation]] — 피드백 기반 평가 기준 개선
- [[InferenceStack]] — 모니터링을 통한 피드백 수집
- [[TrainingStack]] — 피드백 기반 재학습
