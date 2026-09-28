---
title: "EMIB-T, HBM4 Challenges, Microfluidic Cooling, Photonic Interconnects"
origin: lilys_ai
lilys_project_id: 10381159
lilys_project_url: "https://lilys.ai/digest/10381159"
lilys_created_at: "2026-07-03T10:18:14.708Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "12116044"
sources:
  - id: "11143875"
    url: "https://newsletter.semianalysis.com/p/ectc2026"
    title: "EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More"
    status: "done"
---

# EMIB-T, HBM4 Challenges, Microfluidic Cooling, Photonic Interconnects

## LilysAI note

> AI 가속기 패키징 기술의 최신 동향은 무엇인가? 트랜지스터 밀도 스케일링의 한계에 도달하면서 **고급 패키징이 AI 가속기의 성능 향상을 위한 핵심 동력**이 되었으며, EMIB-T, 커스텀 HBM, 마이크로플루이딕 쿨링, 포토닉 인터커넥트 등 다양한 혁신 기술들이 등장하고 있습니다.

## 1. AI 가속기 패키징 기술의 최신 동향
트랜지스터 밀도 스케일링의 한계에 도달하면서 고급 패키징이 AI 가속기의 성능 향상을 위한 핵심 동력이 되었으며, EMIB-T, 커스텀 HBM, 마이크로플루이딕 쿨링, 포토닉 인터커넥트 등 다양한 혁신 기술들이 등장하고 있다.

### 1.1. 인텔 EMIB-T 기술
인텔은 ECTC에서 EMIB-T 기술을 주요하게 발표했으며, 이는 TSMC의 CoWoS 플랫폼에 대한 가장 신뢰할 수 있는 대안으로 평가된다.
1. **EMIB-T의 발전 및 로드맵**
   1. EMIB-T는 기존 EMIB에 TSV(Through-Silicon Vias)를 추가한 차세대 기술이다.
   2. 더 조밀한 범프 피치, 더 큰 패키지, 온-브릿지(on-bridge) 기능이 포함된다.
   3. 구글의 TPU v9에 사용될 것으로 예상된다.
2. **범프 피치 스케일링**
   1. 인텔은 2배 레티클 크기의 실리콘 콘텐츠를 가진 패키지에서 36/35 µm 범프 피치를 검증했다.
   2. 이는 Granite Rapids에 사용된 45 µm 피치보다 감소한 것으로, 범프 밀도가 65% 증가한 것이다.
   3. 36/35 µm 범프 피치 검증은 4.5배 레티클 실리콘 패키지로 확장 중이며, 2026년 말까지 인증을 목표로 한다.
   4. 다음 단계로 25 µm 범프 피치 테스트가 진행 중이며, 두 개의 1레티클 실리콘 다이가 3mm × 18mm EMIB-T 브릿지를 통해 연결된다.
   <img alt="EMIB-T 스케일링 테스트 차량" src="https://substackcdn.com/image/fetch/$s_!yoyO!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a97662-ae09-465d-8158-5ce6575b930d_703x487.jpeg" caption="2배 레티클 실리콘 콘텐츠를 가진 EMIB-T 스케일링 테스트 차량. 상단 SEM 이미지는 110, 55, 36 µm 혼합 범프 피치를 보여준다. 출처: Intel, “Scaling the EMIB-T Advanced Packaging Technology to Address the Future HPC/AI Demand,” ECTC 2026">
   <img alt="EMIB-T 25 µm 범프 피치 테스트 차량" src="https://substackcdn.com/image/fetch/$s_!hVyk!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92a920f5-dc12-4595-8831-b1dcfbf62715_740x377.jpeg" caption="두 개의 1레티클 실리콘 다이가 3mm × 18mm 브릿지로 연결된 EMIB-T 25 µm 범프 피치 테스트 차량. SEM 단면은 조립 후 범프 및 비아 구조를 보여준다. 출처: Intel, “Scaling the EMIB-T Advanced Packaging Technology to Address the Future HPC/AI Demand,” ECTC 2026">
3. **대형 EMIB-T 패키지**
   1. 인텔은 최대 240mm × 240mm 크기의 쿼터 패널 패키지를 실용적인 목표로 제시했다.
   2. 이는 약 67개의 레티클 면적에 해당한다.
   3. 그러나 전시된 샘플에서 심각한 뒤틀림이 관찰되었으며, 이는 대형 패키지에서 기판 처리, 뒤틀림, 오버레이, 패널 레벨 패터닝이 주요 제약이 됨을 시사한다.
   4. 인텔은 대형 기판에서 오버레이를 충분히 정밀하게 유지하기 위해 고급 리소그래피 접근 방식을 평가 중이다.
   <img alt="인텔의 240mm × 240mm 쿼터 패널 EMIB-T 테스트 차량" src="https://substackcdn.com/image/fetch/$s_!wX3w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F299aff21-4041-42e2-ae83-3c05eb18f8b2_1003x889.jpeg" caption="인텔의 240mm × 240mm 쿼터 패널 EMIB-T 테스트 차량. 출처: Intel, “Scaling the EMIB-T Advanced Packaging Technology to Address the Future HPC/AI Demand,” ECTC 2026">
4. **EMIB-T 브릿지 기술**
   1. EMIB-T는 기존 EMIB보다 훨씬 복잡하며, TSV, 더 많은 금속층, 전력 메시, MIM(Metal-Insulator-Metal) 커패시터 층을 추가하여 고밀도 신호와 수직 전력 공급을 모두 지원한다.
   2. 인텔은 4개의 라우팅 층과 M1 및 M2 사이에 MIM 커패시터가 포함된 10개 금속층의 단면을 공개했다.
   <img alt="라우팅, 전력 메시, TSV 및 MIM 층이 있는 EMIB-T 스택업" src="https://substackcdn.com/image/fetch/$s_!BGJZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb9576ca-1e39-4224-a393-75db5798a624_1081x486.jpeg" caption="라우팅, 전력 메시, TSV 및 MIM 층이 있는 EMIB-T 스택업. 출처: Intel, “Enabling 12+Gb/s HBM4E with EMIB-T Advanced Packaging Technology,” ECTC 2026">
5. **전력 공급 개선**
   1. EMIB-T의 "T"는 TSV를 의미하며, 이는 전력 공급을 담당한다.
   2. 기존 EMIB에서는 브릿지 외부 영역에서 수직으로 전력이 공급되었지만, EMIB-T는 브릿지 내 TSV를 통해 직접 전력을 공급하여 전류 경로 거리를 크게 줄인다.
   3. 인텔은 이러한 TSV를 통해 DC 전압 강하를 68-80% 줄일 수 있다고 주장한다.
   <img alt="기존 EMIB와 EMIB-T를 사용한 패키지 DC 전압 강하" src="https://substackcdn.com/image/fetch/$s_!a3Cz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0572fc1a-629c-4747-bd10-4bfb8b71a8b2_912x563.jpeg" caption="기존 EMIB와 EMIB-T를 사용한 패키지 DC 전압 강하. 출처: Intel, “Enabling 12+Gb/s HBM4E with EMIB-T Advanced Packaging Technology,” ECTC 2026">
6. **HBM4E 지원**
   1. HBM4E는 신호 밀도와 전력 공급을 동시에 확장해야 하므로 구현이 어렵다.
   2. HBM4는 HBM3 대비 핀 수가 두 배로 늘어나고, PHY에 VDDQ 및 VDDQL과 같은 추가 전력 레일이 필요하다.
   3. 인텔은 모든 HBM 채널을 동일하게 라우팅하지 않고, 가장 긴 신호 경로를 더 깨끗한 라우팅 층에 배치하여 누화 및 삽입 손실을 최소화했다.
