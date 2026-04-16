---
title: "📌 KUnit 테스팅의 주요 문제점과 한계는 무엇인가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/KUnit Testing Insufficiencies - Matthew Whitehead (The Boeing Company).md
---

## Summary
KUnit은 커널 내에서 유닛 테스트를 수행하는 데 유용하지만, 의존성 관리의 어려움, 느린 빌드 및 실행 시간, 복잡한 테스트 작성 및 유지보수 부담 등 기존 유닛 테스팅 프레임워크에 비해 여러 가지 부족한 점과 한계가 있습니다. - 의존성 관리: 패치 도입 및 유지보수로 인한 복잡성 증가, 수동적인 기능 스터빙/모킹 필요. - 개발 주기: 커널 전체 빌드 및 부팅으로 인해 테스트 작성-실행-관찰 주기가 느림. - 확장성: 많은 수의 정교한 테스트 시 여러 커널 빌드 필요 및 테스트 충실도 문제 발생. - 실행 환경: 시스템 상태에 대한 높은 의존성, 에뮬레이션 또는 실제 하드웨어 필요.

## Key Claims
- 의존성 관리: 패치 도입 및 유지보수로 인한 복잡성 증가, 수동적인 기능 스터빙/모킹 필요.
- 개발 주기: 커널 전체 빌드 및 부팅으로 인해 테스트 작성-실행-관찰 주기가 느림.
- 확장성: 많은 수의 정교한 테스트 시 여러 커널 빌드 필요 및 테스트 충실도 문제 발생.
- 실행 환경: 시스템 상태에 대한 높은 의존성, 에뮬레이션 또는 실제 하드웨어 필요.

## Key Quotes
> "2. 이는 기능적 안전성 검증(functional safety verification)이나 형식 검증(formal verification)처럼, 의존성이 최소화된 작은 환경에서 사양을 테스트하려는 시나리오와 연관된다." — extracted from the source narrative.

## Connections
- [[MatthewWhitehead]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Google]] — directly referenced in or strongly associated with this source.
- [[QEMU]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[KUnit]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
