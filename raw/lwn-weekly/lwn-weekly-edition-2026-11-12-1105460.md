# LWN.net Weekly Edition — 2026년 11월 12일 한국어 기술 번역·해설

- 원문 URL: https://lwn.net/Articles/1105460/bigpage
- Edition: LWN.net Weekly Edition for November 12, 2026 (article_id: 1105460)
- 선택 기준: 이번 실행에 주입된 후보 JSON에서 2026년 11월 19일호(1107147)를 최신 유료 추정호로 제외하고, 바로 이전 2026년 11월 12일호를 선택했습니다. 실행일 기준 최신호를 다시 정의하지 않고 입력 후보를 사용했습니다.
- 공개 접근: 로그인 없이 공개 bigpage 및 각 특집 원문을 확인했습니다. 유료·로그인 콘텐츠는 우회하지 않았습니다.
- 생성시각: 2026-11-27T09:49:15+09:00
- 번역 방식: Codex CLI 실행 파일이 없어, 공개 원문을 추출한 뒤 기사별 병렬 번역 및 독립 검증을 수행했습니다.
- 저작권 및 범위: 특집 5편은 각 원문에서 CC BY-SA 4.0 재배포 허용을 확인하고 전문 번역했습니다. 저작권자 Eklektix, Inc.와 각 저자를 표시하며 번역·편집·각주 해설을 추가했습니다. 해당 번역과 해설은 동일한 CC BY-SA 4.0을 따릅니다(https://creativecommons.org/licenses/by-sa/4.0/). 별도 라이선스가 확인되지 않은 단신과 인용은 전문 번역 대신 독립적으로 서술한 요약으로 제공합니다. 보안 공지·행사·패치 목록은 사실 메타데이터를 보존합니다. 독자 댓글은 포함하지 않습니다.

## 전체 요약

- DisplayLink 드라이버 개발 중단 사례는 코드 저작권과 별개인 특허·상호운용성 문제를 다룹니다.
- Git 커뮤니티는 LLM 기여 정책에 합의하기 위한 의사결정 절차 자체를 논의합니다.
- lockdown 환경에서의 hibernation, user namespace의 file capability 경계, glibc dynamic linker hardening이 보안 특집의 중심입니다.
- 단신, 뉴스레터, 발표 모집과 행사 일정, 보안 업데이트, 커널 패치를 함께 수록합니다.
- 모든 내용은 해당 호가 다루는 시점의 기록입니다. 미병합 패치·제안·당시 릴리스 정보를 현재 확정 상태로 해석하지 않아야 합니다.

## Synaptics의 특허 침해 주장에 중단된 DisplayLink 드라이버 개발

원제: Synaptics patent claims stop work on DisplayLink drivers  
원문: https://lwn.net/Articles/1102549/  
저자: **Joe Brockmeier**, LWN.net  
발행일: 2026년 11월 10일  
저작자 표시 및 라이선스: 원문 © Joe Brockmeier / LWN.net. 제공된 원문의 라이선스 표기는 **CC BY-SA 4.0**입니다. 이 문서는 원문 전체의 한국어 번역이며, 요약과 번역자 해설 각주를 추가했습니다. 원문 저작자 표시를 유지하며 번역본에도 같은 라이선스를 적용합니다.

### 요약

- Mike Lothian은 Linux에서 불안정하게 작동하는 DisplayLink 도킹 스테이션을 개선하려고 LLM의 도움으로 Rust 기반 Vino 드라이버를 개발했습니다.
- 기술 지원을 요청하자 Synaptics는 도움 대신 특허 침해를 주장하며 개발 중단, 공개 자료 철회, 서면 확인 등을 요구했습니다.
- Lothian은 세 세대의 DL3 도크를 제조사 소프트웨어 없이 제어하는 단계에 도달했지만, Synaptics는 영국 특허 두 건의 청구항 대응표를 제시하며 금전 청구를 예고했습니다.
- Synaptics와 Lothian 모두 OIN에 참여하고 있었지만, OIN은 해당 코덱이 Linux System Definition의 보호 범위에 들지 않는다고 판단했습니다.
- Lothian은 소송 방어 비용을 감당할 수 없어 저장소를 내렸고 Vino의 커널 제출도 중단했습니다. 이 사례는 소프트웨어 특허가 여전히 자유 소프트웨어 개발을 가로막는다는 점을 보여 줍니다.

---

Mike Lothian은 [DisplayLink](https://en.wikipedia.org/wiki/DisplayLink) 칩셋을 사용하는 도킹 스테이션(이하 도크)을 갖고 있습니다. 적어도 그가 보기에는 Linux에서의 성능이 기대에 미치지 못했습니다. 그는 LLM의 도움으로 Linux 드라이버를 개선해 보기로 했지만, 해결할 수 없는 문제 하나에 부딪혔습니다. 그래서 Synaptics 개발자들이 도와주기를 바라며 도움을 요청했습니다. (DisplayLink는 2022년에 [Synaptics에 인수되었습니다](https://www.synaptics.com/company/news/displaylink).) 그러나 드라이버 개선을 돕기는커녕 Synaptics 법무팀은 특허 침해 주장, DisplayLink 기술의 무단 구현을 중단하라는 [요구](https://lists.freedesktop.org/archives/dri-devel/attachments/20261006/d690bb16/attachment-0001.pdf), 그리고 거액의 법적 제재를 받을 수 있다는 위협으로 응답했습니다. 당분간 이 회사의 도크를 사용하는 Linux 사용자들은 다른 플랫폼과 동등한 기능을 누리지 못하는 상황을 계속 감수해야 할 것으로 보입니다.

### Synaptics와 DisplayLink

그가 지원하려던 도크는 USB 3로 시스템에 연결하는 Dell 장치로, 여러 모니터와 다른 장치를 컴퓨터에 연결할 수 있게 해 줍니다. Synaptics는 Ubuntu용 APT 저장소를 통해 이 장치들을 위한 [Linux용 DisplayLink Manager(DLM) 소프트웨어](https://www.synaptics.com/products/displaylink-graphics/downloads/ubuntu)를 제공합니다.

이 회사는 DLM 소프트웨어를 바이너리 형태로만, 그것도 x86 기반 플랫폼용으로만 제공합니다. 이 소프트웨어는 독점 소프트웨어이지만, 회사는 DLM에 포함되는 오픈 소스 외부 트리 커널 모듈인 [Extensible Virtual Display Interface](https://github.com/DisplayLink/evdi#readme)(EVDI) 프로젝트를 유지 관리하고 있습니다.[^f1102549-1] 이 프로젝트는 [Linux DRM](https://docs.kernel.org/gpu/introduction.html)과 호환되는 드라이버를 제공하여, 사용자가 [xrandr](https://linux.die.net/man/1/xrandr)나 GNOME 및 KDE Plasma의 유틸리티처럼 디스플레이 설정에 쓰이는 표준 도구로 도크에 연결된 디스플레이를 관리할 수 있게 합니다.[^f1102549-2]

회사가 DLM 소스 코드를 공개하지 않은 이유는 [짧은 설명 글](https://support.displaylink.com/knowledgebase/articles/1104056-why-has-displaylink-not-released-source-code-for-t)에 나와 있습니다. 이 소프트웨어는 DL3라는 독점 그래픽 기술을 사용하여 통신 채널(이 경우 USB 3)을 통해 전송되는 여러 채널(예를 들어 USB, DisplayLink 영상, 오디오)의 압축 스트림을 만들고, 사용자 장치로 출력할 때 이를 다시 디코딩합니다.

안타깝게도 제조사가 제공하는 소프트웨어는 Lothian에게 제대로 작동하지 않았습니다. 저는 이 기사를 쓰면서 Signal로 그와 통화하고 메시지를 주고받았습니다. 그는 Linux에서 드라이버가 계속 충돌했기 때문에, 자신이 구독하는 Claude를 사용해 새 드라이버와 지원 소프트웨어를 개발해 보기로 했다고 말했습니다.

### Vino

그는 6월 17일 커널의 dri-devel 메일링 리스트에 Rust 기반 DRM/KMS 드라이버인 Vino의 [첫 번째 패치 시리즈](https://lwn.net/ml/all/20260617151249.2937-1-mike%40fireburn.co.uk/)를 RFC로 게시했습니다.[^f1102549-3] Lothian은 아직 미완성 상태라고 밝히면서, 도크의 제어 평면과 통신하려다 맞닥뜨린 장애물을 해결하는 데 도움을 요청했습니다. “DisplayLink DL3의 제어 평면 통신 개시 절차를 알고 계시거나, 채널별 차이 비교로는 드러나지 않는 버스 전체의 타이밍·순서 특성을 분리해 확인할 아이디어가 있다면, 도움을 주시면 정말 감사하겠습니다.”[^f1102549-4] 몇몇 개발자에게 피드백을 받았고, 그중에는 Rust [KMS 바인딩](https://lwn.net/Articles/997850/#kms)을 사용하도록 드라이버를 재작업하라는 Danilo Krummrich의 [안내](https://lwn.net/ml/all/DJBG3H7N9GS9.7AMMRJIHGHRN@kernel.org/)도 있었습니다. 하지만 그가 해결하려던 문제에 직접적인 조언은 없었습니다.

Lothian은 같은 6월 17일 EVDI의 GitHub 저장소에도 [이슈](https://github.com/DisplayLink/evdi/issues/577)를 등록했습니다. 이 이슈에는 그때까지 진행한 작업, DL3 프로토콜을 리버스 엔지니어링하기 위해 취한 접근법, Vino 코드가 담긴 자신의 GitHub 저장소 링크가 들어 있었고, 몇 가지 사안에 대한 설명도 요청했습니다. 이슈에는 답변이 달리지 않았습니다.

그는 Synaptics의 Łukasz Spintzyk에게 이메일로 직접 연락하기도 했습니다. 7월 5일부터 10월 7일까지 회사와 주고받은 서신은 [Lothian이 모은 이 PDF](https://lwn.net/images/pdf/synaptics-correspondence-jul-oct-2026.pdf)에서 볼 수 있습니다. 그는 EVDI에서 몇 가지 버그를 발견해 [pull request](https://github.com/DisplayLink/evdi/pull/581)를 열었다고 알렸습니다(이 요청은 몇 달 동안 검토되지 않았습니다). 또한 Vino에서 막힌 부분에 대한 도움을 요청했습니다. 7월 20일 그가 받은 답장은 Spintzyk가 아니라 Synaptics의 Michal Lukaszek가 보낸 것이었습니다.

> 제가 연락드리는 이유는 DisplayLink가 개방형 표준이 아니기 때문입니다. DisplayLink 장치가 사용하는 프로토콜, 코덱 및 기타 기술은 Synaptics의 독점 기술이며, 영국을 포함한 여러 관할권에서 상당한 규모의 특허 포트폴리오로 보호받고 있습니다.
>
> 공개하신 내용을 보면 VINO 프로젝트는 상호운용성 작업을 넘어, 당사의 특허가 적용된다고 판단하는 기술을 구현하는 방향으로 나아가는 것으로 보입니다. 많은 개발자가 저작권으로 보호되는 소스 코드를 사용하지 않는 데 주의를 기울이는 것은 이해할 만하지만, 특허법은 다릅니다. 독립적으로 작성하거나 클린룸 방식으로 구현했더라도, 특허받은 발명을 구현한다면 반드시 특허 침해를 피할 수 있는 것은 아닙니다.

Lukaszek는 Lothian이 “DisplayLink를 둘러싼 지식재산권 상황”을 모르고 있었을 가능성이 충분히 있다며, “나중에 상황이 더 공식적인 절차로 이어지기” 전에 지금 알려 주고 싶었다고 말했습니다. Lothian은 스코틀랜드에 살고 있고 “.co.uk” 이메일 주소를 사용합니다. 이메일에서 영국을 언급한 것은 그 때문입니다.

### 중단 요구

8월 17일 Synaptics의 지식재산권 담당 법무 부책임자인 Andrew Bateman은 [중단 요구 통지서](https://lwn.net/images/pdf/Cease_and_Desist_Notice_Mike_Lothian_08-17-2026.pdf)를 보냈습니다. 서한은 Lothian이 Lukaszek의 연락에 “실질적으로 응답”하지 않았고 “공개적인 발언과 추가 개발 활동”을 계속했다고 주장했습니다. 부록에는 “DisplayLink의 아키텍처와 작동 방식의 근본적인 측면을 포괄하는” 특허 125건의 목록이 있었지만, 그의 작업이 어느 특허를 침해할 수 있는지는 명시하지 않았습니다.

Synaptics는 즉각 이행하라고 요구하는 여덟 가지 사항을 나열했습니다. 여기에는 “Synaptics의 특허를 하나라도 침해하는 모든 소프트웨어나 기타 구현”의 개발을 중단할 것, “Linux 커널 메인테이너, 메일링 리스트, 코드 호스팅 플랫폼, 패키지 메인테이너, 배포판 또는 그 밖의 모든 개인이나 조직에 제출한” 자료를 철회할 것, “관련 자료가 공개, 제출, 저장 또는 배포된” 모든 위치를 서면으로 밝힐 것 등이 포함되었습니다. 또한 8월 28일까지 요구 사항을 이행했음을 확인하는 서명된 확인서를 Synaptics에 제출하라고 요구했습니다.

하지만 Lothian은 8월 26일 DisplayLink 도크를 위한 자신의 [Vino 작업 세 번째 버전](https://lwn.net/ml/all/20260826163913.7052-1-mike@fireburn.co.uk/)을 dri-devel 리스트에 게시했습니다. 그는 앞선 두 버전은 “화면을 한 번도 켜지 못했지만”, 새 작업은 제조사 소프트웨어 없이 세 세대의 DL3 도크를 제어할 수 있다고 말했습니다. 리스트에 게시된 패치 세트에 실질적인 검토 의견은 없었지만, Sashiko의 자동 검토는 일부 있었습니다.

8월 27일 Lothian은 Bateman에게 답장하며, Synaptics가 침해되고 있다고 판단한 특허에 대해 더 자세히 설명해 달라고 요청했습니다. “관련 청구항을 관련 코드에 대응시킨 청구항 대응표가 있다면, 우려하시는 내용을 이해하고 적절히 대응하기가 훨씬 쉬울 것입니다.”[^f1102549-5]

그는 자신의 작업을 특허 침해로 취급하는 Synaptics의 입장이 혼란스럽다고도 했습니다. Synaptics는 [Open Invention Network](https://openinventionnetwork.com/)(OIN)의 회원입니다. OIN은 오픈 소스 개발자와 공급업체가 값비싼 특허 소송의 위협에 대처하도록 돕기 위해 [설립되었습니다](https://lwn.net/Articles/163038/). 이 단체는 개인, 오픈 소스 프로젝트, 대형 공급업체 모두에게 특허 보호를 제공하는 대규모 교차 라이선스 포트폴리오를 보유하고 있습니다. Lothian은 자신도 이제 OIN 라이선스 참여자이며, OIN이 “Linux와 오픈 소스 소프트웨어를 둘러싼 바로 이런 종류의 특허 문제를 줄여 주는” 곳이라고 생각했다고 말했습니다.

그는 Bateman에게 Synaptics의 주장이 “우리 각자가 OIN에 대해 진 약속과 어떤 관계가 있는지” 설명해 달라고 요청했고, Synaptics와 건설적으로 문제를 해결하고 싶다는 뜻을 밝혔습니다. “Synaptics와 개인 오픈 소스 개발자 사이의 공개적인 분쟁은 우리 어느 쪽에도 별 도움이 되지 않을 것 같습니다. 특히 Linux와 오픈 소스 커뮤니티 안에서는 더욱 그렇습니다.”

Lothian은 Synaptics가 어느 특허 청구항의 침해를 주장하는지 이해하지 못한 상태에서는 회사가 요구한 “서명된 확약서를 합리적으로 제출할 수” 없다고 생각했습니다. 그는 8월 28일로 정해진 기한을 연장해 달라고 요청했습니다. Bateman에게서 답이 없자 Lothian은 9월 18일 후속 이메일을 보냈습니다. 그는 지난 이메일에 대한 수신 확인조차 없어 걱정된다며, 작업을 계속해도 괜찮다고 생각해도 되는지 물었습니다. 그는 Vino 드라이버를 직접 꽤 오랫동안 사용하고 있었고, 작업에 특허 위협이 드리워지지 않은 상태에서 업스트림에 반영하고 싶어 했습니다.[^f1102549-6]

Bateman은 다음 날 답장하여, 그가 걱정해야 할 상황이라고 말했습니다.

> 앞서 요청하신 대로, 당사는 귀하의 Vino 드라이버를 당사 DisplayLink 특허의 특정 청구항에 대응시키면서 귀하가 계속하고 있는 특허 침해를 문서화해 왔습니다. 이 청구항 대응 문서를 앞으로 2주 안에 제공하겠습니다. 또한 귀하의 침해 행위를 문서화하는 데 필요한 비용과 노력을 회수하기 위해 상당한 금액의 금전적 보상을 요구하는 서신도 보낼 것입니다. 저는 앞서 귀하에게 침해를 중단할 기회를 드렸지만, 귀하는 반발하며 제 경고를 따르지 않기로 했습니다. 따라서 이제 당사는 적절하다고 판단하는 방식으로 대응 수위를 높이고 있습니다.

서한은 이어 Lothian이 “당사가 독점 기술을 구현하는 방식을 경쟁사와 다른 제삼자에게 알려 줌으로써, 경쟁이 치열한 이 시장에서 DisplayLink의 경쟁 우위를 혼자서 완전히 무너뜨리게 될 것”이라고 주장했습니다. Bateman은 DisplayLink는 OIN 회원이 아니며, 그 어떤 기술도 OIN이나 다른 조직을 통해 라이선스받을 수 없다고 말했습니다.

Bateman은 10월 5일 자 [후속 서한](https://lwn.net/images/pdf/Cease_and_Desist_Notice_Mike_Lothian_10-05-2026.pdf)을 보냈습니다. 여기에는 영국 특허 [GB2484736B](https://lwn.net/images/pdf/GB2484736.pdf)(“영상 생성”)와 [GB2485613B](https://lwn.net/images/pdf/GB2485613.pdf)(“디스플레이 제어 장치”)에 관한 청구항 대응표 두 개가 포함되어 있었습니다. 두 특허 모두 2010년에 출원되어 2012년에 공개되었습니다. 그는 앞선 서한에서 Synaptics가 제시한 요구를 되풀이하고, 기한이 이제 10월 11일이라고 밝혔습니다. 이를 따르지 않으면 회사는 “첨부된 귀하의 침해 행위 문서를 작성하는 데 필요한 비용과 노력을 회수하기 위해 귀하에게 미화 25,000달러의 금전적 보상”을 청구할 것이라고 했습니다. 이 금액은 회사의 요구를 이행할 때까지 매주 25,000달러씩 늘어나게 되어 있었습니다.

Lothian은 다음 날 이메일로 답장하여, 자신이 휴가 중이며 10월 13일이 되어야 집으로 돌아간다고 알렸습니다. 그는 집에 돌아가 청구항 대응표를 “가급적이면 그것을 읽는 데 도움을 줄 자격을 갖춘 사람과 함께” 검토할 수 있도록 기한을 연장해 달라고 요청했습니다. Bateman은 Synaptics가 10월 18일까지 기한을 연장하는 데 동의하지만, 그 이상의 연장은 허용하지 않겠다고 [답했습니다](https://lwn.net/ml/all/MW4PR03MB6540F02E3810CC632C82302598952%40MW4PR03MB6540.namprd03.prod.outlook.com/). 그는 “DisplayLink는 OIN 회원이 아니”며, 그 어떤 기술도 OIN을 통해 라이선스받을 수 없다는 점을 재차 강조했습니다.

### OIN이 구원해 줄 수 있을까?

Synaptics는 OIN 회원이 *맞으며*, [커뮤니티 명부](https://openinventionnetwork.com/community-directory-alphabetical/)에도 올라 있습니다. Lothian은 OIN에 가입한 데 더해, 도움을 얻기 위해 이 단체에 연락했고 일부 직원과 계속 소통해 왔습니다. OIN은 사안을 조사하여 그가 OIN 회원으로서 어떤 보호를 받을 수 있는지 확인하겠다고 했습니다. 이 과정은 Lothian이 바랐던 것보다 오래 걸렸지만, 결국 OIN은 결론을 전달했습니다.

OIN의 포트폴리오는 [Linux System Definition](https://openinventionnetwork.com/linux-system/)에 부합하는 광범위한 소프트웨어를 포괄하지만, Linux 시스템용으로 구현할 수 있는 모든 것을 포괄하지는 않습니다. 특히 이 정의는 코덱(“영상, 정지 영상 또는 오디오 데이터 스트림이나 신호를 변환할 수 있는 프로그램 구성 요소”)이 [이 구성 요소 목록](https://definition.openinventionnetwork.com/table-0/)에 구체적으로 명시되어 있지 않으면 보호 대상이 아니라고 규정합니다.[^f1102549-7]

저는 OIN 직원들이 조사 결과를 Lothian에게 알린 직후인 10월 23일, OIN CEO Keith Bergelt와 잠시 이야기를 나눴습니다. Bergelt는 코덱이 OIN의 Linux System Definition에서 명시적으로 제외되어 있으므로, Lothian이 시도한 커널 기여에는 OIN의 보호가 미치지 않는다는 것이 OIN의 결론이라고 말했습니다. OIN은 Lothian에게 영국의 변호사에게 연락하라고 권고했고, 변호사 한 명을 추천했습니다.

### 현재 상황

안타깝게도 그 소개는 성과로 이어지지 않았다고 Lothian은 말했습니다. 그는 완전히 포기하지는 않았지만 Synaptics의 요구에 따르기 위해 GitHub 저장소를 내렸습니다. 당분간 특허 침해 주장의 영향을 받지 않는 일부 구성 요소의 작업은 계속할 수 있겠지만, Vino 작업은 커널에 제출하지 않을 예정입니다. “이 문제가 해결될 때까지 Vino 자체는 로컬에 남겨 둬야 합니다. Synaptics에 맞서 저를 방어할 비용을 도저히 감당할 수 없습니다.”

어쩌면 우습기도 한 일로, Lothian은 Synaptics의 누군가가 10월 7일 마침내 pull request에 [답을 달았다](https://github.com/DisplayLink/evdi/pull/581#pullrequestreview-5439551411)고 제게 말했습니다. Lothian은 그 의견에 후속 대응할 생각이 없다고 했습니다. “저를 고소하겠다고 위협해 놓고는 ‘pull request를 업데이트해 주시겠어요?’라고 할 수는 없죠.”

당장은 Synaptics가 Linux에서 DisplayLink 도크의 작동을 개선하려던 노력을 중단시키는 데 성공했습니다. 이는 오픈 소스 커뮤니티의 최근 논의 상당 부분이 LLM을 활용한 개발에 집중되어 있는 와중에도, 소프트웨어 특허가 여전히 자유 소프트웨어 개발자와 사용자에게 문제를 일으킨다는 불편한 사실을 상기시킵니다.

---

### 번역자 해설

[^f1102549-1]: 외부 트리(out-of-tree) 커널 모듈은 Linux 커널 본체의 소스 트리와 별도로 관리·배포되는 모듈을 뜻합니다. EVDI가 오픈 소스라는 사실과, 이를 이용하는 DLM 전체의 소스가 공개되어 있다는 것은 별개입니다.
[^f1102549-2]: 여기서 DRM은 저작권 보호 기술인 Digital Rights Management가 아니라 Linux 그래픽 하위 시스템의 **Direct Rendering Manager**입니다. KMS(Kernel Mode Setting)는 해상도나 출력 장치 등 디스플레이 모드 설정을 커널에서 처리하는 기능입니다.
[^f1102549-3]: RFC는 **Request for Comments**의 약자로, 이 문맥에서는 완성된 코드를 즉시 병합해 달라는 요청보다는 설계·구현 방향에 대한 의견을 구하는 패치 제출을 뜻합니다.
[^f1102549-4]: 제어 평면(control plane)은 실제 영상 데이터 자체를 운반하는 경로와 구별하여 장치를 초기화하고 동작 상태를 설정하는 통신 부분을 가리킵니다. 인용문의 요지는 개별 채널만 비교해서는 여러 채널이 공유하는 버스의 타이밍이나 처리 순서에서 발생하는 문제를 놓칠 수 있다는 것입니다.
[^f1102549-5]: 청구항(claim)은 특허에서 보호받으려는 발명의 범위를 기술한 부분입니다. 청구항 대응표(claim chart)는 각 청구항의 구성 요건을 상대방 제품이나 코드의 어느 부분과 연결하는지 정리한 자료입니다. 기사에 등장하는 침해 주장은 당사자의 주장으로, 법원이 침해를 확정했다는 의미는 아닙니다.
[^f1102549-6]: 업스트림(upstream)에 반영한다는 것은 개인 저장소에서만 유지하던 변경을 원 프로젝트, 여기서는 Linux 커널의 공식 개발 흐름에 제출하여 통합하려 한다는 뜻입니다.
[^f1102549-7]: Linux System Definition은 OIN이 보호 대상으로 삼는 소프트웨어 범위를 정하는 명칭입니다. 따라서 “Linux에서 실행된다”거나 “커널에 기여하려는 코드다”라는 사실만으로 해당 범위에 자동으로 포함된다고 이해해서는 안 됩니다. 본문의 코덱 제외 판단은 이 사건에 대해 OIN이 내린 결론입니다.


---

## LLM 정책을 결정하기 위한 투표를 검토하는 Git

- **영문 원제:** Git considers voting to determine its LLM policy
- **원문 / Canonical URL:** https://lwn.net/Articles/1104195/
- **저자:** Jonathan Corbet
- **발행일:** 2026년 11월 9일
- **출처 및 저작자 표시:** Jonathan Corbet, LWN.net, 「Git considers voting to determine its LLM policy」. 위 원문을 한국어로 번역하고 요약 및 옮긴이 해설 각주를 추가했습니다.
- **라이선스:** CC BY-SA 4.0. 원문과 마찬가지로 이 번역 및 추가 해설에도 저작자표시-동일조건변경허락 4.0을 적용합니다.

### 요약

- Git 프로젝트는 LLM이 작성한 기여를 받아들일 조건을 논의하고 있지만, 기존의 엄격한 정책을 완화할지에 관해 합의하지 못했습니다.
- 합의가 어려운 사안을 해결하기 위해 투표 절차를 도입하자는 초안이 나왔습니다. 제안은 문서 패치로 제출하고, 논의와 수정을 거친 뒤 투표에 부치는 방식입니다.
- 투표 자격의 문턱을 어디에 둘지, 어떤 방식으로 개표할지 등 핵심 사항은 아직 정해지지 않았습니다.
- 고용주의 압력을 막기 위한 비밀투표에는 지지가 있었지만, 투표 절차 자체를 채택하는 데도 어느 정도의 합의가 필요하다는 역설이 남아 있습니다.

### 본문

2026년을 관통하는 주요 화두 가운데 하나는 개발 프로젝트들이 LLM이 작성한 기여를 어떤 조건으로 받아들여야 하는지, 아니 애초에 받아들이기는 해야 하는지를 둘러싼 논쟁이었습니다. [Git 프로젝트](https://git-scm.com/)도 이러한 흐름에서 예외가 아니었습니다. 최근 열린 Git Contributor's Summit에서도 이 주제가 [논의되었습니다](https://lwn.net/ml/all/summit-2026.94e33e9ddf234334.06@ttaylorr.com). 다만 이 경우에는 해법에 이르는 길이 다소 우회적일 수 있습니다. 지금껏 민주주의 방식으로 운영된 적이 없는 이 프로젝트가, 논의를 수용 가능한 결론으로 이끌기 위한 수단으로 투표 절차의 도입을 검토하고 있기 때문입니다.[^f1104195-governance]

대부분의 프로젝트와 마찬가지로 Git 커뮤니티도 LLM이 작성한 기여에 대한 정책을 한동안 검토해 왔습니다. 2025년 10월, 프로젝트는 [SubmittingPatches 문서](https://git-scm.com/docs/SubmittingPatches#ai)를 수정해 다음 정책을 포함했습니다.

> Developer's Certificate of Origin은 기여자에게 자신이 프로젝트에 기여하는 내용의 출처를 알고 있으며, 이를 프로젝트의 라이선스에 따라 제출할 권리가 있음을 확인하도록 요구합니다.[^f1104195-dco] AI 도구가 생성한 내용을 상당량 제출할 때 이러한 요건을 법적으로 충족할 수 있는지는 아직 명확하지 않습니다.
>
> AI 생성 콘텐츠의 또 다른 문제는, AI가 여전히 자주 환각을 일으키거나 질 낮은 코드, 커밋 메시지, 문서 또는 출력을 만들어 낸다는 것입니다. 잘못을 지적해 주어도 마찬가지입니다.
>
> 이러한 문제를 피하기 위해, AI가 생성한 것처럼 보이는 내용, 지나치게 격식을 차리거나 장황한 내용, AI slop처럼 보이는 내용, 겉보기에는 그럴듯하지만 말이 되지 않는 내용, 또는 제출자가 이해하지 못하거나 설명할 수 없는 내용은 모두 거부합니다.[^f1104195-slop]

Contributor's Summit에서는 이 정책을 다시 검토했지만 뚜렷한 결론에 이르지 못했습니다. 일부 참가자는 정책을 완화할 여지가 있다고 보는 듯했지만, 다른 참가자들은 여전히 남아 있는 저작권 문제를 제기하거나 LLM이 작성한 기여를 받아들이면 일부 사람들의 프로젝트에 대한 신뢰가 약해질 것이라고 우려했습니다. 사실상 유일하게 도달한 합의가 있다면, 이 주제에서는 합의에 도달할 수 없으리라는 것이었던 듯합니다.

같은 세션에서 이 문제를 투표에 부치자는 아이디어가 나왔고, Emily Shaffer가 그러한 투표를 실시할 수 있는 절차를 만드는 일을 맡기로 했습니다. 이 절차의 초안은 10월 21일 검토를 위해 [게시되었습니다](https://lwn.net/ml/all/20261021200341.378978-1-emilyshaffer@google.com).

투표 제안은 Debian의 절차에서 어느 정도 영향을 받은 듯하지만, 정확히 같지는 않습니다. 어떤 주제에 투표할 때가 되면, 각 제안은 프로젝트 문서를 수정하는 패치 형태로 작성해야 합니다. 그 시점의 판단은 Git maintainer에게 맡깁니다. 각 제안은 개별적으로 게시해 논의하되, 본질적으로 다른 무언가로 바꾸기보다는 다듬는 것을 목표로 합니다. 투표 자격이 있는 사람이라면 누구나 제안을 제출할 수 있습니다. 자격 조건은 뒤에서 다룹니다. 다만 제안이 투표용지에 오르려면 투표 자격이 있는 다른 사람 한 명의 찬동을 받아야 합니다.[^f1104195-second]

제안을 최종 형태로 다듬는 논의 기간은 “약 4주”로 예상하고 있습니다. 이 기간이 끝나면 제안들을 모아 투표용지를 만들고, 2주 동안 투표를 진행합니다. 하지만 초안에는 개표 방식에 관한 언급이 없습니다. 단순히 가장 많은 표를 얻은 제안이 승리하는지, 아니면 어떤 형태의 순위선택 투표를 사용할지는 명시되어 있지 않습니다.[^f1104195-ranked]

초안에 기술된 투표 자격은 다음과 같습니다.

> 자신이 작성한 커밋이 next에 병합된 적이 있거나 코드 리뷰를 2회 이상 제공한 기여자 중에서, 프로젝트 참여가 금지되지 않은 사람의 투표를 환영합니다.[^f1104195-next]

이후 논의에서 지적되었듯이, 이는 Summit에서 논의했던 기준보다 훨씬 포괄적이었습니다. Summit에서는 Git 이력에 적어도 50개의 커밋이 있어야 한다는 요건이 제기되었습니다. 적절한 문턱이 어느 정도인지에 대해서는 실질적인 합의가 없었습니다. Patrick Steinhardt는 25개나 30개의 커밋이 합리적일 수 있다고 [제안했고](https://lwn.net/ml/all/at8IBMQZtJP3bQ9-@pks.im), Jeff King은 장기 기여자에게 어느 정도 가중치를 주는 더 복잡한 규칙을 [제시했습니다](https://lwn.net/ml/all/20261026011731.GA3575069@coredump.intra.peff.net). brian m. carlson은 그저 “사람들이 오직 투표하기 위해 기여할 유인이 생기지 않는” 문턱을 [원했습니다](https://lwn.net/ml/all/atqVZYU3YfuyFdvU@fruit.crustytoothpaste.net). 다행히 이 문제를 투표로 결정하는 절차를 만들자고 제안한 사람은 없었습니다.

Kristoffer Haugsbakk는 이 투표 절차를 도입하면 당면한 문제의 결론은 이미 정해진 것이나 다름없다고 [주장했습니다](https://lwn.net/ml/all/3fe1dc57-5bb2-4e12-8876-a4969e5201cb@app.fastmail.com).

> 투표는 가결될 것입니다. 적어도 한 달에 한 번 Git 작업을 하는 사람들은 기술 기업에서 일합니다. 그 기술 기업들은 이제 AI 기업입니다. 표심은 공교롭게도 경영진의 의견에 동의하는 쪽으로 기울게 될 것입니다.

이에 [Steinhardt](https://lwn.net/ml/all/atoFKhUaM3b38n-b@pks.im)와 [carlson](https://lwn.net/ml/all/atqTWKaRQfvH0Xbm@fruit.crustytoothpaste.net) 같은 개발자들이 반박했습니다. 이들은 고용주의 판단이 아니라 자신의 판단에 따라 투표할 것이라고 강조했습니다. 다만 두 사람 모두, 고용주가 개발자에게 특정 방향으로 투표하도록 강요할 수 없게 비밀투표로 진행해야 한다는 데에는 동의했습니다.

논의는 확고한 결론 없이 잦아들었습니다. 투표 자격 규칙과 개표에 사용할 방식 등 [미해결 질문은 여전히 많습니다](https://lwn.net/ml/all/CAJoAoZmyADCU8VdVDrvR-OuDKybSnT2pMOKbrofRBg6YdpxZ0A@mail.gmail.com). 개표 방식과 관련해서는 Debian의 [devotee](https://salsa.debian.org/debian/devotee/-/blob/master/README?ref_type=heads)와 [Condorcet Internet Voting Service](https://civs1.civs.us/)가 제안되었습니다. 후자는 Linux Foundation Technical Advisory Board 선거에 사용됩니다.[^f1104195-condorcet] Git 프로젝트는 거버넌스 정책에 근본적인 요소를 추가하는 일을 검토하고 있습니다. 가볍게 결정할 수 있는 사안이 아닌 만큼, 결론이 나기까지는 시간이 걸릴 수 있습니다. 투표 절차는 합의가 나올 가능성이 낮아 보이는 상황에서 도움이 되도록 마련하려는 것입니다. 그러나 정작 그 절차 자체도 채택하려면 사실상 이를 뒷받침하는 합의가 필요합니다.

---

### 옮긴이 해설

[^f1104195-governance]: 여기서 민주주의 방식이 아니었다는 설명은 프로젝트 의사결정이 모든 참여자의 동등한 표를 집계하는 제도에 기반하지 않았다는 뜻입니다. 코드 리뷰와 토론을 통해 의견을 모으는 관행과, 정식 투표로 결정을 내리는 거버넌스 규칙은 구분해서 읽어야 합니다.

[^f1104195-dco]: Developer's Certificate of Origin(DCO)은 기여자가 해당 내용을 제출할 권한과 적법한 출처를 확인하는 선언입니다. 프로젝트가 저작권을 양도받는 계약과는 다른 개념이며, 여기서 쟁점은 AI가 생성한 내용에 대해서도 기여자가 그러한 확인을 할 수 있느냐는 것입니다.

[^f1104195-slop]: AI slop은 AI로 대량 생성된 저품질 콘텐츠를 비판적으로 부르는 표현입니다. 이 인용문에서는 문장이 매끈하거나 외형이 그럴듯한 것과, 실제로 의미가 통하고 제출자가 설명할 수 있는 것을 구분하고 있습니다.

[^f1104195-second]: 찬동(seconding)은 제안을 정식 심의나 투표 대상으로 올리는 데 필요한 다른 사람의 지지입니다. 해당 제안을 최종 투표에서 반드시 지지한다는 의미라기보다는, 적어도 투표에 부칠 가치가 있음을 인정하는 절차로 이해하면 됩니다.

[^f1104195-ranked]: 순위선택 투표(ranked-choice voting)는 유권자가 선택지 하나만 고르는 대신 여러 선택지의 선호 순서를 표시하는 방식의 총칭입니다. 순위를 어떤 규칙으로 집계하느냐에 따라 결과가 달라질 수 있으므로, 순위를 받는 것과 개표 알고리즘을 정하는 것은 별개의 결정입니다.

[^f1104195-next]: `next`는 여기서 일반적인 영어 단어가 아니라 Git 프로젝트의 브랜치 이름입니다. 따라서 이 기준은 단순히 패치를 보냈는지가 아니라, 작성한 커밋이 프로젝트의 해당 통합 브랜치에 실제로 반영되었는지를 따집니다.

[^f1104195-condorcet]: Condorcet 방식은 선택지를 둘씩 비교했을 때의 유권자 선호를 활용하는 투표 방식 계열입니다. 모든 다른 선택지를 일대일 비교에서 이기는 선택지를 Condorcet 승자라고 부르지만, 선호가 순환하면 그런 승자가 없을 수도 있어 추가적인 집계 규칙이 필요합니다. 본문은 어떤 구체적인 방식을 채택할지 결정되었다고 말하지 않습니다.


---

## 겨울을 앞두고 최대 절전 모드를 단단히 잠그기

- **영어 원제:** Locking down hibernation for the winter
- **원문 / canonical URL:** https://lwn.net/Articles/1103190/
- **저자:** Daroc Alden / LWN.net
- **발행일:** 2026년 11월 6일
- **저작자 표시 및 라이선스:** Daroc Alden의 LWN.net 원문을 한국어로 번역하고 요약 및 번역자 해설 각주를 추가했습니다. 제공된 원문의 라이선스 표기에 따라 **CC BY-SA 4.0**을 적용합니다. 라이선스: https://creativecommons.org/licenses/by-sa/4.0/ . 원문 본문은 생략하지 않았으며, 추출 과정에서 붙어 있던 목록 항목의 줄바꿈을 복원했습니다.

### 요약

- lockdown은 저장된 최대 절전 이미지를 신뢰할 수 없기 때문에 현재 최대 절전 모드를 비활성화합니다. Matthew Garrett의 패치 세트는 커널만 접근할 수 있는 키로 이미지에 서명하여 이 제약을 해소하려 합니다.
- 단순히 TPM에 키를 보관하는 것만으로는 부족합니다. 공격자가 과거 커널로 부팅하여 키 접근 제한을 우회하는 downgrade 공격까지 막아야 합니다.
- 이 설계는 UEFI가 PCR 5를 cap하기 전에 커널의 boot stub이 표식을 기록하도록 하여, 사용자 공간에서 흉내 낼 수 없는 커널 기능 증거를 만듭니다.
- TPM이 서명한 세션 명령 기록까지 검증함으로써, 이미지 서명 키가 올바른 PCR 상태에서 실제 커널에 의해 만들어졌는지 확인합니다.
- 다만 PCR 5를 cap하지 않는 펌웨어도 있습니다. 패치는 리뷰를 반영한 두 번째 버전이 필요하며, 아직 모든 하드웨어에서 동작하는 완성된 해법은 아닙니다.

### 본문

컴퓨터가 최대 절전 모드(hibernation)에 들어가면 커널은 메모리의 내용을 디스크에 기록한 뒤 시스템을 종료합니다.[^f1103190-hibernation] 최대 절전 모드에서 복귀할 때는 그 데이터를 다시 메모리로 읽어 들이고, 커널이 중단했던 지점부터 실행을 이어 갑니다. 안타깝게도 커널에는 다시 읽어 들이는 데이터가 변조되지 않았는지 알 방법이 없습니다. 이 때문에 실행 중인 커널의 변경을 막으려는 선택적 커널 기능인 [lockdown](https://lwn.net/Articles/791863/)은 최대 절전 모드를 비활성화합니다.[^f1103190-lockdown] 수년간 lockdown을 개발해 온 Matthew Garrett은 이 문제를 해결하려는 [패치 세트](https://lwn.net/ml/linux-pm/20261008132532.1155166-1-matthewg@nvidia.com/)를 공개했습니다. 이 해법은 downgrade 공격, 즉 공격자가 새 보호 장치를 우회하기 위해 이전 버전의 커널로 컴퓨터를 재부팅하는 공격도 막아야 하므로 구현이 복잡해집니다.[^f1103190-antirollback]

Garrett의 패치 세트가 내세우는 기본 발상은 복잡하지 않습니다. 커널만 접근할 수 있는 암호 키로 저장된 최대 절전 데이터에 서명하는 것입니다. 문제는 그런 키를 어떻게 얻느냐에 있습니다. 고정되어 있고 알려진 키는 서명을 위조하는 데 쓸 수 있으므로 이 목적에 아무 소용이 없습니다. 컴퓨터의 [TPM(trusted platform module)](https://en.wikipedia.org/wiki/Trusted_Platform_Module)에 저장된 키가 더 나은 선택입니다.[^f1103190-tpm] 커널은 TPM과 사용자 공간 사이에 있으므로 사용자 공간이 해당 키를 읽지 못하도록 금지하여 키를 안전하게 유지할 수 있습니다. 또한 다른 커널로 부팅했을 때 키를 내주지 않도록 TPM을 설정할 수 있습니다. 다만 과거 커널도 여전히 올바른 secure boot 서명을 가지고 있다는 점 등을 고려하면, 이는 생각만큼 간단하지 않습니다.[^f1103190-secureboot]

TPM을 끌어들이는 주된 동기는 downgrade 공격을 피하는 데 있습니다. 과거 커널은 TPM 접근을 금지해야 한다는 사실을 모르므로, 이론적으로 공격자는 다음과 같이 행동할 수 있습니다.

1. lockdown이 활성화된 새 커널에서 최대 절전 모드 진입을 유발합니다.
2. 복귀(resume)와 swap을 비활성화한 상태로 과거 커널을 부팅합니다.
3. 과거 커널에 해당 TPM 키에 대한 접근을 요청합니다.
4. 저장된 최대 절전 데이터를 변조하고 다시 서명합니다.
5. 새 커널로 재부팅하여 시스템이 변조된 데이터에서 복귀하도록 합니다.

TPM의 핵심 기능 중 하나는 하드웨어가 알려진 상태일 때만 비밀 정보를 읽을 수 있도록 잠그는 기능입니다. TPM은 하드웨어 상태를 추적하기 위해 플랫폼 구성 레지스터(platform-configuration register, PCR)를 사용합니다.[^f1103190-pcr] 이 레지스터에는 값을 직접 쓸 수 없습니다. 대신 시스템이 부팅할 때 TPM이 이를 0으로 초기화하며, 이후 시스템에서 실행되는 소프트웨어가 값을 제공하면 그 값을 PCR의 현재 상태와 함께 해시하여 새 값을 만듭니다.

예를 들어 컴퓨터의 펌웨어가 실행을 시작하면 부트로더의 서명을 검사하고, 특정 secure boot 키를 기준으로 그 서명을 검증했다는 표식을 특정 PCR에 추가할 수 있습니다. 그런 다음 부트로더도 같은 방식으로 운영체제와 연결된 하드웨어의 상태를 확인할 수 있으며, 이런 과정이 이어집니다. 이론적으로는 운영체제와 하드웨어가 변조되지 않았을 때만 PCR이 특정 상태에 도달할 수 있도록 보장하는 것입니다.

실제로는 구현이 더 복잡합니다. 서로 다른 목적에 쓰이는 여러 PCR이 있습니다. 예를 들어 systemd는 시스템이 어느 부팅 단계에 있는지 나타내기 위해 [PCR 11을 사용합니다](https://www.freedesktop.org/software/systemd/man/latest/systemd-pcrphase.service.html). 이를 이용하면 TPM에 저장된 키, 가령 디스크 암호화 키에 initial ramdisk(initrd)가 실행 중일 때만 접근할 수 있도록 만들 수 있습니다. 시스템이 일반 루트 파일시스템으로 전환하려 할 때 systemd는 PCR에 "leave-initrd"를 기록하여, 시스템을 재부팅하기 전에는 되돌릴 수 없는 방식으로 해시를 변경합니다. 이처럼 PCR에 정보를 추가로 기록하여 그 PCR에 연결된 키를 사용할 수 없게 만드는 과정을 PCR을 "cap"한다고 부릅니다.[^f1103190-capping]

커널에 사용자 공간을 시작하기 전에 cap하는 PCR이 있다면, 커널은 새로운 값으로 그 PCR을 extend하고, 그 결과인 PCR 상태에 키를 결부할 수 있을 것입니다. 그러면 새 버전의 커널에서만 키를 읽을 수 있고 과거 버전에서는 읽을 수 없도록 보장할 수 있습니다. 하지만 현재 커널은 어떤 PCR도 cap하지 않고, 그 일을 사용자 공간에 맡깁니다. 따라서 과거 커널에서 실행되는 악성 사용자 공간 애플리케이션도 새 커널이 기대하는 값으로 PCR을 extend할 수 있습니다. 실제로는 과거 커널 위에 있으면서 TPM을 "새 커널" 상태로 만들어 버릴 수 있는 것입니다.

해법은 Garrett이 생각해 낸 "끔찍한 무언가"입니다. PCR 5는 [UEFI](https://uefi.org/) 펌웨어가 하드웨어 측정에 사용하며, 이후 구성요소가 하드웨어 정보를 위조하지 못하도록 [ExitBootServices()](https://uefi.org/specs/UEFI/2.10/07_Services_Boot_Services.html#efi-boot-services-exitbootservices)가 호출될 때 cap됩니다.[^f1103190-uefi] 커널은 시스템을 구동하기 위해 펌웨어와 통신해야 할 수 있으므로, UEFI가 종료되기 전에 boot stub 실행을 시작합니다. 따라서 Garrett은 펌웨어가 PCR 5를 cap하기 전에, 이 커널이 사용자 공간의 TPM 키 접근을 차단하는 기능을 지원한다는 표식을 PCR 5에 삽입하도록 boot stub에 코드를 추가했습니다. 사용자 공간은 그 시점이 지난 뒤에야 시작되므로, 과거 커널에서도 이 표식을 위조할 방법이 없습니다.

하지만 이것만으로는 충분하지 않습니다. PCR 5의 상태는 컴퓨터가 충분히 새로운 커널로 부팅했다는 사실만 보여 줍니다. 사용자 공간이 그 PCR 5 상태에 결부된 자체 키를 만들고, 그 키로 최대 절전 데이터에 서명하는 것까지 막지는 못합니다. 최대 절전 모드 이후 새 커널이 부팅하면 PCR 5에 결부된 키의 서명은 보게 되겠지만, 그 키가 커널 내부에서 생성되었는지, 따라서 사용자 공간에는 숨겨져 있었는지는 여전히 입증할 수 없을 것입니다.

그래서 Garrett의 패치 세트는 한 걸음 더 나아갑니다. TPM과의 상호작용은 개별 세션으로 나눌 수 있습니다. 그의 코드는 그러한 세션을 감사(audit)하여 서명된 다이제스트를 생성할 수 있게 합니다.[^f1103190-audit] 이 다이제스트에는 TPM 자체가 서명합니다. 따라서 서명된 다이제스트가 있다는 것은, 어느 시점에 해당 명령들이 실제로 바로 그 TPM에 전송되었고 바로 그 결과들을 만들었다는 증거가 됩니다.

PCR 5의 활용까지 결합하면, 서명된 최대 절전 이미지를 만드는 전체 절차는 다음과 같습니다.

1. 새 커널이 부팅하면서 PCR 5에 표식을 기록합니다.
2. 펌웨어가 PCR 5를 cap하여 사용자 공간이 커널의 표식을 흉내 내지 못하게 합니다.
3. 커널이 TPM과 새 세션을 시작하고, PCR 5가 해당 상태인지 확인한 다음 새 서명 키를 생성합니다.
4. 세션의 명령 기록(transcript)을 해시하고 TPM으로 서명한 뒤 최대 절전 데이터와 함께 저장합니다.
5. 새로 생성된 키로 최대 절전 데이터에 서명합니다.

이후 재부팅하면 커널은 최대 절전 이미지를 불러오기 전에 여러 검증 단계를 거칩니다.

1. 커널은 서명된 명령 기록의 다이제스트가 현재 TPM에 의해 서명되었는지 확인합니다.
2. 명령 기록을 재현하면 같은 다이제스트가 나오는지 확인합니다.
3. 명령 기록에 올바른 TPM 명령들만 들어 있고 다른 명령은 없는지 확인합니다.
4. 명령 기록이 PCR 5를 읽었는지, 그리고 그 값이 현재 PCR 5의 값과 일치하는지 확인합니다.
5. 마지막으로 명령 기록에서 생성된 키가 최대 절전 데이터에 서명하는 데 사용된 유효한 서명 키인지 확인합니다.

이 모든 작업의 최종 결과는 lockdown 커널을 실행하는 사용자가 최대 절전 모드를 활성화하고, 컴퓨터가 종료된 때부터 최대 절전 모드에서 복귀할 때까지 커널이 변조될 수 없다고 신뢰할 수 있게 된다는 것입니다. 공격자는 데이터에 서명이 있으므로 직접 데이터를 바꿀 수 없습니다. 커널이 막기 때문에 서명에 사용된 키에 접근할 수 없습니다. TPM이 새 커널만 만들 수 있는 상태에 키를 결부하므로 과거 커널로 그 제한을 우회할 수도 없습니다. 그리고 키 생성 명령 기록을 위조할 수 없으므로, 검증을 통과하는 자체 키를 만들 수도 없습니다.

Garrett의 패치 세트에는 약간의 의견이 달렸습니다. James Bottomley는 특정 CPU 권한 수준으로 연산을 제한하는 접근 제어 메커니즘인 "localities"라는 하드웨어 기능을 이용하여, 이런 기능을 더 간단하게 구현할 수는 없는지 [물었습니다](https://lwn.net/ml/linux-pm/435907614242e82ecde1767a967a3110fca6fb37.camel@HansenPartnership.com/). Garrett은 localities가 "이 문제를 다루는 명백히 올바른 방법"이라는 점에는 [동의했지만](https://lwn.net/ml/linux-pm/asqthz69ohnMVCye@srcf.ucam.org/), 하드웨어 지원이 대개 특수 목적 장치로 한정되기 때문에 커널이 이를 활용할 수 있다고 보지는 않았습니다. 대부분의 소비자용 장치에는 TPM이 있지만, 필요한 확장 기능을 지원하는 TPM은 아닙니다.

Bottomley는 펌웨어가 PCR 5를 cap하는 동작도 보편적이지 않다고 지적했습니다. 그의 XPS-13 9380 Core i7(2019년 출시)은 [그 레지스터를 cap하지 않습니다](https://lwn.net/ml/linux-pm/f002fc613bf0bdcf895e5be02dfd2524b7608787.camel@HansenPartnership.com/). Garrett은 그 소식에 [실망했지만](https://lwn.net/ml/linux-pm/asty4acE2B94t5q6@srcf.ucam.org/), 그래도 최신 컴퓨터는 PCR 5를 cap하는 경향이 있으므로 이 패치 세트가 가치 있다고 생각했습니다. 또한 필요하다면 구현을 다른 하드웨어별 해법으로 교체할 가능성도 있습니다.

이 패치 세트는 리뷰에 대응하기 위해 두 번째 버전이 필요합니다. Garrett은 [2021년부터](https://lwn.net/ml/all/20210220013255.1083202-1-matthewgarrett%40google.com/) lockdown에서 최대 절전 모드를 활성화하는 작업을 해 왔지만, 이번에는 downgrade 공격을 체계적으로 막는 설계를 확정한 듯합니다. 그의 목표가 마침내 실현되기까지 그리 오래 걸리지 않을지도 모릅니다.

---

### 번역자 해설

[^f1103190-hibernation]: 최대 절전 모드는 RAM의 실행 상태를 저장장치에 보존한 뒤 전원을 끄는 방식입니다. RAM에 전력을 계속 공급하는 일반적인 suspend-to-RAM과 다릅니다. 이 기사에서 중요한 점은 복귀 이미지가 단순한 사용자 파일이 아니라 커널의 실행 상태까지 복원하는 입력이라는 사실입니다.

[^f1103190-lockdown]: lockdown은 높은 권한을 가진 사용자 공간이라도 실행 중인 커널의 무결성을 훼손할 수 있는 경로를 제한하려는 커널 보안 기능입니다. 여기서는 디스크에서 복원한 메모리 내용이 그 제한을 우회해 커널 상태를 바꿀 수 있다는 점이 문제입니다. lockdown과 secure boot는 관련되지만 같은 기능은 아닙니다.

[^f1103190-antirollback]: antirollback은 이미 허용된 적이 있는 과거 소프트웨어로 되돌아가 새 보안 정책을 우회하는 행위를 막는 성질입니다. 이 설계는 모든 과거 커널의 부팅을 전면 금지하기보다는, 필요한 보호 기능을 갖추지 않은 커널이 최대 절전 이미지의 서명 키를 얻지 못하도록 하는 데 초점을 맞춥니다.

[^f1103190-tpm]: TPM은 키 같은 비밀과 보안 연산을 운영체제의 일반 메모리와 구분해 다루는 신뢰 기반 구성요소입니다. 키를 TPM에 넣었다는 사실만으로 접근 정책이 완성되는 것은 아닙니다. 이 기사에서는 누가 어떤 부팅 상태에서 키를 사용할 수 있는지가 핵심입니다. 또한 이미지에 서명하는 것과 이미지 내용을 암호화하여 숨기는 것은 서로 다른 보안 목표입니다.

[^f1103190-secureboot]: secure boot의 서명 검증은 부팅할 코드가 신뢰된 서명자에 의해 승인되었는지를 확인하는 장치이지, 그 코드가 가장 최신이며 모든 최신 보안 제한을 구현했음을 자동으로 보장하는 장치는 아닙니다. 따라서 정상 서명을 가진 과거 커널도 downgrade 공격의 발판이 될 수 있습니다.

[^f1103190-pcr]: PCR을 extend한다는 것은 기존 값을 임의의 값으로 덮어쓰는 대신, 기존 값과 새 측정값을 해시에 함께 넣어 다음 상태를 만드는 것을 뜻합니다. 부팅 중 쌓인 측정 이력이 최종 값에 반영되며, 여기서는 특정 이력을 가진 경우에만 키 사용을 허용하는 조건으로 활용합니다.

[^f1103190-capping]: 이 글의 capping은 레지스터 자체를 물리적으로 잠그는다는 뜻이 아니라, PCR을 추가로 extend하여 이전 상태를 요구하는 키의 사용 조건을 더 이상 만족하지 않게 만드는 것을 뜻합니다. 이 방식이 보안 경계가 되려면 표식을 기록할 수 있는 시점과 신뢰하지 않는 코드의 실행 시점 사이의 순서가 보장되어야 합니다.

[^f1103190-uefi]: ExitBootServices()는 UEFI 부트 서비스 이용 단계에서 운영체제가 주도하는 실행 단계로 넘어가는 경계입니다. boot stub은 이 경계 이전에 실행되는 커널의 초기 부팅 코드입니다. 기사는 이 시점 차이를 이용하지만, 본문 후반의 사례처럼 PCR 5를 cap하는 펌웨어 동작이 모든 시스템에서 보장되는 것은 아닙니다.

[^f1103190-audit]: 다이제스트는 명령과 결과 같은 데이터를 해시로 요약한 값입니다. 여기서 TPM이 서명한 세션 감사 기록은 이미지 서명 키의 생성 경위를 검증하는 증거가 됩니다. 이미지의 서명만 확인하는 것과 달리, 그 키가 어떤 명령과 PCR 조건 아래에서 만들어졌는지도 검사한다는 점이 중요합니다.


---

## User namespace + file capability = 문제

- 영어 원제: **User namespaces + file capabilities = trouble**
- 원문 URL: https://lwn.net/Articles/1103429/
- 저자: **Jonathan Corbet**, LWN.net
- 원문 게시일: **2026년 11월 5일**
- 저작자 표시 및 라이선스: Jonathan Corbet의 위 LWN.net 기사를 한국어로 번역하고 역자 해설을 추가했습니다. 제공된 원문에 명시된 **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**에 따라 원저자와 출처를 표시하며, 이 번역 및 해설에도 같은 라이선스를 적용합니다.

### 요약

- User namespace는 내부의 root 권한을 외부의 비특권 사용자로 매핑해 컨테이너를 격리하지만, root를 상위 namespace의 root로 매핑하면 file capability를 통한 권한 유출 위험이 생깁니다.
- `CAP_SETFCAP`을 내려놓는 것만으로는 충분하지 않습니다. 중첩 namespace 생성, `setns()`, 열린 `uid_map` 파일 디스크립터, 다른 프로세스의 도움, `ptrace()` 등으로 제한을 우회할 수 있습니다.
- Linux 5.12 직전에 도입된 방어책은 namespace 생성자가 `CAP_SETFCAP`을 보유했는지를 기록하지만, 여러 단계의 namespace와 프로세스 사이 상호작용을 모두 다루지는 못합니다.
- Josef Bacik의 패치 시리즈는 `setfcap_level`로 capability가 상위 namespace 어디까지 유효한지 추적하고, namespace 진입·UID 매핑·file capability 설정·프로세스 추적에 일관된 검사를 추가합니다.
- 기사 작성 시점에 여덟 번째 개정에 도달한 이 작업은 격리 경계를 강화하지만, root 매핑과 file capability의 결합은 여전히 복잡한 보안 문제입니다.

### 본문

[User namespace](https://lwn.net/Articles/532593/)는 커널이 컨테이너를 구성하는 데 사용하는 핵심 도구 중 하나입니다. User namespace 안의 프로세스는 시스템에 대한 완전한 root 접근 권한을 가진 것처럼 보이면서도, 더 넓은 시스템에서는 추가 권한을 전혀 얻지 않을 수 있습니다.[^f1103429-namespace] 적어도 의도는 그렇습니다. 실제로는 권한을 user namespace 안에 가두는 일이 어렵다는 사실이 자주 드러났습니다. 한 가지 예로 Josef Bacik의 [이 작은 패치 시리즈](https://lwn.net/ml/all/20261027-b4-setfcap-userns-v8-0-2674adc63f3c@toxicpanda.com)를 살펴보겠습니다. 이 시리즈는 user namespace 안의 프로세스가 바깥쪽 프로세스의 권한을 높일 수 있는 몇 가지 상황을 해결하려는 것입니다.

#### 배경 지식

User namespace에 처음 배치되는 프로세스는 기본 시스템의 init 프로세스와 상당히 비슷하게 취급됩니다. 사용자 ID 0으로 실행되며 완전한 root 권한을 갖습니다. 다만 커널은 컨테이너 바깥에서 접근 허용 여부를 판단하기 전에 모든 사용자 ID를 다시 매핑합니다. 기본적으로 모든 사용자 ID는, 예를 들어 namespace 바깥에 마운트된 파일시스템에 접근하기 전에, “알 수 없는 사용자” ID인 65534로 매핑됩니다. 따라서 namespace 안의 root 접근 권한이 바깥에서는 아무 접근 권한도 없는 상태로 바뀔 수 있습니다. Namespace가 중첩되어 있다면 시스템 부팅 때 만들어진 최초 namespace에 도달하기까지 여러 단계의 재매핑이 적용될 수 있습니다.[^f1103429-mapping]

해당 namespace 안에서 실행되는 어느 프로세스든 그 프로세스의 `/proc` 디렉터리에 있는 `uid_map` 또는 `gid_map` 파일에 쓰면 user namespace의 사용자 ID 및 그룹 ID 매핑을 바꿀 수 있습니다. 다만 root 권한 없이는 namespace를 만든 프로세스의 ID 이외의 값으로 ID를 다시 매핑할 수 없습니다. 사용자 ID가 1000인 비특권 프로세스가 user namespace를 만들면, namespace 안의 어느 ID에서 시작하는 매핑이든 설정할 수 있지만 바깥쪽 ID는 오직 1000이어야 합니다. 매핑 변경 역시 한 번만 가능한 작업입니다. 매핑을 설정하고 나면 다시 바꿀 수 없습니다.

또 하나 알아 두어야 할 중요한 배경 지식은 [capability](https://man7.org/linux/man-pages/man7/capabilities.7.html)입니다. Capability는 주어진 프로세스가 어떤 권한을 갖는지를 나타냅니다. 기본적으로 root 사용자는 모든 capability를 가지며, 다른 프로세스는 하나도 갖지 않습니다. 뒤에서 보겠지만, root로 실행 중인 프로세스가 특정 동작을 막기 위해 자신의 capability 일부를 내려놓는 경우도 있습니다.[^f1103429-capability]

마지막으로, *file* capability는 일종의 setuid 실행 파일을 만드는 방법으로 생각할 수 있습니다. [setcap](https://man7.org/linux/man-pages/man8/setcap.8.html) 명령으로 특정 capability 집합을 파일에 부여할 수 있습니다. 이후 그 파일에 담긴 프로그램을 실행하는 프로세스는 지정된 capability를 부여받습니다.[^f1103429-filecap] 말할 필요도 없이 이런 식으로 파일에 capability를 부여하는 것은 특권 작업입니다. 구체적으로, 이를 시도하는 프로세스에는 `CAP_SETFCAP` capability가 있어야 합니다. 커널에는 file capability가 user namespace 안에서는 작동하지만 바깥에서는 무시되도록 하는 정교한 장치가 있습니다. 구체적으로 “버전 3 확장 속성”에는 root가 아닌 사용자 ID를 인코딩할 수 있으며, 그 ID가 소유하는 namespace 안에서는 이 ID를 root로 매핑할 수 있습니다. 자세한 내부 동작이 궁금하다면 [capabilities 매뉴얼 페이지의 이 하위 절](https://man7.org/linux/man-pages/man7/capabilities.7.html#:~:text=File%20capability%20extended%20attribute%20versioning)을 참고하시기 바랍니다.[^f1103429-xattr]

#### File capability의 문제

User namespace는 내부의 root 사용자를 외부의 비특권 사용자로 매핑하도록 설계되었습니다. 하지만 namespace 안의 root를 그 namespace를 포함하는 상위 namespace의 root로 매핑하는 것도 가능합니다. 이렇게 하면 여러 보안 문제가 생기는 것은 분명하지만, 충분히 주의를 기울이면 root 매핑 user namespace도 상당한 수준의 격리를 제공할 수 있습니다.[^f1103429-rootmapped] 특히 namespace 안에서 init 프로세스로 실행되는 코드를 상위 namespace 관리자가 신뢰한다면 더욱 그렇습니다. 그 코드는 필요한 설정을 모두 수행한 다음 권한, 즉 capability를 내려놓고 컨테이너가 실행하도록 만들어진 워크로드에 제어를 넘길 수 있습니다.

User namespace 안의 root 사용자가 상위 namespace에서도 보이는 실행 파일에 file capability를 추가하면, 보통 그 capability에는 root가 상위 namespace에서 매핑되는 사용자 ID라는 한정 조건이 붙습니다. 따라서 상위 namespace에서 비특권 사용자가 그 실행 파일을 실행하더라도 해당 capability는 효력을 발휘하지 않습니다. 하지만 내부 namespace가 root 매핑되어 있다면 이런 한정이 이루어지지 않으며, capability는 상위 namespace에서도 *실제로 효력을 발휘합니다*. 그러므로 root가 이런 방식으로 파일에 capability를 추가하도록 허용하면 권한이 namespace 밖으로 빠져나갈 수 있습니다.

이를 막으려면 namespace 안에서 실행되는 root 프로세스가 `CAP_SETFCAP`을 반드시 내려놓도록 주의해야 합니다. 그러면 그 프로세스는 더 이상 file capability를 만들 수 없으며, 권한 유출도 사라집니다. 적어도 그 root 프로세스가 자신만의 root 매핑 user namespace를 만들기 전까지는 그렇습니다. 새 user namespace에서 처음 실행되는 프로세스는 모든 capability를 갖는다는 점을 기억하시기 바랍니다. 따라서 그 프로세스는 `CAP_SETFCAP`을 다시 얻게 됩니다. 그러면 상위 namespace의 파일에 file capability를 추가할 수 있습니다. 그 상위 namespace 역시 root 매핑되어 있으므로 변경 사항은 다시 그 위의 namespace까지 전파됩니다. 그 시점에는 다시금 namespace 바깥에서 접근할 수 있고 비특권 사용자가 실행할 수 있는, 강화된 capability가 붙은 파일이 존재하게 됩니다.

2021년 5.12 커널 릴리스 직전에 병합된 [이 커밋](https://git.kernel.org/linus/db2e718a4798)은 그 문제를 해결하기 위한 것입니다. 어떤 프로세스가 namespace의 `uid_map` 파일에 써서 root-to-root 매핑을 만들려고 하면, 그 프로세스에 `CAP_SETFCAP`이 없는 한 시도는 실패합니다. 하지만 그것만으로는 충분하지 않습니다. 새로 만든 user namespace 안의 root 프로세스에는 그 capability가 있으므로 자신의 `uid_map` 파일에 쓸 수 있기 때문입니다. 이는 namespace 안팎의 유효 UID가 같으면 허용되는 작업입니다. 그래서 이 패치는 해당 namespace의 생성자가 `CAP_SETFCAP`을 보유했는지도 기록합니다. 생성자에게 그 capability가 없었다면, namespace 안에서 root-to-root 매핑을 만들려는 시도는 실패합니다. 문제 해결입니다.

#### 더 많은 유출 경로

물론 문제는 실제로 해결되지 않았습니다. 그렇지 않았다면 이 패치 세트가 존재할 리 없겠지요. 패치 세트 말입니다. 기억하시죠? 이 기사는 Bacik의 패치 세트에 관한 기사입니다. 알고 보니 root 매핑 user namespace를 만들 때 `CAP_SETFCAP`을 요구하는 것만으로는 일부 상황에서 권한 유출을 막기에 충분하지 않습니다.

Root 매핑 user namespace 안에 두 root 프로세스가 있다고 가정해 보겠습니다. 하나를 “A”라고 부르겠습니다. A는 모든 capability를 보유하지만 다른 하나인 “B”에는 `CAP_SETFCAP`이 없습니다. A가 자신의 user namespace를 만들면 그 namespace에는 “생성자가 `CAP_SETFCAP`을 보유했음” 플래그가 설정됩니다. 그러면 B는 [setns()](https://man7.org/linux/man-pages/man2/setns.2.html) 호출로 그 namespace에 들어갈 수 있습니다. B의 UID가 namespace 생성자의 UID와 같으므로 진입이 허용되고, B는 그 namespace 안에서 모든 capability를 갖게 됩니다.[^f1103429-setns] 이 시점에 B는 `uid_map` 파일에 root 매핑을 쓴 뒤, 상위 namespace 바깥에서도 보이는 file capability를 부여하기 시작할 수 있습니다. 다시 말해 B는 이전에 내려놓았던 `CAP_SETFCAP` capability를 되찾게 됩니다.

다른 시나리오도 있습니다. A가 `uid_map` 파일을 열기만 하고 쓰지는 않은 다음, 어떤 식으로든 그 파일 디스크립터를 B에게 넘기면 B가 거기에 root-to-root 매핑을 쓸 수 있습니다. `CAP_SETFCAP` 검사는 `uid_map` 파일에 쓸 때가 아니라 열 때 이루어지므로 그 매핑이 허용됩니다.[^f1103429-fd] A가 그런 식으로 특권이 담긴 파일 디스크립터를 남에게 넘겨서는 안 된다고 말할 수도 있습니다. 하지만 A가 `CAP_SETFCAP`을 내려놓기 전에 그 디스크립터를 닫지 않는 것만으로도 그런 일이 일어날 수 있습니다.

B가 user namespace를 만들면 `CAP_SETFCAP` 플래그가 설정되지 않으므로 B는 그 namespace에 root 매핑을 만들 수 없습니다. 하지만 A에게는 그 capability가 있으므로 B의 새 user namespace에 root 매핑을 써 줄 수 있습니다. 그러면 다시 한번 B는 상위 namespace에서 효력을 발휘하는 file capability를 설정할 수 있게 됩니다. 경우에 따라서는 중간에 root가 아닌 UID를 거치는 여러 단계의 매핑이 있을 수도 있습니다. 컨테이너에서 자주 사용하는 [ID-mapped mount](https://lwn.net/Articles/837566/)도 나름의 복잡성을 더합니다. 기반 파일시스템에서는 root가 아닌 UID가 특정 mount namespace 안에서는 root로 보일 수 있기 때문입니다.[^f1103429-idmount]

마지막으로, B는 그냥 [ptrace()](https://man7.org/linux/man-pages/man2/ptrace.2.html)로 A에 연결한 다음 A가 자신의 `uid_map` 파일에 쓰거나 file capability를 직접 설정하도록 만들 수도 있습니다. 유효 UID가 같기 때문에 연결이 허용되는 것입니다. A에는 `CAP_SETFCAP`이 있으므로 그 작업들은 허용됩니다.[^f1103429-ptrace]

#### 구멍 막기

이러한 권한 유출을 막으려면 `CAP_SETFCAP` 추적을 강화하고 사용자 공간에서 관찰할 수 있는 몇 가지 변경도 해야 합니다. 시리즈의 [첫 번째 패치](https://lwn.net/ml/all/20261027-b4-setfcap-userns-v8-1-2674adc63f3c@toxicpanda.com)는 [user_namespace 구조체](https://elixir.bootlin.com/linux/v7.3/source/include/linux/user_namespace.h#L79)의 불리언 `parent_could_setfcap`을 정수형 `setfcap_level` 필드로 바꿉니다. 기존 불리언은 user namespace 생성자가 `CAP_SETFCAP`을 보유했는지를 기록했습니다. 새 필드는 그 capability가 위로 어디까지 존재했는지, 즉 상위 user namespace 몇 단계에 걸쳐서도 보유하고 있었는지를 기록합니다. 이 새 변수는 현재 user namespace의 `CAP_SETFCAP`이 그만큼의 상위 namespace에서도 효력을 발휘한다는 사실을 반영합니다.[^f1103429-level]

[이 패치](https://lwn.net/ml/all/20261027-b4-setfcap-userns-v8-2-2674adc63f3c@toxicpanda.com)는 프로세스가 `setns()`를 이용해 조상 user namespace에 대한 `CAP_SETFCAP`을 얻지 못하게 하려는 것입니다. 구체적으로는, 프로세스가 더 높은 어떤 단계에서 root 매핑되어 있는 user namespace로 들어가려고 `setns()`를 호출할 때, 그 프로세스의 `setfcap_level`이 최소한 대상 user namespace의 수준만큼은 위로 뻗어 있는지를 확인하는 검사를 추가합니다. Root 매핑 user namespace인지 검사할 때는 아직 매핑이 전혀 설정되지 않은 namespace도 포함합니다. 그런 namespace도 나중에 root 매핑이 *될 수 있기* 때문입니다. `setns()`를 호출한 프로세스에 충분한 범위까지 유효한 `CAP_SETFCAP`이 없으면 호출은 `EPERM` 오류로 실패합니다. 이것은 사용자 공간에 드러나는 변경 중 하나입니다. 현재 커널에서는 그 호출이 성공합니다.

[이 패치](https://lwn.net/ml/all/20261027-b4-setfcap-userns-v8-3-2674adc63f3c@toxicpanda.com)는 `uid_map` 파일에 써서 root 매핑을 설정하는 동작을 제어하기 위해 비슷한 변경을 합니다. 쓰려는 내용이 어느 조상 user namespace에서든 root 사용자로 이어지는 매핑을 만든다면, 쓰는 프로세스의 `setfcap_level`이 적어도 그 단계까지 도달해야 하며, 그렇지 않으면 작업은 실패합니다. [이 패치](https://lwn.net/ml/all/20261027-b4-setfcap-userns-v8-4-2674adc63f3c@toxicpanda.com)는 `CAP_SETFCAP`을 가진 프로세스가 `uid_map` 파일에 쓰는 경우를 다룹니다. File capability를 쓰려는 시도를 검사하여, 쓰는 프로세스의 `setfcap_level`이 root 매핑된 모든 조상 namespace에 도달할 만큼 충분히 높은지 확인합니다. 마지막으로 [이 패치](https://lwn.net/ml/all/20261027-b4-setfcap-userns-v8-5-2674adc63f3c@toxicpanda.com)는 `ptrace()` 호출에도 비슷한 검사를 적용합니다. 추적하는 프로세스의 `setfcap_level`이 최소한 대상 프로세스의 수준만큼 도달하지 않으면 호출은 실패합니다.

이 시리즈는 기사 작성 시점까지 여덟 차례 개정되었습니다. 상당히 발전해 왔지만 최근 몇 버전은 대체로 테스트 추가에 초점을 맞추었습니다. 이론상 이 패치들을 적용하면 file capability를 이용해 user namespace 밖으로 권한을 유출하는 일은 더 이상 가능하지 않아야 합니다. 실제로는 여기 얽힌 복잡성이 워낙 커서 여전히 의구심을 가질 만한 이유가 있을 수 있습니다. User namespace가 정말 안전하도록 보장하는 작업은 수년에 걸쳐 이어져 왔습니다. 이 namespace 바깥의 root 접근 권한으로 매핑하는 일은 그 작업을 더욱 어렵게 만들 뿐입니다.

### 역자 해설

[^f1103429-namespace]: **Namespace와 격리의 범위:** namespace는 프로세스가 보는 자원과 식별자의 범위를 나누는 커널 메커니즘입니다. User namespace는 특히 사용자·그룹 ID와 capability의 적용 범위를 다룹니다. 이것 하나가 파일시스템·네트워크 등 모든 자원을 자동으로 격리하는 것은 아니므로, “안에서 root”와 “호스트 전체에서 root”를 구별해 읽어야 합니다.

[^f1103429-mapping]: **UID 매핑과 최초 namespace:** 같은 숫자 UID라도 어느 user namespace의 값인지에 따라 의미가 달라집니다. 매핑은 내부 ID를 상위 namespace의 ID와 연결하며, 중첩되면 그 관계를 여러 단계 따라가야 합니다. 본문의 65534는 매핑되지 않은 ID를 표시하는 맥락으로 이해하는 것이 좋으며, 그 숫자가 모든 사용자를 실제로 하나의 권한 주체로 바꾼다는 뜻은 아닙니다.

[^f1103429-capability]: **Capability는 root 권한의 분할:** Linux capability는 전통적인 root의 권한을 기능별로 나눈 것입니다. `CAP_SETFCAP`은 파일에 capability를 설정하는 권한입니다. 중요한 것은 capability의 이름뿐 아니라 어느 user namespace에서 유효한가입니다. 자식 namespace에서 capability를 얻었다고 조상 namespace에서도 자동으로 같은 권한을 얻는 것은 아닙니다.

[^f1103429-filecap]: **File capability와 setuid의 차이:** setuid 실행 파일은 실행 시 유효 사용자 ID를 바꾸는 방식이고, file capability는 필요한 capability를 파일에 기록하는 방식입니다. 둘 다 실행을 계기로 권한을 부여할 수 있다는 점에서 비교됩니다. 본문은 개념을 간략히 설명한 것으로, 실제 실행 시 부여되는 capability는 프로세스의 capability 집합과 실행 관련 보안 제한에도 영향을 받습니다.

[^f1103429-xattr]: **버전 3 확장 속성:** 확장 속성(xattr)은 파일 내용과 별도로 저장되는 메타데이터입니다. Namespace를 고려한 file capability는 어떤 namespace의 root에 해당하는지 판별할 수 있도록 UID 정보를 함께 저장합니다. 이 한정 정보가 있어야 내부에서 설정한 권한이 바깥 실행에도 무조건 적용되는 일을 막을 수 있습니다.

[^f1103429-rootmapped]: **Root 매핑의 의미:** 여기서 root 매핑은 내부 UID 0이 상위 또는 조상 namespace에서도 UID 0에 연결되는 경우를 뜻합니다. 내부 root를 외부 UID 1000 같은 비특권 사용자에 연결하는 경우와 달리, 파일에 저장한 권한의 효과가 격리 경계를 넘어갈 위험을 따져야 합니다. “상위”는 바로 바깥의 부모를, “조상”은 그보다 더 위의 namespace까지 포함합니다.

[^f1103429-setns]: **`setns()`와 권한의 재획득:** `setns()`는 기존 namespace에 들어가는 시스템 호출입니다. 이 사례의 핵심은 기존 namespace에서 내려놓은 capability를 다른 user namespace 안에서 다시 얻을 수 있다는 점입니다. 본문의 UID 일치는 설명된 공격 시나리오의 조건이지, UID만 같으면 모든 종류의 `setns()` 진입이 언제나 허용된다는 일반 규칙은 아닙니다.

[^f1103429-fd]: **열린 파일 디스크립터와 권한 검사 시점:** 파일 디스크립터는 이미 열린 커널 객체에 대한 참조입니다. 열 때의 자격으로 권한을 검사하는 경로에서는 나중에 권한을 내려놓거나 다른 프로세스가 디스크립터를 넘겨받아도 그 참조가 남을 수 있습니다. 따라서 안전한 권한 강등은 capability 비트 제거뿐 아니라 남겨 둔 디스크립터도 함께 검토해야 합니다.

[^f1103429-idmount]: **ID-mapped mount:** 마운트 단위로 파일 소유자 ID를 다른 관점에서 해석하도록 하는 기능입니다. 디스크에 기록된 소유자 ID 자체를 일괄 변경하는 것과는 다릅니다. 그래서 file capability의 효력이 어디까지 미치는지 판단할 때는 user namespace 사이의 매핑과 마운트의 ID 매핑을 혼동하지 않고 함께 추적해야 합니다.

[^f1103429-ptrace]: **`ptrace()`가 격리에 미치는 영향:** 디버거 등에 쓰이는 `ptrace()`는 다른 프로세스의 실행과 상태에 개입하는 통로입니다. 낮은 권한의 프로세스가 더 강한 권한의 프로세스를 조종할 수 있다면 직접 금지된 작업을 대신 수행시킬 수 있습니다. 실제 허용 여부에는 UID 외의 보안 검사도 있으므로, 본문은 해당 연결이 허용되는 조건을 전제로 읽어야 합니다.

[^f1103429-level]: **`setfcap_level`이 추적하는 것:** 이 필드는 capability의 종류나 개수가 아니라 namespace 계층에서의 효력 범위를 추적합니다. 단순한 “있다/없다” 플래그로는 중간 namespace를 거친 우회를 구별하기 어렵습니다. 기사에서 설명하는 패치는 진입·매핑·파일 권한 설정·추적이라는 서로 다른 경로가 같은 격리 경계를 존중하도록 범위 검사를 맞추려는 접근입니다.


---

## glibc 동적 링커의 추가 보안 강화

- **영문 원제:** Additional hardening for the glibc dynamic linker
- **원문 / Canonical URL:** https://lwn.net/Articles/1105134/
- **저자:** Daroc Alden
- **발행일:** 2026년 11월 11일
- **저작자 표시 및 라이선스:** Daroc Alden / LWN.net 원문. 제공된 원문 파일에 명시된 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)에 따라 한국어로 번역하고 요약과 옮긴이 각주를 추가했습니다. 이 번역 및 해설에도 같은 라이선스를 적용합니다.

### 요약

- Node.js의 Brotli decoder에서 발견된 buffer overflow는 Linux용 공식 바이너리가 ASLR을 지원하도록 빌드되지 않았다는 문제를 부각했습니다.
- glibc에는 PIE를 요구하고, text relocation과 쓰기·실행 동시 허용 segment 등을 제한하는 여섯 가지 dynamic linker tunable이 제안되었습니다.
- `glibc.rtld.hardened=1`은 이 설정들을 한꺼번에 보안 강화 상태로 전환하기 위한 옵션입니다. 기사에서 다루는 것은 제안된 패치이며 기본 동작은 바꾸지 않습니다.
- 이미 PIE를 기본으로 사용하는 배포판 패키지에는 적용 부담이 작겠지만, 배포판 밖에서 빌드한 프로그램과의 호환성 때문에 정작 보호가 필요한 프로그램에서 설정을 꺼야 할 수도 있습니다.

### 배경이 된 취약점

[Node.js 프로젝트](https://nodejs.org/en)에서는 최근 [Brotli](https://brotli.org/) decoder에 영향을 주는 [보안 취약점](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases#nodejs-brotli-decoder-out-of-bounds-write-permits-remote-code-execution-cve-2026-111497---high)이 발견되었습니다. 이 버그는 [buffer overflow였습니다](https://project-zero.issues.chromium.org/issues/565308158). 그런데 Linux용 공식 Node.js 바이너리의 빌드 방식 때문에, buffer overflow가 원격 코드 실행으로 이어지는 것을 막는 주요 보호 장치 중 하나인 [주소 공간 배치 무작위화](https://en.wikipedia.org/wiki/Address_space_layout_randomization)(address space layout randomization, ASLR)를 활성화할 수 없었습니다.[^f1105134-aslr] ASLR이 활성화되어 있었다면 이 버그는 이론상으로는 여전히 악용할 수 있었겠지만, 실제로 악용하기는 훨씬 어려웠을 것입니다. 이에 GNU C Library(glibc)는 관리자가 ASLR을 지원하지 않는 프로그램을 금지할 수 있도록 새로운 [tunable 설정](https://sourceware.org/glibc/manual/latest/html_node/Tunables.html)들을 [검토하고 있습니다](https://lwn.net/ml/all/20261028175613.3779425-1-adhemerval.zanella@linaro.org/). 이 새 설정은 반가운 보안 강화 조치이지만, 문제의 근본 원인까지 해결하지는 못할 수 있습니다.

### 배경

프로그램에 buffer overflow가 있으면 이를 이용해 프로그램 실행을 장악할 수 있는 경우가 많습니다. 그러면 데이터 손상 버그가 원격 코드 실행 취약점으로 바뀝니다. 일반적으로는 프로그램이 나중에 점프할 대상인 포인터를 덮어써서, 프로그램의 제어 흐름을 공격자가 선택한 주소로 돌리는 방식입니다. 그다음에는 예를 들어 공격자가 제어하는 인자로 [execv()](https://man7.org/linux/man-pages/man3/execv.3.html)를 호출하는 일이 어렵지 않습니다. 덮어쓰는 포인터는 흔히 stack에 있는 반환 주소이지만, callback, 함수 내부의 간접 점프, C++ 가상 메서드 테이블을 이용하는 비슷한 공격도 입증된 바 있습니다.

공격자가 이런 일을 하기 어렵게 만드는 완화 기법은 많습니다. [제어 흐름 무결성](https://en.wikipedia.org/wiki/Control-flow_integrity)(control-flow integrity), [shadow stack](https://en.wikipedia.org/wiki/Shadow_stack), 심지어 [유용한 점프 지점의 수를 줄이도록 코드 생성을 조정하는 방법](https://www.openbsd.org/papers/asiabsdcon2019-rop-paper.pdf)도 있습니다. ASLR은 이런 완화 기법 가운데 가장 단순한 것이라고 할 만합니다. 현대 compiler가 재배치 가능한 코드를 생성할 수 있다는 점을 이용해, 가상 메모리에서 무작위로 선택한 위치에 프로그램을 배치하는 방식입니다. 함수 포인터를 덮어쓰려는 공격자는 유용한 곳으로 제어 흐름을 돌리려면 프로그램의 기준 주소(base address)를 알아내야 합니다.

위치 독립 코드(position-independent code)로 컴파일하는 데에도 영향은 있습니다. 이런 코드는 위치 의존 코드보다 크기가 약간 더 크고 속도가 약간 더 느린 경우가 많습니다.[^f1105134-pie] 2020년 Node.js 기여자 “woodfairy”가 Node.js에 미치는 영향을 [측정한 결과](https://github.com/nodejs/node/issues/33425#issuecomment-711443427), workload에 따라 5~10% 느려졌습니다. 이 정도의 성능 저하는 [macOS에서는 받아들일 수 있다고 판단했지만](https://github.com/nodejs/node/pull/35704), Linux에서는 그렇지 않았습니다. 단, Android는 위치 의존 코드를 금지하기 때문에 선택의 여지가 없으므로 예외였습니다.

Debian, Ubuntu, Arch, Alpine, Gentoo를 비롯한 여러 Linux 배포판은 위치 독립 실행 파일(position-independent executable)을 기본으로 활성화합니다. 이런 배포판에서 Node.js를 소스에서 컴파일하거나 배포판 패키지를 설치하면 ASLR이 활성화됩니다. 반면 Red Hat Enterprise Linux 8을 실행하는 시스템에서 컴파일되는 공식 Node.js 바이너리 패키지는 여전히 그렇지 않습니다.

### 동적 링킹

동적으로 링크된 프로그램은 [새 프로세스의 초기화](https://lwn.net/Articles/961117/)를 동적 링커(dynamic linker)에 의존합니다.[^f1105134-elf] Linux에서는 다른 구성을 택한 배포판도 있지만, 일반적으로 glibc 프로젝트가 이 링커를 제공합니다. 이 링커는 동작에 영향을 주는 tunable이라는 설정 옵션들을 지원합니다. 환경 변수로 설정할 수도 있고, `/etc/tunables.conf` 파일에서 시스템 전체에 적용하도록 설정할 수도 있습니다.

10월 26일, Daniel Colascione는 glibc 개발 메일링 리스트에 위치 의존 실행 파일을 금지하는 새로운 tunable을 추가하는 것이 타당한지 [물었습니다](https://lwn.net/ml/all/87v76pq8oj.fsf%40dancol.org/). Adhemerval Zanella Netto는 구현하고 싶은 보안 강화 관련 tunable 목록을 제시하며, 모두 자신의 할 일 목록에 올라 있다고 [답했습니다](https://lwn.net/ml/all/5f6c2165-e7d8-43d8-b821-5bad42453fd8@linaro.org/). 그는 GCC의 `-fhardened` 옵션과 비슷하게, 이들을 한꺼번에 활성화하는 단일 `glibc.hardened` tunable을 추가하는 방안도 제안했습니다.

Zack Weinberg는 고정 위치 실행 파일 대부분이 낮은 주소에 링크되므로, 최소 [mmap()](https://man7.org/linux/man-pages/man2/mmap.2.html) 주소인 [vm.mmap\_min\_addr](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/vm.html#mmap-min-addr) sysctl을 더 큰 값으로 설정하면 kernel이 이런 실행 파일을 거부하도록 할 수 있다고 [지적했습니다](https://lwn.net/ml/all/ded92b1a-2079-400e-80ba-edc316893a7b@app.fastmail.com/). 다만 그는 이 아이디어에 몇 가지 문제가 있다고 덧붙였으며, Maciej Rozycki는 [추가적인 문제점들을 지적했습니다](https://lwn.net/ml/all/alpine.DEB.2.21.2610262115340.42255@angie.orcam.me.uk/).

Zanella는 약속했던 tunable의 구현을 10월 28일에 게시했습니다. 프로젝트의 기본 동작은 그대로 유지되지만, 각 옵션을 그 의미에 따라 `0` 또는 `1`로 설정하여 새로운 보호 기능을 활성화할 수 있습니다. 새 옵션은 다음과 같습니다.

- `glibc.rtld.require_pie=1`: 로드하는 프로그램이 위치 독립적일 것을 요구합니다.
- `glibc.rtld.textrel=0`: 쓰기 가능으로 매핑되지 않은 실행 파일 section을 대상으로 링커가 relocation을 수행하도록 요청하는 프로그램을 금지합니다.[^f1105134-textrel]
- `glibc.rtld.wx_segments=0`: 시작 시 일부 segment를 쓰기 가능하면서 동시에 실행 가능하도록 매핑해 달라고 요청하는 프로그램을 금지합니다.[^f1105134-stack]
- `glibc.rtld.bind_now=1`: global offset table의 지연 해석(lazy resolution)을 사용하지 않도록 합니다. `LD_BIND_NOW` 환경 변수를 사용하는 것과 같습니다.[^f1105134-binding]
- `glibc.rtld.relative_rpath=0`: 상대 경로를 통해 동적 라이브러리를 찾지 못하게 합니다.[^f1105134-rpath]
- `glibc.rtld.relro={1,2}`: 각각 [relocation read-only](https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro)(RELRO) 또는 `-z now`의 사용을 요구합니다.[^f1105134-relro]

여섯 옵션 모두를 한꺼번에 보안 강화 동작으로 설정하려면 `glibc.rtld.hardened=1`을 사용하면 됩니다. Yury Khrustalev는 [이름 상당수가 지나치게 축약되어 있다](https://lwn.net/ml/all/auMy3ivznxmfrxGN@arm.com/)고 보고, `allow_textrel`처럼 더 긴 이름이 명확할 수 있다고 제안했습니다. Zanella는 다음 패치 세트 버전에서 이름을 더 길게 바꾸는 데 [동의했습니다](https://lwn.net/ml/all/32f676ef-73bc-493b-8aa3-617d035dffd4@linaro.org/).

변경 사항 자체에 대한 의견은 많지 않았습니다. 대부분은 배포판이 큰 혼란 없이 활성화할 수 있을 것으로 보입니다. 특히 이미 위치 독립 실행 파일을 기본으로 활성화하는 배포판은 배포판 패키지에 영향을 주지 않고 이 tunable들을 활성화할 수 있습니다. 더 어려운 문제는 배포판 외부에서 빌드한 실행 파일에서 생길 것입니다. 이 tunable들이 널리 도입되는 것이 Node.js 같은 프로젝트가 위치 의존 코드를 포기할 동기가 되지 않는다면, 사용자는 tunable들이 바로 그 대상으로 삼고 있는 프로그램을 실행하기 위해 해당 tunable을 비활성화해야 할 수도 있습니다.

### 옮긴이 해설

[^f1105134-aslr]: ASLR은 메모리 배치를 예측하기 어렵게 만드는 완화 기법이지 buffer overflow 자체를 수정하는 기능은 아닙니다. 여기서 “ASLR을 활성화할 수 없다”는 설명은 특히 주 실행 파일 코드의 배치에 관한 맥락입니다. non-PIE 프로그램이라고 해서 stack이나 공유 라이브러리 등 모든 영역의 무작위화가 반드시 사라지는 것은 아닙니다.

[^f1105134-pie]: PIC(position-independent code)는 특정 고정 주소에 묶이지 않도록 생성한 코드이고, PIE(position-independent executable)는 이를 이용해 실행 파일 자체를 여러 주소에 로드할 수 있게 만든 형태입니다. 공유 라이브러리의 PIC와 주 실행 파일의 PIE는 관련된 개념이지만 같은 용어는 아닙니다. 성능 비용은 architecture, compiler, workload에 따라 달라지므로 본문의 Node.js 측정치를 모든 프로그램에 일반화해서는 안 됩니다.

[^f1105134-elf]: ELF(Executable and Linkable Format)는 Linux에서 실행 파일과 공유 객체 등에 사용하는 파일 형식입니다. 동적 실행 파일에는 보통 사용할 interpreter, 즉 dynamic linker를 지정하는 `PT_INTERP` 항목이 있습니다. dynamic linker는 필요한 공유 라이브러리를 로드하고 symbol 및 relocation을 처리한 뒤 프로그램 실행을 넘깁니다. 일반적인 non-PIE 실행 파일은 `ET_EXEC`, PIE는 `ET_DYN` 형식을 사용하지만, `ET_DYN`은 공유 라이브러리에도 쓰이므로 그 값 하나만으로 PIE라고 단정할 수는 없습니다.

[^f1105134-textrel]: Relocation은 로드 주소나 외부 symbol의 실제 위치에 맞춰 주소 참조 등을 보정하는 작업입니다. Text relocation은 보통 읽기·실행 전용으로 유지하고 싶은 코드 영역 등에 수정을 요구하므로, 로딩 과정의 메모리 권한 관리와 보안 강화를 어렵게 만듭니다. ELF의 section은 링크 관점의 구획이고, segment는 실행 시 메모리에 매핑하는 구획이므로 두 용어를 구별해 읽는 것이 좋습니다.

[^f1105134-stack]: W+X는 같은 메모리 영역을 쓰기 가능(writable)하면서 실행 가능(executable)하게 두는 것을 뜻합니다. Executable stack도 쓰기 가능한 stack에서 코드를 실행하게 한다는 점에서 관련된 보안 문제이며, ELF에서는 보통 `PT_GNU_STACK`의 권한 표시로 stack 실행 필요 여부를 전달합니다. 다만 stack의 실행 권한과 일반적인 로드 segment의 W+X 여부는 구분되는 검사 대상입니다. 이 기사만으로 제안된 `wx_segments` 옵션이 executable stack의 모든 경우까지 금지한다고 해석해서는 안 됩니다. 또한 반환 주소를 덮어쓰는 공격이 반드시 stack에 새 코드를 넣고 실행하는 방식인 것은 아닙니다. 기존 코드를 재사용하는 공격도 있어 non-executable stack만으로 충분하지 않습니다.

[^f1105134-binding]: GOT(global offset table)는 외부 함수나 데이터의 실제 주소를 간접 참조하는 데 쓰이는 테이블입니다. Lazy binding은 함수 주소 해석을 첫 호출 시점까지 미루는 방식이고, 즉시 binding은 시작 단계에서 처리합니다. `LD_BIND_NOW`나 `-z now`는 이 지연을 없애며, 시작 비용 및 GOT 보호 시점과 관련됩니다.

[^f1105134-rpath]: RPATH/RUNPATH는 ELF 객체에 포함할 수 있는 라이브러리 검색 경로 정보입니다. 상대 경로는 실행 시점의 디렉터리 등 주변 환경에 따라 다른 라이브러리를 선택하게 할 수 있어, 공격자가 제어하는 파일을 잘못 로드할 위험과 연결됩니다. 본문의 옵션은 이런 상대 경로 기반 검색을 제한하려는 것입니다.

[^f1105134-relro]: RELRO는 relocation 처리가 끝난 뒤 더 이상 변경할 필요가 없는 일부 영역을 읽기 전용으로 바꾸는 보호 방식입니다. 일반적으로 `-z relro`와 즉시 binding을 지정하는 `-z now`를 함께 사용하면 지연 binding을 위해 GOT의 일부를 계속 쓰기 가능하게 남겨 둘 필요가 없어져 이른바 full RELRO 구성이 가능합니다. 본문의 `{1,2}`는 두 설정값을 나열한 표기이며, shell에서 중괄호를 포함해 그대로 입력하라는 뜻은 아닙니다.


---

# LWN 단신·뉴스레터·행사 요약

> **범위 안내:** 원문의 재배포 라이선스를 확인하지 않았으므로 전문 번역 대신, 각 단신의 사실관계를 독립적으로 서술한 짧은 한국어 다이제스트를 제공합니다. 인용문도 요지를 풀어 썼습니다. 뉴스레터는 제공된 원문에 제목·발행일·링크만 있으므로 그 범위의 안내만 작성했으며, 링크된 본문을 읽은 것처럼 요약하지 않았습니다. 날짜·버전·행사 정보는 제공된 원문 기준이며 현재 상태를 별도로 검증하지 않았습니다. 댓글·페이지 편집자 표기는 제외했습니다.

## 보안

### [Critical security vulnerability affects OpenSSH on Alpine Linux systems](https://lwn.net/Articles/1105464/)
#### Alpine Linux 등의 OpenSSH 취약점과 완화 조치
**요약**
- OpenSSH [10.6p2](https://openssh.com/releasenotes.html#10.6p2)가 PAM 없이 [musl libc](https://musl.libc.org/)를 사용하는 Linux 환경의 심각한 취약점에 대응하는 우회 조치를 담았다.[^briefs-pam]
- Damien Miller의 [당시 공지](https://hachyderm.io/@damienmiller/117563026759098135)는 해당 시스템의 암호 인증을 `PasswordAuthentication=no`로 끄거나 SSH를 중단하라고 경고했다. 비 Linux, glibc 기반 Linux, 암호 인증에 PAM을 쓰는 Linux는 영향 대상이 아니라고 설명했다.
- [Alpine Linux](https://www.alpinelinux.org/)는 수정 사항을 [2022년 5월 출시된 3.16](https://alpinelinux.org/posts/alpine-3.16.0-released/)까지 [소급 적용하겠다고 발표](https://fosstodon.org/@alpinelinux/117563196640515820)했다.[^briefs-backport]

### [Security quote of the week](https://lwn.net/Articles/1106528/)
#### 소규모 프로젝트의 보안 공지를 어렵게 하는 CVE 절차
**요약**
- John Goerzen은 C-Kermit에서 [취약점들을 발견](https://www.openwall.com/lists/oss-security/2026/11/02/1)했으며, 하나는 1984년까지 거슬러 올라간다고 설명했다.
- [그의 글](https://changelog.complete.org/archives/45097-the-large-project-bias-of-cves)은 소규모 독립 프로젝트가 CVE를 포함한 보안 권고문을 내기 어렵다는 경험을 전한다.[^briefs-cve]
- 대형 기관에 유리한 공지 체계가 작은 프로젝트의 신속한 정보 공개를 위축시키고 사용자에게도 도움이 되지 않는다는 비판이다.

## 커널 개발

### [Kernel release status](https://lwn.net/Articles/1106904/)
#### 커널 7.4 개발판과 안정판 업데이트
**요약**
- 7.4-rc2가 [11월 9일 공개](https://lwn.net/Articles/1106300/)되었으며, 원문은 7.4 정식판이 새해 무렵 완성될 것으로 전망했다.[^briefs-rc]
- 안정판 [7.3.4](https://lwn.net/Articles/1106570/), [6.18.63](https://lwn.net/Articles/1106571/), [6.12.117](https://lwn.net/Articles/1106572/), [6.6.162](https://lwn.net/Articles/1105906/), [6.1.192](https://lwn.net/Articles/1105907/), [5.15.225](https://lwn.net/Articles/1105908/), [5.10.274](https://lwn.net/Articles/1105909/)가 나왔다.
- 출시 직후 발견된 문제 때문에 같은 주에 수정판이 잇따랐으며, 모든 안정판 계열에 평소보다 많은 패치가 백포트되었다.

## 배포판

### [Amutable Foundations: A Technical Overview](https://lwn.net/Articles/1105934/)
#### Amutable 운영체제의 이미지 중심 보안 설계
**요약**
- Lennart Poettering, Michael Vogt, Joaquim Rocha가 AOS와 관련 기반 시설의 [기술 개요](https://amutable.com/blog/amutable-foundations-technical-overview)를 발표했다.
- 기본 설치에서 셸·SSH·Python이나 Perl 같은 인터프리터를 빼, 노드에 불필요한 실행 경로와 공격 가능성을 줄이는 구상이다.
- 이미지 기반 설계를 통해 보안 속성을 강제하며, Verity 키링에 등록된 키로 검증할 수 있는 서명된 Verity 데이터를 갖춘 이미지만 활성화한다.[^briefs-verity]

### [Asahi Linux 7.3 progress report](https://lwn.net/Articles/1105936/)
#### Asahi Linux의 개발 보고와 라이선스 전환 방침
**요약**
- Apple 기기용 Linux를 개발하는 Asahi Linux가 [7.3 진행 보고서](https://asahilinux.org/2026/11/progress-report-7-3/)를 공개했다.
- 개발진은 개인 포크의 개발 중 코드를 무단 출처 생략이나 LLM 재작성으로 가져가 프로젝트를 대체·수익화하려는 사례가 있었다고 주장했다.
- 이를 계기로 모든 저장소를 GPL 버전 2 이상으로 옮기는 절차를 시작하며, 앞으로 강한 카피레프트 라이선스만 쓰겠다는 방침을 밝혔다.[^briefs-copyleft]

### [OpenIndiana 2026.10 released](https://lwn.net/Articles/1106285/)
#### OpenIndiana 2026.10 공개
**요약**
- [OpenIndiana](https://docs.openindiana.org/misc/openindiana/)의 [2026.10 버전](https://openindiana.org/announcements/openindiana-hipster-2026-10-announcement/)이 출시되었다.
- 이 운영체제는 [illumos](https://en.wikipedia.org/wiki/Illumos) 기반이며, 그 계보는 Oracle이 중단한 [OpenSolaris](https://en.wikipedia.org/wiki/OpenSolaris)로 이어진다.
- 라이브 이미지의 UEFI 프레임버퍼 지원, 응용 프로그램·개발 도구 업데이트, TeX Live 2026과 Foliate 전자책 리더 등의 추가가 주요 변경점이다.

## 개발

### [Firefox 160 released](https://lwn.net/Articles/1106542/)
#### Firefox 160의 미디어·창 기능 개선
**요약**
- [Firefox 160](https://www.firefox.com/en-US/firefox/160.0/releasenotes/)이 출시되었으며, 사이트의 `mailto:` 링크 처리 요청을 차단할 수 있게 되었다.
- FLAC·MP3·PCM 오디오를 포함한 Matroska 파일 재생과 [화면 속 화면](https://support.mozilla.org/kb/about-picture-picture-firefox) 플레이어의 재생 속도 조절을 지원한다.
- 초기 개발 단계의 [Mini Window 기능](https://connect.mozilla.org/t5/discussions/mini-window-beta-is-going-live-in-firefox-160-and-we-want-your/m-p/144137#M59048)도 소개되었다.

### [Videos from XDC 2026 are available](https://lwn.net/Articles/1105913/)
#### XDC 2026 발표 영상 공개
**요약**
- [2026 X.Org Developers Conference](https://indico.freedesktop.org/event/12/)(XDC)의 발표 영상이 공개되었다.
- 행사는 9월 28~30일 캐나다 온타리오주 토론토에서 열렸다.
- 발표 영상은 [X.Org Foundation의 YouTube 채널](https://www.youtube.com/@XOrgFoundation/videos)에서 볼 수 있다.

### [Zellij 0.46 released](https://lwn.net/Articles/1106903/)
#### Zellij 0.46, 데스크톱 터미널 기능 추가
**요약**
- 터미널 작업 공간 도구 [Zellij](https://zellij.dev/)의 [0.46 버전](https://github.com/zellij-org/zellij/releases/tag/v0.46.0)이 출시되었다.
- `zellij terminal` 명령으로 Linux·Mac·Windows에서 데스크톱 터미널을 실행할 수 있으며, 기존 터미널 내부의 멀티플렉서 방식도 유지된다. 두 방식의 세션은 공유할 수 있다.[^briefs-multiplexer]
- GUI 설정 화면, 세션 미리 보기, 오른쪽 클릭 메뉴가 추가되었다. 자세한 내용은 [기능 안내](https://zellij.dev/news/terminal-inbox-session-previews/)에 있다.

### [Development quotes of the week](https://lwn.net/Articles/1106071/)
#### 소프트웨어 수정의 자유와 운동의 목표에 관한 견해
**요약**
- [Luis Villa](https://lu.is/2026/11/what-ride-specifically/)는 프로그램을 이해하고 원하는 대로 고치는 [자유 1](https://www.gnu.org/philosophy/free-sw.html)이 법적 권리뿐 아니라 실질적 능력이 되는 데 의미를 두었다.
- 그는 빌드·코드 탐색·패치 유지의 장벽과 대비해, 자신이 GNOME과 [phanpy](https://github.com/cheeaun/phanpy)를 크게 수정해 사용하는 경험을 사례로 들었다.
- 별도의 발언에서 [Eli Zaretskii](https://lwn.net/ml/all/86mrrmknn7.fsf@gnu.org/)는 자유 소프트웨어 운동의 목표를 인류 전체의 포괄적 자유라는 표현과 동일시해서는 안 된다고 선을 그었다.

## 기타

### [In Memoriam: Tim Peters 1952–2026](https://lwn.net/Articles/1106901/)
#### Tim Peters를 추모하며
**요약**
- Guido van Rossum이 Tim Peters(1952–2026)의 별세 소식을 [뒤늦게 전했다](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028).
- Peters는 [PEP 20, Python의 선](https://peps.python.org/pep-0020/)의 저자로 알려졌으며, van Rossum은 그를 오랜 멘토이자 언어 공동 설계자로 기억했다.
- Python 초기부터 참여해 `int`와 `float`의 혼합 연산 지원을 설득하는 등 지속해서 언어 발전에 기여했다고 회고했다.

# 공지

## 뉴스레터

아래는 원문이 제공한 발행 정보의 간단한 안내입니다. 각 링크의 본문 내용은 제공되지 않았습니다. 월·일은 원문 표기를 유지했습니다.

### 배포판·시스템 관리

- [Asahi Linux Progress Report](https://asahilinux.org/2026/11/progress-report-7-3/) — 11월 7일. Asahi Linux 진행 보고.
- [DistroWatch Weekly](https://distrowatch.com/weekly.php?issue=20261109) — 11월 9일. 배포판 주간 소식.
- [This week in F-Droid](https://f-droid.org/en/2026/11/09/twif.html) — 11월 9일. F-Droid 주간 소식.
- [This week in Fedora](https://abompard.fedorapeople.org/twif/2026/11-02-to-11-08/) — 11월 9일. Fedora 주간 소식.
- [openSUSE Tumbleweed Review of the Week](https://dominique.leuenberger.net/blog/2026/11/tumbleweed-review-of-the-week-2026-45/) — 11월 6일. Tumbleweed 한 주 돌아보기.
- [Ubuntu Weekly News](https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-issue-969/90896) — 11월 2일. Ubuntu 주간 소식.

### 개발

- [Emacs News](https://sachachua.com/blog/2026/11/2026-11-09-emacs-news/) — 11월 9일. Emacs 소식.
- [What's cooking in git.git](https://lwn.net/Articles/1105468/) — 11월 4일. Git 개발 진행 소식.
- [What's cooking in git.git](https://lwn.net/Articles/1105978/) — 11월 6일. Git 개발 진행 소식.
- [What's cooking in git.git](https://lwn.net/Articles/1106567/) — 11월 10일. Git 개발 진행 소식.
- [This Week in GNOME](https://thisweek.gnome.org/posts/2026/11/twig-273/) — 11월 7일. GNOME 주간 소식.
- [Golang Weekly](https://golangweekly.com/issues/623) — 11월 6일. Go 주간 소식.
- [Last Week in Kubernetes Development](https://lwkd.info/2026/20261107) — 11월 7일. Kubernetes 개발 주간 소식.
- [LLVM Weekly](https://llvmweekly.org/issue/671) — 11월 9일. LLVM 주간 소식.
- [This Week in Matrix](https://matrix.org/blog/2026/11/06/this-week-in-matrix-2026-11-06/) — 11월 6일. Matrix 주간 소식.
- [OCaml Weekly News](https://lwn.net/Articles/1106359/) — 11월 10일. OCaml 주간 소식.
- [This Week in Plasma](https://blogs.kde.org/2026/11/07/this-week-in-plasma-widgets-widgets-widgets/) — 11월 7일. Plasma 주간 소식.
- [This week in the Perl Steering Committee](https://blogs.perl.org/users/psc/2026/11/this-week-in-psc-242-2026-11-09.html) — 11월 9일. Perl 운영위원회 주간 소식.
- [Perl Weekly](http://perlweekly.com/archive/798.html) — 11월 9일. Perl 주간 소식.
- [PyCoder's Weekly](https://pycoders.com/issues/760) — 11월 10일. Python 개발자 대상 주간 소식.
- [Python Core Dispatch](https://coredispatch.xyz/editions/12) — 11월 7일. Python 핵심 개발 소식.
- [Weekly Rakudo News](https://rakuweekly.blog/2026/11/09/2026-45-general-koan/) — 11월 9일. Rakudo 주간 소식.
- [Ruby Weekly News](https://rubyweekly.com/issues/825) — 11월 5일. Ruby 주간 소식.
- [This Week in Rust](https://this-week-in-rust.org/blog/2026/11/04/this-week-in-rust-676/) — 11월 4일. Rust 주간 소식.
- [September in Servo](https://servo.org/blog/2026/11/05/september-in-servo/) — 11월 5일. Servo의 9월 활동 보고.
- [Wikimedia Tech News](https://meta.wikimedia.org/wiki/Special:FeedItem/technews/20261109000000/en) — 11월 9일. Wikimedia 기술 소식.

### 회의록

- [openSUSE board meeting minutes](https://lwn.net/Articles/1105701/) — 10월 26일. openSUSE 이사회 회의록.

## 발표 제안 모집

### CFP 마감: 2026년 11월 12일~2027년 1월 11일

출처: [LWN.net CFP 달력](https://lwn.net/Calendar/Monthly/cfp/).[^briefs-cfp]

| 마감일 | 행사 날짜 | 행사 | 장소 |
| --- | --- | --- | --- |
| 12월 20일 | 2월 1일 | [OpenEmbedded Workshop 2027](https://pretalx.com/openembedded-workshop-2027/cfp) | 벨기에 브뤼셀 |
| 1월 4일 | 3월 20일~21일 | [Chemnitzer Linux Tage 2027](https://chemnitzer.linux-tage.de/2027/en/programm/call-for-lectures) | 독일 켐니츠 |

목록에 없는 행사의 CFP 정보는 [LWN 등록 양식](https://lwn.net/Calendar/new/)으로 알릴 수 있습니다.

## 예정 행사

### 행사 목록: 2026년 11월 12일~2027년 1월 11일

출처: [LWN.net 행사 달력](https://lwn.net/Calendar/). 다음은 원문 발행 시점의 일정이며, 오늘 기준의 예정 행사만을 뜻하지는 않습니다.

| 날짜 | 행사 | 장소 |
| --- | --- | --- |
| 11월 12일~13일 | [Ubuntu Summit 26.10](https://ubuntu.com/summit) | 온라인 |
| 11월 12일~13일 | [KVM Forum](https://kvm-forum.qemu.org/) | 캐나다 밴쿠버 |
| 11월 14일~15일 | [Capitole du Libre 2026](https://capitoledulibre.org/) | 프랑스 툴루즈 |
| 11월 17일~19일 | [Open Source Monitoring Conference](https://osmc.de/) | 독일 뉘른베르크 |
| 11월 20일~21일 | [OLF Conference](https://olfconference.org/) | 미국 오하이오주 콜럼버스 |
| 11월 21일 | [LocHal Open Source Event 2026](https://linuxeducatie.nl/index.php/open-source-event-2026/) | 네덜란드 틸뷔르흐 |
| 11월 28일 | [FOSS for All Conference 2026](https://2026.fossforall.org) | 대한민국 서울 |
| 12월 1일~3일 | [Yocto Project Virtual Summit 2026.12](https://www.yoctoproject.org/event/virtual-summit-2026-12/) | 온라인, 온라인(원문 표기) |
| 12월 7일~9일 | [Open Source Summit Japan](https://events.linuxfoundation.org/open-source-summit-japan/) | 일본 도쿄 |

목록에 없는 행사 정보는 [LWN 등록 양식](https://lwn.net/Calendar/new/)으로 알릴 수 있습니다.

## 용어 해설

[^briefs-pam]: PAM은 응용 프로그램이 공통 인증 모듈을 이용하도록 하는 체계입니다. 여기서 취약점의 적용 범위는 Linux 여부뿐 아니라 libc 종류와 암호 인증 경로의 조합으로 구분됩니다.
[^briefs-backport]: 백포트는 새로운 버전의 수정 사항을 이전 버전 계열에도 적용하는 작업입니다. 본문의 계획 발표가 해당 구버전의 일반 지원 기간 연장까지 뜻하는 것은 아닙니다.
[^briefs-cve]: CVE는 공개된 보안 취약점을 공통 식별자로 참조하는 체계입니다. 식별자 발급과 실제 수정 배포는 별개의 절차입니다.
[^briefs-rc]: rc는 정식 출시 후보(release candidate)입니다. 원문의 완성 시점은 당시의 전망이지 확정 출시일이 아닙니다.
[^briefs-verity]: 이 문맥의 Verity 데이터와 서명은 이미지 무결성과 승인된 서명 키를 바탕으로 활성화 대상을 제한하는 장치입니다. 서명만으로 이미지 내부의 모든 보안 결함이 사라지는 것은 아닙니다.
[^briefs-copyleft]: 카피레프트는 파생물을 배포할 때 소스와 라이선스에 관한 의무를 부과하는 방식입니다. 재사용 자체를 일률적으로 금지한다는 뜻은 아니며, 본문은 프로젝트가 발표한 전환 방침을 요약합니다.
[^briefs-multiplexer]: 터미널 멀티플렉서는 하나의 터미널 안에서 여러 창·패널·세션을 관리하는 도구입니다. Zellij의 새 데스크톱 실행 방식은 기존 내부 실행 방식을 대체하지 않습니다.
[^briefs-cfp]: CFP(Call for Presentations)는 발표 제안 모집입니다. 표의 마감일과 실제 행사 날짜는 서로 다르며, 원문의 행별 날짜에는 연도가 생략되어 있어 여기서도 월·일만 유지했습니다.


---

## 보안 업데이트 — Security updates

### 요약
- 원문 공지 기간은 2026년 11월 5일부터 11월 11일까지입니다.
- 아래 표의 배포판, 공지 ID, 릴리스, 패키지, 날짜 및 링크는 원문 데이터 그대로 보존합니다.
- 같은 패키지도 배포판·지원 릴리스별 수정 버전이 다르므로 실제 배포판의 공지를 확인해야 합니다.[^security-operations]

원문: https://lwn.net/Articles/1106885/

| 배포판 | 공지 ID | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:95570](https://lwn.net/Articles/1105751/) | 10 | cockpit-files | 2026-11-06 |
| AlmaLinux | [ALSA-2022:7822](https://lwn.net/Articles/1105752/) | 8 | container-tools:rhel8 | 2026-11-05 |
| AlmaLinux | [ALSA-2026:96092](https://lwn.net/Articles/1106364/) | 10 | curl | 2026-11-09 |
| AlmaLinux | [ALSA-2026:95519](https://lwn.net/Articles/1105754/) | 10 | delve | 2026-11-06 |
| AlmaLinux | [ALSA-2026:95518](https://lwn.net/Articles/1105753/) | 9 | delve | 2026-11-06 |
| AlmaLinux | [ALSA-2026:96083](https://lwn.net/Articles/1106365/) | 8 | dpdk | 2026-11-09 |
| AlmaLinux | [ALSA-2026:94629](https://lwn.net/Articles/1105501/) | 9 | dpdk | 2026-11-05 |
| AlmaLinux | [ALSA-2026:96240](https://lwn.net/Articles/1106738/) | 10 | edk2 | 2026-11-10 |
| AlmaLinux | [ALSA-2023:2873](https://lwn.net/Articles/1105755/) | 8 | gcc-toolset-12-binutils | 2026-11-05 |
| AlmaLinux | [ALSA-2026:95482](https://lwn.net/Articles/1105756/) | 8 | gimp:2.8 | 2026-11-05 |
| AlmaLinux | [ALSA-2026:96087](https://lwn.net/Articles/1106366/) | 8 | glibc | 2026-11-10 |
| AlmaLinux | [ALSA-2026:95618](https://lwn.net/Articles/1105757/) | 9 | glibc | 2026-11-06 |
| AlmaLinux | [ALSA-2026:95638](https://lwn.net/Articles/1105758/) | 8 | go-toolset:rhel8 | 2026-11-06 |
| AlmaLinux | [ALSA-2023:0852](https://lwn.net/Articles/1105502/) | 8 | httpd:2.4 | 2026-11-05 |
| AlmaLinux | [ALSA-2026:95367](https://lwn.net/Articles/1105760/) | 10 | kernel | 2026-11-05 |
| AlmaLinux | [ALSA-2026:93413](https://lwn.net/Articles/1106368/) | 10 | kernel | 2026-11-10 |
| AlmaLinux | [ALSA-2026:95212](https://lwn.net/Articles/1105503/) | 8 | kernel | 2026-11-04 |
| AlmaLinux | [ALSA-2026:95370](https://lwn.net/Articles/1105759/) | 9 | kernel | 2026-11-05 |
| AlmaLinux | [ALSA-2026:93412](https://lwn.net/Articles/1106367/) | 9 | kernel | 2026-11-10 |
| AlmaLinux | [ALSA-2026:95100](https://lwn.net/Articles/1105504/) | 8 | kernel-rt | 2026-11-04 |
| AlmaLinux | [ALSA-2023:6431](https://lwn.net/Articles/1105761/) | 9 | libfastjson | 2026-11-05 |
| AlmaLinux | [ALSA-2023:5259](https://lwn.net/Articles/1105762/) | 8 | mariadb:10.3 | 2026-11-05 |
| AlmaLinux | [ALSA-2023:6940](https://lwn.net/Articles/1105763/) | 8 | mod\_auth\_openidc:2.3 | 2026-11-05 |
| AlmaLinux | [ALSA-2022:7119](https://lwn.net/Articles/1105505/) | 8 | mysql:8.0 | 2026-11-05 |
| AlmaLinux | [ALSA-2024:0894](https://lwn.net/Articles/1105764/) | 8 | mysql:8.0 | 2026-11-05 |
| AlmaLinux | [ALSA-2023:3087](https://lwn.net/Articles/1105765/) | 8 | mysql:8.0 | 2026-11-05 |
| AlmaLinux | [ALSA-2026:96236](https://lwn.net/Articles/1106369/) | 10 | nodejs-nodemon | 2026-11-10 |
| AlmaLinux | [ALSA-2026:96094](https://lwn.net/Articles/1106370/) | 10 | nodejs22 | 2026-11-10 |
| AlmaLinux | [ALSA-2026:96088](https://lwn.net/Articles/1106371/) | 10 | nodejs24 | 2026-11-10 |
| AlmaLinux | [ALSA-2023:4536](https://lwn.net/Articles/1106372/) | 8 | nodejs:18 | 2026-11-09 |
| AlmaLinux | [ALSA-2026:96234](https://lwn.net/Articles/1106373/) | 9 | nodejs:22 | 2026-11-10 |
| AlmaLinux | [ALSA-2026:96215](https://lwn.net/Articles/1106374/) | 8 | patch | 2026-11-10 |
| AlmaLinux | [ALSA-2023:2903](https://lwn.net/Articles/1105506/) | 8 | php:7.4 | 2026-11-05 |
| AlmaLinux | [ALSA-2022:7624](https://lwn.net/Articles/1105507/) | 8 | php:8.0 | 2026-11-05 |
| AlmaLinux | [ALSA-2023:0848](https://lwn.net/Articles/1105766/) | 8 | php:8.0 | 2026-11-05 |
| AlmaLinux | [ALSA-2022:7470](https://lwn.net/Articles/1105767/) | 8 | pki-core:10.6 and pki-deps:10.6 | 2026-11-05 |
| AlmaLinux | [ALSA-2022:7482](https://lwn.net/Articles/1105508/) | 8 | qt5 | 2026-11-05 |
| AlmaLinux | [ALSA-2023:6369](https://lwn.net/Articles/1106375/) | 9 | qt5 | 2026-11-09 |
| AlmaLinux | [ALSA-2026:96075](https://lwn.net/Articles/1106376/) | 8 | qt5-qtdeclarative | 2026-11-10 |
| AlmaLinux | [ALSA-2026:96235](https://lwn.net/Articles/1106378/) | 10 | ruby | 2026-11-10 |
| AlmaLinux | [ALSA-2026:96067](https://lwn.net/Articles/1106377/) | 9 | ruby | 2026-11-09 |
| AlmaLinux | [ALSA-2026:96233](https://lwn.net/Articles/1106379/) | 10 | ruby4.0 | 2026-11-09 |
| AlmaLinux | [ALSA-2022:6447](https://lwn.net/Articles/1105509/) | 8 | ruby:2.7 | 2026-11-05 |
| AlmaLinux | [ALSA-2022:6450](https://lwn.net/Articles/1105510/) | 8 | ruby:3.0 | 2026-11-05 |
| AlmaLinux | [ALSA-2026:96068](https://lwn.net/Articles/1106380/) | 9 | ruby:3.3 | 2026-11-09 |
| AlmaLinux | [ALSA-2026:96120](https://lwn.net/Articles/1106381/) | 9 | ruby:4.0 | 2026-11-09 |
| AlmaLinux | [ALSA-2023:7668](https://lwn.net/Articles/1105768/) | 8 | squid:4 | 2026-11-06 |
| AlmaLinux | [ALSA-2026:96078](https://lwn.net/Articles/1106382/) | 8 | squid:4 | 2026-11-09 |
| AlmaLinux | [ALSA-2023:7022](https://lwn.net/Articles/1105769/) | 8 | tang | 2026-11-05 |
| AlmaLinux | [ALSA-2026:95085](https://lwn.net/Articles/1105770/) | 10 | tesseract | 2026-11-05 |
| AlmaLinux | [ALSA-2026:95725](https://lwn.net/Articles/1105771/) | 8 | tesseract | 2026-11-06 |
| AlmaLinux | [ALSA-2026:95086](https://lwn.net/Articles/1105511/) | 9 | tesseract | 2026-11-05 |
| AlmaLinux | [ALSA-2025:2900](https://lwn.net/Articles/1105772/) | 8 | thunderbird | 2026-11-06 |
| AlmaLinux | [ALSA-2026:92862](https://lwn.net/Articles/1106383/) | 10 | tomcat | 2026-11-10 |
| AlmaLinux | [ALSA-2026:96212](https://lwn.net/Articles/1106384/) | 8 | util-linux | 2026-11-09 |
| AlmaLinux | [ALSA-2023:0099](https://lwn.net/Articles/1105773/) | 8 | virt:rhel and virt-devel:rhel | 2026-11-05 |
| AlmaLinux | [ALSA-2026:96080](https://lwn.net/Articles/1106385/) | 8 | webkit2gtk3 | 2026-11-09 |
| AlmaLinux | [ALSA-2026:95194](https://lwn.net/Articles/1105512/) | 9 | webkit2gtk3 | 2026-11-05 |
| AlmaLinux | [ALSA-2026:95281](https://lwn.net/Articles/1105513/) | 8 | xorg-x11-server-Xwayland | 2026-11-04 |
| Debian | [DLA-4882-1](https://lwn.net/Articles/1105774/) | LTS | chromium | 2026-11-05 |
| Debian | [DLA-4887-1](https://lwn.net/Articles/1106116/) | LTS | cjose | 2026-11-07 |
| Debian | [DSA-6611-1](https://lwn.net/Articles/1105514/) | stable | imagemagick | 2026-11-04 |
| Debian | [DSA-6616-1](https://lwn.net/Articles/1106117/) | stable | kernel | 2026-11-08 |
| Debian | [DSA-6615-1](https://lwn.net/Articles/1106118/) | stable | libreoffice | 2026-11-07 |
| Debian | [DLA-4883-1](https://lwn.net/Articles/1105775/) | LTS | ntfs-3g | 2026-11-05 |
| Debian | [DSA-6618-1](https://lwn.net/Articles/1106739/) | stable | openexr | 2026-11-11 |
| Debian | [DLA-4884-1](https://lwn.net/Articles/1105776/) | LTS | puppet-agent | 2026-11-05 |
| Debian | [DSA-6608-1](https://lwn.net/Articles/1105515/) | stable | puppet-agent | 2026-11-04 |
| Debian | [DLA-4888-1](https://lwn.net/Articles/1106119/) | LTS | rsync | 2026-11-09 |
| Debian | [DLA-4891-1](https://lwn.net/Articles/1106740/) | LTS | rsyslog | 2026-11-11 |
| Debian | [DSA-6614-1](https://lwn.net/Articles/1106120/) | stable | ruby3.3 | 2026-11-07 |
| Debian | [DLA-4890-1](https://lwn.net/Articles/1106741/) | LTS | srt | 2026-11-10 |
| Debian | [DSA-6612-1](https://lwn.net/Articles/1105516/) | stable | symfony | 2026-11-04 |
| Debian | [DSA-6617-1](https://lwn.net/Articles/1106386/) | stable | symfony | 2026-11-09 |
| Debian | [DLA-4886-1](https://lwn.net/Articles/1106121/) | LTS | telegram-desktop | 2026-11-09 |
| Debian | [DLA-4889-1](https://lwn.net/Articles/1106387/) | LTS | tomcat10 | 2026-11-09 |
| Debian | [DLA-4885-1](https://lwn.net/Articles/1105777/) | LTS | trapperkeeper-authorization-clojure | 2026-11-05 |
| Debian | [DSA-6609-1](https://lwn.net/Articles/1105517/) | stable | trapperkeeper-authorization-clojure | 2026-11-04 |
| Debian | [DSA-6600-2](https://lwn.net/Articles/1106122/) | stable | vim | 2026-11-08 |
| Debian | [DLA-4881-1](https://lwn.net/Articles/1105519/) | LTS | xen | 2026-11-04 |
| Debian | [DSA-6610-1](https://lwn.net/Articles/1105518/) | stable | xen | 2026-11-04 |
| Debian | [DSA-6613-1](https://lwn.net/Articles/1106123/) | stable | zlib | 2026-11-07 |
| Fedora | [FEDORA-2026-540af356f2](https://lwn.net/Articles/1105520/) | F43 | 3proxy | 2026-11-05 |
| Fedora | [FEDORA-2026-1b5ddbaeb5](https://lwn.net/Articles/1105522/) | F44 | 3proxy | 2026-11-05 |
| Fedora | [FEDORA-2026-1f4dd1b9ff](https://lwn.net/Articles/1105521/) | F45 | 3proxy | 2026-11-05 |
| Fedora | [FEDORA-2026-25e88abcc9](https://lwn.net/Articles/1106165/) | F45 | NetworkManager-l2tp | 2026-11-09 |
| Fedora | [FEDORA-2026-95362fedd2](https://lwn.net/Articles/1106743/) | F44 | alertmanager | 2026-11-11 |
| Fedora | [FEDORA-2026-9028005172](https://lwn.net/Articles/1106742/) | F45 | alertmanager | 2026-11-11 |
| Fedora | [FEDORA-2026-cf9d4ec5e6](https://lwn.net/Articles/1106388/) | F44 | bind | 2026-11-10 |
| Fedora | [FEDORA-2026-468290e984](https://lwn.net/Articles/1105523/) | F45 | bind | 2026-11-05 |
| Fedora | [FEDORA-2026-7198802985](https://lwn.net/Articles/1106124/) | F45 | bind | 2026-11-09 |
| Fedora | [FEDORA-2026-468290e984](https://lwn.net/Articles/1105524/) | F45 | bind-dyndb-ldap | 2026-11-05 |
| Fedora | [FEDORA-2026-f2a72b9a61](https://lwn.net/Articles/1106125/) | F43 | composer | 2026-11-08 |
| Fedora | [FEDORA-2026-0fac5fe7fe](https://lwn.net/Articles/1106126/) | F44 | composer | 2026-11-08 |
| Fedora | [FEDORA-2026-4d013a5c67](https://lwn.net/Articles/1106128/) | F44 | copyparty | 2026-11-09 |
| Fedora | [FEDORA-2026-a7d1759884](https://lwn.net/Articles/1106127/) | F45 | copyparty | 2026-11-09 |
| Fedora | [FEDORA-2026-f2ecc7c470](https://lwn.net/Articles/1105525/) | F45 | curl | 2026-11-05 |
| Fedora | [FEDORA-2026-c36b5fc4ca](https://lwn.net/Articles/1105526/) | F45 | dhcpcd | 2026-11-05 |
| Fedora | [FEDORA-2026-5879bc27e1](https://lwn.net/Articles/1106389/) | F43 | dnf5 | 2026-11-10 |
| Fedora | [FEDORA-2026-97ca946ad2](https://lwn.net/Articles/1106129/) | F44 | dnf5 | 2026-11-08 |
| Fedora | [FEDORA-2026-3a916dbb6c](https://lwn.net/Articles/1106746/) | F43 | dotnet11.0 | 2026-11-11 |
| Fedora | [FEDORA-2026-094b09b38e](https://lwn.net/Articles/1106745/) | F44 | dotnet11.0 | 2026-11-11 |
| Fedora | [FEDORA-2026-a2c4eee1ec](https://lwn.net/Articles/1106744/) | F45 | dotnet11.0 | 2026-11-11 |
| Fedora | [FEDORA-2026-f5e380a553](https://lwn.net/Articles/1106130/) | F43 | elixir | 2026-11-08 |
| Fedora | [FEDORA-2026-7be0823ab4](https://lwn.net/Articles/1106131/) | F44 | elixir | 2026-11-08 |
| Fedora | [FEDORA-2026-173435e952](https://lwn.net/Articles/1106132/) | F45 | elixir | 2026-11-08 |
| Fedora | [FEDORA-2026-85312f9b13](https://lwn.net/Articles/1105528/) | F44 | erlang-jose | 2026-11-05 |
| Fedora | [FEDORA-2026-23264ef42e](https://lwn.net/Articles/1105527/) | F45 | erlang-jose | 2026-11-05 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106133/) | F44 | fasterxml-oss-parent | 2026-11-08 |
| Fedora | [FEDORA-2026-53eede68af](https://lwn.net/Articles/1105529/) | F45 | forgejo | 2026-11-05 |
| Fedora | [FEDORA-2026-f40014e752](https://lwn.net/Articles/1105778/) | F45 | freerdp | 2026-11-06 |
| Fedora | [FEDORA-2026-dd82a0810d](https://lwn.net/Articles/1105530/) | F43 | freetype | 2026-11-05 |
| Fedora | [FEDORA-2026-a002fccd0d](https://lwn.net/Articles/1106747/) | F44 | gdal | 2026-11-11 |
| Fedora | [FEDORA-2026-29b06c5638](https://lwn.net/Articles/1106135/) | F44 | gnome-remote-desktop | 2026-11-09 |
| Fedora | [FEDORA-2026-898c0e2c77](https://lwn.net/Articles/1106134/) | F45 | gnome-remote-desktop | 2026-11-09 |
| Fedora | [FEDORA-2026-8121b4b9af](https://lwn.net/Articles/1106136/) | F43 | goose | 2026-11-07 |
| Fedora | [FEDORA-2026-ffdd457751](https://lwn.net/Articles/1105780/) | F44 | goose | 2026-11-06 |
| Fedora | [FEDORA-2026-5778d995b3](https://lwn.net/Articles/1105779/) | F45 | goose | 2026-11-06 |
| Fedora | [FEDORA-2026-d39bedb422](https://lwn.net/Articles/1105781/) | F45 | gpsd | 2026-11-06 |
| Fedora | [FEDORA-2026-2ef243ce94](https://lwn.net/Articles/1105784/) | F43 | hatch | 2026-11-06 |
| Fedora | [FEDORA-2026-01f9a44339](https://lwn.net/Articles/1105783/) | F44 | hatch | 2026-11-06 |
| Fedora | [FEDORA-2026-1168b946ef](https://lwn.net/Articles/1105782/) | F45 | hatch | 2026-11-06 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106137/) | F44 | jackson-annotations | 2026-11-08 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106138/) | F44 | jackson-bom | 2026-11-08 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106139/) | F44 | jackson-core | 2026-11-08 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106140/) | F44 | jackson-databind | 2026-11-08 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106141/) | F44 | jackson-jaxrs-providers | 2026-11-08 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106142/) | F44 | jackson-modules-base | 2026-11-08 |
| Fedora | [FEDORA-2026-b7ad391dd5](https://lwn.net/Articles/1106143/) | F44 | jackson-parent | 2026-11-08 |
| Fedora | [FEDORA-2026-765549feb9](https://lwn.net/Articles/1106144/) | F43 | java-21-openjdk | 2026-11-08 |
| Fedora | [FEDORA-2026-765549feb9](https://lwn.net/Articles/1106145/) | F43 | java-21-openjdk-portable | 2026-11-08 |
| Fedora | [FEDORA-2026-34aa0f144e](https://lwn.net/Articles/1106146/) | F44 | jupyterlab | 2026-11-07 |
| Fedora | [FEDORA-2026-1028a81d8a](https://lwn.net/Articles/1106390/) | F43 | kernel | 2026-11-10 |
| Fedora | [FEDORA-2026-0e28591060](https://lwn.net/Articles/1106392/) | F44 | kernel | 2026-11-10 |
| Fedora | [FEDORA-2026-655049a906](https://lwn.net/Articles/1106391/) | F45 | kernel | 2026-11-10 |
| Fedora | [FEDORA-2026-1028a81d8a](https://lwn.net/Articles/1106393/) | F43 | kernel-headers | 2026-11-10 |
| Fedora | [FEDORA-2026-0e28591060](https://lwn.net/Articles/1106395/) | F44 | kernel-headers | 2026-11-10 |
| Fedora | [FEDORA-2026-655049a906](https://lwn.net/Articles/1106394/) | F45 | kernel-headers | 2026-11-10 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106148/) | F43 | kryoptic | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106147/) | F44 | kryoptic | 2026-11-07 |
| Fedora | [FEDORA-2026-820191aab4](https://lwn.net/Articles/1105531/) | F45 | laszip | 2026-11-05 |
| Fedora | [FEDORA-2026-9616ace61b](https://lwn.net/Articles/1105532/) | F45 | libical | 2026-11-05 |
| Fedora | [FEDORA-2026-d657495ea3](https://lwn.net/Articles/1106397/) | F44 | libmodulemd | 2026-11-10 |
| Fedora | [FEDORA-2026-946f33e2c8](https://lwn.net/Articles/1106396/) | F45 | libmodulemd | 2026-11-10 |
| Fedora | [FEDORA-2026-f82738ad62](https://lwn.net/Articles/1105533/) | F45 | libmongocrypt | 2026-11-05 |
| Fedora | [FEDORA-2026-a00abaf169](https://lwn.net/Articles/1106149/) | F45 | luksmeta | 2026-11-08 |
| Fedora | [FEDORA-2026-183d3c32a6](https://lwn.net/Articles/1105534/) | F43 | markdownlint-cli2 | 2026-11-05 |
| Fedora | [FEDORA-2026-6215800886](https://lwn.net/Articles/1105536/) | F44 | markdownlint-cli2 | 2026-11-05 |
| Fedora | [FEDORA-2026-8f8cd892e5](https://lwn.net/Articles/1105535/) | F45 | markdownlint-cli2 | 2026-11-05 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106398/) | F45 | maturin | 2026-11-10 |
| Fedora | [FEDORA-2026-043f4fc6f5](https://lwn.net/Articles/1106150/) | F43 | mingw-cfitsio | 2026-11-09 |
| Fedora | [FEDORA-2026-a83294f5ab](https://lwn.net/Articles/1106151/) | F43 | mingw-expat | 2026-11-09 |
| Fedora | [FEDORA-2026-2e919836ea](https://lwn.net/Articles/1106152/) | F43 | mingw-freetype | 2026-11-09 |
| Fedora | [FEDORA-2026-14b302ef32](https://lwn.net/Articles/1106154/) | F43 | mingw-glib-networking | 2026-11-09 |
| Fedora | [FEDORA-2026-0d5f06ec53](https://lwn.net/Articles/1106153/) | F44 | mingw-glib-networking | 2026-11-09 |
| Fedora | [FEDORA-2026-350d904ee3](https://lwn.net/Articles/1106155/) | F43 | mingw-harfbuzz | 2026-11-09 |
| Fedora | [FEDORA-2026-14092cfbb4](https://lwn.net/Articles/1106158/) | F43 | mingw-qt5-qtbase | 2026-11-09 |
| Fedora | [FEDORA-2026-5d7cf14b63](https://lwn.net/Articles/1106157/) | F44 | mingw-qt5-qtbase | 2026-11-09 |
| Fedora | [FEDORA-2026-6a6222dd4a](https://lwn.net/Articles/1106156/) | F45 | mingw-qt5-qtbase | 2026-11-09 |
| Fedora | [FEDORA-2026-29e4b8a289](https://lwn.net/Articles/1106161/) | F43 | mingw-qt5-qtdeclarative | 2026-11-09 |
| Fedora | [FEDORA-2026-2caff2e30b](https://lwn.net/Articles/1106160/) | F44 | mingw-qt5-qtdeclarative | 2026-11-09 |
| Fedora | [FEDORA-2026-587a1cec32](https://lwn.net/Articles/1106159/) | F45 | mingw-qt5-qtdeclarative | 2026-11-09 |
| Fedora | [FEDORA-2026-b3ab9da70c](https://lwn.net/Articles/1106162/) | F43 | mingw-qt5-qtwebkit | 2026-11-09 |
| Fedora | [FEDORA-2026-5244693d13](https://lwn.net/Articles/1106163/) | F43 | mingw-qt6-qtbase | 2026-11-09 |
| Fedora | [FEDORA-2026-e5badbbedc](https://lwn.net/Articles/1105537/) | F43 | mongo-c-driver | 2026-11-05 |
| Fedora | [FEDORA-2026-bc9f778646](https://lwn.net/Articles/1105539/) | F44 | mongo-c-driver | 2026-11-05 |
| Fedora | [FEDORA-2026-dbe693ee92](https://lwn.net/Articles/1105538/) | F45 | mongo-c-driver | 2026-11-05 |
| Fedora | [FEDORA-2026-8c39ba6bab](https://lwn.net/Articles/1106750/) | F43 | mstflint | 2026-11-11 |
| Fedora | [FEDORA-2026-7092a043be](https://lwn.net/Articles/1106749/) | F44 | mstflint | 2026-11-11 |
| Fedora | [FEDORA-2026-015536827f](https://lwn.net/Articles/1106748/) | F45 | mstflint | 2026-11-11 |
| Fedora | [FEDORA-2026-e9b29b6da4](https://lwn.net/Articles/1106164/) | F45 | mtools | 2026-11-08 |
| Fedora | [FEDORA-2026-b6b68838b0](https://lwn.net/Articles/1106753/) | F43 | nextcloud | 2026-11-11 |
| Fedora | [FEDORA-2026-1ffca57dbf](https://lwn.net/Articles/1106752/) | F44 | nextcloud | 2026-11-11 |
| Fedora | [FEDORA-2026-72dc7f85d2](https://lwn.net/Articles/1106751/) | F45 | nextcloud | 2026-11-11 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106166/) | F45 | nginx | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106167/) | F45 | nginx-mod-brotli | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106168/) | F45 | nginx-mod-fancyindex | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106169/) | F45 | nginx-mod-headers-more | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106170/) | F45 | nginx-mod-js-challenge | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106171/) | F45 | nginx-mod-modsecurity | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106172/) | F45 | nginx-mod-naxsi | 2026-11-07 |
| Fedora | [FEDORA-2026-7e0167d39a](https://lwn.net/Articles/1106173/) | F45 | nginx-mod-vts | 2026-11-07 |
| Fedora | [FEDORA-2026-7d4fcfe6c8](https://lwn.net/Articles/1106174/) | F45 | nodejs-pnpm12 | 2026-11-09 |
| Fedora | [FEDORA-2026-5f701776a6](https://lwn.net/Articles/1105540/) | F43 | openbao | 2026-11-05 |
| Fedora | [FEDORA-2026-d255ce2e09](https://lwn.net/Articles/1105542/) | F44 | openbao | 2026-11-05 |
| Fedora | [FEDORA-2026-fc3fbffe59](https://lwn.net/Articles/1105541/) | F45 | openbao | 2026-11-05 |
| Fedora | [FEDORA-2026-450395b11f](https://lwn.net/Articles/1106175/) | F44 | pcre2 | 2026-11-08 |
| Fedora | [FEDORA-2026-3dc7e56d1e](https://lwn.net/Articles/1106176/) | F45 | pcre2 | 2026-11-08 |
| Fedora | [FEDORA-2026-a3a026d9ff](https://lwn.net/Articles/1106399/) | F43 | perl-CGI | 2026-11-10 |
| Fedora | [FEDORA-2026-516e427bac](https://lwn.net/Articles/1106401/) | F44 | perl-CGI | 2026-11-10 |
| Fedora | [FEDORA-2026-a04615c725](https://lwn.net/Articles/1106400/) | F45 | perl-CGI | 2026-11-10 |
| Fedora | [FEDORA-2026-5ca1419368](https://lwn.net/Articles/1105787/) | F43 | perl-HTTP-Headers-ActionPack | 2026-11-06 |
| Fedora | [FEDORA-2026-e94650c1ee](https://lwn.net/Articles/1105786/) | F44 | perl-HTTP-Headers-ActionPack | 2026-11-06 |
| Fedora | [FEDORA-2026-37e6cc76fc](https://lwn.net/Articles/1105785/) | F45 | perl-HTTP-Headers-ActionPack | 2026-11-06 |
| Fedora | [FEDORA-2026-a415b3bf48](https://lwn.net/Articles/1105790/) | F43 | perl-MIME-tools | 2026-11-06 |
| Fedora | [FEDORA-2026-0e79d6ad13](https://lwn.net/Articles/1105789/) | F44 | perl-MIME-tools | 2026-11-06 |
| Fedora | [FEDORA-2026-51fdfb7476](https://lwn.net/Articles/1105788/) | F45 | perl-MIME-tools | 2026-11-06 |
| Fedora | [FEDORA-2026-3cb8ce0117](https://lwn.net/Articles/1106402/) | F43 | perl-Net-IDN-Encode | 2026-11-10 |
| Fedora | [FEDORA-2026-effb380a7c](https://lwn.net/Articles/1106404/) | F44 | perl-Net-IDN-Encode | 2026-11-10 |
| Fedora | [FEDORA-2026-f6acaf8756](https://lwn.net/Articles/1106403/) | F45 | perl-Net-IDN-Encode | 2026-11-10 |
| Fedora | [FEDORA-2026-a2bcaf6c4d](https://lwn.net/Articles/1105793/) | F43 | perl-Plack | 2026-11-06 |
| Fedora | [FEDORA-2026-83600dbb0b](https://lwn.net/Articles/1105792/) | F44 | perl-Plack | 2026-11-06 |
| Fedora | [FEDORA-2026-e720c67bd5](https://lwn.net/Articles/1105791/) | F45 | perl-Plack | 2026-11-06 |
| Fedora | [FEDORA-2026-0942a5b9ea](https://lwn.net/Articles/1106179/) | F43 | perl-Spreadsheet-XLSX | 2026-11-09 |
| Fedora | [FEDORA-2026-e5d1978e9d](https://lwn.net/Articles/1106178/) | F44 | perl-Spreadsheet-XLSX | 2026-11-09 |
| Fedora | [FEDORA-2026-31c16b65d1](https://lwn.net/Articles/1106177/) | F45 | perl-Spreadsheet-XLSX | 2026-11-09 |
| Fedora | [FEDORA-2026-092670ec3e](https://lwn.net/Articles/1106405/) | F43 | perl-Starlet | 2026-11-10 |
| Fedora | [FEDORA-2026-bd36d053a1](https://lwn.net/Articles/1106407/) | F44 | perl-Starlet | 2026-11-10 |
| Fedora | [FEDORA-2026-7d9cd72397](https://lwn.net/Articles/1106406/) | F45 | perl-Starlet | 2026-11-10 |
| Fedora | [FEDORA-2026-a2df1dfb37](https://lwn.net/Articles/1105796/) | F43 | perl-Starman | 2026-11-06 |
| Fedora | [FEDORA-2026-2106e35a84](https://lwn.net/Articles/1105795/) | F44 | perl-Starman | 2026-11-06 |
| Fedora | [FEDORA-2026-c02d051eaf](https://lwn.net/Articles/1105794/) | F45 | perl-Starman | 2026-11-06 |
| Fedora | [FEDORA-2026-0a5b752f19](https://lwn.net/Articles/1106180/) | F43 | pie | 2026-11-08 |
| Fedora | [FEDORA-2026-35cc73bd06](https://lwn.net/Articles/1106181/) | F44 | pie | 2026-11-08 |
| Fedora | [FEDORA-2026-0d5a544c64](https://lwn.net/Articles/1106182/) | F45 | pie | 2026-11-08 |
| Fedora | [FEDORA-2026-a1c8629ff7](https://lwn.net/Articles/1105544/) | F44 | pipx | 2026-11-05 |
| Fedora | [FEDORA-2026-d521258d12](https://lwn.net/Articles/1105543/) | F45 | pipx | 2026-11-05 |
| Fedora | [FEDORA-2026-d2e76a72c7](https://lwn.net/Articles/1105799/) | F43 | proftpd | 2026-11-06 |
| Fedora | [FEDORA-2026-e68a51a81c](https://lwn.net/Articles/1105798/) | F44 | proftpd | 2026-11-06 |
| Fedora | [FEDORA-2026-768558f4ba](https://lwn.net/Articles/1105797/) | F45 | proftpd | 2026-11-06 |
| Fedora | [FEDORA-2026-1f40f6b868](https://lwn.net/Articles/1106183/) | F43 | python-boto3 | 2026-11-08 |
| Fedora | [FEDORA-2026-c23d8c6e6b](https://lwn.net/Articles/1105545/) | F44 | python-boto3 | 2026-11-05 |
| Fedora | [FEDORA-2026-1f40f6b868](https://lwn.net/Articles/1106184/) | F43 | python-botocore | 2026-11-08 |
| Fedora | [FEDORA-2026-c23d8c6e6b](https://lwn.net/Articles/1105546/) | F44 | python-botocore | 2026-11-05 |
| Fedora | [FEDORA-2026-29236f6dd2](https://lwn.net/Articles/1105547/) | F44 | python-crate-ingredients | 2026-11-05 |
| Fedora | [FEDORA-2026-1f38e8ba73](https://lwn.net/Articles/1106754/) | F45 | python-crate-ingredients | 2026-11-11 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106408/) | F45 | python-jiter | 2026-11-10 |
| Fedora | [FEDORA-2026-7888ffd011](https://lwn.net/Articles/1106185/) | F44 | python-joserfc | 2026-11-08 |
| Fedora | [FEDORA-2026-a4d05e8333](https://lwn.net/Articles/1106186/) | F45 | python-joserfc | 2026-11-08 |
| Fedora | [FEDORA-2026-34aa0f144e](https://lwn.net/Articles/1106187/) | F44 | python-jupyter-builder | 2026-11-07 |
| Fedora | [FEDORA-2026-34aa0f144e](https://lwn.net/Articles/1106188/) | F44 | python-jupyterlab-server | 2026-11-07 |
| Fedora | [FEDORA-2026-34aa0f144e](https://lwn.net/Articles/1106189/) | F44 | python-jupytext | 2026-11-07 |
| Fedora | [FEDORA-2026-768edcd81d](https://lwn.net/Articles/1105548/) | F43 | python-lxml-html-clean | 2026-11-05 |
| Fedora | [FEDORA-2026-d470ba3df9](https://lwn.net/Articles/1105550/) | F44 | python-lxml-html-clean | 2026-11-05 |
| Fedora | [FEDORA-2026-7c58252e69](https://lwn.net/Articles/1105549/) | F45 | python-lxml-html-clean | 2026-11-05 |
| Fedora | [FEDORA-2026-340793a2f1](https://lwn.net/Articles/1105801/) | F43 | python-mistune | 2026-11-06 |
| Fedora | [FEDORA-2026-ea39a303cf](https://lwn.net/Articles/1105800/) | F44 | python-mistune | 2026-11-06 |
| Fedora | [FEDORA-2026-34aa0f144e](https://lwn.net/Articles/1106190/) | F44 | python-nbdime | 2026-11-07 |
| Fedora | [FEDORA-2026-34aa0f144e](https://lwn.net/Articles/1106191/) | F44 | python-notebook | 2026-11-07 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106409/) | F45 | python-pydantic-core | 2026-11-10 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106410/) | F45 | python-pysequoia | 2026-11-10 |
| Fedora | [FEDORA-2026-1f40f6b868](https://lwn.net/Articles/1106192/) | F43 | python-s3transfer | 2026-11-08 |
| Fedora | [FEDORA-2026-1520dedf55](https://lwn.net/Articles/1106411/) | F43 | python3-docs | 2026-11-10 |
| Fedora | [FEDORA-2026-f3fe9323aa](https://lwn.net/Articles/1106412/) | F45 | python3-docs | 2026-11-10 |
| Fedora | [FEDORA-2026-30d5bd99e3](https://lwn.net/Articles/1105551/) | F43 | python3.11 | 2026-11-05 |
| Fedora | [FEDORA-2026-7cf032d4b0](https://lwn.net/Articles/1105553/) | F44 | python3.11 | 2026-11-05 |
| Fedora | [FEDORA-2026-015c45363c](https://lwn.net/Articles/1105552/) | F45 | python3.11 | 2026-11-05 |
| Fedora | [FEDORA-2026-4e3279af04](https://lwn.net/Articles/1106193/) | F43 | python3.12 | 2026-11-08 |
| Fedora | [FEDORA-2026-5f99243da4](https://lwn.net/Articles/1106194/) | F45 | python3.12 | 2026-11-08 |
| Fedora | [FEDORA-2026-d6b8383232](https://lwn.net/Articles/1105554/) | F43 | python3.13 | 2026-11-05 |
| Fedora | [FEDORA-2026-a85529a028](https://lwn.net/Articles/1105556/) | F44 | python3.13 | 2026-11-05 |
| Fedora | [FEDORA-2026-77153b01c6](https://lwn.net/Articles/1105555/) | F45 | python3.13 | 2026-11-05 |
| Fedora | [FEDORA-2026-1520dedf55](https://lwn.net/Articles/1106413/) | F43 | python3.14 | 2026-11-10 |
| Fedora | [FEDORA-2026-6530ce786a](https://lwn.net/Articles/1105557/) | F45 | python3.14 | 2026-11-05 |
| Fedora | [FEDORA-2026-5e4931d206](https://lwn.net/Articles/1105558/) | F43 | python3.15 | 2026-11-05 |
| Fedora | [FEDORA-2026-4f056db42e](https://lwn.net/Articles/1105559/) | F44 | python3.15 | 2026-11-05 |
| Fedora | [FEDORA-2026-f3fe9323aa](https://lwn.net/Articles/1106414/) | F45 | python3.15 | 2026-11-10 |
| Fedora | [FEDORA-2026-e85939a5f8](https://lwn.net/Articles/1106195/) | F44 | rccl | 2026-11-08 |
| Fedora | [FEDORA-2026-5b6559d7c1](https://lwn.net/Articles/1106196/) | F45 | rccl | 2026-11-08 |
| Fedora | [FEDORA-2026-db7e033531](https://lwn.net/Articles/1105560/) | F43 | roundcubemail | 2026-11-05 |
| Fedora | [FEDORA-2026-2aba9ce8fc](https://lwn.net/Articles/1105562/) | F44 | roundcubemail | 2026-11-05 |
| Fedora | [FEDORA-2026-7002464a52](https://lwn.net/Articles/1105561/) | F45 | roundcubemail | 2026-11-05 |
| Fedora | [FEDORA-2026-5079b4320a](https://lwn.net/Articles/1105563/) | F43 | rply | 2026-11-05 |
| Fedora | [FEDORA-2026-aa0bdade09](https://lwn.net/Articles/1105565/) | F44 | rply | 2026-11-05 |
| Fedora | [FEDORA-2026-b2f81db711](https://lwn.net/Articles/1105564/) | F45 | rply | 2026-11-05 |
| Fedora | [FEDORA-2026-83a3ff7322](https://lwn.net/Articles/1106198/) | F44 | rsync | 2026-11-09 |
| Fedora | [FEDORA-2026-30581e33eb](https://lwn.net/Articles/1106197/) | F45 | rsync | 2026-11-08 |
| Fedora | [FEDORA-2026-62de4e63a0](https://lwn.net/Articles/1105566/) | F44 | ruby-build | 2026-11-05 |
| Fedora | [FEDORA-2026-80070d1931](https://lwn.net/Articles/1105802/) | F45 | ruby-build | 2026-11-06 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106415/) | F45 | ruff | 2026-11-10 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106416/) | F45 | rust-afterburn | 2026-11-10 |
| Fedora | [FEDORA-2026-9288162688](https://lwn.net/Articles/1105567/) | F43 | rust-app-store-connect | 2026-11-05 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106417/) | F45 | rust-astral\_async\_zip | 2026-11-10 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106200/) | F43 | rust-blake2b\_simd | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106199/) | F44 | rust-blake2b\_simd | 2026-11-07 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106202/) | F43 | rust-blake3 | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106201/) | F44 | rust-blake3 | 2026-11-07 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106418/) | F45 | rust-clearscreen | 2026-11-10 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106204/) | F43 | rust-constant\_time\_eq | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106203/) | F44 | rust-constant\_time\_eq | 2026-11-07 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105803/) | F45 | rust-crypto-bigint | 2026-11-06 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105804/) | F45 | rust-ctutils | 2026-11-06 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105805/) | F45 | rust-elliptic-curve | 2026-11-06 |
| Fedora | [FEDORA-2026-9d5b47fd47](https://lwn.net/Articles/1106757/) | F43 | rust-ingredients | 2026-11-11 |
| Fedora | [FEDORA-2026-5f5462d773](https://lwn.net/Articles/1106756/) | F44 | rust-ingredients | 2026-11-11 |
| Fedora | [FEDORA-2026-91af9931e5](https://lwn.net/Articles/1106755/) | F45 | rust-ingredients | 2026-11-11 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106419/) | F45 | rust-jiter | 2026-11-10 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106206/) | F43 | rust-lzma-rust2 | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106205/) | F44 | rust-lzma-rust2 | 2026-11-07 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106420/) | F45 | rust-lzma-rust2 | 2026-11-10 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106421/) | F45 | rust-mailparse | 2026-11-10 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105806/) | F45 | rust-num-bigint | 2026-11-06 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105807/) | F45 | rust-num-bigint0.4 | 2026-11-06 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105808/) | F45 | rust-num-modular | 2026-11-06 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105809/) | F45 | rust-num-modular0.6 | 2026-11-06 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105810/) | F45 | rust-num-prime | 2026-11-06 |
| Fedora | [FEDORA-2026-695d1995f3](https://lwn.net/Articles/1106758/) | F43 | rust-pore | 2026-11-11 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106208/) | F43 | rust-ppmd-rust | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106207/) | F44 | rust-ppmd-rust | 2026-11-07 |
| Fedora | [FEDORA-2026-99900f26c7](https://lwn.net/Articles/1106761/) | F43 | rust-pulldown-cmark | 2026-11-11 |
| Fedora | [FEDORA-2026-dd379905de](https://lwn.net/Articles/1106760/) | F44 | rust-pulldown-cmark | 2026-11-11 |
| Fedora | [FEDORA-2026-75144eedff](https://lwn.net/Articles/1106759/) | F45 | rust-pulldown-cmark | 2026-11-11 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106422/) | F45 | rust-pyo3-introspection | 2026-11-10 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106423/) | F45 | rust-python-pkginfo | 2026-11-10 |
| Fedora | [FEDORA-2026-d4e37b0053](https://lwn.net/Articles/1105568/) | F43 | rust-qemu-rdp | 2026-11-05 |
| Fedora | [FEDORA-2026-4cf39c1b10](https://lwn.net/Articles/1106764/) | F43 | rust-rbw | 2026-11-11 |
| Fedora | [FEDORA-2026-fc6ab2066a](https://lwn.net/Articles/1106763/) | F44 | rust-rbw | 2026-11-11 |
| Fedora | [FEDORA-2026-12c8566832](https://lwn.net/Articles/1106762/) | F45 | rust-rbw | 2026-11-11 |
| Fedora | [FEDORA-2026-b6daefd0fc](https://lwn.net/Articles/1105569/) | F43 | rust-redlib | 2026-11-05 |
| Fedora | [FEDORA-2026-ab2b8fc1e8](https://lwn.net/Articles/1105570/) | F44 | rust-redlib | 2026-11-05 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106209/) | F44 | rust-regorus | 2026-11-07 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106211/) | F43 | rust-sccache | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106210/) | F44 | rust-sccache | 2026-11-07 |
| Fedora | [FEDORA-2026-eda423298c](https://lwn.net/Articles/1106767/) | F43 | rust-sequoia-sq | 2026-11-11 |
| Fedora | [FEDORA-2026-2aeda2e0f8](https://lwn.net/Articles/1106766/) | F44 | rust-sequoia-sq | 2026-11-11 |
| Fedora | [FEDORA-2026-1958bf759f](https://lwn.net/Articles/1106765/) | F45 | rust-sequoia-sq | 2026-11-11 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106424/) | F45 | rust-serde\_json | 2026-11-10 |
| Fedora | [FEDORA-2026-e50bc09915](https://lwn.net/Articles/1106769/) | F44 | rust-siguldry-fedora-autopen | 2026-11-11 |
| Fedora | [FEDORA-2026-2ce86ea8f8](https://lwn.net/Articles/1106768/) | F45 | rust-siguldry-fedora-autopen | 2026-11-11 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106425/) | F45 | rust-testresult | 2026-11-10 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106213/) | F43 | rust-totp-rs | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106212/) | F44 | rust-totp-rs | 2026-11-07 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106215/) | F43 | rust-typed-path | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106214/) | F44 | rust-typed-path | 2026-11-07 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106217/) | F43 | rust-zip | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106216/) | F44 | rust-zip | 2026-11-07 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106426/) | F45 | rust-zip | 2026-11-10 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106219/) | F43 | rust-zip0.6 | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106218/) | F44 | rust-zip0.6 | 2026-11-07 |
| Fedora | [FEDORA-2026-a011e63a06](https://lwn.net/Articles/1106221/) | F43 | rust-zip2 | 2026-11-07 |
| Fedora | [FEDORA-2026-f782e1aa07](https://lwn.net/Articles/1106220/) | F44 | rust-zip2 | 2026-11-07 |
| Fedora | [FEDORA-2026-45268841b3](https://lwn.net/Articles/1105811/) | F45 | rust-zmij | 2026-11-06 |
| Fedora | [FEDORA-2026-965f6f4669](https://lwn.net/Articles/1105814/) | F43 | rust-zstd | 2026-11-06 |
| Fedora | [FEDORA-2026-ab4ba75e47](https://lwn.net/Articles/1105813/) | F44 | rust-zstd | 2026-11-06 |
| Fedora | [FEDORA-2026-852d99c4f2](https://lwn.net/Articles/1105812/) | F45 | rust-zstd | 2026-11-06 |
| Fedora | [FEDORA-2026-965f6f4669](https://lwn.net/Articles/1105817/) | F43 | rust-zstd-safe | 2026-11-06 |
| Fedora | [FEDORA-2026-ab4ba75e47](https://lwn.net/Articles/1105816/) | F44 | rust-zstd-safe | 2026-11-06 |
| Fedora | [FEDORA-2026-852d99c4f2](https://lwn.net/Articles/1105815/) | F45 | rust-zstd-safe | 2026-11-06 |
| Fedora | [FEDORA-2026-965f6f4669](https://lwn.net/Articles/1105820/) | F43 | rust-zstd-safe7 | 2026-11-06 |
| Fedora | [FEDORA-2026-ab4ba75e47](https://lwn.net/Articles/1105819/) | F44 | rust-zstd-safe7 | 2026-11-06 |
| Fedora | [FEDORA-2026-852d99c4f2](https://lwn.net/Articles/1105818/) | F45 | rust-zstd-safe7 | 2026-11-06 |
| Fedora | [FEDORA-2026-965f6f4669](https://lwn.net/Articles/1105823/) | F43 | rust-zstd-sys | 2026-11-06 |
| Fedora | [FEDORA-2026-ab4ba75e47](https://lwn.net/Articles/1105822/) | F44 | rust-zstd-sys | 2026-11-06 |
| Fedora | [FEDORA-2026-852d99c4f2](https://lwn.net/Articles/1105821/) | F45 | rust-zstd-sys | 2026-11-06 |
| Fedora | [FEDORA-2026-965f6f4669](https://lwn.net/Articles/1105826/) | F43 | rust-zstd0.13 | 2026-11-06 |
| Fedora | [FEDORA-2026-ab4ba75e47](https://lwn.net/Articles/1105825/) | F44 | rust-zstd0.13 | 2026-11-06 |
| Fedora | [FEDORA-2026-852d99c4f2](https://lwn.net/Articles/1105824/) | F45 | rust-zstd0.13 | 2026-11-06 |
| Fedora | [FEDORA-2026-f7bd6aa596](https://lwn.net/Articles/1105828/) | F43 | scribus | 2026-11-06 |
| Fedora | [FEDORA-2026-d407c720c8](https://lwn.net/Articles/1105827/) | F44 | scribus | 2026-11-06 |
| Fedora | [FEDORA-2026-837d6477fa](https://lwn.net/Articles/1105571/) | F45 | scribus | 2026-11-05 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106427/) | F45 | selenium-manager | 2026-11-10 |
| Fedora | [FEDORA-2026-046c8a7938](https://lwn.net/Articles/1106223/) | F43 | sofia-sip | 2026-11-07 |
| Fedora | [FEDORA-2026-b176109503](https://lwn.net/Articles/1106222/) | F44 | sofia-sip | 2026-11-07 |
| Fedora | [FEDORA-2026-3b906c3607](https://lwn.net/Articles/1105829/) | F45 | sofia-sip | 2026-11-06 |
| Fedora | [FEDORA-2026-5546835eb2](https://lwn.net/Articles/1106225/) | F44 | suricata | 2026-11-09 |
| Fedora | [FEDORA-2026-e5e566b6b5](https://lwn.net/Articles/1106224/) | F45 | suricata | 2026-11-09 |
| Fedora | [FEDORA-2026-0451d4f86a](https://lwn.net/Articles/1105832/) | F43 | tailscale | 2026-11-06 |
| Fedora | [FEDORA-2026-c8bfae6071](https://lwn.net/Articles/1105831/) | F44 | tailscale | 2026-11-06 |
| Fedora | [FEDORA-2026-068cc0ad52](https://lwn.net/Articles/1105830/) | F45 | tailscale | 2026-11-06 |
| Fedora | [FEDORA-2026-6b7d3e80f7](https://lwn.net/Articles/1106771/) | F44 | tigervnc | 2026-11-11 |
| Fedora | [FEDORA-2026-80450b1573](https://lwn.net/Articles/1106770/) | F45 | tigervnc | 2026-11-11 |
| Fedora | [FEDORA-2026-d62d139e4b](https://lwn.net/Articles/1105835/) | F43 | tor | 2026-11-06 |
| Fedora | [FEDORA-2026-5db6838405](https://lwn.net/Articles/1105834/) | F44 | tor | 2026-11-06 |
| Fedora | [FEDORA-2026-2e080d83b2](https://lwn.net/Articles/1105833/) | F45 | tor | 2026-11-06 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106428/) | F45 | ty | 2026-11-10 |
| Fedora | [FEDORA-2026-ab4f7ff50a](https://lwn.net/Articles/1106772/) | F43 | unbound | 2026-11-11 |
| Fedora | [FEDORA-2026-2b0f14aa7b](https://lwn.net/Articles/1106429/) | F45 | uutils-coreutils | 2026-11-10 |
| Fedora | [FEDORA-2026-1fd9c58e29](https://lwn.net/Articles/1105572/) | F43 | valkey | 2026-11-05 |
| Fedora | [FEDORA-2026-5aaf7130ef](https://lwn.net/Articles/1105574/) | F44 | valkey | 2026-11-05 |
| Fedora | [FEDORA-2026-3bb241ef05](https://lwn.net/Articles/1105573/) | F45 | valkey | 2026-11-05 |
| Fedora | [FEDORA-2026-f273e7ec4e](https://lwn.net/Articles/1106227/) | F43 | wordpress | 2026-11-07 |
| Fedora | [FEDORA-2026-b11dcc003b](https://lwn.net/Articles/1106226/) | F44 | wordpress | 2026-11-07 |
| Fedora | [FEDORA-2026-c32ba8cfb4](https://lwn.net/Articles/1105836/) | F45 | wordpress | 2026-11-06 |
| Fedora | [FEDORA-2026-0d1924f837](https://lwn.net/Articles/1106228/) | F44 | xen | 2026-11-09 |
| Fedora | [FEDORA-2026-b630871014](https://lwn.net/Articles/1106773/) | F43 | zchunk | 2026-11-11 |
| Gentoo | [202611-01](https://lwn.net/Articles/1106774/) |  | Brotli | 2026-11-11 |
| Gentoo | [202611-02](https://lwn.net/Articles/1106775/) |  | git | 2026-11-11 |
| Gentoo | [202611-03](https://lwn.net/Articles/1106776/) |  | libde265 | 2026-11-11 |
| Mageia | [MGASA-2026-0578](https://lwn.net/Articles/1106229/) | 10 | gimp | 2026-11-07 |
| Mageia | [MGASA-2026-0581](https://lwn.net/Articles/1106430/) | 10 | glibc | 2026-11-09 |
| Mageia | [MGASA-2026-0573](https://lwn.net/Articles/1105575/) | 10 | minetest | 2026-11-04 |
| Mageia | [MGASA-2026-0588](https://lwn.net/Articles/1106777/) | 10 | mopidy | 2026-11-10 |
| Mageia | [MGASA-2026-0582](https://lwn.net/Articles/1106431/) | 10 | packages | 2026-11-09 |
| Mageia | [MGASA-2026-0585](https://lwn.net/Articles/1106432/) | 10 | php-smarty | 2026-11-09 |
| Mageia | [MGASA-2026-0584](https://lwn.net/Articles/1106433/) | 10 | python-aiohttp | 2026-11-09 |
| Mageia | [MGASA-2026-0589](https://lwn.net/Articles/1106778/) | 10 | python-dulwich, rust-similar3 | 2026-11-10 |
| Mageia | [MGASA-2026-0580](https://lwn.net/Articles/1106230/) | 10 | python-gitpython | 2026-11-07 |
| Mageia | [MGASA-2026-0577](https://lwn.net/Articles/1105576/) | 10 | python-pypdf | 2026-11-05 |
| Mageia | [MGASA-2026-0586](https://lwn.net/Articles/1106779/) | 10 | rclone | 2026-11-10 |
| Mageia | [MGASA-2026-0587](https://lwn.net/Articles/1106780/) | 10 | sofia-sip | 2026-11-10 |
| Mageia | [MGASA-2026-0575](https://lwn.net/Articles/1105577/) | 10 | stunnel | 2026-11-05 |
| Mageia | [MGASA-2026-0579](https://lwn.net/Articles/1106231/) | 10 | suricata | 2026-11-07 |
| Mageia | [MGASA-2026-0583](https://lwn.net/Articles/1106434/) | 10 | thunderbird | 2026-11-09 |
| Mageia | [MGASA-2026-0574](https://lwn.net/Articles/1105578/) | 10 | znc | 2026-11-05 |
| Mageia | [MGASA-2026-0576](https://lwn.net/Articles/1105579/) | 10 | zvbi | 2026-11-05 |
| Oracle | [ELSA-2026-86192](https://lwn.net/Articles/1105580/) | OL8 | .NET 10.0 | 2026-11-04 |
| Oracle | [ELSA-2026-92431](https://lwn.net/Articles/1105581/) | OL8 | .NET 10.0 | 2026-11-04 |
| Oracle | [ELSA-2026-93610](https://lwn.net/Articles/1105582/) | OL9 | bind | 2026-11-04 |
| Oracle | [ELSA-2026-90495](https://lwn.net/Articles/1105583/) | OL9 | brotli | 2026-11-04 |
| Oracle | [ELSA-2026-94533](https://lwn.net/Articles/1105584/) | OL9 | cockpit | 2026-11-04 |
| Oracle | [ELSA-2026-95570](https://lwn.net/Articles/1105837/) | OL10 | cockpit-files | 2026-11-06 |
| Oracle | [ELSA-2026-96092](https://lwn.net/Articles/1106435/) | OL10 | curl | 2026-11-09 |
| Oracle | [ELSA-2026-95519](https://lwn.net/Articles/1105838/) | OL10 | delve | 2026-11-06 |
| Oracle | [ELSA-2026-95518](https://lwn.net/Articles/1105839/) | OL9 | delve | 2026-11-06 |
| Oracle | [ELSA-2026-94630](https://lwn.net/Articles/1105585/) | OL10 | dpdk | 2026-11-04 |
| Oracle | [ELSA-2026-96083](https://lwn.net/Articles/1106781/) | OL8 | dpdk | 2026-11-11 |
| Oracle | [ELSA-2026-94629](https://lwn.net/Articles/1105586/) | OL9 | dpdk | 2026-11-04 |
| Oracle | [ELSA-2026-96240](https://lwn.net/Articles/1106782/) | OL10 | edk2 | 2026-11-11 |
| Oracle | [ELSA-2026-94501](https://lwn.net/Articles/1105587/) | OL10 | fence-agents | 2026-11-04 |
| Oracle | [ELSA-2026-94500](https://lwn.net/Articles/1105588/) | OL9 | fence-agents | 2026-11-04 |
| Oracle | [ELSA-2026-93956](https://lwn.net/Articles/1106784/) | OL10 | firefox | 2026-11-11 |
| Oracle | [ELSA-2026-65442-0](https://lwn.net/Articles/1105840/) | OL7 | firefox | 2026-11-06 |
| Oracle | [ELSA-2026-83496](https://lwn.net/Articles/1106436/) | OL7 | firefox | 2026-11-09 |
| Oracle | [ELSA-2026-92363](https://lwn.net/Articles/1106437/) | OL7 | firefox | 2026-11-09 |
| Oracle | [ELSA-2026-76741](https://lwn.net/Articles/1106783/) | OL7 | firefox | 2026-11-11 |
| Oracle | [ELSA-2026-94514](https://lwn.net/Articles/1105589/) | OL10 | freerdp | 2026-11-04 |
| Oracle | [ELSA-2026-94510](https://lwn.net/Articles/1105590/) | OL8 | freerdp | 2026-11-04 |
| Oracle | [ELSA-2026-73425](https://lwn.net/Articles/1106438/) | OL8 | gdb | 2026-11-09 |
| Oracle | [ELSA-2026-93975](https://lwn.net/Articles/1105591/) | OL9 | gimp | 2026-11-04 |
| Oracle | [ELSA-2026-95482](https://lwn.net/Articles/1105841/) | OL8 | gimp:2.8 | 2026-11-06 |
| Oracle | [ELSA-2026-84753](https://lwn.net/Articles/1105593/) | OL10 | glibc | 2026-11-04 |
| Oracle | [ELSA-2026-76781](https://lwn.net/Articles/1106440/) | OL10 | glibc | 2026-11-09 |
| Oracle | [ELSA-2026-80798](https://lwn.net/Articles/1105592/) | OL8 | glibc | 2026-11-04 |
| Oracle | [ELSA-2026-96087](https://lwn.net/Articles/1106785/) | OL8 | glibc | 2026-11-11 |
| Oracle | [ELSA-2026-95618](https://lwn.net/Articles/1106439/) | OL9 | glibc | 2026-11-09 |
| Oracle | [ELSA-2026-90811](https://lwn.net/Articles/1105594/) | OL9 | grafana | 2026-11-04 |
| Oracle | [ELSA-2026-86606](https://lwn.net/Articles/1105595/) | OL7 | gvfs | 2026-11-05 |
| Oracle | [ELSA-2026-71619](https://lwn.net/Articles/1105596/) | OL7 | host-metering | 2026-11-04 |
| Oracle | [ELSA-2026-93911](https://lwn.net/Articles/1105599/) | OL10 | kernel | 2026-11-04 |
| Oracle | [ELSA-2026-95367](https://lwn.net/Articles/1105842/) | OL10 | kernel | 2026-11-06 |
| Oracle | [ELSA-2026-500589](https://lwn.net/Articles/1106795/) | OL7 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-95212](https://lwn.net/Articles/1106441/) | OL8 | kernel | 2026-11-09 |
| Oracle | [ELSA-2026-500588](https://lwn.net/Articles/1106791/) | OL8 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500589](https://lwn.net/Articles/1106793/) | OL8 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500589](https://lwn.net/Articles/1106794/) | OL8 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500590](https://lwn.net/Articles/1106792/) | OL8 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-93412](https://lwn.net/Articles/1105597/) | OL9 | kernel | 2026-11-04 |
| Oracle | [ELSA-2026-93930](https://lwn.net/Articles/1105598/) | OL9 | kernel | 2026-11-04 |
| Oracle | [ELSA-2026-95370](https://lwn.net/Articles/1105843/) | OL9 | kernel | 2026-11-06 |
| Oracle | [ELSA-2026-500587](https://lwn.net/Articles/1106786/) | OL9 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500588](https://lwn.net/Articles/1106787/) | OL9 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500590](https://lwn.net/Articles/1106788/) | OL9 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500590](https://lwn.net/Articles/1106790/) | OL9 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500588](https://lwn.net/Articles/1106789/) | OL9 | kernel | 2026-11-11 |
| Oracle | [ELSA-2026-500587](https://lwn.net/Articles/1106796/) |  | kernel-uek | 2026-11-11 |
| Oracle | [ELSA-2026-96236](https://lwn.net/Articles/1106797/) | OL10 | nodejs-nodemon | 2026-11-11 |
| Oracle | [ELSA-2026-96094](https://lwn.net/Articles/1106798/) | OL10 | nodejs22 | 2026-11-11 |
| Oracle | [ELSA-2026-96226](https://lwn.net/Articles/1106799/) | OL9 | nodejs:24 | 2026-11-11 |
| Oracle | [ELSA-2026-500570](https://lwn.net/Articles/1106442/) | OL8 | oVirt 4.5 ovirt-engine-wildfly | 2026-11-09 |
| Oracle | [ELSA-2026-500571](https://lwn.net/Articles/1106443/) | OL9 | oVirt 4.5 ovirt-engine-wildfly | 2026-11-09 |
| Oracle | [ELSA-2026-69293](https://lwn.net/Articles/1105844/) | OL9 | osbuild-composer | 2026-11-06 |
| Oracle | [ELSA-2026-96215](https://lwn.net/Articles/1106800/) | OL8 | patch | 2026-11-11 |
| Oracle | [ELSA-2026-93471](https://lwn.net/Articles/1106444/) | OL8 | perl-YAML:1.24 | 2026-11-09 |
| Oracle | [ELSA-2026-94749](https://lwn.net/Articles/1105600/) | OL8 | python-dns | 2026-11-04 |
| Oracle | [ELSA-2026-88421](https://lwn.net/Articles/1105601/) | OL9 | qemu-kvm | 2026-11-04 |
| Oracle | [ELSA-2026-94519](https://lwn.net/Articles/1105602/) | OL8 | raptor2 | 2026-11-04 |
| Oracle | [ELSA-2026-96235](https://lwn.net/Articles/1106802/) | OL10 | ruby | 2026-11-11 |
| Oracle | [ELSA-2026-96233](https://lwn.net/Articles/1106803/) | OL10 | ruby4.0 | 2026-11-11 |
| Oracle | [ELSA-2026-96078](https://lwn.net/Articles/1106804/) | OL8 | squid:4 | 2026-11-11 |
| Oracle | [ELSA-2026-95085](https://lwn.net/Articles/1105604/) | OL10 | tesseract | 2026-11-04 |
| Oracle | [ELSA-2026-95725](https://lwn.net/Articles/1106445/) | OL8 | tesseract | 2026-11-09 |
| Oracle | [ELSA-2026-95086](https://lwn.net/Articles/1105603/) | OL9 | tesseract | 2026-11-05 |
| Oracle | [ELSA-2026-96079](https://lwn.net/Articles/1106805/) | OL10 | thunderbird | 2026-11-11 |
| Oracle | [ELSA-2026-96081](https://lwn.net/Articles/1106806/) | OL9 | thunderbird | 2026-11-11 |
| Oracle | [ELSA-2026-95194](https://lwn.net/Articles/1105605/) | OL9 | webkit2gtk3 | 2026-11-05 |
| Oracle | [ELSA-2026-95281](https://lwn.net/Articles/1105606/) | OL8 | xorg-x11-server-Xwayland | 2026-11-05 |
| Red Hat | [RHSA-2026:92438-01](https://lwn.net/Articles/1106701/) | EL10 | .NET 10.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92431-01](https://lwn.net/Articles/1106708/) | EL8 | .NET 10.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92432-01](https://lwn.net/Articles/1106704/) | EL9 | .NET 10.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:98627-01](https://lwn.net/Articles/1106694/) | EL10 | .NET 11.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92511-01](https://lwn.net/Articles/1106700/) | EL8 | .NET 11.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92428-01](https://lwn.net/Articles/1106707/) | EL10 | .NET 8.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:93455-01](https://lwn.net/Articles/1106698/) | EL10.0 | .NET 8.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92420-01](https://lwn.net/Articles/1106711/) | EL8 | .NET 8.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92492-01](https://lwn.net/Articles/1106702/) | EL9 | .NET 8.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:93456-01](https://lwn.net/Articles/1106695/) | EL9.4 | .NET 8.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:93457-01](https://lwn.net/Articles/1106697/) | EL9.6 | .NET 8.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92430-01](https://lwn.net/Articles/1106703/) | EL10 | .NET 9.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:93458-01](https://lwn.net/Articles/1106696/) | EL10.0 | .NET 9.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92427-01](https://lwn.net/Articles/1106712/) | EL8 | .NET 9.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:92429-01](https://lwn.net/Articles/1106705/) | EL9 | .NET 9.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:93459-01](https://lwn.net/Articles/1106699/) | EL9.6 | .NET 9.0 | 2026-11-11 |
| Red Hat | [RHSA-2026:98637-01](https://lwn.net/Articles/1106644/) | EL10 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:94115-01](https://lwn.net/Articles/1106653/) | EL10.0 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:92419-01](https://lwn.net/Articles/1106660/) | EL10.2 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95727-01](https://lwn.net/Articles/1106645/) | EL6 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95726-01](https://lwn.net/Articles/1106646/) | EL7 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:93925-01](https://lwn.net/Articles/1106657/) | EL8 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95477-01](https://lwn.net/Articles/1106643/) | EL8.4 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95435-01](https://lwn.net/Articles/1106649/) | EL8.6 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95478-01](https://lwn.net/Articles/1106650/) | EL8.8 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:93610-01](https://lwn.net/Articles/1106659/) | EL9 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95242-01](https://lwn.net/Articles/1106648/) | EL9.2 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95241-01](https://lwn.net/Articles/1106651/) | EL9.4 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:95048-01](https://lwn.net/Articles/1106652/) | EL9.6 | bind | 2026-11-11 |
| Red Hat | [RHSA-2026:94011-01](https://lwn.net/Articles/1106656/) | EL8 | bind9.16 | 2026-11-11 |
| Red Hat | [RHSA-2026:94277-01](https://lwn.net/Articles/1106654/) | EL8.6 | bind9.16 | 2026-11-11 |
| Red Hat | [RHSA-2026:95017-01](https://lwn.net/Articles/1106655/) | EL8.8 | bind9.16 | 2026-11-11 |
| Red Hat | [RHSA-2026:93072-01](https://lwn.net/Articles/1106658/) | EL9 | bind9.18 | 2026-11-11 |
| Red Hat | [RHSA-2026:94278-01](https://lwn.net/Articles/1106647/) | EL9.6 | bind9.18 | 2026-11-11 |
| Red Hat | [RHSA-2026:98555-01](https://lwn.net/Articles/1106719/) | EL10 | buildah | 2026-11-11 |
| Red Hat | [RHSA-2026:98450-01](https://lwn.net/Articles/1106724/) | EL9 | buildah | 2026-11-11 |
| Red Hat | [RHSA-2026:98629-01](https://lwn.net/Articles/1106678/) | EL10 | c-ares | 2026-11-11 |
| Red Hat | [RHSA-2026:98449-01](https://lwn.net/Articles/1106729/) | EL9 | containernetworking-plugins | 2026-11-11 |
| Red Hat | [RHSA-2026:97644-01](https://lwn.net/Articles/1106733/) | EL9 | containernetworking-plugins | 2026-11-11 |
| Red Hat | [RHSA-2026:98086-01](https://lwn.net/Articles/1106730/) | EL10 | delve | 2026-11-11 |
| Red Hat | [RHSA-2026:95519-01](https://lwn.net/Articles/1105730/) | EL10.2 | delve | 2026-11-06 |
| Red Hat | [RHSA-2026:97877-01](https://lwn.net/Articles/1106735/) | EL9 | delve | 2026-11-11 |
| Red Hat | [RHSA-2026:95518-01](https://lwn.net/Articles/1105729/) | EL9.8 | delve | 2026-11-06 |
| Red Hat | [RHSA-2026:98642-01](https://lwn.net/Articles/1106672/) | EL10 | flatpak-builder | 2026-11-11 |
| Red Hat | [RHSA-2026:92220-01](https://lwn.net/Articles/1106676/) | EL8.4 | flatpak-builder | 2026-11-11 |
| Red Hat | [RHSA-2026:90896-01](https://lwn.net/Articles/1106674/) | EL8.6 | flatpak-builder | 2026-11-11 |
| Red Hat | [RHSA-2026:98536-01](https://lwn.net/Articles/1106675/) | EL9 | flatpak-builder | 2026-11-11 |
| Red Hat | [RHSA-2026:98648-01](https://lwn.net/Articles/1106661/) | EL10 | gcc | 2026-11-11 |
| Red Hat | [RHSA-2026:98115-01](https://lwn.net/Articles/1106665/) | EL8 | gcc | 2026-11-11 |
| Red Hat | [RHSA-2026:98524-01](https://lwn.net/Articles/1106666/) | EL9 | gcc | 2026-11-11 |
| Red Hat | [RHSA-2026:98633-01](https://lwn.net/Articles/1106663/) | EL10 | gcc-toolset-15-gcc | 2026-11-11 |
| Red Hat | [RHSA-2026:98640-01](https://lwn.net/Articles/1106662/) | EL10 | gcc-toolset-16-gcc | 2026-11-11 |
| Red Hat | [RHSA-2026:98534-01](https://lwn.net/Articles/1106664/) | EL9 | gcc-toolset-16-gcc | 2026-11-11 |
| Red Hat | [RHSA-2026:90757-01](https://lwn.net/Articles/1105739/) | EL10.0 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:95234-01](https://lwn.net/Articles/1105720/) | EL8.4 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:89926-01](https://lwn.net/Articles/1105745/) | EL8.6 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:89925-01](https://lwn.net/Articles/1105747/) | EL8.8 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:89922-01](https://lwn.net/Articles/1105748/) | EL9.2 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:89921-01](https://lwn.net/Articles/1105746/) | EL9.4 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:89920-01](https://lwn.net/Articles/1105749/) | EL9.6 | git-lfs | 2026-11-06 |
| Red Hat | [RHSA-2026:98592-01](https://lwn.net/Articles/1106709/) | EL10 | go-fdo-client | 2026-11-11 |
| Red Hat | [RHSA-2026:98593-01](https://lwn.net/Articles/1106716/) | EL10 | go-fdo-server | 2026-11-11 |
| Red Hat | [RHSA-2026:95638-01](https://lwn.net/Articles/1105728/) | EL8 | go-toolset:rhel8 | 2026-11-06 |
| Red Hat | [RHSA-2026:98108-01](https://lwn.net/Articles/1106732/) | EL10.0 | golang-github-openprinting-ipp-usb | 2026-11-11 |
| Red Hat | [RHSA-2026:98056-01](https://lwn.net/Articles/1106734/) | EL10 | grafana | 2026-11-11 |
| Red Hat | [RHSA-2026:3078-01](https://lwn.net/Articles/1105471/) | EL10.0 | grafana | 2026-11-05 |
| Red Hat | [RHSA-2026:89744-01](https://lwn.net/Articles/1105750/) | EL9 | grafana | 2026-11-06 |
| Red Hat | [RHSA-2026:98454-01](https://lwn.net/Articles/1106726/) | EL9 | grafana | 2026-11-11 |
| Red Hat | [RHSA-2026:3529-01](https://lwn.net/Articles/1105470/) | EL9.6 | grafana | 2026-11-05 |
| Red Hat | [RHSA-2026:98579-01](https://lwn.net/Articles/1106717/) | EL10 | grafana-pcp | 2026-11-11 |
| Red Hat | [RHSA-2026:98479-01](https://lwn.net/Articles/1106723/) | EL9 | grafana-pcp | 2026-11-11 |
| Red Hat | [RHSA-2026:98621-01](https://lwn.net/Articles/1106713/) | EL10 | gstreamer1-plugins-bad-free | 2026-11-11 |
| Red Hat | [RHSA-2026:98644-01](https://lwn.net/Articles/1106673/) | EL10 | gstreamer1-plugins-good | 2026-11-11 |
| Red Hat | [RHSA-2026:98623-01](https://lwn.net/Articles/1106683/) | EL10 | gvfs | 2026-11-11 |
| Red Hat | [RHSA-2026:98610-01](https://lwn.net/Articles/1106706/) | EL10 | gvisor-tap-vsock | 2026-11-11 |
| Red Hat | [RHSA-2026:98502-01](https://lwn.net/Articles/1106722/) | EL9 | gvisor-tap-vsock | 2026-11-11 |
| Red Hat | [RHSA-2026:90513-01](https://lwn.net/Articles/1105743/) | EL10.0 | ignition | 2026-11-06 |
| Red Hat | [RHSA-2026:91720-01](https://lwn.net/Articles/1105734/) | EL10.2 | ignition | 2026-11-06 |
| Red Hat | [RHSA-2026:90519-01](https://lwn.net/Articles/1105740/) | EL9.2 | ignition | 2026-11-06 |
| Red Hat | [RHSA-2026:90518-01](https://lwn.net/Articles/1105742/) | EL9.4 | ignition | 2026-11-06 |
| Red Hat | [RHSA-2026:90514-01](https://lwn.net/Articles/1105741/) | EL9.6 | ignition | 2026-11-06 |
| Red Hat | [RHSA-2026:91719-01](https://lwn.net/Articles/1105735/) | EL9.8 | ignition | 2026-11-06 |
| Red Hat | [RHSA-2026:98634-01](https://lwn.net/Articles/1106680/) | EL10 | nginx | 2026-11-11 |
| Red Hat | [RHSA-2026:98529-01](https://lwn.net/Articles/1106681/) | EL9 | nginx | 2026-11-11 |
| Red Hat | [RHSA-2026:98671-01](https://lwn.net/Articles/1106679/) | EL8 | nginx:1.24 | 2026-11-11 |
| Red Hat | [RHSA-2026:98528-01](https://lwn.net/Articles/1106677/) | EL9 | nginx:1.24 | 2026-11-11 |
| Red Hat | [RHSA-2026:98527-01](https://lwn.net/Articles/1106682/) | EL9 | nginx:1.26 | 2026-11-11 |
| Red Hat | [RHSA-2026:98403-01](https://lwn.net/Articles/1106731/) | EL10 | oci-delta | 2026-11-11 |
| Red Hat | [RHSA-2026:95016-01](https://lwn.net/Articles/1105732/) | EL10.0 | opentelemetry-collector | 2026-11-06 |
| Red Hat | [RHSA-2026:95015-01](https://lwn.net/Articles/1105733/) | EL9.4 | opentelemetry-collector | 2026-11-06 |
| Red Hat | [RHSA-2026:95014-01](https://lwn.net/Articles/1105731/) | EL9.6 | opentelemetry-collector | 2026-11-06 |
| Red Hat | [RHSA-2026:96076-01](https://lwn.net/Articles/1106115/) | EL8.4 | osbuild-composer | 2026-11-09 |
| Red Hat | [RHSA-2026:90493-01](https://lwn.net/Articles/1105738/) | EL8.6 | osbuild-composer | 2026-11-06 |
| Red Hat | [RHSA-2026:90363-01](https://lwn.net/Articles/1105744/) | EL8.8 | osbuild-composer | 2026-11-06 |
| Red Hat | [RHSA-2026:19008-01](https://lwn.net/Articles/1105472/) | EL10 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:10713-01](https://lwn.net/Articles/1105482/) | EL10 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11470-01](https://lwn.net/Articles/1105481/) | EL10.0 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11493-01](https://lwn.net/Articles/1105478/) | EL8.4 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11494-01](https://lwn.net/Articles/1105474/) | EL8.6 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11495-01](https://lwn.net/Articles/1105476/) | EL8.8 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:19167-01](https://lwn.net/Articles/1105473/) | EL9 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:10710-01](https://lwn.net/Articles/1105475/) | EL9 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11454-01](https://lwn.net/Articles/1105483/) | EL9.0 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11469-01](https://lwn.net/Articles/1105480/) | EL9.2 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11516-01](https://lwn.net/Articles/1105477/) | EL9.4 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:11471-01](https://lwn.net/Articles/1105479/) | EL9.6 | pcs | 2026-11-05 |
| Red Hat | [RHSA-2026:98554-01](https://lwn.net/Articles/1106720/) | EL10 | podman | 2026-11-11 |
| Red Hat | [RHSA-2026:98447-01](https://lwn.net/Articles/1106727/) | EL9 | podman | 2026-11-11 |
| Red Hat | [RHSA-2026:98641-01](https://lwn.net/Articles/1106667/) | EL10 | python-oauthlib | 2026-11-11 |
| Red Hat | [RHSA-2026:98118-01](https://lwn.net/Articles/1106669/) | EL8.6 | python-oauthlib | 2026-11-11 |
| Red Hat | [RHSA-2026:93077-01](https://lwn.net/Articles/1105721/) | EL8 | python-pillow | 2026-11-06 |
| Red Hat | [RHSA-2026:85239-01](https://lwn.net/Articles/1106687/) | EL8 | python3 | 2026-11-11 |
| Red Hat | [RHSA-2026:98615-01](https://lwn.net/Articles/1106684/) | EL10 | python3.12 | 2026-11-11 |
| Red Hat | [RHSA-2026:98511-01](https://lwn.net/Articles/1106685/) | EL9 | python3.9 | 2026-11-11 |
| Red Hat | [RHSA-2026:89742-01](https://lwn.net/Articles/1106686/) | EL9 | python3.9 | 2026-11-11 |
| Red Hat | [RHSA-2026:98103-01](https://lwn.net/Articles/1106638/) | EL8 | qt5-qtbase | 2026-11-11 |
| Red Hat | [RHSA-2026:98535-01](https://lwn.net/Articles/1106639/) | EL9 | qt5-qtbase | 2026-11-11 |
| Red Hat | [RHSA-2026:98636-01](https://lwn.net/Articles/1106636/) | EL10 | qt6-qtbase | 2026-11-11 |
| Red Hat | [RHSA-2026:98614-01](https://lwn.net/Articles/1106715/) | EL10 | rhc | 2026-11-11 |
| Red Hat | [RHSA-2026:98794-01](https://lwn.net/Articles/1106710/) | EL7 | rhc | 2026-11-11 |
| Red Hat | [RHSA-2026:98506-01](https://lwn.net/Articles/1106721/) | EL9 | rhc | 2026-11-11 |
| Red Hat | [RHSA-2026:98451-01](https://lwn.net/Articles/1106725/) | EL9 | runc | 2026-11-11 |
| Red Hat | [RHSA-2026:98556-01](https://lwn.net/Articles/1106718/) | EL10 | skopeo | 2026-11-11 |
| Red Hat | [RHSA-2026:98448-01](https://lwn.net/Articles/1106728/) | EL9 | skopeo | 2026-11-11 |
| Red Hat | [RHSA-2026:98643-01](https://lwn.net/Articles/1106668/) | EL10 | squid | 2026-11-11 |
| Red Hat | [RHSA-2026:98537-01](https://lwn.net/Articles/1106671/) | EL9 | squid | 2026-11-11 |
| Red Hat | [RHSA-2026:96078-01](https://lwn.net/Articles/1106670/) | EL8 | squid:4 | 2026-11-11 |
| Red Hat | [RHSA-2026:95085-01](https://lwn.net/Articles/1106692/) | EL10 | tesseract | 2026-11-11 |
| Red Hat | [RHSA-2026:98624-01](https://lwn.net/Articles/1106688/) | EL10 | tesseract | 2026-11-11 |
| Red Hat | [RHSA-2026:95725-01](https://lwn.net/Articles/1106693/) | EL8 | tesseract | 2026-11-11 |
| Red Hat | [RHSA-2026:96239-01](https://lwn.net/Articles/1106689/) | EL8.6 | tesseract | 2026-11-11 |
| Red Hat | [RHSA-2026:96238-01](https://lwn.net/Articles/1106690/) | EL8.8 | tesseract | 2026-11-11 |
| Red Hat | [RHSA-2026:95086-01](https://lwn.net/Articles/1106691/) | EL9 | tesseract | 2026-11-11 |
| Red Hat | [RHSA-2026:98630-01](https://lwn.net/Articles/1106637/) | EL10 | util-linux | 2026-11-11 |
| Red Hat | [RHSA-2026:93461-01](https://lwn.net/Articles/1106641/) | EL10 | util-linux | 2026-11-11 |
| Red Hat | [RHSA-2026:96212-01](https://lwn.net/Articles/1106642/) | EL8 | util-linux | 2026-11-11 |
| Red Hat | [RHSA-2026:98519-01](https://lwn.net/Articles/1106640/) | EL9 | util-linux | 2026-11-11 |
| Red Hat | [RHSA-2026:98635-01](https://lwn.net/Articles/1106628/) | EL10 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:91626-01](https://lwn.net/Articles/1106630/) | EL10.0 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:90523-01](https://lwn.net/Articles/1106634/) | EL10.2 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:98530-01](https://lwn.net/Articles/1106629/) | EL9 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:91624-01](https://lwn.net/Articles/1106632/) | EL9.2 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:91623-01](https://lwn.net/Articles/1106631/) | EL9.4 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:91625-01](https://lwn.net/Articles/1106633/) | EL9.6 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:90522-01](https://lwn.net/Articles/1106635/) | EL9.8 | xdg-dbus-proxy | 2026-11-11 |
| Red Hat | [RHSA-2026:91138-01](https://lwn.net/Articles/1105736/) | EL10 | yggdrasil | 2026-11-06 |
| Red Hat | [RHSA-2026:98617-01](https://lwn.net/Articles/1106714/) | EL10 | yggdrasil | 2026-11-11 |
| Red Hat | [RHSA-2026:91572-01](https://lwn.net/Articles/1105737/) | EL10.0 | yggdrasil | 2026-11-06 |
| Slackware | [SSA:2026-310-01](https://lwn.net/Articles/1106232/) |  | httpd | 2026-11-06 |
| Slackware | [SSA:2026-313-01](https://lwn.net/Articles/1106446/) |  | krb5 | 2026-11-09 |
| Slackware | [SSA:2026-309-01](https://lwn.net/Articles/1105845/) |  | openssh | 2026-11-05 |
| Slackware | [SSA:2026-308-01](https://lwn.net/Articles/1105607/) |  | rsync | 2026-11-04 |
| Slackware | [SSA:2026-314-01](https://lwn.net/Articles/1106807/) |  | xorg-server | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5095-1](https://lwn.net/Articles/1105618/) | SLE15 oS15.6 | GraphicsMagick | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5157-1](https://lwn.net/Articles/1106825/) | SLE15 oS15.6 | GraphicsMagick | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5141-1](https://lwn.net/Articles/1106472/) | SLE12 | PackageKit | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5142-1](https://lwn.net/Articles/1106469/) | SLE15 oS15.4 | PackageKit | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5144-1](https://lwn.net/Articles/1106470/) | SLE15 oS15.5 | PackageKit | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5143-1](https://lwn.net/Articles/1106471/) | SLE15 oS15.6 | PackageKit | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5158-1](https://lwn.net/Articles/1106855/) | SLE15 oS15.3 | SDL2\_image | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22241-1](https://lwn.net/Articles/1106808/) | oS16.0 | aliyun-cli | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12208-1](https://lwn.net/Articles/1105608/) | TW | amazon-cloudwatch-agent | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12267-1](https://lwn.net/Articles/1106809/) | TW | amazon-cloudwatch-agent | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5185-1](https://lwn.net/Articles/1106810/) | SLE15 oS15.4 | ansible-core | 2026-11-11 |
| SUSE | [SUSE-SU-2026:24618-1](https://lwn.net/Articles/1106447/) | SLE16.1 | ansible-core | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5099-1](https://lwn.net/Articles/1105609/) | SLE12 | apache2 | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24540-1](https://lwn.net/Articles/1106449/) | SLE16.1 | apr-util | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22232-1](https://lwn.net/Articles/1106448/) | oS16.1 | apr-util | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5163-1](https://lwn.net/Articles/1106811/) | SLE12 | aspell | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5134-1](https://lwn.net/Articles/1106450/) | SLE15 | aspell | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5101-1](https://lwn.net/Articles/1105610/) | SLE15 oS15.6 | aws-efs-utils | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12268-1](https://lwn.net/Articles/1106812/) | TW | azure-storage-azcopy | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5161-1](https://lwn.net/Articles/1106813/) | SLE12 | bind | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5118-1](https://lwn.net/Articles/1105846/) | SLE5.0 SLE5.1 SLE5.2 SLE5.3 SLE5.4 SLE5.5 SLE-m5.0 SLE-m5.1 SLE-m5.2 SLE-m5.3 SLE-m5.4 SLE-m5.5 | bind | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12231-1](https://lwn.net/Articles/1106233/) | TW | bind | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24556-1](https://lwn.net/Articles/1105847/) | SLE-m6.1 | brotli | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24518-1](https://lwn.net/Articles/1105611/) | SLE-m6.2 | brotli | 2026-11-04 |
| SUSE | [SUSE-SU-2026:24601-1](https://lwn.net/Articles/1106234/) | SLE16.0 | brotli | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12232-1](https://lwn.net/Articles/1106235/) | TW | brotli | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:12260-1](https://lwn.net/Articles/1106451/) | TW | buildpacks-cli | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12233-1](https://lwn.net/Articles/1106236/) | TW | ca-certificates-mozilla | 2026-11-07 |
| SUSE | [SUSE-SU-2026:5111-1](https://lwn.net/Articles/1105612/) | SLE15 | cephfs | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12234-1](https://lwn.net/Articles/1106237/) | TW | chromedriver | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:12235-1](https://lwn.net/Articles/1106238/) | TW | containerized-data-importer1.65-api | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:12209-1](https://lwn.net/Articles/1105613/) | TW | coredns | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12248-1](https://lwn.net/Articles/1106239/) | TW | corepack24 | 2026-11-08 |
| SUSE | [SUSE-SU-2026:5123-1](https://lwn.net/Articles/1105848/) | SLE15 oS15.6 | cpupower | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12210-1](https://lwn.net/Articles/1105614/) | TW | cramfs-tools | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5183-1](https://lwn.net/Articles/1106814/) | SLE12 | cups | 2026-11-11 |
| SUSE | [openSUSE-SU-2026:12269-1](https://lwn.net/Articles/1106815/) | TW | dlib-devel | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5182-1](https://lwn.net/Articles/1106816/) | SLE12 | docker | 2026-11-11 |
| SUSE | [openSUSE-SU-2026:12236-1](https://lwn.net/Articles/1106240/) | TW | docker-compose | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:22257-1](https://lwn.net/Articles/1106817/) | oS16.0 | dolphin | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5184-1](https://lwn.net/Articles/1106818/) | SLE15 oS15.6 | dpdk | 2026-11-11 |
| SUSE | [SUSE-SU-2026:5135-1](https://lwn.net/Articles/1106452/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | dpdk22 | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:22263-1](https://lwn.net/Articles/1106819/) | oS16.0 | evolution | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24554-1](https://lwn.net/Articles/1105849/) | SLE-m6.1 | expat | 2026-11-06 |
| SUSE | [SUSE-SU-2026:5174-1](https://lwn.net/Articles/1106820/) | SLE12 | firefox | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5145-1](https://lwn.net/Articles/1106454/) | SLE15 oS15.4 | firefox | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12259-1](https://lwn.net/Articles/1106453/) | TW | firefox | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12211-1](https://lwn.net/Articles/1105615/) | TW | firefox-esr | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12270-1](https://lwn.net/Articles/1106821/) | TW | flannel | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5127-1](https://lwn.net/Articles/1106241/) | SLE15 oS15.5 | flatpak | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24519-1](https://lwn.net/Articles/1105616/) | SLE-m6.2 | fuse-overlayfs | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5124-1](https://lwn.net/Articles/1105850/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 SES7.1 | fuse-overlayfs | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24603-1](https://lwn.net/Articles/1106242/) | SLE16.0 | fuse-overlayfs | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12225-1](https://lwn.net/Articles/1106243/) | TW | fuse-overlayfs | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:22234-1](https://lwn.net/Articles/1106822/) | oS16.0 | fuse-overlayfs | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5094-1](https://lwn.net/Articles/1105617/) | SLE12 | ghostscript | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12261-1](https://lwn.net/Articles/1106455/) | TW | git-bug | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12237-1](https://lwn.net/Articles/1106244/) | TW | git-lfs | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:12238-1](https://lwn.net/Articles/1106245/) | TW | gitoxide | 2026-11-07 |
| SUSE | [SUSE-SU-2026:4348-2](https://lwn.net/Articles/1106456/) | SLE12 | glib2 | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22255-1](https://lwn.net/Articles/1106823/) | oS16.0 | gnome-podcasts | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12212-1](https://lwn.net/Articles/1105851/) | TW | go1.26 | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12239-1](https://lwn.net/Articles/1106246/) | TW | go1.27 | 2026-11-07 |
| SUSE | [SUSE-SU-2026:24604-1](https://lwn.net/Articles/1106247/) | SLE16.0 | google-cloud-sap-agent | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24616-1](https://lwn.net/Articles/1106457/) | SLE16.1 | google-cloud-sap-agent | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22236-1](https://lwn.net/Articles/1106824/) | oS16.0 | google-cloud-sap-agent | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24555-1](https://lwn.net/Articles/1105852/) | SLE-m6 SLE-m6.1 | google-guest-agent | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12240-1](https://lwn.net/Articles/1106248/) | TW | google-guest-agent | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:12226-1](https://lwn.net/Articles/1106249/) | TW | gotosocial | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:22239-1](https://lwn.net/Articles/1106826/) | oS16.0 | graphicsmagick | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5170-1](https://lwn.net/Articles/1106828/) | MP4.3 SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | haproxy | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5171-1](https://lwn.net/Articles/1106827/) | SLE15 oS15.6 | haproxy | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24615-1](https://lwn.net/Articles/1106458/) | SLE16.1 | haproxy | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5119-1](https://lwn.net/Articles/1105853/) | SLE15 SLE5.5 SLE-m5.5 | helm | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12213-1](https://lwn.net/Articles/1105854/) | TW | ibus-typing-booster | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12262-1](https://lwn.net/Articles/1106829/) | TW | istioctl | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24541-1](https://lwn.net/Articles/1106459/) | SLE16.1 | jsoup | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5121-1](https://lwn.net/Articles/1105857/) | SLE12 | kernel | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24648-1](https://lwn.net/Articles/1106830/) | SLE16.0 SLE-m6.2 | kernel | 2026-11-11 |
| SUSE | [SUSE-SU-2026:24543-1](https://lwn.net/Articles/1106460/) | SLE16.1 | kernel | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24549-1](https://lwn.net/Articles/1105855/) | SLE6.0 SLE-m6.0 | kernel | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24550-1](https://lwn.net/Articles/1105856/) | SLE6.0 SLE-m6.0 | kernel | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24553-1](https://lwn.net/Articles/1105858/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-11-06 |
| SUSE | [SUSE-SU-2026:5136-1](https://lwn.net/Articles/1106461/) | SLE12 | krb5 | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5167-1](https://lwn.net/Articles/1106831/) | SLE15 | kubevirt | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12227-1](https://lwn.net/Articles/1106250/) | TW | kubevirt1.8 | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12241-1](https://lwn.net/Articles/1106251/) | TW | kubevirt1.8-container-disk | 2026-11-07 |
| SUSE | [openSUSE-SU-2026:12242-1](https://lwn.net/Articles/1106252/) | TW | kubevirt1.9-container-disk | 2026-11-08 |
| SUSE | [openSUSE-SU-2026:12271-1](https://lwn.net/Articles/1106832/) | TW | kured | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12214-1](https://lwn.net/Articles/1105859/) | TW | kyverno | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24552-1](https://lwn.net/Articles/1105862/) | SLE-m6.1 | libX11 | 2026-11-06 |
| SUSE | [SUSE-SU-2026:5166-1](https://lwn.net/Articles/1106835/) | SLE12 | libXi | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5165-1](https://lwn.net/Articles/1106834/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | libXi | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24545-1](https://lwn.net/Articles/1106466/) | SLE16.1 | libXtst | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5131-1](https://lwn.net/Articles/1106462/) | SLE15 | libjxl | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12245-1](https://lwn.net/Articles/1106253/) | TW | libmariadbd-devel | 2026-11-08 |
| SUSE | [openSUSE-SU-2026:12215-1](https://lwn.net/Articles/1105860/) | TW | libmodplug-devel | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12229-1](https://lwn.net/Articles/1106254/) | TW | libntpc1 | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12249-1](https://lwn.net/Articles/1106255/) | TW | libopenscap33 | 2026-11-08 |
| SUSE | [openSUSE-SU-2026:12203-1](https://lwn.net/Articles/1105619/) | TW | libpolkit-agent-1-0-128 | 2026-11-04 |
| SUSE | [SUSE-SU-2026:24557-1](https://lwn.net/Articles/1105861/) | SLE-m6.1 | librsvg | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24546-1](https://lwn.net/Articles/1106463/) | SLE16.1 | librsvg | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12252-1](https://lwn.net/Articles/1106464/) | TW | libruby4\_0-4\_0 | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12243-1](https://lwn.net/Articles/1106256/) | TW | libsndfile-devel | 2026-11-08 |
| SUSE | [SUSE-SU-2026:24515-1](https://lwn.net/Articles/1105620/) | SLE-m6.2 | libsoup | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12222-1](https://lwn.net/Articles/1106257/) | TW | libspice-server-devel | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12244-1](https://lwn.net/Articles/1106258/) | TW | libtirpc-devel | 2026-11-08 |
| SUSE | [openSUSE-SU-2026:12257-1](https://lwn.net/Articles/1106465/) | TW | libunbound8 | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12266-1](https://lwn.net/Articles/1106833/) | TW | libvips-devel | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12228-1](https://lwn.net/Articles/1106259/) | TW | matomo | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12246-1](https://lwn.net/Articles/1106260/) | TW | mihomo | 2026-11-08 |
| SUSE | [SUSE-SU-2026:5126-1](https://lwn.net/Articles/1106261/) | SLE12 | mozilla-nss | 2026-11-06 |
| SUSE | [SUSE-SU-2026:5168-1](https://lwn.net/Articles/1106836/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | mozilla-nss | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12247-1](https://lwn.net/Articles/1106262/) | TW | nano | 2026-11-08 |
| SUSE | [SUSE-SU-2026:24602-1](https://lwn.net/Articles/1106263/) | SLE16.0 | nmap | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24600-1](https://lwn.net/Articles/1106264/) | SLE16.0 | nodejs22 | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24548-1](https://lwn.net/Articles/1106467/) | SLE16.1 | nodejs24 | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24558-1](https://lwn.net/Articles/1105863/) | SLE-m6.1 | nvidia-open-driver-G06-signed | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12263-1](https://lwn.net/Articles/1106837/) | TW | nvidia-open-driver-G06-signed-check | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5097-1](https://lwn.net/Articles/1105622/) | SLE15 | nvidia-open-driver-G07-signed | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5096-1](https://lwn.net/Articles/1105621/) | SLE15 oS15.6 | nvidia-open-driver-G07-signed | 2026-11-04 |
| SUSE | [SUSE-SU-2026:24547-1](https://lwn.net/Articles/1106468/) | SLE16.1 | nvidia-open-driver-G07-signed | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12264-1](https://lwn.net/Articles/1106838/) | TW | okteto | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5172-1](https://lwn.net/Articles/1106839/) | SLE15 | openssl-1\_1 | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12216-1](https://lwn.net/Articles/1105864/) | TW | owntone | 2026-11-05 |
| SUSE | [SUSE-SU-2026:5117-1](https://lwn.net/Articles/1105865/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.3 | parted | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:22245-1](https://lwn.net/Articles/1106840/) | oS16.0 | pcre2 | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12217-1](https://lwn.net/Articles/1105866/) | TW | perl-Cpanel-JSON-XS | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12202-1](https://lwn.net/Articles/1105623/) | TW | perl-Dancer2 | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12250-1](https://lwn.net/Articles/1106265/) | TW | perl-Mozilla-CA | 2026-11-08 |
| SUSE | [SUSE-SU-2026:5120-1](https://lwn.net/Articles/1105868/) | SLE15 | perl-Text-CSV\_XS | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12218-1](https://lwn.net/Articles/1105867/) | TW | perl-Text-CSV\_XS | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24544-1](https://lwn.net/Articles/1106473/) | SLE16.1 | perl-XS-Parse-Keyword | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12219-1](https://lwn.net/Articles/1105869/) | TW | php8 | 2026-11-05 |
| SUSE | [SUSE-SU-2026:5175-1](https://lwn.net/Articles/1106841/) | SLE12 | poppler, poppler-qt, poppler-qt5 | 2026-11-11 |
| SUSE | [SUSE-SU-2026:5176-1](https://lwn.net/Articles/1106842/) | SLE15 | poppler, poppler-qt5 | 2026-11-11 |
| SUSE | [SUSE-SU-2026:5133-1](https://lwn.net/Articles/1106474/) | SLE15 oS15.6 | poppler | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5181-1](https://lwn.net/Articles/1106843/) | SLE15 oS15.6 | proftpd | 2026-11-11 |
| SUSE | [openSUSE-SU-2026:22261-1](https://lwn.net/Articles/1106844/) | oS16.0 | psqlodbc | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5125-1](https://lwn.net/Articles/1105870/) | SLE15 oS15.4 | python-Brotli | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24597-1](https://lwn.net/Articles/1106266/) | SLE16.0 | python-Brotli | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24542-1](https://lwn.net/Articles/1106476/) | SLE16.1 | python-Brotli | 2026-11-10 |
| SUSE | [SUSE-SU-2026:24596-1](https://lwn.net/Articles/1106267/) | SLE16.0 | python-CairoSVG | 2026-11-06 |
| SUSE | [SUSE-SU-2026:5177-1](https://lwn.net/Articles/1106846/) | SLE12 | python-M2Crypto | 2026-11-11 |
| SUSE | [SUSE-SU-2026:5093-1](https://lwn.net/Articles/1105624/) | SLE12 | python-PyJWT | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5137-1](https://lwn.net/Articles/1106475/) | SLE12 | python | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5130-1](https://lwn.net/Articles/1106268/) | MP4.3 SLE15 oS15.4 | python-certifi | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:22258-1](https://lwn.net/Articles/1106845/) | oS16.0 | python-graphql-core | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22246-1](https://lwn.net/Articles/1106847/) | oS16.0 | python-pillow | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5164-1](https://lwn.net/Articles/1106848/) | SLE15 | python-soupsieve | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22252-1](https://lwn.net/Articles/1106849/) | oS16.0 | python-urllib3\_1 | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12230-1](https://lwn.net/Articles/1106269/) | TW | python313-Pillow | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12251-1](https://lwn.net/Articles/1106270/) | TW | python313-Pillow | 2026-11-08 |
| SUSE | [openSUSE-SU-2026:12204-1](https://lwn.net/Articles/1105625/) | TW | python313-joserfc | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:12265-1](https://lwn.net/Articles/1106850/) | TW | python313-wyoming | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22256-1](https://lwn.net/Articles/1106851/) | oS16.0 | qt6-coap | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12220-1](https://lwn.net/Articles/1105871/) | TW | regclient | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12221-1](https://lwn.net/Articles/1105872/) | TW | roundcubemail | 2026-11-05 |
| SUSE | [SUSE-SU-2026:5122-1](https://lwn.net/Articles/1105873/) | SLE15 oS15.4 | rsyslog | 2026-11-05 |
| SUSE | [SUSE-SU-2026:5100-1](https://lwn.net/Articles/1105626/) | SLE15 oS15.6 | rsyslog | 2026-11-05 |
| SUSE | [SUSE-SU-2026:24598-1](https://lwn.net/Articles/1106271/) | SLE16.0 | rsyslog | 2026-11-06 |
| SUSE | [SUSE-SU-2026:24613-1](https://lwn.net/Articles/1106477/) | SLE16.1 | rsyslog | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22249-1](https://lwn.net/Articles/1106852/) | oS16.0 | rust-keylime | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5162-1](https://lwn.net/Articles/1106853/) | SLE12 | sbc | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22254-1](https://lwn.net/Articles/1106854/) | oS16.0 | scribus | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12223-1](https://lwn.net/Articles/1106272/) | TW | stgit | 2026-11-06 |
| SUSE | [openSUSE-SU-2026:12205-1](https://lwn.net/Articles/1105627/) | TW | switcheroo | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5160-1](https://lwn.net/Articles/1106856/) | SLE15 SLE5.4 SLE5.5 SLE-m5.4 SLE-m5.5 | tar | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12253-1](https://lwn.net/Articles/1106478/) | TW | tekton-cli | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5169-1](https://lwn.net/Articles/1106857/) | MP4.3 SLE15 | terraform-provider-susepubliccloud | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22243-1](https://lwn.net/Articles/1106858/) | SLE6.12.0 oS16.0 | the linux kernel (live patch 18 for suse linux | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12224-1](https://lwn.net/Articles/1106273/) | TW | thunderbird | 2026-11-06 |
| SUSE | [SUSE-SU-2026:5116-1](https://lwn.net/Articles/1105874/) | SLE15 | tomcat | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12254-1](https://lwn.net/Articles/1106479/) | TW | tomcat | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12255-1](https://lwn.net/Articles/1106480/) | TW | tomcat10 | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12256-1](https://lwn.net/Articles/1106481/) | TW | tomcat11 | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:12206-1](https://lwn.net/Articles/1105628/) | TW | trivy | 2026-11-04 |
| SUSE | [openSUSE-SU-2026:22233-1](https://lwn.net/Articles/1106482/) | oS16.1 | trivy | 2026-11-09 |
| SUSE | [SUSE-SU-2026:24539-1](https://lwn.net/Articles/1106484/) | SLE16.1 | udisks2 | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:22231-1](https://lwn.net/Articles/1106483/) | oS16.1 | udisks2 | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5092-1](https://lwn.net/Articles/1105629/) | SLE15 | valkey | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5102-1](https://lwn.net/Articles/1105630/) | SLE15 oS15.6 | valkey | 2026-11-05 |
| SUSE | [openSUSE-SU-2026:12207-1](https://lwn.net/Articles/1105631/) | TW | vexctl | 2026-11-04 |
| SUSE | [SUSE-SU-2026:5156-1](https://lwn.net/Articles/1106860/) | SLE12 | vsftpd | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5155-1](https://lwn.net/Articles/1106859/) | SLE15 oS15.6 | vsftpd | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5098-1](https://lwn.net/Articles/1105632/) | SLE15 oS15.5 | xdg-desktop-portal | 2026-11-05 |
| SUSE | [SUSE-SU-2026:5139-1](https://lwn.net/Articles/1106486/) | SLE12 | xen | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5159-1](https://lwn.net/Articles/1106861/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | xen | 2026-11-10 |
| SUSE | [SUSE-SU-2026:5140-1](https://lwn.net/Articles/1106485/) | SLE15 oS15.6 | xen | 2026-11-09 |
| SUSE | [SUSE-SU-2026:5178-1](https://lwn.net/Articles/1106863/) | SLE12 | xorg-x11-server | 2026-11-11 |
| SUSE | [SUSE-SU-2026:5180-1](https://lwn.net/Articles/1106862/) | SLE15 oS15.4 | xorg-x11-server | 2026-11-11 |
| SUSE | [SUSE-SU-2026:5138-1](https://lwn.net/Articles/1106487/) | SLE15 | zchunk | 2026-11-09 |
| SUSE | [openSUSE-SU-2026:22250-1](https://lwn.net/Articles/1106864/) | oS16.0 | zchunk | 2026-11-10 |
| SUSE | [openSUSE-SU-2026:12258-1](https://lwn.net/Articles/1106488/) | TW | zk | 2026-11-09 |
| Ubuntu | [USN-9016-1](https://lwn.net/Articles/1106489/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | apache2 | 2026-11-10 |
| Ubuntu | [USN-8996-1](https://lwn.net/Articles/1105633/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | apt | 2026-11-04 |
| Ubuntu | [USN-9001-2](https://lwn.net/Articles/1106490/) | 18.04 20.04 | ca-certificates | 2026-11-09 |
| Ubuntu | [USN-9001-1](https://lwn.net/Articles/1105875/) | 22.04 24.04 26.04 26.10 | ca-certificates | 2026-11-05 |
| Ubuntu | [USN-9036-1](https://lwn.net/Articles/1106865/) | 22.04 24.04 26.04 26.10 | ca-certificates-java | 2026-11-10 |
| Ubuntu | [USN-9013-1](https://lwn.net/Articles/1106491/) | 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | fetchmail | 2026-11-09 |
| Ubuntu | [USN-9007-1](https://lwn.net/Articles/1106492/) | 24.04 26.04 26.10 | freerdp3 | 2026-11-09 |
| Ubuntu | [USN-7230-3](https://lwn.net/Articles/1105876/) | 20.04 22.04 24.04 | frr | 2026-11-05 |
| Ubuntu | [USN-9038-1](https://lwn.net/Articles/1106866/) | 16.04 18.04 20.04 22.04 26.10 | gst-plugins-good1.0, gst-plugins-base1.0 | 2026-11-10 |
| Ubuntu | [USN-8972-2](https://lwn.net/Articles/1105877/) | 22.04 | haproxy | 2026-11-05 |
| Ubuntu | [USN-9037-1](https://lwn.net/Articles/1106867/) | 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | hplip | 2026-11-10 |
| Ubuntu | [USN-9035-1](https://lwn.net/Articles/1106493/) | 14.04 | kernel | 2026-11-10 |
| Ubuntu | [USN-9017-1](https://lwn.net/Articles/1106494/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | libgphoto2 | 2026-11-10 |
| Ubuntu | [USN-9012-1](https://lwn.net/Articles/1106495/) | 26.04 | libheif | 2026-11-09 |
| Ubuntu | [USN-9008-1](https://lwn.net/Articles/1106496/) | 22.04 24.04 26.04 26.10 | libnfs | 2026-11-09 |
| Ubuntu | [USN-7530-2](https://lwn.net/Articles/1105634/) | 16.04 18.04 20.04 22.04 24.04 | libphp-adodb | 2026-11-04 |
| Ubuntu | [USN-8890-3](https://lwn.net/Articles/1106497/) | 24.04 26.04 26.10 | libsoup3 | 2026-11-09 |
| Ubuntu | [USN-9027-1](https://lwn.net/Articles/1106498/) | 20.04 22.04 | linux, linux-aws, linux-aws-5.15, linux-aws-fips, linux-azure, linux-azure-5.15, linux-azure-fde-5.15, linux-azure-fips, linux-gcp, linux-gcp-5.15, linux-gcp-fips, linux-gke, linux-gkeop, linux-hwe-5.15, linux-ibm, linux-ibm-5.15, linux-intel-iot-realtime, linux-intel-iotg, linux-intel-iotg-5.15, linux-kvm, linux-lowlatency, linux-lowlatency-hwe-5.15, linux-nvidia, linux-nvidia-tegra, linux-nvidia-tegra-5.15, linux-oracle, linux-oracle-5.15, linux-realtime | 2026-11-10 |
| Ubuntu | [USN-9032-1](https://lwn.net/Articles/1106499/) | 14.04 16.04 18.04 | linux, linux-aws, linux-aws-fips, linux-aws-hwe, linux-azure, linux-azure-4.15, linux-azure-fips, linux-fips, linux-gcp, linux-gcp-4.15, linux-gcp-fips, linux-hwe, linux-kvm, linux-oracle | 2026-11-10 |
| Ubuntu | [USN-9030-1](https://lwn.net/Articles/1106500/) | 18.04 20.04 | linux, linux-aws, linux-aws-fips, linux-azure, linux-azure-5.4, linux-azure-fips, linux-bluefield, linux-fips, linux-gcp, linux-gcp-5.4, linux-gcp-fips, linux-hwe-5.4, linux-ibm, linux-ibm-5.4, linux-iot, linux-kvm, linux-oracle, linux-oracle-5.4, linux-xilinx-zynqmp | 2026-11-10 |
| Ubuntu | [USN-9022-1](https://lwn.net/Articles/1106501/) | 24.04 | linux, linux-aws, linux-azure, linux-azure-fips, linux-gcp, linux-gke, linux-ibm, linux-lowlatency, linux-oracle, linux-vmware | 2026-11-10 |
| Ubuntu | [USN-9018-1](https://lwn.net/Articles/1106502/) | 26.04 | linux, linux-aws, linux-gcp, linux-ibm, linux-oem-7.0, linux-oracle | 2026-11-10 |
| Ubuntu | [USN-9033-1](https://lwn.net/Articles/1106503/) | 14.04 16.04 | linux, linux-aws, linux-kvm, linux-lts-xenial | 2026-11-10 |
| Ubuntu | [USN-9034-1](https://lwn.net/Articles/1106504/) | 14.04 | linux-aws | 2026-11-10 |
| Ubuntu | [USN-9031-1](https://lwn.net/Articles/1106505/) | 18.04 20.04 | linux-aws-5.4, linux-raspi, linux-raspi-5.4 | 2026-11-10 |
| Ubuntu | [USN-9024-1](https://lwn.net/Articles/1106506/) | 22.04 24.04 | linux-aws-6.8, linux-gcp-6.8, linux-ibm-6.8, linux-lowlatency-hwe-6.8, linux-nvidia, linux-realtime-6.8 | 2026-11-10 |
| Ubuntu | [USN-9020-1](https://lwn.net/Articles/1106507/) | 24.04 26.04 | linux-aws-7.0, linux-azure-fde, linux-azure-fde-7.0, linux-gcp-7.0, linux-gke, linux-oracle-7.0, linux-realtime | 2026-11-10 |
| Ubuntu | [USN-9023-1](https://lwn.net/Articles/1106508/) | 24.04 | linux-aws-fips, linux-gcp-fips, linux-gkeop, linux-realtime | 2026-11-10 |
| Ubuntu | [USN-9019-1](https://lwn.net/Articles/1106509/) | 26.04 | linux-azure | 2026-11-10 |
| Ubuntu | [USN-9026-1](https://lwn.net/Articles/1106510/) | 22.04 | linux-azure-6.8, linux-azure-fde-6.8 | 2026-11-10 |
| Ubuntu | [USN-9028-1](https://lwn.net/Articles/1106511/) | 22.04 | linux-azure-fde | 2026-11-10 |
| Ubuntu | [USN-9039-1](https://lwn.net/Articles/1106868/) | 24.04 | linux-azure-fde | 2026-11-11 |
| Ubuntu | [USN-9043-1](https://lwn.net/Articles/1106869/) | 26.04 | linux-nvidia | 2026-11-11 |
| Ubuntu | [USN-9003-1](https://lwn.net/Articles/1105878/) | 24.04 26.04 | linux-nvidia-7.0, linux-nvidia-bos | 2026-11-06 |
| Ubuntu | [USN-9045-1](https://lwn.net/Articles/1106870/) | 24.04 | linux-nvidia-7.0 | 2026-11-11 |
| Ubuntu | [USN-9044-1](https://lwn.net/Articles/1106871/) | 26.04 | linux-nvidia-bos | 2026-11-11 |
| Ubuntu | [USN-9040-1](https://lwn.net/Articles/1106872/) | 24.04 | linux-nvidia-lowlatency | 2026-11-11 |
| Ubuntu | [USN-9002-1](https://lwn.net/Articles/1105879/) | 24.04 | linux-nvidia-tegra | 2026-11-06 |
| Ubuntu | [USN-9025-1](https://lwn.net/Articles/1106512/) | 22.04 24.04 | linux-oracle-6.8, linux-raspi, linux-raspi-realtime | 2026-11-10 |
| Ubuntu | [USN-9029-1](https://lwn.net/Articles/1106513/) | 22.04 | linux-raspi | 2026-11-10 |
| Ubuntu | [USN-8997-1](https://lwn.net/Articles/1105635/) | 22.04 24.04 26.04 | net-snmp | 2026-11-04 |
| Ubuntu | [USN-8955-2](https://lwn.net/Articles/1105880/) | 14.04 16.04 18.04 20.04 | nginx | 2026-11-05 |
| Ubuntu | [USN-9014-1](https://lwn.net/Articles/1106514/) | 18.04 20.04 22.04 24.04 26.04 26.10 | openjdk-17 | 2026-11-09 |
| Ubuntu | [USN-9015-1](https://lwn.net/Articles/1106515/) | 20.04 22.04 24.04 26.04 26.10 | openjdk-21 | 2026-11-09 |
| Ubuntu | [USN-9004-1](https://lwn.net/Articles/1106516/) | 22.04 24.04 26.04 26.10 | openjdk-25 | 2026-11-09 |
| Ubuntu | [USN-9005-1](https://lwn.net/Articles/1106517/) | 26.10 | openjdk-27 | 2026-11-09 |
| Ubuntu | [USN-9009-1](https://lwn.net/Articles/1106518/) | 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | openjdk-8 | 2026-11-09 |
| Ubuntu | [USN-9010-1](https://lwn.net/Articles/1106519/) | 18.04 20.04 22.04 24.04 26.04 26.10 | openjdk-lts | 2026-11-09 |
| Ubuntu | [USN-9006-1](https://lwn.net/Articles/1106520/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | perl | 2026-11-10 |
| Ubuntu | [USN-8999-1](https://lwn.net/Articles/1105636/) | 22.04 24.04 26.04 | pillow | 2026-11-04 |
| Ubuntu | [USN-9011-1](https://lwn.net/Articles/1106521/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | pyasn1 | 2026-11-09 |
| Ubuntu | [USN-8952-2](https://lwn.net/Articles/1106274/) | 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | python-tornado | 2026-11-06 |
| Ubuntu | [USN-8952-3](https://lwn.net/Articles/1106873/) | 16.04 18.04 20.04 22.04 24.04 26.04 26.10 | python-tornado | 2026-11-11 |
| Ubuntu | [USN-9041-1](https://lwn.net/Articles/1106874/) | 26.04 | rust-coreutils | 2026-11-11 |
| Ubuntu | [USN-8998-1](https://lwn.net/Articles/1105637/) | 26.04 | squid | 2026-11-04 |
| Ubuntu | [USN-9000-1](https://lwn.net/Articles/1105638/) | 22.04 24.04 26.04 26.10 | twisted | 2026-11-04 |
| Ubuntu | [USN-8946-2](https://lwn.net/Articles/1106875/) | 26.10 | unbound | 2026-11-11 |

[^security-operations]: 보안 업데이트 표는 CVE 영향 여부를 직접 판정하는 자료가 아닙니다. 배포판은 상위 버전 변경 없이 수정 사항을 backport하기도 하므로 단순 버전 문자열 비교 대신 해당 릴리스 공지와 설치된 패키지 상태를 함께 확인해야 합니다. 이 표는 2026년 11월 당시의 주간 스냅샷이며, 현재 시스템의 취약성 판정이나 최신 패치 목록을 대신하지 않습니다.


---

## 요약

- 커널 릴리스 목록과 분야별 패치 메타데이터를 함께 담았습니다. 목록에 실렸다는 사실만으로 패치가 병합되었거나 특정 릴리스에 포함되었다고 판단할 수는 없습니다.[^patches-status]
- BPF 검증기·JIT, 스케줄링, 빌드 및 추적 도구의 변경을 다룹니다. 제목의 개선·검증 표현은 이 문서에서 시험 결과를 확인했다는 뜻이 아닙니다.[^patches-tests]
- 라이브 업데이트, ioctl 및 ABI 호환성 관련 제안은 인터페이스와 상태 보존 조건을 함께 살펴볼 대상입니다.[^patches-abi]
- 메모리 관리에는 THP·스왑·RSS·folio 변경이, 네트워킹에는 TLS 키 갱신·QUIC 기반 구조·TCP 페이로드 변경이 포함됩니다.[^patches-mm][^patches-network]
- 키 관리·페이지 테이블 강화와 기밀 가상머신 관련 항목도 다룹니다. 보안 관련 제목만으로 취약점 수정 여부나 보호 범위를 확정하지 않습니다.[^patches-security]

## 주목할 만한 커널 패치

### 커널 릴리스

Greg Kroah-Hartman
[Linux 7.3.3](https://lwn.net/Articles/1105903/)  — 리눅스 7.3.3
Nov 06

Greg Kroah-Hartman
[Linux 7.3.2](https://lwn.net/Articles/1105900/)  — 리눅스 7.3.2
Nov 06

Greg Kroah-Hartman
[Linux 6.18.62](https://lwn.net/Articles/1105904/)  — 리눅스 6.18.62
Nov 06

Greg Kroah-Hartman
[Linux 6.18.61](https://lwn.net/Articles/1105901/)  — 리눅스 6.18.61
Nov 06

Greg Kroah-Hartman
[Linux 6.12.116](https://lwn.net/Articles/1105905/)  — 리눅스 6.12.116
Nov 06

Greg Kroah-Hartman
[Linux 6.6.162](https://lwn.net/Articles/1105906/)  — 리눅스 6.6.162
Nov 06

Greg Kroah-Hartman
[Linux 6.1.192](https://lwn.net/Articles/1105907/)  — 리눅스 6.1.192
Nov 06

Greg Kroah-Hartman
[Linux 5.15.225](https://lwn.net/Articles/1105908/)  — 리눅스 5.15.225
Nov 06

Greg Kroah-Hartman
[Linux 5.10.274](https://lwn.net/Articles/1105909/)  — 리눅스 5.10.274
Nov 06

### 아키텍처별 변경

André Almeida
[syscalls: Add a shared table for all archs](https://lwn.net/Articles/1105713/)  — syscalls: 모든 아키텍처가 공유하는 테이블 추가
Nov 05

Melody Wang
[Alternate Injection: Secure Interrupt Delivery for SEV-SNP Guests - Guest Support](https://lwn.net/Articles/1105715/)  — 대체 주입: SEV-SNP 게스트에 안전하게 인터럽트 전달 — 게스트 지원
Nov 06

Matt Turner
[alpha/perf: add ProfileMe sampling](https://lwn.net/Articles/1105718/)  — alpha/perf: ProfileMe 샘플링 추가
Nov 05

Steffen Eiden
[KVM: arm64 on s390 System Register Handling](https://lwn.net/Articles/1106276/)  — KVM: s390에서의 arm64 시스템 레지스터 처리
Nov 06

Himanshu Chauhan
[riscv: Introduce support for hardware break/watchpoints](https://lwn.net/Articles/1106292/)  — riscv: 하드웨어 중단점·감시점 지원 도입
Nov 07

Xu Yilun
[Enable TDX module extensions](https://lwn.net/Articles/1106877/)  — TDX 모듈 확장 활성화
Nov 11

Jinjie Ruan
[arm64: entry: Convert to Generic Entry](https://lwn.net/Articles/1106879/)  — arm64: entry: 공통 진입 처리로 전환
Nov 11

### BPF 관련

Ihor Solodrai
[bpftool: Per-record CO-RE attributes in the C dump](https://lwn.net/Articles/1105663/)  — bpftool: C 덤프에 레코드별 CO-RE 속성 표시
Nov 05

Abhishek Khade
[bpf: Add network namespace boundary inspection kfuncs](https://lwn.net/Articles/1105649/)  — bpf: 네트워크 네임스페이스 경계 검사 kfunc 추가
Nov 05

Alexei Starovoitov
[bpf: Check chains of calls over the call graph, allow 32 frames](https://lwn.net/Articles/1105661/)  — bpf: 호출 그래프의 호출 체인을 검사하고 32개 프레임 허용
Nov 04

Alexei Starovoitov
[bpf: A verifier that joins states](https://lwn.net/Articles/1105724/)  — bpf: 상태를 합치는 검증기
Nov 05

Daniel Borkmann
[bpf: Various arm64 BPF JIT improvements](https://lwn.net/Articles/1106307/)  — bpf: arm64 BPF JIT의 여러 개선
Nov 08

Siddharth Nayyar
[bpf: Support struct\_ops in light skeletons](https://lwn.net/Articles/1106286/)  — bpf: 경량 스켈레톤에서 struct_ops 지원
Nov 06

Anton Protopopov
[bpf: Add BTF ID sets for fmod\_ret targets](https://lwn.net/Articles/1106287/)  — bpf: fmod_ret 대상용 BTF ID 집합 추가
Nov 06

Alexei Starovoitov
[bpf: Find linked registers by scalar evolution, remove scalar ids](https://lwn.net/Articles/1106308/)  — bpf: 스칼라 진화 분석으로 연결된 레지스터를 찾고 스칼라 ID 제거
Nov 09

Emil Tsalapatis
[bpf libarena allocator improvements](https://lwn.net/Articles/1106533/)  — BPF libarena 할당기 개선
Nov 09

Anton Protopopov
[Auto-detect BPF fmodret targets](https://lwn.net/Articles/1106525/)  — BPF fmodret 대상 자동 감지
Nov 09

Kumar Kartikeya Dwivedi
[BPF kthreads and waitqueues](https://lwn.net/Articles/1106534/)  — BPF 커널 스레드와 대기 큐
Nov 10

Kumar Kartikeya Dwivedi
[Exceptions - Resource Cleanup - Redux](https://lwn.net/Articles/1106882/)  — 예외 — 자원 정리 — 재검토
Nov 11

### 빌드 시스템

Lorenzo Stoakes (ARM)
[kbuild: significantly speed up kernel builds](https://lwn.net/Articles/1105642/)  — kbuild: 커널 빌드 속도 대폭 향상
Nov 04

### 커널 핵심부

Pasha Tatashin
[liveupdate: Add LIVEUPDATE\_SESSION\_FREEZE ioctl](https://lwn.net/Articles/1105647/)  — liveupdate: LIVEUPDATE_SESSION_FREEZE ioctl 추가
Nov 05

Kunwu Chan
[hazptr: shared-scan kthread, drain-assist, and stall detector](https://lwn.net/Articles/1105641/)  — hazptr: 공유 스캔 커널 스레드, 드레인 보조 및 정체 감지기
Nov 05

David Woodhouse
[timekeeping: Reduce magnitude of ntp\_error](https://lwn.net/Articles/1105717/)  — timekeeping: ntp_error의 크기 축소
Nov 05

Vincent Guittot
[Improving latency of short slice tasks](https://lwn.net/Articles/1106275/)  — 짧은 타임 슬라이스 태스크의 지연 개선
Nov 06

Vincent Donnefort
[tracing/remotes: Add printk, dump\_on\_panic and boot parameters](https://lwn.net/Articles/1106280/)  — tracing/remotes: printk, dump_on_panic 및 부팅 매개변수 추가
Nov 06

Yuri Andriaccio
[Hierarchical Constant Bandwidth Server](https://lwn.net/Articles/1106524/)  — 계층형 고정 대역폭 서버
Nov 09

Yafang Shao
[BPF-based per-cgroup NUMA balancing mode selection](https://lwn.net/Articles/1106526/)  — BPF 기반 cgroup별 NUMA 밸런싱 모드 선택
Nov 10

Fernand Sieber
[sched/fair: cpu.max.runtime and idle refill for CPU credits](https://lwn.net/Articles/1106532/)  — sched/fair: CPU 크레딧용 cpu.max.runtime 및 유휴 시 재충전
Nov 10

David Matlack
[liveupdate: Preserve tmpfs files across Live Update](https://lwn.net/Articles/1106801/)  — liveupdate: 라이브 업데이트 전후에 tmpfs 파일 보존
Nov 11

Fernand Sieber
[sched/fair: cpu.max.runtime and idle refill for a burstable budget](https://lwn.net/Articles/1106881/)  — sched/fair: 버스트 가능한 실행 예산용 cpu.max.runtime 및 유휴 시 재충전
Nov 11

### 개발 도구

wen.yang@linux.dev
[rv: Add task latency over budget RV monitor](https://lwn.net/Articles/1105657/)  — rv: 태스크 지연 예산 초과를 감시하는 RV 모니터 추가
Nov 06

Ian Rogers
[tools: Add Rust library build infrastructure and prefer zlib-rs](https://lwn.net/Articles/1105710/)  — tools: Rust 라이브러리 빌드 기반 추가 및 zlib-rs 우선 사용
Nov 05

Sasha Levin
[kallsyms: embed source file:line info in kernel stack traces](https://lwn.net/Articles/1105727/)  — kallsyms: 커널 스택 추적에 소스 파일·행 정보 삽입
Nov 06

Ahmed S. Darwish
[tools: Introduce a kernel configuration checker](https://lwn.net/Articles/1105719/)  — tools: 커널 설정 검사기 도입
Nov 06

Karl Mehltretter
[rv: Verify generic IRQ context transitions](https://lwn.net/Articles/1106298/)  — rv: 공통 IRQ 문맥 전환 검증
Nov 07

Li Pengfei
[tracing: Add stack trace deduplication for the ring buffer](https://lwn.net/Articles/1106294/)  — tracing: 링 버퍼에 스택 추적 중복 제거 추가
Nov 07

Ian Rogers
[perf symbol: Sorted arrays, DSO-owned lifetimes, and memory shrinking](https://lwn.net/Articles/1106737/)  — perf symbol: 정렬된 배열, DSO가 관리하는 수명 및 메모리 축소
Nov 10

### 장치 드라이버 기반 구조

alistair23@gmail.com
[lib: Rust implementation of SPDM](https://lwn.net/Articles/1106529/)  — lib: SPDM의 Rust 구현
Nov 10

### 문서

Matthew Weber
[Documentation: Add kernel minimization guide](https://lwn.net/Articles/1105660/)  — Documentation: 커널 최소화 안내서 추가
Nov 04

### 파일시스템 및 블록 계층

Hungyu Lin
[omfs: remove the filesystem](https://lwn.net/Articles/1105646/)  — omfs: 파일시스템 제거
Nov 05

Vitali Lovich
[fs: range-based admission for generation-drained DIO](https://lwn.net/Articles/1105659/)  — fs: 세대별 진행 중 작업을 소진하는 DIO의 범위 기반 진입 허용
Nov 04

### 메모리 관리

Usama Arif
[mm: PMD-level swap entries for anonymous THPs](https://lwn.net/Articles/1105712/)  — mm: 익명 THP용 PMD 수준 스왑 엔트리
Nov 05

Mathieu Desnoyers
[Hierarchical Percpu Counters for RSS](https://lwn.net/Articles/1105714/)  — RSS용 계층형 CPU별 카운터
Nov 05

Ackerley Tng
[guest\_memfd alternative providers](https://lwn.net/Articles/1106288/)  — guest_memfd 대체 제공자
Nov 06

Muchun Song
[mm: Decouple folio-based vmemmap optimization from HugeTLB](https://lwn.net/Articles/1106291/)  — mm: folio 기반 vmemmap 최적화를 HugeTLB에서 분리
Nov 07

Wen Jiang
[mm/vmalloc: Speed up ioremap, vmalloc and vmap with contiguous memory](https://lwn.net/Articles/1106297/)  — mm/vmalloc: 연속 메모리로 ioremap, vmalloc, vmap 가속
Nov 07

Baoquan He
[mm, swap: extendable swap devices (xswap phase I)](https://lwn.net/Articles/1106304/)  — mm, swap: 확장 가능한 스왑 장치(xswap 1단계)
Nov 09

Qiliang Yuan
[mm/filemap: read ahead for mmap readers that move backwards](https://lwn.net/Articles/1106305/)  — mm/filemap: 역방향으로 이동하는 mmap 읽기 작업의 미리 읽기
Nov 09

David Hildenbrand (Arm)
[mm: limit pagecache folio refcount](https://lwn.net/Articles/1106301/)  — mm: 페이지 캐시 folio 참조 횟수 제한
Nov 07

### 네트워킹

Martin Belanger
[tls: perform TLS 1.3 KeyUpdate in the kernel](https://lwn.net/Articles/1105656/)  — tls: 커널에서 TLS 1.3 KeyUpdate 수행
Nov 05

Daniel Zahka
[psp: support rekeying psp protected tcp connections](https://lwn.net/Articles/1106283/)  — psp: PSP로 보호된 TCP 연결의 키 갱신 지원
Nov 06

Xin Long
[net: introduce QUIC infrastructure and core subcomponents](https://lwn.net/Articles/1106531/)  — net: QUIC 기반 구조 및 핵심 하위 구성요소 도입
Nov 09

Alex Markuze
[io\_uring: opaque TCP payload objects](https://lwn.net/Articles/1106536/)  — io_uring: 불투명 TCP 페이로드 객체
Nov 10

Anton Danilov
[tunnels: add core and gre drop reasons](https://lwn.net/Articles/1106736/)  — tunnels: 공통 및 GRE 드롭 사유 추가
Nov 10

### 보안 관련

Jarkko Sakkinen
[KEYS: Sanitize the garbage collector](https://lwn.net/Articles/1105643/)  — KEYS: 가비지 수집기 정비
Nov 05

Aaron Tomlin
[module: Extend module\_blacklist parameter to built-in modules](https://lwn.net/Articles/1106277/)  — module: module_blacklist 매개변수를 내장 모듈까지 확대
Nov 06

Kevin Brodsky
[pkeys-based page table hardening](https://lwn.net/Articles/1106523/)  — pkeys 기반 페이지 테이블 강화
Nov 09

### 가상화 및 컨테이너

David Woodhouse
[KVM: Use atomic SRCU for gfn-to-pfn cache, reinstate guest mode for x86 nesting](https://lwn.net/Articles/1105645/)  — KVM: gfn-to-pfn 캐시에 원자적 SRCU 사용 및 x86 중첩용 게스트 모드 복원
Nov 05

Josef Bacik
[cells: a container as one kernel object](https://lwn.net/Articles/1105655/)  — cells: 컨테이너를 하나의 커널 객체로 표현
Nov 05

Aneesh Kumar K.V (Arm)
[coco: guest: Add a shared-granule allocator for host-shared memory](https://lwn.net/Articles/1105658/)  — coco: guest: 호스트 공유 메모리용 공유 그래뉼 할당기 추가
Nov 04

Aneesh Kumar K.V (Arm)
[KVM/VFIO: Add guest\_memfd support for device MMIO](https://lwn.net/Articles/1105662/)  — KVM/VFIO: 장치 MMIO용 guest_memfd 지원 추가
Nov 04

Zide Chen
[KVM: x86/pmu: Add mediated vPMU PerfMon v5 support](https://lwn.net/Articles/1105716/)  — KVM: x86/pmu: 중재형 vPMU PerfMon v5 지원 추가
Nov 05

Melody Wang
[Add SEV-SNP restricted injection hypervisor support](https://lwn.net/Articles/1106303/)  — SEV-SNP 제한적 주입의 하이퍼바이저 지원 추가
Nov 09

David Woodhouse
[KVM: x86: Cleaning up the KVM clock mess, part 2](https://lwn.net/Articles/1106302/)  — KVM: x86: KVM 클록 혼선 정리, 2부
Nov 08

Zack Rusin
[KVM: Improve VMware guest support](https://lwn.net/Articles/1106878/)  — KVM: VMware 게스트 지원 개선
Nov 11

### 기타

Ian Rogers
[tools/perf: Adopt kernel compiler-context-analysis.h annotations](https://lwn.net/Articles/1105644/)  — tools/perf: 커널 compiler-context-analysis.h 어노테이션 도입
Nov 04

Yanbo Zhao
[perf annotate: Data type profiling support for C++ classes and virtual calls](https://lwn.net/Articles/1105711/)  — perf annotate: C++ 클래스 및 가상 호출의 데이터 형식 프로파일링 지원
Nov 05

Stephen Hemminger
[arpd: remove](https://lwn.net/Articles/1106306/)  — arpd: 제거
Nov 08

Tarun Sahu
[kho, liveupdate: Add feature header for fine-grained ABI compatibility](https://lwn.net/Articles/1106530/)  — kho, liveupdate: 세밀한 ABI 호환성 확인을 위한 기능 헤더 추가
Nov 10

David Laight
[kallsyms: optimise symbol search by name](https://lwn.net/Articles/1106880/)  — kallsyms: 이름 기반 심볼 검색 최적화
Nov 11


## 읽기 참고

[^patches-status]: 패치 제목은 제안된 변경의 주제를 나타내며, 목록 등재와 메인라인 병합은 별개입니다. 커널 릴리스 항목도 나머지 개별 패치의 포함 여부를 보증하지 않습니다. 저자·영문 제목·URL·날짜는 원문 그대로 보존했으며, 날짜에 원문에 없는 연도나 시간대를 덧붙이지 않았습니다.
[^patches-tests]: 성능 향상이나 검증을 언급한 제목은 재현 가능한 시험 결과 자체가 아닙니다. 평가할 때는 패치 본문의 시험 조건, 커널 설정, 하드웨어, 회귀 시험 및 부하를 확인해야 합니다. 이 번역 작업에서는 커널 빌드나 패치 시험을 수행하지 않았습니다.
[^patches-abi]: ABI는 프로그램·구성요소 사이의 바이너리 인터페이스입니다. ioctl·라이브 업데이트·기능 헤더 관련 변경은 새 기능의 존재뿐 아니라 호출 규약, 기존 사용자 공간과의 호환성 및 업데이트 전후 상태 보존 조건을 확인해야 합니다. 제목만으로 ABI 유지가 입증되지는 않습니다.
[^patches-network]: TLS·PSP 키 갱신, QUIC 기반 구조, TCP 페이로드 객체는 서로 다른 네트워크 기능입니다. 검토할 때는 사용자 공간과의 역할 분담, 연결 상태 전환, 상호운용성 및 오류 경로를 구분해야 합니다. 기반 구조를 도입한다는 제목을 완전한 프로토콜 지원으로 읽어서는 안 됩니다.
[^patches-mm]: MM은 메모리 관리입니다. THP는 투명 거대 페이지, RSS는 상주 메모리 사용량을 가리킵니다. 스왑·페이지 캐시·매핑 관련 제안은 메모리 사용량뿐 아니라 지연, 동시성 및 메모리 압박 상황에서의 동작도 확인할 대상입니다. 제목의 최적화 표현만으로 모든 부하에서 이득이 있다고 단정하지 않습니다.
[^patches-security]: 보안 강화, 키 관리 정비, 기밀 게스트 지원은 각각 위협 모델과 적용 조건을 확인해야 합니다. 보안 관련 분류나 제목은 CVE의 존재, 취약점 악용 가능성, 수정 완료 또는 모든 구성에서의 보호를 뜻하지 않습니다. 이 목록만으로 그러한 상태를 추정하지 않습니다.

