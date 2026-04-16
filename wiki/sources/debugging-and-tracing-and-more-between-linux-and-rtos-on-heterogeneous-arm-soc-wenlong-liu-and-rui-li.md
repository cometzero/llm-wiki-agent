---
title: "📌 이기종 ARM SoC 환경에서 Linux와 RTOS 간의 디버깅 및 트레이싱 방법은?"
type: source
tags: [oss2025-japan, safety]
date: 2026-04-16
source_file: raw/OSS2025_Japan/Debugging & Tracing and More Between Linux and RTOS on Heterogeneous ARM SoC - Wenlong Liu & Rui Li.md
---

## Summary
--- tags: - Debug - Trace - Heterogeneous - ARM - SoC - Remoteproc - Linux - RTOS --- 이기종 SOC의 공유 메모리 등 고유한 특성을 활용하여 Linux 원격 프로세스 서브시스템(remote proc)이나 Huawei Open Embedded MSC 같은 기존 솔루션을 개선하고 활용하는 것이 핵심입니다.

## Key Claims
- 본 발표는 이종(Heterogeneous) ARM SOC 환경에서 Linux와 RTOS(실시간 운영체제) 간의 디버깅 및 트레이싱에 대한 실무적인 접근 방식을 공유하는 것을 목적으로 한다.
- 특히 RTOS와 Linux 운영체제 사이에서 시도된 흥미로운 엔지니어링 접근 방식에 초점을 맞추며, 주요 내용은 디버깅 및 트레이싱 방법론이다.
- 발표자는 Amo(Continental Automotive의 독립 법인)에 근무하며, 이전에는 FISA에서 6년간 근무했다.
- 주요 업무 영역은 HPC(고성능 컴퓨팅), 특히 바디 HPC, 콕핏 시스템, 섀시 제품을 포함하는 자동차 제품 개발 분야였다.

## Key Quotes
> "이기종 SOC의 공유 메모리 등 고유한 특성을 활용하여 Linux 원격 프로세스 서브시스템(remote proc)이나 Huawei Open Embedded MSC 같은 기존 솔루션을 개선하고 활용하는 것이 핵심입니다." — extracted from the source narrative.

## Connections
- [[WenlongLiu]] — directly referenced in or strongly associated with this source.
- [[RuiLi]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Android]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[HypervisorVirtualization]] — one of the main technical themes discussed by this source.
- [[MainlineUpstreaming]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
