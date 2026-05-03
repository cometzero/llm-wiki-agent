---
title: "LPU"
type: concept
tags:
  - Accelerator
  - Inference
  - GPU
  - LLM
  - DeterministicExecution
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
[[LPU]](Language Processing Unit)는 LLM 추론에서 특정 연산군(특히 FFN/MoE 경로)에서 높은 예측 가능성과 고대역폭 메모리 접근을 제공하도록 설계된 전용 가속기 개념이다. 본 문맥에서 [[NVIDIA]] [[Groq3LPX]]의 핵심 실행 엔진으로 사용된다.

## Claims from Source
- 320-byte(INT8)/640-byte(FP16) 기반 고정 벡터 단위와 기능 유닛 구성을 통해 컴파일러가 위치·시간을 결정적으로 관리할 수 있다.
- 컴파일러 중심의 스케줄링을 통해 동적 경합(캐시 충돌·가변 큐 관리)을 제거해 실행 변동을 줄인다.
- 온칩 SRAM 기반 흐름에서 FFN 가중치/활성화 이동을 반복적으로 처리하기 유리하며, 대형 모델의 디코드 병목 완화에 적합하다는 주장.
- [[DeterministicExecution]]의 핵심 도구로, 추론 지연의 예측성과 tail 안정화에 기여한다.

## Relations
- [[Groq3LPX]] uses LPU as decode-side accelerator.
- [[FFN]]은 LPX-LPU 오프로딩의 핵심 대상이다.
- [[NVIDIADynamo]]가 LPU와 GPU 간 활성화 토큰 이동을 조정한다.
- [[DecodeDisaggregation]]에서 LPU는 FFN/MoE 단계에 대응한다.