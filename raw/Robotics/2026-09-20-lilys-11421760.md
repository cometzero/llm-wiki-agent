---
title: "Where Does a Robot Think — On-Device vs Datacenter Inference"
origin: lilys_ai
lilys_project_id: 11421760
lilys_project_url: "https://lilys.ai/digest/11421760"
lilys_created_at: "2026-09-20T04:17:09.889Z"
lilys_collection: "AI"
source_type: "webPage"
lilys_note_id: "13489783"
sources:
  - id: "12331587"
    url: "https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device"
    title: "A Brain Too Big to Carry — On-Device vs Datacenter Inference"
    status: "done"
---

# Where Does a Robot Think — On-Device vs Datacenter Inference

## LilysAI note

> 로봇의 '두뇌'인 AI 모델을 로봇 내부에 둘 것인가, 데이터센터에 둘 것인가? **로봇의 범용성과 비용 효율성을 고려할 때, 데이터센터 기반의 AI 모델이 유리**합니다. 이는 로봇의 하드웨어 제약을 넘어 더 크고 복잡한 모델을 활용할 수 있게 하여, 로봇의 지능과 활용도를 극대화할 수 있기 때문입니다.

## 1. 로봇 두뇌: 온디바이스 vs 데이터센터 추론

로봇의 AI 모델을 로봇 내부에 둘 것인지, 데이터센터에 둘 것인지에 대한 논의는 로봇의 범용성과 비용 효율성을 결정한다.

### 1.1. 로봇 모델의 제약 사항
1. **시간 제약**
   1. 로봇은 실시간 제어 루프를 실행하며, 지연이 발생하면 동작이 무효화될 수 있다.
   2. LLM은 느려도 최종 결과에 영향을 미치지 않지만, 로봇은 주변 환경 변화에 즉각 반응해야 한다.
2. **비용 제약**
   1. LLM은 사용자가 제공하는 화면 뒤에서 작동하지만, 로봇은 제조업체가 컴퓨팅 장치와 로봇 자체를 모두 제작하고 선불로 비용을 지불해야 한다.
   2. 대규모로 생산될 경우, 이 초기 비용은 수십억 달러에 달할 수 있다.
3. **하드웨어 고정 및 모델 적합성**
   1. 이러한 제약 때문에 로봇의 온보드 하드웨어는 고정되어 있으며, 모델은 합리적인 제조 범위 내에서 설계된다.
   2. 최첨단 모델 기능은 저렴하고 실시간으로 작동하는 하드웨어에서 실행 가능한 범위 내에서 제한된다.

### 1.2. 로봇 모델 크기 및 추론 위치
1. **로봇 모델의 현재 크기**
   1. 최첨단 로봇 모델은 LLM(수조 개의 매개변수)보다 훨씬 작으며, 현재 수십억 개의 매개변수 수준이다.
   2. 예를 들어, Physical Intelligence의 π0 클래스는 약 30억 개, NVIDIA의 DreamZero는 140억 개의 매개변수를 가진다.
   3. LLM 연구소는 훈련 예산과 추론 비용을 최적화하여 모델 크기를 결정하지만, 로봇 공학 연구소는 데이터가 지원할 수 있는 범위와 Jetson 또는 H100에 지연 시간 예산 내에서 맞는 크기를 선택한다.
2. **확장성 제약**
   1. LLM과 마찬가지로 로봇 공학에서도 모델 확장이 문제 해결 범위를 넓히는 것으로 나타났다.
   2. 그러나 데이터 확보(인터넷 규모의 로봇 경험 데이터 부족)와 네트워크가 주요 제약 사항이다.
   3. 최첨단 모델은 이미 로봇의 온보드 용량을 초과하여 데이터센터의 H100 또는 GB200 GPU가 필요하다.
3. **모델 크기 변화 및 접근 방식**
   1. 로봇 모델 크기는 효율성 향상과 함께 빠르게 변화한다.
   2. NVIDIA의 DreamZero(140억 매개변수)는 실시간 실행을 위해 두 개의 GB200 GPU가 필요하지만, RoboTTT(30억 매개변수)는 온보드 실행이 가능하도록 모델을 소형화했다.
   3. 궁극적으로 일부 로봇은 온보드에서 인식을 완전히 실행하고, 다른 로봇은 데이터센터의 GPU로 일부를 오프로드하는 하이브리드 접근 방식이 불가피하다.
   4. 특히 일반 로봇의 경우, 컴퓨팅 및 전력 예산 제약을 벗어나고 여러 로봇 간 추론을 공유할 수 있는 오프로드 방식이 유리하다.

## 2. 로봇 모델의 작동 방식 및 계층
로봇 모델은 계획, 동작, 서보 및 안전 루프의 세 가지 계층으로 구성되며, 각 계층의 주파수 요구 사항에 따라 온보드 또는 오프로드 여부가 결정된다.

### 2.1. 로봇 모델의 계층 구조
1. **일반 로봇의 정의**
   1. 수십 년간 공장에서 사용된 고전적인 로봇 제어 방식이나 특정 학습된 정책은 이 글의 주제가 아니다.
   2. 이 글은 개방형 지침을 따르고, 이전에 본 적 없는 장면을 처리하며, 다양한 작업을 수행할 수 있는 '일반 로봇'에 초점을 맞춘다.
2. **로봇 모델의 세 가지 계층**
   1. **계획 계층 (Planning Layer)**
      1. 지침과 장면을 해석하고, 로봇이 다음에 무엇을 해야 할지 결정한다.
      2. 하위 작업, 목적지, 파악 자세 또는 발걸음 계획 등을 생성한다.
   2. **동작 계층 (Action or Motion Layer)**
      1. 계획 계층의 출력을 짧은 동작 시퀀스, 신체 자세 또는 속도로 변환한다.
   3. **서보 및 안전 루프 (Servo and Safety Loops)**
      1. 로봇의 상태를 추정하고, 접촉 및 미끄러짐에 반응하며, 균형을 유지하고 최종적으로 액추에이터를 제어한다.

### 2.2. 주파수 및 컴퓨팅 요구 사항에 따른 계층 분리
<img alt="" src="https://substackcdn.com/image/fetch/$s_!10PZ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90990b49-f892-4dfb-a4a2-1021c2d4a584_2074x1386.png" width="1456" height="973">
<figcaption>출처: SemiAnalysis</figcaption>

