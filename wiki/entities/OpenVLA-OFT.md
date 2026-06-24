---
title: "OpenVLA-OFT"
type: entity
tags: [VLA, robot-manipulation, fine-tuning]
sources: [tbd-vla-2606-07895, nvidia-omnidreams-2606-03159, policytrim-2606-22540, policytrim-2606-22540-analysis]
last_updated: 2026-06-24
---

OpenVLA-OFT는 OpenVLA 계열 fine-tuning/speed optimization baseline이며, VLA action generation latency와 deployment efficiency 비교에 자주 등장한다. TBD-VLA 맥락에서는 action generation latency 비교 대상으로, PolicyTrim에서는 RL post-training을 적용해 action chunk utilization과 speedup을 검증한 backbone 중 하나로 다뤄졌다.

## Connections

- [[OpenVLA]] — 상위 open-source VLA 계열.
- [[ActionDecoding]] — VLA action output과 연결.
- [[PolicyTrim]] — intrinsic policy efficiency 개선 framework.
- [[ActionChunk]] — PolicyTrim이 최적화하는 action sequence 단위.
