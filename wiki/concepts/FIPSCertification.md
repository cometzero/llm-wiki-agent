---
title: "FIPS Certification"
type: concept
tags: [security, cryptography, compliance, linux]
sources: [lwn-weekly-edition-2026-06-04-1074950]
last_updated: 2026-06-12
---

## Summary
[[FIPSCertification]]은 암호 모듈이 FIPS 140 계열 요구사항을 만족하는지 검증하는 제도이다. LWN 2026-06-04호의 Linux 커널 기사에서는 인증 범위를 명확히 하기 위해 암호 구현을 loadable module 경계로 분리하려는 접근을 다룬다.

## Connections
- [[LinuxKernel]] — 커널 암호 API와 배포판 compliance 요구가 만나는 지점.
- [[SupplyChainSecurity]] — 규정 준수와 업데이트 경로가 신뢰 가능한 소프트웨어 공급망에 포함된다.
