# LWN.net Weekly Edition for August 27, 2026 (한국어 기술 번역)

- **원문 URL:** https://lwn.net/Articles/1089643/bigpage
- **선택 기준:** 최신호인 2026년 9월 3일호는 유료 공개 전일 가능성이 있어 제외했고, 바로 직전의 공개 `bigpage`인 2026년 8월 27일호(기사 ID `1089643`)를 선택했다.
- **생성 시각(UTC):** 2026-09-04T00:55:09+00:00
- **공개 범위:** 로그인 없이 공개적으로 접근 가능한 위 `bigpage`의 내용만 번역했다. 로그인·구독·유료 전용 콘텐츠를 우회하거나 포함하지 않았다.

## 전체 요약

- Bambu Lab 3D 프린터 소프트웨어의 AGPLv3·GPLv2 준수 논쟁과 사용자 대안 마련 노력을 다룬다.
- OpenMDW 라이선스가 Open Source AI Definition과 충돌할 수 있는 지점, 그리고 LLM 배포의 자유 조건을 살핀다.
- 암호 민첩성(crypto agility), 웹과 OpenPGP의 양자 내성 전환, Linux 7.3 병합 창의 주요 변경을 소개한다.
- Remind와 Quickshell 같은 사용자 공간 도구, 배포판·개발 도구 릴리스와 커뮤니티 소식을 모았다.
- 보안 업데이트와 Linux 커널 패치를 분야별로 묶어 운영자·개발자의 점검 우선순위를 제시한다.


---

### [2026년 8월 27일자 LWN.net 주간판에 오신 것을 환영합니다](https://lwn.net/Articles/1090774/)

#### 요약

- 이번 호의 특집은 3D 프린터 소프트웨어의 AGPL 위반, LLM 배포 라이선스, 양자 컴퓨팅 시대의 암호 전환, Linux 7.3 병합 창 등을 다룬다.
- 명령행 일정 관리 도구 Remind와 Quickshell 데스크톱 구성요소 툴킷도 소개한다.
- 별도 내부 페이지에는 커뮤니티 단신과 뉴스레터·컨퍼런스·보안 업데이트·패치 공지가 수록되어 있다.

이 호에는 다음 특집 기사가 실려 있다.

