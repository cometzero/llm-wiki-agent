---
title: "Intrinsic Policy Efficiency"
type: concept
tags: [VLA, policy-efficiency, deployment]
sources: [policytrim-2606-22540, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

Intrinsic policy efficiency란 model architecture가 아니라 **policy behavior 자체**가 task를 효율적으로 끝내는 정도를 의미한다. 즉 같은 모델이라도 policy의 행동 방식에 따라 deployment 속도와 자원 효율성이 달라질 수 있다는 개념이다.

## Key Distinction

```text
Architecture Efficiency    → inference 속도 (pruning, quantization 등)
Intrinsic Policy Efficiency → policy가 task를 얼마나 빨리/적은 step으로 끝내는가
```

## Why It Matters

VLA deployment에서 실제 병목은:
1. **한 번의 inference 비용** (architecture efficiency — [[Pruning]], [[Quantization]]으로 해결)
2. **필요한 inference 횟수** (intrinsic policy efficiency — [[PolicyTrim]]으로 해결)
3. **[[PhysicalSteps]] 수** (task 완료까지 실제 환경과 상호작용하는 step 수)

[[PolicyTrim]]은 #2와 #3을 동시에 최적화한다.

## Metrics

| Metric | Baseline | PolicyTrim 후 |
|---|---|---|
| [[ActionChunk]] utilization | 1× | 3× |
| [[PhysicalSteps]] | 100% | 48.6% |
| Deployment speed | 1× | 5.83× |
| [[SuccessRate]] | 유지 | 유지 |

## Connections
- [[PolicyTrim]] — intrinsic policy efficiency를 최적화하는 방법론
- [[ActionChunk]] — 효율성의 핵심 단위
- [[TailDegradation]] — intrinsic efficiency 저하 요인
- [[VLA]] — 적용 대상 모델 클래스
