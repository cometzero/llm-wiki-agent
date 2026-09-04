---
title: "LWN.net Weekly Edition for August 27, 2026"
type: source
tags: [lwn, linux, security, kernel, licensing, crypto, tools, distributions]
date: 2026-08-27
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-08-27-1089643.md
source_hash: 60455ab4f2ac2c32
---

## Summary
This issue of [[LWN]] covers disputes around [[BambuLab|Bambu Lab]]'s [[AGPLv3]]/[GPLv2] compliance, a proposed [[OpenMDW]] license for [[LLM]] distribution, and the practical rollout of [[PostQuantumCryptography|Post-Quantum Cryptography (PQC)]] for web and [[OpenPGP]] workflows. It also summarizes the start of the [[LinuxKernel72MergeWindow|Linux Kernel 7.2 Merge Window]] with major scheduler, filesystem, and internal infrastructure changes.

The issue includes a profile of [[Remind]], a text-first calendar/alarm tool with a scripting language for complex schedules, and [[Quickshell]], a QML-based desktop component toolkit for building lightweight shells and widgets. The brief news sections collect distribution releases, security advisories, kernel status updates, and community announcements.

## Key Claims
- [[SoftwareFreedomConservancy|Software Freedom Conservancy]] says [[BambuLab|Bambu Lab]] violated [[AGPLv3]] and [[GPLv2]] obligations in [[BambuStudio|Bambu Studio]] and printer firmware distribution, especially around dynamically loaded libraries and network-access gating.
- The Bambu case shows that copyleft enforcement depends on user and rightsholder action, not automatic license magic.
- [[OpenMDW]] tries to package model, data, weights, software, and documentation under one permissive license, but its rights-termination language is controversial.
- [[PostQuantumCryptography|Post-Quantum Cryptography (PQC)]] deployment is now a practical ops issue for TLS and [[OpenPGP]], with hybrid schemes like [[ML-KEM-768+X25519]] becoming the default transitional choice.
- The [[LinuxKernel72MergeWindow|Linux Kernel 7.2 Merge Window]] introduced notable changes to scheduler fairness, `binfmt_misc`, filesystem isolation primitives, and Rust/kernel infrastructure.
- [[Remind]] is a durable text-script calendar/alarm tool for complex recurrence and exception logic, but it is not designed for collaborative calendar synchronization.
- [[Quickshell]] lowers the barrier to building QML-based desktop shell components and widgets for minimalist Wayland environments.

## Key Quotes
> "Affero GPL 애플리케이션의 일부를 웹 서버에 올려 둔 뒤 독점으로 유지할 수는 없습니다."

> "OpenMDW"는 모델 배포물의 권리를 하나의 라이선스로 정리하려는 시도다.

> `X25519MLKEM768` is the default hybrid path most software is converging on.

## Connections
- [[BambuLab|Bambu Lab]] — 3D printer vendor at the center of the copyleft compliance dispute.
- [[SoftwareFreedomConservancy|Software Freedom Conservancy]] — organization leading compliance and enforcement efforts.
- [[AGPLv3]] — core license involved in the Bambu Studio dispute.
- [[GPLv2]] — implicated by firmware and Linux-based component source distribution claims.
- [[OpenMDW]] — proposed permissive license for model/data/weights distribution.
- [[OpenSourceDefinition|Open Source Definition]] — referenced in criticism of OpenMDW's broad termination language.
- [[QuantumComputing]] — background threat model motivating post-quantum migration.
- [[PostQuantumCryptography|Post-Quantum Cryptography (PQC)]] — migration target for TLS and OpenPGP.
- [[OpenSSL]] — primary server-side crypto stack for TLS rollout.
- [[OpenPGP]] — email/package signing ecosystem facing PQC transition challenges.
- [[LinuxKernel|Linux Kernel]] — merge-window changes and scheduler/filesystem updates.
- [[Remind]] — CLI calendar/alarm tool featured in the tools section.
- [[Quickshell]] — QML desktop shell toolkit featured in the tools section.
- [[LWN]] — publication source for the issue.
- [[LinuxFoundation|The Linux Foundation]] — publisher of OpenMDW submission and other community infrastructure.

## Contradictions
- Contrasts with the idea that copyleft enforcement is self-executing; the Bambu case argues that rights only matter when exercised.
- Challenges the notion that a single permissive license can cleanly cover LLM artifacts without introducing rights/termination ambiguity.
- Shows that PQC deployment is no longer purely research-oriented; operational defaults and distro policy now matter.
