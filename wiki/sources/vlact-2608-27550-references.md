---
title: "VLAct 참고 문헌: VLA backbone·action head·cross-embodiment transfer"
type: source
tags: [vision-language-action, robotics, references, cross-embodiment-transfer, action-space-alignment]
date: 2026-09-02
source_url: https://arxiv.org/html/2608.27550
hf_url: https://huggingface.co/papers/2608-27550
arxiv_id: "2608.27550"
arxiv_url: https://arxiv.org/abs/2608.27550
pdf_url: https://arxiv.org/pdf/2608.27550
week: "2026-W36"
ingested_at_kst: "2026-09-02 09:40:54 KST"
selected_reason: "VLAct의 representation-centric VLA 지속 사전학습을 이해할 때, 핵심 계보/비교군과 벤치마크 선행문헌을 빠르게 추적하기 위해 생성형 모델링된 참조 맵을 동기화한다."
last_updated: 2026-09-02
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/vlact-representation-centric-vla-2608-27550/references.md
source_hash: 2753da40b41a5c95
---

## Summary

[[VLAct]]의 설계 맥락을 정렬하기 위한 핵심 레퍼런스를 9개로 압축한다. 전체 축은 [[StarVLA]], [[GR00T-N1]], [[PI]] 계열, 그리고 최근 휴머노이드/휴리스틱 scaling 계보까지 망라한다. 공통 주제는 단일 action head 고정이나 데이터 스케일 단독 확대가 아닌, **표현 보존 + 다중 continuous action head + partial action-space 정렬**의 조합으로 cross-embodiment 전이 성능을 높이는 쪽으로의 이동이다.

## Key Claims

- [[VLAct]]는 representation 중심 continued pretraining 계보를 추적할 때 [[StarVLA]] 및 [[StarVLA-Alpha]] 기반 코드 계열을 핵심 기반선으로 본다.
- [[PI]] 계열 VLA 계열과 연결되며, [[pi0.5]]는 공개 대형 일반화를 대표하는 비교군이다.
- 휴머노이드/범용 VLA 비교점으로 [[GR00T-N1]]가 anchor이며, VRo/휴먼-로봇 제어 전이에서 중요한 baseline이다.
- industrial + manipulation 계열에서 ABot-M0 및 data-centric trajectory 계열이 sim-to-real transfer의 보조축으로 중요하다.
- 대규모 real trajectory scaling의 대표군으로 [[Xiaomi-Robotics-1]]가 기준점이며, 데이터량 vs representation의 trade-off를 읽는 지점으로 쓸 수 있다.
- 멀티태스크 sim benchmark로 [[RoboDojo]]와 [[VLA-Arena]]는 성능 해석에 핵심이다.
- long-horizon benchmark로 [[VLA-Arena]]/오픈 월드/안전 축의 연동 여부 점검이 필요하다.

## Reference Map

1. **[[StarVLA]]** — [arXiv:2604.05014](https://arxiv.org/abs/2604.05014)
   - [[VLAct]]가 기반으로 삼는 training codebase 계열이다.
   - 핵심 메시지는 backbone representation을 바꾸기보다, action decoding recipe와 alignment 설계가 성능 이동을 좌우한다는 점.

2. **[[StarVLA-Alpha]]** — [arXiv:2604.11757](https://arxiv.org/abs/2604.11757)
   - [[Qwen]] 계열 VLA 구조에서 baseline 단순화/재현을 낮추는 방향의 비교군.
   - [[VLAct]]의 질문은 "같은 VLM 백본 위에서 어떤 action head/레이아웃이 generalization을 개선하는가"로 이어짐.

3. **[[pi0.5]] (Physical Intelligence)** — [project page](https://www.physicalintelligence.company/blog/pi05)
   - 대규모 open-world generalist VLA와 대조되는 지점: public-data representation recipe의 이득을 확인하는 대표점.
   - [[VLAct]]는 private-scale generalist만으로는 설명되지 않는 representation-preserving pretraining 이점을 제시.

4. **[[GR00T-N1]]** — [project page](https://research.nvidia.com/labs/gear/gr00t-n1/)
   - flow-matching motor module anchor이자 humanoid transfer baseline.
   - [[VLAct]]는 GR00T 스타일 multi-head 구성과 같은 구성요소를 cross-embodiment로 재해석해 비교한다.

5. **[[ABot-M0]]** — [arXiv:2602.11236](https://arxiv.org/abs/2602.11236)
   - action manifold 기반 industrial manipulation baseline.
   - [[VLAct]]의 "representation pretraining이 action architecture 독립적으로 성능 기여를 준다"는 논지를 점검하는 장치.

6. **[[Xiaomi-Robotics-1]]** — [arXiv:2607.15330](https://arxiv.org/abs/2607.15330)
   - 100K+ real trajectory scaling 대표 사례.
   - 이 논문의 실험은 scale 효과를 부정하지 않되, 동일 budget에서 representation-centric recipe가 실익을 좌우함을 강조하는 맥락화로 쓰임.

7. **[[RoboDojo]]** — [arXiv:2607.04434](https://arxiv.org/abs/2607.04434)
   - 42-task unified sim benchmark.
   - metric과 leaderboard date의 안정성 확보가 결과 해석의 전제 조건.

8. **[[VLA-Arena]]** — [arXiv:2512.22539](https://arxiv.org/abs/2512.22539)
   - long-horizon + safety 포함 behavioral generalization benchmark.
   - [[VLAct]]의 representation gain이 task-success 지표 외에 일반화 품질(안전/장기 의존성)에서 어떻게 이어지는지 본다.

9. **[[Xiaomi-Robotics-0]]** — [arXiv:2602.12684](https://arxiv.org/abs/2602.12684)
   - real-time execution + baseline 오픈 모델.
   - 실서비스 관점에서 candidate head와 serving latency 간 balance 판단에 유효.

## Key Quotes

> "representation-centric continued pretraining은 단순 데이터 증대 전략을 보완하는 별도 축이다."

> "multi-head action supervision + partial action-space alignment는 unseen embodiment transfer를 위한 인프라 레벨 선택이다."

## Connections

- [[VLAct]] — 이 참고 문헌 맵의 중심 대상.
- [[VisionLanguageAction]] — backbone-target task 패러다임.
- [[VisionLanguageModel]] — base representation 보존의 출발점.
- [[OFT]], [[PI]], [[GR00T]] 기반 action head 비교 구조와 직접 연동.
- [[CrossEmbodimentLearning]], [[ActionSpaceAlignment]], [[Cross-Embodiment Alignment]] — 핵심 transfer 이론 축.
- [[RoboDojo]], [[VLA-Arena]], [[LIBERO-Plus]], [[RoboCasa]], [[RoboTwin 2.0]] 계열 benchmark 연결.
- [[DataRecipe]] — caption mixing, benchmark split discipline, head configuration 분해에 대응.

## Contradictions

- 기존 일부 요약에서 "대규모 real-robot data 확대 자체"가 유일한 성능 향상 경로처럼 해석된 경우가 있으나, 본 참조 맵은 **표현 보존과 action-head 설계가 본질적 차별점**이 될 수 있음을 명시한다. 이는 "규모=정답" 서사와 긴장 관계를 가지나, 정면 충돌이라기보다 우선순위 재배치로 해석하는 것이 적절하다.

## Posting notes

이 문서는 [[VLAct]]의 성능 해석에서 데이터량, head 다양성, action-space 정렬의 축을 함께 읽기 위한 참조 앵커 역할을 수행한다.