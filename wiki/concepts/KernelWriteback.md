---
title: "Kernel Writeback"
type: concept
tags: [linux, kernel, filesystem, storage]
sources: [lwn-weekly-edition-2026-07-02-1079457]
last_updated: 2026-07-10
---

## Summary
[[KernelWriteback]] covers Linux kernel policy for flushing dirty page-cache data to persistent storage. The July 2, 2026 LWN issue highlights discussion of initiating writeback earlier to reduce latency spikes, memory pressure, and delayed I/O bursts.

## Connections
- [[FilesystemMergePolicy]] — both are filesystem/block-layer policy topics.
- [[LinuxKernel]] — writeback is a core kernel I/O path.
- [[lwn-weekly-edition-2026-07-02-1079457]] — source coverage.
