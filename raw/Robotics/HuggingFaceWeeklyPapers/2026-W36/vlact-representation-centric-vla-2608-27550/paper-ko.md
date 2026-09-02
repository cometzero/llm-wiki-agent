---
title: "VLAct: 데이터 스케일링을 넘어선 표현 중심 VLA 지속 사전학습"
document_type: korean-technical-translation
source_url: https://arxiv.org/html/2608.27550
hf_url: https://huggingface.co/papers/2608.27550
arxiv_id: "2608.27550"
arxiv_url: https://arxiv.org/abs/2608.27550
pdf_url: https://arxiv.org/pdf/2608.27550
week: "2026-W36"
ingested_at_kst: "2026-09-02 09:40:54 KST"
selected_reason: "고정된 로봇 데이터 예산에서 VLM prior 보존·다중 action-head·교차 embodiment action semantics로 VLA 전이성을 높이는 최신 공개 연구다."
---

# VLAct: 데이터 스케일링을 넘어선 표현 중심 VLA 지속 사전학습

> 원문: Senqiao Yang 외, *Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models* (arXiv:2608.27550). arXiv HTML v1의 본문, 실험, 부록 핵심을 한국어 기술 번역·정리했다. 수십 개 baseline의 전수 표와 부록의 모든 구현 세부는 압축했으나, 방법·주요 수치·한계는 보존했다.

## Abstract

일반형 Vision-Language-Action(VLA) 모델에 로봇 데이터의 규모를 키우는 일은 중요하지만, embodied trajectory는 수집 비용이 높고 물리 세계를 성기게만 덮으므로 웹 규모 image-text 자료처럼 늘리기 어렵다. 따라서 고정된 로봇 데이터 예산에서는 단순히 action을 맞히는 것보다, 제한된 trajectory로부터 전이 가능한 visual-action representation을 얻는 일이 병목이다.

저자들은 pretrained VLM에서 출발해 이질적 multi-embodiment robot data로 지속 사전학습하는 **VLAct**를 제안한다. 이 recipe는 (1) shallow layer 보호와 caption mixing으로 광범위한 VLM prior를 보존하고, (2) OFT·PI·GR00T의 multi-head continuous action co-supervision으로 특정 decoder에 representation이 고착되는 것을 막으며, (3) 물리적으로 대응되는 dimension만 공유하는 partially unified action layout으로 embodiment 간 action semantics를 정렬한다. Downstream fine-tuning에서는 task별 action head를 새로 붙일 수 있다.

VLAct는 LIBERO-Plus 82.6%, RoboTwin 2.0 92.5%를 보고하며, unseen humanoid GR-1에 대해 RoboCasa-GR1 downstream trajectory의 20%만으로 full-data GR00T-N1.6 baseline을 넘는다. 즉, VLA 진전은 데이터 규모만이 아니라 **표현을 어떻게 보존·정렬·다양화하는가**의 문제이기도 하다는 주장이다.

## 1. Introduction — 로봇 데이터가 만드는 다른 scaling 병목

웹 데이터는 광범위한 visual/semantic variation을 제공하지만 로봇 trajectory는 실제 embodiment 실행·teleoperation을 통해 얻어야 한다. scene, object, task goal, embodiment, contact dynamics의 조합 공간은 연속적이고 매우 크므로, 큰 robot dataset도 coverage가 불균일하다. 저자들의 질문은 “더 많은 trajectory가 필요한가?”가 아니라 **같은 예산의 trajectory가 reusable visual-action knowledge를 얼마나 잘 남기는가**이다.

Naive action-only continual training에는 세 가지 failure mode가 있다.

1. 좁은 robotics distribution으로 end-to-end update하면 web-scale VLM의 visual-language prior가 drift할 수 있다.
2. 한 action head의 supervision은 backbone을 그 decoder의 geometry에 맞추어, 다른 head로의 전이를 약화시킬 수 있다.
3. robot별 독립 action space는 gripper open/close 같은 공유 가능한 physical semantics까지 분리한다.

