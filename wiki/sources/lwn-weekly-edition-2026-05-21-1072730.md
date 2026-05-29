---
title: "LWN.net Weekly Edition for May 21, 2026"
type: source
tags: [linux, kernel, open-source, security, cryptography]
date: 2026-05-21
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-05-21-1072730.md
source_hash: 2f9cbd275b3c5e5e
---

## Summary
2026년 5월 21일자 LWN.net 주간판은 [[openSUSE]] 사이트 이용 약관의 연령 제한 논란, [[LSFMM+BPF Summit]] 메모리 관리 및 [[io_uring]] 관련 기술 논의, [[Post-Quantum Cryptography|PQC]] 기반 [[OpenPGP]] 이메일 생태계 진화 등을 다룬다. 커널 7.1-rc4 출시와 AI 기반 버그 보고의 문제점, [[Peter G. Neumann]] 타계 소식도 포함된다.

## Key Claims
- [[openSUSE]] ToS의 "만 16세 이상" 연령 제한은 [[openSUSE]] 행동 강령의 포용 원칙에 어긋나며, 이후 공개 콘텐츠 열람에는 적용되지 않도록 수정됨
- [[BufferedAtomicWrites]]의 [[RWF_WRITETHROUGH]] 플래그는 [[PostgreSQL]]의 성능을 크게 개선할 수 있으나 같은 파일 내 동시 쓰기 시 [[inode]] 잠금 경합 문제가 있음
- [[MGLRU]]와 기존 [[LRU]]를 같은 파일에 두는 것은 지속 가능하지 않으며 통합 또는 분리가 시급함
- [[OpenPGP]]용 PQC 지원 IETF 초안이 최종 승인 단계에 있으며 [[ML-KEM-768+X25519]] 복합 알고리즘이 v4 키에도 적용 가능함

## Key Quotes
> "커널의 메모리 reclaim은 엉망입니다. 우리는 전통적인 LRU와 MGLRU라는 완전히 별개의 축출 알고리즘 두 개를 같은 파일 안에 담아 배포하고 있습니다." — [[Shakeel Butt]], [[LSFMM+BPF Summit]] 2026

> "AI가 감지한 버그는 거의 정의상 비밀이 아니고, 그것을 어떤 비공개 목록에서 다루는 것은 관련된 모든 사람의 시간 낭비라는 점을 분명히 하고 있다." — [[Linus Torvalds]], 커널 7.1-rc4 출시 공지

## Connections
- [[openSUSE]] — 연령 제한 논란이 [[Fedora]], [[Debian]] 등 커뮤니티 거버넌스와 대비됨
- [[LSFMM+BPF Summit]] — [[MemoryManagement]], [[SwapSubsystem]], [[PerCPUMemory]] 등 커널 핵심 영역 논의
- [[Post-Quantum Cryptography|PQC]] — [[OpenPGP]] 서밋에서 [[ML-KEM-768+X25519]] 복합 방식과 v4/v6 키 전환 전략 논의
- [[BufferedAtomicWrites]] — [[PostgreSQL]] [[WAL]] 성능 최적화와 직결
- [[MGLRU]] — [[Android]]에서 7천만 대 기기에 배포되어 latency-sensitive 환경 검증

## Contradictions
- 기존 [[openSUSE]] 커뮤니티 가이드라인과 새 ToS 연령 제한 간 충돌 (이후 수정됨)
- [[MGLRU]] page cache 보호 부족 vs traditional LRU의 page cache 우선순위 휴리스틱 차이
