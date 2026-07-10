---
title: "Secure Boot Certificate Expiration"
type: concept
tags: [linux, security, firmware]
sources: [lwn-weekly-edition-2026-07-02-1079457]
last_updated: 2026-07-10
---

## Summary
[[SecureBootCertificateExpiration]] covers the operational fallout from expiring UEFI Secure Boot certificates. The LWN issue emphasizes that certificate lifecycle management affects shim, bootloaders, installation media, old firmware, and the ability to keep Linux systems bootable while preserving trust-chain guarantees.

## Connections
- [[KernelHardening]] — both are Linux security mechanisms with deployment trade-offs.
- [[SupplyChainSecurity]] — boot trust chains are a supply-chain boundary for systems software.
- [[lwn-weekly-edition-2026-07-02-1079457]] — source coverage.
