---
title: "Xiaomi-Robotics-1: 100K+ trajectory 기반 VLA 스케일링"
type: source
tags: [robotics, vla, vision-language-action, scaling, trajectory-data, simulation, manipulation]
date: 2026-07-22
last_updated: 2026-07-22
source_url: "https://arxiv.org/html/2607.15330"
hf_url: "https://huggingface.co/papers/2607.15330"
arxiv_url: "https://arxiv.org/abs/2607.15330"
pdf_url: "https://arxiv.org/pdf/2607.15330"
week: "2026-W30"
selected_reason: "10만+ 시간 real-world trajectory와 state-transition language auto-labeling을 결합해 VLA pre-training 및 cross-embodiment post-training 성능 이전을 실증한 scaling paper"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W30/xiaomi-robotics-1-scaling-vla-2607-15330/analysis.md
source_hash: 0de8c5eb94db3a29
---

## 한 문장 결론

**[[Xiaomi-Robotics-1]]는 UMI 기반 100K+ 시간의 real-world 조작 trajectory를 전처리해 state-transition 언어 레이블로 dense supervision을 만들고, [[Qwen3-VL]] + [[DiffusionTransformer]] 기반 action chunk generator를 학습한 뒤, UMI 밖의 인간 지시문 환경과 다양한 로봇 embodiment로 정렬하는 이중 단계 학습을 통해 VLA의 data/model scaling이 실제 성능으로 이전됨을 보였다.**

## 문제 정의

로보틱스 파운데이션 정책 학습에서는 언어 지시와 조작 상태를 실제 실행으로 정확히 접속시키는 grounding이 핵심인데, 조작 데이터는 [[Teleoperation]]의 비용이 크고 다양성이 제한된다. 본 연구는 아래 질문을 다룬다.

- UMI처럼 값싼 장치 기반 로그로 real-world 조작 trajectory를 VLA pre-training 데이터로 만들 수 있는가?
- state transition 설명(변화의 기술)을 language supervision으로 쓰면 action grounding이 강화되는가?
- pre-training의 data/model scaling이 post-training 성능으로 전달되는가?
- 소량의 downstream 데이터로도 새 task 적응이 잘 되는가?

## 핵심 기여

1. **100K+ 조작 trajectory 전처리형 pre-training 구축**
   - [[UMI]] handheld gripper + egocentric 카메라로 대규모 데이터 수집.
   - open-world (household, industrial, office, outdoor) 분포를 확보해 기존 로봇 트레이닝 편향을 완화.

2. **state-transition language 자동 라벨링**
   - trajectory를 fixed-length segment로 잘라 [[Qwen3.5-27B]]로 `현재 상태 -> 목표 상태` 전이를 captioning.
   - task label 대신 상태 변화 기반 문장으로 supervision을 구성해 action grounding의 정보 밀도 증가 시도.

3. **MoT 기반 VLA 구조 설계**
   - visual encoder + instruction 텍스트를 처리하는 [[Qwen3-VL]] 백본.
   - action branch는 robot state를 포함한 [[DiT]]로 action chunk를 생성.
   - pre-training의 representation/priors를 post-training에서 embodiment + instruction 조건으로 맞춤.

4. **cross-embodiment post-training**
   - UMI에서 학습한 공통 능력을 mobile manipulator, dual-arm, static arm로 transfer.
   - state-transition 중심 pre-text에서 human imperative instruction으로 conditioning shift.

5. **강력한 scaling 근거 제시**
   - 데이터 스케일 증가와 모델 스케일 증가 모두 성능 개선에 기여.
   - out-of-the-box 및 downstream에서의 OOD/새 task 적응이 개선됨.

## 아키텍처 / 파이프라인

```mermaid
flowchart TD
  A[UMI real-world trajectory\n100K+ hours] --> B[fixed-length segmenting]
  B --> C[Qwen3.5-27B\nstate transition captions]
  C --> D[Pre-training corpus\n(vision + transition lang + action)]
  D --> E[Qwen3-VL visual-language encoder]
  E --> F[KV cache + action/state conditioning]
  G[robot proprioceptive state] --> F
  F --> H[DiT action generator]
  H --> I[flow matching action chunk]
  I --> J[Cross-embodiment post-training]
  J --> K[Instruction following / OOD execution]
  K --> L[Downstream few-shot adaptation]
```

## Input / Output / Action

| 항목 | 내용 |
|---|---|
| 입력 vision | egocentric 카메라 기반 관측 + robot proprioception |
| language 입력 | pre-training: state transition description / post-training: human instruction |
| 액션 목표 | horizon \(H\) 연속 control chunk \(a_{t:t+H}\) |
| 생성기 | flow-matching 기반 [[DiffusionTransformer]] |
| grounding 방식 | transition 문장을 action chunk로 변환

## Training Recipe

### Pre-training

- 데이터: `100K+ hours` real-world manipulation trajectory (UMI)
- 레이블: VLM 자동 캡션으로 state-transition prompt 생성
- 목표: open-world 조작 분포에서 다영역 조작 prior와 action chunk 생성 능력 학습

### Post-training

