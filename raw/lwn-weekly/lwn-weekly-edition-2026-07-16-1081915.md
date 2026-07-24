# LWN.net Weekly Edition for July 16, 2026 — 한국어 기술 번역

- 원문 URL: https://lwn.net/Articles/1081915/bigpage
- Edition URL: https://lwn.net/Articles/1081915/
- Article ID: 1081915
- 기준: 최신호 “LWN.net Weekly Edition for July 23, 2026”(1083123)은 유료/최신 가능성이 높아 제외하고, 공개 접근 확인이 된 직전 무료판 “July 16, 2026”(1081915)을 번역했습니다.
- 생성 시각(UTC): 2026-07-24T00:53:10Z

## 전체 요약

- 이번 호는 AI scraper bot이 공개 웹 출판사에 주는 부담, residential proxy를 통한 우회, 그리고 open web 방어 전략을 깊게 다룹니다.
- 커널 쪽에서는 io_uring의 lockless MPSC FIFO queue, BPF 기반 exploit 차단, BPF의 직접 packet 송신 등 Linux runtime/network/security 경계의 변화가 핵심입니다.
- LSFMM+BPF Summit 보도는 filesystem testing과 stable kernel patch 검증 문제를 통해 “재현 가능한 테스트”와 “유지보수 현실” 사이의 균형을 보여줍니다.
- 사용자 공간 개발 기사로는 Kitty terminal emulator의 GPU/프로토콜 확장, QBE 1.3의 작은 compiler backend 전략, Rust/Debian/shim/SUSE 보안 소식이 포함됩니다.
- Brief items, announcements, security updates, kernel patches 목록은 원문의 링크 구조를 유지해 후속 확인이 가능하도록 보존했습니다.

---

### 2026년 7월 16일 LWN.net 주간 에디션에 오신 것을 환영합니다(/Articles/1083080/)

이 버전에는 다음과 같은 기능 콘텐츠가 포함되어 있습니다.
                   


                   


  
- 스크레이퍼 상황에 대한 업데이트(/Articles/1080822/): 봇과 게시자 간의 전투가 계속됩니다.

  
- io_uring에 대한 잠금 없는 MPSC FIFO 대기열(/Articles/1081871/): 7.2에서 io_uring에 대한 성능 향상을 살펴봅니다.

  
- 2026 Linux 스토리지, 파일 시스템, 메모리 관리 및 BPF Summit(/Articles/lsfmmbpf2026/)에서 계속해서 다루어집니다.

  


	


	
- 파일 시스템 테스트 주제(/Articles/1082342/): 파일 시스템 테스트, 특히 안정적인 커널을 목표로 하는 패치에 대한 토론입니다.

	
- BPF를 사용하여 악용으로부터 실행 중인 커널 보호(/Articles/1081546/): John Fastabend는 새로운 악용에 대해 취약한 커널을 신속하게 면역시키는 전략에 대해 논의합니다.
	
  	
- BPF에서 직접 패킷 보내기(/Articles/1081696/): BPF가 나가는 네트워크 요청을 할 수 있도록 하는 기능입니다.

	

  
- Kitty가 마우스를 쫓습니다(/Articles/1080821/): Kitty GPU 기반 터미널 에뮬레이터를 살펴보세요.

  
- QBE 1.3: 메타프로그래밍, 성능 및 크로스 플랫폼 지원(/Articles/1080519/): LLVM 및 GCC와 같은 컴파일러 백엔드에 대한 가벼운 대안입니다.






이번 주 버전에는 다음 내부 페이지도 포함되어 있습니다.
                       


                       



- 간략한 항목(/Articles/1081917/): 커뮤니티 전체의 간략한 뉴스 항목입니다.


- 공지사항(/Articles/1081918/): 뉴스레터, 컨퍼런스, 보안 업데이트, 패치 등.


                       


이번 주 버전을 즐겨 주시고, 언제나처럼 LWN.net을 지원해 주셔서 감사합니다.


