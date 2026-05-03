---
title: "Kimi K2"
type: entity
tags:
  - MoE
  - LLM
  - OpenSourceModel
  - FFN
source: nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Profile
[[KimiK2]]는 본 소스에서 FFN 가중치 비중이 극단적으로 높은 오픈소스 MoE 계열 모델 사례로 제시된다.

## Key Claims
- 레이어당 여러 라우팅된 전문가를 갖는 대형 MoE 구조로 설명된다.
- FFN이 모델 총 파라미터에서 거의 99%에 가까운 비중으로 나타나 LPX 오프로딩의 대상성이 높다고 제시된다.
- FFN 크기 추정치가 모델 디스크 요구량 결정에 직접 사용되며, 랙 간 확장 필요성 판단의 정량 예시가 된다.

## Connections
- [[MoE]] — Kimi K2의 핵심 구조.
- [[FFN]] — 모델 파라미터의 주요 구성비.
- [[Groq3LPX]] — 디코드 FFN 가속 적용 대상 모델군의 사례.
- [[LPXRack]] — 초대형 오픈소스 모델 크기 대응 시의 연결성 스케일링 포인트.

## Notes
모델 규모 표기는 소스 간 표기 방식 차이가 있으므로, 공개 평가 자료와 재확인이 권장된다.