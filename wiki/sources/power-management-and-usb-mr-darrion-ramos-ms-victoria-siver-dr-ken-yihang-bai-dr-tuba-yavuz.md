---
title: "📌 \"Power Management and USB\"에 대한 발표는 어떤 내용을 다루는가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/Power Management and USB... Mr DARRION RAMOS, Ms VICTORIA SIVER, Dr Ken Yihang Bai, Dr Tuba Yavuz.md
---

## Summary
전력 관리 퍼징(Power Management Fuzzing)에 대한 모듈식 접근 방식을 소개하고, 특히 저전력 상태 및 USB 상호작용에서 발생하는 버그를 탐색하는 방법을 다룹니다. 저전력 상태(예: 절전 모드)에서는 대부분의 로깅 메커니즘이 꺼지기 때문에, 크래시 발생 시 어떤 문제가 발생했는지 파악하기 매우 어렵고, 시스템 간 상호 의존성이나 경쟁 조건으로 인한 문제가 특히 이해하기 어렵습니다.

## Key Claims
- 로그 기록 손실: 시스템이 저전력 상태(suspend)로 진입하면 모든 로깅 메커니즘이 꺼지기 때문에, 이 상태에서 발생하는 충돌(crash) 상황을 이해하기가 매우 어렵다 .
- 블랙박스 문제: 문제가 발생했을 때 저전력 상태는 일종의 블랙박스와 같으며, 시스템 상호 의존성(system interdependencies)과 레이스 컨디션(race conditions)으로 인해 문제를 파악하기가 특히 어렵다 .
- 기존 방법의 한계: 드라이버 대상 추적(tracing) 및 실패 분석 도구는 존재하지만, 오류 기반 탐색(fault-based exploration)이 부족하다 .
- PM 버그 공간 탐색: 전원 관리 버그 영역을 탐색하여 오류에 대한 이해를 제공하는 퍼저(fuzzer)를 생성한다 .

## Key Quotes
> "4. 장점: VM은 안전하고 일관된 시작 지점(consistent start)을 제공한다 ." — extracted from the source narrative.

## Connections
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Intel]] — directly referenced in or strongly associated with this source.
- [[RedHat]] — directly referenced in or strongly associated with this source.
- [[QEMU]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[PowerManagementUSB]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
