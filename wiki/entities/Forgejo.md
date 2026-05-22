---
title: "Forgejo"
type: entity
tags: [git-forge, security, open-source]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Forgejo

Forgejo는 2022년 Gitea에서 포크된 Git 협업 및 호스팅 플랫폼으로, Codeberg e.V. 비영리 단체가 지원한다. [[Fedora]]도 자체 개발 Pagure 플랫폼을 Forgejo로 대체하는 마지막 단계에 있다.

## Carrot Disclosure Incident (2026)

보안 연구자 Julien Voisin이 Forgejo에서 RCE로 이어질 수 있다고 주장하는 취약점들을 발견했으나, 프로젝트 보안 절차로 비공개 보고하지 않았다. 대신 그는 "carrot disclosure" 방식으로 공개 글과 풀 리퀘스트를 통해 공급업체가 자체 감사를 수행하도록 압박했다.

### Reactions
- **Criticism**: 자원봉사 프로젝트에 적대적, 비전문적 접근이라는 비판
- **Defense**: Forgejo 보안 정책이 지나치게 요구적이라는 반론
- **Outcome**: Voisin이 사과, 익스플로잇 PoC, 권고를 Forgejo 보안팀에 전달. Forgejo는 내부 자격증명 없이는 RCE가 불가능하다고 응답.

## Related Concepts
- [[CarrotDisclosure]] — 비표준 취약점 공개 방식
- [[RCE]] — 원격 코드 실행 취약점
