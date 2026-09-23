---
title: "THAW-VLA 참고 레퍼런스"
document_type: korean-references
source_url: https://arxiv.org/html/2609.24682
hf_url: https://huggingface.co/papers/2609.24682
arxiv_id: "2609.24682"
arxiv_url: https://arxiv.org/abs/2609.24682
pdf_url: https://arxiv.org/pdf/2609.24682
week: "2026-W39"
ingested_at_kst: "2026-09-23 09:40:29 KST"
selected_reason: "world model/VLA representation transfer 계보를 정리한다."
---

# THAW-VLA 참고 레퍼런스

Semantic Scholar `ARXIV:2609.24682/references`와 원문 References에서 THAW-VLA의 teacher, world-action-model, VLA transfer 맥락을 잇는 자료를 골랐다.

1. **Fast-WAM: Do World Action Models Need Test-time Future Imagination?** (2026), [arXiv:2603.16666](https://arxiv.org/abs/2603.16666) — WAM의 미래 imagination을 실제 control에서 어떻게 사용할지 묻는다. THAW-VLA는 rollout을 하지 않고 representation만 transfer한다는 반대 설계 선택을 한다.
2. **Do World Action Models Generalize Better than VLAs? A Robustness Study** (2026), [arXiv:2603.22078](https://arxiv.org/abs/2603.22078) — world-action model과 VLA robustness를 직접 비교한다. THAW의 “world-model prior가 VLA robustness를 보완한다”는 가설을 평가할 배경이다.
3. **Light-WAM: Efficient World Action Models with State-Fusion Action Decoding** (2026), [arXiv:2606.08242](https://arxiv.org/abs/2606.08242) — WAM의 efficiency를 개선하는 경로. THAW는 WAM 자체를 빠르게 하기보다 teacher로 쓰고 student를 유지한다.
4. **Cosmos 3: Omnimodal World Models for Physical AI** (2026), [arXiv:2606.02800](https://arxiv.org/abs/2606.02800) — THAW가 사용하는 Cosmos3-Nano teacher 계열의 physical-AI world-model 배경이다.
5. **OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation** (2026), [arXiv:2605.06481](https://arxiv.org/abs/2605.06481) — object-centric controllability와 robustness를 world-action model로 다룬다. 어떤 teacher representation이 manipulation에 유용한지 비교할 수 있다.
6. **Being-H0.7: A Latent World-Action Model from Egocentric Videos** (2026), [arXiv:2605.00078](https://arxiv.org/abs/2605.00078) — egocentric video로 latent world-action representation을 학습한다. THAW의 hidden feature target과 직접적으로 관련된다.
7. **VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models** (2026), [arXiv:2603.22003](https://arxiv.org/abs/2603.22003) — VLA input representation/interface 설계를 다룬다. THAW가 student action interface는 바꾸지 않고 latent supervision만 추가하는 점을 대비할 수 있다.
8. **S2-VLA: State-Space Guided Vision-Language-Action Models for Long-Horizon Manipulation** (2026), [arXiv:2606.27872](https://arxiv.org/abs/2606.27872) — long-horizon VLA에 state-space guidance를 준다. representation guidance가 planning horizon에 미치는 영향을 비교할 후보이다.
9. **ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining** (2026), [arXiv:2606.17200](https://arxiv.org/abs/2606.17200) — VLA pretraining data source를 확장한다. THAW의 cached teacher target을 대규모 heterogeneous data에 적용할 때 데이터 관점 참고가 된다.
