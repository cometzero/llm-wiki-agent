---
    title: "Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement — learning guide"
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

# Object-Centric Residual RL 학습 노트

## 선수 지식
- Vision-Language-Action policy와 action chunking
- Behavior cloning / imitation learning failure
- TD3와 off-policy continuous control
- Sim-to-real transfer, domain randomization
- 6-DoF pose estimation, SAM2/FoundationPose

## 핵심 용어
| 용어 | 설명 |
|---|---|
| Residual RL | frozen base policy action 위에 corrective action을 더하는 RL |
| Object-centric observation | image 대신 task object pose 중심으로 구성한 state |
| Zero-shot sim-to-real | real-world 추가 학습 없이 simulation-trained policy를 배포 |
| Pose dropout | tracking failure를 가정해 pose component를 제거하는 robustness training |
| VLA self-improvement | residual-corrected rollout을 다시 SFT data로 써서 base VLA를 개선 |

## 핵심 수식
```text
s_t = [s_t^obj, s_t^prop, a_t^base]
a_t = a_t^base ⊕ π_res(s_t)
s_t^real = s_t^sim + η_t
```

의미: residual은 세상을 pixel로 다시 보지 않는다. base VLA가 낸 action과 object pose/proprioception을 보고 “조금 더 어디로 밀어야 하는가”만 학습한다.

## 단계별 설명
1. Real teleoperation으로 base VLA를 학습한다.
2. 같은 action sequence를 simulation에서 replay해 sim VLA를 만든다.
3. Sim VLA가 내는 base action을 residual RL의 입력에 포함한다.
4. Residual policy는 object pose와 proprioception을 보고 correction을 낸다.
5. Training 중 pose noise/dropout을 넣어 reality pose estimator의 오류를 모사한다.
6. Deployment에서는 real VLA action과 sim-trained residual correction을 합친다.

## Deployment Checklist
- Pose estimator confidence threshold를 둔다.
- Pose dropout fallback path를 반드시 구현한다.
- Residual correction magnitude를 safety bound로 clip한다.
- Base VLA가 완전히 틀린 task interpretation을 했을 때 residual이 해결할 수 없음을 감안한다.

## Study Questions
1. **왜 image-based residual보다 object-centric residual이 전이하기 쉬운가?**  
   simulation rendering과 real image의 domain gap을 피하고, pose라는 낮은 차원의 task-relevant variable만 보기 때문이다.
2. **Residual이 base VLA를 대체하지 않는 이유는?**  
   language grounding과 broad task interpretation은 base VLA가 이미 잘하고, residual은 precision/contact correction에 집중한다.
3. **자율주행에 비유하면?**  
   base VLA/AD planner trajectory 위에 surrounding agent, lane, obstacle pose 기반 residual safety controller를 얹는 구조와 유사하다.

## Reading Roadmap
- OpenVLA / π0.5로 VLA base model 이해
- ResFiT / ResiP로 residual policy refinement 이해
- FoundationPose / SAM2로 object-centric perception stack 이해
- 본 논문을 다시 읽으며 observation abstraction과 robustness training을 비교
