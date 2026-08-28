---
title: "AF_ALG"
type: concept
tags: [linux, kernel, cryptography, distribution-security]
sources: [lwn-weekly-edition-2026-08-20-1088565]
last_updated: 2026-08-28
---

## Summary

[[AFALG|AF_ALG]]는 Linux kernel crypto API를 socket interface로 user space에 노출하는 address family다. 이를 범용 배포판에서 제한하려는 논의는 kernel 기능을 쓸 수 있게 하는 편의와 cryptographic primitive 노출·오용·공격 표면을 줄이는 보안 운영 사이의 trade-off를 보여 준다.

## Connections

- [[lwn-weekly-edition-2026-08-20-1088565]] — Fedora의 AF_ALG phase-out·호환성 논의를 정리한다.
