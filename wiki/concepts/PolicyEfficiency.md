---
title: "Policy Efficiency"
type: concept
tags: [VLA, deployment, optimization]
sources: [policytrim-2606-22540-analysis]
last_updated: 2026-06-24
---

Policy efficiency는 [[VLA]] deployment에서 compute efficiency(모델 연산 효율)와 분리된 개념으로, 정책 자체의 행동 효율성을 의미한다. 주어진 task를 성공적으로 완수하면서도 최소한의 forward inference calls와 physical execution steps를 사용하는 능력을 측정한다.

## 정의
- Compute efficiency: 모델 inference 속도/홰율
- Policy efficiency: 위와 분리하여, "정책이 얼마나 신뢰할 수 있는 action을 produzieren하는가"

## 핵심 지표
1. **Reliable action chunk length**: 한 번의 inference로 신뢰할 수 있는 action sequence 길이
2. **Forward inference calls**: deployment 시 필요한 inference 호출 횟수
3. **Physical execution steps**: task 완료까지 필요한 실제 robot 동작 수
4. **End-to-end speedup**: policy efficiency 개선으로 인한 전체 속도 향상

## PolicyTrim 기여
[[PolicyTrim]]은 policy efficiency를 [[RLPostTraining]]으로 최적화하여:
- Action chunk utilization 3배 향상
- Physical steps 51.4% 감소
- 최대 5.83배 speedup 달성

## 연결
- [[VLA]] — 대상 architecture
- [[ActionChunk]] — 최적화 대상
- [[PolicyTrim]] — 최적화 방법론
- [[RLPostTraining]] — 기술적 접근