7. **온-브릿지 커패시터**
   1. EMIB-M에서 도입된 MIM(Metal-Insulator-Metal) 커패시터가 EMIB-T에서도 M1과 M2 사이에 사용된다.
   2. 인텔은 500 nF/mm²의 정전 용량 밀도를 공개했으며, 이는 인텔 18A MIM과 유사하다.
   3. 이러한 온-브릿지 커패시터는 브릿지 MIM 커패시터가 없는 EMIB-T 패키지 대비 전력 공급 네트워크(PDN) AC 임피던스를 82% 이상 개선한다.
   <img alt="브릿지 MIM 커패시터 유무에 따른 HBM4E용 EMIB-T 패키지 PDN AC 임피던스" src="https://substackcdn.com/image/fetch/$s_!3d2h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F433907f7-ee5e-4cc8-9ab6-2db4f980c201_898x615.jpeg" caption="브릿지 MIM 커패시터 유무에 따른 HBM4E용 EMIB-T 패키지 PDN AC 임피던스. 출처: Intel, “Enabling 12+Gb/s HBM4E with EMIB-T Advanced Packaging Technology,” ECTC 2026">
8. **신호 성능 시뮬레이션**
   1. 인텔은 HBM4E를 사용한 EMIB-T 시뮬레이션에서 12Gb/s 속도에서 수신기 이퀄라이제이션 없이 약 67% UI(Unit Interval) 아이 너비를 달성했다.
   2. 1탭 DFE(Decision Feedback Equalizer)를 사용하면 72.5%로 개선된다.
   3. 12.8Gb/s, 14Gb/s, 16Gb/s의 더 높은 속도에서도 UI 아이 너비는 60% 이상을 유지했다.
   <img alt="DFE 유무에 따른 12Gb/s HBM4E EMIB-T 채널의 신호 성능" src="https://substackcdn.com/image/fetch/$s_!jOcF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28ef0ff4-b4d0-48fb-80cb-30ba03f2b7d1_1051x470.jpeg" caption="DFE 유무에 따른 12Gb/s HBM4E EMIB-T 채널의 신호 성능. 출처: Intel, “Enabling 12+Gb/s HBM4E with EMIB-T Advanced Packaging Technology,” ECTC 2026">
9. **EMIB 로드맵 및 경쟁사 비교**
   1. 인텔의 EMIB 로드맵에는 고밀도 온-브릿지 MIM 커패시터, 대형 고종횡비 브릿지 다이, 25 µm 미만 범프 피치, 액티브 브릿지, EMIB 다이 내장 전압 레귤레이터 등이 포함된다.
   2. 인텔은 또한 기판 코어 내장 딥 트렌치 커패시터(DTC) 개념과 2500 nF/mm² 이상의 eMIM-T 커패시터를 공개했지만, 아직 상용 제품에는 적용되지 않았다.
   3. EMIB-T는 TSMC의 CoWoS 플랫폼에 비해 여전히 뒤처져 있으며, TSMC는 이미 DTC/eDTC 통합을 배포했고 통합 전압 레귤레이터 및 액티브 로컬 실리콘 인터커넥트(LSI) 분야에서 더 앞서 있다.

### 1.2. 마벨 커스텀 HBM
마벨은 JEDEC 표준 HBM의 한계를 극복하기 위해 커스텀 HBM을 발표했으며, 이는 HBM 스택과 호스트 간의 인터페이스를 최적화하여 성능, 전력, 면적 효율을 개선한다.
1. **커스텀 HBM의 개념**
   1. 마벨은 2024년 산업 분석가 회의에서 커스텀 HBM을 발표했지만, 당시에는 기술적 세부 사항이 부족했다.
   2. Hot Chips 2025에서 커스텀 베이스 다이의 플로어플랜을 공개했으며, ECTC에서 패키지 레벨 세부 사항을 제공했다.
   <img alt="마벨 커스텀 HBM 요약 및 베이스 다이 플로어플랜" src="https://substackcdn.com/image/fetch/$s_!df9r!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d88155a-4e95-42fa-b1e0-11abf178e433_2186x1210.png" caption="마벨 커스텀 HBM 요약 및 베이스 다이 플로어플랜. 출처: Marvell, Industry Analyst Day 2024 and Hot Chips 2025">
2. **JEDEC 표준의 한계**
   1. JEDEC 사양은 HBM 스택과 호스트 간의 인터페이스를 고정하여 상호 운용성에는 좋지만, 전력, 성능 및 면적에는 불리하다.
   2. 호스트 ASIC은 표준 HBM PHY를 구현하고 표준화된 패드 배치 및 브레이크아웃 규칙을 가진 매우 넓은 병렬 인터페이스를 라우팅해야 한다.
   3. 패키지가 커지고 HBM 속도가 증가함에 따라 고정된 경계는 쇼어라인, 라우팅 밀도, 전력 공급 및 신호 무결성을 최적화하기 어렵게 만든다.
   <img alt="표준 HBM 대 커스텀 HBM 베이스 다이 및 호스트 플로어플랜" src="https://substackcdn.com/image/fetch/$s_!Qcul!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f766f4c-81af-44b6-9c6d-23161835443b_1179x662.png" caption="표준 HBM 대 커스텀 HBM 베이스 다이 및 호스트 플로어플랜. 출처: Marvell, “Marvell custom HBM routing and signal integrity analysis,” ECTC 2026">
3. **커스텀 HBM의 장점**
   1. 커스텀 HBM은 DRAM 코어 다이를 변경하지 않고, 최적화된 다이-투-다이 인터페이스를 가진 커스텀 베이스 다이를 고급 로직 공정으로 제작한다.
   2. 커스텀 베이스 다이는 HBM 컨트롤러, 관리 및 모니터링 기능, 커스텀 로직, 확장 인터페이스를 통합할 수 있다.
   3. 이를 통해 호스트 ASIC에서 HBM PHY 및 관련 로직에 할당되는 면적을 약 60% 줄여 컴퓨팅, 캐시 또는 I/O를 위한 공간을 확보할 수 있다.
   <img alt="JEDEC HBM4E 대 마벨 커스텀 HBM" src="https://substackcdn.com/image/fetch/$s_!3823!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdecd8e76-212e-4d62-a8f2-524de1823bc3_1179x662.png" caption="JEDEC HBM4E 대 마벨 커스텀 HBM. 출처: Marvell, “Marvell custom HBM routing and signal integrity analysis,” ECTC 2026">
4. **대역폭 및 라우팅 개선**
   1. 마벨의 예시에서는 1024개 채널에서 32Gb/s로 4.1TB/s에 도달하며, 이는 16Gb/s의 2048비트 JEDEC HBM4(E) 인터페이스와 동일하다.
   2. 커스텀 인터페이스는 인터포저 채널 길이를 6.5mm에서 1.5mm로 단축하여 라우팅을 용이하게 하고, 동일한 9개 라우팅 층과 2/2 µm 라인/스페이스(L/S)를 유지하면서 대역폭을 늘릴 수 있다.
   3. 마벨은 실리콘 인터포저 대신 유기 RDL(재배선층) 인터포저를 사용하여 패키징 비용을 절감한다.
   4. 유기 RDL은 실리콘 인터포저보다 L/S가 훨씬 거칠기 때문에 레이아웃이 어렵지만, 마벨은 맞춤형 차폐 및 라우팅 패턴을 사용하여 누화를 제어하면서 대역폭 밀도를 극대화한다.
5. **확장 인터페이스 및 엔비디아 페인만 GPU**
   1. 엔비디아는 GTC에서 페인만(Feynman) GPU가 커스텀 HBM을 사용할 것이라고 발표했으며, 이는 마벨과 유사한 이유로 대역폭 증가, 전력 감소, HBM 전용 가속기 다이 면적 감소를 목표로 한다.
   2. 커스텀 HBM은 표준 HBM 링크를 넘어 확장 인터페이스를 가능하게 한다.
   3. 베이스 다이는 보조 메모리 컨트롤러 역할을 하여 추가 메모리(예: 고용량 저대역폭 LPDDR 또는 2차 HBM)로 분산될 수 있다.
   4. 이는 AMD의 MI450 및 MI500 GPU와 같이 메모리 용량 확장을 위해 LPDDR을 지원하는 미래 GPU에 특히 중요하다.
   <img alt="엔비디아 루빈 GPU 웨이퍼" src="https://substackcdn.com/image/fetch/$s_!eBy-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fecc82d-aabe-4e46-9ff0-13cd758f41e4_1756x2246.png" caption="엔비디아 루빈 GPU 웨이퍼. 출처: TSMC, Computex 2026. 사진: SemiAnalysis">

