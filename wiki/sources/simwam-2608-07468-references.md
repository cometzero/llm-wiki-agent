---
title: "SimWAM 참고 레퍼런스"
type: source
tags:
  - autonomous-driving
  - world-action-model
  - world-model-prior
  - references
sources:
  - simwam-2608-07468
source_type: references
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.07468/references
hf_url: https://huggingface.co/papers/2608.07468
arxiv_id: "2608.07468"
arxiv_url: https://arxiv.org/abs/2608.07468
pdf_url: https://arxiv.org/pdf/2608.07468
week: "2026-W33"
ingested_at_kst: "2026-08-12 09:40:01 KST"
selected_reason: "WAM, video generative prior, E2E AD, RL의 직접 선행 연구를 한국어로 연결한다."
title: "SimWAM 참고 레퍼런스"
last_updated: 2026-08-12
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W33/simwam-world-action-model-2608-07468/references.md
source_hash: da1bd56bd1b6dcc0
---

## Summary
[[SimWAM]](arXiv:2608.07468) 주변의 WAM류 선행·대안군을 핵심 축별로 정리한 레퍼런스 맵이다. 특히 WAM 계열에서 **추론 시 비디오 생성을 어떻게 줄일지**, **action 중심 배포 전략이 어디까지 가능할지**, **제로샷 전이와 test-time imagination의 실효성**을 비교하는 읽기 지침을 제공한다.

## Key Claims
- [[DriveWAM]]는 비디오 생성 prior를 AD action modeling에 직접 넣는 WAM류의 직접 선행선이며, [[SimWAM]]은 이 계열의 학습-배포 분리 방식으로 추론 비용을 줄이는 변형으로 읽힌다.
- [[DriveVA]]는 영상/행동 모델을 driving policy로 사용하는 흐름으로, [[SimWAM]]의 zero-shot nuScenes 전이와 “video dynamics→action” 연결 비교 기준을 제공한다.
- [[ExploreVLA]]는 dense world modeling과 탐색을 E2E AD에 결합해, [[WorldActionModel]] 기반 계획 설계 대비 [[SimWAM]]의 latency 중심 설계 차이를 비교할 수 있게 해준다.
- [[DriveDreamer-Policy]]는 geometry-grounded world-action 융합 모델로, SimWAM 대비 추론 시 비디오 출력 유지 전략과 대조해 deployment trade-off 분석이 가능하다.
- Uni-World VLA는 planning과 world modeling을 interleave하는 VLA 계열로, [[SimWAM]]의 action-only 배포 전략이 VLM/VLA 대규모 추론 의존을 지양한 대안임을 보여준다.
- [[Fast-WAM]]는 test-time future imagination의 필요성을 직접 검토해, SimWAM의 핵심 주장인 ‘future video는 학습 신호로 충분할 수 있음’의 반대편 실험 축을 제공한다.
- World Action Models are Zero-shot Policies는 WAM을 zero-shot policy로 해석하는 일반 관점의 anchor로, SimWAM의 nuScenes zero-shot 결과를 broader policy transfer 축에서 해석하게 해준다.
- DriveLaW는 planning과 video generation 통합학습의 대표 선행군으로, SimWAM은 이 계열의 통합 이점을 일부 유지하면서도 추론에서 video branch를 제거해 latency를 낮춘다.

## Key Quotes
> "video generation 비용을 배제한 채 training-time prior만 활용하는 방향은 AD 배포 비용에서 가장 직접적인 리소스-효율 개선축이다." — SimWAM 계열 맥락 정리에서 도출한 비교 기준

> "어떤 WAM이든 trajectory 품질뿐 아니라, 후보 생성 및 policy selection의 검증 가능성까지 함께 봐야 실제 자율주행 배포 적합도를 판단한다." — WAM/AD 레퍼런스 해석의 운영형 기준

## Connections
- [[SimWAM]] — 본 레퍼런스의 중심 모델
- [[WorldActionModel]] — 공통 설계 계열
- [[DriveWAM]] — video generative prior 기반 WAM 선행군
- [[DriveVA]] — video/action 정책 파이프라인 비교군
- [[ExploreVLA]] — dense world modeling + 탐색 기반 E2E AD 비교군
- [[DriveDreamer-Policy]] — geometry-grounded WAM/plan 통합 계열
- Uni-World VLA — interleaved world modeling-planning 비교군
- [[Fast-WAM]] — test-time imagination 부재/존재의 효과 측정 선행군
- World Action Models are Zero-shot Policies — WAM의 zero-shot policy 관점 정합 축
- DriveLaW — planning+video generation 통합 계열과 latency trade-off 비교군
- [[InferenceTimeActionOnlyDeployment]] — SimWAM의 배포 전략과 직접 연결
- [[IsolatedAttentionMask]] — SimWAM의 leakage 제어 핵심 기법을 이해하는데 필요한 문맥
- [[FlowMatching]] — 학습 목표 축에서 video/state/action 신호 공유 설계의 공통 기법

## Contradictions
- 없음. 기존 위키의 SimWAM 분석/번역/AD verifiability 축과 충돌하지 않으며, 오히려 기존 [[WorldActionModel]] 및 [[InferenceTimeActionOnlyDeployment]] 맥락을 선행군 관점에서 보강한다.
