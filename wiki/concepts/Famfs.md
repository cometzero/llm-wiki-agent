---
title: "famfs"
type: concept
tags: [linux, filesystem, memory, cxl]
sources: [lwn-weekly-edition-2026-07-23-1083123]
last_updated: 2026-07-31
---

## Summary
fabric-attached memory를 file-like interface로 노출하려는 Linux filesystem proposal이다.

## Notes
famfs는 CXL/fabric-attached memory 시대의 공유·persistent memory를 Linux VFS와 application ABI에 맞춰 노출하려는 시도다. 병합 논의의 핵심은 ownership, cache coherency, failure semantics, 기존 memory/filesystem subsystem과의 경계 설정이다.

## Connections
- [[Filesystem]] — filesystem subsystem context
- [[lwn-weekly-edition-2026-07-23-1083123]] — famfs merge discussion