### 1.3. 삼성 HBM 인터포저
삼성은 HBM4E의 증가하는 라우팅 복잡성과 전력 소비 문제를 해결하기 위해 8층 실리콘 인터포저와 초고밀도 커패시터(UHC)를 제안한다.
1. **HBM4E의 과제**
   1. HBM4E는 데이터 전송률을 12Gb/s 이상으로 높이고 I/O 핀 수를 두 배로 늘려 라우팅 복잡성을 증가시킨다.
   2. HBM4E는 HBM3E 대비 2배, HBM2 대비 5배의 인터포저 층이 필요할 수 있다.
   3. I/O 수 증가와 높은 데이터 전송률로 인해 전력 소비도 HBM3E 대비 86%, HBM2 대비 5.6배 증가할 것으로 예상된다.
   <img alt="HBM2에서 HBM4E로의 인터포저 및 전력 스케일링" src="https://substackcdn.com/image/fetch/$s_!Y3IU!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa938383f-7fdf-4c90-b9f3-60162f38fde3_355x350.png" caption="HBM2에서 HBM4E로의 인터포저 및 전력 스케일링. 출처: Samsung, “Advanced SI/PI Interposer Design Solution Enabling High-Performance HBM4e at up to 12Gbps,” ECTC 2026">
2. **8층 실리콘 인터포저**
   1. 삼성은 예상 요구 사항 대비 층 수를 20% 줄인 8층 실리콘 인터포저를 제안했다.
   2. 이 인터포저는 고속 신호를 차폐하기 위해 2개 신호/1개 접지(two-signal / one-ground)의 지그재그 배열을 사용하며, 층의 75%가 신호 라우팅에 할당된다.
   <img alt="2개 신호/1개 접지 라우팅을 위한 HBM4E용 8층 실리콘 인터포저 스택업" src="https://substackcdn.com/image/fetch/$s_!AltS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71bf59d1-7dd5-4b60-ae66-2bc3bcf31437_779x401.png" caption="2개 신호/1개 접지 라우팅을 위한 HBM4E용 8층 실리콘 인터포저 스택업. 출처: Samsung, “Advanced SI/PI Interposer Design Solution Enabling High-Performance HBM4e at up to 12Gbps,” ECTC 2026">
3. **초고밀도 커패시터(UHC)**
   1. 인터포저의 또 다른 핵심 요소는 UHC이다.
   2. UHC는 M1 층에만 배치될 수 있으며, 이 층은 신호 라우팅에도 많이 사용되므로 사용 가능한 면적이 제한된다.
   3. 라우팅이 불균형하면 커패시터가 인터페이스의 한쪽으로 밀려 로직 및 HBM 측면 간에 불균일한 PDN 동작을 유발한다.
   4. 삼성의 레이아웃은 UHC가 전체 인터페이스에 더 고르게 배치될 수 있도록 M1 및 다른 층에 라우팅을 재분배한다.
   5. 이는 라우팅 밀도를 관리하면서 PDN 임피던스와 전압 노이즈를 줄인다.
   <img alt="8층 실리콘 인터포저의 불균형 대 균형 커패시터 레이아웃" src="https://substackcdn.com/image/fetch/$s_!OX4T!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9574069-29e8-4e20-a975-0fd51f95fd54_1498x1160.png" caption="8층 실리콘 인터포저의 불균형 대 균형 커패시터 레이아웃. 출처: Samsung, “Advanced SI/PI Interposer Design Solution Enabling High-Performance HBM4e at up to 12Gbps,” ECTC 2026">

### 1.4. 삼성 HBM 하이브리드 본딩 열 관리
삼성은 HBM 스택의 열 관리 문제를 해결하기 위해 하이브리드 본딩(HCB) 기술을 연구하며, 이는 기존 열 압축 본딩(TCB) 대비 열 저항을 크게 개선한다.
1. **HBM 열 관리의 중요성**
   1. HBM 스택은 점점 더 빠르고 높아지며, 하단의 로직 다이도 더 많은 전력을 소비한다.
   2. 16단 HBM에서는 열 저항이 허용 가능하지만, 미래의 20단 및 24단 HBM에서는 새로운 접근 방식이 필요하다.
   <img alt="2.5D 패키지 열 저항 기여도" src="https://substackcdn.com/image/fetch/$s_!z_E5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43135bed-a06d-402c-a455-4b1cb75505de_1179x675.png" caption="2.5D 패키지 열 저항 기여도. 출처: Samsung, “System-Level Thermal Validation of 2.5D Packages in GPU Servers: Impact of TCB vs HCB HBM Platforms,” ECTC 2026">
2. **TCB 대 HCB 비교**
   1. 삼성은 엔비디아 블랙웰과 유사한 2개의 GPU 다이와 8개의 HBM 스택을 가진 2.5D GPU 패키지에서 TCB와 HCB를 비교했다.
   2. HCB는 공랭 시 내부 HBM 열 저항을 12.2%, 수랭 시 12.9% 감소시킨다.
   3. 전체 HBM 열 저항은 공랭 시 3.5%, 수랭 시 7.7% 감소한다.
   4. HCB는 열 네트워크의 일부만 해결하므로 개선 효과가 고르지 않다.
   5. 내부 저항과 누화는 각각 약 12.5%와 9.8% 감소하지만, 열 인터페이스 재료 및 냉각을 포함한 시스템 레벨 저항은 약 2.3% 증가한다.
   6. HBM 베이스 다이로 더 많은 전력이 이동함에 따라 열 병목 현상이 이동하며, GPU-HBM 누화는 전체 열 저항에서 차지하는 비중이 줄어든다.
   <img alt="공랭 및 수랭 조건에서 TCB 및 HCB를 사용한 삼성 HBM 열 저항" src="https://substackcdn.com/image/fetch/$s_!pzk2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F713b5b31-3764-44ba-aa58-73e6aea153d7_1179x675.png" caption="공랭 및 수랭 조건에서 TCB 및 HCB를 사용한 삼성 HBM 열 저항. 출처: Samsung, “System-Level Thermal Validation of 2.5D Packages in GPU Servers: Impact of TCB vs HCB HBM Platforms,” ECTC 2026">
   <img alt="베이스 다이 전력 증가에 따른 HBM 열 저항" src="https://substackcdn.com/image/fetch/$s_!ol4f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fece2b817-e007-400b-a7bf-50537019e4c5_1179x675.png" caption="베이스 다이 전력 증가에 따른 HBM 열 저항. 출처: Samsung, “System-Level Thermal Validation of 2.5D Packages in GPU Servers: Impact of TCB vs HCB HBM Platforms,” ECTC 2026">
3. **HCB의 이점**
   1. 삼성에 따르면 HCB로 전환하면 일정한 패키지 전력에서 입구 온도를 1-2°C 높이거나, 일정한 온도에서 패키지 전력을 약 4% 증가시킬 수 있다.
   2. 또한 냉각 전력은 약 7% 감소할 것으로 예상된다.
   3. 스택 레벨에서 HCB는 TCB 대비 스택 열 저항을 약 19% 감소시킨다.
   4. HCB 패드 밀도를 2배로 늘리면 22.3%, 4배로 늘리면 29.1%까지 감소 효과가 증가한다.
   <img alt="HCB의 다양한 패드 밀도(P.D.)를 사용한 TCB 및 HCB의 스택 레벨 열 저항" src="https://substackcdn.com/image/fetch/$s_!SXW1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12a2d5af-8638-4bb4-bfc3-ed5f4e989810_668x432.png" caption="HCB의 다양한 패드 밀도(P.D.)를 사용한 TCB 및 HCB의 스택 레벨 열 저항. 출처: Samsung, “System-Level Thermal Characterization of Hybrid Cu Bonded HBM on 2.5D Advanced Packaging,” ECTC 2026">

