---
title: "LLaDA"
type: entity
tags: [language-model, discrete-diffusion, text-generation]
sources: [reflectdrive-2-2605-04647-references]
last_updated: 2026-05-13
---

## Overview
LLaDA(Language Large Discrete Diffusion Model)는 Meta의 discrete diffusion language model 시리즈이다. [[ReflectDrive-2]]는 이 discrete diffusion LM 아키텍처를 driving domain에 적용하여 trajectory token generation에 활용한다.

## Variants
- [[LLaDA2.0]] (2512.15745) — 100B 스케일링 및 serving optimization
- [[LLaDA2.1]] (2602.08676) — token-to-token editing 아이디어

## Connections
- [[ReflectDrive-2]] — discrete trajectory token 생성에 LLaDA 아키텍처 활용
- [[MaskGIT]] — related masked token generation approach
- [[MaskedDiffusion]] — paradigm category

## Contradictions
- None identified.