1. **동작 및 서보 계층 (고주파)**
   1. 이 계층은 수백 Hz로 작동하며, 100Hz 루프는 10밀리초마다 다음 출력을 생성해야 한다.
   2. 일반적인 무선 왕복 시간은 10~50밀리초이므로, 네트워크는 지연을 추가할 뿐만 아니라 모델이 아무것도 계산하기 전에 거의 전체 예산을 소모한다.
   3. 따라서 약 100Hz 이상의 모든 것은 로봇을 벗어날 수 없다.
2. **계획 계층 (저주파)**
   1. 약 20Hz 이하로 작동하는 계획 계층은 결정당 200밀리초를 가지므로, 10~50밀리초의 왕복 시간도 충분히 수용 가능하다.
   2. 이는 계획 계층을 로봇에서 완전히 오프로드할 수 있는 여유를 제공하며, 잘 조정된 네트워크 스택은 오프로드 가능한 경계를 20Hz 이상으로 확장할 수 있다.
   3. 그러나 더 큰 문제는 지연 시간(latency)보다 지터(jitter)이다.
      1. 고정된 지연은 시스템이 로봇과 주변 환경이 해당 시간 동안 얼마나 움직일지 예측하여 미리 계획할 수 있으므로 처리 가능하다.
      2. 지터는 명령이 불규칙한 간격으로 도착하여 로봇이 다음 업데이트가 언제 도착할지 정확히 알 수 없으므로 더 어렵다.
      3. 지터를 제어하는 것이 계획 계층 오프로드를 가능하게 하는 핵심이다.
3. **계획 계층의 컴퓨팅 요구 사항**
   1. 계획 계층은 가장 많은 컴퓨팅 자원을 요구하며, 일반화가 증가함에 따라 그 요구 사항도 증가한다.
   2. 개방형 작업은 실제 추론을 필요로 하며, 추론 모델은 크다.
   3. 현재 Jetson Thor는 GB200의 1/10 FLOPs와 1/30 메모리 대역폭만 제공하므로, 일부 기업은 데이터센터 컴퓨팅을 고려하기 시작했다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!U9kS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe499b86b-0b8a-4d8c-924c-d866b008cf34_2048x899.png" width="1456" height="639">
<figcaption>출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!EjjN!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1b186dd-a47f-45b5-be93-7663e20c9cb4_1686x1072.png" width="1456" height="926">
<figcaption>출처: SemiAnalysis</figcaption>

## 3. 공급망 현실 및 총 소유 비용(TCO) 분석
데이터센터 실리콘 중심의 공급망과 DRAM 부족 현상은 로봇 온보드 컴퓨팅에 불리하게 작용하며, TCO 분석 결과 데이터센터 기반 오프로드 방식이 비용 효율성 측면에서 유리하다.

### 3.1. 공급망 현실: 데이터센터 실리콘 중심
1. **데이터센터 실리콘 우선 생산**
   1. 공급망은 로봇 실리콘이 아닌 데이터센터 실리콘에 맞춰져 있으며, 로봇 실리콘 생산 확대는 어렵다.
   2. 엔비디아의 가속기 생산량은 거의 전적으로 데이터센터 실리콘에 집중되어 있다.
   3. Jetson 라인은 전체 생산량에서 매우 작은 부분을 차지하며, 이는 로봇 시장이 아직 초기 단계이기 때문이다.
2. **마진 및 노드 경쟁**
   1. 현재 Blackwell 데이터센터 GPU는 Jetson 모듈보다 훨씬 높은 총마진을 제공하므로, 엔비디아는 희소한 최첨단 웨이퍼 생산 능력을 데이터센터에 집중할 유인이 크다.
   2. 로봇 실리콘은 데이터센터가 경쟁하는 동일한 최첨단 노드(TSMC N4, N3, N2)로 수렴하고 있다.
   3. 따라서 낮은 생산량과 낮은 마진의 Jetson은 항상 고급 노드 웨이퍼 경쟁에서 후순위로 밀릴 수밖에 없다.

### 3.2. 실리콘 및 DRAM 효율성
1. **실리콘 효율성**
   1. 로봇의 웨이퍼 수요는 현재 전체 공급망에 큰 부담을 주지 않는다.
   2. 핵심 질문은 "주어진 로봇 함대에 대해 어떤 접근 방식이 더 적은 최첨단 실리콘을 소비하는가?"이다.
   3. 온보드 칩과 공유 데이터센터 GPU의 실리콘 효율성은 로봇 7대당 GPU 1대에서 교차한다.
   4. 즉, 로봇 7대 이상에서는 공유 GPU에서 인식을 처리하는 것이 각 로봇에 칩을 넣는 것보다 로봇당 더 적은 실리콘을 사용한다.
   5. 이는 웨이퍼 공급이 부족할 때 확장 가능한 접근 방식이 된다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!Kz1z!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d0fc12e-bbab-482f-bba6-a3acc3b350b0_1356x982.png" width="1356" height="982">
<figcaption>출처: SemiAnalysis</figcaption>

2. **메모리 효율성**
   1. DRAM 또한 주요 병목 현상이며, Jetson 세대마다 더 많은 DRAM(Jetson Thor는 128GB LPDDR5X)을 탑재하고 있다.
   2. 대부분의 증분 DRAM 용량은 AI 가속기용 HBM에 흡수되고 있어, 로봇 두뇌가 의존하는 LPDDR 공급은 줄어들고 있다.
   3. DRAM이 부족한 자원일 때, 로봇당 더 적은 DRAM을 사용하는 접근 방식이 확장 가능하다.
   4. 메모리 효율성도 로봇 5대당 GPU 1대에서 교차하며, 그 이상에서는 공유 GPU가 로봇당 더 적은 DRAM을 사용한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!pIul!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bb8c1a5-6631-4253-9529-e2e4e03f4869_1168x854.png" width="1168" height="854">
<figcaption>출처: SemiAnalysis</figcaption>

### 3.3. TCO(총 소유 비용) 비교: B300 vs. RTX 6000 PRO vs. Jetson Thor
1. **벤치마크 모델 및 설정**
   1. 엔비디아의 RoboTTT 모델을 사용하여 벤치마크를 수행했다.
   2. GR00T N1.7 체크포인트에 테스트 시간 훈련(TTT) 블록을 삽입하여 논문의 컴퓨팅 및 메모리 프로필과 일치하도록 재구성했다.
   3. TTT 경로는 전체 FLOPs, 메모리 트래픽, 상태 스와핑 비용을 발생시킨다.
   4. 이 기준으로 B300 1대는 500ms 청크 마감 시간 내에 로봇 12대를 지원하며, RTX PRO 6000은 4대를 지원한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!RlZE!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43f575dd-3c20-4441-b5c2-155fea93a71b_1478x470.png" width="1456" height="463">