- 데이터: 약 `10K hours` cross-embodiment trajectory
  - `7.2K+` 내부 robot 로그
  - `1K+` instruction-labeled UMI 데이터
  - BridgeV2 / RT-1 / DROID 등의 공개 데이터 보강
- 목표: embodiment 정렬 + instruction 정합

### Downstream

- 테스트 task: phone packing, laundry loading, printer refilling, box packing
- 데이터: 36h / 144h 2개 데이터레벨
- 목적: foundation 정책의 data efficiency 확인

## Evaluation

| 축 | 핵심 지표 | 결과 요약 |
|---|---|---|
| pre-training scaling | 12.5/25/50/100% 데이터 구간 | 데이터 증가와 함께 validation action error 감소 추세
| model scaling | 2B / 5B / 10B | 모델 커짐에 따라 action prediction + 실환경 성공률 개선 |
| post-training OOD | shoe storage / bag packing / table organization / sofa tidying | 0% data pre-training 대비 100% data에서 성능(예: 26%→75% 구간) 개선 |
| downstream few-shot | 4개 hold-out task | 소량 데이터로도 baseline 대비 강한 적응력 |
| simulation | RoboCasa, RoboCasa365, VLABench, RoboDojo | RoboCasa365: 57.6%, RoboDojo: 20.07 달성 |

## Open-loop vs Closed-loop 해석

- Open-loop MSE 지표는 action imitation quality를 보여주며, 실시간 feedback의 한계를 가진다.
- 본 연구는 closed-loop real robot / simulation 평가를 함께 제시해 scaling gain이 실제 task 성능으로 이전됨을 보였다.

## 강점

- data scaling의 실증성: UMI 기반 100K+ hours가 유의미한 scaling 기반을 제공.
- language supervision의 정합성: state-transition 중심 설명으로 action grounding 신호를 구조화.
- embodiment transfer의 실질성: UMI 중심 pre-training을 실제 embodiment로 정렬.
- evaluation breadth: pre-training, OOD, downstream, simulation을 포괄.
- AD/VLA 설계 시사점: state transition language를 차량의 route/scene 변화 서술로 확장 가능한 설계 제시.

## 한계와 주의점

- manipuation 중심: 자율주행에는 traffic-rule, occupancy, safety constraint 반영이 추가 필요.
- 비용/컴퓨트: 100K+ h + billion-scale pre-training은 고가 자원 소요.
- auto-label 품질 의존: 언어 캡션 오류가 supervision noise로 증폭될 수 있음.
- safety/uncertainty 지표 미흡: collision, uncertainty calibration 부재.
- latency 상세 공개 부족: real-time 제어 loop에서 지연 특성 분석이 더 필요.

## 관련 비교

| 모델 | 포지션 |
|---|---|
| RT-1 | 대규모 real-robot transformer policy | Xiaomi-Robotics-1은 VLM + DiT, UMI 대규모 데이터, state-transition captioning을 결합 |
| pi0 / pi0.5 | instruction-conditioned VLA |
| DROID / Bridge | 공개 데이터 기반 정책 |
| World-action model | 미래 dynamics modeling 중심 |

Xiaomi은 `real trajectory + language transition + cross-embodiment post-training` 조합을 통해 파운데이션 정책의 실사용 전이를 강화한다.

## 핵심 takeaway

[[Xiaomi-Robotics-1]]의 메시지는 “데이터가 크고 깨끗할수록 모델도 커져야 한다”가 아니라, **real trajectory를 state-transition 언어로 정형화해 action-grounding 신호로 바꾸는 설계가 scaling의 효율을 높인다**는 점이다. 자율주행 설계에서는 이를 `언어로 표현된 장면/route transition` + continuous trajectory 생성으로 치환해 closed-loop 성능 이전을 검토할 수 있다.

## Connections
- [[Xiaomi-Robotics-1]] — 논문의 핵심 모델/프로젝트.
- [[UMI]] — 10K+ 시간급 trajectory 수집 핵심 데이터 인터페이스.
- [[Qwen3-VL]] — 시각-언어 표현 학습 뼈대.
- [[DiffusionTransformer]] — action chunk 생성기.
- [[StateTransitionCaptioning]] — supervision 설계의 핵심 기법.
- [[CrossEmbodimentLearning]] — UMI 기반 pre-training 능력의 실제 robot 전환 전략.
- [[RoboCasa365]], [[RoboDojo]] — 시뮬레이션 성능 검증 축.
- [[ActionChunking]] — control 단위 생성 관점의 실무 연결점.
- [[ActionGrounding]] — 지시문/상태 변화와 제어가 만나는 핵심 축.
- [[FlowMatching]] — action chunk 학습의 핵심 학습적 토대.

## Figure and Table Notes
- Figure: pre-training/post-training 파이프라인 다이어그램.
- Figure: 10K post-training 데이터 구성도.
- Table: data scaling/validation MSE 곡선.
- Table: OOD/simulation 및 downstream 성능 비교.

## Contradictions
- 없음. 기존 [[ScalingLaws]], [[VLA]], [[FoundationModels]] 서사와 충돌되는 주장은 현재 확인되지 않음.