### 1.5. TSMC 및 마이크로소프트의 마이크로플루이딕 쿨링
TSMC와 마이크로소프트는 직접 실리콘 냉각 기술을 선보였으며, 이는 기존 냉각 방식의 한계를 뛰어넘는 고성능 패키지 열 관리를 가능하게 한다.
1. **TSMC의 마이크로필러 직접 실리콘 냉각**
   1. TSMC는 CoWoS-R 플랫폼에서 대형 GPU와 유사한 테스트 차량에 직접 실리콘 냉각 기술을 시연했다.
   2. CoWoS-R은 실리콘 인터포저 대신 유기 인터포저를 사용하여 뒤틀림 허용 오차와 공정 호환성이 더 좋다.
   3. 테스트 차량은 4개의 SoC 다이와 8개의 HBM 스택을 가진 3.3배 레티클 인터포저를 사용했다.
   4. TSMC는 기존 뚜껑 있는 냉각판 패키지, 뚜껑 없는 냉각판 패키지, 그리고 마이크로필러 직접 실리콘 냉각 디자인의 세 가지 접근 방식을 비교했다.
   5. 마이크로필러는 SoC 다이의 뒷면에 직접 형성되어 열원을 액체 냉각제에 훨씬 더 가깝게 가져온다.
   6. 기존 냉각 방식은 1-2 LPM에서 1.9-3.0 kW를 소산했지만, 마이크로필러 테스트 차량은 4 LPM에서 4 kW, 8 LPM에서 5.3 kW를 소산하며 더 높은 유량에서 성능이 우수했다.
   7. 마이크로필러는 CoW(Chip-on-Wafer) 공정 후 CoWoS-R 구조를 손상시키지 않고 형성해야 하며, 패키지 뒤틀림과 열팽창 불일치에도 불구하고 냉각제를 유지하기 위한 새로운 실란트 재료 개발이 필요하다는 단점이 있다.
   8. 테스트 차량은 MSL4(Moisture Sensitivity Level 4)를 통과했으며 헬륨 누출이나 실란트 박리가 없었다.
   <img alt="직접 실리콘 냉각 개념 및 CoWoS-R 테스트 차량" src="https://substackcdn.com/image/fetch/$s_!3Ndc!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1eb5f786-d103-4504-8f23-16f66a3843f3_709x434.jpeg" caption="직접 실리콘 냉각 개념 및 CoWoS-R 테스트 차량. 출처: TSMC, “Process Development and Thermal Characterization of Micropillar Direct-to-Silicon Liquid Cooling Solution on CoWoS-R Platform,” ECTC 2026">
   <img alt="열 방출을 위한 SoC 다이 뒷면의 실리콘 마이크로필러 형성" src="https://substackcdn.com/image/fetch/$s_!D_vu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84f9eee0-4e2d-4087-b4f1-8fdc167283fe_512x417.jpeg" caption="열 방출을 위한 SoC 다이 뒷면의 실리콘 마이크로필러 형성. 출처: TSMC, “Process Development and Thermal Characterization of Micropillar Direct-to-Silicon Liquid Cooling Solution on CoWoS-R Platform,” ECTC 2026">
   <img alt="뚜껑 유무 및 마이크로필러를 사용한 테스트 차량의 열 특성" src="https://substackcdn.com/image/fetch/$s_!ntj7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd14cf27-7fb2-405e-ae5b-48a15f83a6fe_1041x668.jpeg" caption="뚜껑 유무 및 마이크로필러를 사용한 테스트 차량의 열 특성. 출처: TSMC, “Process Development and Thermal Characterization of Micropillar Direct-to-Silicon Liquid Cooling Solution on CoWoS-R Platform,” ECTC 2026">
2. **마이크로소프트의 직접 실리콘 마이크로플루이딕 냉각**
   1. 마이크로소프트는 TSMC와 달리 GPU 실리콘에 직접 에칭된 직선형 마이크로채널을 사용했다.
   2. 실제 엔비디아 GH200 GPU에서 테스트하여 실제 열 분포 및 핫스팟을 더 정확하게 포착했다.
   3. HPCG 및 HPL과 같은 다양한 GPU 워크로드를 테스트하여 컴퓨팅 및 메모리 스트레스 특성을 분석했다.
   4. 1 LPM 유량에서 GPU의 접합부-입구 열 저항이 51-60% 감소했으며, HBM은 냉각판과 TIM을 통해 냉각되었기 때문에 27-37%만 개선되었다.
   5. 전체 패키지의 열 저항은 50% 감소했다.
   6. 6개월 동안 약 4370건의 관찰에서 9건의 잠재적 막힘 현상만 기록되었으며, 시간이 지남에 따라 발생률이 감소하여 초기 설치 후 안정화되는 경향을 보였다.
   7. 6개월 후에도 마이크로채널에서 측정 가능한 실리콘 침식은 없었다.
   8. GH200은 3주간의 반복 벤치마킹과 1주간의 안정적인 패키지 전력 연속 실행을 성공적으로 완료했다.
   <img alt="엔비디아 GH200용 마이크로소프트의 직접 실리콘 마이크로플루이딕 냉각 어셈블리" src="https://substackcdn.com/image/fetch/$s_!K0Rl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb790416-6dc1-4389-aae9-9d9b773e8a1b_699x200.jpeg" caption="엔비디아 GH200용 마이크로소프트의 직접 실리콘 마이크로플루이딕 냉각 어셈블리. 출처: Microsoft, “Direct to Silicon Microfluidic Cooling for Datacenters,” ECTC 2026">
   <img alt="GPU 워크로드 전반에 걸친 마이크로소프트 GH200 마이크로플루이딕 냉각 결과" src="https://substackcdn.com/image/fetch/$s_!Az1C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4d770f1-14c6-4c56-94f7-1212b5c2688b_2203x1349.png" caption="GPU 워크로드 전반에 걸친 마이크로소프트 GH200 마이크로플루이딕 냉각 결과. 출처: Microsoft, “Direct to Silicon Microfluidic Cooling for Datacenters,” ECTC 2026">

### 1.6. 마벨 광학 인터커넥트
마벨은 광학 멀티칩 인터커넥트 브릿지(OMIB)와 포토닉 패브릭(Photonic Fabric)을 통해 광학 인터커넥트 기술을 발전시키고 있으며, 이는 패키지 내 광학 연결의 효율성과 유연성을 높이는 데 중점을 둔다.
1. **광학 인터커넥트의 중요성**
   1. ECTC에서 광학 인터커넥트와 코패키징 광학이 주요 주제로 부상했다.
   2. 마벨은 Celestial AI 인수를 통해 OMIB 및 Photonic Fabric 기술을 확보했다.
   3. 멀티 레티클 포토닉 인터포저 제작은 수율 측면에서 어려움이 있으며, 기존 실리콘 인터포저의 고밀도 커패시터와 같은 기능을 제공하지 못할 수 있다.
2. **OMIB(Optical Multi-Chip Interconnect Bridge) 개념**
   1. 마벨의 접근 방식은 유기 RDL 인터포저에 필요한 부분에만 포토닉 집적 회로(PIC)를 내장하는 것이다.
   2. 광학 인터커넥트가 필요 없는 영역에서는 전기 브릿지를 사용할 수 있다.
   3. PIC가 RDL에 내장되면 그레이팅 커플러가 오버몰딩 후 막힐 수 있으므로, 마벨은 몰딩 전에 그레이팅 영역 위에 실리콘/유리 광학 블록을 배치하여 광학 경로를 유지한다.
   <img alt="EIC가 PIC 위에 쌓이고 유기 인터포저에 전기 브릿지가 내장된 OMIB 패키지 개념" src="https://substackcdn.com/image/fetch/$s_!RZsR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf199b53-e56e-4e81-ab1c-40ac08283250_909x275.png" caption="EIC가 PIC 위에 쌓이고 유기 인터포저에 전기 브릿지가 내장된 OMIB 패키지 개념. 출처: Marvell, “Optical Multi-Chip Interconnect Bridge (OMIB) Interposer Demonstration to Enable High-density Photonic Interconnects for High-Performance Computing Applications,” ECTC 2026">
