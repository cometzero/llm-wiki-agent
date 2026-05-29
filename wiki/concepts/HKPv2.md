---
title: "HKPv2"
type: concept
tags: [openpgp, key-server, api]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[HKPv2]] (HTTP Keyserver Protocol version 2)는 [[OpenPGP]] 생태계의 세 가지 기존 키 배포 시스템을 통합하는 새로운 API 제안이다.

## Current Systems Being Unified
- [[Hockeypuck]] — HKPv1 구현
- [[Hagrid]] ([[keys.openpgp.org]]) — VKS API + HKPv1 하위 집합
- [[WKD]] (Web Key Directory) — 이메일 주소 기반 정적 인증서 제공

## Key Features
- 검증형/비검증형 키 서버 사용 사례 모두 지원
- 정적 파일 기반 인증서 제공 (특수 소프트웨어 불필요)
- v6 및 PQC 키 migration 촉진 특별 설계
- IETF OpenPGP 워킹그룹 채택 대기 중

## Related
- [[OpenPGP]]
- [[Hockeypuck]]
- [[Hagrid]]
- [[WKD]]
- [[OpenPGPEmailSummit]]