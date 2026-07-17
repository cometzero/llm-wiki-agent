---
title: "Eric Biggers"
type: entity
tags: [kernel, cryptography, maintainer]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Profile
커널 트리의 [[CryptoApi]] 및 CRC 라이브러리 코드 관리자. [[Fscrypt]], [[FsVerity]], [[KernelCryptography]] 라이브러리 개발 주도.

## Key Contributions
- 2002년부터 존재하던 전통적 암호화 API의 문제점 파악
- 커널 6.17에서 `hmac_sha256_usingrawkey()` 및 `chacha20poly1305_encrypt()` 라이브러리 함수 추가
- [[MLDSA]] (FIPS 204) 및 [[SHAKE128]]/[[SHAKE256]] XOF 지원 추가
- SHA-256 인터리브 해싱으로 [[DmVerity]] 가속화
- [[Iomap]]과 유사한 "라이브러리" 패턴으로 커널 암호화 단순화 권장

## AF_ALG Deprecation
사용자 공간 암호화 API인 [[AF_ALG]]의 지속적인 보안 취약점 문제를 지적하고 점진적 사용 중단 권장.

## Connections
- [[LinuxSecuritySummit]] — LSS NA 2026에서 커널 암호화 현대화 발표
- [[ArdBiesheuvel]] — 공동 암호화 관리자
- [[JasonDonenfeld]] — 공동 암호화 관리자 (WireGuard)
- [[KUnit]] — 암호화 라이브러리 테스트 도입
- [[KernelCI]] — CI/CD 통합
