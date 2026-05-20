---
title: "Linux Kernel ABI Compatibility"
type: concept
tags: [linux, kernel, abi, compatibility]
sources: [lwn-weekly-edition-2026-05-07-1070466]
last_updated: 2026-05-20
---

## Summary
Linux kernel ABI compatibility describes the kernel community's strong norm that user-space programs should not break when the kernel changes. The rseq/TCMalloc discussion in the May 7, 2026 LWN weekly edition illustrates that even behavior outside the documented ABI can be treated as a regression if deployed user space relies on it.

## Key Points
- The kernel's practical compatibility contract is shaped by deployed programs, not only by formal documentation.
- Regression handling often favors preserving real workloads while adding warnings, documentation, or transition paths.
- Runtime libraries such as allocators can expose subtle ABI dependencies because they sit on performance-critical paths.

## Connections
- [[LinuxKernel]] — kernel development and release policy context.
- [[CoordinatedVulnerabilityDisclosure]] — another maintenance policy where real-world users constrain ideal process design.
