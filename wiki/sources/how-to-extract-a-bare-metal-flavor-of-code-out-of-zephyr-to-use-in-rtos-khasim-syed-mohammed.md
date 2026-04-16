---
title: "📌 Zephyr에서 베어 메탈 코드 추출 방식을 바꾸는 방법의 핵심은 무엇인가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/How to extract a bare metal flavor of code out of Zephyr to use in RTOS_ - Khasim Syed Mohammed.md
---

## Summary
기존의 Artos 방식을 따르기보다 Zephyr 네이티브 드라이버를 우선 개발하여 Zephyr의 오픈소스 커뮤니티, CI/CD, 툴링(west, twister) 등의 이점을 활용하고, 이를 다른 RTOS로 이식할 수 있는 경로를 모색하는 것이 핵심입니다. - 빌드 스크립트를 통해 DT를 include 파일로 변환 - Zephyr에 종속적인 하이레벨 드라이버와 저수준 드라이버를 명확히 분리 - 슬립 함수, 클럭/전원 관리, ISR 컨텍스트 등을 OS 독립적으로 작성하여 이식성을 높여야 합니다.

## Key Claims
- 빌드 스크립트를 통해 DT를 include 파일로 변환
- Zephyr에 종속적인 하이레벨 드라이버와 저수준 드라이버를 명확히 분리
- 슬립 함수, 클럭/전원 관리, ISR 컨텍스트 등을 OS 독립적으로 작성하여 이식성을 높여야 합니다.
- 연사는 안드로이드 부팅 시간 최적화 세션 이후 RTOS(실시간 운영체제)의 세계로 청중을 초대하며, MCU(마이크로컨트롤러 유닛)를 다루는 임베디드 환경에 대해 언급한다.

## Key Quotes
> "기존의 Artos 방식을 따르기보다 Zephyr 네이티브 드라이버를 우선 개발하여 Zephyr의 오픈소스 커뮤니티, CI/CD, 툴링(west, twister) 등의 이점을 활용하고, 이를 다른 RTOS로 이식할 수 있는 경로를 모색하는 것이 핵심입니다." — extracted from the source narrative.

## Connections
- [[KhasimSyedMohammed]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Zephyr]] — directly referenced in or strongly associated with this source.
- [[Meta]] — directly referenced in or strongly associated with this source.
- [[SPDXSBOM]] — one of the main technical themes discussed by this source.
- [[BareMetalExtraction]] — one of the main technical themes discussed by this source.
- [[PowerManagementUSB]] — one of the main technical themes discussed by this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
