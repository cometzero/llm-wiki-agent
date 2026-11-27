---
title: "Secure Hibernation"
type: concept
tags: [lwn, linux, security]
sources: [lwn-weekly-edition-2026-11-12-1105460]
last_updated: 2026-11-27
---

## Summary

Secure Boot/lockdown은 부팅 이후 kernel 변조 경로도 통제해야 한다. Hibernation은 메모리 전체를 디스크에 기록했다가 복원하므로 저장 이미지의 기밀성뿐 아니라 출처·무결성·오래된 이미지 재사용 방지가 필요하다.

## Operational Boundary

TPM에 봉인된 key와 PCR 상태를 활용한 제안은 hardware의 PCR cap 지원과 복원 경로에 의존한다. 암호화 파일이라는 이유만으로 현재 부팅 상태에 대한 신뢰가 보장되지는 않는다.

## Connections

- [[lwn-weekly-edition-2026-11-12-1105460]] — 2026-11-12 보도와 한국어 번역·해설.
- [[LinuxKernel]] — 관련 기술·당사자 맥락.
