---
    title: "Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — Korean technical translation"
    source_url: "https://arxiv.org/abs/2606.18953"
    hf_url: "https://huggingface.co/papers/2606.18953"
    arxiv_id: "2606.18953"
    arxiv_url: "https://arxiv.org/abs/2606.18953"
    pdf_url: "https://arxiv.org/pdf/2606.18953"
    week: "2026-W27"
    category: "raw/Robotics/HuggingFaceWeeklyPapers"
    ingested_at_kst: "2026-07-01 09:40:38 KST"
    selected_reason: "Vision-Language-Action 정책의 real-world robustness와 zero-shot sim-to-real residual RL을 직접 다루는 신규 VLA 논문."
    ---

# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — 한국어 기술 번역

> 원문: arXiv:2606.18953 / Hugging Face Weekly 2026-W27  
> 번역 범위: Abstract, Introduction, Related Work, Method, Experimental Setup, Results, Limitations, Appendix 핵심을 깊게 번역·재구성했습니다. dense appendix table과 reward 세부 수치 전체는 요약했습니다.

## Abstract 번역

Vision-Language-Action (VLA) model은 다양한 manipulation task에 일반화할 수 있지만, imitation learning 기반 policy는 정밀한 물리 상호작용에서 execution error가 누적되어 취약하다. 그렇다면 simulation에서만 학습한 reinforcement learning policy가 real-world VLA의 robustness를 zero-shot으로 높일 수 있을까? Frozen VLA 위에 corrective policy를 학습하는 residual RL은 자연스러운 해법이지만, 기존 방법은 sim-to-real dilemma를 겪는다. Privileged-state method는 배포를 위해 손실 있는 distillation이 필요하고, image-based method는 visual domain gap에 약하며, real-world RL은 비용과 safety risk가 크다.

저자들은 VLA action을 object pose로 보정하는 **object-centric residual RL** framework를 제안한다. Compact object-centric observation space는 simulation과 reality 사이에서 일관되게 전이된다. 또한 동일한 teleoperation demonstration을 simulation에서 replay해 real-world VLA와 paired sim VLA를 함께 학습한다. Residual RL policy는 pose noise injection과 dropout을 포함해 simulation에서만 학습되고, real robot으로 zero-shot transfer된다. FR3 robot의 5개 manipulation task에서 평균 success rate가 42%에서 76%로 향상되며, residual-corrected rollout은 추가 teleoperation 없이 base VLA self-improvement에도 재사용된다.

## 1. Introduction 번역

VLA model은 대규모 pretraining과 robot demonstration을 활용해 broad manipulation capability를 얻는다. 그러나 imitation learning은 distribution shift와 compounding error에 취약하다. 작은 grasp offset, 접촉 force mismatch, 약간의 pose error가 긴 horizon에서 실패로 누적된다. RL은 recovery behavior를 학습할 수 있지만, diffusion/flow/action-chunk 기반 modern VLA에 직접 RL을 적용하기는 어렵다.

Residual RL은 base policy를 freeze하고 그 위에 작은 corrective action을 더한다. 장점은 base VLA의 generalization을 유지하면서 precision을 보완할 수 있다는 점이다. 하지만 residual이 어떤 observation을 보느냐가 sim-to-real transfer를 좌우한다. Simulator privileged state는 현실에서 얻기 어렵고, image observation은 rendering gap에 취약하다. 이 논문은 task-relevant object의 6-DoF pose, robot proprioception, base VLA action으로 residual observation을 구성한다. 이 정보는 simulation과 reality 양쪽에서 비교적 안정적으로 얻을 수 있어 zero-shot transfer의 bridge가 된다.

## 2. Related Work 번역

Residual RL은 behavior cloning이나 hand-designed controller 위에 corrective policy를 얹는 오래된 아이디어다. 최근 ResFiT, ResiP 등은 imitation policy refinement에 residual RL을 사용하지만, privileged state를 쓰거나 real-world adaptation이 필요하다. Sim-to-real transfer는 domain randomization, digital twin, real-world feedback 등으로 접근되어 왔지만, VLA policy의 visual domain gap과 dense robot interaction을 동시에 해결하기 어렵다. 이 논문은 image를 residual observation에서 제거하고 object-centric pose로 압축해 domain gap을 줄인다.

## 3. Method 번역

전체 pipeline은 세 단계다.

1. **Paired Sim/Real VLA via Teleoperation Replay**: real robot teleoperation demonstration으로 real VLA를 학습하고, 동일 action sequence를 MuJoCo simulation에서 replay해 sim VLA를 학습한다. 두 VLA는 같은 demonstration target을 공유하므로 유사한 failure mode를 갖게 된다.
2. **Object-Centric Residual RL**: sim VLA의 base action 위에 residual policy를 학습한다. residual observation은 object 6-DoF pose, proprioception, base action이다.
3. **Zero-Shot Deployment**: real VLA와 sim-trained residual을 freeze한 채 real robot에 적용한다. Pose estimator confidence가 낮으면 pose dropout으로 residual 입력을 안정화한다.

결합 action은 다음처럼 이해할 수 있다.

```text
a_t = a_t^base ⊕ π_res(s_t)
s_t = [s_t^obj, s_t^prop, a_t^base]
```

`⊕`는 base VLA action chunk에 residual correction을 더하는 operator다. `s_t^obj`는 task-relevant object pose, `s_t^prop`는 proprioception, `a_t^base`는 현재 VLA action이다.

## 3.2 Zero-shot transfer condition

논문은 reality observation이 simulation observation에 noise가 더해진 형태로 근사될 수 있으면 zero-shot transfer가 가능하다고 본다.

