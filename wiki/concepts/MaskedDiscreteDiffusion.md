---
title: "Masked Discrete Diffusion"
type: concept
tags: [diffusion, discrete-token, trajectory-generation, masked-denoising]
sources: ["reflectdrive-2-2605-04647"]
last_updated: 2026-05-13
---

# Masked Discrete Diffusion

[[MaskedDiscreteDiffusion]]은 categorical token space에서 parallel generation과 editing을 지원하는 diffusion 패러다임이다. 기존 continuous diffusion과 달리 Gaussian corruption process가 아닌 masked token을 confidence가 높은 순서대로 unmask하는 방식으로 동작한다.

## Driving Planningへの適用
ReflectDrive-2에서는:
- Future trajectory를 BEV coordinate token sequence로 discretize
- Full-mask sequence에서 시작해 confidence 높은 token부터 commit하는 parallel denoising
- Inference 비용은 trajectory token length가 아니라 denoising round 수에 의해 결정
- 어떤 trajectory token subset도 다시 rewrite 가능 → planning correction에 자연스러움

## Related Work Connections
- [[D3PM]], [[MaskGIT]], [[LLaDA]], [[SeedDiffusion]], [[MDLM]], [[SEDD]], [[BlockDiffusion]], [[Fast-dLLM]] 등 연구와 관련

## Connections
- [[ReflectDrive2]] — trajectory generation에 적용
- [[AutoEdit]] — 같은 discrete action space에서 동작하는 editor
