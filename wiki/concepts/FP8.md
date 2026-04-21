---
title: "FP8"
type: concept
tags: [precision, ai, quantization]
sources: [understanding-the-risc-v-extensions-for-ai-john-simpson-sifive]
last_updated: 2026-04-20
---

## Definition
[[FP8]]는 AI 하드웨어 확장에서 계산량을 유지하면서 데이터 읽기 부담을 줄이고 에너지 효율을 개선하기 위한 저비트 부동소수점 정밀도 체계다.

## Relation to source
- [[RiscVExtensionsForAI]] 문맥에서 실제 연산을 위한 FP8 지원은 정밀도 압축만이 아니라 행렬 연산의 처리량/대역폭 균형을 개선하기 위한 핵심 장치로 다뤄진다.
- OCP 계열 경향과 연동해 4-bit/5-bit exponent 형태의 변형도 미래 제안으로 언급된다.

## Tradeoff
정밀도 저하는 신호 표현 오차를 증가시킬 수 있으므로, 모델별 정합성 검증과 함께 사용 경로를 분기해야 한다.
