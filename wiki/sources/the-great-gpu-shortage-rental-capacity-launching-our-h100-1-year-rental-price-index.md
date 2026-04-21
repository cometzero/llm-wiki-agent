---
title: "The Great GPU Shortage – Rental Capacity – Launching our H100 1 Year Rental Price Index"
type: source
tags: [ai-infrastructure, compute, gpu, rental-market, nvidia, inflation]
date: 2026-04-20
source_file: raw/Nvidia/LilysAI/the-great-gpu-shortage-rental-capacity-launching-our-h100-1-year-rental-price-index.md
last_updated: 2026-04-20
sources: [the-great-gpu-shortage-rental-capacity-launching-our-h100-1-year-rental-price-index]
---

## Summary
이 문서는 [[SemiAnalysis]]가 공개한 [[H100]] 1년 렌탈 가격 지수를 바탕으로 AI 컴퓨팅 인프라 공급 제약이 지속되며 가격이 단기적으로 하향하지 않고 오히려 상승하는 구조적 국면에 진입했음을 설명한다. 급증한 [[AI]] 모델 수요, 메모리 가격 상승, 그리고 멀티 에이전트 중심의 토큰 소비 확대가 결합해 {{H100}}를 포함한 고성능 [[GPU]] 공급이 제한되고 있다는 점을 보여준다.

또한 시장은 단순 스팟 가격만으로 설명되지 않으며, 단기 온디맨드/스팟, 중기 1~3년, 장기 4~5년 오프테이크 계약이라는 계약 구조로 나뉘어 있으며, 특히 장기 계약 시장이 가격 형성과 공급 배분의 핵심 축으로 작동한다. 결론적으로, 공급 축소와 수요 탄력성 강화가 맞물려 [[AIInfrastructure]] 비용 압력과 투자 수익률 프레임(ARR/토큰 경제/IRR) 모두를 자극하는 구조라는 점이 핵심이다.

## Key Claims
- [[H100]] 1년 렌탈 가격은 2025년 10월 최저치 대비 2026년 3월 약 40% 상승하여 $1.70/hr에서 $2.35/hr/GPU로 뛰었다.
- [[Anthropic]]의 [[ClaudeOpus46]], [[ClaudeCode]] 수요 확대, Neolabs·OpenAI 등 투자자본 증가가 시장 수요를 끌어올리는 주요 동인으로 묘사되었다.
- DRAM/NAND 가격의 급등, 부품·코로케이션·가스 터빈 등 공급망 비용 상승이 서버 조달을 어렵게 하며 GPU 렌탈 가용성을 더 축소한다.
- 온디맨드 및 기존 단기 용량은 대부분 매진되었고, 기존 계약자들은 가격 인상에도 용량 반납을 꺼리는 경향이 보여 교착된 수요의 징후가 강화되었다.
- 블랙웰 계열([[Blackwell]]) 배포도 발주 리드타임 연장과 초기 예약 완판으로 추가 완충이 어렵고, 향후 추가 GB300 중심 램프업이 수요를 얼마나 상쇄할지가 핵심 모니터링 포인트다.
- 멀티 에이전트 워크플로우와 토큰 소비 확대가 가장 강력한 수요 동인으로 제시되며, 이는 AI 도구의 고ROI가 가격 조정의 완충제로 작동하지 못함을 강화한다.
- GPU 렌탈은 단기(온디맨드/스팟), 중기(3개월~3년), 장기(4~5년)로 구분되며, 가격·위험 노출·자금조달 조건이 계약 유형별로 크게 다르다.
- 장기 오프테이크는 대규모 AI 연구소의 조기 용량 선점과 하이퍼스케일러 재판매를 통해 가격 안정성(반면 고정 비용 부담)과 수익성 개선을 동시에 높이는 구조다.
- 시장 심리는 여전히 공급 과잉 기대를 과대해석하는 반면, 실제 현장은 희소성(용량 고착)과 가격 결정력이 공존한다는 점에서 수요-가격 반응의 이중 구조를 보인다.

## Key Quotes
> "H100 1년 렌탈 가격은 2025년 10월 최저 $1.70/hr/GPU에서 2026년 3월 $2.35/hr/GPU로 거의 40% 급등했다."

> "온디맨드 GPU 렌탈 용량은 모든 GPU 유형에서 매진되었고, 기존 계약자들은 가격 인상에도 용량을 반납하지 않고 있다."

> "토큰 수요 곡선의 우상향 이동은 GPU 렌탈 가격을 상승시키는 강력하고 상대적으로 비탄력적인 힘을 제공한다."

> "대부분의 GPU 렌탈이 가치 기준으로 거래되는 계약 시장은 경제적으로 더 중요하며, 1년 계약은 긴축 장면을 가장 빠르게 반영한다."

> "현재로서는 가격 하락보다 추가 상승 가능성이 더 높다." 

## Connections
- [[SemiAnalysis]] — H100 렌탈 가격 지수 공개 및 시장 모니터링을 수행한 주체.
- [[NVIDIA]] — [[H100]], [[H200]], [[B200]], [[Blackwell]]의 공급 측면에서 핵심 제조사 축.
- [[H100]] — 가격 지수의 중심이 되는 GPU.
- [[AIInfrastructure]] — 메모리·서버·코로케이션·전력까지 포괄하는 비용 압력의 중심축.
- [[ClaudeOpus46]] — 수요 급증의 대표적 촉발 요인으로 제시됨.
- [[ClaudeCode]] — 고집중 사용 사례의 대표로 반복적으로 언급된 도구.
- [[OpenAI]] — 컴퓨팅 투자 경쟁에서 주요 수요측 항목으로 언급.
- [[Neocloud]] — 렌탈 공급·계약 구조 중심의 시장 주체.
- [[CoreWeave]], [[Nebius]], [[IREN]] — 시장 정서가 부정적이나 가격은 계속 경직되는 환경의 대표 기업군.
- [[Runpod]], [[Lambda]] — 단기 탄력성 시장에서 온디맨드/스팟을 운영하는 공급 측면의 플레이어.
- [[GPURentalMarket]] — 본 자료에서 정리된 가격·수요·계약 구조 전체를 설명하는 개념적 축.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.