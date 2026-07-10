---
title: "SupplyChainSecurity"
type: concept
tags: [linux, security, supply-chain, software-supply-chain]
sources: [lwn-weekly-edition-2026-05-14-1071535, lwn-weekly-edition-2026-06-25-1078380, lwn-weekly-edition-2026-07-02-1079457]
last_updated: 2026-07-10
---

## Summary
소프트웨어 공급망 보안은 소스, 빌드, 배포, 업데이트 경로 전반에서 신뢰성과 변조 방지를 다루는 개념이다. Debian의 재현 가능한 빌드 의무화와 같은 정책은 바이너리가 공개 소스에서 예측 가능하게 생성되었는지 검증해 배포판 신뢰를 높인다. 최근 LWN corpus에서는 Debian package behavior, AUR attacks, PyPI trusted publishing, Secure Boot trust chains, distribution security updates까지 포함해 maintainer→artifact→user trust relationship 전반으로 확장된다.

## Connections
- [[lwn-weekly-edition-2026-05-14-1071535]] — Debian reproducible builds and distribution trust.
- [[DebianProtestware]] — maintainer-controlled package behavior and user trust.
- [[AURSupplyChainAttack]] — community package repositories as attack surfaces.
- [[SecureBootCertificateExpiration]] — certificate lifecycle and boot trust.
- [[TrustedPublishing]] — artifact identity and publishing trust.
