---
title: "NVIDIA Groq 3 LPX: Everything we know - StorageReview.com"
type: source
tags:
  - NVIDIA
  - Groq3LPX
  - LPU
  - LP30
  - LPXRack
  - RealScale
  - HeterogeneousInference
  - FFN
  - MoE
  - DecodeDisaggregation
  - DeterministicExecution
  - SpeculativeDecoding
  - NVIDIADynamo
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/nvidia-groq-3-lpx-everything-we-know-storagereview.com.md
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Summary
[[StorageReview]]의 이 문서는 [[NVIDIA]]가 [[NVIDIAGroq3LPX|Groq 3 LPX]]를 [[VeraRubinPlatform]]에 맞춰 재구성한 하이브리드 추론 아키텍처를 상세화한다.
핵심 아이디어는 FFN/[[MoE]] 중심의 디코드 병목을 LPX의 [[LPU]]가 담당하고, 긴 문맥과 상호작용성(workload에서의 지연 민감 구간)은 [[NVIDIA Vera Rubin GPU]]가 처리하는 기존 추론 파이프라인과 분리한다는 점이다.

특히 LPX는 결정론적 실행과 고대역폭 온칩 메모리 이동을 앞세워, 긴 문맥과 잦은 도구-검증 루프를 가진 AI 서비스에서 토큰 간 지연 변동을 줄이려는 방향을 보인다. 또한 랙 스케일 네트워크 토폴로지(전면 C2C, 1D 인터커넥트, 어셈블리 라인식 구성), FFN 파라미터 비중 정량화, 추측 디코딩 워크플로우의 draft/verifier 분리를 결합해 실서비스 운영 관점을 강화한다.

## Key Claims
- [[NVIDIA]]의 [[Groq3LPX]]는 FFN(Feed-Forward Network) 연산 병목을 오프로딩하기 위해 설계된 rack-scale 하이브리드 인프라로, [[VeraRubinPlatform]]와 결합해 인터랙티브 추론의 저지연성을 목표로 한다.
- 2026년 하반기 출시를 전제한 [[LPXRack]]은 기존 [[CPX]] 개념에서 진화했으며, 문맥 처리에서 추론 핵심 병목이 되는 디코드/FFN 구간에 특화된 LPU 기반 가속을 추가한다.
- [[LPU]]는 320-byte(INT8) 또는 640-byte(FP16) 320개 요소 벡터 단위를 기본 연산/통신 크기로 쓰며, `SXM`, `VXM`, `MXM` 등의 유닛과 `MEM`로 구성된다.
- LPX 내부 데이터 이동은 1차원 스트림 레지스터 기반 라우팅으로, 동/서 방향 단일 홉 이동 규칙이 컴파일러가 정확한 스케줄링을 수행할 수 있게 하여 [[DeterministicExecution]]을 강화한다.
- [[RealScale]]는 Groq의 소프트웨어 스케줄링형 C2C 인터커넥트로 동작하며, 기존 NVIDIA C2C의 캐시 일관성형 링크와 설계 의도가 다르다.
- LPU 간 랙 연결은 트레이(8칩), 랙(32트레이), 랙 간(대칭 포트)로 확장되며, 총 스케일업/스케일아웃 대역폭과 희소도 구조가 긴 문맥 모델에서 고정 대역폭 병목을 조절한다.
- 트레이당 256개 [[LP30]] 칩 구성에서 모든 칩 간 all-to-all 성격의 로컬 연결이 유지되어 드래곤플라이형 로컬 그룹 기반 통신 효율을 높인다.
- [[FFN]]은 트랜스포머에서 비용/연산 비중이 매우 높고, 오픈소스 대형 모델에서는 전체 가중치의 95~99%에 달하는 경우가 있어 오프로딩 가치가 높다.
- [[MoE]] 구조에서는 공유 토큰 집행 대비 많은 FFN 전문가 블록이 병렬 존재해, 토큰당 계산은 고정된 FFN 경로에서 처리되는 패턴이 LPX에게 유리하다.
- [[DecodeDisaggregation|디코드 분리]]는 prefill의 주류 GPU-주의 작업과 FFN/MoE 디코드 경로를 분할해, [[NVIDIADynamo]]가 활성화 이동, 라우팅, 지연 목표 기반 스케줄링을 맡는다.
- 긴 추론 체인의 추론형 서비스에서 디코드 단계는 상대적으로 병목이 증가하고, 접두사 캐싱은 사전 계산비용을 줄여 오히려 디코드 지연의 체감 중요도를 높인다.
- LPX는 추측 디코딩에서 초안 생성기 역할을 수행하고 GPU가 verifier 역할을 함으로써 초당 유효 토큰 수와 지연 완화 가능성을 함께 노린다.
- [[RealScale]]-기반 랙 설계는 단일 LPX에서 128GB SRAM(256칩 기준)으로 추론 가능한 FFN 규격을 잡아, DeepSeek R1급 모델은 다중 랙 연동이 필요하다는 sizing 근거를 제공한다.

