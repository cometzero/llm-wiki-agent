---
title: "AI System Design"
type: concept
tags: [ai-ml, system-design, architecture]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
AI 시스템 설계는 "모델을 어떻게 만들고, 어떻게 서비스하고, 어떻게 계속 개선할 것인가"를 전체적으로 설계하는 일이다. [[DataPipeline]], [[TrainingStack]], [[InferenceStack]], [[FeedbackLoop]]가 포함된다.

## The Complete Picture

```
┌─────────────────────────────────────────────────────────┐
│                    AI System                            │
├─────────────────────────────────────────────────────────┤
│  Data Pipeline → Training Stack → Evaluation            │
│       ↑                                    ↓            │
│       └────────── Feedback Loop ←── Inference Stack    │
└─────────────────────────────────────────────────────────┘
```

## Six Key Components

### 1. Data Pipeline
데이터를 수집, 정제, 변환, 저장하는 흐름. 텍스트 tokenization, 이미지 resize, tabular 결측치 처리 포함.

### 2. Training Stack
모델 구조, loss, optimizer, GPU 학습, checkpoint 저장, validation 평가. Gradient가 loss를 줄이는 방향으로 weight를 업데이트.

### 3. Evaluation Layer
학습된 모델이 실제 목표에 맞게 좋아졌는지 확인. 공개 benchmark와 내부 eval set을 함께 봄.

### 4. Inference Stack
모델을 API로 배포하고 실제 요청을 처리. Serving, batching, KV cache, quantization, monitoring 포함.

### 5. Product Layer
사용자가 보는 UI, prompt, policy, 권한, 로그, 안전장치.

### 6. Feedback Loop
사용자 반응과 실패 사례를 수집해 데이터, prompt, 모델, 평가 기준을 개선하는 순환 구조.

## Key Insight
AI 시스템 = 모델이 아니다. 모델은 핵심 부품이지만, 데이터, 평가, serving, monitoring, feedback까지 포함해야 실제 시스템이다.

## Common Failure Points
- 데이터가 지저분해서 학습이 잘 안 됨
- 학습 데이터와 실제 서비스 데이터가 다름 ([[DataDrift]])
- Offline benchmark는 좋은데 실제 사용자 만족도는 낮음
- 모델은 잘 만들었지만 serving 비용이 너무 큼
- 배포 후 오류를 추적할 모니터링이 없음
- 사용자 feedback이 다음 학습 데이터로 연결되지 않음

## Connections
- [[DataPipeline]] — 데이터 흐름
- [[TrainingStack]] — 학습 흐름
- [[InferenceStack]] — 서빙 흐름
- [[FeedbackLoop]] — 개선 흐름
- [[RAG]] — AI 시스템의 한 예시
- [[DataDrift]] — 학습/서비스 데이터 불일치