<figcaption>출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!9vnb!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ae251d0-0772-47cf-ae56-cc31e49590e6_2048x1214.png" width="1456" height="863">
<figcaption>출처: SemiAnalysis</figcaption>

<img alt="" src="https://substackcdn.com/image/fetch/$s_!yqRr!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9726be9f-039f-4064-a2f4-2d5e3bc050e2_2048x1214.png" width="1456" height="863">
<figcaption>출처: SemiAnalysis</figcaption>

2. **세 가지 시나리오의 TCO**
   1. **B300 오프로드 시나리오**
      1. B300 서버 1대와 로봇 96대를 연결하는 무선 보드 96개(GPU당 로봇 12대)를 포함한다.
      2. 총 자본 지출(capex)은 약 55만 4천 달러이며, 운영 비용을 포함한 총 TCO는 시간당 18.63달러이다.
   2. **RTX 6000 Pro 오프로드 시나리오**
      1. 로봇 96대를 위해 8-GPU 서버 3대가 필요하다(GPU당 로봇 4대).
      2. 총 자본 지출은 43만 6천 달러이며, 총 TCO는 시간당 15.61달러이다.
   3. **Jetson Thor 온디바이스 시나리오**
      1. 로봇 96대에 각각 Jetson Thor 모듈(개당 3,500달러)과 베이스보드, 저장 장치, 냉각 장치, 배터리, 온보드 무선 연결이 포함된다.
      2. 총 비용은 약 39만 4천 달러이며, Thor 모듈의 전력 비용을 포함한 TCO는 시간당 14.97달러이다.
3. **온디바이스 Jetson Thor의 수명**
   1. 온디바이스 Jetson Thor의 유효 수명은 데이터센터 GPU보다 짧은 4년으로 가정한다.
   2. 로봇에 장착된 Jetson은 지속적인 진동, 충격, 그리고 작업 환경에 따른 마모로 인해 하드웨어 수명이 단축된다.
4. **자본 비용(WACC) 가정**
   1. 온디바이스 배포의 자본 비용이 더 높을 수 있지만, 온디바이스 컴퓨팅의 경제적 유효 수명을 짧게 가정한 기본 사례를 고려하여 모든 시나리오에서 WACC를 일정하게 유지했다.

### 3.4. TCO 비교 및 활용률의 영향
1. **초기 TCO 비교 (활용률 미고려)**
   1. B300은 FP4 밀집 FLOPs당 TCO가 시간당 0.15달러, Jetson Thor는 0.16달러, RTX 6000 Pro는 0.39달러이다.
   2. RTX 6000 Pro는 FLOPs당 TCO 또는 FLOPs당 자본 지출 측면에서 성능이 좋지 않으므로, B300 오프로드 시나리오와 Jetson Thor 온디바이스 시나리오에 집중한다.
2. **활용률의 영향**
   1. 활용률은 TCO의 핵심 변수이다. 로봇과 GPU는 거의 고정 자본이므로, 작동하든 유휴 상태이든 비용은 동일하며, 생산 시간당 비용은 작동 시간에 반비례한다.
   2. **온로봇 칩 활용률**: 현재 배포 환경에 따라 크게 다르다.
      1. 가정용 로봇은 하루 1~2시간(4~8%)만 작동하며, 이는 작업이 산발적이고 현재 모델이 자율 작업 능력을 제한하기 때문이다.
      2. 산업용 로봇은 Figure의 BMW 배포 사례에서 하루 약 10시간(40%) 작동한다. 모델 기능이 향상됨에 따라 산업용 활용률은 더 높아질 것으로 예상된다.
3. **활용률을 고려한 TCO**
   1. **공유 GPU 서버**: 컴퓨팅 자원이 여러 로봇에 걸쳐 공유되므로 하루 종일 바쁘게 작동한다. B300 GPU 1대가 로봇 12대를 지원하는 시나리오에서 GPU 서버 활용률은 약 90%로 모델링한다.
   2. **온로봇 칩**: 기본 사례로 약 40%의 활용률을 모델링한다.
   3. **결과**: 활용률을 고려하면 B300 오프로드 시나리오의 FP4 밀집 FLOPs당 TCO는 시간당 0.17달러인 반면, Jetson Thor 온로봇 시나리오는 0.37달러이다.
   4. 즉, 오프로드 시나리오가 온로봇 시나리오의 약 46% 수준의 TCO를 달성한다.
   5. 높은 GPU 서버 활용률과 낮은 온디바이스 칩 활용률은 오프로드 시나리오에 유리하게 작용한다.
   6. 산업 배포의 경우 오프로드 시나리오가 온로봇 시나리오 TCO의 약 46%에 불과하며, 가정 배포의 경우 약 12%까지 낮아진다.
   7. B300 클라우드 서버 활용률이 매우 낮고 온디바이스 활용률이 매우 높은 경우에만 온디바이스 추론이 유리하다.
   8. 배치 처리 가정을 변경하면, B300 GPU당 로봇 5대 이상부터는 오프로드 시나리오가 TCO 측면에서 유리하다.
   9. 결론적으로, 클라우드의 B300 서버로 추론을 오프로드하는 것이 매우 설득력 있는 사례이며, 소규모 로봇 배포의 경우에도 서버를 소유하기보다 컴퓨팅을 필요에 따라 임대하는 것이 합리적이다.

## 4. 배포 환경의 현실과 기업별 전략
오프로드 컴퓨팅은 TCO 측면에서 유리하지만, 실제 배포에서는 로봇의 일반성 요구 사항, 무선 네트워크 환경, 고객 현장 변경 허용 여부 등 다양한 요인이 온보드 또는 오프로드 전략을 결정한다.

### 4.1. 배포 환경의 결정 요인
1. **TCO와 실제 배포의 차이**
   1. 이론적으로는 오프로드 컴퓨팅이 TCO에서 우위를 점하지만, 현재 대량 생산 단계가 아니므로 TCO가 결정적인 요소는 아니다.
   2. 실제로 로봇을 출하하는 기업들은 컴퓨팅을 로봇에 두거나 일부를 오프로드하는 두 가지 진영으로 나뉜다.
2. **배포 전략 결정 요인**
   1. 로봇이 필요로 하는 일반성의 정도
   2. 무선 네트워크 환경의 품질
   3. 고객 현장 변경 허용 여부
   4. 대규모 로봇 함대가 구축되면 TCO가 중요해질 것이다.

