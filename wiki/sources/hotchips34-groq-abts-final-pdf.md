---
title: "HotChips34 - Groq - Abts - final"
type: source
tags:
  - Groq
  - StreamingTensorProcessor
  - TSP
  - SoftwareDefinedHardware
  - DeterministicExecution
  - ISA
  - AIInfrastructure
  - ChipletTopology
  - Dragonfly
  - SoftwareControlledMemory
  - ChipToChip
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/hotchips34-groq-abts-final.pdf.md
sources:
  - hotchips34-groq-abts-final-pdf
last_updated: 2026-05-03
---

## Summary
이 자료는 [[Groq]]의 [[StreamingTensorProcessor|Streaming Tensor Processor (TSP)]] 아키텍처를 중심으로, AI 추론에서 예측 가능한 성능을 달성하기 위한 [[SoftwareDefinedHardware|소프트웨어 정의 하드웨어]]·[[DeterministicExecution|결정론적 실행]] 설계를 상세히 설명한다. 핵심은 하드웨어를 단순히 빠르게 만드는 것이 아니라, 컴파일러와 런타임이 완전히 제어 가능한 데이터·명령어 흐름을 만들고, 멀티칩 스케일에서도 성능 변동을 줄이는 것이다.

특히 TSP는 [[GroqChip]]을 기능 단위로 분리하고, 명령어 파이프라인을 소프트웨어가 정적·동적으로 제어하는 방식을 택한다. 저수준 메모리 계층화를 노출하고(캐시 비의존), [[VLIW]] 계열의 ISA 제어 패턴을 통해 각 단일 기능 유닛이 독립적으로 동작하면서도 동기화된 스케줄을 유지한다. 결과적으로 지연 시간의 분산을 줄이고 배치-1 추론·인터랙티브 워크로드에서 성능 예측성을 확보하는 설계를 제시한다.

시스템 계층에서는 [[SoftwareDefinedNetworking]], [[RealScale]], [[DragonflyTopology|그룹 기반 Dragonfly 토폴로지]]와 결합된 고밀도 네트워크를 통해 확장성과 동기화를 확보하며, [[Reliability|신뢰성(복구/중복성)]] 및 예외 처리까지 결정론 철학에 맞게 정리한다.

## Key Claims
- [[Groq]]의 [[StreamingTensorProcessor|TSP]]는 소프트웨어 정의 제어와 [[DeterministicExecution|결정론적 실행]]을 결합해 딥러닝 추론의 예측 불가능한 성능을 줄이려 한다.
- 하드웨어-소프트웨어 인터페이스는 정적 컴파일 시점과 동적 실행 시점을 분리하며, [[MLIR]] 기반 파이프라인이 아키텍처 상태를 컴파일러에 노출한다.
- TSP는 멀티코어 메시를 기능 단위로 분할해 [[ICU]], [[MEM]], [[VXM]], [[MXM]], [[SXM]]가 분리된 [[SoftwareDefinedHardware|소프트웨어 제어형]] 아키텍처를 구성한다.
- 메모리 계층은 캐시 기반 구조를 회피하고 물리적 뱅크를 소프트웨어에 직접 노출하여, 캐시 재정렬이나 비결정성 동작을 줄이는 방식으로 동작한다.
- [[GroqChip]]은 동시 다중 연산 처리에 최적화되어 80TB/s 수준의 SRAM 대역폭, 대규모 [[VXM]] 벡터 유닛(총 5,120개 ALU), 대형 [[MEM]] 슬라이스를 특징으로 한다.
- ISA는 [[IFETCH]], [[READ]], [[STORE]], [[REPEAT]], [[SYNC]], [[NOTIFY]], [[SEND]], [[RECEIVE]], [[DESKEW]] 등과 같은 소프트웨어 제어 명령어를 통해 결정론적 타이밍을 유도한다.
- [[C2C|Chip-to-Chip]] 통신은 기존 RDMA 대비 단순화된 모델을 채택해 분산 TSP 동작에서 상태 일관성과 결정론 유지 문제를 완화한다.
- [[SoftwareDefinedNetworking|소프트웨어 스케줄링 네트워크]]는 적응형 라우팅·딥 입력큐 구조를 배제하고 텐서 기반 라우팅과 고정 트래픽 패턴 기반 스케줄링을 사용한다.
- [[PacketlessRouting|패킷이 아닌 텐서 라우팅]]과 320바이트 텐서 포맷, 낮은 헤더 오버헤드(약 2.5%)가 작은 메시지 성능에 유리하다.
- 신뢰성은 전기적 오류(SEU/SDC) 대응, SECDED 보호, 중복 슈퍼레인, 하드웨어 예외/소프트웨어 예외 처리 흐름을 통해 단순화된다.
- 워크로드 성능은 Cholesky, [[BERT]], [[GEMM]], [[AllReduce]]에서 일관된 성능 향상 또는 특이적 우위를 보이며, 특히 일관된 지연 특성이 서비스 품질 개선에 중요하다고 본다.
- 최종적으로 [[Groq]]는 추론 인프라를 "고처리량+고예측성" 축으로 설계해 소프트웨어 제어 범위를 넓히는 방향성을 제시한다.

