---
title: "DeepSeek R1"
type: entity
tags:
  - DeepSeek
  - LLM
  - MoE
  - FFN
  - Transformer
source: nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Profile
[[DeepSeekR1]]은 오픈소스 대형 LLM 사례로, FFN 파라미터 비중 분석에서 LPX 사이징/오프로딩 논의를 정량화하는 데 활용되는 모델로 등장한다.

## Key Claims
- 계층 수 61개, 일부 레이어는 dense FFN, 다수 레이어는 [[MoE]] 구조를 채택한다.
- FFN 가중치 총량이 모델 전체에서 압도적 비중을 차지해 디코드 경로 오프로딩 타당성의 대표 사례가 된다.
- FP8으로 환산한 FFN 디스크 크기 수치가 큼으로 다중 LPX 연동 필요성이 제기된다.

## Connections
- [[MoE]] — DeepSeek R1 내부 FFN/MoE 구성 분석의 핵심.
- [[FFN]] — 모델 전체 가중치 점유율이 높음.
- [[Groq3LPX]] — 오프로딩 대상 규모 산정에 자주 사용되는 사례.
- [[LPXRack]] — 대형 모델 사이징에서 멀티랙 연동 논리의 근거 대상.

## Notes
출처 기반 크기 수치와 공개된 모델 배포 수치 간 차이가 있을 수 있으므로 검증이 필요하다.