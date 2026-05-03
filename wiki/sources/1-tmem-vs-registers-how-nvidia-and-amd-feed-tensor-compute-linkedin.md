---
title: "TMEM vs Registers: How NVIDIA and AMD Feed Tensor Compute | LinkedIn"
type: source
tags:
  - AI Hardware
  - GPU
  - TensorCores
  - NVIDIA
  - AMD
  - TMEM
  - MFMA
  - Registers
  - AsyncExecution
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/1-tmem-vs-registers-how-nvidia-and-amd-feed-tensor-compute-linkedin.md
last_updated: 2026-05-03
---

## Summary
이 문서는 현대 AI에서 텐서 연산의 핵심 병목이 단일 연산 유닛 자체보다 데이터 공급 경로임을 전제로, [[NVIDIA]]와 [[AMD]]가 이를 어떻게 다르게 풀었는지를 정리한다. 

[[NVIDIA]]는 [[Blackwell]]에서 [[TMEM]]를 도입해 텐서 오퍼랜드를 레지스터에서 분리함으로써 레지스터 압박을 완화하고 비동기 파이프라인을 강화했다. 반대로 [[AMD]]는 [[AMD]] 특유의 큰 레지스터 기반 구조를 통해 [[VGPR]]/[[AGPR]] 확장을 중심으로 유연성을 확보했지만, 커널 최적화의 복잡도를 높였다.

결론적으로 두 접근은 이론적으로는 유사한 성능 상한을 노릴 수 있으나, 스케줄링·메모리 레이아웃·소프트웨어 최적화 전략은 상호 이식성이 낮고 서로 다른 하드웨어 철학을 따른다.

## Key Claims
- 텐서 코어 활용의 진짜 제약은 [[TensorCore]] 연산을 수행하는 유닛이 아니라 지속적인 데이터 공급이다.
- [[NVIDIA]]는 [[Volta]], [[Ampere]], [[Hopper]], [[Blackwell]]로 진화하면서 데이터 이동과 연산을 분리했고, 특히 Blackwell에서 [[TMEM]]을 전용 텐서 스크래치패드로 채택했다.
- Blackwell의 [[SM]]당 [[TMEM]]은 약 256KB 규모이며, 텐서 오퍼랜드를 레지스터 없이 TMEM으로 옮겨 [[TensorCore]] 파이프라인에서 레지스터 리소스를 계산용 코드에 재할당한다.
- [[NVIDIA]]의 비동기 패턴은 워프그룹이 데이터 로딩 후 즉시 다른 명령을 발행할 수 있는 방식이며, pipeline이 비워지는 시점에 명시적으로 커밋된다.
- [[AMD]]는 텐서 전용 전용 스크래치패드를 별도로 두지 않고, [[VGPR]]/[[AGPR]]의 대규모 레지스터 파일(예: [[CDNA3]]/[[CDNA4]]의 SIMD당 VGPR 256 + AGPR 256)을 통해 텐서 피연산자와 누산 중간값을 흡수한다.
- [[AMD]]의 설계는 유연한 파티셔닝이 가능하지만, [[MFMA]] 형태별로 레지스터 레이아웃이 달라지는 구조적 제약으로 인해 웨이브 특수화 같은 최적화가 [[NVIDIA]]에서와 같은 양상의 효과를 내기 어렵다.
- [[NVIDIA]]의 [[TMA]]-기반 비동기 생산자-소비자 파이프라인은 [[mbarrier]] 동기화와 잘 결합되어 높은 점유율을 유지하지만, [[AMD]]는 이러한 경로가 없어 생산자 웨이브가 컴퓨팅 자원과 레지스터를 더 많이 점유한다.
- 아키텍처별 데이터 레이아웃은 최적화 전략의 이식성을 크게 제한한다. 즉 [[NVIDIA]]에서 효과적이던 패턴이 [[AMD]]에서 동일하게 작동하지 않는 경우가 많다.

## Key Quotes
> "TMEM is a dedicated per-SM scratchpad for tensor operands, fully separated from register files."
- [[NVIDIA]]는 텐서 연산 데이터를 레지스터와 분리해 데이터 공급을 비동기화하기 위한 공간을 확보했다는 점을 강조한다.

> "Both paths are theoretically near-peak capable, but software complexity differs drastically."
- 두 제조사 모두 성능 상한의 근접 접근이 가능하지만, 구현 복잡성은 구조 선택에 따라 크게 갈린다.

## Connections
- [[NVIDIA]] — 텐서 코어 데이터 공급을 [[TMEM]]와 [[WGMMA]] 중심의 비동기 모델로 정리한 사례.
- [[AMD]] — [[VGPR]]/[[AGPR]] 기반 대규모 레지스터 모델을 통해 유연성 확보와 스케줄링 난이도 상승의 트레이드오프를 보여줌.
- [[TensorCores]] — 두 플랫폼 모두 텐서 계산 성능의 핵심이지만, 하드웨어-소프트웨어 협업 방식이 다름.
- [[TMEM]] — [[NVIDIA]]의 전용 텐서 스크래치패드 설계와 파이프라인 분리의 중심 개념.
- [[MFMA]] — [[AMD]]의 기본 매트릭스 FMA primitive로, 형태별 레지스터 레이아웃 복잡성의 원인.
- [[VGPR]] & [[AGPR]] — [[AMD]]의 이중 레지스터 구조로 대규모 저장공간을 제공하지만 소프트웨어 복잡성 증가를 유발.
- [[Warp]] / [[WarpGroup]] — [[NVIDIA]]에서 128개 스레드 워프그룹 중심의 협업 모델이 텐서 실행 단위를 규정.
- [[TMA]] — 비동기 메모리 이동이 가능한 NVIDIA 최적화 계열에서 핵심 연결점.
- [[mbarrier]] — 생산자-소비자 오버랩 구조를 지원하는 하드웨어 동기화 개념.

## Contradictions
- 기존 위키의 [[NVIDIA]] 관련 추론 인프라 자료들에서 제시된 텐서 처리 성능 강조와 충돌하지 않는다. 본 소스는 성능의 동반요소인 데이터공급 계층을 구체적으로 보완한다.
- 기존 위키 내 [[AMD]] AI 가속 관련 내용과도 상충하지 않으며, 본문이 제시한 "유연성 대비 소프트웨어 복잡도" 트레이드오프는 기존 문맥을 정제한다.
