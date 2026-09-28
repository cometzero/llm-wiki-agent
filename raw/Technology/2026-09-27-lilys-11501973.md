---
title: "Intel Panther Lake Teardown, 18A, BSPD, GAAFET, SemiAnalysis STEEL"
origin: lilys_ai
lilys_project_id: 11501973
lilys_project_url: "https://lilys.ai/digest/11501973"
lilys_created_at: "2026-09-27T00:38:15.585Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13593105"
sources:
  - id: "12418564"
    url: "https://newsletter.semianalysis.com/p/intel-panther-lake-teardown"
    title: "Intel Panther Lake Teardown"
    status: "done"
---

# Intel Panther Lake Teardown, 18A, BSPD, GAAFET, SemiAnalysis STEEL

## LilysAI note

> 인텔의 최신 소비자 칩인 **Panther Lake**의 내부 구조는? 인텔 18A 공정 노드를 통해 **후면 전력 공급(BSPDN)**과 **게이트-올-어라운드(GAA) 트랜지스터**를 최초로 상용 구현하여, 인텔이 경쟁력 있는 반도체 제조로 복귀하는 중요한 이정표를 제시했습니다.

## 1. 인텔 팬서 레이크(Panther Lake) 개요 및 주요 기술

인텔 팬서 레이크는 후면 전력 공급(BSPDN), 게이트-올-어라운드(GAA) 트랜지스터, 그리고 Foveros-S 어셈블리 기술을 최초로 상용화한 인텔의 최신 소비자 칩이다.

### 1.1. 팬서 레이크의 핵심 기술
1. **후면 전력 공급 (BSPDN) 최초 상용화**
2. **게이트-올-어라운드 (GAA) 트랜지스터 도입**
3. **Foveros-S 어셈블리를 통한 고급 패키징 기능**
4. **인텔 18A 공정 노드 적용**
   1. 4개의 RibbonFET(인텔의 GAAFET 마케팅 명칭) 및 게이트 스택을 통해 전력 공급
   2. 접점, 전면 및 후면 배선, 본딩된 캐리어까지 18A 공정 추적
   3. 이러한 재료 및 통합 선택은 게이트 제어를 개선하고 저항을 줄이지만, 정전 용량, 열 저항 및 공정 복잡성을 증가시킨다
5. **로직 밀도 비교**
   1. 팬서 레이크의 18A 컴퓨팅 로직과 TSMC N3E GPU 로직은 유사한 로직 밀도를 가진다
   2. 그러나 18A는 TSMC N3P, N2 또는 삼성 SF2의 최고 밀도를 능가하지 못한다
   3. 팬서 레이크의 CPU 코어는 점진적인 업데이트이며, 고성능 GPU는 여전히 TSMC N3E를 사용한다

### 1.2. 팬서 레이크의 구성 및 분석 대상
1. **Foveros-S 고급 패키징을 통한 구성**
   1. 하나의 컴퓨팅 타일, 하나의 GPU 타일, 하나의 I/O 타일을 수동 베이스 타일 위에 조립한다
2. **타일별 공정 노드**
   1. 두 가지 컴퓨팅 타일 변형 모두 인텔 18A를 사용한다
   2. Xe3 GPU 옵션은 인텔 3의 4코어 GT1 타일과 TSMC N3E의 더 큰 12코어 GT2 타일로 구성된다
   3. 두 가지 I/O 타일 변형 모두 TSMC N6를 사용한다
3. **주요 분석 대상**
   1. PTL-U 컴퓨팅 타일
   2. 4코어 및 12코어 GPU 타일
   3. 12레인 I/O 타일

## 2. PowerVia 기술 상세 분석
PowerVia는 전력 공급 네트워크를 트랜지스터 층 뒤쪽으로 이동시켜 전면 신호 라우팅과 분리하는 기술이다.

### 2.1. PowerVia의 작동 방식
1. **기존 칩의 전력 및 신호 라우팅 문제점**
   1. 기존 칩에서는 전력과 신호가 동일한 전면 금속 스택을 통해 장치 전면으로 라우팅된다
   2. 전력 레일은 트랜지스터 근처의 희소한 라우팅 자원을 소비하며, 높은 비아 스택은 굵은 상위 와이어에서 로컬 레일로 VDD 및 VSS를 전달한다
2. **후면 전력 공급(BSPD)의 개념**
   1. BSPD는 주 전력 네트워크를 트랜지스터 층 뒤쪽, 즉 후면으로 이동시켜 전면 신호 라우팅과 분리한다
3. **인텔의 PowerVia 구현**
   1. 인텔의 BSPD 구현인 "PowerVia"는 전용 후면 금속을 통해 전력을 라우팅한다
   2. 이 전력은 나노-TSV를 통해 로컬 소스/드레인(S/D) 접점에 연결된다

### 2.2. PowerVia의 제조 공정
1. **상호 연결 스택 구축**
   1. 전면(frontside)은 M0-M14 신호 스택으로 구성되며, 후면(backside)은 BM0-BM5 전력 스택으로 구성된다
   2. M0와 BM0는 트랜지스터에 가장 가깝다
2. **나노-TSV 형성 과정**
   1. 인텔은 접점을 형성한 후 전면에서 각 비아를 패턴화하고 에칭한다
   2. 좁은 비아는 접점 측면에서 실리콘 기판 깊숙이 이어진다
   3. 이후 인텔은 전면 신호 금속 스택을 완성하고, 웨이퍼를 캐리어에 본딩한 후 뒤집어 매립된 비아 팁이 노출될 때까지 원래 기판을 제거한다
   4. 후면 금속 스택은 노출된 비아 위에 직접 증착된다
<img alt="Schematic orientation of the retained carrier, devices and frontside/backside interconnects. Layer counts are illustrative; not to scale. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!rsvx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3333a960-a4cb-4310-95fe-91efaf9da41f_1493x851.png" caption="유지된 캐리어, 장치 및 전면/후면 상호 연결의 개략적인 방향. 레이어 수는 예시이며, 실제 비율과 다르다. 출처: SemiAnalysis">

