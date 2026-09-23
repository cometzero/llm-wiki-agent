---
title: "ShieldVLA 분석"
document_type: korean-paper-analysis
source_url: https://arxiv.org/html/2609.13231
hf_url: https://huggingface.co/papers/2609.13231
arxiv_id: "2609.13231"
arxiv_url: https://arxiv.org/abs/2609.13231
pdf_url: https://arxiv.org/pdf/2609.13231
week: "2026-W39"
ingested_at_kst: "2026-09-23 09:40:29 KST"
selected_reason: "VLA의 visual safety supervision과 feasibility-gated closed-loop control을 직접 다룬다."
---

# ShieldVLA 분석

## 한 문장 결론
VLM이 만든 rubric safety margin을 HJ reachability critic으로 학습하고 feasible/infeasible 상태의 policy gradient를 분리하면, VLA의 task success를 유지·개선하면서 cumulative safety cost를 줄일 수 있다는 접근이다.

## 문제와 기여

| 항목 | 내용 |
|---|---|
| 문제 | Lagrangian penalty는 residual violation 또는 과도한 보수성을 낳고 visual domain에는 dense safety label이 부족하다. |
| 기여 1 | VLM rubric score를 continuous safety cost/margin으로 사용한다. |
| 기여 2 | model-free HJ safety Bellman operator로 \(Q^s(o,a)\)를 online 학습한다. |
| 기여 3 | \(Q^s>\delta\)에서는 reward gradient, 나머지에서는 \(-Q^s\) safety objective를 쓰는 gate를 둔다. |
| 기여 4 | navigation·reach·fetch 다섯 closed-loop benchmark와 visual OOD를 평가한다. |

## Pipeline과 I/O

```mermaid
flowchart LR
 O[RGB observation + task context] --> V[Frozen VLM rubric scorer]
 V --> C[semantic safety margin]
 C --> Q[HJ safety critic Qs(o,a)]
 O --> P[VLA policy]
 P --> A[action]
 Q --> G{Qs > delta?}
 G -->|yes| R[PPO/task-reward update]
 G -->|no| S[-Qs safety update]
```

입력은 visual observation과 VLA task context, 출력은 robot navigation/manipulation action이다. Language의 주된 역할은 action text 생성이 아니라 VLM rubric의 scene-level safety semantics를 만드는 것이다.

## Training·평가

- Shared replay buffer에 VLM score를 저장하고 critic을 off-policy online training한다.
- Base policy의 PPO/action objective 위에 safety gate가 얹힌다.
- **Benchmark:** Dubins-VL, TurtleBot-Nav, Safety-CHORES Nav/Fetch, Franka-Reach.
- **Metric:** SR(높을수록 좋음), CSC(낮을수록 좋음). 둘 다 executed rollout 기준이라 closed-loop다.
- 보고된 aggregate: SafeVLA 대비 평균 CSC 57% 감소, SR +0.13.

## 강점·한계·배포

**강점:** collision 이후의 sparse binary label보다 pre-contact semantic risk를 쓰며, deployment 때 VLM scorer를 제거할 수 있다. HJ feasibility는 action을 “reward-cost 절충”이 아니라 recoverability 관점으로 분리한다.

**한계:** VLM score와 rubric은 ground truth safety가 아니며 visual shift/prompt bias가 critic에 누적된다. learned HJ critic은 approximation·replay coverage에 의존한다. 논문의 robot benchmark는 autonomous driving의 high-speed multi-agent rare-event 안전을 검증하지 않는다.

**AD relevance:** BEV/occupancy·map·route·velocity로 critic input을 확대하면 E2E driving trajectory/VLA policy의 safety shield가 될 수 있다. 다만 hard traffic rules, uncertainty-aware prediction, comfort와 fail-safe fallback을 별도로 설계해야 한다.
