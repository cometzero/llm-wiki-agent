---
title: "Autocrypt v2"
type: concept
tags: [email, encryption, pqc]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[Autocrypt]] v2는 [[Delta Chat]] 프로젝트가 부분적으로 추진한 명세로, 시계 기반 키 회전 방식과 [[PQC]] 암호화를 결합한다.

## Key Features
- 영구 대체 키 + 수명이 짧은 암호화 하위키 (예: 10일)
- [[ReliableDeletion]] ("forward secrecy") 지원
- PQC hybrid cryptography 통합
- "store-now-decrypt-later" 양자 컴퓨터 공격 방어

## Trade-offs
- 신뢰 가능한 삭제는 과거 메일 복구 능력 감소
- [[Delta Chat]] 2026년 배포 예정
- [[OpenPGPEmailSummit]] 2026에서 논의 완료

## Related
- [[OpenPGP]]
- [[Post-Quantum Cryptography|PQC]]
- [[Delta Chat]]
- [[ReliableDeletion]]
- [[OpenPGPEmailSummit]]