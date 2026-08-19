---
title: "TransferReliabilityScore"
type: concept
tags:
  - retrieval
  - calibration
  - reinforcement-learning
  - embodied-ai
last_updated: 2026-08-19
---

## 정의

[[TransferReliabilityScore]](TRS)은 memory card가 새 과제에 실제로 transfer되었는지를 반영하기 위한 축소(shrinkage) 신뢰도 점수다. 단순 과거 성과의 합산이 아니라, 방문 횟수와 누적 보상을 고려해 과대 반응을 줄인다.

## 갱신식

일반적으로 다음 꼴로 계산된다.

$$
v_j = \frac{\lambda v_0 + c_j}{\lambda + n_j},\quad v_0=0.5,\ \lambda=2$$

- $c_j$: 누적 성공/보상 신호
- $n_j$: 방문 횟수
- $v_0$: prior (중립값)
- $\lambda$: shrinkage 강도

## 역할

- 메모리 카드의 raw hit-score를 보정
- similarity 중심 retrieval에서 실제 transfer 기여도를 반영
- one-pass writing + read-only deployment에서 업데이트 불안정성을 완화

## 위치

[[SpatialMemoryAgent]]에서 semantic similarity와 결합되어 ranking 스코어를 구성한다.

```text
S = (1-eta)*sim_norm + eta*TRS_norm
```

## 연관 항목

- [[PersistentMemory]]
- [[Reflection]]
- [[Verifier]]
- [[RetrievalAugmentedPolicy]]
- [[ActionGrounding]]