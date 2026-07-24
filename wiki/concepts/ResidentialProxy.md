---
title: "Residential Proxy"
type: concept
tags: [networking, security, ai-scraping]
sources: [lwn-weekly-edition-2026-07-16-1081915]
last_updated: 2026-07-24
---

## Definition
주거용 프록시(Residential Proxy)는 일반 가정 또는 모바일 ISP 주소를 프록시 출구로 사용하는 방식이다. 서버 입장에서는 데이터센터 IP 차단보다 탐지가 어렵고, rate limit 정책이 정상 사용자까지 건드릴 위험이 커진다.

## Overview
AI/LLM scraper는 대규모 언어 모델의 훈련 데이터를 확보하기 위해 웹사이트를 광범위하게 스크랩한다. 이 트래픽은 주로 주거용 프록시 네트워크에서 발생하며, 수백만 개의 고유 IP 주소에서 각 IP가 2~3회 사이트에 도달하는 패턴을 보인다.

### 운영자 유형
1. **범죄 조직**: 맬웨어로 감염된 시스템에서 스크레이핑 실행
2. **"합법" 기업**: Bright Data처럼 "윤리적으로 소스가 제공된다"고 광고하는 회사
3. **앱 개발자**: 사용자 네트워크 연결을 가로채는 라이브러리 제공

### 주요 사건
- 2026년 초: Google이 [[IPIDEA]] 봇 네트워크 중단 → 스크레이퍼 트래픽 감소
- 2026년 7월 2일: Google이 FBI와 협력하여 [[NetNut]] 주거용 프록시 네트워크 폐쇄

## Connections
- [[AIScraper|AI scraper]] — 주거용 프록시의 주요 고객
- [[OpenWebDefense|Open Web Defense]] — 대응 전략
- [[LWN]] — 영향을 받는 출판사
