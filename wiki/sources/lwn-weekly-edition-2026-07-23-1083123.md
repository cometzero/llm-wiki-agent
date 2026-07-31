---
title: "LWN.net Weekly Edition for July 23, 2026"
type: source
tags: [lwn, linux, open-source, kernel, security, weekly]
date: 2026-07-23
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-07-23-1083123.md
source_hash: f8c4d8fc1b1b7854
last_updated: 2026-07-31
---

## Summary
LWN.net Weekly Edition 2026-07-23 한국어 번역은 [[LLMAssistedKernelDevelopment]]의 커널 커뮤니티 논쟁, [[GNOMESessionRestore]], [[FedoraChangeProcess]], [[BPFTracepoints]], [[BPFLsmSecurity]], [[Famfs]], [[SchedExt]] 진화를 함께 기록한다. 보안/공급망 영역에서는 [[PyPISupplyChainSecurity]], [[XZBackdoor]], GNOME 보안 추적, 배포판 보안 업데이트를 통해 open-source ecosystem governance와 운영 리스크를 정리한다.

## Key Claims
- Kernel LLM 논쟁은 "AI 사용 여부"보다 Assisted-by provenance, reviewer trust, proprietary tool 의존, contributor accountability 같은 프로세스 문제로 확장된다.
- GNOME save/restore는 X11 시절 세션 복원 경험을 Wayland/GNOME 환경에 다시 제공하려는 시도이며 compositor, toolkit, application protocol 협력이 필요하다.
- Fedora change process 논의는 배포판 기술 변경이 QA, maintainer 부담, 사용자 migration, governance rule과 동시에 연결됨을 보여 준다.
- BPF 쪽에서는 여러 tracepoint에 프로그램을 붙이는 효율화와 BPF LSM tampering 방어가 observability와 runtime security boundary를 강화하는 방향으로 이어진다.
- [[Famfs]] 병합 논의와 [[SchedExt]] sub-scheduler/proxy-execution 지원은 새로운 메모리 fabric 및 programmable scheduling 실험을 mainline Linux와 맞추려는 흐름이다.
- [[PyPISupplyChainSecurity]]와 [[XZBackdoor]] 관련 항목은 패키지 저장소 정책, release artifact 불변성, maintainer 신뢰 모델의 중요성을 다시 강조한다.

## Key Quotes
> "Debating the role of large language models in the kernel community" — kernel community의 LLM 사용 정책·문화 논쟁을 다룬 핵심 기사 제목.

> "Save and restore may be coming to GNOME" — GNOME/Wayland 환경에서 데스크톱 세션 복원 기능이 다시 논의되고 있음을 보여 주는 기사 제목.

> "Attaching programs to multiple tracepoints" 및 "Securing BPF LSMs against tampering" — BPF가 관측성과 보안 집행의 양쪽에서 확장되고 있음을 보여 주는 LSFMM+BPF Summit 보도 축.

## Connections
- [[LLMAssistedKernelDevelopment]] — 2026-07-09 LWN의 LLM-assisted MM patch 논의에서 이번 호의 community/process 논쟁으로 이어진다.
- [[BPF]] — tracepoint attachment, BPF LSM tamper 방어, sched_ext와 함께 programmable kernel extension 축을 넓힌다.
- [[BPFTracepoints]] — 여러 tracepoint에 program을 효율적으로 붙이는 observability 개선 흐름.
- [[BPFLsmSecurity]] — BPF 기반 보안 정책이 변조되지 않도록 attachment/protection boundary를 다루는 흐름.
- [[Famfs]] — fabric-attached memory를 파일시스템 형태로 노출하려는 병합 논의.
- [[SchedExt]] — eBPF 기반 scheduler 실험이 sub-scheduler와 proxy execution으로 확장된다.
- [[SupplyChainSecurity]] — PyPI 업로드 정책과 XZ backdoor 서사가 recurring open-source supply-chain thread를 보강한다.

## Contradictions
- 없음. 이번 호는 기존 LWN 추적 페이지의 Linux/open-source 운영·보안 흐름을 확장한다.