### 2.3. PowerVia의 장점 및 한계
1. **나노-TSV 및 후면 비아 프로파일**
   1. 나노-TSV와 후면 비아 프로파일은 웨이퍼의 반대쪽에서 형성되기 때문에 반대 방향으로 테이퍼진다
2. **FEOL 및 전면 상호 연결**
   1. 트랜지스터 구조는 FEOL(Front-End-Of-Line)을 형성한다
   2. 로컬 접점과 나노-TSV는 이들을 배선에 연결한다
   3. M0는 전면 상호 연결 스택을 시작한다
3. **실리콘 캐리어의 역할**
   1. 실리콘 캐리어는 전면 상호 연결 위에 부착된 상태로 유지된다
   2. 이는 기판 제거 및 후면 처리 동안 장치 웨이퍼를 지지하며, 완성된 칩의 열 경로의 일부로 남는다
4. **PowerVia의 이점**
   1. PowerVia는 혼잡한 전면 금속에서 주 전력 분배를 제거하고, 더 짧고 넓은 후면 와이어를 통해 전력을 라우팅한다
5. **PowerVia의 한계**
   1. 측면 랜딩은 여전히 표준 셀에서 면적을 차지하므로, 직접 후면 접점보다 셀 면적 회복률이 낮다
6. **나노-TSV의 역할**
   1. 로직 장치 옆의 나노-TSV는 후면 전력 네트워크에서 VDD 또는 VSS를 전달하며, 신호 연결은 전면 금속을 통해 위로 계속된다
<img alt="Intel 18A RibbonFET and nano-TSV in XTEM (top) and EDS (bottom). Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!qRdI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe07f47dd-574d-47bb-aa0d-b399e2445562_714x460.png" caption="XTEM(상단) 및 EDS(하단)로 본 인텔 18A RibbonFET 및 나노-TSV. 출처: SemiAnalysis">

## 3. 후면 및 전면 상호 연결
인텔 18A는 Mo-라인 W 접점과 나노-TSV를 별도의 후면 Cu 전력 네트워크와 결합하여 전면 라우팅 자원을 확보한다.

### 3.1. 후면 상호 연결
1. **삼성 SF2와의 비교**
   1. 삼성 SF2 데이터는 팬서 레이크와 비교하기 위해 포함되었다
   2. SF2는 BSPD가 없는 기존 GAA 파운드리 노드로서 18A를 평가하는 데 유용한 기준이 된다
2. **PowerVia 공급 경로**
   1. PowerVia 공급 경로는 후면 Cu 레일에서 Mo-라인 W 나노-TSV를 통해 로컬 트랜지스터 접점으로 이어진다
   2. 이 단면에서 테이퍼진 연결은 접점 레벨에서 BM0까지 약 150nm에 걸쳐 있다
   3. 리본 아래의 유전체는 장치를 후면 배선으로부터 전기적으로 분리하고 채널 아래의 전도성 실리콘 본체를 제거한다
<img alt="Intel 18A Mo-lined W nano-TSV and Cu BM0 rail. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!1OnH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ae0c0e2-440b-4937-bf39-6afa3549f20c_2065x1024.png" caption="인텔 18A Mo-라인 W 나노-TSV 및 Cu BM0 레일. 출처: SemiAnalysis">
3. **AlOₓ 에칭 스톱 레이어**
   1. AlOₓ는 에칭 스톱(ES) 역할을 하여 종점 제어를 가능하게 하고 하위 레이어를 보호한다
   2. BM0 및 M1 라인 위의 레이어는 이중 AlOₓ 레이어를 보여주지만, SMIC N+3 분해에서는 단일 AlOₓ 레이어가 나타났다
   3. SMIC는 더 간단한 로컬 AlOₓ 서브스택을 사용하며, 나머지 캡 및 에칭 시퀀스는 필요한 랜딩 보호를 제공한다
<img alt="Intel 18A backside metallization materials. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!cP3E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4363b1d8-2954-4dd8-8e0d-6ffedec7317a_1050x176.png" caption="인텔 18A 후면 금속화 재료. 출처: SemiAnalysis">
4. **이중 AlOₓ 레이어의 이점**
   1. 밀접하게 배치된 AlOₓ 이중층은 에칭 시퀀스에서 두 개의 보호된 종점을 제공한다
   2. 주 유전체 플라즈마 에칭은 첫 번째 AlOₓ 필름에서 멈추고, 선택적 습식 클리어는 해당 필름을 열고, 두 번째 플라즈마 에칭은 중간 SiN을 제거하고 두 번째 AlOₓ 필름에서 멈춘다
   3. 최종 습식 클리어는 금속 랜딩 표면을 노출시킨다
   4. 이중 AlOₓ 스톱은 추가 처리가 정당화되는 또 다른 보호된 종점이 필요한 경우 유용하다
   5. 단계별 보호는 공정 창을 넓히고 금속 침식, 부식 및 보이드 형성을 줄인다
5. **후면 스택의 계층 구조**
   1. 후면 스택은 장치 근처의 비교적 미세한 BM0-BM2 배선과 더 굵은 BM3-BM5 전력 분배로 나뉜다
   2. 가장 큰 피치 증가는 BM2와 BM3 사이에서 발생한다
   3. BM0의 피치는 로직-로우 높이와 밀접하게 일치하여 셀 로우에 로컬 전력 공급을 맞춘다
   4. 이 계층 구조는 희소한 전면 신호 라우팅 자원을 소비하지 않고 전력 공급 네트워크를 위한 넓은 전력 배선을 제공한다
<img alt="Intel 18A BM0-BM5 minimum measured pitches. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!lZLH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8aa7ad4-7dd0-4f61-ac5a-42fe2ffb6298_945x301.png" caption="인텔 18A BM0-BM5 최소 측정 피치. 출처: SemiAnalysis">

### 3.2. 전면 상호 연결
1. **인텔 18A와 삼성 SF2의 차이점**
   1. 인텔 18A는 Mo-라인 W 접점과 나노-TSV를 별도의 후면 Cu 전력 네트워크와 결합한다
   2. 삼성 SF2는 전력을 전면에 유지하며, Ti 기반 접점 인터페이스와 Ta 기반 배리어 및 Cu 배선 주변의 Co 라이너를 사용한다
   3. 18A 표준 셀 로우에서는 후면 전력 레일이 셀 내 나노-TSV를 통해 장치에 전력을 공급하여 전면 라우팅 자원을 확보한다
   4. 삼성의 M0는 전력 및 신호 연결을 모두 수용한다
