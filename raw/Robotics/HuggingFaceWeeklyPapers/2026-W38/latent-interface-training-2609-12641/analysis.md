---
title: "Latent Interface Training 분석"
source_url: https://arxiv.org/html/2609.12641
hf_url: https://huggingface.co/papers/2609.12641
arxiv_id: "2609.12641"
arxiv_url: https://arxiv.org/abs/2609.12641
pdf_url: https://arxiv.org/pdf/2609.12641
week: "2026-W38"
ingested_at_kst: "2026-09-16 09:40 KST"
selected_reason: "VLA/WAM visual shortcut과 OOD action grounding을 분석"
---
# Latent Interface Training 분석

## 한 문장 결론
LIT는 **image 없이 terminal pose로 action prior를 먼저 학습하고, pose reconstruction을 받는 latent token만으로 vision을 action expert에 전달**해 VLA/WAM의 visual shortcut을 줄인다.

## 문제·기여
- Visual feature가 task-causal signal과 우연한 scene correlation을 모두 담을 때 action expert는 shortcut을 학습할 수 있다.
- Stage 1은 language + robot state + terminal SE(3) pose에서 action chunk를 배우며 action generation을 pixel correlation에서 분리한다.
- Stage 2의 100 latent token은 semantic/visual representation을 모으되 terminal pose를 복원해야 한다. direct visual path는 허용하지 않는다.
- Pi0.5, MolmoAct2, FAST-WAM, ImageWAM의 VLA/WAM 4종에서 ID 성능을 보존하고 LIBERO-Plus OOD success를 3.87–10.70pt 높였다고 보고한다.

## input → reasoning/interface → action
| 구성 | 입력 | 중간 표현 | 출력 |
|---|---|---|---|
| Stage 1 | instruction, robot state, terminal pose | semantic + goal tokens | action chunk velocity/flow |
| Stage 2 | image, instruction, robot state | 100 pose-supervised latent tokens | 기존 VLA/WAM native action |
| Inference | image, instruction, robot state | latent interface | action chunk; pose는 미입력 |

```mermaid
flowchart LR
 I[Image] --> V[Visual backbone features]
 L[Language + robot state] --> S[Semantic features]
 V --> Z[Latent tokens: visual cross-attention]
 S --> Z
 Z --> P[Pose reconstruction loss]
 Z --> A[Pretrained action expert]
 G[Terminal SE(3) goal: training only] --> AP[Stage-1 action prior]
 AP --> A
```

## Training recipe
- Stage 1: 3-layer GELU MLP로 \(g_t=[p,r,q]\in\mathbb R^8\)를 goal token으로 만들고 image 없이 native flow-matching/action loss를 학습한다.
- Stage 2: action expert를 stage-1 checkpoint에서 초기화하고, layerwise semantic·visual cross-attention으로 latent token을 갱신한다. pose reconstruction과 native action objective를 함께 쓴다.
- MolmoAct2 비교에서 LIT는 stage 1 10K + stage 2 20K step으로 baseline과 같은 30K-step budget을 사용한다.

## 평가와 해석
- **Open-loop?** 아니다. LIBERO task success는 rollout 결과이므로 closed-loop manipulation evaluation이다. 다만 이는 simulation/robot manipulation이며 autonomous-driving closed-loop safety metric과 동일하지 않다.
- **ID:** 네 architecture 모두 average success가 유지 또는 증가했다.
- **OOD:** 카메라 viewpoint·sensor noise가 특히 개선되어 shortcut 저감 가설을 뒷받침한다. language shift는 모든 model에서 개선되지 않아 language grounding은 별도 문제다.
- **실물:** 3 manipulation task 및 lighting/camera/distractor shift에서 확인했지만, 대규모 장기 과업·더 다양한 embodiment로의 외삽은 아직 검증 대상이다.

## 강점·한계·배포
- **강점:** backbone/action head 전체를 새로 설계하지 않는 framework-agnostic interface다. spatial goal을 두 stage에 공통으로 써 action-relevant bottleneck을 정의한다.
- **안전:** nuisance scene에 대한 안정성은 manipulation accident risk 감소에 도움될 수 있으나, contact dynamics/force, OOD object physics, failed grasp recovery를 보장하지 않는다.
- **latency:** 100 token 및 layerwise attention은 interface overhead를 만든다. 논문은 실시간 control latency를 중심 metric으로 보고하지 않았으므로 target robot의 control period에서 profiling이 필요하다.
- **AD 관련성:** 카메라/BEV feature를 waypoint·trajectory decoder에 direct-concatenate하는 driving policy에서도 동일한 shortcut 문제가 가능하다. 다만 terminal end-effector SE(3) 대신 route-progress/waypoint/vehicle-state goal을 어떻게 설계할지가 핵심 변환 과제다.
