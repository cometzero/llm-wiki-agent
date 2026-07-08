---
title: "Predicted Future"
type: concept
tags: [WAM, future-prediction, runtime-object]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
Predicted Future는 [[WAM]](World Action Model)이 생성하는 미래 상태 예측을 runtime에서 다루는 방식을 말한다. [[EmbodiedCpp]]는 predicted future뿐 아니라 latent future까지 runtime object로 처리한다.

## Runtime Considerations
- **Prediction cache**: 계산된 예측 재사용
- **Latent future validity**: 잠재 공간 예측의 유효성
- **Stale prediction invalidation**: 오래된 예측 무효화

## Connections
- [[WAM]] — prediction source
- [[LingBot-VA]] — WAM implementation
- [[EmbodiedCpp]] — runtime support for future representations
- [[LatentFuture]] — related concept
