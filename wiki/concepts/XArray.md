---
title: "XArray"
type: concept
tags: [linux, rust, data-structures]
sources: [lwn-weekly-edition-2026-10-22-1100612]
last_updated: 2026-10-30
---

## Overview

XArray는 Linux kernel에서 integer index로 항목을 관리하는 자료구조다. 2026-10-22 LWN의 Rust 재작성 논의는 단순 언어 교체가 아니라 기존 C 사용자·성능·순회 API·동시성 계약을 보존하는 문제를 다룬다.

## Engineering implications

- 안전한 wrapper가 있어도 내부 unsafe 부분과 C 경계는 별도 검토가 필요하다.
- 재작성의 평가는 memory safety와 실제 workload 성능·API 호환성을 함께 봐야 한다.
- 기사 당시 구현은 미완성이므로 기존 사용자가 즉시 전환해도 된다는 권고로 해석하지 않는다.

## Connections

- [[LinuxKernel]] — 기존 subsystem 사용자와 concurrency contract.
- [[Rust]] — type/ownership을 이용한 API 설계와 unsafe boundary.
- [[lwn-weekly-edition-2026-10-22-1100612]] — 재작성 토론과 초기 구현의 상태.
