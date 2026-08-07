---
title: "GRUB"
type: concept
tags: [bootloader, uefi, security, confidential-computing, linux]
sources: [lwn-weekly-edition-2026-07-30-1084315]
last_updated: 2026-08-07
---

## Summary
[[GRUB]] is a widely deployed bootloader in Linux distributions. Fedora's minimized-GRUB decision illustrates a security and maintainability trade-off: reduce the UEFI boot-path attack surface for constrained virtual/confidential environments while retaining the hardware and policy support each target actually needs.

## Connections
- [[Fedora]] — distribution approving the reduced package direction
- [[SecureBootCertificateExpiration]] — prior wiki context on UEFI/Secure Boot operational dependencies
