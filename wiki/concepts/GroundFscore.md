---
title: "GroundFscore"
type: concept
tags: [vla, shortcut-learning, evaluation, counterfactual]
sources: [perturbot-2610-04616-paper-ko, perturbot-2610-04616-analysis, perturbot-2610-04616-learning]
last_updated: 2026-10-07
---

# GroundFscore

[[PerturBot]]의 offline evidence-use diagnostic입니다. correct action이 유지되어야 하는 null edit에서의 spurious response $R_c$와 known expert action delta 방향으로 바뀌어야 하는 causal edit에서의 sensitivity $S_c$를 측정합니다. 둘을 [0,1]로 clip한 뒤 harmonic mean으로 결합합니다.

$$GF_c=\frac{2S_c(1-R_c)}{S_c+(1-R_c)}$$

input을 완전히 무시하면 null-edit stability는 높아도 causal sensitivity가 0이라 GF는 0입니다. 모든 edit에 움직이면 spurious response가 커집니다. 따라서 robustness와 responsiveness를 함께 요구합니다.

## Measurement Contract

- normalized full action chunk에서 비교하며 paired forward pass는 같은 flow noise를 사용합니다.
- reference-action norm floor와 near-zero expert delta exclusion을 적용합니다.
- causal target delta는 matched-state expert recordings에서 얻습니다.
- real robot task SR, long-horizon success, formal safety certificate와 구별합니다.
- HF abstract에는 GroundingFscore, full paper에는 GroundFscore로 표기되어 있어 full-text 이름을 채택했습니다.

## Connections

- [[VisionActionShortcut]] — action accuracy와 task evidence 의존도의 차이.
- [[LatentInterfaceTraining]] — interface intervention과 data/metric intervention의 비교.
- [[MotorMind]] — runtime verification은 offline evidence-use 진단과 상보적입니다.

## Sources

- [[perturbot-2610-04616-paper-ko]] — 식과 experimental protocol.
- [[perturbot-2610-04616-analysis]] — offline/closed-loop boundary와 한계.
- [[perturbot-2610-04616-learning]] — paired edit·normalization·noise 구현 원칙.