3. **OMIB 테스트 차량**
   1. 마벨의 OMIB 테스트 차량은 하나의 주 XPU 다이와 6개의 EIC 다이를 포함한다.
   2. 인터포저에는 6개의 PIC, 6개의 전기 브릿지, 12개의 DTC 다이가 내장되어 있다.
   3. 약 2배 레티클 크기의 RDL 인터포저는 2/2 µm L/S의 4개 층을 사용한다.
   <img alt="PIC, 전기 브릿지 및 DTC 부착 후 OMIB 테스트 차량 플로어플랜 및 RDL 인터포저" src="https://substackcdn.com/image/fetch/$s_!22hJ!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F548cf302-eb15-482e-91e4-fdc6ea4009d5_708x593.png" caption="PIC, 전기 브릿지 및 DTC 부착 후 OMIB 테스트 차량 플로어플랜 및 RDL 인터포저. 출처: Marvell, “Optical Multi-Chip Interconnect Bridge (OMIB) Interposer Demonstration to Enable High-density Photonic Interconnects for High-Performance Computing Applications,” ECTC 2026">
4. **XPU-XPU 광학 인터커넥트**
   1. 마벨은 지연 시간과 홉 수를 줄이기 위한 광학 칩-투-칩 인터커넥트를 가진 개념적인 멀티 다이 XPU를 선보였다.
   2. OMIB는 동일한 브릿지가 온-패키지 다이-투-다이 링크와 외부 광학 인터커넥트를 모두 라우팅할 수 있으므로 쇼어라인 제약을 제거한다.
   3. 마벨은 이 접근 방식으로 1.8 Tbps/mm²의 대역폭 밀도를 주장한다.
   <img alt="XPU-XPU 인터커넥트 및 외부 FAU를 포함한 OMIB 개념" src="https://substackcdn.com/image/fetch/$s_!r1jx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ec27f4f-9295-4933-894e-013ee577c76a_631x650.png" caption="XPU-XPU 인터커넥트 및 외부 FAU를 포함한 OMIB 개념. 출처: Marvell, “Optical Multi-Chip Interconnect Bridge (OMIB) Interposer Demonstration to Enable High-density Photonic Interconnects for High-Performance Computing Applications,” ECTC 2026">
5. **OMIB 통합 공정 흐름**
   1. 마벨이 제시한 공정 흐름은 TSMC의 CoWoS-L과 유사한 칩-라스트(chip-last) 방식이다.
   2. 마벨은 내장 브릿지, OMIB PIC, DTC 및 기타 구성 요소를 포함하는 유기 RDL 인터포저를 제작하고, C4 범프를 통해 패키지 기판에 연결한다.
   3. 브릿지 TSV와 높은 구리 기둥이 RDL에 연결되고, ASIC 다이와 EIC는 마지막에 부착된다.
   <img alt="2.5D OMIB 통합 공정 흐름" src="https://substackcdn.com/image/fetch/$s_!aeNu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F831e1806-e179-4581-a0a0-9c63923e8343_699x613.jpeg" caption="2.5D OMIB 통합 공정 흐름. 출처: Marvell, “Optical Multi-Chip Interconnect Bridge (OMIB) Interposer Demonstration to Enable High-density Photonic Interconnects for High-Performance Computing Applications,” ECTC 2026">
6. **광학 엔진 패키지 개념**
   1. 단기적으로는 TSMC의 COUPE와 같은 수직 스택형 광학 엔진이 OMIB 스타일 연결이나 완전한 포토닉 인터포저보다 더 실현 가능하다.
   2. 마벨은 EIC와 PIC를 50 µm 피치의 마이크로범프로 연결한 다음, 결과 엔진을 패키지 기판 또는 인터포저에 장착한다.
   3. 기판 구성은 130 µm C4 피치의 UCIe-S와 유사한 병렬 버스를 사용할 수 있으며, 인터포저 구성은 40-45 µm 피치의 UCIe-A 인터페이스를 사용할 수 있다.
   4. 마벨은 단순성과 더 나은 열 절연성 때문에 기판 접근 방식을 선호한다.
   <img alt="기판, OMIB 및 포토닉 인터포저를 포함한 패키지 개념" src="https://substackcdn.com/image/fetch/$s_!0eyl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1184e6e9-21c3-45e3-8447-213a4589e392_1250x980.png" caption="기판, OMIB 및 포토닉 인터포저를 포함한 패키지 개념. 출처: Marvell, “Photonic Fabric™ Interconnect for a Scale-up Network Solution in Accelerated Computing,” ECTC 2026">
7. **광학 엔진 테스트 및 열 특성**
   1. 마벨은 5nm EIC(TSMC N5로 추정)를 사용하여 광학 엔진을 테스트했으며, 4개의 56Gb/s TX-RX 쌍으로 각 방향에서 224Gb/s를 제공한다.
   2. 이 디자인은 다른 회사들이 선호하는 마이크로링 변조기(MRM) 대신 전기 흡수 변조기(EAM)를 사용하며, 이는 더 나은 열 안정성과 넓은 작동 파장 범위를 제공한다.
   3. XPU 전체 부하에서 PIC 온도는 기판에서는 5°C 미만으로 상승했지만, 인터포저에서는 약 25°C, 브릿지에서는 약 20°C 상승했다.
   4. 유기 기판의 낮은 열전도율과 비교적 큰 밀리미터 규모의 공기 갭이 PIC를 격리한다.
   5. 열 과도 현상은 XPU 전력 상태 변경 후 약 30ms 이내에 발생한다.
   6. PIC는 유기 기판에서 약 10°C/s로 가열되는 반면, 브릿지에서는 약 100°C/s, 인터포저에서는 약 120°C/s로 가열된다.
   7. 마벨은 EAM 바이어스 전압을 이러한 변화에 충분히 빠르게 전자적으로 조정할 수 있다고 주장하며, 링 변조기는 더 느린 시정수에 의해 제약되는 히터-피드백 루프가 필요하다.
   <img alt="4개의 TX-RX 쌍을 가진 포토닉 패브릭 광학 링크 테스트 칩 EIC" src="https://substackcdn.com/image/fetch/$s_!ekF8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d42f8f6-fa47-4a02-9457-d42423bc299e_590x448.jpeg" caption="4개의 TX-RX 쌍을 가진 포토닉 패브릭 광학 링크 테스트 칩 EIC. 출처: Marvell, “Photonic Fabric™ Interconnect for a Scale-up Network Solution in Accelerated Computing,” ECTC 2026">
   <img alt="기판, 실리콘 인터포저 및 실리콘 브릿지에서 XPU 전체 전력 하의 PIC 정상 상태 온도 기울기" src="https://substackcdn.com/image/fetch/$s_!87DB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28d02464-a100-4e88-8a13-71d25c9f559c_853x446.png" caption="기판, 실리콘 인터포저 및 실리콘 브릿지에서 XPU 전체 전력 하의 PIC 정상 상태 온도 기울기. 출처: Marvell, “Photonic Fabric™ Chiplets for Co-Packaged Optics in AI Data Centers,” ECTC 2026">
   <img alt="기판, 실리콘 인터포저 및 실리콘 브릿지에서 PIC 과도 온도 상승" src="https://substackcdn.com/image/fetch/$s_!fTe-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3df60c85-3774-4405-aecf-40a7b728d777_716x406.png" caption="기판, 실리콘 인터포저 및 실리콘 브릿지에서 PIC 과도 온도 상승. 출처: Marvell, “Photonic Fabric™ Chiplets for Co-Packaged Optics in AI Data Centers,” ECTC 2026">

### 1.7. 라이트매터 Passage M1000
라이트매터는 Passage M1000의 광학 인터커넥트 및 제조 공정을 상세히 설명하며, 멀티 레티클 포토닉 인터포저와 ASIC 칩렛 통합의 패키징 결과를 제시한다.
1. **Passage M1000 아키텍처 및 제조**
   1. 라이트매터는 Passage M1000의 아키텍처와 광학 인터커넥트, 제조 접근 방식을 이전에 상세히 설명했다.
   2. ECTC에서는 멀티 레티클 포토닉 인터포저와 ASIC 칩렛 통합을 위한 조립 공정, 광섬유 부착 및 패키징 결과에 대해 더 깊이 있게 다루었다.
   3. 테스트 차량은 4개의 타일 M1000 인터포저에 15개의 ASIC 칩렛을 부착하기 위해 칩-온-웨이퍼(CoW) 조립을 사용한다.
   4. 인터포저는 약 2100 mm²로, Hot Chips 2025에서 보여진 4000 mm²의 8개 타일 구성의 절반 크기이다.
   <img alt="Passage M1000 개략도" src="https://substackcdn.com/image/fetch/$s_!t9kS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a99a955-ba9e-485a-8762-ac813c0e6d2a_652x750.jpeg" caption="Passage M1000 개략도. 출처: Lightmatter, “Advancing Interconnect Performance and Reliability with Innovations in 3D Photonic Integration Packaging and Fiber Coupling,” ECTC 2026">
