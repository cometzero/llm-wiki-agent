---
title: "Transformer Engine"
type: concept
tags:
  - NVIDIA
  - Transformer
  - Precision
  - Inference
  - Training
sources:
  - nvidia-hopper-아키텍처-심층-분석하기-nvidia-technical-blog
last_updated: 2026-05-03
---

## Definition
[[TransformerEngine]]는 대규모 모델에서 레이어별 연산 특성(특히 텍스트/시퀀스 모델)을 고려해 정밀도 모드를 동적으로 조정하는 실행/최적화 개념이다.

## 핵심 기능
- [[FP8]]/[[FP16]]/[[BF16]] 사용 구간을 동적으로 조정해 정확도-속도 균형을 관리한다.
- [[H100]] 계열에서 추론 지연 및 처리량 개선의 중심 모듈로 소개된다.
- 긴 문맥과 높은 동시성 환경에서 메모리 사용량을 낮추는 데 기여한다.

## 활용 맥락
- [[Transformer]] 기반 LLM 추론에서 디코드 병목을 줄이고, 안정적인 토큰 생성 동작(체감 지연 감소)과 효율을 함께 노리는 시스템 설계에 사용된다.

## 연결
- [[FP8]]
- [[AIFactory]]
- [[NVIDIA]]
- [[H100]]
