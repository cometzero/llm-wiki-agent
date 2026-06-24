---
title: "WAMTaxonomy"
type: concept
tags: [taxonomy, world-action-model, classification]
sources: [world-action-models-survey-2606-20781-analysis]
last_updated: 2026-06-24
---

# WAMTaxonomy

[[WorldActionModel]]의 3분류 설계 철학.

## 세 가지 설계 철학

### 1. Render-and-Decode
- 미래를 visual/video로 렌더링
- 디코딩을 통해 action 정보 추출
- 장점: 직관적, visual quality 활용 가능
- 단점: 렌더링 overhead, latency 증가 가능

### 2. Latent-Only
- 잠재 공간에서만 미래 예측
- Visual 렌더링 없음
- 장점: 효율적, 빠른 inference
- 단점: interpretability 낮음

### 3. Video-Generation-Free
- Video 생성을 완전히 우회
- 직접 action 예측
- 장점: 가장 효율적
- 단점: visual feedback 없음

## 관련
- [[WorldActionModel]] — 정의 대상
- [[PredictiveSubstrate]] — substrate 결정이 taxonomy 분류와 연결
