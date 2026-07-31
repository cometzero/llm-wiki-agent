---
title: "PyPI Supply Chain Security"
type: concept
tags: [python, security, supply-chain]
sources: [lwn-weekly-edition-2026-07-23-1083123]
last_updated: 2026-07-31
---

## Summary
[[PyPI]] package index의 업로드 정책과 artifact 불변성을 통해 Python package supply chain을 보호하는 주제다.

## Notes
PyPI가 새 파일 업로드를 일정 기간 이후 제한하는 정책은 release artifact가 나중에 바뀌거나 악성 파일이 추가되는 위험을 낮춘다. 이는 dependency resolver, lockfile, reproducible deployment가 신뢰하는 package index의 시간적 안정성을 강화한다.

## Connections
- [[PyPI]] — Python package index entity
- [[SupplyChainSecurity]] — broader package ecosystem context
- [[lwn-weekly-edition-2026-07-23-1083123]] — PyPI upload policy item