### 4.2. 보스턴 다이내믹스 (Boston Dynamics)
<span><span><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!eU_n!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c16e36-882f-4fed-a8f7-cd11e2cc1b72_493x258.jpeg 424w, https://substackcdn.com/image/fetch/$s_!eU_n!,w_474,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c16e36-882f-4fed-a8f7-cd11e2cc1b72_493x258.jpeg 474w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/$s_!eU_n!,w_474,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c16e36-882f-4fed-a8f7-cd11e2cc1b72_493x258.jpeg" sizes="100vw" alt="" srcset="https://substackcdn.com/image/fetch/$s_!eU_n!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c16e36-882f-4fed-a8f7-cd11e2cc1b72_493x258.jpeg 424w, https://substackcdn.com/image/fetch/$s_!eU_n!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c16e36-882f-4fed-a8f7-cd11e2cc1b72_493x258.jpeg 474w" width="474"></picture><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!qqdL!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca43844-d8d2-422f-bc40-d9fb3a6eaea6_416x259.jpeg 424w, https://substackcdn.com/image/fetch/$s_!qqdL!,w_474,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca43844-d8d2-422f-bc40-d9fb3a6eaea6_416x259.jpeg 474w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/$s_!qqdL!,w_474,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca43844-d8d2-422f-bc40-d9fb3a6eaea6_416x259.jpeg" sizes="100vw" alt="" srcset="https://substackcdn.com/image/fetch/$s_!qqdL!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca43844-d8d2-422f-bc40-d9fb3a6eaea6_416x259.jpeg 424w, https://substackcdn.com/image/fetch/$s_!qqdL!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca43844-d8d2-422f-bc40-d9fb3a6eaea6_416x259.jpeg 474w" width="474" doc-source-index="181"></picture><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!4NfV!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4dd760-29c7-4656-a8c0-e8a18294b325_922x651.jpeg 424w, https://substackcdn.com/image/fetch/$s_!4NfV!,w_474,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4dd760-29c7-4656-a8c0-e8a18294b325_922x651.jpeg 474w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/$s_!4NfV!,w_474,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4dd760-29c7-4656-a8c0-e8a18294b325_922x651.jpeg" sizes="100vw" alt="" srcset="https://substackcdn.com/image/fetch/$s_!4NfV!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4dd760-29c7-4656-a8c0-e8a18294b325_922x651.jpeg 424w, https://substackcdn.com/image/fetch/$s_!4NfV!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d4dd760-29c7-4656-a8c0-e8a18294b325_922x651.jpeg 474w" width="474" doc-source-index="182"></picture></span><figcaption>출처: Boston Dynamics</figcaption></span>

1. **일반 로봇의 필요성**
   1. 보스턴 다이내믹스는 Spot, Stretch, Atlas 세 가지 로봇을 개발하며, 이들은 대규모 데이터 수집 및 애플리케이션 파일럿을 위한 개발 단계에 있다.
   2. 자동차 공장과 같은 환경에서는 수만 개의 부품, 다양한 모델 및 색상으로 인해 전통적인 자동화 방식으로는 비효율적이다.
   3. 이러한 가변성 때문에 수천 대의 전문 기계 대신 일반 로봇이 필요하다.
   4. 일반성은 지능과 직결되며, 물리적 세계에서 작동하는 로봇은 이미지를 소비하고 추론해야 하므로 모델이 본질적으로 커진다.
   5. 보스턴 다이내믹스는 구글의 Gemini Robotics ER(Gemini 3.5 Flash 기반)을 예시로 들며, System 2 모델이 수천억에서 1조 개의 매개변수를 가질 것으로 추정한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!y550!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6f43bcb-0d89-400c-a872-b1c5c8680135_1204x606.png" width="1204" height="606">
<figcaption>출처: Boston Dynamics. 현대 공장</figcaption>

2. **"너무 커서 운반할 수 없는 두뇌"**
   1. 이러한 대규모 모델은 로봇에 탑재할 수 없으므로, 보스턴 다이내믹스는 스택을 네트워크를 통해 분할한다.
   2. **System 1 (시각-운동 정책)**: 로봇을 구동하는 정책으로, Atlas의 NVIDIA Jetson Thor와 같이 온보드에서 실행된다.
   3. **System 2 (추론 계층)**: 로봇 외부에서 실행되며, 회사의 플릿 소프트웨어인 Orbit을 통해 접근하고, 현재 DeepMind 파트너십을 통해 Google TPUs에서 제공된다.
   4. 보스턴 다이내믹스는 무선 링크를 통해 고수준 추론을 의도적으로 오프로드하는 몇 안 되는 회사 중 하나이다.
   5. 이상적으로는 System 2가 로봇에 탑재되어야 하지만, 현재 공장 작업에 충분히 추론할 수 있는 소형 모델이 없으므로, 지금 당장 지능적인 솔루션을 제공하기 위해 오프로드 방식을 선택했다.
3. **System 1과 System 2의 역할 분담**
   1. **System 2 (계획자)**: 제조 실행 시스템에서 작업 지시(예: "작업 345를 실행하고 결과를 재고함 5에 넣으시오")를 받아 로봇이 실행할 수 있는 간단한 단계로 나눈다.
   2. **System 1 (VLA)**: 카메라 시야와 짧은 지시("캔을 집어 녹색 점이 있는 통에 넣으시오")를 받아 모터 동작으로 변환한다.
   3. System 2는 공장의 "재고함 5"와 같은 복잡한 정보를 System 1이 이해할 수 있는 "녹색 점"과 같은 시각적 신호로 번역하는 핵심 역할을 한다.
   4. System 2는 또한 작업 진행 상황을 감독하고 System 1의 오작동을 감지하며, 예상보다 훨씬 자주(수 초에서 1초에 한두 번) 호출된다.
   5. System 2가 로봇에 탑재될 수 없는 또 다른 이유는 필요한 하드웨어가 데이터센터급이기 때문이다.
      1. 랙 마운트형 액체 냉각 Blackwell급 GPU는 칩당 1.2~1.4kW를 소비한다.
      2. 휴머노이드 로봇은 약 2kWh의 배터리를 탑재하고 정상 동작 시 수백 와트, 피크 시 1~2kW를 소비하므로, 온보드 GPU는 40~130W의 Jetson Thor를 사용한다.
      3. 데이터센터 GPU를 로봇에 장착하면 칩 하나만으로도 로봇 전체의 전력을 초과하고, 로봇이 감당할 수 없는 냉각을 요구하며, 배터리를 몇 분 만에 소모시킬 것이다.
