# LWN.net Weekly Edition for May 14, 2026 — 한국어 기술 번역

- 원문 Bigpage: https://lwn.net/Articles/1071535/bigpage
- 원문 Edition: https://lwn.net/Articles/1071535/
- Article ID: `1071535`
- 선택 기준: LWN Archives에서 최신 Weekly Edition(2026-05-21, `1072730`)은 유료/최신호 가능성이 높아 건너뛰고, 바로 전 Weekly Edition(2026-05-14, `1071535`)의 공개 `bigpage`를 선택했다.
- 접근 확인: 공개 페이지에서 가져온 내용만 사용했으며, 로그인/유료 콘텐츠 우회는 하지 않았다.
- 생성시각: 2026-05-22T10:01:55+09:00

## 전체 요약

- Fedora 커뮤니티에서는 AI 개발자 데스크톱 이니셔티브를 둘러싸고 기술 도입의 속도, 자유 소프트웨어 철학, 프로젝트 평판 사이의 긴장이 드러났다.
- Forgejo의 “carrot disclosure” 사건은 보안 취약점 공개에서 실무적 이용자 보호와 공개 절차의 투명성 사이에 균형이 필요하다는 점을 보여준다.
- 2026년 LSFMM+BPF Summit과 여러 메모리 관리 기사들은 `dma-buf`, transparent huge pages, `mshare`, DAMON, direct map 등 Linux 메모리 관리의 성능·보안·확장성 이슈를 집중적으로 다룬다.
- Brief items는 Dirty Frag류 Linux 로컬 권한 상승 취약점, curl 취약점 탐색 사례, emergency mitigation killswitch, Debian reproducible builds, KDE Union style engine 등 보안·배포판·데스크톱 개발 동향을 압축한다.
- Announcements와 보안 업데이트는 배포판 뉴스, 회의록, CFP, 행사 일정, 보안 권고를 한데 묶어 운영자가 추적해야 할 릴리스·패키지·취약점 흐름을 제공한다.
- Kernel patches of interest는 아키텍처, 빌드 시스템, 코어 커널, 드라이버, 파일시스템, 메모리 관리, 네트워킹, 보안, 가상화 패치 흐름을 하위시스템별로 정리한다.

---

### [2026년 5월 14일 LWN.net 주간판에 오신 것을 환영합니다](https://lwn.net/Articles/1072665/)

#### 요약

- 이번 호에는 Fedora의 AI 개발자 데스크톱 구상과 관련한 커뮤니티 논쟁이 실렸습니다.
- Forgejo의 이른바 “carrot disclosure”가 보안 공개 방식과 프로젝트 보안 태세에 관한 논의를 촉발했습니다.
- LSFMM+BPF 2026 관련 보도와 커뮤니티 전반의 짧은 소식, 공지 사항도 포함되어 있습니다.

이번 호에는 다음 특집 콘텐츠가 포함되어 있습니다.

- AI 개발자 데스크톱 구상을 둘러싼 Fedora 내부 마찰
  : 일부 Fedora 기여자들은 공식적인 AI 친화 구상이 필요한지에 의문을 제기하고 있습니다.
- Forgejo “carrot disclosure”가 보안 문제를 제기하다
  : 보안 공개(security disclosure)에 대한 비표준 접근법으로, 당근보다는 채찍에 가까웠습니다.
- LSFMM+BPF 2026 보도:

이번 주 호에는 다음 내부 페이지도 포함되어 있습니다.

- 짧은 소식
  : 커뮤니티 전반에서 나온 간단한 뉴스 항목입니다.
- 공지 사항
  : 뉴스레터, 콘퍼런스, 보안 업데이트, 패치 등입니다.

이번 주 호도 즐겁게 읽어 주시기 바라며, 늘 그렇듯 LWN.net을 후원해 주셔서 감사합니다.

