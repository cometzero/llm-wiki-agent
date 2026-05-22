---
title: "HugeTLBFS"
type: concept
tags: [linux, kernel, memory]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

## Summary
hugetlbfs는 사전에 예약된 huge page를 파일시스템 인터페이스로 노출하는 Linux 메커니즘이다. mshare나 Transparent Huge Page 논의와 달리 명시적 예약·관리 모델을 갖기 때문에 데이터베이스/가상화 워크로드에서 예측 가능성과 운영 비용의 trade-off가 있다.

## Connections
- [[lwn-weekly-edition-2026-05-14-1071535]] — 이 개념/엔티티가 소개되거나 중요 맥락으로 연결된 LWN 주간 번역 소스.