<img alt="Intel 18A M0-M14 minimum measured pitches. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!WulC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97e3382a-e1ee-4cbe-b924-8e1090cc570b_945x624.png" caption="인텔 18A M0-M14 최소 측정 피치. 출처: SemiAnalysis">
2. **M0로의 연결 경로**
   1. 장치에서 M0로의 연결은 Ti 기반 S/D 인터페이스, W 접점 채움, Mo-라인 W 비아, 그리고 Cu M0 와이어를 통해 이루어진다
   2. Mo는 W의 전도성 핵 생성 및 접착층을 제공하여 기존 W 통합에 사용되던 저항성 TiN 라이너를 대체한다
   3. 이는 W 채움 및 확립된 연마, 세척 및 에칭 공정을 유지하면서 기능 내 유효 전도 부피를 증가시킨다
   4. 나노-TSV는 후면 공급 경로에서 동일한 Mo-라인 W 구조를 사용한다
<img alt="Intel 18A and Samsung SF2 contact and via materials. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!Yo77!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff116d635-da7e-4106-8025-7b6aac641a3f_1188x313.png" caption="인텔 18A 및 삼성 SF2 접점 및 비아 재료. 출처: SemiAnalysis">
3. **라이너 및 배리어 재료의 선택**
   1. 인텔은 M0-M1에 Co/Ru 라이너, M2-M4에 Co, M5-M9에 Nb를 사용한다
   2. 하위 레벨 라이너는 Cu의 접착을 돕고 트렌치 채움 중 보이드 형성을 줄인다
   3. 인텔의 Nb 특허는 기존 Ta 기반 배리어에 비해 저항 기여도를 줄이기 위한 전도성 확산 배리어를 설명한다
   4. 상위 금속층은 PVD(물리 기상 증착)를 통해 형성된 더 두꺼운 배리어를 지원한다
   5. 하위 금속층은 ALD(원자층 증착)를 통해 증착된 더 얇은 배리어를 필요로 한다
   6. 금속층별로 라이너와 배리어를 변경함으로써 인텔은 상호 연결 저항, 공정 복잡성 및 신뢰성을 최적화할 수 있다
<img alt="Intel 18A and Samsung SF2 M0-M9 liner, fill and etchstop materials. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!Cn7G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0faf32e-6f06-4087-8fc5-e5b8862893a9_1600x542.png" caption="인텔 18A 및 삼성 SF2 M0-M9 라이너, 채움 및 에칭 스톱 재료. 출처: SemiAnalysis">

## 4. RibbonFET 기술 상세 분석
RibbonFET은 인텔의 GAAFET 명칭으로, FinFET의 수직 핀을 4개의 수평 실리콘 나노시트 스택으로 대체하여 게이트가 채널을 모든 면에서 둘러싸도록 한다.

### 4.1. GAAFET으로의 아키텍처 진화
1. **RibbonFET의 특징**
   1. RibbonFET은 FinFET의 수직 핀을 4개의 쌓인 수평 실리콘 나노시트로 대체한다
   2. 이는 게이트가 채널을 모든 면에서 둘러싸도록 한다
2. **평면 MOSFET의 한계**
   1. 평면 MOSFET은 게이트를 소스 및 드레인 사이의 채널 위에 배치한다
   2. 게이트 길이가 줄어들면서 드레인이 게이트와 제어 경쟁을 시작하여 오프 상태 누설이 증가했다
3. **FinFET의 도입 및 한계**
   1. 정전기 제어는 채널을 수직 핀으로 올리고 게이트를 세 면에 감싸는 아키텍처 진화를 통해 복원되었다
   2. "FinFET"이라고 불리는 이 새로운 아키텍처는 더 작은 공간에 더 많은 유효 채널 폭을 담았다
   3. 추가 스케일링은 더 작은 셀 내에서 구동 전류와 누설을 모두 유지하기 어렵게 만들었고, 평면 MOSFET이 직면했던 동일한 문제를 다시 야기했다
4. **나노시트 GAAFET의 장점**
   1. 나노시트 GAAFET은 수직 핀을 수평 나노시트 스택으로 대체하여 네 번째 면을 닫는다
   2. 더 엄격한 정전기 제어는 더 짧은 게이트 길이에서 누설을 억제하며, 스태킹은 셀 공간 내에서 유효 채널 폭을 추가한다
<img alt="Controlling gate leakage through architectural evolution. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!Ci5j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c40c53f-5c63-4e12-abc6-feeb8fdce130_1183x635.png" caption="아키텍처 진화를 통한 게이트 누설 제어. 출처: SemiAnalysis">
5. **채널 폭 조정의 유연성**
   1. FinFET 공정에서는 채널 폭이 전체 핀을 추가하거나 제거해야 하는 불연속적인 단계로 변경된다
   2. 나노시트 폭은 공정 설계 규칙 내에서 연속적으로 조정될 수 있다
   3. 인텔 18A는 각각 4개의 나노시트 스택을 사용하며, 로직과 SRAM에 걸쳐 폭을 다양하게 조절한다

### 4.2. RibbonFET과 MBCFET 비교
1. **삼성 MBCFET과의 비교**
   1. 삼성은 2022년에 SF3E로 GAAFET 생산을 시작했으며, SF3에 이어 현재 SF2를 사용한다
   2. 삼성의 'MBCFET'은 인텔의 첫 RibbonFET 구현과 유용한 구조적 비교를 제공한다
2. **나노시트 스택 수 및 폭 차이**
   1. 인텔은 삼성의 3개에 비해 4개의 리본을 쌓는다
   2. 삼성의 시트는 이 분야에서 훨씬 넓으므로, 시트 수와 폭 모두 사용 가능한 채널 둘레에 중요하다
