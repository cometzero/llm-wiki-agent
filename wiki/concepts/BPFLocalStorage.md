---
title: "BPF Local Storage"
type: concept
tags: [linux, kernel, bpf]
sources: [lwn-weekly-edition-2026-07-02-1079457]
last_updated: 2026-07-10
---

## Summary
[[BPFLocalStorage]] is the kernel facility that lets BPF programs attach per-object state to kernel objects rather than using only global maps. LWN's July 2, 2026 coverage frames it as a performance and ergonomics issue for tracing, security, and networking programs that need state tied to object lifetime.

## Connections
- [[BPF]] — local storage is part of the broader BPF programming model.
- [[BPFArena]] and [[BPFCoroutines]] — related BPF evolution topics from LSFMM+BPF 2026 coverage.
- [[lwn-weekly-edition-2026-07-02-1079457]] — source coverage.
