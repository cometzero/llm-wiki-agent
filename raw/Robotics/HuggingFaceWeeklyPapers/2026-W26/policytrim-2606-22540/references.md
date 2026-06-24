---
title: "PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training — references"
source_url: "https://arxiv.org/abs/2606.22540"
hf_url: "https://huggingface.co/papers/2606.22540"
arxiv_id: "2606.22540"
arxiv_url: "https://arxiv.org/abs/2606.22540"
pdf_url: "https://arxiv.org/pdf/2606.22540"
html_url: "https://arxiv.org/html/2606.22540"
week: "2026-W26"
ingested_at_kst: "2026-06-24 09:40:00 KST"
selected_reason: "현재 주(2026-W26) 후보 중 VLA deployment의 실제 병목인 action chunk 신뢰도와 redundant physical step을 정면으로 다루며, RL post-training으로 end-to-end 속도를 높이는 방법을 제시한다."
---

# PolicyTrim: VLA의 intrinsic policy efficiency를 높이는 RL post-training 참고 레퍼런스 정리

> Semantic Scholar references API는 이번 실행에서 rate limit(429)로 사용할 수 없어, arXiv HTML 본문과 논문이 명시한 benchmark/model 축을 기준으로 5–10개 핵심 레퍼런스를 정리했다.

## 1. π0 / π0.5 계열 VLA policy

π 계열은 vision-language-action policy의 대표적 foundation model이다. PolicyTrim은 π0.5를 포함한 VLA backbone에서 action chunk reliability와 execution efficiency를 평가한다.

## 2. OpenVLA / OpenVLA-OFT

OpenVLA는 open-source VLA policy 계열이고, OpenVLA-OFT는 fine-tuning/robot action adaptation 맥락에서 자주 비교된다. PolicyTrim의 cross-architecture 결과는 특정 closed model이 아니라 open VLA에도 적용 가능함을 보여준다.

## 3. GR00T / generalist robot policy

GR00T류 generalist robot policy는 다양한 embodiment/task로 일반화를 목표로 한다. PolicyTrim은 이런 foundation-scale policy도 intrinsic policy inefficiency를 가질 수 있음을 보여준다.

## 4. LIBERO Benchmark

LIBERO는 language-conditioned robotic manipulation benchmark로, long-horizon/generalization setting에서 VLA policy를 평가하는 데 널리 쓰인다. PolicyTrim은 success rate뿐 아니라 step 수와 chunk horizon을 함께 보고한다.

## 5. ManiSkill

ManiSkill은 simulation manipulation benchmark로 다양한 robot task를 제공한다. PolicyTrim은 LIBERO 외부 benchmark에서도 speedup과 SR 유지 여부를 검증한다.

## 6. Meta-World

Meta-World는 multi-task robot manipulation benchmark다. PolicyTrim이 여러 benchmark에서 동작한다는 주장을 뒷받침한다.

## 7. Reinforcement Learning for post-training

PolicyTrim은 RL을 task success만이 아니라 reliable horizon과 redundancy reduction에 맞춘다. 이는 sparse success reward를 넘어서 deployment-oriented reward를 설계하는 사례다.

## 8. Efficient VLA / Token pruning / Quantization 연구

기존 효율화는 per-step compute를 줄이는 방향이 많다. PolicyTrim은 per-step 속도가 같아도 policy가 더 긴 chunk를 안정적으로 실행하고 step 수를 줄이면 전체 deployment가 빨라질 수 있음을 보여준다.

## 읽기 순서 제안

1. VLA action chunk 개념 이해
2. LIBERO/ManiSkill/Meta-World metric 확인
3. PolicyTrim Figure 1로 inefficiency 현상 파악
4. Figure 2와 Method로 두 단계 RL objective 학습
5. Table 1–5로 SR/steps/speedup trade-off 확인