## Key Quotes
> "FFN 연산 가속" — [[NVIDIA]]가 LPX의 핵심 임무로 제시한 구간을 요약한 표현

> "결정론적 실행" — 하드웨어 레벨의 스케줄러·인터커넥트·메모리 이동 편차를 낮추어 추론 예측성을 높인다는 점을 반복 강조한다.

> "오래 걸린 추론 체인에서 사용자 체감은 결국 디코드 지연을 따라 결정된다" — 문맥 창이 늘어날수록 attention은 비용이 증가하고 FFN은 모델 고정 비용이라는 주장에 대한 실무적 귀결.

## Connections
- [[NVIDIA]] — 플랫폼 및 생태계 주체
- [[Groq3LPX]] — 본 출처의 핵심 가속기
- [[LPU]] — LPX에서 오프로딩되는 실행 단위
- [[LP30]] — LPX 랙의 코어 추론 유닛
- [[LPXRack]] — 32트레이 단위 확장 구조를 가진 랙 스케일 배치
- [[RealScale]] — LPX C2C 인터커넥트 패턴
- [[VeraRubinPlatform]] — 긴 컨텍스트 prefill/attention을 담당하는 병렬 처리 면
- [[VeraRubinNVL72]] — 본문에서 긴 문맥 특화 성격으로 지칭되는 GPU 계열 기반
- [[NVIDIADynamo]] — prefill/decode 분리 오케스트레이션 레이어
- [[FFN]] — 디코드 병목의 핵심 블록
- [[MoE]] — 대형 오픈소스 LLM의 주요 FFN 형태
- [[DeterministicExecution]] — 지연 예측성과 수렴 안정성의 핵심 설계 원리
- [[DecodeDisaggregation]] — prefill/decode 분리 운영 패턴
- [[SpeculativeDecoding]] — LPX draft + GPU verifier 분리 관점에서 강화되는 최적화
- [[HeterogeneousInference]] — 이기종 분리 실행 전략의 상위 개념
- [[DeepSeekR1]] — FFN 규모 분석의 대표 모델 사례
- [[KimiK2]] — 전문가 수/파라미터 규모가 큰 오픈소스 사례
- [[OpenAIGPTOSS120B]] — 극단적 FFN 비중을 보인 오픈소스 사례
- [[GLM5]] — 대형 BF16 FFN 사례
- [[Qwen3]] — 오픈소스 MoE 모델군의 사례군
- [[StorageReview]] — 본 소스의 매체 출처

## Contradictions
- 기존 위키의 [[NVIDIA]] 추론 인프라 관점(특히 [[Groq3LPX]]가 prefill/attention 분리와 함께 작동한다는 프레임)과 직접 충돌하지 않으며, 본문은 링크 토폴로지·FFN 비중·오프로딩 규격을 추가하는 정량 보완 성격이다.
- DeepSpeed/추론 가속 범주의 다른 문헌이 제시한 추상 수치와 다소 수치 형식이 다를 수 있으나, 본 소스는 `문맥 길이 의존성`, `소형/대형 모델 사이징`, `랙 간 대역폭 희소성`을 구분해 설명하므로 상호 보완 관계로 해석된다.