![그림 1: VLAct의 목표는 task·environment·embodiment·action head를 넘어 재사용되는 action-aware representation이다. arXiv HTML은 이 그림의 별도 raster 원본을 노출하지 않아 caption과 원문 링크를 보존한다.](https://arxiv.org/html/2608.27550)

## 2. Pilot study — action supervision은 중립적이지 않다

저자들은 Qwen3-VL-4B backbone을 고정하고 LIBERO-Plus/RoboTwin-Clean에서 pre-training head와 downstream head 조합을 바꾼다. Discrete FAST supervision은 continuous GR00T head로 어느 정도 transfer하지만, discretization 때문에 미세한 temporal/amplitude information을 잃는다. 반대로 continuous OFT supervision은 같은 OFT head에선 좋지만 PI·GR00T로 전이할 때 성능이 나빠질 수 있다.

이는 single-head continuous training이 더 좋은 “일반 action representation”을 만든다기보다, backbone feature를 해당 head가 읽기 쉬운 방향으로 **head-specific representation collapse/decoder lock-in**시킬 수 있음을 뜻한다. 따라서 좋은 VLA backbone은 특정 policy checkpoint가 아니라 서로 다른 action parameterization이 꺼내 쓸 수 있는 representation이어야 한다.

## 3. VLAct 방법

### 3.1 전체 recipe

지속 사전학습 단계에서는 pretrained VLM backbone에 robot trajectory와 caption data를 함께 넣고, 같은 backbone latent $z$에 여러 continuous action head를 붙인다. Fine-tuning 단계에서는 pre-training head와 caption stream을 버리고, target task/embodiment에 맞는 새 head를 초기화한다. 따라서 비교에서 바뀌는 것은 backbone representation이고, downstream data·optimizer·budget·head protocol은 맞춘다.

![그림 2: VLAct는 VLM prior 보존, multi-head continuous co-supervision, partial action-space unification을 지속 사전학습에만 사용하고 downstream에는 새 action head를 붙인다.](https://arxiv.org/html/2608.27550)

### 3.2 VLM prior 보존

**Shallow-layer protection.** Vision encoder 전체와 LLM lower half를 freeze하고 upper LLM layer/action head만 update한다. 초기 visual processing과 early vision-language alignment를 지키면서 upper layer가 action-conditioned reasoning에 적응하도록 한 것이다. Downstream에서는 full model을 unfreeze한다. 저자들의 ablation에서 full update 대비 LIBERO-Plus는 +3.7 points, RoboTwin 2.0은 +3.4 points 개선됐다.

**Caption-mixed training.** Robot sample과 auxiliary VLM sample을 함께 학습한다. 여러 auxiliary source 중 caption은 object, attribute, spatial relation, scene context에 대한 dense supervision을 주므로 VLM prior의 anchor로 가장 효과적이었다. 핵심은 “데이터를 더 넣는다”가 아니라 action-only gradient가 pretrained representation을 덮어쓰지 않도록 한다는 것이다.

### 3.3 Head-diverse continuous action co-supervision

OFT(parallel regression), PI(flow-matching), GR00T(flow-matching motor module) head가 같은 $z$와 ground-truth action chunk $a$를 본다.

$$\mathcal L_{\mathrm{multi}}=\sum_{h\in\{\mathrm{OFT,PI,GR00T}\}}\lambda_h\mathcal L_{\mathrm{action}}^{(h)}(a,z).$$

여러 decoder bias를 동시에 만족하려면 backbone은 한 head에만 유용한 feature에 의존할 수 없다. Head마다 backbone forward를 반복하지 않으므로 추가 비용은 주로 경량 head 계산이다. OFT는 한 번에 continuous chunk를 회귀해 빠르지만 point estimate이고, PI/GR00T는 noise에서 action으로 flow를 적분해 richer distribution을 나타내는 대신 inference cost가 더 든다.

### 3.4 Embodiment 간 partially unified action space

Fully unified action space는 서로 다른 kinematics의 coordinate를 잘못 같은 의미로 정렬할 수 있고, 별도 head는 공유 가능 semantic을 숨긴다. VLAct의 20-D layout은 Franka 6-DoF delta end-effector, AgileX dual-arm absolute joint angles, gripper coordinate를 함께 담되, **공유 가능한 gripper dimension만 공유**하고 없거나 incompatible한 dimension은 mask한다.

Periodic joint angle에는 $[-\pi,\pi]$ canonical wrapping과 wrap-aware residual을 쓴다.

$$r=\operatorname{wrap}(\hat a-a),\qquad \mathcal L_{\mathrm{wrap}}=\lVert r\rVert_1.$$

따라서 $179^\circ$와 $-179^\circ$를 원시 regression처럼 멀다고 벌주지 않는다. 이 loss는 absolute joint dimension에만 적용하며 translation/gripper에는 적용하지 않는다.

## 4. Experiments

### 설정과 데이터

Base VLM은 Qwen3-VL-4B이며, 공개 DROID, InternData-A1, RoboCoin, MolmoAct와 caption data를 사용한다. Main continual pre-training은 16 GPU에서 수행된다. Franka에는 7-D(delta end-effector 6 + gripper 1), AgileX에는 14-D(두 팔 absolute joint 12 + gripper 2) native action convention을 유지하면서 shared layout을 쓴다.

### Benchmark 결과

| 평가 | 무엇을 보는가 | 보고된 VLAct 결과 | 해석 |
|---|---|---:|---|
| LIBERO-Plus | camera/robot/noise/layout/instruction perturbation | 82.6% | Qwen3VL-OFT 75.0%보다 +7.6 points |
| RoboTwin 2.0 | dual-arm clean/random generalization | OFT 92.5% clean, 90.8% random | clean-only fine-tuning에도 randomized scene에 강함 |
| VLA-Arena | behavioral generalization 11 suites | 54.8% | long-horizon·safety axis의 개선을 보고 |
| DOMINO | dynamic manipulation | SR 18.50, MS 34.20 | moving object/temporal change에 대한 action representation 검사 |
| RoboCasa-GR1 | unseen humanoid transfer | 20% data에서 49.5%, full 54.0% | full-data GR00T-N1.6 47.6%를 넘는다고 보고 |
| RoboDojo | 42 ARX X5 sim tasks | score 10.66, success 7.60% | 35 policy 중 success 6위 snapshot |

실제 Franka Research 3 실험에서는 short-horizon single arm 92.5% 대 77.5% baseline, dual-arm 평균 72.0% 대 44.0% baseline을 보고한다. Long-horizon table cleaning/scoop-beans 및 unseen object에서도 더 높은 success를 보였지만, 각 task 10 rollout의 제한된 physical evaluation이라는 점은 함께 해석해야 한다.

## 5. 결론과 한계

VLAct는 VLA 지속 사전학습을 단순 action fitting이 아닌 representation engineering으로 재정의한다. VLM prior를 보존하고, action decoder 다양성으로 head lock-in을 줄이며, 부분적 embodiment alignment로 shared physical semantics를 전달한다. 공개 data와 16 GPU라는 조건에서도 industrial system과 경쟁할 수 있다는 점이 재현성 측면에서 의미 있다.

다만 연구는 4B backbone에 집중했으며, 더 큰 VLM에서 최적 freeze 범위·data mixture·head diversity가 같을지는 알 수 없다. Benchmark success는 실제 장기 deployment의 safety를 직접 보장하지 않는다. Heterogeneous data의 action convention·teleoperation quality·contact failure, action head의 latency/energy, unseen embodiment의 kinematic safety는 production에서 별도 validation과 safety shield가 필요하다. Dense numeric tables와 부록의 모든 data-cleaning implementation은 이 번역에서 요약했고 원문 Appendix를 병행해야 한다.