4. **꼬리 지연 시간 문제 (Tail-Latency Problem)**
   1. System 2를 오프로드하면 최첨단 모델을 사용할 수 있지만, 네트워크(주로 신뢰성과 지터) 문제가 발생한다.
   2. 평균 지연 시간보다 "꼬리 지연 시간"(가끔 발생하는 1초 지연으로 로봇이 작업 도중 멈추는 현상)이 더 큰 문제이다.
   3. 추론이 무선 링크를 통해 이루어지면 네트워킹이 로봇 공학에서 가장 큰 문제가 되며, 보스턴 다이내믹스는 이를 해결하기 위해 여러 팀을 운영하고 있다.
5. **데이터 소유권 및 보안**
   1. System 2를 무선 링크를 통해 오프로드할 때 또 다른 고려 사항은 데이터 보안이다.
   2. 로봇은 고객 공장의 비디오 피드를 사실상 외부로 전송하므로, 고객은 데이터 훈련 금지, 다른 고객 데이터와 혼합 금지, 요청 시 삭제 등의 조건을 요구한다.
   3. 보스턴 다이내믹스는 데이터 파이프라인을 따라 계층화된 접근 방식을 사용한다.
      1. 로봇에서 고객은 공유할 데이터를 세밀하게 제어할 수 있다.
      2. 공유된 데이터는 SOC 2 Type 2 인증을 받은 클라우드 플랫폼 Orbit에 저장되며, 내부 데이터 위원회의 관리를 받는다.
      3. 마지막으로 Google과의 DeepMind 파트너십을 통해 System 2가 Google 인프라에서 실행되며, Gemini Enterprise Agent Platform을 통해 제공된다.
   4. 회사는 고객이 데이터가 올바르게 처리된다는 것을 확실히 증명할 수 있다면, 민감한 기업들이 Anthropic에 쿼리를 보내는 것과 같은 방식으로 오프사이트 데이터를 수용할 것이라고 예상한다.

### 4.3. 어질리티 로보틱스 (Agility Robotics)
<img alt="" src="https://substackcdn.com/image/fetch/$s_!yRxi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabb290f3-7133-487b-85a6-b996ffdf40f3_1203x802.png" width="1203" height="802">
<figcaption>출처: Agility Robotics</figcaption>

1. **온보드 컴퓨팅 전략**
   1. 어질리티 로보틱스는 창고 및 공장 환경을 위한 이족 보행 휴머노이드 로봇 Digit을 개발한다.
   2. 이 회사는 기본 모델을 처음부터 훈련하지 않고, 성능 좋은 타사 기본 모델을 가져와 자체 데이터로 후처리 훈련한다.
   3. 이 모든 과정은 로봇에 탑재된 NVIDIA Jetson급 가속기에서 온보드로 실행된다.
2. **클라우드 오프로드 기능**
   1. 추론은 온보드에서 이루어지지만, 함대 오케스트레이션, 워크플로우 할당, 현장 매핑, 무선 업데이트와 같은 일부 기능은 클라우드로 오프로드된다.
   2. 원격 조작 및 훈련 데이터 업로드도 동일한 링크를 사용한다.
   3. 오케스트레이션은 제어와 달리 지연 시간 변동에 관대하므로, 로봇이 30~60초의 대기 작업을 가지고 있다면 다음 워크플로우 청크를 10초 동안 받지 못해도 문제가 없다.
3. **네트워크 및 안전 문제**
   1. 어질리티는 네트워크 신뢰성과 지연 시간을 중요한 문제로 인식하며, 공장은 움직이는 금속, 중장비, 다중 경로 간섭 등으로 인해 무선 연결에 특히 어려운 환경이다.
   2. 컴퓨팅을 오프로드할 수 있을 만큼 신뢰할 수 있는 네트워크를 구축하는 것은 가능하지만, 이는 고객의 네트워크 및 엣지 인프라를 재작업해야 함을 의미한다.
   3. 어질리티는 Digit이 기존 현장에 최소한의 변경으로 통합되기를 원하므로, GPU 온로봇 방식을 고수한다.
   4. 안전 또한 온보드 컴퓨팅을 유지하는 이유이다.
      1. Digit은 현재 물리적으로 바리케이드된 작업 셀 내에서만 작동하며, 동적으로 안정적인 로봇은 아직 사람과 근접하여 작업할 수 있도록 안전 인증을 받지 못했다.
      2. 균형을 잡는 이족 보행 로봇은 전력 손실 시 넘어질 수 있으므로, OSHA 규제 환경에서는 Digit과 인간 작업자 간의 물리적 분리를 의무화한다.
      3. Digit의 센서 스위트는 카메라와 LiDAR를 통해 360도 인식을 제공하여 사람을 감지하고 실시간으로 경로를 멈추거나 조정할 수 있다.
      4. 다음 세대는 전용 인간 감지 시스템을 추가하여 사람이 접근하면 멈추고 접촉 전에 지면으로 내려가도록 하여, 장벽 밖에서도 작업할 수 있도록 할 예정이다.
      5. Digit은 또한 감속 중 액추에이터에 전력을 유지하여 전력이 차단되기 전에 부드럽고 안전하게 감속하는 정지 기능과 같은 산업 안전 기능을 갖추고 있다.
   6. 안전 결정을 로봇 외부로 옮기면 네트워크 링크 자체가 고장 모드가 되어, 로봇이 연결을 잃으면 문제가 발생했는지 알 수 없으므로 최악의 경우 안전 장치만 작동할 수 있다.
   7. 따라서 복잡한 안전 결정은 항상 로봇에 남아 있어야 한다.

<img alt="Agility Robotics GXO" src="https://substackcdn.com/image/fetch/$s_!XTT3!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ec88cfc-3729-43d9-927a-38f96706907f_1204x677.png" width="1204" height="677">
<figcaption>출처: Agility Robotics</figcaption>

### 4.4. 베르네 로보틱스 (Verne Robotics)
<img alt="" src="https://substackcdn.com/image/fetch/$s_!OLzK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbaef6321-f3a0-4fe9-8e7b-600f4c723a3e_1204x677.png" width="1204" height="677">
<figcaption>출처: Verne Robotics</figcaption>

