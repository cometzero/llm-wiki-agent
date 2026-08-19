---
title: "Spatial Memory Agent 참고 문헌과 연결 고리"
document_type: references
source_url: https://arxiv.org/html/2608.12743
hf_url: https://huggingface.co/papers/2608.12743
arxiv_id: "2608.12743"
arxiv_url: https://arxiv.org/abs/2608.12743
pdf_url: https://arxiv.org/pdf/2608.12743
week: "2026-W33"
ingested_at_kst: "2026-08-19 09:40:35 KST"
selected_reason: "SMA의 공간 post-training·tool use·procedural memory 계보를 검토하기 위한 핵심 원문 참고문헌이다."
---

# Spatial Memory Agent 참고 레퍼런스

> Semantic Scholar의 `ARXIV:2608.12743/references` 응답은 이 수집 시점에 빈 목록이었다. 아래는 논문 HTML의 bibliography와 본문에서 직접 확인한 핵심 문헌을 골라 정리한 것이다.

## 1. SpatialVLM — 공간 post-training의 비교 축

- **Chen et al. (2024), _SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities_.**
- 링크: https://arxiv.org/abs/2401.12168
- Spatial relation과 grounding을 위한 instruction data로 VLM을 학습하는 흐름이다. SMA는 같은 능력을 weight update가 아닌 external procedure memory로 보완한다. 따라서 “학습한 spatial representation”과 “runtime retrieval로 보강한 reasoning”의 대조점이다.

## 2. SpatialRGPT — grounded spatial reasoning

- **Cheng et al. (2024), _SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models_.**
- 링크: https://arxiv.org/abs/2406.01584
- VLM의 공간 relation을 더 명시적으로 ground하는 모델/데이터 접근이다. SMA가 card에서 요구하는 size, depth, relative location 확인 규칙이 어떤 base spatial competence 위에서 작동하는지 보여 준다.

## 3. EmbSpatial-Bench — embodied spatial relation 평가

- **Du et al. (2024), _EmbSpatial-Bench: Benchmarking Spatial Understanding for Embodied Tasks with Large Vision-Language Models_.**
- 링크: https://aclanthology.org/2024.acl-short.30/
- `left/right/above/under/near/far` 같은 language-grounded relation을 embodied task 관점에서 평가한다. SMA의 main benchmark 중 하나이며, direct control이 아니라 action-supporting spatial answer를 측정한다.

## 4. RAG — semantic retrieval baseline

- **Lewis et al. (2020), _Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks_.**
- 링크: https://arxiv.org/abs/2005.11401
- 외부 corpus의 의미상 유사 문서를 retrieve해 generation을 보강하는 고전 baseline이다. SMA는 semantic similarity만으로는 surface-near but non-transferable procedure를 고를 수 있다고 지적하고, TRS를 추가한다.

## 5. Mem0 — production-oriented long-term memory

- **Chhikara et al. (2025), _Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory_.**
- 링크: https://arxiv.org/abs/2504.19413
- agent memory를 실용적 장기 상태로 관리하는 계보다. SMA는 generic user/agent memory 대신, verifier-grounded **공간 절차**와 transfer reliability를 state로 삼는다.

## 6. MemP — agent procedural memory

- **Fang et al. (2026), _MemP: Exploring Agent Procedural Memory_.**
- 링크: 논문 bibliography 기준 ACL 2026 Findings.
- SMA의 직접 procedural-memory baseline이다. SMA는 MemP의 semantic retrieval에 TRS 보정을 더해, 표면적으로 유사한 경험보다 실제 후속 성공에 연결된 교훈을 선택하려 한다.

## 7. SpaceTools — tool-augmented spatial RL

- **Chen et al. (2026), _SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL_.**
- 링크: https://arxiv.org/abs/2512.04069
- depth/3D 등 전문 도구의 중간 증거와 RL을 사용하는 계열이다. SMA는 추론 시 도구 dependency가 없다는 장점과, 도구가 제공하는 명시적 기하 증거가 없다는 trade-off를 가진다.

## 8. S-Agent — spatial tool use

- **Dai et al. (2026), _S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence_.**
- 링크: https://arxiv.org/abs/2606.20515
- VLM agent가 공간 도구를 호출해 reasoning을 이끌어 낸다. SMA가 다루는 “tool-free inference” 설정의 가장 가까운 대안이며, 실제 deployment에서는 tool cost와 reliability를 포함한 비교가 필요하다.

## 9. SpatialEvo — training-based self-evolution

- **Li et al. (2026), _SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments_.**
- 링크: https://arxiv.org/abs/2604.14144
- deterministic geometric environment의 경험으로 모델을 self-evolve하는 post-training 계열이다. SMA는 Qwen3.5-9B 조건에서 이 baseline과 비교해 47.1→63.5 macro accuracy를 보고하며, external memory가 training-based route의 대안이 될 수 있음을 주장한다.

## 읽는 순서

1. RAG와 Mem0로 memory/retrieval의 기본 가정을 잡는다.
2. SpatialVLM·SpatialRGPT·EmbSpatial로 공간 grounding의 문제를 정의한다.
3. MemP와 SpatialEvo로 procedural memory 및 training-based self-evolution을 비교한다.
4. SpaceTools·S-Agent와 SMA를 비교해, tool evidence와 retrieval memory 중 어떤 inference interface가 실제 로봇/VLA 조건에 적합한지 검토한다.
