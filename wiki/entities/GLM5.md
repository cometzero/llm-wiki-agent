---
title: "GLM 5"
type: entity
tags:
  - OpenSourceModel
  - MoE
  - FFN
  - BF16
source: nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Profile
[[GLM5]]는 BF16 기반 오픈소스 LLM 사례로, 디스크 크기와 FFN 가중치 비중이 매우 높아 LPX 랙 확장 비용 비교에서 상위 사례로 제시된다.

## Key Claims
- FFN 가중치가 모델 총량의 상당 부분을 차지해 LPX 오프로딩 모델군에 해당한다.
- BF16 저장 기준으로 큰 디스크 크기가 요구될 수 있어 LPX 멀티랙 연동 필요성을 강화한다.
- 오픈소스 LLM 인프라 크기 추정의 실무 사례로 FFN 중심 성능 분석에서 반복 인용된다.

## Connections
- [[FFN]] — 핵심 오프로딩 대상 가중치 블록.
- [[MoE]] — 대형 오픈소스 구성에서 자주 함께 등장.
- [[LPXRack]] — 다중 랙 확장 판단의 테스트 사례.
- [[Groq3LPX]] — FFN 중심 인프라 대응 논리의 대상.

## Notes
본 항목은 주어진 기사 기반 기술 요약이며, 모델 공식 스펙은 공개 릴리즈 문서를 병행 확인한다.