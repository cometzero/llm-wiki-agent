---
title: "LWN.net Weekly Edition for July 9, 2026"
type: source
tags: [linux, kernel, security, filesystem, memory-management]
date: 2026-07-09
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-07-09-1080835.md
source_hash: 3c7485feda589f2b
---

## Summary
이 호는 Linux 커널의 주요 내부 구조 변화를 다룬다: 커널 [[KernelCryptography]] 현대화, [[Iomap]] 계층 구조, [[NegativeDentry]] 제한, 더 빠른 [[RCU]]와 lockless 메모리 할당, 그리고 [[LLMAssistedKernelDevelopment]]에 관한 두 가지 패치 세트.

## Key Claims
- Eric Biggers의 암호화 라이브러리 API 현대화는 사용 편의성과 성능을 크게 개선 (기존 API 대비 2.5배 빠른 HMAC-SHA256)
- [[Iomap]] 레이어는 파일시스템이 파일 offset을 block device의 extent와 매핑하는 공통 계층으로 다양한 파일시스템의 I/O 처리를 단순화
- [[NegativeDentry]] 축적이 수백만 개에 이르면 soft-lock과 DoS 문제 발생 가능
- [[RCU]] expedited grace period 콜백 실행 최적화로 메모리 사용 33%-41% 감소
- [[kmalloc_nolock]]은 BPF 프로그램에서 lock 없이 메모리 할당 가능하게 함

## Key Quotes
> "전통적인 암호화 API는 제대로 작동하지 않습니다. 복잡하고, 사용하기 어렵고, 종종 꽤 느립니다." — Eric Biggers, Linux Security Summit NA 2026

> "다른 하위 시스템과 마찬가지로 우리는 AI에서 생성된 패치를 많이 볼 수 있으며... 벽 너머의 바이브 코딩된 복잡한 RFC 제출은... 길고 심층적인 리뷰를 기대하지 마세요." — Christian Brauner

## Connections
- [[EricBiggers]] — 커널 암호화 라이브러리 관리자, crypto API 현대화 작업 주도
- [[RikVanRiel]] — 1GB HugePage 안정적 할당을 위한 패치 세트 개발
- [[KirylShutsemau]] — VM 게스트 메모리 작업 세트 추적 패치 세트 개발
- [[LinuxSecuritySummit]] — 커널 암호화 현대화 발표 장소
- [[LSFMMbpfSummit2026]] — negative dentry, RCU, lockless 메모리 할당 세션 개최지
- [[Iomap]] — 파일시스템 I/O 추상화 레이어
- [[RCU]] — Read-Copy-Update 동기화 메커니즘
- [[DentryCache]] — 경로명 조회 성능 최적화
- [[AF_ALG]] — 사용자 공간 암호화 API (비권장)

## Contradictions
- 없음 — 이전 LWN호와 직접적인 모순 없음

## Technical Notes
- Kernel 7.1에서 암호화 라이브러리는 다수의 알고리즘 지원 (HMAC-SHA256, ChaCha20-Poly1305, ML-DSA, SHAKE128/256 등)
- [[FIPS140]] 인증 지원으로 암호화 라이브러리 테스트 필요
- [[kmalloc_nolock]]은 BPF 맵 사전 할당 없이 BPF 할당자 활용 가능