## Key Quotes
> "컴파일러가 모든 데이터 위치를 파악하고, 명령어 실행을 정확히 조율한다" — 소프트웨어 가시 상태 노출의 핵심 원리.

> "캐시를 두지 않고 아키텍처 노출을 플랫하게 하여, 데이터 위치를 소프트웨어가 직접 관리한다" — 결정론적 메모리 모델.

> "멀티칩 네트워크에서도 결정론은 소프트웨어 스케줄링과 정렬 카운터(HAC/SAC)로 유지한다" — 분산 실행의 핵심 제약 대응.

## Connections
- [[Groq]] — 본 문서의 주요 주체로, [[StreamingTensorProcessor]]의 상위 아키텍처 공급사.
- [[StreamingTensorProcessor]] — 이 소스의 중심 개념. [[ICU]], [[MXM]], [[VXM]], [[SXM]]으로 분할된 TSP 마이크로아키텍처를 설명.
- [[GroqChip]] — 블록 단위 연산 유닛, SRAM 대역폭, 메모리·네트워크 동작을 담는 핵심 하드웨어 제품군.
- [[SoftwareDefinedHardware]] — 정적 컴파일 타깃, 런타임 제어, 메모리 가시성 노출의 공통 설계 철학.
- [[DeterministicExecution]] — 텐서 흐름, ISA 스케줄, 라우팅, 동기화 전략의 일관성 보장 원리.
- [[CompilerBasedInstructionScheduling]] (개념) — 사이클 단위 정적 스케줄링과 성능 예측 가능성의 기제.
- [[SoftwareDefinedNetworking]] — 하드웨어 중재를 배제한 텐서 중심 스케줄링 네트워크.
- [[PacketlessRouting]] — 320바이트 텐서 단위 라우팅과 저오버헤드 경로 구성.
- [[C2C]] — [[RealScale]] 기반 칩-투-칩 통신과 분산 연산 동기화의 기반.
- [[DragonflyTopology]] — 대규모 확장성 토폴로지와 비최소 경로 라우팅의 성능-신뢰성 균형.
- [[Reliability]] — SECDED, SDC/SEU 대응, 예비 슈퍼레인, 런타임 재시도 전략 포함.
- [[BERT]], [[GEMM]], [[Cholesky]], [[AllReduce]] — 워크로드 성능 평가 기준 및 결정론적 품질 검증 지점.

## Contradictions
- 기존 위키의 Groq 관련 프레임(예: 지연 중심의 고성능 추론 강점)과 충돌하지 않는다. 본 소스는 동시성·워크로드 타입별 한계를 포함해 더 정밀한 조건부 해석을 제공한다.
- 기존 [[AIInfrastructure]]·[[TCO]] 논의와 상충하지 않으며, 오히려 "지연 예측성"을 추가 성능 축으로 보강한다.
