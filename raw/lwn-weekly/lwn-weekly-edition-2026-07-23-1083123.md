# LWN.net Weekly Edition for July 23, 2026 한국어 번역

- 원문: https://lwn.net/Articles/1083123/bigpage
- 선택 기준: 최신 Weekly Edition인 2026-07-30호(article_id 1084315)는 최신/유료 가능성이 있어 건너뛰고, 직전 무료 공개판으로 접근 확인된 2026-07-23호(article_id 1083123)를 번역했습니다.
- 생성시각: 2026-07-31T09:47:49+09:00
- 원문 SHA-256: `6b5561bc0bcd207cdc9cc71aae96b925427ae01581f6c5fb6ed764d4d6052bbc`
- 번역 경로: 공개 bigpage 추출 후 Google/deep-translator 기반 markdown 보존 fallback으로 전체 한국어 번역을 생성했습니다. 유료·로그인 전용 콘텐츠는 우회하지 않았습니다.

## 전체 요약

- 이번 호는 Linux kernel community의 LLM 사용 논쟁, GNOME save/restore, Fedora change process, BPF tracing/security, famfs, sched_ext 등 커널·데스크톱·배포판 개발 흐름을 함께 다룹니다.
- BPF LSM tamper 방어, 여러 tracepoint attachment, famfs 병합 논의, sched_ext sub-scheduler/proxy execution은 Linux runtime과 security boundary가 어떻게 확장되는지 보여 줍니다.
- PyPI 업로드 정책, XZ backdoor 관련 서적, GNOME 보안 추적, 배포판 보안 업데이트는 공급망 보안과 ecosystem governance의 실무적 중요성을 강조합니다.
- 보안 업데이트 표와 커널 패치 목록은 추적성을 위해 advisory ID, 패키지명, 링크, 버전 문자열을 원문 중심으로 보존했습니다.
- 각 주요 기사에는 3개 이상의 요약 bullet을 추가했고, 중요한 기술 문단에는 footnote로 배경·중요성·운영 함의를 덧붙였습니다.

### [Welcome to the LWN.net Weekly Edition for July 23, 2026](https://lwn.net/Articles/1084225/)

#### 요약
- 이번 호의 주요 내부 섹션을 종합적으로 정리합니다.
- 보안, 보드 개발, 배포판, 개발 도구, 스토리지, 전력 관리 문제를 함께 소개합니다.
- 각 기사와 공지의 원문 링크를 유지해 추가 확인이 가능하도록 했습니다.

