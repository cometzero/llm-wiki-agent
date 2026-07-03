---
title: "Free-threaded Python"
type: concept
tags: [python, concurrency, runtime]
sources: [lwn-weekly-edition-2026-06-25-1078380]
last_updated: 2026-07-03
---

Free-threaded Python은 CPython의 global interpreter lock (GIL)을 제거해 여러 Python 스레드가 인터프리터 안에서 병렬로 실행될 수 있게 하는 런타임 전환이다. 이번 LWN 호는 PyCon US 2026 발표를 통해 참조 카운팅, 객체별 잠금, critical section, stable ABI, 확장 모듈 포팅 문제가 이 전환의 핵심임을 정리한다.

## Connections
- [[Python]]
