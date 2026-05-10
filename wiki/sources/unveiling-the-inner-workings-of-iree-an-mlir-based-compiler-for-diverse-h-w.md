---
title: "Unveiling the Inner Workings of IREE: An MLIR-Based Compiler for Diverse H/W"
type: source
tags:
  - IREE
  - MLIR
  - LLVM
  - Compiler
  - AMD
  - NVIDIA
  - SharkTank
  - HAL
  - VMFB
  - Host-Device
  - AOT
  - Quantization
  - Dispatches
  - Linalg
  - Heterogeneous Inference
date: 2026-05-10
sources:
  - unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w
last_updated: 2026-05-10
source_file: raw/Technology/LilysAI/unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w.md
source_hash: 2ecf9619178d3dc2
---

## Summary
이 문서는 [[IREE]]의 핵심이 되는 MLIR 기반 컴파일러 설계를 설명한다. [[IREE]]는 텐서 모델을 CPU, GPU, NPU 등 다양한 하드웨어에 효율적으로 배포하기 위해 호스트-디바이스 분할을 적극 활용하고, [[MLIR]]의 다이얼렉트 기반 점진적 하향(Progressive Lowering)과 [[LLVM]] 백엔드 모델을 결합한다. 또한 [[Shark]] 스택 문맥에서 [[Shark Tank]], [[Shark Turbine]], [[IREE]], [[Shark Runtime]](Shortfin), [[Shark Studio]]가 어떻게 이어지는지를 보여준다.

특히 성능과 이식성 균형을 위해 IREE는 컴파일러 내에서 스케줄링·디스패치 생성·바이너리 생성을 정교화하고, [[HAL]](Hardware Abstraction Layer)를 통해 신규 아키텍처 진입 장벽을 낮춘다. 최종 산출물은 [[VMFB]]로서 런타임 배포가 간편하고, 디버깅 가능성이 높다.

핵심은 2가지이다. 첫째, IREE가 아키텍처 불가지론적 구조로 스택 확장성을 확보하고, 둘째, 오토튠/휴리스틱 성숙과 이종 시스템 스케줄링이 아직 초기 단계이더라도 실용적인 이식 경로를 제공한다는 점이다.

## Key Claims
- [[LLVM]]은 타깃-독립 컴파일 스택의 장점을 지닌 반면, 텐서 중심 고수준 추상을 직접 다루기에는 한계가 있어 [[MLIR]]의 다이얼렉트를 함께 사용한다.
- [[IREE]]의 중심 설계는 [[Host]]와 [[Device]] 분리를 기반으로 작업을 분해하고 디스패치 단위로 스케줄링하는 [[Host-Device Programming Model]] 적용이다.
- [[IREE]]는 프론트엔드에서 [[PyTorch]], [[TensorFlow]], [[TOSA]], [[ONNX]] 등 다양한 입력을 받아 [[MLIR]] 변환 후, 이식 가능한 단계적 변환 파이프라인을 통해 디바이스별 백엔드로 전달한다.
- 디스패치 그래프는 데이터 의존성을 기준으로 생성되며, 호스트는 이를 바탕으로 [[Runtime]]에서 명령 버퍼를 구성해 디바이스를 연속 실행시킨다.
- 하드웨어 확장은 [[HAL]] 구현을 통해 이루어지며, CPU, [[GPU]], [[SPV]], [[NPU]](예: Ryzen AI)까지 지원된다.
- IREE의 최종 산출물은 [[VMFB]](VM File)이며, 런타임이 이를 해석해 디바이스 실행으로 연결한다.
- 컴파일러의 장점은 정적 파이프라인(컴파일 타임 고정 최적화), 디버깅 가능성, 아키텍처 불가지론적 확장성, 컴파일러-투입 비용 대비 성능 향상이다.
- 하드웨어 이식의 핵심은 전용 플러그인 혹은 [[Transform Dialect]] 기반 커스터마이징으로, 디폴트 융합/스케줄만으로 해결되지 않는 워크로드는 확장점에서 보완 가능하다.
- 성능은 오브젝트별로 거의 항상 최고치가 아니며, 특히 아웃오브박스 사용성은 아직 과제이나, 점진적 튜닝으로 사용자가 최적 성능에 접근할 수 있다.
- 양자화/희소성은 컴파일러가 입력 모델을 존중하는 방향으로 동작하며, 기본적으로 모델이 양자화되어 있어야 한다.
- IREE 커뮤니티 운영은 오픈소스 공개 개발, [[GitHub]] 이슈, [[Discord]] 기반 지원과 함께 진행되며 초심자 진입 경로는 기존 디버깅 작업을 통해 확보된다.

## Key Quotes
> "디스패치를 받아 명령 버퍼를 생성해 호스트 개입 없이 디바이스가 지속적으로 바쁘게 동작하도록 하는 것이 텐서 성능 확보의 핵심이다." — source

> "새로운 디바이스를 연결하려면 IREE의 HAL을 구현하면 된다." — source

> "하이브리드 오픈소스 컴파일러를 통해 커스터마이징, 플러그인, Transform 다이얼렉트 재정의를 가능하게 하여 확장성을 확보한다." — source

## Connections
- [[IREE]] — 소스의 중심 엔진.
- [[MLIR]] — 변환 언어 계층과 다이얼렉트 확장 기반.
- [[LLVM]] — 최종 저수준 코드 생성의 강력한 기반.
- [[HAL]] — 신규 디바이스 타겟을 연결하는 핵심 계층.
- [[VM]] — 실행 단위로의 경량 가상머신 개념.
- [[VMFB]] — IREE의 최종 산출물 아티팩트.
- [[AOT]] — 컴파일 후 배포 방식의 전제.
- [[Linalg]] — 디바이스 타겟의 코드 생성에서 핵심 다이얼렉트.
- [[Transform Dialect]] — 컴파일 파이프라인 재정의 메커니즘.
- [[Shark]] — AIG Shark 스택 구성요소군(모델 추출~서빙).
- [[Shark Tank]] — 모델 그래프 추출 및 전처리 계층.
- [[Shark Runtime]] — 호스트 추론 런타임.
- [[Shark Studio]] — 모델 배포 워크플로우를 패키지화한 도구층.
- [[Nod.ai]] — AIG Shark의 기원/통합 경로의 출처 중 하나.
- [[AMD]] — AMD 디바이스 및 팀 운영 문맥.
- [[NPU]] — VLIW/AIE 류를 포함한 NPU 표적.
- [[Quantization]] — 모델 변환 전제 및 스택 호환 맥락.
- [[Sparsity]] — 아직 제한적 지원 상태.
- [[GitHub]] — 오픈 개발 채널.
- [[Discord]] — 커뮤니티 운영 채널.
- [[Dispatch]] — 작업 분할 및 스케줄링의 기본 단위.
- [[Host-Device Programming Model]] — 전체 스케줄링 철학.

## Contradictions
- 기존 문헌에서 제기되는 [[MLIR]]의 다이얼렉트 과잉 확장 우려와 대립적으로 보이지는 않으나, 이 소스는 IREE 맥락에서 "필요 기능에 대한 플러그인/Transform 확장"을 실무적 운영 수단으로 제시한다. 즉, 개념적 비용 증가 경고는 그대로 유지되나, 이를 완화할 수 있는 경로를 더 강하게 제시한다.
