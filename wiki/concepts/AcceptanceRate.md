---
title: "Acceptance Rate"
type: concept
tags:
  - SpeculativeDecoding
  - InferenceOptimization
  - Latency
last_updated: 2026-05-03
sources:
  - an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference-nvidia-technical-blog
---

## 정의

[[AcceptanceRate]]는 [[SpeculativeDecoding]]에서 제안된 후보 토큰 중 [[TargetModel]]이 그대로 채택한 토큰 비율이다. 

총 생성량 대비 실제로 수락된 토큰 수를 의미하며, 드래프트 제안기 품질과 검증기 정합성의 직접적 성능 지표다.

## 의미

- 수락율이 높을수록 디코딩 단계 수 통합 효과가 커지고, 평균 응답 지연이 감소한다.
- 최악의 경우 수락율이 0에 가까워지면 사실상 표준 자기회귀와 유사한 단계 비용이 발생한다.

## 관계

- [[SpeculativeDecoding]], [[EAGLE3]], [[DeepSeekMTP]] 모두 수락율 특성에 따라 추론 성능 곡선이 달라진다.
- [[TargetModel]] 검증 전략(확률 비교, 거리)과 관련된다.