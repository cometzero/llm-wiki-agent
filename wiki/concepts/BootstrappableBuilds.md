---
title: "Bootstrappable Builds"
type: concept
tags: [build-system, reproducibility, supply-chain-security, compiler]
sources: [lwn-weekly-edition-2026-08-20-1088565]
last_updated: 2026-08-28
---

## Summary

[[BootstrappableBuilds|Bootstrappable build]]는 self-hosting compiler와 toolchain을 더 작은 audit 가능한 seed에서 단계적으로 재구성해, 이미 설치된 binary를 무조건 신뢰해야 하는 문제를 줄이는 build-system 접근이다. 목적은 완전한 신뢰를 자동으로 보장하는 것이 아니라, source-to-binary 신뢰 사슬을 검토·재현 가능한 경계까지 축소하는 것이다.

## Connections

- [[lwn-weekly-edition-2026-08-20-1088565]] — build germ, cross-architecture bootstrap, compiler trust를 다룬다.
