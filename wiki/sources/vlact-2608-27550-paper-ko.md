---
title: "VLAct: 데이터 스케일링을 넘어선 표현 중심 VLA 지속 사전학습"
type: source
tags: [vision-language-action, robotics, pretraining, cross-embodiment, action-space-alignment]
date: 2026-09-02
source_url: https://arxiv.org/html/2608.27550
hf_url: https://huggingface.co/papers/2608.27550
arxiv_id: "2608.27550"
arxiv_url: https://arxiv.org/abs/2608.27550
pdf_url: https://arxiv.org/pdf/2608.27550
week: "2026-W36"
ingested_at_kst: "2026-09-02 09:40:54 KST"
selected_reason: "고정된 로봇 데이터 예산에서 VLM prior 보존·다중 action-head·교차 embodiment action semantics로 VLA 전이성을 높이는 최신 공개 연구다."
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/vlact-representation-centric-vla-2608-27550/paper-ko.md
source_hash: 5481e2f9e2d109ac
---

## Summary
[[VLAct]]는 pretrained [[VisionLanguageModel|VLM]]을 출발점으로 이질적 multi-embodiment robot data에 대해 지속 사전학습을 수행해 [[VisionLanguageAction|VLA]] representation을 강화하는 방법이다. 핵심은 데이터 규모만 키우는 대신 [[VLM]] prior 보존, 다중 continuous [[ActionHead|action head]] co-supervision, embodiment 간 부분적 action-space 정렬을 통해 더 재사용 가능한 표현을 만드는 것이다.

이 방법은 [[LIBERO-Plus]], [[RoboTwin 2.0]], [[VLA-Arena]], [[DOMINO]], [[RoboCasa]], [[RoboDojo]] 등에서 성능을 보고하며, unseen humanoid transfer에서도 일부 데이터만으로 강한 일반화를 보였다. 저자들은 VLA의 병목이 단순한 scale-up이 아니라 representation preservation, head diversity, cross-embodiment semantics alignment에 있다고 주장한다.

## Key Claims
- [[VLAct]]는 robot trajectory와 caption data를 함께 사용해 [[VLM]] prior를 보존하면서 action-aware representation을 학습한다.
- shallow-layer protection과 caption mixing은 action-only continual training에서 발생하는 drift를 완화한다.
- [[OFT]], [[PI]], [[GR00T]]의 multi-head continuous action co-supervision은 특정 decoder에 표현이 lock-in되는 것을 줄인다.
- partially unified action layout은 서로 다른 embodiment의 공통 물리 semantics, 특히 gripper 관련 semantics를 공유하게 만든다.
- downstream fine-tuning에서는 task별 새 action head를 붙여 pretraining head에 종속되지 않도록 한다.
- 실험은 [[Qwen3-VL-4B]] backbone과 공개 robot/caption data로 수행되었다.

## Key Quotes
> "데이터를 더 넣는다"가 아니라 action-only gradient가 pretrained representation을 덮어쓰지 않도록 한다.

> 좋은 VLA backbone은 특정 policy checkpoint가 아니라 서로 다른 action parameterization이 꺼내 쓸 수 있는 representation이어야 한다.

## Connections
- [[VisionLanguageAction]] — 본 논문의 직접적인 대상인 로봇 VLA 패러다임이다.
- [[VisionLanguageModel]] — pretrained backbone의 출발점이다.
- [[CrossEmbodimentLearning]] — heterogeneous robot embodiment 간 전이 문제를 다룬다.
- [[ActionSpaceAlignment]] — embodiment 간 action semantics를 정렬하는 핵심 설계와 연결된다.
- [[Cross-Embodiment Alignment]] — 여러 로봇 몸체 사이의 representation 공유를 강화한다.
- [[RepresentationLearning]] — 논문의 중심이 데이터 규모가 아니라 표현 보존과 정렬이라는 점을 설명한다.
- [[DataRecipe]] — caption mixing, head diversity, partial unification 같은 recipe 설계와 직접 연결된다.
- [[ActionGrounding]] — visual-action representation이 downstream action으로 이어지는 핵심 목적이다.
- [[ActionHead]] — multi-head continuous supervision과 downstream 새 head 교체에 해당한다.
- [[Qwen3VL]] — base backbone으로 사용된 VLM 계열이다.
- [[LIBERO-Plus]] — 핵심 benchmark 중 하나다.
- [[RoboTwin 2.0]] — dual-arm generalization 평가에 사용된다.
- [[VLA-Arena]] — behavioral generalization 평가 축이다.
- [[RoboCasa]] — unseen humanoid transfer 평가와 연결된다.
- [[RoboDojo]] — large-scale sim task 평가와 연결된다.
- [[GR00T-N1]] — humanoid transfer baseline 비교 대상이다.
- [[DROID]] — 공개 robot trajectory data source 축과 연결된다.
- [[OpenX-Embodiment]] — heterogeneous robot data mixture라는 점에서 배경 맥락이 가깝다.
- [[OpenVLA]] — VLA scaling 계열 선행 연구와 비교되는 맥락을 제공한다.
- [[π0]] — cross-embodiment robot policy 계열 선행 연구와 연결된다.
- [[StateTransitionCaptioning]] — robot/caption pair를 통해 representation을 강화하는 데이터 설계와 연결된다.
- [[ActionChunking]] — continuous action representation을 chunk 단위로 다루는 맥락과 맞닿아 있다.

## Contradictions
- 단순한 데이터 스케일링이 VLA 개선의 주된 해법이라는 관점과는 다르다. 이 소스는 representation preservation과 action-space alignment가 더 중요할 수 있다고 본다.
- fully unified action space가 항상 최선이라는 입장과는 다르다. 이 소스는 물리적으로 대응되는 dimension만 부분 공유하는 것이 더 안전하다고 주장한다.