<img alt="Intel 18A RibbonFET (left) and Samsung SF2 MBCFET (right) cross-sections. Sheet-cut (top) and gate-cut (bottom). Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!slLx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8edaad18-76d3-48f9-9497-c58f938767e7_2048x2048.png" caption="인텔 18A RibbonFET(왼쪽) 및 삼성 SF2 MBCFET(오른쪽) 단면도. 시트 컷(상단) 및 게이트 컷(하단). 출처: SemiAnalysis">
3. **채널 폭이 전류 전달에 미치는 영향**
   1. 시트 폭은 전류를 전달하는 실리콘 표면도 변경한다
   2. 기존 (001) 실리콘에서 넓은 나노시트는 넓은 상단 및 하단 표면을 강조하여 전자 수송에 유리하다
   3. 좁은 시트에서 더 큰 측벽 기여는 정공 수송에 유리하다
   4. 얇은 시트는 게이트 제어를 개선하지만, 구속 및 산란을 증가시킨다

### 4.3. GAAFET의 게이트 스택 및 임계 전압 튜닝
1. **NMOS 및 PMOS의 다른 WFM 스택**
   1. 18A와 같은 GAAFET 설계는 NMOS와 PMOS에 다른 WFM(Work-Function-Metal) 스택을 사용한다
   2. NMOS는 TiAl 기반 스택을 사용하고, PMOS는 TiN WFM을 사용한다
2. **La를 이용한 임계 전압 튜닝**
   1. 게이트 유전체 내의 La는 SiOx/HfOx 경계에서 계면 쌍극자를 생성하여 유효 일함수를 이동시키고 임계 전압을 튜닝한다
   2. 이는 인텔에게 NMOS 및 PMOS WFM 스택 외에 또 다른 제어 수단을 제공한다
   3. 쌍극자 튜닝은 특히 GAA에서 유용하며, 더 두꺼운 WFM으로 좁은 시트 간 간격을 소비하지 않고 임계값을 변경한다
<img alt="Matched-cut EDS, Intel 18A (left) vs. Samsung SF2 (right)." src="https://substackcdn.com/image/fetch/$s_!zMTv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3325ca6-4a44-4e9a-ae33-69ba59f57406_2832x2486.png" caption="일치하는 컷 EDS, 인텔 18A(왼쪽) vs. 삼성 SF2(오른쪽). 상단: 시트 컷, 인텔 P-코어 로직 및 삼성 로직 필드 CU. 하단: 게이트 컷, 인텔 P-코어 로직 및 삼성 NPU 로직. 컷 방향은 일치하며, 셀 기능 및 구동 목표는 다르다. 패널당 스케일 바. 출처: SemiAnalysis">
3. **인텔과 삼성의 소스/드레인 에피 구조 차이**
   1. 인텔은 접점 아래에 소스/드레인 에피를 유지하는 반면, 삼성은 W를 에피 깊숙이 넣어 V자형 Ti-라인 인터페이스를 형성한다
   2. 더 깊은 접점은 금속-반도체 면적을 증가시키고 하위 시트에서 전류 경로를 단축하여 접점 및 확산 저항을 줄인다
   3. 더 많은 에피를 유지하는 것은 특히 SiGe에서 PMOS로의 변형 전달에 사용 가능한 재료를 보존한다
4. **나노시트 폭 및 게이트 스택 재료**
   1. 삼성은 인텔의 4개 리본에 비해 3개의 시트를 쌓으며, 두 공정 모두 구동 강도를 조절하기 위해 시트 폭을 사용한다
   2. 두 공정 모두 HfOx 게이트 유전체와 Ti 기반 일함수 스택을 사용하며, NMOS 스택에는 Al이 포함된다
   3. 인텔의 PMOS 스택은 리본 사이에 더 많은 공간을 남기고, W는 그 간격을 채우는 반면, 더 두꺼운 NMOS 스택은 주로 상단 트렌치에 W를 남긴다
<img alt="Top: Intel 18A P-core logic. Bottom: Samsung SF2 CU logic. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!a7Zl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c00f05f-2aaf-43ea-8718-d2a616b3d5d0_6076x2424.png" caption="상단: 인텔 18A P-코어 로직. 하단: 삼성 SF2 CU 로직. 출처: SemiAnalysis">

### 4.4. GAAFET 공정 흐름 및 재료 선택
1. **NMOS 및 PMOS WFM 통합 시퀀스**
   1. 마스크를 사용한 순차적 WFM 흐름은 다른 게이트 높이와 나노시트 간 채움을 설명한다
   2. 아래 제안된 시퀀스는 별도의 NMOS 및 PMOS 일함수 단계가 해당 기하학적 구조를 생성하는 방법을 보여준다
<img alt="Proposed Intel 18A NMOS and PMOS WFM integration sequence. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!NB05!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F041768b6-ca30-4eba-8a2d-f9e786e10cba_1260x1165.png" caption="제안된 인텔 18A NMOS 및 PMOS WFM 통합 시퀀스. 출처: SemiAnalysis">
2. **유전체 격리 및 열 경로**
   1. BSPDN 공정 덕분에 인텔은 밀집 로직 실리콘 서브핀을 유전체로 대체하여 리본 아래의 기생 전도 경로를 제거하고 기판 관련 정전 용량을 줄인다
   2. 유전체 격리는 누설을 서브핀 도핑 프로파일에 덜 민감하게 만들지만, 제거 및 채움 단계를 추가한다
   3. 또한 실리콘을 통한 직접적인 열 경로를 약화시켜 열 추출을 위해 접점, 금속 스택 및 패키지를 더 중요하게 만든다
3. **불소 농도 및 W 증착**
   1. 불소는 맵에서 선택된 인텔 장치 구조 주변에 집중되어 있다
   2. WF6는 W 핵 생성 및 채움의 표준 전구체이며, 배리어 필름은 인접 유전체를 불소 공격으로부터 보호한다
   3. 염화물 기반 전구체는 W 증착 중 F 도입을 피하지만, 염소 공격, 핵 생성 및 채움 품질 제어가 필요하다
   4. 통합 목표는 얇은 보호 라이너와 주변 스택에 대한 최소한의 화학적 손상을 가진 연속적이고 낮은 저항의 W 경로이다
<img alt="Proposed GAAFET Process Flow. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!DiW4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe13daab3-c017-4c12-a531-a91839c58c3f_1435x2196.png" caption="제안된 GAAFET 공정 흐름. 출처: SemiAnalysis">

