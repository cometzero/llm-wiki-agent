---
title: "FUSE Filesystem"
type: concept
tags: [linux, filesystem, userspace, io]
sources: [lwn-weekly-edition-2026-08-06-1086134]
last_updated: 2026-08-14
---

## Summary
[[FUSEFilesystem]]는 userspace daemon이 filesystem semantics를 구현하고 kernel FUSE layer가 VFS request를 전달하는 Linux interface다. 성능과 correctness는 request batching, buffer ownership, page/cache interaction, daemon scheduling에 민감하며, [[io_uring]] 통합은 submission/completion overhead를 줄일 수 있는 한편 buffer lifetime contract를 더 중요하게 만든다.

## Connections
- [[lwn-weekly-edition-2026-08-06-1086134]] — buffer sizing, `io_uring`, maintainer roadmap
- [[io_uring]] — asynchronous I/O integration
- [[Iomap]] — Linux filesystem I/O abstraction의 인접 계층
