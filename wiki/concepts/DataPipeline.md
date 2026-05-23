---
title: "Data Pipeline"
type: concept
tags: [ai-ml, system-design, data-engineering]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Data pipeline은 데이터를 수집하고, 정제하고, 저장하고, 학습 가능한 형태로 만드는 흐름이다. 텍스트라면 tokenization, 이미지라면 resize와 normalization, tabular data라면 결측치 처리가 포함된다.

## Role in AI System
1. **수집**: 다양한 소스로부터 데이터 모으기
2. **정제**: 개인정보 제거, 중복 제거, 형식 통일
3. **변환**: 모델 입력 형태로 변환 (tokenization, embedding 등)
4. **저장**: 학습/추론에 적합한 형태로 저장

## Why It Matters
"Garbage in, garbage out" — 좋은 모델도 나쁜 데이터 위에서는 나쁜 결과를 낸다. 실제 AI 프로젝트 실패의 주요 원인 중 하나가 데이터质量问题이다.

## Common Issues
- 학습 데이터와 실제 서비스 데이터의 분포 차이 ([[DataDrift]])
- 데이터가 지저분해서 학습이 잘 안 됨
- 개인정보/민감정보 포함
- 레이블 품질 문제

## Connections
- [[TrainingStack]] — pipeline으로 가공된 데이터가 학습에 사용됨
- [[FeedbackLoop]] — 사용자 feedback이 pipeline에 다시流入
- [[Evaluation]] — pipeline 데이터로 eval set 구성
- [[DataDrift]] — 학습/서비스 데이터 불일치 문제
