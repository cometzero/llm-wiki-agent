---
title: "Kernel Cryptography"
type: concept
tags: [kernel, cryptography, security]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Definition
Linux 커널의 암호화 기능 체계. 2002년 이후 전통적인 crypto API와 최근 추가된 라이브러리 함수로 구성.

## 기존 API 문제점
- 복잡하고 사용困难
- 하드웨어 가속 미지원
- 런타임 알고리즘 로드 실패 가능
- 성능 오버헤드 (SHA-256 계산의 62%가 간접비)

## 라이브러리 접근 방식
[[EricBiggers]]가推动하는 새로운 접근:
- 특정 알고리즘에 대한 직접 함수 제공
- 예: `hmac_sha256_usingrawkey(key, key_len, data, data_len, out)`
- 2.5배 성능 향상
- FIPS-140 인증 지원

## 지원 알고리즘 (7.1 기준)
- HMAC-SHA256, ChaCha20-Poly1305
- [[MLDSA]] (FIPS 204)
- SHAKE128/256 XOF
- CRC64 최적화

## Connections
- [[CryptoApi]] — 기존 API
- [[AfAlg]] — 사용자 공간 API (비권장)
- [[Fscrypt]] — 파일시스템 암호화
- [[FsVerity]] — 무결성 검증
- [[DmVerity]] — 디바이스 매퍼 무결성
- [[FIPS140]] — 인증 요구사항