1. **온보드 컴퓨팅 및 데이터 수집**
   1. 베르네 로보틱스는 주로 창고 및 경량 제조 환경에 로봇 Nemo를 배포한다.
   2. Nemo는 이중 팔 모바일 매니퓰레이터로, 물류 회사에서 냉장 보관된 시약 및 아이스팩 검색, 포장, 운송과 같은 콜드 체인 워크플로우를 자동화한다.
   3. 베르네는 원격 조작에 의존하기보다, 직원과 계약자가 착용하는 카메라 장착 데이터 수집 슈트를 사용하여 고객 현장에서 직접 데이터를 수집한다.
   4. 회사는 자체 엔드투엔드 정책 모델(수십억 매개변수 범위)을 개발하며, 이는 Jetson급 또는 RTX 50 시리즈 GPU에서 전적으로 실행된다.
   5. 창고 조작 및 경량 제조 작업(피킹, 포장, 조립 등)은 광범위한 개방형 세계 추론을 필요로 하지 않으므로, 베르네는 대규모 클라우드 호스팅 기반 모델에 의존하지 않고도 높은 작업 성공률을 달성한다.
   6. 전체 인지-행동 스택은 로봇에서 로컬로 실행되므로, 실행 중 오프보드 추론이나 데이터센터 연결이 필요 없다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!WpZS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee0ae32a-5596-4378-bfcb-7d3a1aa93a53_2048x1536.jpeg" width="1456" height="1092">
<figcaption>출처: Verne Robotics</figcaption>

### 4.5. 선데이 로보틱스 (Sunday Robotics)
<img alt="" src="https://substackcdn.com/image/fetch/$s_!TyP4!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F240be3d8-d0b3-4719-afdc-7e8c675acb31_1576x882.png" width="1456" height="815">
<figcaption>출처: Sunday Robotics</figcaption>

1. **가정용 로봇 및 훈련 데이터**
   1. 선데이 로보틱스는 가정용 로봇 Memo를 개발하며, 이 로봇은 바퀴 달린 몸체와 신축성 있는 몸통을 가지고 있다.
   2. 회사는 자체 기반 모델을 훈련하며, 원격 조작 대신 직원과 계약자가 착용하는 Skill Capture Glove를 통해 훈련 데이터를 수집한다.
   3. 이 데이터는 다른 상용 비디오 데이터와 결합되어 엔드투엔드 정책을 사전 훈련하고 후처리 훈련을 통해 개선한다.
2. **모델 성능 및 일반화**
   1. 지난 12개월 동안 선데이는 두 가지 모델을 출시하여 어떤 가정에서든 어떤 작업이든 수행할 수 있는 시스템에 가까워졌다.
   2. 2025년 11월에 출시된 ACT-1은 기능의 폭에 중점을 두어, Memo가 식탁을 치우고 식기세척기에 넣는 15분짜리 장기 작업을 완료하고, 양말 접기, 에스프레소 만들기 등 높은 숙련도를 요구하는 작업을 수행하며, 이전에 본 적 없는 가정에도 일반화되는 능력을 보여주었다.
   3. 7월에 미리 공개된 ACT-2는 이러한 폭넓은 기능을 신뢰성으로 전환하여, 로봇이 이전에 본 적 없는 가정에서 9가지 의류 유형에 걸쳐 99.1%의 제로샷 세탁물 접기 성공률을 달성했다.
   4. 선데이가 가장 중요하게 생각하는 점은 사전 훈련 규모가 후처리 훈련의 일반화를 가능하게 한다는 것이다.
   5. 사전 훈련 없이는 모델이 연구실에서 96%의 성공률을 보였지만, 처음 보는 가정에서는 14%에 불과하여 과적합 현상을 보였다.
   6. 전체 사전 훈련 코퍼스를 사용하면 이 격차가 사라져 두 환경 모두에서 100%의 성공률을 달성한다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!PaLg!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce927f91-7aa8-452e-9fbf-f170185030e7_1518x1032.png" width="1456" height="990">
<figcaption>출처: Sunday Robotics</figcaption>

3. **네트워크 문제와 온보드 추론 전환**
   1. 일반성은 사전 훈련 규모에서 비롯되며, 사전 훈련 규모는 이를 흡수할 만큼 큰 모델을 필요로 한다.
   2. 낯선 세탁실에서 작동하는 정책은 작은 모델이 아니다.
   3. 선데이는 처음에는 클라우드 추론을 가정했지만, ACT-2를 실제 가정에서 테스트한 지 이틀 만에 방향을 바꿨다.
   4. 가정용 WiFi는 데드존, 이웃 간섭, 잘못 구성된 메시 라우터, 비대칭 링크 등으로 인해 문제가 많았다.
   5. 지연 시간은 대부분 괜찮았지만, 지터가 문제였다.
   6. 몇 시간 동안 99%의 성공률을 유지하려는 로봇은 비디오 통화처럼 가끔 발생하는 문제를 무시할 수 없다.
   7. Starlink나 5G 라우터도 동일한 방식으로 연결이 끊기는 문제가 발생했다.

<img alt="" src="https://substackcdn.com/image/fetch/$s_!eZAK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2eb6c9e8-503c-4326-88b1-8450f202888c_603x827.jpeg" width="603" height="827">
<figcaption>출처: X, Sunday Robotics</figcaption>

   8. 선데이는 더 큰 모델이 더 잘 일반화되지만, 클라우드에 의존하면 로봇이 네트워크 연결에 종속된다는 근본적인 트레이드오프에 직면했다.
   9. 선데이는 이 트레이드오프를 해결하기 위해 추론을 완전히 온보드로 전환했다.
   10. 이제 모델은 로봇 내부의 GPU에서 직접 실행되어, 클라우드를 핵심 경로에서 제거하고 Memo가 네트워크와 독립적으로 작동할 수 있도록 한다.

### 4.6. 위브 로보틱스 (Weave Robotics)
<img alt="this soft robot wants to fold laundry without pretending to be human" src="https://substackcdn.com/image/fetch/$s_!_zQs!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c4e28f9-62a4-486b-b764-1aaf6ce860ed_1204x802.png" width="1204" height="802">
<figcaption>출처: Weave Robotics</figcaption>

1. **가정용 로봇 및 온보드 추론**
   1. 위브 로보틱스도 가정용 로봇을 개발한다.
   2. Isaac 0은 빨래를 접는 로봇이며, Isaac 1은 바퀴 달린 베이스와 신축성 있는 몸통을 추가하여 더러운 옷을 찾고, 접힌 옷을 정리하며, 침대를 정리하고, 장난감과 신발을 제자리에 놓는 등의 작업을 수행한다.
   3. 위브는 자체 VLA를 훈련하고 Physical Intelligence의 모델도 사용한다.
   4. 이 모델들은 수십억 매개변수 범위로 로봇에 탑재될 만큼 작으며, 추론은 로컬에서 실행될 것으로 예상된다.