## 5. 라이브러리 분석 및 밀도 비교
인텔 18A 로직 셀은 5트랙 로직 라이브러리를 사용하는 반면, N3E 및 인텔 3 셀은 7트랙 로직 라이브러리를 사용한다.

### 5.1. 측정된 라이브러리 치수
1. **셀 높이, 게이트 피치, 금속 기하학 및 리본 치수 측정**
   1. XTEM(투과전자현미경) 사이트에서 셀 높이, 게이트 피치, 금속 기하학 및 리본 치수를 측정했다
   2. "시트 컷"은 실리콘 채널을 가로질러 리본의 끝을 보여준다
   3. "게이트 컷"은 연속적인 게이트를 통해 채널을 따라 이어진다
<img alt="Measured library dimensions. *Intel 18A PDK provides M0 pitch of 32 nm, but Panther Lake HP libraries shipped at 36 nm, **3rd party discolsures. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!gqg5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ca26391-75aa-4ca5-ba84-b3c047155b38_1666x1712.png" caption="측정된 라이브러리 치수. *인텔 18A PDK는 32nm의 M0 피치를 제공하지만, 팬서 레이크 HP 라이브러리는 36nm로 출시되었다. **제3자 공개. 출처: SemiAnalysis">
2. **로직 라이브러리 비교**
   1. 18A 로직 셀 치수는 5트랙 로직 라이브러리를 가리키는 반면, N3E 및 인텔 3 셀 치수는 7트랙 로직 라이브러리를 증명한다
   2. DDR-PHY는 코어 로직보다 넓은 M0 와이어와 훨씬 큰 간격을 사용한다
3. **PowerVia의 이점**
   1. PowerVia는 18A가 컴팩트한 셀 높이와 넓은 M0 기하학을 결합할 수 있도록 하여, 주 전력 레일을 신호 라우팅 트랙에서 이동시킨다
   2. 이는 로컬 와이어 스케일링을 완화하면서 작은 셀 공간을 유지한다

### 5.2. 대표 셀 밀도 및 M0 단면 기하학
1. **로직 밀도 비교**
   1. 인텔 18A 컴퓨팅 로직과 TSMC N3E GPU 로직은 보어(Bohr) 대표 셀 모델에서 유사한 밀도를 가진다
   2. 18A 예시는 인텔 3 GPU 예시보다 18.6% 더 밀집되어 있다
<img alt="Representative-cell density and input sensitivity. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!wUqw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8012b4b-76c8-4ed5-b7c5-a0ffb9b953a3_1809x445.png" caption="대표 셀 밀도 및 입력 민감도. 출처: SemiAnalysis">
2. **M0 단면 기하학**
   1. 18A P-코어는 N3E 벡터 엔진보다 M0에 훨씬 더 많은 금속 단면적을 제공한다
   2. 각 프로파일을 사다리꼴로 처리하면 라인당 면적이 2.63배, 라우팅 피치로 정규화한 후 면적이 1.84배 증가한다
   3. 더 큰 단면은 선 저항에 대한 기하학적 기여를 줄이고 주어진 전류에 대한 전류 밀도를 낮춘다
   4. 더 높고 넓은 와이어는 또한 정전 용량을 추가하므로, 회로 지연은 저항과 정전 용량의 균형에 따라 달라진다
<img alt="M0 cross-section geometry. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!g5dH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e3fd4d0-e346-4acb-831f-238795842d53_1274x349.png" caption="M0 단면 기하학. 출처: SemiAnalysis">

### 5.3. 컴퓨팅 타일의 리본 치수 및 SRAM 최적화
1. **리본 치수 및 게이트 스택 기하학**
   1. 리본 치수와 게이트 스택 기하학은 컴퓨팅 타일 전체와 NMOS 및 PMOS 간에 다양하게 나타난다
   2. 이는 채널 구동, 게이트 부하 및 유전체/WFM 스택에 필요한 공간을 로직, SRAM 및 DDR-PHY 전반에 걸쳐 균형을 맞추기 위함이다
   3. 폭은 주로 사용 가능한 채널 둘레를 변경하고, 두께는 정전기 제어 및 캐리어 구속을 변경한다
   4. 게이트 스택 두께는 낮은 저항의 채움을 위한 남은 공간을 결정한다
<img alt="Ribbon dimensions. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!5Pha!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52a1dad6-3279-42de-abb4-14c9de265f01_1710x606.png" caption="리본 치수. 출처: SemiAnalysis">
2. **P-코어 및 LP E-코어 로직의 나노시트 폭 다양성**
   1. P-코어와 LP E-코어 모두 여러 나노시트 폭을 사용한다
   2. 타이밍에 민감한 경로, 버퍼 및 다른 팬아웃을 가진 셀은 다른 구동 강도를 필요로 한다
<img alt="LP-E (Left) and P-Cores XTEM Images Capturing Intra-Site Varying Nanosheet Widths. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!IAd5!,w_720,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff687fc56-acb6-4dd2-aaab-3263f071e914_2048x2048.png" caption="LP-E(왼쪽) 및 P-코어 XTEM 이미지, 사이트 내 나노시트 폭 변화 포착. 출처: SemiAnalysis">
3. **L2 및 L3 SRAM의 GAA 이점**
   1. GAA는 SRAM 설계자에게 풀업(PU), 패스 게이트(PG), 풀다운(PD) 트랜지스터의 균형을 맞출 수 있는 또 다른 방법을 제공한다
   2. FinFET 비트셀은 핀 개수를 통해 장치 강도를 설정하는 반면, GAA는 나노시트 폭을 크기 조절 노브로 추가한다
   3. 6T SRAM 셀에서 패스 게이트에 비해 강한 풀다운은 읽기 방해를 제한하고, 풀업에 비해 강한 패스 게이트는 쓰기 가능성을 향상시킨다
