---
title: "VLA-Corrector 참고 레퍼런스 요약"
source_url: "https://arxiv.org/html/2607.01804"
hf_url: "https://huggingface.co/papers/2607.01804"
arxiv_id: "2607.01804"
arxiv_url: "https://arxiv.org/abs/2607.01804"
pdf_url: "https://arxiv.org/pdf/2607.01804"
week: "2026-W28"
ingested_at_kst: "2026-07-08 09:40:16 KST"
selected_reason: "Action chunking, closed-loop VLA verification, recovery policy, flow/diffusion VLA 맥락의 핵심 참고문헌 정리."
---

# VLA-Corrector 참고 레퍼런스 요약

Semantic Scholar `paper/arXiv:2607.01804/references`와 본문 related work를 기반으로 핵심 레퍼런스를 정리했다.

## 1. Adaptive Action Chunking at Inference-time for Vision-Language-Action Models (arXiv:2604.04161)

- 링크: <https://arxiv.org/abs/2604.04161>
- 관계: VLA-Corrector와 가장 직접적으로 연결되는 adaptive chunking 선행 연구.
- 요약: Action entropy를 cue로 사용해 inference-time chunk size를 조절한다. Fixed chunk length가 reactivity와 smoothness 사이의 trade-off를 강요한다는 문제의식은 VLA-Corrector와 같다. VLA-Corrector는 entropy가 아니라 latent visual dynamics mismatch를 보고, stale action을 truncation한 뒤 OGG로 recovery한다는 점이 다르다.

## 2. Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA (arXiv:2604.02965)

- 링크: <https://arxiv.org/abs/2604.02965>
- 관계: open-loop long-horizon planning과 lightweight closed-loop verification을 결합한다는 문제 설정이 유사하다.
- 요약: Heavy VLA가 low-frequency macro-planner로 action chunk와 planning context를 만들고, lightweight verifier가 최신 observation으로 planned action을 closed-loop reference action과 비교해 필요할 때만 replanning한다. VLA-Corrector는 verifier를 latent visual dynamics monitor로 구현하고, replan에 OGG guidance를 추가한다.

## 3. Long-Horizon Manipulation via Trace-Conditioned VLA Planning (arXiv:2604.21924)

- 링크: <https://arxiv.org/abs/2604.21924>
- 관계: long-horizon manipulation에서 progress-aware re-planning이 중요하다는 배경.
- 요약: Task-management VLM이 remaining plan과 visual trace를 반복적으로 예측하고, executor VLA가 trace를 따라 local control을 수행한다. Failed step이 remaining plan에 남아 implicit closed-loop replanning을 가능하게 한다. VLA-Corrector는 subtask trace 대신 action chunk execution 중 latent dynamics를 감시한다.

## 4. Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model (arXiv:2603.18091)

- 링크: <https://arxiv.org/abs/2603.18091>
- 관계: action generation과 action evaluation을 분리한다는 맥락.
- 요약: Diffusion action expert가 여러 candidate action chunk를 draft하고, VLM이 perplexity-style metric으로 candidate를 re-rank한다. VLA-Corrector는 candidate selection보다 execution-time drift detection/recovery에 초점을 둔다.

## 5. Closed-Loop Action Chunks with Dynamic Corrections for Training-Free Diffusion Policy (arXiv:2603.01953)

- 링크: <https://arxiv.org/abs/2603.01953>
- 관계: chunk-based action generation에 real-time correction을 결합한다는 점에서 관련.
- 요약: Diffusion policy에 dynamic feature encoder, cross-attention fusion, asymmetric action encoder-decoder를 붙여 environmental dynamics를 action execution 전에 반영한다. VLA-Corrector는 VLA backbone을 freeze하고 external LVM/OGG로 interrupt/recovery를 수행한다.

## 6. VGAS: Value-Guided Action-Chunk Selection for Few-Shot VLA Adaptation (arXiv:2602.07399)

- 링크: <https://arxiv.org/abs/2602.07399>
- 관계: few-shot VLA adaptation에서 action chunk의 selection/evaluation 문제를 다룬다.
- 요약: Fine-tuned VLA를 high-recall proposal generator로 사용하고, Q-Chunk-Former critic으로 semantically faithful하면서 geometrically precise한 chunk를 고른다. VLA-Corrector의 OGG는 post-interrupt replan을 latent dynamics 방향으로 guide한다는 점에서 value-guided selection과 보완적이다.

## 7. Speedup Patch: Learning a Plug-and-Play Policy to Accelerate Embodied Manipulation (arXiv:2603.20658)

- 링크: <https://arxiv.org/abs/2603.20658>
- 관계: execution efficiency와 safety constraint를 함께 다루는 plug-and-play acceleration framework.
- 요약: External scheduler가 action chunk를 adaptive downsample하여 실행 속도를 높이고, learned world model로 state deviation을 surrogate safety metric으로 사용한다. VLA-Corrector도 external module로 policy를 직접 바꾸지 않고 execution behavior를 조절한다.

## 8. π0 / π0.5 계열 VLA

- 관계: VLA-Corrector의 주요 backbone.
- 요약: Generative action expert와 pretrained VLM semantics를 결합하는 대표적 VLA family다. VLA-Corrector는 π0.5에서 fixed horizon trade-off를 측정하고, horizon 50 등 긴 chunk에서 성공률과 success-per-call efficiency를 높인다.

## 9. SmolVLA, X-VLA

- 관계: cross-architecture generalization 평가에 사용.
- 요약: 서로 다른 VLA backbone에서도 LVM+OGG가 improvement를 보인다는 점은 VLA-Corrector가 특정 backbone hack이 아니라 action-chunked VLA 전반에 적용 가능한 framework임을 뒷받침한다.

## 10. LIBERO / MetaWorld

- 관계: 평가 benchmark.
- 요약: MetaWorld는 contact-rich manipulation difficulty split으로 robustness를 평가하고, LIBERO는 language-conditioned long-horizon manipulation과 sample efficiency를 본다. VLA-Corrector가 두 환경 모두에서 효과를 보인다는 점은 drift monitoring과 corrective replan의 일반성을 시사한다.
