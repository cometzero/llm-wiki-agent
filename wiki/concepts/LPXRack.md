---
title: "LPX Rack"
type: concept
tags:
  - RackScaleSystem
  - InferenceAccelerator
  - C2C
  - LPX
  - Scalability
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
LPX 랙은 다수 LPX 칩(예: LP30 기반)을 하나의 랙 단위로 통합한 추론 가속 플랫폼 인프라 개념이다. 트레이/랙/래크 간 통신 구조를 통해 디코드 오프로딩 스케일링을 구성한다.

## Structural Notes
- 트레이 단위에서 로컬 full-graph 유사 연결 구조가 강조됨.
- 4개 스파인 계열의 스케일업 도메인과 인접 랙으로 확장되는 스케일아웃 도메인이 병행 운영됨.
- 랙 간 링크는 의도적으로 희소성을 유지하여 전역 연결과 도메인별 대역폭 효율의 균형을 맞추려는 설계 의도로 읽힌다.

## Relations
- [[RealScale]] — LPX 랙 링크 동작의 핵심 인터커넥트.
- [[LPU]] — 랙 내에서 오프로딩 실행 엔진.
- [[FFNOffloading]] — 랙 구성의 본질적 사용 사례.
- [[DecodeDisaggregation]] — 랙 단위 오퍼레이션이 분리형 추론에서 실효성을 결정.
- [[NVIDIADynamo]] — 랙 단위/노드 단위 라우팅 관리 레이어.