<img alt="Intel 18A SRAM bitcell features. Source: Intel, ISSCC 2025 (© IEEE). [31]" src="https://substackcdn.com/image/fetch/$s_!F-4E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F290da0e9-8b7f-4f12-b480-2dfc9f6b3db6_1488x655.png" caption="인텔 18A SRAM 비트셀 특징. 출처: 인텔, ISSCC 2025 (© IEEE). [31]">
4. **L2 셀의 리본 폭 활용**
   1. 리본 폭은 인텔이 전체 핀을 추가하지 않고도 SRAM 강도를 균형 있게 조절할 수 있게 한다
   2. L2 셀은 PU에 가장 좁은 리본을, PD에 가장 넓은 리본을 사용하여 각각 쓰기 가능성과 읽기 안정성을 향상시킨다
   3. 인텔의 공개된 HCC는 보조 장치 없이 작동하며, 더 밀집된 HDC는 네거티브 비트라인 쓰기 보조 장치를 사용한다
   4. 선택된 비트라인을 일시적으로 접지 아래로 당기면 패스 게이트 오버드라이브가 증가하여 낮은 공급 전압에서 풀업을 압도할 수 있다
<img alt="L2 SRAM and its PU, PD and PG device fields, in reading order from the top left. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!xEWm!,w_720,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfbad6f6-9b36-4390-8e36-4c1cc07b7039_2048x2048.png" caption="L2 SRAM 및 PU, PD, PG 장치 필드(왼쪽 상단부터 읽는 순서). 출처: SemiAnalysis">

### 5.4. DDR PHY 및 Intel 3 GPU 장치
1. **DDR-PHY의 설계 특징**
   1. DDR-PHY는 밀도 대신 제어된 아날로그 동작과 안정적인 오프칩 신호 전달을 위해 설계되었다
   2. 유사한 폭을 가진 반복되는 4시트 장치는 매칭 및 프로그래밍 가능한 구동을 위한 규칙적인 트랜지스터 유닛 사용에 적합하다
   3. 더 넓은 로컬 배선은 전류 전달 및 민감한 신호 분리를 위한 공간을 제공하지만, 밀집된 코어 로직 그리드보다 더 많은 면적을 소비한다
<img alt="DDR PHY. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!iEvK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88d6334e-d412-47d4-bfa8-65653b442347_2048x2048.png" caption="DDR PHY. 출처: SemiAnalysis">
2. **Intel 3 GPU 장치: 벡터 엔진 로직**
   1. 인텔 3의 XVE 로직은 M0에 전력 레일을 가진 2핀 PMOS 및 NMOS 장치를 사용한다
   2. 셀 높이와 M0 피치는 7트랙 기하학을 제공하며, 이는 18A 로직보다 2트랙 더 많다
<img alt="Intel 3 vector-engine logic. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!YhXj!,w_720,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5aabc128-607f-4c10-9ba6-a1e295443cf7_1044x1044.png" caption="인텔 3 벡터 엔진 로직. 출처: SemiAnalysis">
3. **Intel 3 L2 SRAM**
   1. 인텔 3 L2 SRAM은 친숙한 HCC 크기 패턴을 사용한다: 1개의 PU 핀, 2개의 PG 핀, 2개의 PD 핀
<img alt="Intel 3 L2 SRAM. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!Mk0v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cfdec65-5e08-46de-a569-ec139002c164_2068x2068.png" caption="인텔 3 L2 SRAM. 출처: SemiAnalysis">

## 6. 플로어플랜 분석 및 GPU 타일 비교
팬서 레이크-U는 루나 레이크의 플로어플랜을 밀접하게 따르며, 4개의 P-코어와 4개의 LP E-코어, NPU, 미디어 및 디스플레이 엔진을 유사한 위치에 배치한다.

### 6.1. 컴퓨팅 타일 플로어플랜 및 면적 비교
1. **팬서 레이크-U와 루나 레이크의 플로어플랜 유사성**
   1. 팬서 레이크-U는 루나 레이크의 플로어플랜을 상당히 밀접하게 따른다
   2. 두 제품 모두 4개의 P-코어와 4개의 LP E-코어, NPU, 미디어 및 디스플레이 엔진을 유사한 위치에 배치한다
   3. 루나 레이크는 팬서 레이크의 Xe3 GPU의 직접적인 전신인 Xe2를 사용한다
<img alt="Intel Lunar Lake (left) and Panther Lake-U (right) floorplans. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!x4aK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F377bc2eb-a382-4a12-9fcb-fc2f2efed37a_5022x1948.png" caption="인텔 루나 레이크(왼쪽) 및 팬서 레이크-U(오른쪽) 플로어플랜. 출처: SemiAnalysis">
2. **컴퓨팅 타일의 주요 구성 요소 면적 측정**
   1. 컴퓨팅 타일의 주요 구성 요소 면적을 측정하고 TSMC N3B의 루나 레이크 이전 제품과 비교했다
   2. 이는 블록 면적의 변화를 파악하고 두 칩을 공정 노드 및 설계 전반에 걸쳐 비교하는 데 도움이 된다
   3. 총 타일 면적은 스크라이브 라인 면적을 제외한다
   4. 컴퓨팅-플러스-GPU 소계는 PTL-U 컴퓨팅 타일과 GT1 GPU를 사용하며, I/O 타일과 수동 베이스는 제외한다
<img alt="Panther Lake 4+0+4 compute-tile areas compared with Lunar Lake. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!z_1g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a78ff7a-30a1-4bb6-91bf-56f3859e9a87_1600x1589.png" caption="루나 레이크와 비교한 팬서 레이크 4+0+4 컴퓨팅 타일 면적. 출처: SemiAnalysis">
3. **P-코어 및 LP E-코어 클러스터의 변화**
   1. P-코어 면적은 루나 레이크와 팬서 레이크 사이에 거의 변동이 없지만, L2 용량은 2.5MiB에서 3MiB로 증가했다
   2. 쿠거 코브(Cougar Cove)는 동일한 P-코어 면적에 20% 더 많은 L2를 담는다
   3. 다크몬트(Darkmont)의 4코어 LP E-코어 클러스터는 루나 레이크의 스카이몬트(Skymont)보다 5.0% 더 작으며, 대부분 L2 영역에서 감소했다
