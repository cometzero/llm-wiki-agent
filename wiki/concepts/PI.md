---
title: "PI"
type: concept
tags: [VLA, flow-matching]
sources: [vlact-2608-27550-paper-ko, vlact-2608-27550-analysis]
last_updated: 2026-09-02
---

# PI

PI는 VLA latent와 condition된 continuous action chunk 사이의 vector field를 flow matching으로 학습하는 action-expert 계열이다. Noise에서 action으로 iterative transport하므로 one-shot regression보다 inference cost가 크지만 richer continuous distribution을 표현할 수 있다. [[VLAct]]는 [[OFT]] 및 [[GR00T]]와 함께 PI를 이용해 decoder lock-in을 줄이려 한다.