- [계속되는 3D 프린터 AGPL 위반](https://lwn.net/Articles/1089390/): Bambu Lab 3D 프린터 소프트웨어 사용자가 대안을 이용할 수 있도록 하기 위해 진행 중인 노력.
- [OpenMDW 라이선스 검토](https://lwn.net/Articles/1089251/): LLM과 관련 자료 배포를 위한 라이선스가 현재 형태로는 OSI 승인을 얻기 어려워 보이는 이유.
- [양자 컴퓨팅으로부터 안전해지는 법](https://lwn.net/Articles/1088305/): 미래의 양자 컴퓨터로부터 오늘날의 암호화 데이터를 보호하기 위해 필요한 설정 변경과 프로토콜 업데이트.
- [7.3 병합 창의 시작](https://lwn.net/Articles/1089244/): 다음 커널 릴리스에 들어갈 주목할 만한 변경 사항.
- [Remind로 하는 전통적인 명령행 일정 관리](https://lwn.net/Articles/1090376/): Linux보다도 오래된 일정 관리 시스템 살펴보기.
- [Quickshell 데스크톱 구성요소 툴킷 살펴보기](https://lwn.net/Articles/1083090/): 미니멀 창 관리자를 위한 인기 데스크톱 셸의 기반 프로젝트.

이번 주 판에는 다음 내부 페이지도 포함되어 있다.

- [단신](https://lwn.net/Articles/1089645/): 커뮤니티 전반의 짧은 소식.
- [공지](https://lwn.net/Articles/1089646/): 뉴스레터, 컨퍼런스, 보안 업데이트, 패치 등.

이번 주 호도 즐겁게 읽으시기 바라며, 늘 그렇듯 LWN.net을 후원해 주셔서 감사드린다.

[댓글 (게시물 없음)](https://lwn.net/Articles/1090774/#Comments)

### [계속되는 3D 프린터 AGPL 위반](https://lwn.net/Articles/1089390/)

#### 요약

- Software Freedom Conservancy(SFC)는 Bambu Lab이 Bambu Studio와 프린터 펌웨어에서 AGPLv3 및 GPL 계열 의무를 위반하고 있다고 설명했다.
- 핵심 쟁점은 소스 없이 배포되는 동적 라이브러리와, 서버 쪽 독점 기능에 접근하게 하는 User-Agent 기반 장벽이다. 발표자들은 이것이 AGPL이 막으려 했던 바로 그 우회 방식이라고 본다.
- SFC와 3D 프린팅 커뮤니티는 소송뿐 아니라 역공학, 대체 구현, 소비자의 소스 요구, 공개적인 커뮤니티 압력을 함께 활용하려 한다.
- 이 사안은 코파일레프트가 자동으로 집행되는 장치가 아니라, 사용자와 권리자가 실제로 권리를 행사할 때 작동한다는 점을 부각한다.

**글: Jake Edge**
**2026년 8월 26일**
[FOSSY](https://lwn.net/Archives/ConferenceByYear/#2026-Free_and_Open_Source_Software_Yearly)

[FOSSY 2026](https://2026.fossy.ca/)에서, 이 컨퍼런스를 주최하는 [Software Freedom Conservancy](https://sfconservancy.org/)(SFC)의 여러 구성원은 [계속되고 있는 위반](https://sfconservancy.org/news/2026/may/18/bambu-studio-3d-printer-agpl-violation-response/)을 주제로 발표했다. Bradley Kühn, Karen Sandler, Denver Gingerich는 Bambu Lab의 3D 프린터 소프트웨어와 관련된 [Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.en.html)(AGPLv3) 위반의 서로 다른 측면, 그리고 사용자에게 대안을 제공하려는 노력에 관해 이야기했다. 특히 흥미로운 점은, 이 회사가 이용하는 우회 방식이 바로 AGPL이 방지하려고 만들어진 방식이라는 것이다.[^part1-p1-agpl]

[![Kühn, Sandler, & Gingerich](https://static.lwn.net/images/2026/fossy-kuhn-sandler-gingerich-sm.png)](https://lwn.net/Articles/1090402/)

Kühn은 자신이 자유·오픈소스 소프트웨어(FOSS) 커뮤니티에서 30년 넘게 활동해 왔으며, “이 역사적 순간에는 내가 경력 전체에서 본 것보다 더 많은 활동 기회가 있다”고 말하면서 세션을 시작했다. 과거에는 자신과 동료들이 온갖 종류의 재난을 분류하고 대응했지만, 지난 6~8개월 동안은 오히려 기회를 분류하고 있다고 한다. Sandler는 주어진 기회가 쉽지는 않다고 덧붙였다. “누가 ‘이 돈을 원하나요, 저 돈을 원하나요?’라고 묻는 상황은 아니니까요.”

Kühn이 말한 기회는 사실 돈에 관한 것이 아니라, “활동가가 일을 해내고 사람들을 참여시킬” 방법을 제공하는 것이라고 했다. 지난 약 6개월 동안 SFC는 FOSS를 어렴풋이만 알던 “완전히 하나의 열성 사용자 공동체”와 성공적으로 관계를 맺었다. 그 대상은 “자유 소프트웨어, 자유 문화, 자유로운 창작”이라는, 자유를 중심에 둔 수많은 주제였다. 이는 흥미진진하지만, Kühn은 이야기가 끝나는 지점부터 말해 버린 셈이므로 처음으로 돌아가고자 했다.

#### 배경

얼마 전 [3D 프린팅](https://en.wikipedia.org/wiki/3D_printing)이 발명되었고, Kühn은 이를 멀리서 지켜봤다. 학부생 시절 브레드보드에서 불이 난 경험 때문에 자신은 소프트웨어만 다루는 사람이 되어야겠다고 확신했다는 것이다. 그는 3D 프린팅 문화를 좋아하고 그 문화에서 나온 발표도 즐기지만, 직접 참여하지는 않는다. 다만 라이선스 위반을 조사하면서 Gingerich와 함께 3D 프린팅의 역사를 속성으로 배웠으며, Gingerich는 이미 상당한 배경지식을 갖고 있었다.

[![Bradley Kühn](https://static.lwn.net/images/2026/fossy-kuhn-sm.png)](https://lwn.net/Articles/1090403/)

Kühn은 자신이 배운 내용을 일부 들려주었다. 취미 3D 프린팅 분야는 처음에는 호기심의 대상이었다. 시장에는 조립 완료된 기기가 없었으므로 3D 프린터를 원하는 사람은 직접 만들어야 했다. 초기 프린터를 만든 사람들 중 일부는 훗날 3D 프린터를 판매하는 회사를 세웠고, 이것은 커뮤니티 발전의 핵심 요소가 되었다. Linux와 마찬가지로 3D 프린터는 취미로 시작했으며, “취미 문화가 벤처 자본가에게 즉시 말살되지 않을 만큼 충분히 오랫동안 취미로 남아 있었다”고 그는 말했다.

3D 프린팅의 “멋진 점”은 기기를 구동하는 데 필요한 소프트웨어를 개발하던 사람들이 자유 소프트웨어 커뮤니티를 참고하고, 자신의 코드에 어떤 라이선스를 붙일지 정하기 전에 “한 번 더 생각했다”는 데 있다고 한다. 이 장비를 사용하는 데 필요한 중요한 도구는 “[slicer](https://en.wikipedia.org/wiki/Slicer_(3D_printing))”라는 프로그램이다. 슬라이서는 3D 모델(일부 슬라이서는 이 모델 작성도 돕는다)을 얇은 2D 단면으로 나누고, 이를 프린터 하드웨어가 이해하는 언어로 변환한다. Kühn은 그 언어를 어셈블리 언어에 비유했다. 이는 지나친 단순화이지만, 그가 개념적 틀을 잡는 데 도움이 된다고 한다.[^part1-p1-slicer]

오랫동안 자유 소프트웨어를 지지해 온 Alessandro Ranellucci는 “[`Slic3r`](https://slic3r.org/about/)”라는 슬라이서를 만들었다. Kühn은 Ranellucci에 대한 유일한 불평은 이름을 그렇게 정한 것이라고 말했다. 발표에서 프로그램 이름과 프로그램 일반 유형을 구분하기 어려워지기 때문이다. 그래서 Kühn은 이를 구분하기 위해 “slicer with three”라는 표현을 썼다. 두 사람은 화상 통화를 했고, Ranellucci는 Bambu Lab 사태를 피하려고 Slic3r에 AGPLv3를 선택했다고 말했다. “내 가장 큰 걱정은 누군가가 ‘서비스형 Slic3r’를 만들 것이라는 점이어서, 이 모든 일을 예상했어요.”

Kühn에 따르면 다른 슬라이서를 사용하는 3D 프린터도 있지만, Slic3r의 어떤 포크와 함께 쓰는 것이 최선이 아닌 프린터를 찾기는 어렵다. 활성 포크는 약 18개이며 가장 잘 알려진 것은 [PrusaSlicer](https://www.prusa3d.com/p/prusaslicer/)다. 이것은 Ranellucci의 친구 Josef Prusa가 3D 프린팅을 단순한 사업 기회가 아니라 “자유 소프트웨어 *사업* 기회”로 보면서 생겨났다. Prusa는 프린터 도면, 자유 소프트웨어, 자유 펌웨어 등을 고객에게 제공하는 회사를 세웠고, 그 회사는 한동안 시장의 지배적 사업자였다고 Kühn은 말했다.

동시에 제조용 3D 프린터라는 병행 시장도 발전하고 있었다. 이 프린터들은 방 하나를 통째로 차지하고 수십만 달러의 가격표를 달고 있었다. 한편 500~3,000달러짜리 취미용 프린터는, 특히 그 가격대 상단에서 “정말, 정말, 정말 좋아지고” 있었다.

#### Bambu의 등장

이것이 2019년과 코로나19 이전인 2020년의 시장 상태였다. 코로나19 동안 많은 사람이 3D 프린팅을 포함한 취미를 시작했고, 이는 중국 기업 Bambu Lab을 이 시장으로 끌어들였다. Kühn은 이 회사가 중국 정부와 연계됐다는 소문은 있으나 확인된 바는 없다고 말했다. Bambu Lab은 처음부터 3D 프린터를 만들기로 했다. 2025년에는 분석 보고서에 따라 500~3,000달러 프린터 시장의 38~48%를 이 회사가 차지했다. 부분적으로는 방 크기의 산업용 프린터 시장이 쇠퇴하고, 고객들이 그런 장비를 Bambu Lab 같은 기업의 훨씬 저렴하고 우수하며 신뢰성 높은 프린터 군단으로 대체할 수 있음을 깨달았기 때문이다. 이 회사는 취미 시장과 함께 그 시장을 겨냥했고, 이것이 성공의 배경이다.

물론 Bambu Lab에도 슬라이서가 필요했다. 그래서 AGPLv3를 통해 얻을 수 있었던 수정판 PrusaSlicer를 Bambu Studio라는 이름으로 배포하기 시작했다. 하지만 소스 코드나 이를 제공하겠다는 제안은 배포하지 않았다. Kühn에 따르면 이는 2022년 또는 2023년까지 이어졌으며, 결국 3D 프린팅 커뮤니티의 압력으로 Bambu Lab은 소스를 공개해야 했다. 그러나 첫 공개가 흔히 그렇듯, 실제 대응 소스 코드(corresponding source code)는 아니었다.[^part1-p1-corresponding-source]

Kühn은 “코파일레프트 위반자의 기발함에는 웃음이 나올 수밖에 없다”고 말했다. 이들은 실제 판사가 중요하게 여기지 않을 만한 장치에 흔히 의존한다. 이 경우 Bambu Studio는 “조금 더 많은 것”을 내려받겠느냐는 요청을 띄우며, 전형적으로 “예” 또는 “나중에 묻기”를 선택하게 한다. 사용자는 결국 “예”를 눌러야 슬라이서 일부 기능이 작동한다는 사실을 알아낸다. 내려받는 추가물은 C++ 소스에서 빌드한 두 개의 `.so` 파일이다. 이 공유 라이브러리 파일은, 공개된 소스 코드의 [`dlopen()`](https://man7.org/linux/man-pages/man3/dlopen.3.html) 호출에서 명백히 볼 수 있듯이, 슬라이서에 동적으로 적재된다.[^part1-p1-dlopen]

Kühn은 Bambu Studio와 그 모든 구성 요소가 일반 GPLv3 아래에서는 결합 저작물(combined work)로 간주될 것이라고 말했다. 하지만 이 회사에는 AGPLv3의 제한에도 저촉되는 네트워크 기반 구성요소가 있다. 동적으로 적재되는 슬라이서 부분은 Bambu Lab 서버에서 실행되는 광범위한 3D 애플리케이션에 네트워크로 호출을 보내는 얇은 계층이다. 이것은 추가 기능에 서버에서 접근할 수 있게 하는 “키”, 즉 특정 [User-Agent](https://en.wikipedia.org/wiki/User-Agent_header) 문자열을 전달한다. 회사는 모든 클라이언트에서 동일한 이 User-Agent가 [DMCA](https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act)의 우회 방지 수단이라고 주장한다.[^part1-p1-user-agent]

하지만 Kühn은 그것이 바로 AGPLv3가 방지하려는 행위라고 말했다. “Affero GPL 애플리케이션의 일부를 웹 서버에 올려 둔 뒤 독점으로 유지할 수는 없습니다.” 폴란드의 3D 프린팅 사용자 Paweł Jarczak은 User-Agent 문자열과 네트워크 코드를 역공학했고, 그 결과 Bambu Lab으로부터 DMCA 삭제 통지를 받았다. “물론 GitHub는 Microsoft니까 그 통지를 따랐죠.” Jarczak은 자신의 슬라이서인 OrcaSlicer에서 여전히 그 코드를 유지하고 있다. 이 코드는 Bambu Lab의 AGPLv3 위반을 우회하는 것을 목표로 한 [baltobu 프로젝트](https://f.sfconservancy.org/baltobu)의 일부로서 [SFC 저장소](https://f.sfconservancy.org/baltobu/orca-slicer-for-bambu)에 미러링되고 있다.

[![Denver Gingerich](https://static.lwn.net/images/2026/fossy-gingerich-sm.png)](https://lwn.net/Articles/1090404/)

Gingerich는 Bambu Lab이 AGPLv3뿐 아니라 일부 3D 프린터 모델의 펌웨어에 쓰인 [Buildroot](https://buildroot.org/) 기반 Linux 및 기타 코파일레프트 구성요소의 소스를 제공하지 않아 GPLv2도 위반하고 있다고 지적했다. 그는 Bambu Lab 웹 사이트에서 300MB짜리 펌웨어 이미지를 내려받았지만, 소스나 이를 제공하겠다는 제안을 찾지 못했다.

그는 Bambu Lab이 대규모 벤처캐피털형 투자를 기업에 집행하는, 중국에서 형성 중인 실리콘밸리 영감의 문화에서 나왔다고 말했다. Bambu Lab은 자금력이 풍부했고, 그래서 여러 면에서 경쟁사를 앞지를 수 있었으며, 소셜 미디어 등을 통해 제품을 광범위하게 마케팅하고 Reddit 같은 포럼에서 자사 제품에 대한 메시지를 통제할 수 있었다. 이 회사는 “그 과정에서 코파일레프트 라이선스를 위반하는” 실리콘밸리 기업들이 택해 온 것과 같은 지름길 일부를 택했다.

Gingerich는 이 상황이 “라이선스가 부여한, 우리가 마땅히 받아야 할 통제권을 되찾을 매우 좋은 기회”를 제공한다고 본다. Bambu Lab은 투자금을 “처음부터 다시 구현하는 데” 쓸 수도 있었지만 그러지 않았다. 그 대신 “재현하려면 매우 오랜 시간이 걸리는” 고품질 자유·오픈소스 소프트웨어라는 큰 축적물을 이용했다.

Gingerich는 Bambu Lab이 사실상 이 위반에 대해 흔한 “그럼 우리를 고소하세요” 접근법을 택했다고 말했다. 물론 소송도 선택지다. 그러나 이런 문제를 바로잡는 여러 방식은 각기 걸리는 시간이 다르다. 커뮤니티가 역공학을 수행하고 독점 부분을 교체하도록 하는 일은 소송보다 훨씬 짧은 시간이 걸릴 가능성이 크다. Kühn은 위반 기업들이 실제로 “고소하세요”라고 말하지는 않으며, 대신 답변을 멈출 뿐이라고 덧붙였다.

#### 참여

[![Karen Sandler](https://static.lwn.net/images/2026/fossy-sandler-sm.png)](https://lwn.net/Articles/1090405/)

Sandler는 이 위반들이 특히 흥미로운 이유 중 하나는 SFC가 수년간 다룬 어떤 사안보다도 많은 신규 인원을 FOSS 커뮤니티로 끌어들였기 때문이라고 말했다. 코파일레프트나 FOSS라는 말을 거의 들어 본 적 없던 사람들도 이 일에 열광한다. 이제 그들은 “이 라이선스가 권리를 부여하며 우리가 그것으로 무언가를 할 수 있다”는 점을 깨닫고 있다. 보통 SFC가 이런 문제를 이야기할 때는 이 방에 있는 사람이나 세션 녹화 영상을 볼 사람들처럼 “범위가 좁은 사람들”에게 말하게 되며, 그 가능성을 설명하기도 어렵다고 그녀는 말했다. 그러나 3D 프린팅 커뮤니티는 실제로 이 일을 이어받아 전진시켰다. “여러 YouTuber가 깊이 있는 설명을 내놓고” Reddit 등의 댓글 작성자도 “와, 이것이 이 라이선스들이 의미하는 바구나. 더 많이 써야겠어!”라고 무척 흥분했다.

그러고도 청중 질문 시간이 10분 이상 남았다. 첫 질문은 “Bambu가 AGPL을 따르게 하려면 무엇이 필요합니까?”였다. Gingerich는 Walmart가 현재 소유한 Vizio를 상대로 한 [SFC의 소송](https://sfconservancy.org/copyleft-compliance/vizio.html)처럼, 여러 접근법이 있다고 답했다. 코파일레프트 라이선스는 계약이기도 하므로 그 소송은 계약법에 근거한다. Vizio/Walmart와 TV에 사용된 GPLv2 및 LGPLv2.1 코드를 만든 소프트웨어 개발자 사이에 계약이 존재하며, SFC와 Vizio TV를 구입한 사람은 모두 그 계약의 “제3자 수익자(third-party beneficiaries)”다. SFC는 그 계약이 요구하는 권리를 얻기 위해 소송을 제기하고 있다.

Kühn은 이렇게 계약을 집행하는 일은 표준적인 관행이지만, 자신들이 아는 한 GPL 계열 계약에는 아직 사용되지 않았다고 말했다. 더 전통적인 집행 경로는 코드의 저작권자로서 소송을 제기하는 것이며, SFC가 과거에 했던 방식이기도 하다. “지식재산” 조항이 있는 여러 무역협정을 수단으로 사용하는 방법 등 다른 메커니즘도 있다. 지식재산 규칙이 불쾌하게 느껴질 수는 있어도, 이는 코파일레프트 본래의 의도와 일치한다. 즉 “그런 규칙을 무엇이든 가져와 뒤집고, 소프트웨어 자유를 지키는 데 쓰는 것”이다.[^part1-p1-copyleft]

3D 프린팅 활동과 함께 SFC는 모금 행사를 열었다. Kühn에 따르면 이 행사는 설정했던 25만 달러라는 높은 목표를 [크게 초과했다](https://sfconservancy.org/news/2026/jul/16/software-right-to-repair-baltobu-fundraiser-succes/). “아마 절대 달성하지 못할 목표라고 생각했던 수치”였다. Sandler는 “그 돈으로 실제로 중요한 일을 해낼 수 있겠다고 생각한 숫자를 골랐을 뿐”이며, 도달하지 못할 가능성도 컸다고 말했다. “그 목표를 훌쩍 넘겼고, 기부금 대부분은 아주 작은 금액이었습니다.” 이는 고무적인 일이었다. Kühn은 이제 SFC가 전임 소송 변호사를 고용할 수 있게 되었다며, 참석자들에게 이 사실을 널리 알려 달라고 권했다.

Sandler는 많은 사람이 GPL 라이선스를 “마법의 요정 가루”처럼 생각한다고 말했다. 라이선스를 선택하기만 하면 모두가 따르고 문제가 해결될 것이라는 생각이다. 참석자들의 강한 고개 젓기에서 알 수 있듯, 이는 명백히 사실이 아니다. “누구도 상대를 강하게 추궁하지 않고, ‘잠깐, 실제로 이걸 하고 있지 않잖아요’라고 말하지 않으면 누구도 결코 그렇게 하지 않을 겁니다.”

그녀는 집행을 추구하는 방법은 여러 가지이며 창의성이 필요하다고 말했다. SFC는 “기업이 올바른 일을 하게 만드는 여러 경로”를 보여 주려 한다. 또한 모든 사람이 자신이 사는 모든 기기에 대해 완전한 대응 소스 코드를 요구해야 한다고 권한다. 그러면 그러한 권리에 대한 소비자 수요가 있음을 보여 줄 수 있다. 소스 코드가 공개되지 않았을 때 불만을 담은 YouTube 영상이나 Reddit 스레드를 올리는 것 역시 집행의 한 형태가 될 수 있다.

또 다른 질문은 소송이 집행에 효과적인 도구인지에 관한 것이었다. Gingerich는 Linksys를 상대로 한 집행 조치에서 나온 소스 공개가 [OpenWrt 프로젝트](https://openwrt.org/)의 첫 커밋이었다고 지적했다. 이는 “기업이 원하는 대로가 아니라 우리가 원하는 대로 기기가 작동하도록, 기기를 통제하는 데 도움을 주는” 프로젝트들로 이어진다.

또한 기업 사내 변호사들은 소송 덕분에 자신의 일이 훨씬 쉬워진다며 Sandler에게 정기적으로 감사한다고 한다. 라이선스 위반에 아무런 결과가 없다면, 기업 변호사는 준수를 보장하기 어렵다. 기업의 사업 부문은 라이선스 위반 비용이 무엇인지 알고 싶어 하지만, “소송이 없으면 그 답은 없습니다.”

마지막 질문은 라이선스 위반의 근본 원인을 고치는 일에 관한 것이었고, 이는 여러 방식으로 해석될 수 있다. Kühn은 전 세계 사회 부패를 고치는 일은 벅찬 과제라고 말했고, Sandler는 자본주의를 고치는 일도 마찬가지라고 덧붙였다. Gingerich는 근본 문제는 권력 불균형이며, FOSS와 더 큰 수리할 권리(right-to-repair) 운동이 바로 그것에 맞서고 있다고 말했다. Sandler는 더 나은 세상을 만드는 방식으로 근본 원인을 겨냥하는 것이 이 운동들의 목표라고 말하며 마무리했다. 제품, 기술, 법률을 개선하고, 적극적으로 참여하며, 비기술 인력도 이 문제에 이해관계를 갖도록 돕는 일이 필요하다. 물론 그것 역시 대단히 벅찬 과제처럼 보인다.

> [FOSSY 참석을 위해 밴쿠버를 방문하는 데 도움을 준 LWN의 여행 후원사 Linux Foundation에 감사드린다.]

[댓글 (27개 게시됨)](https://lwn.net/Articles/1089390/#Comments)

[^part1-p1-agpl]: **AGPLv3**는 네트워크를 통해 소프트웨어 기능을 제공하는 경우에도, 상호작용하는 사용자가 해당 프로그램의 대응 소스 코드에 접근할 기회를 받아야 한다고 요구하는 코파일레프트 라이선스다. 일반 GPL의 이른바 “ASP/SaaS 허점”을 보완하려는 목적에서 만들어졌다.
[^part1-p1-slicer]: 3D 프린팅의 **슬라이서**는 3D 형상을 각 층의 인쇄 경로로 변환해 보통 G-code 계열의 명령을 생성한다. 생성된 명령에는 이동, 압출, 온도, 속도 등의 제어 정보가 담긴다.
[^part1-p1-corresponding-source]: GPL 계열에서 말하는 **완전한 대응 소스 코드**는 단순히 일부 소스 파일을 공개하는 것을 넘어, 배포한 바이너리를 수정·빌드·설치하는 데 필요한 소스, 스크립트, 제어 파일을 포함해야 한다는 개념이다. 구체적 의무 적용은 해당 라이선스와 배포 방식에 따라 달라진다.
[^part1-p1-dlopen]: `dlopen()`은 POSIX 계열 시스템에서 실행 중인 프로세스가 공유 객체(`.so`)를 동적으로 불러오게 하는 API다. 별도 다운로드한 라이브러리를 이 방식으로 적재하더라도, 라이선스상 결합 저작물인지 여부가 자동으로 해소되는 것은 아니다.
[^part1-p1-user-agent]: **User-Agent**는 HTTP 요청에 클라이언트 종류를 나타내기 위해 실리는 헤더다. 모든 클라이언트에 동일한 값을 사용하는 문자열은 보안 비밀이라기보다 식별자에 가깝고, 역공학이나 접근 제한 논쟁의 대상이 될 수 있다.
[^part1-p1-copyleft]: **코파일레프트**는 저작권을 이용해 수령자에게 사용·수정·배포의 자유를 부여하면서, 파생 저작물이나 배포 시에도 일정한 자유와 소스 제공 의무가 유지되도록 하는 라이선스 설계 방식이다.

---

### [OpenMDW 라이선스를 검토하며](https://lwn.net/Articles/1089251/)

#### 요약

- OpenMDW는 모델, 데이터, 가중치, 소프트웨어와 문서를 하나의 허용적 라이선스로 배포하려는 시도다.
- 모델 출력에는 제한을 부과하지 않지만, 권리 정리와 실사 책임을 사용자에게 크게 전가한다.
- 특허뿐 아니라 저작권 침해 소송에도 적용되는 권리 종료 조항이 핵심 논쟁거리다.
- 비관련 모델·코드까지 이용 권리를 잃게 할 수 있고, 침해를 입증하려 모델에 접근해야 하는 원고를 막을 수 있다는 비판이 나왔다.
- OSI가 현 형태를 승인할 가능성은 낮아 보이지만, 어떤 수정안이 합의를 이룰지는 아직 불분명하다.

*Jonathan Corbet, 2026년 8월 21일*

오픈소스 세계는 수년 동안 대규모 언어 모델(LLM)과 그에 적용되는 라이선스에 어떻게 접근할지를 이해하려 애써 왔다. 수치 가중치로 채워진 블랙박스에 대해 “자유”란 무엇일까? Open Source Initiative(OSI)가 [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition)을 [개발](https://lwn.net/Articles/995159/)한 과정은, 그 결과물만큼이나 좋게 말해도 논쟁적이었다. 이제 Linux Foundation의 Mike Dolan이 [승인을 위해 새 라이선스를 OSI에 제출](https://lwn.net/ml/all/CAFV=PSG=bsLTemzjyCKYYz9j=rX9dcNo6=2T6htbxTRgervMrA@mail.gmail.com)했다. 이름은 OpenMDW(“Open Model, Data, and Weights”)이며, LLM 및 관련 자료의 배포 라이선스를 명확히 하려 한다. 하지만 이 라이선스 역시 합의를 이끌어 내기 어려운 것으로 드러나고 있다.

Dolan이 설명한 이 새 라이선스의 동기는 모델 배포물이 소프트웨어, 모델 가중치, 문서 등 여러 종류의 아티팩트를 한데 묶는다는 점이다. 기존 라이선스는 소프트웨어에 초점을 맞추며 다른 유형의 아티팩트를 염두에 두고 만들어지지 않았고, 모델의 출력 문제도 전혀 다루지 않는 경향이 있다. OpenMDW는 오픈 모델 배포자가 모든 것을 단일 라이선스 아래에 둘 수 있게 하려는 시도다. [2025년 블로그 게시물](https://lfaidata.foundation/blog/2025/07/22/simplifying-ai-model-licensing-with-openmdw/)은 이전 버전의 라이선스가 나온 동기를 더 자세히 설명한다.

그 핵심에서 OpenMDW는 MIT 라이선스와 비슷한 허용적 라이선스다. 다만 몇 가지 차이가 있다. 모델이 만들어 낸 어떤 출력물에도 이 라이선스가 어떠한 제한도 부과하지 않는다고 명시한 조항이 있다. 또한 보통의 자유 소프트웨어 라이선스보다 더 넓은 범위를 포괄하여, 모델 배포물로 표현되는 “모든 저작권, 특허, 데이터베이스 및 영업비밀 권리”에 대한 이용을 허가한다. 그러나 실제로 허가되는 권리가 무엇을 포괄하는지는 다소 모호하다. 대문자로 쓰인 면책 조항은 배포자가 그와 관련해 아무 보증도 제공하지 않음을 분명히 한다. 실제로 사용자가 모델을 정말 이용할 수 있는지 판단할 책임은 사용자에게 넘어간다.

> 귀하는 (1) 모델 자료 또는 그 이용에 적용될 수 있는 타인의 권리(모델 자료에 포함되거나 구현된 저작권 또는 기타 권리를 제한 없이 포함함)를 정리할 책임, (2) 모델 자료를 이용하는 데 필요한 모든 동의, 허가 또는 기타 권리를 획득할 책임, 또는 (3) 모델 자료나 그에 포함되거나 구현된 모든 것에 관한 실사 또는 그 밖의 조사를 수행할 책임을 전적으로 부담합니다.

Pamela Chestek은 이 문구에 [의문을 제기](https://lwn.net/ml/all/3c71c6bf-1020-49cf-8892-1db26824da16@chesteklegal.com)하며, 그러한 권리 정리는 “일반적으로도 불가능하며, 특히 학습 자료가 무엇인지조차 공개되지 않는다면 더욱 그렇다”고 말했다. 또한 이 문구는 라이선스 제공자가 부과하는 요건으로 읽힐 수 있다고 했다. 즉 누군가 이 모델의 이용과 관련한 저작권 침해로 소송을 당하면, 그 문제에 더해 애초 모델 이용을 허용한 라이선스를 위반했다는 주장까지 받을 수 있다는 것이다.

그러나 가장 큰 관심을 끈 부분은 다음 권리 종료 조항이다.

> 모델 자료가 직접 또는 간접적으로 특허 또는 저작권을 침해한다고 주장하여, 귀하가 어떤 개인이나 법인에 대해 소송을 제기·유지하거나 자발적으로 소송에 참여하면, 여기에 따라 귀하에게 부여된 모든 권리와 허가는 종료됩니다. 다만 그 소송이 먼저 귀하를 상대로 제기된 상응하는 소송에 대응한 것이라면 예외입니다.

Richard Fontana는 특허권과 저작권을 모두 포괄하는 이 조항의 광범위함을 [우려했다](https://lwn.net/ml/all/CAC1cPGxE=ozAmGTfHt4k+SePQcstym_Kaq=w4Aj5_=hvkp15hA@mail.gmail.com). 그가 말한 대로 종료는 분쟁 중인 특정 자료보다 훨씬 더 많은 것에 영향을 줄 수 있다.

> 이 라이선스는 종료를 저작권 소송까지 확대할 뿐 아니라, 겉보기에는 무관한 자료까지 포괄해 종료 범위를 넓힌다. 예를 들어 OpenMDW-1.1 라이선스 모델이 내 저작권을 침해한다고 믿는다고 하자. 내가 모델 라이선스 제공자를 고소하면, 모델과 함께 (어떤 의미에서는) 배포된 일부 Python 코드에 대한 내 저작권 및 특허권은 이제 종료된다.

같은 소프트웨어 기반에서 사용하도록 만들어진 모델 가중치 배포물이 여럿 존재하는 일은 드물지 않다. 저작권자가 특정 가중치 집합에 관한 소송을 제기하면, 다른 모든 모델과 이를 실행하는 데 쓰이는 소프트웨어까지 접근 권한을 잃을 수 있다. Fontana는 이와 같이 무관한 자료에 대한 라이선스가 종료되는 일이, 비관련 소프트웨어에 대한 제한을 금지하는 [Open Source Definition](https://opensource.org/osd)의 9절을 위반할 수 있다고 [덧붙였다](https://lwn.net/ml/all/CAC1cPGwJChNvKCjdWh8r1ZWp+B9fNzpKokM-qkTJxxZmzXEtVg@mail.gmail.com). 일반적으로 그는 계약에 따라 제공되는 자료를 가리키려는 “Model Materials”라는 용어가 잘 정의되어 있지 않다는 우려를 표했다.

Rob Landley는 제3자가 OpenMDW 라이선스 프로젝트를 포크해 일부 독점 코드를 넣었을 때, 그 코드의 소유자가 소송을 제기하면 원래 프로젝트에 대한 접근 권한을 잃게 되는지 [물었다](https://lwn.net/ml/all/c850f40f-e7f6-4a68-8316-af7096da04a8@landley.net). 한편 Kevin Fleming은 다른 잠재적 문제를 [지적했다](https://lwn.net/ml/all/75c8a40c-2c0a-4f11-8b3d-f1f50159910d@app.fastmail.com). 모델 학습에 어떤 데이터가 쓰였는지는 (일반적으로) 알 수 없으므로, 저작권 자료가 포함되었는지 판단하는 유일한 방법은 모델을 실제로 실행해 보는 것이다. 저작권자가 침해를 이유로 소송을 제기하면, 소송을 뒷받침할 증거를 만들기 위해 필요한 바로 그 모델에 대한 접근 권한을 잃게 된다. Simon Phipps는 간단히 “저작권 청구를 했다는 이유로 자유 0을 철회하는 라이선스는 소프트웨어 자유를 보장할 수 없다”고 [말했다](https://lwn.net/ml/all/CAA4ffp9timUaUij8-3+60EM80R3oFZCeNbwk2vr5pVFE6BsCNQ@mail.gmail.com).

Dolan은 종료 조항은 라이선스에 대칭성을 부여하기 위한 것이며, 어떤 배포물이 침해한다고 주장하면서 동시에 그 배포물이 제공하는 이용 권리를 누릴 수 있어서는 안 된다고 [응답했다](https://lwn.net/ml/all/CAFV=PSH_wNaPuPQi5i6-JZP2wfyx5UpudQsrjao3TCCSE4jb9w@mail.gmail.com). 그러나 모델 발행자의 법적 위치는 대부분의 소프트웨어 발행자와 다르고, 따라서 종료 조항에 저작권을 넣는 일이 필요하다고 했다.

> 모델은 방대한 기존 저작물 집합으로부터 만들어지며, 모델 발행자의 법적 노출은 바로 여기에서 발생한다. 그 발행자들이 실제로 마주하는 주장은 라이선스된 자료 자체가 침해한다는 것이고, 그러한 침해 청구는 특허법이 아니라 저작권법 아래에서 제기될 가능성이 크다. 이 맥락에서 특허만을 대상으로 한 조항은 Apache-2.0의 형식은 복제하면서 기능은 포기하는 것이 될 것이다. 즉 대칭성이 없게 된다.

Eric Schultz는 종료 문구가 법원의 판단에 따라 “모델 제작자가 저지른 대규모 저작권 침해에 대한 사면”이 된다고 [답했다](https://lwn.net/ml/all/oWTGZeIzdfCvuuaXBlcpfybXR9fCMSgvPqEZojho4cMtsrPCEJib46YjJbJE2P1Knil3M2P3hAogWR9kZWNLojwiJW9IfxO4W1O00_8LzLE=@wwahammy.com). Fontana는 이 사건에서 문제가 된 모델 가중치에만 종료를 한정하자고 [제안했다](https://lwn.net/ml/all/CAC1cPGxeqtcZmH-n8tkLcoWeA7_KfK13s=GRx+Z8zS+K4-C8MQ@mail.gmail.com/). Chestek은 라이선스가 대칭적이지 않다고 [말했다](https://lwn.net/ml/all/3b86330d-5746-4856-8d8f-a498594eceb1@chesteklegal.com/). 모델 제작자는 자신이 저작권 자료를 복제했는지 알 수 있지만, 수령자는 자신의 저작권이 침해되었는지 사전에 알지 못한 채 저작권 청구권을 포기해야 하기 때문이다.

논의는 명확한 결론 없이 잦아들었다. OSI가 현재 형태의 라이선스를 승인할 준비가 되어 있지 않은 듯하지만, 어떤 변경이 이를 더 수용 가능하게 만들지는 구체화되지 않았고, 라이선스 지지자들이 그런 변경을 받아들이지도 않았다.

결국 OpenMDW 라이선스는 어떤 의미에서든 “공개된” 모델의 배포와 연관된 위험을 줄이는 데 목적을 두는 것으로 보인다. 배포자는 모델 학습에 내재하거나 출력에서 명시적으로 드러나는 저작권 또는 특허권 침해로 제소될 가능성을 최소화하고자 이 라이선스를 채택할 것이다. 일반적인 자유 소프트웨어 라이선스는 그 적용 대상 소프트웨어 자체에 저작권 문제가 없음을 확인하라고 사용자에게 훈계하지 않는다. OpenMDW를 사용하면 배포자의 위험은 줄일 수 있겠지만, LLM을 *이용*하는 일 자체가 여전히 상당히 위험할 수 있음을 분명히 한다.

[댓글 (6개 게시됨)](https://lwn.net/Articles/1089251/#Comments)

### [양자 컴퓨팅으로부터 안전해지는 방법](https://lwn.net/Articles/1088305/)

#### 요약

- 양자 컴퓨터는 RSA·타원곡선 암호의 기반인 인수분해와 이산로그 문제를 위협하므로, 공개키 암호의 전환이 필요하다.
- 웹 TLS에서는 브라우저가 X25519MLKEM768을 기본 지원하며, 서버는 OpenSSL 3.5 이상 또는 배포판 정책으로 이를 활성화할 수 있다.
- 새 알고리즘의 장기 검증 부족을 완화하기 위해 기존 타원곡선 암호와 ML-KEM을 함께 쓰는 하이브리드 방식이 기본 선택으로 자리 잡고 있다.
- OpenPGP 진영은 LibrePGP와 IETF OpenPGP의 호환성 분열 때문에 당분간 고전·양자내성 키의 이중 서명이 현실적인 우회책이다.
- 지금의 실무 과제는 암호 전환을 시작하고, 양자 위조가 가능해지는 시점을 지속적으로 주시하는 것이다.

*Daroc Alden, 2026년 8월 24일*

실용적인 양자 컴퓨터는 지난 수십 년 동안 늘 “10년 뒤에” 등장할 것처럼 보였다. 그러나 이제는 불과 몇 년 안에 가능해질 듯 보이기 시작했다. 최근의 [결과가 난독화된 연구](https://lwn.net/Articles/1066156/)는 양자 컴퓨터에서 [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) 키를 인수분해하는 데 필요한 메모리 요구량이 훨씬 낮음을 보였으며, [공개적으로 수행된 다른 연구자들의 작업](https://www.ecdsa.fail/)은 2023년 최첨단 수준과 비교해 메모리 사용량을 절반 이상 줄였다. 동시에 컴퓨터 제조업체들은 더 오랜 시간 유효한 중첩 상태를 유지하는 양자 프로세서를 [자랑하고 있다](https://abit.ee/en/processors/ibm-quantum-processor-nighthawk-ibm-miami-quantum-computing-qubits-coherence-heron-r3-quantum-advant-en). 소프트웨어 업데이트가 안정판 시스템에 반영되기까지 매우 오래 걸린다는 점을 고려하면, 지금 양자 컴퓨터로부터 안전해지기 위해 필요한 설정 변경과 프로토콜 업데이트를 살펴볼 만하다.

#### 위협은 무엇인가?

양자 컴퓨터는 일반적으로 고전 컴퓨터보다 빠른 것은 아니다. (일부 암호 응용에 중요한 [일반 블랙박스 함수의 역산](https://en.wikipedia.org/wiki/Grover%27s_algorithm)은 더 빨리 할 수 있다.) 대신 정수 인수분해처럼 고전 컴퓨터에서는 어렵다고 여겨지는 특정 문제를 양자 컴퓨터는 더 효율적으로 풀 수 있다. 불행히도 현대의 암호 인프라 상당 부분은 바로 이 문제들의 어려움에 의존한다.

현대 암호학은 일반적으로 대칭키 암호와 비대칭키 암호라는 두 영역으로 나뉜다. 전자는 관련된 모든 당사자가 공유 비밀을 보유하는 데 의존하며, 양자 컴퓨터의 분석에 취약한 것으로 여겨지지 않는다. 문제는 처음에 공유 비밀을 얻는 일이다. 사용자는 보통 여러 웹 사이트에 연결하고 여러 사람과 이메일을 교환하고 싶어 한다. 그 각각과 공유 비밀을 수립하는 일은 어렵다.

여기서 비대칭키 암호(공개키 암호라고도 함)가 등장한다. 이는 공유 비밀 없이 동작하는 암호 프로토콜이다. 대신 참여자는 전 세계에 알려진 공개키와 자신만 알고 있는 개인키를 갖는다. 한 키로 암호화하면 다른 키로만 복호화할 수 있다. 암호 서명은 알려진 값을 개인키로 암호화하여, 서명을 만든 사람이 그 키를 가지고 있었음을 증명하는 방식으로 동작한다. 이 암호계의 보안은 본질적으로 공개키만으로는 풀기 어렵지만 추가 비밀 정보에 접근하면 쉽게 풀리는 문제가 존재한다는 데 달려 있다.

원래의 공개키 암호계는 [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem)로, 큰 수를 인수분해하기 어렵다는 성질에 의존한다. 과학계는 이 작업을 양자 컴퓨터에서 이론적으로 빠르게 할 수 있음을 알고 있다. 뒤이어 RSA는 더 작은 키를 사용하는, 밀접하게 연관된 [이산로그 문제](https://en.wikipedia.org/wiki/Discrete_logarithm)에 의존하는 [타원곡선 암호](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)로 일부 대체되었다.

현재 공개적으로 이용 가능한 최고 수준의 양자 프로세서는 물리 [큐비트](https://en.wikipedia.org/wiki/Qubit) 1,121개를 제공한다. IBM이 공개한 [양자 컴퓨팅 로드맵](https://www.ibm.com/roadmaps/quantum/2026/)은 물리 큐비트 1,386개인 Kookaburra 프로세서를 2026년 말까지 완성하겠다고 약속한다. IBM이 과장하고 있다 해도, 최근 몇 달 사이 ECDSA 키를 인수분해하는 데 알려진 최적 양자 회로의 요구량은 논리 큐비트 1,425개에서 1,154개로 줄었다. 그러나 물리 큐비트와 논리 큐비트 사이에는 차이가 있다. 가장 잘 격리된 양자 컴퓨터도 환경 잡음의 영향을 받으며, 이는 컴퓨터 큐비트 값에 오류를 더한다. 이 오류는 교정하거나 보상해야 한다. 현재 알려진 최선의 양자 오류 정정 기법은 합리적인 충실도로 논리 큐비트 하나를 에뮬레이션하는 데 물리 큐비트 약 500개가 필요하다. 이 수는 알고리즘의 추가 돌파구와 더 나은 물리 칩 모두에 따라 낮아질 것이다.[^part2-p2-logical-qubits]

이 추세에 영감을 받아 암호학자들은 수년 동안 양자 컴퓨터에서 효율적 해법이 알려지지 않은 문제에 기반한 다른 공개키 암호계를 연구해 왔다. 최근에는 일반 용도로 충분히 견고하다고 여겨지는 소수의 암호계를 선택하고 [표준화했다](https://lwn.net/Articles/973231/).

따라서 오픈소스 공동체가 마주한 과제는 공개키 암호화와 서명이 쓰이는 모든 곳에 이 새 암호계를 배포하는 일이다. 이 둘 중 암호화가 더 시급하다. 오늘 암호화되는 것은 내일 공격받을 수 있지만, 오늘 검증한 서명은 신뢰할 수 있다. 양자 위조는 미래에 일어날 것이기 때문이다. 그래도 결국 두 용도 모두 해결해야 하며, 공개키 암호는 놀랄 만큼 많은 곳에 등장한다.

새로 발명된 양자내성 암호계에는 아직 오랜 사용 이력이 없다는 점도 작은 난점이다. 암호학자들은 그것들이 안전하다고 믿지만, 고전 또는 양자 컴퓨터가 이를 깨뜨릴 결함이 발견될 수도 있다. 곧장 포스트양자 암호로 옮겨가도 해가 없을 가능성이 높지만, 보수적 접근은 하이브리드 방식을 쓰는 것이다. 잘 알려진 타원곡선 암호계와 새 포스트양자 암호계 양쪽으로 데이터를 암호화한다. 두 암호 방식 중 하나라도 안전하게 남는 한 전체 구성은 안전하다. 따라서 웹 브라우저, [OpenPGP](https://www.openpgp.org/) 구현체 및 다른 암호화 소프트웨어가 향하는 암호화 방식은 NIST가 표준화한 포스트양자 암호화 방식 ML-KEM-768과 오늘 널리 쓰이는 타원곡선 암호계 X25519를 조합한 것이다.[^part2-p2-hybrid] 여러 정부 기관은 [비하이브리드 암호화 방식의 사용 허용을 요구](https://lwn.net/Articles/1048978/)했으나, 현재로서는 대부분 소프트웨어가 X25519MLKEM768을 기본값으로 삼는 듯하다.

#### 웹 브라우징

현대 세계에서 공개키 암호의 가장 큰 용도는 아마 웹 브라우징일 것이다. 다행히 모든 주요 브라우저는 이제 포스트양자 암호를 사용해 TLS 연결을 암호화하는 것을 지원한다. Firefox 132(2024년 10월 출시), Google Chrome 131(2024년 11월 출시), Safari 26(2025년 9월 출시)부터 기본으로 활성화되어 있다. 세 브라우저 모두 X25519MLKEM768 키 교환 메커니즘을 지원한다.

더 어려운 일은 이 키 교환 메커니즘을 웹 서버에 배포하는 것이다. [Apache HTTP Server](https://httpd.apache.org/)와 [NGINX](https://nginx.org/en/) 같은 대부분의 웹 서버는 암호 관리 기능을 [OpenSSL](https://www.openssl.org/)에 위임한다. OpenSSL은 2025년 4월 출시된 [3.5.0 버전부터](https://openssl-library.org/news/openssl-3.5-notes/) 포스트양자 키 교환 메커니즘을 지원한다. 이전 OpenSSL 버전에 묶인 사용자는 [Open Quantum Safe 프로젝트](https://openquantumsafe.org/)의 [oqs-provider 라이브러리](https://github.com/open-quantum-safe/oqs-provider#oqsprovider---open-quantum-safe-provider-for-openssl-v3)를 이용해 새 암호군 지원을 추가할 수 있다. OpenSSL에 의존하는 웹 서버는 보통 OpenSSL의 [`SSL_CONF_cmd()`](https://docs.openssl.org/master/man3/SSL_CONF_cmd/#ssl_conf_cmd) 함수로 설정 옵션을 전달하는 방법을 제공한다. 그런 재정의가 없으면 OpenSSL은 [`openssl.cnf` 설정 파일](https://docs.openssl.org/3.6/man5/config/)에 지정된 설정을 기본으로 사용한다.

Red Hat 계열 배포판과 openSUSE에서는 이 설정 파일을 crypto-policies 메커니즘이 생성한다. 사용자는 `/etc/crypto-policies`에 정책을 추가한 뒤 [`update-crypto-policies`](https://manpages.opensuse.org/Tumbleweed/crypto-policies-scripts/update-crypto-policies.8.en.html)로 OpenSSL 설정 파일을 다시 생성한다. 이 작업은 [LibreSSL](https://www.libressl.org/) 같은 다른 암호 라이브러리와, [OpenSSH](https://www.openssh.org/)처럼 자체 암호 형식을 처리하는 일부 소프트웨어의 설정도 갱신한다. Fedora 43 및 Red Hat Enterprise Linux 10.1 이후 릴리스는 포스트양자 암호를 우선하도록 기본 설정될 예정이다. 그보다 오래된 릴리스에서는 백포트된 기본 정책을 설정하거나, 적절한 정책 모듈의 `Groups` 지시어를 수동으로 편집해야 한다.

```
# 정책 이름은 배포판과 버전에 따라 다를 수 있다.
update-crypto-policies --set DEFAULT:PQ
```

Debian, Ubuntu, Arch Linux 등에서는 사용자가 `openssl.cnf`를 직접 편집한다. Debian과 Ubuntu에는 crypto-policies 포트가 모두 있지만 기본으로 활성화되어 있지 않다. 이 배포판에서 다른 암호 라이브러리를 쓰는 사용자는 해당 설정도 갱신해야 할 수 있다. 현재 어떤 배포판도 설정 파일에서 포스트양자 암호를 우선하도록 기본 설정하지는 않는다. 다만 충분히 새 OpenSSL 버전을 설치한 경우, 이를 우선하는 OpenSSL 자체 기본값을 사용하게 될 수 있다.

[Caddy](https://caddyserver.com/)처럼 배포판 OpenSSL 라이브러리에 의존하지 않고 내장 라이브러리를 쓰는 웹 서버도 있다. Caddy의 경우 Go 1.24 이상으로 빌드되면 포스트양자 암호가 기본 활성화된다.

전반적으로 웹 서버에서 포스트양자 암호 지원을 활성화하는 가장 안전한 방법은 `SSL_CONF_cmd()`에 전달하는 지원 `Groups`를 명시적으로 설정해 `X25519MLKEM768`을 포함하는 것이다. 하지만 이는 개별 웹 서버에만 영향을 미치며, 더 나은 포스트양자 암호계가 발견되면 낡은 설정이 될 수 있다. 시스템 전역 수준으로 정책을 설정하면 OpenSSL의 다른 용도까지 포괄하지만 똑같은 갱신 문제가 있다. OpenSSL 자체 기본값에 의존하면 늘 최신 암호군 중 하나를 사용하게 되지만, 배포판의 변경된 기본 설정이 이를 조용히 재정의하기는 쉽다.

#### OpenPGP

웹 브라우징이 암호화를 사용하는 가장 흔한 활동일 수 있지만, 디지털 서명은 현대 Linux 시스템의 보안에 더 중요하다고 볼 수 있다. 패키지에는 보통 배포판 패키지 저장소에서 실제로 온 것임을 보장하는 OpenPGP 서명이 따라온다. 개별 Git 커밋이나 태그에도 신뢰할 수 있는 개인이 만들었음을 표시하기 위해 서명할 수 있다. 많은 키의 수명이 수년에 이른다는 점을 고려하면, 어떤 위조가 가능해지기 훨씬 전부터 포스트양자 서명으로 옮기기 시작하는 것이 현명할 수 있다.

불행히도 OpenPGP 생태계는 [2023년부터](https://lwn.net/Articles/953797/) 둘로 나뉘었다. Linux 배포판에서 널리 쓰이는 [GNU Privacy Guard](https://gnupg.org/)(GPG)는 [LibrePGP](https://librepgp.org/)라는 명세를 따르기 시작한 반면, 여러 다른 도구는 IETF가 표준화한 OpenPGP를 계속 따랐다. 두 표준은 포스트양자 암호 구현 방법에 의견이 다르므로, 한 도구 집합으로 만든 서명을 다른 도구로 검증하는 일은 다소 고통스럽다.

OpenPGP의 접근법은 [RFC 9980](https://www.rfc-editor.org/info/rfc9980/)(“OpenPGP의 포스트양자 암호”)에 규정되어 있다. 이 RFC는 새 알고리즘 일곱 가지를 추가하며, 그중 네 가지는 하이브리드 알고리즘이다. 암호화에는 웹 브라우저 권장 기본값과 일치하는 X25519와 조합한 ML-KEM-768, 또는 키와 서명이 다소 더 크지만 더 나은 보안을 제공할 수 있는 X448과 조합한 ML-KEM-1024를 허용한다. 서명에는 같은 기반 알고리즘을 쓰지만, 서명에 최적화한 이름과 매개변수 선택이 부여된다. ML-KEM-768의 보안 수준에 해당하는 ML-DSA-65와 Ed25519, 또는 ML-KEM-1024의 보안 수준에 해당하는 ML-DSA-87과 Ed448을 사용할 수 있다.

RFC는 이 키들을 [RFC 9580](https://www.rfc-editor.org/info/rfc9580/)(“OpenPGP”)에서 명시한 새 v6 키 형식으로 인코딩할 것을 요구하지만, GPG는 이를 지원하지 않는다. RFC 9980이 허용하는 예외가 하나 있다. 구현체는 대개 인식하지 못하는 알고리즘을 가진 PGP 서브키를 건너뛰므로, 포스트양자 서브키를 가진 v4 OpenPGP 키를 만들 수 있게 한다. 버전 4 키는 GPG와 호환되므로, GPG가 관련 서명 알고리즘 지원을 추가하게 된다면 상호운용성을 위한 가장 신중한 선택일 수 있다.

GPG는 포스트양자 키를 암호화에만 사용하는 것을 지원하며, 별도의 서명 키 알고리즘은 없다. 그러한 암호화 키를 만들 때 GPG는 같은 기반 암호화 알고리즘(ML-KEM 및 선택한 타원곡선)을 사용하지만, 키를 저장하고 사용자의 신원 정보에 결합하는 방식은 호환되지 않는다. 구체적으로 ML-KEM은 정적인 프로토콜 정보 집합을 키 유도 함수에 섞어, 두 장치가 서로의 키를 이해할 수 있도록 동일 프로토콜을 사용한다고 확인하는 방법을 정의한다. GPG는 IETF 표준이 지정한 것과 다른 정적 정보 집합을 쓴다. [Sequoia](https://sequoia-pgp.org/)와 다른 OpenPGP 구현체는 GPG의 네이티브 포스트양자 키를 이해할 수 없으며, 그 반대도 마찬가지다.[^part2-p2-openpgp-split]

[RNP](https://www.rnpgp.org/)처럼 Thunderbird의 이메일 암호화를 구동하는 OpenPGP 엔진을 비롯한 일부 암호화 소프트웨어는 GPG의 LibrePGP 키 형식을 쓰지만, 포스트양자 v4 서브키를 이해하는 데는 예외를 둔다. 상황을 더 혼란스럽게 만드는 점은 Sequoia가 GPG 명령줄 인터페이스를 구현하는 “GPG 카멜레온”을 제공한다는 것이다. 따라서 `gpg`를 실행하는 사용자가 실제로는 Sequoia와 대화하고 있을 수도 있다.

실무적으로 가장 간단한 우회책은 별도의 PGP 키 두 개를 만드는 것이다. 하나는 고전적 서명 알고리즘을 사용하고, 하나는 RFC 9980 서명 알고리즘을 사용한 뒤, 모든 것에 두 키로 모두 서명한다. 이것은 Red Hat이 패키지 서명에 사용해 온 방식이며, 서명자가 별개의 PGP 신원 두 개를 관리해야 한다는 비용을 제외하면 동작한다. 이론적으로는 포스트양자 서브키를 가진 v4 PGP 키를 사용할 수 있지만, 형식의 제약 때문에 서명이 아니라 암호화에만 쓸 수 있다.

자신의 서명이 양자내성을 갖도록 하고 싶은 사용자는 Sequoia로 전환하는 것(인터페이스를 그대로 유지하려면 카멜레온을 사용할 수도 있다), v4 고전 서명 키를 생성하거나 기존 키를 재사용하는 것, v6 포스트양자 서명 키를 생성하는 것, 두 키가 서로를 보증하도록 하는 것, 그리고 중요한 모든 것에 두 키로 서명하는 것을 고려해야 한다. 이는 분명 이상적이지 않다. 정말 긴급해지기 전에 더 나은 해결책이 나타나기를 바랄 수밖에 없다.

현재로서는 이런 이중 서명을 검증하는 일은 간단하다. 둘 중 어느 한 서명이라도 유효하다면 아마 신뢰할 수 있다. 하지만 양자 컴퓨터로 RSA 및 타원곡선 서명 일부를 위조할 수 있게 되면, 서명을 소비하는 쪽은 포스트양자 서명만 검증하거나, 고전적 서명이 그런 양자 컴퓨터가 등장하기 전에 만들어졌음을 보장하는 일종의 인증서 투명성 메커니즘을 사용해야 한다.

#### 유일한 진짜 해결책

물론 어떤 종류의 암호 공격이든, 아무리 강력하더라도 완전한 보호를 제공하는 선택지는 하나 있다. 포기하고 숲으로 들어가 사는 것이다. 그 선택지가 없는 우리에게는 OpenSSL과 선택한 OpenPGP 소프트웨어를 적절히 설정하는 것으로 충분하기를 바라고, 양자 공격이 가능해지는 전환점을 계속 주시하는 수밖에 없다.

[댓글 (29개 게시됨)](https://lwn.net/Articles/1088305/#Comments)

[^part2-p2-logical-qubits]: **물리 큐비트와 논리 큐비트**: 물리 큐비트는 실제 하드웨어 소자이고, 논리 큐비트는 오류 정정 부호로 다수의 물리 큐비트를 묶어 더 안정적으로 보이게 만든 계산 단위다. 따라서 두 수량을 직접 비교하면 안 된다.
[^part2-p2-hybrid]: **하이브리드 키 교환**: 두 독립적인 키 교환·암호 체계를 결합해, 둘 중 하나가 훼손되어도 보안을 유지하려는 전환 전략이다. 여기서 X25519MLKEM768은 X25519와 ML-KEM-768을 결합한 명칭이다.
[^part2-p2-openpgp-split]: **상호운용성 문제**: 같은 ML-KEM 알고리즘을 써도 키의 인코딩과 키 유도 함수에 넣는 도메인 분리 정보가 다르면, 구현체는 키 자료를 같은 프로토콜의 것으로 해석하지 못할 수 있다.

---

### [7.3 병합 윈도우의 시작](https://lwn.net/Articles/1089244/)


#### 요약
- 이 항목은 **[7.3 병합 윈도우의 시작](https://lwn.net/Articles/1089244/)** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

작성: **Jonathan Corbet**, August 20, 2026

#### 요약

- 7.3 병합 윈도우 초반만으로도 2,346개의 비-병합 변경 집합이 mainline으로 병합되었고, 8월 30일 종료 전 추가 유입량이 예상된다.
- 아키텍처별로 `nolibc` 기반 Alpha 지원, PowerPC Rust 지원, ARM 32-bit 단계적 폐지 등 큰 축의 변경이 진행되었다.
- 그룹 스케줄링의 CPU 가중치 계산이 `cgroup_mode` 튜닝으로 재설계되어, 기본 동작이 기존 방식과 달라진다.
- 파일시스템 쪽에서는 오래된 EFS/FreeVxFS 제거와 `failfs`, `fchdir()/fchroot()` 관련 변경으로 보안/격리 사용성이 강화된다.
- 내부 커널 계층에서는 iomap 재작성, 커널 스레드 nullfs 분리, `libcrypto`/Rust 지원 확대 등 기반 인프라 업데이트가 진행되었다.

이 문서 기준으로 7.3 커널 릴리스의 mainline 저장소에는 이미 2,346건의 비병합(non-merge) 변경 집합이 병합되었다. 앞으로 병합 윈도우가 마무리되기 전 유입될 변경량에 비하면 시작 단계의 선결제에 불과하지만, 초기부터 이미 눈에 띄는 변경들이 들어왔다. 핵심은 멀티프로세서에서의 그룹 스케줄링 방식이 크게 손질되었다는 점이다.[^part34-linux-sched]
7.3 병합 윈도우 초반에 들어온 2,346건의 비-병합 변경 집합은 시작 단계치고는 방대한 편이며, 전체 유입량이 본격적으로 시작되기 전의 시금석으로 볼 수 있다. 이 시기에 들어온 핵심 변경으로는 멀티프로세서에서의 그룹 스케줄링 동작 재설계가 특히 크다.[^part34-linux-sched]

7.3 병합 윈도우 초반부의 가장 주목할 변경 사항은 다음과 같다.

#### 아키텍처별

- 알파(Alpha) 아키텍처가 `nolibc` 라이브러리 지원을 받기 시작했다. (`nolibc`(minimal C library)는 정적/임베디드 성격의 작은 런타임 요구 환경에서 커널 사용자 공간 실행 파일 구동을 단순화한다.)[^part34-nolibc]
- 일부 32비트 Arm CPU 지원이 deprecated(비권장) 처리되었다. 자세한 내용은 [해당 병합 메시지](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=809177dbf32e) 참조. 해당 시스템은 최소 7.3 릴리스(장기 지원 대상 예정)까지는 유지되나 이후 제거될 수 있다.[^part34-arm32]
- PowerPC 시스템에 Rust 지원이 추가되었다.
- x86의 “SMP alternatives” 코드는 삭제되었다. 과거에는 단일 CPU(UP) 부팅 시 멀티프로세서용 잠금(locking) 명령어를 패치해서 뗐지만, 단일 CPU 환경이 급격히 줄어들면서 유지 비용 대비 이득이 적어져 제거되었다.[^part34-smp-alt]

#### 코어 커널

- 커널의 [binfmt_misc](https://docs.kernel.org/admin-guide/binfmt-misc.html) 메커니즘(실행 파일 인터프리터 지정 메커니즘)이 대폭 확장되었다([내용](https://lwn.net/Articles/1086947/)). 이제 BPF 훅으로 실행 시점에서 사용할 인터프리터를 결정할 수 있어 hermetic(결과 재현성이 보장되는) 바이너리 같은 용도로 확장성이 높아졌다.[^part34-binfmt]
- 그룹 스케줄링 사용 시 CPU 시간 배분 방식에 미묘하지만 중요한 변경이 있었다. 기존에는 작업(task)의 가중치가 해당 cgroup이 특정 CPU에서 동시에 실행되는 비율에 맞춰 축소되었다. 예를 들어 네 개의 동일 가중치 task 중 한 개가 CPU 0에서 실행 중이라면 그 task 가중치가 1/4로 축소되는 식이다. 이 방식은 CPU 간 부하 불균형을 완화하려는 장치이지만 대규모 시스템에서 매우 작은 배율이 발생하며 정수 오버플로/정밀도 이슈와 경쟁 관계 왜곡으로 이어질 수 있다.[^part34-sched]

현재 커널에서의 과도한 스케일링 문제가 커널 스케줄링 메인테이너 Peter Zijlstra의 재설계를 거쳐 `cgroup_mode`라는 튜닝 knob로 바뀌었다. 이는 여러 모드 가운데 선택해 사용할 수 있고 지금은 `debugfs`에 존재한다.[^part34-cgroup-mode] 추후 필요시 `sysfs`로 옮겨질 수도 있다.

`pre-7.3` 동작은 `cgroup_mode = smp`로 설정해 얻을 수 있다.

새로 추가된 [`up` 모드](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=80ad6d3338eb)는 스케일링을 끄고 단일 CPU 정책처럼 동작한다. 다만 Zijlstra는 “uniprocessor 정책을 가정해 SMP 분배를 잘못 잡는다”며 기본값으로 보기 어렵다고 언급했다.

[`max` 모드](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=90ac22ffef48)는 각 task이 이론적으로 동시에 동시 실행된다고 보고 사용 가능 CPU 수만큼 스케일링한다. 수치적 안정성은 개선되지만, 경쟁이 낮은 구간에서 가중치가 과도하게 커지는 단점이 있다.

[`concur` 모드](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=5c0b58bd1c9f)는 CPU 수와 실행 가능한 task 수 중 작은 값을 사용해 조정한다. Zijlstra는 low contention에서는 `smp`처럼 동작하다가 runnable task 수가 CPU 수에 가까워질수록 `max`에 수렴한다고 설명했다.

마지막으로 [`tasks` 모드](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=507f910a4e1f)는 runnable task 수만 보고 조정한다. “완전히 유효하고 동작 가능하지만, 기존의 전통적 의미와는 꽤 다르다”는 한마디가 붙어 있다.

새로운 knob의 기본값은 `concur`이어서 7.3에서는 과거 커널과 스케줄링 동작이 달라진다. [변경 로그](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=fb1050ac8e40)는 “설정 가능성이 있으니 기본값을 바꾸어 더 넓은 사용자층이 이익을 보길 기대한다”라고 적고 있다.

이 시리즈의 마지막은 cgroup을 위한 [single run queue](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=85570f10a4c6)로의 전환이다. 스케줄러 오버헤드를 줄이고 지연시간 문제 일부를 해소하려는 큰 내부 재구현이다.[^part34-runq]

- 새 sysctl 항목으로 `syscall_user_dispatch`가 생겼다. 이 값은 x86에서 한 프로세스가 다른 프로세스의 시스템 콜을 가로챌 수 있게 해 주는 [system-call user dispatch](https://docs.kernel.org/admin-guide/syscall-user-dispatch.html) 기능 활성/비활성 여부를 제어한다. 기본은 활성화이다.[^part34-dispatch]

#### 파일시스템 및 블록 I/O

- SGI 초기 파일시스템인 [EFS(Extent File System)](http://aeschi.ch.eu.org/efs)는 제거되었다. 수십 년간 유의미한 유지보수가 없어 사실상 쓰임이 없던 것으로 보인다. 동시에 SCO UnixWare에서 쓰이던 FreeVxFS 지원도 제거되었다.
- 새 `failfs` 파일시스템이 추가되어, 그 안에서 수행되는 모든 동작은 실패하게 된다. 병합 로그에서는 “작업은 파일시스템 상태를 완전히 벗어날 수 있다”는 문구가 나온다.[^part34-failfs] 절대경로, 절대 심볼릭 링크, `AT_FDCWD` 상대 lookup은 모두 실패한다.
- `failfs` 루트에 들어간 프로세스는 이미 열려 있는 파일 디스크립터를 기준으로만 파일을 열 수 있다. 자세한 내용은 [문서](https://docs.kernel.org/next/filesystems/failfs.html).
- `fchdir()` 시스템콜이 새 특수 파일 디스크립터 값 `FD_FAILFS_ROOT`를 받아서 작업 디렉터리를 failfs 루트로 이동할 수 있다.[^part34-failfs-api]
- 새 `fchroot()` 시스템콜은 기존 `chroot()`의 fd 기반 버전이다. 전달한 fd가 `FD_FAILFS_ROOT`이면 failfs 루트로 이동한다.
- [overlayfs](https://docs.kernel.org/filesystems/overlayfs.html)가 [id-mapped mounts](https://lwn.net/Articles/837566/)를 지원한다.[^part34-overlayfs]
- 커널이 단일 블록 디바이스에서 복수 파일시스템을 마운트하는 지원이 더 좋아졌다. 이는 [EROFS](https://docs.kernel.org/filesystems/erofs.html)가 이미 제공하던 기능과 맞닿는다.[^part34-erofs]

#### 하드웨어 지원

- **하드웨어 모니터링**: Apple SoC 전원 상태 관리자(power-state managers).
- **기타**: Qualcomm Peripheral Authentication Service TEE 인터페이스.

#### 네트워킹

- 새 kfunc `bpf_sock_read_xattr()`는 BPF 프로그램이 소켓 inode에서 `user.*` 확장 속성을 읽을 수 있게 한다. 문서가 거의 없어, 상세 내용은 [changelog](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b4e124d16855) 확인이 필요하다.[^part34-bpf]

#### 내부 커널 변경

- [iomap](https://docs.kernel.org/filesystems/iomap/index.html) 계층이 대대적으로 손봤다. 기존에 `iomap_begin()`/`iomap_end()` 콜백을 제공하던 방식 대신 파일시스템은 `iomap_next()` 한 가지 API로 매핑을 순회한다. 이에 따라 직전의 iomap 정리 글은 일부 낡아졌다.[^part34-iomap]
- 커널 스레드는 더 이상 사용자 공간과 파일시스템 상태를 공유하지 않고 자체 nullfs에 위치한다.[^part34-nullfs]
- 커널 [내부 cryptographic library](https://lwn.net/Articles/1077427/)가 여러 AES 암호화 모드 지원을 받게 되었다. 상세는 [merge message](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=d47db9bf50d2) 및 [libcrypto 문서](https://origin.kernel.org/doc/html/next/crypto/libcrypto.html).
- Rust 지원은 꾸준히 개선되어 모듈 소유권 추상화, 무손실 정수 변환 모듈, 포인터 값 난독화 로깅(주소 누출 방지), pin-init 개선 등이 추가되었다. 또 `synchronize_rcu()`, memory barriers, 인터럽트 enable/disable, interrupt-disabled spinlock 등도 지원 강화가 이어졌다.[^part34-rust]

현재도 linux-next에는 12,640개의 non-merge changeset이 남아 있으며, 이는 8월 30일 병합 윈도우 마감 전에 mainline으로 거의 대부분 유입될 예정이다. 이어지는 기사에서는 그 시기 이후 변경분을 다룰 예정이다.[^part34-next]

[(16개 댓글 보기)](https://lwn.net/Articles/1089244/#Comments)

### [Remind를 이용한 명령줄 캘린더](https://lwn.net/Articles/1090376/)


#### 요약
- 이 항목은 **[Remind를 이용한 명령줄 캘린더](https://lwn.net/Articles/1090376/)** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

작성: **Joe Brockmeier**, August 25, 2026

#### 요약

- `Remind`는 텍스트 기반으로 동작하는 강력한 달력/알람 도구로, 특수 규칙이 많은 일정이나 예외 처리를 유연하게 다룬다.
- 반복 규칙(`REM`, `OMIT`, `TODO`, `UNTIL` 등)과 쉘 명령 실행(`RUN`)이 결합되며, CLI 중심 사용자에게 높은 표현력을 제공한다.
- `TkRemind`와 같은 GUI를 함께 사용할 수 있지만 핵심은 순수 텍스트 스크립트 기반이며, 협업/공유 일정 동기화가 필요한 조직용은 부적합하다.
- 보안·격리 이슈를 피하려는 정교한 일정 관리/알림 설계 관점에서 유용하다.[^part34-remind]
- `-c`, `-cu`, `-ppp` 등 출력 형식 옵션과 `rem2html/rem2pdf/rem2...` 유틸리티 생태계 덕분에 문서화/백업 파이프라인 연계가 쉽다.[^part34-pipeline]

[Remind](https://dianne.skoll.ca/projects/remind/)는 명령줄용 캘린더 및 알람 프로그램으로, Linux 및 Unix 계열에서 동작한다. 선택적으로 Tk 기반 GUI(`TkRemind`)도 제공한다. 자체 스크립트 언어가 있어 다른 달력 프로그램으로는 표현이 어려운 알림 규칙을 만들 수 있다. 다만 기업 환경에서 달력 공유·회의 초대 교환이 필요한 워크플로에는 부적합하지만, CLI와 빠른 유연성 기반의 혼잡한 일정 관리에는 오히려 잘 맞는다.[^part34-remind]

#### 공룡시대 달력 문화

Remind 저자 Dianne Skoll의 책 [The Book of Remind](https://dianne.skoll.ca/projects/remind/download-book.php)에 따르면 첫 번째 버전은 1989년 말, 즉 “공룡시대의 컴퓨팅” 시절에 만들어졌다. Skoll은 1990년 Usenet 접근권을 얻은 뒤 `comp.sources.misc`에 소스 코드를 공개했다. 그녀는 스스로 “달력 소프트웨어에 대한 비정상적인 집착”이라고 한 관심을 2005~2007년의 짧은 공백 기간을 제외하고 계속 유지했다.[^part34-history]

Remind는 GPLv2 하에서 배포되는 여러 프로그램의 모음이다. 핵심은 `remind` 명령어이고, GUI 프론트엔드인 `tkremind`, 출력물을 출력 가능한 캘린더로 변환하는 Rem2HTML/Rem2PDF 같은 보조 유틸이 있다.[^part34-remind-components]

모든 프로그램은 C로 작성되었고 의존성은 최소화되어 있다. `TkRemind`는 Tcl/Tk와 표준 Tcl 라이브러리(tcllib)가 필요하고, Rem2HTML/Rem2PDF는 Perl 모듈이 더 필요하다.[^part34-deps]

Git 이력상 Skoll는 1996년 이전의 Git 이전 커밋까지 보유한 거의 1인 프로젝트로, 외부 기여는 13개 커밋뿐이었다.
공식 저장소는 [Forgejo 인스턴스](https://git.skoll.ca/Skollsoft-Public/Remind)에 있으며(아이디/비번 `notabot` 필요), [Codeberg](https://codeberg.org/dskoll/remind#remind)와 [Debian Salsa](https://salsa.debian.org/dskoll/remind#remind)에도 미러가 있다.

Remind는 주요 Linux 배포판 저장소에 들어 있지만, Arch Linux 패키지는 TkRemind에 필요한 `tcllib` 의존성이 빠져 있다. Arch 사용자는 AUR(Arch User Repository)에서 받아오거나 직접 빌드해야 한다.[^part34-arch]

#### Remind 스크립트

`Remind`는 이름이 중요한 프로그램이 아니라, reminder 스크립트라고 부르는 텍스트 파일을 읽어 알림을 표준 출력으로 내보낸다. TkRemind는 기본 파일명을 `~/.reminders`로 가정하므로, 예제에서도 이 규칙을 사용한다.

Remind의 날짜 지정 언어는 단순 일정에서는 직관적이면서도, GUI 캘린더에서 처리하기 어려운 규칙을 표현할 수 있다. `remind` 실행 시 현재 시각을 기준으로 스크립트를 해석해, 트리거가 맞는 항목을 출력한다(자세한 설명은 [man 페이지의 trigger computation 파트](https://linux.die.net/man/1/remind#:~:text=DETAILS%20ABOUT%20TRIGGER%20COMPUTATION,-Here)).

간단한 예시는 아래와 같다.

```text
REM Friday MSG Send Mr. Spacely the weekly TPS report.
REM 21 Aug 2026 AT 17:00 MSG Dinner at Blue Mountain Pizza in %1.
```

알림은 `REM`으로 시작하고 다음에 트리거 시점을 적는다. 이어서 메시지 부분이 온다. 요일 하나만 쓰면 매주 해당 요일, 특정 날짜(`21 Aug 2026`)는 그 날만 트리거한다. 날짜 입력 형식도 관대해서, 동일 시점에서 `Aug 21`, `21 Aug`, `August 21 2026`, `2026-08-26` 등을 같은 의미로 해석한다. 너무 먼 미래 일정은 습관적으로 연도를 넣는 편이 안전하다.[^part34-dateparse]

`MSG` 뒤 텍스트가 실제 출력 메시지이다. 예제의 `%1`은 대체 필터로, 현재 시점 기준 남은 시간을 넣어준다.

```text
$ remind .reminders
Reminders for Friday, 21st August, 2026 (today):

Send Mr. Spacely the weekly TPS report.

Dinner at Blue Mountain Pizza in 6 hours and 41 minutes from now.
```

금요일이 휴일/휴가라면 TPS 리포트 발송 시점을 앞당기거나 늦추거나 건너뛸 필요가 있다. Remind는 이를 `OMIT` + `AFTER`/`BEFORE`/`SKIP` 조합으로 지원한다.

```text
OMIT 25 December
REM Friday SKIP MSG Send Mr. Spacely the weekly TPS report.
```

`OMIT`은 전역적(글로벌)이므로 `SKIP` 키워드가 붙은 모든 `REM` 항목에 영향이 간다.[^part34-omit]

`RUN` 명령으로 알림 동작 자체를 실제 shell 명령 실행으로 확장할 수 있다. 아래는 매주 금요일 한 번만 백업 스크립트를 실행한다.

```text
REM Friday ONCE RUN ~/bin/backup.sh
```

`remind`는 reminder 스크립트의 마지막 접근 시간을 확인해 마지막 실행 시점 판정에 사용한다. 즉, 하루 중간에 파일이 수정되면 “오늘은 실행한 것으로 간주하지 않음”이 된다. `remind -r`은 `RUN` 명령 재실행을 방지한다.[^part34-run]

Remind는 작업 관리(task manager)가 아니라 이벤트 리마인더이지만 `TODO` 키워드로 마감일 전/후 알림도 가능하다.

```text
REM TODO ++7 COMPLETE-THROUGH 24 Aug 2026 MAX-OVERDUE 3 MSG Big report due %b.
```

`++7`은 만기일 7일 전부터 트리거를 시작한다. 생략일은 기본적으로 포함되므로 제외하려면 `+7`을 사용한다. 이 예는 만기 7일 전~3일 후 알림을 발생시키며 `MAX-OVERDUE`가 없으면 만기 이후 매일 계속 알림이 생긴다. `%b`는 현재 날짜와 트리거 날짜의 일수 차이이다.[^part34-todo]

정기적으로 특정 날짜까지 반복되는 일정을 만들고 싶으면 `UNTIL`을 쓴다.

```text
REM Jun 3 2026 *7 UNTIL Sep 1 2026 MSG Art class in the park.
```

Remind 언어는 변수, 자료형, 연산자, 내장/사용자 함수까지 갖춘 작은 스크립트 언어다. Easter, 히브리력 날짜, 월령, 일출/일몰 계산 함수도 있다. 아래 예시는 [Remind wiki](https://dianne.skoll.ca/wiki/Remind_Cookbook)에서 가져온 것으로, 매일 일출/일몰/차기 보름달 시간 출력이다.

```text
SET $LongDeg 71
SET $LongMin 10
SET $LongSec 30
SET $LatDeg 42
SET $LatMin 20
SET $LatSec 27
MSG Sunrise at [sunrise(trigdate())], Sunset at [sunset(trigdate())], \
next full moon at [moontime(2)] on [moondate(2)]%
```

`moon.rem`로 저장한 결과:

```text
$ remind moon.rem
Reminders for Friday, 21st August, 2026 (today):

Sunrise at 06:53, Sunset at 20:10, next full moon at 00:19 on 2026-08-28
```

이 스크립트는 사용자 위치를 위도/경도로 정의하고 그 값으로 일출/일몰/보름달 시각을 계산한다. `trigdate()`는 계산된 트리거 날짜, 이 예시에서는 8월 21일을 반환한다.[^part34-astronomy]

`remind` man 페이지와 Skoll의 책에 문법이 상세히 정리되어 있다. 단발성 일정, 반복 일정, 휴일 예외, 이벤트 의존 트리거, 드물게 한 번만 발생하는 이벤트까지 다루기 쉬운 것이 핵심이다.[^part34-examples]

`remind`는 실행 모드가 여러 개다. 기본은 agenda 모드로, 그날/지금 기준 알림을 출력한다. 월 단위 뷰는 `remind -c <filename>`가 터미널 ASCII 달력을 출력하고, `-cu`는 유니코드 상자 문자로 가독성이 더 낫다.

주 수를 임의 지정하려면 `+N`을 붙인다. 예: `remind -c+2 <filename>`는 2주 달력 출력.
또한 `-ppp`로 JSON 출력이 가능해 다른 도구와 연계하기 쉬우며, 예를 들어 `remind -ppp filename | rem2pdf > calendar.PDF`로 `rem2pdf`를 통해 PDF 캘린더를 만들 수 있다.[^part34-pipeline]

#### 헬퍼 도구 찾아보기

Remind는 CLI에 익숙하고 텍스트 편집을 좋아하는 사용자에게 특히 어울린다. 다만 TkRemind은 클릭 중심 사용자에게 쓸만한 GUI를 제공한다. 아래처럼 “Add Reminder…”에서 유연한 입력을 지원한다.

> ![TkRemind 인터페이스](https://static.lwn.net/images/2026/tkremind.png)

CLI 유틸과 TkRemind을 배타적으로 쓸 필요는 없다. 다만 TkRemind이 만든 항목은 수동 편집하지 않는 것이 좋다. TkRemind은 `TAG` 항목을 넣어 다른 도구에서 수정하면 예측 불가능한 동작이 날 수 있음을 표시한다.
`remind`를 `-p` 옵션으로 실행하면 이 태그는 보조 프로그램(TkRemind 등)에 전달된다. 그렇지 않으면 `TAG`는 무시된다.[^part34-tag]

또한 시간이 지나면서 Remind용 3rd-party helper가 다수 생겼다. 프로젝트 웹사이트에는 iCalendar 변환기, CalDAV 동기화 도구, Emacs major mode(`remind-calendar.el`), PHP 웹 프런트엔드 등 수많은 예제가 있다.[^part34-helpers]

Skoll의 책과 man 페이지 외에도, 사용자 토론용 [메일링 리스트](https://dianne.skoll.ca/mailman/listinfo/remind-fans)와 OFTC의 IRC 채널 `#remind`가 있다.[^part34-community]

[(16개 댓글 보기)](https://lwn.net/Articles/1090376/#Comments)

[^part34-linux-sched]: Linux 스케줄링은 멀티태스킹 환경에서 각 task가 CPU 시간을 받는 방식(가중치, 런큐 우선순위, 그룹 정책)을 정의하는 핵심 서브시스템이다. 병합 초반부터 정책이 바뀌면 운영 부하 분배 특성이 바뀌므로 실서비스 성능 특성 점검이 필요하다.
[^part34-nolibc]: `nolibc`는 glibc 같은 큰 런타임 라이브러리 없이 가장 작은 라이브러리 세트로 사용자 공간 바이너리를 구동하기 위한 설계다. 커널 통합 테스트나 임베디드 이미지 크기 최적화에서 의미가 크다.
[^part34-arm32]: 32-bit ARM 축소는 장기 지원 범위를 정리해 관리비를 줄이는 방향과 맞닿는다. 임베디드·레거시 디바이스 운영자는 지원 종료 시점 대비 마이그레이션 계획이 필요하다.
[^part34-smp-alt]: x86 SMP alternatives 제거는 단일 CPU 마이너시트에서의 이득이 줄어들면서 보수 비용을 줄인 조치다. 과거 부팅 패치 경로가 사라져 코드 경로 단순화 및 유지보수 난이도 감소 효과가 있다.
[^part34-binfmt]: 실행 파일 해석기를 BPF로 동적으로 선택하면 보안 정책(격리/정책 기반 런타임)과 배포 재현성(hermetic build/run) 관점에서 새로운 적용 가능성이 열린다.
[^part34-sched]: `cgroup_mode`는 cgroup CPU fairness를 조절하는 실질적 정책 스위치다. 컨테이너/멀티테넌트 워크로드에서 latency와 fairness를 트레이드오프하기 위한 운영 상 수단이 된다.
[^part34-cgroup-mode]: `debugfs`는 주로 디버깅 전용 제어면으로 사용되며, 운영 안정성 면에서 sysfs로의 이전은 보안/인터페이스 안정성 관점에서 의미가 크다.
[^part34-runq]: single run queue로의 전환은 cgroup 스케줄러 경로를 단순화해 스케줄러 오버헤드 하락과 지연시간 개선을 기대하게 만든다.
[^part34-dispatch]: `syscall_user_dispatch`는 시스템 콜 인터셉션을 가능하게 하므로 sandboxing, tracing, 보안 감시 도구에서 잠재적으로 중요한 제어 포인트가 된다.
[^part34-failfs]: `failfs`는 테스트/보안 목적의 “결정적으로 실패하는 루트” 개념으로, 파일시스템 상태를 제한해 의도치 않은 파일 조작 경로를 차단한다.
[^part34-failfs-api]: `fchdir()/fchroot()`의 fd 기반 전환은 실행 컨텍스트를 명시적으로 제어하는 데 쓰여 컨테이너/격리 시나리오에서 상태 전환을 단순화한다.
[^part34-overlayfs]: id-mapped mount는 사용자/그룹 매핑이 다른 레이어 간 권한 위임 시 유연성을 높인다.
[^part34-erofs]: 단일 블록 디바이스에서 복수 FS를 마운트하는 능력은 멀티테넌시/시스템 통합 시 파티션 설계 단순화에 기여한다.
[^part34-bpf]: 네트워크/보안 도메인에서 socket inode 메타데이터를 읽는 확장 속성 접근은 정책 엔진 연계에 활용도가 높다.
[^part34-iomap]: iomap은 블록 기반 파일시스템의 핵심 매핑 레이어다. 단일 인터페이스 재정의는 드라이버/커널 코드 안정성 영향이 크므로, 하위 저장소 코드도 함께 재검토가 필요하다.
[^part34-nullfs]: 커널 스레드 전용 nullfs는 사용자 공간과 상태 분리를 강화해, 공격 표면이나 오류 전파 경로를 줄이는 방향이다.
[^part34-rust]: Rust 개선은 커널 코드의 메모리 안전성과 유지보수성에 영향을 준다. 다만 ABI/API 변화와 기존 C 모듈 호환 이슈를 병행 점검해야 한다.
[^part34-next]: linux-next는 최종 병합 전 staging 브랜치다. 여기 남은 변경집합은 출시 전 성능/회귀 위험을 먼저 흡수한다.
[^part34-remind]: Remind는 기존 GUI 중심 캘린더가 잘 다루지 못한 정교한 반복/예외 규칙을 CLI로 제공한다.
[^part34-pipeline]: `rem2html`/`rem2pdf`는 자동 리포팅, 공유 문서화, 백업 파이프라인과의 연계를 쉽게 해준다.
[^part34-history]: 1인 개발이지만 30년 이상 이어진 오픈소스 유지보수는 문서와 문맥을 따라야 재현성과 사용자 적응률이 확보된다.
[^part34-remind-components]: 구성요소 분리는 기능별 최소 의존성 원칙으로, 도구 체인 운영의 모듈화를 돕는다.
[^part34-deps]: 의존성 경량화는 설치/이식성에 유리하고 보안 업데이트 범위를 줄인다.
[^part34-arch]: 패키지 메타데이터와 실제 의존성 불일치는 운영 롤아웃 실패의 대표적 원인이라 주의가 필요하다.
[^part34-dateparse]: 날짜 파서 관용은 사용자 실수 허용성은 높이지만, 규칙이 많은 환경에서는 예외 규칙/타임존/연도 생략 규칙을 점검해야 한다.
[^part34-omit]: `OMIT`은 전역 규칙이라 예기치 않게 광범위하게 적용될 수 있다. 운영 규칙에 따라 누락된 예외를 점검하는 습관이 필요하다.
[^part34-run]: `RUN`은 일정 트리거를 작업 자동화로 연결해 cron-like 동작을 대체할 수 있으나, 중복 실행 제어가 정책상 핵심이다.
[^part34-todo]: 만기일 기반 reminder는 할일 관리의 기능과 경계가 겹치므로, 실제 할일 시스템과 충돌하지 않게 용도 분리를 권장한다.
[^part34-astronomy]: 천문/일출일몰 계산은 위치 기반 데이터 정확도(좌표, 타임존, DST)에 의존한다. 값의 출처가 바뀌면 스케줄의 신뢰도가 달라진다.
[^part34-examples]: “한 번 발생/반복/예외/의존 이벤트”를 동시에 다루는 점이 CLI 기반 자동화에서 강점이 된다.
[^part34-tag]: `TAG`는 다른 도구와 협업할 때 메타데이터 충돌을 줄이기 위한 신호다.
[^part34-helpers]: 외부 helper 생태계는 API 변화 대비를 분산시켜준다. 반대로 신뢰할 수 없는 helper는 보안 검증이 추가적으로 요구된다.
[^part34-community]: 소규모 도구일수록 메일링 리스트와 공개 커뮤니티가 실제 사용성·버그 축적에 결정적이다.

---

### [Quickshell 데스크톱 컴포넌트 툴킷 살펴보기](https://lwn.net/Articles/1083090/)


#### 요약
- 이 항목은 **[Quickshell 데스크톱 컴포넌트 툴킷 살펴보기](https://lwn.net/Articles/1083090/)** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

작성: **Tyler Langlois**, August 20, 2026

#### 요약

- Quickshell은 QML 기반 데스크톱 위젯/컴포넌트를 빠르게 만들기 위한 고수준 툴킷이다.
- Qt 기반 선언형 UI를 사용해 복잡한 데스크톱 셸/바/런처를 적은 코드로 구성할 수 있다.
- PipeWire·Bluetooth·네트워크 타입이 추상화되어 미니멀 WM 환경에서 실용성이 높다.

[Quickshell](https://quickshell.org/)은 툴바나 메뉴 같은 데스크톱 컴포넌트를 만드는 툴킷이다. `QML`은 GUI 애플리케이션 선언형 언어로, 개발 생산성 중심의 그래픽 도구를 만들도록 돕는다. 그 결과, Sway나 niri 같은 최소 창 관리자 환경에서 사용자 데스크톱 구성요소를 꽤 쉽게 구현할 수 있다.[^part56-qs-intro]

#### A high-level toolkit

Quickshell은 시스템 트레이, 오디오 장치 관리 인터페이스 같은 데스크톱 구성요소 UI를 쉽게 만들려는 요구에서 출발했다.[^part56-qs-quick]
기존 툴킷도 유사 기능을 만들 수 있지만, 학습 곡선과 컴파일 단계 비용이 크다. Quickshell은 저장소 기반 반복 편집으로 바로 반영되는 흐름을 제공해 데스크톱 유틸리티(런처·툴바 등)를 빠르게 만들 수 있게 한다.[^part56-qs-quick]

작성자 `outfoxxed`는 기존 대안인 [Elkowar's Wacky Widgets](https://github.com/elkowar/eww#eww) 사용 시 제약을 느끼고, Qt Quick의 반응형 바인딩을 활용한 접근을 택했다.[^part56-qs-reactive]
`Qt`는 Linux 데스크톱에서 GUI 컴포넌트를 직접 다루기에 강하지만, Quickshell은 상위 추상화를 통해 반복 개발 속도를 높인다.[^part56-qs-quick]

`Qt`와 `GTK` 둘 다 Linux에서 GUI 작성에 널리 쓰이지만, 보통은 낮은 수준 코드와 컴파일 단계가 요구된다.[^part56-qs-runtime]
Quickshell은 Qt API와 데스크톱 API 사이의 간극을 줄이고, 반복 빌드 속도를 개선한다.[^part56-qs-runtime]
실행 시 Quickshell 설치만으로도 문서화된 타입(`PopupWindow`, `SystemTray`)을 QML에 바로 사용할 수 있다.[^part56-qs-intro]

또한 Linux에서 PipeWire 같은 서비스 API는 존재하더라도 각 서비스별 지식이 필요하다.[^part56-qs-services]
Quickshell은 PipeWire를 다루는 타입을 제공해 공통 사용 패턴을 단순화한다.[^part56-qs-services]

Quickshell의 첫 버전은 2024년 6월 0.1이었고, 2026년 6월 공개된 0.3은 networking, `polkit`, 네트워크/보안 관련 다수 개선을 담았다.[^part56-qs-release]
현재는 다수 배포판이 패키징하고, Debian에서는 testing에서 사용 가능하다.[^part56-qs-release]
소스는 [GitHub](https://github.com/quickshell-mirror/quickshell#quickshell) 및 [Forgejo mirror](https://git.outfoxxed.me/quickshell/quickshell#quickshell)에서 관리되며, 메인티너는 커뮤니티 제안보다 직접 구현 비중이 높다.[^part56-qs-release]

기여는 기본적으로 금지되는 방식이 아니며, 다만 “인간이 의도한 변경” 원칙과 완전 자동 도구로의 코드 기여를 제한한다.[^part56-qs-contrib]

#### A shell ecosystem

최소 기능 창 관리자/컴포지터는 창 표시/관리만 제공하고, 툴바·런처는 별도 구성요소가 메워야 한다.[^part56-qs-shells]
Waybar·Rofi 같은 대안이 있더라도, 작은 데스크톱에서는 여러 프로젝트를 조립해야 생산성이 보장된다.[^part56-qs-shells]

`caelestia-shell`·`DankMaterialShell` 같은 Quickshell 기반 프로젝트는 GNOME/KDE 수준은 아니더라도 경량 창 관리자에서 실사용 가능한 중간층 기능을 제공한다.[^part56-qs-shells]
또한 구성은 텍스트보다 GUI 형태로 노출되는 경우가 많고, 스타일은 `ext-background-effect` 같은 Wayland 프로토콜 지원 여부에 따라 달라진다.[^part56-qs-shells]

#### A trove of types

QML은 Qt 객체를 선언적으로 구성한다.[^part56-qs-qml]
Python처럼 위젯을 절차적으로 생성하는 대신, 요소를 타입으로 선언해 구조와 상태를 구성한다.[^part56-qs-qml]

```python
from PyQt6.QtWidgets import (QGridLayout, QLabel)
layout = QGridLayout()
label = QLabel("Using Qt 6 in Python.")
layout.addWidget(label)
```

동일 기능을 QML로 쓰면 구조만 선언하면 된다.[^part56-qs-qml]

```qml
import QtQuick.Controls
import QtQuick.Layouts
GridLayout {
    Label {
        text: "Using Qt 6 with QML."
    }
}
```

버튼 이벤트는 JavaScript로 바인딩되며, QML 엔진이 스크립트를 내부에서 컴파일한다.[^part56-qs-qml]

Quickshell은 QtQuick 타입을 확장하는 자체 타입군을 제공한다.[^part56-qs-types]
예로 `Process`는 쉘 실행 및 출력 캡처를, `UPower`는 배터리 정보 조회를 단순 API로 감싸준다.[^part56-qs-types]
`Bluetooth`, `Networking`, `Sockets`도 각각 고수준 속성으로 시스템 상태를 다룰 수 있게 한다.[^part56-qs-types]

반면 QML 스크립트 언어는 기본적으로 JavaScript에 한정되며, 특정 백엔드 확장은 C++ 결합이 필요할 수 있다.[^part56-qs-types]

#### QML and declarative interfaces

기본 예제는 `Text` 객체를 출력하는 코드다.[^part56-qs-text]

```qml
import QtQuick

Text {
    text: "Hello from Quickshell!"
}
```

`quickshell` 명령은 기본적으로 `~/.config/quickshell/shell.qml`을 읽는다.[^part56-qs-runtime]
필요 시 `-p/--path`로 대상 파일을 지정할 수 있고, 저장 즉시 인터페이스가 갱신된다.[^part56-qs-runtime]

> ![Simple Quickshell example with a Text object.](https://static.lwn.net/images/2026/quickshell-text.png)

인터랙티브 예제는 `customData` 변수를 `Button` 클릭과 연결해 카운트를 갱신한다.[^part56-qs-interactive]

```qml
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Quickshell

FloatingWindow {
    property var customData: 0
    ColumnLayout {
        Text {
            text: `Clicks: ${customData}`
        }
        Button {
            text: "Increment"
            onClicked: customData += 1
        }
    }
}
```

> ![An interactive Quickshell window example with text and a button.](https://static.lwn.net/images/2026/quickshell-window.png)

확장 예제는 `DesktopEntries`를 이용해 설치된 데스크톱 엔트리를 스크롤 가능한 그리드로 출력한다.[^part56-qs-launcher]

```qml
import QtQuick
import QtQuick.Controls
import Quickshell
import Quickshell.Widgets

FloatingWindow  {
    title: "LWN Launcher"

    ScrollView {
        anchors.fill: parent

        GridView {
            id: grid
            cellWidth: 48
            cellHeight: 48

            model: DesktopEntries.applications

            delegate: RoundButton {
                radius: 0
                implicitWidth: grid.cellWidth
                implicitHeight: grid.cellWidth

                hoverEnabled: true
                ToolTip.text: modelData.name
                ToolTip.visible: hovered

                contentItem: IconImage {
                    source: Quickshell.iconPath(modelData.icon)
                }

                onClicked: {
                    Quickshell.execDetached([modelData.execString]);
                    Qt.quit()
                }
            }
        }
    }
}
```

`model`과 `delegate` 바인딩은 각 항목을 객체 단위로 렌더링하고, `modelData.icon`이나 `modelData.name` 같은 값을 템플릿처럼 사용한다.[^part56-qs-launcher]

> ![A Quickshell launcher demonstration displaying a grid of icons.](https://static.lwn.net/images/2026/quickshell-launcher.png)

#### 결론

원문 작성자는 NixOS + niri 환경에서 기존 직접 구현 바/런처 대신 DankMaterialShell을 기본 셸로 쓰게 되었고, 작은 GUI 유틸리티에는 Quickshell이 여전히 유용하다고 정리한다.[^part56-qs-conclusion]
단점은 플러그인 브레이크 등 버전 변경의 수동 대응 필요성이며, 최근 빠르게 안정화되는 흐름이다.[^part56-qs-conclusion]

[원문 보기](https://lwn.net/Articles/1083090/) · [댓글 18개](https://lwn.net/Articles/1083090/#Comments)

## Brief items

### Security


#### 요약
- 이 항목은 **Security** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

### [arrayref (Rust blog) 공급망 공격](https://lwn.net/Articles/1089720/)

#### 요약

- `proc-macro1` 악성 배포로 `arrayref`가 영향을 받으면서 버전 회수 조치가 이루어졌다.
- `crates.io` 생태계에서 메인테이너 계정 탈취 징후 발생 시 신속한 yanking이 중요하다.
- 영향받는 동반 패키지도 함께 점검해야 한다.

Rust 블로그는 최근 `crates.io`에 올라온 악성 크레이트(`proc-macro1`)로 인해 `arrayref`가 최근 버전에서 오염되었으며, 해당 버전이 yanked되었고 계정이 잠겼다고 공지했다.[^part56-qs-supply]
`internment`, `append-only-vec`도 같은 저자 체인에서 영향을 받아 함께 조치되었다.[^part56-qs-supply]

[원문 보기](https://lwn.net/Articles/1089720/) · [댓글 3개](https://lwn.net/Articles/1089720/#Comments)

### [Security quote of the week](https://lwn.net/Articles/1089760/)

#### 요약

- PyPI는 제한된 인력으로 방대한 오픈소스 생태계를 떠받치고 있어 보안 리스크가 크다.
- 지원 요청 증가와 유지보수 공백이 운영 성능을 압박한다.
- 오픈소스 인프라는 구조적 인력 확장 계획이 필수다.[^part56-qs-supply]

> PyPI는 공급망 리스크로 봐야 한다. 매우 큰 소프트웨어 산업이 우리의 서비스를 기반으로 돌아가는데, 기능 개발과 보안 처리량은 소수 인력(1.5 FTE + 1 FTE 지원)으로 처리되고 있다.

— Jacob Coffee

[원문 보기](https://lwn.net/Articles/1089760/)

### Kernel development


#### 요약
- 이 항목은 **Kernel development** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

### [Kernel release status](https://lwn.net/Articles/1090769/)

#### 요약

- 7.3 병합 윈도우는 8월 30일에 닫힐 예정이고 현재는 진행 중이다.
- 7.1.10·6.18.46·6.12.105·6.6.153·6.1.184·5.15.217·5.10.266가 8월 23일에 공개됐다.
- 7.2.1 등 안정 브랜치의 소규모 업데이트는 8월 27일에 리뷰 마감 예정이다.[^part56-qs-kernel]

7.3은 여전히 병합 윈도우가 열려 있으며, 종료는 8월 30일로 예상된다.[^part56-qs-kernel]
7.1.10, 6.18.46, 6.12.105, 6.6.153, 6.1.184, 5.15.217, 5.10.266은 8월 23일 배포되었고, 이어서 7.2.1과 여러 6.x/5.x 패치가 검토 단계로 들어갔다.[^part56-qs-kernel]

[원문 보기](https://lwn.net/Articles/1090769/) · [댓글 없음](https://lwn.net/Articles/1090769/#Comments)

### [Mourning Steve French](https://lwn.net/Articles/1090098/)

#### 요약

- Linux SMB/CIFS 장기 메인터이너의 별세가 장기 유지보수 리스크를 상기시켰다.
- 한 명의 핵심 인력이 빠지면 책임 분산이 특히 중요한 인프라 영역이 드러난다.
- 대체/인수인계 흐름이 안정성 확보의 기본이다.[^part56-qs-smb]

Jeremy Allison은 링크드인 게시물을 통해 Steve French의 별세 소식을 전달했다.[^part56-qs-smb]
해당 동향은 Linux SMB 파일시스템 메인터이너의 역할 공백이 어떻게 커뮤니티 운영 리스크로 전파되는지를 보여준다.[^part56-qs-smb]

[원문 보기](https://lwn.net/Articles/1090098/) · [댓글 8개](https://lwn.net/Articles/1090098/#Comments)

### [mklinux-v7.0-mk2 릴리스](https://lwn.net/Articles/1090582/)

#### 요약

- mklinux v7.0-mk2는 같은 기기에서 여러 커널을 동시에 부팅해 독립 동작시키는 모델이다.
- 하이퍼바이저 없이 `kexec_file_load()` 기반으로 분할 실행한다.
- 과거 MkLinux와는 다른, 현대적인 다중 커널 실험이다.[^part56-qs-mklinux]

Cong Wang은 멀티 커널 Linux 실험을 위해 mklinux v7.0-mk2를 발표했다.[^part56-qs-mklinux]
호스트 커널이 CPU·메모리·PCI 자원을 분할해 인스턴스별로 할당하고, 각각의 spawn 커널이 독립적으로 동작한다.[^part56-qs-mklinux]

> “하드웨어 에뮬레이션이 아니라, 각 커널이 자체 자원에서 직접 실행되며 공유는 필요한 것만 남긴다.”
— Cong Wang

[원문 보기](https://lwn.net/Articles/1090582/) · [댓글 2개](https://lwn.net/Articles/1090582/#Comments)

### [Quotes of the week](https://lwn.net/Articles/1089800/)

#### 요약

- 커널 리뷰 자동화는 생산성 향상과 커밋 메시지 가독성 손실 사이의 긴장을 만들고 있다.
- LLM 활용 확대가 리뷰 품질 하락으로 이어질 수 있다는 논의가 핵심이다.
- 핵심은 반복성 자동화와 기술적 맥락 보존의 균형이다.[^part56-qs-review]

> 다음 릴리스에서는 리뷰를 조금 다듬고, 반복 업무는 LLM이 맡고, 검토된 패치에만 자동 적용까지 가는 방향을 기대한다.
— Jakub Kicinski

> 수년 동안 한 줄짜리 커밋 메시지의 문제를 겪었고, 지금은 쓸모없는 노이즈가 많이 보인다. 과연 우리가 이득을 보았는지 의문이다.
— Christian Brauner

[원문 보기](https://lwn.net/Articles/1089800/) · [댓글 3개](https://lwn.net/Articles/1089800/#Comments)

### Distributions


#### 요약
- 이 항목은 **Distributions** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

### [Armbian 26.8 릴리스](https://lwn.net/Articles/1090741/)

#### 요약

- 인스톨러를 `armbian-config` 모듈로 재구성해 테스트·유닛 검증 가능한 구조로 바꿨다.
- SPI/MTD/eMMC/NVMe 처리 경로 분리와 bootloader 실패 보고 개선이 진행됐다.
- CI를 리포지토리와 분리해 유지보수 체계를 조정했다.[^part56-qs-armbian]

Armbian 26.8은 설치기 전면 개편, Armbian Imager 통합, CI 분리 등을 포함한다.[^part56-qs-armbian]
`Done` 메시지만 찍고 끝내던 방식에서 실제 실패 인지로 바뀌는 점이 현장 운영에 영향을 준다.[^part56-qs-armbian]

더 자세한 변경은 [릴리스 노트](https://docs.armbian.com/releases/26.8/)에서 확인한다.[^part56-qs-armbian]

[원문 보기](https://lwn.net/Articles/1090741/) · [댓글 없음](https://lwn.net/Articles/1090741/#Comments)

### [Vanilla OS 3 출시](https://lwn.net/Articles/1090527/)

#### 요약

- Vanilla OS 3는 immutable 데스크톱 배포판의 성숙 단계 업데이트이다.
- Arm64 지원과 `Apx` 패키지 관리자 재구성이 핵심 포인트다.
- SDK 기반 아키텍처 전환이 유지보수 방식 자체에 영향을 준다.[^part56-qs-vanilla]

Vanilla OS 3는 Arm64 지원 추가와 [SDK](https://github.com/Vanilla-OS/sdk#vanilla-os-sdk) 도입, `Apx` 재작성(신규 SDK 기반)을 포함해 출시되었다.[^part56-qs-vanilla]

[원문 보기](https://lwn.net/Articles/1090527/) · [댓글 1개](https://lwn.net/Articles/1090527/#Comments)

### [Distributions quote of the week](https://lwn.net/Articles/1090365/)

#### 요약

- 하드웨어 확장만으로는 긴 빌드를 해소하기 어렵다는 점을 `rpmbuild` 사례로 지적한다.
- `rpmbuild`와 `%build` 구조는 극단 병렬화에서 병목이 생길 수 있다.
- 빌드 성능 튜닝은 Amdahl 한계를 이해한 작업 분해가 필요하다.[^part56-qs-rpm]

> “거대한 하드웨어가 RPM 빌드 시간을 근본적으로 해결하지는 못한다. 병목은 소프트웨어 아키텍처와 작업 흐름이다.”[^part56-qs-rpm]

— Miroslav Suchý

[원문 보기](https://lwn.net/Articles/1090365/) · [댓글 없음](https://lwn.net/Articles/1090365/#Comments)

### Development


#### 요약
- 이 항목은 **Development** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

### [Emacs 31.1 릴리스](https://lwn.net/Articles/1090308/)

#### 요약

- Emacs dumper 제거와 사용자 Lisp 디렉터리 추가가 가장 눈에 띄는 변경이다.
- `context-menu-mode`의 `Send to...` 추가로 메뉴 확장이 이루어졌다.
- 배포 노트를 확인해 플러그인/사용자 설정 호환성 점검이 필요하다.[^part56-qs-emacs]

Emacs 31.1은 [NEWS](https://www.gnu.org/software/emacs/news/NEWS.31.1), 그리고 [해설 글](https://www.masteringemacs.org/article/whats-new-in-emacs-311)에서 여러 변경 사항을 확인할 수 있다.[^part56-qs-emacs]

[원문 보기](https://lwn.net/Articles/1090308/) · [댓글 4개](https://lwn.net/Articles/1090308/#Comments)

### [KDE Gear 26.08 릴리스](https://lwn.net/Articles/1089721/)

#### 요약

- Okular 서명 기능, Dolphin 파일 분류, Kdenlive 편의성 개선이 핵심이다.
- KDE 핵심 앱군의 정기 패키지 번들 업데이트다.
- 주요 변경은 changelog에서 점검하는 것이 좋다.[^part56-qs-kde]

KDE Gear 26.08은 Okular, Dolphin, Kdenlive 등 핵심 앱 개선과 서명 연동 강화가 포함된 릴리스다.[^part56-qs-kde]
전체 목록은 [changelog](https://kde.org/announcements/changelogs/gear/26.08.0/)에서 확인 가능하다.[^part56-qs-kde]

[원문 보기](https://lwn.net/Articles/1089721/) · [댓글 없음](https://lwn.net/Articles/1089721/#Comments)

### [LibreOffice 26.8 릴리스](https://lwn.net/Articles/1090606/)

#### 요약

- RTL/양방향/수직 CJK 텍스트 처리 개선이 핵심이다.
- 문서 열기·붙여넣기 시 방향 자동 탐지 로직이 강화됐다.
- 문서 교차 호환 품질 개선이 기대된다.[^part56-qs-libre]

LibreOffice 26.8은 문서 교환 정합성, 다국어 렌더링, 문서 방향 제어 등을 집중 개선했다.[^part56-qs-libre]
Writer는 방향성 기반 줄바꿈/공백 처리와 컨트롤 문자 시각화를 개선했고, Calc는 셀별 방향 자동 설정을 추가했다.[^part56-qs-libre]

[원문 보기](https://lwn.net/Articles/1090606/) · [댓글 3개](https://lwn.net/Articles/1090606/#Comments)

### [RPM 6.1.0 릴리스](https://lwn.net/Articles/1089719/)

#### 요약

- 매크로 정의 시 modifier 기능과 에러 처리 강화가 이루어졌다.
- `rpmsign` + PKCS#11 토큰 서명 지원이 추가되었다.
- 커널형 릴리스 모델을 참고한 release model 변경이 포인트다.[^part56-qs-rpm-release]

RPM 6.1.0은 매크로 정의, 빌드/검증 오류 처리, `rpmsign` PKCS#11 연동, 문서 확장(여러 man 페이지 추가)을 포함한다.[^part56-qs-rpm-release]
또한 릴리스 모델이 Linux 커널 방식에서 영감을 받았다는 점이 관리 체계 측면에서 의미 있다.[^part56-qs-rpm-release]

[원문 보기](https://lwn.net/Articles/1089719/) · [댓글 1개](https://lwn.net/Articles/1089719/#Comments)

### [Development quote of the week](https://lwn.net/Articles/1090770/)

#### 요약

- 커뮤니티 중심 유지보수의 지속 가능성을 LLM 의존성 관점에서 우려한다.
- 대체 플랫폼 의존 위험을 줄이려면 사람 중심의 문맥 보존이 중요하다.
- 핵심 인프라는 “작동 자동화”보다 “의도 전달”이 더 중요할 수 있다.[^part56-qs-llm]

> 거대한 프로젝트는 커뮤니티가 집단적으로 이해해야 유지된다. 지금은 자동화에 기대는 태도가 커뮤니티 지식의 내구성을 약화시킬 위험이 있다.

— Antoine Beaupré

[원문 보기](https://lwn.net/Articles/1090770/) · [댓글 없음](https://lwn.net/Articles/1090770/#Comments)

[^part56-qs-intro]: Quickshell의 핵심 가치는 “구성 기반 GUI” 접근이다. Linux에서는 컴포넌트 분리형 데스크톱을 직접 조합해야 하는데, 이때 반복 실험 비용이 운영 비용으로 직결된다.
[^part56-qs-quick]: 데스크톱 구성요소를 빠르게 구현하려는 도구는 개발 주기를 단축하므로, 소형 WM 생태계에서 장비별 맞춤 구성이 쉬워진다.
[^part56-qs-reactive]: QML의 반응형 바인딩은 이벤트/상태 변경이 UI 속성으로 자동 전달되도록 하여 유지보수 비용을 낮춘다.
[^part56-qs-runtime]: 반복 실행·즉시 반영 모델은 실시간 구성·디버깅을 가속해 배포 파이프라인에서 재현성 검증에 유리하다.
[^part56-qs-services]: PipeWire 같은 서비스 API를 고수준 타입으로 감싸면 시스템 상태 조회가 단순해져 하드웨어 제어 코드와 UI 코드 분리가 쉬워진다.
[^part56-qs-release]: 새 기능이 빠르게 쌓이는 실험적 프로젝트에서 버전 관리와 배포 채널 정비는 보안 및 신뢰성의 기반이다.
[^part56-qs-contrib]: 기여 정책에서 “완전 자동화 기여”를 제한하는 방식은 저품질 패치 유입 방지와 책임 추적에 유효하다.
[^part56-qs-shells]: 경량 창 관리자 조합 환경에서 통합 셸 구성요소가 없으면 매일 동작이 분산되어 운영이 번거로워진다.
[^part56-qs-qml]: 선언형 UI는 구조와 상태가 분리되어 테스트 및 리뷰가 쉬워지지만, 복잡한 로직은 적절한 경계 설계가 필요하다.
[^part56-qs-types]: Quickshell 타입 레이어는 시스템 API 사용을 추상화해 보일러플레이트를 줄인다. 다만 동적 타입의 동작 경계는 문서 의존성이 커진다.
[^part56-qs-text]: 정적 텍스트 표시보다 상호작용 UI는 이벤트 바인딩과 상태 동기화 전략이 핵심이다.
[^part56-qs-interactive]: `onClicked` 바인딩 기반 상태 변경은 UI-로직 결합이 간단해도, 사용자 수/행위 확장 시 상태 스코프 관리가 중요해진다.
[^part56-qs-launcher]: 데스크톱 entry 목록을 모델 기반으로 렌더링하면 설치된 앱 전체를 동적으로 표시할 수 있으나, 권한 경계 설계가 잘못되면 실행 명령 주입 위험이 생길 수 있다.
[^part56-qs-conclusion]: 문서와 마찬가지로 UI 런처도 버전 드리프트에 취약하다. 운영 중 변경 추적 체계가 있어야 실사용 중 회귀를 억제한다.
[^part56-qs-supply]: crates.io 공급망 이슈는 단일 패키지 문제가 아니라 의존성 트리 전체 신뢰성 문제다. 회수(yanking) 후에도 lockfile 정합성 검토가 필요하다.
[^part56-qs-kernel]: 다수의 stable 업데이트가 동시에 이동하면 배포 순서 정책이 중요하다. 작은 업데이트라도 장기 보안 패치와 함께 검토해야 한다.
[^part56-qs-smb]: SMB/CIFS 계층은 파일 공유와 권한 모델이 교차되기 때문에 메인터이너 공백이 바로 운영 신뢰도 하락으로 이어질 수 있다.
[^part56-qs-mklinux]: 다중 커널 모델은 네이티브 성능이 장점이지만, I/O 및 장치 공유 정책을 정밀히 설계하지 않으면 역효과가 날 수 있다.
[^part56-qs-review]: 리뷰 자동화가 로그 품질을 떨어뜨리면 사후 디버깅 비용이 급증한다. 판단 근거를 남기는 규범이 중요하다.
[^part56-qs-armbian]: 부트로더 실패를 “성공”으로 처리하면 현장 장애시간이 급증한다. 실패 표시는 운영 안전을 위한 기본 설계다.
[^part56-qs-vanilla]: immutable 디스트리뷰션은 업그레이드 단위를 명시적으로 설계해야 롤백/복구 전략이 유효해진다.
[^part56-qs-rpm]: `rpmbuild` 성능은 CPU 개수보다 스크립트 의존성 그래프와 병렬 분배 품질에 의해 좌우된다.
[^part56-qs-emacs]: Emacs와 같이 광범위 플러그인을 가진 플랫폼은 dumper 제거 같은 코어 변경이 부팅시간/메모리 사용량에 직접 영향 준다.
[^part56-qs-kde]: KDE 번들 변경은 사용자 작업흐름 전반으로 확산되므로 배포 전 단계별 회귀검사가 필수다.
[^part56-qs-libre]: LibreOffice의 방향성 처리는 다국어 협업 환경, 보고서 교차 편집, 스크린리더 접근성까지 연결되는 실전 이슈다.
[^part56-qs-rpm-release]: 릴리스 모델 변경은 단순 버전 표기 변경이 아니라 운영 정책(버전 정책/서명/보안 테스트) 체계를 바꾼다.
[^part56-qs-llm]: LLM은 생산성을 높일 수 있지만, 인적 전문성 축소와 플랫폼 독점 의존이 동시에 커질 경우 장기 안정성에 불리하다.

---

# Announcements

## 뉴스레터

### 배포판 및 시스템 관리


#### 요약
- 이 항목은 **배포판 및 시스템 관리** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

- [DistroWatch Weekly](https://distrowatch.com/weekly.php?issue=20260824) — 8월 24일
- [This week in Fedora](https://abompard.fedorapeople.org/twif/2026/08-17-to-08-23/) — 8월 24일
- [openSUSE Tumbleweed Review of the Week](https://dominique.leuenberger.net/blog/2026/08/tumbleweed-review-of-the-week-2026-34/) — 8월 21일
- [Ubuntu Weekly News](https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-issue-958/86309) — 8월 17일

### 개발 소식


#### 요약
- 이 항목은 **개발 소식** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

- [Emacs News](https://sachachua.com/blog/2026/08/2026-08-24-emacs-news/) — 8월 24일
- [These Weeks in Firefox](https://blog.nightly.mozilla.org/2026/08/25/icons-lots-of-them-these-weeks-in-firefox-issue-206/) — 8월 25일
- [What's cooking in git.git](https://lwn.net/Articles/1089836/) — 8월 20일
- [What's cooking in git.git](https://lwn.net/Articles/1090305/) — 8월 24일
- [GNU Tools Weekly News](https://lwn.net/Articles/1090363/) — 8월 23일
- [Last Week in Kubernetes Development](https://lwkd.info/2026/20260820) — 8월 20일
- [LLVM Weekly](https://llvmweekly.org/issue/660/) — 8월 24일
- [This Week in Matrix](https://matrix.org/blog/2026/08/21/this-week-in-matrix-2026-08-21/) — 8월 21일
- [OCaml Weekly News](https://lwn.net/Articles/1090429/) — 8월 25일
- [Perl Weekly](http://perlweekly.com/archive/787.html) — 8월 24일
- [This Week in Plasma](https://blogs.kde.org/2026/08/22/this-week-in-plasma-ui-and-performance-improvements/) — 8월 22일
- [PyCoder's Weekly](https://pycoders.com/issues/749/) — 8월 25일
- [Weekly Rakudo News](https://rakudoweekly.blog/2026/08/25/2026-34-yar-by-coke/) — 8월 25일
- [This Week in Rust](https://this-week-in-rust.org/blog/2026/08/19/this-week-in-rust-665/) — 8월 19일
- [Wikimedia Tech News](https://meta.wikimedia.org/wiki/Special:FeedItem/technews/20260824000000/en) — 8월 24일

### 회의록


#### 요약
- 이 항목은 **회의록** 관련 공개 LWN 주간 소식을 정리한다.
- 원문의 링크·명령·기술 식별자는 재현성과 후속 확인을 위해 보존했다.
- 운영 또는 개발 환경에 영향을 줄 수 있는 변경은 원문 출처와 함께 검토하는 것이 좋다.

- [Fedora FESCo 회의록](https://lwn.net/Articles/1090766/) — 8월 25일

## 발표자 모집

<a id="1090736"></a>

### CFP 마감일: 2026년 8월 27일 ~ 10월 26일

#### 요약

- CFP(발표자 모집 일정)는 LWN.net CFP 캘린더([2026년 8월 기준](https://lwn.net/Calendar/Monthly/cfp/))에서 발췌했으며, 이번 목록은 8월 27일부터 10월 26일까지의 주요 공개 마감일을 정리합니다.
- 대부분 체코, 미국, 오스트레일리아 등 분산된 행사들이 다수 포함되어 있으며, `GNU Tools Cauldron`, `Linux Days 2026`, `Real-time Linux User Forum` 등 공개 소프트웨어 행사 위주입니다.
- 목록에 없는 행사는 LWN에 직접 제보해 누락을 줄일 수 있습니다.

다음은 LWN.net CFP 캘린더에서 가져온 CFP 마감일 목록입니다.

| 마감일 | 행사일 | 행사 | 위치 |
| --- | --- | --- | --- |
| 8월 31일 | 10월 2일<br/>10월 4일 | [GNU Tools Cauldron](https://conf.gnu-tools-cauldron.org/prg26/) | 체코, 프라하 |
| 8월 31일 | 10월 3일<br/>10월 4일 | [Linux Days 2026](https://pretalx.linuxdays.cz/linuxdays-2026/cfp) | 체코, 프라하 |
| 9월 6일 | 10월 6일 | [Real-time Linux User Forum](https://forms.gle/iRK48ACWnMatihg59) | 체코, 프라하 |
| 9월 6일 | 1월 20일<br/>1월 22일 | [Everything Open](https://2027.everythingopen.au/programme/proposals/) | 브리즈번, 오스트레일리아 |
| 9월 18일 | 9월 19일 | [Software Freedom Day NJ](https://digitalfreedoms.org/en/sfd) | 미국, 뉴저지주 몽트클레어 |
| 10월 1일 | 11월 7일<br/>11월 8일 | [OpenFest 2026](https://cfp.openfest.org) | 불가리아, 소피아 |
| 10월 1일 | 11월 12일<br/>11월 13일 | [Ubuntu Summit 26.10](https://ubuntu.com/summit/call-for-collaboration) | 미공개 |

행사 목록에 귀하의 행사가 보이지 않으면 [제보해 주세요](https://lwn.net/Calendar/new/).

## 예정된 행사

<a id="1090735"></a>

### 행사: 2026년 8월 27일 ~ 10월 26일

#### 요약

- LWN.net 캘린더 기준으로 8월 27일부터 10월 26일까지의 공개 행사 일정을 정리합니다.
- 유럽, 북미, 아시아에서의 오픈소스·커널·보안·미디어·저장소 관련 컨퍼런스가 집중되어 있으며, 특히 10월 초 프라하권역 행사가 연달아 밀집되어 있습니다.
- 행사별 중복 일정이 많아 실제 참가 계획 수립 시 겹침 여부를 먼저 점검하는 것이 중요합니다.
- 누락된 행사는 LWN 캘린더 제보 채널로 알려주면 반영할 수 있습니다.

다음은 LWN.net 캘린더에서 가져온 행사 목록입니다.

| 날짜 | 행사 | 위치 |
| --- | --- | --- |
| 8월 25일<br/>8월 30일 | [MiniDebConf and MiniDebCamp Winterthur 2026](https://ch2026.mini.debconf.org/) | 스위스, 윈터투어 |
| 8월 30일<br/>9월 5일 | [FOSS4G Hiroshima 2026](https://2026.foss4g.org/en/) | 일본, 히로시마 |
| 9월 8일<br/>9월 10일 | [RustConf 2026](https://rustconf.com/) | 캐나다, 몬트리올 |
| 9월 17일<br/>9월 18일 | [Git Merge](https://git-merge.com/) | 포르투갈, 리스본 |
| 9월 19일 | [Software Freedom Day NJ](https://njsfd.org/) | 미국, 뉴저지주 몽트클레어 |
| 9월 19일<br/>9월 20일 | [Nextcloud Community Conference 2026](https://nextcloud.com/conference-2026) | 독일, 베를린 |
| 9월 19일<br/>9월 24일 | [Akademy 2026](https://akademy.kde.org/2026/) | 오스트리아, 그라츠 |
| 9월 22일<br/>9월 24일 | [Kernel Recipes](https://kernel-recipes.org/en/2026/) | 프랑스, 파리 |
| 9월 22일<br/>9월 24일 | [Reproducible Builds Summit](https://reproducible-builds.org/events/gothenburg2026/) | 스웨덴, 예테보리 |
| 9월 25일<br/>9월 27일 | [PostmarketOS and Alpine Linux Conference](https://postmarketos.org/conference/) | 독일, 아헨 |
| 9월 28일<br/>9월 30일 | [X.Org Developers Conference](https://indico.freedesktop.org/event/12/) | 캐나다, 토론토 |
| 9월 28일<br/>10월 1일 | [Alpine Linux Persistence and Storage Summit](https://www.alpss.at/) | 오스트리아, 티롤주 리추머회트 |
| 9월 30일<br/>10월 1일 | [All Systems Go! 2026](https://all-systems-go.io/) | 독일, 베를린 |
| 10월 1일<br/>10월 2일 | [embedded Linux for Safe and Secure Applications](https://www.elsa-symposium.com/home) | 독일, 괴팅겐 |
| 10월 1일 | [Open Tech Day: Software-defined Storage](https://opentechday.de/) | 독일, 뉘른베르크 |
| 10월 2일<br/>10월 4일 | [GNU Tools Cauldron](https://gnu-tools-cauldron.org/) | 체코, 프라하 |
| 10월 3일<br/>10월 4일 | [openSUSE.Asia Summit 2026](https://events.opensuse.org/conferences/oSAS26) | 인도네시아, 요요가카르타 |
| 10월 3일<br/>10월 4일 | [Linux Days 2026](https://www.linuxdays.cz/2026/) | 체코, 프라하 |
| 10월 5일<br/>10월 7일 | [Linux Plumbers Conference 2026](https://lpc.events/event/20/) | 체코, 프라하 |
| 10월 6일 | [Yocto Project Developer Day 2026](https://www.yoctoproject.org/event/ypdd-26/) | 체코, 프라하 |
| 10월 6일 | [Real-time Linux User Forum](https://realtime-linux.org/event/real-time-linux-user-forum/) | 체코, 프라하 |
| 10월 7일<br/>10월 9일 | [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) | 체코, 프라하 |
| 10월 7일<br/>10월 9일 | [Embedded Linux Conference Europe](https://events.linuxfoundation.org/embedded-linux-conference-europe) | 체코, 프라하 |
| 10월 8일 | [Linux Security Summit Europe](https://events.linuxfoundation.org/linux-security-summit-europe/program/schedule-at-a-glance/) | 체코, 프라하 |
| 10월 14일<br/>10월 17일 | [PyCon South Africa](https://za.pycon.org/) | 남아프리카공화국, 케이프타운 |
| 10월 16일<br/>10월 18일 | [VideoLAN Developers' Days](https://www.videolan.org/videolan/events/vdd26/) | 이탈리아, 로마 |
| 10월 18일<br/>10월 20일 | [All Things Open](https://2026.allthingsopen.org/) | 미국, 노스캐롤라이나주 롤리 |
| 10월 20일<br/>10월 23일 | [PostgreSQL Conference Europe](https://2026.pgconf.eu/about/) | 스페인, 발렌시아 |
| 10월 20일<br/>10월 23일 | [The Matrix Conference](https://conference.matrix.org/) | 스웨덴, 말뫼 |

행사가 목록에 없으면 [제보해 주세요](https://lwn.net/Calendar/new/).

## 보안 업데이트

<a id="1090733"></a>

---

# LWN 주간 보안 업데이트 및 커널 패치 목록

> 범위: 이 문서는 지정된 두 공개 LWN 콘텐츠 조각만을 한국어로 번역한 것입니다. 유료 콘텐츠나 다른 출처는 포함하지 않습니다.

### Alert summary August 20, 2026 에 August 26, 2026

#### 요약

- 이 표는 2026년 8월 20일부터 8월 26일까지의 공개 보안 업데이트 알림을 나열합니다.
- 배포판, 식별자, 릴리스, 패키지 및 날짜는 원문 데이터 필드를 그대로 보존합니다.
- 각 식별자 링크는 해당 공개 LWN 항목을 가리킵니다.

| 배포판 | 식별자 | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:58555](https://lwn.net/Articles/1090437/) | 8 | NetworkManager | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58572](https://lwn.net/Articles/1090436/) | 9 | NetworkManager | 2026-08-25 |
| AlmaLinux | [ALSA-2026:57148](https://lwn.net/Articles/1090189/) | 10 | ansible-core | 2026-08-21 |
| AlmaLinux | [ALSA-2026:57149](https://lwn.net/Articles/1089910/) | 9 | ansible-core | 2026-08-20 |
| AlmaLinux | [ALSA-2026:55442](https://lwn.net/Articles/1089652/) | 9 | bind9.18 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:57451](https://lwn.net/Articles/1090190/) | 8 | cups-filters | 2026-08-21 |
| AlmaLinux | [ALSA-2026:58560](https://lwn.net/Articles/1090430/) | 9 | cups-filters | 2026-08-25 |
| AlmaLinux | [ALSA-2026:57462](https://lwn.net/Articles/1090191/) | 8 | curl | 2026-08-21 |
| AlmaLinux | [ALSA-2026:58898](https://lwn.net/Articles/1090608/) | 8 | firefox | 2026-08-26 |
| AlmaLinux | [ALSA-2026:57015](https://lwn.net/Articles/1089653/) | 10 | glib2 | 2026-08-20 |
| AlmaLinux | [ALSA-2026:56521](https://lwn.net/Articles/1089654/) | 8 | gstreamer1-plugins-bad-free | 2026-08-19 |
| AlmaLinux | [ALSA-2026:59097](https://lwn.net/Articles/1090431/) | 10 | gstreamer1-plugins-base | 2026-08-25 |
| AlmaLinux | [ALSA-2026:59487](https://lwn.net/Articles/1090609/) | 8 | gstreamer1-plugins-base | 2026-08-26 |
| AlmaLinux | [ALSA-2026:56966](https://lwn.net/Articles/1089655/) | 8 | gstreamer1-plugins-good | 2026-08-20 |
| AlmaLinux | [ALSA-2026:59179](https://lwn.net/Articles/1090432/) | 8 | gstreamer1-plugins-good | 2026-08-25 |
| AlmaLinux | [ALSA-2026:55775](https://lwn.net/Articles/1090192/) | 8 | java-1.8.0-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55775](https://lwn.net/Articles/1090193/) | 9 | java-1.8.0-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55781](https://lwn.net/Articles/1090194/) | 8 | java-17-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55781](https://lwn.net/Articles/1090195/) | 9 | java-17-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55787](https://lwn.net/Articles/1090198/) | 10 | java-21-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55787](https://lwn.net/Articles/1090196/) | 8 | java-21-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55787](https://lwn.net/Articles/1090197/) | 9 | java-21-openjdk | 2026-08-21 |
| AlmaLinux | [ALSA-2026:55798](https://lwn.net/Articles/1090199/) | 9 | java-25-openjdk | 2026-08-24 |
| AlmaLinux | [ALSA-2026:57597](https://lwn.net/Articles/1090201/) | 10 | kbd | 2026-08-21 |
| AlmaLinux | [ALSA-2026:57610](https://lwn.net/Articles/1090200/) | 9 | kbd | 2026-08-21 |
| AlmaLinux | [ALSA-2026:57251](https://lwn.net/Articles/1090433/) | 10 | kernel | 2026-08-25 |
| AlmaLinux | [ALSA-2026:57253](https://lwn.net/Articles/1090202/) | 8 | kernel | 2026-08-21 |
| AlmaLinux | [ALSA-2026:59821](https://lwn.net/Articles/1090610/) | 8 | kernel | 2026-08-26 |
| AlmaLinux | [ALSA-2026:57254](https://lwn.net/Articles/1089656/) | 8 | kernel-rt | 2026-08-20 |
| AlmaLinux | [ALSA-2026:59737](https://lwn.net/Articles/1090611/) | 8 | kernel-rt | 2026-08-26 |
| AlmaLinux | [ALSA-2026:56965](https://lwn.net/Articles/1089657/) | 10 | libcupsfilters | 2026-08-20 |
| AlmaLinux | [ALSA-2026:57596](https://lwn.net/Articles/1090435/) | 10 | mrtg | 2026-08-24 |
| AlmaLinux | [ALSA-2026:57600](https://lwn.net/Articles/1090434/) | 9 | mrtg | 2026-08-25 |
| AlmaLinux | [ALSA-2026:56007](https://lwn.net/Articles/1089658/) | 10 | mysql8.4 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:56936](https://lwn.net/Articles/1089659/) | 8 | mysql:8.4 | 2026-08-20 |
| AlmaLinux | [ALSA-2026:59220](https://lwn.net/Articles/1090438/) | 10 | nginx | 2026-08-25 |
| AlmaLinux | [ALSA-2026:59216](https://lwn.net/Articles/1090439/) | 8 | nginx:1.24 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58819](https://lwn.net/Articles/1090440/) | 10 | nodejs24 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:55617](https://lwn.net/Articles/1089661/) | 10 | pcp | 2026-08-19 |
| AlmaLinux | [ALSA-2026:55560](https://lwn.net/Articles/1089660/) | 8 | pcp | 2026-08-19 |
| AlmaLinux | [ALSA-2026:55740](https://lwn.net/Articles/1089911/) | 9 | pcp | 2026-08-20 |
| AlmaLinux | [ALSA-2026:56971](https://lwn.net/Articles/1089662/) | 10 | perl-Date-Manip | 2026-08-20 |
| AlmaLinux | [ALSA-2026:57562](https://lwn.net/Articles/1090203/) | 8 | perl-Date-Manip | 2026-08-21 |
| AlmaLinux | [ALSA-2026:56970](https://lwn.net/Articles/1090441/) | 9 | perl-Date-Manip | 2026-08-25 |
| AlmaLinux | [ALSA-2026:56969](https://lwn.net/Articles/1089663/) | 10 | php8.4 | 2026-08-20 |
| AlmaLinux | [ALSA-2026:47750](https://lwn.net/Articles/1089664/) | 8 | php:7.4 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:47749](https://lwn.net/Articles/1089666/) | 8 | php:8.2 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:57574](https://lwn.net/Articles/1090204/) | 8 | php:8.2 | 2026-08-21 |
| AlmaLinux | [ALSA-2026:40416](https://lwn.net/Articles/1089665/) | 9 | php:8.2 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:48197](https://lwn.net/Articles/1089667/) | 9 | php:8.3 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:57539](https://lwn.net/Articles/1090205/) | 9 | php:8.3 | 2026-08-21 |
| AlmaLinux | [ALSA-2026:59243](https://lwn.net/Articles/1090443/) | 10 | python-pyasn1 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:59241](https://lwn.net/Articles/1090444/) | 8 | python-pyasn1 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:59242](https://lwn.net/Articles/1090442/) | 9 | python-pyasn1 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58561](https://lwn.net/Articles/1090446/) | 10 | python-urwid | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58562](https://lwn.net/Articles/1090447/) | 8 | python-urwid | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58952](https://lwn.net/Articles/1090445/) | 9 | python-urwid | 2026-08-25 |
| AlmaLinux | [ALSA-2026:56219](https://lwn.net/Articles/1089668/) | 8 | python3 | 2026-08-19 |
| AlmaLinux | [ALSA-2026:58902](https://lwn.net/Articles/1090449/) | 10 | python3.12 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58971](https://lwn.net/Articles/1090450/) | 8 | python3.12 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:59009](https://lwn.net/Articles/1090448/) | 9 | python3.12 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58928](https://lwn.net/Articles/1090452/) | 10 | python3.14 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58901](https://lwn.net/Articles/1090451/) | 9 | python3.14 | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58571](https://lwn.net/Articles/1090453/) | 10 | qemu-kvm | 2026-08-25 |
| AlmaLinux | [ALSA-2026:58938](https://lwn.net/Articles/1090612/) | 8 | sqlite | 2026-08-26 |
| AlmaLinux | [ALSA-2026:57126](https://lwn.net/Articles/1089669/) | 10 | yggdrasil | 2026-08-20 |
| Debian | [DLA-4749-1](https://lwn.net/Articles/1089913/) | LTS | chromium | 2026-08-21 |
| Debian | [DSA-6455-1](https://lwn.net/Articles/1089912/) | stable | chromium | 2026-08-20 |
| Debian | [DLA-4751-1](https://lwn.net/Articles/1090206/) | LTS | designate | 2026-08-23 |
| Debian | [DSA-6452-1](https://lwn.net/Articles/1089670/) | stable | designate | 2026-08-19 |
| Debian | [DSA-6464-1](https://lwn.net/Articles/1090454/) | stable | erlang | 2026-08-25 |
| Debian | [DLA-4750-1](https://lwn.net/Articles/1090207/) | LTS | firefox-esr | 2026-08-21 |
| Debian | [DSA-6451-1](https://lwn.net/Articles/1089671/) | stable | firefox-esr | 2026-08-19 |
| Debian | [DSA-6467-1](https://lwn.net/Articles/1090613/) | stable | freecad | 2026-08-26 |
| Debian | [DSA-6458-1](https://lwn.net/Articles/1090208/) | stable | gst-plugins-bad1.0 | 2026-08-21 |
| Debian | [DSA-6466-1](https://lwn.net/Articles/1090614/) | stable | kernel | 2026-08-25 |
| Debian | [DSA-6453-1](https://lwn.net/Articles/1089914/) | stable | libgit2 | 2026-08-20 |
| Debian | [DSA-6459-1](https://lwn.net/Articles/1090209/) | stable | libnet-dns-perl | 2026-08-22 |
| Debian | [DLA-4755-1](https://lwn.net/Articles/1090615/) | LTS | libvncserver | 2026-08-25 |
| Debian | [DLA-4753-1](https://lwn.net/Articles/1090210/) | LTS | nvidia-graphics-drivers | 2026-08-24 |
| Debian | [DLA-4752-1](https://lwn.net/Articles/1090211/) | LTS | nvidia-graphics-drivers | 2026-08-24 |
| Debian | [DSA-6457-1](https://lwn.net/Articles/1090212/) | stable | openjdk-21 | 2026-08-21 |
| Debian | [DSA-6460-1](https://lwn.net/Articles/1090213/) | stable | openjdk-25 | 2026-08-23 |
| Debian | [DSA-6465-1](https://lwn.net/Articles/1090616/) | stable | openssl | 2026-08-25 |
| Debian | [DLA-4747-1](https://lwn.net/Articles/1089915/) | LTS | python-httplib2 | 2026-08-20 |
| Debian | [DLA-4748-1](https://lwn.net/Articles/1089916/) | LTS | python-httplib2 | 2026-08-20 |
| Debian | [DSA-6454-1](https://lwn.net/Articles/1089917/) | stable | sabnzbdplus | 2026-08-20 |
| Debian | [DSA-6456-1](https://lwn.net/Articles/1090214/) | stable | spip | 2026-08-21 |
| Debian | [DLA-4746-1](https://lwn.net/Articles/1089672/) | LTS | swift | 2026-08-19 |
| Debian | [DLA-4754-1](https://lwn.net/Articles/1090455/) | LTS | thunderbird | 2026-08-25 |
| Debian | [DSA-6461-1](https://lwn.net/Articles/1090215/) | stable | thunderbird | 2026-08-23 |
| Debian | [DSA-6463-1](https://lwn.net/Articles/1090456/) | stable | webkit2gtk | 2026-08-24 |
| Debian | [DSA-6462-1](https://lwn.net/Articles/1090457/) | stable | zfs-linux | 2026-08-24 |
| Fedora | [FEDORA-2026-44f6d8f2e7](https://lwn.net/Articles/1090217/) | F43 | AusweisApp2 | 2026-08-23 |
| Fedora | [FEDORA-2026-2fff59246b](https://lwn.net/Articles/1090216/) | F44 | AusweisApp2 | 2026-08-23 |
| Fedora | [FEDORA-2026-fe4c3064c5](https://lwn.net/Articles/1090223/) | F43 | GitPython | 2026-08-24 |
| Fedora | [FEDORA-2026-1ba2df871e](https://lwn.net/Articles/1090617/) | F43 | apr-util | 2026-08-26 |
| Fedora | [FEDORA-2026-1bbec06c4d](https://lwn.net/Articles/1090218/) | F44 | bluez | 2026-08-22 |
| Fedora | [FEDORA-2026-c10ed2f3b7](https://lwn.net/Articles/1090219/) | F43 | calibre | 2026-08-22 |
| Fedora | [FEDORA-2026-9f2b45e4c1](https://lwn.net/Articles/1090458/) | F44 | calibre | 2026-08-25 |
| Fedora | [FEDORA-2026-ebffec502b](https://lwn.net/Articles/1090220/) | F43 | ceph | 2026-08-22 |
| Fedora | [FEDORA-2026-7de7d03796](https://lwn.net/Articles/1090221/) | F44 | ceph | 2026-08-22 |
| Fedora | [FEDORA-2026-129176284e](https://lwn.net/Articles/1090618/) | F43 | chromium | 2026-08-26 |
| Fedora | [FEDORA-2026-295354c8a1](https://lwn.net/Articles/1090222/) | F44 | chromium | 2026-08-22 |
| Fedora | [FEDORA-2026-7cee1b8755](https://lwn.net/Articles/1090459/) | F44 | chromium | 2026-08-25 |
| Fedora | [FEDORA-2026-99a0f106c9](https://lwn.net/Articles/1089918/) | F43 | dokuwiki | 2026-08-21 |
| Fedora | [FEDORA-2026-f899239e0c](https://lwn.net/Articles/1089919/) | F44 | dokuwiki | 2026-08-21 |
| Fedora | [FEDORA-2026-cda155613e](https://lwn.net/Articles/1089920/) | F43 | domoticz | 2026-08-20 |
| Fedora | [FEDORA-2026-91c099294a](https://lwn.net/Articles/1089921/) | F43 | dotnet10.0 | 2026-08-21 |
| Fedora | [FEDORA-2026-8b4cb2340a](https://lwn.net/Articles/1089922/) | F44 | dotnet10.0 | 2026-08-21 |
| Fedora | [FEDORA-2026-0db5bf0aae](https://lwn.net/Articles/1089923/) | F43 | dotnet8.0 | 2026-08-21 |
| Fedora | [FEDORA-2026-1397d83d94](https://lwn.net/Articles/1089924/) | F44 | dotnet8.0 | 2026-08-21 |
| Fedora | [FEDORA-2026-9c8770dffb](https://lwn.net/Articles/1089925/) | F43 | dotnet9.0 | 2026-08-21 |
| Fedora | [FEDORA-2026-7cfd54a4c1](https://lwn.net/Articles/1089926/) | F44 | dotnet9.0 | 2026-08-21 |
| Fedora | [FEDORA-2026-170e9d62c6](https://lwn.net/Articles/1089928/) | F43 | firefox | 2026-08-20 |
| Fedora | [FEDORA-2026-fc11919789](https://lwn.net/Articles/1089927/) | F44 | firefox | 2026-08-20 |
| Fedora | [FEDORA-2026-903d904933](https://lwn.net/Articles/1090460/) | F44 | freeipa | 2026-08-25 |
| Fedora | [FEDORA-2026-c898a0f547](https://lwn.net/Articles/1089929/) | F43 | i2c-display | 2026-08-21 |
| Fedora | [FEDORA-2026-9b62042c7b](https://lwn.net/Articles/1089930/) | F44 | i2c-display | 2026-08-21 |
| Fedora | [FEDORA-2026-40b2544dda](https://lwn.net/Articles/1090461/) | F43 | java-21-openjdk | 2026-08-25 |
| Fedora | [FEDORA-2026-40b2544dda](https://lwn.net/Articles/1090462/) | F43 | java-21-openjdk-portable | 2026-08-25 |
| Fedora | [FEDORA-2026-760df8d7e8](https://lwn.net/Articles/1090463/) | F43 | java-25-openjdk | 2026-08-25 |
| Fedora | [FEDORA-2026-ff0646db03](https://lwn.net/Articles/1090464/) | F44 | java-25-openjdk | 2026-08-25 |
| Fedora | [FEDORA-2026-760df8d7e8](https://lwn.net/Articles/1090465/) | F43 | java-latest-openjdk | 2026-08-25 |
| Fedora | [FEDORA-2026-ff0646db03](https://lwn.net/Articles/1090466/) | F44 | java-latest-openjdk | 2026-08-25 |
| Fedora | [FEDORA-2026-39186e6ecd](https://lwn.net/Articles/1090467/) | F44 | jfrog-cli | 2026-08-25 |
| Fedora | [FEDORA-2026-1eb1157853](https://lwn.net/Articles/1090225/) | F43 | kernel | 2026-08-22 |
| Fedora | [FEDORA-2026-6d18f005f1](https://lwn.net/Articles/1090468/) | F43 | kernel | 2026-08-25 |
| Fedora | [FEDORA-2026-e57251bf72](https://lwn.net/Articles/1090224/) | F44 | kernel | 2026-08-22 |
| Fedora | [FEDORA-2026-73acdf12db](https://lwn.net/Articles/1090469/) | F44 | kernel | 2026-08-25 |
| Fedora | [FEDORA-2026-60e31281d5](https://lwn.net/Articles/1089931/) | F43 | libgit2 | 2026-08-20 |
| Fedora | [FEDORA-2026-5dace9d06e](https://lwn.net/Articles/1090470/) | F43 | libxls | 2026-08-25 |
| Fedora | [FEDORA-2026-73af37bdd0](https://lwn.net/Articles/1090471/) | F44 | libxls | 2026-08-25 |
| Fedora | [FEDORA-2026-fc9fdfd3fd](https://lwn.net/Articles/1089932/) | F43 | lyx | 2026-08-21 |
| Fedora | [FEDORA-2026-ef5c3f9941](https://lwn.net/Articles/1089933/) | F44 | lyx | 2026-08-20 |
| Fedora | [FEDORA-2026-625cbe86c8](https://lwn.net/Articles/1090472/) | F43 | nextcloud | 2026-08-25 |
| Fedora | [FEDORA-2026-a1368a72b4](https://lwn.net/Articles/1090473/) | F44 | nextcloud | 2026-08-25 |
| Fedora | [FEDORA-2026-7ab20715e6](https://lwn.net/Articles/1090619/) | F43 | nnn | 2026-08-26 |
| Fedora | [FEDORA-2026-d5ab08d6bf](https://lwn.net/Articles/1090620/) | F44 | nnn | 2026-08-26 |
| Fedora | [FEDORA-2026-11d8a5a213](https://lwn.net/Articles/1089935/) | F43 | ntpsec | 2026-08-20 |
| Fedora | [FEDORA-2026-80887c367d](https://lwn.net/Articles/1089934/) | F44 | ntpsec | 2026-08-20 |
| Fedora | [FEDORA-2026-752aa3ff05](https://lwn.net/Articles/1089936/) | F44 | openssh | 2026-08-21 |
| Fedora | [FEDORA-2026-70dd9b4fc0](https://lwn.net/Articles/1090226/) | F43 | pack | 2026-08-22 |
| Fedora | [FEDORA-2026-14ebd38fea](https://lwn.net/Articles/1090227/) | F44 | pack | 2026-08-22 |
| Fedora | [FEDORA-2026-9d65f38b15](https://lwn.net/Articles/1090621/) | F43 | perl-DBI | 2026-08-26 |
| Fedora | [FEDORA-2026-57dcf299cc](https://lwn.net/Articles/1089937/) | F44 | perl-DBI | 2026-08-21 |
| Fedora | [FEDORA-2026-09941e744b](https://lwn.net/Articles/1090474/) | F43 | perl-URI | 2026-08-25 |
| Fedora | [FEDORA-2026-32b0d26c4c](https://lwn.net/Articles/1090228/) | F44 | perl-URI | 2026-08-23 |
| Fedora | [FEDORA-2026-67f1cac6df](https://lwn.net/Articles/1089938/) | F43 | php-phpseclib3 | 2026-08-21 |
| Fedora | [FEDORA-2026-d2d58edf7d](https://lwn.net/Articles/1089939/) | F44 | php-phpseclib3 | 2026-08-21 |
| Fedora | [FEDORA-2026-7d816931eb](https://lwn.net/Articles/1089940/) | F43 | python-alembic | 2026-08-21 |
| Fedora | [FEDORA-2026-6f7b906353](https://lwn.net/Articles/1089941/) | F44 | python-alembic | 2026-08-21 |
| Fedora | [FEDORA-2026-7d816931eb](https://lwn.net/Articles/1089942/) | F43 | python-asyncmy | 2026-08-21 |
| Fedora | [FEDORA-2026-6f7b906353](https://lwn.net/Articles/1089943/) | F44 | python-asyncmy | 2026-08-21 |
| Fedora | [FEDORA-2026-7d816931eb](https://lwn.net/Articles/1089944/) | F43 | python-sqlalchemy | 2026-08-21 |
| Fedora | [FEDORA-2026-6f7b906353](https://lwn.net/Articles/1089945/) | F44 | python-sqlalchemy | 2026-08-21 |
| Fedora | [FEDORA-2026-81ad01b22a](https://lwn.net/Articles/1090622/) | F43 | python-tablib | 2026-08-26 |
| Fedora | [FEDORA-2026-eaa6ecd43e](https://lwn.net/Articles/1090623/) | F44 | python-tablib | 2026-08-26 |
| Fedora | [FEDORA-2026-a64a31b855](https://lwn.net/Articles/1090624/) | F43 | python3.10 | 2026-08-26 |
| Fedora | [FEDORA-2026-7ef4d2b23d](https://lwn.net/Articles/1090625/) | F44 | python3.10 | 2026-08-26 |
| Fedora | [FEDORA-2026-22170bd5c0](https://lwn.net/Articles/1090626/) | F43 | python3.11 | 2026-08-26 |
| Fedora | [FEDORA-2026-4d5b2df275](https://lwn.net/Articles/1090627/) | F44 | python3.11 | 2026-08-26 |
| Fedora | [FEDORA-2026-7de2b1cfc5](https://lwn.net/Articles/1090628/) | F43 | python3.12 | 2026-08-26 |
| Fedora | [FEDORA-2026-b39628a3c3](https://lwn.net/Articles/1089946/) | F43 | python3.13 | 2026-08-21 |
| Fedora | [FEDORA-2026-d2906e4778](https://lwn.net/Articles/1089947/) | F44 | python3.13 | 2026-08-21 |
| Fedora | [FEDORA-2026-914a40b4fd](https://lwn.net/Articles/1089949/) | F43 | roundcubemail | 2026-08-20 |
| Fedora | [FEDORA-2026-2aa96a9ce5](https://lwn.net/Articles/1089948/) | F44 | roundcubemail | 2026-08-20 |
| Fedora | [FEDORA-2026-bfae8723e2](https://lwn.net/Articles/1090229/) | F44 | rsync | 2026-08-22 |
| Fedora | [FEDORA-2026-903d904933](https://lwn.net/Articles/1090475/) | F44 | samba | 2026-08-25 |
| Fedora | [FEDORA-2026-70891f9a3e](https://lwn.net/Articles/1090629/) | F43 | sympa | 2026-08-26 |
| Fedora | [FEDORA-2026-eca56df39d](https://lwn.net/Articles/1090630/) | F44 | sympa | 2026-08-26 |
| Fedora | [FEDORA-2026-096ad5e804](https://lwn.net/Articles/1090231/) | F43 | tcpreplay | 2026-08-24 |
| Fedora | [FEDORA-2026-836c3dec74](https://lwn.net/Articles/1090230/) | F44 | tcpreplay | 2026-08-24 |
| Fedora | [FEDORA-2026-de4e0fac25](https://lwn.net/Articles/1089950/) | F43 | trafficserver | 2026-08-21 |
| Fedora | [FEDORA-2026-b2d993884d](https://lwn.net/Articles/1089951/) | F44 | trafficserver | 2026-08-21 |
| Fedora | [FEDORA-2026-adc1870e77](https://lwn.net/Articles/1089952/) | F43 | wireshark | 2026-08-21 |
| Fedora | [FEDORA-2026-5034844482](https://lwn.net/Articles/1089953/) | F44 | wireshark | 2026-08-20 |
| Fedora | [FEDORA-2026-61704c09ea](https://lwn.net/Articles/1089954/) | F43 | wordpress | 2026-08-21 |
| Fedora | [FEDORA-2026-dc0ff85b8b](https://lwn.net/Articles/1089955/) | F44 | wordpress | 2026-08-21 |
| Gentoo | [202608-24](https://lwn.net/Articles/1090631/) |  | DTrace | 2026-08-26 |
| Gentoo | [202608-18](https://lwn.net/Articles/1089674/) |  | Emacs | 2026-08-20 |
| Gentoo | [202608-21](https://lwn.net/Articles/1090232/) |  | GNU Emacs | 2026-08-24 |
| Gentoo | [202608-27](https://lwn.net/Articles/1090632/) |  | GNU screen | 2026-08-26 |
| Gentoo | [202608-23](https://lwn.net/Articles/1090476/) |  | Incus | 2026-08-25 |
| Gentoo | [202608-25](https://lwn.net/Articles/1090633/) |  | UnrealIRCd | 2026-08-26 |
| Gentoo | [202608-26](https://lwn.net/Articles/1090634/) |  | Vinyl Cache | 2026-08-26 |
| Gentoo | [202608-20](https://lwn.net/Articles/1089673/) |  | acl, attr | 2026-08-20 |
| Gentoo | [202608-17](https://lwn.net/Articles/1089675/) |  | libssh2 | 2026-08-20 |
| Gentoo | [202608-22](https://lwn.net/Articles/1090233/) |  | needrestart | 2026-08-24 |
| Gentoo | [202608-19](https://lwn.net/Articles/1089676/) |  | quickjs-ng | 2026-08-20 |
| Mageia | [MGASA-2026-0336](https://lwn.net/Articles/1090477/) | 10 | kernel | 2026-08-25 |
| Mageia | [MGASA-2026-0337](https://lwn.net/Articles/1090478/) | 10 | kernel-linus | 2026-08-25 |
| Oracle | [ELSA-2026-55857](https://lwn.net/Articles/1089677/) | OL9 | .NET 10.0 | 2026-08-20 |
| Oracle | [ELSA-2026-55856](https://lwn.net/Articles/1089678/) | OL9 | .NET 9.0 | 2026-08-20 |
| Oracle | [ELSA-2026-36205](https://lwn.net/Articles/1090635/) | OL7 | 389-ds-base | 2026-08-26 |
| Oracle | [ELSA-2026-58555](https://lwn.net/Articles/1090490/) | OL8 | NetworkManager | 2026-08-24 |
| Oracle | [ELSA-2026-58572](https://lwn.net/Articles/1090491/) | OL9 | NetworkManager | 2026-08-24 |
| Oracle | [ELSA-2026-57148](https://lwn.net/Articles/1090234/) | OL10 | ansible-core | 2026-08-21 |
| Oracle | [ELSA-2026-57149](https://lwn.net/Articles/1090479/) | OL9 | ansible-core | 2026-08-24 |
| Oracle | [ELSA-2026-59380](https://lwn.net/Articles/1090636/) | OL10 | attr | 2026-08-26 |
| Oracle | [ELSA-2026-56133](https://lwn.net/Articles/1089679/) | OL8 | attr | 2026-08-20 |
| Oracle | [ELSA-2026-55442](https://lwn.net/Articles/1089680/) | OL9 | bind9.18 | 2026-08-20 |
| Oracle | [ELSA-2026-57451](https://lwn.net/Articles/1090480/) | OL8 | cups-filters | 2026-08-24 |
| Oracle | [ELSA-2026-58560](https://lwn.net/Articles/1090481/) | OL9 | cups-filters | 2026-08-24 |
| Oracle | [ELSA-2026-55450](https://lwn.net/Articles/1089682/) | OL10 | curl | 2026-08-20 |
| Oracle | [ELSA-2026-57462](https://lwn.net/Articles/1090482/) | OL8 | curl | 2026-08-24 |
| Oracle | [ELSA-2026-55439](https://lwn.net/Articles/1089681/) | OL9 | curl | 2026-08-20 |
| Oracle | [ELSA-2026-58899](https://lwn.net/Articles/1090638/) | OL10 | firefox | 2026-08-26 |
| Oracle | [ELSA-2026-58898](https://lwn.net/Articles/1090637/) | OL8 | firefox | 2026-08-26 |
| Oracle | [ELSA-2026-58897](https://lwn.net/Articles/1090483/) | OL9 | firefox | 2026-08-24 |
| Oracle | [ELSA-2026-38497](https://lwn.net/Articles/1090639/) | OL9 | gegl04 | 2026-08-26 |
| Oracle | [ELSA-2026-57015](https://lwn.net/Articles/1089684/) | OL10 | glib2 | 2026-08-20 |
| Oracle | [ELSA-2026-55440](https://lwn.net/Articles/1089683/) | OL9 | glib2 | 2026-08-20 |
| Oracle | [ELSA-2026-58982](https://lwn.net/Articles/1090640/) | OL9 | grafana | 2026-08-26 |
| Oracle | [ELSA-2026-56521](https://lwn.net/Articles/1089685/) | OL8 | gstreamer1-plugins-bad-free | 2026-08-20 |
| Oracle | [ELSA-2026-59097](https://lwn.net/Articles/1090641/) | OL10 | gstreamer1-plugins-base | 2026-08-26 |
| Oracle | [ELSA-2026-59133](https://lwn.net/Articles/1090643/) | OL10 | gstreamer1-plugins-good | 2026-08-26 |
| Oracle | [ELSA-2026-56966](https://lwn.net/Articles/1089686/) | OL8 | gstreamer1-plugins-good | 2026-08-20 |
| Oracle | [ELSA-2026-59179](https://lwn.net/Articles/1090642/) | OL8 | gstreamer1-plugins-good | 2026-08-26 |
| Oracle | [ELSA-2026-59152](https://lwn.net/Articles/1090644/) | OL9 | gstreamer1-plugins-good | 2026-08-26 |
| Oracle | [ELSA-2026-59347](https://lwn.net/Articles/1090645/) | OL9 | httpd | 2026-08-26 |
| Oracle | [ELSA-2026-55775](https://lwn.net/Articles/1090235/) | OL8 | java-1.8.0-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55775](https://lwn.net/Articles/1090236/) | OL9 | java-1.8.0-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55781](https://lwn.net/Articles/1090237/) | OL8 | java-17-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55781](https://lwn.net/Articles/1090238/) | OL9 | java-17-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55787](https://lwn.net/Articles/1090241/) | OL10 | java-21-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55787](https://lwn.net/Articles/1090239/) | OL8 | java-21-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55787](https://lwn.net/Articles/1090240/) | OL9 | java-21-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55798](https://lwn.net/Articles/1090242/) | OL10 | java-25-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-55798](https://lwn.net/Articles/1090243/) | OL9 | java-25-openjdk | 2026-08-21 |
| Oracle | [ELSA-2026-57597](https://lwn.net/Articles/1090244/) | OL10 | kbd | 2026-08-21 |
| Oracle | [ELSA-2026-57610](https://lwn.net/Articles/1090245/) | OL9 | kbd | 2026-08-21 |
| Oracle | [ELSA-2026-38492](https://lwn.net/Articles/1089688/) | OL10 | kernel | 2026-08-20 |
| Oracle | [ELSA-2026-57251](https://lwn.net/Articles/1090246/) | OL10 | kernel | 2026-08-21 |
| Oracle | [ELSA-2026-54246](https://lwn.net/Articles/1089687/) | OL8 | kernel | 2026-08-20 |
| Oracle | [ELSA-2026-55764](https://lwn.net/Articles/1090484/) | OL8 | kernel | 2026-08-24 |
| Oracle | [ELSA-2026-57253](https://lwn.net/Articles/1090485/) | OL8 | kernel | 2026-08-24 |
| Oracle | [ELSA-2026-57252](https://lwn.net/Articles/1090247/) | OL9 | kernel | 2026-08-21 |
| Oracle | [ELSA-2026-55446](https://lwn.net/Articles/1089689/) | OL8 | libXfont2 | 2026-08-20 |
| Oracle | [ELSA-2026-56965](https://lwn.net/Articles/1090486/) | OL10 | libcupsfilters | 2026-08-24 |
| Oracle | [ELSA-2026-46386](https://lwn.net/Articles/1090487/) | OL7 | libreoffice | 2026-08-24 |
| Oracle | [ELSA-2026-59387](https://lwn.net/Articles/1090646/) | OL9 | mod_http2 | 2026-08-26 |
| Oracle | [ELSA-2026-57596](https://lwn.net/Articles/1090489/) | OL10 | mrtg | 2026-08-24 |
| Oracle | [ELSA-2026-57600](https://lwn.net/Articles/1090488/) | OL9 | mrtg | 2026-08-24 |
| Oracle | [ELSA-2026-56007](https://lwn.net/Articles/1089690/) | OL10 | mysql8.4 | 2026-08-20 |
| Oracle | [ELSA-2026-56936](https://lwn.net/Articles/1090248/) | OL8 | mysql:8.4 | 2026-08-21 |
| Oracle | [ELSA-2026-56973](https://lwn.net/Articles/1090249/) | OL9 | mysql:8.4 | 2026-08-21 |
| Oracle | [ELSA-2026-55804](https://lwn.net/Articles/1089691/) | OL8 | nghttp2 | 2026-08-20 |
| Oracle | [ELSA-2026-59220](https://lwn.net/Articles/1090647/) | OL10 | nginx | 2026-08-26 |
| Oracle | [ELSA-2026-55601](https://lwn.net/Articles/1089692/) | OL9 | nodejs:22 | 2026-08-20 |
| Oracle | [ELSA-2026-55603](https://lwn.net/Articles/1089693/) | OL9 | nodejs:24 | 2026-08-20 |
| Oracle | [ELSA-2026-59379](https://lwn.net/Articles/1090648/) | OL10 | pam | 2026-08-26 |
| Oracle | [ELSA-2026-56131](https://lwn.net/Articles/1089694/) | OL8 | pam | 2026-08-20 |
| Oracle | [ELSA-2026-55560](https://lwn.net/Articles/1089695/) | OL8 | pcp | 2026-08-20 |
| Oracle | [ELSA-2026-55740](https://lwn.net/Articles/1089696/) | OL9 | pcp | 2026-08-20 |
| Oracle | [ELSA-2026-56971](https://lwn.net/Articles/1089697/) | OL10 | perl-Date-Manip | 2026-08-20 |
| Oracle | [ELSA-2026-57562](https://lwn.net/Articles/1090250/) | OL8 | perl-Date-Manip | 2026-08-21 |
| Oracle | [ELSA-2026-56970](https://lwn.net/Articles/1090492/) | OL9 | perl-Date-Manip | 2026-08-24 |
| Oracle | [ELSA-2026-48225](https://lwn.net/Articles/1090251/) | OL8 | perl:5.32 | 2026-08-21 |
| Oracle | [ELSA-2026-56969](https://lwn.net/Articles/1089698/) | OL10 | php8.4 | 2026-08-20 |
| Oracle | [ELSA-2026-57574](https://lwn.net/Articles/1090493/) | OL8 | php:8.2 | 2026-08-24 |
| Oracle | [ELSA-2026-57539](https://lwn.net/Articles/1090494/) | OL9 | php:8.3 | 2026-08-24 |
| Oracle | [ELSA-2026-59243](https://lwn.net/Articles/1090650/) | OL10 | python-pyasn1 | 2026-08-26 |
| Oracle | [ELSA-2026-59241](https://lwn.net/Articles/1090649/) | OL8 | python-pyasn1 | 2026-08-26 |
| Oracle | [ELSA-2026-59242](https://lwn.net/Articles/1090651/) | OL9 | python-pyasn1 | 2026-08-26 |
| Oracle | [ELSA-2026-58561](https://lwn.net/Articles/1090495/) | OL10 | python-urwid | 2026-08-24 |
| Oracle | [ELSA-2026-58562](https://lwn.net/Articles/1090652/) | OL8 | python-urwid | 2026-08-26 |
| Oracle | [ELSA-2026-58952](https://lwn.net/Articles/1090653/) | OL9 | python-urwid | 2026-08-26 |
| Oracle | [ELSA-2026-56219](https://lwn.net/Articles/1089699/) | OL8 | python3 | 2026-08-20 |
| Oracle | [ELSA-2026-58971](https://lwn.net/Articles/1090654/) | OL8 | python3.12 | 2026-08-26 |
| Oracle | [ELSA-2026-59009](https://lwn.net/Articles/1090655/) | OL9 | python3.12 | 2026-08-26 |
| Oracle | [ELSA-2026-58928](https://lwn.net/Articles/1090496/) | OL10 | python3.14 | 2026-08-24 |
| Oracle | [ELSA-2026-58901](https://lwn.net/Articles/1090656/) | OL9 | python3.14 | 2026-08-26 |
| Oracle | [ELSA-2026-58571](https://lwn.net/Articles/1090497/) | OL10 | qemu-kvm | 2026-08-24 |
| Oracle | [ELSA-2026-56130](https://lwn.net/Articles/1089700/) | OL8 | sg3_utils | 2026-08-20 |
| Oracle | [ELSA-2026-58927](https://lwn.net/Articles/1090498/) | OL10 | sqlite | 2026-08-24 |
| Oracle | [ELSA-2026-58938](https://lwn.net/Articles/1090657/) | OL8 | sqlite | 2026-08-26 |
| Oracle | [ELSA-2026-58936](https://lwn.net/Articles/1090658/) | OL9 | sqlite | 2026-08-26 |
| Oracle | [ELSA-2026-50109-0](https://lwn.net/Articles/1090252/) | OL7 | sssd | 2026-08-21 |
| Oracle | [ELSA-2026-50117-0](https://lwn.net/Articles/1090659/) | OL7 | xorg-x11-server | 2026-08-26 |
| Oracle | [ELSA-2026-57126](https://lwn.net/Articles/1089701/) | OL10 | yggdrasil | 2026-08-20 |
| Red Hat | [RHSA-2026:59372-01](https://lwn.net/Articles/1090423/) | EL10 | assertj-core | 2026-08-25 |
| Red Hat | [RHSA-2026:58956-01](https://lwn.net/Articles/1090425/) | EL9.2 | assertj-core | 2026-08-25 |
| Red Hat | [RHSA-2026:58957-01](https://lwn.net/Articles/1090424/) | EL9.4 | assertj-core | 2026-08-25 |
| Red Hat | [RHSA-2026:58949-01](https://lwn.net/Articles/1090426/) | EL9.6 | assertj-core | 2026-08-25 |
| Red Hat | [RHSA-2026:22315-01](https://lwn.net/Articles/1089862/) | EL8 | compat-openssl10 | 2026-08-21 |
| Red Hat | [RHSA-2026:47096-01](https://lwn.net/Articles/1089852/) | EL8.4 | compat-openssl10 | 2026-08-21 |
| Red Hat | [RHSA-2026:44480-01](https://lwn.net/Articles/1089850/) | EL8.6 | compat-openssl10 | 2026-08-21 |
| Red Hat | [RHSA-2026:36217-01](https://lwn.net/Articles/1089861/) | EL8.8 | compat-openssl10 | 2026-08-21 |
| Red Hat | [RHSA-2026:22313-01](https://lwn.net/Articles/1089864/) | EL9 | compat-openssl11 | 2026-08-21 |
| Red Hat | [RHSA-2026:39012-01](https://lwn.net/Articles/1089856/) | EL9.2 | compat-openssl11 | 2026-08-21 |
| Red Hat | [RHSA-2026:39009-01](https://lwn.net/Articles/1089859/) | EL9.4 | compat-openssl11 | 2026-08-21 |
| Red Hat | [RHSA-2026:35869-01](https://lwn.net/Articles/1089860/) | EL9.6 | compat-openssl11 | 2026-08-21 |
| Red Hat | [RHSA-2026:55450-01](https://lwn.net/Articles/1090142/) | EL10 | curl | 2026-08-24 |
| Red Hat | [RHSA-2026:57462-01](https://lwn.net/Articles/1090145/) | EL8 | curl | 2026-08-24 |
| Red Hat | [RHSA-2026:55439-01](https://lwn.net/Articles/1090146/) | EL9 | curl | 2026-08-24 |
| Red Hat | [RHSA-2026:19158-01](https://lwn.net/Articles/1090184/) | EL10 | dnsmasq | 2026-08-24 |
| Red Hat | [RHSA-2026:20589-01](https://lwn.net/Articles/1090182/) | EL8 | dnsmasq | 2026-08-24 |
| Red Hat | [RHSA-2026:19373-01](https://lwn.net/Articles/1090183/) | EL9 | dnsmasq | 2026-08-24 |
| Red Hat | [RHSA-2026:34508-01](https://lwn.net/Articles/1090158/) | EL9.6 | dnsmasq | 2026-08-24 |
| Red Hat | [RHSA-2026:49927-01](https://lwn.net/Articles/1089895/) | EL8 | fence-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:51152-01](https://lwn.net/Articles/1089894/) | EL8.4 | fence-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:51157-01](https://lwn.net/Articles/1089890/) | EL8.6 | fence-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:51045-01](https://lwn.net/Articles/1089893/) | EL8.8 | fence-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:20613-01](https://lwn.net/Articles/1089846/) | EL10 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:26409-01](https://lwn.net/Articles/1089845/) | EL10.0 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:43575-01](https://lwn.net/Articles/1089839/) | EL7 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:20611-01](https://lwn.net/Articles/1089847/) | EL8 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:20612-01](https://lwn.net/Articles/1089848/) | EL9 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:41921-01](https://lwn.net/Articles/1089840/) | EL9.2 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:32962-01](https://lwn.net/Articles/1089838/) | EL9.4 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:30004-01](https://lwn.net/Articles/1089843/) | EL9.6 | gnutls | 2026-08-21 |
| Red Hat | [RHSA-2026:59347-01](https://lwn.net/Articles/1090427/) | EL9 | httpd | 2026-08-25 |
| Red Hat | [RHSA-2026:57597-01](https://lwn.net/Articles/1090143/) | EL10 | kbd | 2026-08-24 |
| Red Hat | [RHSA-2026:57610-01](https://lwn.net/Articles/1090144/) | EL9 | kbd | 2026-08-24 |
| Red Hat | [RHSA-2026:44270-01](https://lwn.net/Articles/1089900/) | EL10 | kernel | 2026-08-21 |
| Red Hat | [RHSA-2026:36541-01](https://lwn.net/Articles/1090148/) | EL10 | kernel | 2026-08-24 |
| Red Hat | [RHSA-2026:52764-01](https://lwn.net/Articles/1089892/) | EL10.0 | kernel | 2026-08-21 |
| Red Hat | [RHSA-2026:53989-01](https://lwn.net/Articles/1089891/) | EL8.6 | kernel | 2026-08-21 |
| Red Hat | [RHSA-2026:36645-01](https://lwn.net/Articles/1090147/) | EL9 | kernel | 2026-08-24 |
| Red Hat | [RHSA-2026:56573-01](https://lwn.net/Articles/1089881/) | EL9.4 | kernel | 2026-08-21 |
| Red Hat | [RHSA-2026:41236-01](https://lwn.net/Articles/1089904/) | EL7 | kernel-rt | 2026-08-21 |
| Red Hat | [RHSA-2026:8492-01](https://lwn.net/Articles/1089878/) | EL10 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8865-01](https://lwn.net/Articles/1089874/) | EL10.0 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8517-01](https://lwn.net/Articles/1089877/) | EL7 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8534-01](https://lwn.net/Articles/1089872/) | EL8 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8521-01](https://lwn.net/Articles/1089871/) | EL8.2 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:9592-01](https://lwn.net/Articles/1089868/) | EL8.4 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8908-01](https://lwn.net/Articles/1089866/) | EL8.6 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:9026-01](https://lwn.net/Articles/1089867/) | EL8.8 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8510-01](https://lwn.net/Articles/1089876/) | EL9 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8867-01](https://lwn.net/Articles/1089869/) | EL9.0 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8864-01](https://lwn.net/Articles/1089875/) | EL9.2 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8873-01](https://lwn.net/Articles/1089870/) | EL9.4 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:8866-01](https://lwn.net/Articles/1089873/) | EL9.6 | libarchive | 2026-08-21 |
| Red Hat | [RHSA-2026:19456-01](https://lwn.net/Articles/1090188/) | EL10.0 | libcap | 2026-08-24 |
| Red Hat | [RHSA-2026:24346-01](https://lwn.net/Articles/1090185/) | EL8.6 | libcap | 2026-08-24 |
| Red Hat | [RHSA-2026:22957-01](https://lwn.net/Articles/1090186/) | EL8.8 | libcap | 2026-08-24 |
| Red Hat | [RHSA-2026:21254-01](https://lwn.net/Articles/1090187/) | EL9.2 | libcap | 2026-08-24 |
| Red Hat | [RHSA-2026:46398-01](https://lwn.net/Articles/1089903/) | EL10 | libreswan | 2026-08-21 |
| Red Hat | [RHSA-2026:55449-01](https://lwn.net/Articles/1090149/) | EL10.0 | libreswan | 2026-08-24 |
| Red Hat | [RHSA-2026:46396-01](https://lwn.net/Articles/1089901/) | EL8 | libreswan | 2026-08-21 |
| Red Hat | [RHSA-2026:46397-01](https://lwn.net/Articles/1089902/) | EL9 | libreswan | 2026-08-21 |
| Red Hat | [RHSA-2026:57741-01](https://lwn.net/Articles/1090150/) | EL9.6 | libreswan | 2026-08-24 |
| Red Hat | [RHSA-2026:55762-01](https://lwn.net/Articles/1089886/) | EL8 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:33125-01](https://lwn.net/Articles/1089841/) | EL8.4 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:30849-01](https://lwn.net/Articles/1089844/) | EL8.6 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:30850-01](https://lwn.net/Articles/1089842/) | EL8.8 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:55761-01](https://lwn.net/Articles/1089883/) | EL8.8 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:55837-01](https://lwn.net/Articles/1089885/) | EL9.2 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:56224-01](https://lwn.net/Articles/1089884/) | EL9.4 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:56225-01](https://lwn.net/Articles/1089882/) | EL9.6 | multiple packages | 2026-08-21 |
| Red Hat | [RHSA-2026:47757-01](https://lwn.net/Articles/1090154/) | EL10 | openssh | 2026-08-24 |
| Red Hat | [RHSA-2026:47756-01](https://lwn.net/Articles/1090155/) | EL9 | openssh | 2026-08-24 |
| Red Hat | [RHSA-2026:22314-01](https://lwn.net/Articles/1089865/) | EL10 | openssl | 2026-08-21 |
| Red Hat | [RHSA-2026:38503-01](https://lwn.net/Articles/1089858/) | EL8 | openssl | 2026-08-21 |
| Red Hat | [RHSA-2026:43513-01](https://lwn.net/Articles/1089851/) | EL8.4 | openssl | 2026-08-21 |
| Red Hat | [RHSA-2026:38804-01](https://lwn.net/Articles/1089855/) | EL8.6 | openssl | 2026-08-21 |
| Red Hat | [RHSA-2026:38805-01](https://lwn.net/Articles/1089857/) | EL8.8 | openssl | 2026-08-21 |
| Red Hat | [RHSA-2026:22312-01](https://lwn.net/Articles/1089863/) | EL9 | openssl | 2026-08-21 |
| Red Hat | [RHSA-2026:56959-01](https://lwn.net/Articles/1090428/) | EL9.4 | osbuild-composer | 2026-08-25 |
| Red Hat | [RHSA-2026:54481-01](https://lwn.net/Articles/1089889/) | EL10 | python-idna | 2026-08-21 |
| Red Hat | [RHSA-2026:54290-01](https://lwn.net/Articles/1089879/) | EL8 | python-idna | 2026-08-21 |
| Red Hat | [RHSA-2026:54484-01](https://lwn.net/Articles/1089888/) | EL9 | python-idna | 2026-08-21 |
| Red Hat | [RHSA-2026:39127-01](https://lwn.net/Articles/1089854/) | EL8 | python-pillow | 2026-08-21 |
| Red Hat | [RHSA-2026:48760-01](https://lwn.net/Articles/1089849/) | EL8.6 | python-pillow | 2026-08-21 |
| Red Hat | [RHSA-2026:48759-01](https://lwn.net/Articles/1089853/) | EL8.8 | python-pillow | 2026-08-21 |
| Red Hat | [RHSA-2026:39311-01](https://lwn.net/Articles/1089905/) | EL9 | qemu-kvm | 2026-08-21 |
| Red Hat | [RHSA-2026:47126-01](https://lwn.net/Articles/1089897/) | EL8 | resource-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:47091-01](https://lwn.net/Articles/1089899/) | EL8.4 | resource-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:47092-01](https://lwn.net/Articles/1089898/) | EL8.6 | resource-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:47129-01](https://lwn.net/Articles/1089896/) | EL8.8 | resource-agents | 2026-08-21 |
| Red Hat | [RHSA-2026:57590-01](https://lwn.net/Articles/1089880/) | EL10 | rh-podman-desktop | 2026-08-21 |
| Red Hat | [RHSA-2026:26332-01](https://lwn.net/Articles/1090174/) | EL10 | rsync | 2026-08-24 |
| Red Hat | [RHSA-2026:26408-01](https://lwn.net/Articles/1090173/) | EL8 | rsync | 2026-08-24 |
| Red Hat | [RHSA-2026:26410-01](https://lwn.net/Articles/1090172/) | EL9 | rsync | 2026-08-24 |
| Red Hat | [RHSA-2026:37397-01](https://lwn.net/Articles/1089909/) | EL7 | ruby | 2026-08-21 |
| Red Hat | [RHSA-2026:22963-01](https://lwn.net/Articles/1090180/) | EL10 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28055-01](https://lwn.net/Articles/1090167/) | EL10.0 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28132-01](https://lwn.net/Articles/1090164/) | EL7 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:22644-01](https://lwn.net/Articles/1090181/) | EL8 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28058-01](https://lwn.net/Articles/1090163/) | EL8.4 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28057-01](https://lwn.net/Articles/1090165/) | EL8.6 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28056-01](https://lwn.net/Articles/1090166/) | EL8.8 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:25049-01](https://lwn.net/Articles/1090176/) | EL9 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28054-01](https://lwn.net/Articles/1090168/) | EL9.2 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:28053-01](https://lwn.net/Articles/1090169/) | EL9.4 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:25979-01](https://lwn.net/Articles/1090175/) | EL9.6 | samba | 2026-08-24 |
| Red Hat | [RHSA-2026:23231-01](https://lwn.net/Articles/1090179/) | EL10 | unbound | 2026-08-24 |
| Red Hat | [RHSA-2026:37282-01](https://lwn.net/Articles/1089908/) | EL8 | unbound | 2026-08-21 |
| Red Hat | [RHSA-2026:24365-01](https://lwn.net/Articles/1090178/) | EL8 | unbound | 2026-08-24 |
| Red Hat | [RHSA-2026:24369-01](https://lwn.net/Articles/1090177/) | EL9 | unbound | 2026-08-24 |
| Red Hat | [RHSA-2026:48650-01](https://lwn.net/Articles/1090151/) | EL10 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:38509-01](https://lwn.net/Articles/1090156/) | EL10 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:55431-01](https://lwn.net/Articles/1089887/) | EL10.0 | vim | 2026-08-21 |
| Red Hat | [RHSA-2026:30900-01](https://lwn.net/Articles/1090161/) | EL10.0 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:38510-01](https://lwn.net/Articles/1089906/) | EL8 | vim | 2026-08-21 |
| Red Hat | [RHSA-2026:48703-01](https://lwn.net/Articles/1090152/) | EL8 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:33453-01](https://lwn.net/Articles/1090160/) | EL8.4 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:34477-01](https://lwn.net/Articles/1090157/) | EL8.6 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:34476-01](https://lwn.net/Articles/1090159/) | EL8.8 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:38511-01](https://lwn.net/Articles/1089907/) | EL9 | vim | 2026-08-21 |
| Red Hat | [RHSA-2026:47982-01](https://lwn.net/Articles/1090153/) | EL9 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:28133-01](https://lwn.net/Articles/1090162/) | EL9.2 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:28049-01](https://lwn.net/Articles/1090171/) | EL9.4 | vim | 2026-08-24 |
| Red Hat | [RHSA-2026:28050-01](https://lwn.net/Articles/1090170/) | EL9.6 | vim | 2026-08-24 |
| Slackware | [SSA:2026-231-01](https://lwn.net/Articles/1089702/) |  | mozilla-firefox | 2026-08-19 |
| Slackware | [SSA:2026-231-02](https://lwn.net/Articles/1089703/) |  | mozilla-thunderbird | 2026-08-19 |
| SUSE | [SUSE-SU-2026:3678-1](https://lwn.net/Articles/1090255/) | SLE15 | 389-ds | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3687-1](https://lwn.net/Articles/1090253/) | SLE15 oS15.5 | 389-ds | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3686-1](https://lwn.net/Articles/1090254/) | SLE15 oS15.6 | 389-ds | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23234-1](https://lwn.net/Articles/1090660/) | SLE16.0 | amazon-ecs-init | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:21611-1](https://lwn.net/Articles/1090256/) | oS16.0 | apptainer | 2026-08-22 |
| SUSE | [SUSE-SU-2026:23161-1](https://lwn.net/Articles/1090257/) | SLE-m6.1 | avahi | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:21613-1](https://lwn.net/Articles/1090258/) | oS16.0 | bugwarden | 2026-08-22 |
| SUSE | [SUSE-SU-2026:3667-1](https://lwn.net/Articles/1089956/) | SLE15 oS15.4 | buildah | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3784-1](https://lwn.net/Articles/1090499/) | SLE15 oS15.5 | buildah | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:21624-1](https://lwn.net/Articles/1090260/) | oS16.0 | chromium | 2026-08-23 |
| SUSE | [openSUSE-SU-2026:21609-1](https://lwn.net/Articles/1090261/) | oS16.0 | chromium | 2026-08-22 |
| SUSE | [openSUSE-SU-2026:0293-1](https://lwn.net/Articles/1089957/) | osB15 | chromium | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:0298-1](https://lwn.net/Articles/1090259/) | osB15 | chromium | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:11562-1](https://lwn.net/Articles/1090500/) | TW | comfyui | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3654-1](https://lwn.net/Articles/1089958/) | SLE15 | container-suseconnect | 2026-08-20 |
| SUSE | [SUSE-SU-2026:3670-1](https://lwn.net/Articles/1089959/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | containerd | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3783-1](https://lwn.net/Articles/1090661/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | containerd | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3666-1](https://lwn.net/Articles/1089960/) | SLE15 oS15.4 | cosign | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:0292-1](https://lwn.net/Articles/1089961/) | osB15 | ctop | 2026-08-20 |
| SUSE | [SUSE-SU-2026:3798-1](https://lwn.net/Articles/1090662/) | SLE15 | curl | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3786-1](https://lwn.net/Articles/1090663/) | SLE15 oS15.4 | distribution | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3668-1](https://lwn.net/Articles/1089962/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | docker | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23246-1](https://lwn.net/Articles/1090664/) | SLE-m6.0 | dracut | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23195-1](https://lwn.net/Articles/1090501/) | SLE-m6.1 | dracut | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:11559-1](https://lwn.net/Articles/1090502/) | TW | erlang | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:11560-1](https://lwn.net/Articles/1090503/) | TW | erlang27 | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23232-1](https://lwn.net/Articles/1090665/) | SLE16.0 | ffmpeg-7 | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23222-1](https://lwn.net/Articles/1090666/) | SLE16.0 | ffmpeg-7 | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:11545-1](https://lwn.net/Articles/1090262/) | TW | ffmpeg-9-libavcodec-devel | 2026-08-23 |
| SUSE | [SUSE-SU-2026:3683-1](https://lwn.net/Articles/1090263/) | SLE12 | firefox | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3658-1](https://lwn.net/Articles/1089963/) | SLE15 | firefox | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:11546-1](https://lwn.net/Articles/1090264/) | TW | firefox-esr | 2026-08-23 |
| SUSE | [openSUSE-SU-2026:21594-1](https://lwn.net/Articles/1089964/) | oS16.0 | firefox | 2026-08-20 |
| SUSE | [openSUSE-SU-2026:21605-1](https://lwn.net/Articles/1089965/) | oS16.0 | forgejo-cli | 2026-08-20 |
| SUSE | [SUSE-SU-2026:23252-1](https://lwn.net/Articles/1090667/) | SLE-m6.0 | fuse-overlayfs | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23224-1](https://lwn.net/Articles/1090668/) | SLE16.0 | gd | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23213-1](https://lwn.net/Articles/1090669/) | SLE16.0 | gd | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3688-1](https://lwn.net/Articles/1090265/) | SLE15 oS15.4 | gimp | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:11547-1](https://lwn.net/Articles/1090266/) | TW | gimp | 2026-08-23 |
| SUSE | [SUSE-SU-2026:3801-1](https://lwn.net/Articles/1090670/) | SLE15 oS15.6 | git-lfs | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:21603-1](https://lwn.net/Articles/1089966/) | oS16.0 | gitea-tea | 2026-08-20 |
| SUSE | [openSUSE-SU-2026:21592-1](https://lwn.net/Articles/1089967/) | oS16.0 | go1.25 | 2026-08-20 |
| SUSE | [SUSE-SU-2026:3800-1](https://lwn.net/Articles/1090671/) | SLE15 | go1.25-openssl | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:21593-1](https://lwn.net/Articles/1089968/) | oS16.0 | go1.26 | 2026-08-20 |
| SUSE | [SUSE-SU-2026:3799-1](https://lwn.net/Articles/1090672/) | SLE15 | go1.26-openssl | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:11536-1](https://lwn.net/Articles/1090267/) | TW | go1.27 | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23227-1](https://lwn.net/Articles/1090673/) | SLE16.0 | govulncheck-vulndb | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23216-1](https://lwn.net/Articles/1090674/) | SLE16.0 | govulncheck-vulndb | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3718-1](https://lwn.net/Articles/1090504/) | SLE15 | grafana | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:11574-1](https://lwn.net/Articles/1090675/) | TW | hauler | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23162-1](https://lwn.net/Articles/1090268/) | SLE-m6.1 | helm | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3661-1](https://lwn.net/Articles/1089969/) | SLE15 SLE5.5 SLE-m5.5 | helm | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23233-1](https://lwn.net/Articles/1090676/) | SLE16.0 | himmelblau | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23170-1](https://lwn.net/Articles/1090269/) | SLE-m6.1 | ignition | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3790-1](https://lwn.net/Articles/1090681/) | SLE15 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23231-1](https://lwn.net/Articles/1090680/) | SLE16.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23221-1](https://lwn.net/Articles/1090682/) | SLE16.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23237-1](https://lwn.net/Articles/1090684/) | SLE16.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23241-1](https://lwn.net/Articles/1090677/) | SLE6.0 SLE-m6.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23240-1](https://lwn.net/Articles/1090678/) | SLE6.0 SLE-m6.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23244-1](https://lwn.net/Articles/1090683/) | SLE6.0 SLE-m6.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23238-1](https://lwn.net/Articles/1090679/) | SLE6.0 SLE-m6.0 | kernel | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23183-1](https://lwn.net/Articles/1090505/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23193-1](https://lwn.net/Articles/1090506/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3660-1](https://lwn.net/Articles/1089970/) | SLE15 oS15.6 | kubernetes | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3659-1](https://lwn.net/Articles/1089971/) | SLE15 oS15.6 | kubernetes-old | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:21590-1](https://lwn.net/Articles/1089972/) | oS16.0 | kubevirt1.8 | 2026-08-20 |
| SUSE | [SUSE-SU-2026:23173-1](https://lwn.net/Articles/1090270/) | SLE-m6.1 | libarchive | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:11537-1](https://lwn.net/Articles/1090271/) | TW | libjxl-devel | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3796-1](https://lwn.net/Articles/1090686/) | SLE12 | librest | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3795-1](https://lwn.net/Articles/1090685/) | SLE15 oS15.6 | librest | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23168-1](https://lwn.net/Articles/1090272/) | SLE-m6.1 | libssh | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23245-1](https://lwn.net/Articles/1090689/) | SLE-m6.0 | libssh2_org | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23187-1](https://lwn.net/Articles/1090507/) | SLE-m6.1 | libssh2_org | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23225-1](https://lwn.net/Articles/1090687/) | SLE16.0 | libssh2_org | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23214-1](https://lwn.net/Articles/1090688/) | SLE16.0 | libssh2_org | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23160-1](https://lwn.net/Articles/1090273/) | SLE-m6.1 | multipath-tools | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3647-1](https://lwn.net/Articles/1089704/) | SLE15 | open-iscsi | 2026-08-19 |
| SUSE | [SUSE-SU-2026:23235-1](https://lwn.net/Articles/1090690/) | SLE16.0 | open-iscsi | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23223-1](https://lwn.net/Articles/1090691/) | SLE16.0 | open-iscsi | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23249-1](https://lwn.net/Articles/1090692/) | SLE-m6.0 | openssh | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23172-1](https://lwn.net/Articles/1090274/) | SLE-m6.1 | openssl-3 | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23188-1](https://lwn.net/Articles/1090508/) | SLE-m6.1 | openvswitch | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23210-1](https://lwn.net/Articles/1090693/) | SLE-m6.0 | patch | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23174-1](https://lwn.net/Articles/1090275/) | SLE-m6.1 | pcp | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:11564-1](https://lwn.net/Articles/1090509/) | TW | perl-Dancer2-Plugin-Auth-Extensible | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23229-1](https://lwn.net/Articles/1090694/) | SLE16.0 | perl-Date-Manip | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23218-1](https://lwn.net/Articles/1090695/) | SLE16.0 | perl-Date-Manip | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:11550-1](https://lwn.net/Articles/1090276/) | TW | perl-Net-CIDR-Set | 2026-08-23 |
| SUSE | [openSUSE-SU-2026:11551-1](https://lwn.net/Articles/1090277/) | TW | perl-Net-OAuth | 2026-08-23 |
| SUSE | [SUSE-SU-2026:23205-1](https://lwn.net/Articles/1090696/) | SLE-m6.0 | podman | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3662-1](https://lwn.net/Articles/1089973/) | SLE15 SES7.1 oS15.3 | podman | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3652-1](https://lwn.net/Articles/1089705/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | podman | 2026-08-20 |
| SUSE | [SUSE-SU-2026:3671-1](https://lwn.net/Articles/1089974/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | podman | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3793-1](https://lwn.net/Articles/1090697/) | SLE12 | postgresql14 | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:11552-1](https://lwn.net/Articles/1090278/) | TW | postgresql14 | 2026-08-23 |
| SUSE | [openSUSE-SU-2026:11553-1](https://lwn.net/Articles/1090279/) | TW | postgresql15 | 2026-08-23 |
| SUSE | [SUSE-SU-2026:3794-1](https://lwn.net/Articles/1090698/) | SLE12 | postgresql16 | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:11555-1](https://lwn.net/Articles/1090510/) | TW | postgresql17 | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23228-1](https://lwn.net/Articles/1090700/) | SLE16.0 | python-Pillow | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23217-1](https://lwn.net/Articles/1090701/) | SLE16.0 | python-Pillow | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23247-1](https://lwn.net/Articles/1090699/) | SLE-m6.0 | python-cryptography | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23196-1](https://lwn.net/Articles/1090511/) | SLE-m6.1 | python-cryptography | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23169-1](https://lwn.net/Articles/1090280/) | SLE-m6.1 | python-msgpack | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23167-1](https://lwn.net/Articles/1090281/) | SLE-m6.1 | python-pyasn1 | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:21602-1](https://lwn.net/Articles/1089975/) | oS16.0 | python-pytest-html | 2026-08-20 |
| SUSE | [SUSE-SU-2026:3762-1](https://lwn.net/Articles/1090512/) | SLE15 | python-sqlparse | 2026-08-25 |
| SUSE | [openSUSE-SU-2026:21606-1](https://lwn.net/Articles/1089976/) | oS16.0 | python-unearth | 2026-08-20 |
| SUSE | [SUSE-SU-2026:23176-1](https://lwn.net/Articles/1090282/) | SLE-m6.1 | python-urllib3 | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3655-1](https://lwn.net/Articles/1089977/) | MP4.3 SLE15 oS15.4 | python311 | 2026-08-20 |
| SUSE | [SUSE-SU-2026:23212-1](https://lwn.net/Articles/1090702/) | SLE-m6.0 | python311 | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23191-1](https://lwn.net/Articles/1090513/) | SLE-m6.1 | python311 | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3648-1](https://lwn.net/Articles/1089706/) | SLE15 oS15.6 | python311 | 2026-08-19 |
| SUSE | [SUSE-SU-2026:23159-1](https://lwn.net/Articles/1090283/) | SLE-m6.2 | python313 | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3649-1](https://lwn.net/Articles/1089707/) | SLE15 | python313 | 2026-08-19 |
| SUSE | [openSUSE-SU-2026:11556-1](https://lwn.net/Articles/1090514/) | TW | python313-hpack | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:21595-1](https://lwn.net/Articles/1089978/) | oS16.0 | python313 | 2026-08-20 |
| SUSE | [openSUSE-SU-2026:11540-1](https://lwn.net/Articles/1090284/) | TW | python313-pytest-html | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:11542-1](https://lwn.net/Articles/1090285/) | TW | redis | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3792-1](https://lwn.net/Articles/1090703/) | SLE15 | rmt-server | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3669-1](https://lwn.net/Articles/1089979/) | SLE15 | rootlesskit | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3785-1](https://lwn.net/Articles/1090704/) | SLE15 oS15.6 | rootlesskit | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23204-1](https://lwn.net/Articles/1090705/) | SLE-m6.0 | rpm | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23200-1](https://lwn.net/Articles/1090706/) | SLE-m6.0 | rpm | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23182-1](https://lwn.net/Articles/1090515/) | SLE-m6.1 | rpm | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23192-1](https://lwn.net/Articles/1090516/) | SLE-m6.1 | rpm | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23253-1](https://lwn.net/Articles/1090707/) | SLE-m6.0 | rsync | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3657-1](https://lwn.net/Articles/1089980/) | SLE15 oS15.6 | rsync | 2026-08-21 |
| SUSE | [SUSE-SU-2026:23164-1](https://lwn.net/Articles/1090286/) | SLE-m6.1 | runc | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3787-1](https://lwn.net/Articles/1090708/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 SES7.1 | runc | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3674-1](https://lwn.net/Articles/1090287/) | SLE15 oS15.6 | sccache | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3791-1](https://lwn.net/Articles/1090709/) | SLE15 | snpguest | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23251-1](https://lwn.net/Articles/1090711/) | SLE-m6.0 | sssd | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23171-1](https://lwn.net/Articles/1090288/) | SLE-m6.1 | sssd | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3797-1](https://lwn.net/Articles/1090710/) | SLE12 | sssd | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23211-1](https://lwn.net/Articles/1090712/) | SLE-m6.0 | suseconnect-ng | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23186-1](https://lwn.net/Articles/1090517/) | SLE-m6.1 | suseconnect-ng | 2026-08-24 |
| SUSE | [openSUSE-SU-2026:11558-1](https://lwn.net/Articles/1090518/) | TW | thunderbird | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23226-1](https://lwn.net/Articles/1090713/) | SLE16.0 | unbound | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23215-1](https://lwn.net/Articles/1090714/) | SLE16.0 | unbound | 2026-08-25 |
| SUSE | [SUSE-SU-2026:23250-1](https://lwn.net/Articles/1090715/) | SLE-m6.0 | util-linux | 2026-08-25 |
| SUSE | [SUSE-SU-2026:3684-1](https://lwn.net/Articles/1090290/) | SLE15 | util-linux | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3685-1](https://lwn.net/Articles/1090289/) | SLE15 oS15.6 | util-linux | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23181-1](https://lwn.net/Articles/1090519/) | SLE-m6.1 | vim | 2026-08-24 |
| SUSE | [SUSE-SU-2026:23190-1](https://lwn.net/Articles/1090520/) | SLE-m6.1 | vim | 2026-08-24 |
| SUSE | [SUSE-SU-2026:3677-1](https://lwn.net/Articles/1090293/) | SLE12 | vim | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3679-1](https://lwn.net/Articles/1090292/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 | vim | 2026-08-21 |
| SUSE | [SUSE-SU-2026:3680-1](https://lwn.net/Articles/1090291/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | vim | 2026-08-21 |
| SUSE | [openSUSE-SU-2026:21615-1](https://lwn.net/Articles/1090294/) | oS16.0 | weechat | 2026-08-22 |
| SUSE | [SUSE-SU-2026:23163-1](https://lwn.net/Articles/1090295/) | SLE-m6.1 | wget | 2026-08-21 |
| Ubuntu | [USN-8655-1](https://lwn.net/Articles/1090521/) | 20.04 22.04 24.04 26.04 | async-http-client | 2026-08-24 |
| Ubuntu | [USN-8648-1](https://lwn.net/Articles/1089708/) | 22.04 24.04 26.04 | bind9 | 2026-08-19 |
| Ubuntu | [USN-8650-1](https://lwn.net/Articles/1089709/) | 18.04 20.04 22.04 24.04 26.04 | capnproto | 2026-08-19 |
| Ubuntu | [USN-8651-1](https://lwn.net/Articles/1089710/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | curl | 2026-08-19 |
| Ubuntu | [USN-8670-2](https://lwn.net/Articles/1090716/) | 18.04 20.04 22.04 | curl | 2026-08-25 |
| Ubuntu | [USN-8670-1](https://lwn.net/Articles/1090522/) | 24.04 | curl | 2026-08-24 |
| Ubuntu | [USN-8671-1](https://lwn.net/Articles/1090523/) | 16.04 18.04 20.04 22.04 24.04 | ffmpeg | 2026-08-24 |
| Ubuntu | [USN-8680-1](https://lwn.net/Articles/1090717/) | 16.04 18.04 20.04 22.04 24.04 | ffmpeg | 2026-08-25 |
| Ubuntu | [USN-8649-1](https://lwn.net/Articles/1089711/) | 24.04 26.04 | libheif | 2026-08-19 |
| Ubuntu | [USN-8639-1](https://lwn.net/Articles/1089712/) | 14.04 16.04 18.04 20.04 22.04 | libpng, libpng1.6 | 2026-08-19 |
| Ubuntu | [USN-8093-2](https://lwn.net/Articles/1089713/) | 26.04 | libssh | 2026-08-19 |
| Ubuntu | [USN-8666-1](https://lwn.net/Articles/1089981/) | 18.04 20.04 | linux, linux-aws, linux-aws-5.4, linux-azure, linux-bluefield, linux-fips,
 linux-gcp, linux-gcp-5.4, linux-hwe-5.4, linux-ibm, linux-ibm-5.4,
 linux-iot, linux-oracle, linux-raspi, linux-raspi-5.4, linux-xilinx-zynqmp | 2026-08-20 |
| Ubuntu | [USN-8659-1](https://lwn.net/Articles/1089982/) | 24.04 26.04 | linux, linux-aws, linux-aws-7.0, linux-ibm, linux-oem-7.0, linux-raspi,
 linux-realtime | 2026-08-20 |
| Ubuntu | [USN-8658-1](https://lwn.net/Articles/1089983/) | 20.04 22.04 | linux, linux-aws, linux-aws-fips, linux-azure-fips, linux-gkeop,
 linux-ibm-5.15, linux-intel-iot-realtime, linux-intel-iotg,
 linux-intel-iotg-5.15, linux-kvm, linux-nvidia, linux-nvidia-tegra,
 linux-nvidia-tegra-5.15, linux-oracle, linux-oracle-5.15, linux-realtime,
 linux-xilinx-zynqmp | 2026-08-20 |
| Ubuntu | [USN-8662-1](https://lwn.net/Articles/1089984/) | 14.04 16.04 | linux, linux-aws, linux-kvm, linux-lts-xenial | 2026-08-20 |
| Ubuntu | [USN-8643-4](https://lwn.net/Articles/1090718/) | 22.04 24.04 | linux-aws-6.8, linux-azure-fde, linux-azure-fde-6.8, linux-azure-fips,
 linux-nvidia-tegra | 2026-08-25 |
| Ubuntu | [USN-8630-4](https://lwn.net/Articles/1089985/) | 22.04 | linux-aws-6.8 | 2026-08-20 |
| Ubuntu | [USN-8658-3](https://lwn.net/Articles/1090720/) | 22.04 | linux-azure, linux-azure-fde, linux-nvidia-tegra-igx | 2026-08-25 |
| Ubuntu | [USN-8659-3](https://lwn.net/Articles/1090719/) | 26.04 | linux-azure, linux-azure-fde | 2026-08-25 |
| Ubuntu | [USN-8661-1](https://lwn.net/Articles/1089986/) | 20.04 22.04 | linux-azure-5.15, linux-gcp, linux-gcp-fips, linux-hwe-5.15,
 linux-lowlatency-hwe-5.15 | 2026-08-20 |
| Ubuntu | [USN-8666-2](https://lwn.net/Articles/1090721/) | 18.04 20.04 | linux-azure-5.4, linux-azure-fips | 2026-08-25 |
| Ubuntu | [USN-8662-2](https://lwn.net/Articles/1090296/) | 16.04 | linux-fips | 2026-08-21 |
| Ubuntu | [USN-8644-2](https://lwn.net/Articles/1089987/) | 16.04 18.04 | linux-gcp, linux-gcp-4.15, linux-gcp-fips | 2026-08-20 |
| Ubuntu | [USN-8660-1](https://lwn.net/Articles/1089988/) | 26.04 | linux-gcp, linux-gke | 2026-08-20 |
| Ubuntu | [USN-8668-1](https://lwn.net/Articles/1090297/) | 20.04 | linux-gcp-5.15 | 2026-08-21 |
| Ubuntu | [USN-8643-2](https://lwn.net/Articles/1089989/) | 22.04 24.04 | linux-gke, linux-lowlatency, linux-lowlatency-hwe-6.8 | 2026-08-20 |
| Ubuntu | [USN-8656-1](https://lwn.net/Articles/1089990/) | 22.04 | linux-hwe-6.8 | 2026-08-20 |
| Ubuntu | [USN-8659-2](https://lwn.net/Articles/1090298/) | 24.04 | linux-hwe-7.0 | 2026-08-21 |
| Ubuntu | [USN-8658-2](https://lwn.net/Articles/1090299/) | 22.04 | linux-ibm | 2026-08-21 |
| Ubuntu | [USN-8667-1](https://lwn.net/Articles/1090300/) | 20.04 | linux-kvm | 2026-08-21 |
| Ubuntu | [USN-8661-2](https://lwn.net/Articles/1090301/) | 22.04 | linux-lowlatency | 2026-08-21 |
| Ubuntu | [USN-8643-3](https://lwn.net/Articles/1090302/) | 22.04 24.04 | linux-nvidia, linux-nvidia-6.8, linux-nvidia-lowlatency | 2026-08-21 |
| Ubuntu | [USN-8663-1](https://lwn.net/Articles/1089991/) | 24.04 26.04 | linux-nvidia, linux-nvidia-7.0 | 2026-08-20 |
| Ubuntu | [USN-8669-1](https://lwn.net/Articles/1090303/) | 24.04 | linux-nvidia-6.17 | 2026-08-21 |
| Ubuntu | [USN-8664-1](https://lwn.net/Articles/1089992/) | 26.04 | linux-nvidia-bos | 2026-08-20 |
| Ubuntu | [USN-8659-4](https://lwn.net/Articles/1090722/) | 26.04 | linux-oracle | 2026-08-25 |
| Ubuntu | [USN-8665-1](https://lwn.net/Articles/1089993/) | 24.04 | linux-raspi, linux-raspi-realtime | 2026-08-20 |
| Ubuntu | [USN-8630-5](https://lwn.net/Articles/1090723/) | 24.04 | linux-raspi, linux-raspi-realtime | 2026-08-25 |
| Ubuntu | [USN-8654-1](https://lwn.net/Articles/1089994/) | 16.04 18.04 20.04 22.04 24.04 | netty | 2026-08-20 |
| Ubuntu | [USN-8563-4](https://lwn.net/Articles/1089714/) | 22.04 24.04 26.04 | nginx | 2026-08-19 |
| Ubuntu | [USN-8563-3](https://lwn.net/Articles/1089715/) | 22.04 24.04 26.04 | nginx | 2026-08-19 |
| Ubuntu | [USN-8676-1](https://lwn.net/Articles/1090724/) | 18.04 20.04 22.04 24.04 26.04 | openjdk-17 | 2026-08-26 |
| Ubuntu | [USN-8677-1](https://lwn.net/Articles/1090725/) | 20.04 22.04 24.04 26.04 | openjdk-21 | 2026-08-26 |
| Ubuntu | [USN-8681-1](https://lwn.net/Articles/1090726/) | 22.04 24.04 26.04 | openjdk-25 | 2026-08-26 |
| Ubuntu | [USN-8673-1](https://lwn.net/Articles/1090727/) | 16.04 18.04 20.04 22.04 24.04 26.04 | openjdk-8 | 2026-08-26 |
| Ubuntu | [USN-8674-1](https://lwn.net/Articles/1090728/) | 18.04 20.04 22.04 24.04 26.04 | openjdk-lts | 2026-08-26 |
| Ubuntu | [USN-8678-1](https://lwn.net/Articles/1090729/) | 22.04 24.04 26.04 | openssl | 2026-08-25 |
| Ubuntu | [USN-8675-1](https://lwn.net/Articles/1090730/) | 14.04 16.04 18.04 20.04 22.04 | perl | 2026-08-25 |
| Ubuntu | [USN-8653-1](https://lwn.net/Articles/1089995/) | 22.04 24.04 26.04 | postgresql-14, postgresql-16, postgresql-18 | 2026-08-20 |
| Ubuntu | [USN-8113-2](https://lwn.net/Articles/1089716/) | 26.04 | tiff | 2026-08-19 |
| Ubuntu | [USN-8679-1](https://lwn.net/Articles/1090731/) | 14.04 16.04 18.04 20.04 22.04 24.04 | vim | 2026-08-25 |
| Ubuntu | [USN-8657-1](https://lwn.net/Articles/1089996/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | vim | 2026-08-21 |
| Ubuntu | [USN-8543-2](https://lwn.net/Articles/1089997/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | wget | 2026-08-20 |

### 커널 릴리스

#### 요약

- 안정 커널 릴리스 항목을 나열합니다.
- 각 항목은 원문의 게시 링크, 작성자, 날짜를 보존합니다.
- 버전 번호와 `rt` 표기는 원문 그대로 유지합니다.

- [Linux 7.1.10](https://lwn.net/Articles/1090100/) — Greg Kroah-Hartman, 8월 23일
- [Linux 6.18.46](https://lwn.net/Articles/1090101/) — Greg Kroah-Hartman, 8월 23일
- [Linux 6.12.105](https://lwn.net/Articles/1090102/) — Greg Kroah-Hartman, 8월 23일
- [Linux 6.6.153](https://lwn.net/Articles/1090103/) — Greg Kroah-Hartman, 8월 23일
- [Linux 6.1.184](https://lwn.net/Articles/1090104/) — Greg Kroah-Hartman, 8월 23일
- [Linux 5.15.217](https://lwn.net/Articles/1090105/) — Greg Kroah-Hartman, 8월 23일
- [5.15.216-rt98](https://lwn.net/Articles/1090325/) — Joseph Salisbury, 8월 22일
- [Linux 5.10.266](https://lwn.net/Articles/1090106/) — Greg Kroah-Hartman, 8월 23일

### 아키텍처별

#### 요약

- arm64, x86, AMD IOMMU, TDX 및 perf/KVM 관련 변경을 다룹니다.
- CPU 제어, crash hotplug, PMU 및 레지스터 샘플링 항목이 포함됩니다.
- 아키텍처와 기능 식별자는 원문 표기를 유지합니다.

- [arm64: CPU prefetch 및 캐시 modulation 제어 노출](https://lwn.net/Articles/1090574/) — Koba Ko, 8월 26일
- [crash: arm64 crash hotplug 지원 재구성 및 추가](https://lwn.net/Articles/1090752/) — Jinjie Ruan, 8월 26일
- [AMD IOMMU GAPPI 지원 추가](https://lwn.net/Articles/1090011/) — Sairaj Kodilkar, 8월 21일
- [x86: prctl을 통한 shstk 지원](https://lwn.net/Articles/1089784/) — Bill Roberts, 8월 18일
- [TDX module extension 활성화](https://lwn.net/Articles/1090008/) — Xu Yilun, 8월 21일
- [perf용 SIMD/eGPRs/SSP register 샘플링 지원](https://lwn.net/Articles/1090344/) — Dapeng Mi, 8월 24일
- [perf/KVM: x86 플랫폼용 PMU 분할 지원](https://lwn.net/Articles/1090321/) — Zide Chen, 8월 21일

### 빌드 시스템

#### 요약

- BPF selftest의 계층형 Makefile 빌드 재구성 항목입니다.
- 빌드 대상과 식별자는 원문 표기를 유지합니다.
- 아래 링크는 해당 패치 목록의 공개 LWN 항목입니다.

- [selftests/bpf: Makefile을 layered build로 재구성](https://lwn.net/Articles/1090356/) — Mykola Lysenko, 8월 22일

### 핵심 커널

#### 요약

- BPF, sysctl, coredump, tracing, scheduler 및 hrtimer 관련 항목을 포함합니다.
- 메모리 처리와 신호, 실행 및 스케줄링 동작 변경을 다룹니다.
- 각 항목의 작성자와 게시 날짜는 원문 그대로입니다.

- [bpf: linux_binprm용 user 메모리 access kfunc 추가](https://lwn.net/Articles/1089750/) — Anastasios Papagiannis, 8월 20일
- [sysctl: module alias 추가](https://lwn.net/Articles/1089727/) — Mauricio Faria de Oliveira, 8월 19일
- [cgroup: cpu.stat 및 io.stat를 BPF에 노출](https://lwn.net/Articles/1090006/) — Ziyang Men, 8월 20일
- [coredump: 요청별 메모리 유형 선택](https://lwn.net/Articles/1090020/) — Christian Brauner, 8월 21일
- [unwind_user: .eh_frame 처리 구현](https://lwn.net/Articles/1090319/) — Jens Remus, 8월 21일
- [tracing: wprobe: x86: watchpoint용 wprobe 추가](https://lwn.net/Articles/1090328/) — Masami Hiramatsu (Google), 8월 22일
- [재시작 불가 작업을 TIF_NOTIFY_SIGNAL이 중단하지 않도록 변경](https://lwn.net/Articles/1090354/) — Christian Brauner, 8월 24일
- [bpf: arena: fault-in 시 reclaim/OOM으로 메모리.max 처리](https://lwn.net/Articles/1090346/) — Jiayuan Chen, 8월 24일
- [coredump, 파일: 요청 시 파일 종료](https://lwn.net/Articles/1090374/) — Christian Brauner, 8월 24일
- [sched, steal_governor: preferred CPU 및 steal-driven vCPU backoff 도입](https://lwn.net/Articles/1090544/) — Shrikanth Hegde, 8월 25일
- [hrtimer: expiry injecting callback variant 추가](https://lwn.net/Articles/1090545/) — Andreas Hindborg, 8월 25일
- [sched/core: PROXY_EXEC의 sleeping-owner 처리 대안](https://lwn.net/Articles/1090749/) — K Prateek Nayak, 8월 26일
- [bpf: by-value return에서 arena pointer 허용](https://lwn.net/Articles/1090764/) — Yonghong Song, 8월 25일

### 개발 도구

#### 요약

- RV monitor, BPF JIT 검사, selftest 및 debugfs 관련 항목을 모읍니다.
- 테스트 출력과 플랫폼 지원, 테스트 인프라 변경이 포함됩니다.
- 기술 식별자는 번역하지 않았습니다.

- [rv: 예산 초과 task latency RV monitor 추가](https://lwn.net/Articles/1089726/) — wen.yang@linux.dev, 8월 20일
- [bpf: JITed program의 KASAN 검사 지원 추가](https://lwn.net/Articles/1090322/) — Alexis Lothoré (eBPF Foundation), 8월 22일
- [selftests/mm: TAP 출력 및 global-상태 수정](https://lwn.net/Articles/1090542/) — Song Hu, 8월 25일
- [nommu 플랫폼에서 kselftest 지원](https://lwn.net/Articles/1090548/) — Hajime Tazaki, 8월 25일
- [sched/debug: CPU별 debugfs 파일 도입](https://lwn.net/Articles/1090562/) — Aaron Tomlin, 8월 25일
- [configfs: 기본 selftest 추가](https://lwn.net/Articles/1090754/) — Breno Leitao, 8월 26일

### 장치 드라이버

#### 요약

- 전원, 그래픽, HID, 미디어, 네트워크, USB 및 오디오 드라이버 항목을 포함합니다.
- SoC, 센서, 컨트롤러 및 주변기기 지원 추가가 중심입니다.
- 아래 목록의 장치명과 하드웨어 식별자는 원문대로 보존합니다.

- [전원: 재설정: 추가 NVMEM recorder provider 용 PSCRR](https://lwn.net/Articles/1089725/) — Faruque Ansari, 8월 19일
- [drm/tyr: GPU 재설정 인프라](https://lwn.net/Articles/1089728/) — Onur Özkan, 8월 19일
- [추가 RZ/G3L PWRRDY 전원 시퀀싱 지원](https://lwn.net/Articles/1089730/) — Biju, 8월 19일
- [HID: asus: 추가 지원 용 ROG Ally handhelds](https://lwn.net/Articles/1089731/) — Denis Benato, 8월 19일
- [clk: 추가 지원 용 Airoha AN7583 클록](https://lwn.net/Articles/1089732/) — Christian Marangi, 8월 20일
- [net: wwan: 지원 DTR/RTS 에서 AT ports 통해 MHI IP_CTRL](https://lwn.net/Articles/1089733/) — Peter Hunt, 8월 20일
- [iio: 추가 Open Sensor Fusion IIO 드라이버](https://lwn.net/Articles/1089737/) — Jinseob Kim, 8월 20일
- [iio: dac: 추가 지원 용 AD5529R DAC](https://lwn.net/Articles/1089740/) — Janani Sunil, 8월 20일
- [media: stm32: dcmipp: 추가 지원 용 MP2x pixel pipes](https://lwn.net/Articles/1089741/) — Alain Volmat, 8월 20일
- [wifi: rtw88: 준비 용 RTL8723B/RTL8723BS](https://lwn.net/Articles/1089742/) — luka.gejak@linux.dev, 8월 20일
- [추가 Greybus Sotfsvc 및 UART Node 드라이버](https://lwn.net/Articles/1089743/) — Ayush Singh, 8월 20일
- [추가 RZ/G3L USB2.0 host 지원](https://lwn.net/Articles/1089744/) — Biju, 8월 20일
- [추가 pinctrl 지원 용 MSM8952](https://lwn.net/Articles/1089746/) — Muzaffer Kadir, 8월 20일
- [활성화 팬 모니터링 지원 용 Simatic IPC BX-59A](https://lwn.net/Articles/1089747/) — Benedikt Niedermayr, 8월 20일
- [추가 지원 용 MT6392 PMIC](https://lwn.net/Articles/1089748/) — Luca Leonardo Scorcia, 8월 20일
- [nfc: st-nci: Fairphone 5 NFC bring-up (ST21NFCD)](https://lwn.net/Articles/1089751/) — Kristian Brox, 8월 19일
- [media: i2c: 추가 onsemi AR0234 카메라 센서 드라이버](https://lwn.net/Articles/1089752/) — Alexander Shiyan, 8월 20일
- [ASoC: codecs: 추가 Nuvoton NAU83G60 오디오 codec 드라이버](https://lwn.net/Articles/1089753/) — Neo Chang, 8월 20일
- [USB4 모드 프로그래밍 용 QMMPHY 에서 X1E](https://lwn.net/Articles/1089782/) — Konrad Dybcio, 8월 20일
- [net: pse-pd: 추가 LTC4266 PSE 컨트롤러 드라이버](https://lwn.net/Articles/1089783/) — Kyle Swenson, 8월 20일
- [추가 Renesas RZ/G3L SD/eMMC 지원](https://lwn.net/Articles/1089785/) — Biju, 8월 20일
- [leds: 추가 IS32FL3207 컨트롤러 지원](https://lwn.net/Articles/1089786/) — Ahmad Byagowi, 8월 20일
- [inv_icm42600 드라이버 enhancements](https://lwn.net/Articles/1089789/) — Jean-Baptiste Maneyrol, 8월 20일
- [mmc: sdhci-cadence: 추가 SD6HC 지원 및 Agilex5 enablement](https://lwn.net/Articles/1089790/) — Tanmay Kathpalia, 8월 20일
- [iommu/riscv: 활성화 MSI remapping, IOMMU_DMA 및 VFIO](https://lwn.net/Articles/1090007/) — Andrew Jones, 8월 20일
- [mfd: nct6694: 리팩터링 transport 계층 및 추가 HIF (eSPI) 지원](https://lwn.net/Articles/1090009/) — a0282524688@gmail.com, 8월 21일
- [ASoC: 추가 ESS Technology ES9039Q2M codec 드라이버](https://lwn.net/Articles/1090010/) — Karl Asseily, 8월 21일
- [firmware: imx: 드라이버 용 NXP secure-enclave](https://lwn.net/Articles/1090012/) — pankaj.gupta@oss.nxp.com, 8월 21일
- [brcmfmac: 추가 FT/OKC roaming offload 지원](https://lwn.net/Articles/1090013/) — Jason Huang, 8월 21일
- [추가 초기 지원 용 Qualcomm SM7250 SoC](https://lwn.net/Articles/1090014/) — Sreeshankar K, 8월 21일
- [hwmon: 추가 Sensirion STS4x 온도 센서 지원](https://lwn.net/Articles/1090016/) — Alessandro Zini, 8월 21일
- [efi: mm/메모리-failure: 유지 하드웨어-poisoned pages 제외 의 다음 kexec](https://lwn.net/Articles/1090018/) — Breno Leitao, 8월 21일
- [spi: cadence-quadspi: 추가 PHY tuning 지원](https://lwn.net/Articles/1090019/) — Santhosh Kumar K, 8월 21일
- [phy: rockchip-samsung-dcphy: 추가 MIPI D-PHY receiver](https://lwn.net/Articles/1090021/) — Jason Yang, 8월 21일
- [iommu/riscv: 추가 하드웨어 dirty tracking 용 second-stage domains](https://lwn.net/Articles/1090023/) — fangyu.yu@linux.alibaba.com, 8월 21일
- [추가 RTC 지원 용 Renesas RZ/T2H 및 RZ/N2H SoCs](https://lwn.net/Articles/1090024/) — Prabhakar, 8월 21일
- [iio: adc: 추가 AD7768/AD7768-4 ADC 드라이버 지원](https://lwn.net/Articles/1090025/) — Janani Sunil, 8월 21일
- [추가 지원 용 CH1115 Controller](https://lwn.net/Articles/1090027/) — Nicolás Antinori, 8월 21일
- [추가 드라이버 용 Broadcom FacetimeHD 카메라](https://lwn.net/Articles/1090030/) — Jack Flusche, 8월 20일
- [media: ipu6: 추가 지원 용 ipu7 하드웨어](https://lwn.net/Articles/1090031/) — Antti Laakso, 8월 21일
- [추가 지원 용 Renesas RZ/G2M v3.0 (.k. R8A774A3) SoC](https://lwn.net/Articles/1090040/) — Ayman Chaudhry, 8월 21일
- [Apple SoC CIO (USB4/Thunderbolt) 재설정 컨트롤러](https://lwn.net/Articles/1090041/) — Sven Peter, 8월 21일
- [추가 초기 지원 용 Qualcomm Kuno SoC](https://lwn.net/Articles/1090042/) — Hardeep Sharma, 8월 21일
- [추가 지원 용 USB Type-C 에서 STM32MP25](https://lwn.net/Articles/1090043/) — Fabrice Gasnier, 8월 21일
- [소규모 Imagis 드라이버 리팩터링 및 지원 용 IST4050](https://lwn.net/Articles/1090320/) — Markuss Broks, 8월 22일
- [도입 MDSYNC 지원 용 CS35L45](https://lwn.net/Articles/1090323/) — Ricardo Rivera-Matos, 8월 21일
- [gpu: nova-core: 부팅 에서 r000 GSP firmware](https://lwn.net/Articles/1090324/) — John Hubbard, 8월 21일
- [iio: position: 추가 Rust 드라이버 용 ams AS5600](https://lwn.net/Articles/1090326/) — Muchamad Coirul Anwar, 8월 22일
- [arm64: dts: phy: st: usb: 추가 STM32MP2 USB 지원](https://lwn.net/Articles/1090327/) — Marek Vasut, 8월 22일
- [HID: ft260: 추가 UART 및 GPIO 지원, plus I2C fixes](https://lwn.net/Articles/1090329/) — Michael Zaidman, 8월 23일
- [drm/ssd130x: 추가 지원 용 Solomon SSD1351 OLED 컨트롤러](https://lwn.net/Articles/1090330/) — Amit Barzilai, 8월 23일
- [rtc: s35390a: 허용 사용 의 출력 pin 용 interrupt signal 1 용 wakealarm](https://lwn.net/Articles/1090334/) — Markus Probst, 8월 23일
- [RISC-V IOMMU HPM 지원](https://lwn.net/Articles/1090336/) — Zong Li, 8월 23일
- [추가 Aspeed AST2700 SDRAM EDAC 지원](https://lwn.net/Articles/1090337/) — Ryan Chen, 8월 24일
- [ASoC: qcom: 추가 QAIF 드라이버 용 Shikra 오디오 플랫폼](https://lwn.net/Articles/1090338/) — Harendra Gautam, 8월 24일
- [추가 지원 용 USB phys in IPQ9650](https://lwn.net/Articles/1090339/) — Varadarajan Narayanan, 8월 24일
- [추가 드라이버 용 NXP PCF8525 RTC](https://lwn.net/Articles/1090340/) — Shiv Prakash Gupta, 8월 24일
- [media: rockchip: 추가 JPEG decoder 드라이버](https://lwn.net/Articles/1090341/) — Sascha Hauer, 8월 24일
- [wifi: ath11k: airtime queue limits, fairness 및 드라이버 TXQ scheduler](https://lwn.net/Articles/1090342/) — Julius Bairaktaris, 8월 24일
- [media: rockchip: rkisp2: 추가 드라이버 용 ISP 에서 Rk3588](https://lwn.net/Articles/1090345/) — Paul Elder, 8월 24일
- [accel/rocket: RK3576 NPU (RKNN) enablement](https://lwn.net/Articles/1090347/) — Jiaxing Hu, 8월 24일
- [추가 Renesas RZ/G3E GPT 지원](https://lwn.net/Articles/1090350/) — Biju, 8월 24일
- [Subject: 추가 Lontium LT9611C(EX/UXD) MIPI DSI 에 HDMI 드라이버](https://lwn.net/Articles/1090352/) — mohit.dsor@oss.qualcomm.com, 8월 24일
- [추가 UALink 인프라 series 2](https://lwn.net/Articles/1090359/) — Alex Deucher, 8월 21일
- [eth: fbnic: 확장 hwmon 센서 지원](https://lwn.net/Articles/1090387/) — Zinc Lim, 8월 24일
- [iio: pressure: dps310: FIFO 및 triggered buffer 지원](https://lwn.net/Articles/1090400/) — Rupesh Majhi, 8월 24일
- [ALSA: usb-오디오: Topping M62's vendor 제어](https://lwn.net/Articles/1090401/) — Mikhail Gavrilov, 8월 25일
- [nvme-tcp: 병렬화 I/O queue connect](https://lwn.net/Articles/1090530/) — Surabhi Gogte, 8월 24일
- [추가 더 큰 페이지 size 지원 용 USB 오디오 offload 경로](https://lwn.net/Articles/1090531/) — Wesley Cheng, 8월 24일
- [만들기 SBR 작동 용 CXL Downstream Ports](https://lwn.net/Articles/1090532/) — Fabio M. De Francesco, 8월 25일
- [추가 PCIe 지원 용 Qualcomm Nord 플랫폼](https://lwn.net/Articles/1090533/) — Krishna Chaitanya Chundru, 8월 25일
- [thermal: 추가 지원 A9](https://lwn.net/Articles/1090537/) — Xianwei Zhao, 8월 25일
- [drm/panthor: Reduce dma_fence signalling latency](https://lwn.net/Articles/1090539/) — Boris Brezillon, 8월 25일
- [io: accel: mma8452: 허용 open drain interrupt pin 구성](https://lwn.net/Articles/1090540/) — Esben Haabendal, 8월 25일
- [drm: 추가 DRM 드라이버 용 GlandaGPU (VHDL soft-IP GPU)](https://lwn.net/Articles/1090550/) — Leander Kieweg, 8월 24일
- [Crescent Island PMT 지원](https://lwn.net/Articles/1090551/) — Michael J. Ruhl, 8월 24일
- [활성화 USB3 용 Qualcomm IPQ5018](https://lwn.net/Articles/1090547/) — George Moussalem, 8월 25일
- [hwmon: 추가 Minisforum UM780 XTX EC 모니터링 및 팬 제어](https://lwn.net/Articles/1090575/) — Sebastián Peyrott, 8월 25일
- [ASoC: qcom: 활성화 오디오 에서 stage-2 protected DSPs (mDSP)](https://lwn.net/Articles/1090576/) — Ajay Kumar Nandam, 8월 26일
- [net: phy: mediatek: 지원 EcoNet EN751221 gbit SoC PHY](https://lwn.net/Articles/1090580/) — Caleb James DeLisle, 8월 25일
- [추가 UCSI I2C transport 드라이버 용 ITE885x USB-C controllers](https://lwn.net/Articles/1090581/) — Edward Blair, 8월 25일
- [ZTE zx297520v3 클록 바인딩 및 드라이버](https://lwn.net/Articles/1090743/) — Stefan Dösinger, 8월 26일
- [crypto: cmh - 추가 Rambus CryptoManager Hub 드라이버](https://lwn.net/Articles/1090746/) — Alex Ousherovitch, 8월 25일
- [추가 지원 용 Broadcom BCM2712 IOMMU 드라이버 (Raspberry Pi 5)](https://lwn.net/Articles/1090747/) — Daniel Drake, 8월 25일
- [media: imx8-isi: 추가 i.MX952 ISI 지원](https://lwn.net/Articles/1090748/) — Guoniu Zhou, 8월 26일
- [추가 지원 용 NXP P3H2x4x I3C hub 드라이버](https://lwn.net/Articles/1090753/) — Lakshay Piplani, 8월 26일
- [usb: typec: tipd: 추가 sn201202x (ACE3) 지원](https://lwn.net/Articles/1090755/) — Sasha Finkelstein, 8월 26일
- [usb: 추가 지원 용 eUSB2v2 1024-byte Bulk MaxPacketSize](https://lwn.net/Articles/1090756/) — Pawel Laszczak, 8월 26일
- [활성화 cameras 에서 Dell Latitude 5285 2-in-1](https://lwn.net/Articles/1090757/) — Thierry Chatard, 8월 26일
- [media: 추가 Lenovo Yoga Book YB1-X91 카메라 지원](https://lwn.net/Articles/1090759/) — Maurizio Casciano, 8월 26일
- [ASoC: Intel: 추가 Lenovo Yoga Book RT5677 지원](https://lwn.net/Articles/1090760/) — Maurizio Casciano, 8월 26일
- [x86/usb: 추가 Yoga Book XMM7260 modem 전원 시퀀싱](https://lwn.net/Articles/1090761/) — Maurizio Casciano, 8월 26일
- [추가 S32N79RDB UFS 지원](https://lwn.net/Articles/1090762/) — Larisa Grigore, 8월 26일
- [misc: fastrpc: 추가 extended IOVA 매핑 지원](https://lwn.net/Articles/1090763/) — Vinayak Katoch, 8월 26일
- [wifi: rtw89: 갱신 RTL8922D 기능 및 설정, 및 활성화 P2P 장치](https://lwn.net/Articles/1090765/) — Ping-Ke Shih, 8월 26일
- [추가 지원 용 DU, LVDS 및 DSI 에서 Renesas RZ/G3L SoC](https://lwn.net/Articles/1090787/) — Biju, 8월 26일
- [iio: light: stk3310: 별-chip match data 및 STK36C61 지원](https://lwn.net/Articles/1090788/) — Jorijn van der Graaf, 8월 26일

### 장치 드라이버 인프라

#### 요약

- 전원 관리, LED, PCI, DMA, IOMMU 및 Rust 추상화 관련 항목입니다.
- 장치 종료와 인터커넥트, USB 드라이버 기반 변경도 포함합니다.
- 각 패치 제목은 기능 범위를 반영해 번역했습니다.

- [PM: QoS/pmdomains: 시스템 전체 PM의 resume latency 지원](https://lwn.net/Articles/1089724/) — Kevin Hilman (TI), 8월 19일
- [rust: leds: 추가 led classdev 추상화](https://lwn.net/Articles/1089729/) — Markus Probst, 8월 19일
- [leds: 추가 지원 용 하드웨어-initiated 하드웨어 제어 trigger transition](https://lwn.net/Articles/1089787/) — Rong Zhang, 8월 21일
- [shut down 장치 asynchronously](https://lwn.net/Articles/1090026/) — David Jeffery, 8월 21일
- [PCI/P2PDMA: 수정 ACS egress 제어 처리](https://lwn.net/Articles/1090318/) — Leon Romanovsky, 8월 21일
- [drm/fabric: scale-up accelerator interconnect용 벤더 중립 토폴로지 인프라](https://lwn.net/Articles/1090343/) — Konstantin Sinyuk, 8월 24일
- [swiotlb: 네트워크 소켓에서 swiotlb 복사 방지](https://lwn.net/Articles/1090372/) — Luigi Rizzo, 8월 24일
- [Rust: runtime PM 지원 추가](https://lwn.net/Articles/1090758/) — Beata Michalska, 8월 26일
- [iommu: 연속 MSI 매핑 지원 추가](https://lwn.net/Articles/1090777/) — Andrew Jones, 8월 26일
- [rust: usb: bulk-endpoint 드라이버용 host-side 추상화](https://lwn.net/Articles/1090779/) — Mike Lothian, 8월 26일
- [rust: USB display 드라이버용 core 추상화](https://lwn.net/Articles/1090780/) — Mike Lothian, 8월 26일

### 문서화

#### 요약

- scheduler 문서와 man-pages 릴리스 항목을 포함합니다.
- 문서 대상 식별자와 버전은 원문 표기를 유지합니다.
- 아래 링크는 공개 LWN 항목입니다.

- [sched: WF_SYNC wakeup 배치 의미론 문서화](https://lwn.net/Articles/1090607/) — Shubhang Kaushik (Ampere), 8월 25일
- [man-pages-6.19 릴리스](https://lwn.net/Articles/1090742/) — Alejandro Colomar, 8월 25일

### 파일 시스템 및 블록 계층

#### 요약

- FUSE, f2fs, Ceph, NVMe, VFS, SMB 및 NFS 관련 항목을 포함합니다.
- 캐시, I/O, 메타데이터, 압축 및 클라이언트 상태 변경을 다룹니다.
- 시스템 호출 및 플래그 식별자는 원문 그대로입니다.

- [fuse: 권한 있는 userspace server에 FUSE_SYNCFS 허용](https://lwn.net/Articles/1089749/) — Jimmy Zuber, 8월 20일
- [f2fs: metadata 캐시 도입](https://lwn.net/Articles/1089735/) — Chao Yu, 8월 20일
- [f2fs: buffered RWF_DONTCACHE 활성화](https://lwn.net/Articles/1089739/) — Wenjie Qi, 8월 20일
- [ceph: kclient에 'lazyio' mount option 추가](https://lwn.net/Articles/1089736/) — Xiubo Li, 8월 19일
- [jffs2: 모든 write 경로로 write verification 확장](https://lwn.net/Articles/1089745/) — zhouminqiang, 8월 20일
- [차단, nvme: 동일 LBA multipath limit stacking 지원](https://lwn.net/Articles/1090028/) — Yao Sang, 8월 21일
- [blk-cgroup: blkgs를 blkcg_mutex로 보호](https://lwn.net/Articles/1090332/) — Yu Kuai, 8월 23일
- [vfs: open*(2)에 O_CREAT|O_DIRECTORY 추가](https://lwn.net/Articles/1090333/) — Jori Koolstra, 8월 23일
- [ksmbd: Continuously Available (CA) share 지원 구현](https://lwn.net/Articles/1090335/) — Yunseong Kim, 8월 24일
- [fuse: 파일 확장 시 partial EOF 페이지를 0으로 초기화](https://lwn.net/Articles/1090370/) — Jimmy Zuber, 8월 24일
- [netfs: segmented bio_vec[] chain에서 folio 추적](https://lwn.net/Articles/1090371/) — David Howells, 8월 24일
- [fs/ceph: struct layout 최적화](https://lwn.net/Articles/1090388/) — Max Kellermann, 8월 24일
- [btrfs: xattr에 inode별 compression level 추가](https://lwn.net/Articles/1090549/) — koraynilay, 8월 25일
- [nfsd: Netlink로 NFSv4 client 상태 노출](https://lwn.net/Articles/1090538/) — Prabhakar Pujeri, 8월 25일
- [negative dentry 문제의 간단한 부분 수정](https://lwn.net/Articles/1090745/) — NeilBrown, 8월 26일
- [ceph: inline data 경로를 folio로 변환](https://lwn.net/Articles/1090744/) — Tal Zussman, 8월 25일
- [f2fs: writable 파일용 큰 folio 지원 및 최적화](https://lwn.net/Articles/1090750/) — Nanzhe Zhao, 8월 26일

### 메모리 관리

#### 요약

- memcg, folio, mglru, HugeTLB 및 swap 관련 항목을 포함합니다.
- 회수, compaction, 메모리 계정 및 guest memory 변경을 다룹니다.
- 커널 메모리 관리 식별자는 원문 표기를 유지합니다.

- [bpf: BPF 기반 선제적 memcg reclaim](https://lwn.net/Articles/1089738/) — Hui Zhu, 8월 20일
- [mm/huge_memory: folio split 정리 및 swapcache split 제한 해제](https://lwn.net/Articles/1089788/) — Kairui Song, 8월 21일
- [mm/vmscan: 유형별 node reclaim limit 준수](https://lwn.net/Articles/1090015/) — Ridong Chen, 8월 21일
- [mm/mglru: inc_min_seq() 가속 및 cold/hot 역전 수정](https://lwn.net/Articles/1090017/) — Barry Song (Xiaomi), 8월 21일
- [mm/cma: area별 counter로 cma allocation을 memcg에 계정](https://lwn.net/Articles/1090317/) — Eric Chanudet, 8월 21일
- [userfaultfd: uffd 모드를 VMA flag에서 분리](https://lwn.net/Articles/1090331/) — Mike Rapoport (Microsoft), 8월 23일
- [mm/fbatch: lru_add_drain() 및 _all() drain](https://lwn.net/Articles/1090351/) — Hugh Dickins, 8월 24일
- [mm/mglru: aging 중 빈 페이지 table walk 억제](https://lwn.net/Articles/1090353/) — Baoquan He, 8월 24일
- [mm: HugeTLB용 section 기반 vmemmap 최적화 도입](https://lwn.net/Articles/1090541/) — Muchun Song, 8월 25일
- [mm: compaction: mTHP 친화적 메모리 compaction](https://lwn.net/Articles/1090535/) — Bo Zhang, 8월 25일
- [가상 Swap Space (Swap Table Edition)](https://lwn.net/Articles/1090563/) — Nhat Pham, 8월 25일
- [guest_memfd: in-place 변환 지원](https://lwn.net/Articles/1090751/) — Ackerley Tng, 8월 26일

### 네트워킹

#### 요약

- 수신 스티어링과 TSO 세그먼트 수 관련 항목입니다.
- 네트워크 성능 및 전송 동작을 다룹니다.
- 기술 식별자는 원문대로 보존합니다.

- [psp: virt cookie를 Rx steering hint로 사용](https://lwn.net/Articles/1090357/) — Jakub Kicinski, 8월 22일
- [명시적 TSO segment 수](https://lwn.net/Articles/1090380/) — chia-yu.chang@nokia-bell-labs.com, 8월 24일

### 보안 관련

#### 요약

- BPF keyring, 서명 로더, X.509 CRL 및 SELinux 변경을 포함합니다.
- 암호화 바인딩 관련 Rust 항목도 나열합니다.
- 보안 메커니즘의 기술 식별자는 원문 표기를 유지합니다.

- [BPF keyring 및 signed loader ML-DSA 지원](https://lwn.net/Articles/1090355/) — Daniel Borkmann, 8월 21일
- [추가 X.509 CRL 지원](https://lwn.net/Articles/1090358/) — Timofei Novikov, 8월 22일
- [proc,security,selinux: SELinux가 /proc/self/mem의 FOLL_FORCE를 차단하도록 변경](https://lwn.net/Articles/1090577/) — Jann Horn, 8월 25일
- [rust: crypto: AES, CMAC, SHA-256, HMAC 및 RSA 바인딩](https://lwn.net/Articles/1090778/) — Mike Lothian, 8월 26일

### 가상화 및 컨테이너

#### 요약

- Hyper-V, KVM, nSVM, MSHV 및 TDX 관련 항목을 포함합니다.
- 게스트 IOMMU, nested guest 및 메모리 지원 변경을 다룹니다.
- 가상화 식별자는 원문 표기를 유지합니다.

- [Hyper-V: Linux 게스트용 반가상화 IOMMU 지원 추가](https://lwn.net/Articles/1090022/) — Yu Zhang, 8월 21일
- [KVM: nSVM: nested guest용 DecodeAssists 활성화](https://lwn.net/Articles/1090349/) — Tina Zhang, 8월 24일
- [mshv: MSHV root partition용 SEV-SNP 지원 추가](https://lwn.net/Articles/1090534/) — Wei Hu, 8월 25일
- [KVM: arm64: KVM_PRE_FAULT_MEMORY 지원 추가](https://lwn.net/Articles/1090564/) — Lorenzo Stoakes (ARM), 8월 25일
- [KVM: VMX: TDX vCPU를 vcpu_vmx로 해석하는 것을 방어](https://lwn.net/Articles/1090786/) — Sean Christopherson, 8월 26일

### 기타

#### 요약

- coredump, perf trace 및 Rust 소유권 타입 관련 항목입니다.
- 디버깅과 코어 덤프 처리, 언어 추상화 변경을 포함합니다.
- 각 링크의 작성자와 날짜는 원문 그대로입니다.

- [coredump: coredump 소켓에서 sparse coredump 생성 허용](https://lwn.net/Articles/1089734/) — Christian Brauner, 8월 20일
- [perf trace: 커널 가상 주소와 함수 포인터를 심볼화](https://lwn.net/Articles/1090005/) — Aaron Tomlin, 8월 20일
- [rust: 추가 `Ownable` trait 및 `Owned` 유형](https://lwn.net/Articles/1090348/) — Andreas Hindborg, 8월 24일

페이지 편집자: Joe Brockmeier
