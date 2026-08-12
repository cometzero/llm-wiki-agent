---
title: "DEFT-RLVR 참고 레퍼런스"
document_type: references
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.01755/references
hf_url: https://huggingface.co/papers/2608.01755
arxiv_id: "2608.01755"
arxiv_url: https://arxiv.org/abs/2608.01755
pdf_url: https://arxiv.org/pdf/2608.01755
week: "2026-W32"
ingested_at_kst: "2026-08-12 09:40:01 KST"
selected_reason: "DEFT-RLVR의 AD reasoning, verifiable reward, structured CoT 맥락을 연결하기 위한 핵심 인용문헌."
---

# DEFT-RLVR 참고 레퍼런스

Semantic Scholar `ARXIV:2608.01755/references` 응답과 원문 reference section에서 선별했다(조회 성공). 아래 요약은 각 문헌의 제목·공개 메타데이터 및 DEFT-RLVR과의 관계에 근거한다.

1. **Accelerating Structured Chain-of-Thought in Autonomous Vehicles** (2026), [arXiv:2602.02864](https://arxiv.org/abs/2602.02864)
   자율주행에서 structured CoT를 빠르게 만드는 연구 흐름이다. DEFT-RLVR은 CoT의 속도뿐 아니라 **GT 미래를 본 CoT의 인과적 신뢰성**을 문제 삼고, candidate-blind 단계로 방향을 바꾼다.
2. **Rethinking Multiple-Choice Questions for RLVR: Unlocking Potential via Distractor Design** (2026), [arXiv:2603.12826](https://arxiv.org/abs/2603.12826)
   RLVR에서 MCQ 후보/distractor 설계가 reward 품질을 좌우함을 다룬다. AD-MCQ의 scene-specific candidate construction, separation, validity 설계의 직접적 방법론 맥락이다.
3. **Autorubric: A Unifying Framework for Rubric-Based LLM Evaluation on Non-Verifiable Tasks** (2026), [arXiv:2603.00077](https://arxiv.org/abs/2603.00077)
   rubric-based evaluation의 일반 틀을 제공한다. DEFT-RLVR은 candidate selection의 정확한 verifier 외에 reasoning trace에 structured rubric reward를 붙이는 데 이 계열의 아이디어를 사용한다.
4. **ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability** (2026), [arXiv:2607.14145](https://arxiv.org/abs/2607.14145)
   context anchoring을 다루는 agent 연구다. DEFT의 trajectory anchoring bias와는 반대 문제 설정이지만, 어떤 context가 reasoning policy를 shortcut으로 이끄는지 분석할 비교점이다.
5. **Does Your Reasoning Model Implicitly Know When to Stop Thinking?** (2026), [arXiv:2602.08354](https://arxiv.org/abs/2602.08354)
   reasoning length/termination을 다룬다. DEFT-RLVR은 rubric reward로 unproductive exploration을 줄이고 response length·entropy dynamics를 보고하므로 효율적 reasoning 연구와 연결된다.
6. **A Very Big Video Reasoning Suite** (2026), [arXiv:2602.20159](https://arxiv.org/abs/2602.20159)
   video reasoning capability의 넓은 평가 맥락을 제공한다. DEFT-RLVR은 AD 특화 성능을 높이면서 basic/embodied/3D-multiview/referring-spatial 일반 시각 능력을 별도 추적한다.
7. **Real-Time Aligned Reward Model beyond Semantics** (2026), [arXiv:2601.22664](https://arxiv.org/abs/2601.22664)
   실시간 reward/alignment 신호 설계와 관련된다. DEFT-RLVR은 online rubric보다 낮은 overhead로 reasoning 품질 reward를 제공하려는 AD 특화 사례다.

## 읽기 순서
(1) MCQ/RLVR distractor 설계 → (2) rubric reward → (3) structured AD CoT → (4) DEFT-RLVR 본문 순으로 읽으면, 왜 candidate set 품질과 candidate-blind supervision이 동시에 필요한지 파악하기 쉽다.
