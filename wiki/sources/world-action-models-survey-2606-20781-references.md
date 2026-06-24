---
title: "World Action Models: A Survey — references"
type: source
tags: [vla, world-model, autonomous-driving, references]
date: 2026-06-24
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W26/world-action-models-survey-2606-20781/references.md
source_hash: 1955d931a319b378
---

## Summary
Semantic Scholar references API rate-limit(429) 문제로 arXiv HTML 본문/표/분야 맥락에 등장하는 대표 축을 기준으로 WAM survey 관련 레퍼런스를 정리한 페이지이다. VLA 일반, Video World Models, 자율주행 World Model 계열, VLA for AD/robotics 관련 repo 논문들, Latent world model, Action-scoring/MPC, Evaluation 논문으로 7축을 구성하며 읽기 순서 제안을 제공한다.

## Key Claims

### 1. Vision-Language-Action Models 일반
VLA는 vision/language context를 executable action으로 직접 변환한다. WAM survey는 VLA를 "현재에서 바로 action을 예측하는 policy"로 정의하고, WAM은 그 사이에 action-facing future를 넣는 계열로 구분한다.

### 2. Video World Models / Video Generation Models
Video diffusion 또는 autoregressive video model은 realistic future를 생성할 수 있지만, WAM 관점에서는 그 future가 action path에 연결되어야 한다. 단순 visual prediction benchmark는 control utility를 보장하지 않는다.

### 3. DriveDreamer / Drive-WM / OmniDreams 계열
Autonomous driving world model은 ego action에 따른 future scene을 생성하거나 closed-loop simulation을 지원한다. WAM taxonomy에서는 rendered future 또는 latent future를 planner/risk evaluator와 연결하는지 확인해야 한다.

### 4. VisualThink-VLA / TBD-VLA / ReflectDrive 계열
이미 repo에 정리된 VLA 논문들은 visual intermediate reasoning, diffusion action generation, discrete action correction 같은 방식으로 action grounding을 다룬다. WAM survey는 이들을 action-facing future/latent/reasoning의 관점에서 다시 비교하게 해준다.

### 5. Latent world model / action-conditioned latent dynamics
Latent-only WAM은 pixel rendering을 생략해 latency를 낮추지만, latent의 causal validity와 interpretability를 따로 검증해야 한다. 자율주행에서는 latent가 traffic participant state, lane topology, route goal을 충분히 보존하는지가 중요하다.

### 6. Action-scoring rollout / Model-predictive control
여러 candidate action을 rollout하고 future utility를 비교하는 방식은 classic MPC와 닮았다. WAM은 learned predictive substrate를 사용해 이 과정을 vision-language foundation model 시대에 재해석한다.

### 7. Evaluation papers for embodied/world models
WAM 평가는 visual fidelity, temporal consistency, causal consistency, closed-loop success, latency, safety를 함께 봐야 한다. 특히 AD에서는 open-loop prediction metric만으로는 deployment risk를 판단할 수 없다.

## 읽기 순서 제안

1. VLA4AD survey로 VA/VLA taxonomy 파악
2. DriveDreamer/OmniDreams로 AD world model 확인
3. VisualThink-VLA/TBD-VLA로 action generation 방식 비교
4. World Action Models survey로 rendered/latent/video-free WAM을 통합 정리

## Connections
- [[WorldActionModel]] — 이 페이지는 WAM survey(2606.20781)의 레퍼런스를 정리한 것이다
- [[Vision-Language-Action Models]] — 1번 축: VLA를 WAM과 대비하는 핵심 프레임
- [[VideoWorldModels|Video World Models]] — 2번 축: action path 연결 필요성
- [[DriveDreamer]], [[OmniDreams]] — 3번 축: 자율주행 world model의 rendered/latent future 연결
- [[VisualThink-VLA]], [[TBD-VLA]], [[ReflectDrive]] — 4번 축: action grounding 방식 비교
- [[Latent World Models]] — 5번 축: latent-only WAM의 validity 검증 필요
- [[Model-Predictive Control]] — 6번 축: action-scoring rollout과 MPC의 관계
- [[WorldModel]] — 상위 개념: WAM survey의 broader world model taxonomy
- [[Autonomous Driving]] — WAM의 주요 응용 도메인
- [[VLA4AD]] — 읽기 순서 1단계: VA/VLA taxonomy
- [[OmniDreams]] — WAM backbone으로 사용된 생성형 world model

## Contradictions
- 없음. 기존 WAM survey 분석 페이지([[WorldActionModel]])와 동일한 논문 출처이며, 이 페이지는 레퍼런스 정리에 집중하므로 내용 충돌 없음.
