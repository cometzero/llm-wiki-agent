---
title: "LWN.net Weekly Edition for May 14, 2026 — 한국어 기술 번역"
type: source
tags: [linux, kernel, fedora, security, memory-management, open-source]
date: 2026-05-14
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-05-14-1071535.md
source_hash: e058d0e2e45bbda2
---

## Summary
2026년 5월 14일자 LWN.net 주간판은 Fedora 커뮤니티의 AI 개발자 데스크톱 구상을 둘러싼 격렬한 논쟁, Forgejo의 "carrot disclosure" 보안 공개 방식 논란, 그리고 LSFMM+BPF 2026 서밋에서 논의된 커널 메모리 관리의 주요 화제(Andrew Morton 후임, 1GB THP, DAMON 확장, DMA-buf 최적화)를 종합적으로 다룬다.

## Key Claims
- Fedora Council은 AI Developer Desktop 구상을 승인했으나 Justin Wheeler의 반대표 전환으로 합의 절차가 중단됨
- Forgejo "carrot disclosure"는 비표준 취약점 공개 방식으로, 공급업체에 자체 감사를 강제하려는 시도였으나 자원봉사 프로젝트에 적대적이라는 비판을 받음
- Andrew Morton이 메모리 관리 유지관리에서 점진적 은퇴를 시작하며 David Hildenbrand가 통합 트리 관리를 인수
- 커널 7.1-rc3은 2,141명의 개발자가 13,922개 changeset을 기여한 대규모 개발 사이클
- Dirty Frag와 Fragnesia Linux 로컬 권한 상승 취약점이 공개되어 패치 준비 전 엠바고가 깨짐
- Debian이 재현 가능한 빌드를 필수 요건으로 의무화

## Key Quotes
> "저는 Fedora가 정말 오픈소스 프로젝트인지 의문을 부를 것입니다. 라이선스가 특정 활동 분야에서 프로그램을 사용하는 것을 누구에게도 제한해서는 안 된다고 요구하는 OSD를 인용합니다." — Gordon Messmer

> "AI가 찾은 '보안' 버그는 공개된 것이다라는 규칙을 그냥 만들면 된다고 생각합니다." — Linus Torvalds

## Connections
- [[Fedora]] — AI Developer Desktop 구상 관련 커뮤니티 논쟁
- [[RedHat]] — 기업 후원자로서 AI 전략 압력
- [[Forgejo]] — carrot disclosure 보안 공개 사건
- [[AndrewMorton]] — 메모리 관리 유지관리 은퇴
- [[DavidHildenbrand]] — 통합 트리 인수
- [[DAMON]] — 메모리 모니터링 확장
- [[DirtyFrag]] — LPE 취약점 공개
- [[KernelDevelopment]] — 7.1-rc3 대규모 개발 사이클

## Contradictions
- Forgejo는 내부 자격증명 없이는 RCE가 불가능하다고 주장했으나, Voisin은 발견했다고 밝힘 — 정확한 취약점 여부는 추가 검증 필요
- Linus Torvalds의 "AI가 찾은 보안 버그는 공개된 것"이라는 발언은 기존 coordinated disclosure 관행과 충돌 가능
