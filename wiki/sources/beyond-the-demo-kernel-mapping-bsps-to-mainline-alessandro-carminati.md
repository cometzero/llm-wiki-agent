---
title: "📌 BSP를 메인라인 커널에 매핑하는 과정에서 가장 중요한 도전 과제는 무엇인가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/Beyond the Demo Kernel_ Mapping BSPs to Mainline - Alessandro Carminati.md
---

## Summary
BSP의 진정한 하드웨어 지원 부분과 노이즈를 분리하여 어떤 부분이 메인라인에 통합될 수 있는지 파악하고, 이를 유지 관리 가능한 형태로 업스트림하는 것이 핵심 과제입니다. - 하드웨어 동작과 무관한 백포트, 리팩터링, 그리고 오래된 실험 코드 - 메인라인 커널과 분리되어 시간이 지나면서 발생하는 기능적/구조적 차이

## Key Claims
- 하드웨어 동작과 무관한 백포트, 리팩터링, 그리고 오래된 실험 코드
- 메인라인 커널과 분리되어 시간이 지나면서 발생하는 기능적/구조적 차이
- BSP의 본질: BSP는 다른 사람이 쓴 소설과 같아서, 핵심 줄거리(하드웨어 지원)가 있지만 어디서 시작하는지(어떤 부분이 중요한지) 알기 어렵다.
- BSP는 실리콘이 작동함을 증명하기 위해 하드웨어 초기 가동(bring-up) 시점에 찍은 스냅샷이다.

## Key Quotes
> "BSP의 진정한 하드웨어 지원 부분과 노이즈를 분리하여 어떤 부분이 메인라인에 통합될 수 있는지 파악하고, 이를 유지 관리 가능한 형태로 업스트림하는 것이 핵심 과제입니다." — extracted from the source narrative.

## Connections
- [[AlessandroCarminati]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Google]] — directly referenced in or strongly associated with this source.
- [[Qualcomm]] — directly referenced in or strongly associated with this source.
- [[MainlineUpstreaming]] — one of the main technical themes discussed by this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
