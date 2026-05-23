---
title: "Data Drift"
type: concept
tags: [ai-ml, ml-ops, monitoring]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Data drift (또는 distribution shift)는 학습 때 본 데이터와 실제 서비스 데이터의 성격이 달라지는 현상이다. 입력 x의 분포가 변하여 모델 성능이 저하될 수 있다.

## Why It Happens
- 시간이 지나면서 실제 데이터의 패턴이 변함
- 학습 시점의 가정이 실제와 다름
- 새로운 유형의 입력이나 레이블이 등장
- 외부 환경 변화 (계절, 트렌드, 정책 등)

## Example
- 학습 때는 짧은 질문만 봤는데, 서비스에서는 긴 문서와 복잡한 질문이 들어옴
- 의료 AI에서 새로운 질환이나 치료법이 등장
- 추천 시스템에서 사용자 취향이 변함

## Impact
- Offline benchmark는 좋은데 실제 사용자 만족도는 낮음
- 모델이 학습 데이터에 overfitting됨
- 예측 정확도가 점차 저하

## Mitigation
- 지속적인 모니터링 ([[Monitoring]])
- 정기적인 재학습
- [[FeedbackLoop]]로 실제 데이터 반영
- Drift detection 시스템 구축

## Connections
- [[FeedbackLoop]] — drift 감지와 개선 연결
- [[Monitoring]] — drift 감지 도구
- [[Evaluation]] — 성능 저하 감지
- [[DataPipeline]] — drift 데이터 수집
