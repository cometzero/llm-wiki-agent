---
title: "x32 ABI"
type: concept
tags: [linux, abi, x86]
sources: [lwn-weekly-edition-2026-06-04-1074950]
last_updated: 2026-06-12
---

## Summary
[[X32ABI]]는 x86-64 명령어 세트를 사용하면서 32비트 포인터와 C long 크기를 유지하는 Linux ABI이다. 메모리 사용량과 캐시 효율을 줄일 수 있지만, 사용자 기반·테스트·배포판 지원이 제한적이면 [[LinuxKernel]] 유지보수 비용이 기술적 장점을 압도한다.

## Connections
- [[LinuxKernel]] — 오래된 ABI를 얼마나 오래 유지할지 결정하는 커널 정책 사례.
- [[OpenSource]] — 사용자 기반과 유지보수자 관심이 기능의 생존성을 좌우하는 커뮤니티 프로세스.
