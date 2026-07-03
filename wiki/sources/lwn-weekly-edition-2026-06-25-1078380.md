---
title: "LWN.net Weekly Edition for June 25, 2026"
type: source
tags: [lwn, linux, kernel, python, security, bpf]
date: 2026-06-25
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-06-25-1078380.md
source_hash: 47fca4fd417b3330669063f206bfc7bb693fd172c742cdf39a2fc9d87c39ba97
---

## Summary
이번 LWN Weekly Edition은 [[FreeThreadedPython]], [[AURSupplyChainAttack]], [[Fedora2FA]], [[LinuxKernel72]], [[BPF]], [[BPFArena]], [[BPFCoroutines]], [[BPFKASAN]], [[RMRBRMR]], [[OSPM2026]]를 한 호에 묶어 언어 런타임, 공급망 보안, 배포판 거버넌스, 커널 개발 흐름을 종합한다. 공개 bigpage 전체를 한국어로 번역한 raw 문서를 출처로 삼았으며, 보안 업데이트 표와 패치 목록은 추적성을 위해 원문 식별자를 보존했다.

## Key Claims
- [[FreeThreadedPython]]은 Python의 GIL 제거가 실험 단계를 넘어 생태계 포팅과 stable ABI 논의로 이동했음을 보여 준다.
- [[AURSupplyChainAttack]]은 고아 패키지와 사용자 관리 저장소가 대규모 공급망 공격 표면이 될 수 있음을 드러낸다.
- [[Fedora2FA]] 논의는 provenpackager 권한과 계정 탈취 리스크를 연결하며, 배포판 유지관리 권한에 2FA를 강제하는 방향으로 기운다.
- [[LinuxKernel72]] merge window 초반은 아키텍처 정리, Rust 지원, 파일시스템·네트워킹 변경, [[BPF]] 확장을 포함한다.
- [[BPFArena]], [[BPFCoroutines]], [[BPFKASAN]]는 BPF가 단순 필터 언어를 넘어 커널 내부 프로그래밍 모델·메모리 안전성·검증 체계와 결합하고 있음을 보여 준다.
- [[RMRBRMR]]는 RDMA 기반 block replication의 single-hop 설계를 통해 cloud block device durability와 overhead trade-off를 다룬다.
- [[OSPM2026]] 리포트는 CPU idle, EEVDF latency, sched_ext, Arm64 scheduling domains 등 power management와 scheduler 실무 쟁점을 정리한다.

## Key Quotes
> "free threading"은 GIL이 제거되었다는 뜻의 Python 용어라는 설명 — [[FreeThreadedPython]] 기사 맥락

> AUR 공격은 공식 저장소가 아니라 사용자 관리 콘텐츠를 겨냥했다는 설명 — [[AURSupplyChainAttack]] 맥락

## Connections
- [[Python]] — free-threaded interpreter와 GIL 제거 생태계
- [[Fedora]] — 2FA 정책과 공급망 방어
- [[BPF]] — arenas, coroutine, KASAN, 7.2 merge window 기능 확장
- [[LinuxKernel]] — 7.2 merge window, stable releases, patch stream
- [[SchedExt]] — OSPM 2026 scheduler 논의와 scx_lavd 개선

## Contradictions
- 기존 wiki 내용과 직접 충돌하는 주장 없음. 다만 Codex 인증 만료와 NVIDIA JSON 파싱 실패로 source page는 수동 materialization했다.
