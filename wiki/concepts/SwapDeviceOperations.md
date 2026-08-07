---
title: "Swap Device Operations"
type: concept
tags: [linux, kernel, memory-management, swap]
sources: [lwn-weekly-edition-2026-07-30-1084315]
last_updated: 2026-08-07
---

## Summary
[[SwapDeviceOperations]] is the proposed operation/abstraction boundary for swap storage devices. It aims to make the distinct lifetime, I/O, and policy requirements of conventional block swap and emerging swap backends explicit rather than overloading one implementation path.

## Connections
- [[SwapSubsystem]] — the broader Linux swap subsystem
- [[HazardPointers]] — concurrent kernel infrastructure discussed in the same source
