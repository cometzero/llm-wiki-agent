---
title: "LWN Weekly 2026-11-12 한국어 기술 리포트"
type: source
tags: [lwn, linux, security, governance, dynamic-linker]
sources: [lwn-weekly-edition-2026-11-12-1105460]
last_updated: 2026-11-27
date: 2026-11-12
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-11-12-1105460.md
source_hash: 0e8a45abe59ef137e8d92905c373ff37c22b5f23f0f54090e1742ecbbef03f0d
source_url: https://lwn.net/Articles/1105460/bigpage
article_id: "1105460"
---

## Summary

공개 Weekly Edition의 CC BY-SA 4.0 특집 5편을 전문 번역하고 라이선스 미확인 단신·인용은 독자 요약으로 구분했다. 57개 해설 각주, 보안 공지 870행, kernel patch 79개 및 뉴스레터·행사 메타데이터를 보존했다. DisplayLink 특허 분쟁, Git 의사결정 절차, lockdown hibernation, user namespace/file capability 권한 경계, glibc dynamic linker hardening이 중심 주제다.

## Key Claims

- [[DisplayLink]] 드라이버 개발 중단 사례는 소프트웨어 특허가 공개 구현·상호운용성 작업을 제약할 수 있음을 보여 준다. [[Synaptics]]의 주장과 법원의 유효성 판정은 구분한다.
- [[Git]]의 LLM 정책 논의는 내용의 합의뿐 아니라 투표권·집계 방식·의사결정 규칙을 먼저 정해야 하는 governance 문제다. 확정 정책으로 기술하지 않는다.
- [[SecureHibernation]]은 메모리 이미지 암호화뿐 아니라 신뢰된 kernel에서 생성됐는지와 rollback·복원 경로·TPM 상태를 함께 다뤄야 한다.
- [[UserNamespaceFileCapabilities]]는 namespaced root와 host UID mapping, capability 부여 범위 사이의 권한 누출을 다룬다. namespace 존재만으로 강한 격리가 보장되지 않는다.
- [[DynamicLinkerHardening]]은 glibc tunable로 실행 형식·memory permission을 제한할 때 PIE/ASLR 보안 효과와 외부 binary 호환성을 함께 검증해야 함을 보여 준다.
- 보안 공지와 patch 목록은 발행 당시 스냅샷이다. 제출된 patch는 병합·배포·취약성 해소를 의미하지 않는다.

## Key Quotes

독립적인 직접 인용은 추가하지 않았다. 허용된 특집 번역은 저자·발행일·canonical URL·CC BY-SA 4.0 및 변경 사실을 명시한다.

## Connections

- [[LinuxKernel]] — lockdown, namespace, kernel patch 및 release 유지보수.
- [[Git]] — LLM 기여 정책과 governance.
- [[DisplayLink]] / [[Synaptics]] — 상호운용성 구현과 특허 위험.
- [[SecureHibernation]] — boot 신뢰를 suspend/resume 경로까지 확장.
- [[UserNamespaceFileCapabilities]] — ID mapping과 executable 권한 부여의 결합.
- [[DynamicLinkerHardening]] — loader policy, PIE/ASLR, executable stack 호환성.

## Contradictions and Scope

기존 wiki와 직접 충돌하는 주장은 확인하지 못했다. 이 리포트는 호의 전체 항목을 다루되 모든 단신의 전문 번역은 아니다. 주입 JSON이 11월 19일호를 제외하고 11월 12일호를 선택했으며, 11월 27일 기준 최신호를 다시 판정한 결과로 오해하지 않는다. 기사에 등장하는 향후 계획·보안 취약성·릴리스 정보는 발행 당시 맥락이다.

## Materialization

NVIDIA 정상 ingest는 EOL 모델 HTTP 410, 단일 Codex fallback은 실행 파일 부재로 실패했다. 기사별 번역 산출물과 링크·각주·보안 행 원문 일치 QA를 수행한 raw에서 full SHA-256과 nested source_file을 사용해 수동 materialize했다. 기존 다중 source 개념과 overview는 보존했다.
