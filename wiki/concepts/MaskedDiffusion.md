---
title: "Masked Diffusion"
type: concept
tags: [diffusion, generative-model, discrete-diffusion]
sources: [reflectdrive-2-2605-04647-references]
last_updated: 2026-05-13
---

## Overview
Masked Diffusion은 토큰을 점진적으로 마스킹/언마스킹하여 데이터를 생성하는 discrete diffusion 패러다임이다. [[MaskGIT]], [[LLaDA]] 등 recent discrete LM에 적용되며, [[ReflectDrive-2]]는 이 접근법을 trajectory token generation에 활용한다.

## Key Properties
- Masking/unmasking schedule 기반 denoising
- Autoregressive generation보다 병렬 효율적
- Classifier-free guidance 적용 가능

## Connections
- [[ReflectDrive-2]] — trajectory token generation에 활용
- [[LLaDA]] — implementation reference
- [[MaskGIT]] — related masked generation approach
- [[DriveFine]] — driving domain 적용 선행 연구

## Contradictions
- None identified.
