---
title: "PhysBrain 1.0 기술 보고서: 인간 egocentric video에서 물리 상식 supervision을 추출해 VLA로 전이하기 — references"
type: source
tags: [vla, egocentric-video, physical-commonsense, robotics, references]
date: 2026-05-20
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W21/physbrain-1-0-2605-15298/references.md
source_hash: fc494da131404723
---

## Summary
PhysBrain 1.0의 관련 연구 10편을 정리한 레퍼런스 요약으로, [[VLA]] 정책 학습의 핵심 baseline([[OpenVLA]], [[Pi0]], [[GR00T-N1]])부터 egocentric 비디오 데이터셋([[Ego4D]], [[EPIC-KITCHENS]], [[EgoDex]]), 깊이/카메라 추정 모델([[VGGT]]), 그리고 평가 벤치마크([[SimplerEnv]], [[LIBERO]], [[RoboCasa]])까지 VLA域의 전형적인 레퍼런스 체인을 구성한다.

## Key Claims
- [[OpenVLA]]는 VLM을 robot policy로 전이하는 대표 baseline이며, PhysBrain은 단순 trajectory imitation이 아닌 physical commonsense pretraining 후 adaptation을 강조한다.
- [[Pi0]]([[PhysicalIntelligence]])는 generalist robot action generation 계열의 강력한 baseline이며, PhysBrain은 human-derived physics prior가 policy 성능과 out-of-domain robustness를 끌어올릴 수 있음을 비교 검증한다.
- [[GR00T-N1]]([[NVIDIA]])는 대규모 embodied policy baseline으로, PhysBrain 결과표에서 강한 비교군으로 등장한다.
- [[Ego4D]]는 CVPR 2022의 대표적 egocentric video 소스이며, PhysBrain은 이 영상을 generic caption이 아닌 [[StructuredMetaRecord]]으로 변환한다.
- [[EgoDex]]는 egocentric video에서 dexterous manipulation을 학습하는 연구로, PhysBrain의 egocentric-to-robot transfer 맥락과 밀접하다.
- [[EPIC-KITCHENS]]는 human activity video 소스로, PhysBrain은 action label을 넘어 [[PhysicallyGroundedQA]]로 재주석한다.
- [[VGGT]]는 camera parameter/depth 추정 foundation model 계열로, PhysBrain의 camera motion filtering 및 [[DepthAwareAugmentation]]에 활용된다.
- [[SimplerEnv]](CoRL 2024)는 VLA/robot policy simulation benchmark로, PhysBrain의 out-of-domain 성능 주장 평가에 핵심적이다.
- [[LIBERO]](NeurIPS 2023)는 long-horizon manipulation benchmark로, PhysBrain의 embodied control transfer 평가에 사용된다.
- [[RoboCasa]]/[[RoboCasa]](RSS 2024)은 household manipulation task를 제공하는 벤치마크로, PhysBrain의 VLA adaptation 성능 비교에 쓰인다.

## Key Quotes
> "PhysBrain은 단순 robot trajectory imitation보다 physical commonsense pretraining 후 adaptation을 강조한다" — PhysBrain 1.0 references vs. [[OpenVLA]]

> "PhysBrain의 egocentric-to-robot transfer 맥락과 가깝다" — PhysBrain 1.0 references vs. [[EgoDex]]

## Connections
- [[physbrain-1-0-2605-15298]] — 메인 기술 보고서; 10개 레퍼런스는 모두 PhysBrain 1.0의 배경/비교 기반
- [[physbrain-1-0-2605-15298-analysis]] — analysis에서도 유사한 레퍼런스 언급 가능
- [[OpenVLA]] — VLA policy baseline; PhysBrain의 비교 대상 중 하나
- [[Pi0]] — [[PhysicalIntelligence]]의 VLA policy; PhysBrain 성능 비교 대상
- [[GR00T-N1]] — [[NVIDIA]] robotics foundation model; PhysBrain 결과표의 강한 비교군
- [[Ego4D]] — CVPR 2022 egocentric video dataset; PhysBrain의 비디오 소스 데이터
- [[EgoDex]] — egocentric dexterous manipulation; PhysBrain과 직접적 관련
- [[EPIC-KITCHENS]] — human activity video; PhysBrain의 또 다른 비디오 소스
- [[VGGT]] — CVPR 2025 depth estimation; PhysBrain의 depth-aware augmentation에 활용
- [[SimplerEnv]] — CoRL 2024 VLA benchmark; PhysBrain out-of-domain 평가
- [[LIBERO]] — NeurIPS 2023 manipulation benchmark; PhysBrain 평가 벤치마크
- [[RoboCasa]] — RSS 2024 household benchmark; PhysBrain 성능 비교
- [[SimplerEnv]] — CoRL 2024 simulation benchmark
- [[Ego4D]] — egocentric video dataset

## Contradictions
- 본 문서는 기존 [[physbrain-1-0-2605-15298-analysis]]와 내용상 중복 없음; 동일한 논문의 supplementary materials로서 상호 보완적.