```text
s_t^real = s_t^sim + η_t,  η_t ~ P_η
```

따라서 training에서 position/orientation noise와 pose dropout을 주입해 residual이 pose-estimator error와 tracking failure에 견디도록 만든다. Position은 mm 단위 noise, orientation은 small random rotation noise로 perturb한다. Pose confidence가 낮은 deployment step에서는 해당 pose component를 dropout하여 잘못된 correction을 줄인다.

## 3.3 Reinforcement Learning

Residual policy는 TD3로 학습한다. Base VLA는 `H=16` action chunk를 생성하고, residual은 timestep마다 base action을 보정한다. Dense shaped reward는 reach, grasp, carry, place, lift 등 task stage별로 설계된다. 핵심은 residual이 full task를 처음부터 다시 푸는 것이 아니라, base VLA가 거의 맞지만 precision/contact에서 실패하는 영역을 보정한다는 점이다.

## 4. Experimental Setup 번역

평가는 MuJoCo simulation과 real Franka Research 3 robot에서 수행된다. Task는 Cube Lift, Pick-and-Place, Stack Cube, Close Drawer, Stand Plate의 다섯 가지다. Pose tracking은 FoundationPose + SAM2를 사용한다. Baseline으로 base VLA, image-based residual, privileged-state/distillation 계열, 그리고 다른 VLA backbone(π0.5)을 비교한다.

## 5. Results 번역

Main result는 real robot average success rate가 base VLA 42%에서 residual 적용 후 76%로 오른다는 것이다. 모든 task에서 향상되며, simulation에서만 학습한 residual이 real robot으로 zero-shot transfer된다. Ablation은 pose dropout과 noise injection이 모두 중요함을 보인다. Image-based residual은 visual sim-to-real gap 때문에 성능이 낮고, privileged-state distillation은 teacher-to-student loss가 발생한다. Object-centric design이 가장 안정적으로 transfer된다.

Residual intervention 분석에서는 base action이 goal 방향과 어긋날 때 residual vector가 goal 방향으로 correction을 제공하고, base가 이미 잘 맞을 때는 작게 개입한다. 또한 residual-corrected rollout을 SFT data로 재사용하면 base VLA 자체도 self-improvement된다.

## 6. Figures / Tables 번역 메모

- 그림 2: `figures/figure-02.png` — Figure 2: Overview of the object-centric residual RL pipeline.
- 그림 3: `figures/figure-03.png` — Figure 3: Real (top) and simulated (bottom) environments for all five evaluation tasks.
- 그림 4: `figures/figure-04.png` — Table 1: Success rates in simulation and real-robot. Simulation results are reported as mean ± \pm standard deviation over 3 seeds.
- 그림 6: `figures/figure-06.png` — Figure 4: Success rates across 3-seed training in simulation. Shaded regions denote standard deviation.
- 그림 7: `figures/figure-07.png` — Table 2: Ablation studies on real-robot performance (successes / 20 trials). (a) Robustness training: pose dropout and noise injection both contribute; combined training yields the strongest sim-to-real transfer. (b) Observation space: object-centric poses transfer best by avoiding the visual domain gap.
- 그림 9: `figures/figure-09.png` — Figure 5: The residual corrects the base action toward the goal when misaligned.
- 그림 10: `figures/figure-10.png` — Figure 6: (a) Performance improvement on π 0.5 \pi_{0.5} [ 27 ] , demonstrating compatibility with different VLA backbones. (b) Sim-to-real transfer across observation spaces; the object-centric design transfers most effectively. (c, d) SFT on residual-corrected rollouts improves success rate and reduces episode length.
- 그림 11: `figures/figure-11.png` — Figure 7: (a) Cosine similarity between the residual action and the goal direction, conditioned on base action alignment. The residual corrects more strongly when the base deviates. (b) Episode length comparison between base and residual-corrected policies (success episodes). The residual consistently reduces completion time by 9 9 – 22 22 %. Error bars denote standard error of the mean across timesteps (a) and episodes (b).

## 7. Limitations 번역

방법은 real-time 6-DoF pose tracking에 의존한다. FoundationPose + SAM2가 full occlusion, clutter, specular reflection에서 실패하면 residual이 잘못된 방향으로 correction할 수 있다. 또한 task-relevant object를 현재는 사람이 지정해야 한다. Open-world deployment에서는 VLA attention map이나 scene parser로 relevant object를 자동 선택해야 한다. Object-centric pose는 visual domain gap을 줄이지만 dynamics gap, friction, gripper compliance 차이는 여전히 남는다.

## 8. Conclusion 번역

Object-centric residual RL은 VLA policy를 simulation-only RL로 강화하고 real robot에 zero-shot 적용할 수 있음을 보인다. 핵심 통찰은 residual policy가 image가 아니라 simulation/reality 모두에서 recoverable한 object pose와 proprioception, base action을 보게 만드는 것이다. 이 설계는 VLA의 generalist ability를 유지하면서 precision interaction과 recovery를 보완한다. 자율주행 VLA로 일반화하면, base planner trajectory 위에 object/lane/agent-centric residual safety correction을 얹는 방식으로 읽을 수 있다.

## 번역상 생략·주의

- Appendix의 reward table, MuJoCo geometry 설정, 모든 hyperparameter table은 핵심만 요약했습니다.
- arXiv HTML에서 추출 가능한 그림은 `figures/`에 저장했습니다. 일부 표는 이미지/HTML 혼합이라 캡션과 핵심 수치만 본문에 반영했습니다.