<img alt="Lunar Lake Lion Cove (left) vs Panther Lake Cougar Cove (right) P-cores. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!o5gM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01032afd-9c69-4b3d-a103-26a24e01ae21_2386x1380.png" caption="루나 레이크 라이온 코브(왼쪽) vs 팬서 레이크 쿠거 코브(오른쪽) P-코어. 출처: SemiAnalysis">
4. **NPU의 면적 감소 및 성능 향상**
   1. 가장 큰 면적 감소는 NPU에서 발생했으며, 36.9% 더 적은 면적을 차지한다
   2. NPU 5는 동일한 총 INT8 MAC(곱셈-누산) 수를 절반의 신경 컴퓨팅 엔진으로 통합한다
   3. 3개의 NCE(신경 컴퓨팅 엔진) 각각은 더 큰 MAC 배열을 가지며, 전체 NCE 크기는 NPU 4 엔진보다 22.6% 더 크다
   4. 통합은 또한 스크래치패드와 SHAVE DSP의 수를 12개에서 6개로 절반으로 줄인다
<img alt="Lunar Lake NPU 4 (left) vs Panther Lake NPU 5 (right). Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!Yxkt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7bff1891-aabd-4e2d-9358-45793075a886_2382x1433.png" caption="루나 레이크 NPU 4(왼쪽) vs 팬서 레이크 NPU 5(오른쪽). 출처: SemiAnalysis">
5. **NPU 5의 추가 기능**
   1. NPU 5는 또한 기본 FP8을 추가한다
   2. FP16의 절반인 피연산자 폭을 사용하면 저장 및 전송 요구량이 줄어들어 워크로드가 더 작은 로컬 메모리 예산에 맞도록 돕는다
   3. 하드웨어 활성화 기능은 프로그래밍 가능한 DSP를 차지할 수 있는 작업을 더욱 줄인다

### 6.2. GPU 타일 및 I/O 타일
1. **Xe3 GPU 아키텍처 및 타일 옵션**
   1. 팬서 레이크는 인텔의 최신 GPU 아키텍처인 Xe3를 탑재한 첫 번째 제품이다
   2. 두 가지 GPU 타일 옵션을 제공한다: 인텔 3의 4개 Xe3 코어를 가진 작은 GT1 타일과 TSMC N3E의 12개 Xe3 코어를 가진 큰 GT2 타일
<img alt="Intel Panther Lake GT1 (Intel 3, 4 Xe cores) and GT2 (TSMC N3E, 12 Xe cores) GPU tile floorplans. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!8gce!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a70b129-6de6-4449-8e5a-cac7b7a99c10_1761x1475.png" caption="인텔 팬서 레이크 GT1(인텔 3, 4 Xe 코어) 및 GT2(TSMC N3E, 12 Xe 코어) GPU 타일 플로어플랜. 출처: SemiAnalysis">
2. **GT2 타일의 Xe 코어 크기 및 L1/SLM 용량 증가**
   1. TSMC N3E의 GT2 타일은 GT1보다 훨씬 작은 Xe 코어를 가진다
   2. GT1 타일의 Xe 코어는 루나 레이크의 코어보다 약 69% 크고, GT2의 코어보다 약 55% 크다
   3. 측정된 벡터/매트릭스 엔진 영역은 루나 레이크와 팬서 레이크의 GT2 타일 사이에 거의 변동이 없다
   4. 공유 L1/SLM 용량은 192KiB에서 256KiB로 33% 증가했으며, 면적은 5%만 증가하여 유효 밀도가 27% 향상되었다
<img alt="Panther Lake GPU tile area comparison with Lunar Lake. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!M_4N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34458780-2d3f-4f4f-b8f1-f0992b0a1dc8_1600x489.png" caption="루나 레이크와 비교한 팬서 레이크 GPU 타일 면적. 출처: SemiAnalysis">
3. **L2 SRAM 용량 및 밀도 비교**
   1. GT1 타일은 4MiB의 L2를 가지는 반면, GT2 타일은 16MiB를 가진다
   2. GT1은 L2 캐시를 4개의 1MiB 뱅크로 나누고, GT2는 8개의 2MiB 뱅크를 사용한다
   3. 각 뱅크는 128개의 매크로를 포함하지만, 각 N3E 매크로는 인텔 3 매크로의 8KiB 용량의 두 배인 16KiB를 저장한다
   4. N3E 매크로는 두 배의 비트를 저장하면서도 54%만 더 커서 30% 더 높은 밀도를 제공한다: ~23.7 Mbit/mm² 대 18.3 Mbit/mm²
<img alt="Panther Lake Intel 3 (GT1) and TSMC N3E (GT2) area comparison. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!mP_1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc856024b-1cd3-4088-9ac2-b8b0ef954918_1600x329.png" caption="팬서 레이크 인텔 3(GT1) 및 TSMC N3E(GT2) 면적 비교. 출처: SemiAnalysis">
4. **I/O 타일 구성 및 재사용 전략**
   1. 팬서 레이크는 두 가지 I/O 타일 변형을 사용하며, 둘 다 TSMC N6에서 제조된다
   2. 작은 I/O 타일은 루나 레이크의 I/O 레이아웃에 PCIe 4.0 블록과 썬더볼트 블록을 추가하여 4개의 추가 PCIe 4.0 레인과 또 다른 썬더볼트 4 포트를 제공한다
   3. 이러한 검증된 PHY 및 컨트롤러를 재사용함으로써 18A에서 외부 인터페이스를 포팅하고 재검증하는 것을 피할 수 있다
<img alt="Panther Lake 12-lane I/O tile floorplan. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!RAyF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea5fd8fb-d7d4-4a0d-bc3b-61a71e59325a_1909x615.png" caption="팬서 레이크 12레인 I/O 타일 플로어플랜. 출처: SemiAnalysis">

## 7. Foveros-S 패키징 및 인텔의 제조 회복
Foveros-S는 컴퓨팅, GPU, I/O 실리콘을 별도의 타일로 분할하여 확장성과 모듈성을 제공하는 인텔의 고급 패키징 기술이다.

