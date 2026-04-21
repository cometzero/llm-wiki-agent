---
title: "Project Glasswing: Securing critical software for the AI era — Anthropic"
type: source
tags:
  - cybersecurity
  - ai-safety
  - vulnerabilities
  - mythos
  - anthropic
date: 2026-04-21
source_file: raw/AI/LilysAI/project-glasswing-securing-critical-software-for-the-ai-era-anthropic.md
last_updated: 2026-04-21
sources:
  - project-glasswing-securing-critical-software-for-the-ai-era-anthropic
---

## Summary
[[Anthropic]]는 [[ProjectGlasswing]]을 통해 [[Mythos Preview]]의 취약점 탐지·익스플로잇 능력을 방어 목적의 보안 운영으로 전환하려고 한다. 이 이니셔티브는 정부, 오픈소스 커뮤니티, 클라우드/인프라 업체와 협업해 핵심 소프트웨어에 대한 취약점 식별, 패치, 보안 관행 정착을 빠르게 확장하는 것을 목표로 한다.

핵심은 AI의 공격 능력이 급속히 높아지는 상황에서, 동일한 기능을 방어 측에 조기에 배분해 제로데이 대응 속도를 대폭 높이는 것이다. Anthropic은 파트너에게 모델 사용 크레딧과 보안 기부를 제공하고, 결과를 공개 보고·권고안으로 확산해 보안 생태계 전체로 파급하려 한다.

## Key Claims
- [[ProjectGlasswing]]은 [[ClaudeMythosPreview|Mythos Preview]]의 고성능 취약점 탐지·익스플로잇 역량을 활용해 핵심 소프트웨어 보안을 강화하기 위한 협업형 보안 프로그램이다.
- [[Anthropic]]은 주요 OS/브라우저에서 수천 건의 치명적 결함을 확인하고, 그중 다수에 대해 공개 가능한 패치/권고를 가능케 했다고 설명한다.
- [[Linux Kernel]], [[OpenBSD]], [[FFmpeg]] 등 핵심 소프트웨어에서 인간 개입이 거의 없는 자동화 기반으로 취약점 탐지 사례를 제시하며, 기존 정적/자동 보안 테스트를 상향 보완한다.
- 파트너 접근 범위를 40개 이상 조직으로 확대하고, 추가 자원으로 1억 달러 크레딧 및 오픈소스 단체 지원 기금을 지급해 대규모 스캔을 촉진한다.
- AI 기반 공격 위험은 비용·시간 장벽을 낮춰 급격히 증가할 수 있어, 보안은 더 이상 사후 대응이 아니라 선제적 자동화 협력 체계가 필요하다는 점을 강조한다.
- 산업 협업 결과는 90일 내 보고와 공개 가능한 권고 산출을 통해 확산되며, 정보공유·취약점 공개 프로세스·패치 자동화·보안 개발 생명주기 강화가 핵심 과업으로 설정된다.
- 미국 정부, 동맹국, 연방/주/지역 당국의 보안 우선순위와 연동되어, AI 보안은 국가안보 정책과도 직접 연결되는 문제로 다뤄진다.

## Key Quotes
> "Mythos Preview는 거의 인간 개입 없이 다수의 제로데이 취약점을 식별하고, 관련 익스플로잇까지 자율적으로 생성했다."

> "과거에는 몇 달이 걸리던 취약점 대응이 AI 도입 뒤 몇 분·수일 단위로 압축되며, 방어자와 공격자 모두 역량 격차가 동시에 넓어지고 있다."

> "Project Glasswing은 시작점이다. 프론티어 AI 보안은 단일 조직이 아니라 업계, 오픈 소스, 정부의 동시 협업으로만 가능하다."

> "방어자 우위를 만들려면 강력한 AI 기능을 안전하게 대규모 배포하고, 공유 가능한 권고를 빠르게 공개해야 한다."

## Connections
- [[Anthropic]] — 이니셔티브 주최자이자 [[ClaudeMythosPreview|Mythos Preview]] 배포 주체.
- [[Mythos Preview]] — 취약점 탐지/익스플로잇/방어 적용의 핵심 엔진.
- [[ProjectGlasswing]] — 파트너십형 사이버 방어 프로그램.
- [[AIForCybersecurity]] — 본 소스의 핵심 개념축.
- [[OpenBSD]], [[Linux Kernel]], [[FFmpeg]] — 실제 취약점 식별 대상인 핵심 소프트웨어.
- [[OpenSSF]], [[Linux Foundation]], [[Apache Software Foundation]] — 오픈소스 보안 인프라 확장 대상.
- [[AWS]], [[Microsoft]], [[Cisco]], [[CrowdStrike]], [[Google]], [[Palo Alto Networks]], [[JPMorganChase]] — 파트너 보안 운영 사례.
- [[ClaudeOpus46]] — Anthropic의 보안/안전 장치 개선 맥락에서 차기 모델 연계로 언급됨.
- [[USGovernment]] — 보안 우선순위와 AI 기반 국가안보 연동의 정책 맥락.

## Contradictions
- 기존 위키의 전반적 서술과 충돌하지 않는다. 본 소스는 오히려 [[AIForCybersecurity]]에서 "오픈소스/상용 보안 강화의 대규모 협업 필요성"을 구체 운영 예로 정교화한다.