---
title: "Dirty Frag"
type: entity
tags: [vulnerability, lpe, linux]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Dirty Frag

Dirty Frag는 현우 김(Hyunwoo Kim)이 발견하고 2026년 5월 공개한 Linux 로컬 권한 상승(Local Privilege Escalation, LPE) 취약점이다.

## Details
- **Similar to**: Copy Fail 취약점
- **Impact**: 모든 주요 배포판에서 즉각적인 root 권한 상승 가능
- **Disclosure**: 조율된 공개(coordinated disclosure)를 시도했으나 엠바고가 깨짐
- **Status**: 패치나 CVE 존재하지 않음

## Related Vulnerabilities
- **Fragnesia**: XFRM ESP-in-TCP 하위 시스템의 별도 논리 버그, Dirty Frag와 같은 공격 표면

## Mitigation
공격 재현 장벽이 낮아졌으므로, 해당 프로토콜/모듈 사용 여부를 확인하고 임시 비활성화가 우선 적용되어야 한다.

## Related Pages
- [[Fragnesia]]
- [[VulnerabilityDisclosure]]