2. **광학 및 전기 신호 경로**
   1. 4개의 각 타일에는 127 µm 피치의 32개 광학 도파관이 있다.
   2. 전기 신호와 전력은 기판에서 ASIC 칩으로 C4 범프(약 176 µm 피치), 2개의 후면 RDL 층, 126 µm 깊이의 10 µm 폭 TSV를 통해 이동한 후 마이크로범프를 통해 ASIC 칩렛에 도달한다.
   3. 약 2100 mm² 인터포저는 7200 mm² 유기 기판의 1/3 미만을 차지한다.
3. **패키지 뒤틀림 및 조립 수율**
   1. 이 크기의 실리콘 인터포저를 유기 기판에 부착하면 심각한 뒤틀림이 발생한다.
   2. 모듈은 260°C 리플로우 온도에서 약 59 µm, 실온으로 냉각 후 약 56 µm의 뒤틀림을 보였다.
   3. 118 µm 두께의 인터포저와 약 176 µm 피치의 C4 범프를 고려할 때, 이는 접합 형성에 영향을 줄 수 있는 수준이다.
   4. 라이트매터는 기판을 평평하게 유지하기 위해 자기 고정 장치를 사용했으며, 95% 이상의 전기 조립 수율을 보고했다.
   <img alt="온도 상승 및 냉각 중 Passage M1000 패키지 뒤틀림" src="https://substackcdn.com/image/fetch/$s_!-G4F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ef0cfb9-f088-4778-ae04-6f15db1f2c63_955x481.jpeg" caption="온도 상승 및 냉각 중 Passage M1000 패키지 뒤틀림. 출처: Lightmatter, “Advancing Interconnect Performance and Reliability with Innovations in 3D Photonic Integration Packaging and Fiber Coupling,” ECTC 2026">
4. **열 성능 검증**
   1. 라이트매터는 4개의 독립적으로 전원이 공급되는 사분면을 가진 열 테스트 칩을 사용했으며, 각 사분면은 170W를 소산했다.
   2. 이는 369 mm² 활성 영역에서 1.47 W/mm²의 전력 밀도를 초래했다.
   3. 이 전력에서 포토닉 인터포저는 25°C 냉각수가 1.8 LPM/kW로 흐를 때 약 100°C에 도달했다.
   4. 이는 900W 이상을 위해 설계된 패키지에서 집중된 테스트 칩 영역에서 680W를 냉각하는 것을 검증한다.
   <img alt="사분면당 170W에서 테스트 칩의 열 지도" src="https://substackcdn.com/image/fetch/$s_!qqhb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2f59b30-dbe5-4d4b-843b-e055e9fda221_748x477.jpeg" caption="사분면당 170W에서 테스트 칩의 열 지도. 출처: Lightmatter, “Advancing Interconnect Performance and Reliability with Innovations in 3D Photonic Integration Packaging and Fiber Coupling,” ECTC 2026">

## 2. 기타 주요 기술 동향
ECTC 2026에서는 하이브리드 본딩, 인터포저 대체 기술, 열 인터페이스 재료, 유리 기판, RDL 스케일링, 스택형 메모리 등 다양한 첨단 패키징 기술이 논의되었다.

### 2.1. 하이브리드 본딩
하이브리드 구리 본딩은 HPC 애플리케이션을 위한 가장 미세한 피치와 최고의 I/O 밀도를 제공하지만, 인터페이스를 평평하고 깨끗하게 유지하면서 본딩 온도를 낮추는 것이 과제이다.
1. **유기 유전체 활용**
   1. 미쓰이 화학(Mitsui Chemicals)과 ASE는 200°C에서 10 µm 피치의 무압력 Cu/폴리머 본딩을 시연했다.
   2. TOK와 NYCU는 150°C에서 10초 본딩 공정을 시연했으며, 200°C에서 본딩된 샘플은 신뢰성 테스트를 통해 안정적인 저항을 유지했다.
2. **미세 입자 구리 활용**
   1. 미세 입자 구리는 낮은 온도에서 구리 확산을 가속화하고, 이후 결정립 성장을 통해 전도도를 높인다.
   2. 인텔은 미세 입자 구리와 저온 유전체 스택을 결합하여 175°C 및 200°C 어닐링 후 균일한 웨이퍼 본딩을 달성했다.
   3. 전기 수율은 60% 수준이었지만, 테스트 차량 및 프로빙 한계로 인해 낮은 값으로 평가되었다.
   <img alt="175°C 및 200°C에서 어닐링된 미세 입자 Cu의 보이드 없는 C-SAM 본딩 맵" src="https://substackcdn.com/image/fetch/$s_!YdlA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0076e249-2fbb-4b5e-8d06-4aa0e562968a_2453x1008.jpeg" caption="175°C 및 200°C에서 어닐링된 미세 입자 Cu의 보이드 없는 C-SAM 본딩 맵. 출처: Intel, “Enabling Ultra Low Temperature Hybrid Bonding for D2W Scaling,” ECTC 2026">
3. **초미세 피치 본딩**
   1. Applied Materials와 EV Group은 2천만 개 링크 체인에서 98% 수율로 450nm 피치 웨이퍼-투-웨이퍼 본딩을 시연했다.
   2. CEA-Leti는 플라즈마 활성화 없이 100°C 어닐링 후 97% 이상의 수율을 달성했다.
4. **향후 전망**
   1. 피치와 본딩 온도를 줄이려면 구리, 유전체, CMP, 표면 준비 및 어닐링이 공동으로 최적화되어야 한다.
   2. 2027년부터 재료 공급업체 및 장비 공급업체의 지속적인 개선이 예상된다.

### 2.2. 인터포저 대체 기술
패키지 크기가 원형 실리콘 인터포저의 실용적인 한계를 넘어서면서, 인텔의 EMIB-T를 넘어선 인터포저 없는 통합 방식이 제안되고 있다.
1. **FO-EB(Fan-Out Embedded Bridge) 패키지**
   1. 인텔과 SPIL은 FO-EB 패키지의 내장 브릿지 층에 SRAM 칩렛을 배치하고, 25 µm 피치 마이크로범프를 통해 로직 다이에 수직으로 연결했다.
   2. 테스트 칩은 0.24 pJ/b에서 265 GB/s/mm² 이상의 성능을 달성했다.
   <img alt="내장 메모리 칩렛을 포함한 FO-EB의 개략적인 단면도" src="https://substackcdn.com/image/fetch/$s_!iLGS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ebd3c49-889d-4af1-89ea-019f60cc8dfe_658x149.png" caption="내장 메모리 칩렛을 포함한 FO-EB의 개략적인 단면도. 출처: Intel and SPIL, “3D Integration of an SRAM chiplet in Fan-Out Embedded Bridge Platform Achieving Low Energy Read/Write,” ECTC 2026">
2. **패널 스케일 유기 인터포저**
   1. 패널 스케일 유기 인터포저는 실리콘의 크기 제약을 우회하는 또 다른 방법이다.
   2. Resonac은 320mm × 320mm 패널에서 5 µm 마이크로비아 및 2/2 µm L/S를 포함한 건식 필름 내장 브릿지 인터포저의 개별 공정 모듈을 시연했다.
   3. ASE는 600mm × 600mm 패널에 RDL을 제작한 후, 기존 장비로 조립하기 위해 4개의 300mm × 300mm 패널로 분할했다.
