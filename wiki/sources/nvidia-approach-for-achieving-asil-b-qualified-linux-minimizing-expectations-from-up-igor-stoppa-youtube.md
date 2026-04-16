---
title: "📌 NVIDIA는 ASIL B 인증 Linux를 달성하기 위해 어떤 접근 방식을 사용했는가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/NVIDIA Approach for Achieving ASIL B Qualified Linux_ minimizing expectations from up... Igor Stoppa - YouTube.md
---

## Summary
전체 Linux 커널에 안전성 검증을 적용하지 않고, 핵심 메커니즘만 안전성 검증 대상으로 삼아 코드베이스의 유연성과 혁신 속도를 유지하는 접근 방식을 사용합니다. - 스레드에 특정 기능(capability)을 부여하여 메모리 할당 등을 통제 - 메모리 풀을 통해 자원을 안전성 수준별로 분할 및 검증 - MMU를 활용하여 낮은 안전성 스레드의 안전한 메모리 접근 차단

## Key Claims
- 스레드에 특정 기능(capability)을 부여하여 메모리 할당 등을 통제
- 메모리 풀을 통해 자원을 안전성 수준별로 분할 및 검증
- MMU를 활용하여 낮은 안전성 스레드의 안전한 메모리 접근 차단
- ASIL B (A Bravo)는 자동차 산업에서 사용되는 여러 안전성 단계 중 하나이며, 가장 어려운 수준은 아니지만 시작점으로 간주된다.

## Key Quotes
> "전체 Linux 커널에 안전성 검증을 적용하지 않고, 핵심 메커니즘만 안전성 검증 대상으로 삼아 코드베이스의 유연성과 혁신 속도를 유지하는 접근 방식을 사용합니다." — extracted from the source narrative.

## Connections
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[NVIDIA]] — directly referenced in or strongly associated with this source.
- [[IgorStoppa]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[ASILBQualifiedLinux]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
