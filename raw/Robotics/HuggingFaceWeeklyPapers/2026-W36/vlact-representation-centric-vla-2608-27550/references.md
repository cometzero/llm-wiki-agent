---
title: "VLAct 참고 문헌: VLA backbone·action head·cross-embodiment transfer"
document_type: references
source_url: https://arxiv.org/html/2608.27550
hf_url: https://huggingface.co/papers/2608.27550
arxiv_id: "2608.27550"
arxiv_url: https://arxiv.org/abs/2608.27550
pdf_url: https://arxiv.org/pdf/2608.27550
week: "2026-W36"
ingested_at_kst: "2026-09-02 09:40:54 KST"
selected_reason: "VLAct의 representation-centric continued pre-training 계보와 평가 anchor를 연결하기 위한 참고 문헌이다."
---

# VLAct 참고 레퍼런스 논문 요약

> Semantic Scholar `ARXIV:2608.27550/references` endpoint와 원문 bibliography를 교차 확인해, VLAct를 이해하는 데 직접적인 9개를 골랐다.

1. **StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing** — [arXiv:2604.05014](https://arxiv.org/abs/2604.05014)
   - VLAct가 기반으로 삼는 training codebase 계열이다. 논문 contribution은 새 action decoder보다 이 기반 위에서 backbone representation을 shaping하는 recipe라는 점에 있다.

2. **StarVLA-α: Reducing Complexity in Vision-Language-Action Systems** — [arXiv:2604.11757](https://arxiv.org/abs/2604.11757)
   - Qwen 계열 VLM과 VLA system 설계를 연결하는 관련 baseline이다. VLAct는 같은 계열 backbone을 더 좋은 initialization으로 만들 수 있는지 묻는다.

3. **π0.5: A Vision-Language-Action Model with Open-World Generalization** — Physical Intelligence, [project](https://www.physicalintelligence.company/blog/pi05)
   - 대규모 generalist VLA의 대표 비교점이다. VLAct는 proprietary-scale data만이 아니라 public-data representation recipe도 downstream adaptation을 크게 바꿀 수 있음을 주장한다.

4. **GR00T N1/N1.5: Open Foundation Models for Generalist Humanoid Robot Learning** — NVIDIA, [project](https://research.nvidia.com/labs/gear/gr00t-n1/)
   - Flow-matching motor module과 humanoid transfer의 중요한 anchor다. VLAct는 GR00T-style head를 multi-head supervision에 포함하고 RoboCasa-GR1에서 full-data GR00T-N1.6 baseline과 비교한다.

5. **ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning** — [arXiv:2602.11236](https://arxiv.org/abs/2602.11236)
   - action manifold를 이용한 industrial VLA baseline이다. VLAct의 LIBERO-Plus 비교는 backbone pretraining이 action architecture와 별개로 성능을 좌우할 수 있음을 보여 주려는 근거다.

6. **Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories** — [arXiv:2607.15330](https://arxiv.org/abs/2607.15330)
   - 대규모 real-world trajectory scaling의 대표 사례다. VLAct의 “Beyond Data Scaling”은 scale의 가치를 부정하지 않고, 같은 data budget에서 representation design이 독립 축임을 주장한다.

7. **RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies** — [arXiv:2607.04434](https://arxiv.org/abs/2607.04434)
   - 42 task의 broad policy evaluation/leaderboard를 제공한다. VLAct의 score 10.66·success 7.60%와 designated WAM 대비를 해석할 때 benchmark protocol과 leaderboard date를 확인해야 한다.

8. **VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models** — [arXiv:2512.22539](https://arxiv.org/abs/2512.22539)
   - long-horizon, safety를 포함한 VLA behavioral generalization 평가 anchor다. VLAct가 representation gain을 일반 task success 이상으로 주장하는 데 쓰인다.

9. **Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution** — [arXiv:2602.12684](https://arxiv.org/abs/2602.12684)
   - open VLA와 real-time execution을 연결한다. VLAct의 backbone recipe를 실제 배포에 쓸 때에는 multi-head training 성능뿐 아니라 downstream action head의 serving latency를 같이 평가해야 함을 상기시킨다.