3. **DBrM(Direct Bridge Multi-die) 패키지**
   1. IBM은 DBrM이라는 보다 국소적인 접근 방식을 사용했다.
   2. 칩렛은 가장자리를 따라 접합되어 30 µm 피치 실리콘 브릿지를 중심으로 기계적으로 견고한 서브어셈블리를 형성한다.
   3. 이 서브어셈블리는 굽힘 테스트에서 30N 이상의 강도를 견뎌냈으며, 이는 IBM의 이전 언더필 전용 구조의 0.2N보다 훨씬 높은 수치이다.
   <img alt="다이-엣지 접착 기술을 사용한 칩 재구성용 직접 브릿지 멀티 다이(DBrM) 패키지" src="https://substackcdn.com/image/fetch/$s_!XQB4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc3fed56-388d-4d8a-8aa2-53245beb7fa8_1456x1238.png" caption="다이-엣지 접착 기술을 사용한 칩 재구성용 직접 브릿지 멀티 다이(DBrM) 패키지. 출처: IBM, “Direct Bridge Multi-die (DBrM) Package: A Novel Silicon Bridge Chiplet Packaging Technology Using Die-Edge Gluing Technique for Chip Reconstitution,” ECTC 2026">
4. **인터포저 없는 실리콘 브릿지**
   1. Unimicron은 인터포저나 내장 브릿지가 필요 없는 더 간단한 구조를 모델링했다.
   2. 두 개의 칩렛이 하단에 장착된 얇은 실리콘 브릿지를 통해 연결되며, 기판에 직접 부착된다.
   3. Unimicron의 시뮬레이션은 칩렛과 브릿지 사이의 언더필이 마이크로범프 변형을 제어하는 데 필수적임을 보여준다.
   <img alt="인터포저 없이 실리콘 브릿지를 통해 연결된 칩렛" src="https://substackcdn.com/image/fetch/$s_!PEVW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44f35e4a-0ad4-4e2c-92b7-9928d73a018a_1584x993.png" caption="인터포저 없이 실리콘 브릿지를 통해 연결된 칩렛. 출처: Unimicron, “Silicon Bridges for Chiplets Heterogeneous Integration with Microbumps,” ECTC 2026">
5. **향후 전망**
   1. TSMC의 CoWoS-R 및 CoWoS-L은 원형 웨이퍼에 의해 제한되지만, 이러한 대안들은 패널 레벨 또는 재구성된 형식으로 통합을 전환하거나 인터포저를 완전히 제거한다.
   2. 향후 몇 년 내에 유사한 아키텍처가 ASIC에 나타날 것으로 예상된다.

### 2.3. 열 인터페이스 재료(TIM)
첨단 열 솔루션에서 TSMC와 파트너들은 TIM1을 완전히 제거하는 직접 실리콘 냉각을 주도하고 있지만, 대부분의 단기 시스템에서는 실리콘과 히트 스프레더 사이의 더 나은 재료가 여전히 필요하다.
1. **갈륨 기반 액체 금속 복합재**
   1. TSMC의 OSAT 파트너인 SPIL은 55mm × 55mm FO-EB 패키지에서 갈륨 기반 액체 금속(LM) 복합재, 실리콘 기반 HS-TIM, 탄소 섬유 HCF-TIM을 테스트했다.
   2. 측정된 전도도는 각각 5.7 W/m·K 및 10 W/m·K였으며, 둘 다 4 W/m·K의 상용 실리콘 TIM보다 낮은 열 저항을 보였다.
   3. HCF-TIM은 150°C에서 1000시간 후 95%의 커버리지를 유지한 반면, HS-TIM은 실리콘 매트릭스가 경화되고 부분적으로 박리되어 75%로 떨어졌다.
   4. 두 LM 기반 TIM 모두 기존 S-TIM 대비 열 저항을 감소시켰으며, HCF-TIM이 최고의 성능과 신뢰성을 제공했다.
   <img alt="액체 금속 HS-TIM 및 HCF-TIM의 열 성능 및 신뢰성" src="https://substackcdn.com/image/fetch/$s_!tg3K!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1d4cd7b-178a-4854-8d65-7c67ce521a20_1430x800.png" caption="액체 금속 HS-TIM 및 HCF-TIM의 열 성능 및 신뢰성. 출처: SPIL, “Reliability Assessment of Liquid Metal Alloy Thermal Interface Materials in Fan-Out Embedded Bridge (FO-EB) Packages,” ECTC 2026">
2. **나노결정 다이아몬드 내 Cu/Sn 마이크로범프**
   1. 퍼듀(Purdue), 아베이루 대학교(University of Aveiro), UCLA는 나노결정 다이아몬드에 Cu/Sn 마이크로범프를 내장하는 다른 접근 방식을 취했다.
   2. 결과적인 인터커넥트 층은 500~600 W/m·K의 유효 면내 열전도율을 달성했으며, 이는 기존 언더필 마이크로범프의 약 20배에 해당한다.
   3. 이 기술은 TIM1 대체가 아니라 3D 스택의 인터커넥트 층을 통해 열을 측면으로 확산시키는 방법이다.

### 2.4. 유리 기판
유리 기판은 여전히 SeWaRe(RDL 응력 하에서 다이싱된 유리 가장자리에서 시작되는 측면 균열) 문제를 해결해야 하지만, 코팅 및 재료 선택을 통해 신뢰성을 개선하고 있다.
1. **SeWaRe(Side-Wall-Edge) 문제**
   1. 조지아 공대(Georgia Tech)는 실험적으로 파손 특성을 분석했다.
   2. 코닝(Corning)은 유한 요소 분석(FEA), 페리다이내믹스 및 분석적 파괴 역학을 사용하여 균열 전파를 모델링했으며, 단단한 구리 층이 균열을 유리 중간면으로 유도하고 유연한 폴리머 층이 균열 경로를 변경함을 보여주었다.
   3. 코닝은 또한 낮은 CTE(열팽창 계수) 폴리머와 적절한 유리 선택이 파손 위험을 줄일 수 있음을 발견했다.
2. **조립 및 신뢰성 개선**
   1. STATS ChipPAC은 대형 유리 코어 패키지의 조립 및 신뢰성을 조사했다.
   2. 74mm × 74mm 유리 코어 패키지는 가장자리 코팅 없이는 모든 테스트 세그먼트에서 실패했지만, 가장자리 코팅된 패키지는 조립 및 신뢰성 테스트를 이상 없이 완료했다.
   3. 가장자리 코팅은 또한 코팅되지 않은 유리 코어 패키지 대비 뒤틀림을 33.5% 감소시켰다.
   <img alt="74 × 74mm 유기 및 유리 코어 테스트 차량 비교" src="https://substackcdn.com/image/fetch/$s_!1bC9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F419bb2c2-36c9-4873-873a-5428bbbd3ae1_838x575.png" caption="74 × 74mm 유기 및 유리 코어 테스트 차량 비교. 출처: STATS ChipPAC, “Assembly and Reliability Characterization of Glass-Cored Substrate Package for AI/HPC Applications,” ECTC 2026">
3. **인텔의 유리 코어 패널 시연**
   1. 인텔은 업계 최초로 510mm × 515mm, 24층 유리 코어 패널을 시연했으며, 구리로 채워진 TGV(Through-Glass Vias), 2개의 내장 EMIB 브릿지, TGV 사이에 공동 형성된 광학 도파관을 포함한다.
   2. 이 대형 프로토타입은 기존 유기 기판 라인에서 처리되었으며, 열충격 테스트 후 분리된 유닛에서 SeWaRe가 발생하지 않았다.
   <img alt="구리로 채워진 TGV, 내장 EMIB 브릿지 및 광학 도파관을 포함한 24층(10-2-10) 유리 코어 패널, 열충격 테스트 후 SeWaRe가 없는 분리된 유닛" src="https://substackcdn.com/image/fetch/$s_!U9rN!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F212d519a-a5f0-47ba-841b-c3b2ca6a69f9_422x221.png" caption="구리로 채워진 TGV, 내장 EMIB 브릿지 및 광학 도파관을 포함한 24층(10-2-10) 유리 코어 패널, 열충격 테스트 후 SeWaRe가 없는 분리된 유닛. 출처: Intel, “Glass Core Substrates – Next Generation Advanced Packaging Platform for AI and HPC,” ECTC 2026">
