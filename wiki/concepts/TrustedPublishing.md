---
title: "Trusted Publishing"
type: concept
tags: [supply-chain, security, pypi]
sources: [lwn-weekly-edition-2026-06-11-1076254]
last_updated: 2026-06-19
---

## Overview
공급망 공격 방지를 위해 단기 자격 증명을 사용하는 인증 메커니즘. 수명이 긴 API 토큰 대신 OIDC(OpenID Connect) 기반의 임시 토큰을 사용한다.

## How It Works
1. 프로젝트에 신뢰할 수 있는 게시자 설정 (소유자, 저장소, 워크플로 파일, 환경)
2. CI/CD가 GitHub OIDC 공급자로부터 JWT 토큰 요청
3. PyPI가 4가지 문자열 일치 확인 후 15분 만료 토큰 발급

## Adoption
- 2023년 4월 PyPI에 처음 제공
- 2024년 2월: 전체 신규 업로드의 ~10%
- 2026년 5월: 전체 신규 업로드의 36% 이상

## Key Benefits
- 수명이 긴 토큰 유출로 인한 공격 제거
- CI/CD 로그에서 토큰 자동 난독화
- Sigstore 출처 영수증 포함

## Connections
- [[PyPI]] — 주요 플랫폼
- [[MikeFiedler]] — 주요 옹호자
- [[AlphaOmega]] — 자금 지원
- [[Sigstore]] — 출처 검증
