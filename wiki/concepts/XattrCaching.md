---
title: "Xattr Caching"
type: concept
tags: [linux, filesystem, security, caching]
sources: [lwn-weekly-edition-2026-06-04-1074950]
last_updated: 2026-06-12
---

## Summary
[[XattrCaching]]은 SELinux 레이블, ACL, file capability 같은 extended attribute 조회 결과를 캐시해 파일시스템 메타데이터 접근 비용을 줄이는 기법이다. 성능 개선 효과가 있지만 보안 메타데이터의 일관성, invalidation, 메모리 사용량을 함께 관리해야 한다.

## Connections
- [[FilesystemMergePolicy]] — 파일시스템 성능 기능이 보안·일관성 요구와 함께 평가되는 사례.
- [[LinuxKernel]] — VFS, LSM, 파일시스템 구현 사이의 공통 메타데이터 경로.
