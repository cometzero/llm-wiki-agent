---
title: "Context Memory Storage (CMX/STX)"
type: concept
tags: [context-memory, storage, llm]
last_updated: 2026-04-21
sources:
  - gtc-2026-the-inference-kingdom-expands
---

## Definition
[[ContextMemoryStorage]]는 [[KVCache]]가 입력 길이/동시 사용자 수 증가에 따라 폭증하는 부담을 흡수하기 위해, HBM 한계 바깥에서 NVMe 계층 기반의 오프로드/중간 저장 레이어를 두는 접근을 뜻한다.

## Source Components
- [[CMX]]: BlueField 기반 스토리지 연결의 문맥 메모리 계층화.
- [[STX]]: CMX를 클러스터별로 표준화 확장한 스토리지 랙 레퍼런스 구조.

## Why it matters
- 긴 문맥 추론, 다수 동시 세션, 에이전트형 작업에서 KV 캐시와 네트워크 대역폭 한계를 완화.
- 저장 계층이 기존 HBM·DRAM만으로는 부족한 장기 컨텍스트에서 성능/비용 균형을 조절.

## Connections
- [[Vera ETL256]], [[BlueField]], [[NVMe]], [[InferenceOptimization]], [[LongContext]]

## Contradictions
- 기존의 추론 지연 모델과 충돌하지 않고, 오히려 긴 문맥 환경에서 스토리지 계층을 추가해야 한다는 보완적 설계를 강화한다.