[댓글(게시된 댓글 없음)](https://lwn.net/Articles/1072665/#Comments)

### [AI 개발자 데스크톱 구상을 둘러싼 Fedora 내부 마찰](https://lwn.net/Articles/1071949/)

#### 요약

- Red Hat 직원들이 제안한 Fedora “AI Developer Desktop” 구상은 AI 도구와 NVIDIA/CUDA 지원을 쉽게 제공하려는 목적을 갖고 있습니다.
- 제안에는 트리 외부(out-of-tree) 커널 모듈과 Fedora용 장기지원(LTS) 커널 가능성이 포함되어, Fedora의 기존 “상류 커널을 빠르게 추적하는” 정책과 충돌했습니다.
- 일부 기여자들은 AI라는 명칭과 Fedora 공식 구상화가 프로젝트의 철학·평판·우선순위에 부정적 신호를 줄 수 있다고 우려했습니다.
- Fedora Council은 한때 6대 0으로 승인했지만, Justin Wheeler가 막판에 반대표로 바꾸면서 합의 절차가 중단되었습니다.
- 글은 Fedora가 기업 후원자인 Red Hat의 AI 전략 압력 속에서 결국 어떤 형태로든 AI 친화 방향으로 움직일 가능성이 높다고 봅니다.

글쓴이

Joe Brockmeier

2026년 5월 13일

Red Hat 직원들이 트리 외부(out-of-tree) 커널 드라이버와 AI 툴킷(toolkit)을 지원하는 Fedora “AI Developer Desktop”을 만들자고 추진한 데 대해, Fedora 커뮤니티의 오래된 일부 구성원들이 반대 의견을 냈습니다. 한 달 넘게 때로는 격렬했던 논의 끝에 [Fedora Council](https://docs.fedoraproject.org/en-US/council/)은 이 구상을 승인하기로 [투표](https://forge.fedoraproject.org/council/tickets/issues/562#issuecomment-697648)했습니다. 그러나 Council 구성원 Justin Wheeler가 막판에 제안 반대로 표를 바꾸면서, 이 구상은 적어도 일시적으로 원점 재검토 단계로 돌아가게 되었습니다.[^c1-fedora-council]

#### 제안

3월 31일, Red Hat의 선임 소프트웨어 엔지니어 Gordon Messmer는 Fedora 토론 포럼에서 AI Developer Desktop 구상을 [제안](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941)했습니다. 이 구상의 목표는 Fedora 안에서 “AI 기술을 둘러싼 활발한 커뮤니티를 구축”하는 것입니다. 구상은 AI 개발 도구와 이를 가능하게 하는 하드웨어를 배포하는 데 방해가 되는 기술적 난관에 초점을 맞추지만, 그보다 더 나아가 Messmer의 제안은 AI 개발을 Fedora 프로젝트의 주요 우선순위로 만들려는 의도를 담고 있습니다.

[커뮤니티 구상(Community initiatives)](https://docs.fedoraproject.org/en-US/project/initiatives/)은 “반년마다 돌아오는 Fedora Linux 릴리스 주기에 깔끔하게 들어맞지” 않고 여러 릴리스에 걸칠 수 있는 프로젝트입니다. 구상은 Fedora의 [사명 선언](https://docs.fedoraproject.org/en-US/project/#_our_mission)과 부합하는, 프로젝트 전체의 목표이기도 해야 합니다. 구상의 한 예로는 [Bugzilla와 Pagure를 Fedora의 “Git forge”로서 Forgejo로 대체하는 작업](https://fedoraproject.org/wiki/Initiatives/Git_Forge_Initiative_2025)이 있으며, Fedora 위키에는 [완료된 구상 목록](https://fedoraproject.org/wiki/Initiatives/Completed)도 있습니다. 참고로 구상은 이전에 “목표(objectives)”라고 불렸고, Messmer도 그 용어를 사용합니다. 일관성을 위해 여기서는 현재 용어인 “구상(initiative)”을 사용하겠습니다.[^c1-initiative]

Messmer는 Fedora가 하는 작업의 상당 부분이 애플리케이션을 패키징하여 설치 뒤 설정을 최소화해도 소프트웨어를 사용할 수 있게 하는 것이라고 말했습니다. 하지만 AI 도구는 Fedora에서 최소 수준 이상의 설정을 요구하는 경우가 많습니다. 그는 Fedora에서 AI 도구를 사용하려는 사용자가 설치 후 겪어야 하는 번거로움을 줄여 더 쉽게 실행할 수 있게 만들고자 합니다. 그가 “AI 소프트웨어용 플랫폼으로서 Fedora를 개선할 운영체제 이미지”를 제공하기 위해 식별한 [플랫폼 산출물](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941#p-488881-deliverables-7)은, Fedora가 트리 외부 커널 모듈(NVIDIA의 [OpenRM](https://open-iov.org/index.php/OpenRM), “[Nova 드라이버](https://www.kernel.org/doc/html/next/gpu/nova/index.html)가 준비될 때까지”)을 실제로 포함하지는 않더라도 수용해야 하며, NVIDIA의 독점 [CUDA Toolkit](https://developer.nvidia.com/cuda/toolkit)을 지원해야 한다는 요구를 담고 있습니다. 그는 “사용자가 시스템과 상호작용하는 방식을 검사하거나 감시하거나, 그 밖에 사용자 개인정보를 위험에 빠뜨리는 애플리케이션”이나 원격 AI 서비스에 연결되도록 미리 설정된 애플리케이션을 추가할 계획은 없다고 분명히 했습니다.[^c1-oot-cuda]

Messmer는 Fedora의 롤링 릴리스(rolling-release) 커널이 “AI 분야”에는 잘 맞지 않는다고 말하며, 트리 외부 커널 소프트웨어와 “커널 마이너 릴리스에서 흔히 발생하는 변경의 영향을 받을 수 있는” 사용자 공간(user-space) 구성요소의 문제를 피하기 위해 Fedora 장기지원(LTS) 커널이 필요하다고 주장했습니다. Fedora 프로젝트는 상류(upstream) Linux 커널을 밀접하게 따라가며, 여러 커널을 유지하지 않는 정책을 갖고 있습니다. Fedora 릴리스 하나는 보통 릴리스 주기 동안 메이저 버전을 포함해 많은 커널 업데이트를 받습니다. 예를 들어 [Fedora 42](https://lwn.net/Articles/1016845/)는 2025년 4월 6.14.0 커널과 함께 출시되었고, 해당 릴리스(수명 종료에 거의 도달한 상태)의 현재 업데이트 커널은 6.19.14입니다. Fedora의 [커널 정책](https://docs.fedoraproject.org/en-US/quick-docs/kernel-overview/#_policies)은 현재 트리 외부 모듈을 권장하지 않지만 완전히 금지하지는 않습니다. 그는 이 구상이 [Fedora Engineering Steering Committee](https://docs.fedoraproject.org/en-US/fesco/)(FESCo)에 “안정적인 Fedora 커널 선택지를 금지하는 정책을 재검토”하도록 요청해야 한다고 말했습니다.[^c1-fedora-kernel]

또한 그는 2026년 10월로 예정된 Fedora 45 릴리스와 비슷한 시기에 CUDA 툴킷을 포함해 AI 워크로드를 지원하는 [Fedora Atomic](https://fedoramagazine.org/introducing-fedora-atomic-desktops/) 변형판을 공개하고 싶어 했습니다. “라이선스나 우리가 해결할 수 없는 정책 문제 때문에 Fedora가 이 이미지를 배포할 수 없다면, 우리가 빌드한 이미지를 NVIDIA가 공개해 줄 수 있는지 물어보고 싶습니다.” Atomic 데스크톱은 이미지 기반(image-based)이므로, 사용자가 NVIDIA의 CUDA 패키지를 별도로 설치하기가 더 복잡합니다. 이미지를 빌드할 때 패키지를 포함하는 편이 훨씬 단순합니다. 그는 데스크톱의 [프리뷰 빌드](https://quay.io/repository/gordonmessmer/atomic-desktop/silverblue)와 이를 빌드하는 데 사용한 [설정 파일](https://pagure.io/fork/gordonmessmer/workstation-ostree-config/tree/f43-longterm-plus-cuda), 그리고 트리 외부 NVIDIA 모듈을 포함한 Fedora 43용 Linux 6.12 커널이 들어 있는 [Copr 저장소](https://copr.fedorainfracloud.org/coprs/gordonmessmer/kernel-longterm-6.12-plus/)를 링크했습니다. 그는 자신을 이 구상의 책임자로 제안했습니다.[^c1-atomic]

#### 논의

Fedora의 구상 절차에는 토론 단계가 필요하며, Messmer는 Fedora 포럼에 올린 글로 이 단계를 시작했습니다. 제안이 커뮤니티에서 좋은 반응을 얻으면, 그 책임자는 Council 검토를 위한 티켓을 열 수 있습니다. 지금까지 이 대화에는 30명이 넘는 참여자가 140개가 넘는 댓글을 남겼으며, 그것이 “좋은 반응을 얻었다”고 할 수 있는지는 의문에 부쳐졌습니다.

Steve Milner는 전체적인 아이디어와 제안된 계획이 마음에 든다고 [말했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/6). 그는 LTS 커널이 AI 데스크톱에만 한정되는지, 아니면 다른 Fedora 변형판에서도 사용할 수 있는지 궁금해했습니다. Messmer는 AI 데스크톱 사용자뿐 아니라 많은 사람에게 유용할 것이라고 생각한다고 [답했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/10). 그는 커널 업그레이드 뒤 하드웨어 지원 회귀(regression)에 대한 불만을 자주 들으며, 안정적인 커널은 [VirtualBox](https://www.virtualbox.org/)나 [ZFS](https://zfsonlinux.org/)용 다른 트리 외부 모듈이 필요한 사용자에게도 도움이 될 수 있다고 말했습니다. 그는 추가 커널이 [Fedora 품질 팀](https://fedoraproject.org/wiki/QA)에 더 많은 일을 안긴다는 점은 인정했지만, 롤링 릴리스 커널이 “안정 릴리스라는 개념과 잘 맞지 않기” 때문에 “오늘날 Fedora 커널을 둘러싼 테스트 절차에는 심각한 결함이 있다”고 주장했습니다. 사용자가 테스트 데이에 참여해 회귀를 보고하더라도, “새 릴리스 계열을 업데이트로 배포하는 것 말고는 현실적인 대안이 정말 없습니다.”[^c1-regression]

Neal Gompa는 공유할 [생각이 많았습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/16). 그는 트리 외부 커널 모듈 지원과 관련한 Fedora 정책 변경에 반대했습니다. “우리 사용자 시스템이 오염(tainted)된 것으로 간주되어 상류 커널 개발자로부터 지원을 받을 수 없게 될 가능성이 크게 높아집니다.” 그는 Fedora가 현재 트리 외부 모듈을 지원하지 않기 때문에 커널 개발자들이 Fedora를 선호한다고 말했습니다.[^c1-tainted]

그는 AI를 특히 CUDA와 동일시하는 데에도 유보적이었습니다. Fedora 구상은 독점 스택을 지지하는 것이 아니라 완전히 오픈소스 소프트웨어 스택을 장려해야 합니다. 이를 CUDA 중심으로 구축하면 “오픈소스 주도 AI 기술 스택을 밀어붙일 만큼 우리가 충분히 신경 쓰지 않는다는 어두운 신호”를 보내게 됩니다. 그는 FESCo 구성원의 입장에서도 안정적인 Fedora 커널을 찬성하는 정책 변경에는 강하게 반대할 것이라고 덧붙였습니다. “OpenRM에는 그것이 필요하지도 않으므로, 이 근거는 꽤 약합니다.”

Messmer는 OpenRM 모듈이 현재는 잘 작동하지만 “어느 특정 시점에도 계속 그럴 것이라는 보장은 없다”고 [응답](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/17)했습니다. 그것이 OpenRM을 Fedora 커널 패키지 안에서 빌드하지 않는 이유로 자신이 들은 설명이라는 것입니다. 그는 NVIDIA가 제안에서 구체적으로 언급된 것은 NVIDIA 하드웨어를 활성화하기 위해 필요한 작업이 있었기 때문이지, 이 구상이 CUDA 전용으로 의도되었기 때문은 아니라고 말했습니다. 다른 벤더들은 이미 “더 적극적인 지원이나 더 잘 정렬된 지원”을 제공하고 있었습니다. Gompa는 Red Hat이 Fedora 커널의 중요한 개발을 맡을 커널 개발자를 배정하지 않는다고도 불평했는데, Messmer는 그것이 안정 커널이 필요한 이유라고 말했습니다.

> 롤링 커널 릴리스에 충분한 개발자 자원이 배정되어 있지 않다고 주장하면서 동시에 안정 커널은 유용하지도 바람직하지도 않다고 주장하는 사람이 있다는 사실에 저는 사실 꽤 놀랐습니다. 제게는 그 두 관점이 서로 모순되어 보입니다. 후자는 전자의 해결책입니다.

Gompa와 Messmer의 논의는 한동안 이어졌습니다. Gompa는 비슷한 기업 후원이 있던 openSUSE 및 Ubuntu 배포판과 달리 Fedora에는 “엄청나게 과로하고 있으며 Fedora 커널 버그에 관여할 수 없는” 커널 유지관리자가 한 명뿐이라고 계속 [강조](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/30)했습니다. Fedora에 어떤 커널이 있느냐는 중요하지 않은데, 사용자가 발견한 문제를 고칠 사람이 Fedora에 없기 때문입니다. “문제가 7.0-rc6에 있든, 6.19-stable에 있든, 6.18-longterm에 있든 상관없습니다. 여전히 고쳐지지 않습니다.” 그는 여러 커널을 위한 패키징, 설치, 부트로더 인프라의 추가 복잡성은 타당하지 않다고 말했습니다. “Fedora Asahi Remix와 CentOS Stream Hyperscale을 위해 커널 트리와 대체 커널 플레이버(flavor)를 유지관리하는 사람으로서 이 말을 합니다. 그곳은 좋지 않은 자리이며, 절대적으로 필요하지 않았다면 저는 그 자리에 있고 싶지 않았을 것입니다.”

Clement Verna는 Messmer의 제안과 [Universal Blue](https://universal-blue.org/) 커뮤니티가 이미 하고 있는 일 사이에 많은 중복이 있을 것이라고 [말했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/20). 이 프로젝트는 특정 사용 사례에 맞춰 커스터마이즈한 Fedora 기반 이미지를 개발합니다. 예를 들어 [Bazzite](https://lwn.net/Articles/1046228/) 게임 배포판과 [Bluefin](https://projectbluefin.io/) 워크스테이션 배포판이 이 프로젝트의 일부입니다. 그는 Fedora가 Universal Blue에서 사용하는 자동화 도구로부터 많은 것을 배울 수 있으며, “LTS 빌드에 대한 유지관리 노력을 통합할 기회”도 있을 수 있다고 말했습니다.[^c1-universal-blue]

FESCo 구성원 Kevin Fenzi는 Messmer가 전체 프로젝트를 [Fedora Remix](https://fedoraproject.org/wiki/Remix)로 진행하지 않는 이유를 [물었습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/31). 프로젝트는 서드파티 소프트웨어, 심지어 독점 소프트웨어를 배포하더라도 [공식 Fedora 브랜딩 패키지를 사용하지 않는 한](https://fedoraproject.org/wiki/Remix#Including_other_software) “Fedora Remix” 브랜딩을 사용할 수 있습니다. 그는 Fedora에 “‘커널은 하나만’ 규칙”이 있는 이유가 유지관리 부담을 줄이기 위해서라고 덧붙였습니다. Messmer는 리믹스도 고려했지만, AI를 둘러싼 커뮤니티 형성에 Fedora 프로젝트가 참여하기를 원했다고 [말했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/37). “우리가 홍보하는 커뮤니티는 그 보답으로 프로젝트를 홍보할 것이라고 믿습니다.”

#### 철학적 반대

FESCo 구성원이기도 한 Fabio Valentini는 4월 27일 [의견을 냈습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/54). 그는 “조금 늦게 파티에 도착한” 데 대해 사과하며, Fedora가 AI 데스크톱 구상을 만들기를 자신이 원하는지 확신이 없다고 말했습니다. Fedora는 [AI 지원 기여 정책](https://pagure.io/Fedora-Council/tickets/issue/542#comment-990353)을 승인한 Council의 [결정](https://discussion.fedoraproject.org/t/council-policy-proposal-policy-on-ai-assisted-contributions/165092/242) 때문에 이미 “‘AI에 오염되었다’고 인식”되고 있으며, 이는 “AI 쿨에이드(AI Kool-Aid)를 마시지 않는 것으로 인식되는 배포판으로 사용자와 기여자를 떠나게” 하고 있다고 했습니다. (LWN은 Council 결정 이전인 2025년 10월 그 논의를 [다룬 바](https://lwn.net/Articles/1039623/) 있습니다.) 그는 LTS 커널은 흥미로울 수 있지만, “‘AI’가 제목에 들어간 어떤 것”을 공식 구상으로 만드는 데에는 동의하지 않으며, 그것이 사용자를 더 소외시킬까 우려한다고 말했습니다.

Messner는 Fedora가 독점 소프트웨어에 관한 정책 때문이 아니라 제목에 “AI”가 들어갔다는 이유로 프로젝트를 폐기하기로 결정한다면, Fedora가 정말 오픈소스 프로젝트인지 의문을 부를 것이라고 [주장](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/55)했습니다. “*그것*이야말로 우리의 평판에 실제로 나쁠 것입니다.” 그는 라이선스가 “특정 활동 분야에서 프로그램을 사용하는 것을 누구에게도 제한해서는 안 된다”고 요구하는 Open Source Initiative의 [오픈소스 정의](https://opensource.org/osd)(OSD)를 인용했습니다. Valentini는 그것은 말이 되지 않는다고 [말했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/59). Fedora는 프로젝트 범위를 제한하기 위해서라도 “‘우리가 이것을 할 수는 있지만, 하지 않을 것이다/하고 싶지 않다’는 종류의” 결정을 내려야 하기 때문입니다. 윤리적 또는 철학적 이유로 어떤 일을 하지 않기로 선택하는 것은, 어떤 일을 하지 않을 타당한 이유가 되어야 합니다.[^c1-osd]

Fernando Mancera는 OSD가 어떤 프로젝트가 오픈소스로 간주되기 위해 특정 기술을 채택해야 한다고 요구하지는 않는다고 [답했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/60). 결정의 핵심은 Fedora가 특정 사용을 자신과 연결하고 홍보하기를 원하는지 여부이지, 다른 사람들이 AI 사용 사례를 추구하지 못하도록 제한하는 문제가 아닙니다. 어떤 것을 Fedora 구상으로 만든다는 것은 프로젝트 전체가 그 성공에 집중한다는 의미를 갖습니다. “질문은 Fedora라는 프로젝트가 그 분야와 자신의 정체성 및 우선순위를 결부해야 하는가입니다.”

#### 평판 손상

Fedora Project Leader(FPL) Jef Spaleta는 긴 답변과 함께 [논의에 들어왔습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/64). 그는 사람들이 AI 때문에 Fedora를 피하고 있다는 “증거가 제 앞에는 전혀 없다”고 말하며, 그 주장을 뒷받침할 지표를 보여 달라고 했습니다. Fedora는 논쟁적 기술에 대해서도 “대화의 앞자리에” 있어야 하며, 자신이 참여하지 않는 대화에는 영향을 줄 수 없다고 했습니다. 그는 자신이 “AI의 윤리적 사용에 진심으로 우려하고 있다”고 주장했지만, 가능한 최선의 미래를 위해서는 Fedora 커뮤니티가 AI의 윤리적 사용에 관한 대화의 일부가 되어야 한다고 말했습니다.

> 더 나은 AI 미래로 우리를 데려갈 사람들은 여정의 시작점에 있고 그 기술에서 가치를 보는 사람들입니다. Fedora는 그 사람들이 이 기술을 우리의 공유된 이상에 가장 잘 부합하는 윤리적 방향으로 가져가도록 영향을 미쳐야 합니다.

그는 덧붙여, FPL로서 “AI 도구를 사용하려는 개발자에게 매력적인 완전히 새로운 산출물을 마련하는 데 따르는 이 프로젝트의 평판 손상에 대해서는 전혀 걱정하지 않는다”고 했습니다.

Valentini는 Spaleta가 자신의 요점을 놓쳤다고 [답했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/65). 이 모든 노력은 공식 Fedora 구상이 아니어도 진행될 수 있습니다. 누군가가 AI 데스크톱에서 일하는 것을 막을 장치는 없습니다. 다만 그는 현재 형태로는 “심각하게 문제가 있는” 기술을 Fedora가 프로젝트 구상으로 홍보하지 않는 편이 낫다고 생각했을 뿐입니다.

생각을 정리하기 위해 일주일을 쉰 뒤, Mancera는 다시 [응답](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/69)했습니다. 그는 Fedora가 데이터로 결정을 이끌어야 한다는 데 동의했지만, 그것은 양방향으로 적용되어야 한다고 했습니다. “그렇지 않으면, 우리는 서로 다른 주장에 서로 다른 기준을 적용할 위험이 있습니다.” 그는 Spaleta가 “잠재적인 평판 영향에 대해 아무 우려도 표하지 않는” 데 어려움을 느낀다고 했습니다. 그것은 일부 Fedora 기여자들이 깊이 신경 쓰는 문제를 무시하는 것으로 읽힐 수 있기 때문입니다. “그 변화가 기술적 의미에서 비파괴적이라 해도, 프로젝트가 어떻게 인식되는지와 Fedora의 우선순위에 대해 어떤 신호를 보내는지에는 여전히 영향을 줄 수 있습니다.”

Spaleta는 자신이 누구의 우려도 묵살하고 있는 것이 아니라, 그 감정을 어떻게 다루어야 하는지에 동의하지 않는 것이라고 일부 [응답](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/70)했습니다. 그는 자신이 “데이터 센터 밀도가 가장 높은” 지역에 살며, 전력과 물 사용의 직접적 영향을 받고 있다고 말했습니다. 하지만 사람들에게 그 기술을 사용하지 말라고 말하는 것은 통하지 않을 것입니다. “사람들이 더 나아지도록 적극적으로 기여할 수 있는, 더 윤리적인 버전을 제공하는 것이 도움이 될 수 있습니다.” Mancera는 [답했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/71).

> 저는 우리가 이것을 커뮤니티 방식으로 앞으로 나아가게 할 수 있다고 생각하지 않습니다. 저는 지금 즉시 Fedora 프로젝트에서의 모든 활동을 중단합니다. Fedora의 현재 상황은 분명히 제게 맞지 않습니다.

Simon de Vlieger는 AI 데스크톱이 *지금 당장* 구상이 될 필요는 없다고 [말했습니다](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/96). 대신 그는, 구상이 되기 전에 커뮤니티를 구축하는 특별 관심 그룹(special-interest group)을 가진 리믹스가 되어야 한다고 제안했습니다. 그것이 인기 있고 지속 가능하다는 것이 드러나면, 그때 구상이 될 수 있습니다. 그는 이 일이 커뮤니티 구성원과 그들의 우려를 무시한 채 “*반드시* 역을 떠나야 하는 기차”처럼 다뤄지고 있다고 느꼈습니다.

Spaleta는 AI 개발자 데스크톱이 Fedora에 전략적으로 중요하다고 계속 [주장](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/97)했습니다. “저는 이 작업에서 나오는 기본 이미지가 2028년 무렵 자체 워킹 그룹을 가진 에디션(edition)이 되어야 한다고 믿습니다.”[^c1-edition]

#### Council

논의가 격렬하게 이어지는 동안, Wheeler는 Council이 [5월 6일 이 구상을 논의했다](https://discussion.fedoraproject.org/t/fedora-council-meeting-2026-05-06-innovation-lifecycle-policy-f44-interviews-and-ai-desktop/190575)고 [발표](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/84)했습니다. Council은 Messmer가 이끌고 Spaleta가 실행 후원자(executive sponsor)를 맡는 12개월 구상으로 이를 승인하기로 투표했습니다(찬성 6, 반대 없음). Gompa는 Council이 “사실상 커뮤니티 논의를 무시”한 데 [불만](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941/93)을 표시하며, 제안은 현재 형태 그대로 승인하기에는 커뮤니티가 받아들일 수 없다고 말했습니다. “프로젝트에 매우 깊이 관여한 기여자인 우리의 의견과 이해관계가 중요하지 않다는 말을 듣고 있는 방식에 특히 실망했습니다.”

5월 8일, Wheeler는 자신의 표를 -1로 [바꾸었습니다](https://forge.fedoraproject.org/council/tickets/issues/562#issuecomment-698875). Council은 중요한 결정을 통과시키려면 완전한 합의를 요구하므로, Council 구성원 한 명이 절차를 멈추고 논의를 요구할 수 있습니다. “최근의 공개 및 비공개 피드백에 비추어 볼 때, 우리는 아직 진행에 필요한 합의를 갖추지 못했습니다.” 그는 Fedora 커널 전문가들의 피드백이 계획에 충분히 통합되지 않았다고 말했습니다. “저는 핵심 전문가들을 소외시키거나 소진시키지 않으면서 성공하는, 구조적으로 지속 가능한 구상을 만들도록 보장하기 위해 이 표를 던집니다.”[^c1-consensus]

Wheeler는 [Council 티켓](https://forge.fedoraproject.org/council/tickets/issues/562)의 날짜를 5월 22일로 바꾸었고, 그때까지 Council이 “교착 상태와 FPL 재정의(override) 없이” 결론에 도달할 수 있으리라 낙관한다고 했습니다. Council 헌장에 따르면, FPL은 합의가 진정으로 도달될 수 없고 결정을 내려야 할 때 “일을 ‘풀어낼(unstick)’” 수 있습니다.

Spaleta는 말하자면 Fedora가 “AI 대화”에 관여해야 한다는 입장을 확고히 박아 두었습니다. Fedora가 AI 기술을 다루기에 적합하도록 만드는 기술적 작업만으로는 충분하지 않은 것 같습니다. 프로젝트는 그런 것들에 찬성한다는 메시지를 보내야 합니다.

Fedora의 기업 후원자로부터 AI 친화적이어야 한다는 하향식 압력이 분명히 존재하며, 그 회사가 [AI에 전력투구](https://www.redhat.com/en/products/ai)하고 있다는 점을 생각하면 놀라운 일은 아닙니다. 지난해 Red Hat 핵심 플랫폼 부문 부사장 Mike McGrath는 AI 지원 기여 논의에 [개입](https://discussion.fedoraproject.org/t/council-policy-proposal-policy-on-ai-assisted-contributions/165092/12)해, Fedora의 거버넌스 기구들이 자신들이 원하지 않는 것으로 잘 알려져 있다고 불평했습니다. 그는 Fedora가 “미래를 이끌고 형성하며 ‘AI여, 우리의 문은 열려 있다. 다시 미래를 발명하자’고 말하는” 모습을 보고 싶어 했습니다.[^c1-sponsor]

결국 이 구상은 어떤 형태로든 승인될 가능성이 높아 보입니다. Fedora가 AI를 자기 정체성의 일부로 받아들이고 포용하라는 압력은, 프로젝트가 후원자가 원하는 방향으로 움직일 때까지—혹은 바람이 바뀌거나, 거품이 꺼지거나, AI가 어제의 뉴스가 될 때까지—계속될 운명처럼 보입니다. AI 열풍이 곧 사라질 가능성은 낮으므로, Fedora는 조만간 그것을 위한 자리를 마련하게 될 공산이 큽니다.

[댓글(27개 게시됨)](https://lwn.net/Articles/1071949/#Comments)

### [Forgejo “carrot disclosure”가 보안 문제를 제기하다](https://lwn.net/Articles/1071499/)

#### 요약

- 보안 연구자 Julien Voisin은 Forgejo에서 원격 코드 실행(RCE)으로 이어질 수 있다고 주장한 취약점들을 발견했지만, 처음에는 세부 사항을 프로젝트 보안 절차로 비공개 보고하지 않았습니다.
- 그는 공급업체가 스스로 전체적인 감사를 하도록 압박하는 방식인 “carrot disclosure”를 사용했다고 설명했습니다.
- 일부 커뮤니티 구성원은 이 접근이 자원봉사 프로젝트에 적대적이고 비전문적이라고 비판했고, 다른 일부는 Forgejo의 보안 정책이 지나치게 요구적이라고 보았습니다.
- Voisin은 후속 글에서 사과와 설명, 권고, 익스플로잇/개념증명(PoC)을 Forgejo 보안팀에 보냈다고 밝혔습니다.
- Forgejo는 알려진 RCE는 내부 서버 자격증명 없이는 가능하지 않으며, 제기된 사안은 공개적으로 다룰 수 있는 방어 심층화와 서비스 거부 위험이라고 응답했습니다.

글쓴이

Joe Brockmeier

2026년 5월 8일

[Forgejo](https://forgejo.org/) 소프트웨어 협업 플랫폼에서의 이른바 원격 코드 실행(remote-code-execution, RCE) 결함을 공개하는 데 있어, 어떤 이들은 적대적이라고도 할 수 있는 이례적인 접근이 다층적인 대화를 촉발했습니다. 4월의 이른바 “carrot disclosure”는 보안 문제를 드러내는 연구자의 방식, Forgejo의 보안 정책, 그리고 프로젝트 전반의 보안 태세(security posture)에 관한 질문을 제기했습니다.[^c1-rce]

Forgejo는 2022년에 [Gitea](https://about.gitea.com/) 협업 및 호스팅 플랫폼에서 [포크](https://lwn.net/Articles/963095/)되었습니다. 이 프로젝트는 [Codeberg e.V.](https://docs.codeberg.org/getting-started/what-is-codeberg/#what-is-codeberg-e.v.%3F) 비영리 단체가 지원하며, [Codeberg](https://codeberg.org/) 호스팅 서비스에서 사용하는 소프트웨어입니다. Fedora Project도 자체 개발 Pagure 플랫폼을 Forgejo로 [대체하는 마지막 단계](https://communityblog.fedoraproject.org/the-forge-is-our-new-home/)에 있습니다.[^c1-forgejo]

#### Carrot disclosure

4월 29일 자신의 [공개 글](https://dustri.org/b/carrot-disclosure-forgejo.html)에서, 보안 연구자 Julien Voisin은 Fedora가 이 프로젝트를 협업 플랫폼으로 선택한 것이 자신으로 하여금 “Forgejo의 보안 태세를 자세히 살펴보도록” 만든 계기였다고 말했습니다. 그는 Forgejo에서 여러 보안 결함을 발견했다고 주장했습니다.

> 종합하면, 퇴근 뒤 어느 저녁 한 번을 들여 꽤 많은 취약점을 찾을 수 있었고(과거 어느 시점에 gitea를 살펴보다 얻은 것 하나에 더해), 그중 일부를 체이닝(chain)해 완전한 RCE를 얻을 수 있었습니다 [...]

4월 27일, Voisin은 Forgejo 프로젝트에 몇 개의 풀 리퀘스트(pull request)를 열었습니다. 댓글 폼에서 [속성을 인용하도록 고치는 수정](https://codeberg.org/forgejo/forgejo/pulls/12283), 사용자가 제공한 문자열을 명령에 전달하는 메서드를 제거하는 [변경](https://codeberg.org/forgejo/forgejo/pulls/12288), 그리고 [“plain” OAuth 인증 방식을 제거](https://codeberg.org/forgejo/forgejo/pulls/12285)하는 변경입니다. 어떤 풀 리퀘스트에도 유지관리자가 보안상 긴급한 이유로 해당 수정을 처리해야 한다고 인식할 만한 설명은 포함되어 있지 않았습니다.[^c1-pr-security]

또한 그가 프로젝트의 상당히 상세한 [보안 정책](https://codeberg.org/forgejo/governance/src/commit/4cf58828436b302b314c689b6f94de62179bd515/SECURITY-POLICY.md#forgejo-security-policy)을 따라 구체적인 보안 결함을 보고하지 않은 것으로 보입니다. “Gusted”가 Voisin이 “어느 정도 보안과 관련된” 풀 리퀘스트 세 개를 열었다는 사실을 [알아차리고](https://codeberg.org/forgejo/forgejo/pulls/12288#issuecomment-13897232) [질문](https://codeberg.org/forgejo/forgejo/pulls/12288#issuecomment-13899581)한 뒤에도 그렇습니다. Voisin은 자신이 “비공개로 보고할 가치가 있는 보안 문제로 간신히 인정될 수 있을 뿐, 엠바고를 조율할 정도는 아닌” 낮은 영향도의 버그 목록을 처리하는 중이라고 [답했습니다](https://codeberg.org/forgejo/forgejo/pulls/12288#issuecomment-13900052). 그는 또한 이 정책이 보안 문제 보고에서 “해야 한다(MUST), 해서는 안 된다(MUST NOT), 할 수 있다(MAY)”는 요구사항이 많다고 [불평](https://codeberg.org/forgejo/forgejo/pulls/12288#issuecomment-13900577)하며, 그 정책이 어떻게 집행되는지 궁금해했습니다.[^c1-disclosure-policy]

RCE의 구체적 내용을 프로젝트에 직접 보고하는 대신, Voisin은 자신이 “carrot disclosure”라고 부르는 방식을 선택했습니다. 이는 그가 2024년에 [만든 용어](https://dustri.org/b/carrot-disclosure.html)입니다. 그는 이를 “변화를 유도하기 위해 공급업체 앞에 은유적 당근을 매다는 것”으로 정의했지만, 실제로 그 접근은 당근보다는 채찍에 더 가깝게 들립니다. 아이디어는 소프트웨어가 악용 가능하다는 점을 보여 주고, 공급업체가 “제시된 취약점을 고칠 수 있기를 바라며 가능한 한 많은 문제를 고치는 전체론적 소프트웨어 감사(holistic audit)”를 수행하도록 강제하거나, 알려진 취약한 소프트웨어를 실행하는 데 불만을 가진 사용자를 잃게 만드는 것입니다. “물론 이 공개 모델의 사용자는 Bugs Bunnies라고 부릅니다.”

[Looney Tunes](https://en.wikipedia.org/wiki/Looney_Tunes) 만화의 팬들은 일반적으로 [Bugs](https://en.wikipedia.org/wiki/Bugs_Bunny)가 먼저 문제를 찾아 나서지는 않았다고 관찰할 수 있을 것입니다. 그는 종종 어떤 식으로든 사냥당하거나 괴롭힘을 당한 뒤 “물론 알겠지, 이건 전쟁이라는 뜻이야”라고 선언하곤 했지만, 문제를 먼저 일으키지는 않았습니다. 여기서 이 점은 관련이 있어 보입니다. Voisin의 접근은 그 반대였기 때문입니다. 먼저 문제를 찾아 나선 뒤, 결함이 발견되자 도발적으로 행동한 것입니다.

middle-ad

Voisin은 자신이 RCE를 발견했다고 주장했는데, 이는 그가 풀 리퀘스트를 연 문제들과는 관련이 없어 보이며, Forgejo 인스턴스가 [공개 가입(open registration)](https://codeberg.org/forgejo-contrib/delightful-forgejo#public-instances)을 허용해야 한다는 조건이 있었습니다. 다시 말해 누구나 플랫폼 사용을 위해 가입할 수 있어야 한다는 뜻입니다. 또한 “어떤 설정 옵션이 기본값이 아닌 값으로 설정”되어 있어야 했습니다. 그는 어떤 설정 옵션인지는 명시하지 않았지만, 자신이 살펴본 일부 인스턴스에서는 활성화되어 있었다고 말했습니다. 그의 예시는 실제 코드는 공개하지 않은 채 Python 스크립트를 실행하여 로컬 머신에서 실행 중인 Forgejo 인스턴스를 상대로 RCE를 달성하는 모습을 보여 주었습니다.[^c1-open-registration]

그는 공개 글에서, 더 많은 풀 리퀘스트로 문제를 하나씩 해결하려고 할 수도 있었지만 그러지 않기로 했다고 말했습니다.

> 저는 버그를 Forgejo에 공개할 수도 있었습니다. 그들에게는 보안 정책도 있고, 제가 이 길로 가기로 한다면 제가 해야 하거나 해서는 안 되는 것에 대해 MUST/MUST NOT이 많이 있습니다. 하지만 코드베이스의 안타까운 상태를 보면(물론 그들의 잘못은 아닙니다. 그들은 gitea/gogs의 것을 물려받았습니다), 저는 또 다른 저녁을 들여 또 다른 체인을 찾을 수 있을 것이라고 꽤 확신하며, 다른 사람들도 여러 개를 갖고 있을 가능성이 높습니다. 문제를 하나씩 직접 고쳐 풀 리퀘스트를 보낼 수도 있겠지만, 제가 원한다 해도 이것은 시스템적인 문제이고, 끝없는 두더지 잡기(wack-a-mole)를 하는 데에는 별 의미가 없습니다.

그는 친구와 이 주제를 논의한 뒤, “말만 하지 말고 행동으로 보여 주고, 이런 상황에서 내가 보통 옹호하는 carrot disclosure로 그냥 가라”는 말을 들었다고 했습니다. 공개 글을 게시한 뒤, 그는 4월 29일 infosec.exchange Mastodon 서버에서 이를 [홍보](https://infosec.exchange/@jvoisin/116488420408417722)했습니다. 이는 빠르게 관심을 얻어 Fediverse에서 논의 주제가 되었고, [Hacker News](https://news.ycombinator.com/item?id=47941590), [Lobste.rs](https://lobste.rs/s/swbkcl/carrot_disclosure_forgejo) 및 다른 토론 포럼에도 공유되었습니다.

#### 반응

공개 반응은 엇갈렸으며 대체로 두 부류로 나뉘었습니다. Voisin의 접근을 비판하는 사람들과, Forgejo의 보안 정책 및 인식된 문제를 강하게 비판하는 사람들입니다. 예를 들어 Hans van Zijst는 그것이 “다른 사람의 작업에 대해 말하는 믿을 수 없을 정도로 잘난 체하는 방식이며, 자원봉사자들이 당신의 우선순위를 따르도록 강제하려는 끔찍한 시도”라고 [말했습니다](https://social.woefdram.nl/display/9a295f86-e5c5-4020-9f16-fe4a954d7867). Henry Catalini Smith는 [말했습니다](https://radikal.social/@henry/116489533765533237). “당신이 여기서 한 일은 합리적인 어떤 전문적 행동 기준에도 미치지 못했고, 제게는 매우 이상하게도 보입니다.” 그는 최근 Forgejo의 접근성 버그를 살펴보기 시작했고, 이를 해결하기 위해 프로젝트와 함께 일하면 재미있을 것이라고 생각했다고 했습니다. 특정 유형의 문제 전문가가 보안 문제가 있는 프로젝트에 “이렇게 공개적으로 적대적인 사람으로 브랜드를 구축”하고 싶어 한다는 것은 그에게 이해되지 않았습니다.

Privacy Guides 포럼에서 “HackOrSwim”은 보고자가 Forgejo의 많은 문제가 Gitea에서 포크할 때 물려받은 것임을 인정했지만, 그 문제를 고치려면 많은 자원이 필요하다는 점은 인정하지 않았다고 [말했습니다](https://discuss.privacyguides.net/t/carrot-disclosure-forgejo/37484/6). “이것은 본질적으로 기술 부채(technical debt)입니다. 그렇다고 용납되는 것은 아니지만, 왜 이런 문제가 거기에 있는지 이해할 수는 있게 합니다. 이 프로젝트는 비영리, 자원봉사 기반 프로젝트입니다.”[^c1-technical-debt]

반대편에서 Tony Arkles는 그 정책이 “커뮤니티 구성원에게서 무료 지원을 받는 팀치고는 꽤 요구가 많은 것으로 보인다”고 [말하고](https://lobste.rs/s/swbkcl/carrot_disclosure_forgejo#c_2oqu03), 그 절차가 거슬린다고 했습니다. “저는 이 점에서는 저자 쪽에 선 것 같습니다.” 정보보안 컨설턴트이자 연구자인 Elliot Speck은 Forgejo 보안 지침이 “불쾌하고 허세적”이라고 [보았습니다](https://lobste.rs/s/swbkcl/carrot_disclosure_forgejo#c_wl3zvg). 그는 프로젝트가 “엉뚱한 것들을 너무 진지하게 받아들이느라 바쁘다”고 말했습니다.

#### 후속 조치

Voisin은 4월 30일 공개 이후 일어난 사건을 요약한 [후속 글](https://dustri.org/b/follow-up-to-carrot-disclosure-forgejo.html)을 게시했습니다. 그는 자신이 “몇 가지 역겨운 이름으로 불렸고”, “쉬운 표적에 원치 않는 관심을 끌어들였다”는 불만을 받았으며, 자신의 행동이 비전문적이라는 불만에 대해서는 이렇게 답했다고 했습니다. “‘전문적이지 않다’(‘전문적 환경에서 받아들일 수 없다’는 뜻으로)라는 말이 많이 오갔지만, 여기서 어떤 것도 전문적 맥락에서 이루어지고 있거나 이루어진 것은 아닙니다.”

그는 또한 “여러 주체”가 Forgejo가 무엇이고 무엇이 아닌지에 대한 자신들의 의견을 수정했다는 사실을 알게 되었다고 말했으며, 그것이 “이전 블로그 글의 주된 목표”였다고 했습니다. 하지만 이런 소동에도 불구하고, Voisin은 그것이 생산적이고 선의에 기반한 대화로 이어졌다고 말했습니다.

> 이상한 취약점 공개 방식을 실험하는 것은 눈살을 찌푸리게 하는 일인 것 같습니다. 그래서 결국 저는 Forgejo 보안팀에 이메일을 보냈습니다. 그 안에는 사과, carrot disclosure를 진행한 제 이유에 대한 약간의 설명, 강화/검토할 사항에 대한 권고, 그리고 주석이 달린 여러 익스플로잇/개념증명(proof-of-concepts)을 첨부했습니다. 어떻게 될지 지켜보겠습니다.

4월 30일, Forgejo 프로젝트는 짧은 [응답](https://floss.social/@forgejo/116494295922963052)을 게시했습니다. 그 응답은 Voisin이 자신의 발견 사항을 가지고 Forgejo 보안팀과 접촉했다고 밝혔습니다.

> 제기된 문제들은 방어 심층화(defense-in-depth) 개선과 서비스 거부(denial-of-service) 위험에 관한 것입니다. 내부 서버 자격증명 없이는 가능한 것으로 알려진 RCE 익스플로잇이 없습니다.
>
> 우리는 이러한 발견 사항을 공개적으로 다룰 수 있다고 믿습니다. 보안팀은 새로운 방어 조치(defensive measurements)를 구현하는 접근법을 논의할 이슈를 열 것입니다. 단일한 정답은 없다고 믿으므로, 이 문제에 관한 다른 Forgejo 기여자들의 의견을 환영합니다.

자격증명 없이는 RCE가 가능하지 않다는 이 발언은 Voisin의 주장과 어긋나는 *것처럼 보이지만*, 더 많은 정보 없이는 어느 쪽이 맞는지 확인할 방법이 없습니다.[^c1-credentials]

[LLM을 사용해 보안 결함을 찾는 일이 점점 쉬워지고 있다는 점](https://lwn.net/Articles/1066581/)을 고려하면, Voisin이 스포트라이트를 비춘 결과 프로젝트의 구멍을 찾는 데 토큰을 쓰는 사람이 늘어났을 가능성은 충분합니다. 그들 중 일부는 Voisin만큼 선의적이지 않을 수도 있습니다. 앞으로 몇 주와 몇 달 동안 Forgejo를 지켜보며 어떤 종류의 보안 개선이 이루어지고, 어떤 종류의 보안 결함이 드러나는지 보는 일은 흥미로울 것입니다.[^c1-llm-security]

[댓글(26개 게시됨)](https://lwn.net/Articles/1071499/#Comments)

[^c1-fedora-council]: Fedora Council은 Fedora 프로젝트의 전략·정책 결정을 담당하는 거버넌스 기구입니다. 기술 제안이 배포판의 정체성, 유지관리 자원, 법적·정책적 위험에 영향을 줄 때 Council의 승인 여부는 단순한 패키지 추가보다 훨씬 큰 의미를 갖습니다.

[^c1-initiative]: Fedora의 “initiative”는 개별 패키지나 기능 요청보다 범위가 넓은 프로젝트 차원의 목표입니다. 공식 구상으로 지정되면 인력, 홍보, 거버넌스 관심이 따라오기 때문에, 기술적 타당성뿐 아니라 프로젝트가 어떤 신호를 보내는지도 논쟁거리가 됩니다.

[^c1-oot-cuda]: 트리 외부 커널 모듈은 Linux 커널 소스 트리 안에서 함께 개발·검토되지 않는 드라이버를 뜻합니다. NVIDIA GPU와 CUDA는 AI 개발에서 널리 쓰이지만, 독점 구성요소와 커널 ABI 호환성 문제가 결합되어 배포판의 자유 소프트웨어 정책과 안정성 정책을 동시에 건드립니다.

[^c1-fedora-kernel]: Fedora는 새 커널을 빠르게 제공해 최신 하드웨어와 상류 버그 수정을 반영하는 대신, 커널 내부 ABI 안정성을 보장하지 않습니다. LTS 커널을 병행하면 드라이버 호환성은 나아질 수 있지만, 보안 패치 백포트와 테스트 매트릭스가 늘어나 유지관리 부담이 커집니다.

[^c1-atomic]: Fedora Atomic 데스크톱은 rpm-ostree/이미지 기반 시스템으로, 전통적인 패키지 설치보다 재현성과 롤백이 쉽지만 이미지 빌드 시점의 구성 결정이 더 중요합니다. 독점 GPU 스택을 이미지에 포함할지 여부는 사용자 편의성과 배포 정책 사이의 전형적인 충돌입니다.

[^c1-regression]: 커널 회귀는 업데이트 후 이전에 동작하던 하드웨어나 기능이 깨지는 현상입니다. 롤링 커널을 쓰는 배포판에서는 빠른 개선과 회귀 위험이 함께 오며, 특히 GPU·가상화·파일시스템 같은 저수준 구성요소에서 사용자 영향이 큽니다.

[^c1-tainted]: Linux 커널은 독점 모듈이나 특정 위험 상태가 감지되면 “tainted” 플래그를 설정합니다. 이는 버그 보고를 분석하는 상류 개발자에게 시스템 상태가 표준 커널과 다르다는 신호를 주며, 실제 지원 가능성에도 영향을 줄 수 있습니다.

[^c1-universal-blue]: Universal Blue 같은 이미지 기반 Fedora 파생 프로젝트는 특정 워크로드에 맞춘 데스크톱 이미지를 빠르게 실험할 수 있는 장점을 보여 줍니다. 공식 Fedora와 별도 커뮤니티 이미지 사이의 경계는 혁신 속도, 브랜드 신뢰, 유지관리 책임을 어떻게 나눌지의 문제입니다.

[^c1-osd]: 오픈소스 정의(OSD)는 라이선스가 사용 분야를 차별하지 않아야 한다는 조건을 포함하지만, 이것이 모든 오픈소스 프로젝트가 모든 사용 분야를 공식적으로 홍보해야 한다는 뜻은 아닙니다. 여기서 논쟁은 라이선스 자유와 프로젝트 우선순위·윤리적 선택을 구분하는 데 있습니다.

[^c1-edition]: Fedora에서 “Edition”은 단순한 스핀이나 리믹스보다 공식성이 높은 산출물입니다. 자체 워킹 그룹과 품질 기준을 갖게 되므로, AI 데스크톱을 Edition으로 본다는 말은 장기적으로 Fedora의 핵심 제품군에 넣겠다는 전략적 신호입니다.

[^c1-consensus]: Fedora Council의 합의 모델은 소수 의견이 구조적 문제를 제기할 때 결정을 멈출 수 있게 합니다. 이는 의사결정을 느리게 만들 수 있지만, 핵심 유지관리자 번아웃이나 정책 충돌처럼 나중에 비용이 커질 위험을 조기에 드러내는 장치이기도 합니다.

[^c1-sponsor]: Fedora는 커뮤니티 배포판이지만 Red Hat의 후원을 받으며, Red Hat의 사업 전략은 Fedora의 우선순위 논의에 간접적·직접적 압력을 줄 수 있습니다. AI처럼 기업 투자가 큰 분야에서는 기술 방향과 커뮤니티 자율성의 긴장이 더 뚜렷해집니다.

[^c1-rce]: RCE는 공격자가 원격에서 서버나 애플리케이션이 임의 코드를 실행하게 만들 수 있는 취약점 유형입니다. 웹 협업 플랫폼에서 RCE가 성립하면 저장소, 토큰, 사용자 데이터, CI/CD 비밀값까지 연쇄적으로 위험해질 수 있어 심각도가 매우 높습니다.

[^c1-forgejo]: Forgejo·Gitea·Pagure 같은 “forge” 플랫폼은 Git 저장소뿐 아니라 이슈, 풀 리퀘스트, 권한, 웹훅, CI 연동을 다룹니다. 배포판 인프라가 여기에 의존하면 플랫폼 보안은 단일 웹앱 문제가 아니라 전체 개발 공급망 보안 문제가 됩니다.

[^c1-pr-security]: 보안 수정처럼 보이는 변경을 일반 풀 리퀘스트로 제출하면, 유지관리자가 심각도를 모른 채 공개 이슈로 취약점 단서를 노출할 수 있습니다. 반대로 모든 의심을 비공개로 돌리면 오픈 개발 흐름이 느려지므로, 프로젝트별 보안 보고 절차가 중요합니다.

[^c1-disclosure-policy]: 취약점 공개 정책은 연구자와 프로젝트가 엠바고, 재현 정보, 패치 일정, 공개 시점을 조율하기 위한 사회적 계약에 가깝습니다. 정책이 지나치게 엄격하면 외부 제보자가 부담을 느끼고, 너무 느슨하면 사용자 보호가 어려워질 수 있습니다.

[^c1-open-registration]: 공개 가입이 가능한 forge 인스턴스는 공격자가 계정을 만들어 내부 기능에 접근할 수 있으므로 공격 표면이 커집니다. “비기본 설정” 조건은 모든 설치가 취약하지 않을 수 있음을 뜻하지만, 실제 운영자는 자신이 어떤 위험한 조합을 켰는지 파악해야 합니다.

[^c1-technical-debt]: 기술 부채는 과거 설계·코드·의존성 선택이 시간이 지나며 유지보수와 보안 개선을 어렵게 만드는 비용입니다. 포크 프로젝트는 상류에서 물려받은 부채를 동시에 떠안기 때문에, 보안 감사와 리팩터링에 충분한 인력이 없으면 문제가 장기화되기 쉽습니다.

[^c1-credentials]: “내부 서버 자격증명”이 필요한 공격과 무자격 원격 공격은 위협 모델과 심각도가 크게 다릅니다. 전자는 내부자·이미 침해된 계정·구성 오류를 전제로 할 수 있지만, 후자는 인터넷에 노출된 인스턴스 전체에 즉각적인 위험을 의미할 수 있습니다.

[^c1-llm-security]: LLM은 코드 검색, 패턴 매칭, 익스플로잇 초안 작성 속도를 높여 방어자와 공격자 모두의 역량을 증폭합니다. 공개적으로 취약 가능성이 언급된 프로젝트는 선의의 감사뿐 아니라 자동화된 취약점 사냥의 표적도 되므로, 대응 속도와 투명한 커뮤니케이션이 중요합니다.

---

### [2026 Linux Storage, Filesystem, Memory Management, and BPF Summit](https://lwn.net/Articles/1071199/)

#### 요약

- 커널의 스토리지(storage), 파일시스템(filesystem), 메모리 관리(memory management), BPF 하위시스템 개발자들이 2026년 5월 크로아티아 자그레브에 모여 핵심 개발 현안을 논의했다.
- LWN은 메모리 관리 트랙, BPF 트랙, 스토리지·메모리 관리 공동 세션, 스토리지·파일시스템 공동 세션의 기사 목록을 정리했다.
- 메모리 관리 트랙에서는 유지관리 체계 변화, DAMON, 대형 페이지(huge page), CXL, MGLRU, BPF 기반 페이지 캐시 정책 등 다양한 주제가 다뤄졌다.
- 공동 세션에서는 dma-buf를 이용한 읽기/쓰기 API, 플래시 친화적 스왑(swap), 버퍼드 원자적 쓰기(buffered atomic write) 등이 논의되었다.
- 행사 사진과 Linux Foundation에 대한 감사 인사도 함께 소개되었다.

작성자

Jonathan Corbet

2026년 5월 7일

LSFMM+BPF

해마다 한 번씩, 커널의 스토리지, 파일시스템, 메모리 관리, BPF 하위시스템 개발자들이 모여 이메일만으로는 해결하기 어려울 수 있는 긴급한 개발 문제들을 논의한다. 2026년판

Linux Storage, Filesystem, Memory Management, and BPF Summit

은 5월 첫째 주 크로아티아 자그레브에서 열렸다. 당연히 LWN도 그 현장에 대거 참석했다.[^c2-lsfmm-scope]

middle-ad

> ![[Esplanade hotel]](https://static.lwn.net/images/conf/2026/lsfmm/esplanade-sm.png)

이 모임에 대한 보도는 아직 진행 중이다. 지금까지 기사가 나온 세션은 다음과 같다.

#### Memory-management track

- 메모리 관리 유지관리(maintainership)의 새 시대
  : 오랜 유지관리자인 Andrew Morton이 물러날 준비를 하고 있다고 밝혔다. 그다음에는 어떤 일이 일어날까?
- 2026년 DAMON 업데이트
  : 빠르게 움직이는 이 메모리 관리 하위시스템에서 어떤 일이 벌어지고 있는지.
- 4KB 커널에서 64KB 기본 페이지(base page)를 제공하는 두 가지 방법
  : 메모리 낭비를 최소화하면서 더 큰 기본 페이지 크기의 장점을 얻기 위한 두 가지 접근법.
- 투명 대형 페이지(transparent huge page)를 1GB까지 확장하기
  : 2MB 대형 페이지가 더 이상 “크다”고 여겨지지 않는 세상에서 다음 단계는 무엇인가?
- mshare 재검토
  : 페이지 테이블 공유(page-table sharing)를 쉽게 만들려는 오래된 목표를 다시 살펴보기.
- 직접 매핑(direct map) 바깥의 페이지 관리
  : 커널의 직접 매핑에서 메모리를 제거하면 보안을 개선할 수 있지만 성능은 나빠진다. Brendan Jackman은 그 성능 패널티를 피하는 API를 작업 중이다.
- COW를 문맥 속에 두기(일명 익명 역매핑, anonymous reverse mapping)
  : 커널의 역매핑(reverse-mapping) 코드를 갱신하고 단순화하려는 시도.
- 커널을 위한 정책 그룹(policy group)
  : 컨트롤 그룹(control group) 모델에 맞지 않는 정책을 관리하기 위한 더 나은 인터페이스가 있는가?
- 라이브 업데이트(live update) 중 HugeTLB 보존
  : 실행 중인 시스템에서 커널을 교체하면서도 그 시스템에서 동작하는 가상 머신이 사용하는 대형 페이지를 보존한다는 목표를 어떻게 지원할 것인가.
- BPF로 메모리 관리 제어하기
  : BPF를 메모리 관리 하위시스템과 통합하면 무엇이 가능할 수 있는지, 그리고 이를 가로막는 장애물은 무엇인지.
- 스왑 테이블(swap table), 플래시 친화적 스왑(flash-friendly swap), `swap_ops` 등
  : 커널 스왑 하위시스템의 현재와 미래 상태에 관한 세 개 세션.
- CPU별(per-CPU) 메모리 할당자 개선
  : 확장성을 높이려는 할당자 자체에도 확장성 문제가 있다.
- CXL에서 무르익고 있는 것들
  : 커널에서 Compute Express Link(CXL) 장치를 지원하기 위한 여정의 진전.
- MGLRU를 어떻게 해야 하는가?
  : 커널에는 두 개의 별도 회수(reclaim) 구현이 있고, 그중 하나가 다세대 LRU(multi-generational LRU)이다. 이 둘을 어떻게 하나로 통합할 수 있을까?
- 사설 메모리 노드(private memory node) 지원
  : 장치가 제공하는 특수 목적 메모리를 더 잘 관리하는 방법.
  <li> <a href="/Articles/1073071/">major page fault를 더 잘 처리하는 방향</a>: 이 영역에서 많은 작업이 있었음에도, 페이지 폴트 처리에는 여전히 락 경합(lock contention)이 발생할 수 있다. 이 상황을 어떻게 개선할 수 있을까?
  <li> <a href="/Articles/1073103/">BPF를 이용한 사용자 지정 페이지 캐시 정책</a>:
  사용자 공간이 페이지 캐시에서 페이지가 언제 축출(evict)되는지에 영향을 줄 수 있게 만들기.
- 더 빠른 `this_cpu` 연산을 찾아서
  : x86이 아닌 아키텍처에서 CPU별 변수를 더 빠르게 만들기 위한 방안.
  <li> <a href="/Articles/1073400/">계층 인식(tier-aware) 메모리 컨트롤러 제한</a>:
  계층형 메모리(tiered memory) 시스템 지원을 메모리 컨트롤러에 추가하기.
  <li> <a href="/Articles/1073407/">투명 대형 페이지의 더 나은 자동 관리</a>: 투명 대형 페이지를 진정으로 투명하게 만들기 위한 계속되는 작업.
  <li> <a href="/Articles/1073418/">페이지 맵 카운트(page map count) 제거를 향한 추가 진전</a>: 페이지 매핑 회계를 단순화하려는 탐구는 계속된다.
  <li> <a href="/Articles/1073425/">메모리 디스크립터(memory descriptor)를 `struct page`에서 분리하기</a>: 거대한 메모리 디스크립터 전환의 다음 단계를 계획하기.[^c2-mm-track]

#### BPF track

- GCC 16과 그 이후의 BPF 지원
  : GCC의 BPF 지원 현황에 대한 업데이트.

#### Joint storage and memory-management sessions

- 읽기 및 쓰기 작업에 dma-buf 사용하기
  : dma-buf 사용을 더 효율적으로 만들기 위한 새로운 `io_uring` 기반 API.
- 플래시 친화적 스왑
  : 드라이브를 닳게 하지 않으면서 스와핑을 수행하는 방법(더 큰 스왑 하위시스템 주제의 일부로 다뤄짐).

#### Joint storage and filesystems sessions

- 버퍼드 원자적 쓰기(buffered atomic write), writethrough 등
  : PostgreSQL과 그 밖의 사용자를 위한 버퍼드 원자적 쓰기로 가는 길에 관한 여러 슬롯의 세션.[^c2-storage-topics]

#### Group photo

Linux Foundation이 촬영한 전통적인 단체 사진이다. 서밋의 더 많은 사진은 [LF flickr 사이트에서 찾을 수 있다](https://www.flickr.com/photos/linuxfoundation/sets/72177720332838072/).

> ![[Group photo]](https://static.lwn.net/images/2026/lsfmb-group-sm.jpg)

#### Acknowledgment

이 행사를 취재하기 위해 자그레브로 이동하는 LWN의 여행을 지원해 준 여행 후원사 Linux Foundation에 깊이 감사드린다.

[댓글(게시된 것 없음)](https://lwn.net/Articles/1071199/#Comments)

[^c2-lsfmm-scope]: LSFMM+BPF는 커널의 성능·확장성·안정성에 직접 연결되는 하위시스템 담당자들이 한자리에 모이는 개발자 중심 행사다. 이메일 토론만으로 합의하기 어려운 설계 방향, 유지관리 경계, API 형태를 대면으로 조율한다는 점에서 이후 커널 릴리스의 구조적 변화를 예고하는 경우가 많다.
[^c2-mm-track]: 메모리 관리 트랙의 주제들은 페이지 테이블, 페이지 캐시, NUMA, CXL, 스왑, 회수 알고리즘처럼 커널 전체 성능에 영향을 주는 핵심 영역을 포괄한다. 예를 들어 THP와 HugeTLB는 데이터베이스와 가상화 워크로드의 TLB 미스 비용을 줄일 수 있지만, 메모리 낭비와 단편화 문제를 동반하므로 정책과 자동화가 중요하다.
[^c2-storage-topics]: `dma-buf`, `io_uring`, 버퍼드 원자적 쓰기는 스토리지와 메모리 관리의 경계가 점점 더 밀접해지고 있음을 보여준다. 실제 시스템에서는 복사 비용을 줄이고, 데이터베이스의 내구성 보장을 단순화하며, 플래시 장치의 수명을 고려한 스왑 정책을 설계하는 데 이런 논의가 영향을 준다.

### [메모리 관리 유지관리의 새 시대](https://lwn.net/Articles/1070994/)

#### 요약

- Andrew Morton은 커널 메모리 관리 하위시스템 유지관리에서 점차 물러나겠다는 뜻을 밝혔고, LSFMM+BPF에서 향후 유지관리 모델이 논의되었다.
- 메모리 관리 코드는 `mm` 디렉터리 전반에 강하게 얽혀 있어 하위 영역별로 나누는 일이 쉽지 않다.
- David Hildenbrand가 메모리 관리 전체를 위한 catch-all 및 통합 트리(integration tree) 관리를 맡게 된다.
- Morton은 빠른 변화 속도를 가능하게 하는 여러 검증 계층을 설명하면서, 리뷰 부담이 소수에게 치우친 현실을 우려했다.
- 참석자들은 인간 리뷰어의 중요성, LLM 기반 리뷰 도구의 적절한 위치, 향후 작업 그룹 구성 필요성을 논의했다.

작성자

Jonathan Corbet

2026년 5월 7일

LSFMM+BPF

4월 21일, Andrew Morton은 커널의 메모리 관리 하위시스템 유지관리에서 점차 물러나기 시작할 생각이라고

알렸다.

그는 메모리 관리가 독자적인 하위시스템으로 인식되기 전부터 이 책임을 맡아 왔다. 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit의 메모리 관리 트랙 첫 세션 중 하나는 앞으로 이 유지관리를 어떻게 운영할지에 할애되었다. 아직 답해야 할 질문은 많다.[^c2-morton-transition]

Morton은 자신의 발표에 대한 반응을 거의 받지 못했다는 말로 시작했다. 그는 이것이 자신이 다른 이들에게 하위시스템에서 더 많은 책임을 맡아 달라고 요청하고 있었기 때문이라고 보았다. 개발자들은 많은 작업을 떠안아야 할 것이다. middle-ad

[![[Andrew Morton]](https://static.lwn.net/images/conf/2026/lsfmm/AndrewMorton-sm.png)](https://lwn.net/Articles/1071173/) 그 작업을 어떻게 분산할 수 있을지는 열린 질문이다. 커널의 `mm` 디렉터리에는 C 파일이 164개 있다. 간단히 검색해 보면 “THP”(transparent huge page), “cgroup”(control group), “NUMA” 같은 용어가 각각 그 많은 파일 중 상당수에서 나타난다. 다시 말해 핵심 메모리 관리 개념은 하위시스템 전체에 넓게 퍼져 있다. Morton은 코드를 옮기면 어느 정도 도움이 될 수는 있겠지만 크지는 않을 것이라고 말했다. 모든 것이 심하게 서로 연결되어 있어서 하위시스템을 나누려는 시도는 어려울 것이다. 하지만 그는 미소를 지으며 “그건 내 문제가 아니다”라고 덧붙였다.[^c2-mm-coupling]

분할이 얼마나 성공하든, 하위시스템 전체를 담당하는 포괄(catch-all) 트리는 언제나 필요할 것이다. 그 포괄 및 통합 트리 관리는 David Hildenbrand가 맡게 된다. Morton은 그 책임을 맡아 준 Hildenbrand에게 감사를 표했다.[^c2-integration-tree]

그는 메모리 관리 개발자들(그리고 커널 전체 개발자들)에게는 나쁜 코드가 사용자에게 배포되는 것을 막기 위한 여러 방어 계층이 있다고 말했다. 커뮤니티는 임의의 물건을 내놓을 수 있지만, 그것은 `-mm` 트리에서 몇 주 동안 테스트를 거치고, 메인라인 커널에 들어간 뒤에도 다시 몇 주의 테스트를 더 거친다. 수정 사항은 수년 동안 안정(stable) 커널로 백포트될 수 있고, 배포판은 추가적인 지원 계층을 제공한다. 더 최근에는 [Sashiko](https://lwn.net/Articles/1064830/)가 새로운 수준의 패치 리뷰를 제공하면서 또 하나의 방어 계층이 되었다.[^c2-defense-layers]

그는 개발자들이 처음부터 제품 수준(production-quality)의 코드를 만들고 있는 것이 아니라는 점을 인식해야 한다고 말했다. 그들은 기술을 만들고, 다른 이들이 그것을 제품으로 바꾸도록 하는 것이다. 이 모든 방어 계층 덕분에 개발자들은 “공격적인 변화 속도”를 추구할 수 있다. 하지만 그 변화 속도에는 단점도 있다. 리뷰어에게 큰 압박을 준다는 점이다. 메모리 관리 하위시스템 내부에서 리뷰 작업은 꽤 한쪽으로 치우쳐 있다. 소수의 사람이 리뷰의 대부분을 수행하는 반면, 많은 개발자는 리뷰 부담을 거의 지지 않는다. 그는 일이 왜 그런 식으로 돌아가는지 이해하지 못하며, 상황이 개선될 수 있기를 바란다.[^c2-review-load]

그는 메모리 관리 팀이 훌륭한 사람들의 모임이라고 말했다. 그들은 협력적이고 서로 돕는 데 빠르다. 하지만 그는 시간이 지나면서 이 커뮤니티가 커널의 다른 부분이나 다른 오픈소스 프로젝트처럼 퇴행할 수 있다는 점을 걱정한다. 유지관리자들이 너무 바빠서 이메일이 무시되는 곳들 말이다. 기여자의 메시지를 무시하는 것은 부끄럽고 용납할 수 없는 일이라고 그는 말했다. 하지만 그는 메모리 관리 커뮤니티가 그 문화를 가치 있게 여기며 유지하기 위해 노력할 것이라고 생각한다.

Matthew Wilcox는 누군가 커뮤니티에 어떻게 입문하면 되는지 물어보면, 항상 패치 리뷰부터 시작하라고 권한다고 말했다. 하지만 그 조언은 종종 받아들여지지 않는다. 그는 이메일에 답하려고 노력하지만, 어떤 날에는 들어온 모든 메시지에 답하는 것이 그저 불가능하다고 덧붙였다. Dan Williams는 커뮤니티가 응답이 필요할 때 Morton이 압력을 가해 주는 데 오랫동안 의존해 왔다고 말했다. 앞으로는 Hildenbrand와 다른 이들이 그 압력을 가해야 할 것이다.[^c2-review-culture]

Hildenbrand는 사람들이 각자의 몫을 하고 있는지 확인하는 누군가가 항상 필요할 것이라고 답했다. 그것이 이 하위시스템을 훌륭하게 만드는 요소의 일부라는 것이다. 메모리 관리 내부의 개발자 좌절 수준은 다른 많은 하위시스템보다 낮다. 다만 그는 LLM 기반 리뷰 도구의 등장을 조금 걱정하고 있다. 모두가 더 많은 인간 리뷰어가 필요하다는 데 동의하므로, 그는 Sashiko 같은 도구의 리뷰가 공개 메일링 리스트에 게시되어서는 안 된다고 생각한다. 이제 막 길을 익히고 있는 초기 단계 리뷰어는 자동 리뷰가 이미 많은 문제를 찾아냈다는 것을 보면 의욕을 잃을 수 있다. Hildenbrand는 자동 리뷰가 첫 번째 방어선이 아니라 마지막 방어선 중 하나여야 한다고 말했다.[^c2-llm-review]

[![[David Hildenbrand]](https://static.lwn.net/images/conf/2026/lsfmm/DavidHildenbrand-sm.png)](https://lwn.net/Articles/1071174/) Liam Howlett은 일회성 기여자에게 LLM 기반 리뷰를 보내면 나쁜 아이디어를 정당화해 주는 효과가 있을 수 있다고 말했다. 여러 참가자는 이런 도구가 버그를 찾는 데는 능하지만, 어떤 변경을 애초에 해야 하는지 여부라는 질문을 다루는 데는 덜 능하다고 제안했다. Morton은 초보 리뷰어가 숙련된 개발자라면 지나칠 수 있는 이해 가능성(understandability) 문제에 자주 집중한다고 말했다. 그것 역시 중요한 피드백이다.[^c2-llm-limits]

세션 끝에서 Hildenbrand는 앞으로 나서서 통합 트리 운영 책임을 자신에게 맡겨 준 커뮤니티에 감사를 표했다. 다만 그는 Morton에게 커뮤니티가 그를 쉽게 놓아주지는 않을 것이라고 경고했다. 질문이 아주 많을 것이기 때문이다. Hildenbrand는 메모리 관리 커뮤니티의 향후 개발 모델이 어떻게 작동해야 하는지 알아내기 위해 어떤 형태의 작업 그룹이 만들어질 것이라고 말했다. 더 많은 하위 구성요소가 자체 트리로 이동할 수도 있지만, 모든 것을 하나로 끌어모으기 위한 통합 트리는 언제나 존재할 것이다. 그는 그 모든 일을 혼자 하지는 않을 것임을 알리며 마무리했다.[^c2-working-group]

[댓글(10개 게시됨)](https://lwn.net/Articles/1070994/#Comments)

[^c2-morton-transition]: Andrew Morton은 오랫동안 `-mm` 트리와 메모리 관리 패치 흐름의 중심에 있었기 때문에, 그의 단계적 후퇴는 단순한 인사 변화가 아니라 커널 개발 프로세스의 리스크 관리 방식 변화다. 특히 메모리 관리는 거의 모든 워크로드와 아키텍처에 영향을 주므로 유지관리 책임의 분산이 안정적으로 이뤄져야 한다.
[^c2-mm-coupling]: `mm` 하위시스템의 강한 결합은 THP, cgroup, NUMA 같은 기능이 파일 단위로 깔끔하게 분리되지 않고 정책·회계·폴트 처리·회수 경로를 가로질러 얽혀 있음을 뜻한다. 따라서 유지관리 영역을 나누려면 코드 소유권뿐 아니라 설계 리뷰와 통합 테스트 책임도 함께 정의해야 한다.
[^c2-integration-tree]: 통합 트리는 여러 하위 영역에서 온 패치가 서로 충돌하지 않고 메인라인에 들어갈 준비가 되었는지 확인하는 완충 지대다. 메모리 관리처럼 상호작용이 많은 영역에서는 개별 트리만으로는 전체 동작을 검증하기 어려워, catch-all 트리가 회귀(regression)를 줄이는 핵심 역할을 한다.
[^c2-defense-layers]: `-mm` 트리, 메인라인 테스트 기간, stable 백포트, 배포판 검증은 각각 다른 시간 규모와 사용자 집단에서 문제를 걸러낸다. 커널 개발에서는 모든 버그를 사전에 막기 어렵기 때문에, 이런 다층 방어는 빠른 개발 속도와 사용자 안정성 사이의 균형을 맞추는 실용적 장치다.
[^c2-review-load]: 리뷰 부담이 소수에게 집중되면 병목이 생기고 번아웃 위험이 커지며, 중요한 설계 문제가 늦게 발견될 수 있다. 반대로 더 많은 개발자가 리뷰에 참여하면 지식이 분산되고 유지관리 승계가 쉬워지지만, 리뷰 품질을 유지하기 위한 문화와 교육도 필요하다.
[^c2-review-culture]: 커널 메일링 리스트에서의 응답성은 기여자가 계속 참여할지 여부를 좌우한다. 특히 메모리 관리처럼 진입 장벽이 높은 영역에서는 “리뷰부터 시작하라”는 조언이 코드 작성보다 안전하게 지식을 쌓는 경로가 될 수 있다.
[^c2-llm-review]: LLM 기반 리뷰 도구는 흔한 버그 패턴이나 문서화 문제를 빠르게 찾을 수 있지만, 공개 리스트에서 인간 초보 리뷰어보다 앞서 나가면 학습 기회를 빼앗을 수 있다. 실무적으로는 자동 리뷰를 사전 점검이나 후방 방어선으로 배치하고, 최종 판단은 경험 있는 인간 리뷰어가 맡는 구성이 더 안전하다.
[^c2-llm-limits]: 커널 패치 리뷰에서 “코드가 맞는가”와 “이 변경이 커널에 들어가야 하는가”는 다른 질문이다. 후자는 장기 유지보수 비용, ABI/API 영향, 아키텍처별 부작용, 기존 설계와의 일관성을 요구하므로 현재의 자동화 도구만으로는 판단하기 어렵다.
[^c2-working-group]: 작업 그룹은 유지관리 트리 분할, 리뷰 책임, 통합 절차, 자동화 도구 사용 원칙을 명문화하는 장이 될 수 있다. 이는 Morton 개인에게 집중되던 암묵지를 커뮤니티 프로세스로 전환하는 데 필요한 단계다.

---

### [읽기와 쓰기 작업에 dma-buf 사용하기](https://lwn.net/Articles/1072317/)

#### 요약

- dma-buf를 `io_uring`에 등록해 설정 비용을 여러 I/O 작업에 분산시키려는 새로운 패치 시리즈가 논의되었다.
- 목표는 네트워킹과 스토리지 서브시스템에서 dma-buf를 일관되게 사용할 수 있는 공통 인프라를 만드는 것이다.
- P2PDMA만으로는 사용자 공간이 이미 가진 dma-buf 활용, IOMMU 최적화, 맵 무효화 같은 요구를 충분히 만족하지 못한다는 지적이 있었다.
- IOMMU 사전 매핑(pre-mapping) 벤치마크는 최대 8.8배 성능 향상을 보였지만, 보안·권한·자원 고갈 우려도 함께 제기되었다.
- scatterlist 의존성과 향후 파일시스템 지원 방식은 아직 정리가 필요한 과제로 남았다.

작성자

Jonathan Corbet

2026년 5월 12일

LSFMM+BPF

커널의 dma-buf 서브시스템은 드라이버들이 메모리 버퍼를 공유할 수 있는 방법을 제공하며, 보통 효율적인 장치 간(device-to-device) I/O를 지원하는 데 쓰인다. 2026년 Linux Storage, Filesystem, Memory Management, and BPF Summit에서 Pavel Begunkov는 Kanchan Joshi의 도움을 받아 스토리지와 메모리 관리 트랙의 합동 세션을 이끌었다. 이 세션에서는 dma-buf 사용을 한층 더 효율화하고, 사용자 공간이 시작한 읽기 및 쓰기 작업에서도 dma-buf를 사용할 수 있게 하는 방법을 살펴보았다.[^c3a-dmabuf-overview]

Begunkov는 Keith Busch의 [2022년 패치 세트](https://lwn.net/ml/io-uring/20220805162444.3985535-1-kbusch@fb.com/)를 언급하며 발표를 시작했다. 이 패치 세트는 dma-buf가 효율적인 I/O 작업을 가능하게 할 수는 있지만, 실제 작업이 일어나기 전에 비싼 설정(setup) 작업이 꽤 많이 필요한 경우가 많다는 점을 지적했다. 여기에는 여러 내부 자료구조 생성, DMA 매핑 설정, 그리고 때로는 I/O 메모리 관리 장치(IOMMU)의 비용이 큰 구성 작업이 포함된다. 작업마다 새 dma-buf를 만들어야 한다면 그 작업이 반복되어 효율성의 상당 부분이 사라진다. Busch의 해법은 `io_uring`이 등록된 파일과 버퍼를 지원하는 방식과 비슷하게 dma-buf를 [`io_uring`](https://man7.org/linux/man-pages/man7/io_uring.7.html) 서브시스템에 등록할 수 있게 하는 것이었다. 그렇게 하면 등록된 dma-buf를 `io_uring` 안에서 재사용할 수 있어, 설정 비용을 여러 작업에 분산할 수 있다.[^c3a-iouring-registration]

[![[Pavel Begunkov]](https://static.lwn.net/images/conf/2026/lsfmm/PavelBegunkov-sm.png)](https://lwn.net/Articles/1072331/) 그 시리즈는 메인라인에 들어가지 못했지만, 그 개념에 대한 관심은 여전히 남아 있다. Begunkov는 Busch의 작업을 확장하는 [자체 패치 시리즈](https://lwn.net/ml/io-uring/cover.1763725387.git.asml.silence@gmail.com/)를 가지고 있다. 그는 세션에서 자신의 목표가 네트워킹과 스토리지 서브시스템에서 dma-buf를 사용할 수 있도록 일관된 인프라를 만드는 것이라고 말했다. 그는 사용자 공간 API로 `io_uring` 등록 버퍼를 선택했으며, dma-buf에는 별도의 특수 등록 작업이 필요하다. 사용자 공간은 dma-buf를 지원하는 서브시스템에서 dma-buf를 얻은 뒤, 그와 연결된 파일 디스크립터를 `io_uring`에 등록한다. 이후에는 I/O에 사용할 수 있게 된다.

이 작업에는 몇 가지 요구사항이 있다. API로 `io_uring`을 사용하더라도 이 메커니즘의 내부 구조는 `io_uring` 전용이어서는 안 되며, 결국 파일시스템과 그 밖의 영역으로 확장 가능해야 한다. 또한 dma-buf 제공자가 수행하는 맵 무효화(map invalidation)도 지원해야 한다. 내부 API는 새로운 `io_dmabuf_token` 구조체를 중심으로 구성되며, 이는 dma-buf를 구현하는 드라이버와 `io_uring` 사이의 인터페이스다. 개별 I/O 요청은 `io_dmabuf_map` 구조체로 추적되며, 이는 I/O 요청을 드라이버별 방식으로 순회할 수 있게 해주는 [iomap 서브시스템](https://docs.kernel.org/filesystems/iomap/index.html)의 지원을 받는다. 패치 시리즈는 진전되고 있지만 아직 준비가 끝난 상태는 아니다.[^c3a-map-invalidation]

그는 이따금 제기되는 질문 중 하나가 이 목적에 [P2PDMA](https://lwn.net/Articles/767281/)를 써야 하는지 여부라고 말했다. P2PDMA만으로 충분하지 않은 이유는 몇 가지 있다. 우선 사용자 공간이 이미 가지고 있을 수 있는 dma-buf를 사용할 수 없는데, 이는 필수 요구사항이다. 새로운 API는 더 저렴한 중간 데이터 변환, 더 나은 IOMMU 사용 최적화, 맵 무효화 지원을 제공할 수 있다. 청중 중 한 명은 P2PDMA도 맵 무효화를 지원한다고 말했다. 물론 P2PDMA를 쓰지 않는 데 따른 단점은 새 API가 필요하다는 점, 그리고 현재로서는 그 API가 `io_uring`으로 제한된다는 점이다.[^c3a-p2pdma]

middle-ad Begunkov는 사용 사례로 일반 호스트 메모리에서 IOMMU 사용을 최적화해야 하는 애플리케이션을 들었다. 네트워크 인터페이스와 파일시스템 사이에서 데이터를 쉽게 이동할 수 있으면 이득을 볼 네트워크 스토리지 솔루션도 여럿 있다. 또한 어떤 회사가 자사 GPU 인프라에 이 기능을 쓰고 싶어 하는 것으로 보인다. Joshi는 NVMe 서브시스템도 무엇보다 패스스루(pass-through) 지원을 구현하는 데 이 기능의 이점을 얻을 수 있다고 덧붙였다. 향후 계획에는 더 많은 블록 드라이버, SCSI 서브시스템, 파일시스템에 대한 지원 추가가 포함된다.

IOMMU 사전 매핑(pre-mapping) 벤치마크에서는 최대 8.8배의 성능 향상이 나타났다. 특히 사전 매핑은 lazy 모드와 strict 모드 중 어느 쪽에서 IOMMU를 사용하더라도 발생하는 성능 페널티를 완전히 제거했다. 두 모드는 모두 장치 격리를 강제하기 위해 매핑 변경 시 일정량의 TLB 무효화(invalidation)를 수행한다. 다시 말해, 최대 성능을 얻기 위해 일부가 덜 안전하다고 보는 IOMMU 패스스루 모드를 더 이상 사용할 필요가 없다는 뜻이다.[^c3a-iommu-performance]

하지만 Jason Gunthorpe는 패스스루 모드만으로 충분하지 않은 이유가 무엇인지, 그리고 사전 매핑의 추가 복잡성이 어떻게 정당화되는지 의문을 제기했다. Begunkov는 패스스루 모드에서 벗어나고 싶은 이유가 보안 우려 때문이라고 답했다. Gunthorpe는 더 나은 해법은 작업이 완료된 뒤 IOMMU 매핑을 남겨두지 않는 것이라고 말했다. Christoph Hellwig는 일부 사이트가 IOMMU 사용을 요구하고 있으며, IOMMU가 수행하는 메모리 병합(coalescing)이 성능에 도움이 되므로 좋은 성능을 내는 완전한 IOMMU 지원이 필요하다고 말했다. Gunthorpe는 그것이 타당한 지적임을 인정했다. Matthew Wilcox는 버퍼를 매핑하는 시점이 기반 메모리를 조각 모음(defragment)하기에 좋은 때이며, 그렇게 하면 애초에 병합이 필요 없어질 수 있다고 제안했다.

David Howells는 dma-buf의 오용(우발적이든 고의적이든)이 사용 가능한 IOMMU 슬롯을 모두 막아 문제를 일으킬 수 있다고 우려하며, 이 기능 사용에 권한(privilege)이 필요할지 물었다. Begunkov는 문제가 될 수 있다는 데 동의하며, 어떤 형태의 capability 검사가 필요할 것이라고 말했다.[^c3a-iommu-slots]

Christian Brauner는 이 기능이 scatterlist를 사용한다는 점에 이의를 제기했다. scatterlist는 개발자들이 결국 제거하고 싶어 하는 내부 API다. Hellwig는 dma-buf에는 여전히 scatterlist가 필요하므로 당장은 피할 수 없다고 답했다. dma-buf에서 scatterlist 의존성을 제거하는 문제에 대해 다소 초점이 흐린 논의가 있었지만, Hellwig는 Begunkov의 작업이 그 정리 작업이 끝나기를 기다리느라 지연되어서는 안 된다고 말했다. 시간이 다 되어가면서 파일시스템 접근을 어떻게 지원할 수 있을지에 대한 논의도 있었지만, 그와 관련된 패치는 아직 나오지 않았다.[^c3a-scatterlist]

[Comments (2 posted)](https://lwn.net/Articles/1072317/#Comments)

[^c3a-dmabuf-overview]: dma-buf는 GPU, 디스플레이, 네트워크, 스토리지 장치가 같은 물리 메모리 버퍼를 복사 없이 공유하게 해주는 리눅스 커널의 핵심 메커니즘이다. 장치 간 데이터 경로에서 복사를 줄이면 지연시간과 CPU 사용량을 크게 낮출 수 있지만, 매핑 수명과 소유권을 정확히 관리해야 한다.
[^c3a-iouring-registration]: `io_uring`의 등록 객체 모델은 반복 I/O에서 파일·버퍼 조회와 핀 고정(pin) 비용을 줄이기 위해 쓰인다. dma-buf 등록도 같은 철학을 따르며, 고성능 스토리지·네트워크 애플리케이션에서 per-operation 설정 비용을 amortize하는 실용적 효과가 있다.
[^c3a-map-invalidation]: 맵 무효화는 dma-buf 제공자가 버퍼 배치나 접근 가능성이 바뀌었음을 소비자에게 알리는 절차다. 이를 놓치면 장치가 더 이상 유효하지 않은 DMA 주소로 접근할 수 있어 데이터 손상이나 장치 오류로 이어질 수 있다.
[^c3a-p2pdma]: P2PDMA(peer-to-peer DMA)는 PCIe 장치들이 호스트 메모리를 거치지 않고 서로 데이터를 주고받게 하는 접근법이다. 하지만 사용자 공간에서 이미 관리 중인 dma-buf와 통합하거나 여러 서브시스템을 일관되게 다루는 데에는 별도의 API 설계가 필요할 수 있다.
[^c3a-iommu-performance]: IOMMU는 장치 DMA에 주소 변환과 격리를 제공해 보안을 높이지만, 매핑 변경 때 IOTLB/TLB 무효화 비용이 발생한다. 사전 매핑은 이 비용을 반복 경로 밖으로 밀어내 성능을 얻는 대신, 매핑 수명과 자원 소비를 더 신중히 제어해야 한다.
[^c3a-iommu-slots]: IOMMU 매핑 공간과 관련 캐시는 무한하지 않다. 권한 없는 프로세스가 오래 살아 있는 dma-buf 매핑을 대량으로 만들 수 있다면 서비스 거부(DoS)나 다른 장치의 I/O 성능 저하로 이어질 수 있어 capability나 한도 정책이 중요하다.
[^c3a-scatterlist]: scatterlist는 분산된 물리 페이지들을 하나의 DMA 작업 대상으로 표현하는 오래된 커널 내부 자료구조다. 많은 드라이버가 아직 이에 의존하므로 단기간 제거는 어렵지만, 새 API가 이 의존성을 고착화하지 않도록 하는 것이 장기 유지보수성에 중요하다.

### [투명 거대 페이지를 1GB로 확장하기](https://lwn.net/Articles/1071716/)

#### 요약

- Usama Arif는 투명 거대 페이지(THP)를 PMD 수준의 2MB를 넘어 PUD 수준의 1GB까지 확장하는 방안을 논의했다.
- 1GB THP는 테라바이트급 메모리를 가진 대규모 시스템에서 페이지 테이블 관리 비용과 TLB 압박을 줄일 수 있다.
- 기존 hugetlbfs는 정적 풀과 제한적인 fallback 때문에 투명한 1GB 페이지 제공 요구를 충분히 만족하지 못한다.
- 1GB THP 분할, 할당 대상 선정, CMA 필요성, compaction 개선, migration과 hotplug 처리 방식이 주요 쟁점으로 제기되었다.
- 초기 구현은 공유 메모리(shared memory)로 제한하고 shmfs 마운트 옵션으로 관리자가 제어하게 하자는 제안이 나왔다.

작성자

Jonathan Corbet

2026년 5월 12일

LSFMM+BPF

일반적으로 개발자들이 거대 페이지(huge page)를 이야기할 때는 CPU 아키텍처에 따라 1MB 또는 2MB 크기인 PMD 수준 페이지를 가리킨다. 하지만 대부분의 CPU는 다른 거대 페이지 크기도 지원할 수 있다. x86 시스템에서 PUD 수준 거대 페이지는 1GB의 데이터를 담는다. 이렇게 큰 페이지를 프로세스에 투명하게 제공하는 것은 대체로 실현 가능하지도, 바람직하지도 않다고 여겨져 왔지만, Usama Arif는 그 평가를 바꾸려 하고 있다. 2026년 Linux Storage, Filesystem, Memory Management, and BPF Summit에서 그는 메모리 관리 트랙 세션을 이끌며 투명 거대 페이지(transparent huge page, THP)를 진정으로 거대하게 만드는 방법을 다루었다.[^c3a-thp-levels]

middle-ad 대부분의 시스템에서는 1GB의 물리적으로 연속된 메모리 덩어리를 찾기가 어렵다. 특히 시스템이 한동안 동작해 메모리가 조각난 뒤에는 더욱 그렇다. 이렇게 큰 메모리 덩어리를 활용할 수 있는 애플리케이션도 상대적으로 드물었다. 찾기 어려운 자원을, 그 이득을 얻을 가능성이 낮은 프로세스에 투명하게 제공하려는 노력이 거의 없었던 것은 놀랄 일이 아니다. 하지만 Arif가 말문을 열며 설명했듯이, 대규모 설치 환경은 이제 테라바이트 단위의 장착 메모리로 동작하고 있다. 그런 시스템에서는 PMD 수준 거대 페이지가 더 이상 거대하지 않다. 그 모든 메모리를 관리하는 일은 확장성 문제를 낳으며, 1GB 단위로 관리하면 도움이 될 수 있다.[^c3a-thp-scale]

[![[Usama Arif]](https://static.lwn.net/images/conf/2026/lsfmm/UsamaArif-sm.png)](https://lwn.net/Articles/1071721/) 애플리케이션은 현재 [hugetlbfs](https://docs.kernel.org/mm/hugetlbfs_reserv.html) 서브시스템을 사용해 1GB 거대 페이지에 접근할 수 있다. 하지만 hugetlbfs는 정적 자원이며, 부팅 시 별도 풀을 설정해야 한다. 거대 페이지 할당 요청을 만족시킬 수 없을 때 fallback도 제공하지 않는다. Arif는 대형 애플리케이션을 1GB 거대 페이지로 뒷받침할 투명한 방법이 실제로 필요하다고 말했다. 그는 이 요구를 채우기 위한 RFC 패치 세트를 가지고 있으며, [2월에 게시된](https://lwn.net/ml/all/20260202005451.774496-1-usamaarif642@gmail.com/) 그 패치 세트는 예상보다 작고 덜 침습적인 것으로 드러났다.[^c3a-hugetlbfs]

Arif는 1GB 투명 거대 페이지 관리가 어떻게 동작할지에 대한 세부 사항으로 곧장 들어갔다. 현재 커널은 2MB PMD 수준 투명 거대 페이지를 만들 때, 나중에 그 거대 페이지를 분할해야 할 경우 PTE 수준으로 다시 매핑하는 데 사용할 수 있는 여분의 기본(base) 페이지 하나를 “예치(deposit)”한다. 이런 예치를 하는 이유는 분할이 메모리 압박에 대한 응답으로 일어날 수 있으므로, 먼저 추가 메모리를 할당하지 않고도 수행할 수 있어야 하기 때문이다. 이 단일 페이지는 THP가 살아 있는 동안 낭비되지만, 메모리가 부족한 시기를 위한 일종의 보험 역할을 한다.[^c3a-page-table-deposit]

1GB THP를 위한 RFC 패치에서 Arif는 이 정책을 페이지 크기에 맞춰 확장했다. 즉 THP를 분할하는 데 필요할 PMD 수준 페이지 테이블과 512개의 PTE 수준 페이지 테이블을 위한 페이지들을 예치했다. 이는 약 2MB의 낭비 메모리에 해당하므로 비싼 보험이다. David Hildenbrand는 PMD 수준과 PUD 수준 THP 모두에 대해 이런 사전 할당의 필요성에 [의문을 제기한](https://lwn.net/ml/all/ee5bd77f-87ad-4640-a974-304b488e4c64@kernel.org/) 바 있었고, 그래서 Arif는 이제 페이지 테이블 예치 없이 진행하는 방안을 고려하고 있었다. 세션에서 Hildenbrand는 시스템이 1GB 거대 페이지를 분할하고 있다면 누군가가 무언가를 잘못하고 있는 것이라고 말했다. 가장 큰 시스템에서도 그런 페이지는 희소한 자원이며, 가능하다면 온전하게 유지해야 한다는 것이다.

Hildenbrand는 고려해야 할 질문은 어떤 프로세스에 1GB THP를 줄지 어떻게 결정할 것인가라고 말했다. Kiryl Shutsemau는 프로세스가 [`madvise()`](https://man7.org/linux/man-pages/man2/madvise.2.html)로 이를 요청할 수 있다고 제안했지만, Hildenbrand는 여러 이유로 문제가 될 것이라고 말했다. 이어 Shutsemau는 실제로는 1GB THP를 완전히 활용할 수 없는 프로세스가 이를 요청하는 경우를 우려했다. Arif는 바로 그런 경우 때문에 그 페이지들을 분할하는 기능이 동작해야 한다고 답했다.[^c3a-madvise-policy]

Hildenbrand는 다시 한 번 그런 페이지 분할은 피해야 한다고 말하며, 더 똑똑한 할당 방식을 주장했다. 예를 들어 공유 메모리 영역으로 제한할 수도 있다. Arif는 그렇게 하면 사용자 공간이 올바르게 설정해야 하는 부담을 지게 된다고 말했다. 그는 더 투명한 해법을 원하고 있었다. Lorenzo Stoakes는 1GB 거대 페이지가 커널이 계속 통제해야 하는 자원이라고 말했다. Usama는 기본적으로는 시스템 관리자가 활성화하지 않는 한 할당되지 않을 것이라고 답했다.

Matthew Wilcox는 올바른 답은 1GB 거대 페이지가 더 이상 희소 자원이 아니게 만들 만큼 충분히 싸게 만드는 것이라고 말했다. Johannes Weiner는 1GB THP에서 이득을 볼 수 있는 애플리케이션이 많지만, 그 애플리케이션이나 사용자들이 그 사실을 모른다고 말했다. 그의 고용주에서는 1GB 거대 페이지를 광범위하게 배포해 왔고, 그로부터 많은 성능 이점을 보고 있다. 그는 1GB THP를 널리 나눠준 다음, 그것들이 충분히 사용되지 않는 사례를 고쳐 나가자고 제안했다.

Arif는 이어서 1GB THP를 제공하려면 [연속 메모리 할당자(contiguous memory allocator, CMA)](https://lwn.net/Articles/486301/)를 사용해야 하는지에 대한 질문으로 넘어갔다. 그의 패치 시리즈는 CMA 없이 동작하지만, 그 크기의 거대 페이지를 할당하는 일은 어려울 수 있다. 문제의 일부는 메모리 관리 서브시스템의 compaction 코드가 현재 PMD 수준에서 동작하기 때문에, 1GB 거대 페이지를 위해 메모리 조각 모음을 성공시키지 못한다는 점이라고 그는 말했다. 그는 1GB 덩어리를 더 쉽게 할당할 수 있게 하려는 Rik van Riel의 진행 중인 [작업](https://lwn.net/ml/all/20260430202233.111010-1-riel@surriel.com/)도 언급했다.[^c3a-cma-compaction]

Arif는 1GB THP 분할도 열린 질문이라고 말했다. 현재 패치 세트는 그런 페이지를 분할하라는 요청을 받으면 PTE 수준까지 모두 분해해 262,144개의 기본 페이지를 만든다. 그는 512개의 PMD 수준 거대 페이지로만 분할한 뒤, 그중 하나만 PTE 수준으로 더 분할하는 방안을 고려하고 있다. 그는 그것이 받아들일 만한 전략인지 물었다. 회의장에 비교적 침묵이 흐른 것은 적어도 그 아이디어에 대한 실질적 우려가 없었음을 시사했다.[^c3a-splitting]

하지만 그가 `khugepaged` 커널 스레드가 기존 프로세스 메모리에서 1GB THP를 조립하려고 시도해야 하는지 물었을 때, 답은 분명한 “아니오”였다. 초기 매핑 시점에 이를 할당하는 것이 바람직한 접근으로 보인다. 다만 `MADV_COLLAPSE` `madvise()` 호출에 대한 응답으로 사후에 생성하는 것은 허용 가능할 수도 있다.

1GB THP의 migration도 또 다른 과제다. 대상 노드에서 1GB 페이지를 찾는 것은 어려울 수 있다. 대안은 이 페이지들의 migration을 막거나, 아니면 분할하는 것이다. migration을 막는 것은 단순한 해법이지만 투명성이라는 측면을 잃게 되고 메모리 hotplug를 깨뜨릴 수 있다. 분할을 택하면 hotplug와 NUMA balancing은 동작하겠지만 1GB 매핑은 사라진다. 어느 대안이 최선인지, 또는 덜 나쁜지는 분명하지 않다.[^c3a-migration-hotplug]

그룹이 그 문제를 논의하려 했을 수도 있지만, 이 시점에서 세션은 배정된 시간을 훨씬 넘긴 상태였다. Hildenbrand는 초기 구현이 공유 메모리에서만 동작해야 한다고 제안하며 세션을 마무리했다. 그렇게 하면 구현의 여러 측면이 단순해질 것이다. 또한 관리자가 이 기능에 대한 접근을 제어할 수 있게 하는 shmfs 마운트 옵션을 추가하는 것도 가능할 것이다.[^c3a-shmfs]

[Comments (3 posted)](https://lwn.net/Articles/1071716/#Comments)

[^c3a-thp-levels]: x86의 페이지 테이블 계층에서 PMD 수준 huge page는 보통 2MB, PUD 수준 huge page는 1GB 매핑을 뜻한다. 페이지 크기가 커질수록 TLB 항목 하나가 더 많은 메모리를 덮어 TLB miss와 페이지 테이블 관리 비용을 줄일 수 있다.
[^c3a-thp-scale]: 테라바이트급 메모리 시스템에서는 2MB 단위 매핑만으로도 페이지 테이블 수와 메모리 관리 작업량이 커진다. 1GB THP는 대규모 메모리 워크로드에서 커널 오버헤드를 줄이는 잠재력이 있지만, 물리 연속성 요구 때문에 할당 실패와 단편화 문제가 커진다.
[^c3a-hugetlbfs]: hugetlbfs는 명시적으로 예약된 huge page 풀을 애플리케이션에 제공하므로 예측 가능하지만 유연성이 낮다. THP 방식은 커널이 일반 메모리 할당 경로에서 자동으로 큰 페이지를 제공하려는 접근이라 운영 부담을 줄일 수 있다.
[^c3a-page-table-deposit]: THP 분할에는 더 작은 페이지 단위의 페이지 테이블이 필요하다. 메모리 압박 상황에서 분할하려고 추가 페이지 테이블 메모리를 새로 할당하면 실패할 수 있으므로, 기존 커널은 작은 “보험”을 미리 확보해 둔다.
[^c3a-madvise-policy]: `madvise()`는 프로세스가 커널에 메모리 사용 의도를 힌트로 전달하는 인터페이스다. 1GB THP처럼 비싼 자원은 애플리케이션 힌트만 믿고 배정하면 낭비될 수 있어, 커널 정책과 관리자 제어가 함께 필요하다.
[^c3a-cma-compaction]: CMA는 큰 연속 물리 메모리 영역을 확보하기 위해 예약 영역을 관리하는 메커니즘이다. 범용 THP가 CMA에 의존하면 유연성이 줄 수 있으므로, 일반 메모리 compaction이 1GB 단위까지 효과적으로 동작하도록 개선하는 것이 중요하다.
[^c3a-splitting]: 1GB 페이지 하나는 4KB 기본 페이지 262,144개에 해당한다. 이를 한 번에 모두 쪼개면 페이지 테이블과 rmap, LRU 처리 비용이 커지므로, 필요한 하위 범위만 단계적으로 분할하는 전략이 실용적일 수 있다.
[^c3a-migration-hotplug]: NUMA balancing과 memory hotplug는 페이지를 다른 노드나 장치 상태에 맞춰 이동할 수 있어야 제대로 동작한다. 1GB THP는 목적지에서 같은 크기의 연속 공간을 찾아야 하므로 이동성이 떨어지고, 이는 데이터센터 운영과 온라인 메모리 유지보수에 영향을 준다.
[^c3a-shmfs]: shmfs(tmpfs 기반 공유 메모리)는 여러 프로세스가 함께 쓰는 큰 매핑을 만들기 쉬운 경로다. 초기 대상을 공유 메모리로 제한하면 COW, 익명 메모리, 부분 사용률 같은 복잡한 경우를 줄이면서 1GB THP의 실효성을 시험할 수 있다.

---

### [mshare 다시 살펴보기](https://lwn.net/Articles/1072333/)

#### 요약

- `mshare`는 여러 관련 없는 프로세스가 공유 메모리 영역뿐 아니라 그 영역을 가리키는 페이지 테이블(page table)도 함께 쓰게 하려는 제안이다.
- 최신 설계는 특수 `msharefs` 파일 대신 다시 시스템 호출 API(`mshare_create()`, `mshare_attach()` 등)를 중심으로 이동했다.
- 공유 영역의 수명과 소유권은 생성 프로세스에 묶이며, 생성자가 종료하거나 파일 디스크립터를 닫으면 다른 프로세스의 매핑도 제거된다.
- 남은 과제는 페이지 테이블 순회와 잠금, RSS 통계 노출, 소유권 이전, TLB 플러시 처리 등이다.
- 논의에서는 HPC, Android Zygote 같은 사용 사례와 함께 `hugetlbfs`의 기존 페이지 테이블 공유를 장기적으로 대체할 가능성이 언급되었다.

By

Jonathan Corbet

2026년 5월 13일

LSFMM+BPF

Linux는 프로세스 사이에서 메모리를 공유할 수 있지만, 각 프로세스는 (거의 언제나) 자기만의 페이지 테이블(page table) 집합을 가진다. 엄청나게 많은 프로세스가 하나의 메모리 영역을 공유하는 상황에서는, 페이지 테이블들의 총 크기가 공유 메모리 자체의 크기를 넘어설 수 있다. 그래서 공유 메모리를 가리키는 페이지 테이블을 서로 관련 없는 프로세스들이 공유할 수 있게 하려는 관심은 오래전부터 있었다. Anthony Yznaga는 이 아이디어("mshare"로 알려져 있다)를 앞으로 밀어붙이려는 최신 개발자이며, 그는 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

(LSFMM+BPF)의 메모리 관리(memory-management) 트랙 토론에서 이 작업의 현황을 설명했다.[^c3b-mshare-page-tables]

[^c3b-mshare-page-tables]: 리눅스에서 페이지 테이블은 가상 주소를 물리 메모리로 변환하는 핵심 자료구조다. 메모리 내용은 공유하더라도 각 프로세스가 별도 페이지 테이블을 유지하면, 대규모 서버나 런타임처럼 동일 영역을 수천 개 프로세스가 매핑하는 경우 메타데이터 비용이 커진다. `mshare`의 실용적 의미는 메모리 절약뿐 아니라 TLB와 페이지 폴트 처리 비용까지 줄일 수 있는지에 있다.

[![[Anthony Yznaga]](https://static.lwn.net/images/conf/2026/lsfmm/AnthonyYznaga-sm.png)](https://lwn.net/Articles/1072355/) 페이지 테이블 공유가 LSFMM+BPF 의제에 오른 것은 이번이 처음도, 두 번째도 아니다. 가장 최근에는 Khalid Aziz가 이 제안에 대해 참석자들에게 업데이트했던 [2024년 논의](https://lwn.net/Articles/974512/)가 있었다. Aziz는 이후 은퇴했고, Yznaga가 그 작업을 이어받았다.

이 패치 시리즈의 전체적인 형태는 바뀌지 않았다. 공유는 어떤 프로세스가 특수 `msharefs` 파일시스템 안에 파일을 만들어 공유 메모리 영역을 생성할 때 시작된다. 그 영역은 자체 [`mm_struct` 구조체](https://elixir.bootlin.com/linux/v7.0.5/source/include/linux/mm_types.h#L1123)와 함께 만들어지며, 이 구조체는 해당 영역의 페이지 테이블을 관리하는 데 쓰인다. 이후 공유에 참여하는 각 프로세스는 `msharefs` 파일을 열고 매핑함으로써 이 영역에 붙을 수 있고, 그 결과 프로세스의 주소 공간 안에 해당 영역을 나타내는 특수 가상 메모리 영역(VMA), 즉 "윈도우 VMA(window VMA)"가 생성된다. 페이지 폴트(page fault)와 기타 메모리 관리 작업은 윈도우 VMA를 만나면 특수 `mm_struct`로 이어지는 포인터를 따라가 그곳의 페이지 테이블을 대상으로 동작한다.[^c3b-mshare-mmstruct]

[^c3b-mshare-mmstruct]: `mm_struct`는 리눅스 커널에서 한 주소 공간의 메모리 매핑, 페이지 테이블, 통계, 잠금 등을 묶어 관리하는 구조체다. 보통 프로세스마다 하나의 `mm_struct`가 있지만, `mshare`는 공유 영역에 별도 `mm_struct`를 부여해 그 영역의 주소 변환 상태를 여러 프로세스가 함께 참조하도록 만든다. 이는 강력하지만, 기존 MM 코드가 "프로세스 주소 공간"을 전제로 삼는 지점마다 복잡도를 만든다.

적어도 2024년에는 그렇게 보였고, Yznaga가 [패치 세트의 업데이트 버전](https://lwn.net/ml/linux-mm/20250820010415.699353-1-anthony.yznaga@oracle.com/)을 게시했던 2025년에도 마찬가지였다. 하지만 이번 세션에서 그는 `mshare` 구현은 본질적으로 같지만 API는 예전 버전들처럼 다시 시스템 호출(system call) 형태로 돌아갔다고 밝혔다. 당시에는 단일 `mshare()` 시스템 호출이 제안되었지만, 이제는 호출 묶음 전체가 있다. 공유 영역은 이제 `mshare_create()`로 생성된다.

```

    int mshare_create(unsigned int flags);
```

이 호출은 새 영역을 나타내는 파일 디스크립터(file descriptor)를 반환한다. 지원되는 유일한 `flags` 값은 `O_CLOEXEC`이다. 영역의 크기는 이후 [`ftruncate()`](https://man7.org/linux/man-pages/man2/truncate.2.html) 호출로 설정해야 한다. `mshare_attach()` 호출은 공유 영역을 호출 프로세스의 주소 공간에 매핑한다.

```

    int mshare_attach(int fd, unsigned int offset, unsigned int size,
    		      void *addr, unsigned int flags);
```

(Yznaga가 슬라이드에서 매개변수 타입을 보여주지 않았으므로, 위 타입들은 필자가 그럴듯한 것으로 채워 넣은 것이다.) 공유 영역 안의 주소들에 대한 백킹 스토어(backing store)를 설정해 [`mmap()`](https://man7.org/linux/man-pages/man2/mmap.2.html) 호출과 동등한 일을 하는 `mshare_map()`도 있다. 이 영역의 관리를 제어하기 위한 `mshare_advise()`와 `mshare_protect()`를 비롯해 여러 다른 호출도 있다. Yznaga는 다른 프로세스가 이 영역을 어떻게 찾아 붙는지에 대해서는 자세히 설명하지 않았다.[^c3b-mshare-api]

[^c3b-mshare-api]: 파일 디스크립터 기반 API는 권한 전달, 수명 관리, 네임스페이스 상호작용을 명확히 만들 수 있지만, 어떤 프로세스가 그 디스크립터를 어떻게 발견하고 전달받는지는 실제 사용성에 큰 영향을 준다. 예를 들어 Unix 도메인 소켓을 통한 fd 전달, 파일시스템 경로 기반 발견, 런타임 관리 데몬 등이 각각 다른 보안·운영 모델을 만든다.

middle-ad 공유 영역의 소유권 모델은 다소 바뀌었다. `mshare_create()`를 호출한 프로세스가 그 프로세스의 생애 동안 소유자가 된다. 그 프로세스가 종료하거나 파일 디스크립터를 닫으면 영역은 사라지고 다른 프로세스의 매핑도 제거된다. 그는 이 변경이 컨트롤 그룹(control-group) 회계를 단순화하고, 영역의 수명을 명확히 하며, 상황이 거기까지 악화될 경우 OOM(out-of-memory) killer가 겨냥할 대상을 제공한다고 말했다.[^c3b-mshare-lifetime]

[^c3b-mshare-lifetime]: 공유 메모리의 "소유자"를 정하는 일은 단순한 API 취향 문제가 아니다. cgroup 메모리 과금, OOM 희생자 선정, 컨테이너 종료 시 정리, 권한 철회가 모두 소유권에 의존한다. 생성자 수명에 묶는 방식은 구현을 단순하게 만들지만, 장시간 살아야 하는 공유 영역에는 소유권 이전 기능이 필요해질 수 있다.

Yznaga는 현재 작업 중인 문제들을 요약하며 발표를 마쳤다. 그는 페이지 테이블 순회(page-table walking)가 큰 과제이며, 특히 윈도우 VMA와 mshare 영역의 VMA 사이에서 잠금을 올바르게 맞추는 일이 어렵다고 말했다. `mshare`를 사용하는 프로세스의 상주 집합 크기(resident-set-size, RSS) 통계는 잘못되어 있다. 공유 영역의 정보가 특수 `mm_struct`에 저장되지만 어디에도 노출되지 않기 때문이다. 현재 설계는 영역을 만든 프로세스가 계속 살아 있어야 한다. 생성자가 영역을 넘겨주고 종료할 수 있도록 어떤 형태의 소유권 이전 메커니즘이 있으면 가치가 있을 것이다.

그는 또한 이 기능의 잠재적 사용 사례를 더 찾고 있다. Jason Gunthorpe는 리소스를 공유해야 하는 고성능 컴퓨팅(high-performance-computing, HPC) 프로세스를 언급했으므로, 이 기능이 그 사용 사례에 동작할 수 있음을 보여주는 것이 좋을 것이다. 다른 참석자는 시스템의 모든 앱의 부모 역할을 하는 [Android Zygote 프로세스](https://source.android.com/docs/core/runtime/zygote)를 언급했다. 그런 프로세스들 사이에는 상당한 공유가 있고 따라서 `mshare`로 얻을 수 있는 잠재적 이익도 있지만, 한 프로세스가 그 영역에 가한 변경이 연결된 다른 프로세스에 보이면 안 된다. 따라서 그런 경우에는 페이지 테이블 공유를 해제(unshare)할 필요가 있다.[^c3b-mshare-usecases]

[^c3b-mshare-usecases]: Zygote 모델은 프로세스를 빠르게 복제하기 위해 초기 상태를 공유한다는 점에서 `mshare`와 잘 맞아 보이지만, 앱 격리와 copy-on-write 의미론이 더 중요하다. HPC에서는 성능과 메모리 절감이 우선일 수 있으나, Android에서는 보안 경계와 변경 가시성이 핵심 제약이 된다.

또 다른 참석자는 공유 영역에서 TLB 플러시(flush)가 어떻게 처리되는지 물었다. Yznaga의 답에 따르면 영역을 공유하는 모든 프로세스의 연결 리스트(linked list)가 있으며, TLB 플러시가 발생하면 그 리스트를 순회해 각 프로세스를 개별적으로 플러시한다. Gunthorpe는 이 리스트가 MMU notifier와 매우 비슷하게 들린다고 보았다. Yznaga는 notifier를 사용해 보았지만, 그 경우에는 동작하지 않았다고 말했다.[^c3b-mshare-tlb]

[^c3b-mshare-tlb]: TLB는 최근 주소 변환 결과를 CPU가 캐시하는 구조다. 여러 프로세스가 동일 페이지 테이블을 공유하면 한쪽의 매핑 변경이 다른 CPU와 프로세스의 TLB에도 반영되어야 하므로, 플러시 비용과 정확성이 핵심 병목이 될 수 있다. 잘못 처리하면 오래된 변환을 사용해 메모리 보호가 깨질 수 있다.

Matthew Wilcox는 각 프로세스가 공유 영역을 서로 다른 가상 주소에 매핑하도록 허용하면 기능의 복잡도가 증가한다고 지적했다. 어쩌면 그 영역을 모든 곳에서 같은 주소에 매핑하도록 요구하는 것이 유용한 단순화가 될 수 있지 않을까? 회의실의 반응은 이것이 인기 있는 생각이 아님을 분명히 했다. 세션은 Wilcox가 이 기능이 마침내 들어가면 현재 Linux 시스템에서 이런 종류의 공유를 얻을 수 있는 유일한 방법인 [hugetlbfs 서브시스템](https://docs.kernel.org/admin-guide/mm/hugetlbpage.html)이 구현한 페이지 테이블 공유를 제거할 수 있을 것이라고 제안하며 끝났다.

[댓글(5개 게시됨)](https://lwn.net/Articles/1072333/#Comments)

### [4KB 커널에서 64KB 기본 페이지를 제공하는 두 가지 방법](https://lwn.net/Articles/1071484/)

#### 요약

- 일부 아키텍처에서는 큰 기본 페이지(base page)가 성능을 높일 수 있지만, 메모리 낭비와 호환성 비용도 커진다.
- 첫 번째 제안은 커널은 4KB 페이지를 유지하면서 프로세스별로 64KB 페이지 크기를 보이게 하는 방식이다.
- 구현은 ABI 어댑터, 메모리 관리 변경, 아키텍처별 페이지 테이블 처리로 나뉘며, `/proc`, `mmap()`, ELF 로더, page cache 등 광범위한 수정이 필요하다.
- 두 번째 제안은 x86에서 커널 내부 관리 페이지(`PG_SIZE`)와 하드웨어 PTE 크기(`PTE_SIZE`)를 분리해 64KB 기본 페이지 효과를 얻자는 것이다.
- 참석자들은 COW, `userfaultfd()`, folio 의미론, 기존 4KB 애플리케이션 호환성 때문에 두 접근 모두 상당한 복잡도를 초래한다고 우려했다.

By

Jonathan Corbet

2026년 5월 11일

LSFMM+BPF

일부 CPU 아키텍처는 여러 가지 기본 페이지(base-page) 크기로 실행할 수 있다. 더 큰 크기를 사용하면 메모리 사용량 증가라는 비용을 치르는 대신 성능이 좋아지는 경우가 많다. 다른 아키텍처들은 더 제한적이다. 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

에서 메모리 관리 트랙의 두 세션은 기반 커널이 그렇게 동작하지 않을 때도 프로세스가 64KB 페이지 크기로 실행되게 하는 선택지를 탐구했다. 첫 번째 세션은 각 프로세스가 자기만의 페이지 크기를 갖도록 하는 데 초점을 맞췄고, 두 번째 세션은 x86 시스템에 64KB 페이지를 가져오는 문제를 다뤘다.[^c3b-64k-overview]

[^c3b-64k-overview]: 기본 페이지 크기는 커널의 할당 단위, 파일 매핑, 페이지 폴트, ABI 관찰 결과에 깊이 박혀 있다. 4KB와 64KB의 차이는 단순히 숫자만 바꾸는 문제가 아니라, 응용 프로그램이 보는 정렬·크기 규칙과 커널 내부 자료구조의 균형을 바꾸는 문제다.

#### 프로세스별 페이지 크기

64KB 페이지를 사용하면 성능은 향상되지만, 내부 단편화(internal fragmentation)와 상당한 메모리 낭비가 생길 수도 있다. 이런 메모리 사용 비용은 더 큰 기본 페이지 크기의 사용을 제한하는 경향이 있다. Ryan Roberts와 Dev Jain(원격 참여)은 두 세계의 장점을 모두 얻으려는 시도로, 시스템 전체의 페이지 크기와 다른 페이지 크기를 가진 프로세스를 실행할 수 있게 하는 계획을 발표했다.

[![[Ryan Roberts]](https://static.lwn.net/images/conf/2026/lsfmm/RyanRoberts-sm.png)](https://lwn.net/Articles/1071711/) Roberts는 큰 페이지 크기와 작은 페이지 크기를 쓰는 시스템 사이에 성능 격차가 있다고 말하며 시작했다. "무작위로 고른 벤치마크"에서는 더 큰 페이지 크기로 2–17%의 성능 향상을 얻을 수 있다. 하지만 그에 따른 메모리 사용량 증가는 사람들이 많은 아키텍처가 지원하는 표준 4KB 페이지 크기에 머물도록 만든다. 최근 일부 프로세서에서 볼 수 있는 contiguous-PTE 지원(물리적으로 연속된 페이지들이 하나의 translation lookaside buffer(TLB) 항목을 공유할 수 있는 기능)은 약간 도움이 되지만, 그 기능을 사용해도 성능 격차는 남아 있다.[^c3b-64k-performance]

[^c3b-64k-performance]: 큰 페이지는 같은 TLB 항목 수로 더 넓은 메모리 범위를 덮게 해 주소 변환 오버헤드를 줄인다. 그러나 작은 객체나 파일을 많이 다루는 워크로드에서는 64KB 단위로 메모리를 잡는 순간 사용하지 않는 공간이 늘어나 총 메모리 압박이 커질 수 있다.

성능 차이에는 여러 이유가 있다. 소프트웨어 측면에서 더 큰 페이지 크기는 페이지 폴트 수를 줄이고 커널의 LRU(least-recently-used) 리스트를 더 짧게 만든다. 하드웨어 측면에서 큰 페이지는 TLB 사용을 개선한다. 64KB 페이지로 실행되는 시스템은 TLB로 16배 넓은 메모리 영역을 덮을 수 있다. Arm CPU는 마지막 페이지 테이블 순회(page-table walk)의 결과를 캐시할 수 있어, 같은 페이지 테이블 엔트리(page-table entry, PTE) 페이지 안에 들어오는 주소 변환을 빠르게 한다. 더 큰 페이지 크기는 그 캐시의 적용 범위를 늘린다. 큰 페이지를 쓰면 페이지 테이블 자체도 더 조밀해져, TLB와 캐시에 미치는 영향을 줄인다.[^c3b-64k-tlb]

[^c3b-64k-tlb]: 페이지 폴트와 LRU 스캔은 커널 CPU 시간을 쓰고, TLB 미스는 하드웨어 페이지 테이블 순회를 유발한다. 따라서 페이지 크기는 애플리케이션 코드가 바뀌지 않아도 성능에 영향을 준다. 특히 대용량 메모리를 순차·무작위로 훑는 데이터베이스, 런타임, 과학 계산에서 차이가 커질 수 있다.

Roberts에 따르면 성능 격차를 좁히기 위한 아키텍처 수준의 작업이 진행 중이지만, 그 결과가 나오려면 아직 몇 년이 걸릴 것이다. 따라서 대신 소프트웨어 쪽에서 무엇을 할 수 있는지 탐구할 이유가 있다. 한 가지 가능성은 각 프로세스에 자기만의 페이지 크기를 주어, 큰 페이지에서 이익을 얻는 프로세스는 그것을 사용하되 시스템 전체에 더 높은 메모리 사용량을 강제하지 않도록 하는 것이다. 특히 Arm 아키텍처는 이 개념을 지원해, 커널은 4KB 페이지 크기를 유지하면서 개별 프로세스가 더 큰 페이지로 실행되게 할 수 있다.

Jain은 제안된 구현을 설명하기 위해 발표를 이어받았다. 구현은 세 계층으로 나뉜다. 첫 번째인 "ABI 어댑터(ABI adaptor)"는 커널의 페이지 크기와 특정 프로세스의 페이지 크기 사이의 차이를 숨기도록 설계되어 있다. 각 프로세스의 페이지 크기는 [`mm_struct`](https://elixir.bootlin.com/linux/v7.0.1/source/include/linux/mm_types.h#L1123) 구조체에 저장된다. 이 값은 프로세스가 fork할 때 보존되지만, [`execve()`](https://man7.org/linux/man-pages/man2/execve.2.html) 호출로 바뀔 수 있다. 여러 시스템 호출(예를 들어 [`mmap()`](https://man7.org/linux/man-pages/man2/mmap.2.html))은 길이와 정렬 매개변수를 커널의 페이지 크기에 맞게 수정한다. Jain은 그 작업은 꽤 직선적이지만, [`ioctl()`](https://man7.org/linux/man-pages/man2/ioctl.2.html) 호출은 더 많은 주의가 필요할 수 있다고 말했다. ELF 로더(loader)는 서로 다른 페이지 크기를 가진 프로세스의 정렬 요구 사항을 이해하도록 강화된다. 64KB 페이지로 실행 중인 프로세스가 64KB 커널에서 나올 법한 결과를 보도록, 여러 `/proc` 파일 구현에도 상당한 요령이 추가된다.[^c3b-64k-abi]

[^c3b-64k-abi]: ABI는 프로그램이 커널에 기대는 계약이다. `getpagesize()`, `/proc`, `mmap()` 정렬, ELF 세그먼트 배치가 서로 모순된 값을 보이면 애플리케이션과 런타임이 깨질 수 있다. 그래서 "64KB처럼 보이게" 만드는 층은 호환성의 핵심이지만, 동시에 커널 곳곳에 예외 처리를 늘린다.

두 번째 계층은 커널의 메모리 관리 서브시스템에 대한 수정 집합이다. 4KB 커널에서 더 큰 페이지 크기를 쓰는 프로세스에 64KB 페이지를 제공하는 데, 투명 거대 페이지(transparent huge pages)를 구현하는 데 쓰이는 코드 경로의 상당 부분을 재사용할 수 있음이 드러났다. 그런 프로세스에 대해서는 할당 요청이 페이지 크기를 최소 허용 할당 크기로 지정한다. PMD 수준 거대 페이지 크기까지의 더 큰 페이지도 여전히 가능하다.

페이지 캐시(page cache)는 시스템의 모든 프로세스가 공유하므로 그 자체의 난제를 제기한다. 한 가지 선택지는 항상 64KB folio를 사용하는 것이지만, 그러면 작은 파일을 캐시할 때 꽤 많은 메모리를 낭비하게 된다. 그래서 페이지 캐시는 대부분의 경우 여전히 4KB 페이지를 사용한다. 64KB 프로세스가 `mmap()`으로 파일을 매핑하면, 그 파일의 모든 4KB folio는 페이지 캐시에서 제거되고, 이후 새 folio는 더 큰 크기로 캐시에 추가된다.[^c3b-64k-pagecache]

[^c3b-64k-pagecache]: 페이지 캐시는 파일 내용을 메모리에 보관해 I/O를 줄이는 전역 캐시다. 같은 파일을 4KB 프로세스와 64KB 프로세스가 동시에 사용할 수 있으므로, 캐시 단위(folio 크기)를 바꾸는 정책은 성능뿐 아니라 메모리 낭비, 캐시 무효화, 파일시스템 지원 여부와 직접 연결된다.

Kiryl Shutsemau는 이제 모든 파일시스템이 페이지 캐시의 더 큰 folio를 지원하는지 물었다. Matthew Wilcox는 그렇지 않다고 답하면서, 일부 파일시스템은 아직 그 지원을 추가하지 않은 "게으른 농땡이들(lazy slackers)"이라고 말했다. 그에 따르면 가장 큰 문제는 Btrfs다. Wilcox는 페이지 캐시 항목을 버리는 대안으로, 파일 끝을 넘어가지 않는 한 커널이 64KB folio를 계속 사용해도 된다고 제안했다.

Lorenzo Stoakes는 이 작업이 꽤 침습적으로 보인다며, 같은 이점 중 상당수를 제공할 수 있는 다중 크기 투명 거대 페이지(multi-size transparent huge pages, mTHPs)를 더 많이 활용하는 것만으로는 왜 불가능한지 물었다. Roberts는 mTHP가 더 큰 페이지 크기가 제공하는 모든 하드웨어 수준 이점을 제공하지는 않는다고 답했다. Stoakes는 또한 더 큰 페이지 크기를 광범위하게 사용하면 메모리 관리 서브시스템의 압축(compaction) 코드에 큰 압박을 줄 수 있다고 우려했다.[^c3b-64k-mthp]

[^c3b-64k-mthp]: mTHP는 기본 페이지를 바꾸지 않고도 여러 크기의 큰 folio를 쓰려는 접근이다. 이는 덜 파괴적이지만, 하드웨어가 "기본 페이지 크기"로 취급하는 단위가 바뀔 때 얻는 일부 TLB·페이지 테이블 이점과는 다를 수 있다. 그래서 논점은 성능 이득의 원천이 소프트웨어 묶음인지, 하드웨어 페이지 크기 자체인지에 있다.

시간이 부족해지자 Roberts는 의도했던 논의 일부(크기가 다른 페이지 테이블을 처리하는 아키텍처별 코드인 세 번째 계층 포함)를 건너뛰고, 곧바로 미해결 항목 목록으로 넘어갔다. 그 첫 번째는 커널이 64KB 프로세스의 컨텍스트에서 실행되는 동안 4KB 페이지 크기를 요구하는 작업을 시도하면 어떻게 되는가에 관한 것이었다. 한 선택지는 그 프로세스가 4KB 페이지로 되돌아가게 하는 것이다. 이는 기능적 정확성은 제공하지만 성능은 잃게 된다. 대안은 그 작업을 실패시키는 것이다. Roberts는 이 생각이 *겉보기에는* 더 단순하지만, 커널 전체에 많은 페이지 크기 검사를 흩뿌려야 할 것이라고 말했다.

사용자 공간 ABI 호환성은 어려운 문제다. 커널은 64KB 프로세스가 질의할 때 64KB 페이지로 실행 중인 척할 수 있지만, 모든 것을 에뮬레이션할 수는 없다. 예를 들어 일부 `/proc` 파일은 커널이 4KB 페이지를 사용하고 있다는 사실을 도저히 숨길 수 없다. 또한 64KB 프로세스가 [`/proc/*PID*/pagemap`](https://docs.kernel.org/admin-guide/mm/pagemap.html)을 읽을 때 4KB 프로세스를 표현하는 것도 불가능하다. 그 밖에도 에뮬레이션할 수 없는 일부 시스템 호출과 기능(예를 들어 [`userfaultfd()`](https://man7.org/linux/man-pages/man2/userfaultfd.2.html))이 있다.[^c3b-64k-pagemap]

[^c3b-64k-pagemap]: `pagemap`과 `userfaultfd()`는 가상 메모리 상태를 세밀하게 관찰·제어하는 인터페이스다. 페이지 크기를 다르게 보이게 하는 추상화는 일반 애플리케이션에는 충분할 수 있지만, 이런 저수준 인터페이스를 쓰는 런타임, VM, 체크포인트/복원 도구에는 거짓말이 쉽게 들통난다.

Roberts에 따르면 이런 문제를 다루는 한 방법은 64KB 프로세스의 기능을 "줄이는(defeature)" 것이다. 서로 다른 페이지 크기를 가진 프로세스들은 서로에게 보이지 않게 하고, 커널보다 큰 페이지 크기를 가진 프로세스는 `userfaultfd()` 같은 기능을 사용할 수 없게 한다. 64KB 프로세스에 제대로 표현할 수 없는 모든 작업은 단순히 실패하게 된다.

Roberts는 프로세스가 서로 다른 페이지 크기를 갖도록 허용하면 이점은 있지만, 까다로운 지점도 있다고 말하며 결론을 냈다. 이 기능을 추가하면 메모리 관리 서브시스템에도 상당한 churn(변경 소용돌이)이 생길 것이다. 그래도 그 이점은 그 수고를 감수할 만할 수도 있다.

middle-ad

#### x86을 위한 64KB 기본 페이지 크기

더 큰 기본 페이지를 사용하는 것은 그로부터 이익을 얻는 워크로드에는 좋은 해법이 될 수 있다. 하지만 작은 문제가 하나 있다. x86을 포함한 몇몇 사소한(minor) 아키텍처는 더 큰 기본 페이지 크기로 실행하는 것을 지원하지 않는다. 다음 세션에서 Shutsemau는 x86 시스템에서 이 제약을 우회하는 방법을 제안했다. 다만 모인 개발자들은 그 아이디어에 어느 정도 회의적이었다.

[![[Kiryl Shutsemau]](https://static.lwn.net/images/conf/2026/lsfmm/KirylShutsemau-sm.png)](https://lwn.net/Articles/1071712/) Shutsemau는 64KB 기본 페이지를 사용하면 Arm 프로세서의 "매우 중요한 워크로드"에서 1.7% 성능 향상을 제공할 수 있으며, 그는 그 속도 향상을 x86 시스템에도 가져오고 싶다고 말하며 시작했다. 더 큰 페이지를 사용하면 시스템 메모리 맵의 메모리 오버헤드를 줄이고, 쉬운(그리고 성능을 높이는) TLB 병합(coalescing)을 가능하게 하며, I/O 작업을 더 빠르게 하고, 1GB 거대 페이지(huge page) 할당도 더 쉽게 만들 수 있다. 그렇게 하려면 커널의 시스템 페이지 크기 개념을 둘로 나누어야 한다고 그는 말했다.[^c3b-x86-motivation]

[^c3b-x86-motivation]: x86 하드웨어의 기본 PTE 단위가 4KB라는 사실은 바꾸기 어렵다. 제안의 핵심은 하드웨어가 보는 단위와 커널·사용자 공간이 관리 단위로 삼는 "페이지"를 분리해, 소프트웨어적으로 64KB 페이지의 장점을 흉내 내자는 것이다.

현재 `PAGE_SIZE` 매크로는 커널 전반에서 하드웨어의 기본 페이지 크기를 나타내는 데 쓰인다. Shutsemau는 이를 단계적으로 없애고, 하드웨어가 보는 기본 페이지 크기를 설명하는 `PTE_SIZE`와 커널 내부에서 관리되고 사용자 공간에 보이는 페이지 크기인 `PG_SIZE`로 대체하겠다고 했다. `PAGE_SIZE` 매크로는 `PTE_SIZE`와 `PG_SIZE`가 같을 때에만 정의된다. 그는 페이지 프레임 번호(page-frame number)는 항상 `PTE_SIZE` 프레임을 가리킬 것이라고 말했다.

말할 필요도 없이, 커널에는 이런 새로운 세계관을 반영하기 위해 바꿔야 할 곳이 많다. 페이지 테이블 엔트리를 만드는 일은 더 복잡해진다. (`PG_SIZE`) 페이지 안의 오프셋을 고려해야 하기 때문이다. PTE를 다루는 모든 함수는 새 offset 매개변수를 얻게 된다. 커널은 64KB 페이지를 관리하지만, 사용자 공간은 늘 그랬듯 페이지 크기를 여전히 4KB로 보게 된다. 따라서 그런 시스템에서 성공적으로 실행하기 위해 사용자 공간 변경은 필요하지 않다.[^c3b-x86-pagesize-split]

[^c3b-x86-pagesize-split]: `PAGE_SIZE`는 리눅스 커널에서 가장 광범위하게 쓰이는 상수 중 하나다. 이를 둘로 쪼개면 명확한 모델을 만들 수 있지만, 기존 코드가 암묵적으로 "하드웨어 페이지 = 커널 folio 최소 단위 = 사용자 ABI 페이지"라고 가정한 곳을 모두 찾아 고쳐야 한다.

Shutsemau는 가장 어려운 부분이 페이지 폴트 처리라고 말했다. 폴트가 난 각 페이지마다 여러 PTE를 매핑해야 하기 때문이다. 사용자 공간에는 4KB 정렬 요구사항만 적용되므로, 가상 메모리 영역(VMA)이 64KB 페이지 한가운데에서 시작하거나 끝날 수 있다. 그 결과 페이지 폴트 핸들러는 폴트가 발생했을 때 페이지의 일부만 매핑하게 될 수도 있다. 그런 경우 페이지의 매핑되지 않은 부분은 그냥 낭비된다. 정렬되지 않은 페이지도 메모리 낭비로 이어질 수 있다.[^c3b-x86-faults]

[^c3b-x86-faults]: VMA 경계가 64KB 단위와 맞지 않으면 커널은 하나의 관리 단위를 여러 4KB PTE로 쪼개 일부만 노출해야 한다. 이는 메모리 낭비뿐 아니라 권한 비트, dirty/accessed 상태, COW 처리 같은 세부 상태를 어느 단위로 추적할지라는 문제를 만든다.

Wilcox는 이런 시스템에서 copy-on-write(COW) 폴트가 더 비싸질 것이라고 말했다. 64KB 페이지를 채우기 위해 주변 기본 페이지들도 fault-in해야 하기 때문이다. 반면 David Hildenbrand는 `userfaultfd()`를 어떻게 구현할 수 있을지 우려했다. 전체 페이지가 아니라 단일 PTE를 설치하는 새 작업이 필요할 수도 있다.[^c3b-x86-cow-uffd]

[^c3b-x86-cow-uffd]: COW는 fork 이후 실제 쓰기가 발생할 때 페이지를 복사해 메모리를 절약하는 핵심 최적화다. `userfaultfd()`는 사용자 공간이 페이지 폴트를 직접 처리하게 하는 인터페이스다. 둘 다 페이지 단위 의미론에 민감하므로, 64KB 관리 단위와 4KB PTE 단위가 엇갈리면 구현과 성능이 모두 어려워진다.

Hildenbrand는 또한 시스템 전체를 그냥 64KB 페이지 크기로 가는 편이 나을 수도 있다고 제안했다. 그렇게 하면 모두의 삶이 쉬워질 것이라고 그는 말했다. Shutsemau는 그렇게 해도 결국 복잡도를 아키텍처 코드로 옮기는 효과만 낼 뿐이라고 답했다. 아키텍처 코드는 더 큰 기본 페이지 크기라는 허구를 구현하고 그 세부사항을 커널 나머지 부분에서 숨겨야 하기 때문이다. 더 큰 기본 페이지 크기로 가면 일부 애플리케이션도 깨진다. Hildenbrand는 이 마지막 지점에는 동정적이지 않았고, 그런 애플리케이션은 고치거나 그냥 4KB 시스템에서 실행해야 한다고 말했다.

Jason Gunthorpe는 Arm 시스템에서 64KB 페이지 크기에 대한 많은 경험이 있다고 말했다. 그의 말에 따르면 사용자들은 항상 4KB 페이지에서만 실행될 수 있는 특수 애플리케이션 하나가 있기 때문에 반발하는 경향이 있다. 또 다른 참석자는 커널에 시간이 지날수록 더 좋아지고 있는 mTHP 지원이 있는데 왜 이런 복잡성이 필요한지 물었다. Shutsemau에 따르면 그 아이디어의 문제 중 하나는 모든 파일시스템이 더 큰 folio를 지원하지는 않는다는 점이다. 작은 기본 페이지 크기에 머무르는 것도 시스템이 더 큰 메모리 덩어리를 할당하기 어렵게 만든다.

메모리 낭비라는 주제에서 Hildenbrand는 페이지보다 작은 메모리 조각을 나타내는 "negative-order folios"를 만들 가능성을 제안했다. 페이지보다 작은 할당에 slab allocator를 쓰자는 아이디어도 제안되었지만, 모든 경우에 동작하지는 않을 것이다.[^c3b-x86-folios]

[^c3b-x86-folios]: folio는 커널이 하나 이상의 물리 페이지 묶음을 더 명확히 표현하기 위해 도입한 추상화다. 현재 order-zero folio가 단일 페이지라는 전제는 많은 코드의 기반이다. "negative-order"라는 표현은 그보다 작은 단위를 folio로 다루자는 뜻이라, 기존 추상화의 방향을 거스르는 큰 설계 변화가 된다.

세션 시간이 부족해지자 Shutsemau는 자신의 제안에 대한 열기가 많지 않다는 점을 인정했다. 그는 근본적인 반대 이유가 무엇인지 물었다. Hildenbrand는 현재 커널에서 order-zero folio는 단일 페이지이며, 그 이해를 바꾸면 folio 처리 방식에 중대한 변화가 뒤따를 것이라고 답했다. 그는 원하는 목표를 달성하기 위해 "이상한 페이지 일부(part-of-page) 인터페이스"가 필요 없는 더 깨끗한 방법을 요청했다.

Gunthorpe는 근본 제약은 4KB 페이지 크기를 요구하는 오래된 애플리케이션을 실행할 방법이 있어야 한다는 점이라고 말했다. 더 큰 기본 페이지 크기를 가진 시스템에서, 커널 교란을 최소화하면서 그 문제를 해결할 방법을 찾는 편이 나을 것이다. 세션은 Hildenbrand가 커널의 다른 작업들이 Shutsemau가 제안한 변경의 여러 동기를 이미 다루고 있다고 말하며 끝났다. 그렇다면 64KB 기본 페이지가 미래가 아닐 수도 있으며, 올바른 길은 4KB 페이지 시스템의 동작을 더 잘 최적화하는 것일 수 있다고 그는 제안했다.[^c3b-x86-conclusion]

[^c3b-x86-conclusion]: 이 논의는 커널 설계에서 흔한 절충을 보여준다. 특정 워크로드의 몇 퍼센트 성능 향상을 위해 전역 추상화를 흔들 것인지, 아니면 기존 4KB 기반을 유지하며 mTHP·folio·파일시스템 지원을 개선할 것인지의 문제다. 실무적으로는 호환성과 유지보수 비용이 성능 수치만큼 중요하다.

[댓글(11개 게시됨)](https://lwn.net/Articles/1071484/#Comments)

---

### [2026년 DAMON 업데이트](https://lwn.net/Articles/1071256/)

#### 요약

- DAMON은 메모리 접근을 낮은 오버헤드로 샘플링해 사용자 공간에 제공하고, DAMOS를 통해 회수·마이그레이션 같은 메모리 관리 동작까지 수행한다.
- TPP-DAMON과 `damos_migrate`는 CXL 메모리와 RAM 사이의 계층화(tiering), 동적 인터리빙(interleaving), 제어 그룹 인식 기능으로 확장되고 있다.
- 데이터 속성 모니터링(data attributes monitoring)은 페이지 유형, cgroup, 유휴성 등의 속성을 샘플링해 대규모 관측과 DAMOS 필터링에 활용하려 한다.
- DAMON-X는 여러 DAMON 모듈이 공통 모니터링 매개변수를 공유하면서 자동 조정되는 “그냥 동작하는 DAMON”을 지향한다.
- 접근 패턴을 이용해 투명 대형 페이지(THP)를 접거나 나누는 `damos_hugepage`는 유망하지만, 어떤 동작을 DAMON이 맡아야 하는지는 아직 논의 중이다.

글쓴이

Jonathan Corbet

2026년 5월 8일

LSFMM+BPF

커널의

DAMON

서브시스템은 사용자 공간에서 시스템 메모리를 모니터링하고 관리할 수 있게 해준다. DAMON은 빠르게 발전하고 있어서, 그 진행 상황 업데이트는 해마다 열리는

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 정례 항목이 되었다. 이 전통은 2026년 모임에서도 이어졌으며, DAMON 창시자인 박성재(SeongJae Park)는 이 서브시스템에 추가되고 있는 긴 기능 목록 — 계층화(tiering), 데이터 속성 모니터링(data attributes monitoring), 투명 대형 페이지(transparent huge pages) 등 — 을 다루는 업데이트를 발표했다.[^c3c-damon-scope]

[^c3c-damon-scope]: DAMON(Data Access MONitor)은 “어떤 메모리가 얼마나 자주 쓰이는가”를 커널 안에서 비교적 싸게 관측하려는 기반 기술이다. 메모리 회수, NUMA 배치, CXL 같은 느린 메모리 계층 활용은 모두 실제 접근 패턴을 알아야 더 잘 결정할 수 있기 때문에, DAMON은 단순한 관측 도구를 넘어 정책 엔진의 입력으로 중요해진다.

박은 DAMON이 메모리 관리를 위한 효율적인 모니터링과 동작을 제공하는 커널 서브시스템이라고 설명하며 발표를 시작했다. 핵심적으로 DAMON은 5ms마다 메모리 접근을 샘플링하는 커널 스레드를 생성한다. 그 결과는 취합되어 100ms마다 사용자 공간으로 반환되지만, 물론 이 간격은 수동으로든 자동으로든 조정할 수 있다. 반환되는 접근 정보는 메모리 동작의 위치, 안정성, 빈도를 설명한다. 이 시스템은 정확하면서도 가볍고, 조정 가능하면서도 자동 조정이 가능하도록 설계되었다. 일반적인 시스템에서 성능 오버헤드는 0.1% 미만이다. 이 서브시스템은 5.15 커널 릴리스에 처음 병합되었으며, 현시점에는 많은 배포판 커널에서 활성화되어 있다.[^c3c-sampling]

[^c3c-sampling]: 커널 메모리 관측에서 “정확도”와 “오버헤드”는 늘 맞교환 관계다. DAMON은 모든 접근을 추적하지 않고 샘플링과 영역 병합을 사용해 비용을 낮춘다. 실무적으로는 운영 중인 서버에서도 정책 실험을 할 수 있을 만큼 가벼운 관측을 제공하는 것이 핵심 가치다.

박은 “DAMON의 두 번째 얼굴”이 DAMOS 장치라고 말했다. DAMOS는 메모리가 관리되는 방식을 바꾸는 동작을 제공한다. 예를 들어 차가운(cold) 메모리를 강제로 밀어내거나, 사용 패턴에 따라 메모리를 계층 사이에서 마이그레이션할 수 있다. 더 많은 정보는 [DAMON 웹 사이트](https://damonitor.github.io/)에서 볼 수 있다.[^c3c-damos]

[^c3c-damos]: DAMOS(DAMON-based Operation Schemes)는 관측 결과를 실제 행동으로 연결한다. 예컨대 “잘 쓰이지 않는 영역은 회수하라”거나 “뜨거운 영역은 빠른 NUMA 노드로 옮겨라” 같은 규칙을 커널이 실행하게 한다. 이는 사용자 공간 모니터링 도구와 달리 결정과 실행의 지연을 줄일 수 있다.

#### 계층화

박은 [2025년 서밋](https://lwn.net/Articles/1016525/)에서 6.11 릴리스에 병합된 `damos_migrate` 동작을 설명한 바 있다고 말했다. 이 동작은 시스템 RAM과 [CXL](https://en.wikipedia.org/wiki/Compute_Express_Link)로 연결된 메모리 사이에서 페이지 이동을 쉽게 해준다. 달리 말하면 메모리 계층화(memory tiering)다. “TPP”가 “transparent page placement”를 뜻하는 TPP-DAMON 작업이 진행 중이었고, 높은 RAM 활용률을 얻기 위해 임계값을 자동 조정하는 기능이 포함되어 있었다. 계층화 작업은 계속되고 있지만, 단일 스레드는 이 작업에 너무 느린 것으로 드러났다. 그래서 TPP-DAMON은 다중 스레드 모델로 이동했다. 이는 [llama.cpp](https://llama-cpp.com/) 벤치마크에서 94% 향상을 만들어낼 수 있었다. TPP-DAMON은 6.16에 병합되었고, 6.19에서는 제어 그룹(control group) 인식 기능이 추가되었다. 다만 개발의 초점은 다른 곳으로 옮겨갔기 때문에, TPP-DAMON은 이미 지원 모드에 들어갔다.[^c3c-tiering]

[^c3c-tiering]: CXL 메모리는 서버에 더 많은 용량을 비교적 유연하게 붙일 수 있게 하지만, 지연시간과 대역폭 특성이 DRAM과 다를 수 있다. 따라서 자주 접근되는 페이지는 빠른 RAM에, 덜 중요한 페이지는 CXL 계층에 두는 정책이 성능과 비용을 좌우한다. DAMON 기반 계층화는 이 배치를 접근 패턴에 맞춰 자동화하려는 시도다.

[![[SeongJae Park]](https://static.lwn.net/images/conf/2026/lsfmm/SeongJaePark-sm.png)](https://lwn.net/Articles/1071423/) `damos_migrate` 동작은 동적 인터리빙(dynamic interleaving)을 지원하도록 확장되었다. 이는 전체 메모리 대역폭 활용을 극대화하기 위해 일부 뜨거운(hot) 메모리를 더 느린 CXL 메모리에 배치하는 방식이다. 각자 가중치를 가진 여러 목적지 노드를 지원할 수 있지만, 가상 주소 공간에서만 동작한다. 이 기능은 이름이 공개되지 않은 한 벤치마크에서 25% 속도 향상을 낼 수 있었으며, 6.17에 병합되었다.[^c3c-interleaving]

[^c3c-interleaving]: “뜨거운 메모리는 항상 가장 빠른 곳에 둔다”가 최적은 아닐 수 있다. 빠른 RAM의 대역폭이 병목이면 일부 뜨거운 페이지를 CXL 쪽으로 분산해 전체 병렬성을 높일 수 있다. 동적 인터리빙은 지연시간뿐 아니라 대역폭 균형까지 고려하는 정책이라는 점에서 중요하다.

인터리빙 자동 조정은 아직 진행 중인 작업이며, 물리 주소 공간에서 동작한다. 이는 특정 수준의 메모리 압력이 유지되도록 하거나, 뜨거운 페이지의 특정 비율이 CXL 메모리에 배치되도록 하는 목표로 페이지 마이그레이션을 요청할 수 있다. 이 기능은 7.1-rc1 릴리스에 병합되었다.

한편 TPP-DAMON으로 향하던 노력은 이제 NUMA-TPP-DAMON에 집중되고 있다. 결국 계층화는 NUMA 배치의 특수한 경우일 뿐이라는 관찰에 기반한 것이다. 새 모델에서 시스템에는 메모리에 접근하는 주체(CPU, GPU 또는 메모리에 접근하는 다른 장치)들의 집합과, 메모리에 사용할 수 있는 승격 경로(promotion paths)들의 집합이 있다. 박은 개념은 마련되어 있지만 이 작업은 아직 브레인스토밍 단계라고 말했다.[^c3c-numa-tpp]

[^c3c-numa-tpp]: NUMA(Non-Uniform Memory Access)는 접근 주체와 메모리 위치에 따라 비용이 달라지는 구조다. CXL 계층화도 “어느 접근자가 어느 메모리에 더 싸게 접근하는가”의 문제로 보면 NUMA 배치와 닮았다. NUMA-TPP-DAMON은 CPU뿐 아니라 GPU·가속기까지 포함한 더 일반적인 메모리 배치 모델로 확장될 수 있다.

Davidlohr Bueso는 NUMA-TPP-DAMON을 사용하려면 NUMA 밸런싱을 비활성화해야 하는지 물었다. 박은 그렇지 않다고 답했다. Bueso는 서로 다른 계층이 메모리 배치 결정을 두고 싸우는 상황을 우려했지만, 박은 신중하게 목표를 설정하면 피할 수 있다고 보았다.

#### 데이터 속성 모니터링

그는 지난해 개발자들이 페이지 수준 속성 모니터링(page-level attribute monitoring) 작업을 시작했다고 말했다. 이는 예를 들어 특정 영역의 몇 바이트가 대형 페이지로 뒷받침되는지, 또는 특정 제어 그룹에 과금되는지를 묻는 질문에 답하도록 설계되었다. 이 모니터링은 구현되었지만 오버헤드는 높다. 이 기능은 개선되어 6.15에 여러 중요한 수정이 들어갔지만, 오버헤드 문제는 여전히 남아 있다.[^c3c-attr-overhead]

[^c3c-attr-overhead]: 페이지별 속성 조회는 정확하지만, 대규모 메모리를 가진 서버에서는 페이지 수가 매우 많아 비용이 커진다. 운영 환경에서 fleet-wide 모니터링을 하려면 모든 페이지를 자주 훑는 방식보다 샘플링과 필터링이 필요하다.

새로운 데이터 속성 모니터링 프로젝트도 시작되고 있으며, fleet-wide 모니터링 같은 사용 사례를 지원하는 것이 목표다. 이 프로젝트는 사용자가 관심 있는 페이지 집합을 좁히는 프로브(probe)를 등록할 수 있는 샘플링 기반 페이지 수준 모니터를 구현한다. 각 프로브는 유형(익명 또는 파일 기반), 제어 그룹 소속, 유휴성 등과 같은 속성을 기준으로 페이지를 필터링한다. 이 프로브들은 DAMOS 필터로 동작할 수 있다.

이 시스템은 기존 접근 샘플링 로직을 사용하므로 가볍고 확장 가능하다는 것이 드러났다. 다만 정확도는 여러 워크로드 관련 요인에 따라 “논쟁의 여지가 있다”고 그는 말했다. 관련 오버헤드를 감수할 수 있다면 페이지 수준 모니터링을 사용해 더 정확한 정보를 얻을 수 있다고 했다.

그는 [데이터 속성 모니터링 패치 세트의 첫 번째 버전](https://lwn.net/ml/all/20260426205222.93895-1-sj@kernel.org/)이 메일링 리스트에 올라와 있으며, 곧 준비 완료로 선언될 수도 있다고 말했다. 현재 주된 기능은 익명 상태(anonymous status) 모니터링이지만, 향후 계획은 다소 더 야심적이다. 의도는 데이터 접근 자체를 모니터링 가능한 또 하나의 속성으로 바꾸고, 그 속성에 작용할 수 있는 `pg_idle` DAMON 필터를 추가하는 것이다. DAMON은 속성 기반 영역 분할과 병합을 지원하게 된다. 페이지 폴트(page fault)나 시스템의 성능 모니터링 장치(PMU)에서 오는 데이터에 대한 필터와 함께, 더 풍부한 접근 확인 프리미티브(access-check primitives) 집합도 생길 것이다. 이 기능은 결국 NUMA-TPP-DAMON 작업의 기반이 될 수도 있다.[^c3c-pg-idle]

[^c3c-pg-idle]: `pg_idle`은 페이지가 최근 사용되었는지 추적하는 커널 메커니즘과 관련된다. 이를 DAMON 필터로 노출하면 “최근 접근이 적고 특정 cgroup에 속한 익명 페이지”처럼 복합 조건을 커널 정책에 바로 사용할 수 있다. 이는 메모리 회수, 배치, 진단 도구의 표현력을 높인다.

다른 출처의 데이터를 모니터링하는 것도 활발히 검토 중인 영역이다. 박은 데이터 접근을 출처 NUMA 노드, 제어 그룹, 스레드 등 여러 방식으로 분류할 수 있기를 원한다. 이 데이터는 캐시 인식(cache-aware) sched_ext CPU 스케줄러 작성에 도움이 될 것이다. NUMA-TPP-DAMON에도 유용할 수 있다. 예를 들어 쓰기를 가장 적게 하는 가상 머신을 찾아낼 수 있는데, 그런 VM은 보통 라이브 마이그레이션(live migration)이 가장 쉬운 대상이다.[^c3c-sched-ext]

[^c3c-sched-ext]: sched_ext는 BPF로 CPU 스케줄링 정책을 실험·구현할 수 있게 하는 커널 기능이다. 어떤 스레드가 어떤 메모리를 자주 만지는지 알면 캐시 지역성이나 NUMA 지역성을 고려해 더 좋은 CPU 배치를 할 수 있다.

현재 DAMON은 접근 확인에 page-idle 비트를 사용하고 있다. 그 결과 데이터에는 누가 메모리에 접근했는지, 어떤 종류의 접근이 이루어졌는지에 대한 정보가 없다. 더 나은 데이터를 얻기 위해 그는 페이지 폴트 핸들러와 PMU를 포함한 다른 출처의 이벤트를 끌어오고 싶어 한다. 예를 들어 NUMA 서브시스템은 현재 어떤 노드가 페이지에 접근하는지에 대한 데이터를 수집한다. 그 데이터를 DAMON에 공급하는 “프로토타입 해킹”이 존재한다. 하지만 그렇게 데이터를 사용하면 원래의 NUMA 밸런싱 의도와 간섭하며, 이는 원하는 결과가 아니다.[^c3c-page-idle]

[^c3c-page-idle]: page-idle 비트 기반 접근 확인은 “접근이 있었는가”를 알기에는 유용하지만, 접근 주체와 접근 유형을 알려주지 않는다. NUMA 밸런싱도 비슷한 힌트 정보를 사용하므로, 두 기능이 같은 표시를 건드리면 서로의 관측을 오염시킬 수 있다.

따라서 박은 중요한 다음 단계가 NUMA 힌팅(hinting) 코드 정리라고 말했다. 어떤 확장이 시도되기 전에 그 작업이 이루어져야 한다. 그러나 DAMON과 NUMA 힌팅 사이의 간섭 우려는 여전히 남을 것이다. 둘 다 page-idle 비트를 사용하므로, 각각은 상대가 일으킨 폴트를 “측정”하게 된다. 이 문제를 다루는 한 가지 방법은 NUMA 힌팅과 DAMON을 상호 배타적으로 만들어 둘 중 하나만 커널에 빌드될 수 있게 하는 것이다. 이는 단순하지만 유연하지 못한 접근이며, 배포판 담당자들이 어느 기능을 활성화할지 결정해야 하는 어려운 위치에 놓이게 된다.

대안은 런타임 격리(run-time isolation)로, 어느 시점이든 두 기능 중 하나만 활성화될 수 있게 하는 것이다. 이는 깔끔하고 유연한 해결책이지만 구현하기는 비교적 어렵다. 부분 격리(partial isolation)는 또 다른 접근으로, 한 서브시스템에서 다른 서브시스템으로 전환되는 동안 페이지 표시를 그대로 남겨두는 방식이다. 그러면 데이터가 다소 흐려지는 대가로 전환은 더 빨라진다. 또는 박은 두 서브시스템이 그냥 서로 간섭하도록 둘 수도 있다고 말했다. 그것이 실제 문제로 이어질지는 아직 분명하지 않다. DAMON은 그런 간섭을 처리할 수 있어야 한다. 두 서브시스템을 동시에 사용하는 경우는 드물 것이므로, 어쩌면 전체 문제를 그냥 무시할 수도 있다. Kiryl Shutsemau는 NUMA 밸런싱이 샘플링을 사용하므로 일부 정보를 잃는 것이 반드시 큰 문제는 아니라고 지적했다.[^c3c-isolation]

[^c3c-isolation]: 커널 기능 간 “관측 간섭”은 성능 정책에서 흔한 문제다. 배포판 입장에서는 빌드타임 상호 배제가 가장 단순하지만 선택지를 줄이고, 런타임 격리는 사용자에게 유연하지만 코드 복잡도를 높인다. 실제 동시 사용 빈도와 오차 허용 범위가 설계 결정을 좌우한다.

박의 제안은 필요한 정리 작업이 끝난 뒤 첫 구현에서는 빌드타임 격리를 사용하거나, 아니면 문제를 아예 무시하는 것이었다.

유용한 데이터의 또 다른 출처는 perf events 서브시스템을 통한 PMU일 수 있다. PMU를 DAMON에 통합하는 RFC 구현들이 돌아다니고 있으며, perf 유지보수자들은 그 아이디어에 문제가 없어 보인다. 하지만 PMU에서 나오는 데이터는 하드웨어별로 다르고, 가상 머신 안에서는 유용한 데이터를 얻기가 더 어렵다. 따라서 일반적인 경우 이 데이터의 유용성이 완전히 분명하지는 않다.[^c3c-pmu]

[^c3c-pmu]: PMU(Performance Monitoring Unit)는 캐시 미스, TLB 미스, 메모리 접근 같은 하드웨어 이벤트를 셀 수 있다. DAMON이 PMU를 활용하면 더 풍부한 접근 정보를 얻을 수 있지만, CPU 모델별 차이와 가상화 환경의 제약 때문에 이식성과 일관성이 문제가 된다.

#### DAMON-X

박은 “DAMON-X”, 다른 말로 “그냥 동작하는 DAMON(DAMON that just works)”이라고 부른 개념을 간단히 논의했다. DAMON은 원하는 사용자에게 수동 조정 노브(knobs)를 제공하고, 나머지 모두에게는 자동 조정을 제공하지만, 각 DAMON 모듈은 다른 모듈과 배타적으로 실행된다. 박은 모든 모듈이 동일한 기본 모니터링 매개변수를 공유하고, 제공하는 DAMOS scheme만 달라지는 해결책을 작업 중이다. 하나의 컨텍스트가 여러 scheme을 실행할 수 있고, 사용자는 원하는 대로 이를 설치하거나 제거할 수 있다. 가능한 범위에서 이 모든 것은 스스로 자동 조정되며 단순히 동작하게 될 것이다. 개념 증명 구현은 올해 말쯤 나올 것으로 예상된다.[^c3c-damon-x]

[^c3c-damon-x]: DAMON 기능이 늘어날수록 각 기능이 별도 모니터링을 수행하면 중복 비용과 설정 복잡도가 커진다. DAMON-X는 공통 관측을 한 번 수행하고 여러 정책이 공유하게 만들어, 운영자가 세부 튜닝을 몰라도 기능을 안전하게 조합할 수 있게 하려는 방향이다.

#### 접근 인식 투명 대형 페이지

투명 대형 페이지(THP)는 프로그램을 더 빠르게 실행하게 만들 수 있다는 점에서 좋다. 하지만 내부 단편화와 메모리 낭비를 일으킬 수도 있다. 사용자는 [`madvise()`](https://man7.org/linux/man-pages/man2/madvise.2.html)를 통해 THP 사용을 어느 정도 제어할 수 있지만, 올바른 조언을 제공하기는 어렵다. 어쩌면 DAMON이 도움이 될 수 있다. `damos_hugepage` 모듈은 접근 패턴을 추적하고, 메모리가 어떻게 사용되는지에 따라 기본 페이지(base pages)를 대형 페이지로 접거나(collapse), 대형 페이지를 다시 나눈다(split). 한 벤치마크에서는 THP로 인한 메모리 팽창(bloat)의 80%를 제거하면서도 성능 향상의 46%를 보존할 수 있었다. 다만 이 작업은 초기 단계 프로토타입이고, 벤치마크 결과도 안정적이지 않다.[^c3c-thp]

[^c3c-thp]: THP는 여러 4KB 페이지를 2MB 같은 큰 단위로 묶어 TLB 부담을 줄인다. 그러나 실제로 일부만 사용되는 큰 페이지는 메모리를 낭비할 수 있다. DAMON이 접근 밀도를 보고 큰 페이지를 만들거나 해체하면 성능과 메모리 효율 사이의 균형을 자동화할 가능성이 있다.

박은 이 작업을 더 단단히 만들고 싶어 했으며, `damos_hugepage` 모듈이 대형 페이지의 조립과 분할을 모두 해야 하는지, 아니면 둘 중 하나만 해야 하는지를 궁금해했다. Huawei의 개발자들은 시스템에서 CPU 집약적인 프로세스 세 개를 찾는 방식으로 동작하는 collapse-only 접근법을 내놓았다. 그런 다음 이 프로세스들의 뜨거운 메모리 영역을 대형 페이지로 접는다. 정해진 시간이 지나면 새로운 세 개의 집합을 고르고, 과정이 다시 시작된다. 이 작업은 MySQL 기반 워크로드에서 좋은 결과를 냈다.

하지만 일반적으로 DAMON이 기본 페이지를 대형 페이지로 접어야 하는지, 대형 페이지를 다시 나누어야 하는지, 또는 둘 다 해야 하는지는 열린 질문이다. `thp=always` 모드로 실행 중인 시스템은 DAMON이 대형 페이지를 만들 필요가 없을 수 있다. 필요할 때 대형 페이지를 나눌 수 있는 THP shrinker가 이미 존재하므로, DAMON이 그 작업도 할 필요가 없을 수 있다. 현재로서는 최선의 동작 집합이 명확하지 않다.[^c3c-thp-policy]

[^c3c-thp-policy]: 이미 커널에는 THP 생성·회수 경로가 존재한다. DAMON이 같은 일을 반복하면 복잡도만 늘 수 있지만, 접근 패턴 기반 판단을 추가하면 기존 정책의 빈틈을 메울 수도 있다. 핵심은 “DAMON이 새 동작을 직접 수행할지, 기존 THP 메커니즘에 힌트를 줄지”다.

THP 프리미티브가 가상 주소 공간에서 동작해야 하는지, 물리 주소 공간에서 동작해야 하는지에 대한 질문도 있다. 어떤 프로세스의 페이지를 접는 일은 필연적으로 그 프로세스의 가상 주소 공간 안에서 작업하는 것을 포함한다. 물론 어떤 프로세스에 대해 작업할지 선택하는 문제도 있다. 어쩌면 그 선택은 사용자에게 맡길 수 있을 것이다. 가상 주소 공간에서 작업하면 DAMON-X와 간섭할 가능성이 생긴다. 반면 분할 동작은 물리 주소 접근만 필요하므로, 그런 간섭 우려가 없다.[^c3c-vaddr-paddr]

[^c3c-vaddr-paddr]: 페이지를 “접는” 작업은 인접한 가상 주소 범위와 그 매핑 상태를 확인해야 하므로 프로세스별 문맥이 중요하다. 반대로 이미 존재하는 대형 페이지를 나누는 일은 물리 페이지 단위에서 처리할 수 있다. 어느 주소 공간을 기준으로 삼는지는 잠금, 경쟁, 다른 DAMON scheme과의 상호작용에 직접 영향을 준다.

박이 제기한 마지막 질문은 접기에는 뜨거움(hotness), 나누기에는 차가움(coldness)의 정도에 대한 임계값 설정과 관련이 있었다. 이것들은 어쩌면 자동 조정될 수 있지만, 제대로 하려면 목표가 무엇인지에 달려 있다. 가능한 목표로는 대형 페이지와 기본 페이지의 특정 비율, 또는 특정 TLB 미스율이 있을 수 있지만, 후자는 하드웨어별로 다르다. 다른 가능한 목표는 메모리 팽창이나 압력의 관점에서 표현될 수 있다.

시간이 다 되어갈 때 David Hildenbrand는 DAMON이 대형 페이지를 나누는 것은 결코 좋은 생각이 아닐 수 있다고 제안했다. 시스템이 대형 페이지를 만들어냈다면, 가능하면 그대로 유지하는 것이 타당하다. 그 페이지가 완전히 활용되지 않는다면 더 나은 해결책은 아마 그 내용을 다른 곳의 기본 페이지로 마이그레이션하는 것일 수 있다. 그는 또한 대형 페이지의 뜨거움을 어떻게 측정할 수 있는지도 궁금해했다. 접근 비트가 하나뿐이므로, 주어진 대형 페이지 중 얼마나 많은 부분이 접근되고 있는지에 대한 즉각적인 표시는 없기 때문이다.[^c3c-hugepage-hotness]

[^c3c-hugepage-hotness]: 대형 페이지에는 하위 4KB 페이지 각각의 접근 밀도를 바로 보여주는 단일한 저비용 신호가 부족하다. 큰 페이지 전체에 접근 비트 하나만 있으면 일부만 뜨거운지 전체가 뜨거운지 구분하기 어렵다. 이 문제는 THP 자동 정책이 잘못된 결정을 내릴 수 있는 중요한 한계다.

[댓글(2개 게시됨)](https://lwn.net/Articles/1071256/#Comments)

### [직접 매핑 밖의 페이지 관리](https://lwn.net/Articles/1072367/)

#### 요약

- 커널 직접 매핑(direct map)에서 민감한 메모리를 제거하면 보안상 이점이 있지만, 커널이 필요할 때 해당 메모리에 접근하는 방법이 필요하다.
- Brendan Jackman은 직접 매핑에 없는 메모리를 요청하기 위한 `__GFP_UNMAPPED` 플래그와 이를 효율화하는 allocator 변경을 제안했다.
- “mermap”은 CPU 로컬의 일시적 커널 매핑을 제공해 unmapped 페이지를 짧게 접근하게 하지만, TLB 플러시와 API 안전성이 난제다.
- 기존 migration type을 더 풍부한 “freetype”으로 바꾸어 메모리 블록의 직접 매핑 여부 같은 속성을 추적하려는 제안이 포함된다.
- 세션에서는 GFP 플래그가 적절한 API인지, TLB 플러시 의무를 어떻게 추적할지, 리뷰 가능한 작은 패치 단위로 어떻게 나눌지가 논의되었다.

글쓴이

Jonathan Corbet

2026년 5월 13일

LSFMM+BPF

Brendan Jackman이

2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

세션을

제안했을 때,

그의 주제는 “

커널을 위한 페이지테이블 라이브러리

”였다. 하지만 실제 메모리 관리 트랙 세션에서 그는 그 아이디어가 “

힘이 빠졌다(fizzled)

”고 말했고, 대신 관련 주제들을 다루겠다고 했다. 그 결과 나온 것은 커널의 직접 매핑(direct map)에 존재하지 않는 페이지를 효율적으로 관리하는 방법에 대한 세션이었다.[^c3c-direct-map-topic]

[^c3c-direct-map-topic]: 이 논의의 배경은 “커널이 모든 물리 메모리를 항상 쉽게 볼 수 있어야 하는가”라는 질문이다. 직접 매핑을 줄이면 보안은 좋아질 수 있지만, 커널 내부의 수많은 코드 경로가 메모리에 접근하는 방식에 영향을 주므로 메모리 관리 전반의 설계 문제가 된다.

직접 매핑은 시스템의 전체 물리 주소 공간을 커널의 가상 주소 공간 안에서 사용할 수 있게 한다(어쨌든 64비트 시스템에서는 그렇다). 이를 통해 커널은 먼저 어떤 매핑도 설정하지 않고 시스템의 임의 메모리 위치에 접근할 수 있다. 직접 매핑은 빠르고 편리하지만, 버그, 추측 실행 취약점, 또는 어떤 형태의 침해 결과로 커널이 원치 않는 방식으로 메모리에 접근하기 쉽게 만들기도 한다. 따라서 민감한 데이터를 담은 메모리를 직접 매핑에서 제거하면 상당한 보안 이점을 얻을 수 있다.[^c3c-direct-map-security]

[^c3c-direct-map-security]: direct map은 리눅스 커널 성능의 핵심 편의 기능이지만, 공격자가 커널 실행을 일부 제어하거나 추측 실행을 악용할 때 접근 가능한 표면을 넓힌다. 암호키, 게스트 메모리, 격리된 주소 공간 데이터를 direct map에서 빼면 “우연히” 또는 “투기적으로” 읽히는 위험을 줄일 수 있다.

[![[Brendan Jackman]](https://static.lwn.net/images/conf/2026/lsfmm/BrendanJackman-sm.png)](https://lwn.net/Articles/1072376/) Jackman은 자신이 [주소 공간 격리(address-space isolation)](https://lwn.net/Articles/974390/) 작업을 해왔으며, 여기에는 많은 직접 매핑 제거가 수반된다고 말하며 시작했다. 진척은 느렸지만, 그가 받은 피드백은 긍정적이었다. 그는 현재 여러 기술적 세부 사항에서 막혀 있지만, 자신도 위압적으로 크다고 인정한 패치 세트에 대한 리뷰 부족에도 발목이 잡혀 있다. 그래서 그는 문제를 더 쉽게 리뷰할 수 있는 작은 조각들로 나누려 하고 있다.

그 조각 중 하나는 매핑되지 않은(unmapped, 즉 직접 매핑에 없는) 메모리를 할당할 수 있게 하는 것이다. 그는 [Firecracker](https://firecracker-microvm.github.io/) 가상화 관리자 개발자들이 호스트의 직접 매핑에서 게스트 메모리를 unmap하는 여러 방법을 시도해 왔지만, 성능이 좋지 않았다고 말했다. 그는 직접 매핑에 존재하지 않는 메모리를 요청하기 위해 새 할당 플래그 `__GFP_UNMAPPED`를 제공하는 메모리 할당자 변경 세트를 [제안한](https://lwn.net/Articles/1064090/#mermap) 바 있다. 그 플래그를 구현하려면 이 할당이 현재 커널에서보다 더 효율적으로 이루어지도록 새로운 기반 구조를 추가해야 한다. 변경은 상당하며 논쟁적일 수도 있다. 그는 개발자들이 리뷰하지 않으면 David Hildenbrand가 그 변경을 병합할 것이라고 (미소를 지으며) 그룹에 경고했다.[^c3c-gfp-unmapped]

[^c3c-gfp-unmapped]: GFP 플래그는 커널 메모리 할당자가 “어떤 조건의 메모리”를 줄지 결정하는 힌트다. `__GFP_UNMAPPED`는 성능을 위해 기본적으로 direct map에 들어가는 관행을 깨고, 특정 데이터가 처음부터 커널 전역 직접 매핑에 노출되지 않게 하려는 요청이다. 가상 머신 게스트 메모리 보호 같은 사용 사례에 직접 연결된다.

구체적으로 이 시리즈는 기존의 “migration type” 개념을 바꾼다. 현재 이 개념은 이동 가능한 할당과 이동 불가능한 할당을 분리하는 데 쓰인다. migration type은 “freetype”으로 대체될 것이다. freetype은 메모리 블록에 대한 추가 속성 — 그 블록이 현재 직접 매핑에 존재하는지 여부 포함 — 을 담는다. 이를 통해 메모리 블록을 직접 매핑에서 대량으로 제거해 `__GFP_UNMAPPED` 할당 요청을 빠르게 만족시키는 데 사용할 수 있다. middle-ad[^c3c-freetype]

[^c3c-freetype]: 페이지 할당자는 비슷한 성격의 페이지들을 묶어 관리해야 단편화를 줄이고 빠르게 할당할 수 있다. direct map 여부까지 속성으로 추적하면 unmapped 페이지 풀을 미리 준비할 수 있지만, 기존 migration type의 단순한 모델보다 allocator 복잡도가 증가한다.

하지만 직접 매핑에서 메모리를 제거할 때의 문제는 커널이 더 이상 그 메모리에 접근할 수 없다는 점이다(결국 제거의 목적이 바로 그것이지만). 그런데 때로는 커널이 정확히 그 일을 해야 한다. 할당 시 페이지를 0으로 채우기, [`read()`](https://man7.org/linux/man-pages/man2/read.2.html) 같은 시스템 호출 구현, copy-on-write 폴트 처리, [guest_memfd](https://lwn.net/Articles/949277/) 메모리 채우기는 모두 커널이 메모리에 합법적으로 접근해야 하는 시점의 예다. 이 문제에 대한 Jackman의 답은 그가 “mermap”이라고 부르는 커널 내부 구조다. 이는 어떤 작업을 수행할 수 있도록 페이지를 커널 주소 공간에 잠깐 매핑하게 해준다.[^c3c-mermap-need]

[^c3c-mermap-need]: unmapped 메모리는 “평소에는 보이지 않게” 하는 것이 목적이지만, I/O 복사, 초기화, COW 처리처럼 커널이 데이터를 만져야 하는 순간은 피할 수 없다. mermap은 보안 노출 시간을 짧게 제한하면서 필요한 작업만 수행하는 임시 창(window)을 제공하려는 설계다.

mermap 매핑은 CPU 로컬이다. 매핑을 요청한 CPU만 이를 사용할 수 있다. 이는 [`kmap_local_page()`](https://docs.kernel.org/mm/highmem.html#c.kmap_local_page)와 많이 비슷하지만, 그 함수는 여전히 모든 CPU에 보이는 매핑을 만들고 mermap은 그렇지 않다. 또 다른 차이는 mermap이 한 번에 여러 페이지를 매핑할 수 있다는 점이다. 또한 결정적으로, mermap은 실패할 수 있다.[^c3c-cpu-local]

[^c3c-cpu-local]: CPU 로컬 매핑은 다른 CPU가 같은 임시 주소를 이용해 접근할 가능성을 줄여 격리를 강화한다. 하지만 실패 가능성이 있는 API가 되면 기존 커널 코드처럼 “매핑은 항상 성공한다”고 가정하던 경로를 고쳐야 하므로 적용 범위가 까다로워진다.

`__GFP_UNMAPPED` 사용과 관련된 다른 위험도 있다. 성능을 개선하기 위해 mermap은 일시적 매핑이 제거된 뒤 TLB 플러시를 수행하지 않는다. 그러면 오래된(stale) TLB 엔트리가 남을 수 있다. 이 엔트리들은 생각해보면 메모리가 unmap된 뒤에도 그 메모리에 접근하는 데 쓰일 수 있다. 다만 주소가 다시 매핑되기 전에는 반드시 플러시될 것이므로, 잘못된 메모리 내용을 얻을 위험은 없다. 그는 할당자 사용자가 페이지를 해제하기 전에 TLB 플러시를 수행하도록 요구하는 방안을 고려 중이다. 그렇지 않으면 오래된 TLB 엔트리가 남아 있는 동안 그 페이지들이 다른 곳에서 재사용될 수 있다. 전반적으로 그는 이것이 최선의 API는 아니라고 생각하며, 개선 방법에 대한 제안에 관심이 있다.[^c3c-tlb]

[^c3c-tlb]: TLB는 가상주소-물리주소 변환을 캐시한다. 매핑을 지웠더라도 TLB에 변환이 남아 있으면 CPU가 잠시 옛 매핑으로 접근할 수 있다. 보안 격리에서는 이 짧은 잔여 상태도 중요하므로, 언제 플러시해야 하는지를 API가 명확히 강제해야 한다.

Liam Howlett은 일시적으로 매핑된 페이지를 대응되는 TLB 플러시 없이 해제하는 코드를 탐지하는 방법으로, 원래 잠금 버그 탐지를 담당하는 lockdep 검사기에 mermap을 연결하자고 제안했다. Matthew Wilcox는 페이지가 해제될 때 TLB 플러시가 일어나도록 컴파일 타임에 보장하기 위해 [스코프 기반 자원 관리 프리미티브(scoped resource-management primitives)](https://lwn.net/Articles/934679/)를 사용할 수 있는지 궁금해했다. 그 접근의 문제는 페이지가 서로 다른 스코프에서 할당되고 해제되므로, 이 문제가 그 모델에 맞지 않는다는 점이다. David Hildenbrand는 “해제 시 TLB 플러시 필요” 상태를 페이지 자체와 함께 추적하면 도움이 되는지 물었다. Jackman은 도움이 될 것이라고 답했지만, 그러려면 페이지 플래그가 필요하고 그것들은 늘 부족하다.[^c3c-lockdep-pageflag]

[^c3c-lockdep-pageflag]: lockdep은 원래 데드락과 잠금 순서 문제를 찾는 동적 검증 도구지만, 커널에서는 이런 “올바른 사용 규칙”을 검증하는 데도 응용된다. 반면 page flag는 `struct page` 안의 매우 제한된 비트 자원이라 새 의미를 추가하는 데 커널 개발자들이 신중하다.

Jackman이 그룹에 던진 마지막 질문은 GFP 플래그 사용이 적절한지였다. 전반적으로 메모리 할당을 GFP 플래그에서 멀어지게 하려는 흐름이 있으므로, 또 하나를 추가하는 것은 환영받지 못할 수 있다. 이 경우 실제로 필요한 것은 “unmapped” 비트를 페이지 할당자에 전달하는 방법뿐이다. Hildenbrand는 새 할당 컨텍스트(allocation context)를 추가하자고 제안했지만, Jackman은 unmapped 메모리의 필요성이 커널이 그 순간 실행 중인 컨텍스트의 속성이 아니라 그 안에 저장될 데이터의 속성이라고 말했다.[^c3c-api-shape]

[^c3c-api-shape]: API가 GFP 플래그인지, 별도 컨텍스트인지, 데이터 객체의 속성인지는 장기 유지보수에 큰 차이를 만든다. 저장될 데이터가 “민감하므로 direct map에 있으면 안 된다”는 성질을 가진다면, 실행 문맥 중심 API보다 데이터 중심 API가 실수를 줄일 수 있다.

그 시점에서 시간이 다 되어 세션은 끝났다. Jackman은 세션에 대한 [자신의 요약](https://lwn.net/ml/all/DIFTSG6BV7GO.1FZQ3YQF27KTG@google.com)과 [자신의 슬라이드](https://docs.google.com/presentation/d/1zcqEqRrpPR_K8LwcNIH8XpL7mk7mMcI_N1jJ67OWpYA/edit?slide=id.p#slide=id.p)를 가리키는 포인터를 게시했다.

[댓글(게시 없음)](https://lwn.net/Articles/1072367/#Comments)

**페이지 편집자**: Joe Brockmeier

---

# 단신

## 보안

### [Dirty Frag: 제로데이 범용 Linux LPE](https://lwn.net/Articles/1071719/)

#### 요약

- 현우 김(Hyunwoo Kim)이 최근 공개된 Copy Fail과 유사한 로컬 권한 상승(LPE) 취약점인 Dirty Frag를 공개했다.
- 엠바고가 깨져 당시에는 패치나 CVE가 준비되지 않은 상태였다.
- 주요 배포판에서 즉시 root 권한 상승이 가능하다고 보고되었다.
- 김은 익스플로잇 코드와 취약 모듈 제거 예시 스크립트, 전체 공개 타임라인을 포함한 설명 문서를 공개했다.
- 제3자가 엠바고 종료 전 취약점을 공개한 경위는 아직 알려지지 않았다.

현우 김은 최근 공개된 [Copy Fail](https://copy.fail/) 결함과 유사한 로컬 권한 상승(local-privilege-escalation, LPE) 취약점인 [Dirty Frag](https://github.com/V4bel/dirtyfrag#dirty-frag-universal-linux-lpe) 보안 결함을 [발표했다](https://lwn.net/ml/all/afzgS2SCWNcZU3vU%40v4bel/).[^c4-dirtyfrag-lpe]

> 이제 엠바고가 깨졌기 때문에, 이 취약점들에 대한 패치나 CVE는 존재하지 않습니다. linux-distros@vs.openwall.org 유지관리자들과 상의한 뒤, 그리고 유지관리자들의 요청에 따라, 저는 이 Dirty Frag 문서를 공개합니다.
>
> 앞선 Copy Fail 취약점과 마찬가지로, Dirty Frag 역시 모든 주요 배포판에서 즉각적인 root 권한 상승을 허용합니다.

이 결함을 발견하고 5월 12일로 조율된 공개(coordinated disclosure)를 시도했던 김은 익스플로잇 코드와 취약한 모듈을 제거하는 예시 스크립트도 공개했다. 공개 타임라인이 포함된 [전체 설명 문서](https://github.com/V4bel/dirtyfrag/blob/master/assets/write-up.md)도 볼 수 있다. 이것이 병렬 발견(parallel discovery)의 사례인지, 또는 제3자가 어떻게 엠바고 종료 전에 공개할 수 있었는지는 현재 알려지지 않았다. 더 많은 정보가 드러나는 대로 후속 보도가 이어질 예정이다.[^c4-dirtyfrag-disclosure]

[^c4-dirtyfrag-lpe]: LPE는 일반 사용자가 커널 또는 권한 있는 구성요소의 결함을 이용해 root 권한을 얻는 유형의 취약점이다. “범용” LPE는 배포판별 설정 차이를 크게 타지 않을 수 있어, 서버·데스크톱·컨테이너 호스트 모두에서 긴급 완화가 필요해질 수 있다.
[^c4-dirtyfrag-disclosure]: 보안 엠바고는 배포판과 업스트림이 패치를 준비할 시간을 주기 위한 관행이다. 엠바고가 깨지면 공격 코드가 패치보다 먼저 퍼질 수 있으므로, 관리자는 임시 완화책(취약 모듈 비활성화, 기능 차단, 접근 통제 강화)을 즉시 검토해야 한다.

[댓글 (36개 게시)](https://lwn.net/Articles/1071719/#Comments)

### [또 다른 Dirty Frag 유형 취약점: Fragnesia](https://lwn.net/Articles/1072647/)

#### 요약

- Sam James가 Dirty Frag와 같은 계열의 또 다른 LPE 익스플로잇인 “Fragnesia”를 OSS Security 목록에 알렸다.
- Fragnesia는 ESP/XFRM 영역의 별도 버그이며, Dirty Frag와 같은 공격 표면과 완화책을 공유한다.
- Linux XFRM ESP-in-TCP 하위 시스템의 논리 버그를 악용해 읽기 전용 파일의 커널 페이지 캐시에 임의 바이트 쓰기를 수행한다.
- 패치는 준비 중이지만 아직 Linus Torvalds의 트리나 stable 커널에는 병합되지 않았다.
- 개념 증명(PoC) 익스플로잇도 공개되어 있다.

Sam James는 [Dirty Frag](https://github.com/V4bel/dirtyfrag)와 같은 계열의 또 다른 로컬 권한 상승(local-privilege-escalation, LPE) 익스플로잇인 “Fragnesia”에 대해 OSS Security 메일링 리스트에 [공지](https://lwn.net/ml/all/8733zvfucm.fsf%40gentoo.org/)를 보냈다. [공개 문서](https://github.com/v12-security/pocs/tree/main/fragnesia#fragnesia)에 따르면 다음과 같다.[^c4-fragnesia-xfrm]

> 이는 자체 패치를 받은 dirtyfrag와는 별개의 ESP/XFRM 버그입니다. 하지만 같은 공격 표면에 있으며 완화책도 dirtyfrag와 같습니다.
>
> 이는 Linux XFRM ESP-in-TCP 하위 시스템의 논리 버그를 악용해, 어떤 경쟁 조건(race condition)도 필요로 하지 않고 읽기 전용 파일의 커널 페이지 캐시에 임의 바이트 쓰기를 달성합니다.

James는 [패치](https://lwn.net/ml/all/20260513041635.1289541-1-vakzz%40zellic.io/)가 진행 중이지만 아직 Linus Torvalds의 트리에도, 어떤 stable 커널에도 들어가지 않았다고 언급했다. [개념 증명 익스플로잇](https://github.com/v12-security/pocs/blob/d4043edc2acbd75d093e3f5795751b678c66b259/fragnesia/fragnesia.c)도 공개되어 있다.[^c4-fragnesia-stable]

[^c4-fragnesia-xfrm]: XFRM은 Linux 커널의 IPsec 변환·정책 프레임워크이며, ESP는 암호화된 IPsec 페이로드를 처리한다. 이 영역은 네트워크 입력과 커널 메모리·파일 캐시가 만나는 지점이어서, 논리 오류가 임의 쓰기나 권한 상승으로 이어질 수 있다.
[^c4-fragnesia-stable]: 패치가 mainline 및 stable 트리에 들어가기 전에는 배포판 커널 업데이트가 지연될 수 있다. PoC가 공개된 경우에는 공격 재현 장벽이 낮아지므로, 해당 프로토콜·모듈 사용 여부를 확인하고 임시 비활성화 같은 완화책을 우선 적용하는 것이 실무적으로 중요하다.

[댓글 (29개 게시)](https://lwn.net/Articles/1072647/#Comments)

### [Stenberg: Mythos가 curl 취약점을 찾아내다](https://lwn.net/Articles/1072325/)

#### 요약

- Daniel Stenberg가 Anthropic의 Mythos가 curl에서 발견한 취약점에 대한 긴 글을 게시했다.
- 그는 Mythos에 대한 큰 화제가 주로 마케팅이었다는 결론을 내렸다.
- 이 설정이 기존 도구보다 특별히 더 높은 수준으로 문제를 찾는다는 증거는 보지 못했다고 했다.
- 다만 최신 AI 기반 코드 분석기는 과거 전통적 분석기보다 보안 결함과 실수를 훨씬 잘 찾는다고 강조했다.
- AI 도구의 보편화로 더 많은 사람이 보안 문제를 찾아낼 수 있게 되었다는 점을 지적했다.

Daniel Stenberg는 Anthropic의 Mythos에 대한 자신의 생각을 담은 [긴 글](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/)을 공개했다. Anthropic은 이 모델이 광범위한 공개 배포에는 너무 위험하다고 판단한 바 있다.[^c4-mythos-curl]

> 그러나 제 개인적인 결론은 지금까지 이 모델을 둘러싼 큰 화제가 주로 마케팅이었다는 것 외에는 달리 이를 수 없습니다. 이 설정이 Mythos 이전의 다른 도구들보다 특별히 더 높거나 더 진보된 수준으로 문제를 찾아낸다는 증거는 보지 못했습니다. 어쩌면 이 모델이 조금 더 나을 수도 있지만, 설령 그렇다 해도 코드 분석에 의미 있는 흔적을 남길 정도로 더 낫지는 않아 보입니다.
>
> 이것은 단지 하나의 소스 코드 저장소일 뿐이며, 다른 대상에서는 훨씬 더 나을 수도 있습니다. 저는 여기서 그것이 찾아낸 것에 대해서만 말하고 논평할 수 있습니다.
>
> 하지만 제가 전에 말했던 것을 강조하고 다시 말하게 해주십시오. AI 기반 코드 분석기는 과거 어떤 전통적인 코드 분석기보다도 소스 코드에서 보안 결함과 실수를 찾는 데 훨씬 뛰어납니다. 모든 최신 AI 모델은 이제 이 일을 잘합니다. 시간과 약간의 실험 정신이 있는 사람이라면 이제 보안 문제를 찾아낼 수 있습니다. [고품질 혼돈](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/)은 실제입니다.

[^c4-mythos-curl]: curl은 운영체제, 컨테이너 이미지, CI/CD 파이프라인, 임베디드 장비에 폭넓게 포함되는 네트워크 전송 라이브러리·도구다. AI가 이런 핵심 프로젝트에서 더 많은 버그를 찾아내면 보안 향상에 도움이 되지만, 동시에 보고량 폭증과 검증 부담, 엠바고 관리 문제도 커진다.

[댓글 (36개 게시)](https://lwn.net/Articles/1072325/#Comments)

## 커널 개발

### [커널 릴리스 현황](https://lwn.net/Articles/1072646/)

#### 요약

- 현재 개발 커널은 5월 10일 릴리스된 7.1-rc3이다.
- Linus Torvalds는 7.1도 7.0에서 보였던 큰 규모의 패턴을 이어가고 있다고 말했다.
- 7.1에는 현재까지 2,141명의 개발자가 만든 13,922개의 비병합 changeset이 들어갔고, 그중 395명은 첫 커널 기여자다.
- 5월 7일부터 11일까지 다수의 stable 업데이트가 빠른 속도로 릴리스되었다.
- LLM 기반 취약점 보고가 계속되면 이런 빠른 stable 릴리스 속도도 한동안 이어질 수 있다.

현재 개발 커널은 5월 10일 릴리스된 7.1-rc3이다. Linus는 이렇게 말했다. “7.1이 7.0에서 보았던 더 큰 규모의 패턴을 계속 이어가느냐는 질문에 대한 답은 ‘그렇다’라고 생각한다. 그것은 .0 릴리스 때문에 생긴 우연이 아니었고, 단순히 새로운 정상 상태(new normal)가 된 것으로 보인다.”[^c4-kernel-rc]

7.1 커널에는 현재까지 2,141명의 개발자가 만든 13,922개의 비병합 changeset이 들어갔으며, 그중 395명은 처음으로 커널에 기여한 사람이다. 릴리스 이력은 다음과 같다.

> | RC | Date | Commits |  |
> | --- | --- | --- | --- |
> | **v7.1-rc1** | 2026-04-26 | 13963 | 13963 |
> | **v7.1-rc2** | 2026-05-03 | 475 | 475 |
> | **v7.1-rc3** | 2026-05-10 | 584 | 584 |

자세한 내용은 [KSDB 7.1 페이지](https://lwn.net/ksdb/releases/v7.1/)를 참조하라.

**Stable 업데이트**도 부족하지 않았다. [7.0.4](https://lwn.net/Articles/1071569/), [6.18.27](https://lwn.net/Articles/1071570/), [6.12.86](https://lwn.net/Articles/1071571/)은 5월 7일 릴리스되었다. [6.1.171](https://lwn.net/Articles/1071994/), [5.15.205](https://lwn.net/Articles/1071996/), [5.10.255](https://lwn.net/Articles/1071997/)는 5월 8일 릴리스되었고, 몇 밀리초 뒤 [7.0.5](https://lwn.net/Articles/1071776/), [6.18.28](https://lwn.net/Articles/1071777/), [6.12.87](https://lwn.net/Articles/1071778/), [6.6.138](https://lwn.net/Articles/1071779/) [6.1.172](https://lwn.net/Articles/1071998/) 및 [5.15.206](https://lwn.net/Articles/1071999/)이 뒤따랐다. 이어 [7.0.6](https://lwn.net/Articles/1072312/)과 [6.18.29](https://lwn.net/Articles/1072313/)는 5월 11일에 슬그머니 도착했다. LLM이 몰고 오는 취약점 보고 공세가 계속된다면 이런 속도는 한동안 이어질 수 있다.[^c4-stable-updates]

[7.0.7](https://lwn.net/ml/all/20260512173940.117428952@linuxfoundation.org), [6.18.30](https://lwn.net/ml/all/20260512173938.452574370@linuxfoundation.org), [6.12.88](https://lwn.net/ml/all/20260512173932.810559588@linuxfoundation.org) 업데이트는 검토 과정에 있으며, 5월 14일 예정되어 있다.

[^c4-kernel-rc]: -rc(release candidate)는 다음 mainline 커널의 시험판이다. rc 기간에는 대규모 새 기능보다 회귀(regression) 수정과 안정화가 중심이므로, 변경 규모가 커질수록 테스트와 리뷰 부담도 함께 커진다.
[^c4-stable-updates]: stable 커널은 이미 배포판과 운영 환경에서 쓰이는 버전에 보안·버그 수정만 선별해 백포트(backport)한다. 업데이트 빈도가 높아지면 보안 대응은 빨라지지만, 운영자는 재부팅·검증·모듈 호환성 확인 일정을 더 촘촘히 관리해야 한다.

[댓글 (게시 없음)](https://lwn.net/Articles/1072646/#Comments)

### [단기 긴급 취약점 완화를 위한 killswitch](https://lwn.net/Articles/1071861/)

#### 요약

- 수정이 나오기 전에 취약점 공개가 이어지는 시기가 길어질 가능성이 커지고 있다.
- Sasha Levin은 이런 상황에 대응하기 위한 killswitch 제안을 내놓았다.
- killswitch는 실행 중인 커널에서 특정 기능에 대한 접근을 즉시 비활성화할 수 있다.
- 취약 경로와 관련 기능을 사실상 제거해 패치를 설치할 때까지 시간을 벌자는 접근이다.
- 일부 기능이 하루 동안 동작하지 않는 비용이 취약한 커널을 계속 운영하는 비용보다 작을 수 있다는 논리다.

수정이 준비되기 전에 취약점 공개가 이어지는 긴 시기에 접어든 듯하다. 이 홍수에 대처할 수 있는 한 가지 방법은 Sasha Levin의 killswitch 제안일 수 있다. 요약하면, killswitch는 실행 중인 커널에서 특정 기능에 대한 접근을 즉시 비활성화해, 패치를 설치할 수 있을 때까지 취약한 경로와 그 관련 기능을 사실상 존재하지 않게 날려버릴 수 있다. “대부분의 사용자에게 ‘이 소켓 패밀리가 하루 동안 작동하지 않는다’는 비용은 수정이 들어올 때까지 알려진 취약 커널을 실행하는 비용보다 훨씬 작다.”[^c4-killswitch]

[^c4-killswitch]: 커널 killswitch는 취약한 하위 시스템을 런타임에 차단하는 응급 브레이크에 가깝다. 네트워크 프로토콜, 파일 시스템, ioctl 경로처럼 공격 표면이 명확한 경우 유용할 수 있지만, 기능 중단이 서비스 장애로 이어질 수 있으므로 배포판과 운영자는 “보안 위험 대 가용성 손실”을 빠르게 판단해야 한다.

[댓글 (59개 게시)](https://lwn.net/Articles/1071861/)

### [이번 주의 인용문](https://lwn.net/Articles/1072007/)

#### 요약

- Paul McKenney는 RCU 포인터 누수가 실제로 드물게 보고되는 이유를 농담 섞어 질문했다.
- 그는 커널 개발자들이 RCU read-side critical section을 조심스럽게 다루는 것인지, 아니면 긴 grace period 덕분에 버그가 드러나지 않는 것인지 물었다.
- Linus Torvalds는 AI가 찾은 “보안” 버그는 공개된 것으로 간주하자는 규칙을 제안했다.
- 그는 일반적인 AI 도구로 찾을 수 있는 버그라면 본질적으로 비밀이 아니라고 주장했다.
- 이는 보안 리스트와 비공개 처리의 기준을 AI 시대에 다시 생각해야 한다는 문제를 던진다.

> 여러 해 동안 RCU 포인터 누수를 걱정해 왔지만 실제로 그런 일이 많이 일어났다는 이야기는 듣지 못했다는 점에서, 마지막으로 하나 질문이 있습니다. 이것은 Linux 커널 개발자들이 RCU 읽기 측 임계 구역(read-side critical section)을 감탄스러울 만큼 조심스럽게 다루기 때문일까요? 아니면 RCU 유예 기간(grace period)이 보통 충분히 길어서, 이 개발자들이 지독한 RCU 포인터 누수 버그를 저지르고도 그냥 넘어가고 있기 때문일까요? ;–)

—

Paul McKenney

> 저는 “AI가 찾은 ‘보안’ 버그는 공개된 것이다”라는 규칙을 그냥 만들면 된다고 생각합니다.
>
> 물론 “merge window 동안 내 받은편지함은 재앙이다”라는 상황에 영향을 받았을 수도 있지만, 저는 이것이 꽤 근본적이라고 생각합니다. 누군가가 대체로 표준적인 AI 도구로 버그를 찾았다면(마법 같은 특수 하드웨어나 국가 수준의 노력을 말하는 것이 아니라면), 그 버그는 정의상 거의 비밀이 아닙니다.
>
> 그렇다면 왜 그것을 특별하게 취급해서 보안 리스트에 올려야 합니까?

—

Linus Torvalds[^c4-rcu-ai-quotes]

[^c4-rcu-ai-quotes]: RCU(Read-Copy Update)는 읽기 경로를 빠르게 만들기 위해 Linux 커널에서 널리 쓰이는 동기화 기법이다. 포인터 수명 관리 실수는 use-after-free로 이어질 수 있으며, AI가 대량으로 버그를 찾아내는 환경에서는 무엇을 비공개 보안 이슈로 다룰지에 대한 커뮤니티 절차도 함께 압박을 받는다.

[댓글 (게시 없음)](https://lwn.net/Articles/1072007/#Comments)

## 배포판

### [Debian, 재현 가능한 빌드를 요구하기로](https://lwn.net/Articles/1072314/)

#### 요약

- Paul Gevers가 릴리스 팀 소식 메시지에 Debian의 재현 가능한 패키지 의무화 소식을 담았다.
- Debian은 새 패키지가 재현 가능하지 않거나 testing의 기존 패키지가 재현성에서 회귀하면 migration을 막도록 했다.
- 이 조치는 Reproducible Builds 프로젝트의 노력에 힘입은 것이다.
- 여기서 “재현 가능”은 Debian 빌드 환경 인스턴스 안에서의 재현으로 제한된다.
- 일반적으로 말하는 재현 가능 빌드보다 더 좁은 기준이지만, 중요한 진전이다.

Paul Gevers는 “릴리스 팀 소식(bits from the release team)” 메시지에 흥미로운 뉴스를 슬쩍 넣었다.

> Reproducible Builds 프로젝트의 노력에 힘입어, 우리는 Debian이 재현 가능한 패키지를 제공해야 한다고 말할 때가 되었다고 판단했습니다. 어제부터 우리는 migration 소프트웨어가 재현할 수 없는 새 패키지나 재현성에서 회귀한 기존 패키지(testing 안의 패키지)의 migration을 차단하도록 했습니다.

Gioele Barabucci가 [지적했듯이](https://lwn.net/ml/all/603a3905-a87b-47c2-b834-12e58bed136f@debian.org), 이 의미에서의 “재현 가능(reproducible)”은 Debian의 빌드 환경 인스턴스 안에서 빌드하는 경우로 제한되며, 이는 일반적으로 쓰이는 요구사항보다 더 엄격하게 좁혀진 기준이다. 그래도 재현 가능한 빌드(reproducible builds)를 위한 큰 진전이다.[^c4-debian-reproducible]

[^c4-debian-reproducible]: 재현 가능한 빌드는 같은 소스와 빌드 입력으로 동일한 바이너리를 만들 수 있음을 보장하려는 공급망 보안 기법이다. 배포판 차원에서 migration을 막으면 패키지 유지관리자는 빌드 타임스탬프, 파일 순서, 환경 의존성 같은 비결정성을 고쳐야 하며, 사용자는 소스와 바이너리의 대응 관계를 더 신뢰할 수 있다.

[댓글 (24개 게시)](https://lwn.net/Articles/1072314/)

### [배포판 부문의 이번 주 인용문](https://lwn.net/Articles/1072660/)

#### 요약

- Adam Williamson은 Fedora Hummingbird 발표가 Red Hat Summit을 위한 큰 발표였다고 농담 섞어 평했다.
- 그는 Red Hat 내부에서도 Fedora Hummingbird의 정확한 방향이 이미 완전히 정해졌다고 보지는 않는다고 말했다.
- Summit 발표가 끝났으니 이제 실제로 무엇이 될지 정리하는 작업을 할 수 있을 것이라고 했다.
- 이 인용문은 Fedora 커뮤니티에 놀라움으로 다가온 Fedora Hummingbird 발표를 두고 나온 것이다.

> Adam이 자기 관리 체계의 너무 높은 곳에 있는 사람이 보지 않기를 바라는, 지극히 정치적으로 올바르지 않은 견해는 이렇습니다. RH는 Summit을 위한 크고 화려한 발표를 원했고, 이제 그것을 얻었습니다.
>
> RH가 충분히 민첩하고 조직적이며 내부 소통이 잘되어서 Fedora Hummingbird가 실제로 무엇이 되기를 원하는지 이미 완전히 확실히 알고 있다고 믿는다면, PR 담당 누군가는 엄청난 인상을 받아야 합니다. 왜냐하면 우리는 그렇지 않을 거라고 장담하거든요. 😛
>
> 이제 Summit 일이 끝났으니, Summit에 맞춰 발표를 해내는 데 큰 관심이 있는 유형의 사람들은 긴장을 풀 것이고, 나머지 우리는 이것이 실제로 무엇이 될지를 알아내는 일을 계속할 수 있을 것입니다...

—

Adam Williamson

Fedora 커뮤니티에는 놀라움으로 다가온 Fedora Hummingbird [발표](https://lwn.net/Articles/1072660/)에 대해.[^c4-fedora-hummingbird]

[^c4-fedora-hummingbird]: Fedora는 Red Hat 생태계와 밀접하지만 커뮤니티 주도 배포판이라는 정체성도 중요하다. 대형 행사에 맞춘 발표가 커뮤니티 협의보다 앞서 보이면, 기술 방향 자체보다 거버넌스와 의사소통 방식이 더 큰 쟁점이 될 수 있다.

[댓글 (게시 없음)](https://lwn.net/Articles/1072660/#Comments)

## 개발

### [KDE의 Union 스타일 엔진 업데이트](https://lwn.net/Articles/1071703/)

#### 요약

- Arjen Hiemstra가 KDE 애플리케이션 스타일링 기술을 통합하려는 Union 프로젝트의 현황을 공개했다.
- Union은 KDE의 여러 스타일링 기술을 지원하는 단일 시스템을 목표로 한다.
- Union의 Breeze 구현은 기존 Breeze와 구분하기 어려울 정도로 진전되었다.
- 여러 애플리케이션에서 테스트하며 차이를 수정해 왔다.
- Plasma 6.7 릴리스에 Union을 포함할 계획이며, 기본 활성화 여부는 논의 중이다.

Arjen Hiemstra는 KDE의 애플리케이션 스타일링에 쓰이는 모든 기술을 지원하기 위한 단일 시스템인 [Union](https://invent.kde.org/plasma/union#union) 프로젝트의 현황에 대한 글을 [게시했다](https://quantumproductions.info/articles/2026-05/union-spring-2026-update).[^c4-kde-union]

> Union의 Breeze 구현 작업은 Union 버전을 실행 중인지 아닌지 구분하기 매우 어려울 정도로 진전되었습니다. 또한 여러 애플리케이션으로 테스트하고 차이가 있으면 수정되도록 했습니다. 그래서 이제 Union을 더 많은 사람들의 손에 쥐여주어야 하는 단계에 와 있습니다. 중대한 문제가 있는지 더 많은 사람이 테스트하게 하려는 목적도 있고, 관심 있는 사람들이 새 스타일을 만들게 하려는 목적도 있습니다.
>
> 이는 곧 출시될 Plasma 6.7 릴리스에 Union을 포함할 계획이라는 뜻입니다. 기본으로 활성화할지 여부는 현재 논의 중이지만, 그렇지 않더라도 사용해 볼 방법은 있을 것입니다.

프로젝트와 그 탄생 배경에 대해 더 알고 싶다면 2025년 2월에 게시된 Hiemstra의 [Union 소개 글](https://planet.kde.org/arjen-hiemstra-2025-02-10-moving-kde-s-styling-into-the-future/)을 참조하라. KDE 6.7은 6월 중순에 릴리스될 것으로 예상된다.[^c4-plasma-union]

[^c4-kde-union]: KDE 애플리케이션은 Qt 위젯, Qt Quick, Plasma 구성요소 등 여러 UI 기술을 함께 사용한다. 스타일 엔진이 분산되어 있으면 테마 일관성, 접근성, 유지보수 비용이 문제가 되므로, Union은 KDE 데스크톱의 시각적 통일성과 새 스타일 개발의 진입 장벽을 낮추는 데 의미가 있다.
[^c4-plasma-union]: Plasma 릴리스에 포함되면 배포판 패키징과 사용자 테스트가 본격화된다. 기본값으로 켜지지 않더라도 실사용자 피드백을 받는 단계에 들어간다는 뜻이며, 테마 작성자와 배포판은 호환성 문제를 조기에 확인할 수 있다.

[댓글 (게시 없음)](https://lwn.net/Articles/1071703/#Comments)

### [개발 부문의 이번 주 인용문](https://lwn.net/Articles/1072652/)

#### 요약

- Trammell Hudson은 Mastodon 미디어 보존 설정이 자동 정리를 하지 않은 듯하다고 말했다.
- 저장소 사용량을 통제하기 위해 `tootctl media remove`를 수동으로 실행 중이라고 했다.
- 원격 Mastodon 아바타와 프로필 이미지가 100GB를 넘었다.
- 1980년대부터 1990년대 초까지의 Usenet 아카이브는 9.5GB에 불과하다고 비교했다.
- 농담처럼 NNTP로 돌아가야 할지 모른다고 말했다.

> 우리 Mastodon 미디어 보존 설정이 자동으로 정리하지 않고 있었던 것 같습니다. 저장소 사용량을 다시 통제해 보려고 지금 `tootctl media remove`를 수동으로 실행하고 있습니다.
>
> 우리에게는 원격 Mastodon 아바타와 프로필 이미지가 100GB 넘게 있습니다. 반면 1982년부터 1990년대 초까지의 제 Usenet 아카이브(utzoo 미러)는 9.5GB에 불과합니다. 어쩌면 NNTP로 돌아가야 할지도 모르겠습니다.

—

Trammell Hudson[^c4-mastodon-media]

[^c4-mastodon-media]: Mastodon 같은 ActivityPub 서버는 원격 인스턴스의 미디어와 프로필 이미지를 캐시하므로, 보존 정책이 제대로 작동하지 않으면 저장소가 빠르게 늘어난다. `tootctl media remove` 같은 관리 명령은 운영 비용을 줄이는 실무 도구이며, 오래된 텍스트 중심 프로토콜인 NNTP와의 비교는 현대 소셜 웹의 미디어 중심 저장 비용을 드러낸다.

[댓글 (3개 게시)](https://lwn.net/Articles/1072652/)

## 기타

### [Sovereign Tech Fund, KDE에 투자](https://lwn.net/Articles/1072565/)

#### 요약

- KDE 프로젝트가 Sovereign Tech Fund로부터 100만 유로가 넘는 지원금을 받았다고 발표했다.
- 이 자금은 KDE 데스크톱 환경 소프트웨어 개선에 쓰인다.
- Plasma, KDE Linux, 커뮤니케이션 서비스 기반 프레임워크 등 핵심 인프라의 구조적 신뢰성과 보안을 강화하는 것이 목표다.
- 공공성 있는 오픈소스 데스크톱 인프라에 대한 장기 투자의 의미가 있다.

KDE 프로젝트는 데스크톱 환경 소프트웨어를 개선하기 위해 Sovereign Tech Fund로부터 100만 유로가 넘는 지원금을 받았다고 발표했다. “이 투자는 Plasma, KDE Linux, 그리고 커뮤니케이션 서비스의 기반이 되는 프레임워크를 포함해 KDE 핵심 인프라의 구조적 신뢰성과 보안을 강화하는 데 사용될 것이다.”[^c4-stf-kde]

[^c4-stf-kde]: Sovereign Tech Fund는 공공 디지털 인프라로 쓰이는 오픈소스 프로젝트에 자금을 지원한다. KDE처럼 배포판과 최종 사용자 데스크톱에 널리 쓰이는 프로젝트가 보안·신뢰성 개선 자금을 받으면, 유지관리 부담을 줄이고 장기적인 생태계 안정성을 높일 수 있다.

[댓글 (1개 게시)](https://lwn.net/Articles/1072565/)

**페이지 편집자**: Daroc Alden

---

# 공지

## 뉴스레터

### 배포판 및 시스템 관리

DistroWatch Weekly

May 11

This week in F-Droid

April 30

This week in F-Droid

May 8

openSUSE Tumbleweed Review of the Week

May 8

### 개발

Emacs News

May 11

What's cooking in git.git

May 11

What's cooking in git.git

May 12

This Week in GNOME

May 8

GNU Tools Weekly News

May 10

Golang Weekly

May 8

Last Week in Kubernetes Development

May 7

LLVM Weekly

May 11

This Week in Matrix

May 8

OCaml Weekly News

May 12

Perl Weekly

May 11

This Week in Plasma

May 9

PyCoder's Weekly

May 12

Weekly Rakudo News

May 11

Ruby Weekly News

May 7

This Week in Rust

May 6

Wikimedia Tech News

May 11

### 회의록

Fedora FESCo meeting minutes

May 12

openSUSE Release Engineering minutes

May 6

openSUSE Release Engineering minutes

May 13

This week in the Perl Steering Committee

May 12

## 발표 모집(CFP)

### CFP 마감일: 2026년 5월 14일부터 2026년 7월 13일까지

#### 요약

- 이 목록은 LWN.net CFP Calendar에서 가져온 발표 모집(CFP, Call for Presentations) 마감 일정이다.
- DebConf 26, Open Tech Day, Neocypherpunk Summit, All Systems Go! 2026 등의 제안서 접수 마감일이 포함되어 있다.
- Embedded Linux Conference Europe 및 Open Source Summit Europe의 CFP 마감은 June 24로 표시되어 있다.
- 행사 날짜, 행사명, 장소 및 제안서 제출 링크를 표 형식으로 보존했다.

다음 CFP 마감 목록은

LWN.net CFP Calendar

에서 가져온 것이다.

| 마감일 | 행사 날짜 | 행사 | 장소 |
| --- | --- | --- | --- |
| May 25 | July 20 July 25 | [DebConf 26](https://debconf26.debconf.org/cfp/) | Santa Fe, Argentina |
| May 31 | October 1 | [Open Tech Day | Software-defined Storage](https://opentechday.de/propose/) | Nuremberg, Germany |
| June 14 | June 14 | [Neocypherpunk Summit](https://luma.com/f47k4xnd) | Berlin, Germany |
| June 14 | September 30 October 1 | [All Systems Go! 2026](https://cfp.all-systems-go.io/all-systems-go-2026/cfp) | Berlin, Germany |
| June 24 | October 7 October 9 | [Embedded Linux Conference Europe](https://events.linuxfoundation.org/embedded-linux-conference-europe/program/cfp/) | Prague, Czech Republic |
| June 24 | October 7 October 9 | [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/program/cfp/) | Prague, Czech Republic |
| June 30 | November 17 November 19 | [Open Source Monitoring Conference](https://osmc.de/call-for-papers/) | Nuremberg, Germany |

행사의 CFP 마감일이 여기에 보이지 않으면 [알려 주십시오](https://lwn.net/Calendar/new/).

## 예정된 행사

### 행사: 2026년 5월 14일부터 2026년 7월 13일까지

#### 요약

- 이 목록은 LWN.net Calendar에서 가져온 예정 행사 일정이다.
- PyCon US, RustWeek 2026, Open Source Summit North America, Linux Security Summit North America 등이 포함되어 있다.
- 유럽, 북미, 아시아 지역의 오픈소스·리눅스·개발자 행사를 날짜순으로 정리했다.
- 행사명 링크와 장소 정보는 원문과 동일하게 보존했다.

다음 행사 목록은

LWN.net Calendar

에서 가져온 것이다.

| 날짜 | 행사 | 장소 |
| --- | --- | --- |
| May 15 May 17 | [PyCon US](https://us.pycon.org/2026/) | Long Beach, California, US |
| May 16 May 17 | [Lomiri Tech Meeting](https://os-sci.nl/event/lomiri-tech-meeting-24/register) | Tilburg, The Netherlands |
| May 18 May 23 | [RustWeek 2026](https://2026.rustweek.org/) | Utrecht, Netherlands |
| May 18 May 20 | [Open Source Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/) | Minneapolis, Minnesota, US |
| May 21 May 22 | [Linux Security Summit North America](https://events.linuxfoundation.org/linux-security-summit-north-america/) | Minneapolis, Minnesota, US |
| May 23 May 24 | [Curl up](https://github.com/curl/curl-up/wiki/2026) | Prague, Czechia |
| May 26 | [Media Summit](https://lwn.net/ml/all/92e24f36-d189-4ba8-ad0b-43277bc1aabd@kernel.org) | Nice, France |
| May 27 May 28 | [Embedded Recipes](https://embedded-recipes.org/2026/) | Nice, France |
| May 29 | [libcamera workshop](https://lwn.net/ml/all/20260315221126.GA520505@killaraus.ideasonboard.com) | Nice, France |
| May 29 | [Yocto Project Developer Day](https://pretalx.com/yocto-embedded-recipes-2026/) | Nice, France |
| May 30 May 31 | [Journées du Logiciel Libre 2026](https://jdll.org/) | Lyon, France |
| June 6 | [Hong Kong Open Source Conference](https://hkoscon.org) | Hong Kong |
| June 8 June 12 | [RISC-V Summit Europe 2026](https://riscv-europe.org/summit/2026/) | Bologna, Italy |
| June 12 June 14 | [Southeast Linuxfest](https://southeastlinuxfest.org/) | Charlotte, NC, US |
| June 14 | [Neocypherpunk Summit](https://s26ber.web3privacy.info/) | Berlin, Germany |
| June 14 June 16 | [Flock to Fedora](https://fedoramagazine.org/flock-to-fedora-2026-prague/) | Prague, Czechia |
| June 16 June 17 | [Open Source Summit India](https://events.linuxfoundation.org/open-source-summit-india/) | Mumbai, India |
| June 18 June 20 | [Linux Audio Conference](https://lac26.mucs.club/) | Maynooth, Ireland |


행사가 여기에 보이지 않으면 [알려 주십시오](https://lwn.net/Calendar/new/).

## 보안 업데이트

### [2026년 5월 7일부터 2026년 5월 13일까지의 알림 요약](https://lwn.net/Articles/1072662/)

#### 요약

- 이 표는 2026년 5월 7일부터 5월 13일까지 LWN에 집계된 배포판별 보안 권고(Security advisory) 목록이다.[^c5-security-scope]
- AlmaLinux, Debian, Fedora, Mageia, Oracle, Slackware, SUSE, Ubuntu의 업데이트가 포함되어 있다.
- `kernel`, `linux-*`, `firefox`, `thunderbird`, `openssl`, `apache2`, `exim4` 등 핵심 패키지와 사용자 공간 패키지 업데이트가 함께 나열되어 있다.[^c5-security-packages]
- 표의 ID 링크는 각 LWN 보안 공지 항목으로 연결되며, 릴리스·패키지·날짜 정보는 원문 값을 유지했다.[^c5-advisory-links]

| 배포판 | ID | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:13644](https://lwn.net/Articles/1072568/) | 10 | corosync | 2026-05-13 |
| AlmaLinux | [ALSA-2026:13673](https://lwn.net/Articles/1072184/) | 9 | corosync | 2026-05-08 |
| AlmaLinux | [ALSA-2026:13498](https://lwn.net/Articles/1071599/) | 10 | dovecot | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13857](https://lwn.net/Articles/1071598/) | 9 | dovecot | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13916](https://lwn.net/Articles/1071601/) | 10 | fence-agents | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13917](https://lwn.net/Articles/1071600/) | 9 | fence-agents | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13515](https://lwn.net/Articles/1071602/) | 10 | freeipmi | 2026-05-06 |
| AlmaLinux | [ALSA-2026:14819](https://lwn.net/Articles/1072185/) | 9 | freeipmi | 2026-05-08 |
| AlmaLinux | [ALSA-2026:16014](https://lwn.net/Articles/1072569/) | 10 | freerdp | 2026-05-13 |
| AlmaLinux | [ALSA-2026:16019](https://lwn.net/Articles/1072470/) | 8 | freerdp | 2026-05-11 |
| AlmaLinux | [ALSA-2026:16875](https://lwn.net/Articles/1072570/) | 8 | git-lfs | 2026-05-13 |
| AlmaLinux | [ALSA-2026:14200](https://lwn.net/Articles/1071603/) | 9 | git-lfs | 2026-05-06 |
| AlmaLinux | [ALSA-2026:15969](https://lwn.net/Articles/1072571/) | 10 | glib2 | 2026-05-13 |
| AlmaLinux | [ALSA-2026:15953](https://lwn.net/Articles/1072471/) | 8 | glib2 | 2026-05-11 |
| AlmaLinux | [ALSA-2026:15971](https://lwn.net/Articles/1072472/) | 9 | glib2 | 2026-05-11 |
| AlmaLinux | [ALSA-2026:13642](https://lwn.net/Articles/1071604/) | 10 | image-builder | 2026-05-06 |
| AlmaLinux | [ALSA-2026:16252](https://lwn.net/Articles/1072572/) | 8 | jq | 2026-05-13 |
| AlmaLinux | [ALSA-2026:13566](https://lwn.net/Articles/1071606/) | 10 | kernel | 2026-05-07 |
| AlmaLinux | [ALSA-2026:A006](https://lwn.net/Articles/1072187/) | 10 | kernel | 2026-05-08 |
| AlmaLinux | [ALSA-2026:A004](https://lwn.net/Articles/1072188/) | 8 | kernel | 2026-05-08 |
| AlmaLinux | [ALSA-2026:13565](https://lwn.net/Articles/1071605/) | 9 | kernel | 2026-05-07 |
| AlmaLinux | [ALSA-2026:A005](https://lwn.net/Articles/1072186/) | 9 | kernel | 2026-05-08 |
| AlmaLinux | [ALSA-2026:A007](https://lwn.net/Articles/1072189/) | 8 | kernel-rt | 2026-05-08 |
| AlmaLinux | [ALSA-2026:16196](https://lwn.net/Articles/1072573/) | 8 | kernel-rt | 2026-05-13 |
| AlmaLinux | [ALSA-2026:16799](https://lwn.net/Articles/1072574/) | 8 | krb5 | 2026-05-13 |
| AlmaLinux | [ALSA-2026:14790](https://lwn.net/Articles/1072576/) | 10 | libpng | 2026-05-13 |
| AlmaLinux | [ALSA-2026:14791](https://lwn.net/Articles/1072575/) | 9 | libpng | 2026-05-13 |
| AlmaLinux | [ALSA-2026:14087](https://lwn.net/Articles/1071793/) | 8 | libsoup | 2026-05-08 |
| AlmaLinux | [ALSA-2026:13978](https://lwn.net/Articles/1071607/) | 9 | libsoup | 2026-05-06 |
| AlmaLinux | [ALSA-2026:15968](https://lwn.net/Articles/1072473/) | 10 | libsoup3 | 2026-05-11 |
| AlmaLinux | [ALSA-2026:16055](https://lwn.net/Articles/1072577/) | 8 | libtiff | 2026-05-13 |
| AlmaLinux | [ALSA-2026:14929](https://lwn.net/Articles/1071794/) | 8 | mingw-libtiff | 2026-05-08 |
| AlmaLinux | [ALSA-2026:15888](https://lwn.net/Articles/1072474/) | 10 | openexr | 2026-05-11 |
| AlmaLinux | [ALSA-2026:15887](https://lwn.net/Articles/1072578/) | 9 | openexr | 2026-05-13 |
| AlmaLinux | [ALSA-2026:13643](https://lwn.net/Articles/1071608/) | 10 | osbuild-composer | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13641](https://lwn.net/Articles/1071609/) | 10 | python-tornado | 2026-05-06 |
| AlmaLinux | [ALSA-2026:15892](https://lwn.net/Articles/1072579/) | 9 | thunderbird | 2026-05-13 |
| Debian | [DLA-4571-1](https://lwn.net/Articles/1071795/) | LTS | apache2 | 2026-05-08 |
| Debian | [DSA-6248-1](https://lwn.net/Articles/1071610/) | stable | apache2 | 2026-05-06 |
| Debian | [DSA-6250-1](https://lwn.net/Articles/1071796/) | stable | chromium | 2026-05-07 |
| Debian | [DSA-6261-1](https://lwn.net/Articles/1072190/) | stable | corosync | 2026-05-10 |
| Debian | [DSA-6264-1](https://lwn.net/Articles/1072475/) | stable | dnsmasq | 2026-05-11 |
| Debian | [DLA-4580-1](https://lwn.net/Articles/1072580/) | LTS | exim4 | 2026-05-12 |
| Debian | [DSA-6265-1](https://lwn.net/Articles/1072581/) | stable | exim4 | 2026-05-12 |
| Debian | [DLA-4575-1](https://lwn.net/Articles/1072191/) | LTS | firefox-esr | 2026-05-09 |
| Debian | [DSA-6254-1](https://lwn.net/Articles/1072192/) | stable | firefox-esr | 2026-05-08 |
| Debian | [DLA-4572-1](https://lwn.net/Articles/1072194/) | LTS | kernel | 2026-05-08 |
| Debian | [DSA-6258-1](https://lwn.net/Articles/1072193/) | stable | kernel | 2026-05-09 |
| Debian | [DSA-6253-1](https://lwn.net/Articles/1072195/) | stable | kernel | 2026-05-08 |
| Debian | [DLA-4568-1](https://lwn.net/Articles/1071797/) | LTS | lcms2 | 2026-05-07 |
| Debian | [DSA-6262-1](https://lwn.net/Articles/1072196/) | stable | lcms2 | 2026-05-10 |
| Debian | [DLA-4570-1](https://lwn.net/Articles/1071611/) | LTS | libdatetime-timezone-perl | 2026-05-07 |
| Debian | [DLA-4573-1](https://lwn.net/Articles/1072198/) | LTS | libpng1.6 | 2026-05-09 |
| Debian | [DSA-6263-1](https://lwn.net/Articles/1072197/) | stable | libpng1.6 | 2026-05-10 |
| Debian | [DSA-6251-1](https://lwn.net/Articles/1071798/) | stable | libreoffice | 2026-05-07 |
| Debian | [DLA-4574-1](https://lwn.net/Articles/1072199/) | LTS | linux-6.1 | 2026-05-09 |
| Debian | [DLA-4567-1](https://lwn.net/Articles/1071612/) | LTS | lrzip | 2026-05-06 |
| Debian | [DLA-4576-1](https://lwn.net/Articles/1072476/) | LTS | p7zip | 2026-05-11 |
| Debian | [DLA-4577-1](https://lwn.net/Articles/1072477/) | LTS | p7zip-rar | 2026-05-11 |
| Debian | [DSA-6255-1](https://lwn.net/Articles/1072200/) | stable | php8.2 | 2026-05-08 |
| Debian | [DSA-6256-1](https://lwn.net/Articles/1072201/) | stable | php8.4 | 2026-05-08 |
| Debian | [DSA-6257-1](https://lwn.net/Articles/1072202/) | stable | postorius | 2026-05-08 |
| Debian | [DSA-6252-1](https://lwn.net/Articles/1071799/) | stable | prosody | 2026-05-07 |
| Debian | [DSA-6259-1](https://lwn.net/Articles/1072203/) | stable | pyjwt | 2026-05-09 |
| Debian | [DLA-4579-1](https://lwn.net/Articles/1072478/) | LTS | python-authlib | 2026-05-11 |
| Debian | [DLA-4578-1](https://lwn.net/Articles/1072479/) | LTS | rails | 2026-05-11 |
| Debian | [DSA-6260-1](https://lwn.net/Articles/1072204/) | stable | tor | 2026-05-10 |
| Debian | [DLA-4569-1](https://lwn.net/Articles/1071613/) | LTS | tzdata | 2026-05-07 |
| Debian | [DSA-6249-1](https://lwn.net/Articles/1071614/) | stable | wireshark | 2026-05-06 |
| Fedora | [FEDORA-2026-0f01e844c3](https://lwn.net/Articles/1072231/) | F43 | SDL3_image | 2026-05-11 |
| Fedora | [FEDORA-2026-992a75bea6](https://lwn.net/Articles/1072232/) | F44 | SDL3_image | 2026-05-08 |
| Fedora | [FEDORA-2026-f4e92d8d66](https://lwn.net/Articles/1072480/) | F43 | chromium | 2026-05-12 |
| Fedora | [FEDORA-2026-be6ea464d0](https://lwn.net/Articles/1072207/) | F42 | dotnet10.0 | 2026-05-10 |
| Fedora | [FEDORA-2026-018d6721a0](https://lwn.net/Articles/1072205/) | F43 | dotnet10.0 | 2026-05-11 |
| Fedora | [FEDORA-2026-32952baba5](https://lwn.net/Articles/1072206/) | F44 | dotnet10.0 | 2026-05-10 |
| Fedora | [FEDORA-2026-51dba40a65](https://lwn.net/Articles/1071616/) | F43 | dovecot | 2026-05-07 |
| Fedora | [FEDORA-2026-4349d04c20](https://lwn.net/Articles/1071615/) | F44 | dovecot | 2026-05-07 |
| Fedora | [FEDORA-2026-fff37fe569](https://lwn.net/Articles/1072210/) | F42 | exim | 2026-05-10 |
| Fedora | [FEDORA-2026-c23e1d19d2](https://lwn.net/Articles/1072209/) | F43 | exim | 2026-05-10 |
| Fedora | [FEDORA-2026-7f7b8d957f](https://lwn.net/Articles/1072208/) | F44 | exim | 2026-05-10 |
| Fedora | [FEDORA-2026-6acccc3bff](https://lwn.net/Articles/1072482/) | F42 | firefox | 2026-05-12 |
| Fedora | [FEDORA-2026-8978a60b68](https://lwn.net/Articles/1072483/) | F43 | firefox | 2026-05-12 |
| Fedora | [FEDORA-2026-6bdf499f6b](https://lwn.net/Articles/1072481/) | F44 | firefox | 2026-05-12 |
| Fedora | [FEDORA-2026-cf660bc96a](https://lwn.net/Articles/1071617/) | F43 | forgejo-runner | 2026-05-06 |
| Fedora | [FEDORA-2026-5df889949e](https://lwn.net/Articles/1071618/) | F44 | gh | 2026-05-07 |
| Fedora | [FEDORA-2026-d5f140eb90](https://lwn.net/Articles/1071619/) | F43 | gnutls | 2026-05-07 |
| Fedora | [FEDORA-2026-668d2793e8](https://lwn.net/Articles/1072211/) | F44 | gnutls | 2026-05-08 |
| Fedora | [FEDORA-2026-3e32c54eab](https://lwn.net/Articles/1072484/) | F44 | httpd | 2026-05-12 |
| Fedora | [FEDORA-2026-87dc12705e](https://lwn.net/Articles/1072213/) | F42 | kernel | 2026-05-08 |
| Fedora | [FEDORA-2026-abc00fb4e8](https://lwn.net/Articles/1072214/) | F43 | kernel | 2026-05-08 |
| Fedora | [FEDORA-2026-8cffa03dad](https://lwn.net/Articles/1072212/) | F44 | kernel | 2026-05-08 |
| Fedora | [FEDORA-2026-684396998a](https://lwn.net/Articles/1071620/) | F43 | krb5 | 2026-05-06 |
| Fedora | [FEDORA-2026-d0a0f1c3d2](https://lwn.net/Articles/1071621/) | F43 | nano | 2026-05-07 |
| Fedora | [FEDORA-2026-2fed8dd674](https://lwn.net/Articles/1072217/) | F42 | nextcloud | 2026-05-10 |
| Fedora | [FEDORA-2026-6599e30e04](https://lwn.net/Articles/1072215/) | F43 | nextcloud | 2026-05-11 |
| Fedora | [FEDORA-2026-cb5661d883](https://lwn.net/Articles/1072216/) | F44 | nextcloud | 2026-05-10 |
| Fedora | [FEDORA-2026-e3f870229a](https://lwn.net/Articles/1072219/) | F43 | nodejs22 | 2026-05-08 |
| Fedora | [FEDORA-2026-3b76d8047d](https://lwn.net/Articles/1072218/) | F44 | nodejs22 | 2026-05-08 |
| Fedora | [FEDORA-2026-6acccc3bff](https://lwn.net/Articles/1072486/) | F42 | nss | 2026-05-12 |
| Fedora | [FEDORA-2026-8978a60b68](https://lwn.net/Articles/1072487/) | F43 | nss | 2026-05-12 |
| Fedora | [FEDORA-2026-6bdf499f6b](https://lwn.net/Articles/1072485/) | F44 | nss | 2026-05-12 |
| Fedora | [FEDORA-2026-7af660d639](https://lwn.net/Articles/1071800/) | F42 | openssl | 2026-05-08 |
| Fedora | [FEDORA-2026-edc32576bb](https://lwn.net/Articles/1071622/) | F42 | pdns | 2026-05-06 |
| Fedora | [FEDORA-2026-b47d3e7e16](https://lwn.net/Articles/1071623/) | F43 | pdns | 2026-05-06 |
| Fedora | [FEDORA-2026-4cca750484](https://lwn.net/Articles/1071801/) | F42 | perl-Starman | 2026-05-08 |
| Fedora | [FEDORA-2026-b94aad33a5](https://lwn.net/Articles/1071802/) | F43 | perl-Starman | 2026-05-08 |
| Fedora | [FEDORA-2026-5bb108e1b7](https://lwn.net/Articles/1071803/) | F44 | perl-Starman | 2026-05-08 |
| Fedora | [FEDORA-2026-c66eaae759](https://lwn.net/Articles/1072220/) | F44 | php | 2026-05-11 |
| Fedora | [FEDORA-2026-739d341ab8](https://lwn.net/Articles/1072222/) | F42 | proftpd | 2026-05-08 |
| Fedora | [FEDORA-2026-bdb9342c72](https://lwn.net/Articles/1072223/) | F43 | proftpd | 2026-05-08 |
| Fedora | [FEDORA-2026-549ee32ea1](https://lwn.net/Articles/1072221/) | F44 | proftpd | 2026-05-08 |
| Fedora | [FEDORA-2026-1efa008794](https://lwn.net/Articles/1072226/) | F42 | prosody | 2026-05-10 |
| Fedora | [FEDORA-2026-36c53b9ca8](https://lwn.net/Articles/1072225/) | F43 | prosody | 2026-05-10 |
| Fedora | [FEDORA-2026-2947986ad6](https://lwn.net/Articles/1072224/) | F44 | prosody | 2026-05-10 |
| Fedora | [FEDORA-2026-bc62ef0a6a](https://lwn.net/Articles/1071624/) | F43 | pyOpenSSL | 2026-05-06 |
| Fedora | [FEDORA-2026-44919b3d9f](https://lwn.net/Articles/1072227/) | F44 | python-pulp-glue | 2026-05-10 |
| Fedora | [FEDORA-2026-44919b3d9f](https://lwn.net/Articles/1072228/) | F44 | python-requests | 2026-05-10 |
| Fedora | [FEDORA-2026-2bb2aee489](https://lwn.net/Articles/1072229/) | F43 | rclone | 2026-05-11 |
| Fedora | [FEDORA-2026-63341da831](https://lwn.net/Articles/1072230/) | F44 | rclone | 2026-05-10 |
| Fedora | [FEDORA-2026-e6a4814a4d](https://lwn.net/Articles/1071625/) | F43 | squid | 2026-05-06 |
| Fedora | [FEDORA-2026-11d7d4d8f3](https://lwn.net/Articles/1071626/) | F42 | vim | 2026-05-07 |
| Fedora | [FEDORA-2026-0174d1953a](https://lwn.net/Articles/1071627/) | F42 | xorg-x11-server-Xwayland | 2026-05-07 |
| Mageia | [MGASA-2026-0129](https://lwn.net/Articles/1072582/) | 9 | apache | 2026-05-13 |
| Mageia | [MGASA-2026-0124](https://lwn.net/Articles/1072233/) | 9 | firefox, nss, rootcerts | 2026-05-09 |
| Mageia | [MGASA-2026-0117](https://lwn.net/Articles/1071628/) | 9 | graphicsmagick | 2026-05-07 |
| Mageia | [MGASA-2026-0110](https://lwn.net/Articles/1071629/) | 9 | kernel-linus | 2026-05-07 |
| Mageia | [MGASA-2026-0122](https://lwn.net/Articles/1071630/) | 9 | krb5-appl | 2026-05-07 |
| Mageia | [MGASA-2026-0112](https://lwn.net/Articles/1071631/) | 9 | libexif | 2026-05-07 |
| Mageia | [MGASA-2026-0114](https://lwn.net/Articles/1071632/) | 9 | libtiff | 2026-05-07 |
| Mageia | [MGASA-2026-0121](https://lwn.net/Articles/1071633/) | 9 | nano | 2026-05-07 |
| Mageia | [MGASA-2026-0111](https://lwn.net/Articles/1071634/) | 9 | nginx | 2026-05-07 |
| Mageia | [MGASA-2026-0118](https://lwn.net/Articles/1071635/) | 9 | ntfs-3g | 2026-05-07 |
| Mageia | [MGASA-2026-0116](https://lwn.net/Articles/1071636/) | 9 | opam | 2026-05-07 |
| Mageia | [MGASA-2026-0126](https://lwn.net/Articles/1072234/) | 9 | openvpn | 2026-05-10 |
| Mageia | [MGASA-2026-0130](https://lwn.net/Articles/1072583/) | 9 | perl-Gazelle | 2026-05-13 |
| Mageia | [MGASA-2026-0115](https://lwn.net/Articles/1071637/) | 9 | perl-Net-CIDR-Lite | 2026-05-07 |
| Mageia | [MGASA-2026-0120](https://lwn.net/Articles/1071638/) | 9 | perl-Starlet | 2026-05-07 |
| Mageia | [MGASA-2026-0119](https://lwn.net/Articles/1071639/) | 9 | perl-Starman | 2026-05-07 |
| Mageia | [MGASA-2026-0127](https://lwn.net/Articles/1072584/) | 9 | php | 2026-05-13 |
| Mageia | [MGASA-2026-0128](https://lwn.net/Articles/1072585/) | 9 | sed | 2026-05-13 |
| Mageia | [MGASA-2026-0113](https://lwn.net/Articles/1071640/) | 9 | tcpflow | 2026-05-07 |
| Mageia | [MGASA-2026-0125](https://lwn.net/Articles/1072235/) | 9 | thunderbird | 2026-05-09 |
| Mageia | [MGASA-2026-0123](https://lwn.net/Articles/1072236/) | 9 | vim | 2026-05-09 |
| Mageia | [MGASA-2026-0109](https://lwn.net/Articles/1071641/) | 9 | virtualbox | 2026-05-06 |
| Oracle | [ELSA-2026-13284](https://lwn.net/Articles/1071654/) | OL8 | LibRaw | 2026-05-06 |
| Oracle | [ELSA-2026-13673](https://lwn.net/Articles/1072237/) | OL9 | corosync | 2026-05-08 |
| Oracle | [ELSA-2026-13498](https://lwn.net/Articles/1071644/) | OL10 | dovecot | 2026-05-06 |
| Oracle | [ELSA-2026-13830](https://lwn.net/Articles/1071642/) | OL8 | dovecot | 2026-05-06 |
| Oracle | [ELSA-2026-13857](https://lwn.net/Articles/1071643/) | OL9 | dovecot | 2026-05-06 |
| Oracle | [ELSA-2026-13916](https://lwn.net/Articles/1071646/) | OL10 | fence-agents | 2026-05-06 |
| Oracle | [ELSA-2026-13917](https://lwn.net/Articles/1071645/) | OL9 | fence-agents | 2026-05-06 |
| Oracle | [ELSA-2026-13515](https://lwn.net/Articles/1071647/) | OL10 | freeipmi | 2026-05-06 |
| Oracle | [ELSA-2026-14819](https://lwn.net/Articles/1072238/) | OL9 | freeipmi | 2026-05-08 |
| Oracle | [ELSA-2026-14200](https://lwn.net/Articles/1071804/) | OL9 | git-lfs | 2026-05-07 |
| Oracle | [ELSA-2026-7673](https://lwn.net/Articles/1072239/) | OL7 | gstreamer1-plugins-bad-free, gstreamer1-plugins-base, and gstreamer1-plugins-good | 2026-05-08 |
| Oracle | [ELSA-2026-13642](https://lwn.net/Articles/1071649/) | OL10 | image-builder | 2026-05-06 |
| Oracle | [ELSA-2026-13671](https://lwn.net/Articles/1071648/) | OL9 | image-builder | 2026-05-06 |
| Oracle | [ELSA-2026-13566](https://lwn.net/Articles/1071652/) | OL10 | kernel | 2026-05-06 |
| Oracle | [ELSA-2026-13577](https://lwn.net/Articles/1071650/) | OL8 | kernel | 2026-05-06 |
| Oracle | [ELSA-2026-50258](https://lwn.net/Articles/1072242/) | OL8 | kernel | 2026-05-11 |
| Oracle | [ELSA-2026-50257](https://lwn.net/Articles/1072243/) | OL8 | kernel | 2026-05-11 |
| Oracle | [ELSA-2026-13565](https://lwn.net/Articles/1071651/) | OL9 | kernel | 2026-05-06 |
| Oracle | [ELSA-2026-50257](https://lwn.net/Articles/1072240/) | OL9 | kernel | 2026-05-11 |
| Oracle | [ELSA-2026-50259](https://lwn.net/Articles/1072241/) | OL9 | kernel | 2026-05-11 |
| Oracle | [ELSA-2026-13285](https://lwn.net/Articles/1071653/) | OL8 | libcap | 2026-05-06 |
| Oracle | [ELSA-2026-14790](https://lwn.net/Articles/1072245/) | OL10 | libpng | 2026-05-08 |
| Oracle | [ELSA-2026-14791](https://lwn.net/Articles/1072244/) | OL9 | libpng | 2026-05-08 |
| Oracle | [ELSA-2026-14087](https://lwn.net/Articles/1071805/) | OL8 | libsoup | 2026-05-07 |
| Oracle | [ELSA-2026-13978](https://lwn.net/Articles/1071655/) | OL9 | libsoup | 2026-05-06 |
| Oracle | [ELSA-2026-14929](https://lwn.net/Articles/1072246/) | OL8 | mingw-libtiff | 2026-05-08 |
| Oracle | [ELSA-2026-13380](https://lwn.net/Articles/1071658/) | OL10 | openssh | 2026-05-06 |
| Oracle | [ELSA-2026-13383](https://lwn.net/Articles/1071656/) | OL8 | openssh | 2026-05-06 |
| Oracle | [ELSA-2026-13381](https://lwn.net/Articles/1071657/) | OL9 | openssh | 2026-05-06 |
| Oracle | [ELSA-2026-13643](https://lwn.net/Articles/1071659/) | OL10 | osbuild-composer | 2026-05-06 |
| Oracle | [ELSA-2026-8578](https://lwn.net/Articles/1071806/) | OL7 | perl-XML-Parser | 2026-05-07 |
| Oracle | [ELSA-2026-9614](https://lwn.net/Articles/1071660/) | OL7 | python | 2026-05-06 |
| Oracle | [ELSA-2026-13641](https://lwn.net/Articles/1071662/) | OL10 | python-tornado | 2026-05-06 |
| Oracle | [ELSA-2026-13670](https://lwn.net/Articles/1071661/) | OL9 | python-tornado | 2026-05-06 |
| Oracle | [ELSA-2026-9745](https://lwn.net/Articles/1071663/) | OL7 | python3 | 2026-05-06 |
| Oracle | [ELSA-2026-13651](https://lwn.net/Articles/1071665/) | OL10 | systemd | 2026-05-06 |
| Oracle | [ELSA-2026-13677](https://lwn.net/Articles/1071664/) | OL9 | systemd | 2026-05-06 |
| Oracle | [ELSA-2026-13537](https://lwn.net/Articles/1071666/) | OL8 | thunderbird | 2026-05-06 |
| Oracle | [ELSA-2026-13414](https://lwn.net/Articles/1071667/) | OL8 | tigervnc | 2026-05-06 |
| Slackware | [SSA:2026-132-01](https://lwn.net/Articles/1072586/) |  | expat | 2026-05-12 |
| Slackware | [SSA:2026-128-01](https://lwn.net/Articles/1072247/) |  | kernel | 2026-05-08 |
| Slackware | [SSA:2026-127-01](https://lwn.net/Articles/1071807/) |  | libgpg | 2026-05-07 |
| Slackware | [SSA:2026-127-02](https://lwn.net/Articles/1071808/) |  | mozilla | 2026-05-07 |
| Slackware | [SSA:2026-128-02](https://lwn.net/Articles/1072248/) |  | mozilla | 2026-05-08 |
| Slackware | [SSA:2026-127-03](https://lwn.net/Articles/1071809/) |  | php | 2026-05-07 |
| SUSE | [SUSE-SU-2026:1753-1](https://lwn.net/Articles/1071810/) | SLE15 oS15.4 | 389-ds | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21534-1](https://lwn.net/Articles/1072275/) | SLE-m6.2 | Mesa | 2026-05-11 |
| SUSE | [SUSE-SU-2026:21564-1](https://lwn.net/Articles/1072276/) | SLE16.0 | Mesa | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10739-1](https://lwn.net/Articles/1072587/) | TW | assimp-devel | 2026-05-12 |
| SUSE | [SUSE-SU-2026:21518-1](https://lwn.net/Articles/1072249/) | SLE-m6.2 | build, product-composer | 2026-05-11 |
| SUSE | [SUSE-SU-2026:21574-1](https://lwn.net/Articles/1072250/) | SLE16.0 | c-ares | 2026-05-11 |
| SUSE | [SUSE-SU-2026:21573-1](https://lwn.net/Articles/1072251/) | SLE16.0 | cairo | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:20697-1](https://lwn.net/Articles/1071811/) | oS16.0 | cairo | 2026-05-08 |
| SUSE | [openSUSE-SU-2026:10688-1](https://lwn.net/Articles/1071812/) | TW | cf-cli | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10689-1](https://lwn.net/Articles/1071813/) | TW | chromedriver | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21490-1](https://lwn.net/Articles/1071668/) | SLE-m6.0 | containerd | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:10716-1](https://lwn.net/Articles/1072252/) | TW | copacetic | 2026-05-09 |
| SUSE | [openSUSE-SU-2026:10690-1](https://lwn.net/Articles/1071814/) | TW | cri-tools | 2026-05-07 |
| SUSE | [SUSE-SU-2026:1717-1](https://lwn.net/Articles/1071669/) | MP4.3 SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | curl | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21560-1](https://lwn.net/Articles/1072253/) | SLE16.0 | distribution | 2026-05-11 |
| SUSE | [SUSE-SU-2026:1714-1](https://lwn.net/Articles/1071670/) | SLE15 oS15.3 | erlang | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21541-1](https://lwn.net/Articles/1072254/) | SLE16.0 | firefox | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10720-1](https://lwn.net/Articles/1072255/) | TW | firefox-esr | 2026-05-10 |
| SUSE | [SUSE-SU-2026:1713-1](https://lwn.net/Articles/1071671/) | SLE12 | flatpak | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1754-1](https://lwn.net/Articles/1071815/) | SLE12 | freeipmi | 2026-05-07 |
| SUSE | [SUSE-SU-2026:1755-1](https://lwn.net/Articles/1071816/) | SLE15 oS15.4 | freeipmi | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21550-1](https://lwn.net/Articles/1072256/) | SLE16.0 | frr | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10721-1](https://lwn.net/Articles/1072257/) | TW | frr | 2026-05-10 |
| SUSE | [openSUSE-SU-2026:10722-1](https://lwn.net/Articles/1072258/) | TW | glibc | 2026-05-10 |
| SUSE | [openSUSE-SU-2026:10691-1](https://lwn.net/Articles/1071817/) | TW | gnutls | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10723-1](https://lwn.net/Articles/1072259/) | TW | go1.25 | 2026-05-10 |
| SUSE | [openSUSE-SU-2026:10741-1](https://lwn.net/Articles/1072588/) | TW | go1.26 | 2026-05-12 |
| SUSE | [SUSE-SU-2026:21540-1](https://lwn.net/Articles/1072260/) | SLE16.0 | google-cloud-sap-agent | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10692-1](https://lwn.net/Articles/1071818/) | TW | grafana | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21572-1](https://lwn.net/Articles/1072261/) | SLE16.0 | iproute2 | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10724-1](https://lwn.net/Articles/1072262/) | TW | java-11-openj9 | 2026-05-10 |
| SUSE | [SUSE-SU-2026:1703-1](https://lwn.net/Articles/1071672/) | SLE12 | java-11-openjdk | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1731-1](https://lwn.net/Articles/1071819/) | SLE15 | java-11-openjdk | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10725-1](https://lwn.net/Articles/1072263/) | TW | java-17-openj9 | 2026-05-10 |
| SUSE | [SUSE-SU-2026:1732-1](https://lwn.net/Articles/1071820/) | SLE15 oS15.4 | java-17-openjdk | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21552-1](https://lwn.net/Articles/1072264/) | SLE16.0 | java-17-openjdk | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10726-1](https://lwn.net/Articles/1072265/) | TW | java-1_8_0-openj9 | 2026-05-10 |
| SUSE | [openSUSE-SU-2026:10727-1](https://lwn.net/Articles/1072266/) | TW | java-21-openj9 | 2026-05-10 |
| SUSE | [SUSE-SU-2026:1705-1](https://lwn.net/Articles/1071673/) | SLE15 oS15.6 | java-21-openjdk | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21551-1](https://lwn.net/Articles/1072267/) | SLE16.0 | java-21-openjdk | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10728-1](https://lwn.net/Articles/1072488/) | TW | java-25-openj9 | 2026-05-11 |
| SUSE | [SUSE-SU-2026:1704-1](https://lwn.net/Articles/1071674/) | SLE15 | java-25-openjdk | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21543-1](https://lwn.net/Articles/1072268/) | SLE16.0 | java-25-openjdk | 2026-05-11 |
| SUSE | [SUSE-SU-2026:1751-1](https://lwn.net/Articles/1071821/) | SLE15 | jetty-minimal | 2026-05-07 |
| SUSE | [SUSE-SU-2026:1777-1](https://lwn.net/Articles/1072270/) | SLE11 | kernel | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1778-1](https://lwn.net/Articles/1072269/) | SLE15 | kernel | 2026-05-08 |
| SUSE | [openSUSE-SU-2026:10729-1](https://lwn.net/Articles/1072489/) | TW | krb5 | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10742-1](https://lwn.net/Articles/1072589/) | TW | libQt6Svg6 | 2026-05-12 |
| SUSE | [openSUSE-SU-2026:10717-1](https://lwn.net/Articles/1072271/) | TW | libexif-devel | 2026-05-09 |
| SUSE | [openSUSE-SU-2026:10678-1](https://lwn.net/Articles/1071675/) | TW | liblxc-devel | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:10694-1](https://lwn.net/Articles/1071822/) | TW | libmariadbd-devel | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10732-1](https://lwn.net/Articles/1072490/) | TW | libmodsecurity3 | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10705-1](https://lwn.net/Articles/1072272/) | TW | libpcp-devel | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1716-1](https://lwn.net/Articles/1071676/) | SLE15 | libpng12 | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1750-1](https://lwn.net/Articles/1071823/) | SLE15 oS15.6 | librsvg | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10685-1](https://lwn.net/Articles/1071677/) | TW | libthrift-0_23_0 | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21571-1](https://lwn.net/Articles/1072273/) | SLE16.0 | libtpms | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10715-1](https://lwn.net/Articles/1072274/) | TW | libtree-sitter0_26 | 2026-05-09 |
| SUSE | [openSUSE-SU-2026:10731-1](https://lwn.net/Articles/1072491/) | TW | mcphost | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:20688-1](https://lwn.net/Articles/1071824/) | oS16.0 | mesa | 2026-05-08 |
| SUSE | [openSUSE-SU-2026:10704-1](https://lwn.net/Articles/1072277/) | TW | micropython | 2026-05-08 |
| SUSE | [SUSE-SU-2026:21545-1](https://lwn.net/Articles/1072278/) | SLE16.0 | mozjs128 | 2026-05-11 |
| SUSE | [SUSE-SU-2026:1742-1](https://lwn.net/Articles/1071825/) | SLE15 | mozjs52 | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10695-1](https://lwn.net/Articles/1071826/) | TW | mutt | 2026-05-07 |
| SUSE | [SUSE-SU-2026:1761-1](https://lwn.net/Articles/1072279/) | SLE15 oS15.6 | nginx | 2026-05-08 |
| SUSE | [openSUSE-SU-2026:10696-1](https://lwn.net/Articles/1071827/) | TW | nix | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21492-1](https://lwn.net/Articles/1071679/) | SLE-m6.0 | openCryptoki | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21575-1](https://lwn.net/Articles/1072281/) | SLE16.0 | openCryptoki | 2026-05-11 |
| SUSE | [SUSE-SU-2026:1723-1](https://lwn.net/Articles/1071678/) | SLE5.5 SLE-m5.5 oS15.5 | openCryptoki | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21553-1](https://lwn.net/Articles/1072280/) | SLE16.0 | opencc | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:20699-1](https://lwn.net/Articles/1071828/) | oS16.0 | opencryptoki | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1712-1](https://lwn.net/Articles/1071680/) | SLE15 | openexr | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1711-1](https://lwn.net/Articles/1071681/) | SLE15 oS15.5 | openssl-3 | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1784-1](https://lwn.net/Articles/1072283/) | SLE15 oS15.6 | php-composer2 | 2026-05-11 |
| SUSE | [SUSE-SU-2026:21542-1](https://lwn.net/Articles/1072282/) | SLE16.0 | php-composer2 | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:10706-1](https://lwn.net/Articles/1072284/) | TW | podman | 2026-05-08 |
| SUSE | [openSUSE-SU-2026:10707-1](https://lwn.net/Articles/1072285/) | TW | postfix | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1740-1](https://lwn.net/Articles/1071829/) | SLE15 oS15.6 | python-Django | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:20704-1](https://lwn.net/Articles/1071830/) | oS16.0 | python-django | 2026-05-08 |
| SUSE | [openSUSE-SU-2026:0165-1](https://lwn.net/Articles/1072590/) | osB15 | python-jupyterlab | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1744-1](https://lwn.net/Articles/1071831/) | SLE15 oS15.4 | python-pytest | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21568-1](https://lwn.net/Articles/1072286/) | SLE16.0 | python-pytest | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:20692-1](https://lwn.net/Articles/1071832/) | oS16.0 | python-pytest | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1715-1](https://lwn.net/Articles/1071682/) | SLE15 SLE5.2 SLE5.3 SLE5.4 SLE5.5 SLE-m5.2 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.3 oS15.6 | python3 | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:10718-1](https://lwn.net/Articles/1072287/) | TW | python311-Django | 2026-05-10 |
| SUSE | [openSUSE-SU-2026:10708-1](https://lwn.net/Articles/1072288/) | TW | python311-Django4 | 2026-05-09 |
| SUSE | [openSUSE-SU-2026:10681-1](https://lwn.net/Articles/1071683/) | TW | python311-social-auth-core | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:20717-1](https://lwn.net/Articles/1072591/) | oS16.0 | raylib | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:10682-1](https://lwn.net/Articles/1071684/) | TW | rclone | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:10711-1](https://lwn.net/Articles/1072289/) | TW | redis | 2026-05-09 |
| SUSE | [SUSE-SU-2026:1745-1](https://lwn.net/Articles/1071833/) | SLE15 | rmt-server | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10712-1](https://lwn.net/Articles/1072290/) | TW | semaphore | 2026-05-09 |
| SUSE | [openSUSE-SU-2026:10683-1](https://lwn.net/Articles/1071685/) | TW | skim | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1762-1](https://lwn.net/Articles/1072292/) | SLE12 | strongswan | 2026-05-08 |
| SUSE | [SUSE-SU-2026:21547-1](https://lwn.net/Articles/1072291/) | SLE16.0 | strongswan | 2026-05-11 |
| SUSE | [SUSE-SU-2026:1763-1](https://lwn.net/Articles/1072293/) | MP4.3 SLE15 | terraform-provider-aws, terraform-provider-azurerm, terraform-provider-external, terraform-provider-google, terraform-provider-helm, terraform-provider-kubernetes, terraform-provid | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1741-1](https://lwn.net/Articles/1071834/) | SLE15 | thunderbird | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:10687-1](https://lwn.net/Articles/1071686/) | TW | thunderbird | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:10738-1](https://lwn.net/Articles/1072592/) | TW | thunderbird | 2026-05-12 |
| SUSE | [openSUSE-SU-2026:20709-1](https://lwn.net/Articles/1072294/) | oS16.0 | tor | 2026-05-10 |
| SUSE | [openSUSE-SU-2026:0164-1](https://lwn.net/Articles/1072593/) | osB15 | tor | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:10697-1](https://lwn.net/Articles/1071835/) | TW | traefik | 2026-05-07 |
| SUSE | [openSUSE-SU-2026:20720-1](https://lwn.net/Articles/1072594/) | oS16.0 | trivy | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:10719-1](https://lwn.net/Articles/1072295/) | TW | valkey | 2026-05-10 |
| SUSE | [SUSE-SU-2026:1764-1](https://lwn.net/Articles/1072296/) | SLE12 | vim | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1749-1](https://lwn.net/Articles/1071836/) | oS15.4 | webkit2gtk3 | 2026-05-07 |
| SUSE | [SUSE-SU-2026:21559-1](https://lwn.net/Articles/1072297/) | SLE16.0 | wireshark | 2026-05-11 |
| SUSE | [openSUSE-SU-2026:20685-1](https://lwn.net/Articles/1071837/) | oS16.0 | wireshark | 2026-05-08 |
| SUSE | [SUSE-SU-2026:1743-1](https://lwn.net/Articles/1071838/) | SLE15 | xen | 2026-05-07 |
| Ubuntu | [USN-8239-1](https://lwn.net/Articles/1071687/) | 22.04 24.04 25.10 26.04 | apache2 | 2026-05-06 |
| Ubuntu | [USN-8242-1](https://lwn.net/Articles/1071839/) | 16.04 18.04 20.04 22.04 | civicrm | 2026-05-07 |
| Ubuntu | [USN-8241-1](https://lwn.net/Articles/1071688/) | 14.04 16.04 18.04 | coin3 | 2026-05-07 |
| Ubuntu | [USN-8249-1](https://lwn.net/Articles/1071840/) | 24.04 25.10 | dpkg | 2026-05-07 |
| Ubuntu | [USN-8238-1](https://lwn.net/Articles/1071689/) | 24.04 25.10 26.04 | editorconfig-core | 2026-05-06 |
| Ubuntu | [USN-8270-1](https://lwn.net/Articles/1072595/) | 22.04 24.04 25.10 26.04 | exim4 | 2026-05-12 |
| Ubuntu | [USN-8220-1](https://lwn.net/Articles/1071841/) | 16.04 18.04 | htmlunit | 2026-05-07 |
| Ubuntu | [USN-8263-1](https://lwn.net/Articles/1072492/) | 14.04 16.04 18.04 20.04 22.04 24.04 25.10 | imagemagick | 2026-05-12 |
| Ubuntu | [USN-8235-1](https://lwn.net/Articles/1071690/) | 16.04 | insighttoolkit | 2026-05-07 |
| Ubuntu | [USN-8250-1](https://lwn.net/Articles/1071842/) | 25.10 26.04 | lcms2 | 2026-05-07 |
| Ubuntu | [USN-8251-1](https://lwn.net/Articles/1071843/) | 22.04 24.04 25.10 | libpng1.6 | 2026-05-07 |
| Ubuntu | [USN-8255-1](https://lwn.net/Articles/1071844/) | 20.04 22.04 | linux, linux-* | 2026-05-07 |
| Ubuntu | [USN-8254-1](https://lwn.net/Articles/1071845/) | 22.04 24.04 | linux, linux-* | 2026-05-07 |
| Ubuntu | [USN-8244-1](https://lwn.net/Articles/1071691/) | 24.04 25.10 | linux, linux-aws, linux-aws-6.17, linux-gcp, linux-gcp-6.17, linux-hwe-6.17, linux-oracle, linux-realtime, linux-realtime-6.17 | 2026-05-07 |
| Ubuntu | [USN-8266-1](https://lwn.net/Articles/1072493/) | 16.04 18.04 | linux, linux-aws, linux-aws-fips, linux-aws-hwe, linux-azure-4.15, linux-fips, linux-gcp, linux-gcp-4.15, linux-gcp-fips, linux-hwe, linux-kvm, linux-oracle | 2026-05-11 |
| Ubuntu | [USN-8245-1](https://lwn.net/Articles/1071692/) | 24.04 25.10 | linux-azure, linux-azure-6.17, linux-oem-6.17 | 2026-05-07 |
| Ubuntu | [USN-8267-1](https://lwn.net/Articles/1072494/) | 16.04 18.04 | linux-azure, linux-azure-fips, linux-oracle | 2026-05-11 |
| Ubuntu | [USN-8258-1](https://lwn.net/Articles/1071846/) | 24.04 | linux-azure | 2026-05-07 |
| Ubuntu | [USN-8243-1](https://lwn.net/Articles/1071693/) | 20.04 | linux-azure-5.15 | 2026-05-07 |
| Ubuntu | [USN-8255-2](https://lwn.net/Articles/1072495/) | 20.04 | linux-azure-5.15 | 2026-05-11 |
| Ubuntu | [USN-8260-1](https://lwn.net/Articles/1071847/) | 24.04 | linux-azure-fips | 2026-05-07 |
| Ubuntu | [USN-8179-4](https://lwn.net/Articles/1071694/) | 22.04 | linux-gcp-6.8 | 2026-05-07 |
| Ubuntu | [USN-8254-2](https://lwn.net/Articles/1072496/) | 22.04 24.04 | linux-nvidia, linux-nvidia-6.8, linux-nvidia-lowlatency | 2026-05-11 |
| Ubuntu | [USN-8265-1](https://lwn.net/Articles/1072298/) | 24.04 | linux-nvidia-tegra | 2026-05-11 |
| Ubuntu | [USN-8200-3](https://lwn.net/Articles/1072299/) | 18.04 20.04 | linux-raspi, linux-raspi-5.4 | 2026-05-11 |
| Ubuntu | [USN-8180-6](https://lwn.net/Articles/1072497/) | 22.04 | linux-raspi | 2026-05-11 |
| Ubuntu | [USN-8257-1](https://lwn.net/Articles/1071848/) | 25.10 | linux-raspi | 2026-05-07 |
| Ubuntu | [USN-8261-1](https://lwn.net/Articles/1071849/) | 24.04 | linux-xilinx | 2026-05-07 |
| Ubuntu | [USN-8262-1](https://lwn.net/Articles/1071850/) | 16.04 | lua5.1 | 2026-05-08 |
| Ubuntu | [USN-8248-1](https://lwn.net/Articles/1071851/) | 22.04 24.04 | nasm | 2026-05-07 |
| Ubuntu | [USN-8248-2](https://lwn.net/Articles/1072300/) | 24.04 | nasm | 2026-05-08 |
| Ubuntu | [USN-8233-2](https://lwn.net/Articles/1071695/) | 26.04 | nghttp2 | 2026-05-06 |
| Ubuntu | [USN-8256-1](https://lwn.net/Articles/1071852/) | 20.04 22.04 24.04 25.10 26.04 | opam | 2026-05-07 |
| Ubuntu | [USN-8259-1](https://lwn.net/Articles/1071853/) | 16.04 18.04 20.04 22.04 24.04 26.04 | openexr | 2026-05-07 |
| Ubuntu | [USN-8252-1](https://lwn.net/Articles/1071854/) | 22.04 24.04 25.10 26.04 | openjpeg2 | 2026-05-07 |
| Ubuntu | [USN-8247-1](https://lwn.net/Articles/1071855/) | 16.04 18.04 20.04 22.04 | owslib | 2026-05-07 |
| Ubuntu | [USN-8253-1](https://lwn.net/Articles/1071856/) | 22.04 24.04 25.10 26.04 | postfix | 2026-05-07 |
| Ubuntu | [USN-8242-2](https://lwn.net/Articles/1071857/) | 24.04 | postfixadmin | 2026-05-07 |
| Ubuntu | [USN-8231-1](https://lwn.net/Articles/1071696/) | 22.04 24.04 25.10 26.04 | python-dynaconf | 2026-05-06 |
| Ubuntu | [USN-8236-1](https://lwn.net/Articles/1071697/) | 22.04 24.04 | slurm-wlm | 2026-05-07 |
| Ubuntu | [USN-8240-1](https://lwn.net/Articles/1071698/) | 16.04 18.04 20.04 22.04 24.04 26.04 | swish-e | 2026-05-07 |
| Ubuntu | [USN-8246-1](https://lwn.net/Articles/1071858/) | 22.04 24.04 25.10 26.04 | vim | 2026-05-07 |
| Ubuntu | [USN-8237-1](https://lwn.net/Articles/1071699/) | 24.04 25.10 26.04 | webkit2gtk | 2026-05-06 |

전체 기사

(

댓글: 없음

)

[^c5-security-scope]: LWN의 “Alert summary”는 여러 배포판의 보안 공지를 한곳에 모은 색인으로, 각 배포판의 원 공지를 대체하지 않는다.
[^c5-security-packages]: 커널(kernel) 및 브라우저·메일 서버·암호화 라이브러리 같은 네트워크 노출 패키지 업데이트는 배포판의 권고에 따라 우선 적용 여부를 검토하는 것이 일반적이다.
[^c5-advisory-links]: 표의 권고 ID와 링크, 배포판 릴리스, 패키지 이름, 날짜는 추적 가능성을 위해 번역하지 않고 그대로 두었다.

---

## 주목할 만한 커널 패치

### 커널 릴리스

Linus Torvalds

Linux 7.1-rc3

5월 10일

Greg Kroah-Hartman

Linux 7.0.6

5월 11일

Greg Kroah-Hartman

Linux 7.0.5

5월 08일

Greg Kroah-Hartman

Linux 7.0.4

5월 07일

Greg Kroah-Hartman

Linux 6.18.29

5월 11일

Greg Kroah-Hartman

Linux 6.18.28

5월 08일

Greg Kroah-Hartman

Linux 6.18.27

5월 07일

Greg Kroah-Hartman

Linux 6.12.87

5월 08일

Greg Kroah-Hartman

Linux 6.12.86

5월 07일

Greg Kroah-Hartman

Linux 6.6.138

5월 08일

Greg Kroah-Hartman

Linux 6.1.172

5월 08일

Greg Kroah-Hartman

Linux 6.1.171

5월 08일

Greg Kroah-Hartman

Linux 5.15.206

5월 08일

Joseph Salisbury

5.15.206-rt95

5월 11일

Greg Kroah-Hartman

Linux 5.15.205

5월 08일

Greg Kroah-Hartman

Linux 5.10.255

5월 08일

Luis Claudio R. Goncalves

5.10.255-rt151

5월 08일

### 아키텍처별[^c6-arch]

Jinjie Ruan

arm64/riscv: crashkernel CMA 예약 지원 추가

5월 11일

Jinjie Ruan

arm64: entry: Generic Entry로 변환

5월 11일

Anshuman Khandual

arm64/mm: 128비트 페이지 테이블 엔트리 활성화

5월 13일

Bibo Mao

인터럽트 주입 관련 소규모 개선

5월 11일

Kuan-Wei Chiu

m68k, bpf: 초기 BPF JIT 컴파일러 지원 추가

5월 11일

Zhanpeng Zhang

riscv: SBI Supervisor Software Events 지원 추가

5월 09일

Drew Fustini

riscv: Ssqosid 및 CBQRI resctrl 지원 추가

5월 10일

Guodong Xu

riscv: hwprobe: RVA23U64 기본 동작 노출

5월 11일

Milan Tripkovic

riscv: lib: memcmp() 구현 추가

5월 12일

Himanshu Chauhan

RISC-V 아키텍처용 RAS 지원 추가

5월 13일

Jan Polensky

s390: Rust 지원 활성화 및 필요한 arch glue 추가

5월 12일

Mike Rapoport

sh: NUMA 및 SPARSEMEM 지원 제거

5월 10일

### 빌드 시스템[^c6-build]

Josh Poimboeuf

objtool/arm64: klp-build를 arm64로 포팅

5월 12일

### 코어 커널[^c6-core]

Andrea Righi

sched: proxy execution을 sched_ext와 호환되게 함

5월 06일

Frederic Weisbecker

tick/sched: idle cputime accounting 리팩터링

5월 08일

Boqun Feng

Rust용 참조 카운트 기반 interrupt disable 및 SpinLockIrq (Part 1)

5월 07일

Yonghong Song

bpf: BPF 함수와 kfunc의 스택 인자 지원

5월 07일

Andrea Righi

sched/fair: SMT-aware asymmetric CPU capacity

5월 09일

Peter Zijlstra

sched: pick 경로 평탄화

5월 11일

Leon Hwang

bpf: 공통 속성 지원으로 BPF syscall 확장

5월 11일

John Stultz

Proxy Execution을 위한 최적화된 Donor Migration

5월 12일

Pavel Begunkov

dynamic area 추가

5월 12일

Chuyi Zhou

실시간 성능 향상을 위해 IPI 완료 대기 중 선점 허용

5월 13일

### 개발 도구

Minxi Hou

selftests: openvswitch: pop_vlan 테스트 추가

5월 07일

Jesung Yang via B4 Relay

rust: 최신 rust-analyzer 기능 활용

5월 07일

Paul E. McKenney

Hazard-pointer torture test

5월 07일

Albert Esteve

kunit: 경고 backtrace 억제 지원 추가

5월 08일

Julian Braha

kconfirm 추가

5월 09일

Allison Henderson

selftests: rds: rds selftests에 ROCE 지원 추가

5월 11일

Mike Rapoport

MM selftests를 CI 친화적으로 개선

5월 11일

wen.yang@linux.dev

rv/tlob: task latency over budget RV monitor 추가

5월 12일

Bart Van Assche

lock context analysis 활성화

5월 11일

### 장치 드라이버[^c6-drivers]

John Ogness

8250: 콘솔 흐름 제어 추가

5월 06일

Gregor Herburger

nvmem: Raspberry Pi OTP nvmem 드라이버 추가

5월 06일

sukhdeeps@marvell.com

net: atlantic: AQC113 (Antigua)용 PTP 지원 추가

5월 06일

Rodrigo Alencar via B4 Relay

ADF41513/ADF41510 PLL 주파수 합성기

5월 06일

Wei Wang

PCI: ACS Enhanced Capability 지원 추가

5월 06일

Michal Piekos

H616 및 T113-S3용 hstimer 지원 추가

5월 06일

Ioana Ciornei

dpaa2-switch: LAG offload 지원 추가

5월 06일

Vivek Aknurwar

clk: qcom: 출시 예정 Hawi SoC용 초기 clock controller 추가

5월 06일

Dipayaan Roy

net: mana: full-page RX buffer용 ethtool private flag 추가

5월 06일

Terry Hsiao

drm/panel-edp: 여러 AUO, BOE, CMN, IVO 패널 추가 및 갱신

5월 07일

Rob Clark

drm/msm: PERFCNTR_CONFIG ioctl 추가

5월 06일

Icenowy Zheng

drm: verisilicon: 하드웨어 커서 지원 추가

5월 07일

Dave Stevenson

media/imx355: 일반 코드 정리 및 2-lane 동작 지원 추가

5월 06일

Frank Wunderlich

RSS 및 LRO 지원 추가

5월 06일

Stefan Dösinger

ZTE zx297520v3 지원 추가

5월 06일

Jihong Min

AMD PROM21 xHCI 온도 hwmon 지원

5월 07일

Frank Li

dmaengine: 설정과 descriptor 준비를 결합하는 새 API 추가

5월 06일

Phil Pemberton

ata: libata-scsi: multi-LUN ATAPI 장치 지원

5월 07일

Luiz Angelo Daros de Luca

net: dsa: realtek: rtl8365mb: bridge offloading 및 VLAN 지원

5월 06일

Jihong Min

AMD Promontory 21 xHCI 온도 hwmon 지원

5월 07일

Colin Huang via B4 Relay

Delta E50SN12051 지원 추가

5월 07일

Jagadeesh Kona

X1P42100 플랫폼에서 videocc 및 camcc 지원 추가

5월 07일

Wangao Wang

media: iris: purwa 플랫폼 지원 추가

5월 07일

Sibi Sankar

arm_scmi: vendors: Qualcomm Generic Vendor Extensions

5월 07일

Dmitry Baryshkov

media: iris: AR50LT 코어 지원 추가 및 Agatti 플랫폼 활성화

5월 07일

Mukesh Ojha

firmware: qcom: scm: minidump SRAM destination 지원 추가

5월 07일

Dong Yibo

net: rnpgbe: TX/RX 및 link status 지원 추가

5월 07일

Erikas Bitovtas

media: qcom: venus: MSM8939 지원 추가

5월 07일

Dmitry Baryshkov

drm/panel: Waveshare DSI TOUCH kits 지원

5월 07일

Tommaso Merciai

drm: renesas: rz-du: RZ/G3E 지원 추가

5월 07일

Tommaso Merciai

drm: renesas: rz-du: mipi_dsi: RZ/G3E 지원 추가

5월 07일

fangyu.yu@linux.alibaba.com

iommu/riscv: second-stage domain을 위한 하드웨어 dirty tracking 추가

5월 07일

Vladislav Kulikov

iio: magnetometer: MEMSIC MMC5983MA 드라이버 추가

5월 07일

Dmitry Baryshkov

soc/qcom/ubwc: UBWC 설정 데이터베이스 재작업

5월 07일

Svyatoslav Ryhel

input: misc: Imagis ISA1200 haptic motor 드라이버 지원 추가

5월 07일

Xilin Wu

SC8280XP에서 QoS 설정 활성화

5월 07일

Kartik Rajput

Kernel WDT 지원 추가

5월 07일

Manivannan Sadhasivam via B4 Relay

PCI M.2 전원 시퀀싱 드라이버 수정/개선

5월 07일

Janani Sunil

iio: dac: AD5529R DAC 지원 추가

5월 07일

Miquel Raynal

mtd: spi-nor: 소프트웨어 보호 강화

5월 07일

Kathiravan Thirumoorthy

Qualcomm IPQ9650 SoC용 최소 부팅 지원 추가

5월 07일

Derek J. Clark

lenovo-wmi: 수정 및 개선 추가

5월 07일

Long Li

net: mana: Per-vPort EQ 및 MSI-X interrupt 관리

5월 07일

Harshitha Ramamurthy

gve: PTP gettimex64 지원 추가

5월 07일

Adrián Larumbe

Panthor의 sparse mappings 지원

5월 07일

Loic Poulain

media: qcom: camss: CAMSS Offline Processing Engine 지원

5월 08일

Deborah Brouwer

drm/tyr: userspace MMIO mmap 지원 추가

5월 07일

KhaiWenTan

igc: autonegotiation 없이 link speed 강제 설정 지원 추가

5월 08일

Ratheesh Kannoth

octeontx2-af: npc: 개선 사항.

5월 08일

Edelweise Escala

LTC3220 18채널 LED 드라이버 지원 추가

5월 08일

Imran Shaik

clk: qcom: Qualcomm Shikra SoC용 RPMCC 및 GCC 지원 추가

5월 08일

Thangaraj Samynathan

net: lan743x: PCI11x1x용 SFP 지원 추가

5월 08일

Changhuang Liang

JHB100 SoC용 기본 clock 및 reset 추가

5월 07일

Arun Muthusamy

can: grcan: CANFD 지원 및 개선으로 드라이버 강화

5월 08일

Daniel Machon

net: lan966x: PCIe FDMA 지원 추가

5월 08일

Hangxiang Ma

media: qcom: camss: Kaanapali 지원 추가

5월 08일

Hangxiang Ma

media: qcom: camss: SM8750 지원 추가

5월 08일

Prabhakar

RZ/T2H 및 RZ/N2H SoC용 DU 지원 추가

5월 08일

Yu-Chun Lin

clk: realtek: RTD1625 clock 지원 추가

5월 08일

javen

r8169: RTL8127용 RSS 지원 추가

5월 08일

Griffin Kroah-Hartman

gpio-keys에 regulator 지원 추가

5월 08일

Markus Schneider-Pargmann (TI)

clocksource/drivers/timer-ti-dm: clocksource 및 clockevent 지원 추가

5월 08일

Lorenzo Bianconi

net: airoha: 동일 GDM 포트에 연결된 여러 net_device 지원

5월 07일

Przemek Kitszel

devlink, mlx5, iavf, ice: iavf용 XLVF

5월 08일

Ping-Ke Shih

wifi: rtw89: 특히 HE SIG-A/SIG-B 관련 radiotap 개선

5월 06일

Sriharsha Basavapatna

RDMA/bnxt_re: QP uapi extension 지원

5월 08일

Honglei Huang

drm/amdgpu: drm_gpusvm 기반 SVM 구현

5월 08일

syyang@lontium.com

Lontium LT7911EXC eDP to MIPI DSI bridge 추가

5월 08일

Shyam Sundar S K

platform/x86/amd/pmf: userspace interface를 갖춘 PMF util layer 도입

5월 07일

Jihong Min

AMD Promontory 21 xHCI 온도 센서 지원

5월 08일

Rodrigo Alencar via B4 Relay

AD9910 Direct Digital Synthesizer

5월 08일

Vishnu Reddy

media: iris: glymur 플랫폼 지원 추가

5월 09일

Matthew Leung

phy: qcom: qmp-pcie: Hawi용 PCIe PHY 지원 추가

5월 08일

Wei Fang

i.MX94용 예비 NETC switch 지원 추가

5월 09일

Jernej Skrabec

drm/sun4i: DE33 지원 갱신

5월 09일

Derek J. Clark

MSI Claw HID Configuration Driver 추가

5월 10일

Tariq Toukan

net/mlx5: satellite PF 지원을 위한 eswitch infrastructure 준비

5월 10일

Stefan Dösinger

ZTE zx297520v3 clock bindings 및 드라이버

5월 10일

Piyush Patle

iio: adc: hx711: HX710B 지원 추가

5월 11일

Ben Hoff

media: pci: AVMatrix HWS capture driver 추가

5월 10일

Jiafei Pan

remoteproc: i.MX 플랫폼에서 Cortex-A Core remoteproc 지원 추가

5월 11일

Peter Chen

CIX Sky1 Cadence USB3 지원 추가

5월 11일

Krishna Chaitanya Chundru

PCI: PCIe WAKE# interrupt 지원 추가

5월 11일

Wei Fang

net: enetc: ENETC v4 VF 지원 준비

5월 11일

Wenmeng Liu

media: camss: purwa 플랫폼 지원 추가

5월 11일

Michael Dege

net: renesas: rswitch: R-Car S4에 VLAN aware switching 추가

5월 11일

Neil Armstrong

media: qcom: iris: 10bit 형식 디코딩 지원 추가

5월 11일

Guoniu Zhou

media: nxp: CSI Pixel Formatter 지원 추가

5월 11일

Radu Sabau via B4 Relay

iio: adc: ad4691: AD4691 multichannel SAR ADC family용 드라이버 추가

5월 11일

Dumitru Ceclan via B4 Relay

media: i2c: Maxim GMSL2/3 serializer 및 deserializer 드라이버 추가

5월 11일

Anvesh Jain P

Qualcomm reference device에서 발견되는 EC용 드라이버 추가

5월 11일

Jian Hu via B4 Relay

A9 family clock controller 지원 추가

5월 11일

Minghuan Lian

net: dsa: NXP i.MX RT1180 NETC switch 지원 추가

5월 09일

Jiawen Wu

net: wangxun: timeout 및 error

5월 09일

Mika Westerberg

thunderbolt: USB4STREAM 도입

5월 11일

Antoine Bouyer

media: iMX95 neoisp 드라이버 추가

5월 11일

Svyatoslav Ryhel

Infineon/Intel XMM6260 modem 지원 추가

5월 11일

Benoît Monin

dmaengine: fsl-edma: scatter/gather 개선

5월 11일

Vladimir Oltean

Lynx 28G SerDes: 25GbE 지원

5월 11일

Ben Horgan

arm_mpam: resctrl: Counter Assignment (ABMC)

5월 11일

Tariq Toukan

net/mlx5e: RSS indirection table 크기 산정 및 resize 개선

5월 11일

Selvamani Rajagopal

onsemi: s2500: TS2500 MAC-PHY용 드라이버 지원 추가

5월 11일

Jacob Pan

iommufd: cdev용 noiommu 모드 활성화

5월 11일

Prabhakar

RZ/T2H 및 RZ/N2H SoC용 System Controller 지원 추가

5월 11일

Nathan Lynch via B4 Relay

dmaengine: Smart Data Accelerator Interface (SDXI) 기본 지원

5월 11일

Prabhakar

RZ/T2H 및 RZ/N2H용 PLL3 및 LCDC_CLKD 지원 추가

5월 11일

Grzegorz Nitka

dpll/ice: E825용 generic DPLL type 및 전체 TX reference clock control 추가

5월 12일

Abdurrahman Hussain

hwmon: Murata D1U74T-W PSU 드라이버 추가

5월 11일

dongxuyang@eswincomputing.com

ESWIN EIC7700 HSP clock 및 reset generator용 드라이버 지원 추가

5월 12일

Yu-Chun Lin

gpio: realtek: Realtek DHC RTD1625 지원 추가

5월 12일

Louis-Alexis Eyraud

Airoha AN8801R series Gigabit Ethernet PHY 드라이버 도입

5월 12일

Roman Vivchar via B4 Relay

MediaTek mt6323 PMIC용 AUXADC, EFUSE 및 thermal driver 추가

5월 12일

Zi-Yu Chen

i2c: ma35d1: MA35D1 I2C controller 지원 추가

5월 12일

Changhuang Liang

StarFive JHB100 syscon module 추가

5월 12일

Boris Brezillon

drm/panthor: dma_fence signalling latency 감소

5월 12일

Marcin Szycik

ACL 지원 추가

5월 11일

Laurent Pinchart

media: renesas: vsp1: 드라이버 현대화

5월 12일

Markus Stockhausen

i2c: i2c-shared-gpio 드라이버 추가

5월 11일

Dmitry Baryshkov

media: iris: SM8350 및 SC8280XP 지원 활성화

5월 12일

Benoît Monin

Mobileye EyeQ7H용 clock 및 reset 지원 추가

5월 12일

Jagadeesh Kona

Glymur 플랫폼에서 camera clock controller 지원 추가

5월 12일

Bastien Curutchet (Schneider Electric)

net: dsa: microchip: 불필요한 ksz_dev_ops callback 제거

5월 12일

Dmitry Baryshkov

media: qcom: iris: generic Gen2 firmware 탐지 및 로딩 추가

5월 12일

John Madieu

ASoC: rsnd: RZ/G3E audio driver 지원 추가

5월 12일

Markus Stockhausen

irqchip/irq-realtek-rtl: multicore 지원 추가

5월 12일

Akhil P Oommen

drm/msm: GMU에 드라이버 연결

5월 13일

Lothar Rubusch

crypto: atmel - 공통 i2c 지원 리팩터링 및 SHA256 ahash 지원 추가

5월 12일

illusion.wang

Nebulamatrix NIC용 nbl 드라이버

5월 13일

Tianyang Zhang

Loongarch irq-redirect 지원

5월 13일

Javier Carrasco

iio: light: veml6031x00 ALS series 지원 추가

5월 13일

Ryan Chen

ASPEED AST2600 I2C controller 드라이버 추가

5월 13일

Avinash Bhatt

wifi: iwlwifi: Device Tree hardware integration 정보 추가

5월 13일

Herve Codina

ASoC: GPIO 구동 amplifier 지원 추가

5월 13일

Angelo Dureghello

mcf54415 DAC 드라이버 추가

5월 13일

Tomi Valkeinen

drm/tidss: BeagleY-AI display 지원 추가(및 일부 추가 사항)

5월 13일

Raag Jadav

drm_ras에 error threshold 도입

5월 13일

Michael Chan

bnxt_en: kTLS TX offload 지원 추가

5월 12일

Maciek Machnikowski

netdevsim에서 PTP 지원 구현

5월 13일

Chris Morgan

Invensense ICM42607 추가

5월 12일

Guilherme Ivo Bozi

drm/amd/display: GPIO translation logic을 lookup table로 변환

5월 12일

Thadeu Lima de Souza Cascardo

dmem: amdgpu 지원 및 테스트 하나 더 추가

5월 12일

Junhua Shen

drm/amdgpu: drm_pagemap을 통한 SVM VRAM migration (XNACK-on)

5월 13일

### 장치 드라이버 인프라[^c6-drivers]

Sungho Bae

virtio: virtio-mmio용 noirq system sleep PM callback 추가

5월 07일

Danilo Krummrich

rust: device: 장치 드라이버용 Higher-Ranked Lifetime Types

5월 06일

Danilo Krummrich

rust: drm: Higher-Ranked Lifetime private data

5월 07일

Danilo Krummrich

rust: devres: ForLt-aware device resource access용 DevresLt 추가

5월 06일

Troy Mitchell

ASoC: cross-DAI coordination을 위한 shared BCLK rate constraint 추가

5월 07일

Lyude Paul

DeviceContext 도입

5월 07일

alistair23@gmail.com

lib: SPDM의 Rust 구현

5월 08일

Tzung-Bi Shih

drivers/base: revocable 도입

5월 08일

Ulf Hansson

driver core / pmdomain: fine-grained sync_state 지원 추가

5월 08일

Jiri Pirko

RDMA: umem용 generic buffer descriptor infrastructure 도입

5월 07일

Sanjay Chitroda

iio: hid sensor 설정 및 정리를 위한 devm_ API 도입

5월 09일

Manos Pitsidianakis

Rust virtio binding 및 sample device 추가

5월 09일

Francesco Valla

splash DRM client 추가

5월 10일

AngeloGioacchino Del Regno

SPMI: sub-device 구현 및 드라이버 마이그레이션

5월 11일

Thomas Hellström

dmem cgroup controller에 reclaim 추가

5월 11일

Aneesh Kumar K.V (Arm)

dma-mapping: direct, pool, swiotlb 경로에서 DMA_ATTR_CC_SHARED 사용

5월 12일

Linus Walleij

sparse unidirectional GPIO line 지원.

5월 11일

Vipin Sharma

vfio/pci: VFIO용 기본 Live Update 지원

5월 11일

Adrian Hunter

i3c: Hot-Join 개선 및 MIPI HCI Hot-Join 지원

5월 12일

Michael Margolin

Completion Counter 도입

5월 11일

Francois Dugast

gpu/buddy: order별 free 및 used block scoreboard

5월 11일

Thomas Weißschuh

driver core: device attribute의 const화 허용

5월 12일

David Matlack

PCI: liveupdate: Live Update를 위한 PCI core 지원

5월 12일

Maxime Chevallier

net: phy_port: SFP module 표현 및 phy_port 목록화

5월 13일

Tao Cui

cgroup/rdma: rdma.peak 및 rdma.events[.local] 추가

5월 13일

### 문서화

Mauro Carvalho Chehab

process/maintainers 출력 개선

5월 09일

Willy Tarreau

Documentation: security-bugs: triage와 AI를 다루는 새 업데이트

5월 09일

### 파일시스템 및 블록 계층[^c6-fs]

Alex Markuze

ceph: 수동 client session reset

5월 07일

Namjae Jeon

exfat: iomap으로 변환

5월 07일

Loic Poulain

block device NVMEM provider 지원

5월 07일

Baolin Liu

ext4: mballoc statistics reporting 및 control 개선

5월 08일

Chuck Lever

case folding 동작 노출

5월 07일

Qu Wenruo

btrfs: folio ordered flag 제거

5월 07일

Baokun Li

ext4/lib-crc: LBS 성능 part 1 - bitmap checksum용 incremental CRC32c

5월 08일

DaeMyung Kang

ntfs: MFT record 및 attribute parsing 강화

5월 09일

Zhang Yi

ext4: 일반 파일의 buffered I/O path에 iomap 사용

5월 11일

Li Chen

ext4: fast commit: FC log를 위한 inode state snapshot

5월 11일

Aaron Tomlin

blk: isolcpus configuration 준수

5월 12일

Daniel Vacek

btrfs: fscrypt 지원 추가

5월 13일

Qu Wenruo

btrfs: huge data folio에 대한 실험적 지원

5월 13일

Jeff Layton

nfs: struct nfs_inode에서 fileid field 제거

5월 12일

LiaoYuanhong-vivo

f2fs: encrypted inline data 지원

5월 13일

### 메모리 관리[^c6-mm]

Thadeu Lima de Souza Cascardo

cgroup/dmem: peak 파일 도입

5월 06일

Zhen Ni

mm/page_owner: print_mode 및 NUMA filtering용 filter infrastructure 추가

5월 07일

Ackerley Tng via B4 Relay

guest_memfd: In-place conversion 지원

5월 07일

Michael S. Tsirkin

mm/virtio: host-zeroed page의 중복 zeroing 건너뛰기

5월 07일

Wenchao Hao

mm/zsmalloc: swap entry release 가속을 위한 per-cpu deferred free

5월 08일

Wenchao Hao

mm/zsmalloc: zs_free()의 lock contention 감소

5월 08일

Vernon Yang

mm: mTHP를 더 투명하게 만들기 위해 cgroup-bpf를 통한 mthp_ext 도입

5월 08일

Kiryl Shutsemau (Meta)

userfaultfd: VM guest memory용 working set tracking

5월 08일

fujunjie

mm: zswap-backed anonymous large folio swapin 지원

5월 08일

Baoquan He

mm/swap: swap_ops를 사용해 swap device method 등록

5월 11일

Shivam Kalra via B4 Relay

mm/vmalloc: vrealloc() shrink 시 사용하지 않는 page 해제

5월 11일

Hao Jia

mm/zswap: per-cgroup proactive writeback 구현

5월 11일

Breno Leitao

mm/memory-failure: 복구 불가능한 page에 대한 panic option 추가

5월 11일

Nico Pache

khugepaged: mTHP 지원

5월 11일

Alexandre Ghiti

per-memcg-per-node kmem accounting

5월 11일

Albert Esteve

memcg: pid_fd를 통한 dma-buf per-cgroup accounting

5월 12일

Christoph Hellwig

swap_activate interface 개선

5월 12일

SeongJae Park

mm/damon: data attributes monitoring 도입

5월 12일

Stanislav Kinsburskii

mm/hmm: userfaultfd-backed mapping용 mmap lock-drop 지원 추가

5월 13일

Muchun Song

mm: HugeTLB 및 device DAX용 HVO 일반화

5월 13일

### 네트워킹[^c6-net]

Simon Schippers

tun/tap & vhost-net: TX drop 감소를 위해 가득 찬 ptr_ring에 qdisc backpressure 적용

5월 06일

Mark Bloch

devlink: boot-time default 추가

5월 06일

Bobby Eshleman

net: devmem: netkit device와 함께 devmem 지원

5월 07일

Wei Wang

psp: dev-assoc/disassoc 지원 추가

5월 07일

Kuniyuki Iwashima

bpf: TCP AutoLOWAT용 SOCK_OPS hook 추가.

5월 08일

David Carlier

mptcp: parent socket에서 MSG_ERRQUEUE 지원

5월 06일

Lorenzo Bianconi

IPv6 상의 IPv4 및 SIT flowtable SW acceleration 추가

5월 06일

Eric Dumazet

net/sched: lockless qdisc dump 준비

5월 07일

Priyansha Tiwari

wifi: nl80211: AP 및 STA용 PROBE_PEER 도입

5월 07일

Matthieu Baerts (NGI0)

mptcp: pm: in-kernel: limit 증가

5월 08일

Mahe Tardy

bpf: bpf_netpoll 도입

5월 11일

Breno Leitao

net: 남은 bluetooth socket family를 getsockopt_iter로 변환

5월 11일

Maciej Fijalkowski

xdp: veth에 generic skb XDP handling 재사용

5월 09일

Miri Korenblit

wifi: iwlwifi: mld: NAN DATA 지원 추가 - part 1

5월 10일

David Howells

rxrpc: DATA/RESPONSE decrypt 대 splice()에 대한 더 나은 수정

5월 11일

Alice Mikityanska

UDP tunnel용 BIG TCP

5월 12일

### 보안 관련[^c6-security]

Sasha Levin

killswitch: per-function short-circuit mitigation primitive 추가

5월 07일

Blaise Boscaccy

Hornet LSM 재도입

5월 07일

Song Liu

lsm: security_sb_mount를 세분화된 mount hook으로 대체

5월 08일

### 가상화 및 컨테이너[^c6-virt]

Wei-Lin Chang

KVM: arm64: nv: nested stage-2 reverse map 구현

5월 10일

David Woodhouse

00/30] KVM clock mess 정리

5월 09일

Douglas Freimuth

KVM: s390: kvm_arch_set_irq_inatomic Fast Inject 도입

5월 11일

Yu Zhang

Hyper-V: Linux guest용 para-virtualized IOMMU 지원 추가

5월 12일

Chang S. Bae

KVM: x86: guest용 APX 활성화

5월 12일

Mukesh R

Hyper-V에서 PCI passthru (Part I)

5월 11일

Mukesh R

Hyper-V에서 PCI passthru (Part II)

5월 11일

Paolo Bonzini

KVM: struct kvm_mmu에 chainsaw 적용

5월 11일

Amit Machhiwal

KVM: PPC: nested guest의 CPU compatibility mode 처리

5월 13일

### 기타

Yushan Wang

perf tool: 여러 플랫폼의 iostat 지원

5월 07일

Luis

SPDX SBOM generation script 추가

5월 07일

Ian Rogers

perf tools: inject --aslr 기능 및 선행 robustness fix 추가

5월 08일

Andrey Albershteyn

xfsprogs: v7.0.0 릴리스

5월 07일

Sean Christopherson

perf/x86: KVM 전환 시 PEBS_ENABLED를 쓰지 않음

5월 08일

Arnaldo Carvalho de Melo

perf: 조작/손상된 파일에 대해 perf.data parsing 강화

5월 10일

David Sterba

Btrfs progs release 7.0

5월 10일

Kaitao cheng

bpf: bpf_list family API 확장

5월 12일

Ian Rogers

perf build: 빌드 시간을 1/3 줄임

5월 11일

Maciej Wieczor-Retman

tools: kernel tools에 intel-lpmd 추가

5월 12일

Ian Rogers

perf tool: perf_sample에 evsel 추가

5월 12일

**페이지 편집자**: Joe Brockmeier

[^c6-arch]: 아키텍처별 패치는 CPU/플랫폼별 저수준 지원(엔트리 코드, 페이지 테이블, NUMA 등)에 관련된다.
[^c6-build]: 빌드 시스템 항목은 커널 빌드·분석 도구 및 아키텍처 포팅 작업을 다룬다.
[^c6-core]: 코어 커널 항목은 스케줄러, BPF, 인터럽트, 선점 등 공통 커널 메커니즘을 포함한다.
[^c6-drivers]: 장치 드라이버와 드라이버 인프라는 하드웨어 지원 및 드라이버 공통 프레임워크 변경을 포함한다.
[^c6-fs]: 파일시스템 및 블록 계층 항목은 저장장치 I/O 경로, 파일시스템 기능, 무결성·암호화 지원을 포함한다.
[^c6-mm]: 메모리 관리 항목은 cgroup, swap, folio, userfaultfd, HugeTLB/DAX 등 메모리 하위시스템 변경을 다룬다.
[^c6-net]: 네트워킹 항목은 네트워크 스택, BPF/XDP, 무선, MPTCP, 드라이버 연동 기능을 포함한다.
[^c6-security]: 보안 관련 항목은 LSM hook, 완화 primitive, 보안 버그 대응 문서 등 보안 하위시스템 변경을 포함한다.
[^c6-virt]: 가상화 및 컨테이너 항목은 KVM, Hyper-V, IOMMU, PCI passthrough 등 guest/host 가상화 지원을 다룬다.
