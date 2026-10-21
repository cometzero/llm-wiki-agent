---
title: "MorphAct 핵심 참고문헌 9편과 연구 연결"
source_url: "https://arxiv.org/html/2610.20019v1"
hf_url: "https://huggingface.co/papers/2610.20019"
arxiv_id: "2610.20019"
arxiv_url: "https://arxiv.org/abs/2610.20019v1"
pdf_url: "https://arxiv.org/pdf/2610.20019v1"
week: "2026-W43"
ingested_at_kst: "2026-10-21 09:40:10 KST"
selected_reason: "현재 주 후보의 VLA 직접 관련성 점수 23; raw/wiki에서 ID 및 고유 제목 중복 없음. perception과 action의 context-conditioned parameter generation을 함께 학습하는 numerical-action VLA 연구."
---

# MorphAct 참고문헌 학습 지도

Semantic Scholar의 arXiv:2610.20019/references endpoint와 원문 §6·References를 대조했습니다. 아래는 MorphAct에서의 역할을 정리한 문헌 지도이며 아홉 원논문의 전수 재현/심층 검증 보고가 아닙니다.

## HyperNetworks
- arXiv: [1609.09106](https://arxiv.org/abs/1609.09106)
- 관계: Hypernetwork의 기본 개념: 한 network가 다른 network의 weight를 만든다는 원류입니다. MorphAct의 generator를 이해하는 배경이며 그 자체가 VLA coupling을 다루는 것은 아닙니다.

## HY-WU (Part I): An Extensible Functional Neural Memory Framework and An Instantiation in Text-Guided Image Editing
- arXiv: [2603.07236](https://arxiv.org/abs/2603.07236)
- 관계: MorphAct가 차용한 structured low-rank synthesis primitive의 직접 배경입니다. condition token과 layer/projection query에서 A/B를 만든다는 구현 관점을 연결합니다.

## Gradient Surgery for Multi-Task Learning
- arXiv: [2001.06782](https://arxiv.org/abs/2001.06782)
- 관계: 서로 다른 task gradient의 충돌을 다루는 PCGrad 계열 배경입니다. MorphAct는 gradient surgery 자체를 제안하기보다 context별 effective parameter로 공유 문제를 접근합니다.

## π0: A Vision-Language-Action Flow Model for General Robot Control
- arXiv: [2410.24164](https://arxiv.org/abs/2410.24164)
- 관계: continuous robot action을 flow matching으로 생성하는 π0 backbone입니다. MorphAct가 바꾸지 않는 native objective와 sampler interface를 이해하는 핵심입니다.

## π0.5: a Vision-Language-Action Model with Open-World Generalization
- arXiv: [2504.16054](https://arxiv.org/abs/2504.16054)
- 관계: open-world generalization을 다루는 π0.5입니다. MorphAct의 simulation 및 real-world baseline이며 성능 향상과 deployment cost를 같은 backbone에서 비교합니다.

## X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model
- arXiv: [2510.10274](https://arxiv.org/abs/2510.10274)
- 관계: cross-embodiment soft-prompted VLA인 X-VLA입니다. MorphAct의 핵심 coupling/condition ablation은 이 backbone의 LIBERO integration에서 수행됩니다.

## LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning
- arXiv: [2306.03310](https://arxiv.org/abs/2306.03310)
- 관계: LIBERO benchmark의 배경입니다. Spatial/Object/Goal/Long suite의 성공률과 transfer 평가를 해석하는 기준을 제공합니다.

## Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning
- arXiv: [1910.10897](https://arxiv.org/abs/1910.10897)
- 관계: Meta-World의 multi-task benchmark 배경입니다. MorphAct MT50 표에서 difficulty-group 평균과 task-weighted 성공률을 구분하도록 돕습니다.

## HyperVLA: Efficient Inference in Vision-Language-Action Models via Hypernetworks
- arXiv: [2510.04898](https://arxiv.org/abs/2510.04898)
- 관계: HyperVLA는 hypernetwork를 통한 효율적인 VLA inference의 비교 축입니다. MorphAct는 episode 단위 compact policy 생성과 달리 context/replanning 단위 perception-action coupling에 초점을 둡니다.

## 읽는 순서
HyperNetworks → π0 → HY-WU → MorphAct Method → LIBERO/Meta-World metric → HyperVLA와 deployment 비교. Gradient Surgery는 conflict 진단을 별도로 공부할 때 읽습니다.

근거: [원문 bibliography](https://arxiv.org/html/2610.20019v1#bib), [Semantic Scholar endpoint](https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.20019/references?fields=title,year,externalIds&limit=100).
