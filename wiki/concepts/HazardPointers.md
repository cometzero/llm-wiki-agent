---
title: "Hazard Pointers"
type: concept
tags: [linux, kernel, concurrency, lockless, memory-management]
sources: [lwn-weekly-edition-2026-07-30-1084315]
last_updated: 2026-08-07
---

## Summary
[[HazardPointers]] are a lockless object-lifetime technique: readers publish the pointer they are using, and a remover waits until no published hazard references the retired object before freeing it. The July 30 LWN source describes a proposed Linux API with per-CPU fast slots, overflow contexts, wildcard states, and preemption-aware handling.

## Connections
- [[RCU]] — related read-side lifetime mechanism with different reclamation and preemption trade-offs
- [[SwapDeviceOperations]] — another kernel-internal abstraction discussed in the same weekly edition