2. **네트워크 의존성 및 적응 전략**
   1. 추론이 로봇에서 실행되더라도 위브는 네트워크에서 완전히 자유롭지 않다.
   2. WiFi 링크는 훈련 데이터로 사용되는 고유 수용 및 시각 데이터를 전송하며, 로봇이 어려움을 겪을 때 원격 조작자가 개입하여 제어한다.
   3. 연결 상태가 좋지 않으면 양방향 트래픽이 모두 저하된다.
   4. 가정에서는 벽과 다른 장애물로 인해 약한 지점과 데드존이 발생하며, 일반적인 라우터는 핸드오프에 적합하지 않다.
   5. 혼잡도 문제도 있는데, 가정은 보통 공유 광섬유를 사용하므로 이웃집에서 넷플릭스를 시청하면 로봇이 가장 활발하게 작업하는 시간에 링크에 부담을 줄 수 있다.
   6. 이러한 조건에 대처하기 위해 위브는 가정 환경에 어떤 변경도 요구하지 않는다(새 라우터나 추가 액세스 포인트 불필요).
   7. 이는 모든 적응을 로봇 자체에 맡긴다는 것을 의미한다.

## 5. 네트워킹 문제 해결 (The Networking Wall)
대부분의 로봇 배포가 온보드 추론을 유지하는 주된 이유는 네트워크 문제 때문이다. 이러한 네트워킹 문제는 해결 가능하며, 해결될수록 더 많은 배포가 오프로드 방식으로 전환될 것이다.

### 5.1. 네트워크 문제의 본질
<img alt="" src="https://substackcdn.com/image/fetch/$s_!VJdy!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dec7d04-90d5-4e6e-ba0a-5c0de9e68d0d_1290x1676.png" width="1290" height="1676">
<figcaption>출처: X</figcaption>

1. **오프디바이스 정책의 어려움**
   1. 로봇 모델을 오프디바이스로 실행하는 것은 매우 어렵다.
   2. 세 가지 주요 문제가 오프디바이스 정책을 어렵게 만든다.
2. **구현 (Embodiment) 문제**
   1. 물리적 계층에서 로봇은 금속으로 만들어지고 움직이며, 모터와 전자기기가 전송하려는 주파수와 동일한 주파수에서 노이즈를 방출한다.
   2. 로봇 섀시는 자체 신호를 차단하고 반사하며, 방향 변화는 안테나 위치를 바꾸고, RF 조건은 전송 간에 동적으로 변한다.
3. **네트워크 인프라 문제**
   1. WiFi 및 5G 인프라는 로봇 공학을 염두에 두고 설계되지 않았다.
   2. 넷플릭스 스트리밍과 같은 다운링크 중심의 정지된 장치에는 잘 작동하지만, 로봇은 넷플릭스 크기의 비디오 피드를 데이터센터로 스트리밍하면서 움직인다.
   3. 이는 업링크 문제로, 기존 인프라는 다운링크를 중심으로 구축되었다.
   4. 넷플릭스에는 가끔 패킷 손실이나 지연 시간 급증이 괜찮지만, 로봇 공학에서는 사고로 이어질 수 있다.
   5. 기존 액세스 포인트, 칩셋, 알고리즘은 로봇 공학에 적합하지 않다.
      1. 우선순위가 역전되어 있고, 업링크 MIMO는 거의 지원되지 않으며, UDP 스트림의 신뢰성을 위한 중복성이 없고, 액세스 포인트 간 저지연 핸드오프가 없으며, 업링크 스케줄링은 부차적인 고려 사항이다.
      2. 모든 것이 결정적이어야 할 때 통계적이다.
   6. 공유 광섬유 환경에서는 이웃이 넷플릭스를 켜는 것이 휴머노이드 로봇의 작동에 치명적일 수 있다.
4. **환경 문제**
   1. 이는 핵심 과제이며, 오프디바이스 컴퓨팅이 실행될 수 있는 곳과 없는 곳을 결정한다.
   2. 자율 주행은 온디바이스가 엄격히 요구되는 대표적인 예시이다.
      1. 커버리지 영역이 방대하고, RF 조건에 대한 제어가 거의 없으며, 차량이 빠르게 움직여 지연 시간 예산이 거의 없고 빈번한 액세스 포인트 핸드오프가 필요하다.
      2. 운전은 휴머노이드 노동보다 학습 문제가 더 간단하므로 모델이 온디바이스에 적합하다.
      3. 따라서 컴퓨팅은 온디바이스에 탑재되고, 오프디바이스 스택은 느리고 저주파 루프인 함대 관리로 축소된다.
   3. 오프디바이스 컴퓨팅을 위한 환경적 전제 조건은 RF 제어가 가능한 작거나 중간 크기의 구조화된 공간이다.
      1. 자율 주행은 이러한 조건을 충족하지 못하지만, 가정과 공장은 충족한다.
      2. 그러나 여전히 환경 문제는 크다. 벽, 금속, 다른 전자기기가 RF 조건에 영향을 미친다.
      3. 집에서 식기세척기를 켜거나 공장에서 중장비를 가동하면 RF 환경이 변하거나 데드존이 생길 수 있다.
   4. 액세스 포인트 배치는 매우 중요하며, 시간이 지남에 따라 환경이 어떻게 변할지 예측해야 한다.
   5. 액세스 포인트 간 이동은 핸드오프를 의미하며, 일반적인 라우터는 핸드오프 동안 100ms에서 몇 초 동안 침묵한다.
   6. 이는 조작 도중에 발생하여 정책을 중단시키거나 원격 조작자를 지연시킬 수 있다.
   7. 복구에는 몇 초가 더 걸릴 수 있으며, 그 사이에 휴머노이드 로봇이 넘어질 수도 있다.
   8. 가정에서 신호 차단기 및 반사체의 배치는 예측 불가능하며, 모든 집은 다른 RF 퍼즐이다.
   9. 공장은 더 구조화되어 있지만, 금속 랙, 모터 및 기계의 간섭, 매일 이동하는 재고 및 장비, 동일한 업링크 시간을 놓고 경쟁하는 수십 대의 로봇 등 더 많은 방해 요소가 있다.

### 5.2. 네트워킹 문제 해결 방안
1. **일반적인 엔지니어링 해결책**
   1. 모델을 오프디바이스 추론에 대비하는 것은 모델의 계층 구조, 컴퓨팅 요구 사항, 수행해야 할 작업, 동작 공간, 구동하는 구현체에 따라 달라지는 미묘한 문제이다.
   2. 현재 발생하는 문제 중 일부는 일반적인 엔지니어링으로 해결할 수 있다.
   3. 예를 들어, 전송 계층은 종종 수정된 WebRTC를 사용한다.
      1. 재전송 없는 UDP, 여러 안테나를 통한 반복으로 신뢰성 확보, 패킷 중요도에 대한 애플리케이션 계층 인식, 그리고 무엇보다 최신성 유지가 핵심이다.
      2. 이러한 기술은 이미 개발되어 있으며, 노하우는 보편화되어 있다.