이 버전에는 다음과 같은 기능 콘텐츠가 포함되어 있습니다.
- [Debating the role of large language models in the kernel community](https://lwn.net/Articles/1083275/): 커널 LLM 논의는 많은 사람들이 생각하는 것보다 더 미묘했습니다.[^lwn1083123-llm-kernel-community]
- [Save and restore may be coming to GNOME](https://lwn.net/Articles/1083750/): Wayland의 GNOME에 많이 놓친 X11 기능을 제공하기 위해 여러 부분이 함께 모이고 있습니다.[^lwn1083123-gnome-session-restore]
- [Fedora grapples with change](https://lwn.net/Articles/1081557/): 배포 및 프로젝트 변경 관리에 대한 Fedora의 지속적인 논의를 살펴봅니다.[^lwn1083123-fedora-change-process]
- [the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit](https://lwn.net/Articles/lsfmmbpf2026/)의 추가 적용 범위:
- [Sched-ext: enqueue() for sub-schedulers and proxy-execution support](https://lwn.net/Articles/1082717/): sched_ext 하위 시스템에서 진행이 계속됩니다.

이번 주 버전에는 다음 내부 페이지도 포함되어 있습니다.

- [Brief items](https://lwn.net/Articles/1083125/): 커뮤니티 전체의 간략한 뉴스 항목입니다.
- [Announcements](https://lwn.net/Articles/1083126/): 뉴스레터, 컨퍼런스, 보안 업데이트, 패치 등.[^lwn1083123-security-updates]

이번주도 재미있게 즐겨주시고, 언제나처럼 감사드립니다.
                       LWN.net을 지원합니다.

[Comments (none posted)](https://lwn.net/Articles/1084225/#Comments)


### [Debating the role of large language models in the kernel community](https://lwn.net/Articles/1083275/)

#### 요약
- Linux 커널 커뮤니티에서 LLM을 어떻게 사용하는지에 대한 사회적·기술적 논쟁을 다뤄보세요.
- 자동 생성 패치의 출처, 책임을 지고, 파괴하는 것을 유지하기 위해 유지 관리 모델과 충돌하는 목적을 설명합니다.
- AI 기관 개발을 고신뢰 코드 베이스에 적용할 때 필요한 기준과 적절하게 정리합니다.

작성자:
조나단 코벳
2026년 7월 21일
많은 개발 커뮤니티와 마찬가지로 커널 커뮤니티도 어려움을 겪고 있습니다.
개발에 얼마나 큰 언어 모델(LLM)이 사용될 것인지 결정하기 위해
프로세스.  최근 뉴스는 강렬한 표현의 서신으로 가득 차 있습니다.
이 주제에 대해서는 Linus Torvalds의 글이 있지만 논의는 좀 더 많이 이루어졌습니다.
그것보다 광범위하고 미묘한 차이가 있습니다.  고려한 주제
최근에는 LLM 속성 요구 사항, 코드 검토 도구,
독점 도구에 대한 의존성과 우려할 부분이 있는지 여부
LLMs.[^lwn1083123-kernel-community]의 윤리에 대해
중간 광고

#### 지원 재검토

LLM 생성 코드에 관한 커널 커뮤니티의 지침은 [added to the kernel](https://git.kernel.org/linus/78d979db6cef)이었습니다.
Linux에서 오랜 논의 끝에 2025년 말 7.0 릴리스 예정
재단의 기술 자문 위원회(TAB) 및 메일링 리스트에 있습니다.  는
[`coding-assistants.rst`](https://docs.kernel.org/process/coding-assistants.html)
파일에는 코드 제출이 부분적으로 또는 전체적으로 완료되었을 때 다음과 같은 내용이 나와 있습니다.
LLM에 의해 생성된 패치에는 이 부분에 Assisted-by 태그가 있어야 합니다.
형식:


```

지원자: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]
```

이 태그의 목적은 LLM 사용을 문서화하고 경고하는 것이었습니다.
그 사실에 대한 검토자와 유지관리자.  의 이름도 포함되어 있습니다.
사용되는 특정 도구.  해당 정보는 다음과 같은 경우에 잠재적으로 유용하다고 간주되었습니다.
특정 LLM이 특정 버그에 대한 경향이 있는 것으로 밝혀지거나 결국
저작권 관련 문제가 있는 경우 개발자가 다음을 수행할 수 있게 해줄 것입니다.
문제가 있는 모델에 의해 생성된 패치를 검토하고 가능하면 수정하거나
제거하십시오.

Since then, this tag has not won over all developers.  7.2-rc4부터
1,200개의 커밋에는 Assisted-by 태그가 있습니다.  그러나 분명히
significant stream of machine-generated patches that do not carry that tag;
sometimes that is a result of ignorance of the rules, but other times the
origin of the code is, seemingly, being deliberately obscured.  로서
result, the tag's usefulness as an indicator of LLM involvement is unclear
기껏해야.  Meanwhile, some developers see placing the names of specific LLMs
into the kernel's development history as a form of advertising.  모두들, 많은 사람들이 말했다
태그가 어떤 가치를 추가하는지 궁금합니다.

이 논의는 크리스천이 7월 초에 전면에 등장했습니다.
브라우너 [suggested](https://lwn.net/ml/all/20260701-work-coding-assistants-v1-1-a20a94d1d606@kernel.org)
태그를 제거하거나 적어도 특정 모델의 이름을 제거하십시오.
사용:

> 나는 내 입장이 훨씬 더 급진적이라는 것을 인정합니다.
> 공개 요구 사항을 완전히 중지하면 됩니다. 그것은
> 쓸모없는 임호.  우리는 이미 핵심 기여자 외에 다른 것을 확인했습니다.
> 대부분의 사람들은 신경 쓰지 않으며 자신의 사용법을 공개하지 않습니다.
> AI. 나는 이것이 완전히 무의미하고 더 나쁜 것이라고 생각합니다.
> 법적 지위도 정의되지 않았습니다. 최근 사건과는 다르지만
> 지구 표면에서 특정 모델을 끌어당겨 이것을 만들었습니다.
> 덜 걱정스럽습니다.
> 하지만 좋습니다. 이 작업을 수행하려면 그냥 간단하게 처리하면 됩니다.
> 어시스트: LLM

Jeff Layton은 나중에 [a separate
patch](https://lwn.net/ml/all/20260702-aidoc-v1-1-735572dfb995@kernel.org)을 통해 저작자 표시 요구 사항을 완전히 제거했습니다.  일부 개발자
분명히 그것에 찬성했습니다. 네트워킹 관리자 Jakub Kicinski [let it be known](https://lwn.net/ml/all/20260701115302.29c66401@kernel.org)
그는 단순히 자신이 적용한 패치에서 해당 태그를 제거합니다.
TAB와 커뮤니티가 내린 이전 결정을 훼손합니다.
다른 사람들은 그런 조치를 취하지 않았지만 태그에 대한 애정을 거의 표현하지 않았습니다.[^lwn1083123-networking]

하지만 이 기능을 계속 사용하고 싶어하는 개발자가 있습니다.  그렉
Kroah-Hartman [described](https://lwn.net/ml/all/2026070224-unholy-commode-cf45@gregkh)으로
패치 생성에 LLM이 관여했다는 신호와
결과를 좀 더 자세히 검토해야 합니다.  로렌조 스토크스 [characterized](https://lwn.net/ml/all/akYz2aMIco1fbD-t@lucifer) 현재
정책은 "유지관리자에게 반발할 수 있는 권한을 부여하는 것"입니다.  이
파견단은 지원 요건이 계속 유지되기를 원합니다.
가능하다면 더 나은 시행이 필요할 수도 있습니다.

결국 태그를 유지하는 데 충분한 지원이 있었던 것으로 나타났습니다.
완전한 제거를 막았지만 누구도 요구하는 것을 방어할 의사가 없었습니다.
사용된 특정 도구를 공개합니다.  그래서 합의는 *생각* 것 같았습니다
Brauner의 초기 제안을 따르는 것이 좋습니다.
변경 로그.  하지만 새로운 개정판은 아직 나오지 않았으며 아마도 그럴 수도 있습니다.
이 정책에 대한 최종 결정은 유지 관리 담당자가 완료할 때까지 내려지지 않습니다.
10월 정상회담.


#### 의존성과 지속가능성

코드 작성을 위해 LLM을 사용하는 비율이 확실히 증가하고 있는 반면,
커뮤니티에서 LLM은 여전히 패치 검토에 훨씬 더 널리 사용됩니다.
그들의 창조보다는  특히 [Sashiko
review tool](https://lwn.net/Articles/1064830/)은 많은 기업에서 광범위하게 채택되었습니다.
하위 시스템 및 유지 관리 담당자는 점점 더 개발자가
그것이 방출하는 리뷰.  그러나 이러한 도구는 사용자의 의지에 크게 의존합니다.
기업이 사용 자금을 조달하기 때문에 몇 가지 우려 사항이 발생합니다.
그 관대함은 앞으로도 계속될 것이며, 지역사회도 그렇게 될 것인가?
미래의 러그풀로 인해 상당한 피해를 입을 수 있는 도구에 의존
개발 과정?

Sashiko의 가장 활발한 개발자인 Roman Gushchin이 이를 제기했습니다.
그의 [proposal](https://lwn.net/ml/all/7ia4qzl45h20.fsf@castle.c.googlers.com)에 대한 우려는 다음과 같습니다.
유지관리자 서밋 토론:

> 여러 커널 엔지니어와 유지관리자가 정당하게 표현했습니다.
> 단일 회사가 제공하는 인프라에 의존하는 것에 대한 우려
> 명확한 공식 보증이 없는 회사. 그것은 좋을 것입니다
> 보다 지속 가능한 모델이 현실적으로 어떤 모습일 수 있는지 논의합니다.
> 그리고 우리가 거기에 어떻게 갈 수 있는지.

또한 커뮤니티에 [brought this
issue up](https://lwn.net/ml/all/87wluv7yzc.fsf@trenco.lwn.net)이 두 번 이상 있습니다.  20년 전,
BitKeeper에 대한 커뮤니티의 의존은 해당 비트키퍼에 액세스할 때 큰 충격을 가져왔습니다.
독점 도구 [was suddenly withdrawn](https://lwn.net/Articles/130746/).
다른 독점 도구에 의존하면 이제 비슷한 충격을 받을 위험이 있습니다.
커뮤니티가 Torvalds의 생성에 의존하지 못할 수도 있습니다.
긴 주말 동안 교체.

이 질문에 대한 많은 답변은 다음과 같은 생각에 기반을 두고 있습니다.
LLM 기반 도구는 커뮤니티의 생산성을 높이는 데 도움이 됩니다.
그들에게 의존하게 될 위험이 있습니다.  Sasha Levin(예: [said](https://lwn.net/ml/all/alo3tBAc_tBNgtg0@laps)): "AI가 갑자기 사라지면
내일은 형편없겠지만, 다시 도구 작성으로 돌아가겠습니다.
예전처럼 수동으로요."  하지만 해당 이메일의 앞부분은
읽기:

> 지난 1~2년 동안 나는 내 추악한 글 대부분을 다시 쓸 수 있었습니다.
> 스크립트를 사용하면 수동으로 수행했던 수많은 프로세스를 자동화할 수 있습니다.
> AI 덕분에 수많은 삶의 질 항목이 향상됩니다. 봐
> 작년에 만들어진 CVE 프로세스에서도:
> 이를 구동하는 데 사용되는 인프라는 AI로 만들어졌습니다.

아니면 전혀 다른 방식으로 [the words of another
long-time kernel developer](https://lwn.net/ml/all/alltqTAwLLMcJfzG@dread), Dave Chinner를 생각해 보세요.
대화:

> 나는 LLM을 배울 필요가 없을 만큼 잘 운전하는 방법을 배웠습니다.
> 더 이상 코드를 작성하지 마세요. LLM은 내 코드 편집기 역할을 합니다.
> 매우 멋진 DWIM 예측 텍스트 삽입이 가능합니다. 에 대한
> 코드를 입력하는 과정을 싫어하는 사람, 이것은
> 계시.

그런 단어를 쓴 사람은 이러한 도구에 의존하지 않을 수도 있지만,
그럼에도 불구하고 그들은 LLM 기반 도구에 중요한 역할을 부여했습니다.
그들은 일을 끝냅니다.

Sashiko의 Ted Ts'o [said](https://lwn.net/ml/all/allGeaXQ6DFv1M14@mit.edu)
인간 검토자가 알아차리지 못할 수도 있는 문제를 찾아냅니다.
사람의 검토 대신: "나는 검토자가 이 작업을 중단하면
우리는 상처받은 세상에 있을 것이다."  그는 또한 다른 [said](https://lwn.net/ml/all/alfBvhZkAelq5RVf@mit.edu)
"사시코에 관해 저를 정말 흥분시키는 것 중 하나는
업무량을 줄여준다는 것입니다."  유지관리자가 어떻게 대응할 것인가?
장기적으로 LLM 기반 검토는 아직 남아 있지만 거의
워크로드 감소의 이점을 활용하고 중단할 것이라고 확신합니다.
Sashiko와 같은 도구가 발견하는 경향이 있는 문제를 찾고 있습니다.
어쨌든.  그런 일을 하는 데 필요한 기술이 있다고 상상하기는 어렵습니다.
그러한 시나리오에서는 장기적으로 검토가 위축되지 않습니다.

LLM 기반 검토 도구를 장기적으로 사용한다면 이러한 도구가 손실될 수 있습니다.
기술은 낮은 수준의 조립 기술을 잃는 것보다 더 비극적이지 않을 수 있습니다.
더 이상 필요하지 않으며 인간은 더 많은 것에 집중할 수 있습니다.
전략적이고 장기적인 유지 관리 문제.  하지만 이러한 검토 도구가 있다면
LLM 산업 뒤에 있는 돈의 통로가 수축되면서 사라지고,
개발 커뮤니티에서는 기술 손실을 후회하게 될 수도 있습니다.
컴파일러는 우리에게서 빼앗길 수 없습니다. 대규모 데이터 센터 기반 LLM
수 있습니다.  도구가 완전히 사라지지는 않더라도
돈을 지불할 수 있는 대기업에 근무하지 않는 개발자는 이용할 수 없습니다.
사용에 대한 청구서.

Sashiko와 같은 도구를 실행하는 방법을 모색하는 일부 개발자가 있습니다.
개방형 모델을 사용하여 로컬로; [Mauro Carvalho Chehab](https://lwn.net/ml/all/20260719110103.04896f34@foz.lan)
[Takashi Iwai](https://lwn.net/ml/all/87o6g4sl6k.wl-tiwai@suse.de)에는
그런 노력을 언급했다.  이와이에 따르면 아직 결과는 나오지 않았다.
동일: "예, 확실히 많은 오탐이 있습니다.
항상 최근 변경 사항을 따르십시오.  또한 그들은보다 훨씬 적은 변화를 다루고 있습니다.
사시코."  그러나 아마도 이러한 노력은 시간이 지남에 따라 진전을 이룰 것입니다.
회사가 제공하는 자원에 대한 의존도를 줄입니다.


#### 사시코가 보낸 이메일

기여자는 어느 정도까지 또는 최소한
상호 작용 - LLM 기반 도구?  5월에 열린 [2026 Media
Summit](https://lwn.net/ml/all/40b6589d-ef42-48d0-9853-341dc196fd18@kernel.org/)에서는 미디어 패치에 Sashiko를 사용하는 방법이 논의되었습니다.
해당 토론의 결과 중 일부는 [this email from Chehab](https://lwn.net/ml/all/20260710083845.23c753ca@foz.lan)에서 볼 수 있습니다.
(미디어 하위 시스템의 관리자)는 별도의 이메일을
Sashiko 이메일을 수신하여 기본 이메일에서 제외되도록 목록이 설정되었습니다.
미디어 메일링 리스트.  개인의 욕심도 있다고 하더군요.
기여자는 Sashiko 리뷰 수신을 거부할 수 있습니다.
패치.  그로 인해 꽤 긴 논의가 이어졌습니다.

구쉬친 [responded](https://lwn.net/ml/all/87wlv2jq4t.fsf@linux.dev)
거부 기능은 이상한 요청처럼 보였습니다.
단위 테스트를 거부합니다.  Chehab [agreed](https://lwn.net/ml/all/20260713095538.3d5e86f1@foz.lan)과 함께 이렇게 말했습니다.
그 커뮤니티 에티켓은 항상 답글에 작성자를 따라하는 것을 요구했습니다.
하지만 커뮤니티에는 사물을 다르게 보는 구성원이 있습니다.
로랑 핀차트 [answered](https://lwn.net/ml/all/20260713094120.GD1127719@killaraus.ideasonboard.com/)
그 에티켓은 누군가에게 가입하기 전에 명시적인 요청을 요구했습니다.
새로운 메일링 리스트를 위해.  Gushchin [asked](https://lwn.net/ml/all/7ia4mrvtrxjl.fsf@castle.c.googlers.com) 여부
Sashiko가 발견한 "중요한 문제"라도
패치 작성자, Pinchart [responded](https://lwn.net/ml/all/20260715005909.GF1656185@killaraus.ideasonboard.com):
"사시코 리뷰에 따라 작업을 수행하려는 관리자는 분류하고
작성자를 괴롭히기 전에 먼저 확인하세요."

유지관리자가 검토를 기대한다는 생각은 타당하다고 말할 수 있습니다.
기고자에게 보내기 전 Sashiko의 리뷰가 전부가 아니었습니다.
유지관리자에게 인기가 있습니다.  Ts'o [refused](https://lwn.net/ml/all/alcBvuIMEGSjAD1R@mit.edu) 그 의무를 다하고 말했습니다.
대신 그는 기여자들로부터 패치를 받아들일 필요가 없다고 생각합니다.
Sashiko 리뷰를 보는 것을 거부하십시오.  이호르 솔로드라이 [said](https://lwn.net/ml/all/00a244f8-5be6-4ee7-b5b1-e4cbdcd4fc77@linux.dev)
병합될 수 있을 만큼 좋은 패치를 만드는 것이 기여자의 임무입니다.
현재 환경에서는 다음을 통해 발견된 버그를 해결하는 것이 포함됩니다.
LLM 기반 도구.  구쉬친 [pointed out](https://lwn.net/ml/all/7ia47bmw0xls.fsf@castle.c.googlers.com) 그
공격자는 기여자가 이를 거부하더라도 이러한 도구를 사용하고 있습니다.  제임스
바텀리 [added](https://lwn.net/ml/all/460bb8002edc009194dcc0ad68a0538e5df6bfb5.camel@HansenPartnership.com)
"기고자는 관리자가 도구를 승인할 수 없습니다.
패치를 평가하고 적용하는 데 사용됩니다."

그러나 Pinchart는 [saying](https://lwn.net/ml/all/20260715174138.GI1778116@killaraus.ideasonboard.com)을 밀어냈습니다.
유지관리자가 이러한 도구에 대한 변경을 강요하고 있기 때문에
대신 도구를 통해 절약되는 시간을 사용하여 리뷰를 분류하도록 하세요.
Sashiko와의 거래를 요구하기 위해 그는 [said](https://lwn.net/ml/all/20260715163921.GH1778116@killaraus.ideasonboard.com/),
"기여자들이 자신의 가치를 지속적으로 정당화하도록 강요하는 것입니다.
무시할 수 없을 만큼의 양을 생산하는 것으로 알려진 기계
말도 안돼."  LLM의 확인되지 않은 리뷰에 응답해야 하는 그는 [said](https://lwn.net/ml/all/20260715161111.GC1778116@killaraus.ideasonboard.com),
유지관리자가 LLM 생성 패치를 강제로 읽어야 하는 것과 같습니다.
확인하지 않은 기여자로부터.  그는 또한 기계 생성 전송에 관한 Media-Summit 토론에서 [referred
back](https://lwn.net/ml/all/20260715190654.GK1778116@killaraus.ideasonboard.com)을 사용했습니다.
신규 개발자를 위한 리뷰:

> 이는 오탐지 및
> 주니어 개발자에 대한 다른 환각. 그들은 최고를 가질 수도 있습니다
> 작업의 맥락에 따라 다르지만 그렇지 않을 위험도 가장 높습니다.
> 리뷰의 타당성에 의문을 제기합니다.

다수의 개발자(포함)가 제기한 관련 우려 사항
Gushchin은 유지관리자 정상회의 제안에서 다음과 같이 말했습니다.
기존 문제.  Sashiko는 패치를 검토하면서 다음과 같은 버그도 발견합니다.
변경되는 코드에 이미 존재합니다.  놀랍게도 그럴 것 같다.
현재 커널 코드 베이스에는 여전히 오류가 부족하지 않습니다.  아무도
이러한 버그는 보고되어서는 안 된다고 생각하는 것 같지만, 많은 사람들은 이를 보고하는 것으로 생각합니다.
검토 중인 패치 개발자가 할 필요가 없는 소음
일하다.  개발자가 다 고쳐주면 정말 좋을 것 같아요.
그러나 일반적으로 요구하는 것은 합리적이지 않은 것으로 간주됩니다.
개발자는 추가 작업을 수행해야 합니다.

토발즈 [noted](https://lwn.net/ml/all/CAHk-=wjCcHUr=-Ycsey0khWnn68O6D=ZN-bE+8Sq4NetXpFuPA@mail.gmail.com),
일부 관리자는 기여자가 관련 없는 문제를 해결하기를 기대하는 경향이 있습니다.
과거에는 문제가 골칫거리였습니다.  작동하지 않습니다.
LLM이 발견한 버그도 처리하지 마세요.  그는 다소 눈을 뜨고 있었다
아마도 LLM이 최소한 자체 수정 사항을 만들 수 있다는 제안입니다.
이러한 버그 중 일부를 제거하고 자체 패치 트리를 유지합니다.  "그럴 거야.
패치 검토를 수행하는 것만으로도 명백한 '다음 단계'인 것 같습니다. 사소한
AI가 높은 신뢰도를 갖고 있고 우리도 높은 신뢰를 갖고 있는 패치입니다.
AI를 운영하는 그룹".
그 아이디어에 대한 즉각적인 지지는 없었다.  대신,
개발자들은 주로 어떻게든 별도의 목록을 유지하려고 노력하는 것에 대해 이야기했습니다.
누군가가 할 시간이 있을 때 주의가 필요한 기존 버그
그래서.


#### 포크와 윤리

미디어 토론으로 돌아가기; Gushchin에는 [responded](https://lwn.net/ml/all/4928C919-7999-4E76-ADCB-F8643FED105B@linux.dev)이 있었습니다.
개발자별 선택 해제 기능에 대한 요청에 다음을 설명하여
"일반적으로 매우 반 LLM 입장"이라고 요청하는 것과
유지관리자를 돕는 목적을 무너뜨릴 것입니다.  이로 인해 [the
Torvalds response](https://lwn.net/ml/all/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com)이 전 세계에 보고되었습니다.

> Linux는 AI 반대 프로젝트 중 하나가 아니며 누군가가
> 그 문제는 오픈 소스 작업을 수행하고 포크할 수 있다는 것입니다.
> 아니면 그냥 걸어가세요.
> AI는 우리가 사용하는 다른 도구와 마찬가지로 도구입니다.  그리고 그것은 분명히
> 유용한 것.

류드 폴의 [response](https://lwn.net/ml/all/3a5d891b536588e8e4fc84d60a5c8af72091d852.camel@redhat.com)
to Torvalds is worth reading in its entirety.  그녀는 많은 것을 지적한다.
개발자는 급여가 필요하며 포크할 수 있는 위치에 있지 않습니다.
the kernel or to walk away from it.  Developers are currently under heavy
LLM 기반 도구를 사용하라는 압력으로 인해 교육의 품질이 저하됩니다.
생성된 코드:

> 우리 고용주 중 다수는 명시적으로 이러한 조치를 강요하려고 합니다.
> 기대되는 결과가 마법같은 10배인 사람들을 위한 도구
> 감독과 양립할 수 없는 생산성 향상. 그것은
> 많은 직장에서 관념을 던지는 핑계로 사용됩니다.
> 창밖으로 실제 리뷰나 코드 품질을 확인합니다. 우리가 지내는 동안
> 커널에서 이미 수십 년 동안 slop을 처리해 왔습니다. 제 생각에는
> 극적으로 낮추는 도구라는 점을 지적하는 것은 매우 가치 있는 일입니다.
> 엄청난 양의 스니프 테스트 통과를 생성하는 데 필요한 막대
> slop은 사실 다른 도구와는 다릅니다.

커널의 품질을 유지하기 위해 노력하는 개발자를 위한
Paul은 커널 내에서 LLM 사용에 대한 지침이 유일한 지침일 수 있다고 말했습니다.
개발자가 고용주에게 안전하게 반발해야 하는 도구입니다.

고용주의 이러한 압력은 틀림없이 다음과 같은 결과를 가져왔습니다.
많은 개발자들은 그 사용에 대해 공개적으로 논쟁하기를 꺼려합니다.
핀차트는 그렇게 하려는 몇 안 되는 사람 중 한 명입니다.  그는 주제에 대해 [made his
position clear](https://lwn.net/ml/all/20260715185141.GJ1778116@killaraus.ideasonboard.com): "오늘은 그런 일이 없다고 생각합니다.
FOSS에서 생성 AI 사용에 대한 윤리적 정당성
개발".  Torvalds는 다음과 같은 논의에 신속하게 [shut
down](https://lwn.net/ml/all/CAHk-=wi7KN9_DYdmaE2chC92EhTrO=Wtx1bPBER-EQfAZ8FREg@mail.gmail.com)을 했습니다. "그러므로 윤리를 어디에 두십시오.
그들은 당신의 개인적인 삶에 속합니다. 윤리를 강요하려고 하지 마세요.
다른 사람 ".

이 입장은 잠시 생각해 볼 가치가 있습니다.  개발자는
기회가 주어지면 이러한 도구에 대한 여러 가지 윤리적 의혹을 설명하십시오.
그들은 저작권을 무시하기로 한 업계의 결정과
LLM 출력이 저작권을 위반할 가능성이 있습니다.  그들은 다음을 언급할 수도 있습니다.
막대한 기가와트의 컴퓨팅 성능에 대한 환경 비용이 발생하고 있습니다.
이러한 모델을 향하여 또는 데이터 센터 건설이
주변의 커뮤니티.  개발자는 이러한 문제가 어떻게 발생하는지에 대해 우려를 표명할 수 있습니다.
모델은 과두제에 의해 통제되거나 시스템적 경제적 위험에 대해 통제됩니다.
이는 경제의 막대한 부분이 이 산업으로 유입되고 있기 때문입니다.
그들은 잠시 시간을 내어 웹사이트 운영자에게 애도를 표할 수도 있습니다.
봇 네트워크에 의한 스크래핑 문제로 어려움을 겪고 있습니다.

이러한 우려 사항에 대해 동의(또는 관심) 여부와 관계없이
그들이 존재하는지 의심해 보세요.  그러나 Torvalds에 따르면 그 전체 논의는
출입금지입니다. 문제에 대해 이야기할 수 있는 유일한 측면은
"기술적 이유" 및 도구가 유용한지 여부.  분명히,
커널 커뮤니티는 이러한 문제를 해결할 수 있는 위치에 있지 않습니다.  그것은
또한 커뮤니티에서는 이러한 도구가 존재하지 않는 척할 수 없다는 점도 분명합니다.
그러나 커뮤니티에서도 LLM과 관련된 윤리적 문제가 있는 척할 수 없습니다.
적어도 소외될 위험이 없지는 않습니다.
이런 것에 관심을 갖고 있는 개발자들입니다.

이 지나치게 긴 글을 끝까지 읽어본 사람이라면 누구나 그럴 것이다.
인식된 지 오래되었으므로 사용에 관해 많은 미결 질문이 있습니다.
커널 커뮤니티의 LLM 기술.  많은 개발자와 유지관리자
분명히 그러한 사용을 상당히 지지하고 있으며, 그 역할이 분명한 것 같습니다.
커널 개발 분야의 LLM이 늘어날 예정입니다.  이 커뮤니티는 혼란스러워졌습니다
그 방향에 관해 수년에 걸쳐 수많은 논쟁을 거쳐, 그렇습니다.
그 윤리.  그 결과 일반적으로 더 강력하고 더 큰 커뮤니티가 탄생했습니다.
앞으로.  커뮤니티가 그러한 종류에 도달할 수 있는 방법을 찾을 수 있기를 바랍니다.
이번에도 결과가 나왔다.

[Comments (132 posted)](https://lwn.net/Articles/1083275/#Comments)


### [Save and restore may be coming to GNOME](https://lwn.net/Articles/1083750/)

#### 요약
- GNOME 데스크톱에서 세션 저장/복원 기능이 추가 가능성이 있는 프로젝트를 소개합니다.
- 기존 상태 복원, 컴포지터/툴킷 통합, 사용자 환경 간의 균형을 설명합니다.
- 방해받지 않고 활동할 수 있는 실질적인 존재는 여러 가지 협력을 요구한다는 점을 표시하는 것입니다.

작성자:
조 브록마이어
2026년 7월 22일
구아덱
X11에서 Wayland로 이동할 때 사용자가 자주 놓치는 기능 중 하나는
세션 간 창 위치를 저장하고 복원하는 기능. [GUADEC 2026](https://events.gnome.org/event/306/)에서 개최
스페인 아 코루냐(A Coruña)의 Adrian Vovk가 지금까지 진행된 작업에 대한 개요를 제공했습니다.
그놈을 위한 플랫폼 전체의 저장 및 복원 프레임워크를 제공하는 것입니다. 2시 이후
API 착륙 시도가 실패하면 그는 세 번째 시도가 성공할 것이라고 믿습니다.
하나는 성공할 것입니다. 하지만 곧 출시될 GNOME 51 릴리스에는 시기상조입니다.
10월 만기.

저는 올해 GUADEC에 직접 참석하지는 않았지만,
Vovk의 강연이 스트리밍된 후의 동영상입니다. 개인 토크 영상
아직 게시되지 않았지만 그의 강연은 컨퍼런스 둘째 날부터 [5:40
in the full video](https://www.youtube.com/live/EGazCEww9II?si=q1xPggPxg__fsEw-&t=20417)에서 볼 수 있습니다. 슬라이드에서
세션이 아직 게시되지 않았습니다.

저장 및 복원 기능의 기본 아이디어는 간단하다고 Vovk는 말했습니다. 사람
시스템을 사용하고 있으며 작업 중에 응용프로그램을 열어 놓은 경우
어떤 이유로든 데스크톱에서 로그아웃하거나 재부팅해야 합니다. 로그할 때
데스크탑으로 돌아가서 이전 세션을 복원하려고 합니다.
즉, 응용 프로그램 창은 이전 위치와 크기를 다시 시작하고
동일한 문서 등. 현재는 적어도 GNOME에서는 이것이 불가능합니다.
추가 확장 없이는 아닙니다.

"[Restore
Geometry](https://extensions.gnome.org/extension/8908/restore-geometry/)" 및 창의적인 제목의 "[Another
Window Session Manager](https://extensions.gnome.org/extension/4709/another-window-session-manager/)"과 같이 이 동작을 에뮬레이션하려는 GNOME 확장이 있습니다. 그러나 기능은 틀림없이 뭔가입니다
GNOME 자체에서 사용할 수 있어야 합니다.


#### 이익

저장 및 복원은 그놈에서 일반적으로 요청되는 기능이라고 Vovk는 말했습니다. 그
부재는 또한 사람들이 종종 Wayland의 결핍으로 언급하는 것이기도 합니다.
X11과 비교해보세요. 그는 회복에 있어 실질적인 이점이 있다고 지적했습니다.
응용 프로그램 및 시스템 충돌.

그는 저장에서 가장 흥미로운 이점 중 하나를 말했습니다.
복원을 통해 사용자가 더 많은 정보를 업데이트하도록 유도할 수 있었습니다.
자주. 업데이트를 하려면 시스템을 재부팅해야 하는 경우가 많으며, 사용자는
업데이트를 적용하려면 불변 시스템을 재부팅해야 합니다. "그러나 재부팅
시스템이 상당히 파괴적입니다. 당신은 당신이 일했던 모든 것을 잃었습니다
에." 그는 자신의 작업 공간을 준비할 것이라고 인정했습니다.
마음에 들었고 1~2주 동안 업데이트 적용을 피하여
다시 시작할 필요는 없습니다.

저장 및 복원을 위한 기반은 "기타, 더 멋진" 용도로도 사용될 수 있습니다.
기능". 예를 들어 휴대폰 운영 체제는 상태를 저장합니다.
전원이나 RAM을 절약하기 위해 응용 프로그램을 종료한 다음, 사용자가 사용할 때 복원합니다.
응용 프로그램으로 다시 전환합니다. 비슷한 일을 할 수도 있겠네요
그놈 데스크탑에서. 프레임워크를 사용할 수 있는 또 다른 방법은 다음을 구현하는 것입니다.
Apple의 [Handoff](https://support.apple.com/en-us/102426) 기능과 같은 것입니다.
사용자는 한 장치의 애플리케이션 상태를 다른 장치로 이동하고 계속할 수 있습니다.
대상 장치에서 작업 중입니다.

Vovk는 이러한 기능이 다음과 같이 될 것이라고 약속하지 *않았다*고 강조했습니다.
구현했거나 작업을 진행했지만 저장 및 복원 프레임워크는
그런 것들을 위한 기초.


#### 역사

X11을 사용하면 애플리케이션은 다음을 사용하여 [session manager](https://en.wikipedia.org/wiki/X_session_manager)에 등록됩니다.
[X
Session Management Protocol](https://xorg.freedesktop.org/releases/X11R7.7/doc/libSM/xsmp.html)(XSMP)은 균일한 메커니즘을 제공했습니다.
세션을 저장하고 복원할 수 있습니다. 응용 프로그램은 다음을 담당했습니다.
자신의 상태를 알리고 자신을 회복하기 위해. "이론적으로 우리는
Wayland와 함께 사용할 수도 있었지만 몇 가지 문제가 있었습니다."라고 Vovk는 말했습니다. 그는
그놈에서 X11 세션 저장 및 복원이 꽤 오랫동안 중단되었음을 언급했습니다.
년; 그런 다음 GNOME 50에서 [X11
session support code was removed from GNOME](https://blogs.gnome.org/alatiera/2025/06/08/the-x11-session-removal/)가 발생하면 이에 대한 코드가 완전히 삭제되었습니다.

그는 가장 큰 문제는 XSMP가 모두 명령줄이었다는 점이라고 말했습니다.
이는 애플리케이션이 세션에 대한 명령을 제공한다는 의미입니다.
관리자는 일반적으로 응용 프로그램의 파일이 있는 파일을 사용하여 다음 로그인 시 실행됩니다.
상태가 어떤 방식으로든 저장되었습니다. "물론, 그건 아무것도 아니라는 뜻이야
샌드박스와 함께 작동합니다. 내 말은, 우리는 샌드박스 앱이
로그인 시 일부 명령을 실행하는 운영 체제입니다."

저장 및 복원이 샌드박싱에서 작동하도록 하기 위해 Vovk는 다음을 대체합니다.
XSMP는 [XDG desktop
portal](https://flatpak.github.io/xdg-desktop-portal/docs/)입니다. 이는 XSMP의 작동 방식과 크게 다르지 않습니다.
말했다. 응용프로그램은 여전히 GNOME 세션 관리자에 등록되어 있으며 계속해서 유지됩니다.
다음 로그인 시 다시 시작할 항목을 추적합니다. 응용 프로그램은 다음에 의해 다시 시작됩니다.
관리자가 실행할 명령줄을 전달하는 대신 [desktop
entry](https://specifications.freedesktop.org/desktop-entry/latest/)을 사용합니다. 때
응용 프로그램이 다시 시작되면 "복원 이유"가 제공되어 무엇을 해야 하는지 알려줍니다.
해야 할 일:

> 그러면 앱에 "이것은 정상적인 실행입니다. 복원해야 합니다."라고 알립니다.
> 창 위치일 수도 있지만 창 내부 내용은 아닐 수도 있습니다." 아니면 그럴 수도 있지
> "전체 세션 복원을 수행 중입니다. 최대한 많이 복원하세요."라고 말하거나
> "방금 충돌이 발생했으므로 일부 항목을 복원할 수 있지만 다음과 같은 일이 발생하지 않도록 주의하세요."라고 말할 수 있습니다.
> 충돌 루프에 빠지게 됩니다." 그리고 나는 많은 복잡성에 대해 얼버무리고 있습니다.

X11의 XSMP를 사용하면 응용 프로그램이 모든 것을 저장하는 역할을 했습니다.
창 관리 상태를 포함하여 자체적으로. X 서버에 요청합니다.
위치, 크기, 그리고 모든 창 관리 플래그에 대해 묻는 것 같았습니다.
약. 그런 다음 이를 기록하고 나중에 복원합니다."

그러나 Wayland에서는 애플리케이션이 여러 위치에 위치할 수 없습니다.
이유는 Vovk가 말했지만 그 이유에 대해 자세히 설명하지는 않았습니다. 대신,
Wayland는 [`xdg_session_management_v1`](https://hoyon.github.io/wayland-protocol-docs/protocols/xdg_session_management_v1.html)을 제공합니다
프로토콜. 애플리케이션은 자신의 상태를 저장하지 않습니다.
합성자, '야, 내 상태를 저장하고 토큰을 줄 수 있니?' 그것은 단지
본질적으로 큰 난수입니다." GNOME의 [mutter](https://mutter.gnome.org/)과 같은 합성기는 모든 것을 저장합니다. 나중에,
애플리케이션은 컴포지터에 토큰을 제공할 수 있습니다.
"복원하는 것이 합리적이라면 무엇이든".

Vovk는 GNOME이 X11에서 가졌던 것보다 낫다고 말했습니다. 첫째, 더 많았습니다.
일관성: 저장되고 복원된 내용은 합성기로 중앙 집중화됩니다.
데스크탑에 적합한 정책을 실행할 수 있습니다. 예를 들어 그는 설명했다.
애플리케이션이 시작되면 위치가 복원될 수 있지만 사용자는
응용 프로그램이 원래 있던 작업 공간을 복원하는 것을 원하지 않을 수 있습니다.
이전에도 그렇고. "네가 3위라면 정말 이상할 것 같아.
작업 공간에서 앱을 실행했는데 첫 번째 작업 공간에서 열립니다.
저번에 있던 곳이에요."

"기존 X11 작업 방식"을 사용하면 애플리케이션이 다음을 수행해야 합니다.
존재하지 않았을 수도 있는 작업 공간을 인식하고 이러한 가장자리를 처리하십시오.
사례. "데스크탑마다 작동 방식이 다르며 이는 다음과 같습니다.
완전 엉망이야." Vovk는 Wayland 프로토콜을 사용하면 합성자가 다음을 결정할 수 있다고 말했습니다.
응용 프로그램을 시작할 때 해야 할 일. "정상 출시 중에는
이 데스크톱 환경에서는 작업 공간을 복원하는 것이 의미가 없습니다.
그러지 않아."


#### GTK

Vovk는 이 모든 것 중에서 가장 어려운 부분이 GTK라고 말했습니다. XSMP에서 누락된 것
"앱이 세션 저장과 상호작용하고
복원했기 때문에 앱에서 널리 구현되지 않았습니다." 만약에
애플리케이션이 저장 및 복원을 지원하려면 쉬운 방법이 필요합니다.
이 시스템에 접속하는 것입니다. 그가 GTK에 대해 원했던 전반적인 접근 방식은 다음과 같습니다.
[`Gtk.Application()`](https://docs.gtk.org/gtk4/class.Application.html),
세션 관리를 처리하고 모든 것을 관리합니다. "이것은
포털에서는 Wayland 프로토콜 등을 처리합니다." 구현
그가 "상태 스냅샷"이라고 부르는 것을 기반으로 구축될 것입니다.

그 아이디어는 GTK가 애플리케이션의 모든 상태와 정보를 수집하기로 결정할 수 있다는 것이었습니다.
나중에 복원할 수 있도록 저장하세요. 극단적인 경우가 꽤 많았습니다.
고려해 보세요, 라고 그는 말했다. 예를 들어 애플리케이션에 저장된 상태가 있고 사용자가
노틸러스 파일 관리자에서 해당 파일과 관련된 파일을 두 번 클릭합니다.
응용 프로그램, "먼저 복원합니까? 새 파일을 열어서 처리합니까?
파일? 정말 명확하지 않습니다." 의 경우와 비슷하다고 하더군요.
응용프로그램은 이미 두 개의 창을 열어둔 채 실행 중이었고,
새 파일을 열라는 활성화 요청이 전송되었습니다.

> 그래서 제가 생각하는 복원은 앱과 크게 다르지 않습니다.
> 한동안 실행되었으며 사용자는 이미 몇 가지 작업을 수행했습니다.
> 거기. 따라서 GTK가 할 일은 앱을 실행할 때 앱을 복원하는 것입니다.
> 먼저. 그러면 앱이 개념적으로 다음과 같은 상태가 됩니다.
> 사용자가 한동안 앱을 사용한 것과 동일한 상태, 커플이 있는 경우
> 창문이 열리는 등.
> 그런 다음 앱에 활성화 요청을 보냅니다. 그리고 이는 모든
> 저장, 복원, 라이프사이클의 극단적인 사례는 사라지는 것처럼 보입니다.
> 해당 경우는 이미 실행중인 앱의 경우와 같습니다.

GTK에는 충돌 복원력을 위해 주기적인 자동 저장 기능이 있다고 그는 말했습니다. 15일마다
초마다 기본적으로 GTK는 애플리케이션 상태의 스냅샷을 찍습니다. 만약에
충돌이 발생했습니다. "컴퓨터에서 하고 있던 작업의 최대 15초를 잃게 됩니다.
마지막에 초점을 맞춘 앱". GTK의 목표는 모든 복잡성을 숨기는 것입니다.
Wayland 프로토콜 및 엣지 케이스. 그는 사용자가
응용 프로그램을 닫았다가 완전히 종료되기 전에 다시 시작합니다. "어쩌면
검색 공급자가 앱 실행을 보류하고 있거나 다음에서 일부 작업을 실행 중입니다.
배경이든 뭐든." GTK는 애플리케이션 창을 복원해야 하지만
"아직 살아 있는" 애플리케이션 부분이 아닙니다.


#### 첫 번째 API

GTK에 적용된 첫 번째 API는 "아주 단순"했고 완전히
동기식이라고 그는 말했다. "우리는 단지 신호를 방출할 뿐이고, 모든 신호가
핸들러가 반환되면 작업이 완료된 것으로 가정합니다. 우리는 모든 상태가 다음과 같다고 가정합니다.
수집했다." 이는 최종 릴리스 [GNOME 50](https://release.gnome.org/50/) 및 GTK 4.22에 거의 포함되었습니다.
2026년 3월 18일에 발표되었습니다. "우리는 이것을 거의 출시했습니다." 첫 번째 API
그러나 몇 가지 단점이 있어서 이를 방해했습니다.

단점 중 일부는 구현에 "많은 노력"이 필요하다는 점이었습니다.
반복적인 종류의 코드"라는 점을 고려하지 않았습니다.
응용 프로그램의 전체 창 계층 구조입니다. 첫 번째 API는 적합하지 않았습니다.
자체 상태가 있는 하위 페이지와 같은 일종의 탐색 계층 구조입니다.
응용 프로그램이 있을 것입니다. "나무를 세우는 데 도우미가 없었습니다.
그런 다음 내비게이션을 전달하고 싶다고 말합니다.
계층 구조."

또한 대량 데이터 지원도 부족했습니다. 그는 GNOME의 텍스트 예를 인용했습니다.
편집자: "복원하려는 창 상태가 모두 있을 수 있지만 그런 다음에는
또한 거기에는 수 메가바이트에 달하는 미완성 텍스트 문서가 있습니다.
크기." 해당 텍스트 문서를 저장 파일에 복사하는 것은 바람직하지 않았습니다.
시스템을 복원합니다. "왜냐하면 우리는 데이터를 메모리에 복사하고 있기 때문입니다.
그런 다음 모든 것을 디스크에 기록하면 불필요한 작업이 너무 많습니다." 그럴 것이다
데이터를 "외부" 파일에 저장하고 상태를 유지하는 것이 더 좋습니다.
전체 시스템이 빠르도록 스냅샷이 작습니다.

그러나 그는 첫 번째 API의 가장 큰 단점은 애플리케이션이
비동기식 작업을 수행하고 싶지만 API는 완전히 동기식이었습니다. 그놈에서
텍스트 편집기의 예에서 텍스트 문서를 디스크에 저장하는 것은 비동기식이어야 합니다.
작업: 파일이 클 수도 있고, 디스크가 느릴 수도 있습니다. "우리는 원하지 않습니다.
모든 것을 직렬화하는 동안 앱을 정지하세요."

Vovk는 비동기 문제가 첫 번째 API를 죽인 것이라고 말했습니다. 이 문제
Vovk는 개발자들이 테스트하고 확인할 수 있도록 API를 게시했기 때문에 이런 일이 일어났다고 말했습니다.
그것을 사용하는 데 적합한 몇 가지 응용 프로그램이 있었습니다. "큰 조각 중 하나
피드백은 '음, 여기서 비동기식 작업을 하고 싶지만 할 수 없습니다'였습니다." 그는
그들에게 "실제로는 그렇게 할 수 없습니다"라고 말해야 했습니다. 그는 원래 생각했다
API에 비동기식 지원을 추가하는 것이 가능하지만
"우리가 고칠 수 없는 크고 큰 경쟁 조건 더미"가 포함되었습니다. 그래서,
GTK 4.22 릴리스 직전에 "우리는 이 API를 가져왔습니다. 우리는 그것을 숨겼을 뿐이고,
기본적으로. 모든 공개 API 부분이 삭제되었으며 배관은 여전히 ​​있습니다.
GTK 내부에 숨겨져 있었지만 숨겨져 있었습니다."


#### 두 번째, 세 번째 시도

GNOME 50 출시 이후 그는 구현이 가능해지기를 바랐습니다.
GNOME 51에 맞춰 두 번째 API를 출시했습니다. 그의 두 번째 시도는 비동기식이었습니다.
지원, 창 계층 관리 및 대량 데이터에 대한 솔루션도 보유했습니다. 하지만
비동기 [GObject](https://en.wikipedia.org/wiki/GObject) 신호를 사용하여 구현된 방식, 
유지관리자들에 의해 "압도적으로 거부"되었습니다. "피드백이 좀
비동기 신호는 사람들이 관심을 갖는 것이 아니라는 사실을 알게 되었습니다.
충분히 공평해."

지난 몇 주 동안 Vovk는 세 번째 API 제안을 작업해 왔습니다.
약간 다른 방식으로 두 번째 API의 이점을 유지합니다.
그것. 더 이상 비동기 신호가 없습니다. 비동기식 방법이나 가상을 사용합니다.
함수(vfuncs). "그냥 인터페이스일 뿐, 이상한 건 없어"
기계."

"그럼 이 착륙은 언제 다 이뤄지나요?" Vovk는 수사적으로 물었습니다. 더 웨이랜드
비트는 대부분 존재하며 프로토콜이 릴리스되었습니다. 다음 사용자가 사용할 수 있습니다.
툴킷 및 컴포지터. 저장 및 복원의 중얼거리는 측면이 GNOME 51에 상륙했습니다.
베타, "그러나 실제로 이것을 넣을 때 해결해야 할 몇 가지 버그가 있습니다.
전체 세션에서 함께." GTK용 Wayland 부품은 다음과 같이 출시되었습니다.
GNOME 51 알파이지만 아직 애플리케이션에서 사용할 수 없습니다.

[XDG
session save/restore portal](https://github.com/flatpak/xdg-desktop-portal/discussions/1698)은 아직 완료되지 않았습니다. 그는 자신이 가지고 있다고 말했다
핵심에 동의한 KDE 개발자 및 Firefox 개발자와 대화했습니다.
포털의 개념은 명확하지만 구체적인 세부 사항과 같은 세부 사항에는 여전히 작업이 필요합니다.
이유와 다른 언어의 일부를 복원합니다. 해당 작업은 GitHub의 [this pull
request](https://github.com/flatpak/xdg-desktop-portal/pull/1818)에서 추적되고 있습니다. 그는 또한 [GNOME
Session Manager](https://gitlab.gnome.org/GNOME/gnome-session#gnome-session-manager)에 대한 API를 작업 중이며 다른 부분이 도착하기를 기다리는 [merge
request](https://gitlab.gnome.org/GNOME/gnome-session/-/merge_requests/162)이 있습니다.

세 번째 API의 기본 사항은 피드백을 기다리는 분기에 있습니다.
GTK 관리자로부터 "내 어느 시점에 이를 얻게 될 것이라고 확신합니다.
앞으로 몇 주 동안." 그는 아직 어떤 반응을 보일지 확신하지 못했습니다. 그는
API가 만들어지기 전에 일부 애플리케이션을 API로 포팅하고 싶다고 말했습니다.
GTK에서는 안정적이다. "우리는 인체공학이 어떻게 생겼는지 알아야 합니다.
사용하기 전에, 안정화하기 전에." 결국 그러지 않겠다고 하더군요
GNOME 51 출시에 맞춰 만드세요. 그는 개발자들에게 피드백을 제공하도록 독려했습니다.
그에게 연락하기 위한 API입니다.


#### 질문

한 청중은 듣기 어려운 질문을 했지만 Vovk는
저장 및 복원 옵션이 있는지 알고 싶다고 생각했습니다.
꺼져. 그는 그놈 설정에 사용자 관련 옵션이 있을 것이라고 말했습니다.
애플리케이션을 끄려면 애플리케이션이 이를 선택해야 한다는 점을 언급했습니다.
API도 지원합니다.

다른 사람은 저장을 구현할 수 있는지 알고 싶어했습니다.
GTK보다 낮은 수준에서 기능을 복원합니다. Vovk는 문제가 다음과 같다고 말했습니다.
관련이 있기 때문에 `GtkApplication()`을 사용해야 했습니다.
Wayland와 XDG 포털과의 대화에서 "GTK는 할 것이지만 GLib
안 하고 있어." 이 기능은 또한 GTK 창을 인식해야 합니다.
그렇지 않으면 우리는 당신이 스스로 처리해야 하는 모든 극단적인 경우를 얻게 됩니다."
그는 실현 가능하다고 생각하지 않은 응용 프로그램을 적용했습니다.

마지막 질문은 현재 구현되는 GNOME 확장에 관한 것이었습니다.
기능을 저장하고 복원합니다. 적절한 그놈 기능을 도입한다면 어떨까요?
그 확장을 의미합니까? 연장은 아마 안 될 것 같다고 하더군요.
장기적으로 필요하지만 신청하는 동안 전환 기간이 있습니다.
계속 사용하는 것이 합리적일 수 있는 기능을 사용하도록 포팅되었습니다.
확장.

[Comments (14 posted)](https://lwn.net/Articles/1083750/#Comments)


### [Fedora grapples with change](https://lwn.net/Articles/1081557/)

#### 요약
- Fedora 프로젝트가 크게 변경되어 어떻게 방식과 커뮤니티 거버넌스 문제를 살펴보겠습니다.
- 배치판 배치가 유지관리자, QA, 사용자 이주에 미치는 영향을 설명합니다.
- 기술 방향 성과 프로젝트 운영 절차가 어떻게 표시되는지 표시합니다.

작성자:
조 브록마이어
2026년 7월 20일
[Fedora Project](https://fedoraproject.org/)은 다음과 같이 알려져 있습니다.
무엇보다도 잘 정의된 프로세스 세트를 보유하고 있습니다.
모든 것. 설치할 RPM 생성의 복잡성을 처리하는 광범위한 [packaging
guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/)이 있습니다.
소프트웨어뿐만 아니라 [legal questions](https://docs.fedoraproject.org/en-US/legal/)를 관리하는 프로세스도 포함합니다.
배송 소프트웨어 주변에서 발생합니다. Fedora에는 [self-contained technical changes](https://docs.fedoraproject.org/en-US/operations/changes_policy/#_self_contained_changes)뿐만 아니라 [major
changes to the distribution](https://docs.fedoraproject.org/en-US/operations/changes_policy/#_system_wide_changes) 및 발생하는 기타 문제를 처리하기 위해 잘 정의된 [change
process](https://docs.fedoraproject.org/en-US/operations/changes_guide/)도 있습니다. 현재,
하지만 이 프로젝트는 일종의 중년의 위기를 겪고 있는 것 같습니다.
여러 가지 변경 프로세스를 한 번에 재검토하여 올바른지 확인합니다.
여전히 효과적입니다.


#### 진화

Vendor가 후원하는 프로젝트로서 Fedora는 항상 어려운 길을 걸어야 했습니다.
사용자, 기여자 커뮤니티 및 기업 마스터에게 서비스를 제공합니다. 무엇이 만드는가
가장 행복한 당사자가 다른 당사자에게는 불안의 원인이 될 수 있습니다. [trial technologies in Fedora](https://lwn.net/Articles/680278/)에 대한 Red Hat의 요구는 [not always spark joy](https://lwn.net/Articles/742497/)을 수행합니다.
기여자와 사용자. 자원 봉사자들은 [ideas that are of little interest to Red
Hat](https://lwn.net/Articles/463506/)를 푸시하기를 원할 수도 있고(적어도 그 당시에는) 선택 사항과 충돌할 수도 있습니다. 에 대한
예를 들어 Fedora의 [Btrfs as the
default filesystem](https://fedoramagazine.org/btrfs-coming-to-fedora-33/) 선택은 Red Hat의 [not to support](https://access.redhat.com/solutions/197643) 결정과 대조됩니다.
RHEL(Hat Enterprise Linux).[^lwn1083123-filesystems]

사용자는 [patent-encumbered games](https://lwn.net/Articles/265740/) 또는 [codecs](https://lwn.net/Articles/910978/)과 같은 문제가 있는 소프트웨어에 쉽게 액세스하기를 원하지만 이를 배송하면
Red Hat에 비용이 많이 드는 법적 문제를 야기합니다. Fedora를 더욱 발전시키려는 시도
사용자 친화적입니다(예: [setting
the default for the `$EDITOR` environment variable to GNU nano](https://lwn.net/ml/fedora-devel/CA+voJeWK=rPnJEOrfR4++Jnj3mPbo7VqkbVuegbZ1-THKD-R4A@mail.gmail.com/), [may
not please some developers](https://lwn.net/ml/fedora-devel/20200625185023.GA1670318@host1.jankratochvil.net/)).

2003년 [launched](https://lwn.net/Articles/50516/) 프로젝트가 일종의 일종의 형태로 진행되었을 때 Fedora는 거버넌스나 정책 방식이 거의 없었습니다.
[Red Hat
Linux](https://en.wikipedia.org/wiki/Red_Hat_Linux)을 대체합니다. 초기에 Red Hat은 "Fedora"를 만드는 아이디어를 접했습니다.
재단"은 프로젝트에 어느 정도 독립성을 부여한 다음 철회했습니다.
2006년부터.
Fedora Board 및 Fedora Extras와 같은 기반에 대한 기대
시간이 지남에 따라 운영 위원회, [evolved](https://lwn.net/Articles/608546/)가 [Fedora Council](https://docs.fedoraproject.org/en-US/council/) 및 [Fedora Engineering Steering
Committee](https://docs.fedoraproject.org/en-US/fesco/)(FESCo)로 변경되었습니다.

중간 광고
회사 간 마찰이 있었던 경우도 여러 번 있었습니다.
그리고 지역사회 우선순위; 하지만 프로젝트는 어느 정도 작동하게 되었습니다.
년. 문제를 논의하고 어떤 종류의 해결책을 찾음으로써 이를 수행했습니다.
합의, 그 과정에서 결정된 정책을 문서화하고
그런 다음 이를 새로운 결정에 사용합니다. 예를 들어 Tom Callaway의 개요를 참조하십시오.
[how Fedora's legal policies were
developed](https://lwn.net/Articles/714524/). 수년에 걸쳐 Fedora의 거버넌스와 정책은
다른 오픈 소스 프로젝트의 모델이 됩니다.

프로젝트의 거버넌스는 한 가지 변함없는 원칙을 가지고 있습니다: Red Hat이 최종 결정권을 가지고 있습니다. 다음과 같이
Red Hat이 아이디어를 폐기했을 때 전 Fedora 프로젝트 리더(FPL) Max Spevack [noted](https://lwn.net/Articles/178518/)
독립 재단의:

> Red Hat은 *반드시* Fedora 결정에 대해 일정 수준의 통제권을 유지해야 합니다.
> Red Hat의 비즈니스 모델은 Fedora에 *의존*하기 때문입니다. Red Hat이 기여합니다
> Fedora와 Red Hat의 성공을 위해 수백만 달러에 달하는 직원과 리소스 제공
> 또한 Fedora에 대한 모든 법적 위험을 감수합니다. 따라서 Red Hat은
> 때때로 Fedora에 관해 어려운 결정을 내려야 할 때가 있습니다. 자주는 못하겠지만,
> 그렇게 할 때, 우리는 그러한 결정의 근거를 공개적으로 논의할 것입니다.
> 할 수 있습니다.

Red Hat이 Fedora에 대한 권한을 갖고 있다고 해서 회사가 Fedora를 압도한다는 의미는 아닙니다.
그것을 사용하고 싶다고 그는 말했다. 또한 모든 중요한 결정을 내리고 싶지도 않았습니다.
Fedora 소개: 효과적인 커뮤니티 중심의 의사 결정은 직접적입니다.
Fedora의 성공의 척도. "우리는 오픈소스의 표준을 설정하는 것을 목표로 하고 있습니다.
혁신.  진정한 개방형 Fedora 프로젝트가 이를 가능하게 합니다."


#### 샌드박스

하지만 지난 1년 정도 동안 효과가 있었던 프로젝트 프로세스는
지금까지는 점점 더 자주 의문이 제기되는 것 같습니다.
Red Hat의 우선순위와 충돌하는 것 같습니다. 예를 들어 작년의 [deliberation on Fedora's AI-assisted
contribution policy](https://lwn.net/Articles/1039623/)은 Red Hat의 목표 사이의 단절을 보여주었습니다.
Fedora에서 AI를 실험하고 Fedora의 정책이
AI에 훨씬 덜 우호적입니다.

3월 현재 FPL Jef Spaleta [proposed](https://lwn.net/Articles/1062579/) a
그는 기술-혁신-라이프사이클 프로세스를 "Fedora Sandbox"라고 불렀습니다.
"실험적 기능, 구성 요소, 출력, 프로세스 또는 서비스".

Spaleta의 샌드박스 아이디어의 원동력은 좌절감과 관련된 것 같습니다.
Red Hat 리더십은 Fedora에 대한 실험을 추진했습니다. 는
Fedora의 엄격한 규정을 준수하는 프로젝트의 기존 프로세스
패키징 및 라이센스 정책뿐만 아니라 커뮤니티 동의를 얻어야 할 필요성도 있습니다.
Red Hat이 RHEL을 위해 수행할 작업을 느리거나 방해하는 방식으로 수용
어쨌든.

Fedora 외부에서 해당 프로젝트를 유지해야 하며, 이는 궁극적으로
RHEL 릴리스의 기반 역할을 하며 좌절감을 유발할 가능성이 있음
관리자와 Red Hat은 물론이고 두 가지 작업 모두에 종사하는 사람들을 위한 것입니다.
(불합리하지는 않지만) 일정에 따라 RHEL에 기능이 제공되기를 원하는 리더십
고객을 행복하게 하기 위해.

Spaleta's sandbox process would have allowed experiments to be conducted in
Fedora even if they broke "non legally binding" policies as long as they
had a "reasonable path forward towards resolution" before being fully
integrated into the project or distribution. He proposed that the sandbox would
be in addition to the existing change processes and [community
initiatives](https://docs.fedoraproject.org/en-US/project/initiatives/) that can be used to set longer-term goals for Fedora, such
as the completed initiative to create the [Fedora IoT](https://fedoraproject.org/iot/) project,
or the current [Git
Forge initiative](https://fedoraproject.org/wiki/Initiatives/Git_Forge_Initiative_2025) to replace the [Pagure](https://pagure.io/)
collaboration platform with the [Forgejo](https://forgejo.org/)-based
[Fedora Forge](https://forge.fedoraproject.org/) service.
The sandbox proposal has not been accepted (or rejected) yet.


#### 주도적 마찰

Red Hat 개발자 Gordon Messmer [proposed
an AI developer desktop](https://discussion.fedoraproject.org/t/fedora-ai-developer-desktop-objective/184941) 이니셔티브는 3월 31일에 '번창하는 환경 구축'을 목표로 합니다.
Fedora 내의 AI 기술 관련 커뮤니티'입니다. 그
커뮤니티에서 [met with some
opposition](https://lwn.net/Articles/1071949/) 제안, AI에 대한 혐오감 등 다양한 반대 의견 제시
트리 외부 커널에 대한 Fedora의 정책 변경 가능성에 대한 불만 사항
모듈. 궁극적으로 이 제안은 페도라 위원회([initially
approved](https://forge.fedoraproject.org/council/tickets/issues/562#issuecomment-697648))에 의해 논의되었으며, 위원회 회원인 Justin이 마지막 순간에 차단했습니다.
Wheeler [changed
his vote](https://forge.fedoraproject.org/council/tickets/issues/562#issuecomment-698875)(5월 8일). 위원회 회원 Miro Hrončok도 마찬가지로 5월 13일 [also
changed his vote](https://forge.fedoraproject.org/council/tickets/issues/562#issuecomment-711131)에서 "Fedora 커뮤니티는 그렇지 않습니다.
이 계획을 있는 그대로 지지합니다."

Red Hat의 또 다른 아이디어, 운영 체제 구축을 위한 자동화된 접근 방식
4월 Fedora 개발 목록에 Project Hummingbird, [was
raised](https://lwn.net/ml/all/177691074183.855997.8416552677702727530@mailman01.rdu3.fedoraproject.org/)이라고 불렸습니다. 몇몇 사람들의 환영을 받았어요
관심뿐만 아니라 다른 Fedora와 어떻게 다른지에 대한 혼란도 있습니다.
변형되었지만 큰 반대에 직면하지는 않은 것 같습니다. 결코 공식적으로는 아니었지만
제안되었지만 McCarty [said](https://lwn.net/ml/all/177733652424.1739841.13553204795429552242@mailman01.rdu3.fedoraproject.org/)
그는 Spaleta의 샌드박스 이니셔티브를 통해 그렇게 할 계획이었습니다.

대신 Red Hat은 공개 프로세스를 완전히 우회했습니다. [announce](https://www.redhat.com/en/about/press-releases/fedora-hummingbird-linux-brings-agentic-linux-builders)을 사용할 수 있도록 Fedora 상표 사용 승인을 [in
private](https://discussion.fedoraproject.org/t/fedora-hummingbird-taking-the-hummingbird-model-to-the-full-operating-system/191184/25) 협의회에 요청했습니다.
5월 12일 Red Hat Summit의 프로젝트. Red Hat 외부의 Fedora 기여자
그 발표에 놀랐고 혼란스러웠다. 마이클 그루버(예: [wondered](https://discussion.fedoraproject.org/t/fedora-hummingbird-taking-the-hummingbird-model-to-the-full-operating-system/191184/7))
Hummingbird가 합법적으로 Fedora 프로젝트인지 여부. "그럴 수도 있지.
거기에 몇 가지 좋은 아이디어가 있지만 이것이 어떻게 시작되었고 어떻게 전달되었는지를 고려하면
나는 이것에 대해 전혀 신뢰하지 않을 수 있습니다."

Red Hat 직원이자 Fedora 기여자 Adam Williamson [said](https://discussion.fedoraproject.org/t/fedora-hummingbird-taking-the-hummingbird-model-to-the-full-operating-system/191184/50)
Red Hat이 좀 더 공개적으로 요청을 하는 것이 이상적이었을 것입니다.
회사가 Fedora 내에서 Hummingbird 프로젝트를 수행하려고 시도한 것이 기뻤습니다.
프로젝트를 마무리하는 중입니다. Red Hat이 Fedora 외부에서 수행해야 하는 작업이 많아질수록 그는
그럴수록 회사가 자금 조달에 의문을 제기할 위험이 커집니다.
프로젝트.

> Red Hat 내부에서, 특히 Fedora에서 작업하지 않는 경우에는
> Fedora를 분쟁의 원인으로 보는 것이 가능/유혹적입니다. 이거 다 들어있어요
> 급여에 포함되지 않은 의견을 가진 사람들! 당신은 그들에게 무엇을 말할 수 없습니다
> 매니저에게 행동이나 생각, 불만을 토로합니다! 그들은 그것에 대해 영원한 논쟁을 벌이고 있습니다.
> 모든 것! 위키 페이지를 작성하고 한 번도 본 적이 없는 사람을 설득해야 합니다.
> 당신의 아이디어가 좋다고 들었어요! 누가 이것을 필요로 합니까?
> 그래서 우리는 RH가 갑자기 일을 늘리는 경향에 맞서 끊임없이 싸우고 있습니다.
> 채널에서는 100% 제어되며 처음에는 가장 쉬워 보이는 경향이 있지만 실제로는
> 몇년 지나면 엉망이 될 것 같아요.

그러나 크리스토퍼 클루즈는 [worried](https://discussion.fedoraproject.org/t/fedora-hummingbird-taking-the-hummingbird-model-to-the-full-operating-system/191184/52)
자금 조달의 정당성은 Fedora가 "단계적으로" 될 수 있다는 것을 의미했습니다.
RH'라는 법인 단위로 전환되었습니다. 그는 이미 그랬다고 덧붙였다.
위원회가 언제 RH의 대리인 역할을 하는지, 언제 RH의 대리인 역할을 하는지는 확실하지 않습니다.
커뮤니티".

윌리엄슨 [replied](https://discussion.fedoraproject.org/t/fedora-hummingbird-taking-the-hummingbird-model-to-the-full-operating-system/191184/56)
그는 요점을 이해했지만 이것은 "항상 존재하는" 것이라고 말했습니다.
Fedora가 거의 오랫동안 관리해야 했던 "긴장"
주위:

> Fedora가 "경쟁"할 수 있는 방법은 RH의 일부를 변경하는 것이 아닙니다.
> 표면적으로는 오픈 소스인 업스트림 프로젝트를 원한다고 생각할 수도 있습니다.
> 라이센스 조건이지만 거버넌스에서 엄격하게 통제됩니다.
> 필요 - 열정적이고 참여하는 사람들과 느슨하게 결합된 업스트림 프로젝트
> 때때로 일을 어색하고 불편하게 만들지만 대개는
> 장기적으로 더 나은 최종 결과를 얻고 RH에 대한 유용한 점검 역할을 합니다.
> 때때로 인식.

그는 Fedora에 관심이 있는 Red Hat 직원은 Fedora를 계속 판매해야 한다고 말했습니다.
비전을 확인하고 그것이 작동하는지 확인합니다. Hummingbird 토론은 줄어들지 않았습니다.
Williamson의 답변이 있은 지 오랜 시간이 지났지만 Fedora의 의사 결정 기관은
일이 어떻게 진행되는지 고민하고 있습니다.


#### 일시중지 누르기

7월 1일, Fedora의 '변경 담당자'인 Aoife Moloney, [announced](https://discussion.fedoraproject.org/t/fedora-council-statement-on-the-future-of-community-initiatives-and-the-ai-developer-desktop-proposal/195402/1)
Fedora 위원회는 Fedora 커뮤니티에 일시 중지를 제안했습니다.
이니셔티브 프로세스. 기존 계획은 계획대로 계속될 것입니다.
그러나 "주변의 관리 프레임워크가 발전할 수 있다"고 말했습니다.

그녀는 AI 개발자 데스크탑에서 이니셔티브 프로세스가 다음과 같이 실패했음을 보여주었다고 말했습니다.
새로운 아이디어가 표면화되고, 존중받는 피드백을 받으며,
프로젝트의 현재 및/또는 적합한 작업에 대한 의회 지원을 얻습니다.
미래". 그러나 실패의 성격은 명시되지 않았습니다. 하나는 할 수 있다
그 토론에 참여한 다양한 참가자들이 다음에 동의할 것이라고 상상해 보십시오.
*뭔가* 잘 안 됐는데, 그게 *뭔가* 어땠을까
전적으로 관찰자의 관점에 달려있습니다.

Moloney는 의회가 새로운 설정 방법을 모색하기를 원했다고 말했습니다.
전략적 방향은 "개방적이고 투명한 방식으로 보다 의도적으로
커뮤니티의 목소리도 포함됩니다." 의회는 그렇게 해야 한다고 인정했다.
"토론과 의사결정에 있어서 더 개방적인 태도를 취하는 것이 더 좋습니다."
왜냐하면 제안으로 이어지는 작업의 대부분은 " 레이더 아래에서 발생하기 때문입니다.
공식 승인 절차가 시작되기 전에." 현재 기존의 
이니셔티브에 대한 "승인 파이프라인"에는 시의회 수행이 포함됩니다.
상표 검토, FESCo에서 변경 제안 검토. 그거 잘 되네, 그녀는
말했지만 "전 세계 모든 사람을 위한 초기의 포괄적인 토론이 그리워요."
프로젝트". 따라서 의회는 샌드박스 제안을 면밀히 검토할 것입니다.
이니셔티브에 대한 대안으로 또는 다른 프로세스에 대한 보완으로
발전할 수도 있습니다.

발표에서는 일시 중지를 제안으로 표현했지만 Moloney는 AI 개발자 데스크톱 제안에서 [closed
the discussion](https://forge.fedoraproject.org/council/tickets/issues/562#issuecomment-876724)도 협의회에서 다음과 같이 말했습니다.
이제 커뮤니티 중단으로 인해 이를 고려할 수 없게 되었습니다.
이니셔티브 프로세스." 의회는 다음 문제로 돌아갈 것이다.
"이번 조치가 완료되면 커뮤니티 이니셔티브를 폐기해야 할지 아니면 개선해야 할지 여부가 결정됩니다.
논의가 어느 정도 결론에 이르렀다”고 말했다.


#### 변경사항 변경사항

협의회가 발표하기 직전에 FESCo 회원은
'Maxwell G'가 [discussion](https://lwn.net/ml/all/dc24cfc7-0a63-43f0-a36b-c62c794902db%40gtmx.me/)을 시작했습니다.
Fedora 개발 메일링 리스트에서 변경 사항에 대한 피드백을 수집하세요.
프로세스가 개선될 수 있습니다. 구체적인 제안은 하지 않았지만,
몇 가지 아이디어를 던져보고 다른 사람들이 어떻게 생각하는지 알고 싶었습니다.

예를 들어, 그는 이제 [Fedora's wiki](https://fedoraproject.org/wiki/Fedora_Project_Wiki) 사용을 중단해야 할 때가 되었는지 궁금했습니다.
제안서뿐만 아니라 [Wikitext](https://en.wikipedia.org/wiki/Help:Wikitext) 형식도
그것과 함께 간다. 서식은 종종 위키를 벗어나 다음 위치로 이동합니다.
다른 포럼; 예를 들어, 2020년의 [Btrfs
change proposal for Fedora 33](https://lwn.net/ml/fedora-devel/CA+voJeXGvEk9gZzcTJkL56XXHWzo_L+m8s-=x7Y6KtNEh_a60Q@mail.gmail.com/)에는 일반
불쾌감을 주는 텍스트, MediaWiki 형식 및 HTML `<span>` 태그
메일 클라이언트에서 해독을 시도합니다.

그는 변화가 이루어져야 한다고 제안했다.
Markdown 또는 "쉽게 변환할 수 있는 일부 형식"으로 저장하고 다음과 같이 저장합니다.
Wiki가 아닌 Git 저장소의 텍스트 파일입니다. 소유자를 변경할 수 있습니다.
제안서를 병합 요청으로 제출하면 해당 제안은 검토 및 병합됩니다.
랭글러를 바꾸세요. 그는 또한 [Discourse forum](https://discussion.fedoraproject.org/)에서 벗어나는 아이디어를 기본으로 제시했습니다.
변경 제안에 대한 진실의 원천 그는 또한 연습을 중단하고 싶었습니다
포럼과 Fedora 개발 모두에서 변경 사항에 대한 논의가 이루어집니다.
목록:

> [fesco [ticket] #2989](https://pagure.io/fesco/issue/2989)에서는 Discourse에 대한 교차 게시가 실험으로 제안되었지만
> 중단할지 계속할지에 대한 결정이 내려진 적이 없습니다.
> 실험. 나는 devel@과 Discourse 사이의 단절된 토론이 어렵다고 생각합니다.
> 따라가다. Discourse 설정을 사용하면 토론을 더 쉽게 할 수 있다고 생각합니다.
> "가속화"하거나 유독하거나 반복적으로 변합니다. 내 생각엔 그게 더 나은 것 같지는 않아
> 큰 스레드를 처리합니다.

메일링 리스트에 토론을 통합하라는 제안이 있는 것 같았습니다.
인기. 마이클 쇼름 [agreed](https://lwn.net/ml/all/CALC7GWwRUepPNMkg2Kf4Y9nG-GitCTBaAXwY_JEjURw=YPprAQ@mail.gmail.com/)
메일링 리스트와 포럼 사이에 토론을 나누는 것은 좋지 않았다는 점,
특히 두 가지를 모두 따라야 하는 변경 소유자에게는 더욱 그렇습니다. 비욘 페르손 역시
논의를 통합해야 한다는 데 동의했지만 그는 [observed](https://lwn.net/ml/all/20260629151940.64df8971@tag.xn--rombobjrn-67a.se/)
포럼과 메일링 리스트를 팔로우하는 것보다 훨씬 더 나빴습니다.
토론. "변화 과정을 거치면서 변화의 상태는
Wiki, Pagure, Bugzilla, 심지어 Gitlab까지 분열되었습니다." 그는 계산했다
10개의 서로 다른 토론 포럼과 문제 추적기가 모두 자체 사일로에 있습니다. "에
적어도 Pagure와 Bugzilla는 누군가가 글을 쓸 때 나에게 이메일을 보내는 데 능숙합니다.
댓글."

그러나 Kevin Fenzi는 [thought](https://lwn.net/ml/all/akKtyIIaen8pwvdt@orm.scrye.com/)
변경 요청을 위해 포럼을 이용하는 관행은 계속되어야 합니다. 그는 있었다는 것을 인정했다.
몇 가지 문제가 있었지만 이는 Fedora가 "사람들로부터 피드백을 받았다는 것을 의미합니다.
다른 방법으로는 관여하지 않으며 때로는 [그것이] 매우 유용합니다." 그는 느꼈다
새로운 목소리를 듣고 피드백을 받아들이는 것이 중요하다고 말했습니다.
그들이 있는 곳."

Fedora와 긴밀히 협력했던 전 Fedora 프로그램 관리자 Ben Cotton
임기 중 변화 과정, [thought](https://lwn.net/ml/all/CAJox115Pxf71kq0x_ucrdBwz7RDck1Cv9MpX_iWxZqPTKtTD2g@mail.gmail.com/)
프로세스를 현대화해야 하지만 더 나은 접근 방식을 제안했습니다.
프로세스가 높은 수준에서 어떤 모습이어야 하는지 생각하는 것입니다.
어떻게 구현하는지 생각해 보세요.

[suggestion](https://lwn.net/ml/all/8d6938a6fcb2330b1649c56470810a62662948a4.camel@redhat.com/)이 있었습니다
Martin Kolman은 Fedora가 간단한 웹 애플리케이션을 구축해야 한다고 말했습니다.
변경 프로세스를 관리합니다. 새로운 기여자에게는 덜 부담스러울 것입니다.
변경이 이루어지기 전에 정보를 검증하도록 설계될 수 있습니다.
제출되었습니다. 그러나 유지 관리할 또 다른 자체 개발 애플리케이션에 대한 아이디어는
지지자를 얻지 못합니다. 다니엘 P. 베랑제 [said](https://lwn.net/ml/all/akTUpZ3TFIUaoa28@redhat.com/) 페도라
물건을 만드는 데 있어 "오랜 (그리고 실망스러운) 실적"을 갖고 있었고
장기적으로 그들을 지원할 수 없습니다. "나는 그것이 좋은 것이라고 볼 수 없다
이를 위한 맞춤형 앱을 구축하고 유지하기 위해 리소스를 사용합니다."

6월 30일 [weighed
in](https://lwn.net/ml/all/CAJqbrbfk0b5CDhjTYkjaTs_+KRaDq3Cg9SfHvMLx5zm=d5FkWA@mail.gmail.com/) 업무의 일환으로 변화 작업을 하고 있는 Moloney는 몇 가지 제안에 동의했다고 말했습니다.
예를 들어 변경 논의를 메일링 리스트로 제한하는 등의 내용을 요청했지만
토론 참가자들은 실습 시간이 얼마나 되는지 스스로에게 묻습니다.
방법을 제안하기 전에 프로세스의 메커니즘에 참여했습니다.
이를 수행하는 새로운 방법을 설계하는 것입니다." 그녀는 또한 많은 것이 있다고 지적했습니다.
Fedora Forge로의 이전과 같은 부분은 이미 움직이고 있으며 그럴 수도 있다고 생각했습니다.
먼지를 가라앉힌 다음 우리가 어떤지 살펴보는 것이 좋은 생각입니다.
누락되었습니다."

Red Hat 엔지니어링 관리자 Brendan Conoboy도 [spoke
up](https://lwn.net/ml/all/CAKzUzufLmxoD-zmyt9wSJpAL1YK-V8mVZO+-viiZ3UN96BPvzw@mail.gmail.com/)을 통해 Fedora의 프로세스를 외부에서 바라보고 있습니다.
in. 전반적으로 그는 변화 프로세스가 꽤 잘 작동한다고 생각했습니다.
리눅스 배포판의 경우. "작동하지 않는 점은 다음과 같습니다. 이를 변경합니다.
기존 프로세스에 적합하지 않습니다." 그는 [recent two-factor
authentication discussion](https://lwn.net/Articles/1078964/)과 AI 개발자 데스크톱 제안을 다음과 같이 인용했습니다.
예. "모든 이해관계가 존중받는 방식으로 변화를 시작하기 위해 거쳐야 할 기준
대화를 시작하는 것조차 어려울 정도로 힘들다.
괴로워."

Maxwell G [pointed
out](https://lwn.net/ml/all/fc71da0a-1cf0-45ad-9130-7cbc06ce5ece@gtmx.me/)은 AI 논의가 "많은 어려움을 겪었다"고 말했습니다.
그 중 일부는 절차적이었습니다(예: 의회가 명확하게 규정하지 못함).
제안에 대한 투표 의사를 발표했지만)
사회적, 정치적 불일치도 마찬가지다. 어쨌든 그는 이렇게 말했다.
변화 제안이라기보다는 하나의 계획이었고 그 과정은
별도의 심의를 거쳐 의회에 제출됐다. 코노보이 [replied](https://lwn.net/ml/all/CAKzUzufD6VpaPo=m1KesmcEB6RNDZTBboN_K9V+uSQKCE5ngqA@mail.gmail.com/),
"우리는 [AI] 주제가 논란의 여지가 있다는 것을 알고 있었고,
문서화된 프로세스를 따르면 더 나은 프레임워크를 제공할 수 있습니다.
건설적인 피드백". 아마도 그랬을 수도 있겠지만 그랬을 수도 있다고 그는 말했다.
아이디어가 FESCo를 통해 먼저 사회화되었더라면 더 좋았을 것입니다.


#### 결과

논의가 끝난 후 Maxwell G [replied](https://lwn.net/ml/all/6b56af97-0d2f-4e07-ad37-9638bc1438ec@gtmx.me/)
7월 7일에 그의 대화 요약이 포함되어 있습니다. 그의 첫 번째 테이크아웃은
더 많은 맥락을 포함하는 더 자세한 문제 설명이 있었어야 했다는 것입니다.
그가 토론에서 무엇을 찾고 있었는지에 대해. 그는 뭔가가 있다는 것을 발견했습니다
Git 기반 워크플로를 지원하지만 Wiki 기반 워크플로에도 많은 기능이 있었습니다.
지지자; 많은 아이디어가 제시되었지만 확실한 승자는 없었습니다.

그러나 분명한 것은 메일링 리스트와 메일링 리스트가 분리되어 있다는 것입니다.
포럼 "변경 소유자와 다른 사람들에게 실망스러운 부담을 안겨줍니다.
토론을 따르기 위해." 이 프로젝트는 "분할 두뇌"를 시도했습니다.
개발 논의를 위한 접근 방식"을 3년 동안 진행했지만, 그렇지 않았습니다.
일하고 있습니다. 그는 먼저 그 문제점을 해결하는 데 집중하고 그 다음에는
나중에 다른 위키 기반 프로세스에 대한 아이디어를 가지고 다시 오세요.

세계 대부분의 지역이 휴가철이라는 점을 고려하면 좋은 기회가 있습니다.
Fedora의 프로세스를 수정하려는 다양한 노력은 거의 움직임이 없을 것입니다.
다음 달이나 두 달 안에. 그래도 좀 있을 것 같기는 하다.
Fedora 기여자가 휴가에서 돌아오면 프로젝트 프로세스가 개편됩니다.
대화가 중단된 부분부터 다시 시작하세요.

[Comments (11 posted)](https://lwn.net/Articles/1081557/#Comments)


### [Attaching programs to multiple tracepoints](https://lwn.net/Articles/1082948/)

#### 요약
- BPF 추적점 부착물과 BPF LSM 보호처럼 닫히는·보안 확장 관련 토론을 다룹니다.
- 여러 추적점 연결, 규정 반대, 검증자/권한 모델이 BPF 사용에 왜 중요한지 설명합니다.
- BPF가 디버깅 도구는 런타임 보안 경계를 넘어 일부가 있음을 표시합니다.

작성자:
다록 알덴
2026년 7월 22일
LSFMM+BPF[^lwn1083123-bpf-security]
커널의 추적점은 디버깅,
능동 모니터링, 성능 측정 등이 포함됩니다. 이전에는
특정 BPF 프로그램은 단일 추적점에만 연결할 수 있습니다.
지리 올사(Jiri Olsa)는 이를 바꾸기 위해 노력해 왔으며 다음과 같은 토론을 주도했습니다.
2026년 그의 진전
[Linux Storage, Filesystem, Memory-Management, and BPF
Summit](https://events.linuxfoundation.org/lsfmmbpf/). 그 일은 그 이후로
[merged](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c49f336dbcf30ff8622d3725c54fe1c90e8ccd9c)이며 7.2의 일부로 예상될 수 있습니다.
커널.[^lwn1083123-bpf-tracepoints]

커널의 다른 유사한 기능은 여러 첨부 파일을 지원합니다. kprobes
특히 이를 지원하며 추적점과 동일한 작업을 대부분 수행할 수 있습니다. 는
차이점은 성능의 하나라고 Olsa는 말했습니다. 추적점 설정 속도가 더 느립니다.
하지만 실행 속도가 눈에 띄게 빨라졌습니다. 그의
[slides](https://drive.google.com/file/d/132N1l5ndqMQwwOQKbyin38S_821C_3um/view)에는 초당 수백만 건의 실행 횟수에 대한 측정이 포함되었습니다.
각 방법으로 관리할 수 있습니다. 추적점과 kprobe가 정확히 어떻게 되어 있는지에 따라
연결하면 추적점이 약 두 배 정도 빨라질 수 있습니다. 추적점을 만들 수 있는 경우
성능 저하 없이 다중 첨부를 지원하려면
성능에 민감한 작업을 모니터링하는 데 매력적인 옵션이 될 수 있습니다.

그런 다음 Olsa는 추적점이 어떻게 만들어졌는지에 대한 약간의 역사를 살펴보았습니다.
구현되었습니다. 런타임 코드 패치를 사용하여 추적된 코드에서 실행을 리디렉션합니다.
전에 연결된 후크를 실행하는 생성된 트램펄린에 대한 함수
추적된 함수로 돌아갑니다. 원래 추적점은 다음을 사용하여 구현되었습니다.
오래된
트램폴린 간의 일대일 대응을 갖는 [ftrace API](https://lwn.net/Articles/365835/)은,
기능 및
[ftrace objects](https://elixir.bootlin.com/linux/v7.1.3/source/include/linux/ftrace.h#L436). 분명히 지원에 도움이 되지 않습니다.
다중 첨부. 멍롱 동
[tried a different approach](https://lwn.net/ml/all/20250703121521.1874196-1-dongml2@chinatelecom.cn/)는 다음을 사용했습니다.
모든 추적점에 대한 단일 전역 트램폴린. 그게 성과를 냈다.
왜냐하면 트램폴린은 어떤 기능이 사용되었는지 식별해야 했기 때문입니다.
전화를 걸었고 결정을 내리는 데 드는 오버헤드가 너무 높았습니다.

새로운 접근 방식은 단일 사용을 지원하는 최신 ftrace API를 사용하는 것입니다.
ftrace 객체를 사용하여 여러 기능을 구성합니다. 각 기능은 여전히 할당되어 있습니다.
그 자체의
트램펄린이지만 트램펄린 관리는 그룹으로 처리할 수 있습니다.
트램폴린 생성이 빠르기 때문에
한 번에 여러 트램펄린을 재생성하는 것은 성능에 큰 영향을 미치지 않습니다.

새로운 다중 첨부 코드 개발 중 한 가지 문제
잠금 처리였습니다. 원래,
각 트램펄린에는 수정을 위해 코드가 취해야 하는 자체 잠금 장치가 있습니다.
그것. 많은 트램폴린을 동시에 수정해야 할 경우,
결과적으로 코드는 많은 수의 잠금을 사용하고 lockdep과 충돌하게 됩니다.
48 잠금 제한으로 인해 디버깅에 문제가 발생합니다.
해결책은 Andrii Nakryiko가 잠금 장치를 제거하는 것이었습니다.
트램펄린을 사용하고 상황에 따라 공유되는 32개의 자물쇠 풀로 교체하세요.
트램폴린 주소에; 실제로 이는 다음과 같은 경우 거의 동시성을 허용합니다.
자물쇠가 잠시만 잠겨 있기 때문에 트램펄린에 접근할 수 있습니다.

중간 광고
또 다른 문제 - 이는
[Sashiko patch-review system](https://sashiko.dev/) — 입니다
추적점과 라이브 커널 패치 간의 상호 작용. 후자도 사용
라이브 커널 패치가 있을 때 ftrace 하위 시스템에 알리기 위한 ftrace API
추적된 함수를 대체했습니다. 그러한 기능이 있을 때
추적점이 연결되면 ftrace는 추적점 코드에 다음을 알립니다.
트램펄린을 재생성해야 합니다. 그렇게 하려면 트램폴린을 타야 합니다.
잠금이 할당되었지만 스레드가 이미 잠금을 보유하고 있을 수 있습니다(아마도 ftrace에 있을 수 있음).
Olsa가 지정하지는 않았지만) 이후에 획득되는 하위 시스템
다른 코드에 의한 트램펄린의 잠금으로 인해 잠금 반전(교착 상태)이 발생합니다. 이를 해결하기 위해,
코드는 루프에서 잠금을 획득하려고 시도하며 반복 사이에 잠을 자고 있습니다.
스레드가 보유한 모든 뮤텍스를 일시적으로 해제합니다.[^lwn1083123-kernel-patches]

하지만 그것은 버그가 아닙니다. 문제는 라이브 패치가 실행될 때 발생하는 것입니다.
제거되었습니다. 그러한 상황에서는 트램펄린을 다시 교체해야 하지만
잠금 상태는 코드가 잠금을 획득하려고 시도할 수 없는 상태입니다.
루프의 트램펄린 잠금 장치. 따라서 라이브 중에 트램폴린 잠금 장치를 잡고 있으면
패치가 제거되면 트램펄린은 이전 버전을 참조하도록 변경될 수 없습니다.
추적된 함수의 위치. Steven Rostedt는 이 사건이 다음과 같이 이루어져야 한다고 제안했습니다.
라이브 패치 제거 코드가 릴리스를 알 수 있도록 `EAGAIN`을 반환하세요.
잠그고 다시 시도하세요. 다른 개발자는 무시해도 괜찮다고 생각했습니다.
문제는 정확성이 아니라 성능 문제일 뿐임을 설명합니다.
문제는 트램펄린을 재생성하지 않는 유일한 단점이기 때문입니다.
사례는 제거된 패치 위치에서 다시 패치 위치로의 추가 간접 참조입니다.
함수의 원래 위치.

BPF 프로그램을 여러 추적점에 연결하는 실제 API는 상대적으로
간단하고, 프로그램에 대한 포인터를 가져와서, 어떤 것을 지정하는 패턴을 사용합니다.
연결할 추적점 및 선택적 세트
BPF를 허용하는 [cookies](https://grant.pizza/blog/bpf-cookies/)
프로그램은 자신이 호출된 추적점을 알고 있습니다.


```

구조체 bpf_link *
    bpf_program__attach_tracing_multi(
        const 구조체 bpf_program *prog,
        const char *패턴,
        const struct bpf_tracing_multi_opts *opts);
                                     
    구조체 bpf_tracing_multi_opts {
        size_t sz;
        __u32 *id;
        __u64 *쿠키;
        size_t cnt;
        size_t :0;
    };
```

API는 추적 함수 항목, 종료 또는 둘 다를 지원합니다. 지원하지 않습니다
함수의 반환 값을 변경하거나 Linux 보안 모듈에 연결
후크.
Nakryiko는 이것이 디자인의 한계인지, 아니면
다른 종류의 추적점에 대한 지원은 나중에 추가될 수 있습니다. 올사가 확인했습니다
다른 종류도 지원이 가능하다고 생각했지만, 그는 단지
가장 간단한 경우부터. 그는 아직 더 많은 문제를 해결하기 위한 패치를 공유하지 않았습니다.
복잡한 사건.

이 인터페이스의 또 다른 제한 사항은 BPF 검증자가 할 수 있는 것입니다.
따라서 연결된 BPF 프로그램이 수행하는 것이 안전한지 확인하고,
올사가 설명했다. 단일 추적점에 연결할 때 검증자는 다음을 수행할 수 있습니다.
해당 함수의 인수에 대한 BPF 프로그램의 액세스를 확인하고 따라서
BPF 프로그램은 전달된 커널 객체에 대한 모든 포인터를 안전하게 역참조합니다.
기능. 여러 추적점에 연결할 때 추적된 함수는 다음과 같습니다.
서명이 다르기 때문에 검증자는 BPF 프로그램의 내용을 확인할 수 없습니다.
단일 패스로 액세스합니다. 따라서 BPF 프로그램은 여러
Tracepoints는 추적된 함수의 함수 인수를 로드할 수 있습니다.
그러나 거기에서 발견된 포인터를 역참조하지는 않습니다. 그게 제약이거든요
새 API에 대한 성능 문제를 일으키지 않고는 해제하기 어려울 것입니다.
이는 그 이점의 대부분을 제거합니다.

한 사람은 Olsa가 프로그램에 몇 개의 기능을 추가할 것으로 예상하는지 물었습니다.
여러 번 보내면 성능 문제가 발생하는지 여부
트램폴린이 생성되고 연결될 때 IPI(프로세서 간 인터럽트)가 발생합니다.
Olsa는 새 API를 사용하는 대부분의 사용자가 아마도 다음에 연결하고 싶어할 것이라고 생각했습니다.
모든 시스템 호출에 연결하는 등 최대 수백 개의 추적점
구현. 반면에 수백 개의 IPI가 필요하지는 않습니다. 는
ftrace API는 여러 IPI 발행을 방지하기 위해 일부 x86 관련 트릭을 사용합니다. 그
Arm에서는 작동하지 않지만 비교적 쉽게 지원을 추가할 수 있습니다.

Rostedt는 x86에서 이를 처리하기 위한 코드를 작성했음을 확인했습니다.
Arm에 대한 지원을 추가하려면 약간 다른 종류의 코드만 작성하면 됩니다.
트램펄린. Nakryiko는 그 작업을 수행할 계획이 있는지 물었습니다.
Rostedt는 "누군가 그런 일을 한다면 나는 NAK하지 않을 것입니다."라고 대답했습니다.

자세한 내용을 문의하자 Rostedt는 Arm에는 단일 제품이 없다고 설명했습니다.
현재 명령어 포인터를 스택에 푸시하는 명령어
x86의 `call`과 같은 방식으로 주소로 직접 점프합니다. 는
Arm에 대한 동등한 명령어인 `bl`("분기 및 링크")은
레지스터의 이전 명령어 포인터. 그러므로 트램펄린을 패치하는 것은
함수로 만들려면 둘 이상의 명령어를 변경해야 하며, 이로 인해 IPI가 생성됩니다.
CPU가 잘못된 중간 상태를 보지 않도록 보장하는 데 필요합니다.

누군가가 다음을 사용하여 패치할 수 있는 트램폴린을 구현한다면
실행 파일 패치에 대한 Arm의 규칙을 준수하는 방식의 단일 원자 쓰기
코드를 사용하면 x86과 동일한 IPI 방지 트릭을 사용할 수 있으며
여러 개의 추적점이 더 빨라질 것이라고 Olsa는 말했습니다. 그러나 그 시점까지,
세션이 예정된 시간의 끝에 도달하여 토론이 종료되었습니다.
이 글을 쓰는 시점에는 누구도 그런 Arm 트램펄린을 제공하지 않았습니다.
Olsa의 패치 세트는 6월 7일에 병합되었습니다.

[Comments (none posted)](https://lwn.net/Articles/1082948/#Comments)


### [Securing BPF LSMs against tampering](https://lwn.net/Articles/1082111/)

#### 요약
- BPF 추적점 부착물과 BPF LSM 보호처럼 닫히는·보안 확장 관련 토론을 다룹니다.
- 여러 추적점 연결, 규정 반대, 검증자/권한 모델이 BPF 사용에 왜 중요한지 설명합니다.
- BPF가 디버깅 도구는 런타임 보안 경계를 넘어 일부가 있음을 표시합니다.

작성자:
다록 알덴
2026년 7월 17일
LSFMM+BPF
2020년부터 BPF 프로그램은 다음을 수행할 수 있었습니다.
[act as](https://docs.kernel.org/bpf/prog_lsm.html) Linux 보안 모듈
(LSM). systemd를 포함한 여러 프로젝트에서 사용하기 위해 노력해 왔습니다.
사용자에게 더 많은 보안을 제공하는 기능입니다. 크리스티안 브라우너
2026년에 연설함
[Linux Storage, Filesystem, Memory-Management, and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/)
이런 방식으로 BPF를 사용하는 데 따른 몇 가지 제한 사항과 그가 변경한 사항에 대해
systemd의 사용을 확인하고 싶습니다. 특히 그는 다음과 같은 방법을 원합니다.
BPF 프로그램이 제거되거나 개인 데이터가 변조될 수 없는지 확인하십시오.[^lwn1083123-bpf-lsm]

BPF 프로그램이 LSM 후크 또는 기타 커널 리소스에 연결되면
reference-counted: BPF 프로그램을 제출한 사용자 공간 프로그램이
커널은 BPF 프로그램에 대한 파일 설명자를 닫습니다(예:
충돌이 발생함) BPF 프로그램이 자동으로 정리됩니다. 이 디자인은 유지
일이 깔끔하고 BPF 프로그램이 유출되는 것을 방지하지만
BPF LSM에 대한 취약점. 게다가 방해가 되는 경우도 많다.
BPF 맵에 저장된 데이터를 변경하여 BPF 프로그램을 실행합니다.
예상치 못한 방법. BPF 맵은 사용자 공간과의 통신에 자주 사용됩니다.
프로그램이지만 BPF 프로그램의 보조 데이터를 저장하는 데에도 사용할 수 있습니다.
BPF 프로그램은 해당 데이터의 정확성에 의존할 수 있습니다.
Brauner는 이러한 두 가지 동작이 모두 변경되어 BPF 보안이 향상되기를 원합니다.
프로그램은 일단 설치되면 쉽게 피할 수 없습니다.

그가 작업해온 코드는 컴퓨터가 파일만 실행하도록 보장합니다.
유효한
[dm-verity signatures](https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/verity.html), 커널과 유사
[integrity measurement architecture](https://wiki.gentoo.org/wiki/Integrity_Measurement_Architecture)(IMA); 보안상의 이점은 모든 것을 방지한다는 것입니다.
실행 파일을 덮어쓰거나 프로그램을 실행하는 데 의존하는 공격
예상치 못한 위치. 신뢰할 수 있고 수정되지 않은 디스크에서 나온 프로그램만
달릴 수 있습니다. 기본 IMA와 비교하여 BPF에서 검사를 수행하면 다음이 가능합니다.
systemd의 기존 구성과의 더 큰 사용자 정의 및 통합.
해당 코드는 작동 중이며 계획은 이를 systemd에 통합하는 것입니다.

Brauner가 어려움을 겪고 있는 부분은 BPF가
구성 요소 자체는 변조되지 않습니다. "어쩌면 내가 너무 멍청한 것일지도 모르지만, 난 알아냈어
모든 수정으로부터 BPF LSM 프로그램을 보호할 수 있는 확실한 방법은 없습니다." 그는
결국 해결 방법을 찾았습니다. BPF를 사용하여 모든 부분에 연결하는 것입니다.
로드된 BPF 프로그램을 수정할 수 있고 수정을 허용하지 않는 커널
이는 관리할 수 있다고 신뢰되는 init 프로세스에서 제공되지 않습니다.
것들.

이를 돕기 위한 기능이 있다고 그는 덧붙였습니다.
연습만으로는 충분하지 않습니다.
[discussed at the
summit in 2025](https://lwn.net/Articles/1017549/)이었던 서명된 BPF 프로그램은 로드 중에만 보호됩니다. 그들은 아직도 그럴 수 있어
다른 프로그램과 동일한 방식으로 언로드됩니다.
[Exclusive maps](https://lwn.net/Articles/1031854/), 동일한 일부로 도입됨
서명된 BPF 프로그램으로서의 노력은 저장된 데이터 변경 문제를 해결하는 데 도움이 될 수 있습니다.
신뢰할 수 있는 프로그램으로 맵에 대한 액세스를 제한하여 BPF 맵에서 그들은 아니다
그러나 BPF당 하나의 독점 맵으로 제한되기 때문에 완벽한 솔루션입니다.
프로그램이라고 Brauner는 말했습니다. 그의 프로그램에는 7개의 서로 다른 맵이 필요합니다.
그건 모두 보호받아야 해요.

중간 광고
Andrii Nakryiko는 Brauner에게 자신의 해결 방법에 대해 어떻게 느꼈는지 자세히 설명해달라고 요청했습니다.
부족하고 그가 보고 싶은 것이 바뀌었습니다. 문제는 그 사람이
Brauner는 커널의 여러 위치에 사용자 정의 후크를 추가해야 한다고 말했습니다.
BPF 관리자가 다른 기능을 추가하면 이에 대해 알고 업데이트해야 합니다.
그의 BPF 프로그램을 안전하게 유지하기 위해서입니다. 예를 들어 BPF는
프로그램의 뼈대가 init 프로세스에 매핑된 상태로 남아 있다는 것은 그가 다음을 수행해야 함을 의미합니다.
누구든지 수정하지 못하도록 하세요. 이는 다음과 같은 기능을 차단한다는 의미입니다.
[`ptrace()`](https://man7.org/linux/man-pages/man2/ptrace.2.html);
그가 정말로 모든 것을 다뤘는지 확신하기는 어렵습니다
그건 영향을 받을 수 있어요. 그는 표시를 하는 것이 훨씬 더 간단할 것이라고 말했습니다.
BPF 프로그램은 불변이므로 걱정할 필요가 없습니다.

Nakryiko는 또한 자체 보호 BPF 프로그램을 만들었습니다. 로드한 후
프로그램에서 그는 관련된 모든 리소스에 대한 파일 설명자를 기록하고
그런 다음 해당 파일과 관련된 작업을 위해 모든 LSM BPF 후크에 프로그램을 연결합니다.
설명자. 그 해결책은 그에게 효과가 있었습니다. 비록 약간의 추가가 있더라도 말이죠.
프로그램의 복잡성 때문에 그는 실제로 프로그램의 내용을 알지 못합니다.
그 이상은 필요합니다.
Brauner는 Nakryiko가 더 간단한 솔루션에서 유용성을 보지 못했다면 왜 그렇게 했는지 물었습니다.
커널에 독점 맵을 추가하는 데 도움을 주었습니다. Alexei Starovoitov는 설명했습니다.
보안 이외의 이유로 독점 지도가 유용하다고 말하면서
이 기능은 이미 프로그램당 여러 지도를 지원한다고 생각했습니다.

한 청중은 Nakryiko가 제안한 접근 방식에 만족하지 않았습니다.
모든 BPF LSM은 비슷한 작업을 수행하기를 원하므로
커널에서 불변 BPF 프로그램에 대한 지원을 구현하는 것이 더 합리적입니다.
Liam Wiseheart는 수많은 방법이 있다고 지적했습니다.
누군가 로드된 BPF 프로그램을 방해할 수 있는 경우 — 커널 모듈 로드,
원시 메모리 등에 쓰는 것 등이 결국 그는 어떤 종류의 것인지 확신하지 못했습니다.
Brauner가 요구한 완전한 보호는 내부에서도 가능했습니다.
커널.

Nakryiko는 몇 가지 가능한 접근 방식을 브레인스토밍했지만 그 중 어느 것도 성공하지 못했습니다.
Brauner는 완전히 받아들일 수 있습니다. Nakryiko의 제안 대부분은 제한에 의존했습니다.
BPF 프로그램 및 해당 리소스에 대한 파일 설명자에 대한 액세스입니다.
불행히도 이러한 접근 방식은 시스템화되어 있다는 사실로 인해 복잡해졌습니다.
재실행을 지원한다고 Lennart Poettering은 말했습니다.
init 프로세스를 다시 시작하여 열린 프로세스를 전달할 수 있습니다.
파일 설명자. 해결하기가 어렵습니다. Brauner는 결국 그것을 받아들였습니다.
파일 설명자 보호를 기반으로 하는 솔루션이 작동하도록 만들 수 있습니다.
하지만 여전히 너무 복잡할 것이라고 생각했습니다.

Wiseheart가 왜 해당 파일만 고정할 수 없는지 물었습니다.
설명자. Brauner는 그것이 시도되었다고 생각했고 그로 인해 발생했다고 대답했습니다.
파일 설명자를 보호하는 것과 관련된 추가 복잡성
다시 열거나 마운트 해제했습니다. Wiseheart는 계속해서 보호에 회의적이었습니다.
이런 방식의 BPF 프로그램도 가능했습니다. systemd만 허용되더라도
BPF 프로그램과 통신하기 위해 방해할 수 있는 방법은 여전히 많습니다.
실행 중인 프로세스.

Nakryiko는 결국 BPF 프로그램의 참조를 늘리는 것을 제안했습니다.
파일 설명자를 닫아도 참조가 줄어들지 않도록 계산됩니다.
0으로 계산되므로 프로그램은 항상 로드된 상태로 유지됩니다. 그렇지 않습니다
사용자 공간이 프로그램 지도를 방해하는 것을 방지하지만 이는 다음 단계입니다.
올바른 방향. Wiseheart는 사용자 공간에서 지도를 분리하고
해당 ID를 [`bpf()`](https://man7.org/linux/man-pages/man2/bpf.2.html)에 대한 인수로 허용하지 않음
시스템 호출. 브라우너는 이에 동의했다.
그의 사용 사례에서는 초기화 후 사용자 공간에서 지도에 액세스할 필요가 없었습니다.
따라서 사용자 공간에서 BPF 프로그램을 완전히 분리하는 것이 허용되었습니다.

그 시점에서 앞으로 나아갈 디자인은 확정되지는 않았지만 적어도
당분간은 충분히 논쟁의 여지가 있다. Wiseheart는 질문을 계속했습니다.
Brauner가 BPF로 구현하려고 했던 정책이 실행 중인지 여부
유효한 dm-verity 서명이 있는 바이너리)도 가능했습니다. 그는 다음과 같이 지적했다.
uprobes는 사용자 공간 코드의 제어 흐름을 수정하는 데 사용될 수 있습니다.
사용을 허용하다
[return-oriented programming](https://en.wikipedia.org/wiki/Return-oriented_programming) 또는 유사한 기술을 실행
본질적으로 임의의 코드입니다. 또한 스크립팅 언어에 대한 인터프리터가 실행됩니다.
BPF가 일반 파일 액세스와 쉽게 구별할 수 없는 방식으로 프로그램을 실행합니다.

Brauner는 스크립트가 문제라는 데 동의했으며 통역사가 문제를 해결할 것이라고 생각했습니다.
될 필요가
[taught to perform a check similar to what the kernel does](https://lwn.net/Articles/982085/). 와
그 큰 잠재적 허점을 처리하고 실행 파일에 대한 여러 관련 정책을 처리했습니다.
프로그램을 시행할 수 있어야 합니다. 어떤 솔루션인지는 아직 명확하지 않습니다.
BPF 개발자는 구현하지만 인원 수는 제한됩니다.
진정으로 안전한 BPF LSM을 가능하게 만드는 데 관심이 있는 것으로 보입니다.
해결책은 미래의 어느 시점에 나올 것입니다.

[Comments (2 posted)](https://lwn.net/Articles/1082111/#Comments)


### [Merging famfs?](https://lwn.net/Articles/1082687/)

#### 요약
- famfs를 메인라인에 헬멧에 대한 논의와 fabric-attached memory의 파일 시스템 모델을 소개합니다.
- CXL/공유 메모리 환경의 소유권, 일관성, 실패 의미론이 파일 시스템에 영향을 미치게 됩니다.
- 새 하드웨어 메모리 섹션을 Linux ABI로 볼 때 필요한 검토 포인트를 표시합니다.

By
Jake Edge
July 20, 2026
LSFMM+BPF
The [famfs filesystem](https://github.com/cxl-micron-reskit/famfs#famfs-shared-memory-filesystem-framework---user-space-repo), which is meant to provide shared access to huge
memory-resident files on  [CXL](https://en.wikipedia.org/wiki/Compute_Express_Link) and other
devices, returned to
the [Linux Storage,
Filesystem, Memory Management, and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/) (LSFMM+BPF) in 2026.
It was [first discussed at LSFMM+BPF 2024](https://lwn.net/Articles/983105/) and a [new implementation was described at the 2025
gathering](https://lwn.net/Articles/1020170/), but it still has not made its way into the kernel;  LWN [looked
at a discussion about merging famfs](https://lwn.net/Articles/1068686/) back in April 2026.[^lwn1083123-famfs]

John Groves는 자신이 famfs의 창시자이자 유지관리자임을 언급하며 세션을 시작했습니다.
이는 "패브릭 연결 메모리 파일 시스템"입니다.  그는 다음을 위해 일한다
액세스 가능한 대규모 메모리 풀을 갖춘 장치를 만드는 Micron
여러 서버에;
해당 제품은 곧 출시될 예정이지만 조기 액세스가 가능한 사용자는
일부.  이와 같은 "흥미로운 관리 과제"가 있습니다.
devices 및 famfs는 Linux 사용자가 이를 처리할 수 있도록 하기 위한 것입니다.  지난번부터
올해 정상회담에서 그는 소프트웨어 및 시스템 부문의 공동 의장이 되었습니다.
[CXL
Consortium](https://computeexpresslink.org/) 작업 그룹; "그들은 나를 그런 일에 선출하는 나쁜 판단을 했습니다"라고 그는 말했습니다.
웃으며 말했다.

그는 지금까지 famfs의 발전을 보는 두 가지 다른 방식을 가지고 있었습니다.
"2023년부터 VFS와 FUSE의 상황을 더욱 악화시키고 있습니다", 
하지만
파일 시스템 커뮤니티는 "완벽한 적을 만들고 있습니다.
그 기간 동안에도 좋아요."  그는 자신의 세션이 도움이 되기를 바랐습니다.
famfs가 그 길을 갈 수 있도록 "그 일을 멈추는 방법을 찾으십시오"
커널에.


#### 소개

Famfs 소개의 일환으로 Groves는 "famfs는
범용 파일 시스템으로 사용됩니다."  애플리케이션은 단순히
famfs에서 파일을 열고 쓰기 시작합니다. 대신에 그것은 창조를 위한 것입니다.
비희소하고 공유 가능한 메모리에 있는 비희소 파일.  Famfs는 읽기 전용이 아닙니다.
그러나 일반적으로 상당히 정적입니다. 데이터가 그 곳으로 이동된 다음 다음에 대해 액세스됩니다.
분석 또는 기타 처리.

Famfs는 공유 가능한 [DAX](https://docs.kernel.org/filesystems/dax.html) 메모리에 대한 파일 시스템 인터페이스를 제공합니다.  액세스
[`mmap()`](https://man7.org/linux/man-pages/man2/mmap.2.html)로 생성된 지역을 통해 이루어지며,
읽기 및 쓰기는 일반적으로 [`memcpy()`](https://man7.org/linux/man-pages/man3/memcpy.3.html)에 의해 처리됩니다.

여러 호스트가 famfs 파일 시스템을 마운트할 수 있도록 메타데이터가 관리됩니다.
파일을 파일 시스템에 저장하는 단일 마스터 노드가 있습니다.
클라이언트 노드에서 사용할 수 있도록 합니다.  "파일 맵"은 다음을 설명합니다.
여러 DAX 장치의 오프셋 및 범위에 파일을 매핑합니다.
여러 장치에 걸쳐 데이터를 인터리빙하는 것은 성능에 매우 중요합니다. 그게 방법이야
메모리는 시스템 RAM용으로 배치되며 공유용으로 그렇게 되어야 합니다.
메모리 장치도 마찬가지입니다.  그는 인터리빙 메커니즘이 아니라고 말했습니다.
CXL에만 해당되며 다음과 같은 다른 공유 메모리 장치에 사용될 수 있습니다.
DAX 인터페이스를 제공합니다.

Ted Ts'o는 마스터 노드가 생성할 수 있는 유일한 노드인지 물었습니다.
아니면 파일을 쓰세요.  Groves는 가까운 미래에는 오직
마스터는 생성 시 완전히 사전 할당된 파일을 생성할 수 있습니다.
파일에 쓰는 것은 일반적으로 마스터뿐이지만,
고객은 "그리고 당신이 무엇을 하고 있는지에 대한 책임은 당신에게 있습니다.
뭔가 말이 된다."  CXL은 "캐시 일관성을 악화시킵니다",
그는 방 주위를 낄낄 웃으며 말했습니다.

메모리를 위한 [device
mapper](https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/index.html)은 없다고 Groves는 말했습니다. 페이지 테이블, 번역만 있습니다.
TLB(lookaside 버퍼) 및 오류 처리기.  파일 시스템은 브리지할 수 있습니다
그 세계.  그러나 famfs는 스토리지가 아니라 휘발성 메모리일 뿐입니다.
백업 매장.  일반적으로 관심 있는 데이터는 다음 파일에 수집됩니다.
마스터 노드에 의한 일반 파일 시스템(예: XFS)을 생성한 후 famfs에 복사
파일.  그런 다음 클러스터의 각 노드는 famfs 파일 시스템을 마운트하고
파일의 데이터에 대해 워크로드를 실행합니다.

Famf에는 두 가지 별도의 구현이 있습니다. 원래 독립 실행형
버전과 최신 FUSE 기반 파일 시스템.  그는 다음과 같은 접근 방식을 취했습니다.
마운트 시간으로 구별되는 두 구현을 모두 지원합니다.
옵션.  FUSE 버전은 2024년 정상회담에서 논의된 후 나왔습니다.
그리고 그 일을 하는 데 거의 1년이 걸렸습니다.

현재 사용할 수 있는 100TB 어플라이언스가 있지만 이를 위한 메모리는
실제로 2030년까지는 이용할 수 없다”고 말해 웃음을 자아냈다.  하지만
현재 커널에서 사용할 수 있는 추상화가 없습니다.  는
막대한 데이터 세트를 메모리에 저장하는 능력은 문제를 해결할 수 있는 수단을 제공합니다.
현재 현실적으로 불가능한 문제.  애플리케이션은 이미 방법을 알고 있습니다.
파일을 사용하십시오. famfs를 사용하면 이점을 활용하기 위해 다시 작성할 필요가 없습니다.
이 새로운 장치 중.

Amir Goldstein은 Groves에게 "다음을 위해 시간을 좀 절약해야 한다"고 상기시켰습니다.
논쟁 지점", Groves는 맥주를 가져왔다고 농담을 했지만
그는 에서 가정된 것처럼 긴 토론으로 그것을 빼앗길 수 없었다.
4월 LWN 기사.  결국 크리스티안 브라우너는 "무엇을 해야 합니까?"라고 물었습니다.
우리한테 원하는 거야?" 본질적으로 대답은 "famfs 병합"이지만
Groves가 거기에 도착하는 데 약간의 시간이 걸렸습니다.

FUSE 기반 구현의 딜레마는 famfs에 ABI가 필요하다는 것입니다.
파일 맵을 처리하기 위해 FUSE로 변경됩니다.  하지만 FUSE 기반 famfs
독립형 버전만큼 성능이 좋지 않습니다.  그는 "됐어.
1년 동안 FUSE 패치를 적용했습니다." 이 시점에서는 별다른 작업 없이
FUSE 커뮤니티의 응답.  하지만 최근에는
FUSE ABI에 필요한 변경 사항에 대한 이의.


#### BPF?

이러한 ABI 변경에 대한 논의의 일환으로 다음과 같이 제안되었습니다.
BPF는 인터리브 정보를 기반으로 범위를 계산하는 데 사용됩니다.
이를 위해서는 BPF 프로그램을 오류 처리기로 실행해야 합니다.
Groves는 기발한 아이디어이지만 famfs는 성능이 중요하므로 꼭 필요한 것은 아니라고 말했습니다.
아이디어가 실행 가능한지 테스트하기에 좋은 후보입니다.  그 사람은 계속 유지하는 것 같아
그가 X를 변경하면 FUSE 커뮤니티가 이를 받아들일 수도 있지만 이는 사실입니다.
그는 자주 변화하는 환경에 점점 지쳐가고 있음이 분명합니다.

Goldstein은 famfs에 필요한 두 가지 FUSE ABI 변경 사항을 요약했습니다.
어떤 DAX 디바이스가 있는지 확인하고 다른 디바이스는 파일 맵을 제공합니다.
오류를 올바르게 처리할 수 있도록 FUSE 서버에 보냅니다.  그는 물었다
FUSE 관리자인 Miklos Szeredi가 동의한다면 말이죠.
Szeredi는 현재의 famfs 합병에 반대하지 않는다고 말했습니다.  그로서
[discussion
of the FUSE famfs version 10 patch set](https://lwn.net/ml/all/0100019d43e5f632-f5862a3e-361c-4b54-a9a6-96c242a8f17a-000000@email.amazonses.com/)의 [said](https://lwn.net/ml/all/CAJfpegvVTcV89=q3L326aGQjhduBcv7PVg5QKftGLjNZmCLmaw@mail.gmail.com/), 그는
famfs 특정 인터페이스의 대안입니다.  당시 famfs는 날고 있었어
어느 정도 그의 레이더 아래에 있었기 때문에 그는 무엇을 자세히 살펴보지 않았습니까?
그것을 위해 제안되고 있었습니다; BPF 아이디어가 제기되었고 그는 그것에 대해 궁금해합니다.
어떻게 작동할까요?

Christoph Hellwig는 BPF를
그림.  그는 famfs의 문제는 실제로 그다지 중요하지 않다고 말했습니다.
파일 시스템과 전혀 관련이 없습니다.  대신에 매핑 레이어를 적용하는 것입니다.
다른 파일 시스템에서 사용하는 FUSE와는 별도의 FUSE: [iomap](https://lwn.net/Articles/1079415/).  Darrick Wong은 다음과 같은 작업을 해왔습니다.
[implementation of iomap for a FUSE-based ext4](https://lwn.net/ml/linux-fsdevel/177188734044.3935739.1368557343243072212.stgit@frogsfrogsfrogs/) 그
올바른 접근 방식을 취합니다. "우리는 사용자 공간 FUSE 서버가 다음을 수행하기를 원합니다. 
디스크나 물리적 레이아웃에 논리적 오프셋을 매핑하는 것
DAX와 스트라이핑을 포함하는 것이 완전히 합리적입니다."  그는 강하게
"적절한 높은 수준의 인프라" 구축을 제안했지만
이러한 종류의 작업을 파일 시스템별 코드에 숨깁니다.

Groves는 그와 Wong이 몇 달 전에 결합에 대해 이야기했다고 말했습니다.
그들의 작업이지만 그들은 famfs 관련이 있다는 결론에 도달했습니다.
데이터를 인터리빙하는 데 사용되는 반복 패턴입니다.
다른 파일 시스템이 수행해야 하는 작업입니다.

참석자가 FUSE 기반 famfs의 성능 차이에 대해 질문했습니다.
대 독립형.  Groves는 자신이 몇 가지 사항을 측정했지만 알고 있다고 말했습니다.
FUSE는 성능면에서 유명하지 않습니다.  골드스타인은 다음과 같이 지적했다.
파일 맵 전송은 성능에 특별히 민감하지 않습니다.
그로브스는 인정했다.

Groves는 BPF 아이디어의 개념 증명을 실행하려고 시도했습니다.
Gregory Price는 LLM의 "지원"을 받았지만 실패했습니다.
작동시키려면.  가격
LLM에서 사용하는 빌드 환경이 비표준이라는 점에 동의했으며
그가 실험에서 얻은 대부분의 사실은 BPF가
FUSE에 사용하는 것이 좋습니다.

Goldstein은 파일 맵을 설명하는 방법이 있다면 다음과 같이 말했습니다.
Szeredi는 FUSE 프로토콜에 구현 방법을 추가할 의향이 있습니다.
지금 당장은 별로 중요하지 않습니다.  이제 Groves의 코드와 iomap을 사용할 수 있습니다.
예를 들어 나중에.  그렇기 때문에 새로운 것을 일반화하는 것이 중요합니다.
Hellwig는 기능을 말했습니다. Wong의 현재 ext4 코드는 스트라이핑을 수행하지 않지만
다른 커널 파일 시스템(예: Btrfs)에서는 수행하므로 다음과 같은 경우 해당 기능이 필요합니다.
FUSE iomap 코드는 더 광범위하게 사용될 예정입니다.

Hellwig는 Wong과 Groves의 공동 노력을 통해 다음을 추가할 것을 제안했습니다.
famfs 사용 사례 이상의 유용한 인프라를 찾을 수 있습니다.
커널로의 경로가 훨씬 쉬워졌습니다.  다음과 같은 다른 메시지를 보냅니다.
다른 개발자들은 이 기능이 단순한 famfs 이상의 영향을 미친다고 말합니다.  세레디
Wong과 Groves는 이미 공통점을 찾으려고 노력했지만 실패했다고 말했습니다.

그 시점에서 Wong은 원격 링크를 통해 전화를 걸었습니다.  그는 famfs라고 말했다
패턴 기반 범위로 인해 엄청난 수의 매핑이 발생할 수 있습니다.
iomap 기반 구현에서는 커널에 의해 저장되어야 합니다.  파일
예를 들어 2MB 스트라이프를 포함하는 100TB의 용량은 다음과 같은 방대한 범위 목록을 생성합니다.
커널 메모리에 저장해야 합니다.  그 사람 입장에서는 말이 안 되는 일이었는데
famfs가 단순히 해당 정보를 기반으로 계산할 수 있을 때 그렇게 하십시오.
사용하고 있는 패턴입니다. "수억 달러를 업로드하는 건 좀 어리석은 일인 것 같아요.
약간의 매핑을 원하지 않기 때문에 커널에 매핑하는 것
약간의 실행 가능한 코드."  그것이 "미친 BPF"로 이어진 것입니다.
것"이라고 말했고 그는 "끔찍했다"고 말했다.

Hellwig는 줄무늬 패턴의 공식이 잘 알려져 있다고 말했습니다.
오랫동안 확립된; 설명하는 데 사용되는 세 가지 매개변수가 있습니다.
이를 위한 사용자 정의 실행 코드(예: BPF)를 추가하면 안 됩니다.
필요합니다.  Groves는 이에 동의하고 이러한 매개변수가 기본적으로 자신이 갖고 있는 것이라고 말했습니다.
퓨즈에 사용 
파일 맵 프로토콜 메시지. Goldstein은 다른 사람들이 사용할 수 있는 한 다음과 같이 말했습니다.
파일 맵 기능을 자체 목적으로 사용하려면 FUSE에 병합해야 합니다.
메시지 필드의 프로토콜 세부사항 등은 여전히 필요합니다.
그러나 해결되었습니다.

Wong은 Groves의 파일 맵 패치를 가져와 이름을 바꿀 수 있다고 제안했습니다.
FUSE iomap을 사용하여 업스트림으로 가져오려면 "FUSE 맵" 또는 일반적인 항목으로 이동하세요.
일.  골드스타인은 동의했다
그런 일이 가능해야 한다는 것입니다.  그로브스는 농담으로 그게 아닐까 궁금해했다.
2028년 정도까지 기다려야 한다는 의미였지만 Brauner는 다음과 같이 지적했습니다.
방금 누군가가 그를 위해 더 많은 일을 해줄 것을 제안했습니다. 더 많은 웃음을 선사하기 위해서였습니다.
Goldstein은 Wong의 패치가 Groves의 기능을 복잡하게 만드는 것처럼 보일 수 있다고 말했습니다.
하려고 노력 중이지만 상당한 양의 중복이 있고 코드가 너무 많아서
Groves는 famfs에 사용할 수 있습니다.  결국 진전이 이루어졌다고 Goldstein은 말했습니다.
그리고 Groves는 이에 동의했습니다. 따라서 famfs를 위한 앞으로의 길은 다음에서 찾을 수 있기를 바랍니다.
이 점.

[Comments (none posted)](https://lwn.net/Articles/1082687/#Comments)


### [Sched-ext: enqueue() for sub-schedulers and proxy-execution support](https://lwn.net/Articles/1082717/)

#### 요약
- sched_ext의 하위 스케줄러 enqueue()와 프록시 실행 지원 논의를 정리합니다.
- eBPF 기반 검색러 실험이 CPU 배치, 대기 시간, 공정성 제어를 어떻게 바꾸는지 설명합니다.
- 클러스터를 클러스터링하여 실험 가능하게 만들 때의 성능·안정성 트레이드 오프를 표시합니다.

작성자:
조나단 코벳
2026년 7월 16일
는
확장 가능
스케줄러 클래스[^lwn1083123-scheduler]
(sched_ext)는 사용자 정의 CPU 설치를 허용합니다.
스케줄러는 BPF 프로그램 세트입니다.  sched_ext는 현재 형식으로,
이미 많은 흥미로운 스케줄러 개발 작업이 이루어졌습니다.
하위 시스템 자체는 여전히 급속한 발전을 겪고 있습니다.  다른 작업 중에는
계층 구조를 설정하는 능력
하위 스케줄러
완성을 앞두고 있으며,
오랫동안의 비호환성
프록시
처형
끝나가고 있습니다.

#### 하위 스케줄러 인큐 경로

Sched_ext는 원래 구현된 대로 다음의 설치만 허용했습니다.
특정 시스템의 단일 사용자 정의 스케줄러.  시간은 오래 걸리지 않았지만,
다중 테넌트 시스템 사용자가 설정 기능을 요청할 수 있습니다.
다양한 프로세스 그룹에 대한 다양한 스케줄러.  그 결과는
sched_ext 스케줄러를
대조군; 해당 그룹 내의 모든 프로세스는 해당 그룹에 의해 관리됩니다.
첨부된 스케줄러.  일반적인 제어 그룹과 마찬가지로 sched_ext
스케줄러는 상위 레벨 스케줄러와 함께 계층 구조로 배열됩니다.
하위 레벨이 CPU에 프로세스를 배치할 수 있는 시점을 결정합니다.

초기 하위 스케줄러 작업은 7.1 커널 릴리스에 병합되었지만
그것은 불완전하다.  특히 하위 스케줄러가 디스패치를 처리할 수 있습니다.
경로 — 주어진 CPU에서 다음에 실행할 프로세스를 선택합니다.  파견
처리는 상위 그룹 스케줄러가 언제 처리할지 결정한다는 점에서 계층적입니다.
연결된 각 하위 그룹 스케줄러에 대해 디스패치 핸들러를 실행합니다.
디스패칭은 디스패치 큐에서 프로세스를 꺼낼 수 있지만 그렇지 않습니다.
처음부터 해당 대기열에 배치되는 방법을 설명합니다.

[This series](https://lwn.net/ml/all/20260709225041.1695495-1-tj@kernel.org)
허태준이 인큐 경로를 다루었는데, 이는 자연스럽게 다음과 같이 밝혀졌습니다.
그 자체의 복잡성을 가지고 있습니다.  파견측은 상대적으로 쉽습니다.
제어는 스케줄러 계층 구조 아래로 진행되며 각 수준에서는 다음을 결정합니다.
그 아래에 어떤 하위 스케줄러가 주어진 CPU에 작업을 배치하도록 허용되는지
주어진 시간에 대기열에 넣습니다.  하위 스케줄러의 `enqueue()` 콜백,
하지만 언제든지 스케줄러 코어에서 직접 호출할 수 있습니다.
해당 제어 하에 있는 작업이 실행 가능해집니다.  그러면 (현재
커널) 해당 작업을 모든 CPU의 디스패치 큐에 배치합니다.
선점된 작업이 실행되는지 여부에 관계없이 그곳에서 실행 중인 모든 항목을 선점합니다.
동일한 스케줄러의 제어를 받는지 여부입니다.

제어 그룹은 프로세스 그룹 간의 격리를 제공하기 위한 것입니다.
대기열에 추가 경로는 해당 격리를 유지해야 합니다.  일정이 잡혀있기 때문에
성능이 중요한 활동인 경우 대기열에 넣기 경로는 가능하면 다음과 같아야 합니다.
스케줄러 계층 구조를 호출하여
주어진 하위 스케줄러는 특정 배치 결정을 내릴 수 있습니다.  는
그 문제에 대한 대답은 스케줄러가 다음을 수행할 수 있도록 하는 기능 메커니즘입니다.
아래의 하위 스케줄러와 액세스 권한 중 일부를 공유합니다.

하위 스케줄러가 계층 구조에 연결되면 처음에는 액세스할 수 없습니다.
시스템의 모든 CPU에.  그런 다음 해당 부모는 (다음을 호출하여)
`scx_bpf_sub_grant()`) 새 스케줄러에 액세스할 수 있는 기능을 제공합니다.
특정 CPU 세트.  이러한 액세스는 세 가지 수준으로 이루어집니다.
유휴 CPU에 작업을 배치하고 CPU에 작업을 넣는 기능
나중에 실행하기 위한 디스패치 큐와 작업을 선점하는 기능
다른 스케줄러에 의해 제어됩니다.  루트 스케줄러에는 모든 것이 있습니다
모든 CPU의 기능; 그런 다음 그 중 전부 또는 일부를 아래로 전달할 수 있습니다.
이에 연결된 하위 스케줄러입니다.  스케줄러는 기능만 제공할 수 있습니다.
그 자체가 소유한 하위 스케줄러에게.

하위 스케줄러가 작업이 부족한 CPU에 작업을 대기열에 넣으려고 하면
필요한 기능이 없으면 작업은 특수 거부 대기열로 전환됩니다.
그 후에는 동일한 하위 스케줄러에게 다시 전달됩니다.
특수 플래그가 있는 `enqueue()` 콜백
(`SCX_TASK_REENQ_CAP`) 스케줄러에게 다시 시도하라고 지시합니다.  에이
부모가 이전에 부여한 권한을 취소하면 비슷한 일이 발생합니다.
하위 스케줄러: 영향을 받는 CPU에 예약된 모든 작업이 제거됩니다.
그런 다음 새 배치를 위해 하위 스케줄러로 다시 전달됩니다.

이러한 변경으로 인해 하위 스케줄러 작업이 거의 완료되었습니다.
허씨가 자기 소개서에 기재한 몇 가지 세부 사항이 남아 있습니다.
하나는 한 통제 그룹에서 다른 통제 그룹으로 프로세스를 이동하는 것은
그것을 제어하는 하위 스케줄러를 변경하십시오.  다른 하나는 그렇다는 것이다.
제한 가능(예: [`sched_setaffinity()`](https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html) 사용)
CPU 외부의 CPU 집합에 대한 프로세스
하위 스케줄러는 프로세스를 실행할 수 있습니다. 이 경우 프로세스는 종료됩니다.
아무데도 뛰지 못하는 것.  그 상황은 확실히 좋아질 거야
그러나 영향을 받는 프로세스의 소유자는 감사하지 않을 것입니다.
그 개선.

이러한 문제는 추가 작업을 기다려야 합니다.  그 사이 패치는
대기열 경로는 5번의 수정을 거쳤습니다(이 글을 쓰는 시점에서).
현재 7.3 커널 릴리스로 병합하는 작업이 진행 중입니다.


#### 프록시 실행에 익숙해지기

우선순위 역전은 우선순위가 낮은 프로세스가 자원을 보유할 때 발생합니다.
우선순위가 높은 프로세스에 필요하지만 우선순위가 낮은 프로세스는 사용할 수 없습니다.
달리다.  우선순위 상속 — 리소스 보유 프로세스가 다음에서 실행되도록 합니다.
자원을 해제할 때까지 대기 중인 프로세스의 우선순위는
문제에 대해 일반적으로 사용되는 솔루션이지만 우선순위 상속은 그렇지 않습니다.
[deadline scheduling](https://lwn.net/Articles/743740/)에 적용 가능합니다.
마감일 작업은 우선순위를 사용하지 않지만 여전히 차단될 수 있습니다.
다른 프로세스가 보유하는 리소스.

이 경우 해결책은 프록시 실행으로, 이는 다음과 같이 생각할 수 있습니다.
우선순위 상속 아이디어의 확장.  프록시 실행을 사용하면
대기 프로세스의 전체 스케줄링 컨텍스트는
자원을 보유하고 있는 프로세스, 대기 중인 프로세스의 위치에서 실행 가능
(그리고 대기 프로세스의 자원을 사용하여).  프록시가 없는 경우
실행 시 뮤텍스를 차단하는 프로세스는 실행에서 제거됩니다.
대기열.  프록시 실행이 활성화되면 해당 프로세스는 그대로 유지됩니다.
실행 대기열에 있습니다. 스케줄러가 CPU에서 실행하기 위해 이를 선택하면
뮤텍스를 보유하고 있는 프로세스가 뒤따르며, 그 프로세스는 다음과 같습니다.
스케줄링 컨텍스트를 사용하여 그 자리에서 실행됩니다.

이 알고리즘은 커널의 내장 스케줄러에 대해 작동하지만
sched_ext를 사용할 때 혼란이 발생합니다.  sched_ext 스케줄러는 다음을 믿습니다.
어떤 프로세스가 실행되는지 결정했으며, 이를 발견하면 놀랄 것입니다.
다른 프로세스(아마도 완전히 제어할 수 없음)
대신 달리고 있습니다.  이러한 이유로 프록시 실행과 sched_ext가
커널 구성 시스템에서 상호 배타적으로 만들어졌습니다. 커널은 할 수 있다
그 중 하나만 활성화하여 빌드하세요.  다른 건 몰라도 이 상황은
선택할 필요가 없는 유통업체에 문제를 야기합니다.
사용자가 액세스하기를 원하는 두 기능 사이.

이 문제에 대한 잠재적인 해결책은 [this patch set](https://lwn.net/ml/all/20260716132229.61603-1-arighi@nvidia.com)에서 찾을 수 있습니다.
안드레아 리기(Andrea Righi)와 존 스툴츠(John Stultz)로부터.  방법에 두 가지 근본적인 변화가 있습니다.
sched_ext는 프록시 실행과 함께 작동하며 그 중 첫 번째는 대부분의 내용을 숨기는 것입니다.
sched_ext 스케줄러에서 완전히 가져옵니다.  스케줄러가 차단된 항목을 선택할 때
프로세스를 실행하면 잠금 홀더가 대신 투명하게 실행되지만
sched_ext 스케줄러는 해당 리디렉션을 절대 볼 수 없으므로
예약되지 않은 프로세스가 실행되고 있다는 사실에 놀랐습니다.
전혀 통제하지 마세요.  대기 프로세스의 스케줄링 컨텍스트가 사용됩니다.
해당 프로세스에는 잠금 보유자가 사용한 CPU 시간에 대한 요금이 부과됩니다.

프록시 실행 중에 대기 프로세스의 스케줄링 컨텍스트는 다음과 같습니다.
잠금 홀더가 실행 중인 CPU로 이동됩니다.  일단 자물쇠가 있으면
릴리스되면 스케줄링 컨텍스트가 뒤로 이동되고 스케줄러는
(현재 실행 가능한) 프로세스를 다시 대기열에 넣기 위해 호출됩니다.

하지만 이런 일이 발생하기 전에 스케줄러는
프록시 실행에 기꺼이 참여할 sched_ext 코어; 그
새로운 `SCX_OPS_ENQ_BLOCKED` 플래그를 제공하여 수행됩니다.
등록 시간.  스케줄러가 그런 식으로 등록되면
뮤텍스에서 차단된 프로세스는 스케줄러의 프로세스로 전달됩니다.
`SCX_ENQ_BLOCKED` 플래그가 설정된 `enqueue()` 콜백.
그러면 스케줄러는 스케줄링을 처리할지 여부를 결정할 수 있습니다.
특별히 차단된 작업.  이 시리즈에는 [a simple
change](https://lwn.net/ml/all/20260713162112.26785-10-arighi@nvidia.com)부터 `scx_qmap` 스케줄러까지 포함되어 있습니다.
차단된 작업을 즉시 예약하고 무슨 일이 일어나든 선점합니다.
그 시간에 달리고 있어요.  이 "의도적으로 불공평한" 정책은 다음과 같은 의미를 갖습니다.
프록시 실행을 관찰하기 쉽게 만듭니다. 이는 또한 얼마나 적은 양이 필요한지 보여줍니다.
sched_ext 스케줄러가 프록시 실행과 함께 작동하도록 만듭니다.
인프라가 갖추어져 있습니다.

그러나 프록시 실행이 얼마나 잘 작동할지는 다음 요소의 조합에 따라 달라집니다.
시스템의 프로세스.  sched_ext가 일부만 담당하는 경우
실행 중인 프로세스는 실행 중인 프로세스를 선점할 수 없습니다.
sched_ext 외부에는 더 높은 우선순위가 있습니다.  테이블이 있습니다
[this patch](https://lwn.net/ml/all/20260713162112.26785-5-arighi@nvidia.com)의 변경 로그에서
8가지 상황에서 어떤 일이 일어나는지 설명합니다.
대기 프로세스, 잠금 보유자 및 관련되지 않은 프로세스의 스케줄링 상태
CPU에서 경쟁하는 프로세스.

이 시리즈는 현재까지 7번의 개정을 거쳤으며,
7.3 릴리스에 병합됩니다.

[Comments (none posted)](https://lwn.net/Articles/1082717/#Comments)

**페이지 편집자**: 조 브록마이어


## 간략한 항목


### 보안

#### 요약
- PyPI에 대해, GNOME 보안 추적, XZ 백도어 관련 자료 등 공급망·보안 소식을 정리합니다.
- 센서와 릴리스 아티팩트는 보안에 미치는 영향을 설명합니다.
- 보안 사건의 원인이 아니라 생태계 거버넌스가 중요하다는 점을 표시합니다.


### [Catanzaro: Some changes to GNOME security tracking](https://lwn.net/Articles/1083754/)

#### 요약
- GNOME 데스크톱에서 세션 저장/복원 기능이 추가 가능성이 있는 프로젝트를 소개합니다.
- 기존 상태 복원, 컴포지터/툴킷 통합, 사용자 환경 간의 균형을 설명합니다.
- 방해받지 않고 활동할 수 있는 실질적인 존재는 여러 가지 협력을 요구한다는 점을 표시하는 것입니다.

Michael Catanzaro는 이후 GNOME 보안 문제 추적을 관리해 왔습니다.
2020년 11월, 그가 어떻게 할 것인지에 대한 몇 가지 변경 사항을 자세히 설명하는 [blog post](https://blogs.gnome.org/mcatanzaro/2026/07/20/some-changes-to-gnome-security-tracking/)을 작성했습니다.
증가로 인해 지금부터 그놈 취약점 보고서를 관리해야 합니다.
AI가 생성한 보안 보고서. 그는 90일 기한에서 전환할 예정입니다.
8월 1일 이후에 보고된 문제는 30일까지 공개됩니다. "
기한이 짧을수록 그놈에는 더 잘 작동할 것입니다.
AI로 생성된 문제 보고서가 증가했습니다."

또 경영직에서 물러나겠다는 뜻도 밝혔다.
보안 문제는 2026년 12월 1일까지 완전히 추적됩니다.
채워야 할 격차가 될 것입니다:

> 현재 그놈 보안 문제를 추적하는 사람은 아무도 없습니다. 당신이
> 경험이 풍부한 GNOME 커뮤니티 회원이며 이 커뮤니티를 인수하는 데 관심이 있습니다.
> 작업 중이라면 알려주시면 시작하는 데 도움을 드리겠습니다. (보안 추적은
> 신규 이민자에게 좋은 일입니다.)
> 이는 또한 추적 인프라를 개선할 수 있는 기회가 될 수도 있습니다. 나는 사용한다
> [wiki
> page](https://gitlab.gnome.org/Teams/Releng/security/-/wikis/home)이지만 이는 매우 원시적이며 상당한 수동 작업이 필요합니다.
> 유지. 이슈 보고서가 닫힐 때 페이지를 업데이트하는 것을 잊어버리기 쉽습니다.
> 예를 들면. 이상적으로 우리는 위키를 적절한 웹 앱으로 대체할 것입니다.
> 문제의 실제 상태에 따라 동적으로 업데이트됩니다.

[Comments (none posted)](https://lwn.net/Articles/1083754/#Comments)


### [PyPI now rejects new files after 14 days](https://lwn.net/Articles/1084218/)

#### 요약
- PyPI에 대해, GNOME 보안 추적, XZ 백도어 관련 자료 등 공급망·보안 소식을 정리합니다.
- 센서와 릴리스 아티팩트는 보안에 미치는 영향을 설명합니다.
- 보안 사건의 원인이 아니라 생태계 거버넌스가 중요하다는 점을 표시합니다.

Python Software Foundation 보안 개발자 Seth
Larson에는 [announced](https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/)이 있습니다.
[Python Package Index](https://pypi.org/)(PyPI)은 이제 다음과 같은 새 파일을 거부합니다.
14일이 지난 릴리스에 업로드됩니다. 제한사항은 다음과 같습니다.
토큰을 게시하는 경우 이전 릴리스의 중독을 방지하거나
PyPI 프로젝트의 워크플로가 손상되었습니다.[^lwn1083123-pypi-supply-chain]

> 1월 PEP 740(디지털 증명) 중 [discussion
> of this behavior began](https://discuss.python.org/t/restricting-open-ended-releases-on-pypi/43566)
> 2024. 인기 패키지 [LiteLLM
> and Telnyx were compromised](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/) 이후 [restarted
> in March 2026](https://discuss.python.org/t/restricting-open-ended-releases-on-pypi/43566/34)에 대한 논의가 있었습니다. 해당 프로젝트의 Trivy GitHub Action 사용 시 "[mutable
> reference](https://mikael.barbero.tech/blog/post/2026-03-24-stop-trusting-mutable-references/)"으로 인해 이러한 패키지가 손상되었습니다.
> 원래 이 동작에 따른 일부 프로젝트로 인해 논의가 중단되었습니다.
> 이미 게시된 릴리스에 새 Python 버전에 대한 지원을 추가합니다. 어떻게 정량화하려면
> 이 변경 사항은 기존 워크플로에 지장을 줄 수 있으므로 PyPI 데이터베이스가 쿼리되었습니다.
> [projects
> that have published new files to old releases](https://discuss.python.org/t/restricting-open-ended-releases-on-pypi/43566/48)의 경우(이후 경과 일수로 버킷팅됨)
> 릴리스). 나중에 특히 `cp314` 휠이 상단에 대해 쿼리되었습니다.
> 15,000개 패키지, [only
> 56 projects of 15,000](https://discuss.python.org/t/restricting-open-ended-releases-on-pypi/43566/63)가 14일 이상 3.14 호환 휠을 게시했음을 나타냄
> 릴리스가 출시된 후.

LWN [covered](https://lwn.net/Articles/1064693/) LiteLLM 타협
3월에.

[Comments (13 posted)](https://lwn.net/Articles/1084218/#Comments)


### ["Half a Second" — a book on the XZ backdoor](https://lwn.net/Articles/1083466/)

#### 요약
- PyPI에 대해, GNOME 보안 추적, XZ 백도어 관련 자료 등 공급망·보안 소식을 정리합니다.
- 센서와 릴리스 아티팩트는 보안에 미치는 영향을 설명합니다.
- 보안 사건의 원인이 아니라 생태계 거버넌스가 중요하다는 점을 표시합니다.

Adrian Mastronardi는 다음과 같은 책을 발표했습니다.
0.5초
; 그것은
자세히 살펴보고
XZ 백도어 시도[^lwn1083123-xz-backdoor]
2024년. 이 책은 (비무료) 비상업적 목적으로 무료로 사용할 수 있습니다.
파생 없는 CC 라이선스.
> *0.5초*는 그 이야기를 하나의 연속적인 이야기로 전달합니다.
> 혼자서 코드를 관리하다가 지친 자원봉사자
> 인내심을 갖고 전문적으로 조작하여 포기하도록 합니다. 엔지니어
> 반초의 호기심으로 체인을 통해 공격을 포착했습니다.
> 행운과 힘들게 얻은 본능; 그리고 그것을 만든 운영자는
> 신원이 확인된 적이 없으며, 이 책에서는 결코 신원이 확인되지 않을 수도 있다고 주장합니다.

[Comments (16 posted)](https://lwn.net/Articles/1083466/)


### [Security quotes of the week](https://lwn.net/Articles/1083501/)

#### 요약
- PyPI에 대해, GNOME 보안 추적, XZ 백도어 관련 자료 등 공급망·보안 소식을 정리합니다.
- 센서와 릴리스 아티팩트는 보안에 미치는 영향을 설명합니다.
- 보안 사건의 원인이 아니라 생태계 거버넌스가 중요하다는 점을 표시합니다.

> 개척자 모델 출신 사람들이 얼마나 많은지 자랑하는 것을 볼 수 없습니다.
> 수정한 취약점, 발견한 취약점 수만 표시됩니다.

—
다니엘
스텐버그
> 로그 분석을 시작할 때 먼저 프런티어 모델을 사용했습니다.
> 상용 API 뒤에 있습니다. 이것은 작동하지 않았습니다. 분석에는 다음이 필요합니다.
> 대량의 실제 공격 명령 제출, 페이로드 악용,
> 및 C2 아티팩트가 포함되어 있으며 이러한 요청은 공급자에 의해 차단되었습니다.
> 사고 대응자를 식별할 수 없는 안전 가드레일
> 공격자로부터. 대신 GLM 5.2에서 포렌식 분석을 실행했습니다.
> 자체 인프라를 기반으로 하는 개방형 모델입니다. 이건 1초도 안 남았어
> 이점: 공격자 데이터가 없고 그에 대한 자격 증명도 없습니다.
> 참조하여 우리 환경을 떠났습니다.
> 이 경험은 계획할 가치가 있는 격차를 지적합니다. 우리는 모른다
> 탈옥 여부에 관계없이 공격자의 에이전트를 구동하는 모델은 무엇입니까?
> 호스팅 모델 또는 제한되지 않은 개방형 모델; 어느 쪽이든,
> 공격자는 사용 금지 정책에 구속되어 있지만 자체 포렌식 작업은
> 우리가 먼저 호스팅된 모델의 가드레일에 의해 차단되었습니다.
> 노력했습니다. 수비수를 위한 실용적인 교훈: 유능한 모델을 갖추세요
> 사전에 검증되고 준비된 자체 인프라에서 실행할 수 있습니다.
> 가드레일 잠금을 방지하고 공격자 데이터를 유지하기 위한 사고
> 귀하의 환경을 떠나는 데 필요한 자격 증명. 이것은 아니다
> 호스팅된 모델의 안전 조치에 반대하는 주장이며, 우리는
> 이 피드백을 관련 제공자와 공유합니다.

—
포옹
페이스 보도자료
OpenAI 모델의 공격을 받은 후
> HuggingFace는 자체 소프트웨어를 끝까지 활용한 것 같습니다.
> 다운. 그들은 이 수많은 바이브에 임의의 입력을 제공합니다.
> 적대적인 인터넷. 그런 다음 챗봇은 이 결과를 다음 사용자에게 보냅니다.
> 전체 Kubernetes 명령을 실행할 수 있는 서비스 계정
> 통제.
> 이 모든 것이 잘못되면 더 많은 AI로 "분석"합니다. 그러면 그들은
> 더 많은 AI로 패치하세요.

—
데이비드
제라드
[Comments (none posted)](https://lwn.net/Articles/1083501/#Comments)


### 커널 개발

#### 요약
- 이 부분은 "커널 개발" 주제를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.


### [Kernel release status](https://lwn.net/Articles/1084209/)

#### 요약
- 이 버섯은 “[Kernel release status](https://lwn.net/Articles/1084209/)” 게임을 하위로 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

현재 개발 커널은 7.2-rc4입니다.
,
석방됨
7월 19일.
    리누스는 이렇게 말했습니다.
이번 주 내내 나는 사람들이
여름 휴가를 떠나기 시작했는데 숫자를 계산해 보면
제가 틀렸나봐요. 모든 게 꽤 평범해 보이네요.
"
이번 릴리스에서는 14,716개의 비병합 변경 세트가 확인되었습니다.
        2,343명의 개발자 중,
        그 중 481명은 최초의 커널이었습니다.
        기여자.  릴리스 내역은 다음과 같습니다.

> RCDate커밋
> **v7.2-rc1**
> 2026-06-2814395
> 14395
> **v7.2-rc2**
> 2026-07-05433
> 433
> **v7.2-rc3**
> 2026-07-12475
> 475
> **v7.2-rc4**
> 2026-07-19557
> 557

자세한 내용은 [the LWN KSDB v7.2 page](https://lwn.net/ksdb/releases/v7.2/)을 참조하세요.
      더 많은 세부사항.

**안정적인 업데이트**: 대형 [7.1.4](https://lwn.net/Articles/1083463/),
[6.18.39](https://lwn.net/Articles/1083464/) 및
[6.12.96](https://lwn.net/Articles/1083465/) 업데이트가 출시되었습니다.
7월 18일.

The truly massive
[7.1.5](https://lwn.net/ml/all/20260721152552.646164743@linuxfoundation.org) (2,077 commits),
[6.18.40](https://lwn.net/ml/all/20260721152514.750365251@linuxfoundation.org) (1,611),
[6.12.97](https://lwn.net/ml/all/20260721152446.065700225@linuxfoundation.org) (1,276),
[6.6.145](https://lwn.net/ml/all/20260721152441.786066624@linuxfoundation.org) (1,266),
[6.1.178](https://lwn.net/ml/all/20260721152424.521567757@linuxfoundation.org) (1,067),
[5.15.212](https://lwn.net/ml/all/20260721152405.946368001@linuxfoundation.org) (843), and
[5.10.261](https://lwn.net/ml/all/20260721152355.667394603@linuxfoundation.org) (699)
are in the review process; they are due on July 23.

[Comments (none posted)](https://lwn.net/Articles/1084209/#Comments)


### [Quotes of the week](https://lwn.net/Articles/1084199/)

#### 요약
- 이 버섯은 “[Quotes of the week](https://lwn.net/Articles/1084199/)” 게임을 하위로 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

> 음.  우리는 항상 /proc/vmstat가
> 개발자가 쓰레기장을 만들어 추가, 제거 및 추가할 수 있습니다.
> 변경되었습니다.  문서화 실패/파일은 우리의 비밀스러운 방법입니다
> 사용자에게 이것을 말함 ;)

—
앤드류
모튼
> 일요일에 발생한 400개 이상의 CVE에 대한 메타 코멘트입니다.  드디어 좀 조각했어요
> 주말에 시간을 내어 보류 중인 검토 대기열을 따라잡습니다.
> 저는 _너무_ 뒤처져 있었고 마무리 작업에 가까워졌습니다.  모두
> 커널 CVE는 git repo에서 공개적으로 검토됩니다.
> 모두 시청하고 댓글을 달아주세요.  이것들은 모두 보류 중이었습니다.
> 몇 주 동안, 그 일은 누구에게도 놀랄 만한 일이 아니었습니다.
> 유일한 문제는 그것들을 꺼내는 데 이렇게 오랜 시간이 걸린다는 것입니다.
> (6주 연속 컨퍼런스의 엄청난 폭풍으로 인해 발생)
> 및 휴가).

—
그렉 크로아-하트만
[Comments (none posted)](https://lwn.net/Articles/1084199/#Comments)


### 배포판

#### 요약
- 이 축제는 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.


### [Building an Arch Linux aarch64 port for Holo Core (Collabora blog)](https://lwn.net/Articles/1083392/)

#### 요약
- 이 버섯은 “[Building an Arch Linux aarch64 port for Holo Core (Collabora blog)](https://lwn.net/Articles/1083392/)” 게임을 하위로 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

Collabora는 Arch Linux의 포트인 Holo Core에서 Valve와의 작업에 대한 [blog
post](https://www.collabora.com/news-and-blog/news-and-events/building-an-arch-linux-aarch64-port-for-holo-core.html)을 게시했습니다.
Valve의 운영 체제로 aarch64가 사용됩니다.
64비트 Arm Steam Frame 게이밍 시스템. 콜라보라가 출시한
[sources](https://gitlab.steamos.cloud/holo/holo-core-aarch64-preview),
[binary
packages](https://steamdeck-packages.steamos.cloud/holo-core-aarch64-preview/mash-20251118.3/) 및 aarch64 장치용 컨테이너 이미지입니다. 게시물
Arch Linux를 새로운 Linux로 포팅하는 데 따른 몇 가지 과제를 설명합니다.
아키텍처, 그리고 앞으로 해야 할 일:

> 현재까지 개발된 인프라는
> 첫 번째 원칙부터 특정 시점 스냅샷까지 구축
> 다음 단계는 이를 Arch Linux를 추적할 수 있는 시스템으로 구축하는 것입니다.
> 개발되었습니다. 이 작업은 다음의 기초가 될 것입니다.
> Arch Linux를 섀도잉할 수 있는 지속적으로 작동하는 CI 시스템
> 그 자체. 우리는 Arch Linux 프로젝트와 협력하여 Arch를 도울 것입니다.
> 배포판을 `aarch64` 아키텍처로 포팅하려는 노력
> 자동화된 반복 가능한 빌드를 위해 노력합니다.

게시물에는 생성 및 테스트 방법에 대한 지침도 포함되어 있습니다.
x86_64 호스트의 aarch64 빌드 컨테이너(다음을 원하는 사용자용)
집에서 따라해 보지만 64비트 Arm 장치가 부족합니다.

[Comments (6 posted)](https://lwn.net/Articles/1083392/#Comments)


### [Distributions quote of the week](https://lwn.net/Articles/1084217/)

#### 요약
- 이 버섯은 “[Distributions quote of the week](https://lwn.net/Articles/1084217/)” 게임을 하위로 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

> 유통자로서 어떤 종류의 제품이 있는지 정리해야 할 것 같습니다.
> 업스트림 개발자들과 갖고 싶은 관계
> 귀하가 제공하는 소프트웨어.
> 먼 관계를 맺고 싶나요? **그럼 나는
> 개별 릴리스를 포기하고 *롤링 방식을 채택할 것을 권장합니다.
> 릴리스* 접근 방식.**
> 이 모델에서는 소프트웨어가 출시되는 순간 업스트림 소프트웨어를 사용하게 됩니다.
> — 또는 적어도 그 직후. 그러면 갈등이 사라집니다! 거의
> 모든 버그는 업스트림 버그가 되며 사용자를 업스트림으로 안내할 수 있습니다.
> 개발자로부터 어떠한 반발도 받지 않고. 남은 모든 것은
> OS에서 해결할 수 있는 문제입니다.
> 롤링 릴리스 OS는 여전히 다른 OS와 좋은 관계를 유지할 수 있습니다.
> 물론 업스트림이죠. 그러나 그다지 중요하지는 않습니다.
> 롤링 릴리스가 되고 싶지 않으신가요? 괜찮습니다. **그렇다면 해야 할 일
> 업스트림과 긴밀히 협력합니다.**

—
네이트
그레이엄
[Comments (18 posted)](https://lwn.net/Articles/1084217/#Comments)


### 개발

#### 요약
- 이 부분은 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.


### [Firefox 153 released](https://lwn.net/Articles/1083981/)

#### 요약
- 이 버섯은 “[Firefox 153 released](https://lwn.net/Articles/1083981/)” 게임을 하위로 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

Firefox 웹 브라우저의 [Version
153.0](https://www.firefox.com/en-US/firefox/153.0/releasenotes/)이 출시되었습니다. 주목할만한
이번 릴리스의 변경 사항에는 기본값 변경이 포함됩니다.
확장에 대한 로컬 파일 액세스 권한, LAN 활성화
기본적으로 모든 사용자에 대한 제한, 웹이 작동할 때 시각적 표시
사이트는 사용자의 위치에 접근할 수 있고 PDF를 병합할 수 있으며
PDF 내에 이미지를 페이지로 추가하고 실험적으로 지원합니다.
[JPEG XL](https://jpegxl.info/) 이미지 형식.

참조
웹 개발자에게 영향을 미치는 모든 변경 사항은 [release
notes for developers](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/153),
이 릴리스에서 해결된 취약점은 [security
advisories](https://www.mozilla.org/en-US/security/advisories/mfsa2026-68/)입니다.

[Comments (25 posted)](https://lwn.net/Articles/1083981/)


### [Development quotes of the week](https://lwn.net/Articles/1083468/)

#### 요약
- 이 버섯은 “[Development quotes of the week](https://lwn.net/Articles/1083468/)” 게임을 하위로 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

> 유지관리자의 소진은 이미 문제가 되었으며, 유지관리자의 죽음은
> FOSS가 점점 더 예전처럼 보이기 때문에 빈도가 증가합니다.
> 나팔바지나 플라워파워 같은 세대적인 것.
> 견습 유지보수 담당자를 유인하여 내 교체를 시도합니다.
> 선량한 사람들의 세대는 이미 지는 제안이며,
> 관리자의 역할이 무료라면 전혀 일어나지 않을 것입니다.
> 표지판에 칠해진 페인트가 아직 젖어 있는 동안 "FOSS 관리인" 및 "FOSS
> 제조업체는 동일한 소프트웨어로 반죽을 긁어 모았습니다.
> "자비로운 종신독재자" 시대 FOSS 메인테이너들은 다음과 같습니다.
> 내 자신이 끝나가고 있습니다. 미래에는 모든 결과적인 FOSS가
> 프로젝트는 FOSS가 임명한 위원회에 의해 유지됩니다.
> 청지기 또는 FOSS 회사.

—
폴헤닝 캠프
> 커먼즈가 없습니다. 다른 사람의 인프라에 DoS를 수행하는 것일 뿐입니다.

—
스테파노 자치롤리
[Comments (none posted)](https://lwn.net/Articles/1083468/#Comments)

**페이지 편집자**: Daroc Alden


## 공지사항


### 뉴스레터

#### 요약
- 이 축제는 “Newsletters” 주제를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.


### 배포 및 시스템 관리

#### 요약
- 이 버섯은 “배포 및 시스템 관리” 테마를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

재정의요약
DistroWatch 주간
7월 20일
재정의요약
이번 주 F-Droid에서는
7월 16일
재정의요약
금주의 openSUSE Tumbleweed 리뷰
7월 17일
재정의요약
우분투 주간 뉴스
7월 13일

### 개발

#### 요약
- 이 부분은 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

재정의요약
이맥스 뉴스
7월 20일
재정의요약
git.git에서는 무엇을 요리하고 있나요?
7월 16일
재정의요약
git.git에서는 무엇을 요리하고 있나요?
7월 19일
재정의요약
git.git에서는 무엇을 요리하고 있나요?
7월 20일
재정의요약
이번 주 그놈
7월 17일
재정의요약
GNU 도구 주간 뉴스
7월 19일
재정의요약
골랑 주간
7월 17일
재정의요약
지난 주 Kubernetes 개발
7월 16일
재정의요약
LLVM 주간
7월 20일
재정의요약
이번 주 매트릭스
7월 17일
재정의요약
OCaml 주간 뉴스
7월 21일
재정의요약
펄 주간
7월 20일
재정의요약
이번 주 플라즈마
7월 18일
재정의요약
PyCoder의 주간
7월 21일
재정의요약
Python 코어 파견
7월 18일
재정의요약
이번 달 Radicle CI
7월 22일
재정의요약
루비 주간 뉴스
7월 16일
재정의요약
이번 주 Rust에서
7월 15일
재정의요약
위키미디어 기술 뉴스
7월 20일

### 회의록

#### 요약
- 이 부분은 “회의록” 주제를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

재정의요약
GNU 툴체인 업무 시간
7월 16일
재정의요약
openSUSE 릴리스 엔지니어링 회의록
7월 16일
재정의요약
openSUSE 릴리스 엔지니어링 회의록
7월 22일

### 프레젠테이션 요청

#### 요약
- 이 버섯은 “Calls for Presentations” 주제를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.


### CFP 마감일: 2026년 7월 23일부터 2026년 9월 21일까지

#### 요약
- 이 뮤직은 “CFP 마감일: 2026년 7월 23일 ~ 2026년 9월 21일” 테마를 기지국으로 LWN의 관련 소식과 독창적인 내용을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

다음 CFP 마감일 목록은
LWN.net CFP 캘린더
.

| Deadline | Event Dates | Event | Location |
| --- | --- | --- | --- |
| July 31 | October 14 October 17 | PyCon South Africa | Cape Town, South Africa |
| July 31 | October 1 October 2 | embedded Linux for Safe and Secure Applications | Göttingen, Germany |
| July 31 | September 25 September 27 | PostmarketOS and Alpine Linux Conference | Aachen, Germany |
| August 1 | September 28 October 1 | Alpine Linux Persistence and Storage Summit | Lizumerhütte, Tyrol, Austria |
| August 1 | August 25 August 30 | MiniDebConf and MiniDebCamp Winterthur 2026 | Winterthur, Switzerland |
| August 11 | October 6 | Yocto Project Developer Day 2026 | Prague, Czechia |
| August 31 | October 2 October 4 | GNU Tools Cauldron | Prague, Czechia |
| August 31 | October 3 October 4 | Linux Days 2026 | Prague, Czechia |

귀하의 이벤트에 대한 CFP 마감일이 여기에 표시되지 않는 경우,
[tell us about it](https://lwn.net/Calendar/new/).


### 다가오는 이벤트

#### 요약
- 이 축제는 “Upcoming Events” 주제를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.


### 이벤트: 2026년 7월 23일부터 2026년 9월 21일까지

#### 요약
- 이 축제는 “이벤트: 2026년 7월 23일부터 2026년 9월 21일까지” 테마를 배포하여 LWN의 관련 소식과 역사적 내용을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

다음 이벤트 목록은 다음에서 가져왔습니다.
LWN.net 캘린더
.

| Date(s) | Event | Location |
| --- | --- | --- |
| July 20 July 25 | DebConf 26 | Santa Fe, Argentina |
| August 6 August 9 | FOSSY 2026 | Vancouver, Canada |
| August 8 August 9 | UbuCon Asia 2026 @ COSCUP | Taipei, Taiwan |
| August 11 August 12 | Open Source Summit Korea | Seoul, South Korea |
| August 14 August 16 | Hackers on Planet Earth | New York, NY, US |
| August 25 August 30 | MiniDebConf and MiniDebCamp Winterthur 2026 | Winterthur, Switzerland |
| August 30 September 5 | FOSS4G Hiroshima 2026 | Hiroshima, Japan |
| September 17 September 18 | Git Merge | Lisbon, Portugal |
| September 19 September 20 | Nextcloud Community Conference 2026 | Berlin, Germany |

귀하의 이벤트가 여기에 표시되지 않으면,
[tell us about it](https://lwn.net/Calendar/new/).


### 보안 업데이트

#### 요약
- PyPI에 대해, GNOME 보안 추적, XZ 백도어 관련 자료 등 공급망·보안 소식을 정리합니다.
- 센서와 릴리스 아티팩트는 보안에 미치는 영향을 설명합니다.
- 보안 사건의 원인이 아니라 생태계 거버넌스가 중요하다는 점을 표시합니다.


### [Alert summary July 16, 2026 to July 22, 2026](https://lwn.net/Articles/1084215/)

#### 요약
- 주목할만한 배포판 보안 업데이트와 자문 목록을 추적하는 것으로 정리합니다.
- 패키지명, 권고 ID, 버전 연결을 참조하여 실제 패치 여부를 확인할 수 있습니다.
- 운영 환경에서는 CVE 제목보다 배포판별 백포트와 업데이트 적용 상태가 중요함을 표시합니다.


| Dist. | ID | Release | Package | Date |
| --- | --- | --- | --- | --- |
| AlmaLinux | ALSA-2026:36196 | 10 | 389-ds-base | 2026-07-21 |
| AlmaLinux | ALSA-2026:42096 | 10 | c-ares | 2026-07-21 |
| AlmaLinux | ALSA-2026:39309 | 9 | capstone | 2026-07-20 |
| AlmaLinux | ALSA-2026:39576 | 9 | cifs-utils | 2026-07-16 |
| AlmaLinux | ALSA-2026:38504 | 8 | container-tools:rhel8 | 2026-07-16 |
| AlmaLinux | ALSA-2026:39316 | 9 | cups | 2026-07-15 |
| AlmaLinux | ALSA-2026:41988 | 10 | dovecot | 2026-07-21 |
| AlmaLinux | ALSA-2026:25902 | 10 | fence-agents | 2026-07-20 |
| AlmaLinux | ALSA-2026:36203 | 10 | freerdp | 2026-07-21 |
| AlmaLinux | ALSA-2026:40751 | 9 | gimp | 2026-07-20 |
| AlmaLinux | ALSA-2026:39272 | 10 | git-lfs | 2026-07-15 |
| AlmaLinux | ALSA-2026:39319 | 9 | git-lfs | 2026-07-15 |
| AlmaLinux | ALSA-2026:42063 | 10 | glib2 | 2026-07-21 |
| AlmaLinux | ALSA-2026:42090 | 8 | glib2 | 2026-07-21 |
| AlmaLinux | ALSA-2026:42089 | 9 | glib2 | 2026-07-21 |
| AlmaLinux | ALSA-2026:36675 | 10 | gstreamer1-plugins-good | 2026-07-21 |
| AlmaLinux | ALSA-2026:36673 | 10 | gstreamer1-plugins-ugly-free | 2026-07-21 |
| AlmaLinux | ALSA-2026:39976 | 10 | hplip | 2026-07-21 |
| AlmaLinux | ALSA-2026:40894 | 8 | hplip | 2026-07-20 |
| AlmaLinux | ALSA-2026:40831 | 9 | hplip | 2026-07-20 |
| AlmaLinux | ALSA-2026:41906 | 9 | httpd | 2026-07-21 |
| AlmaLinux | ALSA-2026:40895 | 9 | jackson-annotations, jackson-core, jackson-databind, jackson-jaxrs-providers, and jackson-modules-base | 2026-07-20 |
| AlmaLinux | ALSA-2026:39494 | 10 | kernel | 2026-07-15 |
| AlmaLinux | ALSA-2026:42552 | 8 | kernel | 2026-07-21 |
| AlmaLinux | ALSA-2026:42550 | 8 | kernel-rt | 2026-07-21 |
| AlmaLinux | ALSA-2026:36832 | 9 | libreoffice | 2026-07-16 |
| AlmaLinux | ALSA-2026:39315 | 9 | libsolv | 2026-07-15 |
| AlmaLinux | ALSA-2026:41892 | 10 | libtiff | 2026-07-20 |
| AlmaLinux | ALSA-2026:39317 | 9 | libxml2 | 2026-07-15 |
| AlmaLinux | ALSA-2026:40841 | 8 | maven:3.8 | 2026-07-20 |
| AlmaLinux | ALSA-2026:41947 | 8 | nodejs:22 | 2026-07-21 |
| AlmaLinux | ALSA-2026:39868 | 8 | nodejs:24 | 2026-07-16 |
| AlmaLinux | ALSA-2026:39323 | 9 | pacemaker | 2026-07-20 |
| AlmaLinux | ALSA-2026:39547 | 10 | perl-XML-LibXML | 2026-07-21 |
| AlmaLinux | ALSA-2026:39878 | 8 | perl-XML-LibXML | 2026-07-16 |
| AlmaLinux | ALSA-2026:39553 | 9 | perl-XML-LibXML | 2026-07-16 |
| AlmaLinux | ALSA-2026:39893 | 8 | python3.12 | 2026-07-16 |
| AlmaLinux | ALSA-2026:39771 | 9 | python3.12 | 2026-07-15 |
| AlmaLinux | ALSA-2026:40856 | 10 | python3.14 | 2026-07-20 |
| AlmaLinux | ALSA-2026:41949 | 9 | python3.14 | 2026-07-21 |
| AlmaLinux | ALSA-2026:39798 | 9 | python3.9 | 2026-07-15 |
| AlmaLinux | ALSA-2026:42088 | 8 | webkit2gtk3 | 2026-07-21 |
| AlmaLinux | ALSA-2026:42062 | 9 | webkit2gtk3 | 2026-07-21 |
| AlmaLinux | ALSA-2026:39573 | 10 | yggdrasil | 2026-07-21 |
| Debian | DLA-4687-1 | LTS | chromium | 2026-07-16 |
| Debian | DSA-6390-1 | stable | chromium | 2026-07-16 |
| Debian | DLA-4686-1 | LTS | dhcpcd5 | 2026-07-15 |
| Debian | DLA-4688-1 | LTS | kernel | 2026-07-18 |
| Debian | DSA-6393-1 | stable | kernel | 2026-07-21 |
| Debian | DLA-4689-1 | LTS | libnfs | 2026-07-19 |
| Debian | DLA-4694-1 | LTS | nss | 2026-07-22 |
| Debian | DSA-6389-1 | stable | ntfs-3g | 2026-07-15 |
| Debian | DLA-4693-1 | LTS | roundcube | 2026-07-22 |
| Debian | DSA-6391-1 | stable | roundcube | 2026-07-19 |
| Debian | DLA-4691-1 | LTS | rtpengine | 2026-07-21 |
| Debian | DLA-4692-1 | LTS | samba | 2026-07-21 |
| Debian | DSA-6392-1 | stable | tiff | 2026-07-19 |
| Debian | DLA-4690-1 | LTS | xz-utils | 2026-07-21 |
| Fedora | FEDORA-2026-b45924b5e5 | F44 | ImageMagick | 2026-07-17 |
| Fedora | FEDORA-2026-50e5126be4 | F43 | ansible-collection-ansible-posix | 2026-07-17 |
| Fedora | FEDORA-2026-0f941ecaa6 | F44 | ansible-collection-ansible-posix | 2026-07-17 |
| Fedora | FEDORA-2026-d9ca28a7b8 | F43 | antlr4-project | 2026-07-19 |
| Fedora | FEDORA-2026-619f648cde | F44 | antlr4-project | 2026-07-19 |
| Fedora | FEDORA-2026-131c82812a | F44 | btrbk | 2026-07-22 |
| Fedora | FEDORA-2026-d70d93fcd7 | F43 | c-ares | 2026-07-21 |
| Fedora | FEDORA-2026-32e3e23696 | F43 | chromium | 2026-07-18 |
| Fedora | FEDORA-2026-7437330b17 | F44 | chromium | 2026-07-18 |
| Fedora | FEDORA-2026-1c78e384e3 | F43 | dnsx | 2026-07-21 |
| Fedora | FEDORA-2026-902340971e | F44 | dnsx | 2026-07-21 |
| Fedora | FEDORA-2026-965be97ac0 | F43 | erlang | 2026-07-19 |
| Fedora | FEDORA-2026-dcf80dc1ff | F44 | erlang | 2026-07-19 |
| Fedora | FEDORA-2026-365cce949c | F43 | firefox | 2026-07-17 |
| Fedora | FEDORA-2026-51c2920764 | F44 | firefox | 2026-07-16 |
| Fedora | FEDORA-2026-fa672d26a8 | F43 | freerdp | 2026-07-21 |
| Fedora | FEDORA-2026-a9bfa4361b | F44 | freerdp | 2026-07-17 |
| Fedora | FEDORA-2026-d31eea6f5e | F44 | freerdp | 2026-07-21 |
| Fedora | FEDORA-2026-36e3aa0593 | F44 | gpsd | 2026-07-21 |
| Fedora | FEDORA-2026-f1fc7772c3 | F43 | kernel | 2026-07-22 |
| Fedora | FEDORA-2026-2dd8b600bb | F44 | kernel | 2026-07-22 |
| Fedora | FEDORA-2026-538c26f96a | F44 | libreswan | 2026-07-21 |
| Fedora | FEDORA-2026-9afc6b6bb3 | F43 | libseccomp | 2026-07-21 |
| Fedora | FEDORA-2026-752186819e | F44 | libseccomp | 2026-07-20 |
| Fedora | FEDORA-2026-feac063d56 | F43 | libtiff | 2026-07-21 |
| Fedora | FEDORA-2026-cfbf964c2e | F44 | libtiff | 2026-07-18 |
| Fedora | FEDORA-2026-31a8569c4b | F43 | log4cxx | 2026-07-18 |
| Fedora | FEDORA-2026-8d954936a5 | F44 | mbedtls | 2026-07-20 |
| Fedora | FEDORA-2026-8e39f35701 | F43 | mingw-glib2 | 2026-07-17 |
| Fedora | FEDORA-2026-7bf2937528 | F44 | mingw-glib2 | 2026-07-17 |
| Fedora | FEDORA-2026-9dbf4d0ca8 | F43 | mingw-python-idna | 2026-07-21 |
| Fedora | FEDORA-2026-db2b7b6415 | F44 | mingw-python-idna | 2026-07-21 |
| Fedora | FEDORA-2026-71562f8836 | F43 | mingw-python-pip | 2026-07-21 |
| Fedora | FEDORA-2026-6edc44733c | F44 | mingw-python-pip | 2026-07-21 |
| Fedora | FEDORA-2026-d815916e2c | F44 | mupdf | 2026-07-22 |
| Fedora | FEDORA-2026-5924722657 | F43 | node-exporter | 2026-07-18 |
| Fedora | FEDORA-2026-d36ca2dd19 | F43 | nuclei | 2026-07-22 |
| Fedora | FEDORA-2026-3a8abe43fb | F44 | nuclei | 2026-07-22 |
| Fedora | FEDORA-2026-fb48505840 | F43 | opam | 2026-07-19 |
| Fedora | FEDORA-2026-239dbbff34 | F44 | opam | 2026-07-19 |
| Fedora | FEDORA-2026-169fd93089 | F43 | openssh | 2026-07-21 |
| Fedora | FEDORA-2026-c9d8542bb3 | F44 | openssh | 2026-07-19 |
| Fedora | FEDORA-2026-7b98f6d033 | F43 | perl-Crypt-OpenSSL-X509 | 2026-07-22 |
| Fedora | FEDORA-2026-df7ecb3577 | F44 | perl-Crypt-OpenSSL-X509 | 2026-07-22 |
| Fedora | FEDORA-2026-71d7e4d1da | F43 | perl-DBI | 2026-07-17 |
| Fedora | FEDORA-2026-8cec3cbf5b | F44 | perl-HTTP-Date | 2026-07-17 |
| Fedora | FEDORA-2026-38f958d25a | F43 | perl-Imager | 2026-07-16 |
| Fedora | FEDORA-2026-5f5efe281d | F44 | perl-Imager | 2026-07-16 |
| Fedora | FEDORA-2026-75a8969e55 | F43 | proftpd | 2026-07-18 |
| Fedora | FEDORA-2026-2f95481529 | F44 | proftpd | 2026-07-18 |
| Fedora | FEDORA-2026-574496d9ae | F43 | python-asyncssh | 2026-07-20 |
| Fedora | FEDORA-2026-1f248487e4 | F44 | python-asyncssh | 2026-07-20 |
| Fedora | FEDORA-2026-31ec71cf0b | F43 | python-bcrypt | 2026-07-16 |
| Fedora | FEDORA-2026-65b6511854 | F44 | python-bcrypt | 2026-07-16 |
| Fedora | FEDORA-2026-595d35a4d1 | F44 | python-django5 | 2026-07-18 |
| Fedora | FEDORA-2026-17c484fafa | F44 | python-libcst | 2026-07-18 |
| Fedora | FEDORA-2026-c8f1a4ee05 | F43 | python-orjson | 2026-07-19 |
| Fedora | FEDORA-2026-dd78d37ecf | F44 | python-orjson | 2026-07-19 |
| Fedora | FEDORA-2026-fc2ded926e | F43 | python-pillow | 2026-07-21 |
| Fedora | FEDORA-2026-8abedbcc4f | F43 | python-tiktoken | 2026-07-16 |
| Fedora | FEDORA-2026-e0bcb90c9f | F44 | python-tiktoken | 2026-07-16 |
| Fedora | FEDORA-2026-8893ec1aeb | F43 | python-uv-build | 2026-07-19 |
| Fedora | FEDORA-2026-be84487fdd | F44 | python-uv-build | 2026-07-19 |
| Fedora | FEDORA-2026-c3351f4ae4 | F43 | roundcubemail | 2026-07-16 |
| Fedora | FEDORA-2026-517daa8d64 | F44 | roundcubemail | 2026-07-16 |
| Fedora | FEDORA-2026-7b7c2b373e | F43 | ruby | 2026-07-18 |
| Fedora | FEDORA-2026-32d5a3d450 | F44 | ruby | 2026-07-18 |
| Fedora | FEDORA-2026-8893ec1aeb | F43 | rust-astral_async_zip | 2026-07-19 |
| Fedora | FEDORA-2026-be84487fdd | F44 | rust-astral_async_zip | 2026-07-19 |
| Fedora | FEDORA-2026-6d5a7be3b9 | F43 | rust-cargo-rpmstatus | 2026-07-17 |
| Fedora | FEDORA-2026-08f5aab9ed | F44 | rust-cargo-rpmstatus | 2026-07-17 |
| Fedora | FEDORA-2026-659cb50390 | F43 | rust-fern | 2026-07-22 |
| Fedora | FEDORA-2026-ec9f1ca21a | F44 | rust-fern | 2026-07-22 |
| Fedora | FEDORA-2026-ec9f1ca21a | F44 | rust-ifcfg-devname | 2026-07-22 |
| Fedora | FEDORA-2026-5e3ab17662 | F43 | rust-opendal | 2026-07-17 |
| Fedora | FEDORA-2026-e465328a8d | F44 | rust-opendal | 2026-07-17 |
| Fedora | FEDORA-2026-659cb50390 | F43 | rust-routinator | 2026-07-22 |
| Fedora | FEDORA-2026-ec9f1ca21a | F44 | rust-routinator | 2026-07-22 |
| Fedora | FEDORA-2026-659cb50390 | F43 | rust-rpki | 2026-07-22 |
| Fedora | FEDORA-2026-ec9f1ca21a | F44 | rust-rpki | 2026-07-22 |
| Fedora | FEDORA-2026-659cb50390 | F43 | rust-syslog | 2026-07-22 |
| Fedora | FEDORA-2026-ec9f1ca21a | F44 | rust-syslog | 2026-07-22 |
| Fedora | FEDORA-2026-77f23c0bc4 | F43 | spoofdpi | 2026-07-18 |
| Fedora | FEDORA-2026-812049f95c | F44 | spoofdpi | 2026-07-18 |
| Fedora | FEDORA-2026-8893ec1aeb | F43 | uv | 2026-07-19 |
| Fedora | FEDORA-2026-be84487fdd | F44 | uv | 2026-07-19 |
| Fedora | FEDORA-2026-1b91a2f126 | F44 | wget1 | 2026-07-21 |
| Fedora | FEDORA-2026-bc152c9ff6 | F44 | wireshark | 2026-07-21 |
| Fedora | FEDORA-2026-bd0a75766f | F43 | xrdp | 2026-07-16 |
| Fedora | FEDORA-2026-05c06fa0a8 | F44 | xrdp | 2026-07-16 |
| Fedora | FEDORA-2026-990cdd8329 | F43 | yq | 2026-07-18 |
| Fedora | FEDORA-2026-710adfa806 | F44 | yq | 2026-07-18 |
| Mageia | MGASA-2026-0258 | 10, 9 | bind | 2026-07-18 |
| Mageia | MGASA-2026-0271 | 10 | clamav | 2026-07-19 |
| Mageia | MGASA-2026-0270 | 10 | erlang | 2026-07-19 |
| Mageia | MGASA-2026-0276 | 10, 9 | golang | 2026-07-20 |
| Mageia | MGASA-2026-0282 | 10, 9 | graphicsmagick | 2026-07-20 |
| Mageia | MGASA-2026-0275 | 10, 9 | haveged | 2026-07-20 |
| Mageia | MGASA-2026-0262 | 10, 9 | libidn | 2026-07-18 |
| Mageia | MGASA-2026-0259 | 10, 9 | libreoffice | 2026-07-18 |
| Mageia | MGASA-2026-0273 | 10, 9 | libssh2 | 2026-07-20 |
| Mageia | MGASA-2026-0279 | 10, 9 | nginx | 2026-07-20 |
| Mageia | MGASA-2026-0280 | 10, 9 | nilfs-utils | 2026-07-20 |
| Mageia | MGASA-2026-0268 | 10, 9 | nmap | 2026-07-19 |
| Mageia | MGASA-2026-0257 | 10, 9 | nodejs | 2026-07-18 |
| Mageia | MGASA-2026-0253 | 10, 9 | openssl | 2026-07-15 |
| Mageia | MGASA-2026-0266 | 10, 9 | perl-Bytes-Random-Secure | 2026-07-19 |
| Mageia | MGASA-2026-0286 | 10 | perl-CGI-Session | 2026-07-20 |
| Mageia | MGASA-2026-0267 | 10, 9 | perl-CSS-Minifier-XS | 2026-07-19 |
| Mageia | MGASA-2026-0263 | 10, 9 | perl-Config-IniFiles | 2026-07-19 |
| Mageia | MGASA-2026-0264 | 10, 9 | perl-HTML-Parser | 2026-07-19 |
| Mageia | MGASA-2026-0284 | 10, 9 | perl-Imager | 2026-07-20 |
| Mageia | MGASA-2026-0283 | 10, 9 | perl-JavaScript-Minifier-XS | 2026-07-20 |
| Mageia | MGASA-2026-0269 | 10, 9 | perl-Mojolicious | 2026-07-19 |
| Mageia | MGASA-2026-0272 | 10, 9 | perl-String-Util | 2026-07-19 |
| Mageia | MGASA-2026-0274 | 9 | php | 2026-07-20 |
| Mageia | MGASA-2026-0285 | 10 | php8.4, php8.5 | 2026-07-20 |
| Mageia | MGASA-2026-0256 | 10, 9 | poppler | 2026-07-16 |
| Mageia | MGASA-2026-0254 | 10 | python-mistune | 2026-07-15 |
| Mageia | MGASA-2026-0281 | 10, 9 | python-nltk | 2026-07-20 |
| Mageia | MGASA-2026-0260 | 10 | python-pydantic-settings | 2026-07-18 |
| Mageia | MGASA-2026-0265 | 10, 9 | rsync | 2026-07-19 |
| Mageia | MGASA-2026-0278 | 10, 9 | sqlite3 | 2026-07-20 |
| Mageia | MGASA-2026-0287 | 10 | tig | 2026-07-21 |
| Mageia | MGASA-2026-0255 | 10, 9 | tmux | 2026-07-15 |
| Mageia | MGASA-2026-0261 | 10 | upower | 2026-07-18 |
| Mageia | MGASA-2026-0277 | 10, 9 | xmlstarlet | 2026-07-20 |
| Oracle | ELSA-2026-25115 | OL10 | .NET 10.0 | 2026-07-17 |
| Oracle | ELSA-2026-22145 | OL10 | .NET 10.0 | 2026-07-20 |
| Oracle | ELSA-2026-41900 | OL8 | .NET 10.0 | 2026-07-22 |
| Oracle | ELSA-2026-41898 | OL9 | .NET 10.0 | 2026-07-22 |
| Oracle | ELSA-2026-25111 | OL10 | .NET 8.0 | 2026-07-17 |
| Oracle | ELSA-2026-41901 | OL8 | .NET 8.0 | 2026-07-22 |
| Oracle | ELSA-2026-41894 | OL9 | .NET 8.0 | 2026-07-22 |
| Oracle | ELSA-2026-25112 | OL10 | .NET 9.0 | 2026-07-17 |
| Oracle | ELSA-2026-21754 | OL10 | .NET 9.0 | 2026-07-20 |
| Oracle | ELSA-2026-41899 | OL8 | .NET 9.0 | 2026-07-22 |
| Oracle | ELSA-2026-41896 | OL9 | .NET 9.0 | 2026-07-22 |
| Oracle | ELSA-2026-26453 | OL7 | 389-ds-base | 2026-07-15 |
| Oracle | ELSA-2026-19141 | OL10 | PackageKit | 2026-07-17 |
| Oracle | ELSA-2026-19354 | OL9 | PackageKit | 2026-07-15 |
| Oracle | ELSA-2026-42736 | OL9 | acl | 2026-07-22 |
| Oracle | ELSA-2026-24338 | OL10 | bind | 2026-07-17 |
| Oracle | ELSA-2026-39575 | OL8 | cifs-utils | 2026-07-16 |
| Oracle | ELSA-2026-39576 | OL9 | cifs-utils | 2026-07-16 |
| Oracle | ELSA-2026-21676 | OL10 | cockpit | 2026-07-17 |
| Oracle | ELSA-2026-24331 | OL10 | cockpit-image-builder | 2026-07-17 |
| Oracle | ELSA-2026-38504 | OL8 | container-tools:ol8 | 2026-07-20 |
| Oracle | ELSA-2026-33124 | OL10 | coreutils | 2026-07-17 |
| Oracle | ELSA-2026-39316 | OL9 | cups | 2026-07-15 |
| Oracle | ELSA-2026-23102 | OL10 | delve | 2026-07-17 |
| Oracle | ELSA-2026-19158 | OL10 | dnsmasq | 2026-07-17 |
| Oracle | ELSA-2026-19149 | OL10 | dovecot | 2026-07-17 |
| Oracle | ELSA-2026-41905 | OL9 | dovecot | 2026-07-22 |
| Oracle | ELSA-2026-22715 | OL10 | expat | 2026-07-17 |
| Oracle | ELSA-2026-25902 | OL10 | fence-agents | 2026-07-17 |
| Oracle | ELSA-2026-19157 | OL10 | firefox | 2026-07-20 |
| Oracle | ELSA-2026-19160 | OL10 | firefox | 2026-07-20 |
| Oracle | ELSA-2026-27733 | OL10 | firefox | 2026-07-20 |
| Oracle | ELSA-2026-21757 | OL10 | flatpak | 2026-07-17 |
| Oracle | ELSA-2026-24347 | OL10 | frr | 2026-07-17 |
| Oracle | ELSA-2026-19127 | OL10 | gdk-pixbuf2 | 2026-07-17 |
| Oracle | ELSA-2026-38485 | OL8 | gegl | 2026-07-16 |
| Oracle | ELSA-2026-33502 | OL10 | giflib | 2026-07-17 |
| Oracle | ELSA-2026-19154 | OL10 | giflib | 2026-07-20 |
| Oracle | ELSA-2026-40751 | OL9 | gimp | 2026-07-16 |
| Oracle | ELSA-2026-39266 | OL8 | git-lfs | 2026-07-16 |
| Oracle | ELSA-2026-39319 | OL9 | git-lfs | 2026-07-15 |
| Oracle | ELSA-2026-19148 | OL10 | glib2 | 2026-07-17 |
| Oracle | ELSA-2026-42090 | OL8 | glib2 | 2026-07-22 |
| Oracle | ELSA-2026-42089 | OL9 | glib2 | 2026-07-22 |
| Oracle | ELSA-2026-33092 | OL10 | glibc | 2026-07-20 |
| Oracle | ELSA-2026-33126 | OL8 | glibc | 2026-07-15 |
| Oracle | ELSA-2026-22141 | OL10 | go-fdo-client and go-fdo-server | 2026-07-17 |
| Oracle | ELSA-2026-19139 | OL10 | go-fdo-client | 2026-07-20 |
| Oracle | ELSA-2026-19137 | OL10 | go-fdo-server | 2026-07-20 |
| Oracle | ELSA-2026-38995 | OL8 | go-toolset:ol8 | 2026-07-16 |
| Oracle | ELSA-2026-35832 | OL10 | golang-github-openprinting-ipp-usb | 2026-07-17 |
| Oracle | ELSA-2026-19144 | OL10 | golang-github-openprinting-ipp-usb | 2026-07-20 |
| Oracle | ELSA-2026-27740 | OL10 | golang-github-openprinting-ipp-usb | 2026-07-20 |
| Oracle | ELSA-2026-35827 | OL10 | grafana | 2026-07-17 |
| Oracle | ELSA-2026-19134 | OL10 | grafana | 2026-07-20 |
| Oracle | ELSA-2026-35826 | OL10 | grafana-pcp | 2026-07-17 |
| Oracle | ELSA-2026-19136 | OL10 | grafana-pcp | 2026-07-20 |
| Oracle | ELSA-2026-16101 | OL7 | host-metering | 2026-07-15 |
| Oracle | ELSA-2026-40894 | OL8 | hplip | 2026-07-20 |
| Oracle | ELSA-2026-40831 | OL9 | hplip | 2026-07-16 |
| Oracle | ELSA-2026-34109 | OL10 | httpd | 2026-07-17 |
| Oracle | ELSA-2026-21433 | OL10 | httpd | 2026-07-20 |
| Oracle | ELSA-2026-41906 | OL9 | httpd | 2026-07-22 |
| Oracle | ELSA-2026-22937 | OL10 | image-builder | 2026-07-20 |
| Oracle | ELSA-2026-19151 | OL10 | jq | 2026-07-17 |
| Oracle | ELSA-2026-39494 | OL10 | kernel | 2026-07-17 |
| Oracle | ELSA-2026-25191 | OL10 | kernel | 2026-07-20 |
| Oracle | ELSA-2026-36349 | OL8 | kernel | 2026-07-15 |
| Oracle | ELSA-2026-39083 | OL8 | kernel | 2026-07-15 |
| Oracle | ELSA-2026-39179 | OL8 | kernel | 2026-07-20 |
| Oracle | ELSA-2026-36645 | OL9 | kernel | 2026-07-15 |
| Oracle | ELSA-2026-38491 | OL9 | kernel | 2026-07-16 |
| Oracle | ELSA-2026-500004 | OL9 | kernel | 2026-07-16 |
| Oracle | ELSA-2026-28582 | OL10 | keylime | 2026-07-17 |
| Oracle | ELSA-2026-19145 | OL10 | krb5 | 2026-07-17 |
| Oracle | ELSA-2026-19130 | OL10 | libcap | 2026-07-17 |
| Oracle | ELSA-2026-22529 | OL10 | libexif | 2026-07-17 |
| Oracle | ELSA-2026-28233 | OL10 | libpng | 2026-07-17 |
| Oracle | ELSA-2026-35839 | OL8 | libreoffice | 2026-07-16 |
| Oracle | ELSA-2026-36832 | OL9 | libreoffice | 2026-07-16 |
| Oracle | ELSA-2026-19560 | OL10 | libsndfile | 2026-07-17 |
| Oracle | ELSA-2026-28236 | OL10 | libsolv | 2026-07-17 |
| Oracle | ELSA-2026-39315 | OL9 | libsolv | 2026-07-15 |
| Oracle | ELSA-2026-19143 | OL10 | libsoup3 | 2026-07-17 |
| Oracle | ELSA-2026-28235 | OL10 | libtasn1 | 2026-07-17 |
| Oracle | ELSA-2026-19150 | OL10 | libtiff | 2026-07-17 |
| Oracle | ELSA-2026-41892 | OL10 | libtiff | 2026-07-20 |
| Oracle | ELSA-2026-42668 | OL9 | libtiff | 2026-07-22 |
| Oracle | ELSA-2026-39317 | OL9 | libxml2 | 2026-07-15 |
| Oracle | ELSA-2026-28584 | OL10 | libxslt | 2026-07-17 |
| Oracle | ELSA-2026-24758 | OL10 | libyang | 2026-07-17 |
| Oracle | ELSA-2026-33093 | OL10 | mariadb10.11 | 2026-07-17 |
| Oracle | ELSA-2026-38500 | OL9 | maven:3.9 | 2026-07-16 |
| Oracle | ELSA-2026-34355 | OL10 | mod_http2 | 2026-07-17 |
| Oracle | ELSA-2026-22528 | OL10 | mod_http2 | 2026-07-20 |
| Oracle | ELSA-2026-25225 | OL10 | mod_http2 | 2026-07-20 |
| Oracle | ELSA-2026-30845 | OL10 | mod_md | 2026-07-17 |
| Oracle | ELSA-2026-38847 | OL8 | nginx:1.24 | 2026-07-15 |
| Oracle | ELSA-2026-28231 | OL10 | opencryptoki | 2026-07-17 |
| Oracle | ELSA-2026-39322 | OL8 | pacemaker | 2026-07-22 |
| Oracle | ELSA-2026-39323 | OL9 | pacemaker | 2026-07-20 |
| Oracle | ELSA-2026-30857 | OL10 | perl-Archive-Tar | 2026-07-17 |
| Oracle | ELSA-2026-38901 | OL8 | perl-DBI:1.641 | 2026-07-20 |
| Oracle | ELSA-2026-36189 | OL10 | perl-HTTP-Daemon | 2026-07-20 |
| Oracle | ELSA-2026-30860 | OL10 | perl-IO-Compress | 2026-07-17 |
| Oracle | ELSA-2026-30843 | OL7 | perl-IO-Compress | 2026-07-22 |
| Oracle | ELSA-2026-39878 | OL8 | perl-XML-LibXML | 2026-07-16 |
| Oracle | ELSA-2026-39553 | OL9 | perl-XML-LibXML | 2026-07-16 |
| Oracle | ELSA-2026-40416 | OL9 | php:8.2 | 2026-07-20 |
| Oracle | ELSA-2026-38796 | OL9 | plexus-utils | 2026-07-22 |
| Oracle | ELSA-2026-24985 | OL10 | poppler | 2026-07-17 |
| Oracle | ELSA-2026-25930 | OL10 | postfix | 2026-07-17 |
| Oracle | ELSA-2026-24348 | OL10 | postgresql-jdbc | 2026-07-17 |
| Oracle | ELSA-2026-19155 | OL10 | python-markdown | 2026-07-20 |
| Oracle | ELSA-2026-39127 | OL8 | python-pillow | 2026-07-15 |
| Oracle | ELSA-2026-28000 | OL10 | python-urllib3 | 2026-07-17 |
| Oracle | ELSA-2026-35838 | OL7 | python3 | 2026-07-22 |
| Oracle | ELSA-2026-39320 | OL8 | python3 | 2026-07-16 |
| Oracle | ELSA-2026-39893 | OL8 | python3.12 | 2026-07-16 |
| Oracle | ELSA-2026-39771 | OL9 | python3.12 | 2026-07-16 |
| Oracle | ELSA-2026-40856 | OL10 | python3.14 | 2026-07-17 |
| Oracle | ELSA-2026-36193 | OL10 | python3.14-pip | 2026-07-17 |
| Oracle | ELSA-2026-27929 | OL10 | python3.14-urllib3 | 2026-07-17 |
| Oracle | ELSA-2026-39798 | OL9 | python3.9 | 2026-07-16 |
| Oracle | ELSA-2026-39311 | OL9 | qemu-kvm | 2026-07-15 |
| Oracle | ELSA-2026-20567 | OL10 | qt6-qtdeclarative | 2026-07-17 |
| Oracle | ELSA-2026-33731 | OL10 | rrdtool | 2026-07-17 |
| Oracle | ELSA-2026-26332 | OL10 | rsync | 2026-07-17 |
| Oracle | ELSA-2026-33565 | OL10 | ruby | 2026-07-17 |
| Oracle | ELSA-2026-33540 | OL10 | ruby4.0 | 2026-07-17 |
| Oracle | ELSA-2026-20606 | OL10 | ruby4.0 | 2026-07-20 |
| Oracle | ELSA-2026-22963 | OL10 | samba | 2026-07-17 |
| Oracle | ELSA-2026-29035 | OL10 | skopeo | 2026-07-17 |
| Oracle | ELSA-2026-18153 | OL10 | systemd | 2026-07-20 |
| Oracle | ELSA-2026-30846 | OL10 | thunderbird | 2026-07-17 |
| Oracle | ELSA-2026-19131 | OL10 | thunderbird | 2026-07-20 |
| Oracle | ELSA-2026-22325 | OL10 | thunderbird | 2026-07-20 |
| Oracle | ELSA-2026-500004 |  | uek-kernel | 2026-07-16 |
| Oracle | ELSA-2026-25216 | OL10 | valkey | 2026-07-17 |
| Oracle | ELSA-2026-42088 | OL8 | webkit2gtk3 | 2026-07-22 |
| Oracle | ELSA-2026-42062 | OL9 | webkit2gtk3 | 2026-07-22 |
| Oracle | ELSA-2026-20600 | OL10 | wireshark | 2026-07-17 |
| Oracle | ELSA-2026-26566 | OL10 | xorg-x11-server-Xwayland | 2026-07-17 |
| Oracle | ELSA-2026-25999 | OL10 | yggdrasil-worker-package-manager | 2026-07-17 |
| Red Hat | RHSA-2026:29195-01 | EL10 | buildah | 2026-07-16 |
| Red Hat | RHSA-2026:36199-01 | EL10 | buildah | 2026-07-21 |
| Red Hat | RHSA-2026:29455-01 | EL9 | buildah | 2026-07-16 |
| Red Hat | RHSA-2026:35833-01 | EL8 | container-tools:rhel8 | 2026-07-21 |
| Red Hat | RHSA-2026:29703-01 | EL9 | containernetworking-plugins | 2026-07-16 |
| Red Hat | RHSA-2026:26534-01 | EL8 | dracut | 2026-07-21 |
| Red Hat | RHSA-2026:27740-01 | EL10 | golang-github-openprinting-ipp-usb | 2026-07-21 |
| Red Hat | RHSA-2026:38492-01 | EL10 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:21557-01 | EL10 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:41062-01 | EL10.0 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:39371-01 | EL10.0 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:39179-01 | EL8 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:39984-01 | EL8.4 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:40068-01 | EL8.6 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:40760-01 | EL8.8 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:38491-01 | EL9 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:21556-01 | EL9 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:40082-01 | EL9.2 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:41063-01 | EL9.4 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:40425-01 | EL9.6 | kernel | 2026-07-17 |
| Red Hat | RHSA-2026:41234-01 | EL7 | kernel-rt | 2026-07-17 |
| Red Hat | RHSA-2026:39180-01 | EL8 | kernel-rt | 2026-07-17 |
| Red Hat | RHSA-2026:21745-01 | EL8 | kernel-rt | 2026-07-17 |
| Red Hat | RHSA-2026:39983-01 | EL9.2 | kernel-rt | 2026-07-17 |
| Red Hat | RHSA-2026:41892-01 | EL10 | libtiff | 2026-07-21 |
| Red Hat | RHSA-2026:27711-01 | EL10.0 | osbuild-composer | 2026-07-21 |
| Red Hat | RHSA-2026:37072-01 | EL10 | podman | 2026-07-17 |
| Red Hat | RHSA-2026:37123-01 | EL9 | podman | 2026-07-17 |
| Red Hat | RHSA-2026:28000-01 | EL10 | python-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:36732-01 | EL8 | python-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:28158-01 | EL9 | python-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:32992-01 | EL8 | python3.12-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:28159-01 | EL9 | python3.12-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:27929-01 | EL10 | python3.14-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:28157-01 | EL9 | python3.14-urllib3 | 2026-07-21 |
| Red Hat | RHSA-2026:29702-01 | EL9 | runc | 2026-07-21 |
| Red Hat | RHSA-2026:29035-01 | EL10 | skopeo | 2026-07-16 |
| Slackware | SSA:2026-202-01 |  | libssh | 2026-07-21 |
| Slackware | SSA:2026-202-02 |  | mozilla-firefox | 2026-07-21 |
| Slackware | SSA:2026-197-01 |  | netatalk | 2026-07-16 |
| SUSE | SUSE-SU-2026:3137-1 | SLE15 oS15.5 | 389-ds | 2026-07-20 |
| SUSE | SUSE-SU-2026:3136-1 | SLE15 oS15.6 | 389-ds | 2026-07-20 |
| SUSE | SUSE-SU-2026:3053-1 | SLE15 oS15.4 | ImageMagick | 2026-07-15 |
| SUSE | SUSE-SU-2026:3023-1 | SLE15 oS15.6 | ImageMagick | 2026-07-15 |
| SUSE | openSUSE-SU-2026:11273-1 | TW | ImageMagick | 2026-07-16 |
| SUSE | openSUSE-SU-2026:11310-1 | TW | ImageMagick | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11312-1 | TW | acl | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11274-1 | TW | agama | 2026-07-16 |
| SUSE | openSUSE-SU-2026:11313-1 | TW | avahi | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11275-1 | TW | aws-nitro-enclaves-binaryblobs-upstream | 2026-07-16 |
| SUSE | SUSE-SU-2026:3152-1 | SLE15 oS15.6 | aws-nitro-enclaves-cli | 2026-07-21 |
| SUSE | openSUSE-SU-2026:21383-1 | oS16.0 | beets | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11288-1 | TW | blender | 2026-07-18 |
| SUSE | SUSE-SU-2026:3063-1 | SLE15 oS15.5 | buildah | 2026-07-15 |
| SUSE | openSUSE-SU-2026:11309-1 | TW | chromedriver | 2026-07-20 |
| SUSE | openSUSE-SU-2026:21363-1 | oS16.0 | chromium | 2026-07-17 |
| SUSE | openSUSE-SU-2026:21382-1 | oS16.0 | chromium | 2026-07-21 |
| SUSE | openSUSE-SU-2026:0254-1 | osB15 | chromium | 2026-07-20 |
| SUSE | openSUSE-SU-2026:11305-1 | TW | containerized-data-importer1 | 2026-07-19 |
| SUSE | SUSE-SU-2026:3068-1 | SLE15 oS15.4 | cosign | 2026-07-16 |
| SUSE | SUSE-SU-2026:3043-1 | MP4.3 SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | curl | 2026-07-15 |
| SUSE | openSUSE-SU-2026:21368-1 | oS16.0 | cyrus-imapd | 2026-07-18 |
| SUSE | SUSE-SU-2026:3049-1 | SLE15 oS15.4 | distribution | 2026-07-15 |
| SUSE | SUSE-SU-2026:3028-1 | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | dnsmasq | 2026-07-15 |
| SUSE | openSUSE-SU-2026:11311-1 | TW | firefox | 2026-07-21 |
| SUSE | openSUSE-SU-2026:21359-1 | oS16.0 | gimp | 2026-07-16 |
| SUSE | SUSE-SU-2026:3032-1 | SLE15 oS15.6 | glib-networking | 2026-07-15 |
| SUSE | SUSE-SU-2026:3029-1 | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.3 | glibc | 2026-07-15 |
| SUSE | SUSE-SU-2026:3030-1 | SLE15 oS15.6 | glibc | 2026-07-15 |
| SUSE | SUSE-SU-2026:3042-1 | SLE15 SLE5.4 SLE5.5 SLE-m5.4 SLE-m5.5 oS15.4 | gnutls | 2026-07-15 |
| SUSE | SUSE-SU-2026:3151-1 | SLE15 oS15.6 | go1.25-openssl | 2026-07-21 |
| SUSE | SUSE-SU-2026:3102-1 | SLE15 oS15.6 | go1.26-openssl | 2026-07-17 |
| SUSE | openSUSE-SU-2026:11290-1 | TW | gomuks | 2026-07-18 |
| SUSE | openSUSE-SU-2026:11276-1 | TW | gpsd | 2026-07-16 |
| SUSE | openSUSE-SU-2026:11277-1 | TW | grafana | 2026-07-16 |
| SUSE | openSUSE-SU-2026:21366-1 | oS16.0 | grafana | 2026-07-18 |
| SUSE | SUSE-SU-2026:3133-1 | SLE15 oS15.4 | gstreamer-plugins-bad | 2026-07-20 |
| SUSE | SUSE-SU-2026:3125-1 | SLE15 oS15.5 | gstreamer-plugins-bad | 2026-07-20 |
| SUSE | SUSE-SU-2026:3058-1 | SLE15 oS15.6 | gstreamer-plugins-bad | 2026-07-15 |
| SUSE | openSUSE-SU-2026:11278-1 | TW | hostapd | 2026-07-16 |
| SUSE | openSUSE-SU-2026:21360-1 | oS16.0 | hostapd | 2026-07-16 |
| SUSE | openSUSE-SU-2026:11317-1 | TW | iscsiuio | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11279-1 | TW | jackson-databind | 2026-07-16 |
| SUSE | openSUSE-SU-2026:11306-1 | TW | kbfs | 2026-07-19 |
| SUSE | SUSE-SU-2026:3044-1 | MP4.3 SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | kernel | 2026-07-15 |
| SUSE | SUSE-SU-2026:3089-1 | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-07-17 |
| SUSE | SUSE-SU-2026:3156-1 | SLE15 oS15.6 | kernel | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11307-1 | TW | kubevirt1.8-container-disk | 2026-07-19 |
| SUSE | openSUSE-SU-2026:11314-1 | TW | kubevirt1.8-container-disk | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11315-1 | TW | libgit2-1_9 | 2026-07-21 |
| SUSE | openSUSE-SU-2026:0255-1 | osB15 | libkrun | 2026-07-22 |
| SUSE | SUSE-SU-2026:3140-1 | SLE15 oS15.5 | libreoffice | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11316-1 | TW | libsoup-3_0-0 | 2026-07-21 |
| SUSE | SUSE-SU-2026:3076-1 | SLE15 oS15.6 | libssh2_org | 2026-07-16 |
| SUSE | openSUSE-SU-2026:11308-1 | TW | libsuricata8_0_6 | 2026-07-20 |
| SUSE | SUSE-SU-2026:3095-1 | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | libxml2 | 2026-07-17 |
| SUSE | SUSE-SU-2026:3096-1 | SLE15 SLE5.5 SLE-m5.5 oS15.5 | libxml2 | 2026-07-17 |
| SUSE | openSUSE-SU-2026:21367-1 | oS16.0 | lux | 2026-07-18 |
| SUSE | SUSE-SU-2026:3110-1 | SLE15 oS15.6 | mariadb-connector-c | 2026-07-17 |
| SUSE | SUSE-SU-2026:3153-1 | SLE15 oS15.6 | nghttp2 | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11295-1 | TW | nginx | 2026-07-18 |
| SUSE | openSUSE-SU-2026:11280-1 | TW | nm-configurator | 2026-07-16 |
| SUSE | openSUSE-SU-2026:21380-1 | oS16.0 | opam | 2026-07-21 |
| SUSE | openSUSE-SU-2026:0250-1 | osB15 | opam | 2026-07-17 |
| SUSE | openSUSE-SU-2026:11281-1 | TW | opennlp | 2026-07-16 |
| SUSE | SUSE-SU-2026:3094-1 | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | openssl-3 | 2026-07-17 |
| SUSE | openSUSE-SU-2026:11297-1 | TW | oras | 2026-07-18 |
| SUSE | openSUSE-SU-2026:11298-1 | TW | perl-DBI | 2026-07-19 |
| SUSE | openSUSE-SU-2026:11282-1 | TW | perl-Mojolicious | 2026-07-16 |
| SUSE | SUSE-SU-2026:3105-1 | SLE15 oS15.6 | php-composer2 | 2026-07-17 |
| SUSE | openSUSE-SU-2026:11300-1 | TW | php-composer2 | 2026-07-19 |
| SUSE | SUSE-SU-2026:3165-1 | SLE15 oS15.4 | php7 | 2026-07-21 |
| SUSE | SUSE-SU-2026:3070-1 | SLE15 SES7.1 oS15.3 | podman | 2026-07-16 |
| SUSE | SUSE-SU-2026:3126-1 | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | podman | 2026-07-20 |
| SUSE | SUSE-SU-2026:3071-1 | SLE15 SLE5.5 SLE-m5.5 oS15.5 | podman | 2026-07-16 |
| SUSE | SUSE-SU-2026:3084-1 | SLE15 oS15.3 | python-Pillow | 2026-07-17 |
| SUSE | openSUSE-SU-2026:21372-1 | oS16.0 | python-aiohttp | 2026-07-21 |
| SUSE | SUSE-SU-2026:3040-1 | MP4.3 SLE15 oS15.4 | python-cryptography | 2026-07-15 |
| SUSE | SUSE-SU-2026:3026-1 | SLE15 oS15.6 | python-cryptography | 2026-07-15 |
| SUSE | openSUSE-SU-2026:0252-1 | osB15 | python-django-haystack | 2026-07-19 |
| SUSE | SUSE-SU-2026:3093-1 | MP4.3 SLE15 oS15.4 | python-paramiko | 2026-07-17 |
| SUSE | SUSE-SU-2026:3085-1 | SLE15 oS15.6 | python-python-engineio | 2026-07-17 |
| SUSE | SUSE-SU-2026:3086-1 | SLE15 oS15.6 | python-python-socketio | 2026-07-17 |
| SUSE | SUSE-SU-2026:3155-1 | SLE15 oS15.4 | python-tornado6 | 2026-07-21 |
| SUSE | openSUSE-SU-2026:0251-1 | osB15 | python-weasyprint | 2026-07-19 |
| SUSE | SUSE-SU-2026:3132-1 | MP4.3 SLE15 oS15.4 | python311 | 2026-07-20 |
| SUSE | SUSE-SU-2026:3104-1 | SLE15 oS15.6 | python311 | 2026-07-17 |
| SUSE | openSUSE-SU-2026:11283-1 | TW | python313-Pillow | 2026-07-17 |
| SUSE | openSUSE-SU-2026:11271-1 | TW | python313-django-debug-toolbar | 2026-07-15 |
| SUSE | openSUSE-SU-2026:11286-1 | TW | python315 | 2026-07-17 |
| SUSE | SUSE-SU-2026:3069-1 | SLE15 oS15.4 | rekor | 2026-07-16 |
| SUSE | SUSE-SU-2026:3022-1 | SLE15 oS15.6 | sccache | 2026-07-15 |
| SUSE | SUSE-SU-2026:3123-1 | SLE15 oS15.3 | shibboleth-sp | 2026-07-20 |
| SUSE | SUSE-SU-2026:3139-1 | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | sssd | 2026-07-21 |
| SUSE | SUSE-SU-2026:3025-1 | SLE15 oS15.6 | sssd | 2026-07-15 |
| SUSE | openSUSE-SU-2026:11304-1 | TW | system-user-zabbix | 2026-07-19 |
| SUSE | SUSE-SU-2026:3087-1 | SLE15 oS15.6 | tomcat11 | 2026-07-17 |
| SUSE | openSUSE-SU-2026:21374-1 | oS16.0 | vim | 2026-07-21 |
| SUSE | openSUSE-SU-2026:11303-1 | TW | wget | 2026-07-19 |
| SUSE | SUSE-SU-2026:3037-1 | SLE15 oS15.4 | yelp | 2026-07-15 |
| SUSE | SUSE-SU-2026:3036-1 | SLE15 oS15.6 | yelp | 2026-07-15 |
| Ubuntu | USN-8578-1 | 16.04 | CUPS | 2026-07-21 |
| Ubuntu | USN-8580-2 | 14.04 16.04 18.04 20.04 | accountsservice | 2026-07-21 |
| Ubuntu | USN-8580-1 | 22.04 24.04 26.04 | accountsservice | 2026-07-21 |
| Ubuntu | USN-8571-1 | 14.04 16.04 18.04 20.04 | apache2 | 2026-07-20 |
| Ubuntu | USN-8553-1 | 22.04 24.04 26.04 | dotnet8, dotnet10 | 2026-07-16 |
| Ubuntu | USN-8561-1 | 24.04 26.04 | freerdp3 | 2026-07-20 |
| Ubuntu | USN-8562-1 | 26.04 | freetype | 2026-07-20 |
| Ubuntu | USN-8558-1 | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | imagemagick | 2026-07-21 |
| Ubuntu | USN-8582-1 | 22.04 24.04 26.04 | jbig2dec | 2026-07-21 |
| Ubuntu | USN-8573-1 | 16.04 18.04 20.04 22.04 24.04 26.04 | libde265 | 2026-07-20 |
| Ubuntu | USN-8550-1 | 22.04 24.04 26.04 | libslirp | 2026-07-15 |
| Ubuntu | USN-8560-1 | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | libxfont | 2026-07-20 |
| Ubuntu | USN-8567-1 | 22.04 24.04 | linux, linux-gcp, linux-gcp-6.8, linux-gke, linux-gkeop, linux-realtime, linux-realtime-6.8 | 2026-07-20 |
| Ubuntu | USN-8575-1 | 20.04 22.04 | linux, linux-gcp, linux-gcp-fips, linux-gke, linux-gkeop, linux-hwe-5.15, linux-kvm, linux-lowlatency, linux-lowlatency-hwe-5.15, linux-realtime, linux-xilinx-zynqmp | 2026-07-21 |
| Ubuntu | USN-8566-1 | 26.04 | linux, linux-gcp, linux-gke, linux-realtime | 2026-07-20 |
| Ubuntu | USN-8570-1 | 24.04 | linux-gcp-6.17, linux-realtime-6.17 | 2026-07-20 |
| Ubuntu | USN-8574-1 | 24.04 | linux-gcp-fips | 2026-07-21 |
| Ubuntu | USN-8569-1 | 24.04 | linux-hwe-7.0 | 2026-07-20 |
| Ubuntu | USN-8576-1 | 20.04 | linux-nvidia-tegra-5.15 | 2026-07-21 |
| Ubuntu | USN-8568-1 | 26.04 | linux-oem-7.0 | 2026-07-20 |
| Ubuntu | USN-8544-1 | 14.04 16.04 18.04 20.04 22.04 24.04 | luajit | 2026-07-15 |
| Ubuntu | USN-8563-2 | 22.04 24.04 26.04 | nginx | 2026-07-20 |
| Ubuntu | USN-8563-1 | 22.04 24.04 26.04 | nginx | 2026-07-20 |
| Ubuntu | USN-8554-1 | 22.04 24.04 26.04 | ntfs-3g | 2026-07-16 |
| Ubuntu | USN-8577-1 | 16.04 | openssh | 2026-07-21 |
| Ubuntu | USN-8564-1 | 22.04 24.04 26.04 | php8.1, php8.3, php8.5 | 2026-07-20 |
| Ubuntu | USN-8557-1 | 22.04 24.04 26.04 | python-authlib | 2026-07-16 |
| Ubuntu | USN-8549-1 | 22.04 24.04 26.04 | python-idna | 2026-07-15 |
| Ubuntu | USN-8559-1 | 20.04 22.04 24.04 26.04 | rlottie | 2026-07-20 |
| Ubuntu | USN-8556-1 | 16.04 | ruby2.3 | 2026-07-16 |
| Ubuntu | USN-8579-1 | 16.04 18.04 20.04 22.04 24.04 26.04 | snapd | 2026-07-21 |
| Ubuntu | USN-8565-1 | 22.04 24.04 26.04 | sqlite3 | 2026-07-20 |
| Ubuntu | USN-8552-1 | 16.04 18.04 20.04 22.04 24.04 | sympa | 2026-07-15 |
| Ubuntu | USN-8477-2 | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | tar | 2026-07-16 |
| Ubuntu | USN-8551-1 | 16.04 18.04 | tomcat8 | 2026-07-15 |
| Ubuntu | USN-8555-1 | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | ubuntu-advantage-tools | 2026-07-16 |
| Ubuntu | USN-8572-1 | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | wget | 2026-07-20 |

전체 이야기
(
코멘트: 없음
)

### 관심 있는 커널 패치

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.


### 커널 릴리스

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

리누스 토발즈
리눅스 7.2-rc4
7월 19일
세바스티안 안드레이 시에비오르
v7.2-rc4-rt3
7월 21일
그렉 크로아-하트만
리눅스 7.1.4
7월 18일
그렉 크로아-하트만
리눅스 6.18.39
7월 18일
그렉 크로아-하트만
리눅스 6.12.96
7월 18일
다니엘 와그너
v6.12.96-rt19
7월 21일
클라크 윌리엄스
6.1.177-rt65
7월 15일

### 아키텍처별

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

스티븐 프라이스
arm64: KVM에서 Arm CCA 지원
7월 15일
양시
x86이 아닌 경우(이 시리즈의 경우 ARM64) this_cpu_*() 작업 최적화
7월 15일
안드레 알메이다
arm64: vdso: __vdso_futex_robust_try_unlock() 구현
7월 17일
진지에 루안
arm64: 항목: 일반 항목으로 변환
7월 21일
나라야나 머티 N
powerpc/eeh: pSeries에 RTAS 기반 오류 주입 지원 추가
7월 21일
추이 윤희
riscv: Svnapot PTE 접기 지원 추가
7월 16일
시에 보
riscv: 감독자 포인터 마스킹 인프라 추가
7월 21일
바룬 R 말리아
RISC-V에 대한 BPF 예외 지원 추가
7월 22일
알렉산더 고르디예프
s390/mm: 지연 MMU 모드에서 일괄 PTE 업데이트
7월 15일
하이코 카르스텐스
s390: DCACHE_WORD_ACCESS에 대한 지원을 다시 도입합니다.
7월 16일
릭 엣지컴
동적 PAMT
7월 17일
다펭미
성능을 위한 SIMD/eGPR/SSP 레지스터 샘플링 지원
7월 21일

### 빌드 시스템

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

제임스 클라크
tools/build: 모든 LLVM 도구의 버전 관리 허용
7월 15일

### 코어 커널

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

황 레온
bpf: 전역 percpu 데이터 소개
7월 15일
안드레아 리기
sched: 프록시 실행이 sched_ext와 호환되도록 만듭니다.
7월 15일
허태준
sched_ext: 하위 스케줄러 후속 조치
7월 15일
히라마츠 마사미(구글)
추적: wprobe: x86: 감시점에 wprobe 추가
7월 16일
폴 E. 맥케니
간단한 위험 포인터 구현 및 고문 테스트
7월 15일
쿠마르 카르티케야 드위베디
kfuncs 및 struct_ops에 경기장 인수 지원 추가
7월 16일
리 첸
pidfd: 최소 프로세스 생성 빌더를 추가합니다.
7월 16일
트브르트코 우르술린
실시간 작업 대기열 및 Pantor 실시간 제출
7월 17일
안드레 알메이다
sched: 긴 작업 이름에 대한 지원 추가
7월 17일
K 프라텍 나약
sched/core: 프록시 실행이 코어 스케줄링과 함께 작동하도록 허용합니다.
7월 17일
보쿤 펭
Rust: sync: Rcu*Box 소개
7월 17일
허태준
sched_ext: 하위 스케줄러를 위한 Cgroup 마이그레이션 및 작업 전달
7월 17일
크리스티안 브라우너
binfmt_misc: 투명한 인터프리터 및 PT_INTERP 로더 대체
7월 20일
슈리칸스 헤그데
sched, Steal_governor: cpu_preferred_mask 및 도용 기반 vCPU 백오프 도입
7월 20일
첸 양유
sched/cache: 캐시 인식 스케줄링의 프로세스별 제어
7월 22일
장 구펑
sched: 활성 도메인 관리 CPU 없이 CPU 정지를 처리합니다.
7월 22일

### 개발 도구

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

발렌틴 슈나이더
추적/오스노이즈: IPI 추적
7월 15일
사르탁 샤르마
selftests/mm: 기능 테스트와 GUP 마이크로벤치마킹을 분리합니다.
7월 16일
왕 진차오
mm/kwatch: 메모리 손상 추적을 위한 동적 하드웨어 감시점
7월 17일
가브리엘레 모나코
rv: 도구 및 KUnit 테스트에 자체 테스트 추가
7월 17일
진지에 루안
kselftest/arm64: orig_x0 문제에 대한 두 개의 arm64 kselftest 추가
7월 17일
마크 브라운
KVM: 자체 테스트: arm64: set_id_regs의 진단 개선
7월 19일
쯔양먼
자체 테스트: BPF 프로그램 및 뼈대 구축을 위한 공유 lib.bpf.mk
7월 21일
조쉬 힐케
vfio: 자체 테스트: Intel 이더넷 기가비트 컨트롤러(IGB)용 드라이버 추가
7월 22일
리차드 쳉
selftests/resctrl: MPAM 플랫폼에 대한 MBA 스키마 ABI 자체 테스트
7월 22일

### 장치 드라이버

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

B4 릴레이를 통한 Nikolai Burov
pmdomain: mediatek: MT6858 지원 추가
7월 15일
안젤로조아키노 델 레뇨
drm/mediatek: DSC, WDMA, MT8189/96 DSI 지원 추가
7월 15일
비슈누 레디
미디어: iris: glymur 플랫폼에 대한 지원 추가
7월 15일
스티븐 프라이스
펌웨어: arm_rmm: RMM v2.0 지원 추가
7월 15일
자오 홍양
QCS6490 RubikPi3에 대한 오디오 지원 추가
7월 15일
Uwe Kleine-König(능력 있는 허브)
gpio: 장치 ID 배열 관련 개선 사항
7월 15일
pankaj.gupta@oss.nxp.com
펌웨어: imx: NXP 보안 엔클레이브용 드라이버
7월 15일
매트 에반스
vfio/pci: DMABUF용 mmap() 추가
7월 15일
크리스 루
블루투스: btmtk: MT7928 지원 추가
7월 16일
자가디시 코나
clk: qcom: Qualcomm Maili SoC에 대한 비디오 클럭 컨트롤러 지원 추가
7월 16일
Md 사드레 알람
QPIC SNAND에 대한 쿼드 모드 지원 추가
7월 16일
guoniu.zhou@oss.nxp.com
미디어: nxp: CSI 픽셀 포맷터 지원 추가
7월 16일
킴 시어 팔러
AD5710R/AD5711R DAC 추가
7월 16일
mohit.dsor@oss.qualcomm.com
제목: HDMI 드라이버에 Lontium LT9611C(EX/UXD) MIPI DSI 추가
7월 16일
B4 릴레이를 통한 Rodrigo Alencar
AD5686 IIO 드라이버의 새로운 기능
7월 16일
프라브하카르
CPG/MSSR 드라이버에 Renesas RZ/T2H 및 RZ/N2H에 대한 syscon 지원 추가
7월 16일
토니 응우옌
iXD 드라이버 소개
7월 15일
츠유쿠사 아카리
soc: mediatek: pwrap: MT6589 + MT6320 지원
7월 17일
B4 릴레이를 통한 Alexandru Chimac
clk: samsung: Exynos9610 클럭 지원 소개
7월 16일
티에리 레딩
PCI: tegra: Tegra264 지원 추가
7월 16일
아르템 심코
DAPU Telecom DAP8211R(I) 기가비트 이더넷 PHY 드라이버 추가
7월 16일
유 펑화
resctrl: MBA 제어 에뮬레이션 및 ARM MPAM MB_NODE 지원
7월 16일
마르셀로 슈미트
iio: adc: LTC2378 및 유사한 ADC에 대한 지원 추가
7월 16일
루이스 안젤로 다로스 데 루카
hwmon: (adt7470) 열 프레임워크 지원 추가
7월 16일
제이슨 군소프
VFIO 자가 테스트를 위한 mlx5 지원
7월 16일
스테판 되싱어
ZTE zx297520v3 클록 바인딩 및 드라이버
7월 17일
정 리펭
ACPI: CPPC: 리소스 우선순위 레지스터 지원 및 sysfs 인터페이스
7월 17일
류웬멍
미디어: i2c: Samsung S5KJN5 이미지 센서 추가
7월 17일
코이치로 덴
dmaengine: dw-edma: PCI EP DMA 준비(1/3부)
7월 17일
코이치로 덴
PCI: 엔드포인트: 엔드포인트 DMA 리소스 노출(2/3부)
7월 17일
코이치로 덴
PCI: 엔드포인트: PCI DMA 엔드포인트 기능 추가(3/3부)
7월 17일
페타르 스테파노비치
iio: adc: Axiado SARADC 드라이버 추가
7월 16일
크리스티앙 마랑기
net: PC: fwnode PCS에 대한 지원 소개
7월 17일
사친 쿠마르 가르그
media: qcom: iris: 멀티 슬라이스 지원 추가
7월 17일
첸 차오이
drm/bridge: 일반 USB Type-C DP HPD 브리지 구현
7월 17일
우 펑린
입력: 기타: Qcom PMIH010x PMIC 내부에 햅틱용 초기 드라이버를 추가합니다.
7월 17일
타니야 다스
Eliza에 비디오, 카메라, 그래픽 시계 컨트롤러에 대한 지원 추가
7월 17일
휴고 발티에
pinctrl: rockchip: RK3308B SoC에 대한 지원 추가
7월 17일
바르토스 골라스제프스키
crypto/dmaengine: qce: BAM 잠금을 도입하고 레지스터 I/O에 DMA를 사용합니다.
7월 17일
션 로즈
펌웨어: coreboot CFR 펌웨어 특성 드라이버 추가
7월 17일
제롬 브루넷
레귤레이터: X-Powers AXP318W PMIC 지원 추가
7월 17일
후 자싱
가속/로켓: RK3576 NPU(RKNN) 활성화
7월 17일
유 치앙
QMP PCIe 다중 링크 모드 PHY 지원 추가
7월 17일
Herve Codina (슈나이더 일렉트릭)
타이머: RZ/N1 SoC 타이머 지원 추가
7월 17일
라이언 로버츠
Arm 코어 로컬 가속기 드라이버
7월 17일
자이 루트라
platform/raspberrypi: Broadcom Videocore 공유 메모리 지원 추가
7월 17일
자이 루트라
미디어: Broadcom/RPi BCM2835 ISP에 대한 지원 추가
7월 17일
록 마르코비치
drm/rockchip: RK3568 LVDS 지원 추가
7월 17일
마르코 귄타
ALSA: hda: Lenovo Legion용 AW88399 HDA 사이드 코덱 드라이버 추가
7월 17일
아서 키야노프스키
ptp: PHC 타임스탬프 품질 속성 추가
7월 17일
핑케 시
wifi: rtw89: LED 지원 추가 및 일부 임의 설정 업데이트
7월 17일
핑케 시
wifi: rtw89: coex: 최신 버전에 대한 더 많은 펌웨어 명령 및 이벤트 형식 추가
7월 17일
크리스 모건
인벤센스 ICM42607 추가
7월 16일
스테판 포파
iio: ADC: MAX40080 전류 감지 증폭기 드라이버 추가
7월 17일
멜리사 웬
drm/drm_colorop: AMD 디스플레이 드라이버에 혼합 후 colorop 지원 추가
7월 16일
닐레시 자바리
scsi: qla2xxx: QLA29xx 시리즈 어댑터 지원 추가
7월 17일
산토시 쿠마르 K
spi: cadence-quadspi: PHY 튜닝 지원 추가
7월 18일
테오 르브룬
net: macb: 컨텍스트 스와핑 구현
7월 17일
MD 쇼피쿨 이슬람
iio: 건강: MAX86150 ECG 및 PPG 바이오센서 드라이버 추가
7월 17일
신시에
net: hsr: PRP RedBox(PRP-SAN) 지원
7월 17일
아킬 P 옴멘
drm/msm: Eliza GPU 지원
7월 18일
루이스 안젤로 다로스 데 루카
hwmon: (adt7470) 열 영역 및 PWM 공급자 지원 추가
7월 17일
수미트 굽타
ACPI / cpufreq: CPPC: ospm_nominal_perf 지원 추가
7월 18일
테리 보우먼
CXL PCIe 포트 프로토콜 오류 처리 및 로깅 활성화
7월 17일
아누샤 아룬 난디
media: qcom: camss: sa8775p, sa8300 및 sm8250에 대한 C-PHY 지원 추가
7월 17일
지안루카 보이아노
ASoC: 코덱: Texas Instruments TAS2557 스마트 증폭기 드라이버 추가
7월 18일
브라이언 오도노휴
phy: qcom-mipi-csi2: CSI2 MIPI DPHY 드라이버 추가
7월 18일
메테한 구넨
드라이버/기타: Goodix GXFP5130 eSPI 지문 센서 드라이버 추가
7월 18일
이고르 파우노비치
미디어: synopsys: hdmirx: HDMI 오디오 캡처 지원 추가
7월 18일
임란 샤이크
clk: qcom: Qualcomm Shikra SoC에 대한 DISPCC 및 GPUCC 지원 추가
7월 18일
비주
Renesas RZ/G3L SD/eMMC 지원 추가
7월 18일
세르하트 쿰랄
RDMA/rxe: GID 테이블에서 UDP 터널 소켓 수명 구동
7월 18일
타랑 라발
media: i2c: os05b10: 드라이버 리팩터링 및 새 기능 추가
7월 19일
사티시 카라트
enic: SR-IOV V2 관리 채널 및 MBOX 프로토콜
7월 19일
B4 릴레이를 통한 Rodrigo Alencar
iio: dac: ad5686: 장치 지원 확장
7월 19일
vishnu.saini@oss.qualcomm.com
이 시리즈는 LT9211을 확장하여 LT9211C 브리지 드라이버를 추가합니다.
7월 19일
B4 릴레이를 통한 Jia Wang
clk: ultrarisc: DP1000 클록 지원 추가
7월 20일
카이리 우
미디어: mediatek: vcodec: mt8196에서 비디오 디코더 지원
7월 20일
마렉 바수트
PCI: dwc: rcar-gen4: R-Car X5H PCIe4에 대한 지원 추가
7월 20일
첸 지유
i2c: ma35d1: MA35D1 I2C 컨트롤러에 대한 지원 추가
7월 20일
다니엘 골레
net: dsa: mxl862xx: 펌웨어 업데이트 지원
7월 20일
데릭 J. 클라크
MSI Claw HID 구성 드라이버 추가
7월 20일
tze.yee.ng@altera.com
hwmon: Altera SoC FPGA 하드웨어 모니터링 지원 추가
7월 19일
joakim.zhang@cixtech.com
Cix Sky1 AUDSS 클록 및 재설정 지원 추가
7월 20일
호세 이그나시오 토르노스 마르티네즈
wifi: ath11k/ath12k: TX 흐름 제어 구현
7월 20일
싱룽
tee: MbedTEE 드라이버 추가
7월 20일
B4 릴레이를 통한 헤르메스 우
미디어: i2c: ITE IT6625/IT6626 HDMI - MIPI CSI-2 브리지에 대한 지원 추가
7월 20일
자오 홍양
Hynetek HUSB320 Type-C 컨트롤러 지원 추가
7월 20일
안드레아 델라 포르타
RP1 PWM 컨트롤러 지원 추가
7월 20일
루이 알렉시스 에로(Louis-Alexis Eyraud)
MT8189: 시스템 및 기본 클록 컨트롤러에 대한 지원 추가
7월 20일
조이 루
phy: nuvoton: 듀얼 포트 OTG 지원을 위해 MA35D1 USB2 PHY 드라이버 확장
7월 20일
B4 릴레이를 통한 Jean-Baptiste Maneyrol
iio: 공통: InvenSense 샘플 타임스탬프 개선
7월 20일
안토니우 미클라우스
iio: adc: ade9000: ADE9078에 대한 지원 추가
7월 20일
파비트라쿠마르 마나구테
crypto: spacc - SPAcc 암호화 드라이버 추가
7월 20일
판공
net: hinic3: PF 초기화
7월 20일
프라사드 쿰파틀라
ASoC: qcom 및 pinctrl: LPASS LPR 투표 및 Hawi LPASS LPI TLMM 추가
7월 20일
마이클 마골린
완료 카운터 도입
7월 20일
블라디미르 올테안
10G Lynx 동적 프로토콜 재구성을 위한 RCW 재정의
7월 20일
마크 클라인-버드
가능: gs_usb: candleLight 펌웨어에 최근 추가된 새로운 기능 구현
7월 20일
롬.왕
virtio: vhost-scsi에 대한 SQ/CQ 초인종 폴링
7월 20일
모하마드 라피 샤이크
ASoC: qcom: qdsp6: MI2S 클럭 제어 추가
7월 20일
안젤로조아키노 델 레뇨
PHY: MediaTek PCI-Express Gen4 S-PHY 드라이버 추가
7월 20일
카말 와드와
레귤레이터: qcom-rpmh: RPMH 주소 읽기를 지원하고 rpmh-regulator에 사용합니다.
7월 20일
딘 응우옌
EDAC/altera: Agilex5 플랫폼에 대한 지원 추가
7월 20일
마시에크 마치니코프스키
netdevsim에서 PTP 지원 구현
7월 20일
티무르 크리스토프
drm/amdgpu: GFX6-8(v3)에서 DRM 형식 수정자를 지원합니다.
7월 20일
비슈누 레디
미디어: iris: ar50lt에 대한 LTR 및 계층적 코딩 지원 추가
7월 21일
야븐
RTL8261에 대한 지원 추가
7월 21일
항샹 마
미디어: qcom: camss: Kaanapali 지원 추가
7월 20일
웽 치웬
pwm: Nuvoton MA35D1 PWM 컨트롤러 지원 추가
7월 21일
가우라브 콜리
Qualcomm Remoteproc 하위 시스템 냉각에 대한 지원 추가
7월 21일
앤디 정
hwmon: Kandou KB9002 PCIe 리타이머 드라이버 추가
7월 21일
차이첸유
arm64: mediatek: Chromebook에 M.2 E-키 슬롯 추가
7월 21일
린유춘
gpio: realtek: Realtek DHC RTD1625에 대한 지원 추가
7월 21일
타니야 다스
clk: qcom: Nord 멀티미디어 시계 컨트롤러 지원 추가
7월 21일
라티시 칸노스
스위치 지원
7월 21일
킴 시어 팔러
AD5710R/AD5711R DAC에 대한 지원 추가
7월 21일
스뱌토슬라프 리헬
mfd: Asus Transformer 내장 컨트롤러에 대한 지원 추가
7월 21일
트로이 미첼
hwmon: (lm63) Sensylink CTF2301 지원 추가
7월 21일
제이슨 양
피hy: rockchip-samsung-dcphy: D-PHY 수신기 방향 지원
7월 21일
동쉬양
디자인웨어 PWM 드라이버 업데이트
7월 21일
콘라드 디비시오
SMEM에서 DDR에 대한 정보 검색
7월 21일
항샹 마
미디어: qcom: camss: SM8750 지원 추가
7월 21일
로익 풀랭
media: qcom: camss: 미디어 컨트롤러를 통해 CAMSS 하드웨어 버전 보고
7월 21일
요린 반 데르 그라프
iio: 자력계: QST QMC6308에 대한 지원 추가
7월 21일
야코포 몬디
media: i2c: Mira220용 드라이버 추가
7월 21일
로렌조 비안코니
airoha: 필요에 따라 GDM3/GDM4를 WAN/LAN으로 구성하는 기능 추가
7월 21일
양옌리
wifi: aic: AIC8800 SDIO FullMAC 드라이버 추가
7월 21일
빈빈 저우
열: loongson2: Loongson-2K0300 SoC에 대한 지원 추가
7월 21일
왕 션웨이
i.MX 플랫폼에서 RPMSG를 통한 원격 GPIO 활성화
7월 21일
징크림
eth: fbnic: hwmon 센서 지원 확장
7월 21일
롱 리
net: mana: HWC를 강화하고 동적 대기열 깊이를 추가합니다.
7월 21일
데보라 브라워
drm/tyr: 펌웨어 로딩 및 MCU 부팅 지원
7월 21일
알렉시스 체자르 토레노
hwmon: (pmbus/max34440): 버그 수정 및 새 장치 지원
7월 22일
야븐
r8169: phylink 지원 추가
7월 22일
유 치앙
clk: qcom: 공통 clkref 지원 추가 및 Glymur 및 Mahua 마이그레이션
7월 21일
드미트리 바리시코프
drm/msm: msm_display 구조체 인터페이스를 소개합니다.
7월 22일
하샬 데브
UEFI 보안 애플리케이션용 TEE 기반 클라이언트 드라이버 추가
7월 22일
후 자싱
미디어: rockchip: RK3576용 VEPU510 H.264 인코더
7월 22일
왕 지
gpu: nova-core: vGPU가 활성화된 GSP 부팅
7월 22일
자나니 수닐
iio: dac: AD5529R DAC에 대한 지원 추가
7월 22일
아드리안 응 호 인
SVC 드라이버 및 FPGA 구성에 Agilex5 지원을 추가하고 Agilex5에 대한 부분 재구성 지원을 추가합니다.
7월 22일
사친 굽타
Thermal: qcom: Qualcomm SPMI MBG 열 모니터 지원 추가
7월 22일
로한 조시
케이던스 eMMC 호스트 컨트롤러에 대한 CQE 지원
7월 22일
지슈누 프라카쉬
Thermal: qcom: PMIC5 Gen3 ADC 열 모니터링 지원 추가
7월 22일
헤이키 크로게루스
drm/xe/i2c: 수정을 가능하게 하는 경고 및 컨트롤러
7월 22일
니힐 P. 라오
pds_core: PLDM 펌웨어 업데이트 및 호스트 지원 메모리 지원 추가
7월 21일
마르쿠스 슈톡하우젠
net: mdio: realtek-rtl9300: RTL83xx 지원 추가
7월 22일
해리 웬트랜드
amdgpu 및 VKMS를 사용한 YUV 변환 colorop
7월 22일
제롬 브루넷
clk: sun6i-rtc: Allwinner A733 SoC에 대한 지원 추가
7월 22일

### 장치 드라이버 인프라

#### 요약
- 이 부분은 "장치 드라이버 인프라" 주제를 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

마커스 프롭스트
녹: 기본 직렬 장치 버스 추상화 추가
7월 15일
미켈 레이날(슈나이더 일렉트릭)
clk: 클록 넥서스에 대한 지원 추가
7월 16일
지리 피르코
RDMA: 넷 네임스페이스별로 장치 이름을 고유하게 만듭니다.
7월 16일
바르토스 골라스제프스키
드라이버 코어: 동적으로 할당된 플랫폼 장치에 대한 릴리스 경로 통합
7월 16일
타룬 사후
장치를 비동기적으로 종료
7월 16일
B4 릴레이를 통한 Pawel Laszczak
usb: eUSB2v2 1024바이트 대량 MaxPacketSize에 대한 지원 추가
7월 17일
아니쉬 쿠마르 K.V (팔)
dma-mapping: 직접, 풀 및 swiotlb 경로를 통해 공유 DMA 상태 추적
7월 17일
장롱
LED: 하드웨어 시작 하드웨어 제어 트리거 전환에 대한 지원 추가
7월 19일
마커스 포크슨
채널별 I2C Mux 버스 속도
7월 19일
볼프람 상
hwspinlock: XArray로 변환하고 디버그 기능 추가
7월 18일
막심 슈발리에
net: phy_port: SFP 모듈 표현 및 phy_port 목록
7월 20일
아킬 R
ACPI 및 SETAASA 장치 검색 지원
7월 21일
안젤로조아키노 델 레뇨
SPMI: 하위 장치 구현 및 드라이버 마이그레이션
7월 21일
압두라만 후세인
of: /aliases를 동기화 상태로 유지하도록 오버레이 코드를 교육합니다.
7월 20일
비타 미칼스카
Rust: 런타임 PM 지원 추가
7월 21일
니콜라스 프라타롤리
커넥터 debugfs에 SCDC 정보 추가
7월 22일
필립 스타너
Rust / dma_buf: dma_fence에 대한 추상화 추가
7월 22일

### 파일 시스템 및 블록 레이어

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

프란잘 슈리바스타바
nfs: 직접 I/O 경로 현대화
7월 15일
데이비드 하웰스
netfs: 분할된 bio_vec[] 체인에서 Folio를 추적합니다.
7월 16일
크리스토프 헬윅
기타 lib/raid/개선 v2
7월 15일
전남재
ntfs: 최종 EA 속성 크기 확인
7월 16일
Ze Tan
smb: EA를 통한 보안 및 신뢰할 수 있는 xattrs 지원
7월 17일
제프 레이튼
nfsd/sunrpc: netlink를 사용하도록 nfsstat 서버측 인터페이스를 변환합니다.
7월 17일
B4 릴레이를 통한 Bryam Vargas
dm-pcache: 위조된 캐시 이미지에 대해 미디어 내 메타데이터를 검증합니다.
7월 17일
제프 레이튼
btrfs: 중단하지 않고 일부 동기 dirop에서 -ENOMEM 오류를 처리합니다.
7월 17일
미콜라 마르잔
block,md,nvme: 지원되지 않는 P2PDMA 전송의 올바른 처리
7월 19일
안드레이 알버슈테인
EOF 이후 머클 트리를 사용하여 XFS에 대한 fs-verity 지원
7월 20일
아디트야 프라카시 스리바스타바
io_uring: Removexattr 및 listxattr 지원 추가
7월 20일
프란잘 슈리바스타바
nfs: 직접 I/O 경로 현대화
7월 20일
키스 부시
블록: 직접 I/O 메모리 정렬 확인
7월 20일
조앤 쿵
iomap: 반복 내 iomap_next() 모델로 변환
7월 20일

### 메모리 관리

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

스타니슬라프 킨스부르스키
mm/hmm: userfaultfd 지원 매핑에 대한 mmap 잠금 삭제 지원 추가
7월 15일
원 지앙
mm/vmalloc: 연속 메모리로 ioremap, vmalloc 및 vmap 속도를 높입니다.
7월 15일
바오린 왕
MGLRU를 처음 사용한 후 매핑된 실행 파일 Folio 승격
7월 16일
쉬에위안 첸
mm: 스왑을 사용할 수 없을 때 대규모 Folio 분할 방지
7월 17일
알렉산더 고르디예프
mm: __ptent 희소 속성을 도입합니다.
7월 17일
릭 반 리엘
mm: VMA별 잠금 하에서 원격 프로세스 메모리에 액세스합니다.
7월 17일
로렌조 스토익스(ARM)
mm/rmap: virt pgoff의 MAP_PRIVATE 파일 기반 Folio 색인
7월 17일
쉬에위안 첸
영구 거대 제로 Folio를 읽기 전용으로 설정
7월 18일
장 펭
mm: vmscan의 더티 Folio에 대한 일괄 TLB 플러시
7월 20일
송무춘
mm: HugeTLB를 위한 섹션 기반 vmemmap 최적화 도입
7월 20일
리제
mm: 영역 장치 memmap 초기화 최적화
7월 20일
Gutierrez.asier@huawei-partners.com
mm/damon: 자동 조정을 사용하여 거대한 페이지 축소 메커니즘을 도입합니다.
7월 20일
유해리 (오라클)
mm/slab: kfree_rcu_nolock() 도입 및 slub_kunit 적용 범위 개선
7월 20일
아디트야 샤르마
mm: 대규모 종료 프로세스의 주소 공간 분해를 kthread로 연기합니다.
7월 20일
리안 왕
mm/damon: DAMOS_SPLIT 작업 소개
7월 20일
블라스티밀 바브카(SUSE)
mm/slab, alloc_tag: obj_ext 메모리 낭비 줄이기
7월 20일
그레고리 프라이스
개인 메모리 NUMA 노드
7월 20일
치 젱
사용하지 않는 거대한 축소기 memcg를 인식하게 만듭니다.
7월 21일
마이크 라포포트(마이크로소프트)
arch, mm: 일반 set_memory/change_page_attr 코어 생성
7월 21일

### 네트워킹

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

마크 블로흐
devlink: 부팅 시 eswitch 모드 기본값 추가
7월 16일
신 롱
net: QUIC 인프라 및 핵심 하위 구성 요소 소개
7월 15일
데이브 세돈
net: flow_dissector: 공통 형태에 대한 옵트인 바이트 동일 빠른 경로
7월 15일
로렌조 비안코니
eBPF 프로그램에 HW RX 체크섬을 로드하는 기능 추가
7월 15일
양샤오량
tc: 더 빠른 조치(IEEE 802.1CB)를 도입합니다.
7월 17일
황 유양
ipv6: RTM_DELROUTE에서 경로가 삭제된 이유를 보고합니다.
7월 18일
유태희
net: knod: 커널 내 네트워크 오프로드 장치
7월 19일
사이먼 디에츠
GeoNetworking 프로토콜 추가
7월 18일
척 레버
커널 read_sock 소비자에게 TLS 제어 레코드 전달
7월 20일
마헤 타르디
bpf_ksock 소개
7월 22일

### 보안 관련

#### 요약
- PyPI에 대해, GNOME 보안 추적, XZ 백도어 관련 자료 등 공급망·보안 소식을 정리합니다.
- 센서와 릴리스 아티팩트는 보안에 미치는 영향을 설명합니다.
- 보안 사건의 원인이 아니라 생태계 거버넌스가 중요하다는 점을 표시합니다.

콩 왕
seccomp: 비협조적인 pinned-memfd 인수 리디렉션
7월 15일
에릭 비거스
AES 암호화 모드용 라이브러리 API
7월 15일
요크 재스퍼 니버
Bootpatch-SLR: 부팅 시 Linux 커널 구조 레이아웃 무작위화
7월 20일
옥사나 카리토노바
landlock: POSIX 메시지 큐 범위 지정 추가
7월 22일

### 가상화 및 컨테이너

#### 요약
- 업데이트된 패치와 하위 시스템 별 변경을 새롭게 표시합니다.
- 릴리스 거부, 실행, 빌드 시스템, 드라이버, 파일 시스템, 메모리 관리, 네트워킹, 보안 관련 패치가 어떤 방향으로 동적지 추적됩니다.
- 헬리콥터 릴리스 전 개발 동향과 회귀 가능성을 즉각적으로 파악하는 데 도움이 됩니다.

아니쉬 쿠마르 K.V (팔)
KVM: arm64: hVHE 런타임 매핑에 TTBR1_EL2 사용
7월 16일
데이비드 우드하우스
KVM: PFNMAP 메모리가 지원하는 guest_memfd의 대체 공급자 허용
7월 16일
파올로 본지니
KVM: x86: 메모리 보호 속성 도입
7월 16일
모스타파 살레
KVM: arm64: BBM 레벨 3 지원
7월 17일
무케시 R
Hyper-V의 PCI 패스스루
7월 17일
마크 브라운
KVM: arm64: SME에 대한 지원 구현
7월 20일
오다키 아키히코
KVM: arm64: PMU: 여러 호스트 PMU 사용
7월 20일
배창석
KVM: x86: 게스트에 대해 APX 활성화
7월 20일
푸아드 타바
KVM: arm64: 호스트/hyp 하이퍼콜 경계를 넘어 유형 검사 복원
7월 20일
빈센트 도네포트
KVM: arm64: pKVM 하이퍼바이저 힙 할당자 소개
7월 20일
마크 징거
KVM: arm64: FEAT_NV2p1 및 FEAT_NV3에 대한 지원 추가
7월 22일

### 기타

#### 요약
- 이 버섯은 LWN의 관련 소식과 부분을 정리합니다.
- 원문의 링크, 명, 해제 번호, 기술적인 한계를 없애고 사랑하는 것이 가능합니다.
- 운전자와 개발자가 실제로 영향을 미치는 범위와 추가 확인 사항을 빠르게 확인할 수 있도록 했습니다.

앨리스 릴
Rust에 대한 속도 제한 인쇄
7월 16일
안드레이 알버슈테인
xfsprogs: v7.1.1 출시
7월 17일
**페이지 편집자**: 조 브록마이어


## 기술 각주

[^lwn1083123-llm-kernel-community]: LLM 보조 개발은 코드 작성 속도를 높일 수 있지만, 커널처럼 회귀 비용이 큰 코드베이스에서는 테스트 증거, 설명 가능성, 작성 책임이 핵심 검증 기준이 됩니다.
[^lwn1083123-gnome-session-restore]: GNOME의 save/restore 기능은 데스크톱 세션 상태, 애플리케이션 프로토콜, crash recovery, user expectation이 만나는 영역입니다. UX 개선처럼 보여도 compositor/toolkit integration 비용이 큽니다.
[^lwn1083123-fedora-change-process]: Fedora Change 프로세스는 배포판 기술 방향과 community governance를 연결합니다. 큰 변경은 패키지 maintainer, QA, 사용자 migration 비용을 함께 관리해야 합니다.
[^lwn1083123-security-updates]: 배포판 보안 업데이트 표는 CVE 자체보다 패키지 버전, advisory ID, 배포판별 backport 여부를 함께 추적해야 실제 패치 상태를 판단할 수 있습니다.
[^lwn1083123-kernel-community]: 커널 개발 문화는 기술 토론뿐 아니라 maintainer 책임, review bandwidth, contributor trust 위에 굴러갑니다. 도구 변화는 사회적 프로세스에도 영향을 줍니다.
[^lwn1083123-networking]: 커널 네트워킹 패치는 성능·보안·하드웨어 offload·컨테이너 네트워크 동작에 넓게 영향을 주므로 배포 전 workload별 검증이 중요합니다.
[^lwn1083123-filesystems]: 파일시스템 변경은 데이터 무결성, page cache, writeback, block layer와 직접 연결되므로 기능 개선과 regression 위험을 함께 봐야 합니다.
[^lwn1083123-bpf-security]: BPF는 tracing, networking, security enforcement를 커널 안에서 확장하지만, verifier·권한·LSM hook 무결성이 깨지면 방어 기법 자체가 공격 표면이 될 수 있습니다.
[^lwn1083123-bpf-tracepoints]: BPF tracepoint attachment는 관측성(observability), performance analysis, production debugging의 기반입니다. 여러 tracepoint를 효율적으로 다루면 tooling overhead와 verifier 제약이 줄어듭니다.
[^lwn1083123-kernel-patches]: 커널 패치 목록은 아직 릴리스 노트가 되기 전의 개발 방향을 보여 주며, 하위 시스템별 maintainer 관심사와 regression 위험을 조기에 파악하는 데 유용합니다.
[^lwn1083123-bpf-lsm]: BPF LSM은 보안 결정을 프로그래머블하게 만들지만, 정책이 우회·변조되지 않도록 attachment, pinning, capability boundary를 엄격히 다뤄야 합니다.
[^lwn1083123-famfs]: famfs는 fabric-attached memory를 파일시스템 인터페이스로 노출하려는 시도입니다. CXL/공유 메모리 시대에는 persistent/shared memory의 ownership, cache coherency, failure semantics가 중요합니다.
[^lwn1083123-scheduler]: 스케줄러 변경은 CPU 배치, 지연시간, 전력, fairness를 동시에 움직이므로 서버·데스크톱·모바일 워크로드에 서로 다른 영향을 줄 수 있습니다.
[^lwn1083123-pypi-supply-chain]: PyPI 업로드·삭제 정책은 Python 공급망의 재현 가능성과 incident response에 직결됩니다. 파일 교체나 늦은 업로드를 제한하면 dependency confusion과 post-release tampering 위험이 줄어듭니다.
[^lwn1083123-xz-backdoor]: XZ backdoor 사건은 long-game maintainer compromise와 release artifact 조작이 얼마나 현실적인 공급망 위협인지 보여 줍니다. 빌드 재현성, review 분산, 사회적 신뢰 검증이 모두 중요합니다.
