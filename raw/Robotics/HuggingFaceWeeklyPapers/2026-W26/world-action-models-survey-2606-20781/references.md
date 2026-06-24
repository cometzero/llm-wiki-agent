---
title: "World Action Models: A Survey — 미래를 덜 꿈꾸고 행동을 더 잘하게 만드는 WAM 서베이 — references"
source_url: "https://arxiv.org/abs/2606.20781"
hf_url: "https://huggingface.co/papers/2606.20781"
arxiv_id: "2606.20781"
arxiv_url: "https://arxiv.org/abs/2606.20781"
pdf_url: "https://arxiv.org/pdf/2606.20781"
html_url: "https://arxiv.org/html/2606.20781"
week: "2026-W26"
ingested_at_kst: "2026-06-24 09:40:00 KST"
selected_reason: "현재 주(2026-W26) 후보 중 VLA와 world model의 경계를 직접 정리하고, World Action Model(WAM)을 action-facing predictive model로 정의해 VLA for AD/robotics 학습 로드맵에 기준 taxonomy를 제공한다."
---

# World Action Models: A Survey — 미래를 덜 꿈꾸고 행동을 더 잘하게 만드는 WAM 서베이 참고 레퍼런스 정리

> Semantic Scholar references API는 이번 실행에서 rate limit(429)로 사용할 수 없어, arXiv HTML 본문/표/분야 맥락에 등장하는 대표 축을 기준으로 레퍼런스를 정리했다.

## 1. Vision-Language-Action Models 일반

VLA는 vision/language context를 executable action으로 직접 변환한다. WAM survey는 VLA를 “현재에서 바로 action을 예측하는 policy”로 두고, WAM은 그 사이에 action-facing future를 넣는 계열로 구분한다.

## 2. Video World Models / Video Generation Models

Video diffusion 또는 autoregressive video model은 realistic future를 생성할 수 있지만, WAM 관점에서는 그 future가 action path에 연결되어야 한다. 단순 visual prediction benchmark는 control utility를 보장하지 않는다.

## 3. DriveDreamer / Drive-WM / OmniDreams 계열

Autonomous driving world model은 ego action에 따른 future scene을 생성하거나 closed-loop simulation을 지원한다. WAM taxonomy에서는 rendered future 또는 latent future를 planner/risk evaluator와 연결하는지 확인해야 한다.

## 4. VisualThink-VLA / TBD-VLA / ReflectDrive 계열

이 repo에 이미 정리된 VLA 논문들은 visual intermediate reasoning, diffusion action generation, discrete action correction 같은 방식으로 action grounding을 다룬다. WAM survey는 이들을 action-facing future/latent/reasoning의 관점에서 다시 비교하게 해준다.

## 5. Latent world model / action-conditioned latent dynamics

Latent-only WAM은 pixel rendering을 생략해 latency를 낮추지만, latent의 causal validity와 interpretability를 따로 검증해야 한다. 자율주행에서는 latent가 traffic participant state, lane topology, route goal을 충분히 보존하는지가 중요하다.

## 6. Action-scoring rollout / Model-predictive control

여러 candidate action을 rollout하고 future utility를 비교하는 방식은 classic MPC와 닮았다. WAM은 learned predictive substrate를 사용해 이 과정을 vision-language foundation model 시대에 재해석한다.

## 7. Evaluation papers for embodied/world models

WAM 평가는 visual fidelity, temporal consistency, causal consistency, closed-loop success, latency, safety를 함께 봐야 한다. 특히 AD에서는 open-loop prediction metric만으로는 deployment risk를 판단할 수 없다.

## 읽기 순서 제안

1. VLA4AD survey로 VA/VLA taxonomy 파악
2. DriveDreamer/OmniDreams로 AD world model 확인
3. VisualThink-VLA/TBD-VLA로 action generation 방식 비교
4. World Action Models survey로 rendered/latent/video-free WAM을 통합 정리
