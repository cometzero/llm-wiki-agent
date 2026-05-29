---
title: "Post-Quantum Cryptography (PQC)"
type: concept
tags: [cryptography, security, quantum-computing]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[Post-Quantum Cryptography|PQC]]는 양자 컴퓨터로도 깨뜨릴 수 없는 암호화 알고리즘으로, "수집 후 나중에 복호화" 공격에 대비한다. [[OpenPGP]] 생태계에서 PQC 지원이 곧 배포될 예정이다.

## OpenPGP PQC Implementation
- IETF 초안 최종 승인 단계 (RFC 곧公布)
- 7개 알고리즘 (암호화 2개, 서명 3개, PQC 전용 2개)
- [[ML-KEM-768+X25519]] — v4 키에서도 PQC 하위키 사용 가능
- v6 키는 [[SHA2-256]] 지문 사용

## Deployment Timeline
- [[Proton]]: 이미 완전한 PQC 구현 배포
- [[Delta Chat]]: 2026년 말 프로덕션 예정
- [[Thunderbird]]: 2026년 말 v4 PQC 지원 예정
- [[Hockeypuck]]: 베타릴리스에 복합 PQC 키 지원 추가

## Related
- [[OpenPGP]]
- [[ML-KEM-768+X25519]]
- [[QuantumComputing]]
- [[OpenPGPEmailSummit]]
- [[HQC]] (Hammin Quasi-Cyclic — 논의 중)