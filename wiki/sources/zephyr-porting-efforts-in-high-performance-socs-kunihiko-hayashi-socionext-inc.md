---
title: "📌 고성능 SoC에 Zephyr를 포팅하는 주요 동기와 과제는 무엇인가?"
type: source
tags: [oss2025-japan, safety]
date: 2026-04-16
source_file: raw/OSS2025_Japan/Zephyr Porting Efforts in High Performance SoCs - Kunihiko Hayashi, Socionext Inc..md
---

## Summary
미래 하이브리드 시스템(메인 OS + Zephyr) 구축을 위한 사전 준비가 주요 동기이며, 현재 마이크로컨트롤러 기반의 Zephyr 설계를 고성능 SoC 환경에 맞게 개선하는 것이 주요 과제입니다. - 메모리 관리 유닛(MMU) 지원 부족 및 불충분한 번역 테이블 요소 - SMP (Symmetric Multi-Processing) 관련 문제 - Linux와 충돌하는 인터럽트 번호 - 드라이버의 MMIO (Memory-mapped I/O) 지원 부족 및 디바이스 트리 구조의 비효율성

## Key Claims
- 메모리 관리 유닛(MMU) 지원 부족 및 불충분한 번역 테이블 요소
- SMP (Symmetric Multi-Processing) 관련 문제
- 드라이버의 MMIO (Memory-mapped I/O) 지원 부족 및 디바이스 트리 구조의 비효율성
- 발표자 소개 및 역할: 발표자는 Socionext의 임베디드 소프트웨어 엔지니어인 Kuni Kohayashi이며, 고객 SOC에 오픈소스 소프트웨어 포팅 및 배포를 담당한다.

## Key Quotes
> "3. 고성능 SoC에 Zephyr 포팅의 필요성: Zephyr는 경량성, 모듈성, 보안 지원 기능을 갖추고 있지만 주로 소형 마이크로컨트롤러(MCU)용으로 개발되었다. 그럼에도 고성능 SoC에 Zephyr를 포팅하는 이유는 미래 혼합 시스템(Mixed System) 구성을 목표로 하기 때문이다." — extracted from the source narrative.

## Connections
- [[KunihikoHayashi]] — directly referenced in or strongly associated with this source.
- [[SocionextInc]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Zephyr]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
