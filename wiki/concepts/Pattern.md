---
title: "Pattern"
type: concept
tags: [Compiler, Rewriting, MLIR]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 한 줄 요약
[[Pattern]]은 컴파일러 연산 그래프에서 특정 형태를 다른 형태로 치환하는 규칙 집합으로, 최적화/단순화/하향 변환의 단위이다.

## 방식
- 선언적 패턴 정의(제약 조건, 매칭 방식, 재작성 결과)
- 네이티브 C++ 재작성
- M-N 패턴 및 동적 조건자 지원

## 역할
- 보일러플레이트를 줄이고 반복 최적화 규칙을 관리하기 쉬움.
- 전면/후면에서 성능, 메모리, 그래프 단순화를 동시에 다룰 수 있음.

## 연결
- [[MLIR]], [[Pass]], [[TableGen]], [[Pattern Description Language|PDL]], [[Rewrite]]