### 7.1. Foveros-S 패키징 기술
1. **Foveros-S의 확장성 및 모듈성**
   1. 팬서 레이크는 컴퓨팅, GPU, I/O 실리콘을 별도의 타일로 분할하는 분리된 패키징을 통해 확장성과 모듈성을 제공한다
   2. 이 분할은 각 제품이 얼마나 많은 최첨단 웨이퍼 면적을 소비하는지, 어떤 기능이 다른 공정에 남아 있을 수 있는지, 그리고 공유 타일 세트에서 인텔이 얼마나 많은 구성 자유를 제공할 수 있는지를 결정하므로 패키지가 인텔의 노드 경제학의 일부가 된다
2. **18A 공정의 활용**
   1. 컴퓨팅 및 GPU 타일을 별도로 제조함으로써 새로운 18A 공정을 컴퓨팅 타일에만 국한시키고, 그래픽 및 I/O는 다른 더 확립되고 비용 효율적인 공정을 사용할 수 있게 한다
   2. 팬서 레이크의 경우, GPU 및 I/O 타일은 Foveros-S를 사용하여 수동 실리콘 베이스 위에 컴퓨팅 타일과 함께 조립된다
3. **Foveros-S의 구조**
   1. 인텔의 현재 기술 브리핑은 Foveros-S에 대해 공칭 36µm 피치를 명시한다
   2. 베이스의 TSV(Through-Silicon Via)는 위의 미세 배선을 아래의 더 큰 패키지 연결에 연결한다
   3. 기능 타일은 2.5D 구성으로 해당 수동 베이스 위에 나란히 놓인다
<img alt="Foveros-S package schematic: active tiles connect through microbumps to a passive silicon base. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!ufv2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a11c35f-101e-404d-815d-f75ba672170b_1216x503.png" caption="Foveros-S 패키지 개략도: 활성 타일은 마이크로범프를 통해 수동 실리콘 베이스에 연결된다. 출처: SemiAnalysis">
4. **패키지 배선 계층 구조**
   1. 컴퓨팅 및 GPU 타일을 통한 단면은 패키지의 배선 계층 구조를 보여준다
   2. 마이크로범프는 각 활성 타일을 수동 실리콘 베이스에 연결한다
   3. 베이스의 미세 재분배층(RDL)은 짧고 밀집된 타일 간 링크를 전달한다
   4. TSV는 베이스를 통해 패키지 기판으로 연결을 전달하며, 이는 더 굵은 마더보드 솔더 조인트로 연결을 분산시킨다
   5. 베이스는 상호 연결을 제공하는 반면, 계산은 그 위의 활성 타일에 남아 있다
<img alt="Panther Lake package cross section through the compute and graphics tiles. Source: SemiAnalysis" src="https://substackcdn.com/image/fetch/$s_!8jFH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10a5b31b-6002-4da0-81f7-9903e64f7648_4892x1572.png" caption="컴퓨팅 및 그래픽 타일을 통한 팬서 레이크 패키지 단면. 출처: SemiAnalysis">
5. **메모리 컨트롤러 통합의 이점**
   1. CPU 옆에 메모리 컨트롤러를 배치하면 메테오 레이크(Meteor Lake) 및 애로우 레이크(Arrow Lake)에서 CPU 메모리 요청에 필요했던 D2D(Die-to-Die) 전송이 제거된다
   2. 이는 추가 송신기, 수신기 및 링크 통과를 피하여 인터페이스 에너지와 지연 시간을 절약한다
   3. 팬서 레이크의 별도 GPU는 여전히 D2D 링크를 통해 DRAM에 도달하므로, 더 큰 로컬 캐시도 패키지 트래픽을 억제하는 데 도움이 된다

### 7.2. 인텔의 제조 회복 및 과제
1. **인텔의 공정 로드맵 목표**
   1. 2021년 7월, 인텔 CEO 팻 겔싱어는 2025년까지 성능 리더십을 되찾기 위한 야심찬 공정 로드맵을 제시했으며, 이는 나중에 4년 안에 5개 노드를 달성하는 것으로 설명되었다
   2. 5년 후, 인텔의 복귀 스토리는 팻이 희망했던 만큼 명확하게 긍정적이지는 않다
2. **과거 인텔의 공정 기술 리더십**
   1. 인텔은 한때 하이-k 금속 게이트 기술과 FinFET을 업계보다 몇 년 앞서 대량 생산에 도입하며 공정 기술의 속도를 주도했다
   2. 22nm FinFET 공정은 2012년 아이비 브릿지(Ivy Bridge)와 함께 소비자에게 도달했다
3. **14nm 및 10nm 공정에서의 어려움**
   1. 이러한 리더십은 14nm에서 흔들리고 10nm에서 무너졌다
   2. 인텔은 2.7배의 엄청난 밀도 증가를 목표로 했지만, 해당 노드는 몇 년 늦게 출시되었고 인텔의 전체 라인업을 지원하기 위해 여러 번의 수정이 필요했다
   3. 2019년까지 인텔은 대부분의 제품 스택에서 14nm를 여전히 출하하고 있었고, 10nm 클라이언트 램프는 아이스 레이크(Ice Lake) 모바일 프로세서에 집중되었다
   4. 반면, TSMC는 N7 및 N7+를 출하하고 있었고, AMD의 Zen 2 컴퓨팅 칩렛은 N7을 사용하여 코어 수를 늘리고 효율성을 개선했다
4. **인텔의 회복 노력**
   1. 인텔의 회복은 소비자 CPU와 고급 패키징에 집중되었다
   2. 타이거 레이크(Tiger Lake), 앨더 레이크(Alder Lake), 루나 레이크(Lunar Lake), 그리고 현재 팬서 레이크는 인텔의 소비자 로드맵을 복원했다
   3. 공정 측면에서는 메테오 레이크와 함께 인텔 4, 그래나이트 래피즈(Granite Rapids) 및 시에라 포레스트(Sierra Forest)와 함께 인텔 3, 그리고 팬서 레이크와 함께 인텔 18A가 출시되었다
   4. 인텔은 또한 고급 패키징을 파운드리 서비스의 일부로 만들었다
5. **제조 이정표로서의 팬서 레이크**
   1. 팬서 레이크는 상당한 제조 이정표이다
   2. 단면도는 RibbonFET과 PowerVia가 로컬 접점 및 배선을 어떻게 재구성하는지 보여주며, 플로어플랜은 아키텍처 통합 및 공정 선택이 면적을 어떻게 절약하는지 보여준다