댓글(게시되지 않음) (/Articles/1083080/#Comments)





### 스크레이퍼 상황 업데이트 (/Articles/1080822/)

#### 요약
- AI/LLM scraper traffic is still rising and is now difficult to distinguish from ordinary residential-user traffic.[^scraper-proxy]
- Residential proxy networks, bot operators, and customers form a layered market that lets abusive scraping hide behind real ISP addresses.
- LWN frames the problem as an open-web sustainability issue: rate limiting and blocking help tactically, but policy and accountability are needed too.[^open-web]



조나단 코베트(Jonathan Corbet) 작성 2026년 7월 10일
           
2025년 초에 발행된 우리 기사 "AI 스크레이퍼 봇 재앙에 맞서 싸우기(/Articles/1008897/)"에서는 대규모 언어 모델 및 관련 프로젝트에 대한 훈련 데이터를 검색하기 위해 웹사이트가 광범위하게 스크랩되는 문제를 논의했습니다.  이 활동은 사이트의 트래픽을 압도합니다.  해당 기사가 게재된 지 1년이 넘었지만 문제는 여전히 커지고 있습니다.  비밀스러운 행위자들에 의한 사이트 공격이 새로운 수준에 도달했으며, 공개 웹을 유지 관리하기가 점점 더 어려워지고 있습니다.  이 트래픽은 어디에서 발생하며 이에 대해 무엇을 할 수 있습니까?





#### 주거용 프록시



작년에 설명했듯이 스크레이퍼 공격은 인터넷 전반에 걸쳐 수많은 소스에서 발생합니다.  몇 시간 동안 수백만 개의 고유한 IP 주소에서 요청이 조율되는 것을 보는 것은 드문 일이 아니며 각 IP 주소는 최대 2~3회 사이트에 도달합니다.  사용자 에이전트 필드와 같은 공격자가 제어하는 ​​데이터는 완전히 허구입니다. 각 히트는 웹 브라우저를 사용하는 또 다른 사람처럼 보이도록 만들어졌습니다.  차이점을 알 수 있는 방법이 있습니다. 예를 들어 봇은 일반적으로 이미지나 CSS를 가져오지 않습니다. 그러나 결정이 내려지면 문제의 주소는 다시 사용되지 않습니다.  그 시점에서 주소를 차단하는 것은 시간 낭비일 뿐입니다.




이 트래픽은 주로 중앙 명령 및 제어 노드가 지시하는 주거용 및 모바일 네트워크에서 발생합니다.  소프트웨어는 제어 노드에서 명령을 받고, 요청 시 웹 페이지를 가져오고, 결과 데이터를 다시 컨트롤러로 전달하는 일반 시스템에 설치됩니다.  대부분의 경우 이러한 활동은 해당 장치 소유자의 인지나 동의 없이 발생합니다.  "주거용 프록시"라는 용어는 이러한 방식으로 사용되는 시스템을 설명하는 데 사용됩니다.



웹 사이트를 공격하기 위해 주거용 프록시 네트워크를 운영하는 몇 가지 다른 유형의 운영자(적어도 표면적으로는)가 있습니다.  한 가지 유형은 일종의 맬웨어로 손상된 시스템에서 스크레이퍼를 실행하는 순전히 범죄입니다.  올해 초 Google은 IPIDEA(https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network)라는 봇 네트워크를 중단하고 이러한 작업이 어떻게 작동하는지에 대한 많은 정보를 제공했습니다.  IPIDEA의 폐쇄는 여기 LWN의 스크레이퍼 트래픽의 상당한 감소와 관련이 있습니다. 몇 달 동안 상황은 비교적 평화로웠습니다.  하지만 그 평화의 기간은 이제 끝났습니다.



최근에는 미디어 스트리밍 장치가 악성 스크레이핑 소프트웨어의 주요 전달자로 확인되었습니다(https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/).  때로는 장치가 소스에서 손상될 수도 있습니다. 다른 경우에는 보안이 취약하고 사후에 쉽게 손상될 수 있습니다.



두 번째 종류의 운영자는 어느 정도 합법성을 가장하고 "윤리적으로 소스가 제공되는" IP 주소를 제공하면서 좀 더 공개적으로 작업합니다.  Bright Data라는 회사는 이들 중 가장 눈에 띄는 회사 중 하나입니다. 웹 사이트 액세스 제어 및 트래픽 제한을 우회하는 능력을 즐겁게 광고합니다. Bright Data는 "무료" VPN 서비스를 제공합니다. 필요한 것은 사용자가 Bright Data에 사용자 장치를 통해 트래픽을 라우팅하는 기능, 즉 회사의 주거용 프록시 네트워크의 일부가 되는 기능을 제공하는 것입니다.  이 VPN을 사용하는 모든 전화기나 기타 장치는 웹 사이트를 공격하는 데 사용되는 또 다른 엔드포인트가 됩니다.



이러한 유형의 연산자에 대한 다른 예도 많이 있습니다. 종종 그들은 앱 개발자가 자신의 서비스에 연결할 수 있고 사용자의 네트워크 연결을 가로채는 대가를 받을 수 있는 라이브러리를 제공합니다.  그 중 한 명은 LWN에서 SDK용 광고를 실행하는 것에 대한 문의를 보냈습니다. 그것은 짧은 대화라고 말하는 것으로 충분합니다.  일반적으로 이러한 회사는 예를 들어 "GDPR 규정 준수"를 광고하는 등 합법성을 추구하는 회사부터 지나치게 천박한 회사까지 다양합니다.



이러한 주거용 프록시 네트워크는 웹 사이트 스크래핑에 사용되지만 이러한 운영자는 수백만 대의 장치가 연결되는 네트워크에 관계없이 리소스에 액세스하는 코드를 실행할 수 있다는 점을 강조할 가치가 있습니다.  이러한 유형의 액세스가 스크래핑에만 사용된다고 가정하는 것은 기껏해야 순진한 것입니다.



물론, 핵심 사업으로 모델을 개발하는 유명 기업도 있습니다.  이 회사들은 자체적으로 스크래핑을 수행합니다. 쉽게 발생할 수 있는 트래픽은 사용자 에이전트 필드에서 명확하게 식별되며 일반적으로 robots.txt와 같은 측정값을 관찰합니다.  그들 역시 2003년에 작성된 기사가 마지막 날에 어떻게든 변경되었을 수 있다는 이론에 따라 전체 사이트를 반복적으로 긁어낼 것입니다. 그러나 수백만 개의 시스템에서 압도적인 양의 트래픽을 생성하지 않으며 가장 큰 문제도 아닙니다.



명확하지 않은 것은 누가 주거용 프록시를 사용하고 있는지입니다. 누군가가 웹 사이트에 이러한 공격을 실행하기 위해 돈을 지불하고 있습니다.  프론티어 모델 기업이 이러한 네트워크를 사용하고 있다는 증거는 없습니다.  하지만 만약 그들이 그렇게 하고 있는 것으로 밝혀진다면, 세계적인 놀라움의 증가는 거의 기록되지 않을 것입니다.  이러한 회사는 어떻게든 모델에 정보를 제공하고 있으며, 훈련 데이터를 얻는 방법에 대해 공개하지 않고 있으며, 콘텐츠 제작자 또는 운영에 대해 우려할 수 있는 사람에 대한 존경심의 수준이 두각을 나타내지 않습니다.



그러나 모든 공개 모델에는 엄청난 수의 비밀 모델이 있어야 합니다.  많은 기업들이 확실히 자체 구축을 시도하고 있습니다. 결국, 우리는 AI가 세계를 장악할 것이며 그 경쟁에서 앞서 나가는 회사는 막대한 돈의 가치가 있을 것이라는 확실한 정보를 얻었습니다.  많은 국가에는 자체 모델을 작업하고 훈련 데이터를 찾을 수 있는 곳이면 어디든 찾아다니는 비밀스러운 정부 기관이 있을 것입니다.  대규모 범죄 조직(정부와는 별개)도 아마도 자신만의 모델을 갖고 싶어할 것입니다. 이러한 도구는 무기로 간주되며 군비 경쟁이 진행 중입니다.  인터넷 전체가 총격전을 벌이고 있습니다.





#### 개방형 인터넷 방어



이에 대응하여 웹사이트 운영자들은 실제 사용자에게 미치는 영향을 최소화하면서 사이트를 방어하기 위해 안간힘을 쓰고 있습니다.  작업 증명을 요구하여 스크레이퍼를 막으려는 Anubis(/Articles/1028558/)가 이제 널리 퍼져 있습니다.  다른 사이트는 상용 서비스를 사용하는데, 때때로 "당신이 인간임을 증명하세요" 버튼을 통해 자신을 알립니다.  또는 사이트에서는 사용자에게 가로등이 있는 사각형(단, LED 전구만 있음)을 선택하거나, 퍼즐 조각을 배치하거나, ​​스페이스바를 누른 상태에서 노래를 흥얼거리도록 강요합니다.  많은 사이트 기능이 로그인 게이트나 페이월 뒤에 배치되었습니다.  일부 사이트에서는 아이오카인(/Articles/1056953/)과 같은 도구를 사용하여 스크래퍼로 전송된 데이터를 적극적으로 오염시키려고 시도합니다.



이러한 메커니즘을 설정하고 유지해야 하는 필요성과 사용자가 웹 사이트에 액세스하기 위해 이에 대처해야 하는 요구 사항 모두 스크래퍼와 이를 지불하는 사람들이 전 세계에 부과하는 무거운 세금을 구성합니다.



최근 LWN은 지금까지 가장 강력한 스크레이퍼 공격을 받았습니다.  구현된 방어 덕분에 사이트는 대부분의 실제 독자가 눈치 채지 못할 정도로 트래픽을 잘 처리했습니다. 사이트를 방어하기 위해 우리가 취한 조치를 설명해 달라는 요청이 있었습니다. 분명한 이유로 우리는 이에 대해 자세히 논의하고 싶지 않습니다. 이 수준에서도 역시 군비경쟁이다.



우리가 말할 수 있는 것은 실제 독자들에게 미치는 영향을 최대한 최소화하려고 노력했다는 것입니다.  우리는 Anubis와 같은 도구를 사용하지 않았습니다. 부분적으로는 사이트에 접속하려는 사람들에게 짜증나는 지연을 초래하기 때문이기도 하지만, 부분적으로는 스크래퍼가 결국에는 사이트를 우회할 방법을 찾는 것이 불가피해 보이기 때문이기도 합니다.  실제로 이미 일어나고 있는 몇 가지 징후가 있습니다.  작업을 수행할 다른 사람의 컴퓨터가 수백만 대에 달하는 경우 작업 증명 요구 사항은 큰 장애물이 아닙니다.



또한 합법적인 검색 엔진, 인터넷 아카이브 및 기타 유사한 그룹의 운영을 방해하지 않기를 바라는 바램도 있습니다.  예를 들어 일부 사이트에서는 주요 검색 엔진에 해당 사이트에 대한 액세스 권한을 부여하기 위해 명시적인 허용 목록을 추가할 수 있습니다.  그러한 조치는 이미 우리에게 제대로 도움이 되지 않으며 피해야 하는 독점을 더욱 강화하는 효과가 있습니다.  우리는 지금까지 이에 성공했습니다.



우리는 사이트의 일부를 공격적으로 최적화했으며 사이트가 공격을 받는 동안 비용이 많이 드는 작업을 최소화하는 방법을 찾았습니다. 익명의 독자는 때때로 이러한 조치 중 하나를 접할 수 있습니다. 로그인한 사용자는 그렇지 않습니다.  흥미롭게도 사이트가 공격을 받을 때의 응답 시간은 방어 조치가 휴면 상태인 평온한 시간보다 더 나은 경우가 많습니다.  하지만 우리는 문제가 해결되었다고 생각하는 것보다 더 나은 것을 배웠습니다. 현재 조치가 더 이상 효과적이지 않으면 다음 단계를 고려해야 합니다.



7월 2일, Google은 미국 연방 수사국(Federal Bureau of Investigation) 및 기타 기관과 협력하여 "NetNut"이라는 주거용 프록시 네트워크를 폐쇄했다고 발표했습니다(https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks).  당분간 그 조치는 실제로 스크레이퍼 공격 수준을 다소 줄이는 데 성공한 것으로 보입니다.  하지만 경험에 따르면 이러한 반가운 평화는 오랫동안만 지속될 것입니다.  Google은 이제 Play 스토어에서 NetNut에 감염된 앱을 확인할 것이라는 점을 지적하기 위해 노력하고 있지만 모든 주요 공급업체는 주거용 프록시 기능이 있는 앱을 앱 스토어에 넣는 것이 왜 그렇게 쉬운지에 대해 침묵하고 있습니다.



인터넷 전체가 방어벽 뒤에 갇히고, 그토록 많은 창의성을 불러일으켰던 개방형 네트워크가 사라지기 전에 보다 지속적인 해결책을 찾는 것이 좋을 것입니다.  이러한 공격을 주도하는 업계는 콘텐츠를 약탈한 후 독립적인 웹 사이트를 연기가 나는 분화구로 바꾸는 데 전혀 안주하지 않는 것 같습니다. 이러한 태도는 지구와 경제에도 적용됩니다.  하지만 우리 중 일부는 그러한 생각에 반대하고 이에 맞서 싸울 것입니다.  언젠가 운이 좋다면 세계 전체가 대규모 언어 모델과 관련 기술을 뒷받침하는 회사를 최소한의 윤리적 기준으로 유지하기로 결정할 것입니다.  하지만 그때까지 이러한 행동은 계속될 것이며 우리는 이에 맞서 스스로를 방어할 수밖에 없을 것입니다.


댓글(152개 게시) (/Articles/1080822/#Comments)





### io_uring에 대한 잠금 없는 MPSC FIFO 대기열(/Articles/1081871/)

#### 요약
- io_uring 7.2 is gaining a lockless multi-producer/single-consumer FIFO queue path aimed at reducing contention.[^mpsc]
- The design replaces spinlock-heavy enqueue behavior with atomic operations while preserving FIFO ordering for submitters.
- The practical implication is better scaling under highly concurrent async I/O workloads, especially where many threads submit to one ring.[^io-uring]



조나단 코베트(Jonathan Corbet) 작성 2026년 7월 15일
           
io_uring(https://man7.org/linux/man-pages/man7/io_uring.7.html)을 사용하는 프로세스는 많은 공을 공중에 유지하는 경향이 있습니다. 주어진 시간에 많은 작업을 진행할 수 있다는 것은 우선 해당 API의 핵심 중 일부입니다.  결과적으로 io_uring 하위 시스템은 적시에 수행해야 하는 많은 작업을 추적해야 합니다.  현재 커널에서 io_uring은 표준 커널 연결 목록 기본 요소를 사용하여 해당 작업 항목을 추적합니다.  하지만 7.2 커널 릴리스부터는 io_uring이 새로운 잠금 없는 다중 생산자, 단일 소비자(MPSC) 대기열을 사용하여 눈에 띄는 성능 향상을 가져옵니다.  무잠금 알고리즘은 까다로운 경향이 있지만 여기에 사용된 알고리즘은 상대적으로 접근하기 쉽고 이러한 알고리즘이 어떻게 작동할 수 있는지 보여줍니다.



#### 기존 방식의 단점



7.2 이전 io_uring의 작업 대기열은 커널의 잠금 없는 단일 연결 목록(https://elixir.bootlin.com/linux/v7.1.2/source/include/linux/llist.h)(llist) API를 기반으로 합니다.  이 유형의 핵심은 간단한 구조입니다.





```

    struct llist_node {
	struct llist_node *next;
    };

```




이 구조는 관심 있는 실제 데이터를 포함하는 다른 구조에 내장될 때 해당 외부 구조를 목록에 바인딩하는 링크를 포함합니다.



이 목록 유형이 성능을 위해 설계되었음에도 불구하고 io_uring에 적합하지 않은 데에는 몇 가지 이유가 있습니다.  목록은 단일 연결 목록이므로 현실적으로 헤드에서만 액세스할 수 있습니다.  생산자가 항목을 추가하고 소비자가 항목을 제거하는 목록의 경우 목록은 본질적으로 스택입니다.  io_uring의 작업 항목은 기본 공정성을 위해 수신된 순서대로 처리되어야 하므로 각 처리가 실행되기 전에 작업 대기열을 통해 순서를 반대로 전달해야 합니다.  설상가상으로 io_uring은 목록이 너무 길면 전체 목록을 처리하지 않을 수도 있지만, 순서가 거꾸로 된 나머지 항목은 단순히 작업 목록에 다시 넣을 수 없습니다.  따라서 취소되었으나 처리되지 않은 항목에 대한 별도의 목록을 유지해야 합니다. 마지막으로, 목록에 항목을 추가하려면 단일 헤드 포인터에 액세스해야 합니다. 잠금을 사용하지 않고도 수행할 수 있지만 재시도 루프가 필요합니다. 경쟁이 심한 목록의 경우 이러한 재시도(및 관련 캐시 라인 바운싱)가 손상될 수 있습니다.



이러한 문제를 해결하려면 io_uring 하위 시스템의 요구 사항에 더 적합한 데이터 구조가 필요합니다.  잠금 없이 최소한의 경합으로 목록에 작업 항목을 추가하는 여러 생산자를 처리해야 합니다.  각 목록에는 단일 소비자가 있습니다. 해당 소비자는 생산자와의 캐시 경합을 최대한 피해야 합니다.  그리고 분명히 처리 전에 목록을 다시 정렬할 필요가 없어야 합니다.





#### 잠금이 없는 MPSC 대기열



해결책은 Jens Axboe가 게시하고 Dmitry Vyukov가 제공한 알고리즘을 사용하여 게시한(/ml/all/20260612025125.1690253-1-axboe@kernel.dk) 잠금 없는 MPSC 대기열입니다.  이 큐는 여전히 struct llist_node를 사용하여 목록의 항목을 하나로 묶지만 목록의 헤드는 다음과 같습니다.





```

    struct mpscq {
	struct llist_node	*tail;
	struct llist_node	stub;
    };

```




"헤드"라는 용어는 실제로 약간 오해의 소지가 있습니다. 여기에는 목록의 헤드에 대한 포인터가 없기 때문입니다. 그것에 대해서는 나중에 다루겠습니다.  이 목록 보기는 목록의 꼬리에 항목을 추가해야 하는 생산자를 위한 것입니다.  스텁 항목은 목록에 있는 유일한 항목인 경우, 즉 목록이 비어 있는 경우에만 목록에 존재하는 감시자입니다.  목록이 초기화되면 꼬리 포인터가 스텁 항목을 가리키도록 설정됩니다.




![[빈 대기열]](https://static.lwn.net/images/2026/mpscq1.svg)




스텁 항목의 다음 포인터는 NULL로 설정됩니다.  목록의 꼬리에 노드를 추가하려면 다음 짧은 함수를 호출하면 됩니다.





```

    static inline bool mpscq_push(struct mpscq *q, struct llist_node *node)
    {
	struct llist_node *prev;

	node->next = NULL;
	prev = xchg(&q->tail, node);
	WRITE_ONCE(prev->next, node);
	return prev == &q->stub;
    }

```




새 항목의 다음 포인터는 NULL로 설정되어 목록의 끝임을 나타냅니다.  그런 다음 xchg() 호출은 목록의 꼬리 포인터에 새 항목에 대한 포인터를 원자적으로 저장하고 해당 포인터의 이전 값을 반환합니다. 빈 목록의 경우 이는 스텁 항목에 대한 포인터가 됩니다.  그런 다음 이전 목록 끝 항목(다시 말하면 스텁일 수 있음)의 다음 포인터가 새 항목으로 설정되어 해당 항목을 목록에 추가하는 작업이 완료됩니다.




![[항목이 하나인 대기열]](https://static.lwn.net/images/2026/mpscq2.svg)




여기서 주목할 가치가 있는 잠금 없는 알고리즘에는 미묘함이 있습니다. 꼬리 포인터가 새 목록 항목을 가리키면 해당 항목은 나머지 세계에서 볼 수 있습니다.  무엇보다도 이러한 가시성은 꼬리를 변경하기 전에 새 항목의 다음 포인터를 적절하게 설정해야 함을 의미합니다.  일반적으로 컴파일러나 CPU는 next 및 tail에 대한 할당 순서를 변경할 자격이 있다고 느낄 수 있으며, 이로 인해 새 노드가 완전히 초기화되기 전에 새 tail이 표시될 수 있습니다.  그러나 xchg() 작업은 전체 장벽으로 정의됩니다. 즉, 이전에 발생한 작업(예: 다음 할당)은 교환이 발생하기 전에 시스템의 나머지 부분에서 볼 수 있어야 함을 의미합니다.  장벽 작업이 없으면 두 할당 사이에 장벽을 수동으로 삽입해야 했습니다.



여러 CPU가 동시에 동일한 목록에 항목을 추가하려고 하면 xchg() 호출이 해당 항목을 직렬화하여 꼬리 포인터가 순서대로 업데이트되도록 합니다.  두 CPU가 xchg() 호출을 동시에 수행하는 경우 하나가 "승리"하여 먼저 진행되고 다른 CPU가 그 뒤를 따릅니다.  그러면 간단히 다음과 같은 목록이 생성될 수 있습니다.




![[경합 중 큐]](https://static.lwn.net/images/2026/mpscq3.svg)




각 xchg() 호출은 꼬리 포인터의 이전 상태를 반환하므로 추가할 때마다 목록의 이전 항목이 어디에 있는지 알 수 있습니다.  이를 통해 그에 따라 다음 포인터를 설정할 수 있습니다. 두 가지 추가가 완료되면 목록은 다음과 같습니다.




![[경합 후 큐]](https://static.lwn.net/images/2026/mpscq4.svg)




목록을 일관된 상태로 유지하는 데 잠금이 필요하지 않으며 재시도 루프도 필요하지 않으므로 추가 작업이 빠릅니다.  커널 컨텍스트 내에서 실행하는 동안에도 추가 작업을 수행할 수 있습니다.





#### 소비자의 시각



소비자 측에서는 소비자가 mpscq 구조와 별도로 목록 헤드 포인터를 유지 관리한다는 사실부터 시작하여 조금 더 복잡합니다. 이는 목록의 첫 번째 항목 주소를 보유하는 간단한 struct llist_node 포인터입니다.  이렇게 분리하는 목적은 헤드 포인터와 테일 포인터가 별도의 캐시 라인에 배치되어 생산자와 소비자 사이의 캐시 경합을 방지하는 것입니다.  목록의 첫 번째 항목을 제거하기 위해 소비자는 해당 헤드 포인터를 다음으로 전달합니다.





```

    static inline struct llist_node *mpscq_pop(struct mpscq *q,
					   struct llist_node **headp);

```




이 기능을 준비해야 하는 경우가 몇 가지 있습니다.  목록이 처음 생성되면 (위에 표시된 것처럼) 빈 상태에서 목록 헤드 포인터에는 스텁 항목의 주소가 포함됩니다.  목록에 추가해도 헤드 포인터가 변경되지 않으므로 첫 번째 항목이 목록에서 제거될 때까지 해당 상황이 유지됩니다.  위에 표시된 목록에서 아직 제거된 항목이 없다고 가정해 보세요. 별도의 헤드 포인터를 사용하면 그림은 다음과 같습니다.




![[헤드 포인터가 있는 큐]](https://static.lwn.net/images/2026/mpscq5.svg)




해당 사례의 항목 제거는 다음과 같이 처리됩니다.





```

	struct llist_node *head = *headp, *next;

	if (head == &q->stub) {
	    head = READ_ONCE(head->next);
	    if (!head)
		return NULL;
	    q->stub.next = NULL;
	    *headp = head;
	}

```




목록에 첫 번째 항목을 추가하면 해당 첫 번째 항목에 대한 스텁의 다음 포인터가 설정된다는 점을 기억하십시오. 여기서 코드는 해당 포인터를 확인합니다.  NULL이면 목록이 비어 있으므로 NULL이 반환됩니다.  그렇지 않으면 헤드는 스텁의 다음 필드 값으로 진행되며 이후에 NULL로 설정됩니다.




![[스텁이 제거된 큐]](https://static.lwn.net/images/2026/mpscq6.svg)




스텁은 다시 비워질 때까지 목록 관리에서 더 이상 역할을 수행하지 않습니다.



이제 목록에 항목이 있다는 것이 확인되었으므로 다음 확인은 그것이 마지막 항목인지 확인하는 것입니다.  부정적인 경우, 추가 항목이 있으면 헤드 포인터는 해당 항목의 다음 항목으로 이동할 수 있으며 헤드 항목에 대한 포인터가 반환됩니다.





```

	next = READ_ONCE(head->next);
	if (next) {
	    *headp = next;
	    return head;
	}

```




이런 방식으로 품목이 반품된 후의 상황은 다음과 같습니다.




![[항목 하나가 제거된 대기열]](https://static.lwn.net/images/2026/mpscq7.svg)




그러나 다음 포인터가 NULL이면 목록에 더 이상 항목이 없으며 꼬리 포인터는 다시 한 번 스텁으로 설정되어야 합니다.  하지만 반전이 있습니다. 동시에 목록에 새 항목을 추가하는 제작자가 있을 수도 있습니다.  따라서 목록을 빈 상태로 재설정하려면 비교 및 ​​교환 작업이 필요합니다.





```

	if (try_cmpxchg(&q->tail, &head, &q->stub)) {
	    *headp = &q->stub;
	    return head;
	}
	return NULL;

```




try_cmpxchg() 호출은 tail 포인터를 head 포인터(목록의 한 항목을 가리킨다는 것을 기억하세요)와 비교합니다.  둘이 동일하면 꼬리가 스텁을 가리키도록 원자적으로 설정되어 목록이 처음에 표시된 빈 상태로 재설정됩니다. 그런 다음 목록의 마지막 항목을 반환합니다.



그러나 try_cmpxchg() 호출이 실패하면 소비자는 다른 생산자와 경쟁하고 해당 생산자는 소비자 뒤에서 꼬리 포인터를 변경했습니다.  이 경우 NULL이 반환되고 소비자가 다음에 다시 시도할 때까지 마지막 항목이 목록에 남아 있습니다.  소비자는 꼬리 포인터가 스텁 항목을 겨냥하는지 확인하여 이 경우를 목록이 비어 있는 경우와 구별할 수 있습니다.





```

    static inline bool mpscq_empty(struct mpscq *q)
    {
	return READ_ONCE(q->tail) == &q->stub;
    }

```




이는 전체 API를 설명합니다.  코드는 io_uring/mpscq.h(https://elixir.bootlin.com/linux/v7.2-rc1/source/io_uring/mpscq.h)에서 찾을 수 있습니다. 이 시점에서는 lib/ 아래에 배치되어 나머지 커널에서 사용할 수 없습니다.  물론 io_uring 외부의 관심 있는 사용자가 등장하면 변경될 수 있습니다.



7.2부터 이 새로운 대기열 유형은 io_uring 내의 몇 가지 다른 작업 목록에 사용됩니다.  이 패치(/ml/all/20260612025125.1690253-4-axboe@kernel.dk)에 설명된 대로 결과는 오버헤드 감소로 성능이 크게 향상되었습니다. 즉, 더 많은 작업이 더 빠르게 수행되는 동시에 커널에서 실행하는 데 소요되는 시간이 줄어듭니다.  io_uring 코드도 다소 단순화되었습니다. 더 이상 목록을 뒤집거나 작업 목록에서 제거되었지만 아직 실행되지 않은 별도의 작업 항목 목록을 유지할 필요가 없기 때문입니다. 모두 합하면 때가 된 최적화인 것처럼 보입니다.



(후기: 이 주제는 무시될 위험이 있었지만 프로젝트 리더 수준 이상의 구독자가 사용할 수 있는 LWN 공개 주제 페이지(/TopicList/)에서 충분한 투표를 받았기 때문에 다시 살펴보기로 결정했습니다. 이 개발이 기사를 쓸 가치가 있다고 생각한 LWN 독자들에게 감사드립니다.)


댓글(5개 게시) (/Articles/1081871/#Comments)





### 파일 시스템 테스트 주제 (/Articles/1082342/)

#### 요약
- LSFMM+BPF discussions focused on how filesystem tests should cover stable-kernel fixes without creating unrealistic maintenance burdens.[^xfstests]
- Developers debated regression-test expectations, reproducer quality, and how to avoid test suites becoming a gate that blocks legitimate stable patches.
- The operational theme is that filesystem correctness requires both broad automated tests and human judgment about risk.



제이크 엣지 2026년 7월 15일
           
LSFMM+BPF(/Articles/lsfmmbpf2026/)




파일 시스템 개발자 모임이 파일 시스템 테스트에 대해 논의하는 것은 놀라운 일이 아닙니다. 이는 수년 동안 Linux 스토리지, 파일 시스템, 메모리 관리 및 BPF 서밋(https://events.linuxfoundation.org/lsfmmbpf/)의 중심이었으며 2026 서밋도 예외는 아니었습니다.  이번에는 Ted Ts'o가 토론을 주도했습니다. 그는 안정적인 커널에서 ext4의 회귀 증가에 대한 인식과 이를 줄이기 위해 수행할 수 있는 작업을 포함하여 몇 가지 다른 주제를 제기했습니다.  수년에 걸쳐 서밋에서 열린 (/Articles/789225/) 다른 (/Articles/896523/) 유사한 (/Articles/937830/) 세션(/Articles/982099/)과 마찬가지로 테스트 입력 및 출력에 대한 공동 작업에 많은 관심이 있었지만 해당 정보를 중앙 집중화하는 방법을 찾는 것은 지금까지 파일 시스템 커뮤니티에서 벗어나었습니다.







Ts'o는 최근 안정적인 커널에서 더 많은 ext4 회귀를 발견했다는 점을 언급하면서 시작했습니다.  그 이유 중 하나는 ext4 개발자가 Folio 지원과 같은 기능을 개발해 왔기 때문입니다. 이러한 패치 중 일부에는 "자동화에 의해 반드시 선택되지 않는 미묘한 종속성 요구 사항이 있습니다".



![[Ted Ts'o]](https://static.lwn.net/images/2026/lsfmb-tso-sm.png) (/Articles/1082682/)




또 다른 요인은 패치가 LLM의 도움으로 더 자주 이전 커널로 백포트되고 있다는 점이라고 그는 말했습니다.  그래서 그는 6.1 및 6.6 안정 커널로 백포트된 기능이 해당 커널에 버그를 일으키는 것을 보았습니다.  일부 버그로 인해 fstests 제품군(https://github.com/kdave/xfstests)의 특정 테스트에서 커널이 충돌했습니다.  백포트된 패치가 12개가 넘었기 때문에 "실제로 이러한 문제를 찾는 것은 상당히 고통스러웠습니다". 그는 안정적인 커널을 위한 자동화된 패치 선택을 선택하지 않은 다른 파일 시스템에서도 이러한 문제가 발생하는지 궁금했습니다.





그는 안정적인 커널용 패치를 모니터링하는 테스트 실행기를 설정했습니다. 해당 패치가 포함된 커널에서 fstest를 실행합니다.  그러나 그는 결과를 검토하고 이를 기준선과 비교하여 회귀를 찾을 시간이 없었습니다.  자동화할 수는 있지만 아직 도달하지 못했습니다.





Ts'o는 자신의 테스트 실행기에서 fstest로 테스트할 수 있는 모든 파일 시스템("대부분")을 안정 커널 패치 후보와 함께 테스트하기 위해 혼합에 추가할 수 있다고 말했습니다. 그는 그렇게 할 수 있는 능력이 있으며 안정적인 백포트를 사용하여 더 많은 파일 시스템을 테스트할 수 있도록 이메일을 통해 보고서를 제공할 수 있습니다.  그는 또한 두 실행의 테스트 출력을 비교하여 둘 사이의 회귀를 찾는 프로그램을 개발할 Python 프로그래머를 찾고 있다는 말을 내놓았습니다.





Ts'o는 xfstests-bld(https://github.com/tytso/xfstests-bld#xfstests-bld) 테스트 어플라이언스의 자동화에도 시간을 투자했습니다.  그는 테스트를 실행하는 동안 커널이 충돌하는 상황을 포함하여 Git 이분법 수행에 대한 지원을 추가했습니다.  그는 관심 있는 사람이 그 설정을 할 수 있도록 기꺼이 도와줄 것입니다.  Kdevops(https://github.com/linux-kdevops/kdevops#table-of-contents)는 파일 시스템 개발자가 사용할 수 있는 또 다른 옵션입니다.  그는 LLM의 버그 보고서와 패치로 인해 훨씬 ​​더 많은 활동이 있을 것이라고 의심합니다. "테스트는 우리가 최신 상태를 유지할 수 있는 유일한 방법입니다."





그런 다음 그는 다른 사람들이 파일 시스템 테스트에 대한 아이디어를 공유할 수 있는 기회를 열었습니다.  한 참석자는 테스트 매트릭스와 테스트 결과의 공유 데이터베이스를 제안하면서 아이디어가 이전에 나왔다는 점을 지적했습니다. 다른 사람들도 동의했지만 테스트에 사용된 환경(실제 하드웨어, 가상 머신, 다양한 종류의 스토리지 등)으로 인해 테스트 결과를 비교하기가 어렵다는 점을 지적했습니다.





Chuck Lever는 kdevops 프로젝트에 fstest 실행 결과 아카이브(https://github.com/linux-kdevops/kdevops#kdevops-tests-results)가 있는데 이것이 좋은 출발점이 될 수 있다고 말했습니다. 그는 또한 커널 네트워킹 하위 시스템(netdev)이 추적 중인 패치와 함께 데이터를 저장할 수 있는 기능이 있는 패치워크(https://patchwork.kernel.org/)에 CI(지속적 통합) 테스트 결과를 저장한다는 사실도 방금 알아냈습니다. Netdev는 CI 결과를 저장하기 위해 이를 사용하고 있습니다. (자세한 내용은 패치 자동화를 위한 Netdev 인프라 위키(https://github.com/linux-netdev/nipa/wiki/)에서 확인할 수 있습니다.)





Ts'o는 Konstantin Ryabitsev에게 lore.kernel.org(https://lore.kernel.org/)에 보관될 테스트 결과에 대한 메일링 리스트 설정에 대해 문의했다고 말했습니다. 1년 정도 전에 요청이 이루어졌을 때 Ryabitsev는 생성될 수 있는 데이터의 양 때문에 자동화된 테스트 결과를 그런 식으로 저장하는 것에 열광하지 않았습니다. 다른 사람들이 그런 목록에 가치가 있을 수 있다고 생각한다면 Ts'o는 그 아이디어를 다시 제기할 수 있다고 말했습니다.





두 명의 참석자가 회사에서 보고서를 테스트하는 데 사용되는 대시보드에 대해 설명했습니다.  Ts'o는 그러한 성격의 모든 오픈 소스 노력이 fstests 메일링 리스트(https://lore.kernel.org/fstests/)에 게시되어야 한다고 제안했습니다. 왜냐하면 이를 사용할 다른 개발자가 있을 수 있기 때문입니다.  테스트 결과를 모니터링하는 데 사용할 수 있는 대시보드를 사용하여 테스트 결과에 대한 중앙 데이터베이스를 개발하는 것은 모든 정상회담에서 나오는 아이디어라고 Lever는 말했습니다.  그는 이것이 "문샷"일 수도 있다고 생각했지만 아마도 Linux 재단이 이를 실현하는 데 도움을 줄 수 있을 것입니다.  Ts'o는 재단이 이미 KernelCI 프로젝트(https://kernelci.org/)의 문제를 해결하고 있다고 믿고 있지만 이러한 노력은 파일 시스템 테스트에 적합하지 않다고 생각합니다.


Ts'o는 KernelCI와 같은 프로젝트를 만드는 것보다 단순히 도구를 개발하기 위해 일회성 자금을 확보하는 것이 더 쉬울 수 있지만 유지 관리를 위해 지속적인 자금 조달이 필요한 파일 시스템 테스트를 위해 더 쉬울 수 있다고 말했습니다.  그는 누군가가 바이브 코딩한 프로토타입을 중심으로 필요한 사항에 대해 파일 시스템 개발자의 동의를 얻으면 프로덕션에 바로 사용할 수 있는 도구 버전을 만들기 위한 자금이 조달될 수 있다고 제안했습니다.  "우리는 오프라인에서 머리를 맞대어야 합니다."





Ts'o가 제기하고 싶었던 또 다른 항목은 그가 유지 관리하고 있는 테스트 실패 파일이었습니다.  이는 실행해서는 안 되는 테스트를 나열하지만 테스트가 통과하지 못하는 커널 버전을 기반으로 하는 fstests 삭제 파일과 같습니다. 이는 파일 시스템 유형별 오류뿐만 아니라 파일 시스템 유형과 테스트 시나리오의 조합을 기반으로 한 오류도 다룹니다.  다양한 LTS(장기 안정) 커널 버전에서 작동하지 않고 해당 버전에서는 절대 작동하지 않을 가능성이 높은 테스트를 문서화합니다.





그는 배포판이 사용 중인 커널에 해당하는 이전 버전의 fstest를 선택하는 경향이 있다고 말했습니다.  그러나 그는 여러 버전의 fstest를 유지하고 싶지 않으며 최신 테스트를 실행하는 것이 가치가 있다고 생각합니다. fstests의 최신 버전에서는 버그가 수정된 커널 버전을 지적하는 경우가 있는데, 이는 유용한 백포트를 나타낼 수 있습니다.  최신 fstests 버전을 실행하면 결과에 더 많은 노이즈가 발생합니다. 예를 들어 6.1 또는 6.6과 같이 통과하지 못하는 테스트가 더 많기 때문입니다.  이것이 그가 테스트 실패 파일을 유지하는 이유입니다.





해당 파일은 현재 그의 테스트 어플라이언스에 보관되어 있지만 다른 곳으로 이동하여 공동으로 유지 관리해야 하는지 궁금했습니다.  그의 초점은 ext4에 있으므로 테스트 실패 파일에서 잘 다루어집니다. Lever는 테스트 실패 정보를 fstests 저장소에 추가할 것을 제안했지만 대신 테스트를 수정하기 위한 푸시백이 있을 수 있다고 언급했습니다. Ts'o는 fstests 관리자가 "어떤 버전에서 수정된 사항"을 추적하는 데 관심이 없다는 점을 분명히 했다고 말했습니다.  서로 다른 사람들이 서로 다른 방식으로 테스트를 사용하고 있기 때문에 어느 정도 의미가 있습니다. Ts'o는 LTS 커널만 추적하는 반면, 배포판에서는 업스트림 커널 버전과 다를 수 있는 커널을 추적하려고 합니다.





크리스티안 브라우너(Christian Brauner)는 때때로 통과하는 "불안정한" 테스트 문제를 제기했습니다.  Ts'o는 테스트 결과를 불안정하게 표시할 수 있는 내부 버전의 하네스가 있다고 말했습니다. 실패하면 세 번 더 실행되고 모두 실패하는 경우에만 보고됩니다.  그는 그 기능이 유용하기 때문에 공개 버전에 추가하려고 했지만 시간을 찾지 못했습니다.





Ts'o는 다양한 사람들이 서로 다른 커널 버전에 대한 자신만의 말소 파일 버전을 갖고 있으므로 모두 함께 정리하는 것이 좋을 것이라고 말했습니다. fstests는 올바른 위치가 아니기 때문에 아마도 커널이 그럴 것이라고 그는 제안했습니다.  이로써 토론이 마무리되고 세션이 종료되었습니다.





[여기서 오류가 발생한 경우 사과드리고 싶습니다.  방의 음향은 청각과 녹음 모두에 문제가 있었습니다. 오해와 오해가 생길 수 있습니다.]



댓글(6개 게시) (/Articles/1082342/#Comments)





### BPF를 이용한 익스플로잇으로부터 실행 중인 커널 보호(/Articles/1081546/)

#### 요약
- The article covers a proposal to use BPF as a rapid kernel-exploit mitigation mechanism before a full patched kernel can be deployed.[^bpf-mitigation]
- BPF programs could recognize and block exploit behavior at vulnerable kernel interfaces, buying administrators time during emergency response.
- The idea is powerful but sensitive: mitigation logic must be safe, verifiable, and narrow enough not to break legitimate workloads.



작성자: Daroc Alden, 2026년 7월 13일
           
LSFMM+BPF(/Articles/lsfmmbpf2026/)




Cisco는 맞춤형 커널을 실행하는 회사의 여러 장치에 보안 패치를 배포할 때 몇 가지 특이한 문제를 안고 있습니다. John Fastabend는 2026년에 BPF로 공격을 방지하는 작업에 대해 이야기했습니다.

Linux 스토리지, 파일 시스템, 메모리 관리 및 BPF Summit(https://events.linuxfoundation.org/lsfmmbpf/). 이 기술은 커널 취약점에 대응하는 데 필요한 시간을 크게 줄일 수 있지만 커널에 더 많은 후크가 추가되지 않으면 완전히 효과적이지 않습니다.





네트워크 스위치는 광범위한 하드웨어를 포괄한다고 Fastabend가 시작되었습니다. 작은 단일 랙 시스템부터 거대한 고속 장치까지. Cisco가 지원하는 각 플랫폼에는 다음을 사용하여 사용자 정의 커널을 구축하는 자체 커널 팀이 있습니다.

욕토(https://www.yoctoproject.org/). 언제든지 해당 팀은 다양한 커널(다행히도 대부분 안정적인 커널)을 지원하고 있다고 그는 덧붙였습니다. 널리 배포되고 사용자 정의 커널을 갖춘 인터넷 연결 장치는 모두 공격자의 유혹적인 표적이 됩니다.



![[존 패스트벤드]](https://static.lwn.net/images/2026/john-fastabend-lsfmmbpf-small.png) (/Articles/1081694)




Cisco는 분명히 보안 업데이트를 게시하지만 문제를 식별하고 수정 사항을 작성하고 새 빌드를 생성하고 테스트하여 고객에게 제공한 다음 스위치를 업데이트하는 데 시간이 걸립니다. 특히 스위치를 재부팅하면 네트워크 중단이 발생할 수 있기 때문입니다. 이러한 중단으로 인해 고객은 가동 중지 시간을 계획하고 관리해야 하며 전체 프로세스는 발견부터 마지막 ​​취약한 시스템에 패치를 적용하는 데 수개월이 걸릴 수 있습니다. Fastabend 작업의 목표는 BPF를 사용하여 실시간으로 공격을 관찰한 다음 재부팅하지 않고도 요청 시 공격을 처리할 수 있도록 하는 것이었습니다. 이상적으로는 전체 프로세스가 단 몇 분만에 완료될 것이라고 그는 말했습니다. "우리는 한동안 거기에 있지 않을 것이지만 그것이 꿈일 것입니다."






오픈 소스 BPF 기반 모니터링 및 시행 도구인 Tetragon(https://tetragon.io/)은 실행 중인 시스템에 대한 "많은 데이터"를 수집하는 데 사용됩니다. 언제든지 스위치의 모니터링 인프라는 어떤 프로그램이 어떤 시간에 실행되었는지, 어떤 네트워크 연결이 이루어졌는지 보여줄 수 있습니다. 해당 데이터는 시계열 데이터베이스에 저장됩니다. Tetragon은 현재 작동 상태를 유지하기 위해 사용자 공간 에이전트에 의존하고 있지만 Fastabend와 그의 동료들은 공격자가 사용자 공간 에이전트를 죽이더라도 BPF 구성 요소가 살아남을 수 있도록 노력해 왔습니다. 그는 새로운 CVE가 발견되면 해당 데이터베이스를 확인하여 악용되었는지 여부를 확인할 수 있기를 원한다고 설명했습니다. 또한 데이터를 사용하여 데이터 유출이나 명령 및 제어 서버 연결과 같은 공격 증상을 확인할 수도 있습니다.





익스플로잇이 식별되면 BPF에서 직접 차단할 수 있습니다. 익스플로잇을 트리거하기 위해 특정 시스템 호출이 필요한 경우 BPF는 시스템 호출의 반환 값을 재정의하여 작업을 거부할 수 있습니다. 내부 커널 함수에 대한 인수가 올바른지 확인하기 위해 추적점을 사용하는 것도 가능합니다. Fastabend 팀은 두 가지를 모두 사용합니다.

uprobes (/Articles/499190/) 및

이에 대해서는 kprobes(/Articles/132196/)를 참조하세요. 그러나 이러한 프로브는 반환 값 변경을 안정적으로 허용하지 않으므로 이를 위해 Linux 보안 모듈(LSM) 후크가 사용됩니다.







Andrii Nakryiko는 이 설계에 의해 초당 몇 개의 이벤트가 확인되고 잠재적으로 차단되는지 물었습니다. 네트워크 패킷의 라우팅은 대부분 전용 하드웨어에 의해 수행되므로 커널은 제어 평면 트래픽과 사용자 공간 애플리케이션만 관리하면 된다고 Fastabend는 설명했습니다. 전체적으로 스위치가 수십억 개의 패킷을 이동하더라도 수십억 개가 아닌 초당 수백 또는 수천 개의 이벤트만 있습니다.





한 가지 문제는 Fastabend 팀이 인라인 기능에서도 작동하기 위해 프로브를 사용하기를 원한다는 것입니다. 디버깅 기호를 사용하고 원시 오프셋에 프로브를 설정하면 가능합니다. Cisco에는 모든 커널 패키지를 생산하는 데 사용되는 빌드 팜이 있다고 그는 설명했습니다. 빌드 머신은 BTF 및 일반 디버깅 기호를 모두 포함하여 모든 빌드의 빌드 ID와 디버깅 정보를 저장합니다. 해당 정보는 고객 문제를 디버깅하는 데 사용되지만 배포된 커널의 구조와 관련된 라이브 커널 패치 또는 BPF 프로그램을 작성하는 것도 가능하게 합니다.





Jakub Sitnicki는 부분적으로 인라인된 함수에 프로브를 연결하는 데 문제가 있다고 언급했습니다. 해당 함수가 인라인된 위치에 대한 정보가 현재 커널의 BTF에 포함되어 있지 않기 때문입니다. 그러나 문제는 작업 중입니다. Alan Maguire는 이 주제가 회의 다음 날에 제안한 세션 중 하나에서 다루어질 것이라고 말했습니다.




#### 악용 차단




그런 다음 Fastabend는 최근의 영향을 차단하는 데 사용할 수 있는 BPF 프로그램의 예를 보여주었습니다.

복사 실패 취약점(https://copy.fail/). 프로그램은 버그를 유발하는 방식으로 호출될 때 splice() (https://man7.org/linux/man-pages/man2/splice.2.html) 시스템 호출이 오류를 반환하도록 만들었습니다. 그의 팀은 이러한 BPF 프로그램을 "방패"라고 부릅니다. 그는 이와 같은 작업이 일반 커널 라이브 패치를 사용하면 기술적으로 가능하다고 인정했습니다. 하지만 Cisco는 동시 제품 라인이 너무 많고 다양한 안정적인 커널이 실행되고 있기 때문에 모두 패치하려면 개발자 시간에 막대한 투자가 필요합니다. BPF를 사용하면 일반적으로 동일한 프로그램이 지원되는 모든 커널에서 실행될 수 있습니다. 한 번만 작성한 다음 각 커널에서 자동으로 테스트하여 어떤 문제도 발생하지 않는지 확인하면 됩니다.





BPF 쉴드는 작동할 때 훌륭하지만 가끔 딸꾹질이 발생합니다. Fastabend 팀은 영향을 받는 커널 하위 시스템에 보호막을 구축할 관련 후크가 없는 CVE를 찾는 경우가 많다고 그는 말했습니다. 가장 최근에는 문제의 원인에 가까이 접근할 수 있는 편리한 위치가 없는 악용 가능한 use-after-free 버그가 있었습니다. 팀은 결국 버그를 유발할 수 있는 시스템 호출을 연결하기로 결정했지만 이로 인해 코드가 더 복잡해졌습니다.





따라서 Fastabend가 이와 같은 노력을 지원하기 위해 커널에서 보고자 하는 주요 변경 사항은

ALLOW_ERROR_INJECTION() (https://docs.kernel.org/fault-injection/fault-injection.html#error-injectable-functions), 커널의 오류 주입 프레임워크의 적용을 받을 수 있는 함수를 표시하는 데 사용되는 매크로입니다. 일반적으로 테스트에 사용되는 동안 프레임워크를 사용하면 커널 프로그래머가 사용자 정의 BPF 프로그램으로 내부 함수의 반환 값을 재정의할 수 있으며 이는 Fastabend의 사용 사례와 완벽하게 일치합니다. 불행하게도 커널 함수의 하위 집합만 오류 주입과 함께 사용하도록 표시되었습니다. 이상적으로 그는 BPF를 사용하여 0과 비교되는 정수를 반환하고 해당 오류가 스택 위로 전파되는 모든 함수의 반환 값을 수정할 수 있기를 원합니다. 이 기준에 맞는 기능이 많이 있다고 그는 말했다. 그는 이 모든 것을 위한 LSM 후크가 있어야 한다고 말했습니다. Fastabend는 이러한 기능을 BPF에서 쉽게 연결할 수 있는지 물었습니다.





Nakryiko는 오류 처리 코드가 복잡하기 때문에 이러한 변경 작업을 수동으로 수행해야 한다고 생각했습니다. Alexei Starovoitov는 Rust 코드에서 컴파일러가 생성한 정리 논리가 예측 가능한 구조를 가지고 있다는 점을 고려하면 Rust 코드에 대해 자동으로 수행하는 것이 가능해야 한다고 제안했습니다. C 코드의 경우 취약성 보고서를 제출하는 사람들에게 관련 LSM 후크도 도입하도록 요청할 것을 제안했습니다. 나는 사용을 제안했다

Coccinelle(/Articles/315686/)을 사용하여 변경하세요.





수동 프로세스로 끝난다면 대상으로 삼아야 할 가장 중요한 위치는 커널의 넷링크 코드일 것이라고 Fastabend는 생각했습니다. 어떤 이유로든 그의 팀은 커널의 해당 영역을 표적으로 삼는 많은 공격을 목격했습니다.





취약점으로부터 보호하기 위해 내부 커널 기능을 연결하는 기술은 확실히 다른 Linux 커널 사용자에게도 유용합니다. 그가 보여준 방패는 단지 몇 줄의 코드에 불과하며, 커널이 충분히 적용되면 이러한 종류의 간단한 수정이 어떻게 회사나 배포판이 훨씬 덜 번거롭게 여러 커널 버전에 걸쳐 취약점 완화를 배포할 수 있는 방법을 제공하는지 쉽게 알 수 있습니다. 즉, 관련 영역에 LSM 후크를 추가하는 작업은 큰 변화가 될 것이며 LSM 유지 관리 담당자가 작업을 승인하는 경우 시간이 다소 걸릴 수 있습니다.



댓글(7개 게시) (/Articles/1081546/#Comments)

### BPF에서 직접 패킷 전송하기 (/Articles/1081696/)

#### 요약
- A proposed helper would let BPF programs initiate outgoing network packets directly rather than only observing or redirecting traffic.[^bpf-net]
- The use cases include kernel-resident monitoring, control-plane responses, and faster feedback paths for networking tools.
- The security model matters because packet generation from BPF expands what in-kernel programmable logic can do on the network.


           Daroc Alden
2026년 7월 14일
           
LSFMM+BPF (/Articles/lsfmmbpf2026/)





Tetragon (https://tetragon.io/)은 BPF 기반 보안 모니터링 도구로, 실행 중인 kernel의 여러 측면을 감시하고 사용자가 지정한 policy를 적용한다. 데이터는 user-space process로 보내고, 이 process가 네트워크의 중앙 monitoring service로 전달한다. 하지만 이는 취약점이 된다. 공격자가 Tetragon의 user-space agent를 죽이면 상황을 제대로 보고하지 못한다. Song Liu, Mahé Tardy, Liam Wiseheart는 2026

Linux Storage, Filesystem, Memory-Management, and
BPF Summit (https://events.linuxfoundation.org/lsfmmbpf/)에서 user-space agent 없이 동작하도록 만드는 작업을 소개했다.





Wiseheart는 Meta에서 일하지만 Tetragon 자체를 담당하지는 않는다고 설명했다. 다만 BPF program이 모든 user-space component와 분리된 채 실행되는 동일한 문제에 관심이 있다. 현재 Meta는 system boot 시 program을 pinning하여 user-space component가 죽어도 program 제거는 막지만, 문제를 완전히 피하지는 못한다.





Tardy는 Tetragon(그리고 아마 Wiseheart의 유사 program)이 ring buffer를 통해 user space와 통신한다고 설명했다. user-space component는 주로 ring buffer의 message를 읽어 remote server로 보내고, reply를 받은 뒤 다시 ring buffer에 넣는다. BPF program이 remote server와 직접 통신할 수 있다면 훨씬 효율적일 것이다. BPF program은 이미 들어오는 network packet을 intercept할 수 있으며, 빠진 부분은 BPF에서 데이터를 직접 보내는 기능이다.





2025년에 Tardy 일행은

splice() (https://man7.org/linux/man-pages/man2/splice.2.html)를 사용한 해결책 (/Articles/1022034/)을 발표했지만 인기가 없었다. 당시 Andrii Nakryiko는 synchronous option이 BPF에 잘 맞지 않을 것이라고 봤다. 그 세션의 kernel developer들은 kernel이 원래 serial port로 보낼 log message를 remote location으로 보내게 하는

netconsole (https://docs.kernel.org/networking/netconsole.html) code를 쓰라고 제안했다.





“해 봤는데요,” Tardy는 말했고, 잘 작동하는 듯하다.

Netpoll (https://elixir.bootlin.com/linux/v7.1.2/source/include/linux/netpoll.h#L3)은 netconsole 뒤의 kernel infrastructure로, 어떤 context에서든 kernel code가 packet을 보내게 하며 normal networking stack을 우회한다. 그래서 kfunc를 작성해 이를 위한

patch set (https://lwn.net/ml/all/20260309131635.302424-1-mahe.tardy@gmail.com/)를 보냈고, 그해 후반에
updated version (https://lwn.net/ml/all/20260511085344.3302-1-mahe.tardy@gmail.com/)도 냈다. 사용 시 user-space loading program이 network address 정보를 BPF program에 넘기고, program은 bpf_netpoll_create()로 netpoll context를 만든다. 이어 bpf_netpoll_send_udp()로 임의 데이터를 담은 UDP packet을 보낸다.





Tardy는 간단한 demo도 보였다. virtual machine을 boot하고 host machine으로 간헐적인 ping을 보내는 BPF program을 설치하는 demo agent를 시작한 다음, 별도 terminal에서 message가 도착하는 모습을 보였다. user-space agent를 죽인 뒤에도 ping은 계속 도착했다. 새 packet-sending function은 kernel의 기존 cryptography API와 결합해 encrypted packet을 보낼 수도 있다. 현재 demo는 단순 symmetric key를 쓰지만 더 복잡한 scheme도 가능하다.





netpoll 방식이 작동하긴 하지만 “UDP는 evil이라는 feedback도 받았습니다”라고 Liu는 말했다. netpoll이 보낸 packet은 normal networking stack을 우회하므로, BPF program이 지나치게 많은 traffic을 보내면 contention을 제한할 실질적 방법 없이 다른 process의 bandwidth를 빼앗을 수 있다. 한 참석자는 어떤 kernel context에서도 보낼 수 있는 netpoll 기능이 꼭 필요하지는 않으며, BPF interface가 kernel thread를 생성해 normal 방식으로 packet을 보내면 networking code가 traffic에 모든 normal networking setting을 적용할 수 있다고 제안했다.





발표 열 시간 전 기준으로, Liu는 UDP 대신 TCP traffic을 보내는 version을 실험했다고 말했다. networking 담당자들은 이를 더 편안하게 여겼지만, kernel-thread 기반 해법처럼 atomic context에서는 kfunc를 사용할 수 없게 된다. 이어 UDP와 TCP의 장단점에 대한 긴 토론이 있었고, 다수는 UDP 쪽이었다. Alexei Starovoitov는 특히 netpoll이 이미 kernel에서 쓰이고 있으므로 TCP를 선호할 이유가 없다고 봤다. John Fastabend는 Tetragon use case에는 UDP가 충분하다고 생각했다. Wiseheart는 netpoll이 normal networking stack을 우회하므로 깨진 security module hook 등의 문제가 netpoll 기반 logging을 방해하기 더 어렵다고 지적했다.





Starovoitov는 이 견고성의 사례를 들었다. 어느 때 NIC가 부분적으로 고장 나 packet을 받을 수 없었고, 이로 인해 전체 networking stack이 망가진 적이 있었다. 그러나 netpoll code는 그 device에서 계속 전송됐다. 다른 참석자는 netpoll 기반 해법의 진짜 문제는 host의 bandwidth management뿐이지만 심각한 문제라고 반박했다. Starovoitov는 Netpoll이 NIC에서 single queue만 쓰므로 문제가 될 만큼은 아닐 것이라고 봤다. Liu는 networking maintainer들을 설득하는 데 도움을 요청했고, Starovoitov는 돕겠다고 했다.





Daniel Borkmann은 netpoll을 지원하는 NIC driver가 얼마나 되는지, 아니면 모든 driver에서 동작하는 generic utility인지 물었다. Starovoitov는 driver의 약 90%가 의도적으로 혹은 단순히 고장 나서 netpoll을 지원하지 않는다고 생각했다. Meta에서 정기적으로 쓰는 driver만 확실히 올바르게 처리한다고 했다.





아무도 이에 이견을 보이지 않아 netpoll이 정말 최선인지 불분명해졌다. 아쉽게도 이때 세션 시간이 끝났다. 이후 Tardy 일행은 작업을 계속했으며, 7월 6일 BPF program이 netpoll 대신 UDP kernel socket을 생성하고 쓰게 하는 새
patch set (https://lwn.net/ml/all/20260706093525.13030-1-mahe.tardy@gmail.com/)을 게시했다.



Comments (4 posted) (/Articles/1081696/#Comments)





### Kitty chases the mouse (/Articles/1080821/)

#### 요약
- Kitty is presented as a GPU-accelerated terminal emulator with low latency, rich protocol extensions, and an ecosystem of “kittens”.[^terminal-gpu]
- The article explains why terminal emulators are now interface platforms, not merely text renderers.
- Compatibility trade-offs remain: nonstandard protocols can improve UX but require coordination with applications.



           

2026년 7월 9일
           

이 글은 Lee Phillips가 기고했다
           




Kitty (https://sw.kovidgoyal.net/kitty/)는 Linux, macOS, BSD에서 실행되는 terminal emulator이며, 속도 (https://sw.kovidgoyal.net/kitty/performance/)와 image support, 고급 font handling 같은 기능으로 유명하다. 활발히 개발되고 있으며, 최근 major release (https://sw.kovidgoyal.net/kitty/changelog/#id5)는 새 수준의 mouse support를 더했다. 여기서는 그 기능 일부와 이 program을 text-based application의 platform으로도 쓸 수 있는 방법을 살펴본다. Kitty는 GPLv3로 배포되는 free software다.



#### 기능

![[Kitty logo]](https://static.lwn.net/images/2026/kitty-logo.svg)




Kitty는 GPU 기반 terminal emulator다. 오늘날 인기 있는 여러 terminal emulator처럼 GPU를 써서 순식간에 수 megabyte의 text를 screen에 쏟아낼 충분한 bandwidth를 얻는다. cat으로 거대한 file을 실수로 표시했을 때 반가운 장점이며, GPU는 scrollback buffer도 매끄럽게 탐색하게 한다. Kitty는 key를 누른 시점부터 해당 character가 screen에 나타날 때까지의 시간인 low latency를 목표로 설계됐다. 사용자가 흔히 의식하지는 않지만 terminal jockey (/Articles/751763/)의 만족감과 행복에 큰 영향을 미치는 속성이다.





Kovid Goyal (https://kovidgoyal.net/)은 사용하던 terminal emulator의 속도에 불만을 느껴 [YouTube interview video] (https://www.youtube.com/watch?v=8PYLPC3dzWQ&list=PLZWMav2s1MZRMrfCtT3HYhvuAmo_KIl2y&t=590s) 더 빠른 것을 만들기로 하면서 kitty를 만들었다. 이후 colored underline부터 기존 program이 지원하지 않지만 자신이 원한 기능을 추가했다.





Kitty는 configuration file로 철저히 customize할 수 있다. 사용자는 수십 가지 command에 keyboard shortcut이나 mouse action을 정의할 수 있다. option은 일반적인 appearance와 shortcut setting을 훨씬 넘어선다. 예를 들어 performance tuning (https://sw.kovidgoyal.net/kitty/conf/#conf-kitty-performance)을 위한 parameter도 여럿 노출한다. 최근 kitty version에서는 configuration file을 저장하면 setting 변경이 즉시 적용된다.





kitty의 font handling (https://sw.kovidgoyal.net/kitty/conf/#fonts)은 유연하다. 단 bitmap font는 포함하지 않는데, 임의로 scale할 수 없어서 kitty가 지원하지도 앞으로 지원하지도 않기 때문이다 (https://github.com/kovidgoyal/kitty/issues/97#issuecomment-373970232). Kitty는 어떤 monospace TrueType 또는 OpenType font도 사용할 수 있고 shortcut으로 즉시 size를 바꿀 수 있다.





Ligature도 지원하며(다행히 disable 가능), OpenType의 alternative glyph shape와 variable font (https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)도 지원한다. normal, italic, bold text마다 별도의 font를 정할 수 있다. configuration file에서 사용자는 kitty (https://sw.kovidgoyal.net/kitty/conf/#opt-kitty.symbol_map)에 어떤 Unicode codepoint 또는 range에 어떤 font를 쓸지 지시할 수도 있다. 즐겨 쓰는 coding font의 Unicode coverage가 좋지 않거나 glyph마다 다른 font가 더 잘 rendering할 때 유용하다. font metric, underline과 strikethrough의 position 및 thickness를 조절하는 parameter도 있으며, kitty가 text를 background color 위에 합성하는 방식 (https://sw.kovidgoyal.net/kitty/conf/#opt-kitty.text_composition_strategy)까지 조절할 수 있다.





사용자가 허용하면 kitty는 terminal에서 실행 중인 application이 고른 색이 foreground와 background 사이의 contrast를 부족하게 할 때 이를 override할 수 있다. 나는 이를 켜 두는데 Vim highlight에 지나치게 비슷한 foreground와 background color를 부주의하게 정하는 경우 등을 막아 준다. 문서 (https://sw.kovidgoyal.net/kitty/kittens/choose-fonts/)의 말처럼 “Terminal 애호가는 하루 종일 text를 바라보므로 text rendering을 정확히 맞추는 일이 매우 중요하다.”



#### Kittens



Kitty에는 program에 추가 기능과 customization을 제공하는 “kittens (https://sw.kovidgoyal.net/kitty/kittens_intro/)”라는 보조 program들이 함께 들어 있다. keyboard shortcut으로 호출하거나 shell에서 원하는 kitten을 argument로 지정해 kitten command를 실행할 수 있다. argument 없이 kitten command를 실행하면 사용 가능한 kitten 목록이 표시된다. 각 항목의 간단한 문서는 -h flag로 볼 수 있다. 예를 들어 ssh kitten 사용 안내는 kitten ssh -h다 (https://sw.kovidgoyal.net/kitty/kittens/ssh/).





Kitty는 user extension을 염두에 두고 설계됐다. 이를 위해 kittens는 kitty를 제어하고 kitty window 및 scrollback buffer의 text에 접근하게 하는 API (https://sw.kovidgoyal.net/kitty/kittens/custom/)를 사용하는 external Python program으로 구현된다.





사용 가능한 kitten은 많다. 여기서는 kitty에 번들된 특히 유용한 것 몇 가지를 언급하겠다. ssh kitten은 system의 ssh command를 감싸 remote connection이 kitty와 잘 동작하게 한다. 주로 필요한 terminfo (https://man7.org/linux/man-pages/man5/terminfo.5.html) setting을 전송하고 remote machine에서 shell integration(뒤에서 설명)을 enable하며, 기존 connection 재사용 같은 편의 기능도 제공한다. 설치된 사용 가능 font를 목록과 preview로 보여 주는 kitten (https://sw.kovidgoyal.net/kitty/kittens/choose-fonts/)도 있다. theme picker (https://sw.kovidgoyal.net/kitty/kittens/themes/)는 너무나 많은 contributed option 중 preset color theme를 interactive하게 고르게 한다. icat (https://sw.kovidgoyal.net/kitty/kittens/icat/) kitten은 아래에서 설명할 “terminal graphics protocol”을 사용해 animated GIF를 포함한 일반 format의 image file을 terminal 안에 직접 표시한다. image file은 local file일 수도 HTTP(S)나 FTP로 가져온 것일 수도 있으며 remote machine에 kitty가 설치돼 있다면 SSH 위에서도 직접 동작한다.





show-key (https://www.mankier.com/1/kitten-show-key) kitten은 xev (https://manpages.debian.org/stretch/x11-utils/xev.1.en.html) program과 비슷하게 key press에 대응하는 keycode를 보여 준다. clipboard kitten (https://sw.kovidgoyal.net/kitty/kittens/clipboard/)은 SSH를 통해 image 등 여러 data type을 copy/paste하게 한다. screenshot 아래처럼 Unicode character를 interactive하게 검색하고 선택하는 unicode input kitten (https://sw.kovidgoyal.net/kitty/kittens/unicode_input/)도 있다.



![[Unicode input kitten]](https://static.lwn.net/images/2026/kitty-unicode.png)





Kitty에는 screen에 보이는 URL을 key 하나로 사용자 web browser에서 여는 “hints mode (https://sw.kovidgoyal.net/kitty/kittens/hints/)”가 있다. 인기 있는 Vimium (https://vimium.github.io/) browser extension처럼 동작하며 내부적으로 kitten을 쓴다. kitty의 remote control (https://sw.kovidgoyal.net/kitty/remote-control/)은 많은 option을 가진 kitten으로 제공되어, 특정 window에 text를 보내고 property를 바꾸며 window와 tab을 열고 닫는 등의 일을 할 수 있다.





kitty program에는 문서가 “shell integration (https://sw.kovidgoyal.net/kitty/shell-integration/)”이라고 부르는 기능이 있다. Zsh (https://www.zsh.org/), fish (https://fishshell.com/), Bash (https://www.gnu.org/software/bash/) 같은 유명 shell 대부분에서 동작하고, Nushell (https://www.nushell.sh/), Xonsh (https://xon.sh/) 같은 이색 shell에는 third-party integration이 있다. Shell integration은 command line 작업을 편하게 하는 function과 shortcut 모음이다. scrollback buffer 내용, 가장 최근 command의 output, 또는 현재 command를 기본 editor로 여는 command가 있다. kitty command의 tab completion도 제공하며, clone-in-kitty처럼 shell environment에 넣는 여러 utility function도 제공한다. 이 function은 모든 environment variable을 포함한 현재 shell environment를 새 window나 tab으로 clone한다. 또 다른 유용한 utility인 edit-in-kitty는 local editor로 SSH의 remote file을 편집하게 한다.



#### 새 protocol



Kitty는 escape code 집합으로 구현한 여러 새 terminal protocol (https://sw.kovidgoyal.net/kitty/protocol-extensions/)을 만들었다. 이 protocol 일부는 앞서 말한 icat command를 구동하는 terminal graphics protocol (https://sw.kovidgoyal.net/kitty/graphics-protocol/) 같은 kitty trick을 가능하게 한다. 오래된 sixel protocol (https://rioterm.com/docs/features/sixel-protocol)에 익숙한 독자는 왜 kitty가 이를 쓰지 않았는지 궁금할 수 있다. kitty 제작자가 sixel graphics가 지원하지 않는 몇몇 기능을 원했기 때문이다 (https://github.com/kovidgoyal/kitty/issues/2511#issuecomment-609543803). 추가 kitty protocol은 더 유연한 keyboard handling (https://sw.kovidgoyal.net/kitty/keyboard-protocol/)을 구현하는 것처럼 다른 legacy protocol도 개선한다.





그 밖의 새 protocol 또는 extension은 colored/styled text underline, clipboard로 여러 type의 data(image, text style) 복사, mouse pointer shape 변경, GUI file navigator와 file을 mouse drag-and-drop (https://sw.kovidgoyal.net/kitty/kittens/dnd/)하는 기능을 구현한다. 마지막 기능은 최신 major release에 들어온 향상된 mouse support로 가능해졌다.





이 protocol 일부는 다른 project에도 채택됐다. 따라서 Ghostty (https://ghostty.org/), Wezterm (https://github.com/wezterm/wezterm/issues/986) 및 여러 terminal emulator 사용자는 kitty의 terminal graphics protocol 혜택을 누린다. terminal emulator 외에도 긴 목록의 terminal-based application과 editor plugin이 이를 쓴다. 내가 Neovim (http://neovim.io/)에서 쓰는 enhancement 중 하나는 snacks plugin (https://github.com/folke/snacks.nvim#-snacksnvim)의 image component다. Markdown buffer에서 image 삽입 Markdown syntax를 보면 graphic을 embed하거나 선택적으로 popup window에 표시한다. 또한 Typst (https://typst.app)와 LaTeX (https://www.latex-project.org/)(물론 설치돼 있어야 한다)를 호출해 math input을 처리하고 결과를 buffer에 직접 표시한다. plugin은 image를 포함하는 Typst와 LaTeX syntax도 이해해 이를 embed한다. Typst가 매우 빠르므로 (/Articles/1037577/) 사용자는 Typst document 편집 중 math의 realtime preview를 얻는다.



![[Kitty, Typst, and snacks]](https://static.lwn.net/images/2026/kitty-typst-snacks.png)





유용하다고 느낀 kitty terminal graphics protocol의 마지막 application 두 가지도 언급하겠다. gnuplot (/Articles/961003/)과 Julia (/Articles/1044280/) 모두 graphical output을 read-eval-print loop(REPL)에 직접 embed할 수 있다. 전자는 built-in “terminal”을, 후자는 KittyTerminalImages (https://github.com/simonschoelly/KittyTerminalImages.jl?tab=readme-ov-file#kittyTerminalImagesjl) Julia package를 쓴다. REPL에서 plot을 만든 command와 나란히 plot 기록을 두는 것이 유용할 때가 있는데, graphic을 별도 window에 띄우면 이 연결은 사라진다.



#### Interface builder



kitty window는 각각 title, background color와 기타 property를 가진 임의 개수의 sub-window로 vertical 또는 horizontal split할 수 있다. 구성 window 모음은 dwm (https://dwm.suckless.org/) 같은 tiling window manager처럼 다양한 layout으로 재배열하고 자유롭게 resize할 수 있다. keyboard shortcut으로 window arrangement를 “session (https://sw.kovidgoyal.net/kitty/sessions/)”으로 저장할 수 있다. session 정보는 layout detail과 session 생성 당시 각 window가 실행하던 program을 기록한 text file에 저장된다. 이 session은 tmux (https://github.com/tmux/tmux/wiki) 같은 terminal multiplexer를 상당 부분 대체할 수 있다.





이전 kitty version에서는 session window의 arrangement와 resize를 keyboard로 했다. 일반적으로 mouse보다 keyboard를 선호하지만 이는 이상적이지 않았다. kitty v0.47.0의 새 mouse handling은 window partition을 drag하고 window를 drag-and-drop해 재배열하는 잘 설계된 interface로 visual resize와 이동을 가능하게 한다. session window를 session 밖으로 drag하여 별도 window로 만들 수도 있다.





session은 kitty command의 --session flag로 load할 수 있다. 사용자는 keyboard shortcut으로 kitty를 쓸 때도 session을 load하거나 switch할 수 있다. session을 load하면 각 window에서 실행되던 모든 program이 시작된다. 앞서 언급한 ssh kitten으로 만든 shared SSH connection (https://sw.kovidgoyal.net/kitty/kittens/ssh/#opt-kitten-ssh.share_connections) 중 session 저장 당시 active였던 것은 다시 활성화된다.





kitty session의 명백한 용도는 다양한 project 또는 task에 필요한 environment를 정의하는 것이다. system administrator는 서로 다른 server에 연결된 여러 window를 가진 session을 원할 수 있다. programming project에는 code editor, REPL, documentation을 표시하는 window를 넣을 수 있다.





session을 kitty의 remote-control 기능과 결합하면 간단한 text-user-interface(TUI) application의 기반이 된다. kitty로 그런 application을 만들려면 원하는 layout을 만들어 session으로 저장하면 충분하다. 구성 window에서 실행되는 program은 user input을 처리하고 그에 맞춰 서로 text와 command를 주고받을 수 있다. 이렇게 보면 kitty는 일종의 TUI construction kit가 된다.



![[Kitty photo browser]](https://static.lwn.net/images/2026/kitty-picpicker.png)





위는 이 구조로 내가 만든 간단한 image browser의 screenshot이다. 사용자가 list에서 image file을 선택하면 image와 그 정보 일부를 표시한다. list는 한 window에서 fzf (https://github.com/junegunn/fzf)가 filter하고 표시하며, image는 다른 window에서 kitty의 icat kitten이 표시한다. image 정보는 세 번째 window에서 exif (https://libexif.github.io/) command output을 처리해 표시한다.





Kitty는 일반적으로 distribution repository에서 사용할 수 있다. 더 최신 release를 원하는 사람을 위해 installation instructions (https://sw.kovidgoyal.net/kitty/binary/)는 binary installation과 source build 방법을 설명한다. Kitty의 GitHub page (https://github.com/kovidgoyal/kitty)는 400명 이상의 contributor를 보여 주며, Goyal이 압도적으로 많은 commit을 했다. Python, C, Go와 약간의 다른 language로 작성됐다.



#### 결론



몇 년 전 advanced image display 같은 기능에 흥미를 느껴 kitty를 써 보기로 했고, 이제는 없어서는 안 될 도구가 됐다. Kitty는 terminal emulator 이상을 지향하며 textual human-computer interaction을 위한 풍부한 environment를 제공한다. 그러나 좋은 font support를 갖춘 빠른 terminal만 원하는 사용자에게도 수많은 기능은 방해가 되지 않는다. 점진적으로 살펴보고 원하는 대로 workflow에 넣을 수 있다. 나는 여전히 terminal 생활을 더 편하게 하는 kitty 기능을 발견하고 있다.





Kitty에는 때때로 혼란을 만드는 문제도 하나 있다. 그 이름이 Windows용 combination networking client 및 terminal emulator와 겹친다는 점이다.





마지막으로, 분명 일부 독자가 궁금해할 것이므로 답하자면, 그렇다. kitty에서 Doom (https://github.com/jserv/kitty-doom#kitty-doom)을 플레이할 수 있다.



Comments (45 posted) (/Articles/1080821/#Comments)





### QBE 1.3: metaprogramming, performance, cross-platform support (/Articles/1080519/)

#### 요약
- QBE 1.3 advances a small compiler backend alternative to LLVM/GCC, with performance work, metaprogramming for instruction selection, and Windows ABI support.[^qbe]
- The release shows the value of minimalist compiler infrastructure where full LLVM integration is too heavy.
- Remaining limitations make QBE a pragmatic backend for selected languages rather than a universal replacement.



           

2026년 7월 10일
           

이 글은 Arshal Aromal이 기고했다
           




Quentin Carbonneaux가 개발한 compact compiler backend QBE (https://c9x.me/compile/)는 LLVM, GCC 같은 더 큰 compiler backend의 lightweight alternative다. 단일 developer도 이해할 수 있을 만큼 작게 설계된 QBE는

static single-assignment (https://en.wikipedia.org/wiki/Static_single-assignment_form)(SSA) intermediate representation(IR)를 쓰고 C ABI를 지원하며 Hare (https://harelang.org/)와 cproc (https://github.com/michaelforney/cproc) C11 compiler 같은 project의 backend 역할을 한다. Frontend는 QBE IR의 textual form을 직접 emit하고, QBE가 register allocation, optimization, native-code generation을 처리해 target architecture용 assembly를 만든다.





QBE는 MIT license이며 contributor는 38명이지만 Carbonneaux가 가장 많은 작업을 했다. 2026년 6월 2일 version 1.3이
released (https://c9x.me/compile/release/qbe-1.3.html)됐다. release note에서는 2022년
1.0 (https://c9x.me/compile/releases.html) 이후 가장 중요한 update로 설명한다. 약 7,000줄을 추가하고 1,500줄을 제거했으며, QBE compile code의 performance 향상, metaprogramming을 통한 backend development 단순화, platform support 확장을 겨냥한 architectural change를 도입한다.



#### minimalist ecosystem



QBE는 Vladimir Makarov의 Medium Internal Representation (https://github.com/vnmakarov/mir#mir-project)(MIR), Dmitry Stogov의 IR (https://github.com/dstogov/ir#ir---lightweight-jit-compilation-framework)처럼 minimalist compiler project와 나란히 틈새를 차지한다. 1.3
release (https://news.ycombinator.com/item?id=48373442) 뒤 토론에서 참가자들은 이 system들이 전통적 C programming paradigm에 뿌리를 둔 공통 technical lineage를 공유한다고 언급했다. 그러나 우선순위는 크게 다르다.





MIR이 function inlining 같은 technique으로 aggressive optimization에 자주 집중하는 반면, QBE는 compilation speed와 작고 유지보수 가능한 code base를 우선한다. 이 철학은 초보자에게 어려울 수 있는 조밀하고 전통적인 Unix C 구현으로 이어지지만, 이해하고 나면 구조는 단순하고 추가 복잡성도 적다. resulting binary와 external API 모두 최소한으로 유지된다.



#### CoreMark performance gap 줄이기



1.3 release의 주요 동기는 QBE가 생성한 code의 performance가 “gcc -O2” performance 약 70%에 도달한다는 project 목표와 벌어진 차이였다. 이전
CoreMark (https://www.eembc.org/coremark/) suite 측정에서 QBE는 40%에 더 가까웠다.





release note에 따르면 이 차이를 해결하려는 노력은 contributor Roland Paterson-Jones가 optimization의 구체적 baseline으로 CoreMark를 쓰자고 제안하면서 시작됐다. Profiling은 CoreMark benchmark 자체의 소수 hot function, 특히
ee_isdigit() (https://github.com/eembc/coremark/blob/1f483d5b8316753a742cbf5590caf5bd0a4e4777/core_state.c#L197-L203)와
crcu8() (https://github.com/eembc/coremark/blob/1f483d5b8316753a742cbf5590caf5bd0a4e4777/core_util.c#L164-L188)를 overhead의 큰 원인으로 식별했다. 이 function은 edge case다. 예를 들어 CRC는 raw arithmetic보다 pre-computed table로 구현하는 것이 낫다. 하지만 low-level workload가 실행 시간을 쓰는 compact한 CPU-bound code section을 보여 준다.





이를 해결하기 위해 1.3은 여러 고전적 optimization pass를 도입했다. 추가 사항에는
global value-numbering (https://en.wikipedia.org/wiki/Value_numbering)(GVN)과
global code-motion (https://en.wikipedia.org/wiki/Code_motion)(GCM)이 있다. compiler가 redundant computation을 제거하고 hot path 밖으로 옮길 수 있게 한다. GVN/GCM과 함께 QBE 1.3에는 targeted loop optimization과 control-flow graph 단순화를 위한 if-elimination도 들어갔다.





Function inlining은 많이 논의됐지만 결국 미뤄졌다고 Carbonneaux는 release note에서 말했다. QBE는 minimal memory footprint를 유지하기 위해 function을 개별적으로 parse하고 compile하는 엄격한 streaming, per-function compilation model로 동작한다. Carbonneaux는 이 streaming architecture를 깨지 않기 위해 inlining을 연기했다고 설명했다.





이 생략에도 새 pass는 수정하지 않은 CoreMark에서 다른 compiler 결과의 63%를 넘는 generated-code performance를 보였고, benchmark에서 핵심 routine을 수동 inlining하면 70% target에 도달했다. 새 optimization은 더 현실적인 workload에도 이어졌다. Carbonneaux는 QBE 1.2와 비교해 Hare language test suite용 compiled code의 runtime performance가 33% 개선됐다고 측정했다. 이는 compiled Hare test program이 실행되는 속도이지 QBE 자체의 compile 속도가 아니다. QBE는 self-hosting할 수 없으므로 구현한 optimization이 QBE 자신의 compilation process 속도에는 영향을 주지 않는다.



#### instruction selection을 위한 metaprogramming



release는 instruction selection도 다시 다룬다. QBE는 역사적으로 Ken Thompson의 Plan 9 C
compiler (https://c9x.me/compile/bib/new-c.pdf)에서 영감을 얻은 bottom-up tree-numbering algorithm에 의존했다. 기능은 했지만 pure C로 직접 구현하려면 arithmetic operator의 associativity와 commutativity를 관리하는 복잡한 hand-written logic이 필요해 새 architecture backend 추가가 번거로웠다.





release note에서 Carbonneaux는 이 문제의 metaprogramming solution 구현이 오랜 목표였다고 말했다. Version 1.3은 declarative Lisp-like instruction pattern에서 C code를 만드는 OCaml 기반 metaprogramming tool인 mgen을 도입한다. Backend developer는 이 pattern을 source comment에 직접 쓰고, QBE build process 중 mgen이 backend source를 scan하여 바로 아래에 generated C code를 inline한다.





generated code는 function의 instruction directed acyclic-graph를 bottom-up 방식으로 처리한다. sub-graph가 취할 수 있는 각각의 unique shape는 tree-numbering pass에서 numeric code를 배정받는다. 이전에는 이 numbered code를 target assembly instruction으로 바꾸는 데 hand-written C code가 필요했다. QBE 1.3은 그 대부분을 mgen generated code로 교체한다. build time에 tool은 주어진 shape code와 매치할 수 있는 pattern을 계산하고 이를 저장하는 bit set을 만든다. QBE가 function을 compile할 때는 주어진 tree number의 associated bit set을 검사하여 어떤 pattern이 매치하는지 빠르게 확인한다.





선택된 pattern에 capture할 variable이 있으면 mgen은 전용 matcher program을 생성한다. 이 program은 단순화된 bytecode language로 compile되어 compile time에 interpret된다. 이 접근은 manual complexity를 크게 줄이며, Carbonneaux는 앞으로 optimization pass 안에서 복잡한 bit-rotation idiom을 식별하는 것처럼 더 advanced pattern recognition을 가능하게 할 것으로 기대한다.



#### Windows ABI와 shared object



performance와 maintainability를 넘어 QBE 1.3은 실질적인 platform support를 넓힌다. developer Scott Graham이 기여한 Windows x64 ABI backend를 추가했다.





이제 QBE에 "-t amd64_win" flag를 넘기면 Windows를 target으로 삼을 수 있다. Unix와 Linux system의 System V AMD64 ABI는 register usage, stack alignment, shadow-space management 등에서 Windows x64 ABI와 크게 다르다. 이 차이는 근본적이므로 Windows 구현은 대부분 별도로 존재한다. Graham이 Hacker News (https://news.ycombinator.com/item?id=48377871)에서 지적했듯, 이 격리는 System V implementation을 오염시키지 않고 Graham의 약간 다른 coding style로 QBE의 Windows support code를 작성하게 한다.





또한 QBE 1.3은 position-independent code(PIC)를 지원해 Executable and Linkable Format(ELF) system에서 native shared object를 생성할 수 있게 한다.





shared library 생성의 주된 장애물은
global offset table (https://en.wikipedia.org/wiki/Global_Offset_Table)(GOT)을 통한 global variable의 indirect access 처리였다. QBE 1.3은 dynamically loaded되는 external symbol을 표시하는 flag를 도입해 IR level에서 이를 해결한다. 그러한 variable 접근은 dynamic linker가 relocation (/Articles/961117/)을 수행할 위치를 제공하는 helper function을 암묵적으로 사용한다.





이 추가 사항으로 QBE 위에 구축된 language는 이전에 가능했던 statically-linked executable뿐 아니라 modular, dynamically-linked program도 만들 수 있다.



#### 계속되는 한계와 ecosystem 영향



release 이후 community 토론은 project의
progress (https://news.ycombinator.com/item?id=48375047)와
ongoing limitations (https://news.ycombinator.com/item?id=48374842)를 함께 부각했다. Windows support 추가는 이전에 부재를 desktop-targeted project의 치명적 문제로 보던 developer에게 큰 장벽을 없앤다.





그러나 minimalist C에 대한 QBE의 엄격한 고수는 계속 가파른 learning curve를 만든다. 해결되지 않은 큰 한계는
DWARF (https://dwarfstd.org/)나
PDB (https://llvm.org/docs/PDB/index.html) 같은 native source-level debugging-information generation의 부재다. Hare 같은 project는 QBE 위에 포괄적인 DWARF support를 구축하는 복잡한 작업을 맡았지만 backend 자체는 여전히 이를 생성하지 못한다.





QBE만으로는 자신을 compile할 수 없다는 오랜 논쟁도 계속된다. QBE는 compiler backend일 뿐이라 self-hosting이 아니다. self-hosting하려면 project에 C frontend를 추가해야 한다. 그러나 release 뒤 토론에서 한 commenter가
argued (https://news.ycombinator.com/item?id=48375990)했듯, self-hosted backend는 모든 것에서 자신의 code generation에 의존해야 한다. 일부 compiler engineer는 project가 의지할 다른 compiler가 없기에 backend 자신의 optimization quality를 계속 끌어올리도록 하는 유용한 압력이라고 본다.





이 한계에도 QBE는 comparable performance와 단순한 external interface를 갖춘 backend라는 매우 독특한 접근을 계속 제공한다. 검증된 optimization, 더 유연한 instruction-selection pipeline, 더 넓은 platform support를 갖춘 version 1.3은 성능을 너무 많이 포기하지 않고 작고 이해 가능한 backend가 필요한 project에 더 실용적인 선택지가 된다.



Comments (4 posted) (/Articles/1080519/#Comments)









Page editor: Joe Brockmeier

# 간략한 항목


## 보안



### 많은 이전 shim 버전이 여전히 secure boot에서 허용됨 (/Articles/1082940/)
CMU CERT Coordination Center는 UEFI secure boot가 활성화된 시스템에서 Linux를 부팅하는 데 쓰이는 shim binary의 악용 가능한 다수 버전이 revocation list에 한 번도 추가되지 않았다는 권고문 (https://kb.cert.org/vuls/id/616257)을 발표했다.




	관리자 권한을 갖거나 boot process를 수정할 수 있는 공격자는 취약한 shim bootloader 중 하나를 이용해 Secure Boot 보호를 우회하고 operating system이 로드되기 전에 임의의 코드를 실행할 수 있다. 이 초기 boot 단계에서 실행된 코드는 unsigned 또는 악성 kernel component를 로드하는 능력을 포함해 플랫폼을 지속적으로 compromise할 수 있으며, 이는 시스템 재부팅과 경우에 따라 operating system 재설치 후에도 살아남을 수 있다.




이 권고문에는 취약한 shim 목록이 들어 있다.



Comments (6 posted) (/Articles/1082940/)








### seunshare 3.10의 로컬 DoS attack vector (/Articles/1083076/)


SUSE Security Team Blog는 SELinux가 신뢰할 수 없는 프로그램을 격리하는 데 사용하는 seunshare (https://man7.org/linux/man-pages/man8/seunshare.8.html)를 분석한 글 (https://security.opensuse.org/2026/07/15/selinux-seunshare.html)을 게시했다. 팀은 이 프로그램의 버전 3.10 (https://github.com/SELinuxProject/selinux/releases/tag/3.10)을 검토하는 과정에서 두 가지 로컬 Denial-of-Service (DoS) vector를 발견했다.




seunshare는 SELinux가 활성화된 시스템에서 실행되도록 설계되었으므로, 이와 같은 setuid-root binary의 취약점이 악용될 때 어떤 privilege escalation이 가능한지 이해하는 일이 중요하다. Fedora 및 openSUSE처럼 SELinux가 활성화된 많은 시스템은 기본적으로 "targeted" SELinux policy를 제공한다. 이 policy는 잘 알려진 system service를 격리하는 데 초점을 맞추지만, 보안과 usability의 균형을 위해 기본적으로 interactive user에게 unconfined SELinux context를 할당한다.



seunshare를 위한 SELinux policy에 정의된 더 제한적인 seunshare_t로, unconfined domain에서 전환하는 domain transition은 현재 없다. 이는 seunshare 실행이 unconfined domain에서 계속된다는 뜻이다. 따라서 interactive user가 수행하는 attack의 맥락에서는, 시스템이 SELinux enforced mode로 실행 중이더라도 아래 취약점의 영향은 root와 유사한 privilege escalation이 된다.




팀의 발견과 timeline에 관한 전체 설명은 해당 글을 참조하라. 취약점은 버전 3.11 (https://github.com/SELinuxProject/selinux/releases/tag/3.11)에서 수정되었다.







Comments (6 posted) (/Articles/1083076/#Comments)








### 이번 주의 보안 인용문 (/Articles/1082720/)




AI 자체에 관해서 말하자면, 이 tech company들에 power와 wealth가 집중되는 것이 오늘날 사회가 직면한 가장 큰 existential risk다. 이는 우리가 corporate power, 특히 public을 착취하고 political system을 조작하는 corporation의 능력을 제한해야 한다는 뜻이다.



data center에 반대하는 일은 시작점일 뿐이어야 한다. 우리는 주 정부가 AI를 규제하도록 (https://gizmodo.com/against-the-federal-moratorium-on-state-level-regulation-of-ai-2000698390) 요구하고, 이 기술의 무책임한 사용을 거부하며 corporate behavior를 형성하도록 옹호할 수 있다. AI computation에 세금을 부과하도록 (https://www.theguardian.com/commentisfree/2026/jun/08/bernie-sanders-ai-sovereign-wealth-fund-plan) 싸울 수 있다. 그러면 public은 AI 사용의 이익 일부를 얻을 수 있고, 동시에 AI company가 사용과 연관된 energy 및 environmental consequence를 더 많이 internalize하도록 강제할 수 있다. 또한 우리는 private profit이 아니라 public benefit을 만들도록 incentive structure가 마련된, public control 아래 개발되는 대안 ecosystem인 Public AI (https://www.brookings.edu/articles/how-public-ai-can-strengthen-democracy/)를 위한 global movement (https://publicai.network/)에 모두 참여할 수 있다.

— Bruce
Schneier and Nathan E. Sanders (https://www.schneier.com/blog/archives/2026/07/ai-data-centers-and-the-concentration-of-wealth.html)



Comments (none posted) (/Articles/1082720/#Comments)











## Kernel 개발



### Kernel 릴리스 상태 (/Articles/1083072/)
현재 development kernel은 7.2-rc3이며, 7월 12일에 릴리스되었다 (/Articles/1082486/). Linus는 다음과 같이 말했다. "상황은 계속 정상으로 보입니다('new normal', 즉 commit 비율은 약간 높아졌지만 사람들이 summer vacation을 가기 시작하면서 그 증가분이 어느 정도 상쇄되는 듯한 느낌도 듭니다)."



이번 릴리스에서는 2,261명의 developer가 14,229개의 non-merge changeset을 만들었으며, 이 가운데 448명은 처음으로 kernel에 기여한 사람이었다. 릴리스 이력은 다음과 같다:
        
        
        RCDateCommits
    v7.2-rc1
            2026-06-2814395
            14395
        
        v7.2-rc2
            2026-07-05433
            433
        
        v7.2-rc3
            2026-07-12475
            475
        
        
      
      


      자세한 내용은 LWN KSDB v7.2 페이지 (/ksdb/releases/v7.2/)를 참조하라.
      





지난주에는 stable update가 릴리스되지 않았다.



Comments (none posted) (/Articles/1083072/#Comments)








### 2026 Maintainers Summit 주제 모집 (/Articles/1082838/)
Maintainers Summit은 development process 문제를 논의하기 위해 열리는 kernel developer와 maintainer의 연례 초대 전용 모임이다. 예시는 LWN의 2025 Maintainers Summit 보도 (/Articles/1049982/)를 참조하라. 2026년 모임(10월 8일, Prague)을 위한 주제 모집 (/ml/all/alW3eJ9x6iJ8Juhi@mit.edu)이 시작되었다. Summit 초대를 받는 가장 좋은 방법 중 하나는 좋은 주제 제안서를 내는 것이다. 충분한 검토를 받으려면 주제를 7월 24일 이전에 제출해야 한다.



Comments (none posted) (/Articles/1082838/)








### 이번 주의 인용문 (/Articles/1082712/)




	NOMMU 작업을 도와주셔서 다시 한 번 감사합니다. medal을 드리고 싶지만, 대신 넘쳐나는 inbox로 만족하셔야 할 것 같습니다.

— Andrew
Morton (/ml/all/20260710174340.9f3b420629769b556f44640f@linux-foundation.org)






	일부 사람이 AI를 정말 싫어한다는 점은 알고 있지만, 이는 최상위 maintainer로서 제가 단호하게 입장을 고수할 영역입니다.



	Linux는 anti-AI project 중 하나가 아닙니다. 이에 문제가 있다면 open-source 방식으로 fork하면 됩니다.



	아니면 그냥 떠나도 됩니다.



	AI는 우리가 쓰는 다른 도구와 마찬가지로 도구입니다. 그리고 분명 유용한 도구입니다.

— Linus
Torvalds (/ml/all/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com)






	Linus가 이런 헛소리를 더 강하게 밀어붙이는 건, 기본적으로 그가 AI slop을 직접 처리할 필요가 없기 때문이죠 :)



	AI를 합리적이고 세련되게 사용하면 유용하다는 그의 말에는 동의합니다. 그 부분은 괜찮고 kernel이 anti-AI가 아니라고 말하는 것도 괜찮습니다.



	하지만 그냥 도구라고요? 에이, 정말.



	이제 멍청이들이 엄청난 양의 헛소리를 보낼 수 있게 되었고 maintainer는 그 규모에 맞춰 늘지 않으니, reviewer와 maintainer는 큰 혼란을 겪고 있습니다.



	핵폭탄도 그저 도구라고 하는 것과 같은 의미에서 AI도 도구인 모양입니다...

— Lorenzo Stoakes (https://mastodonapp.uk/@ljs/116922806894828844)






	생성형 AI를 모두에게 강제로 삼키게 하는 것 외에 정말 받아들일 수 있는 선택지는 없는 건가요? 윤리적 우려를 가진 사람이 계속 kernel community의 일부로 여겨질 선택지는 없나요? 완전한 항복과 충성 맹세 외에는 선택지가 없나요? 저는 점점 이런 대우를 받는 느낌이고, 저만 그런 것이 아니라는 점도 압니다.

— Laurent
Pinchart (/ml/all/20260715174138.GI1778116@killaraus.ideasonboard.com)



Comments (37 posted) (/Articles/1082712/#Comments)











## Distributions



### Debian bookworm의 마지막 일반 릴리스 (/Articles/1082647/)



Debian은 Debian 12 ("bookworm")의 마지막 일반 update를 발표했다 (/ml/all/e0718a5433efa5ba4a71fd3b671aab06f1441a07.camel@debian.org). Long-term-support update는 2028년까지 계속된다 (/ml/all/a27c47d0f34f36e497d2596a9adfbcb662cd4439.camel%40debian.org/). stable version에서 예상할 수 있듯, 이 update는 대부분 security fix에 한정된다. 하지만 Debian user는 더 최신 버전으로 upgrade할 시점일 수 있다. 마침 Debian 13 ("trixie")도 이번 주말에 update를 받았으며 (/ml/all/baf38e8be7c03f43ace7fb06433aed0aac8196de.camel@debian.org), 같은 security fix가 다수 포함되어 있다.




Comments (none posted) (/Articles/1082647/)








### 이번 주 Distributions 인용문 (/Articles/1082885/)

copyleft software가 성공하는 모습을 보고 싶다면, 이를 더 좋게 만드는 데 기여하는 것이 최선의 방법이다. license 때문에 그들에게 가장 적합하지 않은 software를 사용하도록 user를 강제하거나 gatekeep하려 해서는 안 된다. 그 길의 끝에는 우리의 credibility가 죽는 일만 있다.


— Ted Ts'o (https://lwn.net/ml/all/alWiuJkCSSaeJgjf%40mit.edu/)




copyleft는 corporation으로부터 우리를 보호하는 마법의 주문이 아니다. 그것도 그저 도구일 뿐이고, 어떤 상황에서는 유용하지만 다른 상황에서는 그렇지 않다.




하지만 내가 틀렸고 copyleft가 내가 생각하는 것보다 더 중요할 수도 있다. 그렇다면 copyleft software 작업에 참여할 더 많은 사람을 모집할 방법을 찾아야 하고, 다른 model이 현재 지닌 상당한 본질적 legal advantage를 줄이기 위해 더 넓은 사회에서 political fight를 벌여야 할 가능성이 크다.




그 싸움에 전혀 도움이 되지 않을 일이 무엇인지 아는가? "우리 copyleft software를 사용하세요. 품질은 낮고 우리는 code를 거의 작성하지 않지만, 늙어 죽을 때까지 어떤 software를 써야 하는지 강의할 moralizing scold는 아주 많습니다."


— Russ Allbery (https://lwn.net/ml/all/87ldbd38vu.fsf%40hope.eyrie.org/)







Comments (10 posted) (/Articles/1082885/#Comments)











## Development



### Rust 1.97.0 릴리스 (/Articles/1082032/)
Rust programming language 버전 1.97.0 (https://blog.rust-lang.org/2026/07/09/Rust-1.97.0/)이 릴리스되었다. 변경 사항에는 새 symbol-mangling scheme을 기본값으로 사용하는 것, Cargo에서 warning을 거부하는 기능 지원, 성공적으로 build한 뒤 linker output을 숨기던 관행의 종료가 포함된다.



Comments (13 posted) (/Articles/1082032/)








### Linux.org 이야기 (/Articles/1082901/)
Rob Kennedy가 가장 이른 Linux 관련 web site 중 하나인 Linux.org (https://linux.org/)의 탄생과 최근 재탄생에 관한 이야기 (https://www.linux.org/threads/the-linux-org-story.68810/)를 게시했다.



	이 site는 Linux 자체가 겨우 세 살이던 1994년 5월 Michael McLagan이 설립했다. Linus Torvalds가 이를 세상에 공개한 지도 얼마 되지 않았고, newcomer가 시작점을 찾을 실질적인 방법도 없었다. search engine도 Wikipedia도, 새로운 기술을 파악하기 위해 사람들이 이제는 당연하게 여기는 infrastructure도 없었다. Michael은 그 공백을 메우고자 linux.org를 만들었다. 사람들이 Linux를 배우고 movement가 성장하는 모습을 따라갈 수 있는 장소였다.




Comments (4 posted) (/Articles/1082901/)












Page editor: Daroc Alden







# 공지


## 뉴스레터



### Distributions 및 system administration




DistroWatch Weekly (https://distrowatch.com/weekly.php?issue=20260713)
7월 13일



This week in F-Droid (https://f-droid.org/en/2026/07/09/twif.html)
7월 9일



openSUSE Tumbleweed Review of the Week (https://dominique.leuenberger.net/blog/2026/07/tumbleweed-review-of-the-week-2026-28/)
7월 10일



Ubuntu Weekly News (https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-issue-952/84897)
7월 6일



Ubuntu Weekly Newsletter (/Articles/1082834/)
7월 13일






### Development




Emacs News (https://sachachua.com/blog/2026/07/2026-07-13-emacs-news/)
7월 13일



What's cooking in git.git (/Articles/1082173/)
7월 9일



What's cooking in git.git (/Articles/1082644/)
7월 12일



What's cooking in git.git (/Articles/1082946/)
7월 14일



This Week in GNOME (https://thisweek.gnome.org/posts/2026/07/twig-257/)
7월 10일



GNU Tools Weekly News (/Articles/1082675/)
7월 12일



Golang Weekly (https://golangweekly.com/issues/609)
7월 10일



Last Week in Kubernetes Development (https://lwkd.info/2026/20260711)
7월 11일



LLVM Weekly (https://llvmweekly.org/issue/654)
7월 13일



This Week in Matrix (https://matrix.org/blog/2026/07/10/this-week-in-matrix-2026-07-10/)
7월 10일



OCaml Weekly News (/Articles/1082836/)
7월 14일



OpenPrinting News (https://openprinting.github.io/OpenPrinting-News-Opportunity-Open-Source-4.0-Call-for-Proposals-extended-to-end-of-July/)
7월 8일



Perl Weekly (http://perlweekly.com/archive/781.html)
7월 13일



This Week in Plasma (https://blogs.kde.org/2026/07/11/this-week-in-plasma-audio-recording-in-spectacle/)
7월 11일



PyCoder's Weekly (https://pycoders.com/issues/743)
7월 14일



Python Core Dispatch (https://coredispatch.xyz/editions/7)
7월 6일



Ruby Weekly News (https://rubyweekly.com/issues/808)
7월 9일



This Week in Rust (https://this-week-in-rust.org/blog/2026/07/08/this-week-in-rust-659/)
7월 8일



Wikimedia Tech News (https://meta.wikimedia.org/wiki/Special:FeedItem/technews/20260713000000/en)
7월 13일






### 회의록




Fedora FESCo 회의록 (/Articles/1083071/)
7월 14일



openSUSE Release Engineering 회의록 (/Articles/1082097/)
7월 8일



This week in the Perl Steering Committee (https://blogs.perl.org/users/psc/2026/07/this-week-in-psc-233-2026-07-13.html)
7월 13일






## 발표 모집




### CFP 마감일: 2026년 7월 16일~2026년 9월 14일
다음 CFP 마감일 목록은 LWN.net CFP Calendar (/Calendar/Monthly/cfp/)에서 가져왔다.






           
           DeadlineEvent Dates
               EventLocation
           
               7월 20일
               11월 14일
11월 15일
               Capitole du Libre 2026 (https://cfp.capitoledulibre.org/cdl-2026/cfp)
               Toulouse, France
               
               
               7월 31일
               10월 14일
10월 17일
               PyCon South Africa (https://za.pycon.org/pages/speaking/how_to_apply/)
               Cape Town, South Africa
               
               
               7월 31일
               10월 1일
10월 2일
               embedded Linux for Safe and Secure Applications (https://www.elsa-symposium.com/call-papers)
               Göttingen, Germany
               
               
               7월 31일
               9월 25일
9월 27일
               PostmarketOS and Alpine Linux Conference (https://pretalx.postmarketos.org/postmarketos-conference-2026/cfp)
               Aachen, Germany
               
               
               8월 1일
               9월 28일
10월 1일
               Alpine Linux Persistence and Storage Summit (https://lwn.net/ml/all/20260701114321.GB17996@lst.de)
               Lizumerhütte, Tyrol, Austria
               
               
               8월 1일
               8월 25일
8월 30일
               MiniDebConf and MiniDebCamp Winterthur 2026 (https://ch2026.mini.debconf.org/contribute/cfp/)
               Winterthur, Switzerland
               
               
               8월 31일
               10월 2일
10월 4일
               GNU Tools Cauldron (https://conf.gnu-tools-cauldron.org/prg26/)
               Prague, Czechia
               
               
               8월 31일
               10월 3일
10월 4일
               Linux Days 2026 (https://pretalx.linuxdays.cz/linuxdays-2026/cfp)
               Prague, Czechia
               
               




CFP 마감일 목록에 귀하의 event가 없다면, 이를 알려 달라 (/Calendar/new/).



## 예정된 이벤트




### 이벤트: 2026년 7월 16일~2026년 9월 14일
다음 event 목록은 LWN.net Calendar (/Calendar/)에서 가져왔다.






           
           Date(s)EventLocation
           
               7월 13일
7월 16일
               Netdev (https://www.netdevconf.info/0x1A/)
               Rome, Italy
               
               
               7월 13일
7월 19일
               DebCamp 26 (https://debconf26.debconf.org/)
               Santa Fe, Argentina
               
               
               7월 13일
7월 19일
               EuroPython (https://ep2026.europython.eu/)
               Kraków, Poland
               
               
               7월 15일
7월 22일
               BornHack 2026 (https://bornhack.dk/bornhack-2026/)
               Funen, Denmark
               
               
               7월 16일
7월 19일
               Electromagnetic Field (https://www.emfcamp.org/)
               Eastnor, UK
               
               
               7월 18일
               AlmaLinux Day: Los Angeles (https://almalinux.org/almalinux-day-los-angeles-2026/)
               Los Angeles, CA, US
               
               
               7월 20일
7월 25일
               DebConf 26 (https://debconf26.debconf.org/)
               Santa Fe, Argentina
               
               
               8월 6일
8월 9일
               FOSSY 2026 (https://2026.fossy.ca/)
               Vancouver, Canada
               
               
               8월 8일
8월 9일
               UbuCon Asia 2026 @ COSCUP (https://2026.ubucon.asia)
               Taipei, Taiwan
               
               
               8월 11일
8월 12일
               Open Source Summit Korea (https://events.linuxfoundation.org/open-source-summit-korea/)
               Seoul, South Korea
               
               
               8월 14일
8월 16일
               Hackers on Planet Earth (https://www.hope.net/)
               New York, NY, USA
               
               
               8월 25일
8월 30일
               MiniDebConf and MiniDebCamp Winterthur 2026 (https://ch2026.mini.debconf.org/)
               Winterthur, Switzerland
               
               
               8월 30일
9월 5일
               FOSS4G Hiroshima 2026 (https://2026.foss4g.org/en/)
               Hiroshima, Japan
               
               




귀하의 event가 여기에 없다면, 이를 알려 달라 (/Calendar/new/).


## Security updates

### 2026년 7월 9일부터 7월 15일까지의 경보 요약 (/Articles/1083045/)

               배포판
                   ID
                   릴리스
                   패키지
                   날짜
AlmaLinux
                       ALSA-2026:36195 (https://lwn.net/Articles/1081919/)
                       9
                       389-ds-base
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36201 (https://lwn.net/Articles/1082756/)
                       8
                       389-ds:1.4
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:36782 (https://lwn.net/Articles/1082174/)
                       10
                       aardvark-dns
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36318 (https://lwn.net/Articles/1081920/)
                       9
                       aardvark-dns
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36199 (https://lwn.net/Articles/1081921/)
                       10
                       buildah
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38494 (https://lwn.net/Articles/1082759/)
                       10
                       buildah
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38493 (https://lwn.net/Articles/1082757/)
                       9
                       buildah
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:37410 (https://lwn.net/Articles/1082758/)
                       9
                       buildah
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:39575 (https://lwn.net/Articles/1082951/)
                       8
                       cifs-utils
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:36215 (https://lwn.net/Articles/1081922/)
                       8
                       compat-openssl10
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:19043 (https://lwn.net/Articles/1082952/)
                       10
                       corosync
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:39302 (https://lwn.net/Articles/1082953/)
                       10
                       cups
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:36733 (https://lwn.net/Articles/1082175/)
                       8
                       cups
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36721 (https://lwn.net/Articles/1082176/)
                       8
                       edk2
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36211 (https://lwn.net/Articles/1082760/)
                       10
                       freeipmi
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:36307 (https://lwn.net/Articles/1081923/)
                       8
                       freeipmi
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36210 (https://lwn.net/Articles/1081924/)
                       9
                       freeipmi
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38501 (https://lwn.net/Articles/1082954/)
                       8
                       freerdp
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:37207 (https://lwn.net/Articles/1082761/)
                       9
                       freerdp
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:24347 (https://lwn.net/Articles/1081925/)
                       10
                       frr
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38485 (https://lwn.net/Articles/1082762/)
                       8
                       gegl
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:38496 (https://lwn.net/Articles/1082763/)
                       9
                       gimp
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:39266 (https://lwn.net/Articles/1082955/)
                       8
                       git-lfs
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:20613 (https://lwn.net/Articles/1081926/)
                       10
                       gnutls
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:22141 (https://lwn.net/Articles/1082956/)
                       10
                       go-fdo-client and go-fdo-server
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:38995 (https://lwn.net/Articles/1082957/)
                       8
                       go-toolset:rhel8
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:37436 (https://lwn.net/Articles/1082765/)
                       10
                       golang
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:37435 (https://lwn.net/Articles/1082764/)
                       9
                       golang
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:35828 (https://lwn.net/Articles/1081927/)
                       9
                       grafana
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:35829 (https://lwn.net/Articles/1081928/)
                       9
                       grafana-pcp
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36749 (https://lwn.net/Articles/1082178/)
                       10
                       gstreamer1-plugins-bad-free
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:37130 (https://lwn.net/Articles/1082177/)
                       8
                       gstreamer1-plugins-bad-free
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36834 (https://lwn.net/Articles/1082179/)
                       9
                       gstreamer1-plugins-bad-free
                       2026-07-10
                       AlmaLinux
                       ALSA-2026:36774 (https://lwn.net/Articles/1082180/)
                       8
                       gstreamer1-plugins-good
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:37129 (https://lwn.net/Articles/1082181/)
                       9
                       gstreamer1-plugins-good
                       2026-07-10
                       AlmaLinux
                       ALSA-2026:36674 (https://lwn.net/Articles/1082182/)
                       9
                       gstreamer1-plugins-ugly-free
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36541 (https://lwn.net/Articles/1082185/)
                       10
                       kernel
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36956 (https://lwn.net/Articles/1082187/)
                       10
                       kernel
                       2026-07-10
                       AlmaLinux
                       ALSA-2026:38492 (https://lwn.net/Articles/1082766/)
                       10
                       kernel
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:36366 (https://lwn.net/Articles/1081929/)
                       8
                       kernel
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36349 (https://lwn.net/Articles/1081930/)
                       8
                       kernel
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:39179 (https://lwn.net/Articles/1082958/)
                       8
                       kernel
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:39083 (https://lwn.net/Articles/1082959/)
                       8
                       kernel
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:36018 (https://lwn.net/Articles/1082183/)
                       9
                       kernel
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36645 (https://lwn.net/Articles/1082184/)
                       9
                       kernel
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36957 (https://lwn.net/Articles/1082186/)
                       9
                       kernel
                       2026-07-10
                       AlmaLinux
                       ALSA-2026:38491 (https://lwn.net/Articles/1082767/)
                       9
                       kernel
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:36365 (https://lwn.net/Articles/1081931/)
                       8
                       kernel-rt
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36348 (https://lwn.net/Articles/1081932/)
                       8
                       kernel-rt
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:39180 (https://lwn.net/Articles/1082961/)
                       8
                       kernel-rt
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:39082 (https://lwn.net/Articles/1082960/)
                       8
                       kernel-rt
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:39296 (https://lwn.net/Articles/1082962/)
                       10
                       libinput
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:28290 (https://lwn.net/Articles/1082768/)
                       9
                       libreoffice
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:36730 (https://lwn.net/Articles/1082188/)
                       8
                       libsolv
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36728 (https://lwn.net/Articles/1082189/)
                       8
                       libtasn1
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:39304 (https://lwn.net/Articles/1082963/)
                       10
                       libxml2
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:36734 (https://lwn.net/Articles/1082190/)
                       8
                       libxml2
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:24758 (https://lwn.net/Articles/1081933/)
                       10
                       libyang
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38500 (https://lwn.net/Articles/1082769/)
                       9
                       maven:3.9
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:36364 (https://lwn.net/Articles/1081935/)
                       10
                       nginx
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36331 (https://lwn.net/Articles/1081934/)
                       9
                       nginx
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38847 (https://lwn.net/Articles/1082964/)
                       8
                       nginx:1.24
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:36618 (https://lwn.net/Articles/1082191/)
                       9
                       nginx:1.24
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36639 (https://lwn.net/Articles/1082192/)
                       9
                       nginx:1.26
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:36617 (https://lwn.net/Articles/1082193/)
                       9
                       oci-seccomp-bpf-hook
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:19146 (https://lwn.net/Articles/1081936/)
                       10
                       openexr
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38499 (https://lwn.net/Articles/1082770/)
                       10
                       openexr
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38498 (https://lwn.net/Articles/1082771/)
                       9
                       openexr
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38503 (https://lwn.net/Articles/1082965/)
                       8
                       openssl
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:39322 (https://lwn.net/Articles/1082966/)
                       8
                       pacemaker
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:19167 (https://lwn.net/Articles/1081937/)
                       9
                       pcs
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38513 (https://lwn.net/Articles/1082772/)
                       10
                       perl-DBI
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38512 (https://lwn.net/Articles/1082773/)
                       9
                       perl-DBI
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38901 (https://lwn.net/Articles/1082967/)
                       8
                       perl-DBI:1.641
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:36187 (https://lwn.net/Articles/1081938/)
                       9
                       perl-HTTP-Daemon
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:22649 (https://lwn.net/Articles/1082968/)
                       10
                       php8.4
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:38514 (https://lwn.net/Articles/1082774/)
                       10
                       plexus-utils
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38796 (https://lwn.net/Articles/1082775/)
                       9
                       plexus-utils
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38495 (https://lwn.net/Articles/1082778/)
                       10
                       podman
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:37123 (https://lwn.net/Articles/1082776/)
                       9
                       podman
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:38878 (https://lwn.net/Articles/1082777/)
                       9
                       podman
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:26204 (https://lwn.net/Articles/1081939/)
                       9
                       postgresql:18
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:39127 (https://lwn.net/Articles/1082969/)
                       8
                       python-pillow
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:36732 (https://lwn.net/Articles/1082194/)
                       8
                       python-urllib3
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:39320 (https://lwn.net/Articles/1082970/)
                       8
                       python3
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:39183 (https://lwn.net/Articles/1082971/)
                       10
                       python3.12
                       2026-07-15
                       AlmaLinux
                       ALSA-2026:36193 (https://lwn.net/Articles/1081941/)
                       10
                       python3.14-pip
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36315 (https://lwn.net/Articles/1081940/)
                       9
                       python3.14-pip
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36317 (https://lwn.net/Articles/1081942/)
                       9
                       skopeo
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36788 (https://lwn.net/Articles/1082779/)
                       10
                       tomcat
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:37137 (https://lwn.net/Articles/1082196/)
                       8
                       tomcat
                       2026-07-10
                       AlmaLinux
                       ALSA-2026:36879 (https://lwn.net/Articles/1082195/)
                       9
                       tomcat
                       2026-07-09
                       AlmaLinux
                       ALSA-2026:25341 (https://lwn.net/Articles/1081943/)
                       10
                       tomcat9
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:36790 (https://lwn.net/Articles/1082780/)
                       10
                       tomcat9
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:20600 (https://lwn.net/Articles/1081944/)
                       10
                       wireshark
                       2026-07-08
                       AlmaLinux
                       ALSA-2026:38487 (https://lwn.net/Articles/1082782/)
                       8
                       xorg-x11-server
                       2026-07-13
                       AlmaLinux
                       ALSA-2026:38486 (https://lwn.net/Articles/1082781/)
                       9
                       xorg-x11-server
                       2026-07-14
                       AlmaLinux
                       ALSA-2026:38488 (https://lwn.net/Articles/1082783/)
                       8
                       xorg-x11-server-Xwayland
                       2026-07-13
                       Debian
                       DLA-4674-1 (https://lwn.net/Articles/1081946/)
                       LTS
                       chromium
                       2026-07-09
                       Debian
                       DLA-4677-1 (https://lwn.net/Articles/1082515/)
                       LTS
                       chromium
                       2026-07-12
                       Debian
                       DSA-6384-1 (https://lwn.net/Articles/1081945/)
                       stable
                       chromium
                       2026-07-08
                       Debian
                       DSA-6387-1 (https://lwn.net/Articles/1082514/)
                       stable
                       chromium
                       2026-07-12
                       Debian
                       DLA-4685-1 (https://lwn.net/Articles/1082972/)
                       LTS
                       grub2
                       2026-07-15
                       Debian
                       DLA-4680-1 (https://lwn.net/Articles/1082784/)
                       LTS
                       imagemagick
                       2026-07-14
                       Debian
                       DLA-4678-1 (https://lwn.net/Articles/1082516/)
                       LTS
                       libxfont
                       2026-07-12
                       Debian
                       DSA-6388-1 (https://lwn.net/Articles/1082973/)
                       stable
                       libxfont
                       2026-07-15
                       Debian
                       DLA-4679-1 (https://lwn.net/Articles/1082517/)
                       LTS
                       mesa
                       2026-07-13
                       Debian
                       DLA-4684-1 (https://lwn.net/Articles/1082974/)
                       LTS
                       opam
                       2026-07-15
                       Debian
                       DSA-6386-1 (https://lwn.net/Articles/1082518/)
                       stable
                       opam
                       2026-07-10
                       Debian
                       DLA-4681-1 (https://lwn.net/Articles/1082785/)
                       LTS
                       p7zip
                       2026-07-13
                       Debian
                       DSA-6385-1 (https://lwn.net/Articles/1081947/)
                       stable
                       pgextwlist
                       2026-07-08
                       Debian
                       DLA-4682-1 (https://lwn.net/Articles/1082786/)
                       LTS
                       redis
                       2026-07-13
                       Debian
                       DLA-4675-1 (https://lwn.net/Articles/1082197/)
                       LTS
                       rlottie
                       2026-07-10
                       Debian
                       DLA-4676-1 (https://lwn.net/Articles/1082519/)
                       LTS
                       wireless-regdb
                       2026-07-11
                       Debian
                       DLA-4683-1 (https://lwn.net/Articles/1082975/)
                       LTS
                       wolfssl
                       2026-07-15
                       Fedora
                       FEDORA-2026-25954ebccf (https://lwn.net/Articles/1082535/)
                       F44
                       OpenImageIO
                       2026-07-11
                       Fedora
                       FEDORA-2026-67504c329b (https://lwn.net/Articles/1082521/)
                       F43
                       acl
                       2026-07-13
                       Fedora
                       FEDORA-2026-6b9a652463 (https://lwn.net/Articles/1082520/)
                       F44
                       acl
                       2026-07-11
                       Fedora
                       FEDORA-2026-b85570f8e4 (https://lwn.net/Articles/1082523/)
                       F43
                       attr
                       2026-07-13
                       Fedora
                       FEDORA-2026-daa458d11d (https://lwn.net/Articles/1082522/)
                       F44
                       attr
                       2026-07-11
                       Fedora
                       FEDORA-2026-c872d91489 (https://lwn.net/Articles/1082787/)
                       F44
                       breezy
                       2026-07-14
                       Fedora
                       FEDORA-2026-950a662010 (https://lwn.net/Articles/1082198/)
                       F44
                       c-ares
                       2026-07-10
                       Fedora
                       FEDORA-2026-6776f4e492 (https://lwn.net/Articles/1082788/)
                       F43
                       calibre
                       2026-07-14
                       Fedora
                       FEDORA-2026-79a5573be3 (https://lwn.net/Articles/1082789/)
                       F44
                       calibre
                       2026-07-14
                       Fedora
                       FEDORA-2026-9a7d180869 (https://lwn.net/Articles/1082524/)
                       F43
                       chromium
                       2026-07-12
                       Fedora
                       FEDORA-2026-7e82bf89f4 (https://lwn.net/Articles/1082525/)
                       F44
                       chromium
                       2026-07-12
                       Fedora
                       FEDORA-2026-0c3f6c7c67 (https://lwn.net/Articles/1082526/)
                       F44
                       cjson
                       2026-07-11
                       Fedora
                       FEDORA-2026-3017b1bec1 (https://lwn.net/Articles/1082528/)
                       F43
                       composer
                       2026-07-11
                       Fedora
                       FEDORA-2026-22ba02bee3 (https://lwn.net/Articles/1082527/)
                       F44
                       composer
                       2026-07-11
                       Fedora
                       FEDORA-2026-8e7eb40534 (https://lwn.net/Articles/1082529/)
                       F43
                       docker-compose
                       2026-07-11
                       Fedora
                       FEDORA-2026-e2afc3151d (https://lwn.net/Articles/1082977/)
                       F43
                       freerdp
                       2026-07-15
                       Fedora
                       FEDORA-2026-931f893f1b (https://lwn.net/Articles/1082976/)
                       F44
                       freerdp
                       2026-07-15
                       Fedora
                       FEDORA-2026-d7dfd8e9ba (https://lwn.net/Articles/1082790/)
                       F43
                       golang-github-openprinting-ipp-usb
                       2026-07-14
                       Fedora
                       FEDORA-2026-a5e27945f7 (https://lwn.net/Articles/1082530/)
                       F44
                       jfrog-cli
                       2026-07-11
                       Fedora
                       FEDORA-2026-d6f3a0fa5a (https://lwn.net/Articles/1082200/)
                       F43
                       k9s
                       2026-07-10
                       Fedora
                       FEDORA-2026-4890ba29de (https://lwn.net/Articles/1082199/)
                       F44
                       k9s
                       2026-07-10
                       Fedora
                       FEDORA-2026-085c9e92a4 (https://lwn.net/Articles/1082978/)
                       F43
                       kernel
                       2026-07-14
                       Fedora
                       FEDORA-2026-e8e294a7fa (https://lwn.net/Articles/1082979/)
                       F44
                       kernel
                       2026-07-14
                       Fedora
                       FEDORA-2026-e48c1b5f93 (https://lwn.net/Articles/1082202/)
                       F43
                       kind
                       2026-07-10
                       Fedora
                       FEDORA-2026-b902c91814 (https://lwn.net/Articles/1082201/)
                       F44
                       kind
                       2026-07-10
                       Fedora
                       FEDORA-2026-18ea3f47f8 (https://lwn.net/Articles/1082533/)
                       F43
                       libXfont2
                       2026-07-12
                       Fedora
                       FEDORA-2026-43652cd5e8 (https://lwn.net/Articles/1082203/)
                       F44
                       libXfont2
                       2026-07-10
                       Fedora
                       FEDORA-2026-fc2f661416 (https://lwn.net/Articles/1082531/)
                       F44
                       librabbitmq
                       2026-07-11
                       Fedora
                       FEDORA-2026-eed9e67393 (https://lwn.net/Articles/1082532/)
                       F43
                       libssh2
                       2026-07-12
                       Fedora
                       FEDORA-2026-43767b6007 (https://lwn.net/Articles/1082534/)
                       F44
                       log4cxx
                       2026-07-12
                       Fedora
                       FEDORA-2026-602d919dbc (https://lwn.net/Articles/1082204/)
                       F43
                       nmap
                       2026-07-10
                       Fedora
                       FEDORA-2026-95b955a09b (https://lwn.net/Articles/1082536/)
                       F43
                       openssh
                       2026-07-11
                       Fedora
                       FEDORA-2026-a80275b42d (https://lwn.net/Articles/1081948/)
                       F44
                       openssh
                       2026-07-09
                       Fedora
                       FEDORA-2026-387cf555e7 (https://lwn.net/Articles/1081950/)
                       F43
                       opkssh
                       2026-07-09
                       Fedora
                       FEDORA-2026-a7570524a7 (https://lwn.net/Articles/1081949/)
                       F44
                       opkssh
                       2026-07-09
                       Fedora
                       FEDORA-2026-695fd36daa (https://lwn.net/Articles/1082537/)
                       F44
                       p11-kit
                       2026-07-12
                       Fedora
                       FEDORA-2026-377015b34b (https://lwn.net/Articles/1082205/)
                       F44
                       pam
                       2026-07-10
                       Fedora
                       FEDORA-2026-abc468979d (https://lwn.net/Articles/1081952/)
                       F43
                       perl-CSS-Minifier-XS
                       2026-07-09
                       Fedora
                       FEDORA-2026-9f14575d85 (https://lwn.net/Articles/1081951/)
                       F44
                       perl-CSS-Minifier-XS
                       2026-07-09
                       Fedora
                       FEDORA-2026-b77b9c5f04 (https://lwn.net/Articles/1082538/)
                       F43
                       perl-Crypt-DSA
                       2026-07-12
                       Fedora
                       FEDORA-2026-fcfc08d46c (https://lwn.net/Articles/1082539/)
                       F44
                       perl-Crypt-DSA
                       2026-07-12
                       Fedora
                       FEDORA-2026-9fdda5018f (https://lwn.net/Articles/1082206/)
                       F44
                       perl-DBI
                       2026-07-10
                       Fedora
                       FEDORA-2026-a457bf78b4 (https://lwn.net/Articles/1082541/)
                       F43
                       perl-HTML-Gumbo
                       2026-07-11
                       Fedora
                       FEDORA-2026-75010c7f44 (https://lwn.net/Articles/1082540/)
                       F44
                       perl-HTML-Gumbo
                       2026-07-11
                       Fedora
                       FEDORA-2026-f4272d87ef (https://lwn.net/Articles/1082208/)
                       F43
                       php
                       2026-07-10
                       Fedora
                       FEDORA-2026-ec9cb4652f (https://lwn.net/Articles/1082207/)
                       F44
                       php
                       2026-07-10
                       Fedora
                       FEDORA-2026-4179e03375 (https://lwn.net/Articles/1082543/)
                       F43
                       prometheus
                       2026-07-11
                       Fedora
                       FEDORA-2026-6a44db4fa9 (https://lwn.net/Articles/1082980/)
                       F43
                       prometheus
                       2026-07-14
                       Fedora
                       FEDORA-2026-01a1840582 (https://lwn.net/Articles/1082542/)
                       F44
                       prometheus
                       2026-07-11
                       Fedora
                       FEDORA-2026-e07fd81708 (https://lwn.net/Articles/1082981/)
                       F44
                       prometheus
                       2026-07-14
                       Fedora
                       FEDORA-2026-fbd55e52fb (https://lwn.net/Articles/1082544/)
                       F44
                       python-dulwich
                       2026-07-12
                       Fedora
                       FEDORA-2026-822c07add4 (https://lwn.net/Articles/1082545/)
                       F44
                       python-idna
                       2026-07-12
                       Fedora
                       FEDORA-2026-f774d1a878 (https://lwn.net/Articles/1081954/)
                       F43
                       python-jiter
                       2026-07-09
                       Fedora
                       FEDORA-2026-a7f46c285f (https://lwn.net/Articles/1081953/)
                       F44
                       python-jiter
                       2026-07-09
                       Fedora
                       FEDORA-2026-5ebb12f543 (https://lwn.net/Articles/1081955/)
                       F44
                       python-nh3
                       2026-07-09
                       Fedora
                       FEDORA-2026-e55bcd0c54 (https://lwn.net/Articles/1082209/)
                       F43
                       python-pendulum
                       2026-07-10
                       Fedora
                       FEDORA-2026-2559684e58 (https://lwn.net/Articles/1081956/)
                       F44
                       python-pendulum
                       2026-07-09
                       Fedora
                       FEDORA-2026-46c4892063 (https://lwn.net/Articles/1082546/)
                       F44
                       python-pillow
                       2026-07-11
                       Fedora
                       FEDORA-2026-23656e6d2f (https://lwn.net/Articles/1082547/)
                       F43
                       python-tornado
                       2026-07-12
                       Fedora
                       FEDORA-2026-0f40de2581 (https://lwn.net/Articles/1082548/)
                       F44
                       python-tornado
                       2026-07-12
                       Fedora
                       FEDORA-2026-f774d1a878 (https://lwn.net/Articles/1081958/)
                       F43
                       rust-jiter
                       2026-07-09
                       Fedora
                       FEDORA-2026-a7f46c285f (https://lwn.net/Articles/1081957/)
                       F44
                       rust-jiter
                       2026-07-09
                       Fedora
                       FEDORA-2026-5acfb0243b (https://lwn.net/Articles/1082549/)
                       F44
                       sssd
                       2026-07-11
                       Fedora
                       FEDORA-2026-5060f8da27 (https://lwn.net/Articles/1082211/)
                       F43
                       tmux
                       2026-07-10
                       Fedora
                       FEDORA-2026-7fa12630d5 (https://lwn.net/Articles/1082550/)
                       F43
                       tmux
                       2026-07-12
                       Fedora
                       FEDORA-2026-20eaa64d75 (https://lwn.net/Articles/1082210/)
                       F44
                       tmux
                       2026-07-10
                       Fedora
                       FEDORA-2026-f5dd9fb83f (https://lwn.net/Articles/1082551/)
                       F44
                       tmux
                       2026-07-11
                       Fedora
                       FEDORA-2026-ce80ea7afe (https://lwn.net/Articles/1082552/)
                       F43
                       upower
                       2026-07-12
                       Fedora
                       FEDORA-2026-e5305cffc2 (https://lwn.net/Articles/1081959/)
                       F44
                       upower
                       2026-07-09
                       Fedora
                       FEDORA-2026-3bc4b3ccb3 (https://lwn.net/Articles/1082553/)
                       F44
                       webkitgtk
                       2026-07-12
                       Fedora
                       FEDORA-2026-28b7854014 (https://lwn.net/Articles/1082554/)
                       F44
                       xorg-x11-server
                       2026-07-12
                       Fedora
                       FEDORA-2026-6a00d3109f (https://lwn.net/Articles/1082555/)
                       F43
                       xorg-x11-server-Xwayland
                       2026-07-12
                       Fedora
                       FEDORA-2026-a3d32667b8 (https://lwn.net/Articles/1082212/)
                       F44
                       xorg-x11-server-Xwayland
                       2026-07-10
                       Mageia
                       MGASA-2026-0238 (https://lwn.net/Articles/1082213/)
                       10
                       7zip
                       2026-07-09
                       Mageia
                       MGASA-2026-0239 (https://lwn.net/Articles/1082214/)
                       10, 9
                       ack
                       2026-07-09
                       Mageia
                       MGASA-2026-0249 (https://lwn.net/Articles/1082791/)
                       10, 9
                       ffmpeg
                       2026-07-14
                       Mageia
                       MGASA-2026-0245 (https://lwn.net/Articles/1082792/)
                       10, 9
                       gzip
                       2026-07-13
                       Mageia
                       MGASA-2026-0250 (https://lwn.net/Articles/1082793/)
                       10, 9
                       haproxy
                       2026-07-14
                       Mageia
                       MGASA-2026-0252 (https://lwn.net/Articles/1082982/)
                       10
                       imagemagick
                       2026-07-14
                       Mageia
                       MGASA-2026-0241 (https://lwn.net/Articles/1082556/)
                       10
                       libarchive
                       2026-07-11
                       Mageia
                       MGASA-2026-0247 (https://lwn.net/Articles/1082794/)
                       10
                       libheif
                       2026-07-13
                       Mageia
                       MGASA-2026-0246 (https://lwn.net/Articles/1082795/)
                       10
                       libtiff
                       2026-07-13
                       Mageia
                       MGASA-2026-0248 (https://lwn.net/Articles/1082796/)
                       10
                       libxml2
                       2026-07-14
                       Mageia
                       MGASA-2026-0236 (https://lwn.net/Articles/1081960/)
                       10, 9
                       openvpn
                       2026-07-08
                       Mageia
                       MGASA-2026-0242 (https://lwn.net/Articles/1082797/)
                       10, 9
                       packages
                       2026-07-13
                       Mageia
                       MGASA-2026-0243 (https://lwn.net/Articles/1082798/)
                       10, 9
                       packages
                       2026-07-13
                       Mageia
                       MGASA-2026-0244 (https://lwn.net/Articles/1082799/)
                       10, 9
                       perl-List-SomeUtils-XS
                       2026-07-13
                       Mageia
                       MGASA-2026-0251 (https://lwn.net/Articles/1082800/)
                       10, 9
                       perl-Socket
                       2026-07-14
                       Mageia
                       MGASA-2026-0240 (https://lwn.net/Articles/1082557/)
                       10, 9
                       vim
                       2026-07-10
                       Mageia
                       MGASA-2026-0237 (https://lwn.net/Articles/1081961/)
                       10
                       vips
                       2026-07-08
                       Oracle
                       ELSA-2026-36195 (https://lwn.net/Articles/1081962/)
                       OL9
                       389-ds-base
                       2026-07-08
                       Oracle
                       ELSA-2026-36201 (https://lwn.net/Articles/1082558/)
                       OL8
                       389-ds:1.4
                       2026-07-13
                       Oracle
                       ELSA-2026-36318 (https://lwn.net/Articles/1081963/)
                       OL9
                       aardvark-dns
                       2026-07-08
                       Oracle
                       ELSA-2026-37410 (https://lwn.net/Articles/1082559/)
                       OL9
                       buildah
                       2026-07-13
                       Oracle
                       ELSA-2026-38493 (https://lwn.net/Articles/1082983/)
                       OL9
                       buildah
                       2026-07-14
                       Oracle
                       ELSA-2026-36215 (https://lwn.net/Articles/1081964/)
                       OL8
                       compat-openssl10
                       2026-07-08
                       Oracle
                       ELSA-2026-35833 (https://lwn.net/Articles/1081965/)
                       OL8
                       container-tools:ol8
                       2026-07-08
                       Oracle
                       ELSA-2026-36733 (https://lwn.net/Articles/1082560/)
                       OL8
                       cups
                       2026-07-13
                       Oracle
                       ELSA-2026-36721 (https://lwn.net/Articles/1082561/)
                       OL8
                       edk2
                       2026-07-13
                       Oracle
                       ELSA-2026-36307 (https://lwn.net/Articles/1081966/)
                       OL8
                       freeipmi
                       2026-07-08
                       Oracle
                       ELSA-2026-36210 (https://lwn.net/Articles/1081967/)
                       OL9
                       freeipmi
                       2026-07-08
                       Oracle
                       ELSA-2026-38501 (https://lwn.net/Articles/1082984/)
                       OL8
                       freerdp
                       2026-07-14
                       Oracle
                       ELSA-2026-37207 (https://lwn.net/Articles/1082562/)
                       OL9
                       freerdp
                       2026-07-13
                       Oracle
                       ELSA-2026-38496 (https://lwn.net/Articles/1082985/)
                       OL9
                       gimp
                       2026-07-14
                       Oracle
                       ELSA-2026-37435 (https://lwn.net/Articles/1082563/)
                       OL9
                       golang
                       2026-07-13
                       Oracle
                       ELSA-2026-35830 (https://lwn.net/Articles/1082564/)
                       OL8
                       grafana
                       2026-07-13
                       Oracle
                       ELSA-2026-37130 (https://lwn.net/Articles/1082566/)
                       OL8
                       gstreamer1-plugins-bad-free
                       2026-07-13
                       Oracle
                       ELSA-2026-36834 (https://lwn.net/Articles/1082565/)
                       OL9
                       gstreamer1-plugins-bad-free
                       2026-07-13
                       Oracle
                       ELSA-2026-36774 (https://lwn.net/Articles/1082567/)
                       OL8
                       gstreamer1-plugins-good
                       2026-07-13
                       Oracle
                       ELSA-2026-37129 (https://lwn.net/Articles/1082568/)
                       OL9
                       gstreamer1-plugins-good
                       2026-07-13
                       Oracle
                       ELSA-2026-36674 (https://lwn.net/Articles/1082569/)
                       OL9
                       gstreamer1-plugins-ugly-free
                       2026-07-13
                       Oracle
                       ELSA-2026-50388 (https://lwn.net/Articles/1082574/)
                       OL7
                       kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-50387 (https://lwn.net/Articles/1082571/)
                       OL8
                       kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-50388 (https://lwn.net/Articles/1082572/)
                       OL8
                       kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-50388 (https://lwn.net/Articles/1082575/)
                       OL8
                       kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-33743 (https://lwn.net/Articles/1082986/)
                       OL8
                       kernel
                       2026-07-14
                       Oracle
                       ELSA-2026-36366 (https://lwn.net/Articles/1082987/)
                       OL8
                       kernel
                       2026-07-14
                       Oracle
                       ELSA-2026-30848 (https://lwn.net/Articles/1081968/)
                       OL9
                       kernel
                       2026-07-08
                       Oracle
                       ELSA-2026-33285 (https://lwn.net/Articles/1081969/)
                       OL9
                       kernel
                       2026-07-08
                       Oracle
                       ELSA-2026-50387 (https://lwn.net/Articles/1082570/)
                       OL9

kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-50387 (https://lwn.net/Articles/1082573/)
                       OL9
                       kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-36018 (https://lwn.net/Articles/1082576/)
                       OL9
                       kernel
                       2026-07-13
                       Oracle
                       ELSA-2026-36957 (https://lwn.net/Articles/1082988/)
                       OL9
                       kernel
                       2026-07-14
                       Oracle
                       ELSA-2026-26567 (https://lwn.net/Articles/1082577/)
                       OL7
                       libexif
                       2026-07-13
                       Oracle
                       ELSA-2026-36730 (https://lwn.net/Articles/1082578/)
                       OL8
                       libsolv
                       2026-07-13
                       Oracle
                       ELSA-2026-36728 (https://lwn.net/Articles/1082579/)
                       OL8
                       libtasn1
                       2026-07-13
                       Oracle
                       ELSA-2026-36734 (https://lwn.net/Articles/1082580/)
                       OL8
                       libxml2
                       2026-07-13
                       Oracle
                       ELSA-2026-25051 (https://lwn.net/Articles/1081970/)
                       OL9
                       libyang
                       2026-07-08
                       Oracle
                       ELSA-2026-36331 (https://lwn.net/Articles/1082989/)
                       OL9
                       nginx
                       2026-07-14
                       Oracle
                       ELSA-2026-36618 (https://lwn.net/Articles/1082581/)
                       OL9
                       nginx:1.24
                       2026-07-13
                       Oracle
                       ELSA-2026-36639 (https://lwn.net/Articles/1082582/)
                       OL9
                       nginx:1.26
                       2026-07-13
                       Oracle
                       ELSA-2026-35892 (https://lwn.net/Articles/1082583/)
                       OL9
                       nodejs:22
                       2026-07-13
                       Oracle
                       ELSA-2026-35891 (https://lwn.net/Articles/1082584/)
                       OL9
                       nodejs:24
                       2026-07-13
                       Oracle
                       ELSA-2026-36617 (https://lwn.net/Articles/1082585/)
                       OL9
                       oci-seccomp-bpf-hook
                       2026-07-13
                       Oracle
                       ELSA-2026-38498 (https://lwn.net/Articles/1082990/)
                       OL9
                       openexr
                       2026-07-14
                       Oracle
                       ELSA-2026-38503 (https://lwn.net/Articles/1082991/)
                       OL8
                       openssl
                       2026-07-14
                       Oracle
                       ELSA-2026-38512 (https://lwn.net/Articles/1082992/)
                       OL9
                       perl-DBI
                       2026-07-14
                       Oracle
                       ELSA-2026-36188 (https://lwn.net/Articles/1081971/)
                       OL8
                       perl-HTTP-Daemon
                       2026-07-08
                       Oracle
                       ELSA-2026-36187 (https://lwn.net/Articles/1081972/)
                       OL9
                       perl-HTTP-Daemon
                       2026-07-08
                       Oracle
                       ELSA-2026-37123 (https://lwn.net/Articles/1082586/)
                       OL9
                       podman
                       2026-07-13
                       Oracle
                       ELSA-2026-38878 (https://lwn.net/Articles/1082993/)
                       OL9
                       podman
                       2026-07-14
                       Oracle
                       ELSA-2026-26204 (https://lwn.net/Articles/1082587/)
                       OL9
                       postgresql:18
                       2026-07-13
                       Oracle
                       ELSA-2026-36732 (https://lwn.net/Articles/1082588/)
                       OL8
                       python-urllib3
                       2026-07-13
                       Oracle
                       ELSA-2026-36315 (https://lwn.net/Articles/1081973/)
                       OL9
                       python3.14-pip
                       2026-07-08
                       Oracle
                       ELSA-2026-36317 (https://lwn.net/Articles/1081974/)
                       OL9
                       skopeo
                       2026-07-08
                       Oracle
                       ELSA-2026-22456 (https://lwn.net/Articles/1082589/)
                       OL7
                       tigervnc
                       2026-07-10
                       Oracle
                       ELSA-2026-37137 (https://lwn.net/Articles/1082590/)
                       OL8
                       tomcat
                       2026-07-13
                       Oracle
                       ELSA-2026-36879 (https://lwn.net/Articles/1082591/)
                       OL9
                       tomcat
                       2026-07-13
                       Oracle
                       ELSA-2026-37282 (https://lwn.net/Articles/1082592/)
                       OL8
                       unbound
                       2026-07-13
                       Oracle
                       ELSA-2026-36777 (https://lwn.net/Articles/1082593/)
                       OL9
                       unbound
                       2026-07-13
                       Oracle
                       ELSA-2026-38510 (https://lwn.net/Articles/1082994/)
                       OL8
                       vim
                       2026-07-14
                       Oracle
                       ELSA-2026-38511 (https://lwn.net/Articles/1082995/)
                       OL9
                       vim
                       2026-07-14
                       Oracle
                       ELSA-2026-20590 (https://lwn.net/Articles/1082594/)
                       OL7
                       xorg-x11-server
                       2026-07-10
                       Oracle
                       ELSA-2026-38486 (https://lwn.net/Articles/1082996/)
                       OL9
                       xorg-x11-server
                       2026-07-14
                       Oracle
                       ELSA-2026-38488 (https://lwn.net/Articles/1082997/)
                       OL8
                       xorg-x11-server-Xwayland
                       2026-07-14
                       Red Hat
                       RHSA-2026:39893-01 (https://lwn.net/Articles/1082947/)
                       EL8
                       python3.12
                       2026-07-15
                       Slackware
                       SSA:2026-189-01 (https://lwn.net/Articles/1081975/)
                       
                       libXfont2
                       2026-07-08
                       Slackware
                       SSA:2026-191-01 (https://lwn.net/Articles/1082595/)
                       
                       p11-kit
                       2026-07-10
                       Slackware
                       SSA:2026-189-02 (https://lwn.net/Articles/1081976/)
                       
                       proftpd
                       2026-07-08
                       Slackware
                       SSA:2026-190-01 (https://lwn.net/Articles/1082215/)
                       
                       tigervnc
                       2026-07-09
                       Slackware
                       SSA:2026-189-03 (https://lwn.net/Articles/1081977/)
                       
                       xorg-server
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2820-1 (https://lwn.net/Articles/1082232/)
                       SLE15 oS15.6
                       GraphicsMagick
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2877-1 (https://lwn.net/Articles/1082809/)
                       SLE15
                       ImageMagick
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11228-1 (https://lwn.net/Articles/1082606/)
                       TW
                       ImageMagick
                       2026-07-11
                       SUSE
                       SUSE-SU-2026:22528-1 (https://lwn.net/Articles/1082248/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22527-1 (https://lwn.net/Articles/1082249/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22536-1 (https://lwn.net/Articles/1082251/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22534-1 (https://lwn.net/Articles/1082254/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22533-1 (https://lwn.net/Articles/1082255/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22532-1 (https://lwn.net/Articles/1082256/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22530-1 (https://lwn.net/Articles/1082258/)
                       SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22535-1 (https://lwn.net/Articles/1082253/)
                       SLE-m6 SLE-m6.0 SLE-m6.1 oS16
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22531-1 (https://lwn.net/Articles/1082257/)
                       SLE15 SLE-m6 SLE-m6.0 SLE-m6.1
                       SUSE_Multi-Linux_Manager Client Tools
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11255-1 (https://lwn.net/Articles/1082998/)
                       TW
                       afterburn
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:0243-1 (https://lwn.net/Articles/1082999/)
                       osB15
                       afterburn
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:21292-1 (https://lwn.net/Articles/1082596/)
                       oS16.0
                       agama
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2824-1 (https://lwn.net/Articles/1082216/)
                       SLE15
                       alloy
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21251-1 (https://lwn.net/Articles/1081978/)
                       oS16.0
                       alloy
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2885-1 (https://lwn.net/Articles/1082801/)
                       SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4
                       alsa
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21235-1 (https://lwn.net/Articles/1081979/)
                       oS16.0
                       apache2
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:11197-1 (https://lwn.net/Articles/1081980/)
                       TW
                       apptainer
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:21242-1 (https://lwn.net/Articles/1081981/)
                       oS16.0
                       assimp
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2964-1 (https://lwn.net/Articles/1083000/)
                       SLE15 oS15.4
                       buildah
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:11256-1 (https://lwn.net/Articles/1083001/)
                       TW
                       busybox
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:11210-1 (https://lwn.net/Articles/1082217/)
                       TW
                       cargo-c
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:11254-1 (https://lwn.net/Articles/1082802/)
                       TW
                       chromedriver
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:0233-1 (https://lwn.net/Articles/1081982/)
                       osB15
                       chromium
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:0238-1 (https://lwn.net/Articles/1082218/)
                       osB15
                       chromium
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2833-1 (https://lwn.net/Articles/1082221/)
                       SLE12
                       clamav
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2834-1 (https://lwn.net/Articles/1082220/)
                       SLE15 oS15.4
                       clamav
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2835-1 (https://lwn.net/Articles/1082219/)
                       SLE15 oS15.6
                       clamav
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21252-1 (https://lwn.net/Articles/1081983/)
                       oS16.0
                       clamav
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2827-1 (https://lwn.net/Articles/1082222/)
                       SLE15 oS15.4
                       cosign
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22553-1 (https://lwn.net/Articles/1082804/)
                       SLE-m6.2
                       curl
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2926-1 (https://lwn.net/Articles/1082803/)
                       SLE15 oS15.6
                       curl
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:21301-1 (https://lwn.net/Articles/1082597/)
                       oS16.0
                       dash
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:22542-1 (https://lwn.net/Articles/1082805/)
                       SLE-m6.2
                       dhcpcd
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11213-1 (https://lwn.net/Articles/1082223/)
                       TW
                       dirmngr
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:22513-1 (https://lwn.net/Articles/1081984/)
                       SLE-m6.0
                       docker
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22546-1 (https://lwn.net/Articles/1082806/)
                       SLE-m6.2
                       docker-compose
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21247-1 (https://lwn.net/Articles/1081985/)
                       oS16.0
                       docker-compose
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2851-1 (https://lwn.net/Articles/1082598/)
                       SLE15
                       dracut
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2803-1 (https://lwn.net/Articles/1081986/)
                       SLE15 oS15.6
                       dracut
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:0245-1 (https://lwn.net/Articles/1083002/)
                       osB15
                       enc
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:2582-2 (https://lwn.net/Articles/1082224/)
                       SLE15
                       firefox
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:2814-1 (https://lwn.net/Articles/1082225/)
                       SLE15
                       firefox
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:11231-1 (https://lwn.net/Articles/1082599/)
                       TW
                       flannel
                       2026-07-11
                       SUSE
                       openSUSE-SU-2026:0239-1 (https://lwn.net/Articles/1082226/)
                       osB15
                       flannel
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11211-1 (https://lwn.net/Articles/1082227/)
                       TW
                       fluidsynth
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:11257-1 (https://lwn.net/Articles/1083003/)
                       TW
                       freetype2-devel
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2810-1 (https://lwn.net/Articles/1081987/)
                       SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4
                       glib-networking
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:22538-1 (https://lwn.net/Articles/1082807/)
                       SLE-m6.2
                       glibc
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2822-1 (https://lwn.net/Articles/1082228/)
                       SLE5.3 SLE-m5.3
                       gnutls
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:0232-1 (https://lwn.net/Articles/1081988/)
                       osB15
                       go-sendxmpp
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2817-1 (https://lwn.net/Articles/1082229/)
                       SLE15
                       go1.25
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21324-1 (https://lwn.net/Articles/1083004/)
                       oS16.0
                       go1.25
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:21319-1 (https://lwn.net/Articles/1083005/)
                       oS16.0
                       go1.25-openssl
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:2818-1 (https://lwn.net/Articles/1082230/)
                       SLE15
                       go1.26
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11232-1 (https://lwn.net/Articles/1082600/)
                       TW
                       go1.26
                       2026-07-11
                       SUSE
                       openSUSE-SU-2026:21254-1 (https://lwn.net/Articles/1081989/)
                       oS16.0
                       go1.26-openssl
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:21321-1 (https://lwn.net/Articles/1083006/)
                       oS16.0
                       go1.26-openssl
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:11212-1 (https://lwn.net/Articles/1082231/)
                       TW
                       gol
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:0244-1 (https://lwn.net/Articles/1083007/)
                       osB15
                       gosec
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:21351-1 (https://lwn.net/Articles/1083008/)
                       oS16.0
                       grafana
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:21303-1 (https://lwn.net/Articles/1082601/)
                       oS16.0
                       gsasl
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2844-1 (https://lwn.net/Articles/1082602/)
                       SLE15 oS15.4
                       gstreamer-plugins-good
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2842-1 (https://lwn.net/Articles/1082604/)
                       SLE15 oS15.5
                       gstreamer-plugins-good
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2843-1 (https://lwn.net/Articles/1082603/)
                       SLE15 oS15.6
                       gstreamer-plugins-good
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21240-1 (https://lwn.net/Articles/1081990/)
                       oS16.0
                       gstreamer-plugins-good
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22515-1 (https://lwn.net/Articles/1081991/)
                       SLE-m6.0
                       haproxy
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22544-1 (https://lwn.net/Articles/1082808/)
                       SLE-m6.2
                       haproxy
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21262-1 (https://lwn.net/Articles/1081992/)
                       oS16.0
                       hauler
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2823-1 (https://lwn.net/Articles/1082233/)
                       SLE15 SLE5.5 SLE-m5.5
                       helm
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21331-1 (https://lwn.net/Articles/1083009/)
                       oS16.0
                       helm
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:21291-1 (https://lwn.net/Articles/1082605/)
                       oS16.0
                       imagemagick
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2801-1 (https://lwn.net/Articles/1081993/)
                       SLE15
                       jackson-annotations, jackson-bom, jackson-core, jackson- databind, jackson-dataformats-binary, jackson-modules-base, jackson-parent
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:22545-1 (https://lwn.net/Articles/1082810/)
                       SLE-m6.2
                       jq
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2839-1 (https://lwn.net/Articles/1082608/)
                       SLE11
                       kernel
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2914-1 (https://lwn.net/Articles/1082811/)
                       SLE12
                       kernel
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2799-1 (https://lwn.net/Articles/1081999/)
                       SLE15
                       kernel
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2800-1 (https://lwn.net/Articles/1081998/)
                       SLE15
                       kernel
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2841-1 (https://lwn.net/Articles/1082607/)
                       SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4
                       kernel
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2840-1 (https://lwn.net/Articles/1082609/)
                       SLE15 SLE5.5 SLE-m5.5 oS15.5
                       kernel
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:22522-1 (https://lwn.net/Articles/1081994/)
                       SLE6.0 SLE-m6.0
                       kernel
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22521-1 (https://lwn.net/Articles/1081995/)
                       SLE6.0 SLE-m6.0
                       kernel
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22511-1 (https://lwn.net/Articles/1081997/)
                       SLE6.0 SLE-m6.0
                       kernel
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22512-1 (https://lwn.net/Articles/1081996/)
                       SLE6.0 SLE-m6.0
                       kernel
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:11214-1 (https://lwn.net/Articles/1082234/)
                       TW
                       kernel-devel
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:2848-1 (https://lwn.net/Articles/1082612/)
                       SLE15 oS15.6
                       krb5, krb5-mini
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2849-1 (https://lwn.net/Articles/1082611/)
                       SLE12
                       krb5
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2954-1 (https://lwn.net/Articles/1083010/)
                       SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4
                       krb5
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2847-1 (https://lwn.net/Articles/1082610/)
                       SLE15 SLE5.5 SLE-m5.5 oS15.5
                       krb5
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21238-1 (https://lwn.net/Articles/1082000/)
                       oS16.0
                       krb5
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2942-1 (https://lwn.net/Articles/1082812/)
                       SLE15 oS15.6
                       kubernetes
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2965-1 (https://lwn.net/Articles/1083011/)
                       SLE15 oS15.6
                       kubernetes-old
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2804-1 (https://lwn.net/Articles/1082001/)
                       SLE15
                       kubevirt
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:11218-1 (https://lwn.net/Articles/1082613/)
                       TW
                       libIex-3_4-33
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2793-1 (https://lwn.net/Articles/1082004/)
                       SLE12
                       libXfont2
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2794-1 (https://lwn.net/Articles/1082003/)
                       SLE15
                       libXfont2
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2829-1 (https://lwn.net/Articles/1082235/)
                       SLE15 oS15.4
                       libaom
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2838-1 (https://lwn.net/Articles/1082236/)
                       SLE12
                       libexif
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2837-1 (https://lwn.net/Articles/1082237/)
                       SLE15
                       libexif
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11215-1 (https://lwn.net/Articles/1082614/)
                       TW
                       libmbedtls23
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11259-1 (https://lwn.net/Articles/1083012/)
                       TW
                       libopenbabel8
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2878-1 (https://lwn.net/Articles/1082813/)
                       SLE12
                       libpng15
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11247-1 (https://lwn.net/Articles/1082814/)
                       TW
                       libredwg-devel
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:22514-1 (https://lwn.net/Articles/1082002/)
                       SLE-m6.0
                       libslirp
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2931-1 (https://lwn.net/Articles/1082815/)
                       SLE15 SLE5.5 SLE-m5.5 oS15.5
                       libslirp
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2886-1 (https://lwn.net/Articles/1082816/)
                       SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.3
                       libslirp
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21284-1 (https://lwn.net/Articles/1082615/)
                       oS16.0
                       libxfont2
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11258-1 (https://lwn.net/Articles/1083014/)
                       TW
                       libxml2-16
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:21317-1 (https://lwn.net/Articles/1083013/)
                       oS16.0
                       libxml2
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:21267-1 (https://lwn.net/Articles/1082005/)
                       oS16.0
                       mpv, libkpipewirerecord6, ffmpegthumbs-kf5
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:11217-1 (https://lwn.net/Articles/1082616/)
                       TW
                       nasm
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21333-1 (https://lwn.net/Articles/1083015/)
                       oS16.0
                       nasm
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:2802-1 (https://lwn.net/Articles/1082006/)
                       SLE15
                       netty, netty-tcnative
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:2883-1 (https://lwn.net/Articles/1082817/)
                       SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5
                       nghttp2
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21302-1 (https://lwn.net/Articles/1082617/)
                       oS16.0
                       nghttp2
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:0235-1 (https://lwn.net/Articles/1082238/)
                       osB15
                       openQA, os-autoinst
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:21266-1 (https://lwn.net/Articles/1082007/)
                       oS16.0
                       openqa, os-autoinst
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:3005-1 (https://lwn.net/Articles/1083017/)
                       SLE15 oS15.5
                       openssl-3
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:3004-1 (https://lwn.net/Articles/1083016/)
                       SLE15 oS15.6
                       openssl-3
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:11260-1 (https://lwn.net/Articles/1083019/)
                       TW
                       patch
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:21332-1 (https://lwn.net/Articles/1083018/)
                       oS16.0
                       patch
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:0240-1 (https://lwn.net/Articles/1082618/)
                       osB15
                       perl-CGI-Session
                       2026-07-12
                       SUSE
                       SUSE-SU-2026:2845-1 (https://lwn.net/Articles/1082620/)
                       SLE15
                       perl-List-SomeUtils-XS
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21293-1 (https://lwn.net/Articles/1082619/)
                       oS16.0
                       perl-dbi
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2880-1 (https://lwn.net/Articles/1082818/)
                       oS15.4
                       php8
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:22516-1 (https://lwn.net/Articles/1082009/)
                       SLE-m6.0
                       podman
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:21244-1 (https://lwn.net/Articles/1082008/)
                       oS16.0
                       podman
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2968-1 (https://lwn.net/Articles/1083020/)
                       SLE15 oS15.6
                       python-Authlib
                       2026-07-14
                       SUSE
                       SUSE-SU-2026:2819-1 (https://lwn.net/Articles/1082239/)
                       SLE15 oS15.6
                       python-Django
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2875-1 (https://lwn.net/Articles/1082819/)
                       SLE15 oS15.3
                       python-Pillow
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2828-1 (https://lwn.net/Articles/1082240/)
                       MP4.3 SLE15 oS15.4
                       python-idna
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2811-1 (https://lwn.net/Articles/1082010/)
                       oS15.6
                       python-maturin
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:2949-1 (https://lwn.net/Articles/1083022/)
                       SLE15 oS15.4
                       python-mistune
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:21339-1 (https://lwn.net/Articles/1083021/)
                       oS16.0
                       python-mistune
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:21239-1 (https://lwn.net/Articles/1082011/)
                       oS16.0
                       python-msgpack
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:21296-1 (https://lwn.net/Articles/1082621/)
                       oS16.0
                       python-pillow
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:0241-1 (https://lwn.net/Articles/1082622/)
                       osB15
                       python-social-auth-app-django
                       2026-07-12
                       SUSE
                       openSUSE-SU-2026:21342-1 (https://lwn.net/Articles/1083023/)
                       oS16.0
                       python-soupsieve
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:2821-1 (https://lwn.net/Articles/1082241/)
                       SLE15
                       python-sqlparse
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:21343-1 (https://lwn.net/Articles/1083024/)
                       oS16.0
                       python-sqlparse
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:2854-1 (https://lwn.net/Articles/1082623/)
                       SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.3
                       python-urllib3
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2984-1 (https://lwn.net/Articles/1083025/)
                       SLE15 oS15.4
                       python3-dulwich
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:11248-1 (https://lwn.net/Articles/1082820/)
                       TW
                       python313-Django
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11235-1 (https://lwn.net/Articles/1082624/)
                       TW
                       python313-Django4
                       2026-07-12
                       SUSE
                       openSUSE-SU-2026:11236-1 (https://lwn.net/Articles/1082625/)
                       TW
                       python313-Django6
                       2026-07-12
                       SUSE
                       openSUSE-SU-2026:11261-1 (https://lwn.net/Articles/1083026/)
                       TW
                       python313-Pillow
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:11220-1 (https://lwn.net/Articles/1082626/)
                       TW
                       python313-pytest-html
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11221-1 (https://lwn.net/Articles/1082627/)
                       TW
                       python313-sqlparse
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11249-1 (https://lwn.net/Articles/1082821/)
                       TW
                       python313-weasyprint
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11240-1 (https://lwn.net/Articles/1082628/)
                       TW
                       python313-websockets
                       2026-07-12
                       SUSE
                       openSUSE-SU-2026:11196-1 (https://lwn.net/Articles/1082012/)
                       TW
                       python313-yt-dlp
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22550-1 (https://lwn.net/Articles/1082822/)
                       SLE-m6.2
                       qemu
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:0231-1 (https://lwn.net/Articles/1082013/)
                       osB15
                       radare2
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:11241-1 (https://lwn.net/Articles/1082629/)
                       TW
                       rclone
                       2026-07-12
                       SUSE
                       SUSE-SU-2026:3000-1 (https://lwn.net/Articles/1083027/)
                       SLE15 oS15.6
                       rootlesskit
                       2026-07-15
                       SUSE
                       SUSE-SU-2026:22554-1 (https://lwn.net/Articles/1082823/)
                       SLE-m6.2
                       rust-keylime
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2825-1 (https://lwn.net/Articles/1082243/)
                       SLE5.3 SLE-m5.3
                       rust-keylime
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2826-1 (https://lwn.net/Articles/1082242/)
                       SLE5.4 SLE-m5.4
                       rust-keylime
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2807-1 (https://lwn.net/Articles/1082014/)
                       SLE5.5 SLE-m5.5
                       rust-keylime
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:21274-1 (https://lwn.net/Articles/1082630/)
                       oS16.0
                       rust-keylime
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2831-1 (https://lwn.net/Articles/1082246/)
                       SLE15 oS15.4
                       rustup
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2832-1 (https://lwn.net/Articles/1082245/)
                       SLE15 oS15.6
                       rustup
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11205-1 (https://lwn.net/Articles/1082244/)
                       TW
                       rustup
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:11223-1 (https://lwn.net/Articles/1082631/)
                       TW
                       rustup
                       2026-07-10
                       SUSE
                       openSUSE-SU-2026:11262-1 (https://lwn.net/Articles/1083028/)
                       TW
                       sbootutil-1
                       2026-07-14
                       SUSE
                       openSUSE-SU-2026:11206-1 (https://lwn.net/Articles/1082247/)
                       TW
                       sccache
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:11224-1 (https://lwn.net/Articles/1082632/)
                       TW
                       sccache
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2874-1 (https://lwn.net/Articles/1082824/)
                       oS15.4
                       sccache
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:11242-1 (https://lwn.net/Articles/1082633/)
                       TW
                       spectre-meltdown-checker
                       2026-07-12
                       SUSE
                       openSUSE-SU-2026:21290-1 (https://lwn.net/Articles/1082634/)
                       oS16.0
                       sssd
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2785-1 (https://lwn.net/Articles/1082016/)
                       SLE5.2 SLE-m5.2 oS15.3
                       systemd, systemd-mini
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:22537-1 (https://lwn.net/Articles/1082825/)
                       SLE-m6.2
                       systemd
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2809-1 (https://lwn.net/Articles/1082015/)
                       SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4
                       systemd
                       2026-07-09
                       SUSE
                       SUSE-SU-2026:2850-1 (https://lwn.net/Articles/1082635/)
                       MP4.3 SLE15
                       terraform-provider-aws, terraform-provider-azurerm, terraform-provider-external, terraform-provider-google, terraform-provider-helm, terraform-provider-kubernetes, terraform-provid
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2852-1 (https://lwn.net/Articles/1082636/)
                       SLE15
                       thunderbird
                       2026-07-13
                       SUSE
                       SUSE-SU-2026:2853-1 (https://lwn.net/Articles/1082638/)
                       SLE15 oS15.6
                       tiff
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21289-1 (https://lwn.net/Articles/1082637/)
                       oS16.0
                       tiff
                       2026-07-13
                       SUSE
                       openSUSE-SU-2026:21327-1 (https://lwn.net/Articles/1083029/)
                       oS16.0
                       tomcat
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:11195-1 (https://lwn.net/Articles/1082017/)
                       TW
                       tomcat11
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:21329-1 (https://lwn.net/Articles/1083030/)
                       oS16.0
                       tomcat11
                       2026-07-15
                       SUSE
                       openSUSE-SU-2026:11243-1 (https://lwn.net/Articles/1082639/)
                       TW
                       traefik2
                       2026-07-12
                       SUSE
                       openSUSE-SU-2026:0237-1 (https://lwn.net/Articles/1082250/)
                       osB15
                       transmission
                       2026-07-09
                       SUSE
                       openSUSE-SU-2026:21249-1 (https://lwn.net/Articles/1082018/)
                       oS16.0
                       trivy
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2830-1 (https://lwn.net/Articles/1082252/)
                       SLE15 oS15.5
                       warewulf4
                       2026-07-10
                       SUSE
                       SUSE-SU-2026:2792-1 (https://lwn.net/Articles/1082019/)
                       SLE12
                       xorg-x11-server
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2788-1 (https://lwn.net/Articles/1082022/)
                       SLE15
                       xorg-x11-server
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2789-1 (https://lwn.net/Articles/1082021/)
                       SLE15 oS15.4
                       xorg-x11-server
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2791-1 (https://lwn.net/Articles/1082020/)
                       SLE15 oS15.5
                       xorg-x11-server
                       2026-07-08
                       SUSE
                       SUSE-SU-2026:2786-1 (https://lwn.net/Articles/1082023/)
                       SLE15 oS15.6
                       xorg-x11-server
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:11244-1 (https://lwn.net/Articles/1082640/)
                       TW
                       xorg-x11-server
                       2026-07-12
                       SUSE
                       SUSE-SU-2026:2787-1 (https://lwn.net/Articles/1082024/)
                       SLE15
                       xwayland
                       2026-07-08
                       SUSE
                       openSUSE-SU-2026:21283-1 (https://lwn.net/Articles/1082641/)
                       oS16.0
                       xwayland
                       2026-07-13
                       Ubuntu
                       USN-8538-1 (https://lwn.net/Articles/1083031/)
                       22.04 24.04 26.04
                       alsa-lib
                       2026-07-14
                       Ubuntu
                       USN-8516-1 (https://lwn.net/Articles/1082025/)
                       22.04 24.04 26.04
                       apache2
                       2026-07-08
                       Ubuntu
                       USN-8496-3 (https://lwn.net/Articles/1082826/)
                       22.04 24.04 26.04
                       cifs-utils
                       2026-07-13
                       Ubuntu
                       USN-8517-1 (https://lwn.net/Articles/1082026/)
                       22.04 24.04 26.04
                       clamav
                       2026-07-08
                       Ubuntu
                       USN-8525-1 (https://lwn.net/Articles/1082259/)
                       14.04 16.04 18.04 20.04 24.04 25.10 26.04
                       curl
                       2026-07-09
                       Ubuntu
                       USN-8542-1 (https://lwn.net/Articles/1083032/)
                       16.04 18.04 20.04 22.04 24.04 26.04
                       dnsmasq
                       2026-07-14
                       Ubuntu
                       USN-8520-1 (https://lwn.net/Articles/1082260/)
                       16.04
                       expat
                       2026-07-09
                       Ubuntu
                       USN-8539-1 (https://lwn.net/Articles/1083033/)
                       16.04 18.04 20.04
                       gnutls28
                       2026-07-14
                       Ubuntu
                       USN-8519-1 (https://lwn.net/Articles/1082261/)
                       16.04 18.04 20.04 22.04 24.04 25.10
                       golang-go.crypto
                       2026-07-09
                       Ubuntu
                       USN-8531-1 (https://lwn.net/Articles/1082827/)
                       22.04 24.04 26.04
                       libexif
                       2026-07-13
                       Ubuntu
                       USN-8526-2 (https://lwn.net/Articles/1083034/)
                       24.04
                       libheif
                       2026-07-14
                       Ubuntu
                       USN-8526-1 (https://lwn.net/Articles/1082262/)
                       25.10 26.04
                       libheif
                       2026-07-09
                       Ubuntu
                       USN-8521-1 (https://lwn.net/Articles/1082263/)
                       22.04 24.04 26.04
                       libidn
                       2026-07-09
                       Ubuntu
                       USN-8522-1 (https://lwn.net/Articles/1082264/)
                       22.04 24.04 26.04
                       libraw
                       2026-07-09
                       Ubuntu
                       USN-8534-1 (https://lwn.net/Articles/1082828/)
                       22.04 24.04 26.04
                       libreoffice
                       2026-07-13
                       Ubuntu
                       USN-8523-1 (https://lwn.net/Articles/1082265/)
                       16.04 18.04 20.04 22.04 24.04 25.10 26.04
                       libsoup2.4
                       2026-07-09
                       Ubuntu
                       USN-8532-1 (https://lwn.net/Articles/1082829/)
                       24.04 26.04
                       libssh2
                       2026-07-13
                       Ubuntu
                       USN-8529-1 (https://lwn.net/Articles/1082266/)
                       18.04
                       linux, linux-azure-4.15, linux-azure-fips, linux-fips, linux-gcp-4.15, linux-gcp-fips, linux-kvm, linux-oracle
                       2026-07-10
                       Ubuntu
                       USN-8530-1 (https://lwn.net/Articles/1082267/)
                       18.04
                       linux-aws, linux-aws-fips
                       2026-07-10
                       Ubuntu
                       USN-8548-1 (https://lwn.net/Articles/1083035/)
                       14.04 16.04
                       linux-aws, linux-fips, linux-lts-xenial
                       2026-07-15
                       Ubuntu
                       USN-8492-5 (https://lwn.net/Articles/1082268/)
                       24.04
                       linux-azure-fips, linux-fips
                       2026-07-10
                       Ubuntu
                       USN-8547-1 (https://lwn.net/Articles/1083036/)
                       20.04
                       linux-gcp-5.15, linux-intel-iotg-5.15
                       2026-07-15
                       Ubuntu
                       USN-8545-1 (https://lwn.net/Articles/1083037/)
                       24.04
                       linux-hwe-6.17
                       2026-07-15
                       Ubuntu
                       USN-8527-1 (https://lwn.net/Articles/1082269/)
                       22.04
                       linux-raspi
                       2026-07-10
                       Ubuntu
                       USN-8492-4 (https://lwn.net/Articles/1082028/)
                       24.04
                       linux-raspi
                       2026-07-09
                       Ubuntu
                       USN-8490-2 (https://lwn.net/Articles/1082027/)
                       25.10
                       linux-raspi
                       2026-07-09
                       Ubuntu
                       USN-8546-1 (https://lwn.net/Articles/1083038/)
                       25.10
                       linux-raspi
                       2026-07-15
                       Ubuntu
                       USN-8528-1 (https://lwn.net/Articles/1082270/)
                       22.04
                       linux-xilinx-zynqmp
                       2026-07-10
                       Ubuntu
                       USN-8518-1 (https://lwn.net/Articles/1082029/)
                       22.04 24.04 25.10 26.04
                       mailcap
                       2026-07-08
                       Ubuntu
                       USN-8536-1 (https://lwn.net/Articles/1083039/)
                       26.04
                       mariadb
                       2026-07-14
                       Ubuntu
                       USN-8533-1 (https://lwn.net/Articles/1082830/)
                       22.04 24.04 26.04
                       openssh
                       2026-07-13
                       Ubuntu
                       USN-8540-1 (https://lwn.net/Articles/1083040/)
                       22.04 24.04 26.04
                       openvpn
                       2026-07-14
                       Ubuntu
                       USN-8535-1 (https://lwn.net/Articles/1082831/)
                       22.04 24.04 26.04
                       pipewire
                       2026-07-13
                       Ubuntu
                       USN-8537-1 (https://lwn.net/Articles/1083041/)
                       22.04 24.04 26.04
                       python-httplib2
                       2026-07-14
                       Ubuntu
                       USN-8524-1 (https://lwn.net/Articles/1082271/)
                       16.04
                       python2.7, python3.5
                       2026-07-09
                       Ubuntu
                       USN-8541-1 (https://lwn.net/Articles/1083042/)
                       14.04 16.04 18.04 20.04 22.04 24.04 26.04
                       vim
                       2026-07-14
                       Ubuntu
                       USN-8543-1 (https://lwn.net/Articles/1083043/)
                       14.04 16.04 18.04 20.04 22.04 24.04 26.04
                       wget
                       2026-07-14
                       
전체 기사 (/Articles/1083045/) (댓글: 없음 (/Articles/1083045/#Comments))


## 주목할 만한 kernel patch


### Kernel 릴리스


           Linus Torvalds
           Linux 7.2-rc3 (/Articles/1082486/) 
           Jul 12
           
           
           Sebastian Andrzej Siewior
           v7.2-rc2-rt1 (/Articles/1082092/) 
           Jul 09
           
           
           Clark Williams
           6.6.144-rt76 (/Articles/1082871/) 
           Jul 14
           
           
           Joseph Salisbury
           5.15.211-rt97 (/Articles/1082278/) 
           Jul 09
           
           


### Architecture별


           Tian Zheng
           Support the FEAT_HDBSS introduced in Armv9.5 (/Articles/1082076/) 
           Jul 09

Vladimir Murzin
           arm64: 지원 추가 FEAT_NMI (/Articles/1082096/) 
           Jul 09
           
           
           Linu Cherian
           추가 BBML3 cpu feature (/Articles/1083052/) 
           Jul 15
           
           
           Bibo Mao
           LoongArch: KVM: Harden interrupt injection (/Articles/1082065/) 
           Jul 09
           
           
           Inochi Amaoto
           RISC-V: KVM: 추가 Svadu/Zicfiss/Zicfilp FWFT 지원 (/Articles/1082653/) 
           Jul 13
           
           
           Kuan-Wei Chiu
           riscv, bpf: 지원 추가 signed operations 및 32-bit atomics (/Articles/1082843/) 
           Jul 14
           
           
           Feng Jiang
           bpf, riscv: 추가 timed may_goto 지원 (/Articles/1082869/) 
           Jul 14
           
           
           Drew Fustini
           riscv: 추가 Ssqosid 및 initial CBQRI resctrl 지원 (/Articles/1083049/) 
           Jul 14
           
           
           Alexander Gordeev
           s390/mm: 일괄 처리 PTE updates in lazy MMU mode (/Articles/1082701/) 
           Jul 13
           
           
           Cong Wang
           um: 도입 pidfd_mmap()/pidfd_munmap() syscalls (/Articles/1082357/) 
           Jul 10
           
           
           Lin Wang
           x86/hygon: 추가 Family 0x18 DF node enumeration 및 SMN access (/Articles/1082063/) 
           Jul 09
           
           
           Fu Hao
           지원 추가 Hygon family 18h models 4h-8h (/Articles/1082296/) 
           Jul 10
           
           
           Sairaj Kodilkar
           지원 추가 AMD IOMMU GAPPI (/Articles/1082666/) 
           Jul 13
           
           


### 빌드 시스템


           James Clark
           tools/build: 허용 versioning of all LLVM tools (/Articles/1083063/) 
           Jul 15
           
           


### 코어 커널


           Tejun Heo
           sched_ext: Capability-based CPU delegation 용 sub-schedulers (/Articles/1082044/) 
           Jul 08
           
           
           Chuyi Zhou
           허용 preemption during IPI completion waiting to 개선 real-time performance (/Articles/1082082/) 
           Jul 09
           
           
           Marco Crivellari
           workqueue: 설정 alloc_workqueue() unbound by default (/Articles/1082075/) 
           Jul 09
           
           
           Pratyush Yadav
           kho: 설정 boot time huge page allocation work nicely 및 KHO (/Articles/1082279/) 
           Jul 09
           
           
           Jing Wu
           동적 Housekeeping Management (DHM) via CPUSets (/Articles/1082293/) 
           Jul 10
           
           
           Andrea Righi
           sched: 설정 proxy execution compatible 및 sched_ext (/Articles/1082301/) 
           Jul 10
           
           
           Shrikanth Hegde
           sched, steal_monitor: 도입 cpu_preferred_mask 및 steal-driven vCPU backoff (/Articles/1082289/) 
           Jul 10
           
           
           John Ogness
           도입 sync mode (/Articles/1082325/) 
           Jul 10
           
           
           Farid Zakaria
           binfmt_misc: bpf-backed binary type handlers (/Articles/1082458/) 
           Jul 11
           
           
           Pavel Begunkov
           zcrx RQ improvements 및 동적 memory provisioning (/Articles/1082467/) 
           Jul 11
           
           
           Pavel Begunkov
           최적화 zcrx refs cache bouncing (/Articles/1082468/) 
           Jul 11
           
           
           Pavel Begunkov
           io_uring: prototype 용 device memory tx (/Articles/1082469/) 
           Jul 11
           
           
           Thomas Gleixner
           entry: 재작업 syscall skip logic (/Articles/1082485/) 
           Jul 12
           
           
           Tejun Heo
           bpf: 설정 arena pointers first-class kfunc 및 struct_ops arguments (/Articles/1082654/) 
           Jul 12
           
           
           Leon Hwang
           bpf: 도입 global percpu data (/Articles/1082707/) 
           Jul 13
           
           
           Tvrtko Ursulin
           Realtime workqueues 및 panthor realtime submission (/Articles/1082700/) 
           Jul 13
           
           
           Ankur Arora
           barrier: 추가 smp_cond_load_{relaxed,acquire}_timeout() (/Articles/1082858/) 
           Jul 14
           
           
           Kumar Kartikeya Dwivedi
           재설계 Verification Errors (/Articles/1082876/) 
           Jul 13
           
           
           Masami Hiramatsu (Google)
           tracing: wprobe: x86: 추가 wprobe 용 watchpoint (/Articles/1083050/) 
           Jul 15
           
           
           Tejun Heo
           sched_ext: Sub-scheduler follow-ups (/Articles/1083048/) 
           Jul 14
           
           


### 개발 도구


           wen.yang@linux.dev
           rv/tlob: 추가 task latency over budget RV monitor (/Articles/1082035/) 
           Jul 08
           
           
           Abhishek Bapat
           alloc_tag: 도입 IOCTL-based filtering 용 MAP (/Articles/1082039/) 
           Jul 08
           
           
           Alexis Lothoré (eBPF Foundation)
           bpf: 지원 추가 KASAN checks in JITed programs (/Articles/1082071/) 
           Jul 09
           
           
           Josh Hilke
           vfio: selftests: 추가 driver 용 Intel Ethernet Gigabit Controller (IGB) (/Articles/1082048/) 
           Jul 08
           
           
           Kurt Kanzenbach
           RTC-Testbench v5.5 (/Articles/1082091/) 
           Jul 09
           
           
           Sasha Levin
           kallsyms: embed source file:line info in kernel stack traces (/Articles/1082126/) 
           Jul 09
           
           
           Jinchao Wang
           mm/kwatch: 동적 hardware watchpoints 용 hunting memory corruption (/Articles/1082907/) 
           Jul 15
           
           


### 디바이스 드라이버


           Grégoire Layet
           soc: aspeed: 추가 BMC 및 host driver 용 PCIe BMC device (/Articles/1082034/) 
           Jul 08
           
           
           Ivan Vecera
           dpll: zl3073x: 추가 PTP clock 지원 (/Articles/1082037/) 
           Jul 08
           
           
           Selvamani Rajagopal via B4 Relay
           지원 용 onsemi's S2500 10Base-T1S MAC-PHY (/Articles/1082038/) 
           Jul 08
           
           
           Imran Shaik
           clk: qcom: 추가 Audio Core clock controller 지원 on Qualcomm Shikra SoC (/Articles/1082040/) 
           Jul 08
           
           
           Birger Koblitz
           ax88179_178a: 지원 추가 AX88179A-based chips (/Articles/1082041/) 
           Jul 08
           
           
           Nicolin Chen
           iommufd: Iterate the cache invalidation array in the core (/Articles/1082042/) 
           Jul 08
           
           
           Armin Wolf
           platform/x86: lg-laptop: 개선 지원 용 modern devices (/Articles/1082043/) 
           Jul 08
           
           
           Bruce Robertson
           rust: power_supply class abstraction 및 SMB347 charger driver (/Articles/1082046/) 
           Jul 08
           
           
           Cristian Ciocaltea
           지원 10-bit YUV422 및 8/10-bit YUV420 color format on DW HDMI QP (/Articles/1082047/) 
           Jul 09
           
           
           Deborah Brouwer
           drm/tyr: firmware loading 및 MCU boot 지원 (/Articles/1082050/) 
           Jul 08
           
           
           Srirangan Madhavan
           PCI/CXL: 추가 CXL reset 지원 용 Type 2 devices (/Articles/1082052/) 
           Jul 09
           
           
           Alexey Klimov
           thermal: samsung: acpm-tmu: 추가 Exynos850 지원 (/Articles/1082053/) 
           Jul 09
           
           
           David Yang
           net: dsa: motorcomm: 추가 LED 지원 (/Articles/1082054/) 
           Jul 09
           
           
           Sriman Achanta
           HID: steelseries: split out Arctis driver 및 추가 Nova 5X/Nova 7 지원 (/Articles/1082055/) 
           Jul 08
           
           
           Inochi Amaoto
           riscv: spacemit: 추가 PCIe RC controller 지원 용 K3 (/Articles/1082056/) 
           Jul 09
           
           
           Crescent Hsieh
           serial: 8250: 추가 Moxa MUEx50 PCIe board 지원 (/Articles/1082058/) 
           Jul 09
           
           
           Changhuang Liang
           지원 추가 StarFive JHB100 SFC (/Articles/1082059/) 
           Jul 08
           
           
           Krishna Chaitanya Chundru
           PCI: qcom: 추가 link retention 지원 (/Articles/1082060/) 
           Jul 09
           
           
           Shubham Patil
           추가 AMD I3C master controller driver 및 bindings (/Articles/1082061/) 
           Jul 09
           
           
           Ramshouriesh R
           media: 추가 Himax HM1092 mono NIR sensor driver (/Articles/1082064/) 
           Jul 09
           
           
           Biju
           추가 RZ/G3L USB2.0 host 지원 (/Articles/1082066/) 
           Jul 09
           
           
           Lorenzo Pieralisi
           irqchip/ACPI: Arm GICv5 IWB ACPI IRQ probe deferral (/Articles/1082067/) 
           Jul 09
           
           
           AngeloGioacchino Del Regno
           pmdomains: 수정 및 지원 추가 HFRP 직접 (/Articles/1082068/) 
           Jul 09
           
           
           Janani Sunil
           iio: adc: 추가 AD7768/AD7768-4 ADC driver 지원 (/Articles/1082069/) 
           Jul 09
           
           
           George Moussalem via B4 Relay
           지원 추가 IPQ5018 Bluetooth (/Articles/1082070/) 
           Jul 09
           
           
           Chen-Yu Tsai
           arm64: mediatek: 추가 M.2 E-key slot on Chromebooks (/Articles/1082072/) 
           Jul 09
           
           
           javen
           r8169: 지원 추가 phylink (/Articles/1082073/) 
           Jul 09
           
           
           Roman Vivchar via B4 Relay
           AUXADC driver 용 the MediaTek mt6323 PMIC (/Articles/1082077/) 
           Jul 09
           
           
           AngeloGioacchino Del Regno
           drm: MediaTek DisplayPort cleanups 및 MT8196 eDP (/Articles/1082078/) 
           Jul 09
           
           
           Jack Wu via B4 Relay
           net: wwan: t9xx: 추가 MediaTek T9XX WWAN driver (/Articles/1082079/) 
           Jul 09
           
           
           joakim.zhang@cixtech.com
           추가 Cix Sky1 AUDSS clock 및 reset 지원 (/Articles/1082081/) 
           Jul 09
           
           
           Nikhil P. Rao
           pds_core: 추가 PLDM firmware update 및 host backed memory 지원 (/Articles/1082085/) 
           Jul 08
           
           
           Markus Stockhausen
           net: mdio: realtek-rtl9300: 추가 RTL83xx 지원 (/Articles/1082086/) 
           Jul 09
           
           
           Rafael J. Wysocki
           ACPI: processor: idle/intel_idle: 추가 ACPI _LPI 지원 to intel_idle (/Articles/1082090/) 
           Jul 09
           
           
           Melissa Wen
           drm/drm_colorop: 추가 post-blend colorop 지원 to AMD display driver (/Articles/1082095/) 
           Jul 08
           
           
           Marc-Olivier Champagne
           drm/panel: jd9365da: 지원 추가 DCLTek DT300250 (/Articles/1082045/) 
           Jul 08
           
           
           Dmitry Baryshkov
           media: iris: 추가 AR50LT core 지원 및 활성화 Agatti platform (/Articles/1082119/) 
           Jul 09
           
           
           Louis-Alexis Eyraud
           MT8189: 지원 추가 system 및 base clock controllers (/Articles/1082120/) 
           Jul 09
           
           
           Pengyu Luo
           drm/panel: 추가 Novatek NT36536 panel driver (/Articles/1082121/) 
           Jul 09
           
           
           Ben Levinsky
           remoteproc: 추가 AMD MicroBlaze/V BRAM-based remote processor driver (/Articles/1082124/) 
           Jul 09
           
           
           Zhi Wang
           gpu: nova-core: boot GSP 및 vGPU enabled (/Articles/1082125/) 
           Jul 09
           
           
           Prasad Kumpatla
           지원 추가 the Qualcomm WSA885X Stereo smart speaker amplifier (/Articles/1082280/) 
           Jul 09
           
           
           Kristian Mide
           Input: ilitek_ts: 추가 stylus 지원 용 0x0c reports (/Articles/1082281/) 
           Jul 09
           
           
           Biju
           추가 Renesas RZ/G3L SD/eMMC 지원 (/Articles/1082282/) 
           Jul 09
           
           
           Dmitry Baryshkov
           media: iris: 활성화 VP8, MPEG2 및 interlaced video 지원 (/Articles/1082283/) 
           Jul 09
           
           
           Jonas Jelonek
           net: pse-pd: 추가 Realtek PSE MCU 지원 (/Articles/1082284/) 
           Jul 09
           
           
           Saravanakrishnan Krishnamoorthy
           crypto: cmh - 추가 CRI CryptoManager Hub driver (/Articles/1082285/) 
           Jul 09
           
           
           Marcelo Schmitt
           iio: adc: 지원 추가 LTC2378 및 similar ADCs (/Articles/1082286/) 
           Jul 09
           
           
           Christian Marangi
           serial: 8250: 추가 AN7581 UART 지원 (/Articles/1082288/) 
           Jul 09
           
           
           Gianluca Boiano
           ASoC: codecs: 추가 Texas Instruments TAS2557 smart amplifier driver (/Articles/1082290/) 
           Jul 10
           
           
           Xianwei Zhao via B4 Relay
           추가 Amlogic general DMA (/Articles/1082294/) 
           Jul 10
           
           
           Sean Rhodes
           coreboot CFR firmware attributes (/Articles/1082295/) 
           Jul 10
           
           
           Mikko Perttunen
           Host1x memory context stealing (/Articles/1082297/) 
           Jul 10
           
           
           Koichiro Den
           dmaengine: dw-edma: 준비:  PCI EP DMA (part 1/3) (/Articles/1082298/) 
           Jul 10
           
           
           Koichiro Den
           PCI: endpoint: Expose endpoint DMA resources (part 2/3) (/Articles/1082299/) 
           Jul 10
           
           
           Koichiro Den
           PCI: endpoint: 추가 PCI DMA endpoint function (part 3/3) (/Articles/1082300/) 
           Jul 10
           
           
           Loic Poulain
           media: qcom: camss: CAMSS Offline Processing Engine 지원 (/Articles/1082303/) 
           Jul 10
           
           
           Christian Gmeiner
           drm/etnaviv: 추가 GPU reset counters 용 robustness (/Articles/1082305/) 
           Jul 10
           
           
           Oleksij Rempel
           mfd: 지원 추가 NXP MC33978/MC34978 MSDI (/Articles/1082306/) 
           Jul 10
           
           
           Rodrigo Alencar via B4 Relay
           새 기능:  the AD5686 IIO driver (/Articles/1082308/) 
           Jul 10
           
           
           Claudiu Beznea
           pinctrl: renesas: rzg2l: 지원 추가 RZ/G3S I3C (/Articles/1082309/) 
           Jul 10
           
           
           Michael Chan
           bnxt_en: 추가 kTLS TX offload 지원 (/Articles/1082318/) 
           Jul 09
           
           
           Andre Przywara
           arm_mpam: 추가 MPAM-Fb firmware 지원 (/Articles/1082324/) 
           Jul 10
           
           
           Nikolai Burov via B4 Relay
           pinctrl: mediatek: 추가 MT6858 지원 (/Articles/1082326/) 
           Jul 10
           
           
           Jerome Brunet
           regulator: 추가 X-Powers AXP318W PMIC 지원 (/Articles/1082350/) 
           Jul 10
           
           
           Kathiravan Thirumoorthy
           지원 추가 the QMP PCIe PHYs in Qualcomm IPQ9650 (/Articles/1082351/) 
           Jul 10
           
           
           Dave Marquardt via B4 Relay
           ibmvfc: 설정 ibmvfc 지원 FPIN messages (/Articles/1082354/) 
           Jul 10
           
           
           Tanmay Shah
           개선 RPMsg buffer management (/Articles/1082355/) 
           Jul 10
           
           
           David Matlack
           PCI: liveupdate: PCI core 지원 용 Live Update (/Articles/1082358/) 
           Jul 10
           
           
           Matthew Brost
           drm/ttm, drm/xe: Minimize dma-resv hold times 및 defragment sub-optimally backed BOs (/Articles/1082412/) 
           Jul 10
           
           
           David Lechner
           iio: adc: new ti-ads112c14 driver (/Articles/1082413/) 
           Jul 10
           
           
           Junhui Liu
           clk: sunxi-ng: 지원 추가 Allwinner A733 CCU 및 PRCM (/Articles/1082414/) 
           Jul 11
           
           
           Mohammad Rafi Shaik
           ASoC: qcom: qdsp6: 추가 MI2S clock control (/Articles/1082415/) 
           Jul 11
           
           
           Mohamed Khalfella
           TP8028 Rapid Path Failure Recovery (/Articles/1082457/) 
           Jul 11
           
           
           Prasad Kumpatla
           ASoC: qcom: 추가 AudioReach TDM backend 지원 (/Articles/1082460/) 
           Jul 12
           
           
           Ketil Johnsen
           drm/panthor: Protected mode 지원 용 Mali CSF GPUs (/Articles/1082461/) 
           Jul 12
           
           
           Gregory Price
           dax/kmem: atomic whole-device hotplug via sysfs (/Articles/1082462/) 
           Jul 12
           
           
           Tony Nguyen
           도입 iXD driver (/Articles/1082470/) 
           Jul 10
           
           
           Ping-Ke Shih
           wifi: rtw89: coex: 구현 coex 용 RTL8922D (/Articles/1082471/) 
           Jul 12
           
           
           Ping-Ke Shih
           wifi: rtw89: 추가 RF diagnosis 및 update random patches (/Articles/1082472/) 
           Jul 12
           
           
           Jakub Szczudlo
           iio: adc: 지원 추가 TI ADS1110 to  ti-ads1100 driver (/Articles/1082473/) 
           Jul 11
           
           
           Maíra Canal
           drm/vc4: 전환:  DRM GPU scheduler (/Articles/1082474/) 
           Jul 12
           
           
           Daniel Drake
           지원 추가 Broadcom BCM2712 IOMMU driver (Raspberry Pi 5) (/Articles/1082488/) 
           Jul 12
           
           
           Muralidhara M K
           platform/x86/amd/hsmp: Serialize the data plane against socket teardown (/Articles/1082656/) 
           Jul 13
           
           
           Ekansh Gupta
           misc: fastrpc: 추가 polling mode 지원 (/Articles/1082657/) 
           Jul 13
           
           
           Sean Rhodes
           firmware: 추가 coreboot CFR firmware attributes driver (/Articles/1082658/) 
           Jul 13
           
           
           Varadarajan Narayanan
           추가 new driver 용 WCSS secure PIL loading (/Articles/1082659/) 
           Jul 13
           
           
           Bastien Curutchet (Schneider Electric)
           net: dsa: microchip: 추가 PTP 지원 용 KSZ8463 (/Articles/1082660/) 
           Jul 13
           
           
           Ciprian Costea
           can: flexcan: 추가 NXP S32N79 SoC 지원 (/Articles/1082663/) 
           Jul 13
           
           
           AngeloGioacchino Del Regno
           drm/mediatek: 추가 DSC, WDMA, MT8189/96 DSI 지원 (/Articles/1082664/) 
           Jul 13
           
           
           Roman Vivchar via B4 Relay
           nvmem: 지원 추가 the MediaTek mt6323 PMIC (/Articles/1082665/) 
           Jul 13
           
           
           Bartosz Golaszewski
           software node: provide 지원 용 fw_devlink (/Articles/1082667/) 
           Jul 13
           
           
           Jahnavi MN via B4 Relay
           rust_binder : 구현 동적 debug logging mask (/Articles/1082668/) 
           Jul 13
           
           
           Bartosz Golaszewski
           crypto/dmaengine: qce: 도입 BAM locking 및 사용 DMA 용 register I/O (/Articles/1082669/) 
           Jul 13
           
           
           Claudiu Beznea
           i3c: renesas: Suspend to RAM 및 power loss 및 runtime PM (/Articles/1082670/) 
           Jul 13
           
           
           Bartosz Golaszewski
           net: stmmac: qcom-ethqos: 지원 추가 SCMI power domains (/Articles/1082671/) 
           Jul 13
           
           
           Baochen Qiang
           wifi: ath12k: 지원 firmware-allocated MLD peer ID (/Articles/1082673/) 
           Jul 13
           
           
           Chaitanya Kumar Borah
           drm/i915/color: 활성화 SDR plane color pipeline (/Articles/1082674/) 
           Jul 13
           
           
           han.junyang@zte.com.cn
           추가 ZTE DingHai Ethernet PF driver (/Articles/1082702/) 
           Jul 13
           
           
           Jens Emil Schulz Østergaard
           net: dsa: 추가 DSA 지원 용 the LAN9645x switch chip family (/Articles/1082703/) 
           Jul 13
           
           
           Taniya Das
           지원 추가 Video, Camera, Graphics clock controllers on Eliza (/Articles/1082704/) 
           Jul 13
           
           
           Frieder Schrempf
           지원 ELE API in i.MX OCOTP NVMEM driver (/Articles/1082705/) 
           Jul 13
           
           
           Heikki Krogerus
           drm/xe/i2c: alerts 및 controller enabling modifications (/Articles/1082708/) 
           Jul 13
           
           
           Yu-Chun Lin
           clk / reset: realtek: 추가 RTD1625 clock 및 reset 지원 (/Articles/1082709/) 
           Jul 13
           
           
           hang.suan.wang@altera.com
           추가 Altera SoCFPGA Crypto Service (FCS) driver (/Articles/1082840/) 
           Jul 13
           
           
           Prasad Kumpatla
           ASoC: qcom 및 pinctrl: 추가 LPASS LPR voting 및 Hawi LPASS LPI TLMM (/Articles/1082841/) 
           Jul 14
           
           
           Dmitry Torokhov
           MIPS: BCM47XX: 변환 buttons to software nodes (/Articles/1082842/) 
           Jul 13
           
           
           Daniel Golle
           net: dsa: mxl862xx: 지원 firmware update (/Articles/1082844/) 
           Jul 14
           
           
           Jia Wang via B4 Relay
           clk: ultrarisc: 추가 DP1000 clock 지원 (/Articles/1082845/) 
           Jul 14
           
           
           Ratheesh Kannoth
           전환 지원 (/Articles/1082848/) 
           Jul 14
           
           
           Jonathan Santos
           spi: 추가 multi-CS 및 per-transfer lane mask 지원 (/Articles/1082849/) 
           Jul 14
           
           
           Hal Feng
           추가 OpenCores PTC PWM 지원 (/Articles/1082850/) 
           Jul 14
           
           
           Vishnu Santhosh
           net: wwan: qcom_bam_dmux: Alloc RX buffers as a single coherent block (/Articles/1082852/) 
           Jul 14
           
           
           Esteban Urrutia via B4 Relay
           초기 PCIe0 및 QMP USB PHYs 지원 용 SM8475 (/Articles/1082855/) 
           Jul 14
           
           
           syyang@lontium.com
           추가 Lontium LT7911EXC eDP to MIPI DSI bridge (/Articles/1082856/) 
           Jul 14
           
           
           Uwe Kleine-König (The Capable Hub)
           gpio: Improvements around device-id arrays (/Articles/1082857/) 
           Jul 14
           
           
           Wadim Mueller
           counter: 추가 GPIO-based counter driver (/Articles/1082859/) 
           Jul 14
           
           
           Andy Chung via B4 Relay
           hwmon: 추가 Kandou KB9002 PCIe retimer driver (/Articles/1082860/) 
           Jul 14
           
           
           Lakshay Piplani
           지원 추가 NXP P3H2x4x I3C hub driver (/Articles/1082861/) 
           Jul 14
           
           
           Derek J. Clark
           추가 MSI Claw HID Configuration Driver (/Articles/1082863/) 
           Jul 14
           
           
           Rodrigo Alencar via B4 Relay
           AD9910 직접 Digital Synthesizer (/Articles/1082864/) 
           Jul 14
           
           
           Kyle 전환
           net: phy: 추가 driver 용 Motorcomm Quad 2.5GbE phy (/Articles/1082865/) 
           Jul 14
           
           
           AngeloGioacchino Del Regno
           drm/mediatek: The Huge Restructuring 및 MT8196 지원 (/Articles/1082866/) 
           Jul 14
           
           
           Zhanpeng Zhang
           riscv: iommu: 추가 QoS ID 지원 용 resctrl device assignment (/Articles/1082870/) 
           Jul 14
           
           
           Arthur Kiyanovski
           ptp: 추가 PHC timestamp quality attributes (/Articles/1082874/) 
           Jul 14
           
           
           Jacob Moroni
           RDMA/irdma: Adopt robust udata (/Articles/1082879/) 
           Jul 13
           
           
           Chris Morgan
           추가 Invensense ICM42607 (/Articles/1082880/) 
           Jul 13
           
           
           Leander Kieweg
           drm: 추가 DRM driver 용 GlandaGPU (VHDL soft-IP GPU) (/Articles/1082881/) 
           Jul 14
           
           
           Shyam Sundar S K
           platform/x86/amd/pmf: 추가 1AH_M80H 지원 및 accumulator based NPU metrics (/Articles/1082883/) 
           Jul 14
           
           
           Nilesh Javali
           scsi: qla2xxx: 추가 QLA29xx series adapter 지원 (/Articles/1082884/) 
           Jul 14
           
           
           Ramiro Oliveira
           지원 추가 Advantech EIO MFD series devices (/Articles/1082905/) 
           Jul 14
           
           
           Shivendra Pratap
           구현 PSCI reboot mode driver 용 PSCI resets (/Articles/1082906/) 
           Jul 14
           
           
           Yazen Ghannam
           PCIe Flit Logging Ext Capability 지원 (/Articles/1082908/) 
           Jul 14
           
           
           Deepa Guthyappa Madivalara
           구현 Region of Interest(ROI) 지원 (/Articles/1082920/) 
           Jul 14
           
           
           Simon Glass
           pinctrl: 지원 추가 the Rockchip RV1106 (/Articles/1082921/) 
           Jul 14
           
           
           Simon Glass
           지원 추가 the Rockchip RV1106 및 RV1103 (/Articles/1082922/) 
           Jul 14
           
           
           Jakub Szczudlo
           iio: adc: ti-ads1100: 지원 추가 TI ADS1110 to ti-ads1100 driver (/Articles/1082923/) 
           Jul 14
           
           
           Jorijn van der Graaf
           iio: magnetometer: 지원 추가 QST QMC6308 (/Articles/1082924/) 
           Jul 14
           
           
           Amit Sunil Dhamne via B4 Relay
           지원 추가 Battery Status AMS (/Articles/1082925/) 
           Jul 14
           
           
           Coia Prant
           net-next: 추가 basic 지원 용 RK3568 XPCS (/Articles/1082927/) 
           Jul 15
           
           
           Mohamed Ahmed
           drm/nouveau: GSP telemetry via RUSD, 및 fdinfo telemetry exposure (/Articles/1083046/) 
           Jul 15
           
           
           Douglas Anderson
           mailbox: 개선 the mbox core then 도입 the goog-mba driver (/Articles/1083047/) 
           Jul 14
           
           
           tze.yee.ng@altera.com
           hwmon: 추가 Altera SoC FPGA hardware monitoring 지원 (/Articles/1083053/) 
           Jul 14
           
           
           Stefan Popa
           iio: adc: 추가 MAX40080 current-sense amplifier driver (/Articles/1083054/) 
           Jul 15
           
           
           Esteban Urrutia via B4 Relay
           초기 QMP USB PHY 지원 용 SM8475 (/Articles/1083055/) 
           Jul 15
           
           
           Chris Lu
           Bluetooth: btmtk: 추가 MT7928 지원 (/Articles/1083059/) 
           Jul 15
           
           
           Janani Sunil
           iio: dac: 지원 추가 AD5529R DAC (/Articles/1083060/) 
           Jul 15
           
           
           Konrad Dybcio
           DWC3 link tunneling state reporting (/Articles/1083062/) 
           Jul 15
           
           
           Jose Ignacio Tornos Martinez
           ath11k/ath12k: 구현 TX flow control (/Articles/1083064/) 
           Jul 15
           
           
           luka.gejak@linux.dev
           wifi: rtw88: 추가 RTL8723B/RTL8723BS 지원 (/Articles/1083066/) 
           Jul 14
           
           
           Timur Kristóf
           drm/amdgpu: 지원 DRM format modifiers on GFX6-8 (v2) (/Articles/1083067/) 
           Jul 15
           
           
           Jason Gunthorpe
           Organize the SMMUv3 invalidation flow so iommupt can 사용 it (/Articles/1083068/) 
           Jul 14
           
           


### 디바이스 드라이버 인프라


           Maxime Ripard
           drm: 추가 DRM_MODE_ATOMIC_RESET flag (/Articles/1082036/) 
           Jul 08
           
           
           Samiullah Khawaja
           dma-mapping: 추가 preservation of 직접 allocations (/Articles/1082049/) 
           Jul 08
           
           
           Jiri Pirko
           RDMA: 설정 device names unique per net namespace (/Articles/1082083/) 
           Jul 09
           
           
           Thomas Zimmermann
           vga_switcheroo, drm: Push fbcon handling into DRM clients (/Articles/1082094/) 
           Jul 09
           
           
           Miquel Raynal (Schneider Electric)
           clk: 지원 추가 clock nexus (/Articles/1082352/) 
           Jul 10
           
           
           Christian König
           Refcounting dma_resv 및 using that 용 drm_exec 지원 in TTM (/Articles/1082353/) 
           Jul 10
           
           
           Markus Probst
           rust: 추가 basic serial device bus abstractions (/Articles/1082463/) 
           Jul 12
           
           
           Markus Probst via B4 Relay
           rust: leds: 추가 led classdev abstractions (/Articles/1082464/) 
           Jul 12
           
           
           Marcus Folkesson
           I2C Mux per channel bus speed (/Articles/1082662/) 
           Jul 13
           
           
           Markus Stockhausen
           i2c: i2c-gpio: 개선 driver 용 buses 및 shared SCL (/Articles/1082854/) 
           Jul 14
           
           
           Vipin Sharma
           vfio/pci: Base Live Update 지원 용 VFIO (/Articles/1082904/) 
           Jul 14
           
           


### 문서화


           Lincoln Wallace
           doc: LSM: update usage document 용 current LSM stacking (/Articles/1082847/) 
           Jul 13
           
           
           Weijie Yuan
           What's cooking in zh_CN (Jul 2026) (/Articles/1082873/) 
           Jul 14
           
           


### 파일시스템 및 블록 계층


           Yun Zhou
           ext4: deferred iput framework 용 EA inodes (/Articles/1082292/) 
           Jul 10
           
           
           Andrey Albershteyn
           fs-verity 지원 용 XFS 및 post EOF merkle tree (/Articles/1082314/) 
           Jul 10
           
           
           Hiroshi Nishida
           md/raid5: 감소 resync/recovery dispatch overhead (/Articles/1082310/) 
           Jul 10
           
           
           Hiroshi Nishida
           md/raid5: size stripe-cache 및 worker tuning from the hardware (/Articles/1082311/) 
           Jul 10
           
           
           Keith Busch
           직접-io file extended attributes (/Articles/1082417/) 
           Jul 10
           
           
           Jori Koolstra
           vfs: 추가 O_CREAT|O_DIRECTORY to open*(2) (/Articles/1082465/) 
           Jul 12
           
           
           Jeremy Bingham
           minix: 변환 to iomap 및 추가 직접 I/O (/Articles/1082456/) 
           Jul 11
           
           
           Eric Biggers
           fscrypt: 표준화:  blk-crypto (/Articles/1082672/) 
           Jul 12
           
           
           wang zhaolong
           ksmbd: 사용 splice 용 SMB2 READ responses (/Articles/1082661/) 
           Jul 13
           
           
           Artem Blagodarenko
           Data in direntry (dirdata) feature (/Articles/1082872/) 
           Jul 14
           
           
           Xiubo Li via B4 Relay
           ceph: 감소 mdsc->mutex contention in the cephfs kclient (/Articles/1083051/) 
           Jul 15
           
           
           Ze Tan
           smb: 지원 security 및 trusted xattrs over EAs (/Articles/1083056/) 
           Jul 15
           
           
           Miklos Szeredi
           fs: 허용 opening overlayfs/erofs layers through O_ALT (/Articles/1083065/) 
           Jul 15
           
           


### 메모리 관리


           Anshuman Khandual
           mm: 표준화 printing 용 pgtable entries (/Articles/1082057/) 
           Jul 09
           
           
           Wen Jiang
           mm/vmalloc: Speed up ioremap, vmalloc 및 vmap 및 contiguous memory (/Articles/1082062/) 
           Jul 09
           
           
           Li Zhe
           mm: 최적화 zone-device memmap initialization (/Articles/1082080/) 
           Jul 09
           
           
           Stanislav Kinsburskii
           mm/hmm: 추가 mmap lock-drop 지원 용 userfaultfd-backed mappings (/Articles/1082093/) 
           Jul 07
           
           
           SJ Park
           mm/damon: 도입 data attributes only monitoring (/Articles/1082122/) 
           Jul 09
           
           
           Xueyuan Chen
           mm: 방지 large folio splits when swap is unavailable (/Articles/1082123/) 
           Jul 09
           
           
           Matthew Wilcox (Oracle)
           사용 generic_file_read_iter() in hugetlbfs (/Articles/1082312/) 
           Jul 09
           
           
           Christoph Hellwig
           개선된 block swap batching 및 a different take on swap_ops v4 (/Articles/1082313/) 
           Jul 10
           
           
           Lorenzo Stoakes
           mm: 설정 VMA page offset handling more consistent (/Articles/1082356/) 
           Jul 10
           
           
           Lorenzo Stoakes
           mm: 변환 more vm_flags_t users to vma_flags_t (/Articles/1082416/) 
           Jul 11
           
           
           Shivank Garg
           mm: 일괄 처리 rmap walks during large folio migration (/Articles/1082459/) 
           Jul 12
           
           
           Youngjun Park
           mm/swap, memcg: 도입 swap tiers 용 cgroup based swap control (/Articles/1082655/) 
           Jul 13
           
           
           Usama Arif
           mm: PMD-level swap entries 용 anonymous THPs (/Articles/1082698/) 
           Jul 13
           
           
           Usama Arif
           mm/vmscan: 감소 lru_lock contention via vmstat-derived scan-balance cost (/Articles/1082711/) 
           Jul 13
           
           
           Yeoreum Yun
           mm: 최적화 unnecessary loads due to ptep_get() 및 friends out (/Articles/1082699/) 
           Jul 13
           
           
           Kairui Song via B4 Relay
           mm/swap: 도입 priority queue to remove global cluster cache 및 plist (/Articles/1082839/) 
           Jul 14
           
           
           Zicheng Wang
           mm/mglru: proactive aging via memory.aging (/Articles/1082867/) 
           Jul 14
           
           
           Kevin Brodsky
           단순화 special kernel page table handling (/Articles/1082887/) 
           Jul 14
           
           
           Vlastimil Babka (SUSE)
           mm/slab, alloc_tag: 감소 obj_ext memory waste (/Articles/1083058/) 
           Jul 15
           
           


### 네트워킹


           Lorenzo Bianconi
           추가 IPv4 over IPv6 및 SIT flowtable SW acceleration (/Articles/1082087/) 
           Jul 09
           
           
           Priyansha Tiwari
           wifi: nl80211: 도입 PROBE_PEER 용 AP 및 STA (/Articles/1082088/) 
           Jul 09
           
           
           Vladimir Vdovin
           기능 추가:  load HW RX checksum in eBPF programs (/Articles/1082084/) 
           Jul 08
           
           
           Mahe Tardy
           bpf: 추가 icmp_send kfunc (/Articles/1082315/) 
           Jul 09
           
           
           Rishikesh Jethwani
           tls: 추가 TLS 1.3 hardware offload 지원 (/Articles/1082317/) 
           Jul 09
           
           
           Alice Mikityanska
           BIG TCP 용 UDP tunnels (/Articles/1082319/) 
           Jul 10
           
           
           Yuya Kusakabe
           seg6: 지원 추가 the SRv6 End.MAP behavior (/Articles/1082304/) 
           Jul 10
           
           
           Pablo Neira Ayuso
           initial flowtable bridge 지원 (/Articles/1082320/) 
           Jul 10
           
           
           Jori Koolstra
           net: af_unix: useful handling of LSM denials on SCM_RIGHTS (/Articles/1082466/) 
           Jul 12
           
           
           Avinash Duduskar
           bpf: bidirectional VLAN 지원 용 bpf_fib_lookup() (/Articles/1082710/) 
           Jul 13
           
           
           Jeremy Kerr
           net: mctp: usb: 지원 추가 MCTP-over-USB v1.1 (/Articles/1082877/) 
           Jul 13
           
           
           Srikar Dronamraju
           net: 사용 synchronous wakeups selectively (/Articles/1082846/) 
           Jul 14
           
           
           David 'equinox' Lamparter
           RFC 6724 rule 5.5 지원 (/Articles/1082875/) 
           Jul 14
           
           
           Florian Westphal
           netfilter: ipset: 변환 to rhashtable (/Articles/1082878/) 
           Jul 14
           
           
           Jakub Sitnicki
           skb extension 용 BPF metadata (/Articles/1082926/) 
           Jul 14
           
           


### 보안 관련


           Renzo Davoli
           PTRACE_SET_SYSCALL_INFO: 지원 추가 seccomp syscall skipping (/Articles/1082074/) 
           Jul 09
           
           
           Justin Suess
           구현 LANDLOCK_RESTRICT_SELF_NNP_ON_EXEC (/Articles/1082089/) 
           Jul 08
           
           
           Pawan Gupta
           cBPF JIT spray hardening (/Articles/1082316/) 
           Jul 09
           
           
           Sean Rhodes
           PM: hibernate: encrypted snapshots under lockdown (/Articles/1082706/) 
           Jul 13
           
           


### 가상화 및 컨테이너


           Mark Brown
           KVM: arm64: 구현 지원 용 SME (/Articles/1082051/) 
           Jul 09
           
           
           Akihiko Odaki
           KVM: arm64: PMU: 사용 multiple host PMUs (/Articles/1082307/) 
           Jul 10
           
           
           Sean Christopherson
           KVM: SEV: 수정 RMP #PF due to freeing in-사용 VMSA (/Articles/1082287/) 
           Jul 09
           
           
           Fuad Tabba
           KVM: arm64: pKVM vCPU state management at EL2 (series A) (/Articles/1082862/) 
           Jul 14
           
           
           Wei-Lin Chang
           KVM: arm64: nv: 구현 nested stage-2 reverse map (/Articles/1082868/) 
           Jul 14
           
           
           Marc Zyngier
           KVM: arm64: 지원 추가 FEAT_NV2p1 및 FEAT_NV3 (/Articles/1082882/) 
           Jul 14
           
           
           Tina Zhang
           KVM: nSVM: 활성화 DecodeAssists 용 nested guests (/Articles/1082851/) 
           Jul 14
           
           
           Mostafa Saleh
           KVM: arm64: SMMUv3 driver 용 pKVM (trap 및 emulate) (/Articles/1083061/) 
           Jul 15
           
           
           Fuad Tabba
           KVM: arm64: pKVM vCPU state management at EL2 (/Articles/1083057/) 
           Jul 15
           
           


### 기타


           Jiebin Sun
           perf c2c: 추가 a function view (/Articles/1082302/) 
           Jul 10
           
           
           Thomas Falcon
           perf: 지원 추가 memory region/range reporting (/Articles/1082291/) 
           Jul 09
           
           
           John Kacur
           tuna: 추가 comprehensive cgroup v2 cpuset 지원 (/Articles/1082321/) 
           Jul 10
           
           



Page editor: Joe Brockmeier\n

---

## 번역자 기술 각주

[^scraper-proxy]: Residential proxy는 일반 가정/모바일 ISP 주소를 프록시 출구로 쓰는 방식입니다. 서버 입장에서는 데이터센터 IP 차단보다 탐지가 어렵고, rate limit 정책이 정상 사용자까지 건드릴 위험이 커집니다.
[^open-web]: 공개 웹의 운영 비용은 crawler가 지불하지 않는 대역폭·CPU·캐시 비용으로 전가됩니다. 기술적 차단만으로 해결하기 어려워 robots 정책, 계약, 법적 책임, 검색/AI 업체의 투명성이 함께 필요합니다.
[^mpsc]: MPSC(multi-producer, single-consumer) queue는 여러 생산자가 동시에 enqueue하고 하나의 소비자가 dequeue하는 구조입니다. lockless 설계는 spinlock contention을 줄이지만 memory ordering과 ABA류 경쟁 조건을 신중히 다뤄야 합니다.
[^io-uring]: io_uring은 Linux의 고성능 asynchronous I/O 인터페이스입니다. submit/completion queue를 공유 메모리로 사용해 system call 왕복을 줄이지만, hot path lock은 다중 thread 부하에서 병목이 될 수 있습니다.
[^xfstests]: xfstests 같은 filesystem regression suite는 안정성을 높이지만, stable kernel patch마다 완벽한 테스트를 요구하면 backport 속도와 현실성이 떨어질 수 있습니다. 그래서 reproducer, risk class, maintainer judgment가 중요합니다.
[^bpf-mitigation]: BPF는 verifier를 통과한 프로그램을 kernel 안에서 실행하는 기술입니다. exploit 차단에 쓰면 긴급 완화가 빠르지만, verifier 한계·성능 overhead·false positive가 실서비스 위험 요소가 됩니다.
[^bpf-net]: BPF에서 직접 packet을 만들 수 있으면 tracing/monitoring을 넘어 active networking control에 가까워집니다. 권한 모델과 helper API 범위를 좁게 유지해야 privilege escalation이나 예기치 않은 traffic injection을 막을 수 있습니다.
[^terminal-gpu]: GPU terminal은 대량 text rendering, scrollback, ligature/graphics 처리에서 장점이 있습니다. 다만 terminal protocol 확장은 원격 host, multiplexer, editor 간 호환성 문제가 함께 따라옵니다.
[^qbe]: QBE는 작은 intermediate representation과 backend를 지향하는 compiler infrastructure입니다. LLVM보다 기능은 적지만 이해·빌드·이식 비용이 낮아 작은 언어 구현체에 매력적입니다.
