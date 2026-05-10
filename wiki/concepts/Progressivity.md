---
title: "Progressivity"
type: concept
tags: [CompilerDesign, Abstraction, IR]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 한 줄 요약
정보를 과도하게 조기에 버리지 않고 단계적으로 하향 변환하는 설계 원칙이다.

## 핵심 메시지
- 고수준 연산 의미를 너무 빨리 없애면 향후 최적화 기회가 감소한다.
- 중간 상태를 유지하면 배치/타깃별 전환이 유연해진다.

## MLIR 맥락
- [[MLIR]]의 핵심 세 가지 원칙 가운데 하나.
- 추상화 단계를 적절히 보존해 디버깅 가능성과 유연성 확보.

## 연결
- [[MLIR]], [[Traceability]], [[Parsimony]], [[Dialect]], [[Pass]]