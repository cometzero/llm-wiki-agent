---
title: "vmsplice() Removal"
type: concept
tags: [kernel, system-call, security]
sources: [lwn-weekly-edition-2026-06-11-1076254]
last_updated: 2026-06-19
---

## Overview
사용자 메모리와 파이프 사이의 zero-copy 데이터 이동을 제공하는 vmsplice() 시스템 호출의 복잡한 의미 체계를 제거하려는 논의.

## Problem
- 복잡한 pinning/lifetime 규칙으로 다수의 보안 취약점 발생
- 2008년 이래로 여러 차례 주목할 만한 익스플로잇 발생
- 유지보수 부담 가중

## Proposed Solution
Askar Safin의 패치: vmsplice()를 단순 복사 구현으로 대체 (preadv2/pwritev2로 매핑)

## Developer Reactions
- Matthew Wilcox: "우리가 이 일을 해야 한다는 것이 정말 슬프다"
- Andy Lutomirski: "vmsplice는 형편없는 API이므로 제거해야 한다" - 100% 찬성
- Linus Torvalds: 조심스럽게 찬성, splice() 유사 변경 제안
- Willy Tarreau: 62Gbps→31Gbps 성능 저하 우려

## Status
패치 시리즈가 7.2 개발 주기 병합 목표로 Christian Brauner에 의해 적용됨

## Connections
- [[LinuxKernel]] — 적용 분야
- [[AskarSafin]] — 패치 제안자
- [[LinusTorvalds]] — 커널 관리자
