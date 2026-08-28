# LWN.net Weekly Edition 2026년 8월 20일 — 한국어 기술 번역

- **원문 공개 Bigpage:** https://lwn.net/Articles/1088565/bigpage
- **선정 기준:** 최신 2026년 8월 27일 호는 유료 공개 가능성이 있어 번역하지 않았다. 그 직전인 2026년 8월 20일 호 중 공개 접근이 확인된 Bigpage만 사용했다.
- **생성 시각(UTC):** 2026-08-28T00:55:40Z
- **범위:** 공개 페이지에 표시된 기사·단신·공지·보안 업데이트·커널 패치 목록을 원문 순서와 링크/이미지/표/코드를 보존하여 번역했다. 로그인 전용 또는 유료 전용 콘텐츠는 포함하지 않았다.

## 전체 기술 요약

- Debian은 프로젝트 차원의 LLM 사용 원칙을 놓고 여덟 가지 선택지를 투표에 부쳤으며, 개발 공동체의 규범·재현성·환경 비용 논의가 배포판 거버넌스와 연결된다.[^report-debian]
- Python `pathlib`는 문자열 경로보다 의도를 명확하게 표현하고 OS별 경로 규칙을 안전하게 다루는 객체 모델을 제공한다.[^report-pathlib]
- bootstrappable build는 컴파일러와 도구 체인을 신뢰할 수 있는 작은 seed에서 재구성해 공급망 신뢰의 출발점을 좁힌다.[^report-bootstrap]
- Fedora의 AF_ALG 단계적 제한, Arm 128-bit page-table 논의, BPF 지속 테스트는 커널 API·메모리 확장·안정 브랜치 검증이 배포 운영과 직접 맞닿아 있음을 보여 준다.[^report-kernel]
- AMD 메모리 컨트롤러의 보호 우회 가능성 및 배포판 보안 공지는 펌웨어·권한 경계·신속한 업데이트를 함께 점검해야 한다는 신호다.[^report-security]
- 커널 패치 목록은 파일시스템·메모리 관리·네트워킹·가상화·드라이버의 진행 중인 변경을 운영자가 추적할 수 있는 주간 레이더로 보아야 한다.[^report-patches]

## 주요 기사 다이제스트

이 보고서는 아래 핵심 기사와 이어지는 단신·공지·보안·커널 패치를 **완전 번역**한다. 각 기사 제목 바로 아래의 `요약`은 빠른 훑어보기용이며, 본문은 원문의 순서와 Markdown 구조를 보존한다.

### 주요 읽을거리

- **Debian의 LLM 사용 투표** — 패키지·커뮤니티·의사결정에서 생성형 AI 사용을 둘러싼 규범 선택.
- **`pathlib` 경로 표현** — 문자열 조작 오류를 줄이고 파일 경로 조합을 읽기 쉽게 만드는 Python 표준 라이브러리.
- **Bootstrappable build** — Trusting Trust 문제를 줄이기 위한 최소 시드와 재현 가능한 빌드 체인.
- **AF_ALG 종료 준비** — 범용 배포판에서 커널 암호화 API를 노출하는 방식의 보안·호환성 재검토.
- **Arm 128-bit page table** — 대규모 주소 공간과 페이지 테이블 오버헤드 사이의 아키텍처 설계 논의.
- **BPF CI와 stable kernel** — 새 BPF 기능뿐 아니라 유지보수 브랜치에서의 지속적인 회귀 검증 필요성.

## 완전 한국어 번역

# 2026년 8월 20일자 LWN.net 주간판

원본 공개 큰 페이지: https://lwn.net/Articles/1088565/bigpage

### [2026년 8월 20일자 LWN.net 주간판에 오신 것을 환영합니다](https://lwn.net/Articles/1089553/)

#### 요약

- 이번 호는 LLM 사용 정책, Python 경로 표현, 부트스트랩 가능한 빌드 등을 다룹니다.
- 커널 측면에서는 AF\_ALG, 128비트 페이지 테이블, BPF 테스트, 7.2 개발 통계가 주요 주제입니다.
- 커뮤니티 단신과 공지 페이지도 함께 제공합니다.

이번 호에는 다음과 같은 특집 콘텐츠가 실려 있습니다:

- [LLM
  사용에 관한 투표에서 여덟 가지 선택지를 검토하는 Debian](https://lwn.net/Articles/1087134/): 오랜 논의 끝에 Debian 개발자들은 프로젝트가 LLM 기반 도구[^c01-llm] 사용에 대해 어떤 입장을 취할지 투표하고 있습니다.
- [pathlib를 사용해 Python 경로 표현하기](https://lwn.net/Articles/1088781/):
  Trey Hunner는 Python 개발자들이 파일시스템 경로[^c01-filesystem-path]를 문자열로 표현하는 일을 그만두기를 바라고 있습니다.
- [부트스트랩 가능한 빌드: 방법과 이유](https://lwn.net/Articles/1088279/):
  아주 작은 시드로부터 현대적인 Linux 사용자 공간[^c01-linux-userspace]을 빌드합니다.
- [AF\_ALG의 종말을 준비하는 Fedora](https://lwn.net/Articles/1088489/):
  곧 출시될 Fedora 45는 Crypto API[^c01-crypto-api]에 대한 커널의
  사용자 공간 인터페이스(AF\_ALG)[^c01-af-alg] 사용을 제한할 예정입니다.
- [Arm용 128비트 페이지 테이블](https://lwn.net/Articles/1088125/): 72PB의 RAM이
  충분하지 않을 경우를 대비해 Arm에서 128비트 PTE[^c01-pte] 지원을 추가하는 패치
  시리즈입니다.
- [BPF, 지속적 테스트, 그리고 안정 커널](https://lwn.net/Articles/1087823/): 안정 커널[^c01-stable-kernel]을 위한 BPF[^c01-bpf] 테스트 인프라의 현황 업데이트입니다.
- [7.2 커널의 개발 통계](https://lwn.net/Articles/1088776/): 커널 역사상 가장 분주했던 개발 주기 가운데 하나를 살펴봅니다.

이번 주 판에는 다음과 같은 내부 페이지도 포함되어 있습니다:

- [단신](https://lwn.net/Articles/1088567/): 커뮤니티 전반의 짧은 뉴스 항목입니다.- [공지](https://lwn.net/Articles/1088568/): 뉴스레터, 콘퍼런스, 보안 업데이트, 패치 등입니다.

이번 호를 즐겨 주시기를 바라며, 언제나처럼 LWN.net을
후원해 주셔서 감사합니다.

[댓글(게시된 댓글 없음)](https://lwn.net/Articles/1089553/#Comments)

[^c01-llm]: LLM(대규모 언어 모델)은 대량의 텍스트·코드 데이터로 학습되어 생성·요약·분석 등에 쓰이는 모델이다.
[^c01-filesystem-path]: 파일시스템 경로는 파일이나 디렉터리의 위치를 식별하는 문자열 또는 경로 객체이며, `pathlib`는 이를 운영체제별 규칙에 맞게 다룬다.
[^c01-linux-userspace]: Linux 사용자 공간은 커널 위에서 실행되는 셸, 라이브러리, 명령줄 도구와 서비스 등으로 구성된다.
[^c01-crypto-api]: Linux Crypto API는 커널 내부와 사용자 공간에서 암호 알고리즘과 가속기를 사용할 수 있게 하는 인터페이스 모음이다.
[^c01-af-alg]: AF_ALG는 Linux 소켓 주소 계열을 통해 사용자 공간 프로그램이 커널 Crypto API를 사용할 수 있게 하는 인터페이스다.
[^c01-pte]: PTE(Page Table Entry)는 가상 메모리 페이지를 물리 메모리에 매핑하고 권한 등의 속성을 담는 페이지 테이블 항목이다.
[^c01-stable-kernel]: 안정 커널은 새 기능보다 검증된 버그 수정의 백포트를 중심으로 유지되는 Linux 커널 릴리스 계열이다.
[^c01-bpf]: BPF는 커널에서 제한된 프로그램을 안전하게 실행해 관찰, 네트워킹, 보안 정책 구현 등에 사용하는 기술이다.

---

### [데비안, LLM 사용에 관한 투표에서 여덟 가지 선택지를 검토하다](https://lwn.net/Articles/1087134/)

글: **Joe Brockmeier**
2026년 8월 19일

#### 요약

- 데비안 프로젝트는 LLM을 이용해 만든 기여를 어떻게 다룰지 여덟 개의 안건으로 투표하고 있다.
- 안건은 LLM 기여 전면 금지부터 조건부 허용, 인간이 작성한 결과물만 직접 기여로 허용하는 방안까지 다양하다.
- 저작권, 품질, 숙련도 저하, 환경 영향이 논쟁의 핵심 쟁점이다.
- 콘도르세 방식 투표 결과와 무관하게, 이 문제는 다시 부상할 가능성이 크다.

데비안 프로젝트는 프로젝트에 기여할 때 [대규모 언어 모델의 사용](https://lwn.net/ml/all/an-mRkddZVaNW3CT%40roeckx.be/)(LLM)[^c02-llm]을 두고 투표하고 있다. Matthias Geiger가 7월 말에 제출한 [첫 번째 제안](https://lwn.net/ml/all/til24c.3ns3jl2mkmzmn@riseup.net/)은 LLM이 만들었거나 LLM의 도움을 받아 만든 모든 데비안 기여를 명시적으로 금지했을 것이다. 이 제안은 격렬한 논쟁과 대체 제안의 홍수를 촉발했다. 이제 데비안 개발자들은 LLM 지원 기여를 금지하는 방안부터 명시적으로 승인하는 방안까지, 총 [여덟 개의 제안](https://www.debian.org/vote/2026/vote_002)에 대해 투표하고 있다. 여기에는 데비안이 합의된 정책을 갖지 않게 되는 표준 선택지인 “위 항목 모두 아님”도 포함된다.

#### 데비안과 AI

Fedora와 [Fedora](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/), [Gentoo](https://wiki.gentoo.org/wiki/Project:Council/AI_policy) 같은 다른 배포판은 AI 지원 기여에 관한 정책을 정했지만, 데비안은 결정을 미뤄 왔다. 논의가 부족해서는 아니었다. 이 주제는 수년에 걸쳐 여러 차례 제기되었으나 해결되지 않았다.

2024년에 Tiago Bortoletto Vaz는 AI 생성 콘텐츠 사용 때문에 데비안이 “이미 부정적인 결과에 직면하고 있다”고 [우려](https://lwn.net/ml/all/3qxsesyoouxh2h6fodosnln4wsyl3tpmnbcu6pqzekqkz6k577%40a2gos5jbaowf/)했고, 이 주제에 관한 총회 결의안(GR)[^c02-gr] 가능성에 앞서 데비안 개발자들의 의견을 모으고자 했다. [논의](https://lwn.net/Articles/972331/)를 거친 뒤 그는 생성형 AI 사용에 관한 “공식적인 데비안 입장에 대한 합의와는 거리가 멀다”고 [결론](https://lwn.net/ml/all/51fc56869829fe76d00c610238f9b425@debian.org/) 내렸고, GR을 추진하지 않았다.

2026년 2월 Lucas Nussbaum은 데비안이 AI 지원 기여를 허용하자고 제안하면서 이 주제에 관한 [또 다른 논의](https://lwn.net/ml/all/aZY_P6jA8cGYkev2%40grub.nussbaum.fr/)를 시작했다. 그는 AI를 썼다고 밝힌 사람들이 “AI를 격렬하게 거부하는 한 무리의 사람들”에게 공격받고 있다고 [말](https://lwn.net/ml/all/aZbUjl9Mb2752MOY@grub.nussbaum.fr/)했으며, 데비안이 앞으로 나아갈 수 있도록 중간 지점을 찾고 싶었다. 그에 따른 [논의](https://lwn.net/Articles/1061544/)는 그의 [표현](https://lwn.net/ml/all/aabk25lxsVdikvQd@grub.nussbaum.fr/)대로 “대체로 문명적이고 흥미로웠고”, 그는 결국 GR이 필요하지 않을 수도 있다고 생각했다.

#### 이제는 때가 되었다

지난달 Geiger는 결국 필요하다고 판단했다. 그는 “생성형 AI와 LLM 사용에 관해 데비안이 입장을 표명할 때”라고 말했다. 이 주제는 이미 상세히 논의되었으므로, 다른 이들이 그랬던 것처럼 반응을 살피는 대신 공식 GR 제안을 곧바로 제출하기로 했다. 둑이 무너지자 제안들이 쏟아졌다. 전체적으로 데비안 개발자가 검토할 제안은 아래에 요약한 여덟 가지와 “위 항목 모두 아님”이다.

1. [사회 계약을 통해 데비안에 대한 LLM 기여 금지](https://www.debian.org/vote/2026/vote_002#texta). Geiger의 선택지다. [데비안 사회 계약](https://www.debian.org/social_contract)을 수정하여 LLM이나 다른 생성형 AI 도구를 사용해 만든 모든 데비안 기여를 명시적으로 금지한다. LLM이나 AI 관련 소프트웨어를 사용하는 업스트림 프로젝트에는 적용되지 않는다(따라서 AI 관련 개발용 애플리케이션을 패키징하는 일은 영향을 받지 않는다).
2. [조건부 AI 지원 기여 허용](https://www.debian.org/vote/2026/vote_002#textb). Nussbaum의 선택지다. 기여자가 기술적 타당성, 보안, 라이선스 준수 등에 대해 전적인 책임을 지는 것을 포함한 조건을 따른다면 AI 지원 기여를 명시적으로 허용한다. 또한 “기여의 상당 부분이 도구에 의해 생성되었거나 실질적인 도움을 받았다면” 공개할 것을 요청하지만 요구하지는 않는다. 공개 형식은 기여자에게 맡긴다.
3. [실용적인 범위에서 LLM 거부, 행동 강령 갱신](https://www.debian.org/vote/2026/vote_002#textc). Ian Jackson이 제안한 이 선택지는 [데비안 행동 강령](https://www.debian.org/code_of_conduct)을 수정하여 버그 보고서, 이메일, Salsa에서의 토론, 심지어 Planet Debian에 수집되는 블로그 게시물 같은 “사람에게 보내는 메시지”를 만드는 데 LLM을 쓰지 못하게 한다. 기여자에게 “데비안 작업에서 LLM 사용을 피하라”고 요청하지만, LLM 출력물을 완전히 금지하는 일은 비현실적임을 인정한다.
4. [데비안 전용 작업에 AI 기여 수용](https://www.debian.org/vote/2026/vote_002#textd). Pierre-Elliott Bécue가 제안한 이 선택지는 제출자에게 책임을 지우는 여러 조건 아래 생성형 AI 도구가 만들었거나 이를 사용해 만든 기여를 명시적으로 허용한다.
5. [생성형 AI의 책임 있는 사용](https://www.debian.org/vote/2026/vote_002#texte). Marc Haber의 선택지에 따르면, 데비안은 데비안에서 생성형 AI 도구 사용을 지지하지도 금지하지도 않는다는 입장문을 내고, 그러한 도구 사용은 “데비안 기여자에게 이미 기대되는 기준을 넘어 특별 규칙의 대상도 아니고, 그 규칙에서 면제되는 것도 아니다”라고 밝힌다.
6. [생성형 AI에 대한 신중한 접근](https://www.debian.org/vote/2026/vote_002#textf). Tobias Frost가 제안했다. 채택되면 프로젝트는 기여자에게 “실용적인 곳에서는 생성형 AI 사용을 피하고 AI 생성 출력보다 인간의 저작, 협업, 기술적 이해를 우선할 것”을 권장하는 입장문을 낸다. 그러나 생성형 AI 사용을 금지하지는 않으며, 데비안의 “높은 품질 가치”를 지킬 개발자들을 프로젝트가 신뢰한다는 점을 확인한다.
7. [데비안은 인간이 만든다](https://www.debian.org/vote/2026/vote_002#textg). Gard Spreemann이 낸 이 제안은 [GCC 프로젝트의 AI 정책](https://gcc.gnu.org/ai-policy.html)과 Rust 언어 팀의 [rust-lang/rust 정책](https://forge.rust-lang.org/policies/llm-usage.html)에서 영감을 받았다. 생성형 AI 도구의 출력을 직접 기여로 제출하는 것은 허용하지 않지만, 기여자가 그러한 도구를 “탐색, 조사, 분석, 비평 등을 위한 [보조] 도구”로 쓰는 것은 허용한다.
8. [LLM 사용을 피하자: 기후 파괴는 타협 불가 사안이다](https://www.debian.org/vote/2026/vote_002#texth). Holger Levsen의 선택지는 환경적 근거와 “중대한 윤리적, 법적, 기술적, 사회적 우려”를 바탕으로 LLM에 반대하는 입장문을 데비안이 내게 한다. 그러나 LLM 사용은 “탐지하기 어려울 수 있으며, 불가능할 수도 있다”는 점을 인정한다. 따라서 이는 입장문일 뿐이다. 데비안 기여에서 LLM 사용을 금지하지는 않는다.

데비안은 다수 선호 선택지를 찾기 위해 [콘도르세 방식](https://en.wikipedia.org/wiki/Condorcet_method)[^c02-condorcet]으로 투표하므로, 유권자는 하나만 선택하는 대신 선호 순서대로 선택지를 순위 매긴다. Geiger의 선택지는 사회 계약을 수정하므로 통과하려면 3 대 1의 다수가 필요하다.

#### 논의

오늘날 LLM 사용 논쟁에 빠져들지 않고 오픈 소스 프로젝트에 참여하기는 어렵고, 어쩌면 불가능하다. 데비안의 논의에서 나온 입장과 주장은 대부분의 독자에게 익숙할 법하다. 예를 들어 코드 저작권과 관련해 Geiger는 LLM 출력물의 저작권 상태에 “막대한 불확실성”이 있다고 주장했다. 그는 LLM 생성 코드가 [데비안 자유 소프트웨어 지침](https://www.debian.org/social_contract#guidelines)(DFSG)[^c02-dfsg]을 어떻게 준수할 수 있는지 알 수 없었다. “학습 데이터로 인한 라이선스 의무가 없다는 것을 100% 확신할 수 없다면, 함수를 생성하게 해서는 안 된다.”

다른 이들은 LLM이 데비안에 위험을 초래하거나 DFSG를 위반한다는 주장에 설득되지 않았다. Russ Allbery는 커널을 비롯한 데비안의 많은 업스트림 프로젝트가 “이 우려들은 아무것도 중요하지 않으며 LLM 출력물 주변의 모든 라이선스 문제를 무시하겠다고 결정했다”고 [지적](https://lwn.net/ml/all/87ik66kgm9.fsf@hope.eyrie.org/)했다. 이미 돌이킬 수 없는 일이었다고 그는 말했다. Ted Ts'o는 “저작권 문제가 없다고 믿는다고 인증하는 데 전적으로 만족한다”고 [말](https://lwn.net/ml/all/amF9Zk40oBJ3wUVX@mit.edu/)했다. 그는 [Stack Overflow](https://stackoverflow.com/)에서 예시를 검색한 뒤 코드를 작성할 수 있는 인간보다 LLM 출력물에 저작권 불확실성이 더 크지 않다고 주장했다.

Simon Richter는 미국 법 체계가 LLM 출력물은 “학습 데이터와 무관하고 저작권 보호 대상이 아니다”라고 판정할 것으로 예상한다고 [말](https://lwn.net/ml/all/d1f2c0a8-537d-406d-947e-6e9f60273439@debian.org/)했다. 그러나 그는 법적 타당성 때문이 아니라, 저작권 문제로 LLM 출력물을 배포할 수 없다고 판단하는 결과에 맞서 “비싼 변호사들”이 일할 것이기 때문에 그 결론에 도달했다.

품질 또는 품질 부족이라는 주제도 길게 다뤄졌다. “데비안 전용 작업에 AI 기여 수용”이 된 Bécue의 투표안 [첫 초안](https://lwn.net/ml/all/87se5bj5jk.fsf@debian.org/)에는 처음에 AI 보조자에게 커밋을 푸시하거나 패키지를 업로드하게 하는 일을 특정하여 금지하는 조항이 있었다. Nussbaum은 이것이 개인 작업 흐름에 자의적인 제약을 더한다고 [불평](https://lwn.net/ml/all/amHAOAfFq4PoC7I9@grub.nussbaum.fr/)했다. 로컬 에이전트에게 커밋하고 브랜치로 푸시하라고 요청하는 것이 무슨 문제냐고 물었다.

이어진 공방에서 Bécue는 LLM을 매일 사용하지만, “도구가 더 자동화되고 더 빠르게 움직일수록 더 많은 안전망이 필요하다”고 [말](https://lwn.net/ml/all/87ecgtk85p.fsf@debian.org/)했다. 인간이 저품질 작업을 하지 않는다는 주장이 아니라, 자동화 시스템이 더 많은 양의 그런 작업을 푸시하는 일을 막고 싶었다는 것이다. Haber는 사람들이 어차피 저품질 작업을 할 것이라면 LLM을 써도 되게 해야 한다고 [응답](https://lwn.net/ml/all/amI8v_ddbmJG71bJ@torres.zugschlus.de/)했다.

> 어차피 형편없는 일을 할 거라면, 왜 형편없는 일을 하는 데 도움을 받지 못하게 해야 합니까? 나쁜 사람들은 AI의 도움을 받아 형편없는 일을 할 것이고, 좋은 사람들은 자신이 선택한 도움을 쓸 수 있다면 형편없는 일을 덜 만들 것입니다.

Bécue는 그것이 “10배 더 많은 형편없는 결과물을 10배 더 빠르게 만들어내며, 이는 상당한 영향을 주고 더 큰 부담을 낳을 것”이라고 [말](https://lwn.net/ml/all/87zezhiq1u.fsf@debian.org/)했다. 또 다른 메시지에서 그는 자신이 아는 생성형 AI 사용자 대부분이 “AI가 작성한 코드의 절반도 읽지 않는다”고 [말](https://lwn.net/ml/all/87ldb1ict0.fsf@debian.org/)했으며, 이들이 이미 스스로 코드를 작성하는 데 어려움을 겪고 있다고 경고했다.

그러나 Matthias Urlichs는 품질에 관한 Bécue의 우려를 공유하지 않았다. 그는 자신의 패키징이 LLM에게 맡기기 시작한 뒤 크게 좋아졌으며, 데비안에 형편없는 결과물이 100배나 더 많아질 것이라고는 믿지 않는다고 [말](https://lwn.net/ml/all/3847f107-f59a-4a13-9e2a-3f6f07cae401@urlichs.de/)했다.

> 반대로, LLM이 명확한 가치를 더할 수 있는 활용 사례가 몇 가지는 즉시 떠오릅니다. 이를테면 재현 가능한 빌드 실패를 추적하는 일입니다. 또는 새 패키지가 추가하려는 기능을 이미 수행하는 기존 소프트웨어를 찾기 위해 [[Intent to Package](https://wiki.debian.org/ITP) 버그]를 거르는 일도 있습니다. NEW 대기열의 패키지를 검사하는 데 도움을 주거나, Rust, Go, Python 및/또는 Node 패키지의 우리 클론을 최신 상태로 유지하는 데 도움을 줄 수도 있습니다. 솔직히 말해 이는 데비안에서 가장 지루하고 보람도 적은 작업 중 하나입니다.

#### 컴파일러와 계산기

Ts'o는 LLM에 의존하는 사람들이 코딩 방법을 잊을 수 있다는 우려에 [논평](https://lwn.net/ml/all/amNuy61exc4fa9Wr@mit.edu/)했다. 그는 계산기가 암산할 수 있는 사람의 수를 줄였고, 컴파일러가 어셈블리 언어를 잘 작성하는 사람을 확실히 줄였다는 점을 인정했다. “하지만 이는 더 이상 중요하지 않은 특정 기술에 사람들이 덜 능숙해지는 문제에 가깝고, ‘인지적 쇠퇴’라는 더 일반적인 주장에 관한 문제는 아니라고 생각합니다.”

Adrian Bunk는 데비안에 더 가까운 사례로 데비안 패키지 빌드용 [debhelper](https://www.man7.org/linux/man-pages/man7/debhelper.7.html) 도구[^c02-debhelper]를 [언급](https://lwn.net/ml/all/amN-PIHr_os3np0t@localhost/)했다. 그는 이제 데비안 개발자들 사이에 데비안 패키지 빌드 내부 작동에 대한 지식 부족이 분명히 존재하며, 그 결과 개발자들이 “자신의 패키지에서 문제를 디버그하고 고치는 방법을 모르는 경우가 흔하다”고 말했다. Bunk와 Ts'o는 이 숙련도 상실 사례들을 LLM 사용에 반대하는 논거가 아니라 찬성하는 논거로 제시했다.

그러나 Bécue는 설득되지 않았다. 그는 Ts'o에게 [답하며](https://lwn.net/ml/all/87mrvgxfpr.fsf@pimeys.fr/) 계산기 비교에는 “일정한 장점이 있지만, 그래도 좋은 비교는 아니다”라고 했다. 사람들은 문제를 비판적으로 생각하는 능력을 먼저 기르지 않은 채 LLM을 찾게 될 것이며, 그 때문에 “서비스가 갑자기 사라지는 상황에도 취약하고, 쓰레기를 먹여도 그 사실을 전혀 깨닫지 못하게 된다”고 우려했다.

#### 환경 영향

LLM의 환경 영향은 논의에서 지배적인 주제였다. Bas Wijnen은 다른 이들이 LLM이 “우리 생태계를 파괴한다”는 데 동의하면서도 사용을 고려할 때 타협 불가 사안으로 보지 않는 이유를 이해할 수 없다고 [말](https://lwn.net/ml/all/fa69b7c0-c1a8-4386-b27b-b8bd16e1ea17@debian.org/)했다. 그가 그 지점에서 본 유일한 응답은 “다른 활동도 기후에 나쁘다(어떤 것은 더 나쁘다)”는 것이었고, 그는 이를 합리적인 논거로 보지 않았다.

> 모든 사용자는 이 행성에 살고 있으므로, 이 행성을 보호하는 일은 그들에게 생사가 걸린 문제입니다. 다시 말해 데비안 작업 중 기후 변화처럼 큰 문제를 염려하는 일은 (논의의 다른 곳에서 제안되었듯이) 사회 계약을 위반하는 것이 아닙니다. 반대로, 사회 계약은 우리에게 기후 변화를 염려하고 가능한 한 막아야 한다고 요구한다고 주장합니다.

Nussbaum은 기후 변화 주제를 경시하는 것은 아니지만, LLM만 골라내는 것은 “기후 변화 영향에 관한 합리적 논의라기보다 AI 때리기처럼 들린다”고 [답](https://lwn.net/ml/all/anyUL-S4XnXY5ebF@grub.nussbaum.fr/)했다. 그는 데비안이 더 적은 패키지를 빌드하고, 많은 재빌드를 요구하는 대규모 QA 활동을 중단하는 등 다른 방식으로 환경 영향을 줄일 수 있으며, DebConf를 운영하는 방식을 바꿔 데비안의 “여행 유발 CO2”를 줄일 방안도 제시했다. “데비안은 왜 Debconf를 위해 인도, 한국, 아르헨티나 또는 일본까지 여행하라고 나를 장려하면서, 동시에 AI 보조를 쓰는 것은 받아들일 수 없다고 결정합니까?”

Ts'o는 [무료 맥주 의미의 무료 LLM에 관한 메시지](https://lwn.net/ml/all/anfgUPNbV1uM1hzU@mit.edu/)의 추신에서 환경 영향 우려는 단지 “누군가가 다른 이유로 이미 정한 입장을 정당화하기 위한 구실”이라고 제안했다. Didier ‘OdyX’ Raboud는 Ts'o 유형의 주장이 “부적절하거나 악의적”이라고 [응답](https://lwn.net/ml/all/5742777.MHq7AAxBmi@turnagra/)했다. 그의 우려는 질의 하나당 생태 영향이 아니라 LLM 산업 전체의 효과였다.

> AI 기업은 우리 사회의 필수 기능이 아닙니다. LLM을 학습시키기 위해 AI 기업이 책을 파괴하도록 내버려 둘 필요는 없습니다 [[0]](https://en.wikipedia.org/wiki/Project_Panama). 데이터센터 건설이 지역 전력망이나 수도망에 부담을 주거나 지역 온도를 높이게 할 필요도 없습니다. 유럽과 북미 전역에서 극심한 가뭄과 산불이 이어지고 소방, 기후 행동 등에 (공공) 자금이 절실히 부족한 여름에, AI 기가팩토리에 300억 유로를 투자하기로 결정하는 일 [[1]](https://digital-strategy.ec.europa.eu/en/news/eu-launches-ai-gigafactories-call-boost-europes-computing-capacity-and-unlock-more-eu30-billion) \_는\_ 우리 “인류 전체”가 하는 선택이며, 나는 그것이 전혀 옳지 않다고 생각합니다.

데비안 개발자들이 주고받은 수십 개 메시지가 패키지 빌드를 LLM에게 도움받아 요청하는 것보다 더 많은 에너지를 썼는지 적은 에너지를 썼는지는 분명하지 않다. 하지만 논의 중 마음을 바꾼 사람은 거의 없었거나 전혀 없었다는 점은 분명하다.

#### 투표

물론 데비안은 이전에도 분열적인 결정을 다뤄 왔다. 예를 들어 프로젝트는 기본 init 시스템[^c02-init] 선택 문제로 한동안 [고심](https://lwn.net/Articles/583182/)하다가 2014년 2월 [데비안 기술 위원회](https://lwn.net/Articles/585319/)가 결정했다. 이 주제는 2014년 10월 [GR로 다시 고개를 들었고](https://lwn.net/Articles/618277/), [결과](https://www.debian.org/vote/2014/vote_003#outcome)는 GR이 필요하지 않다는 것이었다.

“[init 시스템 다양성](https://lwn.net/Articles/804254/)” 형태의 init 논쟁은 2018년에 [재점화되었고](https://lwn.net/Articles/770093/), 2019년 말에는 [GR로 투표에 부쳐졌다](https://lwn.net/Articles/806332/). 결국 데비안은 [다른 대안을 탐색하는 지원과 함께 systemd를 선택했다](https://www.debian.org/vote/2019/vote_002#outcome). init 논쟁은 강한 감정과 격한 말을 불러냈지만, 장기적으로 데비안에 큰 해를 끼친 것으로 보이지는 않는다.

선택지 수와 그중 여러 개가 성격상 비슷하다는 사실을 고려하면 어떤 제안이 이길지 추측하기 어렵다. 하지만 역사가 길잡이가 된다면, 투표 뒤 프로젝트는 털고 일어나 다시 일할 가능성이 크다. 다만 모든 이야기가 끝나기 전 이 주제가 다시 끓어오를 수도 있다.

투표 기간은 8월 15일에 시작되어 8월 28일까지 이어진다. 논의에 참여한 사람은 꽤 많았지만, 실제로 의견을 낸 개발자는 유력 투표자 수보다 훨씬 적었다. [투표 집계표](https://vote.debian.org/~secretary/gr_llm/)에 따르면, 투표 자격이 있는 1,000명 이상의 유권자 중 이미 130명 넘는 개발자가 투표했다.

어느 선택지가 이기든, 장기적으로 프로젝트에 더 나은 결과가 되기를 바란다.

[댓글(114개 게시됨)](https://lwn.net/Articles/1087134/#Comments)

[^c02-llm]: **대규모 언어 모델(LLM)**은 방대한 텍스트 데이터로 학습되어 자연어와 코드를 생성·분석하는 생성형 AI 모델이다.
[^c02-gr]: **총회 결의안(GR)**은 데비안 개발자 전체가 프로젝트의 중요한 정책이나 헌법적 사안을 표결하는 절차다.
[^c02-condorcet]: **콘도르세 방식**은 선택지들을 1대1로 비교해 다른 모든 선택지보다 다수에게 선호되는 선택지를 찾는 선호 투표 방식이다.
[^c02-dfsg]: **DFSG**는 데비안이 ‘자유 소프트웨어’로 간주하는 라이선스·배포 조건을 정한 원칙이다.
[^c02-debhelper]: **debhelper**는 `debian/rules`에서 흔한 패키징 작업을 자동화하는 데비안 패키지 빌드 도구 모음이다.
[^c02-init]: **init 시스템**은 리눅스 커널이 시작한 뒤 사용자 공간 서비스와 프로세스를 초기화·관리하는 첫 사용자 공간 프로세스 체계다.

---

### [pathlib로 Python 경로 표현하기](https://lwn.net/Articles/1088781/)

#### 요약

- Trey Hunner는 파일시스템 경로를 문자열 대신 `pathlib.Path`로 표현하자고 제안한다.
- `Path`는 경로 결합, 탐색, 파일 I/O를 더 읽기 쉽고 이식성 있게 만든다.
- Python의 path-like protocol 덕분에 `Path`와 호환되는 자체 경로 객체도 표준 라이브러리 전반에서 사용할 수 있다.
- 성능 차이는 있을 수 있지만, 일반적인 경로 작업에서는 명확성과 유지보수성이 더 중요하다는 것이 발표의 결론이다.

글쓴이: **Jake Edge**
2026년 8월 19일

---

[PyCon US](https://lwn.net/Archives/ConferenceByYear/#2026-PyCon)

[PyCon US 2026](https://us.pycon.org/2026/) 발표를 시작하며 Trey Hunner는 참석자들이 파일시스템 경로를 문자열로 표현하는 일을 멈추고, 대신 [pathlib](https://docs.python.org/3/library/pathlib.html)를 사용하게 만드는 것이 자신의 목표라고 말했다. 특히 오랫동안 Python을 사용해 온 이들에게는 꽤 높은 목표다. 문자열 기반 경로는 널리 쓰여 왔고 대체로 잘 작동하기 때문이다. 물론 Hunner가 바꾸고 싶어 하는 이유는 바로 그 “대체로”라는 부분이다. 그는 언어의 덜 알려진 한 구석을 설명하고 사람들의 생각을 바꿔 보고자 했다.

Hunner는 개발 팀을 위한 [Python 트레이너](https://truthful.technology/)라고 자신을 소개했다. 또한 모든 숙련도의 개발자를 위한 “주간 역량 향상 서비스”인 [Python Morsels](https://www.pythonmorsels.com/)도 운영한다. 이와 별개로 그는 매주 Python 팁을 담은 [뉴스레터](https://www.pythonmorsels.com/newsletter/)도 발행한다.

#### 문자열과 경로

[![[Trey Hunner]](https://static.lwn.net/images/2026/pycon-hunner-sm.png "Trey Hunner")](https://lwn.net/Articles/1089373/)

Python 역사의 대부분 동안 경로는 일반 문자열로 표현되었으며, 이는 지금까지도 작동하고 앞으로도 계속 작동할 것이다. 하지만 그 방식에는 문제가 있다. 10년이 넘은 과거에 Python 3.4는 이 문제를 정리하기 위해 [PEP 428](https://peps.python.org/pep-0428/)(“The pathlib module – object-oriented filesystem paths”)에 기반한 pathlib를 도입했다. 그가 설명할 문자열 경로의 문제는 여러 가지다. pathlib에 대한 표준 라이브러리 대안은 찾기 어렵고 사용하기 불편한 반면, 문자열 경로는 버그를 낳을 수 있으며 경로와 다른 문자열을 구별하기도 어렵다.

그는 많은 사용자가 아직 Python 2.7을 쓰던 2016년으로 시간을 되돌려, 파일 경로 작업을 위해 표준 라이브러리에 무엇이 있었는지 살펴봤다. 경로를 다루기 위해 “손을 뻗었을 법한” 모듈은 [os](https://docs.python.org/2.7/library/os.html), [os.path](https://docs.python.org/2.7/library/os.path.html), [glob](https://docs.python.org/2.7/library/glob.html), [shutil](https://docs.python.org/2.7/library/shutil.html)의 네 가지였다. shutil에는 “파일과 관련된 고수준 기능이 잔뜩 있으며, 파일과 디렉터리를 복사하는 함수만도 서로 다른 일곱 개가 있다”. 반대로 glob은 경로 이름에 셸 같은 패턴 매칭을 수행하는 glob()과 iglob()만 있어 더 단순하다. os.path는 경로 분할, 결합, 질의 등을 포함해 “파일 경로를 조작”하는 데 쓴다.

os 모듈의 이야기는 더 복잡하다고 그는 말했다. 그의 생각에 Python 표준 라이브러리에는 os와 [sys](https://docs.python.org/3.13/library/sys.html)라는 두 개의 “잡동사니 서랍”이 있다. os는 컴퓨터와 운영체제에 관련된 것을 담고, sys에는 Python 인터프리터 자체와 관련한 “잡동사니”가 들어 있다. os에는 경로 및 파일 작업을 위한 함수가 많지만 다른 목적의 함수도 많다. 그는 파일 또는 경로 관련 함수 열여 개가 넘는 것을 간단히 나열한 뒤, os의 다른 모든 함수를 열거한 슬라이드 일곱 장을 보여 주었다. 전부 합치면 아마 200개쯤일 것이다([슬라이드](https://treyhunner.com/pathlib-talk/slides/), 화살표 키로 진행). 그의 요점은 os에서 경로 함수를 찾기 쉽지 않았다는 것이며, os.path, glob, shutil에 흩어진 다른 함수들은 말할 것도 없다.

하지만 경로가 단지 문자열이라면, 왜 os.path 함수 대신 문자열 조작 함수를 쓰면 안 되느냐고 그는 물었다. 그는 Django 프로젝트에서 파일이 있는 디렉터리와 같은 상위 디렉터리 아래의 `templates` 디렉터리 경로를 변수에 설정하는 코드 세 가지 버전을 보였다. 첫 번째는 다음과 같다.

```
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
```

두 번째는 다음과 같다.

```
    BASE_DIR = os.path.abspath(__file__).rsplit("/", maxsplit=2)[0]
    TEMPLATES_DIR = BASE_DIR  + "/templates"
```

물론 둘 다 `os.path`를 import해야 한다. 두 번째도 작동하지만 아마 다소 덜 읽기 쉽다. 또한 Windows는 경로 구분자로 `"\\"`를 쓰므로 그런 종류의 경로에서는 작동하지 않을 수 있다는 이식성 문제가 있다. os를 import하면 `os.sep`를 사용할 수 있지만, 그것조차 그다지 읽기 쉽지는 않다고 그는 말했다.

```
    BASE_DIR = os.path.abspath(__file__).rsplit(os.sep, maxsplit=2)[0]
    TEMPLATES_DIR = BASE_DIR  + os.sep + "templates"
```

그는 뒤의 두 예제에서 드러나는 가독성과 유지보수성 문제 때문에 os.path의 유틸리티 함수가 추가되었다고 말했다. 한편 경로의 여러 부분이 어디에서 왔는지에 따라 슬래시와 역슬래시가 섞일 수도 있다. 실제로 Windows에서는 동작하지만 상당히 이상해 보인다고 했다. (하지만 Linux에서는 전혀 작동하지 않는다.)

문자열로서의 경로에는 또 다른 문제가 있는데, Hunner는 이를 “stringly typed code”라고 부른다. 더 나은 타입이 있는데도 문자열로 전달되는 데이터가 stringly typed인 것이다. 그는 (분명 작년에 썼던) 다음 예를 들었다.

```
    target = "2025-09-25"

    if target[:4] == "2025":
        print("That's this year")
```

이는 작동하지만 해당 문자열이 올바른 형식의 날짜라고 가정한다. 대신 [datetime](https://docs.python.org/3/library/datetime.html) 객체를 사용하면 코드는 조금 더 길어지지만 그 문자열이 실제로 유효한 날짜라는 보장을 얻는다. 그렇지 않으면 [strptime()](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime)가 ValueError를 발생시킨다.

```
    from datetime import datetime

    user_input = "2025-09-25"
    target = datetime.strptime(user_input, "%Y-%m-%d").date()

    if target.year == 2025:
        print("That's this year")
```


Hunner는 경로를 표현하는 문자열도 마찬가지로 stringly typed라고 주장했다. 앞선 예제로 돌아가 [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) 객체가 이를 어떻게 바꿀 수 있는지 보였다.

```
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent
    TEMPLATES_DIR = BASE_DIR / "templates"
```

Hunner가 발표 뒤쪽에서 설명했듯 [resolve()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve) 메서드는 Path를 절대 경로로 바꾸며, [parent](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent) 속성은 부모 디렉터리의 경로로 해석된다. 두 경로를 결합할 때는 [슬래시(`/`) 연산자](https://docs.python.org/3/library/pathlib.html#operators)를 사용한다.

타입 애너테이션을 사용하는 코드에서는 Path 객체가 또 다른 이점을 제공한다. 타입 검사기는 코드에서 문자열과 경로를 혼동하는 문제를 찾아낼 수 있다. 이러한 용도를 구별할 수 있으면 코드를 추론하고 버그를 잡기가 더 쉬워진다.

한편 Path 버전은 그가 앞서 보인 os.path 버전보다 읽기 쉽다.

```
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
```

그는 첫 줄을 이해하려면 오른쪽에서 왼쪽으로 읽어야 한다. [abspath()](https://docs.python.org/3/library/os.path.html#os.path.abspath)로 파일의 절대 경로를 구하고, [dirname()](https://docs.python.org/3/library/os.path.html#os.path.dirname)으로 부모 디렉터리를 구한 다음, 다시 그 부모를 구한다. 이 코드는 중첩 호출을 쓰지만 Path 버전은 메서드와 속성을 연결해 훨씬 자연스럽게 읽힌다. 적어도 그에게는 그렇다.

그는 Path 대안이 더 읽기 쉽고 사용하기 쉬운 예를 몇 가지 보였다. 파일을 읽는 고전적인 `with` 블록은 한 줄로 바꿀 수 있다.

```
    with open("config.txt", mode="rt") as file:
        content = file.read()

    # one line replacement using Path
    content = Path("config.txt").read_text()
```

os 모듈로 디렉터리를 만들 때는 중간 디렉터리도 생성해야 하는지에 따라 [mkdir()](https://docs.python.org/3/library/os.html#os.mkdir) 또는 [makedirs()](https://docs.python.org/3/library/os.html#os.makedirs)를 사용해야 한다. Path 객체의 [mkdir()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir) 메서드에는 중간 디렉터리를 생성할 수 있는 `parents` 플래그가 있다. 마찬가지로 파일을 복사할 때 Path 객체에는 Python 3.14에서 추가된 [copy()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.copy) 및 [copy\_into()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.copy_into) 메서드가 있다. 그 전에는 shutil의 서로 다른 네 함수([copyfile()](https://docs.python.org/3/library/shutil.html#shutil.copyfile), [copy()](https://docs.python.org/3/library/shutil.html#shutil.copy), [copy2()](https://docs.python.org/3/library/shutil.html#shutil.copy2), [copytree()](https://docs.python.org/3/library/shutil.html#shutil.copytree))를 사용할 수 있었다. “어느 것이 어느 일을 하는지 기억나지 않아서 이 가운데 무엇이 필요한지 알 수 없다.”

#### pathlib 사용하기

pathlib 모듈에는 핵심적인 것이 하나 있다고 Hunner는 말했다. 바로 Path 객체다. Path() 생성자는 경로의 문자열 표현을 받아 Path 객체를 반환한다. 이 객체는 기반 운영체제에 따라 [PosixPath](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath) 또는 [WindowsPath](https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath)가 된다. 두 타입은 모두 같은 연산을 지원하며 경로를 정규화하는 방식만 다르므로 사용자는 신경 쓸 필요가 없다.


Path 객체에서 호출할 수 있는 유용한 메서드는 24개가 조금 넘고, 속성은 여섯 개(예: [name](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name))이며, 클래스 메서드는 두 개다. 현재 작업 디렉터리를 위한 [Path.cwd()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd)와 사용자의 홈 디렉터리를 위한 [Path.home()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home)가 그것이다. 전체적으로는 속성과 메서드가 70개가 넘지만, 그는 나머지는 거의 쓰지 않는다.

pathlib가 처음 도입되었을 때 사용자는 Path 객체를 사용하려면 종종 문자열로 변환해야 했다(예: `open(str(path), ...)`). 하지만 시간이 지날수록 더 많은 Python 내장 함수와 표준 라이브러리 모듈이 지원을 추가했다. 그는 “파일 경로를 받는 Python의 유틸리티는 사실상 모두 Path 객체도 받는다”고 말했다. 여섯 가지 별도 예를 나열하며, 명시적으로 경로 문자열을 받도록 설계된 함수와 메서드조차 Path 객체와 함께 동작한다고 지적했다. 따라서 이전 함수를 계속 쓰는 레거시 코드(예: `os.path.join()` 또는 `os.mkdir()`)도 Path 객체를 넘기면 올바르게 작동한다. 그뿐 아니라 [Django](https://www.djangoproject.com/), [pandas](https://pandas.pydata.org/), [pytest](https://docs.pytest.org/en/stable/) 같은 대부분의 서드파티 패키지도 Path 객체를 받는다. 서드파티 패키지가 Path 객체를 받지 않는다면 보고해야 할 버그일 가능성이 높다고 Hunner는 말했다.

pathlib 사용을 시작하는 방법은 경로를 지정하는 문자열을 Path() 생성자에 넘기는 것뿐이다.

```
    >>> from pathlib import Path
    >>> notes_path = Path("Documents/notes.txt")
```

이식성을 위해 문자열 리터럴에서 이름을 구분할 때는 슬래시를 사용해야 한다. 하지만 WindowsPath는 필요에 따라 역슬래시로 구분된 이름을 정규화한다.

Path 객체는 파일 이름과 결합하는 등 여러 작업에 쓸 수 있다. [joinpath()](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath) 메서드나 슬래시 연산자를 사용하면 된다.

```
    >>> from pathlib import Path
    >>> home = Path.home()
    >>> path1 = home.joinpath(".config.toml")
    >>> path2 = home / ".config.toml"
```

그는 처음 보았을 때 슬래시 연산자가 이상해 보였지만, 이제는 익숙해졌고 상당히 읽기 쉽다고 생각한다. 또한 생성자는 여러 인수(문자열 또는 다른 Path 객체)를 받아 함께 결합하므로 다음과 같이 할 수 있다.

```
    >>> path3 = Path(home, ".config.toml")
    >>> path3
    PosixPath('/home/trey/.config.toml')
    >>> path1 == path2 == path3
    True
```

세 방식은 모두 동등하며 어느 하나가 다른 것보다 명백히 낫지는 않다. 다만 세 번째 방식은 구성 요소가 문자열인지 Path 객체인지 알 수 없을 때 주로 쓴다고 그는 말했다.

Hunner는 os.path 함수의 이름이 “유감스럽다”고 느낀다. 단어를 붙여 쓰고 흔히 줄여 놓은 반면, pathlib의 대응물은 더 잘 설계됐다는 것이다. 예를 들어 그는 `os.path.basename(path)`보다 `path.name`을, `os.path.dirname(path)`보다 `path.parent`를 선호한다. 더 설득력 있는 예는 `os.path.splitext(path)[1]` 대신 `path.suffix`를 사용하는 것이다. 그는 자신이 쓴 [글](https://www.pythonmorsels.com/pathlib-module/)과 [Python pathlib 문서](https://docs.python.org/3/library/pathlib.html#corresponding-tools)에 pathlib 치트 시트가 있다고 덧붙였다.

#### 상속과 확장

Python 3.12부터 클래스는 상속을 통해 pathlib.Path의 기능을 확장할 수 있다. 예를 들어 디렉터리를 변경하는 메서드를 가진 맞춤 Path 클래스를 만들 수 있다.

```
    import os
    import pathlib

    class BetterPath(pathlib.Path):
        def chdir(self):
            os.chdir(self)
```

Path 상속이 흔한 일은 아닐 것이다. 그러나 상속할 때 새 클래스가 사용하는 속성(어쩌면 메타데이터 저장용)을 서브클래스에서 [with\_segments()](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_segments) 메서드를 재정의하여 파생 Path 객체(예: `parent`)로 전파할 수 있다.

2016년에는 [PEP 519](https://peps.python.org/pep-0519/)(“Adding a file system path protocol”)가 Python 3.6에 포함되도록 승인되었다. 이 문서는 어떤 객체가 path-like로 간주되려면 무엇이 필요한지 설명했으며, 그러면 경로 문자열 또는 Path 객체가 기대되는 모든 곳에서 받아들여진다. 사실상 [duck typing](https://en.wikipedia.org/wiki/Duck_typing)이 그 오리를 경로로 취급해야 한다고 판단하는 데 어떤 종류의 꽥꽥거림이 필요한지를 설명한 것이다. 제대로 꽥꽥거리기 위해 클래스가 구현해야 할 것은 단 하나, path-like 객체의 문자열 또는 bytes 표현을 반환하는 [\_\_fspath\_\_()](https://peps.python.org/pep-0519/#protocol) 메서드뿐이다.


경로 protocol을 따르는 path-like 객체는 `open()`과 다른 내장 함수 및 표준 라이브러리 함수에서 받아들여진다. 또한 PEP 519는 서드파티 경로 라이브러리를 가능하게 한다. 그는 pathlib가 훌륭하다고 생각하지만, “마음에 들지 않는다면 pathlib 외에도 path-like 객체로 이루어진 전체 생태계가 있다”고 말했다. 그는 Path를 상속하지 않았지만 `open()`과 함께 동작하며 Path를 넘길 수 있는 다른 모든 곳에서도 동작하는 path-like 클래스의 “아주 어리석은 예”를 보였다.

#### 흔한 실수

이어서 그는 새로운 Path 사용자가 하는 몇 가지 실수를 설명했다. 첫 번째는 일종의 역사적 우연이다. 이 기능이 Python 3.4에 도입되었을 때 경로로 파일을 여는 일반적인 방법은 Path의 [open()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open) 메서드였다. PEP 519와 함께 Python 3.6이 출시되면서 `open()` 내장 함수가 path-like 객체를 받기 시작했으므로 그 메서드를 쓸 필요가 없어졌다. 이제는 단지 역사적 이유일 뿐이므로 Path의 `open()` 메서드는 피해야 한다고 그는 생각한다. “모두가 그 조언에 동의하는 것은 아니지만, 나는 무대에 있으니 이렇게 말할 수 있다.” Hunner의 말에 웃음이 터졌다.

또 다른 흔한 실수는 Path 객체를 불필요하게 문자열로 변환하는 것이다. 경로를 표시하거나 로그로 남길 때 f-string은 객체를 암묵적으로 문자열로 변환한다.

```
    >>> print(f"Reading: {path}")
    Reading: example.txt
```

`open()`이나 path-like 객체를 받는 다른 함수에는 객체를 명시적으로 문자열로 변환할 필요가 없다. “경로를 문자열로 변환해야 한다고 생각한다면, 아마 그럴 필요가 없다.”

마지막으로 Path() 생성자의 유연성 덕분에 여러 문자열을 생성자에 넘겨 하나의 경로로 결합할 수 있다. 한 조각에 대해 Path 객체를 만들고 `joinpath()`나 슬래시 연산자를 사용해 최종 경로를 구성할 필요는 없다.

지속적으로 제기되지만, 그의 생각에는 대체로 근거 없는 불만이 있다. 바로 pathlib가 느리다는 것이다. “일부 연산에서 pathlib가 더 느릴 수 있는 것은 사실이지만, 가독성은 때로 작은 성능 페널티를 감수할 가치가 있다.” 그는 파일 400,000개에서 [os.walk()](https://docs.python.org/3/library/os.html#os.walk)와 [Path.walk()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk)의 성능을 비교했다. 둘은 1초보다 약간 짧은 수준으로 대략 같았다(`os.walk()`는 0.91초, 0.85초). 다만 `Path.walk()`는 Path 객체가 아니라 문자열을 반환한다고 그는 지적했다. 이 문자열들을 Path 객체로 변환하자 테스트에는 2.22초가 걸렸다.


대부분의 경로 연산은 tight loop에서 수행하지 않으므로 그 페널티는 실제로는 별로 중요하지 않을 수 있다고 그는 말했다. Path 객체는 더 나은 가독성도 제공하며, 이것 역시 중요하다. “정말 중요할 때만 최적화하라.”

그는 pathlib가 단순히 다른 API가 아니라, 파일 경로가 “자체 데이터 타입을 가질 만큼 중요하다”는 사실을 인정하는 것이라고 말하며 마무리했다. pathlib의 목적은 경로 연산을 언어 안에서 올바르게 표현하여 쉽게 처리하게 하는 것이다.

[PyCon US 참석을 위해 캘리포니아주 롱비치로 가는 제 여행을 지원해 준 LWN의 여행 후원사 Linux Foundation에 감사드립니다.]

[댓글(15개 게시됨)](https://lwn.net/Articles/1088781/#Comments)

---

### [부트스트래핑 가능한 빌드: 방법과 이유](https://lwn.net/Articles/1088279/)

글: **Jake Edge**
2026년 8월 17일

---

#### 요약

- FOSSY 발표에서 Timothy Sample은 아주 작은 seed부터 현대 Linux user space를 빌드하는 bootstrappable builds를 설명했다.
- 이 접근은 reproducible builds가 해결하지 못하는 Trusting Trust형 binary backdoor 위험을 줄인다.
- Guix와 live-bootstrap은 긴 bootstrap chain을 사용하며, Germ은 이를 Scheme 중심의 더 짧은 경로로 바꾸려는 프로젝트다.

[FOSSY](https://lwn.net/Archives/ConferenceByYear/#2026-Free_and_Open_Source_Software_Yearly)

[올해 Free and Open
Source Software Yearly conference](https://2026.fossy.ca/)는 더 잘 알려진 이름인 “FOSSY”로 불리며, 지난 세 번의 개최지인 미국 오리건주 포틀랜드에서 캐나다 밴쿠버의 아름답고 (그리고 거대한) University of British Columbia(UBC) 캠퍼스로 북상했다. FOSSY에는 심도 있는 기술적 kernel track 주제부터 법률 및 커뮤니티 문제에 관한 발표, “일상 속 FOSS” 발표까지 여러 종류의 발표가 있었다. “Toolchains and Other Development Tools” track에서 Timothy Sample은 [bootstrappable builds](https://bootstrappable.org/)에 관해 발표했다. 이는 사촌 격인 [reproducible builds](https://reproducible-builds.org/)보다 다소 덜 알려져 있지만, LWN은 2년여 전 [이 주제](https://lwn.net/Articles/983340/)를 다룬 바 있다. 간단히 말해 bootstrappable build는 다른 약간 더 큰 program을 빌드할 수 있는 작은 program에서 시작하고, 그것이 또 다른 program을 빌드하는 과정을 반복하여 작은 seed로부터 현대 Linux user space 전체를 빌드하는 방식이다.[^c04-user-space] 궁극적으로 이는 오늘날의 일반적인 Linux user space와 달리, 기원이 완전히 이해된 code를 만들어 낸다.

그는 참석자들에게 bootstrappable builds를 들어 본 적이 있는지, 그리고 그 개념에 대체로 익숙한지를 물으며 발표를 시작했다. 대다수가 이 용어를 알고 있고 청중의 절반가량은 그보다 더 많이 안다는 점에 그는 인상받은 듯했다. 그는 거의 10년 전 [GNU Guix](https://guix.gnu.org/)를 쓰기 시작하면서 bootstrappable builds를 향한 길에 들어섰다고 말했다(그는 이를 “geeks”라고 발음했는데, 내게는 놀라웠다). 당시 Guix를 사용했다면 Guix에 기여하고 있던 셈이었다고 그는 웃으며 말했다. Guix는 [Nix](https://nixos.org/)와 [유사하고](https://lwn.net/Articles/962788/) (거기에서 영감을 받은) “functional package manager”다.[^c04-functional-package-manager]

[![[Timothy Sample]](https://static.lwn.net/images/2026/fossy-sample-sm.png "Timothy Sample")](https://lwn.net/Articles/1088544/)

Guix와 Nix 모두에서 system의 모든 software는 각 program을 빌드하는 방법을 설명하는 “derivation graph”로 표현된다.[^c04-derivation-graph] 특정 program을 빌드하려면 여러 input이 필요하며, 이는 graph에 명시된다. 각 input을 빌드하는 방법(그리고 당연히 input의 input 등)도 graph에 표현된다. “현대 software에는 수백, 수백 개의 node가 있고, 이는 무서울 정도로 복잡하다.”

그는 Python program을 예로 들었다. 이는 당연히 실행하려면 Python이 필요하지만, Python은 C program이므로 C compiler가 필요하다. 그 C compiler는 어떤 언어로 작성되었으므로, 그 언어의 compiler가 필요해진다. 그리고 이 과정은 계속된다. Guix는 이 모든 것을 살펴보고 탐색할 수 있는 object인 graph에 모은다. “그러면 내 compiler의 compiler compiler는 누가 compile하고, 그 과정은 어디에서 멈추는지 궁금해지기 시작한다.”

Debian 같은 system에서는 누군가 repository에 upload한 C compiler binary에서 그 과정이 멈춘다. Guix에서 원래의 종착점은 GNU user-space program으로 이루어진 250MB 정적 링크 blob이었다. 그 모든 code가 어디에서 왔는지에 대한 답은 당연히 완전히 명확하지 않으며, Guix 개발자들은 이에 만족하지 못했다. 그 blob은 reproducibly build할 수 있었고, 이는 좋은 일이지만 전체 문제를 해결하지는 못한다고 Sample은 말했다.[^c04-static-linking]

#### 부트스트래핑 가능성

#### 요약

- bootstrappable builds는 pre-built artifact에 의존하지 않고 build system을 만드는 것을 목표로 한다.
- reproducible builds와 달리 compiler binary에 숨은 Trusting Trust backdoor도 위협 모델에 포함한다.
- self-hosting tool은 source에 없는 동작을 binary에 지속시킬 수 있어 bootstrap chain 검증이 필요하다.

bootstrappable builds의 기본 개념은 pre-built artifact에 의존하지 않고 빌드할 수 있는 system을 만드는 것이다.[^c04-artifact] “이미 우리를 위해 빌드되어 있는 artifact가 존재한다고 그냥 가정하지 않고, zero에서 현대에 이르는 경로를 만들 수 있을까?” 고전적인 yogurt 제조법은 공정을 시작할 yogurt가 필요하다. 이는 오늘날 보통 C compiler를 빌드하는 방식, 즉 기존 C compiler binary에서 시작하는 것과 같다. 오래된 고향에서 가져온 할머니의 starter로 sourdough bread를 만드는 일을 떠올릴 수도 있다. “우리는 본질적으로 Bell Labs에서 가져온 Dennis Ritchie의 starter로 C compiler를 만들고 있다.”

물론 이는 C에만 해당하지 않으며, 대부분의 언어에서 사실이다. 언어 자체로 compiler와 다른 tool을 작성하여 “self host”하는 것은 언어의 자랑거리 같은 부분이다.[^c04-self-hosting] 당연히 자기 언어가 최고이므로 언어 개발자가 그렇게 하는 것은 자연스럽지만, 그 결과 chicken-and-egg 문제가 남는다. Bootstrappable builds는 이를 넘어서 이런 tool을 “from scratch”로 빌드하려는 노력이다.

Reproducible builds는 “실제로 computer에서 실행되는 사용 중인 binary가 source code에 대응한다는 점을 더 신뢰할 수 있게” 해 준다.[^c04-reproducible-build] 사용자는 source code file 집합에서 왔다고 주장하는 binary를 받을 수 있지만, 그것이 정말 그러한지는 어떻게 확신할 수 있을까? Reproducible build라면 binary를 직접 만들고, 받은 것과 bit-for-bit 동일한지 확인할 수 있다.

Bootstrappable builds도 정확히 같은 일을 하지만, 다른 failure mode를 다룬다. Reproducible build가 검증에 실패했다면 binary를 빌드한 사람이 그 출처에 관해 거짓말을 했거나 실수했기 때문이다. Bootstrappable builds는 Ken Thompson이 유명한 Turing Award 강연인 [Reflections on
Trusting Trust](https://dl.acm.org/doi/epdf/10.1145/1283920.1283940)에서 설명한 종류의 문제를 방지할 수 있다.[^c04-trusting-trust]

Sample은 그 강연에서 Thompson이 든 예가 C compiler의 어느 곳에서 "\n" 정의를 찾을 수 있는가를 묻는 것이었다고 말했다. Compiler의 source code를 보아도 정의는 나오지 않고, "\n"이 "\n"이라는 순환 정의만 보일 것이다. "\n"을 ASCII 10으로 변환하는 것은 C compiler binary 자체에 구현되어 있다. Thompson은 강연을 계속하면서 login program용 backdoor처럼 훨씬 더 위험한 무언가도 같은 방식으로 compiler에 숨길 수 있다고 지적했다.[^c04-backdoor]

이런 종류의 결함은 C compiler, 심지어 compiler에만 국한되지 않는다. 모든 self-hosting program은 잠재적으로 이에 취약할 수 있다. 이런 program은 source code에서 세부 사항을 제거하면서도 그것이 binary 형태로 지속되게 할 수 있다. 발표를 준비하던 중 동료가 이 종류의 실제 공격을 보여 주는 최근 [논문](https://arxiv.org/pdf/2607.24888) (“Trusting-Trust Attack against an Entire Linux Distribution
through Binary Manipulation”)을 알려 주었다. 연구자들은 system에서 빌드되는 거의 모든 binary에 실행되는 NixOS의 [strip](https://man7.org/linux/man-pages/man1/strip.1.html) program에 backdoor를 삽입했다.[^c04-strip] “그들은 source-code analysis로는 완전히 보이지 않는 방식으로 system의 사실상 모든 단일 program에 backdoor를 넣을 수 있었다.” 이것이 bootstrappable builds가 저지하려는 공격의 종류다.

Security 관점이 bootstrappable builds의 가장 큰 이점이지만, software freedom 측면도 있다고 Sample은 말했다. Source code를 읽을 수 있는 것은 유용하지만, source code가 실행 중인 program에 대응한다는 사실을 아는 것도 중요하다. 또한 자신의 code를 명확하고 이해 가능하게 만드는 데 많은 programmer가 느끼는 자부심도 있다. Code를 검사할 수 있고 모든 세부 사항이 이용 가능한 source code 안에 존재하도록 보장하는 것은 그 일부다.

그는 bootstrapping을 선제적으로 처리하는 것이 가장 좋다고 말했다. Compiler가 self-hosted되기 전에는 보통 다른 언어로 작성되므로, 그 code를 보존하고 self-hosted version과 함께 유지하면 binary에 아무것도 숨기지 않았음을 보장할 수 있다. [GNU Guile](https://www.gnu.org/software/guile/) project가 바로 그렇게 한다. Guile은 Guix와 여러 다른 project가 쓰는 [Scheme](https://www.scheme.org/) 구현이다. Guile에는 compiler를 bootstrapping할 때 사용할 수 있는 언어의 C implementation이 여전히 있다. [GNU Make](https://www.gnu.org/software/make/)에는 당연히 makefile이 있지만, make를 사용할 수 없을 경우를 위해 shell script도 있다. “우리는 우리가 근본적인 build tool임을 인식하며, 여기에는 다른 on-ramp가 있어야 한다.”

self-hosted build만 지원하는 tool의 경우, 그 부족함을 우회하기 위해 그와 bootstrappable-builds community의 다른 이들이 사용하는 기법이 있다. 첫째는 project의 history를 이용해 non-self-hosted version을 찾는 “archaeological dig”다. 그 version은 그 시대의 tool을 이용해 빌드한다. “그런 뒤 version을 거듭해 history를 따라 이동하여 [...] 현대 tool에 도달한다.” 때로는 version 단계 일부를 건너뛸 수 있지만, 전반적으로 느린 과정이다. “어떤 면에서는 그저 문제를 뒤로 미루는 것일 뿐이다. 기술적으로는 모든 source code를 갖고 있다.” 하지만 누군가에게 예컨대 tool의 서로 다른 version 12개를 보라고 하는 일은 꽤 부담스럽다. 검증할 version 하나만 있으면 좋을 것이다.

청중 한 명이 이것이 OCaml version Rust compiler를 써서 현재 Rust까지 bootstrap하는 것과 같은지 물었고, Sample은 그렇지만 OCaml Rust compiler는 더 이상 이용할 수 없다고 답했다. 또 다른 참석자는 [Go](https://go.dev/) programming language를 빌드하는 데 사용된 [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs) C compiler와, 그 C compiler를 빌드한 더 이른 Plan 9 C compiler가 모두 여전히 이용 가능하다고 언급했다. 그런 build chain은 Guix에서 일반적이라고 Sample은 말했다. Rust의 경우 현재 C++ 기반 [mrustc](https://github.com/thepowersgang/mrustc#mutabahs-rust-compiler)로 Rust version 1.54 또는 1.56을 빌드한 뒤 시작한다. 현대 Rust는 1.97이고 그 사이 거의 모든 version을 빌드해야 하므로 매우 느리다. Guix system을 rebuild할 때 “Rust compile chain에 도달하면 정말 우울하다”고 Sample은 말했다. 한 참석자는 Arm laptop에서 이를 빌드하는 데 사흘이 걸렸다고 했다.[^c04-cross-architecture]

검증해야 할 단계가 너무 많으므로 이런 chain의 최종 결과는 그다지 좋지 않다. 대안은 “무언가를 올리기 위한 새 tool을 purpose-build하는 것”이며, mrustc가 정확히 그러한 경우다. 하나의 code base만 검사하면 되므로 결과는 더 낫지만, 그런 bespoke tool을 개발하는 데는 “영원히 걸린다”. 그는 그런 작업을 일부 해 보았고, 그 tool은 다른 tool의 bootstrap을 가능하게 하기 위해서만 존재하므로 어느 수준에서는 결과가 만족스럽지 않다. 그뿐 아니라 target tool을 따라가기 위해 maintenance가 필요하지만, 다른 개발자를 끌어들일 만한 특별히 흥미로운 작업은 아니다.

가장 성공적인 bootstrappable builds는 두 접근법을 조합한다. Rust와 mrustc처럼 alternative bespoke tool로 빌드할 수 있는 더 단순한 과거 version으로 돌아간 뒤, 현재 version으로 전진한다. 실제로 mrustc는 이제 Rust 1.90을 빌드할 수 있지만 아직 Guix에 통합되지는 않았다. 그는 가까운 시일 안에 이를 통합할 계획이다.

#### 프로젝트

#### 요약

- Guix의 seed는 현재 약 256 byte로 축소되었지만, 일부 작업에는 여전히 statically linked Guile이 쓰인다.
- live-bootstrap은 182단계의 철저한 bootstrap process를 제공하며 Fiwix kernel bootstrap도 탐구한다.
- hex0에서 M2-Planet, Mes, TCC로 이어지는 chain이 현대 development tool을 만들 수 있게 한다.

그는 Guix와 그 seed로 돌아왔다. 이제는 250MB blob 대신 약 256 byte에 불과하다. 이는 [hex0라는 program으로
구성되며](https://guix.gnu.org/manual/1.5.0/en/html_node/Full_002dSource-Bootstrap.html), “수많은 layer를 거쳐 빌드하고 결국 GCC 2, GCC 4, 현대 GCC, 현대 Guile 및 이 모든 tool에 도달할 수 있다”. 이는 “정말 멋지지만”, 많은 caveat가 있다. 가장 큰 것은 여전히 statically linked Guile을 “여러 작업을 하는 데” 사용한다는 점이다. 이는 “명백한 cheating”이라고 그는 말했지만, 이를 고칠 계획이 있고 그가 작업 중이지만 달성하려면 시간이 걸릴 것이다.

사람들을 자주 실망시키는 또 다른 점은 kernel을 어떻게 bootstrap할지에 대한 답이 없다는 것이다. Guix는 kernel이 존재한다고 가정한다. “userland 전체를 nothing에서 bootstrap하겠지만, kernel은 이 논의의 범위 밖이다.”[^c04-kernel]

관련 project로는 Guix와 함께 동작하고 많은 같은 tool 및 접근법을 사용하는 [live-bootstrap](https://github.com/fosslinux/live-bootstrap#live-bootstrap)이 있다. 다만 live-bootstrap은 Guix보다 더 빠르게 움직이며 [Fiwix](https://www.fiwix.org/) kernel을 사용한 kernel bootstrapping을 탐구했다. Live-bootstrap은 source release에 딸려올 수 있는 machine-created file(예: configure)도 재생성한다. “그들이 얼마나 철저한지는 매우 훌륭하지만”, “단점은 극도로 복잡하다는 것”이다.[^c04-configure]

이를 보여 주기 위해 그는 system을 bootstrap하는 [182단계
process](https://github.com/fosslinux/live-bootstrap/blob/master/parts.rst)를 띄웠다. 이는 base Linux system에 도달하는 데 필요한 순서대로 빌드해야 하는 tool을 나열한다. hex0에서 시작해, 복잡도가 점차 높아지는 여러 C compiler, [Automake](https://www.gnu.org/software/automake/)와 [Autoconf](https://www.gnu.org/software/autoconf/)를 bootstrap하기 위한 여러 version의 Perl 등을 빌드한다. Rust나 Go 같은 tool은 포함하지 않는다. “이는 그저 현대 GNU/Linux base system일 뿐이다.”

“그들이 그 작업을 해낸 것은 훌륭하다. 꽤 놀랍고 복잡하며, 이를 개선하면 좋겠다”고 Sample은 말했다.

hex0 program은 hexadecimal text 문자열을 해당 byte를 가진 binary로 바꾸는 방법을 제공한다. 보통 이는 [hex1과 hex2를
빌드하는 데](https://man.sr.ht/~oriansj/bootstrappable/stage0.md) 사용된다. 이들도 hexadecimal converter이며, 각각 single-character label(hex1)과 더 화려한 addressing mode를 허용하는 더 완전한 label(hex2)을 추가한다. 이를 사용하면 hex opcode 대신 assembly mnemonic을 쓸 수 있게 해 주는 [M0](https://github.com/oriansj/stage0#m0)를 빌드할 수 있다.[^c04-assembler]

Sample은 몇 단계를 생략했지만, 결국 [M2-Planet](https://github.com/oriansj/m2-planet#m2-planet)을 빌드할 수 있으며 이는 “거의 C와 같다”고 말했다. Code를 compile할 수 있지만 때로는 일부 C feature가 빠져 있으므로 이를 피하도록 다시 작성해야 한다. 그 시점부터 모든 것은 M2-Planet C dialect로 작성된 Scheme interpreter인 [GNU Mes](https://www.gnu.org/software/mes/)를 사용하도록 전환된다. Mes에는 C library(Meslibc)와 Scheme으로 작성된 C compiler(MesCC)가 있다. 이들은 “단순한 C compiler지만 MesCC보다 훨씬 완전한” [Tiny C Compiler](https://bellard.org/tcc/)(TCC)를 빌드할 수 있게 한다. 이후 TCC를 이용해 현대 development tool을 빌드할 수 있다.

#### Germ

#### 요약

- Germ은 C와 Scheme 사이를 오가는 긴 중간 단계를 건너뛰어 처음부터 Scheme interpreter를 제공하려 한다.
- 약 2.25KB binary가 Scheme assembler와 두 번째 interpreter stage를 실행해 Guix build script에 근접한다.
- Mes보다 빠른 일부 micro-benchmark 결과와 달리 실제 workload 성능과 x86_64 이식성은 아직 과제다.

그것이 Guix와 live-bootstrap 모두가 택한 경로다. “작동은 한다. [...] 하지만 모든 것이 엄청나게 복잡하다.” 그는 [Germ(또는 Germ Lisp)](https://git.ngyro.com/germ/tree/README?id=dd840f291cc26f71e99cc859f25a63ecf9839ddf)이라는 다른 접근법을 작업 중이며, 이는 그의 site의 [blog post에서 소개된다](https://ngyro.com/blog/introducing-germ-lisp.html). 그 글에서 그는 Guix가 Scheme 기반인데도 기존 mechanism이 C에서 Scheme으로, 다시 C로 간다고 지적했다. 하지만 그는 “primitive Lisp interpreter는 primitive assembler보다 훨씬 더 복잡하지 않다”는 점을 깨달았다.

그는 Mes 작업을 하며 좋아한다. “가끔 Mes 작업으로 돈을 받는데, Mes는 훌륭하다.” 그러나 Mes replacement도 작성 중이며, 이는 그다지 드문 일이 아니다. 예를 들어 [Haskell](https://www.haskell.org/)과 [ML](https://en.wikipedia.org/wiki/ML_%28programming_language%29)로 작성 중인 Mes replacement가 있다. 이 문제를 보는 사람은 누구나 즉시 [Forth](https://forth-standard.org/)로 replacement를 작성하고 싶어 한다고 그는 말했다. Hex monitor를 통해 Forth를 bootstrap하는 것은 이 언어의 명백한 용도지만, 대부분 개발자는 나머지 code를 Forth로 작성하고 싶어 하지 않는다고 그는 생각한다. “나는 binary를 읽는 편이 낫다.” 청중석의 Keith Packard는 이렇게 말했다. “Assembly가 Forth보다 작성하기 쉽다.”

Sample은 Scheme 사람들은 다르며 그 언어로 code를 작성하려 한다고 말했다. Germ의 의도는 모든 중간 단계를 뛰어넘어 처음부터 Scheme interpreter를 갖는 것이다. “그저 ‘Scheme, 가라!’라고 말하는 셈이다. 정확히는 두 stage가 있지만, 거의 ‘Scheme, 가라!’다.” 이는 원래 Mes가 설계된 방식이라고 그는 말했다. Mes는 일찍 성공할 수 있게 해 준 일부 shortcut을 취했지만, “이제는 막히고 있다”.

Germ은 약 2.25KB다. 그는 2KB가 되기를 바랐지만 목표를 약간 놓쳤다. 이는 “almost-Scheme을 실행할 수 있는” binary다. Scheme으로 작성된 assembler를 실행할 수 있을 만큼의 Scheme만 제공한다. 그 assembler는 “대략 Scheme interpreter와 같은” 두 번째 stage를 빌드하는 데 쓰인다. 여기에는 contiguous byte와 vector, I/O와 kernel 작업을 위한 feature가 있으며, 수정되지 않은 Guix build script를 *거의* 실행할 수 있다(이를 완전히 동작하게 하려면 여전히 몇 가지 미해결 항목이 있다). C code를 compile하기 위해 MesCC를 사용하고, shell script를 처리하려고 그가 몇 년 전에 작성한 Scheme shell도 있다. “결국에는 awk script와 sed script도 실행할 것이다.”[^c04-repl]

Sample은 이 시점에서 참석자들이 demo를 기대할 수 있지만, 자기 slide가 Germ을 사용해 laptop에서 실행 중이었으므로 발표 내내 이미 demo를 하고 있었다고 말했다. 그는 Germ에 [SDL](https://www.libsdl.org/) interface를 추가하고 “draw pixel” function을 제공했으며 font 정보를 불러왔다.[^c04-sdl] 청중 한 명이 추측했듯이(1,000 nerd point 상을 받았다), 그가 쓴 font는 원래 Symbolics [Lisp machine](https://en.wikipedia.org/wiki/Lisp_machine)의 것이었다.

그는 Germ code를 짧게 둘러보며 [memory.scm](https://git.ngyro.com/germ/tree/scm/germ/x86/memory.scm?id=dd840f291cc26f71e99cc859f25a63ecf9839ddf)의 것 같은 Scheme 기반 assembly를 보였다. 동시에 일반 assembly version([memory.s](https://git.ngyro.com/germ/tree/gas/x86/memory.s?id=dd840f291cc26f71e99cc859f25a63ecf9839ddf))도 병행해 유지한다고 언급했다. 실제 assembler를 쓰면 “debugging symbol과 모든 것을 얻지만, 다른 쪽에서는 확실히 얻지 못한다”는 점에서 이 선택에는 실용적인 측면도 있다고 그는 웃으며 말했다.[^c04-debug-symbols]

전반적으로 Germ은 그의 목표를 잘 충족한다. Guix 사용 사례에 정확히 맞는 높은 수준의 abstraction에 빠르게 도달한다. 모든 Guix build script는 Scheme으로 작성되어 있으며, Guix는 대부분 shell script 사용을 피한다.
> 개념적으로 단순하다. 모두가 Lisp나 Scheme을 좋아하지는 않는다는 것을 안다. 어쩌다 보니 논쟁적이지만, 평범하고 일반적인 Scheme은 존재하지도 않는 언어를 위한 bespoke assembler와 compiler의 이 탑보다 나아야 한다.

예상할 수 있듯 그 말은 청중의 웃음을 샀다. 결국 Lisp/Scheme은 논쟁적이고 다소 분열적인 주제다. Germ이 직면한 가장 큰 문제는 놀랍지 않게도 performance라고 그는 말했다. 그는 1950년대 원래 Lisp interpreter가 작성된 방식처럼 assembly language를 사용해 Scheme을 작성하고 있다. “Assembly로 작성하는 것은 어렵고 작게 유지하는 것도 어려워서, 현대 기법을 모두 활용할 수 없다.”

적어도 function call micro-benchmark에서는 Germ이 “기술적으로 Mes보다 빠르다”. 그러나 실제 program을 실행하면 Germ에서는 거의 모든 것(예: loop)이 Scheme에서 실행되므로 Mes가 훨씬 빠르다. 비교하면 그의 desktop에서 Mes가 자신을 compile하는 데는 약 100초가 걸리고, experimental bytecode compiler를 쓰면 60초가 걸린다. 그가 시험 중인 여러 optimization을 켠 Germ에서 Mes를 compile하는 데는 약 140~150초가 걸린다. 문제는 Mes가 “참을 수 없을 정도로 느리다”는 것이므로, Mes보다 느린 것은 사실상 출발선에서 탈락하는 문제다.[^c04-bytecode]

또한 Germ은 Arm과 RISC-V에서 실행 가능한 Mes보다 이식성이 낮으며, 현재는 x86_64 전용이다.[^c04-isa] Germ이 직면한 또 다른 문제는 “사람들이 그냥 괄호를 싫어한다”는 것이다. 이는 비합리적이지만, 그도 Guix를 만나기 전에는 싫어하던 사람 중 하나였으므로 공감할 수 있다. 그래도 Scheme은 구현하기 비교적 쉬운 언어이고 Guix와도 잘 맞으므로, bootstrapping에 매우 타당하다.

#### 미래

#### 요약

- Germ은 Guix의 statically linked %bootstrap-guile을 대체할 수 있는 bootstrap seed 후보가 될 수 있다.
- assembly loop를 최적화하고 C compiler backend 및 RISC-V port를 추진하는 것이 다음 기술 과제다.
- 긴 bootstrap chain의 검증 부담은 줄어들지만, 남아 있는 단계의 supply-chain 위험은 계속 고려해야 한다.

앞으로 그는 Germ을 “모두에게 흥미로운 방식으로” Guix와 통합하고 싶어 한다. 현재 Guix는 statically linked Guile binary인 %bootstrap-guile에 의존하지만, Germ이 이를 잠재적으로 대체할 수 있다. Mes로 대체할 수도 있지만, 어느 쪽이든 좋은 진전이 될 것이다.

그는 Germ performance도 개선하고 싶어 한다. 일부 looping construct를 assembly code로 옮기는 일은 쉽게 얻을 수 있는 개선점이다. 하지만 이는 “임시방편처럼 느껴지며”, 단순히 compiler를 작성해야 할지 고민하고 있다. C용 compiler backend가 필요하므로 둘을 결합할 수 있을지도 모른다.[^c04-compiler-backend] 끝내고 싶은 RISC-V port를 위한 시작 작업도 일부 해 두었다.

그는 여기서 발표를 마쳤지만 이후 활발한 Q&A session이 이어졌다. Packard는 Germ이 Scheme을 얼마나 구현했는지, 예를 들어 [R5RS](https://conservatory.scheme.org/schemers/Documents/Standards/R5RS/)를 준수하는지 물었다. Sample은 이것이 Guile Scheme이지만 [Guile
Object Oriented Programming System](https://doc.guix.gnu.org/guile/latest/en/html_node/GOOPS.html)(GOOPS) 같은 extra는 없다고 답했다. 실질적으로는 [R7RS](https://r7rs.org/) Scheme이지만 필요하지 않으므로 floating-point number를 제거하는 등의 shortcut을 취했다.

Mark Wielaard는 이 작업으로 182단계 중 몇 단계가 제거되었는지 물었다. Sample은 자기 “꿈꾸는 마음”에서는 Germ이 다른 사람들이 Perl과 autoconf 같은 긴 build chain 일부를 제거할 Scheme 기반 shortcut을 만들고 문제를 더 줄이는 데 쓸 wedge 역할을 할 것이라고 말했다. 그는 여전히 80단계 이상이 남는다는 Wielaard의 추정을 인정했다. Wielaard는 누군가 73단계를 sabotage해도 눈치채지 못할 가능성이 높다고 지적했다. Sample은 이것이 접근법의 알려진 결함이라는 데 동의했지만, 모든 것을 검증할 수 있는 능력을 서서히 개선하려고 단계 수를 줄이고 있다고 말했다.[^c04-supply-chain]

한 참석자는 원한다면 seed를 2.25KB보다 더 작게 만들 수 있다고 말했다. 그는 동의하면서 hex0로 Germ의 첫 stage를 load하면 된다고 언급했지만, “나는 게임을 하고 싶은 것이 아니라 실제 결과를 내고 싶다”고 말했다. 싸움을 시작하고 싶지는 않았고 hex0를 쓰는 이들을 존중하지만, 그에게는 약간 cheating처럼 느껴진다.

마지막 질문은 Germ에 read-eval-print loop(REPL)가 있는지였다. 답은 당연히 그렇다. 이미 그것으로 slide를 표시하고 있었기 때문이다. 그는 REPL과 (next-slide), (prev-slide) function 사용을 보였고, error에서 backtrace를 제공하는 것도 시연했다. “나는 늘 이것으로 program을 작성한다. 나를 미치게 만들 수는 없으니, 몇 가지 생활 편의 기능은 있어야 한다.” Floating-point number 없음 같은 shortcut을 취했지만, [delimited
continuations](https://en.wikipedia.org/wiki/Delimited_continuation) 같은 extra도 있다.

그는 작동하는 [syntax-case](https://cs.brown.edu/courses/cs173/2008/Manual/guide/syntax-case.html) form을 포함해 Germ에는 “가장 화려한 macro”가 있다고 말하며 마쳤다. 아이러니하게도 bootstrappable syntax-case는 없고 syntax-case를 사용해 작성되어 있기 때문에, 그는 이를 직접 구현해야 했다.[^c04-hygienic-macros]

[FOSSY 참석을 위해 밴쿠버로 가는 여행 경비를 지원해 준 LWN의 여행 sponsor인 Linux Foundation에 감사드리고 싶습니다.]

[댓글(14개 게시됨)](https://lwn.net/Articles/1088279/#Comments)

[^c04-user-space]: **user space**는 kernel 밖에서 실행되는 일반 application과 library 영역이며, kernel이 제공하는 system call을 통해 hardware 및 kernel service를 사용한다.
[^c04-functional-package-manager]: **functional package manager**는 package build와 dependency를 입력이 명시된 함수처럼 취급해 격리·재현 가능한 결과를 지향하는 package-management 방식이다.
[^c04-derivation-graph]: **derivation graph**는 package와 그 build input, dependency, build recipe 사이의 관계를 나타내는 directed graph다.
[^c04-static-linking]: **static linking**은 필요한 library code를 executable 안에 포함하는 link 방식이다. 실행 환경 의존성은 줄지만 binary가 커질 수 있다.
[^c04-artifact]: **artifact**는 build 과정에서 생성되거나 입력으로 사용하는 binary, archive, generated file 같은 산출물이다.
[^c04-self-hosting]: **self-hosting**은 compiler나 interpreter가 자신이 구현하는 언어로 작성되어, 기존 version을 사용해 다음 version을 빌드하는 성질이다.
[^c04-reproducible-build]: **reproducible build**는 같은 source와 build environment에서 독립적으로 수행해도 동일한 binary를 생성할 수 있는 build다.
[^c04-trusting-trust]: **Trusting Trust**는 compiler binary에 악성 동작을 넣고 그 compiler가 자신을 다시 빌드할 때도 그 동작을 전파하여 source inspection을 우회하는 공격 개념이다.
[^c04-backdoor]: **backdoor**는 정상 인증 또는 보안 절차를 우회해 system에 접근하도록 숨겨 둔 기능이다.
[^c04-strip]: strip은 object file이나 executable에서 symbol 및 debug 정보 등을 제거해 binary 크기를 줄이는 tool이다.
[^c04-cross-architecture]: **Arm**, **x86_64**, **RISC-V**는 서로 다른 instruction set architecture(ISA)다. 같은 source도 target ISA에 맞는 compiler와 bootstrap chain이 필요하다.
[^c04-kernel]: **kernel**은 process, memory, device, filesystem 같은 핵심 system resource를 관리하며 user space에 system call interface를 제공하는 privileged core다.
[^c04-configure]: configure는 Autoconf가 생성하는 shell script로, build 전에 host 환경을 검사하고 Makefile 등의 설정 file을 생성한다.
[^c04-assembler]: **assembler**는 assembly mnemonic을 processor instruction을 담은 object code 또는 machine code로 변환한다.
[^c04-repl]: **REPL**은 read, eval, print loop의 약자로 입력식을 읽고 평가한 뒤 결과를 출력하는 대화형 programming environment다.
[^c04-sdl]: **SDL**(Simple DirectMedia Layer)은 graphics, audio, input 같은 cross-platform multimedia 기능을 제공하는 library다.
[^c04-debug-symbols]: **debugging symbols**는 binary address를 source의 function, variable, line과 대응시켜 debugger와 backtrace가 사람이 읽을 수 있게 하는 metadata다.
[^c04-bytecode]: **bytecode**는 virtual machine 또는 interpreter가 실행하는 중간 instruction 표현이다. native machine code보다 이식이 쉬운 경우가 많다.
[^c04-isa]: **ISA**(instruction set architecture)는 processor가 실행할 수 있는 instruction, register, memory model의 규격이다.
[^c04-compiler-backend]: **compiler backend**는 compiler의 front-end가 만든 intermediate representation을 target-specific machine code 또는 assembly로 변환하는 부분이다.
[^c04-supply-chain]: **software supply chain**은 source, build tool, dependency, artifact가 software를 만드는 데 이르는 경로 전체를 말한다. 어느 단계든 변조되면 결과물의 신뢰가 훼손될 수 있다.
[^c04-hygienic-macros]: **hygienic macro**는 macro expansion 중 identifier의 scope를 보존해 의도치 않은 name capture를 막는 macro system의 성질이다.

---

### [Fedora, AF\_ALG의 종말을 준비하다](https://lwn.net/Articles/1088489/)

#### 요약

- Linux kernel은 보안 위험과 좁은 사용 범위를 이유로 AF\_ALG를 단계적으로 제거하고 있다.
- Fedora 45는 제한 모드를 미리 도입해 알려지지 않은 사용자와 호환성 문제를 파악하려 한다.
- `cryptsetup` 등 일부 도구는 대체 사용자 공간 crypto 라이브러리를 사용할 수 있지만, 알고리즘 지원 차이가 문제를 일으킬 수 있다.
- Fedora는 업스트림 제거가 배포판 릴리스 중간에 사용자의 시스템을 갑자기 망가뜨리는 일을 피하려 한다.

글쓴이: **Joe Brockmeier**
2026년 8월 18일

Linux kernel의 [Crypto API](https://docs.kernel.org/crypto/index.html)를 위한 [사용자 공간 인터페이스
(AF\_ALG)](https://docs.kernel.org/crypto/userspace-if.html)는 최근의 여러 대형 보안 문제와 연관되어 왔다.[^c05-af-alg] 여기에는 [Copy Fail](https://copy.fail/)과 그 후속 취약점이 포함된다. 이것은 올해 초 [deprecated](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a67afb1884ba)되었다. Eric Biggers와 다른 kernel 개발자들은 이를 [kernel에서 제거하기 위해
작업해 왔다](https://lwn.net/Articles/1077427/#alf). 이를 염두에 두고 Fedora Project는 다음 Fedora 릴리스에서 AF\_ALG 사용을 제한하여, API를 아직 사용하는 이들이 궁극적인 제거에 대비하도록 유도할 계획이다.

#### AF\_ALG와의 작별

사용자 공간 프로그램이 kernel에 crypto 연산을 요청하도록 허용하는 일은, AF\_ALG가 [crypto subsystem maintainer인
Herbert Xu에 의해 2010년에 추가되었을 때](https://lwn.net/Articles/410536/), [인기가 있으면서도
논쟁적이었다](https://lwn.net/Articles/410763/). Xu는 성능 향상을 제공하기 위해 사용자 공간 프로그램이 하드웨어 암호화 가속기에 접근할 수 있도록 AF\_ALG를 [설계했다](https://lwn.net/Articles/410833/).

그러나 일부는 이것이 좋은 생각이라는 데 설득되지 않았다. 예를 들어 Christoph Hellwig는 이것이 "절대적으로 필요하지 않은 한(예: kernel 소비자를 위해) kernel 공간에 있을 이유가 없는" 계산 비용이 큰 코드라고 [말했다](https://lwn.net/Articles/410850/). 그는 CPU가 암호화를 위한 "제대로 된 명령어"를 갖추게 되고 있으므로 사용자 공간 API를 제공하는 일은 더더욱 쓸모가 없어진다고 [덧붙였다](https://lore.kernel.org/all/20100907142427.GA14207@infradead.org/).

돌이켜 보면 AF\_ALG를 추가한 것은 나쁜 생각이었다. 다만 당시 비판자들이 제시한 이유 때문은 꼭 아니었다. 이제 kernel 개발자들이 AF\_ALG를 없애려고 하는 까닭은, 그것이 불필요하다는 점뿐 아니라 Biggers가 AF\_ALG의 deprecation을 문서화한 패치에서 [지적했듯이](https://lwn.net/ml/all/20260430011544.31823-1-ebiggers@kernel.org/), kernel 취약점의 지속적인 원인이기도 하다는 사실이 입증되었기 때문이다.

> AF\_ALG는 거의 완전히 불필요하며, 최신 취약점 발견 도구를 견뎌 내지 못하고 있는 거대한 공격 표면을 노출합니다. [...]
>
> 특히 LLM이 취약점 유입 속도를 가속한 상황에서 이는 지속 가능하지 않습니다. 실제로 이를 사용하는 몇 안 되는 프로그램에 비해 이 기능에 투입되는 노력은 터무니없이 크며, 그 프로그램들도 어차피 사용자 공간 코드로 더 잘 지원될 것입니다.

이제 kernel에서 AF\_ALG를 없앨 때가 분명히 왔지만, kernel 개발자들은 이에 의존하게 된 사용자 공간 프로그램이 중단되지 않도록 신중하게 제거해야 한다.

AF\_ALG를 사용하는 널리 쓰이는 사용자 공간 프로그램 중 하나는 [cryptsetup](https://gitlab.com/cryptsetup/cryptsetup/#what-the-:~:text=Cryptsetup%20is%20an%20open%2Dsource%20utility) 유틸리티다. 이 유틸리티는 [dm-crypt](https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/dm-crypt.html)를 사용하여 LUKS volume 같은 디스크 암호화를 설정하는 데 쓰인다.[^c05-luks] 이 프로젝트는 [cryptsetup 2.8.7 릴리스
노트](https://cdn.kernel.org/pub/linux/utils/cryptsetup/v2.8/v2.8.7-ReleaseNotes)에서 AF\_ALG가 deprecated되었다고 알렸다.

릴리스 노트는 AF\_ALG가 없다면 cryptsetup이 대신 사용자 공간 crypto 라이브러리를 사용할 수 있다고 설명했지만, 일부 방식에는 root 권한이 필요하다. 필요한 알고리즘(또는 암호화 모드)이 사용자 공간 라이브러리에 구현되어 있지 않으면 AF\_ALG의 부재가 "심각한 호환성 문제를 초래할 수 있다"고 사용자에게 경고했다. [Serpent](https://en.wikipedia.org/wiki/Serpent_%28cipher%29)와 [Twofish](https://en.wikipedia.org/wiki/Twofish) cipher는 특히 여러 사용자 공간 라이브러리에 빠져 있는 것으로 언급된다.[^c05-ciphers]

Christoph Anton Mitterer는 cryptosetup 2.8.7-rc1이 공개되었을 때 그 경고를 발견했다. 그는 7월 8일 [linux-crypto 메일링 리스트에서
손을 들고](https://lwn.net/ml/all/27816cc353731e8e5484adad7d0fc447777727d8.camel@scientia.org/), AF\_ALG deprecation의 잠재적 여파를 물었다. Mitterer는 자신이 그 cipher들을 사용하고 있으며 "언젠가 그것들을 쓸 수 없게 된다면 정말로 꽤 유감스러울 것"이라고 말했다. 그는 그것들이 계속 이용 가능하도록 보장하기 위해 무언가 하고 있는지 물었다.

Biggers는 [답변에서](https://lwn.net/ml/all/20260708011112.GA3890@sol/) Mitterer가 cryptsetup 릴리스 노트를 잘못 이해했을 수 있다고 말했다. 지금까지 AF\_ALG에서 제거된 것, 즉 zero-copy 및 async-execution 지원은 cryptsetup에 영향을 주지 않아야 한다. "실제로 이제 자신의 kernel에서 AF\_ALG를 끄는 사람이 더 많기는 합니다. 하지만 범용 배포판은 그렇게 하고 있지 않습니다." 이 말은 7월에는 사실이었지만, 오래지 않아 사실이 아니게 된다.

#### 범용 배포판도 그렇게 하고 있다

Justin Forbes와 Peter Robinson은 Fedora 45를 위한 "[Kernel Crypto Userspace API 비활성화(1단계)](https://fedoraproject.org/wiki/Changes/Disable_CRYPTO_USER_API)" 변경 제안을 내놓았고, Aoife Moloney가 7월 22일 [이를 발표했다](https://lwn.net/ml/all/CAJqbrbfkD7ZA467UHq_fUzUVCgbzQyOp6O%3DvTrwq69BS-TY%2BkQ%40mail.gmail.com/). 제안서는 보안 위험 때문에 AF\_ALG가 kernel에서 deprecated되었고 "7.2 주기 초기에 그 일부가 적극적으로 제거되고 있다"고 언급한다. "지원 종료를 통제된 방식으로 진행할 수 있도록" Fedora 45 릴리스에서 AF\_ALG 사용을 제한할 것을 권고한다. 변경 제안은 그 변경이 배포판에 미칠 영향을 식별해야 하는데, 제안서는 AF\_ALG를 쓰는 것으로 알려진 Fedora 패키지가 많지 않아 "영향은 최소 수준일 것"이라고 말한다.

그러나 제안서는 Fedora에서 AF\_ALG를 사용하는 것으로 알려진 몇 가지도 식별한다. cryptsetup, [iNet Wireless
Daemon](https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/) (iwd), 그리고 [Linux
kernel crypto API 사용자 공간 인터페이스 라이브러리](https://github.com/smuellerDD/libkcapi#libkcapi----linux-kernel-crypto-api-user-space-interface-library-) (libkcapi)가 그것이며, libkcapi는 [dracut](https://dracut-ng.github.io/dracut/)에서 사용된다.[^c05-initramfs] 이 사용자들은 변경의 영향을 받지 않지만, AF\_ALG를 사용하는 서드파티 패키지가 있을 수 있다고 한다. 그렇다면 AF\_ALG가 완전히 사라지기 전에 수정할 수 있도록 지금 그것들을 식별하는 것이 타당하다.

> 첫 단계는 곧 upstream에 병합될 패치들(아마도 7.3에서)을 사용하여 API 사용을 알려진 앱으로 제한하고 그 사용을 제한합니다. 이렇게 하면 Fedora가 알려지지 않은 사용자를 식별하고, upstream에서 인터페이스를 적극적으로 없애기 전에 그들을 원만하게 처리할 수 있습니다. 아무런 통지 없이 모두의 발밑에서 양탄자를 빼 버리는 대신, 사용자에게 더 완만한 절차를 제공하는 것입니다.

언급된 upstream 패치는 특정되어 있지 않지만, Biggers가 6월 22일에 [게시하고](https://lwn.net/ml/all/20260622234803.6982-1-ebiggers@kernel.org/) Xu가 7월 5일에 [적용한](https://lwn.net/ml/all/akoYUzceY0bC1jP1@gondor.apana.org.au/) 패치로 보인다. Biggers는 AF\_ALG를 위해 세 가지 가능한 설정을 갖는 sysctl knob인 `af_alg_restrict`를 추가했다. 0은 제한 없음, 1은 제한된 기능, 2는 완전 비활성화다.[^c05-sysctl]

Linux 7.3부터 기본값은 1로 설정된다. 그러면 iwd, bluez, iproute2 같은 권한 없는 프로세스에는 제한된 알고리즘 allowlist가 활성화되고, 권한 있는 프로세스에는 더 긴 목록이 활성화된다. 그는 "iwd와 bluez [Bluetooth] 같은 일반적인 사용 사례는 이미 고려했다"고 말했으며, 새 기본 설정에서도 iwd가 여전히 작동함을 확인했다.

Fedora 변경 제안의 비상 계획은 문제가 너무 많이 발생하는 것으로 드러날 경우 Fedora 45가 릴리스되기 전에 AF\_ALG를 다시 활성화하는 것이다. Fedora 사용자는 이를 알아차리지 못할 것이라는 전제가 깔려 있다.

#### 논의

Fedora devel 메일링 리스트 토론에서 Ondrej Kozina는 AF\_ALG가 이미 kernel에서 제거되고 있는데도 왜 이 변경이 필요한지 이해하지 못한다고 [말했다](https://lwn.net/ml/all/548b5c22-2d0b-43df-bd46-c1aa471d1d17@redhat.com/).

Robinson은 [답변에서](https://lwn.net/ml/all/CALeDE9MBbpRTgBhS5QZOXCHTBnYXdADKTr4j-kzAUr0G-vdYPg@mail.gmail.com/) 이 변경에는 몇 가지 이유가 있다고 말했다. 하나는 Fedora 사용자가 AF\_ALG의 향후 제거를 알도록 알리는 것이고, 다른 하나는 호환성을 깨는 변경을 릴리스 주기 중간이 아니라 릴리스 경계에서 수행하는 것이다. Fedora 45는 7.2 kernel과 함께 출시된 뒤 7.3 kernel이 릴리스되면 그 버전으로 옮겨 갈 것이기 때문이다. "upstream가 원할 때 원하는 양탄자를 걷어 가서 7.3으로 향하는 upstream 패치가 릴리스 중간에 갑자기 사용자 [시스템]을 망가뜨리게 하고 싶지는 않습니다. 좋은 사용자 경험이 아니지 않습니까?"

그것은 Kozina를 완전히 만족시키지 못했다. 그는 대체 수단 없이 AF\_ALG를 끄는 데 [반대했다](https://lwn.net/ml/all/b2b796c5-80da-49a0-b789-7d40c5b49dfd@redhat.com/). 예를 들어 cryptsetup이 일부 cipher에 사용할 때 사용자에게 [CAP\_SYS\_ADMIN](https://lwn.net/Articles/486306/)을 요구하게 되고, Fedora의 [TrueCrypt](https://en.wikipedia.org/wiki/TrueCrypt) 및 [VeraCrypt](https://en.wikipedia.org/wiki/VeraCrypt) container 지원이 제한된다고 불평했다.[^c05-cap-sys-admin] Robinson은 [지적했다](https://lwn.net/ml/all/CALeDE9OrzKFdAMx6qm3NyYGGgTmFT_eNXRiDwpBfn0unjFpk4Q@mail.gmail.com/) Kozina가 식별한 사용 사례 중 다수가 Fedora 자체에는 존재하지 않는다고. "사용자가 대체로 수동 설치 과정을 통해, 일부러 그렇게 하려고 하지 않는 한 이것들은 사용되지 않을 것으로 생각합니다." 그는 AF\_ALG는 "우리가 좋아하든 싫어하든" 사라질 것이며, 그 취지는 Fedora 사용자를 미리 준비시키는 것이라고 거듭 강조했다.

Barry Scott은 [말했다](https://lwn.net/ml/all/E3DF50F1-8ED9-4B08-B9EF-87FF75A8591E@barrys-emacs.org/) 자신은 AF\_ALG 제한의 영향을 받을 cipher로 "\*internet\*의 조언을 받아" 설정한 LUKS 2 vault를 Raspberry Pi 4에 가지고 있다고. "분명히 f45로 업그레이드하기 전에 지원되는 cipher로 마이그레이션해야 할 것입니다." Robinson은 [언급했다](https://lwn.net/ml/all/CALeDE9N7+tcVOgFXB9QsUk-8-wDfJADKCFNBjX3zg7EAQwv1+Q@mail.gmail.com/) "internet의 조언이 완전히 옳지는 않았다"며, Scott은 "머지않아" 다른 cipher로 마이그레이션해야 하지만 Fedora 45를 위해서일 필요는 없다고 말했다.

Ian McInerney는 [궁금해했다](https://lwn.net/ml/all/178490914870.887813.18200980392199697336@mailman01.rdu3.fedoraproject.org/) 4월에 [릴리스된](https://fedoramagazine.org/announcing-fedora-linux-44/) Fedora 44에는 이것이 무엇을 의미하는지. "이 변경은 F45와 kernel 7.2를 대상으로 하므로, F44에는 kernel 7.2가 릴리스되지 않고 kernel 7.1에 머무른다는 뜻인가요?" Forbes는 [답변했다](https://lwn.net/ml/all/CAFxkdAoju_hV4sYHAdzTrJU08hnhToboxF7KeHsLSxBT6kZWGw@mail.gmail.com/) 특정 Fedora 릴리스에 대해 패치를 추가하거나 제거하는 방법이 있으므로 Fedora 44도 AF\_ALG 제한 패치 없이 7.2를 받게 될 것이라고.

[Fedora Engineering
Steering Committee](https://docs.fedoraproject.org/en-US/fesco/) (FESCo)는 [티켓](https://forge.fedoraproject.org/fesco/tickets/issues/3667)에서 이 변경을 논의했고, 찬성 5표와 반대 0표로 변경을 [승인하기로 투표했다](https://forge.fedoraproject.org/fesco/tickets/issues/3667#issuecomment-1263116). Fedora 45의 beta 릴리스는 9월 15일로 [예정되어 있다](https://fedorapeople.org/groups/schedule/f-45/f-45-key-tasks.html). AF\_ALG 제한이 Fedora 사용자에게 많은 문제를 일으킬지, 아니면 단계적 폐지가 비교적 별일 없이 진행될지는 지켜볼 만하다.

[댓글 (5개 게시됨)](https://lwn.net/Articles/1088489/#Comments)

[^c05-af-alg]: **AF\_ALG**는 사용자 공간 프로그램이 socket 기반 인터페이스로 Linux kernel Crypto API의 암호화 알고리즘과 구현을 호출하게 하는 Linux 주소 계열이다. kernel에 대규모 공격 표면을 추가한다.
[^c05-luks]: **LUKS**(Linux Unified Key Setup)는 Linux 디스크 암호화의 표준 메타데이터 형식이며, **dm-crypt**는 device-mapper 위에서 block device 암호화를 제공하는 kernel 대상이다.
[^c05-ciphers]: **Serpent**와 **Twofish**는 대칭 block cipher다. 호환성은 선택한 cipher와 모드를 사용자 공간 crypto 라이브러리가 구현하는지에 달려 있다.
[^c05-initramfs]: **dracut**는 초기 부팅에 쓰이는 initramfs를 생성하는 도구다. initramfs는 root filesystem을 마운트하기 전에 필요한 driver와 사용자 공간을 담는다.
[^c05-sysctl]: **sysctl**은 `/proc/sys`를 통해 runtime 중 kernel parameter를 읽고 설정하는 Linux 메커니즘이다. 여기서 knob는 AF\_ALG 접근 정책을 조절한다.
[^c05-cap-sys-admin]: **CAP\_SYS\_ADMIN**은 Linux capabilities 중 매우 광범위하고 강력한 권한이다. 전통적 root 권한을 세분화한 capability 모델에서 흔히 "새로운 root"라고 불릴 정도로 많은 privileged 동작을 허용한다.

---

### [Arm용 128비트 페이지 테이블](https://lwn.net/Articles/1088125/)

#### 요약

- 128비트 PTE는 현재 Arm의 물리 주소 범위를 즉시 넓히지는 않지만, 향후 확장할 여유와 소프트웨어용 비트를 제공한다.
- PTE가 커지면 페이지 테이블 메모리 사용량이 두 배가 되고 huge page 크기가 줄어드는 비용이 있다.
- SKL 필드는 중간 단계에서도 huge page를 지정할 수 있어 페이지 테이블 자체에 huge page를 쓸 가능성을 연다.
- Arm에는 128비트 원자 연산이 없으므로 커널은 `ldp` 및 `stp` 기반 접근으로 이를 처리한다.
- 하드웨어 보급과 배포판의 부팅 호환성 문제가 실제 채택의 주요 과제다.

글쓴이 **Jonathan Corbet**
2026년 8월 13일

프로세서의 페이지 테이블 엔트리 크기는 해당 프로세서가 접근할 수 있는 물리 메모리의 양을 직접 제한한다. 32비트 시절에는 그 한계가 4GB였는데, 한때는 거의 무한해 보였던 메모리 양이지만 이제는 기본적인 AI 지원 “hello world” 앱조차 담기 어려울 것이다. 널리 쓰이는 대부분의 아키텍처에서 64비트로 확장하면서 이런 한계는 사라진 듯하다. 예를 들어 일부 Arm 시스템은 그중 56비트를 사용해 최대 72PB의 메모리에 접근할 수 있다. 따라서 Arm 아키텍처가 더 큰 페이지 테이블 엔트리(PTE)[^c06-pte]를 지원하도록 진화하고 있다는 사실은 놀라울 수 있다. Anshuman Khandual의 [이 패치 세트](https://lwn.net/ml/all/20260729122452.3797443-1-anshuman.khandual@arm.com)는 128비트 PTE 지원을 추가하지만, 누가 이 기능의 혜택을 볼지는 완전히 분명하지 않다.

PTE에서 가장 중요한 정보는 물리 주소이다. 최하위 엔트리에서는 실제 메모리의 주소이고, 상위 레벨에서는 다음 테이블의 주소다. 하지만 PTE의 모든 비트가 그 주소를 담는 것은 아니다. 최소한 가상 주소에서 페이지 내부 오프셋에 해당하는 최하위 비트는 다른 용도로 사용할 수 있다. “[페이지와 folio에 관하여](https://lwn.net/Articles/1064861/)”라는 기사는 PTE 엔트리를 상당히 자세히 설명한다. 64비트 PTE가 어떻게 나뉠 수 있는지를 보여 주는 다음 도표는 그 기사에서 가져온 것이다.

> ![[Simple address
> structure]](https://static.lwn.net/images/2026/address-structure1.svg)

56비트 주소와 4096바이트 페이지로 구성된 현대의 64비트 Arm 시스템에서는 PTE의 최대 44비트를 메모리 내 페이지의 물리 주소를 표현하는 데 사용할 수 있고, 12비트는 관리 용도로 쓸 수 있다.

PTE를 128비트로 확장하면 당연히 엔트리에 더 많은 정보를 저장할 수 있지만 비용이 따른다. PTE 크기를 두 배로 하면 페이지 테이블의 크기도 명백히 두 배가 된다. 일부 워크로드에서는 이미 페이지 테이블이 사용자가 원하는 것보다 많은 메모리를 차지한다. 페이지 테이블이 차지한 모든 페이지는 시스템 워크로드에 사용할 수 없다. 한 페이지에는 이전의 절반만큼의 PTE만 담을 수 있으므로 huge page에도 영향이 있다. 64비트 PTE 시스템에서 2MB인 PMD 레벨 huge page[^c06-hugepage]는 PTE가 128비트가 되면 1MB로 줄어들고, PUD 레벨 huge page는 1GB에서 256MB로 축소된다. 그런 페이지에서는 페이지 테이블 레벨 두 개가 제거되므로 4배 감소하는 것이다. 더 빠른 translation lookaside buffer(TLB)[^c06-tlb] 접근을 위해 병합할 수 있는 다중 크기 transparent huge page의 크기 또한 비슷한 비율로 줄어든다. 성능을 위해 huge page에 크게 의존하는 워크로드에서는 이러한 감소가 고통스러울 수 있다.

더 큰 PTE 크기로 전환하는 데 명확한 비용이 있으므로, 다른 영역에서 이득도 있을 것이라고 예상하게 된다. 그렇지 않다면 변경할 이유가 거의 없을 것이다. 그 이득을 이해하려면 새 형식을 좀 더 자세히 살펴볼 가치가 있다. 128비트 Arm PTE의 세부 사항은 [이 페이지](https://support.arm.com/documentation/ddi0487/mb/-Part-D-The-AArch64-System-Level-Architecture/-Chapter-D8-The-AArch64-Virtual-Memory-System-Architecture/-D8-3-Translation-table-descriptor-formats/-D8-3-2-VMSAv9-128-descriptor-formats)에서 볼 수 있다. 최하위 PTE 형식은 다음과 같다.

> ![[128-bit PTE format]](https://static.lwn.net/images/2026/128-bit-pte.svg)

바로 눈에 띄는 한 가지는 비트 12부터 55까지 뻗어 있는 PTE의 주소 부분이 길이 44비트에 불과하다는 점이다. 여기에 12개의 오프셋 비트를 더하면 최대 주소 크기는 56비트로, 현재 64비트 PTE로 가능한 것과 같다. 따라서 주소 지정 가능한 물리 메모리 범위를 확장하는 것은 이 변경의 즉각적인 목표가 아니다. 그렇긴 해도 예약 비트, 즉 회색으로 표시되고 레이블이 없는 비트를 모두 주목할 만하다. 최상위 주소 비트 위에 예약 비트가 35개 있어, 향후 주소 필드를 확장할 공간이 상당히 남아 있다.

PTE 중에는 하드웨어가 전혀 해석하지 않는 비트가 열 개 있으며, 이 비트들은 소프트웨어용으로 예약되어 있다. 이는 64비트 PTE를 사용하는 Arm 시스템에서 이용할 수 있는 다섯 비트의 두 배다. 비트 다섯 개가 많아 보이지 않을 수 있지만, 커널은 결국 메모리 관리에 이를 유용하게 활용할 수 있을 것이다.

비트 109와 110은 “skip level”(SKL) 필드다. 모든 페이지 테이블 레벨에 존재하는 이 필드는 페이지 테이블 순회 과정이 동작하는 방식을 제어한다. 대부분의 시스템에서 페이지 테이블 계층은 경직되어 있으며, 예상된 수의 레벨(보통 3개에서 5개)이 항상 존재한다. 유일한 예외는 huge page로, 검색의 끝에서 하나 이상의 레벨이 제거된다. 최종 페이지 테이블 레벨보다 한 레벨 위에 있는 PMD를 생각해 보자. PMD의 한 엔트리는 PTE 전체 페이지 하나를 가리키며 (일반적으로) 2MB의 주소 공간을 담당한다. 그러나 PMD 엔트리에 비트를 설정하면 커널은 전체 2MB가 단일 페이지에 할당되었음을 나타낼 수 있다. 이것이 PMD 레벨 huge page다.

SKL 필드는 이 메커니즘을 어느 정도 일반화한다. 조회 과정의 다음 단계가 최종 단계가 아니라 페이지 테이블 계층의 다른 레벨이더라도 huge page임을 나타낼 수 있다. 이 기능은 페이지 테이블 자체에 huge page를 사용하는 길을 여는 것으로 보이며, 주소 변환을 가속하고 TLB 사용량을 줄일 잠재력이 있다.

128비트 PTE 지원에 필요한 커널 변경은 비교적 작으며, 주로 다양한 필드와 비트의 위치를 설명하는 매크로 정의 모음으로 이루어진다. 가장 큰 변화를 일으키는 부분은 페이지 테이블 조작과 관련된다. 페이지 테이블 계층의 여러 레벨에서 엔트리를 다룰 때는 전체 엔트리가 일관되도록 원자적으로 읽는 것이 중요하다. 현재 커널에서는 READ\_ONCE()로 읽지만, READ\_ONCE()는 원자 연산에 의존하고 Arm CPU에는 128비트 원자 연산이 없다. PTE 수정에도 비슷한 우려가 적용된다. 이 패치 시리즈는 이러한 접근을 새 함수 쌍(ptval\_get() 및 ptval\_set())으로 감싼다. 이 함수들은 기본적으로 READ\_ONCE()와 WRITE\_ONCE()를 사용하지만 필요하면 아키텍처가 재정의할 수 있다. 128비트 PTE용으로 빌드된 Arm 시스템에서 이 함수들은 원자적인 ldp 및 stp(load-pair와 set-pair) 명령으로 구현된다.[^c06-atomic]

적어도 현재 구현에서는 커널을 128비트 PTE용으로 특별히 빌드해야 하며, 그렇게 빌드한 커널은 해당 PTE 크기를 지원하지 않는 CPU에서 부팅할 수 없다. 이는 배포판을 더 어렵게 만들 것이다. 배포판에는 빌드하는 커널 수를 최소화하려는 강한 동기가 있다. 이 문제를 해결하려면 부팅 시점 코드 패칭이 상당히 필요할 것이 거의 확실하지만, 배포판이 더 큰 PTE 지원 활성화를 고려하기 전에 필요할 수 있다.

이 시리즈는 몇 차례 RFC 반복을 거쳤고 어느 정도 안정화되고 있는 것으로 보인다. 물론 128비트 PTE를 지원하는 하드웨어를 가진 사람은 상대적으로 적으므로, 이 작업에 대한 현장 테스트 양은 필연적으로 제한적이다. 하지만 하드웨어가 더 널리 보급될 무렵에는 Linux가 이를 지원할 준비를 마쳤을 가능성이 크다. 다만 단기적으로는 많은 시스템이 이 기능을 사용해 이득을 볼지 전혀 분명하지 않다.

[댓글 (8개 게시됨)](https://lwn.net/Articles/1088125/#Comments)

### [BPF, 지속적 테스트, 그리고 stable kernel](https://lwn.net/Articles/1087823/)

#### 요약

- BPF-CI는 LLM 기반 코드 검토, ASAN, verifier 성능 회귀 탐지, GCC·Clang 실행으로 적용 범위를 넓혔다.
- 테스트 대상이 BPF 트리에서 `linux-next`까지 확장되어 통합 문제를 더 일찍 찾을 수 있게 되었다.
- stable kernel용 BPF self test는 AUTOSEL이 놓칠 수 있는 verifier 회귀와 backport 문제를 발견한다.
- stable 브랜치의 테스트 실패에는 잘못 backport된 테스트, namespace 차이, 누락된 선행 패치가 포함된다.
- 테스트를 backport 변경과 함께 backport하고, 아키텍처 다양성을 추가하는 일이 앞으로의 과제다.

글쓴이 **Daroc Alden**
2026년 8월 14일

---

[LSFMM+BPF](https://lwn.net/Articles/lsfmmbpf2026/)

Ihor Solodrai와 Shung-Hsi Yu는 2026년 [Linux Storage, Filesystem, Memory-Management, and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/)에서 테스트와 관련된 두 세션으로 BPF 트랙을 마무리했다. Solodrai는 BPF의 지속적 통합(CI)[^c06-ci] 테스트에서 바뀐 점을 발표했다. Yu는 stable kernel에서 BPF 업데이트를 더 철저히 테스트하는 데 필요한 일이 무엇인지 발표했다. 두 사람은 BPF 서브시스템의 CI 테스트가 좋은 상태에 있다고 말했다. 그럼에도 Solodrai와 Yu는 앞으로 더 나은 테스트 커버리지를 가능하게 할 몇 가지 길을 제시했다.

#### BPF CI

지난해부터 Solodrai는 자신이 관리하는 BPF-CI 인프라에 여러 개선을 적용했다. 그는 특히 LLM 기반 검토, 추가 테스트 워크플로, 그리고 테스트 인프라에 적용한 몇 가지 업데이트를 논의하고 싶어 했다. LLM 검토는 [Sashiko](https://github.com/sashiko-dev/sashiko#sashiko)가 가능함을 보여 주기 전부터 Solodrai가 조사하던 것이었다. 그는 결국 이 아이디어를 독립적으로 구현했다. BPF-CI 인프라는 [Chris Mason의 검토 프롬프트](https://github.com/masoncl/review-prompts#review-prompts-for-ai-assisted-code-review), semantic search, Lore 메일링 리스트 아카이브, 커널 소스 트리를 사용하여 BPF 변경에 관한 검토를 생성한다. 검토는 GitHub actions를 통해 트리거된다. BPF 트리의 GitHub 미러에 pull request를 만들면 잠시 뒤 LLM의 검토가 담긴 댓글이 달린다.

처음에 Solodrai는 이런 방식이 유용할지 알지 못했다. 알고 보니 “지금은 모두가 AI 검토에 흥분하고” 있으므로, 유용해 보인다. 전담 개발 팀이 있는 Sashiko는 Solodrai 혼자 관리하는 도구보다 더 강력하므로, 그는 BPF-CI-LLM 검토를 끄는 방안을 고려하고 있다. 다만 Sashiko가 Google을 사용하는 것과 달리 다른 LLM 제공자(Anthropic)를 사용하므로 약간 다른 성격의 검토를 만들며, 그 때문에 당분간 유지할 생각이다. 또한 모든 실패를 직접 조사하지 않아도 되도록 LLM을 사용해 flaky test[^c06-flaky]를 조사하고 보고하고 있다.

전통적인 테스트 커버리지도 확장되었다. 이제 BPF self test의 user-space 부분은 address sanitization(ASAN)[^c06-asan]을 활성화한 상태로 실행된다. 이는 libbpf의 버그를 잡기 위한 것이었지만, 지금까지는 주로 테스트 자체의 버그를 잡았고 그것도 여전히 유용하다. BPF 프로그램을 로드하는 데 걸리는 시간을 측정하는 커널 트리의 도구인 [Veristat](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/testing/selftests/bpf/veristat.c)는 verifier의 성능 회귀를 잡기 위해 확장된 프로그램 코퍼스에서 실행된다.

이전에는 테스트가 BPF 트리에 대해서만 실행되었다. 이제 `linux-next`에도 실행되므로 통합 문제를 더 일찍 잡는 데 도움이 될 것이다. self test는 이제 GCC와 Clang 모두를 사용해 실행된다. 예전에는 둘 모두로 컴파일했지만 Clang으로 컴파일한 테스트만 실행했다. 이제 두 컴파일러의 출력물을 모두 실행한다. 이 테스트는 아직 새롭고 더 개발이 필요할 수 있지만, Solodrai는 유용할 것으로 기대한다.

기반 CI 테스트 인프라도 일부 업데이트되었는데, 주로 Ubuntu에서 Debian으로 옮기는 작업이었고 일부 Ubuntu 호스트는 남아 있다. 테스트 머신은 GCC 14와 Clang 19에서 업그레이드한 GCC 15.x와 Clang 21.x를 사용한다. Solodrai는 컴파일러 버전 변경이 언급할 만큼 사소했으면 좋았겠지만, 상당한 작업량이 들었다. 그는 곧 GCC 16과 Clang 22로 업그레이드하기를 바란다.

이 모든 좋은 소식과 함께, 그는 계속되는 불만도 몇 가지 갖고 있다. Anthropic, GitHub, Ubuntu 저장소, 심지어 git.kernel.org까지 모두 종종 중단된다. 그가 CI 인프라 작업을 시작했을 때 실패는 보통 그의 잘못이었다. 이제는 대부분 의존하는 외부 서비스의 잘못이라서 답답하다. “요즘 소프트웨어는 덜 신뢰할 수 있습니다. 그 이유가 무엇인지 궁금하지만, 이 회사들에 영향력이 있다면 더 신뢰할 수 있게 만들어 주십시오.”

그는 이어 모인 개발자들에게 CI에서 무엇을 더 테스트해야 하는지 물었다. Amery Hung은 빌드별이 아니라 테스트 사례별로 실패와 성공을 보여 주는 대시보드를 제안했다고 그가 말했다. 다른 사람들은 대체로 테스트 인프라의 상태에 만족했지만, 누군가는 LLM 기반 검토에 더 일찍 접근할 수 있으면 좋겠다고 제안했다.

이것이 BPF-CI-LLM 검토와 Sashiko의 차이에 관한 긴 토론으로 이어졌다. 전자의 한 장점은 문맥을 위해 메일링 리스트 아카이브를 검색할 수 있다는 것이다. 누군가는 이 아이디어를 Sashiko 개발자인 Roman Gushchin에게 가져가자고 제안했다. 그 차이가 사라지더라도 BPF 개발자들은 미묘한 문제를 잡는 데 여러 독립적인 검토가 도움이 된다고 생각했다.

#### Stable kernels

Linux kernel의 stable release는 수동으로 backport 대상으로 표시된 패치나 [AUTOSEL](https://lwn.net/Articles/825536/) 패치 선택 도구가 고른 패치를 사용해 조립된다.[^c06-stable] Yu가 설명한 문제는 AUTOSEL이 BPF self test를 실행하지 않는다는 점이다. 패치를 backport해야 하는지 판단할 때 AUTOSEL은 패치가 깨끗하게 적용되는지 확인하지만, 그것만으로 verifier가 의도대로 계속 동작한다고 확신하기에는 부족하다.

지난해 Yu는 이를 고치자고 제안했고, Solodrai는 기존 self test에 접근할 수 있게 하여 설정을 복제할 수 있도록 도왔다. 이제 Yu는 여러 다른 stable 트리에 대해 self test를 실행하고 있으며, 추가된 커버리지가 무엇을 잡아냈는지 공유할 수 있다.

실패 대부분은 잡음이라고 그가 말했다. 특히 backport된 코드에는 맞지 않는 테스트에서 그렇다. 예를 들어 세션 직전에 그는 6.6 kernel에 없는 helper를 사용하는 새 테스트를 추가한 변경을 되돌리는 revert를 보냈다. 때로 실패는 더 미묘하다. 한 backport된 테스트는 네트워크의 maximum transfer unit을 10바이트로 설정했는데, network namespace[^c06-netns] 내부에서는 괜찮지만 충분히 오래된 커널에서는 root namespace에 영향을 주어 많은 후속 실패를 일으켰다.

빌드 실패는 더 성가시지만, 대부분은 놓친 추가 패치를 backport해야 하는 경우다. 테스트는 더 복잡한 문제도 잡았다. 예를 들어 struct\_ops 구조체의 포인터가 유효하다고 잘못 가정해 발생한 kernel panic을 발견했다. 그렇지만 Yu는 이 작업을 시작했을 때 더 많은 실제 회귀를 잡기를 바랐다. 회귀를 잡는 가장 유용한 방법은 backport하는 모든 변경과 함께 테스트도 backport하는 것이라고 그가 말했다.

Daniel Borkmann은 Yu가 얼마나 자주 테스트를 실행하는지 알고 싶어 했다. Yu는 매일 아침, 일어나서 결과를 볼 수 있도록 실행한다고 답했다. Borkmann은 stable 테스트를 주 BPF-CI 테스트 스위트의 일부로 실행할 방법이 있는지 물었다. Yu는 불가능하다고 생각하지는 않았지만, 약간 다른 방식으로 하고 있다고 언급했다. 모든 변경에서 실행하는 대신, 그의 테스트는 실행될 때 stable 트리에 있는 것을 가져오기만 한다. 메일링 리스트를 지켜보는 것만큼 빠르지는 않지만, Greg Kroah-Hartman이 stable release candidate를 만들기 전에 대개 완전한 테스트 실행을 끝낼 수 있다고 말했다. 그는 stable 테스트를 주 BPF-CI 인프라와 분리해 두는 것도 유용하다고 생각한다.

Solodrai는 Yu가 stable 브랜치에서 테스트를 backport하거나 테스트 실패를 조사해야 하는 일이 얼마나 자주 있었는지 물었다. Yu는 현재 세 stable 브랜치를 테스트하고 있으며, 한 달에 한 번 정도는 무언가가 깨지는 것을 본다. 엄청난 양은 아니지만 유지 관리할 사람은 필요하다고 Yu는 말했다.

물론 더 할 일이 있다. Yu는 더 많은 self test를 backport해야 하며, 테스트에는 서로 다른 아키텍처에서의 실행도 포함해야 할 가능성이 크다고 말했다. known-bad 테스트 목록을 유지할 수 있다면 BPF 개발 트리의 self test를 stable kernel에서 실행하는 일도 가능할 수 있다. 어느 쪽이든 커널의 BPF 코드는 어느 때보다 더 많은 자동화 테스트와 검토를 받고 있다. summit 전반에서 수많은 흥미로운 새 기능이 논의된 만큼, 테스트가 그 속도를 따라가고 있다는 사실은 반갑다.

[댓글 (10개 게시됨)](https://lwn.net/Articles/1087823/#Comments)

[^c06-pte]: **PTE (page-table entry)**: 가상 페이지를 물리 페이지에 매핑하고 접근 권한·캐시 정책 같은 속성을 담는 페이지 테이블의 엔트리다.
[^c06-hugepage]: **huge page**: 일반 페이지보다 큰 메모리 매핑으로, 페이지 테이블 단계와 TLB 미스를 줄여 대용량 연속 메모리 작업을 가속할 수 있다.
[^c06-tlb]: **TLB**: 최근의 가상-물리 주소 변환을 캐시하는 CPU 구성 요소다.
[^c06-atomic]: **원자적 접근**: 다른 CPU나 실행 흐름이 중간 상태를 관찰하지 못하도록 하나의 불가분 작업처럼 값을 읽거나 쓰는 방식이다.
[^c06-ci]: **CI (continuous integration)**: 변경을 자동으로 빌드·테스트하여 통합 문제를 조기에 찾는 개발 관행이다.
[^c06-flaky]: **flaky test**: 코드 변경과 무관하게 간헐적으로 성공하거나 실패해 신뢰하기 어려운 테스트다.
[^c06-asan]: **ASAN (AddressSanitizer)**: use-after-free, 버퍼 오버플로 같은 메모리 안전성 오류를 감지하는 런타임 도구다.
[^c06-stable]: **stable kernel**: 새 기능보다 검증된 수정의 backport에 초점을 맞춘 Linux kernel 유지보수 브랜치와 릴리스다.
[^c06-netns]: **network namespace**: 네트워크 인터페이스, 라우팅, 방화벽 상태 등을 격리하는 Linux namespace 기능이다.

---

### [7.2 커널의 개발 통계](https://lwn.net/Articles/1088776/)

#### 요약

- 7.2는 거의 60만 줄을 추가한, 역사상 두 번째로 바쁜 Linux 커널 릴리스였다.
- 2,652명의 개발자가 기여해 개발자 참여 기록을 새로 썼다.
- `Assisted-by` 및 `Fixes` 태그의 급증은 LLM이 패치 작성과 버그 탐지에 미치는 영향을 보여 준다.
- 활발한 활동은 7.3 개발 주기에도 이어질 전망이다.

글쓴이 **Jonathan Corbet**
2026년 8월 17일

Linus Torvalds는 들어오는 수정의 수가 여전히 ""바랐던 것보다 더 많다""고 언급한 뒤, 8월 17일에 [7.2 커널을 릴리스했다](https://lwn.net/ml/all/CAHk-=wjk5StpAmUKHacj=GPKwA88y_YRHK=i_YAJFgmxn1=k4w@mail.gmail.com/). 실제로 7.2는 커널 역사상 가장 바쁜 개발 주기 중 하나였으며, 거의 60만 줄의 코드를 추가했다. 커널 개발 커뮤니티가 어떻게 변화하고 있는지 파악하기 위해 몇 가지 통계를 살펴볼 때다.

7.2 릴리스에는 16,418개의 비병합 커밋이 메인라인[^c07-mainline]에 들어왔으며, 이미 바빴던 7.1 릴리스를 넘어섰다. 이는 실제로 커널 역사상 두 번째로 바쁜 릴리스다. [6.7 릴리스](https://lwn.net/Articles/956765/)만이 더 많은 커밋을 받아들였지만, 6.7은 bcachefs 개발 이력의 병합이 지배했던 반면 7.2의 규모는 더 폭넓은 기반을 가진다.

이 커밋들은 2,652명의 개발자가 기여했으며, 이는 이전 기록(7.1의 2,479명)을 크게 넘어선 수치다. Git 시대가 시작된 이래 개발자 참여 이력을 살펴보면 결과는 다음과 같다.

> ![[릴리스별 개발자 수 선 그래프]](https://static.lwn.net/images/2026/developer-plot-7.2.svg)

(이 그래프는 여기의 많은 정보와 마찬가지로 구독자 전용 [LWN Kernel Source Database](https://lwn.net/ksdb/)에서 가져왔다.) 전체 이력에 걸쳐 뚜렷한 추세가 있다. 각 릴리스에 기여하는 개발자 수는 시간이 지나면서 증가한다. 하지만 그 선의 기울기는 분명히 변했다.

7.2 작업에서 가장 활발했던 개발자는 다음과 같다.

> | 가장 활발한 7.2 개발자 | |
> | --- | --- |
> | | 변경 집합 기준 | | | | --- | --- | --- | | Uwe Kleine-König | 151 | 0.9% | | Rosen Penev | 146 | 0.9% | | Ian Rogers | 138 | 0.8% | | Johan Hovold | 133 | 0.8% | | Arnaldo Carvalho de Melo | 131 | 0.8% | | Chuck Lever | 129 | 0.8% | | Eric Dumazet | 121 | 0.7% | | Ville Syrjälä | 115 | 0.7% | | Johannes Berg | 112 | 0.7% | | Krzysztof Kozlowski | 110 | 0.7% | | Thorsten Blum | 108 | 0.7% | | Namjae Jeon | 106 | 0.6% | | Christoph Hellwig | 104 | 0.6% | | Sean Christopherson | 100 | 0.6% | | Jakub Kicinski | 96 | 0.6% | | SJ Park | 94 | 0.6% | | Mike Rapoport | 91 | 0.6% | | Dmitry Baryshkov | 87 | 0.5% | | Eric Biggers | 86 | 0.5% | | Rafael J. Wysocki | 78 | 0.5% | | | 변경된 줄 기준 | | | | --- | --- | --- | | Matthew Stewart | 83587 | 8.4% | | Hawking Zhang | 62893 | 6.3% | | Miguel Ojeda | 38979 | 3.9% | | Ian Rogers | 31949 | 3.2% | | Darren Ye | 20843 | 2.1% | | Ethan Nelson-Moore | 16893 | 1.7% | | Harry Wentland | 15233 | 1.5% | | Uwe Kleine-König | 13803 | 1.4% | | Ingo Molnar | 13649 | 1.4% | | Chuck Lever | 10172 | 1.0% | | Eric Biggers | 10067 | 1.0% | | Jakub Kicinski | 9449 | 0.9% | | Rodrigo Siqueira | 7749 | 0.8% | | Johannes Berg | 7110 | 0.7% | | Arnd Bergmann | 7085 | 0.7% | | Emil Tsalapatis | 6810 | 0.7% | | Vivek Aknurwar | 6544 | 0.7% | | Rob Clark | 6490 | 0.6% | | Sabrina Dubroca | 6401 | 0.6% | | Svyatoslav Ryhel | 6072 | 0.6% | |

Uwe Kleine-König [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=72)]는 드라이버 하위 시스템 전반의 정리 작업으로 7.2 릴리스에서 가장 많은 커밋을 기여했다. Rosen Penev [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=10224)]는 아키텍처별, 드라이버, 네트워킹, 암호 하위 시스템 등을 아우르는 LLM 작성 버그 수정의 긴 목록을 기여했다. Ian Rogers [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=1033)]는 Arnaldo Carvalho de Melo [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=1031)]와 마찬가지로 사용자 공간 `perf` 도구[^c07-perf]를 광범위하게 작업했다. Johan Hovold [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=3)]는 주로 SPI[^c07-spi] 및 USB 하위 시스템을 다수 개선했다.

Matthew Stewart [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=38654)]는 오래된 전통대로 더 거대한 기계 생성 `amdgpu`[^c07-amdgpu] 헤더 파일을 추가하여 변경 줄 수 부문 정상에 올랐으며, Hawking Zhang [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=949)]도 마찬가지였다. Miguel Ojeda [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=1135)]는 [Rust `zerocopy` 크레이트](https://docs.rs/zerocopy/latest/zerocopy/)를 커널 소스에 들여왔다. Darren Ye [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=40316)]는 MediaTek mt8196 사운드 드라이버를 추가했다.

7.2 커밋 중 8%를 조금 넘는 수가 `Tested-by` 태그를 달았고, 48%에는 `Reviewed-by` 태그가 포함됐다. 특히 검토 태그는 최근 릴리스에서 완만한 하락 추세를 보이고 있다.
> ![[릴리스별 Reviewed-by 태그]](https://static.lwn.net/images/2026/review-tags-7.2.svg)

그 하락이 실제로 수행되는 검토 양의 감소를 반영하는지는 기껏해야 불분명하다. 어쨌든 이번 주기에서 가장 활발한 테스터와 검토자는 다음과 같다.

> | 7.2의 테스트 및 검토 공로 | |
> | --- | --- |
> | | Tested-by | | | | --- | --- | --- | | Dan Wheeler | 117 | 7.0% | | Luiz Capitulino | 54 | 3.2% | | James Clark | 44 | 2.6% | | Sarthak Sharma | 44 | 2.6% | | Venkat Rao Bagalkote | 32 | 1.9% | | Tommaso Merciai | 27 | 1.6% | | David Riley | 27 | 1.6% | | Jie Gan | 27 | 1.6% | | Geert Uytterhoeven | 25 | 1.5% | | Arthur Kiyanovski | 25 | 1.5% | | Marek Szyprowski | 25 | 1.5% | | Randy Dunlap | 24 | 1.4% | | Shivaprasad G Bhat | 24 | 1.4% | | Rinitha S | 21 | 1.3% | | Vitaly Prosyak | 20 | 1.2% | | | Reviewed-by | | | | --- | --- | --- | | Konrad Dybcio | 231 | 2.2% | | Dmitry Baryshkov | 225 | 2.1% | | Andy Shevchenko | 175 | 1.7% | | Geert Uytterhoeven | 171 | 1.6% | | Krzysztof Kozlowski | 152 | 1.5% | | Frank Li | 147 | 1.4% | | Ilpo Järvinen | 145 | 1.4% | | Christoph Hellwig | 143 | 1.4% | | Jan Kara | 121 | 1.2% | | Christian König | 120 | 1.1% | | Linus Walleij | 116 | 1.1% | | Alex Deucher | 105 | 1.0% | | Simon Horman | 102 | 1.0% | | Jeff Layton | 101 | 1.0% | | Ido Schimmel | 94 | 0.9% | |

Dan Wheeler [[KSDB](https://lwn.net/ksdb/releases/v7.2/taglist?tag=tested-by&dev=612)]는 언제나 그렇듯 AMD 그래픽 드라이버 패치 작업 덕분에 최고 테스터다. 검토 측면에서는 Konrad Dybcio [[KSDB](https://lwn.net/ksdb/releases/v7.2/taglist?tag=reviewed-by&dev=236)]가 231개 변경에 자신의 태그를 추가했고 Dmitry Baryshkov [[KSDB](https://lwn.net/ksdb/releases/v7.2/taglist?tag=reviewed-by&dev=8)]는 225개에 태그를 달았다. 두 사람 모두 Qualcomm 장치용 드라이버와 devicetree[^c07-devicetree] 파일에 집중하는 경향이 있으며, 7.1 주기에서도 그 목록의 최상위에 있었다.

7.2 커널 작업은 식별할 수 있었던 249개 고용주가 지원했으며, 그중 가장 활발한 곳은 다음과 같다.

> | 가장 활발한 7.2 고용주 | |
> | --- | --- |
> | | 변경 집합 기준 | | | | --- | --- | --- | | (알 수 없음) | 2743 | 16.7% | | Intel | 1512 | 9.2% | | Google | 1191 | 7.3% | | Red Hat | 873 | 5.3% | | AMD | 813 | 5.0% | | Qualcomm | 767 | 4.7% | | (없음) | 743 | 4.5% | | NVIDIA | 535 | 3.3% | | Meta | 441 | 2.7% | | (컨설턴트) | 429 | 2.6% | | SUSE | 358 | 2.2% | | Renesas Electronics | 328 | 2.0% | | IBM | 307 | 1.9% | | Kylin | 278 | 1.7% | | NXP Semiconductors | 264 | 1.6% | | Oracle | 245 | 1.5% | | Arm | 222 | 1.4% | | BayLibre | 203 | 1.2% | | Microsoft | 201 | 1.2% | | Bootlin | 194 | 1.2% | | | 변경된 줄 기준 | | | | --- | --- | --- | | AMD | 224121 | 22.4% | | (알 수 없음) | 103861 | 10.4% | | Google | 102565 | 10.3% | | Qualcomm | 59021 | 5.9% | | Intel | 53661 | 5.4% | | Red Hat | 51559 | 5.2% | | Meta | 38635 | 3.9% | | (없음) | 28218 | 2.8% | | NVIDIA | 27417 | 2.7% | | MediaTek | 22025 | 2.2% | | NXP Semiconductors | 17692 | 1.8% | | BayLibre | 15972 | 1.6% | | Oracle | 12233 | 1.2% | | Microsoft | 11786 | 1.2% | | Renesas Electronics | 11103 | 1.1% | | Linaro | 10209 | 1.0% | | (컨설턴트) | 9362 | 0.9% | | IBM | 9205 | 0.9% | | Texas Instruments | 8398 | 0.8% | | SUSE | 8350 | 0.8% | |

이번에 가장 중요한 변화는 아마도 소속을 알 수 없는 개발자가 크게 증가한 점이다. 이는 적어도 부분적으로는 커널 커뮤니티로 유입되는 신규 개발자의 지속적인 물결을 반영한다.

#### 신규 개발자와 그들의 도구

이전 두 커널 릴리스는 모두 처음으로 변경을 기여한 개발자 수의 기록을 세웠고, 7.2는 이전에 여기에서 보이지 않았던 기여자 613명 [[KSDB](https://lwn.net/ksdb/releases/v7.2/first_timers)]으로 그 기록을 다시 깼다. 여기서도 다시 한 번 추세는 명확하다.

> ![[릴리스별 최초 개발자]](https://static.lwn.net/images/2026/first-timers-7.2.svg)

가장 활발한 신규 개발자는 Bryam Vargas [[KSDB](https://lwn.net/ksdb/releases/v7.2/commits?dev=40015)]였으며, 입력, NVMe[^c07-nvme], F2FS[^c07-f2fs], AppArmor[^c07-apparmor], Landlock[^c07-landlock], SELinux[^c07-selinux], NTFS, WiFi, ATA, SCSI, 네트워킹, Ceph, Thunderbolt 등의 하위 시스템에서 문제를 고치는 43개 커밋을 기여했다. 이전에도 여기서 관찰했듯, 숙련된 커널 개발자라도 단일 개발 주기 동안 그렇게 많은 하위 시스템을 깊이 파고들기는 어려울 것이다. 적어도 자신이 무엇을 하는지 이해하고자 한다면 말이다. 이전에 알려지지 않았던 개발자가 이를 해내는 것은 기껏해야 놀랍다. 하지만 Vargas의 패치에는 `Assisted-by` 태그가 없으므로, 이 작업이 LLM 도움 없이 수행됐다고 믿을 수밖에 없다.

전체적으로 7.2의 변경 1,111개(전체의 7% 미만)가 `Assisted-by` 태그를 달았으며, 이는 7.1에서 보인 301개보다 크게 증가한 수치다. 그러나 7.2에서 LLM 지원을 받은 실제 패치 수는 틀림없이 그보다 훨씬 많을 것이다. 많은 개발자가 그런 태그를 제공하지 않고(종종, 항상 그렇지는 않지만, 규칙을 몰라서), 관리자는 LLM 사용을 거의 묻지 않으며, 최소 한 명의 관리자는 패치를 적용할 때 [그 태그를 적극적으로 제거한다](https://lwn.net/ml/all/20260701115302.29c66401@kernel.org/). LLM 지원으로 개발된 커밋을 정확히 추적하는 일은 불가능한 것으로 판명될 수 있지만, 때로는 커널 커뮤니티가 정말로 시도할 만큼 충분히 신경 쓰지 않는 듯하다.

LLM 사용이 커널 개발에서 그 존재감을 드러내는 다른 방식은 패치 검토 영역이다. 7.2에는 [Sashiko 검토 시스템](https://lwn.net/Articles/1064830/) [[KSDB](https://lwn.net/ksdb/releases/v7.2/taglist?tag=reported-by&dev=39782)]에 공로를 돌리는 `Reported-by` 태그가 있는 패치가 252개 있고, 568개 커밋이 변경 로그에서 Sashiko를 언급한다. 다른 LLM 역시 커널 버그를 찾는 데 분명히 사용되고 있으며, 실제 효과를 내고 있다.

7.2 릴리스에는 `Fixes` 태그가 있는 커밋 4,830개가 포함되어 있는데, 이는 이전 커밋이 도입한 버그를 수정한다는 표시다. 증가 폭이 얼마나 큰지 보려면, 이전에도 여기서 보았던 그래프(가장 최근에는 [6.17 개발 주기)](https://lwn.net/Articles/1038358/))의 업데이트판인 다음 그래프를 고려해 보자.

> ![[7.2의 Fixes 태그]](https://static.lwn.net/images/2026/fixes-7.2.svg)

굵은 초록색 선은 각 릴리스에서 `Fixes` 태그를 포함한 커밋 수를 나타내고, 굵은 갈색 선은 후속 커밋의 `Fixes` 태그로 식별된 커밋 수를 나타낸다. 교차 지점은 5.9이며, 이는 해당 릴리스 시점부터 커널 커뮤니티가 도입하는 버그보다 더 많은 버그를 수정하기 시작했음을 시사한다. 하지만 그 결론은 유지되지 않을 것이다. 5.9 이후 버그가 모두 식별되고 수정되기까지는 수년이 걸릴 것이며, 그 과정에서 그 선은 이동할 것이다.

하지만 그래프에서 주목할 부분은 오른쪽 끝이다. 꽤 많은 릴리스 동안 대략 같은 수준이었던 `Fixes` 태그 보유 커밋 수가 그곳에서 극적으로 증가한다. 많은 사람이 기존 소프트웨어의 버그를 찾는 과제에 LLM을 투입하기 시작하면 이것이 일어나는 듯하다. 이는 지켜볼 흥미로운 추세가 될 것이다. 버그 수가 무한할 수는 없다. 커널에서도 마찬가지다. 그러므로 버그 탐지와 수정 속도는 결국 감소해야 한다. 기존 버그는 수정되고, LLM 검토는 새로 도입되는 버그 수를 줄였을 것이다. 적어도 그것이 희망이다.

그 감소가 *일어나지 않는다면*, 답해야 할 흥미로운 질문이 생길 것이다. LLM의 확산으로 이전에는 그렇게 할 능력이 없었던 사람들이 커널 패치를 만들 수 있게 됐다는 점은 상당히 명확해 보인다. 그것이 사실이라면, 많은 경우 이 패치의 제출자가 그 패치가 무엇을 하는지 완전히 이해하지 못한다는 결론으로 넘어가는 것은 그리 무리가 아니다. 어쩌면 LLM이 이 이해가 더는 필요 없을 만큼 충분히 뛰어날 수도 있지만, 아무도 제대로 이해한 적이 없고 앞으로 수년간 유지보수해야 할 코드 더미를 만들고 있는 것일 수도 있다.

Linux 커널은 연구나 실험이 아니라 프로덕션 사용을 목표로 한다. 하지만 현재 커널의 개발 프로세스와 커뮤니티에는 거대한 실험이 진행 중이다. 이 커뮤니티는 35년 역사 동안 새로운 프로세스와 도구를 여러 번 흡수했고, 이번에도 거의 확실히 그렇게 할 방법을 찾아낼 것이다. 하지만 그 흡수가 그 과정에서 항상 난기류 없이 이루어진 것은 아니다.

한편 `linux-next`[^c07-linux-next] 저장소에는 7.3 릴리스로 풀되기를 기다리는 비병합 변경 집합이 거의 14,000개 있으며, 그중 1,100개 이상이 `Assisted-by` 태그를 포함한다. 최근 릴리스를 특징지은 높은 활동 수준은 조만간 끝나지 않을 듯하다. 다음 개발 주기와 그 뒤의 주기를 따라갈 때도 언제나 그렇듯 LWN을 주시하라.

[^c07-mainline]: 메인라인은 Linus Torvalds가 관리하는 Linux 커널의 공식 통합 개발 계통이다.
[^c07-perf]: `perf`는 성능 계수와 추적 기능을 이용해 Linux 시스템과 프로그램의 성능을 분석하는 사용자 공간 도구다.
[^c07-spi]: SPI(Serial Peripheral Interface)는 센서·플래시 등 주변 장치를 연결하는 동기식 직렬 버스다.
[^c07-amdgpu]: `amdgpu`는 AMD GPU용 Linux 커널 그래픽 드라이버다.
[^c07-devicetree]: devicetree는 하드웨어 구성을 데이터로 기술하여 커널이 장치를 발견·설정하도록 하는 형식이다.
[^c07-nvme]: NVMe는 PCIe 기반 비휘발성 저장장치용 고성능 호스트 컨트롤러 인터페이스 및 프로토콜이다.
[^c07-f2fs]: F2FS는 플래시 저장장치 특성에 맞춰 설계된 Linux 파일 시스템이다.
[^c07-apparmor]: AppArmor는 프로파일 기반으로 프로세스 권한을 제한하는 Linux 강제 접근 제어 시스템이다.
[^c07-landlock]: Landlock은 비특권 프로세스도 스스로에게 파일 시스템·네트워크 접근 제한을 부여할 수 있게 하는 Linux 보안 프레임워크다.
[^c07-selinux]: SELinux는 레이블과 정책을 사용해 접근을 제어하는 Linux 강제 접근 제어 시스템이다.
[^c07-linux-next]: `linux-next`는 다음 메인라인 병합 창을 앞두고 유지보수자 트리를 통합·검증하는 사전 통합 저장소다.

[댓글 (13개 게시됨)](https://lwn.net/Articles/1088776/#Comments)

**페이지 편집자**: Joe Brockmeier

# 짧은 항목

## 보안

### [Domas: AMD 메모리 컨트롤러로 메모리 보호 우회하기](https://lwn.net/Articles/1088778/)

#### 요약

- AMD 메모리 컨트롤러의 bank swizzle 모드가 임의 메모리 읽기·쓰기에 악용될 수 있음을 보인 개념 증명이 공개됐다.
- 커널 권한이 필요하므로 일반 소프트웨어에 즉각적인 위협은 아니지만, 펌웨어와 격리 보안 경계를 약화할 수 있다.
- 해당 동작은 AMD 문서에 기록돼 있으나, 그 영향은 설계상 의도치 않은 부작용으로 보인다.

Christopher Domas는 AMD 메모리 컨트롤러의 bank swizzle 모드를 이용해 메모리 보호를 우회하고 CPU 마이크로코드 정의와 [플랫폼 보안 프로세서](https://en.wikipedia.org/wiki/AMD_Platform_Security_Processor)의 메모리를 포함한 임의 데이터를 읽거나 쓰는 방법을 설명하는 개념 증명을 [공개했다](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts#skitter-creek-bath-salts). 무엇보다도 이는 커널 수준에서 실행되는 코드가 프로세서 명령어의 의미를 직접 조작하도록 하여, 메모리 암호화와 가상 머신 격리[^c07-vm-isolation] 같은 다른 보안 조치를 잠재적으로 우회하게 한다.

이는 엄밀히 말해 예상하지 못한 동작은 아니다. [AMD 매뉴얼](https://www.amd.com/content/dam/amd/en/documents/archived-tech-docs/programmer-references/32559.pdf)의 해당 PDF 113쪽에 문서화돼 있다. 하지만 임의 메모리에 접근해 컴퓨터 펌웨어의, 불변이라고 여겨지는 부분을 호스트 머신을 충돌시키지 않고 다시 쓸 수 있다는 사실은 설계의 의도치 않은 부작용처럼 보인다. 다행히 bank swizzle 모드를 활성화하려면 커널 수준 권한이 필요하므로, 이 취약점은 대부분의 소프트웨어에 즉각적인 문제는 아니다. 그래도 이 기법은 결국 악의적인 목적으로 사용될 가능성이 높아 보인다.

[^c07-vm-isolation]: 가상 머신 격리는 하이퍼바이저가 각 VM의 메모리와 실행을 다른 VM 및 호스트로부터 분리하는 보안 경계다.

[댓글 (9개 게시됨)](https://lwn.net/Articles/1088778/#Comments)

## 커널 개발

---

### [커널 릴리스 현황](https://lwn.net/Articles/1089538/)

#### 요약

- Linux 7.2 커널이 8월 16일에 릴리스되었다.
- 이번 릴리스에는 `bpf()` 공통 attribute, CPU scheduler의 cache-aware load balancing, Btrfs large folio 지원이 포함된다.
- swap, Landlock, `dm-inlinecrypt`를 비롯한 보안 및 storage 관련 기능도 개선되었다.
- 2,652명의 개발자가 16,418개의 non-merge changeset을 기여했으며, 이 중 613명은 첫 기여자였다.

**7.2 커널이 출시되었다**,
8월 16일에 [릴리스되었다](https://lwn.net/Articles/1089033/).
Linus는 다음과 같이 말했다:

> 음, 이번 릴리스의 마지막 주도 — 또다시 — 내가 바랐던 것보다 규모가 컸다.
> 하지만, 이른바 “new normal”이라는 상황을 고려하면, 그 이유로 릴리스를
> 미룬다면 아마 릴리스 자체가 전혀 없게
> 될 것이다.

이번 릴리스의 주요 기능으로는 `bpf()` system call의 [common
attributes 지원](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6318f11d53a3), CPU
scheduler를 위한 [cache-aware load balancing](https://lwn.net/Articles/1018334/),
Btrfs filesystem의 large-folio 지원, 추가적인 [swap subsystem 개선](https://lwn.net/Articles/1072657/),
Landlock security module 개선, 그리고 [dm-inlinecrypt](https://docs.kernel.org/next/admin-guide/device-mapper/dm-inlinecrypt.html)
device-mapper target을 통한 inline encryption hardware 탑재 block device 지원 등이 있으며,
그 외에도 많은 변경이 있다.[^c08-bpf] [^c08-scheduler] [^c08-folio] [^c08-landlock] [^c08-dm-inlinecrypt]
자세한 내용은 LWN의 merge window 요약
([1부](https://lwn.net/Articles/1078068/), [2부](https://lwn.net/Articles/1078539/)) 및 [KernelNewbies 7.2 페이지](https://kernelnewbies.org/Linux_7.2)를
참고하라.

이번 릴리스에는 2,652명의 개발자가 작성한 16,418개의 non-merge changeset이 포함되었으며,
그중 613명은 처음으로 커널에 기여한 사람들이다.
릴리스 이력은 다음과 같다:
> | RC | 날짜 | 커밋 | |
> | --- | --- | --- | --- |
> | **v7.2-rc1** | 2026-06-28 | 14395 | 14395 |
> | **v7.2-rc2** | 2026-07-05 | 433 | 433 |
> | **v7.2-rc3** | 2026-07-12 | 475 | 475 |
> | **v7.2-rc4** | 2026-07-19 | 557 | 557 |
> | **v7.2-rc5** | 2026-07-26 | 611 | 611 |
> | **v7.2-rc6** | 2026-08-02 | 615 | 615 |
> | **v7.2-rc7** | 2026-08-09 | 500 | 500 |
> | **(최종)** | 2026-08-16 | 247 | 247 |

더 많은 세부 사항은 [LWN KSDB v7.2 페이지](https://lwn.net/ksdb/releases/v7.2/)를 참고하라.

**안정 업데이트**: [7.1.9](https://lwn.net/Articles/1089545/),
[6.18.45](https://lwn.net/Articles/1089546/),
[6.12.104](https://lwn.net/Articles/1089547/),
[6.6.152](https://lwn.net/Articles/1089548/),
[6.1.183](https://lwn.net/Articles/1089549/), [5.15.216](https://lwn.net/Articles/1089550/), 그리고 [5.10.265](https://lwn.net/Articles/1089551/)가 8월 19일에 릴리스되었다.

[댓글(게시물 없음)](https://lwn.net/Articles/1089538/#Comments)

### [이번 주의 커널 인용문](https://lwn.net/Articles/1089535/)

#### 요약

- Greg Kroah-Hartman은 LLM이 오픈 소스 프로젝트에 주는 부담을 강하게 비판했다.
- 동시에 LLM 기반 도구가 실제 security bug를 찾아 고치는 데 쓸모가 있음을 인정했다.
- 그는 일부 Linux 영역에서는 사용을 금지했지만, fuzzer와 마찬가지로 제한적으로 활용할 수 있다고 본다.

> 나는 지금 LLM이 나와 대부분의 open source 프로젝트에 초래하는 고통을
> 천 개의 태양의 열정으로 싫어한다. 그러나 그것들이 막대한 비용을 들여,
> 실제 security bug를 찾아 고치면서도 3분의 1은 거짓말을 하는 fuzzy-tool을
> 만들었다는 사실은 무시할 수 없다. 이 도구에 실제 돈을 낼 사람은 아무도
> 없겠지만, Linux를 더 낫게 만들기 위해 그들의 자원을 가져다 쓸 수 있도록
> 이제 마지못해 이를 다루겠다.
>
> 지난 몇 달 동안 내가 최근 이 도구들을 사용해 rsync의 실제 bug를 찾아
> 고쳤듯이, 이 도구들은 우리 ecosystem이 작동하도록 만드는, 모두가 의존하는
> infrastructure를 개선하는 데 사용할 수 있다. 또한 오늘날 LLM이 야기하는
> 잔혹함의 일부를 피하는, 로컬에서 쓸 수 있는 “어느 정도 제정신인” 사용법도
> 있다고 말할 수 있다(물론 전부는 아니라는 데 동의한다).
>
> 내가 유지보수하는 Linux의 일부 영역에서는 이 도구들의 사용을 금지했다.
> 그곳에서는 사용할 이유가 없기 때문이다. 그러나 다시 말하지만, 이는
> fuzzer와 매우 비슷하게, 우리 software를 더 좋게 만들기 위해 활용할 수 있는
> 도구다.[^c08-fuzzer]

— [Greg
Kroah-Hartman](https://lists.sr.ht/~sircmpwn/sr.ht-discuss/%3CDKSTMKM0ZD9N.2FTBDFREZH699@ddevault.org%3E#%3C2026081920-sitting-rematch-09ba@gregkh%3E)

[댓글(4개 게시)](https://lwn.net/Articles/1089535/#Comments)

## 개발

### [Firefox 154.0 릴리스](https://lwn.net/Articles/1089386/)

#### 요약

- Firefox 154.0이 릴리스되었다.
- WebSocket 연결에도 local network access protection이 확장된다.
- 사이트별 cookie 및 data 삭제 설정이 더 유연해졌다.

Firefox browser의 [버전
154.0](https://www.firefox.com/en-US/firefox/154.0/releasenotes/)이 릴리스되었다. 변경 사항에는 WebSocket connection으로의
local network access protection 확장, 더 유연한 사이트별 cookie 및 data 삭제 설정 등이
포함된다.[^c08-websocket]

[댓글(6개 게시)](https://lwn.net/Articles/1089386/)

### [GNU poke 5.0 릴리스](https://lwn.net/Articles/1089211/)

#### 요약

- binary-data editor인 GNU Poke 5.0이 릴리스되었다.
- Poke compiler와 Poke language가 개선되었다.
- runtime 및 standard library도 업데이트되었다.

binary-data editor인 [GNU Poke](https://www.jemarch.net/poke)의
5.0 버전이 릴리스되었다. 이번 릴리스에는 Poke compiler 개선,
Poke language 추가 사항, runtime 및 standard library 업데이트가 다수 포함되었다.[^c08-runtime]
전체 변경 목록은 아래를 참고하라.

[전체 기사](https://lwn.net/Articles/1089211/) ([댓글: 없음](https://lwn.net/Articles/1089211/#Comments))

### [Go 1.27 릴리스](https://lwn.net/Articles/1089559/)

#### 요약

- Go programming language의 최신 버전인 Go 1.27이 릴리스되었다.
- 새 도구와 ML-DSA post-quantum algorithm 지원이 추가되었다.
- JSON 처리 package와 언어 기능도 업데이트되었다.

[Go 1.27](https://go.dev/doc/go1.27)은 [Go programming language](https://go.dev/)의 최신 버전으로,
새로운 도구, [ML-DSA](https://go.dev/doc/go1.27#crypto_mldsa) post-quantum algorithm 지원 추가,
새로운 JSON-processing package, language 업데이트 등을 포함하여 릴리스되었다.[^c08-ml-dsa]

[댓글(1개 게시)](https://lwn.net/Articles/1089559/)

### [Python packaging council 후보 발표](https://lwn.net/Articles/1088920/)

#### 요약

- PSF가 Python packaging council 선거 후보를 발표했다.
- 첫 선거에서 PPC의 다섯 자리를 모두 선출하며, 임기가 다른 두 cohort로 나뉜다.
- 투표 자격 회원은 8월 25일까지 투표 의사를 확인해야 하며, 투표는 9월 1일부터 15일까지다.

Python Software Foundation(PSF)은 [발표했다](https://pyfound.blogspot.com/2026/08/announcing-packaging-council-election.html):
[후보자들](https://www.python.org/nominations/elections/2026-python-packaging-council/nominees/)은 [4월에 Python steering council이
승인한](https://lwn.net/Articles/1068704/) Python packaging council 선거에 출마한다.

> 이번 첫 선거는 PPC의 다섯 자리를 모두 채운다. 가장 많은 표를 받은 두 후보는
> 2년 임기의 Cohort A로 지정되며, 그다음으로 많은 표를 받은 세 후보는
> 1년 임기의 Cohort B로 지정된다.
>
> 이후 선거에서는 각 cohort가 교대하는 해에 완전한 2년 임기로 선출되므로,
> 매 선거 주기마다 PPC의 약 절반이
> 교체된다.

공석 다섯 자리에 17명의 후보가 출마했다. PSF 투표 자격 회원은 이번 선거에서
8월 25일까지 [투표 의사를
확인](https://pyfound.blogspot.com/2026/07/affirm-PSF-voting-status-2026.html)해야 한다. 투표는
9월 1일에 시작하여 9월 15일에 종료된다.

[댓글(게시물 없음)](https://lwn.net/Articles/1088920/#Comments)

### [rsync 3.5.0 릴리스](https://lwn.net/Articles/1088759/)

#### 요약

- rsync 3.5.0이 릴리스되었으며 대규모 security fix가 포함되었다.
- path handling과 daemon protocol audit, fuzzing, 외부 연구자 보고가 취약점 발견에 기여했다.
- 모든 수정에는 수정 전 tree에서 실패하는 regression test가 함께 제공된다.

rsync의 [버전
3.5.0](https://download.samba.org/pub/rsync/NEWS#3.5.0)이 [매우 많은 security fix](https://download.samba.org/pub/rsync/NEWS#SECURITY_FIXES-3.5.0)를 포함하여 릴리스되었다:

> 이번 릴리스는 rsync의 path handling과 daemon protocol에 집중한 audit,
> 이를 보완한 daemon-protocol fuzzing 작업, 그리고 외부 연구자 보고에서 발견된
> 33개의 security issue —⁠— 그리고 여러 robustness hardening — 를 수정한다.
> VulnCheck(CNA)가 CVE ID를 할당했으며, 정확한 “introduced in” version range는
> 각 advisory와 함께 제공된다. 많은 범위가 “3.5.0 이전의 모든 버전”보다 훨씬
> 좁다. 모든 fix에는 수정되지 않은 tree에서 실패하는 regression test가 test suite에
> 포함되어 있다.[^c08-cve]
> [^c08-fuzzing]

[댓글(42개 게시)](https://lwn.net/Articles/1088759/)

### [Tuba 0.11 릴리스](https://lwn.net/Articles/1089537/)

#### 요약

- fediverse client인 Tuba 0.11이 릴리스되었다.
- Mastodon collection과 quote를 지원한다.
- attachment custom thumbnail, 새 emoji picker, Android build 등도 추가되었다.

[버전
0.11](https://codeberg.org/GeopJr/Tuba/releases/tag/v0.11.0)의 [Tuba](https://codeberg.org/GeopJr/Tuba#:~:text=Tuba-,Browse%20the%20Fediverse)
fediverse client가 릴리스되었다. 이번 릴리스의 주목할 만한 변경으로는
Mastodon [collection](https://docs.joinmastodon.org/client/collections/#overview) 및 [quote](https://docs.joinmastodon.org/user/quote-posts/#what) 지원,
attachment용 custom thumbnail 생성 기능, 새 emoji picker, Android용 build 및
기타 여러 개선 사항이 있다.[^c08-fediverse]

[댓글(게시물 없음)](https://lwn.net/Articles/1089537/)

## 기타

### [Mark J. Wielaard, Software Freedom Distinguished Service Award 수상](https://lwn.net/Articles/1089208/)

#### 요약

- Software Freedom Conservancy가 Mark J. Wielaard에게 두 번째 연례 Distinguished Service Award를 수여했다.
- 그는 Sourceware 유지보수와 FOSS 기여를 오랫동안 이어 왔다.
- DWARF Debugging Standard Committee, Valgrind, elfutils 및 여러 GNU project에서도 활동한다.

[Software Freedom
Conservancy](https://sfconservancy.org/)는 Mark J. Wielaard가 오랜 기간 software freedom에 기여한 공로로
두 번째 연례 Software Freedom Distinguished Service Award를 받았다고 [발표했다](https://sfconservancy.org/news/2026/aug/12/mark-j-wielaard-receives-2-annual-award/).

> Mark는 고용주가 그의 FOSS 작업 상당 부분을 지원하도록 자신의 경력을 설계해 온
> 많은 핵심 FOSS developer 중 한 명이다. 그럼에도 Mark는 역사상 가장 오래된
> FOSS collaboration 및 developer infrastructure hosting site인
> [Sourceware](https://sourceware.org/)를 유지보수하는 핵심 contributor로서,
> 근무 시간 이후에도 자원봉사 작업을
> 계속하고 있다.[^c08-foss]

Sourceware 작업 외에도 Wielaard는 [DWARF Debugging Standard Committee](https://dwarfstd.org/)의 구성원이며,
[Valgrind](https://valgrind.org/)와 [elfutils](https://elfutils.org/)의 maintainer이고,
그 밖의 다양한 GNU project에도 기여하고 있다.[^c08-dwarf]

[댓글(1개 게시)](https://lwn.net/Articles/1089208/#Comments)

**페이지 편집자**: Daroc Alden

# 공지

## 뉴스레터

### 배포판 및 system administration

[DistroWatch Weekly](https://distrowatch.com/weekly.php?issue=20260817)
8월 17일

[This week in F-Droid](https://f-droid.org/en/2026/08/14/twif.html)
8월 14일

[This week in Fedora](https://abompard.fedorapeople.org/twif/2026/08-10-to-08-16/)
8월 17일

[openSUSE Tumbleweed Review of the Week](https://dominique.leuenberger.net/blog/2026/08/tumbleweed-review-of-the-week-2026-33/)
8월 14일

[Ubuntu Weekly News](https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-issue-957/86061)
8월 10일

### 개발

[Emacs News](https://sachachua.com/blog/2026/08/2026-08-17-emacs-news/)
8월 17일

[What's cooking in git.git](https://lwn.net/Articles/1088564/)
8월 12일

[What's cooking in git.git](https://lwn.net/Articles/1088999/)
8월 14일

[What's cooking in git.git](https://lwn.net/Articles/1089068/)
8월 17일

[What's cooking in git.git](https://lwn.net/Articles/1089374/)
8월 18일

[This Week in GNOME](https://thisweek.gnome.org/posts/2026/08/twig-262/)
8월 14일

[GNU Tools Weekly News](https://lwn.net/Articles/1089362/)
8월 16일

[Golang Weekly](https://golangweekly.com/issues/614)
8월 14일

[Last Week in Kubernetes Development](https://lwkd.info/2026/20260813)
8월 13일

[LLVM Weekly](https://llvmweekly.org/issue/659)
8월 17일

[This Week in Matrix](https://matrix.org/blog/2026/08/14/this-week-in-matrix-2026-08-14/)
8월 14일

[OCaml Weekly News](https://lwn.net/Articles/1089407/)
8월 18일

[OpenPrinting News](https://openprinting.github.io/OpenPrinting-News-Opportunity-Open-Source-4.0-Schedules-and-contributions-published)
8월 11일

[Perl Weekly](http://perlweekly.com/archive/786.html)
8월 17일

[This Week in Plasma](https://blogs.kde.org/2026/08/15/this-week-in-plasma-bi-directional-rdp-clipboard-sync/)
8월 15일

[PyCoder's Weekly](https://pycoders.com/issues/748)
8월 18일

[This month in Radicle CI](https://blog.liw.fi/posts/2026/radicle-status-quo-08/)
8월 19일

[Weekly Rakudo News](https://rakudoweekly.blog/2026/08/18/2026-33-all-the-way-to-infinity/)
8월 18일

[Ruby Weekly News](https://rubyweekly.com/issues/813)
8월 18일

[This Week in Rust](https://this-week-in-rust.org/blog/2026/08/12/this-week-in-rust-664/)
8월 12일

[Wikimedia Tech News](https://meta.wikimedia.org/wiki/Special:FeedItem/technews/20260817000000/en)
8월 17일

### 회의록

[Fedora FESCo 회의록](https://lwn.net/Articles/1089528/)
8월 18일

## 발표 제안 요청

### CFP 마감일: 2026년 8월 20일~2026년 10월 19일

다음 CFP 마감일 목록은 [LWN.net CFP Calendar](https://lwn.net/Calendar/Monthly/cfp/)에서 가져왔다.[^c08-cfp]

| 마감일 | 행사 날짜 | 행사 | 장소 |
| --- | --- | --- | --- |
| 8월 31일 | 10월 2일 10월 4일 | [GNU Tools Cauldron](https://conf.gnu-tools-cauldron.org/prg26/) | 체코 프라하 |
| 8월 31일 | 10월 3일 10월 4일 | [Linux Days 2026](https://pretalx.linuxdays.cz/linuxdays-2026/cfp) | 체코 프라하 |
| 9월 6일 | 10월 6일 | [Real-time Linux User Forum](https://forms.gle/iRK48ACWnMatihg59) | 체코 프라하 |
| 9월 6일 | 1월 20일 1월 22일 | [Everything Open](https://2027.everythingopen.au/programme/proposals/) | 오스트레일리아 브리즈번 |
| 9월 18일 | 9월 19일 | [Software Freedom Day NJ](https://digitalfreedoms.org/en/sfd) | 미국 뉴저지주 몽클레어 |
| 10월 1일 | 11월 7일 11월 8일 | [OpenFest 2026](https://cfp.openfest.org) | 불가리아 소피아 |

행사의 CFP 마감일이 여기에 없다면,
[알려 달라](https://lwn.net/Calendar/new/).

## 예정 행사

### 행사: 2026년 8월 20일~2026년 10월 19일

다음 행사 목록은 [LWN.net Calendar](https://lwn.net/Calendar/)에서 가져왔다.

| 날짜 | 행사 | 장소 |
| --- | --- | --- |
| 8월 25일 8월 30일 | [MiniDebConf and MiniDebCamp Winterthur 2026](https://ch2026.mini.debconf.org/) | 스위스 빈터투어 |
| 8월 30일 9월 5일 | [FOSS4G Hiroshima 2026](https://2026.foss4g.org/en/) | 일본 히로시마 |
| 9월 17일 9월 18일 | [Git Merge](https://git-merge.com/) | 포르투갈 리스본 |
| 9월 19일 9월 24일 | [Akademy 2026](https://akademy.kde.org/2026/) | 오스트리아 그라츠 |
| 9월 19일 | [Software Freedom Day NJ](https://njsfd.org/) | 미국 뉴저지주 몽클레어 |
| 9월 19일 9월 20일 | [Nextcloud Community Conference 2026](https://nextcloud.com/conference-2026) | 독일 베를린 |
| 9월 22일 9월 24일 | [Kernel Recipes](https://kernel-recipes.org/en/2025/) | 프랑스 파리 |
| 9월 22일 9월 24일 | [Reproducible Builds Summit](https://reproducible-builds.org/events/gothenburg2026/) | 스웨덴 예테보리 |
| 9월 25일 9월 27일 | [PostmarketOS and Alpine Linux Conference](https://postmarketos.org/conference/) | 독일 아헨 |
| 9월 28일 9월 30일 | [X.Org Developers Conference](https://indico.freedesktop.org/event/12/) | 캐나다 토론토 |
| 9월 28일 10월 1일 | [Alpine Linux Persistence and Storage Summit](https://www.alpss.at/) | 오스트리아 티롤주 리주머휘테 |
| 9월 30일 10월 1일 | [All Systems Go! 2026](https://all-systems-go.io/) | 독일 베를린 |
| 10월 1일 | [Open Tech Day | Software-defined Storage](https://opentechday.de/) | 독일 뉘른베르크 |
| 10월 1일 10월 2일 | [embedded Linux for Safe and Secure Applications](https://www.elsa-symposium.com/home) | 독일 괴팅겐 |
| 10월 2일 10월 4일 | [GNU Tools Cauldron](https://gnu-tools-cauldron.org/) | 체코 프라하 |
| 10월 3일 10월 4일 | [openSUSE.Asia Summit 2026](https://events.opensuse.org/conferences/oSAS26) | 인도네시아 욕야카르타 |
| 10월 3일 10월 4일 | [Linux Days 2026](https://www.linuxdays.cz/2026/) | 체코 프라하 |
| 10월 5일 10월 7일 | [Linux Plumbers Conference 2026](https://lpc.events/event/20/) | 체코 프라하 |
| 10월 6일 | [Real-time Linux User Forum](https://realtime-linux.org/event/real-time-linux-user-forum/) | 체코 프라하 |
| 10월 6일 | [Yocto Project Developer Day 2026](https://www.yoctoproject.org/event/ypdd-26/) | 체코 프라하 |
| 10월 7일 10월 9일 | [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) | 체코 프라하 |
| 10월 7일 10월 9일 | [Embedded Linux Conference Europe](https://events.linuxfoundation.org/embedded-linux-conference-europe) | 체코 프라하 |
| 10월 8일 | [Linux Security Summit Europe](https://events.linuxfoundation.org/linux-security-summit-europe/program/schedule-at-a-glance/) | 체코 프라하 |
| 10월 14일 10월 17일 | [PyCon South Africa](https://za.pycon.org/) | 남아프리카공화국 케이프타운 |
| 10월 18일 10월 20일 | [All Things Open](https://2026.allthingsopen.org/) | 미국 노스캐롤라이나주 롤리 |

행사가 여기에 없다면,
[알려 달라](https://lwn.net/Calendar/new/).

## 보안 업데이트

[^c08-bpf]: `bpf()` system call은 eBPF program과 map을 kernel에 생성·관리·연결하는 Linux interface다.
[^c08-scheduler]: CPU scheduler는 실행 가능한 task를 CPU에 배치하며, cache-aware balancing은 cache locality를 고려해 migration 비용을 줄인다.
[^c08-folio]: folio는 filesystem과 memory management가 page 묶음을 더 효율적으로 다루도록 하는 kernel memory abstraction이다.
[^c08-landlock]: Landlock은 unprivileged process가 자신 또는 자식 process에 filesystem·network 접근 제한을 적용할 수 있게 하는 Linux security module이다.
[^c08-dm-inlinecrypt]: `dm-inlinecrypt`는 storage device의 inline encryption hardware를 device-mapper 계층에 노출하는 target이다.
[^c08-fuzzer]: fuzzer는 무작위 또는 변형된 입력을 자동 생성하여 crash 및 취약점을 찾아내는 테스트 도구다.
[^c08-websocket]: WebSocket은 HTTP handshake 뒤 장기적인 양방향 통신을 제공하는 웹 protocol이다.
[^c08-runtime]: runtime은 program 실행 중 memory, scheduling, I/O 같은 실행 환경 서비스를 제공하는 구성 요소다.
[^c08-ml-dsa]: ML-DSA는 lattice 기반 digital signature를 위한 NIST 표준 post-quantum cryptography algorithm이다.
[^c08-cve]: CVE는 공개적으로 추적되는 cybersecurity vulnerability identifier 체계다.
[^c08-fuzzing]: fuzzing은 비정상적·예상 밖 입력을 대량 제공해 software 결함과 security vulnerability를 찾는 기법이다.
[^c08-fediverse]: fediverse는 ActivityPub 등 연합 protocol로 서로 연결되는 독립 social network server들의 생태계다.
[^c08-foss]: FOSS는 Free and Open Source Software의 약자로, 사용·연구·수정·재배포의 자유를 중시한다.
[^c08-dwarf]: DWARF는 compiler와 debugger가 source-level debugging 정보를 교환하는 표준 format이다.
[^c08-cfp]: CFP(Call for Presentations)는 conference 발표 제안을 모집하는 절차다.

---

### [2026년 8월 13일부터 2026년 8월 19일까지의 보안 경보 요약](https://lwn.net/Articles/1089504/)

#### 요약

- 이 기간에 여러 Linux 배포판이 공개한 보안 권고[^c09-security-advisory]와 관련 패키지 업데이트를 모아 놓았다.
- 권고 대상에는 `kernel`[^c09-kernel], `bind`, `curl`, `OpenSSH`, `nginx`, `rsync` 등 핵심 시스템·네트워크 소프트웨어가 포함된다.
- 배포판, 릴리스, 패키지 및 공개 날짜별로 권고 ID와 원문 링크를 제공한다.

| 배포판 | ID | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:55858](https://lwn.net/Articles/1089419/) | 10 | .NET 10.0 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54542](https://lwn.net/Articles/1088833/) | 8 | .NET 10.0 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:55857](https://lwn.net/Articles/1089420/) | 9 | .NET 10.0 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54541](https://lwn.net/Articles/1089069/) | 10 | .NET 8.0 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54538](https://lwn.net/Articles/1088834/) | 8 | .NET 8.0 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54574](https://lwn.net/Articles/1089298/) | 9 | .NET 8.0 | 2026-08-17 |
| AlmaLinux | [ALSA-2026:54590](https://lwn.net/Articles/1089070/) | 10 | .NET 9.0 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54550](https://lwn.net/Articles/1088835/) | 8 | .NET 9.0 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:55856](https://lwn.net/Articles/1089421/) | 9 | .NET 9.0 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55424](https://lwn.net/Articles/1089422/) | 10 | 389-ds-base | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55423](https://lwn.net/Articles/1089423/) | 9 | 389-ds-base | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55530](https://lwn.net/Articles/1089299/) | 8 | 389-ds:1.4 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54272](https://lwn.net/Articles/1088595/) | 8 | abrt | 2026-08-12 |
| AlmaLinux | [ALSA-2026:56133](https://lwn.net/Articles/1089424/) | 8 | attr | 2026-08-19 |
| AlmaLinux | [ALSA-2026:55437](https://lwn.net/Articles/1089300/) | 10 | bind | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54654](https://lwn.net/Articles/1088836/) | 8 | bind | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54510](https://lwn.net/Articles/1089071/) | 9 | bind | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54509](https://lwn.net/Articles/1088837/) | 8 | bind9.16 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:55432](https://lwn.net/Articles/1089425/) | 10 | curl | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55439](https://lwn.net/Articles/1089426/) | 9 | curl | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54210](https://lwn.net/Articles/1088596/) | 10 | dhcpcd | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54576](https://lwn.net/Articles/1089072/) | 10 | dracut | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54575](https://lwn.net/Articles/1088838/) | 8 | dracut | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54571](https://lwn.net/Articles/1089073/) | 9 | dracut | 2026-08-14 |
| AlmaLinux | [ALSA-2026:39297](https://lwn.net/Articles/1088597/) | 10 | edk2 | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54486](https://lwn.net/Articles/1089074/) | 10 | freerdp | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54485](https://lwn.net/Articles/1088712/) | 8 | freerdp | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54487](https://lwn.net/Articles/1089075/) | 9 | freerdp | 2026-08-14 |
| AlmaLinux | [ALSA-2026:38497](https://lwn.net/Articles/1088598/) | 9 | gegl04 | 2026-08-12 |
| AlmaLinux | [ALSA-2026:55440](https://lwn.net/Articles/1089427/) | 9 | glib2 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54512](https://lwn.net/Articles/1089076/) | 10 | gnome-remote-desktop | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54178](https://lwn.net/Articles/1088599/) | 10 | grafana | 2026-08-13 |
| AlmaLinux | [ALSA-2026:55865](https://lwn.net/Articles/1089429/) | 9 | gstreamer1-plugins-bad-free and gstreamer1-plugins-ugly-free | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55433](https://lwn.net/Articles/1089428/) | 10 | gstreamer1-plugins-bad-free | 2026-08-18 |
| AlmaLinux | [ALSA-2026:53451](https://lwn.net/Articles/1088600/) | 10 | gstreamer1-plugins-good | 2026-08-13 |
| AlmaLinux | [ALSA-2026:55434](https://lwn.net/Articles/1089430/) | 10 | gstreamer1-plugins-good | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55436](https://lwn.net/Articles/1089431/) | 9 | gstreamer1-plugins-good | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55435](https://lwn.net/Articles/1089432/) | 10 | gstreamer1-plugins-ugly-free | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55679](https://lwn.net/Articles/1089302/) | 10 | haproxy | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55859](https://lwn.net/Articles/1089301/) | 8 | haproxy | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55772](https://lwn.net/Articles/1089433/) | 9 | haproxy | 2026-08-18 |
| AlmaLinux | [ALSA-2026:53845](https://lwn.net/Articles/1088601/) | 10 | iscsi-initiator-utils | 2026-08-12 |
| AlmaLinux | [ALSA-2026:53846](https://lwn.net/Articles/1088602/) | 10 | isns-utils | 2026-08-12 |
| AlmaLinux | [ALSA-2026:53330](https://lwn.net/Articles/1088604/) | 10 | kernel | 2026-08-13 |
| AlmaLinux | [ALSA-2026:51295](https://lwn.net/Articles/1088606/) | 10 | kernel | 2026-08-12 |
| AlmaLinux | [ALSA-2026:54343](https://lwn.net/Articles/1089077/) | 10 | kernel | 2026-08-14 |
| AlmaLinux | [ALSA-2026:54246](https://lwn.net/Articles/1088605/) | 8 | kernel | 2026-08-12 |
| AlmaLinux | [ALSA-2026:55764](https://lwn.net/Articles/1089303/) | 8 | kernel | 2026-08-18 |
| AlmaLinux | [ALSA-2026:53329](https://lwn.net/Articles/1088603/) | 9 | kernel | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54443](https://lwn.net/Articles/1089434/) | 9 | kernel | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54247](https://lwn.net/Articles/1088713/) | 8 | kernel-rt | 2026-08-13 |
| AlmaLinux | [ALSA-2026:55765](https://lwn.net/Articles/1089304/) | 8 | kernel-rt | 2026-08-18 |
| AlmaLinux | [ALSA-2026:28582](https://lwn.net/Articles/1088607/) | 10 | keylime | 2026-08-13 |
| AlmaLinux | [ALSA-2026:55448](https://lwn.net/Articles/1089306/) | 10 | libXfont2 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55446](https://lwn.net/Articles/1089305/) | 8 | libXfont2 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55447](https://lwn.net/Articles/1089436/) | 9 | libXfont2 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:52675](https://lwn.net/Articles/1088608/) | 10 | libarchive | 2026-08-12 |
| AlmaLinux | [ALSA-2026:55855](https://lwn.net/Articles/1089435/) | 10 | libssh | 2026-08-18 |
| AlmaLinux | [ALSA-2026:25051](https://lwn.net/Articles/1088609/) | 9 | libyang | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54650](https://lwn.net/Articles/1089078/) | 10 | nghttp2 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:55804](https://lwn.net/Articles/1089307/) | 8 | nghttp2 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:54662](https://lwn.net/Articles/1089079/) | 9 | nghttp2 | 2026-08-14 |
| AlmaLinux | [ALSA-2026:52841](https://lwn.net/Articles/1088610/) | 10 | nodejs-nodemon | 2026-08-12 |
| AlmaLinux | [ALSA-2026:55541](https://lwn.net/Articles/1089437/) | 10 | nodejs22 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:28231](https://lwn.net/Articles/1088611/) | 10 | opencryptoki | 2026-08-13 |
| AlmaLinux | [ALSA-2026:49526](https://lwn.net/Articles/1088612/) | 10 | osbuild-composer | 2026-08-13 |
| AlmaLinux | [ALSA-2026:49838](https://lwn.net/Articles/1088613/) | 9 | osbuild-composer | 2026-08-12 |
| AlmaLinux | [ALSA-2026:40833](https://lwn.net/Articles/1088614/) | 10 | pacemaker | 2026-08-13 |
| AlmaLinux | [ALSA-2026:56131](https://lwn.net/Articles/1089438/) | 8 | pam | 2026-08-19 |
| AlmaLinux | [ALSA-2026:48170](https://lwn.net/Articles/1089439/) | 10 | php | 2026-08-18 |
| AlmaLinux | [ALSA-2026:49914](https://lwn.net/Articles/1089440/) | 10 | php8.4 | 2026-08-18 |
| AlmaLinux | [ALSA-2026:24348](https://lwn.net/Articles/1088615/) | 10 | postgresql-jdbc | 2026-08-12 |
| AlmaLinux | [ALSA-2026:27742](https://lwn.net/Articles/1088616/) | 10 | postgresql18 | 2026-08-12 |
| AlmaLinux | [ALSA-2026:54481](https://lwn.net/Articles/1088618/) | 10 | python-idna | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54290](https://lwn.net/Articles/1088619/) | 8 | python-idna | 2026-08-12 |
| AlmaLinux | [ALSA-2026:54484](https://lwn.net/Articles/1088617/) | 9 | python-idna | 2026-08-13 |
| AlmaLinux | [ALSA-2026:54268](https://lwn.net/Articles/1088620/) | 9 | python3.9 | 2026-08-13 |
| AlmaLinux | [ALSA-2026:56130](https://lwn.net/Articles/1089441/) | 8 | sg3\_utils | 2026-08-19 |
| AlmaLinux | [ALSA-2026:53435](https://lwn.net/Articles/1088621/) | 10 | udisks2 | 2026-08-13 |
| AlmaLinux | [ALSA-2026:55892](https://lwn.net/Articles/1089309/) | 10 | unbound | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55784](https://lwn.net/Articles/1089308/) | 8 | unbound | 2026-08-18 |
| AlmaLinux | [ALSA-2026:55841](https://lwn.net/Articles/1089442/) | 9 | unbound | 2026-08-18 |
| AlmaLinux | [ALSA-2026:25216](https://lwn.net/Articles/1088622/) | 10 | valkey | 2026-08-13 |
| AlmaLinux | [ALSA-2026:38509](https://lwn.net/Articles/1088624/) | 10 | vim | 2026-08-13 |
| AlmaLinux | [ALSA-2026:38510](https://lwn.net/Articles/1088714/) | 8 | vim | 2026-08-13 |
| AlmaLinux | [ALSA-2026:38511](https://lwn.net/Articles/1088623/) | 9 | vim | 2026-08-13 |
| AlmaLinux | [ALSA-2026:38489](https://lwn.net/Articles/1088625/) | 10 | xorg-x11-server-Xwayland | 2026-08-13 |
| AlmaLinux | [ALSA-2026:26566](https://lwn.net/Articles/1088626/) | 10 | xorg-x11-server-Xwayland | 2026-08-13 |
| AlmaLinux | [ALSA-2026:38490](https://lwn.net/Articles/1088627/) | 9 | xorg-x11-server-Xwayland | 2026-08-12 |
| AlmaLinux | [ALSA-2026:25999](https://lwn.net/Articles/1088628/) | 10 | yggdrasil-worker-package-manager | 2026-08-13 |
| Debian | [DLA-4742-1](https://lwn.net/Articles/1089080/) | LTS | apr-util | 2026-08-16 |
| Debian | [DSA-6437-1](https://lwn.net/Articles/1088839/) | stable | apr-util | 2026-08-13 |
| Debian | [DLA-4744-1](https://lwn.net/Articles/1089310/) | LTS | calibre | 2026-08-18 |
| Debian | [DLA-4739-1](https://lwn.net/Articles/1088841/) | LTS | chromium | 2026-08-13 |
| Debian | [DSA-6436-1](https://lwn.net/Articles/1088840/) | stable | chromium | 2026-08-13 |
| Debian | [DSA-6443-1](https://lwn.net/Articles/1089081/) | stable | docker.io | 2026-08-16 |
| Debian | [DSA-6446-1](https://lwn.net/Articles/1089311/) | stable | expat | 2026-08-18 |
| Debian | [DSA-6432-1](https://lwn.net/Articles/1088629/) | stable | flatpak | 2026-08-12 |
| Debian | [DLA-4743-1](https://lwn.net/Articles/1089082/) | LTS | ironic | 2026-08-16 |
| Debian | [DSA-6445-1](https://lwn.net/Articles/1089312/) | stable | ironic | 2026-08-17 |
| Debian | [DSA-6434-1](https://lwn.net/Articles/1088630/) | stable | lemonldap-ng | 2026-08-12 |
| Debian | [DSA-6447-1](https://lwn.net/Articles/1089443/) | stable | librabbitmq | 2026-08-18 |
| Debian | [DLA-4745-1](https://lwn.net/Articles/1089313/) | LTS | linux-6.12 | 2026-08-18 |
| Debian | [DLA-4735-1](https://lwn.net/Articles/1088631/) | LTS | neutron | 2026-08-12 |
| Debian | [DSA-6444-1](https://lwn.net/Articles/1089083/) | stable | neutron | 2026-08-16 |
| Debian | [DLA-4740-1](https://lwn.net/Articles/1089084/) | LTS | postgresql-15 | 2026-08-14 |
| Debian | [DSA-6438-1](https://lwn.net/Articles/1088842/) | stable | postgresql-17 | 2026-08-13 |
| Debian | [DLA-4736-1](https://lwn.net/Articles/1088632/) | LTS | python-django | 2026-08-12 |
| Debian | [DSA-6441-1](https://lwn.net/Articles/1088843/) | stable | python-httplib2 | 2026-08-14 |
| Debian | [DLA-4706-2](https://lwn.net/Articles/1089444/) | LTS | ruby-grape | 2026-08-19 |
| Debian | [DSA-6435-1](https://lwn.net/Articles/1088633/) | stable | spip | 2026-08-12 |
| Debian | [DSA-6448-1](https://lwn.net/Articles/1089445/) | stable | spip | 2026-08-18 |
| Debian | [DSA-6450-1](https://lwn.net/Articles/1089446/) | stable | srt | 2026-08-18 |
| Debian | [DSA-6449-1](https://lwn.net/Articles/1089447/) | stable | swift | 2026-08-18 |
| Debian | [DLA-4741-1](https://lwn.net/Articles/1089085/) | LTS | unzip | 2026-08-16 |
| Debian | [DSA-6440-1](https://lwn.net/Articles/1088844/) | stable | unzip | 2026-08-14 |
| Debian | [DSA-6442-1](https://lwn.net/Articles/1089086/) | stable | util-linux | 2026-08-14 |
| Debian | [DSA-6433-1](https://lwn.net/Articles/1088634/) | stable | xdg-dbus-proxy | 2026-08-13 |
| Debian | [DLA-4737-1](https://lwn.net/Articles/1088635/) | LTS | xorg-server | 2026-08-13 |
| Debian | [DLA-4738-1](https://lwn.net/Articles/1088636/) | LTS | xorg-server | 2026-08-13 |
| Debian | [DSA-6439-1](https://lwn.net/Articles/1088845/) | stable | zip | 2026-08-14 |
| Fedora | [FEDORA-2026-166bfc4f18](https://lwn.net/Articles/1089448/) | F44 | GitPython | 2026-08-19 |
| Fedora | [FEDORA-2026-edfb6293ee](https://lwn.net/Articles/1088637/) | F44 | apr-util | 2026-08-13 |
| Fedora | [FEDORA-2026-51e9d3c767](https://lwn.net/Articles/1089088/) | F43 | chromium | 2026-08-15 |
| Fedora | [FEDORA-2026-c374680c6a](https://lwn.net/Articles/1089087/) | F44 | chromium | 2026-08-15 |
| Fedora | [FEDORA-2026-13e2cf6827](https://lwn.net/Articles/1089314/) | F43 | coturn | 2026-08-18 |
| Fedora | [FEDORA-2026-50c75def83](https://lwn.net/Articles/1089315/) | F44 | coturn | 2026-08-18 |
| Fedora | [FEDORA-2026-7e85920dc5](https://lwn.net/Articles/1088639/) | F43 | cri-o1.34 | 2026-08-13 |
| Fedora | [FEDORA-2026-8ce4ffda9c](https://lwn.net/Articles/1088638/) | F44 | cri-o1.34 | 2026-08-13 |
| Fedora | [FEDORA-2026-ce97d80dae](https://lwn.net/Articles/1088847/) | F43 | erlang-cowboy | 2026-08-14 |
| Fedora | [FEDORA-2026-7d233ad8b0](https://lwn.net/Articles/1088846/) | F44 | erlang-cowboy | 2026-08-14 |
| Fedora | [FEDORA-2026-ce97d80dae](https://lwn.net/Articles/1088849/) | F43 | erlang-cowlib | 2026-08-14 |
| Fedora | [FEDORA-2026-7d233ad8b0](https://lwn.net/Articles/1088848/) | F44 | erlang-cowlib | 2026-08-14 |
| Fedora | [FEDORA-2026-6b83471b0e](https://lwn.net/Articles/1088850/) | F44 | flatpak | 2026-08-14 |
| Fedora | [FEDORA-2026-9f70b173c8](https://lwn.net/Articles/1089089/) | F44 | jfrog-cli | 2026-08-17 |
| Fedora | [FEDORA-2026-d51fe2075c](https://lwn.net/Articles/1089090/) | F43 | jrnl | 2026-08-16 |
| Fedora | [FEDORA-2026-1f4ad7617f](https://lwn.net/Articles/1089091/) | F44 | jrnl | 2026-08-16 |
| Fedora | [FEDORA-2026-d8ffb92441](https://lwn.net/Articles/1089450/) | F43 | lemonldap-ng | 2026-08-19 |
| Fedora | [FEDORA-2026-55e1334aed](https://lwn.net/Articles/1089449/) | F44 | lemonldap-ng | 2026-08-19 |
| Fedora | [FEDORA-2026-f77201a75e](https://lwn.net/Articles/1088640/) | F44 | libcupsfilters | 2026-08-13 |
| Fedora | [FEDORA-2026-86684eb696](https://lwn.net/Articles/1089451/) | F44 | libgit2 | 2026-08-19 |
| Fedora | [FEDORA-2026-110274a705](https://lwn.net/Articles/1089092/) | F43 | libgsasl | 2026-08-16 |
| Fedora | [FEDORA-2026-f2ced62115](https://lwn.net/Articles/1089093/) | F44 | libgsasl | 2026-08-16 |
| Fedora | [FEDORA-2026-2e196b6fa5](https://lwn.net/Articles/1089452/) | F43 | libnfs | 2026-08-19 |
| Fedora | [FEDORA-2026-8ae1795f2b](https://lwn.net/Articles/1088851/) | F44 | libnfs | 2026-08-14 |
| Fedora | [FEDORA-2026-c8cfd2f2f9](https://lwn.net/Articles/1089094/) | F44 | libsoup3 | 2026-08-15 |
| Fedora | [FEDORA-2026-e82e06fcae](https://lwn.net/Articles/1089316/) | F43 | linux-firmware | 2026-08-18 |
| Fedora | [FEDORA-2026-c53019ed4f](https://lwn.net/Articles/1088641/) | F44 | linux-firmware | 2026-08-13 |
| Fedora | [FEDORA-2026-8aaf6f724b](https://lwn.net/Articles/1089096/) | F43 | pdns | 2026-08-15 |
| Fedora | [FEDORA-2026-706965c440](https://lwn.net/Articles/1089095/) | F44 | pdns | 2026-08-15 |
| Fedora | [FEDORA-2026-ac51ed6e75](https://lwn.net/Articles/1089098/) | F43 | pdns-recursor | 2026-08-17 |
| Fedora | [FEDORA-2026-707054d631](https://lwn.net/Articles/1089097/) | F44 | pdns-recursor | 2026-08-17 |
| Fedora | [FEDORA-2026-030f3f2029](https://lwn.net/Articles/1089099/) | F43 | perl-Archive-Tar | 2026-08-15 |
| Fedora | [FEDORA-2026-4fb0f012fb](https://lwn.net/Articles/1089454/) | F43 | perl-Imager | 2026-08-19 |
| Fedora | [FEDORA-2026-8a61adae6f](https://lwn.net/Articles/1089453/) | F44 | perl-Imager | 2026-08-19 |
| Fedora | [FEDORA-2026-6217093b91](https://lwn.net/Articles/1089455/) | F43 | perl-List-SomeUtils-XS | 2026-08-19 |
| Fedora | [FEDORA-2026-fdc77dd5f5](https://lwn.net/Articles/1089101/) | F43 | php-pear-PHP-CodeSniffer | 2026-08-15 |
| Fedora | [FEDORA-2026-d536e7004b](https://lwn.net/Articles/1089100/) | F44 | php-pear-PHP-CodeSniffer | 2026-08-15 |
| Fedora | [FEDORA-2026-b2ce3f8e3e](https://lwn.net/Articles/1089317/) | F43 | php-phpseclib | 2026-08-18 |
| Fedora | [FEDORA-2026-fac5581caa](https://lwn.net/Articles/1089318/) | F44 | php-phpseclib | 2026-08-18 |
| Fedora | [FEDORA-2026-a9f0296a41](https://lwn.net/Articles/1089456/) | F44 | python3.12 | 2026-08-19 |
| Fedora | [FEDORA-2026-7f32bbb5b0](https://lwn.net/Articles/1089458/) | F43 | python3.14 | 2026-08-19 |
| Fedora | [FEDORA-2026-2c124fcf93](https://lwn.net/Articles/1089457/) | F44 | python3.14 | 2026-08-19 |
| Fedora | [FEDORA-2026-057cd843d0](https://lwn.net/Articles/1089460/) | F43 | radsecproxy | 2026-08-19 |
| Fedora | [FEDORA-2026-099bb42b08](https://lwn.net/Articles/1089459/) | F44 | radsecproxy | 2026-08-19 |
| Fedora | [FEDORA-2026-7ebec18d52](https://lwn.net/Articles/1089102/) | F43 | rust-bat | 2026-08-17 |
| Fedora | [FEDORA-2026-74c4a6f82e](https://lwn.net/Articles/1089103/) | F44 | rust-bat | 2026-08-16 |
| Fedora | [FEDORA-2026-7ebec18d52](https://lwn.net/Articles/1089104/) | F43 | rust-git-delta | 2026-08-17 |
| Fedora | [FEDORA-2026-74c4a6f82e](https://lwn.net/Articles/1089105/) | F44 | rust-git-delta | 2026-08-16 |
| Fedora | [FEDORA-2026-7ebec18d52](https://lwn.net/Articles/1089106/) | F43 | rust-git-interactive-rebase-tool | 2026-08-17 |
| Fedora | [FEDORA-2026-74c4a6f82e](https://lwn.net/Articles/1089107/) | F44 | rust-git-interactive-rebase-tool | 2026-08-16 |
| Fedora | [FEDORA-2026-7ebec18d52](https://lwn.net/Articles/1089108/) | F43 | rust-lsd | 2026-08-17 |
| Fedora | [FEDORA-2026-74c4a6f82e](https://lwn.net/Articles/1089109/) | F44 | rust-lsd | 2026-08-16 |
| Fedora | [FEDORA-2026-7ebec18d52](https://lwn.net/Articles/1089110/) | F43 | rust-pretty-git-prompt | 2026-08-17 |
| Fedora | [FEDORA-2026-74c4a6f82e](https://lwn.net/Articles/1089111/) | F44 | rust-pretty-git-prompt | 2026-08-16 |
| Fedora | [FEDORA-2026-7ebec18d52](https://lwn.net/Articles/1089112/) | F43 | rust-tokei | 2026-08-17 |
| Fedora | [FEDORA-2026-74c4a6f82e](https://lwn.net/Articles/1089113/) | F44 | rust-tokei | 2026-08-16 |
| Fedora | [FEDORA-2026-344515cf47](https://lwn.net/Articles/1089319/) | F43 | sqlite | 2026-08-18 |
| Fedora | [FEDORA-2026-4bc86fb6d0](https://lwn.net/Articles/1088642/) | F44 | sqlite | 2026-08-13 |
| Fedora | [FEDORA-2026-de8630b736](https://lwn.net/Articles/1089114/) | F43 | stunnel | 2026-08-16 |
| Fedora | [FEDORA-2026-67c2201ad8](https://lwn.net/Articles/1089115/) | F44 | stunnel | 2026-08-16 |
| Fedora | [FEDORA-2026-84a39c58c9](https://lwn.net/Articles/1088644/) | F43 | vaultwarden | 2026-08-13 |
| Fedora | [FEDORA-2026-c28185613c](https://lwn.net/Articles/1088643/) | F44 | vaultwarden | 2026-08-13 |
| Gentoo | [202608-05](https://lwn.net/Articles/1088852/) |  | Apache HTTPD | 2026-08-13 |
| Gentoo | [202608-09](https://lwn.net/Articles/1088853/) |  | Bubblewrap | 2026-08-14 |
| Gentoo | [202608-04](https://lwn.net/Articles/1088854/) |  | Dnsmasq | 2026-08-13 |
| Gentoo | [202608-07](https://lwn.net/Articles/1088855/) |  | Exim | 2026-08-14 |
| Gentoo | [202608-06](https://lwn.net/Articles/1088856/) |  | Flatpak | 2026-08-14 |
| Gentoo | [202608-02](https://lwn.net/Articles/1088645/) |  | FreeType | 2026-08-12 |
| Gentoo | [202608-10](https://lwn.net/Articles/1089117/) |  | HTTP-Daemon | 2026-08-14 |
| Gentoo | [202608-13](https://lwn.net/Articles/1089119/) |  | NTFS-3G | 2026-08-16 |
| Gentoo | [202608-12](https://lwn.net/Articles/1089120/) |  | Portage | 2026-08-15 |
| Gentoo | [202608-15](https://lwn.net/Articles/1089121/) |  | PostgreSQL | 2026-08-17 |
| Gentoo | [202608-14](https://lwn.net/Articles/1089122/) |  | X.Org X server, XWayland | 2026-08-17 |
| Gentoo | [202608-11](https://lwn.net/Articles/1089116/) |  | haveged | 2026-08-15 |
| Gentoo | [202608-08](https://lwn.net/Articles/1088857/) |  | libinput | 2026-08-14 |
| Gentoo | [202608-16](https://lwn.net/Articles/1089118/) |  | nginx | 2026-08-17 |
| Gentoo | [202608-03](https://lwn.net/Articles/1088858/) |  | rsync | 2026-08-13 |
| Mageia | [MGASA-2026-0335](https://lwn.net/Articles/1088859/) | 10 | dhcpcd | 2026-08-14 |
| Mageia | [MGASA-2026-0334](https://lwn.net/Articles/1088860/) | 10 | qemu | 2026-08-13 |
| Mageia | [MGASA-2026-0333](https://lwn.net/Articles/1088862/) | 10 | roundcubemail | 2026-08-13 |
| Mageia | [MGASA-2026-0332](https://lwn.net/Articles/1088861/) | 9 | roundcubemail | 2026-08-13 |
| Oracle | [ELSA-2026-55858](https://lwn.net/Articles/1089461/) | OL10 | .NET 10.0 | 2026-08-18 |
| Oracle | [ELSA-2026-54542](https://lwn.net/Articles/1089123/) | OL8 | .NET 10.0 | 2026-08-15 |
| Oracle | [ELSA-2026-54541](https://lwn.net/Articles/1088863/) | OL10 | .NET 8.0 | 2026-08-14 |
| Oracle | [ELSA-2026-54538](https://lwn.net/Articles/1089124/) | OL8 | .NET 8.0 | 2026-08-15 |
| Oracle | [ELSA-2026-54574](https://lwn.net/Articles/1088864/) | OL9 | .NET 8.0 | 2026-08-14 |
| Oracle | [ELSA-2026-54590](https://lwn.net/Articles/1088865/) | OL10 | .NET 9.0 | 2026-08-14 |
| Oracle | [ELSA-2026-54550](https://lwn.net/Articles/1089125/) | OL8 | .NET 9.0 | 2026-08-15 |
| Oracle | [ELSA-2026-55424](https://lwn.net/Articles/1089462/) | OL10 | 389-ds-base | 2026-08-18 |
| Oracle | [ELSA-2026-55423](https://lwn.net/Articles/1089463/) | OL9 | 389-ds-base | 2026-08-18 |
| Oracle | [ELSA-2026-55530](https://lwn.net/Articles/1089464/) | OL8 | 389-ds:1.4 | 2026-08-18 |
| Oracle | [ELSA-2026-55437](https://lwn.net/Articles/1089465/) | OL10 | bind | 2026-08-18 |
| Oracle | [ELSA-2026-54654](https://lwn.net/Articles/1089126/) | OL8 | bind | 2026-08-15 |
| Oracle | [ELSA-2026-54510](https://lwn.net/Articles/1088866/) | OL9 | bind | 2026-08-14 |
| Oracle | [ELSA-2026-54509](https://lwn.net/Articles/1088867/) | OL8 | bind9.16 | 2026-08-14 |
| Oracle | [ELSA-2026-55432](https://lwn.net/Articles/1089466/) | OL10 | curl | 2026-08-18 |
| Oracle | [ELSA-2026-54210](https://lwn.net/Articles/1089127/) | OL10 | dhcpcd | 2026-08-15 |
| Oracle | [ELSA-2026-26564](https://lwn.net/Articles/1088646/) | OL7 | dovecot | 2026-08-12 |
| Oracle | [ELSA-2026-49513](https://lwn.net/Articles/1088647/) | OL7 | dovecot | 2026-08-12 |
| Oracle | [ELSA-2026-54576](https://lwn.net/Articles/1089128/) | OL10 | dracut | 2026-08-15 |
| Oracle | [ELSA-2026-54575](https://lwn.net/Articles/1089130/) | OL8 | dracut | 2026-08-15 |
| Oracle | [ELSA-2026-54571](https://lwn.net/Articles/1089129/) | OL9 | dracut | 2026-08-15 |
| Oracle | [ELSA-2026-41904](https://lwn.net/Articles/1088648/) | OL7 | evince | 2026-08-12 |
| Oracle | [ELSA-2026-53363](https://lwn.net/Articles/1088649/) | OL8 | fence-agents | 2026-08-12 |
| Oracle | [ELSA-2026-53365](https://lwn.net/Articles/1088650/) | OL9 | fence-agents | 2026-08-12 |
| Oracle | [ELSA-2026-54486](https://lwn.net/Articles/1088868/) | OL10 | freerdp | 2026-08-13 |
| Oracle | [ELSA-2026-54485](https://lwn.net/Articles/1088870/) | OL8 | freerdp | 2026-08-14 |
| Oracle | [ELSA-2026-54487](https://lwn.net/Articles/1088869/) | OL9 | freerdp | 2026-08-14 |
| Oracle | [ELSA-2026-51183](https://lwn.net/Articles/1088871/) | OL7 | glib2 | 2026-08-13 |
| Oracle | [ELSA-2026-54512](https://lwn.net/Articles/1088872/) | OL10 | gnome-remote-desktop | 2026-08-14 |
| Oracle | [ELSA-2026-43575](https://lwn.net/Articles/1088651/) | OL7 | gnutls | 2026-08-12 |
| Oracle | [ELSA-2026-54178](https://lwn.net/Articles/1088874/) | OL10 | grafana | 2026-08-13 |
| Oracle | [ELSA-2026-54243](https://lwn.net/Articles/1088873/) | OL8 | grafana | 2026-08-13 |
| Oracle | [ELSA-2026-54184](https://lwn.net/Articles/1089131/) | OL9 | grafana | 2026-08-15 |
| Oracle | [ELSA-2026-55865](https://lwn.net/Articles/1089468/) | OL9 | gstreamer1-plugins-bad-free and gstreamer1-plugins-ugly-free | 2026-08-18 |
| Oracle | [ELSA-2026-55433](https://lwn.net/Articles/1089467/) | OL10 | gstreamer1-plugins-bad-free | 2026-08-18 |
| Oracle | [ELSA-2026-47176](https://lwn.net/Articles/1088652/) | OL7 | gstreamer1-plugins-bad-free | 2026-08-12 |
| Oracle | [ELSA-2026-53451](https://lwn.net/Articles/1088654/) | OL10 | gstreamer1-plugins-good | 2026-08-12 |
| Oracle | [ELSA-2026-55434](https://lwn.net/Articles/1089469/) | OL10 | gstreamer1-plugins-good | 2026-08-18 |
| Oracle | [ELSA-2026-49603](https://lwn.net/Articles/1088875/) | OL7 | gstreamer1-plugins-good | 2026-08-13 |
| Oracle | [ELSA-2026-53452](https://lwn.net/Articles/1088653/) | OL9 | gstreamer1-plugins-good | 2026-08-12 |
| Oracle | [ELSA-2026-55436](https://lwn.net/Articles/1089470/) | OL9 | gstreamer1-plugins-good | 2026-08-18 |
| Oracle | [ELSA-2026-55435](https://lwn.net/Articles/1089471/) | OL10 | gstreamer1-plugins-ugly-free | 2026-08-18 |
| Oracle | [ELSA-2026-55679](https://lwn.net/Articles/1089473/) | OL10 | haproxy | 2026-08-18 |
| Oracle | [ELSA-2026-55859](https://lwn.net/Articles/1089474/) | OL8 | haproxy | 2026-08-18 |
| Oracle | [ELSA-2026-55772](https://lwn.net/Articles/1089472/) | OL9 | haproxy | 2026-08-18 |
| Oracle | [ELSA-2026-53845](https://lwn.net/Articles/1089132/) | OL10 | iscsi-initiator-utils | 2026-08-15 |
| Oracle | [ELSA-2026-53844](https://lwn.net/Articles/1089133/) | OL9 | iscsi-initiator-utils | 2026-08-15 |
| Oracle | [ELSA-2026-53846](https://lwn.net/Articles/1088656/) | OL10 | isns-utils | 2026-08-12 |
| Oracle | [ELSA-2026-53848](https://lwn.net/Articles/1088876/) | OL8 | isns-utils | 2026-08-13 |
| Oracle | [ELSA-2026-53847](https://lwn.net/Articles/1088655/) | OL9 | isns-utils | 2026-08-12 |
| Oracle | [ELSA-2026-42877](https://lwn.net/Articles/1088657/) | OL8 | java-1.8.0-openjdk | 2026-08-12 |
| Oracle | [ELSA-2026-42877](https://lwn.net/Articles/1088658/) | OL9 | java-1.8.0-openjdk | 2026-08-12 |
| Oracle | [ELSA-2026-42887](https://lwn.net/Articles/1088878/) | OL8 | java-17-openjdk | 2026-08-14 |
| Oracle | [ELSA-2026-42887](https://lwn.net/Articles/1088877/) | OL9 | java-17-openjdk | 2026-08-13 |
| Oracle | [ELSA-2026-34911](https://lwn.net/Articles/1088663/) | OL10 | kernel | 2026-08-12 |
| Oracle | [ELSA-2026-53330](https://lwn.net/Articles/1088664/) | OL10 | kernel | 2026-08-12 |
| Oracle | [ELSA-2026-36541](https://lwn.net/Articles/1088880/) | OL10 | kernel | 2026-08-13 |
| Oracle | [ELSA-2026-36956](https://lwn.net/Articles/1089134/) | OL10 | kernel | 2026-08-15 |
| Oracle | [ELSA-2026-54343](https://lwn.net/Articles/1089135/) | OL10 | kernel | 2026-08-15 |
| Oracle | [ELSA-2026-500162](https://lwn.net/Articles/1088659/) | OL8 | kernel | 2026-08-12 |
| Oracle | [ELSA-2026-52765](https://lwn.net/Articles/1088879/) | OL8 | kernel | 2026-08-13 |
| Oracle | [ELSA-2026-500162](https://lwn.net/Articles/1088660/) | OL9 | kernel | 2026-08-12 |
| Oracle | [ELSA-2026-500162](https://lwn.net/Articles/1088662/) | OL9 | kernel | 2026-08-12 |
| Oracle | [ELSA-2026-53329](https://lwn.net/Articles/1088661/) | OL9 | kernel | 2026-08-12 |
| Oracle | [ELSA-2026-54443](https://lwn.net/Articles/1089136/) | OL9 | kernel | 2026-08-15 |
| Oracle | [ELSA-2026-55448](https://lwn.net/Articles/1089476/) | OL10 | libXfont2 | 2026-08-18 |
| Oracle | [ELSA-2026-51063](https://lwn.net/Articles/1088882/) | OL7 | libXfont2 | 2026-08-13 |
| Oracle | [ELSA-2026-55447](https://lwn.net/Articles/1089477/) | OL9 | libXfont2 | 2026-08-18 |
| Oracle | [ELSA-2026-8517](https://lwn.net/Articles/1088665/) | OL7 | libarchive | 2026-08-12 |
| Oracle | [ELSA-2026-52674](https://lwn.net/Articles/1088666/) | OL9 | libarchive | 2026-08-12 |
| Oracle | [ELSA-2026-50808](https://lwn.net/Articles/1088881/) | OL7 | libpng | 2026-08-13 |
| Oracle | [ELSA-2026-55855](https://lwn.net/Articles/1089475/) | OL10 | libssh | 2026-08-18 |
| Oracle | [ELSA-2026-54650](https://lwn.net/Articles/1088884/) | OL10 | nghttp2 | 2026-08-14 |
| Oracle | [ELSA-2026-54662](https://lwn.net/Articles/1088883/) | OL9 | nghttp2 | 2026-08-14 |
| Oracle | [ELSA-2026-55541](https://lwn.net/Articles/1089478/) | OL10 | nodejs22 | 2026-08-18 |
| Oracle | [ELSA-2026-54530](https://lwn.net/Articles/1089479/) | OL8 | nodejs:22 | 2026-08-18 |
| Oracle | [ELSA-2026-54371](https://lwn.net/Articles/1089137/) | OL8 | nodejs:24 | 2026-08-15 |
| Oracle | [ELSA-2026-47756](https://lwn.net/Articles/1089138/) | OL9 | openssh | 2026-08-15 |
| Oracle | [ELSA-2026-49526](https://lwn.net/Articles/1088667/) | OL10 | osbuild-composer | 2026-08-12 |
| Oracle | [ELSA-2026-22450](https://lwn.net/Articles/1089139/) | OL10 | osbuild-composer | 2026-08-15 |
| Oracle | [ELSA-2026-55617](https://lwn.net/Articles/1089480/) | OL10 | pcp | 2026-08-18 |
| Oracle | [ELSA-2026-52772](https://lwn.net/Articles/1088885/) | OL8 | perl-DBI:1.641 | 2026-08-13 |
| Oracle | [ELSA-2026-47082](https://lwn.net/Articles/1088668/) | OL9 | pipewire | 2026-08-12 |
| Oracle | [ELSA-2026-52395](https://lwn.net/Articles/1088669/) | OL9 | postgresql | 2026-08-12 |
| Oracle | [ELSA-2026-54481](https://lwn.net/Articles/1088887/) | OL10 | python-idna | 2026-08-13 |
| Oracle | [ELSA-2026-54290](https://lwn.net/Articles/1088886/) | OL8 | python-idna | 2026-08-13 |
| Oracle | [ELSA-2026-54484](https://lwn.net/Articles/1089140/) | OL9 | python-idna | 2026-08-15 |
| Oracle | [ELSA-2026-54268](https://lwn.net/Articles/1088888/) | OL9 | python3.9 | 2026-08-13 |
| Oracle | [ELSA-2026-50778](https://lwn.net/Articles/1089141/) | OL10 | ruby | 2026-08-15 |
| Oracle | [ELSA-2026-37397](https://lwn.net/Articles/1088670/) | OL7 | ruby | 2026-08-12 |
| Oracle | [ELSA-2026-50773](https://lwn.net/Articles/1089142/) | OL10 | ruby4.0 | 2026-08-15 |
| Oracle | [ELSA-2026-50728](https://lwn.net/Articles/1088671/) | OL8 | ruby:3.3 | 2026-08-12 |
| Oracle | [ELSA-2026-13895](https://lwn.net/Articles/1088672/) | OL7 | sudo | 2026-08-12 |
| Oracle | [ELSA-2026-53435](https://lwn.net/Articles/1088673/) | OL10 | udisks2 | 2026-08-12 |
| Oracle | [ELSA-2026-55892](https://lwn.net/Articles/1089482/) | OL10 | unbound | 2026-08-18 |
| Oracle | [ELSA-2026-55784](https://lwn.net/Articles/1089483/) | OL8 | unbound | 2026-08-18 |
| Oracle | [ELSA-2026-55841](https://lwn.net/Articles/1089481/) | OL9 | unbound | 2026-08-18 |
| Oracle | [ELSA-2026-36083](https://lwn.net/Articles/1088889/) | OL7 | xorg-x11-server | 2026-08-14 |
| Red Hat | [RHSA-2026:54510-01](https://lwn.net/Articles/1088582/) | EL9 | bind | 2026-08-13 |
| Red Hat | [RHSA-2026:54509-01](https://lwn.net/Articles/1088583/) | EL8 | bind9.16 | 2026-08-13 |
| Red Hat | [RHSA-2026:53363-01](https://lwn.net/Articles/1089296/) | EL8 | fence-agents | 2026-08-18 |
| Red Hat | [RHSA-2026:53365-01](https://lwn.net/Articles/1089295/) | EL9 | fence-agents | 2026-08-18 |
| Red Hat | [RHSA-2026:54512-01](https://lwn.net/Articles/1088588/) | EL10 | gnome-remote-desktop | 2026-08-13 |
| Red Hat | [RHSA-2026:47719-01](https://lwn.net/Articles/1089415/) | EL9.2 | golang | 2026-08-19 |
| Red Hat | [RHSA-2026:47712-01](https://lwn.net/Articles/1089418/) | EL9.4 | golang | 2026-08-19 |
| Red Hat | [RHSA-2026:46391-01](https://lwn.net/Articles/1088594/) | EL8 | grafana | 2026-08-13 |
| Red Hat | [RHSA-2026:47722-01](https://lwn.net/Articles/1089411/) | EL9.2 | grafana | 2026-08-19 |
| Red Hat | [RHSA-2026:47714-01](https://lwn.net/Articles/1089417/) | EL9.4 | grafana | 2026-08-19 |
| Red Hat | [RHSA-2026:51112-01](https://lwn.net/Articles/1088592/) | EL9.6 | grafana | 2026-08-13 |
| Red Hat | [RHSA-2026:47721-01](https://lwn.net/Articles/1089414/) | EL9.2 | grafana-pcp | 2026-08-19 |
| Red Hat | [RHSA-2026:47716-01](https://lwn.net/Articles/1089416/) | EL9.4 | grafana-pcp | 2026-08-19 |
| Red Hat | [RHSA-2026:53413-01](https://lwn.net/Articles/1088590/) | EL10.0 | opentelemetry-collector | 2026-08-13 |
| Red Hat | [RHSA-2026:53412-01](https://lwn.net/Articles/1088591/) | EL9.4 | opentelemetry-collector | 2026-08-13 |
| Red Hat | [RHSA-2026:53415-01](https://lwn.net/Articles/1088589/) | EL9.6 | opentelemetry-collector | 2026-08-13 |
| Red Hat | [RHSA-2026:48790-01](https://lwn.net/Articles/1089297/) | EL8 | osbuild-composer | 2026-08-18 |
| Red Hat | [RHSA-2026:48036-01](https://lwn.net/Articles/1089413/) | EL9.2 | osbuild-composer | 2026-08-19 |
| Red Hat | [RHSA-2026:47910-01](https://lwn.net/Articles/1089412/) | EL9.4 | osbuild-composer | 2026-08-19 |
| Red Hat | [RHSA-2026:56131-01](https://lwn.net/Articles/1089293/) | EL8 | pam | 2026-08-18 |
| Red Hat | [RHSA-2026:48021-01](https://lwn.net/Articles/1088587/) | EL8 | python-pillow | 2026-08-13 |
| Red Hat | [RHSA-2026:52551-01](https://lwn.net/Articles/1088586/) | EL8.4 | python-pillow | 2026-08-13 |
| Red Hat | [RHSA-2026:54528-01](https://lwn.net/Articles/1088584/) | EL8.6 | python-pillow | 2026-08-13 |
| Red Hat | [RHSA-2026:54417-01](https://lwn.net/Articles/1088585/) | EL8.8 | python-pillow | 2026-08-13 |
| Red Hat | [RHSA-2026:39320-01](https://lwn.net/Articles/1088581/) | EL8 | python3 | 2026-08-13 |
| Red Hat | [RHSA-2026:50816-01](https://lwn.net/Articles/1088572/) | EL8.4 | python3 | 2026-08-13 |
| Red Hat | [RHSA-2026:50065-01](https://lwn.net/Articles/1088575/) | EL8.6 | python3 | 2026-08-13 |
| Red Hat | [RHSA-2026:50064-01](https://lwn.net/Articles/1088571/) | EL8.8 | python3 | 2026-08-13 |
| Red Hat | [RHSA-2026:39183-01](https://lwn.net/Articles/1088580/) | EL10 | python3.12 | 2026-08-13 |
| Red Hat | [RHSA-2026:47939-01](https://lwn.net/Articles/1088573/) | EL10.0 | python3.12 | 2026-08-13 |
| Red Hat | [RHSA-2026:39771-01](https://lwn.net/Articles/1088578/) | EL9 | python3.12 | 2026-08-13 |
| Red Hat | [RHSA-2026:50771-01](https://lwn.net/Articles/1088570/) | EL9.4 | python3.12 | 2026-08-13 |
| Red Hat | [RHSA-2026:50770-01](https://lwn.net/Articles/1088574/) | EL9.6 | python3.12 | 2026-08-13 |
| Red Hat | [RHSA-2026:40856-01](https://lwn.net/Articles/1088577/) | EL10 | python3.14 | 2026-08-13 |
| Red Hat | [RHSA-2026:41949-01](https://lwn.net/Articles/1088576/) | EL9 | python3.14 | 2026-08-13 |
| Red Hat | [RHSA-2026:54268-01](https://lwn.net/Articles/1088569/) | EL9 | python3.9 | 2026-08-13 |
| Red Hat | [RHSA-2026:39798-01](https://lwn.net/Articles/1088579/) | EL9 | python3.9 | 2026-08-13 |
| Red Hat | [RHSA-2026:53364-01](https://lwn.net/Articles/1089294/) | EL8 | resource-agents | 2026-08-18 |
| Red Hat | [RHSA-2026:49600-01](https://lwn.net/Articles/1089410/) | EL9.2 | rhc | 2026-08-19 |
| Red Hat | [RHSA-2026:49509-01](https://lwn.net/Articles/1089409/) | EL9.4 | rhc | 2026-08-19 |
| Red Hat | [RHSA-2026:54401-01](https://lwn.net/Articles/1088593/) | EL9.6 | rhc | 2026-08-13 |
| Red Hat | [RHSA-2026:50142-01](https://lwn.net/Articles/1089290/) | EL10 | sg3\_utils | 2026-08-18 |
| Red Hat | [RHSA-2026:56130-01](https://lwn.net/Articles/1089291/) | EL8 | sg3\_utils | 2026-08-18 |
| Red Hat | [RHSA-2026:50141-01](https://lwn.net/Articles/1089292/) | EL9 | sg3\_utils | 2026-08-18 |
| Slackware | [SSA:2026-227-01](https://lwn.net/Articles/1089143/) |  | proftpd | 2026-08-15 |
| Slackware | [SSA:2026-225-01](https://lwn.net/Articles/1088890/) |  | rsync | 2026-08-13 |
| SUSE | [openSUSE-SU-2026:11502-1](https://lwn.net/Articles/1089144/) | TW | 7zip | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23071-1](https://lwn.net/Articles/1089145/) | SLE-m6.1 | afterburn | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11503-1](https://lwn.net/Articles/1089146/) | TW | ansible-lint | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23150-1](https://lwn.net/Articles/1088891/) | SLE16.0 | bouncycastle | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23127-1](https://lwn.net/Articles/1089147/) | SLE16.0 | bouncycastle | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11512-1](https://lwn.net/Articles/1089148/) | TW | cargo-audit | 2026-08-16 |
| SUSE | [openSUSE-SU-2026:11513-1](https://lwn.net/Articles/1089149/) | TW | cargo-c | 2026-08-16 |
| SUSE | [openSUSE-SU-2026:11511-1](https://lwn.net/Articles/1089150/) | TW | chromedriver | 2026-08-16 |
| SUSE | [openSUSE-SU-2026:21561-1](https://lwn.net/Articles/1088675/) | oS16.0 | chromium | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:21581-1](https://lwn.net/Articles/1089151/) | oS16.0 | chromium | 2026-08-16 |
| SUSE | [openSUSE-SU-2026:0281-1](https://lwn.net/Articles/1088674/) | osB15 | chromium | 2026-08-13 |
| SUSE | [openSUSE-SU-2026:0284-1](https://lwn.net/Articles/1088892/) | osB15 | chromium | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11494-1](https://lwn.net/Articles/1088676/) | TW | clusterctl | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:11514-1](https://lwn.net/Articles/1089152/) | TW | containerized-data-importer | 2026-08-16 |
| SUSE | [SUSE-SU-2026:23146-1](https://lwn.net/Articles/1088893/) | SLE16.0 | dnsdist | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23123-1](https://lwn.net/Articles/1089153/) | SLE16.0 | dnsdist | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11504-1](https://lwn.net/Articles/1089154/) | TW | dracut-112 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3598-1](https://lwn.net/Articles/1088678/) | SLE12 | dracut | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3613-1](https://lwn.net/Articles/1088896/) | SLE15 | dracut | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3599-1](https://lwn.net/Articles/1088677/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | dracut | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3611-1](https://lwn.net/Articles/1088895/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | dracut | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3612-1](https://lwn.net/Articles/1088894/) | SLE15 oS15.6 | dracut | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3645-1](https://lwn.net/Articles/1089484/) | SLE15 oS15.3 | erlang | 2026-08-19 |
| SUSE | [openSUSE-SU-2026:11515-1](https://lwn.net/Articles/1089155/) | TW | ffmpeg-9-libavcodec-devel | 2026-08-16 |
| SUSE | [SUSE-SU-2026:3632-1](https://lwn.net/Articles/1089320/) | SLE15 | ffmpeg | 2026-08-18 |
| SUSE | [SUSE-SU-2026:23115-1](https://lwn.net/Articles/1089156/) | SLE16.0 | firefox | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23137-1](https://lwn.net/Articles/1089157/) | SLE16.0 | firefox | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11529-1](https://lwn.net/Articles/1089485/) | TW | forgejo-cli | 2026-08-18 |
| SUSE | [SUSE-SU-2026:23074-1](https://lwn.net/Articles/1089158/) | SLE-m6.1 | freetype2 | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21548-1](https://lwn.net/Articles/1088679/) | oS16.0 | gd | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:11495-1](https://lwn.net/Articles/1088680/) | TW | git-cliff | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:0287-1](https://lwn.net/Articles/1089159/) | osB15 | git-cliff | 2026-08-17 |
| SUSE | [openSUSE-SU-2026:21557-1](https://lwn.net/Articles/1088681/) | oS16.0 | gleam | 2026-08-12 |
| SUSE | [SUSE-SU-2026:23078-1](https://lwn.net/Articles/1089160/) | SLE-m6.1 | glib2 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3640-1](https://lwn.net/Articles/1089486/) | SLE15 | go1.25 | 2026-08-18 |
| SUSE | [openSUSE-SU-2026:11516-1](https://lwn.net/Articles/1089161/) | TW | go1.25 | 2026-08-16 |
| SUSE | [SUSE-SU-2026:3641-1](https://lwn.net/Articles/1089487/) | SLE15 | go1.26 | 2026-08-18 |
| SUSE | [openSUSE-SU-2026:11517-1](https://lwn.net/Articles/1089162/) | TW | go1.26 | 2026-08-16 |
| SUSE | [SUSE-SU-2026:23077-1](https://lwn.net/Articles/1089163/) | SLE-m6.1 | google-guest-agent | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23073-1](https://lwn.net/Articles/1089164/) | SLE-m6.1 | google-osconfig-agent | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21551-1](https://lwn.net/Articles/1088682/) | oS16.0 | govulncheck-vulndb | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:21553-1](https://lwn.net/Articles/1088683/) | oS16.0 | graphicsmagick | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3590-1](https://lwn.net/Articles/1088685/) | SLE12 | gzip | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3592-1](https://lwn.net/Articles/1088684/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | gzip | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:11518-1](https://lwn.net/Articles/1089165/) | TW | gzip | 2026-08-16 |
| SUSE | [openSUSE-SU-2026:21573-1](https://lwn.net/Articles/1089166/) | oS16.0 | himmelblau | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11531-1](https://lwn.net/Articles/1089488/) | TW | htop | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3614-1](https://lwn.net/Articles/1088898/) | SLE12 | java-1\_8\_0-ibm | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3615-1](https://lwn.net/Articles/1088897/) | SLE15 | java-1\_8\_0-ibm | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3622-1](https://lwn.net/Articles/1089167/) | SLE12 | java-1\_8\_0-openjdk | 2026-08-17 |
| SUSE | [SUSE-SU-2026:3623-1](https://lwn.net/Articles/1089168/) | SLE15 | java-1\_8\_0-openjdk | 2026-08-17 |
| SUSE | [SUSE-SU-2026:3631-1](https://lwn.net/Articles/1089321/) | SLE15 | jetty-minimal | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3593-1](https://lwn.net/Articles/1088688/) | MP4.3 SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | kernel | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3594-1](https://lwn.net/Articles/1088689/) | SLE12 | kernel | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3616-1](https://lwn.net/Articles/1088900/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 | kernel | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3595-1](https://lwn.net/Articles/1088687/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3617-1](https://lwn.net/Articles/1088899/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3602-1](https://lwn.net/Articles/1088686/) | SLE15 oS15.6 | kernel | 2026-08-13 |
| SUSE | [SUSE-SU-2026:23066-1](https://lwn.net/Articles/1089169/) | SLE16.0 SLE-m6.2 | kernel | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23068-1](https://lwn.net/Articles/1089170/) | SLE16.0 SLE-m6.2 | kernel | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11506-1](https://lwn.net/Articles/1089171/) | TW | kernel-devel | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11519-1](https://lwn.net/Articles/1089172/) | TW | kubeshark-cli | 2026-08-16 |
| SUSE | [SUSE-SU-2026:3604-1](https://lwn.net/Articles/1088690/) | SLE15 | kubevirt | 2026-08-13 |
| SUSE | [openSUSE-SU-2026:11520-1](https://lwn.net/Articles/1089173/) | TW | kubevirt1.9-continer-disk | 2026-08-16 |
| SUSE | [SUSE-SU-2026:23151-1](https://lwn.net/Articles/1088901/) | SLE16.0 | libXfont2 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23128-1](https://lwn.net/Articles/1089175/) | SLE16.0 | libXfont2 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3597-1](https://lwn.net/Articles/1088691/) | SLE15 | libheif | 2026-08-12 |
| SUSE | [SUSE-SU-2026:23070-1](https://lwn.net/Articles/1089174/) | SLE-m6.1 | libkrun | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21563-1](https://lwn.net/Articles/1088692/) | oS16.0 | librest0\_7 | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:11507-1](https://lwn.net/Articles/1089176/) | TW | molecule | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23076-1](https://lwn.net/Articles/1089177/) | SLE-m6.1 | net-tools | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23118-1](https://lwn.net/Articles/1089178/) | SLE16.0 | nginx | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23140-1](https://lwn.net/Articles/1089179/) | SLE16.0 | nginx | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23154-1](https://lwn.net/Articles/1088902/) | SLE16.0 | nodejs22 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23130-1](https://lwn.net/Articles/1089180/) | SLE16.0 | nodejs22 | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21545-1](https://lwn.net/Articles/1088693/) | oS16.0 | nodejs22 | 2026-08-12 |
| SUSE | [SUSE-SU-2026:23155-1](https://lwn.net/Articles/1088903/) | SLE16.0 | nodejs24 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23131-1](https://lwn.net/Articles/1089181/) | SLE16.0 | nodejs24 | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21546-1](https://lwn.net/Articles/1088694/) | oS16.0 | nodejs24 | 2026-08-12 |
| SUSE | [SUSE-SU-2026:23157-1](https://lwn.net/Articles/1089322/) | SLE-m6.2 | open-iscsi | 2026-08-17 |
| SUSE | [openSUSE-SU-2026:21580-1](https://lwn.net/Articles/1089182/) | oS16.0 | open-iscsi | 2026-08-16 |
| SUSE | [SUSE-SU-2026:3605-1](https://lwn.net/Articles/1088695/) | SLE15 oS15.6 | openssh | 2026-08-13 |
| SUSE | [SUSE-SU-2026:3596-1](https://lwn.net/Articles/1088696/) | SLE15 oS15.6 | openvpn | 2026-08-12 |
| SUSE | [SUSE-SU-2026:23075-1](https://lwn.net/Articles/1089183/) | SLE-m6.1 | perl | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11508-1](https://lwn.net/Articles/1089184/) | TW | pgadmin4 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23116-1](https://lwn.net/Articles/1089185/) | SLE16.0 | php-composer2 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23138-1](https://lwn.net/Articles/1089186/) | SLE16.0 | php-composer2 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23144-1](https://lwn.net/Articles/1088904/) | SLE16.0 | php8 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23121-1](https://lwn.net/Articles/1089187/) | SLE16.0 | php8 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3635-1](https://lwn.net/Articles/1089323/) | SLE15 | python | 2026-08-18 |
| SUSE | [SUSE-SU-2026:23142-1](https://lwn.net/Articles/1088905/) | SLE16.0 | python-httplib2 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23120-1](https://lwn.net/Articles/1089188/) | SLE16.0 | python-httplib2 | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21589-1](https://lwn.net/Articles/1089489/) | oS16.0 | python-pypdf2 | 2026-08-18 |
| SUSE | [SUSE-SU-2026:23112-1](https://lwn.net/Articles/1089189/) | SLE16.0 | python-sh | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23134-1](https://lwn.net/Articles/1089190/) | SLE16.0 | python-sh | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23114-1](https://lwn.net/Articles/1089191/) | SLE16.0 | python-ujson | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23136-1](https://lwn.net/Articles/1089192/) | SLE16.0 | python-ujson | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3601-1](https://lwn.net/Articles/1088697/) | SLE12 | python3 | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:11509-1](https://lwn.net/Articles/1089193/) | TW | python3-ansible-compat | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11523-1](https://lwn.net/Articles/1089324/) | TW | python313-h2 | 2026-08-17 |
| SUSE | [openSUSE-SU-2026:11510-1](https://lwn.net/Articles/1089194/) | TW | python313-nltk | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11524-1](https://lwn.net/Articles/1089325/) | TW | python313-pysaml2 | 2026-08-17 |
| SUSE | [openSUSE-SU-2026:11498-1](https://lwn.net/Articles/1088698/) | TW | python313-scikit-learn | 2026-08-12 |
| SUSE | [openSUSE-SU-2026:11533-1](https://lwn.net/Articles/1089490/) | TW | python313-tablib | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3637-1](https://lwn.net/Articles/1089327/) | SLE15 oS15.4 | redis | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3638-1](https://lwn.net/Articles/1089326/) | SLE15 oS15.6 | redis | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3636-1](https://lwn.net/Articles/1089329/) | SLE15 oS15.5 | redis7 | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3639-1](https://lwn.net/Articles/1089328/) | SLE15 oS15.6 | redis7 | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3600-1](https://lwn.net/Articles/1088699/) | MP4.3 SLE15 SLE5.4 SLE5.5 SLE-m5.4 SLE-m5.5 oS15.4 | rpm | 2026-08-12 |
| SUSE | [SUSE-SU-2026:23141-1](https://lwn.net/Articles/1088906/) | SLE16.0 | rrdtool | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23119-1](https://lwn.net/Articles/1089195/) | SLE16.0 | rrdtool | 2026-08-14 |
| SUSE | [SUSE-SU-2026:3629-1](https://lwn.net/Articles/1089330/) | SLE12 | rsync | 2026-08-18 |
| SUSE | [SUSE-SU-2026:3634-1](https://lwn.net/Articles/1089331/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | rsync | 2026-08-18 |
| SUSE | [SUSE-SU-2026:23145-1](https://lwn.net/Articles/1088907/) | SLE16.0 | rsyslog | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23122-1](https://lwn.net/Articles/1089196/) | SLE16.0 | rsyslog | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23152-1](https://lwn.net/Articles/1088908/) | SLE16.0 | samba | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23129-1](https://lwn.net/Articles/1089197/) | SLE16.0 | samba | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11527-1](https://lwn.net/Articles/1089332/) | TW | sccache | 2026-08-17 |
| SUSE | [SUSE-SU-2026:3642-1](https://lwn.net/Articles/1089491/) | SLE15 | snphost | 2026-08-18 |
| SUSE | [SUSE-SU-2026:23109-1](https://lwn.net/Articles/1089198/) | SLE16.0 | spice-vdagent | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23110-1](https://lwn.net/Articles/1089199/) | SLE16.0 | sssd | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23132-1](https://lwn.net/Articles/1089200/) | SLE16.0 | sssd | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:11500-1](https://lwn.net/Articles/1088700/) | TW | stunnel | 2026-08-12 |
| SUSE | [SUSE-SU-2026:3628-1](https://lwn.net/Articles/1089333/) | SLE15 oS15.6 | texlive | 2026-08-18 |
| SUSE | [openSUSE-SU-2026:11528-1](https://lwn.net/Articles/1089334/) | TW | wasm-bindgen | 2026-08-17 |
| SUSE | [SUSE-SU-2026:23111-1](https://lwn.net/Articles/1089201/) | SLE16.0 | webkit2gtk3 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23133-1](https://lwn.net/Articles/1089202/) | SLE16.0 | webkit2gtk3 | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23147-1](https://lwn.net/Articles/1088909/) | SLE16.0 | wireshark | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23124-1](https://lwn.net/Articles/1089203/) | SLE16.0 | wireshark | 2026-08-14 |
| SUSE | [SUSE-SU-2026:23072-1](https://lwn.net/Articles/1089204/) | SLE-m6.1 | wpa\_supplicant | 2026-08-14 |
| SUSE | [openSUSE-SU-2026:21567-1](https://lwn.net/Articles/1088701/) | oS16.0 | zk | 2026-08-12 |
| Ubuntu | [USN-8642-1](https://lwn.net/Articles/1089492/) | 18.04 20.04 22.04 24.04 26.04 | c3p0 | 2026-08-18 |
| Ubuntu | [USN-8641-1](https://lwn.net/Articles/1089493/) | 22.04 24.04 26.04 | dotnet8, dotnet10 | 2026-08-19 |
| Ubuntu | [USN-8640-1](https://lwn.net/Articles/1089335/) | 16.04 18.04 20.04 22.04 | engrampa | 2026-08-17 |
| Ubuntu | [USN-8634-1](https://lwn.net/Articles/1088702/) | 14.04 | kernel | 2026-08-12 |
| Ubuntu | [USN-8646-1](https://lwn.net/Articles/1089494/) | 14.04 | kernel | 2026-08-18 |
| Ubuntu | [USN-8628-1](https://lwn.net/Articles/1088703/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | libgit2 | 2026-08-12 |
| Ubuntu | [USN-8644-1](https://lwn.net/Articles/1089495/) | 16.04 18.04 | linux, linux-aws, linux-aws-fips, linux-aws-hwe, linux-fips, linux-hwe, linux-kvm | 2026-08-18 |
| Ubuntu | [USN-8630-1](https://lwn.net/Articles/1088704/) | 22.04 24.04 | linux, linux-aws, linux-aws-fips, linux-azure, linux-azure-6.8, linux-azure-fde, linux-azure-fde-6.8, linux-azure-fips, linux-fips, linux-gcp, linux-gcp-6.8, linux-gcp-fips, linux-gke, linux-gkeop, linux-ibm, linux-ibm-6.8, linux-nvidia, linux-nvidia-6.8, linux-nvidia-lowlatency, linux-realtime, linux-realtime-6.8, linux-xilinx | 2026-08-12 |
| Ubuntu | [USN-8631-1](https://lwn.net/Articles/1088705/) | 20.04 22.04 | linux, linux-aws, linux-aws-fips, linux-azure, linux-azure-fde, linux-azure-fips, linux-gkeop, linux-ibm, linux-ibm-5.15, linux-intel-iot-realtime, linux-intel-iotg, linux-intel-iotg-5.15, linux-kvm, linux-nvidia, linux-nvidia-tegra, linux-nvidia-tegra-5.15, linux-oracle-5.15, linux-realtime, linux-xilinx-zynqmp | 2026-08-12 |
| Ubuntu | [USN-8643-1](https://lwn.net/Articles/1089496/) | 22.04 24.04 | linux, linux-aws, linux-aws-fips, linux-azure, linux-fips, linux-gcp, linux-gcp-6.8, linux-gcp-fips, linux-gkeop, linux-oracle, linux-realtime, linux-realtime-6.8, linux-xilinx | 2026-08-18 |
| Ubuntu | [USN-8633-1](https://lwn.net/Articles/1088706/) | 18.04 | linux, linux-aws, linux-aws-fips, linux-azure-4.15, linux-azure-fips, linux-fips, linux-gcp-4.15, linux-gcp-fips, linux-kvm | 2026-08-12 |
| Ubuntu | [USN-8629-1](https://lwn.net/Articles/1088707/) | 26.04 | linux, linux-aws, linux-azure, linux-azure-fde, linux-ibm, linux-oracle, linux-raspi, linux-realtime | 2026-08-12 |
| Ubuntu | [USN-8548-2](https://lwn.net/Articles/1088910/) | 16.04 | linux, linux-aws, linux-kvm | 2026-08-13 |
| Ubuntu | [USN-8629-2](https://lwn.net/Articles/1089336/) | 24.04 | linux-aws-7.0 | 2026-08-17 |
| Ubuntu | [USN-8633-2](https://lwn.net/Articles/1088912/) | 16.04 | linux-aws-hwe, linux-azure, linux-gcp, linux-hwe | 2026-08-13 |
| Ubuntu | [USN-8530-2](https://lwn.net/Articles/1088911/) | 16.04 | linux-aws-hwe | 2026-08-13 |
| Ubuntu | [USN-8529-2](https://lwn.net/Articles/1088913/) | 16.04 | linux-azure, linux-gcp, linux-hwe, linux-oracle | 2026-08-13 |
| Ubuntu | [USN-8635-1](https://lwn.net/Articles/1088708/) | 14.04 | linux-azure | 2026-08-12 |
| Ubuntu | [USN-8636-1](https://lwn.net/Articles/1088709/) | 24.04 | linux-azure-6.17, linux-gcp-6.17, linux-hwe-6.17, linux-oem-6.17, linux-realtime-6.17 | 2026-08-12 |
| Ubuntu | [USN-8631-4](https://lwn.net/Articles/1089337/) | 20.04 | linux-azure-fde-5.15 | 2026-08-17 |
| Ubuntu | [USN-8629-3](https://lwn.net/Articles/1089497/) | 24.04 | linux-hwe-7.0 | 2026-08-18 |
| Ubuntu | [USN-8630-2](https://lwn.net/Articles/1088914/) | 22.04 24.04 | linux-lowlatency, linux-lowlatency-hwe-6.8, linux-nvidia-tegra, linux-oracle | 2026-08-13 |
| Ubuntu | [USN-8631-3](https://lwn.net/Articles/1088915/) | 22.04 | linux-nvidia-tegra-igx | 2026-08-13 |
| Ubuntu | [USN-8637-1](https://lwn.net/Articles/1088916/) | 26.04 | linux-oem-7.0 | 2026-08-13 |
| Ubuntu | [USN-8645-1](https://lwn.net/Articles/1089498/) | 16.04 18.04 | linux-oracle | 2026-08-18 |
| Ubuntu | [USN-8631-2](https://lwn.net/Articles/1088917/) | 22.04 | linux-oracle | 2026-08-13 |
| Ubuntu | [USN-8636-2](https://lwn.net/Articles/1089499/) | 24.04 | linux-oracle-6.17 | 2026-08-18 |
| Ubuntu | [USN-8630-3](https://lwn.net/Articles/1089500/) | 22.04 | linux-oracle-6.8 | 2026-08-18 |
| Ubuntu | [USN-8638-1](https://lwn.net/Articles/1088918/) | 20.04 22.04 24.04 26.04 | node-axios | 2026-08-13 |
| Ubuntu | [USN-8632-1](https://lwn.net/Articles/1088710/) | 18.04 20.04 22.04 24.04 26.04 | node-follow-redirects | 2026-08-13 |
| Ubuntu | [USN-8627-1](https://lwn.net/Articles/1088711/) | 16.04 18.04 20.04 22.04 24.04 26.04 | yelp | 2026-08-12 |

[전체 기사](https://lwn.net/Articles/1089504/) ([댓글: 없음](https://lwn.net/Articles/1089504/#Comments))

[^c09-security-advisory]: 보안 권고는 취약점의 영향, 영향을 받는 패키지, 수정 업데이트 정보를 배포판이 공지하는 문서다.
[^c09-kernel]: kernel은 하드웨어 자원과 프로세스, 메모리, 파일 시스템, 네트워크를 중재하는 운영체제의 핵심 구성 요소다.

## 주목할 만한 커널 패치

---

### 커널 릴리스

#### 요약

- Linux 7.2와 여러 장기 지원 안정 릴리스가 공개되었습니다.
- 실시간(`-rt`) 커널 릴리스도 7.2, 6.6, 6.1, 5.10 계열에 걸쳐 포함됩니다.[^c10-rt]
- GNU Linux-libre 7.2-gnu는 Linux 7.2를 기반으로 한 자유 소프트웨어 지향 변형입니다.[^c10-linux-libre]

Linus Torvalds
[Linux 7.2](https://lwn.net/Articles/1089033/)
8월 16일

Sebastian Andrzej Siewior
[v7.2-rt5](https://lwn.net/Articles/1089352/)
8월 18일

Greg Kroah-Hartman
[Linux 7.1.9](https://lwn.net/Articles/1089545/)
8월 19일

Freedo
[GNU Linux-libre 7.2-gnu](https://lwn.net/Articles/1089207/)
8월 16일

Greg Kroah-Hartman
[Linux 6.18.45](https://lwn.net/Articles/1089546/)
8월 19일

Greg Kroah-Hartman
[Linux 6.12.104](https://lwn.net/Articles/1089547/)
8월 19일

Greg Kroah-Hartman
[Linux 6.6.152](https://lwn.net/Articles/1089548/)
8월 19일

Clark Williams
[6.6.151-rt78](https://lwn.net/Articles/1089265/)
8월 17일

Greg Kroah-Hartman
[Linux 6.1.183](https://lwn.net/Articles/1089549/)
8월 19일

Clark Williams
[6.1.182-rt67](https://lwn.net/Articles/1089266/)
8월 17일

Greg Kroah-Hartman
[Linux 5.15.216](https://lwn.net/Articles/1089550/)
8월 19일

Greg Kroah-Hartman
[Linux 5.10.265](https://lwn.net/Articles/1089551/)
8월 19일

Luis Claudio R. Goncalves
[5.10.264-rt160](https://lwn.net/Articles/1089379/)
8월 18일

### 아키텍처별

#### 요약

- 시스템 호출 표와 ARM64, RISC-V, s390, SPARC, x86 관련 변경이 제안되었습니다.
- RISC-V의 BPF JIT와 hwprobe, x86의 FPU 신호 프레임 및 MSR 인터페이스가 주요 대상입니다.[^c10-bpf][^c10-jit][^c10-msr]
- 성능 관찰을 위한 Hygon uncore PMU 지원과 이벤트 정의도 추가됩니다.[^c10-pmu]

André Almeida
[syscalls: 모든 아키텍처를 위한 공유 테이블 추가](https://lwn.net/Articles/1088717/)
8월 12일

KobaK
[arm64: CPU prefetch 및 cache modulation 제어 노출](https://lwn.net/Articles/1089217/)
8월 17일

Guodong Xu
[riscv: hwprobe: RVA23U64 기본 동작 노출](https://lwn.net/Articles/1088735/)
8월 12일

Feng Jiang
[bpf, riscv: RV64 JIT에 BPF 스택 인자 지원 추가](https://lwn.net/Articles/1088741/)
8월 13일

Alexander Gordeev
[s390/mm: lazy MMU 모드에서 PTE 업데이트 일괄 처리](https://lwn.net/Articles/1089234/)
8월 17일

Magnus Lindholm
[sparc32: RAM 시작 지점에서 떨어진 위치에 커널을 로드하도록 허용](https://lwn.net/Articles/1088929/)
8월 14일

Sebastian Andrzej Siewior
[X86\_X32\_ABI 제거 시작](https://lwn.net/Articles/1088750/)
8월 13일

Andrei Vagin
[x86/fpu: 신호 프레임 이식성 복원 및 강화](https://lwn.net/Articles/1089222/)
8월 17일

Qi Liu
[perf/x86/amd/uncore: Hygon uncore PMU 및 JSON 이벤트 추가](https://lwn.net/Articles/1089349/)
8월 18일

Juergen Gross
[x86/msr: 32비트 MSR 인터페이스 제거](https://lwn.net/Articles/1089517/)
8월 19일

### 코어 커널

#### 요약

- BPF verifier, cgroup CPU controller, 반환값과 per-CPU 데이터 기능이 확장됩니다.[^c10-verifier][^c10-cgroup][^c10-percpu]
- scheduler와 CFS의 실시간 성능, `sched_ext` 호환성 및 CPU 작업 순서가 개선 대상입니다.[^c10-scheduler][^c10-cfs]
- tracing, system call, 사용자 스택 unwinding, software interrupt moderation 관련 기능도 포함됩니다.[^c10-unwind][^c10-softirq]

Kumar Kartikeya Dwivedi
[검증 오류 재설계](https://lwn.net/Articles/1088753/)
8월 13일

Leon Hwang
[bpf: 전역 percpu 데이터 도입](https://lwn.net/Articles/1088796/)
8월 13일

Ziyang Men
[cgroup, sched: cgroup CPU controller에 bpf 추가](https://lwn.net/Articles/1088804/)
8월 13일

Yonghong Song
[bpf: 최대 16바이트 aggregate 반환값 지원](https://lwn.net/Articles/1088934/)
8월 13일

Kunwu Chan
[perf/core: AUX buffer kernel-consumer API 추가](https://lwn.net/Articles/1088955/)
8월 14일

Andrea Righi
[sched: proxy execution을 sched\_ext와 호환되도록 변경](https://lwn.net/Articles/1089027/)
8월 16일

Vineet Gupta
[bpf: 하위 32비트 전반에서 scalar equality 추적](https://lwn.net/Articles/1089007/)
8월 14일

Xin Zhao
[sched/fair: CFS 작업의 실시간 성능을 개선하는 load balance 패치 시리즈](https://lwn.net/Articles/1089017/)
8월 15일

Tejun Heo
[sched\_ext: scheduler hierarchy를 위한 core-sched 작업 순서 갱신](https://lwn.net/Articles/1089020/)
8월 15일

mathura kumar
[POSIX IPC mqueue에 새 system call mq\_recvmmsg() 및 mq\_sendmmsg() 두 개 추가](https://lwn.net/Articles/1089026/)
8월 16일

Vincent Donnefort
[tracing/remotes: printk, dump\_on\_panic 및 boot parameter 추가](https://lwn.net/Articles/1089239/)
8월 17일

Con Kolivas
[linux-7.2-ck1, linux-7.2용 MuQSS CPU scheduler](https://lwn.net/Articles/1089220/)
8월 17일

Ziyang Men
[cgroup: BPF에 cpu.stat 노출](https://lwn.net/Articles/1089341/)
8월 17일

Christian Brauner
[재시작할 수 없는 작업을 TIF\_NOTIFY\_SIGNAL이 중단하지 못하게 함](https://lwn.net/Articles/1089356/)
8월 18일

Jens Remus
[unwind\_user: .eh\_frame 처리 구현](https://lwn.net/Articles/1089377/)
8월 18일

Luigi Rizzo
[전역 Software Interrupt Moderation(GSIM)](https://lwn.net/Articles/1089521/)
8월 19일

### 개발 도구

#### 요약

- `selftests`가 XSK shared-UMEM, BPF 빌드, 메모리 관리 동작의 적용 범위를 넓힙니다.[^c10-selftests][^c10-xsk]
- `rtla`의 CPU 수 처리와 `khugepaged` 테스트 범위가 강화됩니다.[^c10-rtla][^c10-thp]
- persistent stack depot 기록을 위한 path-compressed trie 저장소가 추가됩니다.[^c10-stack-depot][^c10-trie]

Tushar Vyavahare
[selftests/xsk: shared-UMEM 적용 범위 개선](https://lwn.net/Articles/1088754/)
8월 13일

Ziyang Men
[selftests: BPF 프로그램과 skeleton 빌드를 위한 공유 lib.bpf.mk](https://lwn.net/Articles/1088924/)
8월 14일

Tomas Glozar
[rtla: 더 견고한 nr\_cpus 처리 구현](https://lwn.net/Articles/1088951/)
8월 14일

Kiryl Shutsemau
[selftests/mm: khugepaged 적용 범위 개선](https://lwn.net/Articles/1089008/)
8월 15일

Song Hu
[selftests/mm: TAP 출력 및 전역 상태 수정](https://lwn.net/Articles/1089013/)
8월 15일

Caleb Kan
[persistent stack depot 기록을 위한 path-compressed trie 저장소](https://lwn.net/Articles/1089237/)
8월 17일

[^c10-rt]: `-rt`는 PREEMPT_RT 실시간 패치 계열로, 예측 가능한 낮은 지연 시간을 목표로 합니다.
[^c10-linux-libre]: GNU Linux-libre는 비자유 펌웨어와 관련 코드를 제거한 Linux 커널 변형입니다.
[^c10-bpf]: BPF는 커널에서 안전하게 실행되는 프로그램을 위한 Linux의 확장 메커니즘입니다.
[^c10-jit]: JIT는 중간 표현을 실행 시점에 네이티브 기계어로 변환하는 컴파일 방식입니다.
[^c10-msr]: MSR(Model-Specific Register)은 CPU 공급업체별 제어 및 상태 레지스터입니다.
[^c10-pmu]: PMU(Performance Monitoring Unit)는 하드웨어 성능 이벤트를 계수하는 CPU 기능입니다.
[^c10-verifier]: BPF verifier는 BPF 프로그램이 커널에서 안전하게 실행될 수 있는지 정적으로 검사합니다.
[^c10-cgroup]: cgroup은 프로세스 그룹의 CPU, 메모리 등 자원 사용을 제한하고 계정 처리하는 Linux 기능입니다.
[^c10-percpu]: per-CPU 데이터는 각 CPU가 독립 복사본을 사용하여 경합을 줄이는 저장 방식입니다.
[^c10-scheduler]: Linux scheduler는 실행 가능한 작업에 CPU 시간을 배정합니다.
[^c10-cfs]: CFS(Completely Fair Scheduler)는 일반 작업에 CPU 시간을 공정하게 배분하는 Linux scheduler입니다.
[^c10-unwind]: stack unwinding은 호출 프레임을 거슬러 올라가 실행 경로를 복원하는 과정입니다.
[^c10-softirq]: software interrupt는 하드웨어 인터럽트 처리 이후 연기된 커널 작업을 수행하는 메커니즘입니다.
[^c10-selftests]: kernel selftests는 커널 기능을 직접 검증하는 Linux의 회귀 테스트 모음입니다.
[^c10-xsk]: XSK는 AF_XDP socket을 위한 사용자 공간 인터페이스로, 고성능 패킷 처리를 지원합니다.
[^c10-rtla]: rtla는 Linux 실시간 지연 시간과 스케줄링 동작을 분석하는 도구입니다.
[^c10-thp]: khugepaged는 Transparent Huge Pages를 병합·승격하는 커널 데몬입니다.
[^c10-stack-depot]: stack depot는 중복 스택 추적을 공유 저장해 메모리를 절약하는 커널 저장소입니다.
[^c10-trie]: trie는 공통 접두사를 공유하여 키를 압축하는 트리 기반 자료 구조입니다.

---

### 디바이스 드라이버

#### 요약

- 이 섹션은 다양한 하드웨어 플랫폼과 주변기기를 위한 Linux kernel 드라이버 제안을 모은다.[^c11-driver]
- PCIe, DMA, IOMMU, interrupt 등 장치 입출력 경로의 기능과 신뢰성을 확장한다.[^c11-pcie][^c11-dma][^c11-iommu][^c11-interrupt]
- 네트워크, GPU, 미디어, 센서, 전원 관리 하위 시스템의 지원 범위를 넓힌다.

Pavitrakumar Managutte
[crypto: SPAcc Crypto Driver 추가](https://lwn.net/Articles/1088718/)
Aug 12

Ali Rouhi
[dpll: SiTime SiT9531x DPLL clock driver 추가](https://lwn.net/Articles/1088719/)
Aug 12

Jesse Taube
[nvme-fc: FPIN 링크 무결성 처리](https://lwn.net/Articles/1088720/)
Aug 12

Wim de With
[backlight: Orient Chip OCP8178 지원 추가](https://lwn.net/Articles/1088724/)
Aug 12

Nikita Dubrovskih
[hwmon: HONOR FMI-XX 팬 모니터링 지원 추가](https://lwn.net/Articles/1088725/)
Aug 12

Leon Romanovsky
[PCI/HMAT: P2PDMA 도달 가능성 및 성능 기술](https://lwn.net/Articles/1088726/)
Aug 12

Maurice Hieronymus
[rust: samples: EDU PCI driver sample 추가 (MMIO + IRQ + DMA)](https://lwn.net/Articles/1088727/)
Aug 12

Elliot Douglas
[HID: logitech-hidpp: Signature M650 측면 버튼 타이밍 수정](https://lwn.net/Articles/1088728/)
Aug 12

Enzo Adriano
[clk: sunxi-ng: A523/T527 단일 divider clock 수정](https://lwn.net/Articles/1088729/)
Aug 12

Javier Carrasco
[iio: light: veml6031x00 ALS series 지원 추가](https://lwn.net/Articles/1088730/)
Aug 12

Jerome Brunet
[regulator: X-Powers AXP318W PMIC 지원 추가](https://lwn.net/Articles/1088732/)
Aug 12

Ian Rogers
[perf: Raspberry Pi AXI PMU driver 추가](https://lwn.net/Articles/1088733/)
Aug 12

Kyle Hsieh
[iio: adc: Texas Instruments ADS112C04 지원 추가](https://lwn.net/Articles/1088737/)
Aug 13

Long Li
[net: mana: queue set 교체를 통한 재구성](https://lwn.net/Articles/1088739/)
Aug 12

Koichiro Den
[PCI: endpoint: PCI DMA endpoint function 추가](https://lwn.net/Articles/1088740/)
Aug 13

Christian Marangi
[net: pcs: fwnode PCS 지원 도입](https://lwn.net/Articles/1088743/)
Aug 13

mhonap@nvidia.com
[vfio/pci: CXL Type-2 device passthrough 지원 추가](https://lwn.net/Articles/1088744/)
Aug 13

Long Zhao
[Ambarella CV75: bindings, RCT clocks 및 DT](https://lwn.net/Articles/1088745/)
Aug 13

Long Zhao
[Ambarella CV75: pinctrl 및 PL061 GPIO](https://lwn.net/Articles/1088746/)
Aug 13

Onur Özkan
[drm/tyr: GPU reset infrastructure](https://lwn.net/Articles/1088747/)
Aug 13

Robin Snyders
[power: supply: qcom\_smbx: SMB5 지원 추가](https://lwn.net/Articles/1088748/)
Aug 13

Kanak Shilledar
[Invensense ICM42370P accelerometer용 driver 추가](https://lwn.net/Articles/1088751/)
Aug 13

Tony Nguyen
[iXD driver 도입](https://lwn.net/Articles/1088752/)
Aug 12

Jason Gunthorpe
[SMMUv3에 generic iommu page table 사용](https://lwn.net/Articles/1088760/)
Aug 12

Sudeep Holla
[firmware: arm\_scmi: ACPI PCC transport의 리팩터링 및 활성화](https://lwn.net/Articles/1088761/)
Aug 13

Michael J. Ruhl
[Crescent Island PMT 지원](https://lwn.net/Articles/1088762/)
Aug 12

Janani Sunil
[iio: adc: AD7768/AD7768-4 ADC driver 지원 추가](https://lwn.net/Articles/1088792/)
Aug 13

Mukesh Kumar Savaliya
[QCOM GENI controllers용 multi-owner I2C 지원 활성화](https://lwn.net/Articles/1088793/)
Aug 13

Denis Benato
[HID: asus: ROG Ally handhelds 지원 추가](https://lwn.net/Articles/1088794/)
Aug 13

Miquel Raynal
[mtd: spi-nor: QE 처리 정리 + fixup 재작업 + Winbond RV chips 추가](https://lwn.net/Articles/1088795/)
Aug 13

Viken Dadhaniya
[Qualcomm I2C target controller driver 추가](https://lwn.net/Articles/1088797/)
Aug 13

Andrei Stancovici
[iio: adc: LTC2499 기능 지원 추가](https://lwn.net/Articles/1088798/)
Aug 13

Lyude Paul
[drm/nouveau: atomic modesetting을 기본으로 활성화](https://lwn.net/Articles/1088802/)
Aug 13

Brian Daniels
[media: virtio-media driver 추가](https://lwn.net/Articles/1088803/)
Aug 13

Vishwaroop A
[spi: tegra210-quad: 부하가 큰 시스템을 위한 interrupt 처리 개선](https://lwn.net/Articles/1088806/)
Aug 13

Jonas Jelonek
[net: pse-pd: Realtek PSE MCU 지원 추가](https://lwn.net/Articles/1088808/)
Aug 13

Vikas Gupta
[bnge에 기능 추가](https://lwn.net/Articles/1088921/)
Aug 14

javen
[r8169: RTL8127용 RSS 지원 추가](https://lwn.net/Articles/1088922/)
Aug 14

Hardeep Sharma
[Qualcomm Kuno SoC 초기 지원 추가](https://lwn.net/Articles/1088923/)
Aug 14

Ciprian Costea
[can: flexcan: NXP S32N79 SoC 지원 추가](https://lwn.net/Articles/1088925/)
Aug 14

Aniruddha Rao
[firmware: tegra: bpmp: ACPI 및 MBWT 지원 추가](https://lwn.net/Articles/1088926/)
Aug 14

luka.gejak@linux.dev
[wifi: rtw88: RTL8723B/RTL8723BS를 위한 준비](https://lwn.net/Articles/1088928/)
Aug 14

Dong Yibo
[net: rnpgbe: TX/RX 및 링크 상태 지원 추가](https://lwn.net/Articles/1088930/)
Aug 14

Luo Jie
[clk: qcom: ipq-cmn-pll: IPQ5210 CMN PLL 지원 추가](https://lwn.net/Articles/1088931/)
Aug 14

Joris Vaisvila
[net: dsa: mt7628 embedded switch 초기 지원](https://lwn.net/Articles/1088936/)
Aug 13

Maciek Machnikowski
[netdevsim에서 PTP 지원 구현](https://lwn.net/Articles/1088937/)
Aug 14

Mingming Cao
[ibmveth: multi-queue RX 지원 추가](https://lwn.net/Articles/1088938/)
Aug 14

Jack Flusche
[Broadcom FacetimeHD camera용 driver 추가](https://lwn.net/Articles/1088939/)
Aug 13

Claudiu Beznea
[PCI: rzg3s-host: PCIe hotplug 지원 추가](https://lwn.net/Articles/1088952/)
Aug 14

Tanmay Shah
[RPMsg buffer management 개선](https://lwn.net/Articles/1088956/)
Aug 14

Thierry Reding
[dma-buf: heaps: Tegra VPR 지원 추가](https://lwn.net/Articles/1088957/)
Aug 14

Thierry Reding
[PCI: tegra: Tegra264 지원 추가](https://lwn.net/Articles/1088958/)
Aug 14

Aaron Kling
[drm/panel: Retroid Pocket 6 panel 지원](https://lwn.net/Articles/1088961/)
Aug 14

Fangzhi Zuo
[HDMI 2.1 VRR 및 ALLM 지원](https://lwn.net/Articles/1088962/)
Aug 14

Markus Probst
[rtc: s35390a: wakealarm용 interrupt signal 1에 output pin 사용 허용](https://lwn.net/Articles/1089004/)
Aug 14

Ahmad Byagowi
[ptp: ocp: R4006 및 V9 I2C peripheral 지원 추가](https://lwn.net/Articles/1089006/)
Aug 14

Vladislav Zaharov
[gpu: nova-core: GSP-RM log buffers 유지](https://lwn.net/Articles/1089010/)
Aug 15

Daniel Golle
[net: dsa: mxl862xx: devlink flash 및 rescue](https://lwn.net/Articles/1089011/)
Aug 15

Rustam Adilov
[phy: realtek: usb2: RTL9607C USB2 PHY 지원](https://lwn.net/Articles/1089015/)
Aug 15

Shawn Guo
[remoteproc: qcom: Nord HPASS ADSP cluster 지원](https://lwn.net/Articles/1089018/)
Aug 15

Cristian Marussi
[SCMI Telemetry 지원 도입](https://lwn.net/Articles/1089019/)
Aug 15

Sreeshankar K
[SM7250용 Global Clock Controller (GCC) driver 추가](https://lwn.net/Articles/1089022/)
Aug 16

Sasha Finkelstein
[spmi: apple: 추가 commands 및 interrupt 지원](https://lwn.net/Articles/1089023/)
Aug 16

Peter Hunt
[net: wwan: MHI IP\_CTRL을 통해 AT ports에서 DTR/RTS 지원](https://lwn.net/Articles/1089024/)
Aug 16

Dawid Olesinski
[crypto: rockchip: RK356x/RK3588 cryptographic offloader 추가](https://lwn.net/Articles/1089028/)
Aug 16

Jan Carlo Roleda
[LTC3208 multi-display driver 지원 추가](https://lwn.net/Articles/1089216/)
Aug 17

Finn Thain
[block/swim: 수정 및 개선](https://lwn.net/Articles/1089218/)
Aug 17

Fan Gong
[net: hinic3: PF 초기화](https://lwn.net/Articles/1089219/)
Aug 17

Sai Krishna Musham
[pci: AMD: Versal2 CPM6 PCIe host controller 지원 추가](https://lwn.net/Articles/1089221/)
Aug 17

Ekansh Gupta
[accel/qda: Qualcomm DSP Accelerator driver](https://lwn.net/Articles/1089223/)
Aug 17

Kim Seer Paller
[AD5710R/AD5711R DAC 지원 추가](https://lwn.net/Articles/1089224/)
Aug 17

Christian Marangi
[net: dsa: Airoha AN8855 지원 추가](https://lwn.net/Articles/1089226/)
Aug 17

Pankaj Gupta
[firmware: imx: NXP secure-enclave용 driver](https://lwn.net/Articles/1089227/)
Aug 17

Sumit Kumar
[bus: mhi: loopback driver 추가](https://lwn.net/Articles/1089229/)
Aug 17

Stoyan Bogdanov
[TPS25990 direct conversions 재작업 및 TPS1689 지원 추가](https://lwn.net/Articles/1089230/)
Aug 17

Aiden Isik
[clk: samsung: Exynos5515 clock driver 지원 도입](https://lwn.net/Articles/1089231/)
Aug 17

Lakshay Piplani
[NXP P3H2x4x I3C hub driver 지원 추가](https://lwn.net/Articles/1089232/)
Aug 17

Peng Fan (OSS)
[clk: spread spectrum 지원 및 clk-scmi에서 사용](https://lwn.net/Articles/1089233/)
Aug 17

Jiaxing Hu
[accel/rocket: RK3576 NPU (RKNN) 활성화](https://lwn.net/Articles/1089235/)
Aug 17

Eliot Courtney
[gpu: nova-core: NVKV codec 추가](https://lwn.net/Articles/1089238/)
Aug 17

Harry Wentland
[amdgpu 및 VKMS에서 YUV conversion colorop](https://lwn.net/Articles/1089242/)
Aug 14

Krzysztof Karas
[drivers: i915/shmem을 iommu와 함께 사용할 때 large object allocations의 memory management 개선](https://lwn.net/Articles/1089243/)
Aug 17

Rupesh Majhi
[iio: pressure: dps310: FIFO 및 triggered buffer 지원](https://lwn.net/Articles/1089250/)
Aug 17

Prabhakar
[CPG/MSSR driver에서 Renesas RZ/T2H 및 RZ/N2H용 syscon 지원 추가](https://lwn.net/Articles/1089257/)
Aug 17

Dave Marquardt
[scsi: ibmvfc: ibmvfc가 FPIN messages를 지원하도록 변경](https://lwn.net/Articles/1089258/)
Aug 17

Sean Rhodes
[coreboot CFR firmware attributes](https://lwn.net/Articles/1089267/)
Aug 17

Swark Yang
[mailbox: Axiado AX3005 mailbox driver 추가](https://lwn.net/Articles/1089343/)
Aug 17

Amit Barzilai
[drm/ssd130x: Solomon SSD1351 OLED controller 지원 추가](https://lwn.net/Articles/1089346/)
Aug 18

Sreeshankar K
[Qualcomm SM7250 SoC 초기 지원 추가](https://lwn.net/Articles/1089347/)
Aug 18

Atharva Tiwari
[Apple T2 NHI Device links 추가](https://lwn.net/Articles/1089348/)
Aug 18

Grégoire Layet
[soc: aspeed: PCIe BMC device용 BMC 및 host driver 추가](https://lwn.net/Articles/1089351/)
Aug 18

Long Zhao
[Ambarella CV75 SoC 최소 bring-up](https://lwn.net/Articles/1089353/)
Aug 18

Markus Stockhausen
[net: mdio: realtek-rtl9300: RTL83xx 지원 추가](https://lwn.net/Articles/1089358/)
Aug 17

Geliang Tang
[nvme-tcp: IPv6 traffic class 지원 추가](https://lwn.net/Articles/1089360/)
Aug 18

Stefan Popa
[iio: adc: MAX40080 current-sense amplifier driver 추가](https://lwn.net/Articles/1089376/)
Aug 18

Priyank Rathod
[PCI/pcie: PCIe Lane Margining at Receiver (LMR) 지원 추가](https://lwn.net/Articles/1089380/)
Aug 18

illusion.wang
[Nebulamatrix NIC용 nbl driver](https://lwn.net/Articles/1089507/)
Aug 19

John Hubbard
[gpu: nova-core: r000 GSP firmware로 boot](https://lwn.net/Articles/1089508/)
Aug 18

Muralidhara M K
[platform/x86/amd/hsmp: Family 1Ah client 지원](https://lwn.net/Articles/1089511/)
Aug 19

Esben Haabendal
[io: accel: mma8452: open drain interrupt pin 구성 허용](https://lwn.net/Articles/1089512/)
Aug 19

Xing Loong
[tee: MbedTEE driver 추가](https://lwn.net/Articles/1089513/)
Aug 19

Atanas Filipov
[Qualcomm CAMNOC ICC provider 추가](https://lwn.net/Articles/1089514/)
Aug 19

Prabhakar
[Renesas RZ/T2H 및 RZ/N2H SoC용 RTC 지원 추가](https://lwn.net/Articles/1089518/)
Aug 19

Sascha Hauer
[media: verisilicon: RK3588 VPU720 JPEG decoder 추가](https://lwn.net/Articles/1089520/)
Aug 19

Himanshu Bhavani
[media: i2c: imx576 camera sensor driver 추가](https://lwn.net/Articles/1089522/)
Aug 19

Krishna Chaitanya Chundru
[bus: mhi: host: mhi bus bw 지원 추가](https://lwn.net/Articles/1089523/)
Aug 19

Raag Jadav
[drm\_ras에 error threshold 도입](https://lwn.net/Articles/1089526/)
Aug 18

Pardeep Kaur
[wifi: ath12k: TX 및 RX 관측성을 위한 device DP stats 확장](https://lwn.net/Articles/1089527/)
Aug 19

Thierry Chatard
[Dell Latitude 5285 2-in-1에서 cameras 활성화](https://lwn.net/Articles/1089532/)
Aug 19

Claudiu Beznea
[pinctrl: renesas: rzg2l: RZ/G3S I3C 지원 추가](https://lwn.net/Articles/1089534/)
Aug 19

### 디바이스 드라이버 인프라

#### 요약

- DRM panel, vblank, file private data와 Rust bindings의 기반 기능을 정비한다.[^c11-drm]
- driver core와 `fw_devlink`의 연계를 확장해 장치 의존성 처리를 개선한다.[^c11-fw-devlink]
- virtio device가 virtqueue memory를 직접 소유하도록 지원한다.[^c11-virtio]

Luca Ceresoli
[drm/panel: 모든 panel에 panel\_bridge 추가](https://lwn.net/Articles/1088953/)
Aug 14

Eliav Farber
[notifier: device-managed registration API 추가 및 drivers 변환](https://lwn.net/Articles/1089021/)
Aug 16

Lyude Paul
[drm/vblank: all-or-nothing vblank 지원 강제](https://lwn.net/Articles/1089003/)
Aug 14

Danilo Krummrich
[lifetime-parameterized DRM File private data](https://lwn.net/Articles/1089005/)
Aug 15

Albert Esteve
[rust: drm: panel bindings 추가](https://lwn.net/Articles/1089236/)
Aug 17

James Hilliard
[driver core, net: class devices 및 PHY packages를 위한 fw\_devlink 처리](https://lwn.net/Articles/1089345/)
Aug 18

Alexander Graf
[virtio: 자체 virtqueue memory를 소유하는 devices 지원](https://lwn.net/Articles/1089505/)
Aug 18

Gary Guo
[rust: io: register projections 지원 및 relative registers 제거](https://lwn.net/Articles/1089519/)
Aug 19

### 문서화

#### 요약

- Sphinx 문서 빌드의 사전 설치 dependency 검사를 개선한다.[^c11-sphinx]
- FUSE cache 동작을 문서화하고 테스트한다.[^c11-fuse]
- 문서 및 테스트 개선으로 파일시스템 기능의 사용성과 검증 가능성을 높인다.

Chen Miao
[docs: sphinx-pre-install: dependency checks 개선](https://lwn.net/Articles/1088721/)
Aug 13

Luis Henriques
[fuse: caches 문서화 및 테스트](https://lwn.net/Articles/1089240/)
Aug 17

### 파일시스템 및 블록 계층

#### 요약

- Ceph, ext4, XFS, NFS의 I/O 경로 및 metadata 처리 성능을 개선한다.[^c11-ceph][^c11-ext4][^c11-xfs][^c11-nfs]
- fs-verity, atomic multi-extent operation, zoned block device 처리를 확장한다.[^c11-fs-verity][^c11-zoned]
- BPF에 block cgroup I/O 통계를 노출하여 관측성을 강화한다.[^c11-bpf]

Max Kellermann
[fs/ceph: struct layouts 최적화](https://lwn.net/Articles/1088731/)
Aug 12

Zhang Yi
[ext4: regular file의 buffered I/O path에 iomap 사용](https://lwn.net/Articles/1088927/)
Aug 14

Andrey Albershteyn
[post EOF merkle tree를 사용하는 XFS용 fs-verity 지원](https://lwn.net/Articles/1088932/)
Aug 14

Damien Le Moal
[offline 및 read-only zones 처리 개선](https://lwn.net/Articles/1088933/)
Aug 14

Pranjal Shrivastava
[nfs: direct I/O path 현대화](https://lwn.net/Articles/1088954/)
Aug 14

NeilBrown
[negative dentry 문제의 쉬운 부분 수정](https://lwn.net/Articles/1089009/)
Aug 15

Tal Zussman
[ceph: writeback path를 folios로 변환](https://lwn.net/Articles/1089256/)
Aug 17

Ziyang Men
[block: blkcg io.stat을 BPF에 노출](https://lwn.net/Articles/1089264/)
Aug 17

Xiubo Li
[ceph: cephfs kclient에서 mdsc->mutex contention 감소](https://lwn.net/Articles/1089354/)
Aug 18

Dave Chinner
[XFS: rolling transactions를 통한 atomic multi-extent operations](https://lwn.net/Articles/1089525/)
Aug 19

### 메모리 관리

#### 요약

- large folio, HugeTLB, migration, reverse mapping의 확장성과 효율을 개선한다.[^c11-folio][^c11-hugetlb][^c11-rmap]
- zswap 및 swap의 저장 구조와 reclaim 동작을 정비한다.[^c11-zswap][^c11-swap]
- memcg, DAMON, BPF를 통해 메모리 계층별 제어와 관측성을 확장한다.[^c11-memcg][^c11-damon][^c11-bpf]

Kairui Song
[mm/huge\_memory: folio split 정리 및 swapcache split 제한 해제](https://lwn.net/Articles/1088722/)
Aug 13

Shivank Garg
[mm: large folio migration 중 rmap walks 일괄 처리](https://lwn.net/Articles/1088738/)
Aug 13

Baoquan He
[xswap: zswap이 뒷받침하는 확장 가능한 (virtual) swap device](https://lwn.net/Articles/1088749/)
Aug 13

Pengpeng Hou
[mm/slub: 이전 object lifetime 보존](https://lwn.net/Articles/1088799/)
Aug 14

Lorenzo Stoakes (ARM)
[mm/rmap: MAP\_PRIVATE file-backed folios를 anonymous pgoff로 index](https://lwn.net/Articles/1088801/)
Aug 13

Suren Baghdasaryan
[mm: unconditional per-VMA locks 및 정리](https://lwn.net/Articles/1088805/)
Aug 13

Jianyue Wu
[mm/zswap: fixed pool index를 통해 zswap\_entry 축소](https://lwn.net/Articles/1089012/)
Aug 15

Kunwu Chan
[mm/damon/perf: ARM SPE AUX backend 추가](https://lwn.net/Articles/1089025/)
Aug 16

Kiryl Shutsemau
[mm/collapse: migration primitives 기반으로 collapse 재구축](https://lwn.net/Articles/1089032/)
Aug 16

Usama Arif
[mm: anonymous THP용 PMD-level swap entries](https://lwn.net/Articles/1089355/)
Aug 18

liuqiqi@kylinos.cn
[mm/memcontrol: per-tier memory accounting 및 control 도입](https://lwn.net/Articles/1089342/)
Aug 18

Kunwu Chan
[mm/damon/perf: hardware-sampled access reports를 위한 observability framework](https://lwn.net/Articles/1089344/)
Aug 18

Alexandre Ghiti
[mm: zswap: cold writeback folios를 즉시 해제](https://lwn.net/Articles/1089378/)
Aug 18

Hui Zhu
[bpf: BPF 기반 proactive memcg reclaim](https://lwn.net/Articles/1089510/)
Aug 19

Muchun Song
[mm: HugeTLB용 section-based vmemmap optimization 도입](https://lwn.net/Articles/1089515/)
Aug 19

Barry Song (Xiaomi)
[mm: 더 작은 large folios에 lru cache 활성화](https://lwn.net/Articles/1089506/)
Aug 19

[^c11-driver]: **device driver**는 Linux kernel이 특정 하드웨어를 공통 subsystem 인터페이스로 제어하게 하는 구성 요소다.
[^c11-pcie]: **PCIe**는 고속 주변장치 연결을 위한 직렬 인터커넥트 규격이다.
[^c11-dma]: **DMA**는 CPU의 직접 복사 없이 장치와 memory 사이에서 데이터를 전송하는 방식이다.
[^c11-iommu]: **IOMMU**는 장치 DMA 주소 변환과 접근 격리를 제공한다.
[^c11-interrupt]: **interrupt**는 장치가 CPU에 비동기 이벤트 처리를 요청하는 신호다.
[^c11-drm]: **DRM**은 Linux kernel의 GPU·display 관리 subsystem이다.
[^c11-fw-devlink]: **fw_devlink**는 firmware가 기술한 장치 의존성을 kernel device links로 반영하는 메커니즘이다.
[^c11-virtio]: **virtio**는 가상화 환경의 표준화된 반가상화 I/O 장치 인터페이스다.
[^c11-sphinx]: **Sphinx**는 Linux kernel 문서에 사용되는 문서 빌드 시스템이다.
[^c11-fuse]: **FUSE**는 userspace 파일시스템 구현을 지원하는 kernel interface다.
[^c11-ceph]: **Ceph**는 분산 스토리지 시스템이며 CephFS는 그 파일시스템 인터페이스다.
[^c11-ext4]: **ext4**는 Linux에서 널리 사용하는 journaling 파일시스템이다.
[^c11-xfs]: **XFS**는 대용량 및 높은 병렬 I/O에 적합한 journaling 파일시스템이다.
[^c11-nfs]: **NFS**는 네트워크를 통해 파일시스템을 제공하는 프로토콜이다.
[^c11-fs-verity]: **fs-verity**는 읽기 전용 파일 내용의 무결성을 Merkle tree로 검증하는 Linux 기능이다.
[^c11-zoned]: **zoned block device**는 쓰기 순서와 영역 경계를 제약하는 저장장치 모델이다.
[^c11-bpf]: **BPF**는 안전하게 kernel 이벤트를 관찰하거나 program 가능한 동작을 수행하게 하는 runtime이다.
[^c11-folio]: **folio**는 Linux memory management에서 페이지 묶음을 표현하는 memory 단위다.
[^c11-hugetlb]: **HugeTLB**는 huge page를 명시적으로 관리하는 Linux memory 기능이다.
[^c11-rmap]: **reverse mapping (rmap)**은 physical memory가 매핑된 virtual address를 역으로 추적하는 기법이다.
[^c11-zswap]: **zswap**은 swap-out page를 압축해 RAM에 보관하는 kernel cache다.
[^c11-swap]: **swap**은 RAM이 부족할 때 memory page를 보조 저장장치로 내보내는 메커니즘이다.
[^c11-memcg]: **memcg**는 cgroup 단위의 memory 사용량 accounting과 제한을 제공한다.
[^c11-damon]: **DAMON**은 데이터 접근 패턴을 모니터링해 memory management를 돕는 kernel subsystem이다.

---

### 네트워킹

#### 요약

- 이 섹션은 Linux 네트워크 스택에서 BPF, packet pacing, neighbour discovery, `skb` metadata를 확장하는 제안을 다룬다.[^c12-bpf][^c12-pacing][^c12-neighbour][^c12-skb]
- `virtio_net`, NTB, netconsole, netfilter flowtable의 성능·오프로드·운영 기능을 개선한다.[^c12-virtio-net][^c12-ntb][^c12-netconsole][^c12-netfilter]
- Wi-Fi 수신 링크 결정과 상태 플래그 처리도 조정한다.

Mahe Tardy
[bpf\_ksock 도입](https://lwn.net/Articles/1088755/)
Aug 13

Willem de Bruijn
[hardware pacing offload](https://lwn.net/Articles/1088756/)
Aug 12

Kuniyuki Iwashima
[neighbour: arp\_tbl 및 nd\_tbl의 namespace화](https://lwn.net/Articles/1088757/)
Aug 13

Jakub Sitnicki
[BPF metadata를 위한 skb extension](https://lwn.net/Articles/1088935/)
Aug 14

Shahar Shitrit
[virtio\_net: ethtool flow rules 지원 추가](https://lwn.net/Articles/1089241/)
Aug 16

Koichiro Den
[net: ntb\_netdev: NTB 전반에서 checksum offload 보존](https://lwn.net/Articles/1089225/)
Aug 17

Breno Leitao
[netconsole: 메시지 rate limiting 지원](https://lwn.net/Articles/1089350/)
Aug 18

Pablo Neira Ayuso
[netfilter: flowtable: GC를 건너뛰기 위해 NF\_FLOW\_CONFIRMED bit 추가 및 사용](https://lwn.net/Articles/1089361/)
Aug 17

Benjamin Berg
[NO_STA flag 추가 및 RX link resolution 재작업](https://lwn.net/Articles/1089539/)
Aug 19

### 보안 관련

#### 요약

- Landlock, SELinux, audit, BPF loader 등 Linux 보안 경계를 강화하는 변경을 모은다.[^c12-landlock][^c12-selinux][^c12-audit]
- 메모리 보호 키와 page table hardening으로 메모리 격리를 강화한다.[^c12-pkeys][^c12-page-tables]
- 네트워크 packet의 security mark 저장 방식도 확장 가능한 인덱스로 전환한다.[^c12-secmark]

Günther Noack
[landlock: whiteout object 생성 제한](https://lwn.net/Articles/1088758/)
Aug 13

Thiébaud Weksteen
[bpf: LOADER\_LOAD\_FD 도입](https://lwn.net/Articles/1088736/)
Aug 13

Ricardo Robaina
[audit: SYSCALL record에 여섯 syscall argument 모두 기록](https://lwn.net/Articles/1088800/)
Aug 13

Casey Schaufler
[skb secmark를 x-array index로 변경](https://lwn.net/Articles/1088807/)
Aug 13

Kevin Brodsky
[pkeys 기반 page table hardening](https://lwn.net/Articles/1089381/)
Aug 18

Jann Horn
[proc, security, selinux: SELinux가 `/proc/self/mem`의 `FOLL_FORCE`를 차단하도록 허용](https://lwn.net/Articles/1089382/)
Aug 18

### 가상화 및 컨테이너

#### 요약

- KVM의 arm64, x86, RISC-V 지원을 확장하고 guest 안전성과 관측성을 개선한다.[^c12-kvm]
- TDX와 nested virtualization 경로에서 type confusion 및 service denial 위험을 줄이는 변경을 포함한다.[^c12-tdx][^c12-nsvm]
- pre-faulting, PMU Topdown metrics, GCS 같은 CPU·메모리 가상화 기능을 guest에 제공한다.[^c12-prefault][^c12-pmu][^c12-gcs]

Mark Brown
[KVM: arm64: guest를 위한 GCS 지원 제공](https://lwn.net/Articles/1088723/)
Aug 12

Sean Christopherson
[KVM: VMX: TDX vCPU를 `vcpu_vmx`로 해석하는 문제에 대한 방어 강화](https://lwn.net/Articles/1088960/)
Aug 14

Jinyu Tang
[KVM: riscv: KVM\_PRE\_FAULT\_MEMORY 지원 추가](https://lwn.net/Articles/1089016/)
Aug 15

Zide Chen
[KVM: x86/pmu: hardware Topdown metrics 지원 추가](https://lwn.net/Articles/1089255/)
Aug 17

Tina Zhang
[KVM: nSVM: nested guest에 DecodeAssists 활성화](https://lwn.net/Articles/1089509/)
Aug 19

Xiaoyao Li
[KVM: TDX: TDX용 VM-DoS Prevention Features 활성화](https://lwn.net/Articles/1089516/)
Aug 19

### 기타

#### 요약

- Rust ID 범위 예약, BPF hash map 메모리 절감 등 kernel 내부 자료구조와 runtime 효율을 개선한다.[^c12-kernel-ids][^c12-bpf-map]
- CPU isolation, cache-to-cache 분석, trace, branch history를 위한 성능 분석 도구의 기능을 확장한다.[^c12-cpu-isolation][^c12-perf][^c12-lttng][^c12-coresight]
- `iproute2` 릴리스도 포함되어 사용자 공간 네트워크 관리 도구의 최신 변경을 다룬다.[^c12-iproute2]

Eliot Courtney
[rust: ID 범위 예약 지원 추가](https://lwn.net/Articles/1088742/)
Aug 13

T.J. Mercier
[bpf: htab: hash map의 메모리 사용량 감소](https://lwn.net/Articles/1088734/)
Aug 12

Marco Crivellari
[cpunoise (CPU isolation 테스트 도구) v0.2](https://lwn.net/Articles/1089014/)
Aug 15

Jiebin Sun
[perf c2c: function view 추가](https://lwn.net/Articles/1089228/)
Aug 17

Mathieu Desnoyers
[LTTng-modules 2.15.3 및 2.14.7 (Linux kernel tracer)](https://lwn.net/Articles/1089246/)
Aug 17

Amir Ayupov
[perf: 기존 sample에 CoreSight branch history 추가](https://lwn.net/Articles/1089357/)
Aug 17

Stephen Hemminger
[iproute2 7.2 릴리스](https://lwn.net/Articles/1089359/)
Aug 17

**페이지 편집자**: Joe Brockmeier

[^c12-bpf]: BPF는 kernel 안에서 검증된 프로그램을 실행해 networking, tracing, security 기능을 확장하는 Linux 기술이다.
[^c12-pacing]: packet pacing은 packet 전송 시점을 조절하여 burst와 혼잡을 완화하는 기법이다.
[^c12-neighbour]: neighbour subsystem은 IPv4 ARP와 IPv6 Neighbor Discovery의 IP-to-link-layer 주소 해석을 관리한다.
[^c12-skb]: `skb` (`struct sk_buff`)는 Linux networking stack에서 packet 데이터를 표현하는 핵심 구조체다.
[^c12-virtio-net]: `virtio_net`은 virtio 기반 가상 네트워크 장치 driver다.
[^c12-ntb]: NTB(Non-Transparent Bridge)는 서로 다른 PCIe 도메인 간 통신을 제공한다.
[^c12-netconsole]: netconsole은 kernel log를 network를 통해 원격 호스트로 전송한다.
[^c12-netfilter]: netfilter는 packet filtering, NAT, connection tracking을 위한 Linux kernel framework다.
[^c12-landlock]: Landlock은 unprivileged process도 사용할 수 있는 Linux의 sandboxing LSM이다.
[^c12-selinux]: SELinux는 label 기반 mandatory access control을 제공하는 Linux Security Module이다.
[^c12-audit]: Linux audit subsystem은 보안 관련 system call 및 이벤트를 기록한다.
[^c12-secmark]: secmark는 packet에 부여되는 보안 label로, LSM 및 netfilter 정책에서 사용할 수 있다.
[^c12-pkeys]: protection keys(pkeys)는 page마다 access permission을 빠르게 전환할 수 있는 CPU memory-protection 기능이다.
[^c12-page-tables]: page table은 virtual address를 physical memory에 매핑하고 access permission을 적용한다.
[^c12-kvm]: KVM은 Linux kernel을 hypervisor로 동작하게 하는 kernel 기반 virtual machine 기술이다.
[^c12-tdx]: Intel TDX는 VM을 host와 다른 VM으로부터 격리하기 위한 confidential-computing 기술이다.
[^c12-nsvm]: nested SVM(nSVM)은 AMD SVM 환경에서 guest hypervisor를 실행하는 nested virtualization 기능이다.
[^c12-prefault]: pre-faulting은 실제 접근 전 memory mapping의 page fault를 미리 처리해 지연을 줄이는 기법이다.
[^c12-pmu]: PMU(Performance Monitoring Unit)는 CPU hardware performance event를 계수한다.
[^c12-gcs]: GCS(Guarded Control Stack)는 control-flow 공격 완화를 위한 Arm의 hardware control stack 기능이다.
[^c12-kernel-ids]: kernel ID allocator는 kernel object에 사용할 정수 ID를 안전하게 관리한다.
[^c12-bpf-map]: BPF map은 BPF program과 user space 사이 또는 BPF program 간에 상태를 공유하는 자료구조다.
[^c12-cpu-isolation]: CPU isolation은 특정 CPU에서 scheduler work와 interrupt를 배제해 예측 가능한 실행을 확보하는 구성이다.
[^c12-perf]: `perf`는 Linux의 performance profiling 및 event analysis 도구다.
[^c12-lttng]: LTTng은 낮은 오버헤드로 Linux kernel과 user space event를 추적하는 tracing framework다.
[^c12-coresight]: CoreSight는 Arm platform의 hardware trace 및 debug architecture다.
[^c12-iproute2]: `iproute2`는 `ip`, `tc` 등을 제공하는 Linux user-space networking administration suite다.

## 보고서 기술 배경 각주

[^report-debian]: 배포판 거버넌스는 코드만이 아니라 기여·리뷰·문서화의 신뢰 경계를 정한다. LLM 정책은 생성물의 출처, 라이선스, 책임 소재를 운영 규칙으로 명확히 하는 문제다.
[^report-pathlib]: 파일 경로는 운영체제·상대 경로·심볼릭 링크에 따라 문자열 결합이 쉽게 깨진다. 객체 API는 조합과 정규화를 분리해 이식성 오류를 줄인다.
[^report-bootstrap]: 컴파일러가 자기 자신을 빌드하는 순환은 악성 초기 바이너리를 검증하기 어렵게 만든다. 작은 auditable seed는 이 신뢰 사슬을 독립적으로 재구성할 수 있게 한다.
[^report-kernel]: kernel ABI와 VM 메모리 구조, eBPF 검증은 사용자 공간 호환성·성능·공격 표면을 함께 바꾼다. 따라서 새 기능은 stable backport와 실제 워크로드 시험까지 포함해야 한다.
[^report-security]: 하드웨어 메모리 컨트롤러와 펌웨어는 OS보다 낮은 신뢰 계층이다. kernel privilege 요구가 있어도 권한 획득 이후의 영향 범위를 줄이는 방어와 업데이트가 필요하다.
[^report-patches]: 주간 패치 흐름은 아직 릴리스되지 않은 변경을 포함한다. 운영 적용 전에는 해당 stable 릴리스, 배포판 backport, 의존 드라이버의 지원 상태를 확인해야 한다.