4. **OSAT 채택 및 과제**
   1. Amkor와 STATS ChipPAC은 더 얇은 유리 코어가 유기 참조 기판보다 30-40% 낮은 기판 레벨 뒤틀림을 보였지만, 조립 결함 및 TGV 충전 문제는 공정이 아직 미성숙함을 나타낸다.
   2. 유리 기판은 진전을 보이고 있지만, 아직 대량 채택보다는 제조 개발 단계에 있다.

### 2.5. RDL(재배선층) 스케일링
RDL L/S(라인/스페이스)는 패키지 크기가 커짐에도 불구하고 계속 축소되고 있으며, UCIe 3.0과 같은 고속 다이-투-다이 인터커넥트가 주요 동력이다.
1. **RDL 스케일링의 필요성**
   1. RDL L/S는 패키지 크기가 커짐에도 불구하고 계속 축소되고 있다.
   2. 주요 동력은 미래 ASIC-투-ASIC 및 ASIC-투-HBM 링크를 위해 최대 64 GT/s 속도를 지원하는 UCIe 3.0이다.
   3. 이러한 고속 다이-투-다이 인터커넥트는 유기 인터포저가 더 커지고 밀도가 높아짐에 따라 신호 무결성 요구 사항을 강화한다.
2. **기술 발전 및 목표**
   1. 로드맵은 2015년경 10/10 µm L/S에서 현재 2/2 µm로 발전했으며, 1/1 µm가 다음 목표이다.
   2. 서브마이크론 시대에 도달하려면 RDL 라우팅 아키텍처와 제조 공정 모두에 큰 변화가 필요하다.
   3. 공정은 세미-애디티브 도금에서 서브-2 µm 구리용 다마신(damascene)으로 전환되고 있으며, CMP 평탄화 및 저수축 유전체가 핵심 게이팅 단계가 된다.
3. **주요 연구 성과**
   1. Resonac은 320mm × 320mm 유리 패널에 2/2 µm 배선을 형성하기 위해 폴리머 다마신 및 패널 CMP를 사용했다.
   2. imec과 Fujifilm은 300mm 웨이퍼에서 다마신을 1/1 µm로 확장했다.
   3. Ushio는 스티칭 없이 18개 레티클 필드에서 1.5/1.5 µm L/S를 해결했으며, 16번의 노출로 510mm × 515mm 패널 전체를 커버했다.
   4. Sumitomo Bakelite과 조지아 공대는 200°C의 비교적 낮은 온도에서 4%의 경화 수축률을 가진 완전 이미드화 액체 유전체를 2/2 µm L/S로 시연했다.
4. **TSMC 및 GUC의 8층 RDL 스케일링**
   1. 가장 진보된 RDL 제조업체인 TSMC는 GUC와 협력하여 CoWoS-R 플랫폼의 단기 한계로 여겨지는 8층 RDL 스케일링에 대한 연구를 발표했다.
   2. GUC는 TSMC N3에서 제작되고 8층 CoWoS-R RDL에 통합된 64비트 UCIe-A 인터페이스를 위한 STCO(Space-Time Co-Optimization) 기반 설계 및 검증 흐름을 시연했다.
   3. STCO 프레임워크는 누화 및 스큐를 제어하기 위해 접지-신호-접지(ground-signal-ground) 인터리브 전송 라인을 사용하며, 시뮬레이션은 C4 측 IPD가 국소적인 디커플링을 제공하고 칩렛 마이크로범프의 전압 변동을 줄임을 보여준다.
   4. 이 디자인은 45 µm 범프 피치에서 16-36 GT/s를 목표로 하며, 6개 층에 2/2 µm로 신호 트레이스가 라우팅되고 7번째 층은 전력 공급용으로 예약되었다.
   5. 테스트 칩은 32 GT/s에서 0.77 UI의 측정된 온-다이 아이 너비를 달성했으며, 시뮬레이션은 36 GT/s에서 0.74 UI의 아이 너비를 보여주었다.
   6. 이 결과는 유기 인터포저가 이종 칩렛 시스템의 신호 및 전력 무결성 요구 사항을 충족할 수 있음을 보여준다.
   <img alt="8층 CoWoS-R RDL의 UCIe-A 설계 흐름 및 STCO" src="https://substackcdn.com/image/fetch/$s_!y3jQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28208d53-ff49-4dbc-b650-235d118c7894_1536x1024.png" caption="8층 CoWoS-R RDL의 UCIe-A 설계 흐름 및 STCO. 출처: GUC, “Design of UCIe-A x64 Chiplets Integration for 16–36 GT/s Using Organic Interposer,” ECTC 2026">
   <img alt="16 및 32 GT/s에서 측정된 UCIe-A 아이 다이어그램" src="https://substackcdn.com/image/fetch/$s_!K5hL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb26a7f83-521f-482c-8d26-1786be1a497c_1416x1111.png" caption="16 및 32 GT/s에서 측정된 UCIe-A 아이 다이어그램. 출처: GUC, “Design of UCIe-A x64 Chiplets Integration for 16–36 GT/s Using Organic Interposer,” ECTC 2026">

### 2.6. 스택형 메모리
삼성은 TSV를 사용하지 않고 DRAM을 스택하는 VCS(Vertical Cu post Stack) 방식을 선보였으며, 이는 모바일 및 고성능 컴퓨팅 플랫폼 모두에서 대역폭, 전력 효율성 및 폼 팩터를 개선할 잠재력을 보여준다.
1. **VCS(Vertical Cu post Stack) 기술**
   1. 삼성은 TSV를 완전히 피하는 DRAM 스태킹 접근 방식을 선보였다.
   2. VCS는 실리콘을 통해 비아를 에칭하는 대신, 몰딩 컴파운드에 내장된 56 µm 미만 피치, 30 µm 미만 폭의 고종횡비 구리 기둥을 통해 4개의 스택형 메모리 다이를 연결한다.
   3. 또한 패키지 기판을 RDL로 대체한다.
   4. 인터커넥트 단축으로 기존 와이어 본딩 스택 대비 동일 속도에서 전력 소비가 41% 감소(0.646W에서 0.384W로)했다.
   5. 삼성은 또한 최대 데이터 전송률이 8.6Gb/s에서 11.8Gb/s로 증가하고 전력 소비는 8%만 증가하는 더 나은 신호 성능을 보고했다.
   <img alt="기존 와이어 본딩 스택 대 수직 Cu 포스트 스택" src="https://substackcdn.com/image/fetch/$s_!pMpH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98ff3793-40e7-4ec6-88df-cf0d8c9b1fe4_652x181.jpeg" caption="기존 와이어 본딩 스택 대 수직 Cu 포스트 스택. 출처: Samsung, “Multi Stacked FOWLP utilizing Extreme Aspect Ratio Cu Post for Mobile on-Device AI Memory Solution,” ECTC 2026">
   <img alt="고종횡비 구리 포스트로 연결된 4단 VCS DRAM 스택의 단면도" src="https://substackcdn.com/image/fetch/$s_!G2al!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa65f8822-861b-4d0c-969c-250b121bdca3_770x62.jpeg" caption="고종횡비 구리 포스트로 연결된 4단 VCS DRAM 스택의 단면도. 출처: Samsung, “Multi Stacked FOWLP utilizing Extreme Aspect Ratio Cu Post for Mobile on-Device AI Memory Solution,” ECTC 2026">
2. **폼 팩터 및 대역폭 개선**
   1. 폼 팩터도 크게 개선되어 패키지 높이와 면적이 각각 40% 감소했으며, 대역폭은 2.6배, I/O 수는 6배 증가했다.
   2. 삼성은 모바일 플랫폼에 중점을 두지만, 이 접근 방식은 고전력 워크로드에도 유망하다.
   3. VCS 및 유사한 접근 방식은 미래 AI 가속기가 더 높은 대역폭을 더 낮은 전력과 더 작은 폼 팩터로 달성하는 데 도움이 될 수 있으며, 서버 CPU용 SOCAMM과 같은 고밀도 메모리 모듈도 가능하게 할 것으로 예상된다.
