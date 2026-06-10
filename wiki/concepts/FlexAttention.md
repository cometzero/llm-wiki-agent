---
title: "Flex-Attention"
type: concept
tags: [attention, optimization, PyTorch]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# Flex-Attention

PyTorch의 flexible attention mechanism으로, causal masking 구현에 사용된다.

## OmniDreams에서의 사용
- [[Diffusion Forcing]]의 causal masking 구현
- Full video distribution의 autoregressive factorize 지원

## 장점
- Standard attention보다灵活的한 masking pattern
- Efficient한 streaming generation 가능

## Connections
- [[OmniDreams]] — 사용처
- [[DiffusionForcing]] — 응용
- [[KVCache]] — streaming 지원