2. **네트워크 벽을 넘기 위한 4가지 핵심 문제 해결**
   1. 네트워크 벽은 전송 계층이나 일련의 일반적인 엔지니어링 문제가 아니다.
   2. 기존 하드웨어의 문제에 기반하며, 기존 인프라를 넘어 오프디바이스 모델을 안정적으로 만들 수 있는 네 가지 어렵고 영향력 있는 문제가 있다.
3. **환경 개선 (로봇이 아닌 환경부터)**
   1. 가장 효과적인 해결책은 액세스 포인트이다.
   2. 로봇 공학의 액세스 포인트는 다운링크 중심의 고정 클라이언트를 위한 소비자 및 기업 액세스 포인트와 반대되는 기능을 수행해야 한다.
   3. **로봇 인식 업링크 스케줄링**: 로봇 업링크는 가정 또는 공장 트래픽보다 먼저 스케줄링되어야 한다. 각 로봇은 채널 경쟁 대신 고정된 주기로 예약된 슬롯을 얻으며, 스케줄러는 로봇이 실행하는 것을 알아야 한다.
   4. **위치 인식 빔포밍**: 액세스 포인트는 각 로봇의 위치와 이동 방향을 알아야 하며, 이동에 반응하거나 클라이언트가 고정되어 있다고 가정하는 대신 미리 조향, 스케줄링 및 핸드오프를 수행해야 한다.
   5. **중앙 집중식 타이밍**: 사이트당 하나의 타이밍 권한이 무선으로 모든 로봇에 보장되어 분배되어야 하므로, 함대 전체의 관측이 동일한 클록을 공유한다.
   6. **멀티링크 작동**: 여러 링크를 동시에 실행하여(대역 및 WiFi와 5G를 가로질러), 동일한 관측을 복제하거나 분할하여 신뢰성을 높이고 지연 시간을 줄인다.
   7. **클린 스펙트럼**: 가능한 경우 6GHz 대역을 사용한다. 혼잡하지 않고 채널 폭이 넓어 재전송 없는 전송이 현실적이다.
   8. **빠른 멀티 액세스 포인트 핸드오프**: 실제 건물에는 하나 이상의 무선 장치가 필요하며, 로밍은 관측 주기 내에 완료되어야 한다. 200ms의 핸드오프는 여러 프레임 손실을 의미한다.
   9. **배치 최적화**: 하드웨어만큼 배치도 중요하다. 로봇의 작업 경로를 따라 RF 조사를 하고, 데드존을 매핑하며, 로봇의 일반적인 높이와 방향에 맞춰 안테나 방향을 선택해야 한다.
   10. **WiFi와 5G의 공존**: WiFi는 가정과 대부분의 공장 환경에서 빠르고 부하를 감당할 수 있어 지배적일 것이다. 5G는 야외 경로, 더 넓은 현장, WiFi 혼잡을 제어할 수 없는 위치를 채울 것이다. 이 둘은 하나의 스케줄러 아래 공존하며, 로봇은 이들 간에 빠르게 페일오버할 수 있어야 한다.
   11. **네트워크 제공업체와의 협력**: 현장이 통신사에 의존하는 경우, 마지막 단계는 업링크 우선순위 지정 및 GPU 클러스터로의 전용 광섬유에 대해 네트워크 제공업체와 협력하여 스케줄링된 경로가 액세스 포인트에서 끝나지 않도록 하는 것이다.
4. **부하 축소 (Shrink the load)**
   1. 네트워크는 대역폭이 제한적이다. 네트워크 벽을 넘는 또 다른 방법은 전송해야 할 데이터 양을 줄이는 것이다.
   2. 이미지 센서가 로봇 업링크의 거의 전부이므로, 이는 네트워킹 문제 이전에 인지 문제이다.
5. **업링크 최대화 (Maximize the uplink)**
   1. 로봇 공학은 모든 무선 칩셋이 설계된 트래픽 패턴을 역전시킨다.
   2. 메인보드는 이를 위해 구축되어야 한다.
      1. 소비자 모듈이 제공하는 1~2개 스트림 대신 4x4 업링크 MIMO를 사용해야 한다.
      2. 다운링크 처리량보다 업링크 처리량을 위해 칩셋을 선택해야 한다.
      3. 무선 통신을 위해 구축된 운영 체제와 액세스 포인트의 스케줄에 참여하는 무선 장치(자신의 슬롯을 알고 주기에 맞춰 채우며, 그 외에는 조용히 유지)가 필요하다.
   3. 이러한 규칙적인 작동은 스케줄링을 결정론적으로 만들며, 메인보드와 액세스 포인트가 공동 설계될 때만 가능하다.
   4. 어느 한쪽만으로는 링크에 질서를 부여할 수 없다.
6. **모든 것을 하나의 클록으로 동기화 (Everything on one clock)**
   1. 데이터센터 GPU는 배치 효율성이 증가함에 따라 온디바이스 컴퓨팅보다 비용 효율적이며, 배치는 합리적인 지연 시간 예산을 맞추기 위해 많은 로봇의 관측이 시간 정렬되어 도착해야 한다.
   2. 모든 것이 동일한 클록에서 실행되어야 한다.
   3. 메인보드의 우수한 수정 발진기와 함대 전체의 무선 시간 동기화를 통해 서브 밀리초 동기화가 가능하다.
   4. 이를 통해 현장의 모든 로봇이 동일한 주기에 맞춰 데이터를 캡처, 인코딩 및 전송한다.
   5. GPU 오케스트레이션은 이 주기를 중심으로 구축된다.
      1. 스케줄러는 다음 관측 프레임이 언제 도착할지 알고, 이를 위한 컴퓨팅 자원을 예약하며, 프레임이 완료되는 즉시 실행한다.
      2. 지연된 관측은 다음 배치로 이동하며, 지연 시간 예산은 대기하는 대신 추론에 사용된다.
   6. 메인보드가 스케줄을 유지하고, 액세스 포인트가 이를 강제하며, 부하를 줄이는 인지 스택과 결합하면, 지연 시간을 늘리지 않고 대규모로 배치 처리를 수행하는 시스템이 구축된다.
   7. 이는 모델을 오프디바이스로 실행하는 전체 경제적 근거가 된다.
