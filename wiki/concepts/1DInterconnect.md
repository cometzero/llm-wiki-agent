---
title: "1D Interconnect"
type: concept
tags:
  - Interconnect
  - Dataflow
  - DeterministicExecution
  - LPU
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
1차원 인터커넥트는 LPX 내부 기능 유닛 간 통신을 동/서 방향의 단일 홉 경로로 규칙화하여 데이터 이동을 예측 가능하게 만드는 통신 모델이다.

## Claims from Source
- 컴파일러가 각 hop 수를 정확히 산정해 동기화를 최소화한다.
- 큐/경쟁 구조를 줄여 스케줄링 복잡성을 낮추고 결정론적 실행을 강화한다.
- 디코드 단계에서의 반복 토큰 흐름을 안정적으로 처리하는 데 유리한 동작 모델로 제시됨.

## Relations
- [[DeterministicExecution]] — 예측 가능성의 물리/네트워크 기반.
- [[LPU]] — 내부 유닛간 데이터 이동 경로.
- [[StreamRegister]] — 이와 유사한 개념으로 본문의 이동 경로 설명에 등장.