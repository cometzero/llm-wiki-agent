---
title: "Filesystem Merge Policy"
type: concept
tags: [linux, filesystem, kernel]
sources: [lwn-weekly-edition-2026-06-04-1074950]
last_updated: 2026-06-12
---

## Summary
[[FilesystemMergePolicy]]는 새 파일시스템을 [[LinuxKernel]] 메인라인에 병합할 때 요구되는 코드 품질, 유지보수자 책임, 사용자 공간 ABI, 복구 도구, 보안 모델, 장기 지원 기준을 뜻한다. LWN 2026-06-04호는 파일시스템 기능성보다 장기 운영 가능성이 병합 정책의 핵심임을 강조한다.

## Connections
- [[LinuxKernel]] — 메인라인 병합과 장기 유지보수 정책.
- [[MemoryManagement]] — 파일시스템은 page cache, block layer, writeback 등 커널 내부 하위 시스템과 밀접하다.
