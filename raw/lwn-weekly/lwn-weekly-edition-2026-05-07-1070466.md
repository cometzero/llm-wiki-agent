# LWN.net Weekly Edition for May 7, 2026 — 한국어 기술 번역

- 원문 Edition: https://lwn.net/Articles/1070466/
- 원문 Bigpage: https://lwn.net/Articles/1070466/bigpage
- LWN Archives: https://lwn.net/Archives/
- 선택 정책: 최신호(2026-05-14, article 1071535)는 유료 공개 가능성이 높아 건너뛰고, 직전 무료 공개판(2026-05-07, article 1070466)을 번역했습니다.
- 생성 시각: 2026-05-20 (Hermes cron)
- 출처/라이선스: 원문 저작권과 이용 조건은 LWN.net에 있습니다. 이 문서는 공개 bigpage에서 확인 가능한 내용을 찬호님 개인 지식베이스 ingest용으로 한국어 번역·주석화한 것입니다.

## 전체 요약

- 이번 호의 핵심은 LLM 기반 보안 취약점 탐색이 전통적인 coordinated disclosure와 embargo 관행을 흔들고 있다는 점입니다.
- Linux 커널의 rseq ABI 논쟁은 문서화된 계약과 실제 사용자 공간 의존성이 충돌할 때, 커널이 회귀(regression)를 어떻게 다뤄야 하는지를 보여줍니다.
- Fedora/GNOME 버그 모니터링 정책, Prolly tree 기반 버전 관리 데이터베이스, s390에서 Arm VM을 구동하려는 실험 등 운영체제·배포판·데이터 구조·가상화 주제가 함께 다뤄집니다.
- Brief items와 Announcements는 보안, 커널 릴리스, 배포판, GCC/Incus/NetHack/PHP 라이선스, 뉴스레터·CFP·보안 업데이트·패치 흐름을 한 번에 정리합니다.
- 각주에는 커널, 보안, 런타임, 파일시스템, 네트워킹, 빌드/배포 관점의 배경과 실무적 함의를 덧붙였습니다.


---

### [2026년 5월 7일 LWN.net 주간판에 오신 것을 환영합니다](https://lwn.net/Articles/1071490/)

#### 요약

- 이번 호는 LLM 기반 보안 보고, 재시작 가능 시퀀스(restartable sequences), Fedora GNOME 패키지의 버그 모니터링 기대치 등을 다룹니다.
- 데이터베이스 버전 관리를 위한 Prolly 트리와 s390에서 Arm VM을 지원하려는 작업도 소개됩니다.
- 커뮤니티 전반의 짧은 소식, 공지, 보안 업데이트와 패치 정보도 포함되어 있습니다.

이번 호에는 다음 특집 기사가 포함되어 있습니다.

- LLM 주도 보안 보고가 조율된 공개를 흔들다
  : 보안 취약점에 대한 잘 짜인 공개 절차는 과거의 일이 될지도 모른다.
- 재시작 가능 시퀀스, TCMalloc, 그리고 하이럼의 법칙
  : 어떤 프로그램이 문서화된 ABI를 위반하더라도, Linus는 회귀(regression) 규칙이 적용된다고 판정한다.
- 버그 모니터링 기대치와 Fedora GNOME 패키지
  : FESCo는 GNOME 버그 보고가 적극적으로 모니터링되지 않는다는 자동 응답 문구를 조정하라고 요구한다.
- Prolly 트리를 이용한 버전 관리 데이터베이스
  : 데이터베이스의 효율적인 버전 관리를 지원하는 데 쓰이는 B-tree 변종을 살펴본다.
- s390을 위한 하드웨어 지원 Arm VM
  : s390에서 Arm VM을 활성화하려는 작업은 두 아키텍처 모두의 테스트, 디버깅, 문서화를 개선할 수 있다.

이번 주 판에는 다음 내부 페이지도 포함되어 있습니다.

- 짧은 소식
  : 커뮤니티 전반의 간단한 뉴스 항목.
- 공지
  : 뉴스레터, 컨퍼런스, 보안 업데이트, 패치 등.

이번 주 판도 즐겁게 읽어주시기 바라며, 늘 그렇듯 LWN.net을 후원해 주셔서 감사합니다.

[댓글(게시된 댓글 없음)](https://lwn.net/Articles/1071490/#Comments)

### [LLM 주도 보안 보고가 조율된 공개를 흔들다](https://lwn.net/Articles/1070698/)

#### 요약

- LLM 도구로 보안 취약점 보고가 급증하면서 유지관리자들이 전례 없는 양의 보고를 처리하고 있습니다.
- 같은 취약점이 엠바고(embargo) 기간 안에 여러 독립 연구자에게 병렬로 발견되는 사례가 이미 나타나고 있습니다.
- Copy Fail 공개는 배포판과 사용자에게 충분한 사전 경고 없이 동작 가능한 PoC가 공개되면서 기존 조율된 공개(coordinated disclosure) 모델의 한계를 드러냈습니다.
- 커널 보안팀은 “최신 안정 커널로 업데이트하라”는 오랜 정책을 강조하지만, 배포판들은 많은 CVE 속에서 중요한 취약점을 선별하기 어렵다고 지적합니다.
- AI 보조 취약점 발견과 보고자들의 절차 미숙이 결합되면서, 엠바고와 조율된 수정에 의존하는 방식은 점점 더 위험해지고 있습니다.

작성자

Joe Brockmeier

2026년 5월 6일

LLM 도구가 보안 취약점 보고의 급증을 일으킬 것이라는 예측은 의심의 여지 없이 현실이 되었다. 예상대로 유지관리자들은 그 어느 때보다 많은 보안 보고를 헤쳐 나가야 하고 있으며, 그뿐 아니라 LLM 도구는 전통적인 조율된 공개(coordinated disclosure) 관행까지 흔들고 있다.[^art1a-note1] 특히 [Copy Fail](https://copy.fail/)의 공개 방식은 벤더, 프로젝트, 사용자를 허둥대게 만들었다. 게다가 유지관리자들은 엠바고 기간 안에 동일한 보안 결함이 병렬로 발견되는 상황도 목격하고 있다. 이 두 흐름은 조율된 보안 공개가 과거의 일이 될 수 있음을 뜻한다.

#### "보안 금광 캐기"

[OpenStack](https://www.openstack.org/) 클라우드 컴퓨팅 프로젝트의 [취약점 관리팀](https://security.openstack.org/vmt.html) 구성원인 Jeremy Stanley는 4월 28일 OSS Security 메일링 리스트에 [이 주제를 제기했다](https://lwn.net/ml/all/afDLFWVMK-r70PB0%40yuggoth.org/). 그는 자신이 작업하는 프로젝트들이 “우리 소프트웨어에서 보안 금광을 캐내기 위해 LLM을 사용하는 연구자들의 보고가 끝없이 밀려드는 듯한 상황”에 놓여 있다고 말했다. 그 결과 그는 공개 LLM 서비스가 전통적인 취약점 처리 워크플로, 엠바고, 보안 결함의 조율된 공개에 어떤 위험을 줄 수 있는지 생각하게 되었다. 그는 병렬 발견이나 다른 LLM 사용자에게로의 공개 위험을 줄이기 위해 엠바고를 짧게 유지하는 것이 도움이 될지 궁금해했다.

> 보고량 증가와 조기 공개 위험 때문에, LLM을 사용한 연구 결과로 보고된 모든 취약점은 다른 사람들도 사소하게 발견할 수 있다고 가정하고, 엠바고 아래에서 작업하는 척하는 데 무슨 의미가 있다는 생각을 포기하고 싶은 유혹이 매우 큽니다. 마찬가지로 엠바고 아래에서 작업 중인 취약점에 대해서는 패치 개발과 설명 문서 작성에 LLM 지원을 쓰지 않는 것이 타당해 보입니다.

그는 이 문제를 생각하는 사람이 자신뿐일 리 없다고 말하며 다른 사람들의 의견을 물었다. Jacob Bachmeyer는 병렬 발견이 큰 위험이라고 [답했다](https://lwn.net/ml/all/521d0295-6a93-4a28-be55-332d663ec457@gmail.com/). “LLM이 화이트햇을 위해 버그를 찾을 수 있다면, 블랙햇을 위해서도 똑같이 할 수 있다. [...] LLM이 발견한 취약점은 이미 공개적으로 알려진 것으로 간주해야 한다.”

#### 엠바고에 미치는 영향

취약점이 (논쟁의 여지는 있지만) 여러 사람에게 알려져 있다면, 보안 엠바고를 둘러싼 표준 관행이 여전히 의미가 있는지 의문이 생긴다. Lucas Holt는 엠바고를 단축하려는 “논리와 유혹”은 이해한다고 [말했지만](https://lwn.net/ml/all/dc97be31-0762-4a91-a1ad-6795abaab8a9@foolishgames.com/), 작은 프로젝트에 제로데이 익스플로잇(zero-day exploit)을 던지는 것은 누구에게도 도움이 되지 않는다고 했다. 그는 큰 프로젝트에는 같은 결함을 찾고 발견하는 사람이 여럿 있을 수 있지만, 작은 프로젝트가 동시에 여러 사람에게 취약점 탐색을 당할 가능성은 낮다고 보았다.

Stanley는 자신이 이 문제를 “이런 보고를 받는 대형/인기 프로젝트의 업스트림 유지관리자이자 취약점 조율자” 관점에서 접근하고 있다고 [분명히 했다](https://lwn.net/ml/all/afI79Ruw_74rdrxq@yuggoth.org/). 그는 보고가 홍수처럼 밀려드는 것을 보고 있었고, 그 모두를 비공개로 관리하려다 보니 “준비가 끝나거나 배포판/배포 담당자들에게 충분한 사전 경고가 주어지기 전에 사고로 엠바고가 깨지는” 상황으로 이어지고 있다고 했다. 보안 보고가 즉시 공개된다면, 프로젝트는 “과부하 상태인 취약점 조율자와 보안 중심 유지관리자에게만 의존하는 대신” 더 넓은 커뮤니티의 도움을 크라우드소싱할 수 있다고 그는 생각했다.

Holt는 LLM을 사용해 보안 버그를 찾는 사람들이 그 도구를 사용해 패치도 만들 수 있다고 제안한 바 있다. Brian May는 사람들에게 그 접근법을 조심하라고 [경고했다](https://lwn.net/ml/all/87340d2y55.fsf@linuxpenguins.xyz/). “겉보기에는 좋아 보이는 단순한 패치가 사실은 심각한 보안 문제를 숨기고 있을 수 있습니다. 여기서는 [2006년 9월 Debian openssl 문제](https://research.swtch.com/openssl)를 떠올립니다.”

Greg Dahlman도 LLM은 보안 수정 사항을 만드는 데 있어 신뢰하기 어렵다고 [생각했다](https://lwn.net/ml/all/CAM=PXV7qd66ceLZJmz2usDYJVunFPMPBL1m=s+bjUR6orL9GDA@mail.gmail.com/). 그는 현재 LLM이 정확하고 *동시에* 안전한 코드를 만들어낼 능력을 “동전 던지기 수준”이라고 묘사했다. 달리 말하면, 결함을 고치기 위해 LLM이 제안한 해법이 적절할 가능성을 50 대 50 정도로 본 것이다. 따라서 어떤 엠바고 일정이든 결함을 발견하는 데 걸리는 시간과 실제로 수정하는 데 필요한 시간 사이의 비대칭을 고려해야 한다.

#### 이미 벌어지고 있는 일

Stanley의 병렬 발견 가설은 이미 현실에서 입증된 것으로 드러났다. Red Hat Enterprise Linux(RHEL) 암호화 팀에서 일하는 Clemens Lang은 그 이론을 뒷받침하는 [자료점을 제공했다](https://lwn.net/ml/all/3CD03E7B-92A9-4C32-AC58-E811FB8A43A6@redhat.com/). “우리는 엠바고 기간 안에 LLM을 사용하는 여러 독립 그룹이 같은 문제를 찾아 중복 보고하는 사례를 보고 있습니다.” Greg Kroah-Hartman도 커널 개발자들이 “수정 사항을 병합하는 데 걸리는 기간 안에 서로 다른 그룹으로부터 같은 문제에 대한 중복 보고를 받고 있다”고 [전했다](https://lwn.net/ml/all/2026043030-unpinned-grafted-38eb@gregkh/).

Willy Tarreau는 몇 달 전부터 보안 엠바고의 죽음을 예견했다고 [말했다](https://lwn.net/ml/all/afI-PPAr7EP8SEsu@1wt.eu/).

> 이제 엠바고는 보안에 역행합니다. 우리가 행동하지 않는 동안 사용자는 같은 문제를 우연히 찾은 누구에게나 계속 노출되어 있기 때문입니다. 이는 LLM의 강함의 문제가 아니라, 작은 모델을 여러 번 실행해 더 깊이 파고들게 할 수 있는 연구자의 집요함의 문제입니다. 더 큰 모델은 더 빨리 찾을 뿐인데, 그것은 보호하려는 사람들에게나 의미가 있지 공격하려는 사람들에게는 그렇지 않습니다.

#### Copy Fail 공개 실패

Copy Fail 권한 상승(privilege-escalation) 취약점([CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431))은 Xint가 4월 29일 [발표했다](https://xint.io/blog/copy-fail-linux-distributions). 이는 “직선형 논리 결함(straight-line logic flaw)”으로, 경쟁 조건(race condition)이나 다른 특별한 상황을 필요로 하지 않으며, 최신 커널을 갖추지 않은 대부분의 Linux 배포판에서 로컬 사용자가 손쉽게 root 접근 권한을 얻을 수 있게 했다.[^art1a-note2]

발표와 함께 사용자가 자신의 시스템이 취약한지 확인할 수 있는 [개념증명(proof-of-concept, PoC)](https://github.com/theori-io/copy-fail-CVE-2026-31431/blob/main/copy_fail_exp.py) Python 스크립트도 공개되었다. 수정은 이미 7.0, 6.19.12, 6.18.22 커널에 포함되어 있었지만, [4월 30일까지](https://lwn.net/Articles/1070641/)는 더 오래된 안정 커널로 백포트(backport)되어 제공되지 않았다. 대부분의 Linux 배포판은 속담처럼 바지가 내려간 채 붙잡힌 꼴이었다. 4월 30일, 취약점 악용 방법을 보여주는 PoC가 널리 공개된 상황에서 Debian, Red Hat Enterprise Linux, SUSE, Ubuntu 같은 주요 배포판은 사용자에게 제공할 준비된 수정이 없었다.

OSS Security 리스트에서 Eddie Chapman은 이를 최근 커널에서 나온 “최악의 make-me-root 취약점 중 하나”라고 [묘사했다](https://lwn.net/ml/oss-security/d6111caa-db61-498a-92cb-ea7a0aa0a5e2@ehuk.net/). 그는 무엇이 잘못되었는지 궁금해했다.

> 오늘 엠바고가 일찍 깨진 것입니까? 누구를 비난하려는 것은 아닙니다. 우리 커뮤니티에서 일이 굴러가게 만드는 사람들은 정말 열심히 일하고 있으며 존중과 지원을 받을 자격이 있습니다. 특히 이제 AI 찌꺼기(AI slop)라는 추가 부담까지 생긴 상황에서는 더욱 그렇습니다.

Gentoo 기여자 Sam James는 커널 취약점을 Linux 배포판에 알리는 것은 보안 보고자의 책임이라고 [말했다](https://lwn.net/ml/oss-security/87se8dgicq.fsf@gentoo.org/). “보고자가 이를 linux-distros [메일링 리스트]에 가져가기로 선택하지 않는 한, 배포판에는 사전 알림이 없습니다. 여기서는 그런 일이 일어나지 않았습니다.”

논의는 임시 사후분석(postmortem), 책임 공방, 문제 해결 세션과 비슷한 방향으로 흘러갔다. “Solar Designer”라는 이름을 쓰는 Alexander Peslyak은 이 취약점이 다른 모든 취약점 사이에서 두드러지지 않았기 때문에 배포판이 그 중요성을 알 방법이 거의 없었다고 [말했다](https://lwn.net/ml/oss-security/20260501032146.GA31617@openwall.com/).

Xint 발표의 일정표에 따르면 이 취약점은 3월 23일 커널 팀에 보고되었다. 패치는 4월 1일 메인라인 커널에 커밋되었다. [CVE-2026-31431은 4월 25일 커널 보안 저장소에 추가되었으며](https://git.kernel.org/pub/scm/linux/security/vulns.git/commit/?id=cb9d133eed6ab823b8fdefdc10600189aa69a107), Common Vulnerability Scoring System(CVSS) 점수는 가능한 10점 만점 중 7.8이었다. 이는 Copy Fail 발표 나흘 전이었다. Peslyak은 그날 묶음에는 7.1에서 9.8 사이의 점수를 가진 CVE가 168개 있었다고 지적했다. “점수만으로 보면 이것은 정말 두드러지지 않습니다. 제게는 신호가 거의 없는 평소의 잡음입니다.” 그 점수는 PoC가 곧 공개될 것이라는 심각성이나 임박한 위협을 암시하지 않았다. 실제로 4월 25일 추가된 CVE 중에는 CVSS 점수가 “9.8 CRITICAL”인 것이 21개나 있다.

Greg Kroah-Hartman은 커널 팀의 “변함없는 메시지”는 수십 년 동안 사용자가 현재 알려진 문제에 대한 모든 수정 사항을 갖추려면 최신 릴리스로 업그레이드해야 한다는 것이었다고 [답했다](https://lwn.net/ml/oss-security/2026050155-yelp-bonnet-bfd2@gregkh/). 그는 또한 “누구도 사소한 익스플로잇을 풀어놓으려 한다고 우리에게 말할 의무가 없기 때문에” 커널 팀은 Copy Fail 발표를 사전에 알지 못했고, 무엇보다 모두에게 모든 것을 알려야 하는 상황이 되지 않도록 팀은 다른 이들에게 사전에 알리는 것이 허용되지 않는다고 덧붙였다. “그것이 모든 법률/정부 기관이 우리가 운영할 수 있도록 동의한 유일한 정책이므로, 우리는 그 안에 묶여 있습니다.”

5월 3일 James는 Xint의 Brian Pak이 남긴 [댓글](https://xcancel.com/brian_pak/status/2050255271184994538#m) 링크를 [공유했다](https://lwn.net/ml/oss-security/878qa0b1o9.fsf@gentoo.org/). 그 댓글은 회사가 취약점을 보고할 때 완전히 동작하는 익스플로잇을 커널 보안팀에 제공했다고 말했다. “그 뒤로 우리는 그런 세부 사항이 하위 단계(downstream)로 자동 전달되지 않으며 Linux 커널 커밋 메시지는 보통 최소한으로 유지된다는 것을 알게 되었습니다. 그저 그 과정이 그렇게 작동할 뿐입니다.” James는 커널 팀이 “처음부터 그 영향을 매우 잘 알고 있었다”고 말하며, 커널 팀이 “이번 일이 이렇게 진행된 방식에 진심으로 자부심을 느끼는지” [물었다](https://lwn.net/ml/oss-security/878qa0b1o9.fsf@gentoo.org/).

#### CVE 쓰레기 더미

Kroah-Hartman은 James가 커널 팀이 정확히 무엇을 더 잘해야 한다고 제안하는지, 그리고 그것을 어떻게 해야 하는지 [물었다](https://lwn.net/ml/oss-security/2026050453-gamma-stuffing-8606@gregkh/). 그는 팀이 로컬 사용자 권한 상승 버그 보고를 항상 받는다고 덧붙였다. 제출자가 이를 자기 소프트웨어를 과시하는 데 사용하기 전까지는 이 건이 특별하다는 점이 사후적으로야 분명해졌을 뿐이었다. “그런 일은 보통 일어나지 않으며, 여기에 관여한 우리 모두의 통제 밖에 있습니다.” Emily Shepherd는 PoC나 결함의 심각성에 대한 설명이 제공되었는지 [알고 싶어 했다](https://lwn.net/ml/oss-security/CACHV8XoX5vtjH3d1KKhQJ5_fr8qBRG7pnWFsLxw5UzngeoeA=Q@mail.gmail.com/). Kroah-Hartman은 “그것은 몇 달 전, 수백 건 아니면 수천 건의 보고 전 일이었기 때문에” 솔직히 기억하지 못한다고 [답했다](https://lwn.net/ml/oss-security/2026050435-c08cb4e9297e204898fa6911@gregkh/). 그는 또한 커널 보안팀이 어떻게 운영되는지 리스트에 상기시켰다.

> 커널 보안팀의 임무는 버그 보고를 분류(triage)하고, 관련 유지관리자/개발자를 끌어들여 문제를 최대한 빨리 수정하고 Linus의 트리에 병합되게 하는 것입니다. 일단 Linus의 트리에 들어가면 우리의 역할은 끝납니다.
>
> 우리는 누구에게도 어떤 “공지”도 하지 않습니다. 따라서 이것이 “이 시스템을 얼마나 심하게 악용할 수 있는지 보라”는 유형의 것이라 하더라도, 우리는 누구에게도 아무것도 말하지 않을 것입니다.

그는 자신이 이를 자세히 문서화했고, 여러 차례 강연했으며, 관련 내용을 [블로그에도 써 오고 있다](http://www.kroah.com/log/blog/2026/01/02/linux-kernel-security-work/)고 덧붙였다.

소셜 미디어에서 Josh Bressers는 “모든 AI 취약점 회사는 그럴듯한 것을 찾고 싶어 하지만, 발견 사항을 어떻게 조율해야 하는지는 전혀 모른다”며 책임이 회사에 있다고 [제안했다](https://infosec.exchange/@joshbressers/116496779235415652). Kroah-Hartman은 취약점 조율이 이제 가능하다는 생각 자체를 [일축했다](https://social.kernel.org/notice/B5qZYF8W1VYkUdhkUi#:~:text=people%20think%20that). Bressers도 “전통적인 공개 모델이 영원히 사라졌다는 점에서는 당신이 옳다고 생각합니다”라고 [동의했다](https://infosec.exchange/@joshbressers/116499242263234495). 그는 Copy Fail이 큰 사건이 될 것이라는 점은 “꽤 명백했다”고 보았지만, 중요한 취약점이 “거대한 CVE 쓰레기 더미” 속에 파묻히는 것을 막기 위해 무엇을 해야 할지는 알지 못했다.[^art1a-note3]

Copy Fail은 수천 개 취약점 중 하나일 뿐이다. LLM 도구가 발견 속도를 높이는 듯한 속도를 보면, Kroah-Hartman의 말에도 일리가 있어 보인다. 전통적인 공개 알림은 점점 더 어려워지고 있으며, 아예 불가능해지고 있을지도 모른다. 보고량 자체와 더불어, AI 보조 보고자 중 상당수가 보안 공개가 보통 어떻게 작동하는지 익숙하지 않을 것이라는 사실은 엠바고와 조율된 수정에 의존하는 일이 점점 더 위험해질 것임을 뜻한다. 원하든 원하지 않든, 우리는 오픈소스 보안에 있어 흥미로운 시대를 살고 있다.

[댓글(28개 게시됨)](https://lwn.net/Articles/1070698/#Comments)

### [재시작 가능 시퀀스, TCMalloc, 그리고 하이럼의 법칙](https://lwn.net/Articles/1070072/)

#### 요약

- Linux 6.19의 restartable sequences 성능 개선은 문서화된 ABI를 지켰지만, TCMalloc이 의존하던 문서화되지 않은 동작을 바꾸어 실제 애플리케이션을 깨뜨렸습니다.
- TCMalloc은 `struct rseq`의 `cpu_id_start` 필드를 내부 포인터와 겹쳐 쓰는 방식으로 스케줄링 중단을 감지해 왔습니다.
- 커널 개발자들은 이 사용법이 ABI 위반이라고 보지만, Linus Torvalds는 “이전에 동작하던 프로그램이 커널 변경으로 깨졌다”는 점에서 회귀 규칙을 적용해야 한다고 했습니다.
- 제안된 해결책은 `struct rseq` 크기와 정렬을 이용해 기존 TCMalloc에는 이전 동작을, 최신 glibc 등에는 더 빠른 6.19 동작을 제공하는 것입니다.
- 이 사건은 하이럼의 법칙처럼, 커널이 우연히 노출한 관찰 가능한 동작이 장기 호환성 부담으로 굳어질 수 있음을 보여줍니다.

작성자

Jonathan Corbet

2026년 4월 30일

하이럼의 법칙(Hyrum's Law)은 시스템의 관찰 가능한 모든 동작이 결국 누군가에게 의존 대상이 된다고 말한다. 커널 커뮤니티는 현재 그 원칙을 분명하게 보여주는 사례를 다루고 있다. 6.19 릴리스에서 일부 재시작 가능 시퀀스(restartable sequences) 성능 문제를 해결하기 위한 최근 작업은 문서화된 API를 모든 면에서 유지했지만, 그것만으로는 충분하지 않았다. Google의 TCMalloc 라이브러리는 밝혀진 바에 따르면 문서화된 API를 위반하고, 다른 코드가 restartable 기능을 사용하지 못하게 하며, 6.19에서 깨진다. 하지만 커널의 “회귀 금지(no regressions)” 규칙은 개발자들에게 TCMalloc의 동작을 수용할 방법을 찾도록 강제하고 있다.[^art1a-note4]

간단히 상기하자면, [`rseq()` 시스템 호출](https://lwn.net/Articles/1033957/)을 통해 접근하는 restartable sequences 기능은 사용자 공간(user space)에서 짧은 임계 구역(critical section)을 실행하기 위한 메커니즘을 제공한다. 공유 메모리 세그먼트를 사용해 임계 구역이 활성 상태임을 커널에 알리고, 실행 중인 스레드가 그 임계 구역 중에 선점(preempt)되거나 다른 CPU로 이동(migrate)되면 커널이 실행을 다른 위치로 돌릴 수 있다. 관련 기능은 여럿 있는데, 스레드가 어느 CPU에서 실행 중인지 빠르게 확인하는 기능도 포함된다. 7.0 릴리스에 병합된 [time-slice-extension 기능](https://lwn.net/Articles/1038235/)도 restartable sequences와 연결되어 있다. middle-ad

#### TCMalloc 문제

4월 22일 Mathias Stearn은 restartable sequences에 대한 6.19 개선으로 인해 TCMalloc에서 발생한 [두 가지 문제를 보고했다](https://lwn.net/ml/all/CAHnCjA25b+nO2n5CeifknSKHssJpPrjnf+dtr7UgzRw4Zgu=oA@mail.gmail.com). 그중 하나는 64비트 Arm 구현의 단순한 버그로 드러났으며, Arm 아키텍처가 아직 generic entry code를 완전히 사용하지 않는다는 사실과 관련되어 있었다. 이 버그에는 논란의 여지가 없으며 다른 버그처럼 수정될 것이다. 그러나 두 번째 문제는 더 깊은 뿌리를 가지고 있다.

restartable sequences를 위해 커널과 사용자 공간이 공유하는 메모리에는 [`struct rseq`](https://elixir.bootlin.com/linux/v7.0.1/source/include/uapi/linux/rseq.h#L89) 인스턴스가 포함된다. 그 구조체에는 여러 필드가 있는데, 이 논의에서 특히 관심을 끄는 필드가 하나 있다. 32비트 `cpu_id_start` 필드는 스레드가 실행 중인 CPU 번호를 담는다. 커널이 유지하는 이 값은 사용자 공간에 대해 명시적으로 읽기 전용 값으로 정의되어 있으며, restartable sequences가 사용 중이 아니더라도 항상 유효한 CPU 번호를 담는다고 보장된다.

6.19 릴리스 전에는 CPU 번호가 바뀌었는지 여부와 상관없이, 커널이 커널에서 사용자 공간으로 돌아갈 때마다 `cpu_id_start`를 갱신했다. 정수 값 하나를 저장하는 일이 비싼 작업처럼 보이지는 않지만, 겉보기와 다를 수 있다. 많은 CPU에는 커널이 사용자 공간 메모리를 임의로 변경하지 못하게 하는 기능이 있다. 그 보호를 끄고(그리고 저장 후 다시 켜는) 일은 *비용이 크다*. 불필요한 저장을 제거하자 restartable-sequences ABI를 전혀 바꾸지 않고도 많은 워크로드에서 성능이 15% 향상되었다. 적어도 그렇게 보였다.

TCMalloc 라이브러리는 성능 향상을 위해 restartable sequences를 광범위하게 사용한다. 특히 이 기능을 임계 구역에 사용하기는 하지만, 임계 구역 밖의 스케줄링 중단을 감지하는 데도 사용한다. 더 부정적인 표현을 피하자면 이 요령은 [이 문서](https://google.github.io/tcmalloc/rseq.html)에 자세히 설명되어 있다. 간단히 말해, TCMalloc의 내부 데이터 구조는 공유 `struct rseq` 위에 겹쳐지도록(overlay) 설계되어 `cpu_id_start`가 내부 캐시 포인터의 상위 4바이트가 되게 한다. TCMalloc이 이 포인터를 저장하면 그 결과 `cpu_id_start`에 0이 기록된다. 다만 최상위 비트는 설정되어, `cpu_id_start`의 내용이 유효한 CPU 번호와 구별되도록 한다. 커널이 `cpu_id_start`에 저장하면 결국 그 최상위 비트가 지워지고, TCMalloc은 그 변화를 빠르게 감지해 해당 포인터를 다시 생성할 수 있다.

핵심은 실행 중인 스레드가 새 CPU로 이동하지 않았더라도, TCMalloc은 어떤 종류의 중단에 대해서도 그 신호가 필요하다는 점이다. 6.19 이전 커널은 언제나 `cpu_id_start`를 덮어썼다. 이는 문서화되지 않았지만 관찰 가능한 동작이었고, TCMalloc에 그 신호를 제공했다. 6.19부터는 스레드가 새 CPU로 이동할 때만 그 덮어쓰기가 일어난다. 그 결과 그 문서화되지 않은 동작에 의존하게 된 TCMalloc은 이를 사용하려는 모든 애플리케이션 한가운데에 연기 나는 분화구를 남기게 된다.

#### 회귀인가?

이 동작의 문제성은 몇 년 전부터 널리 알려져 있었다. 위에서 링크한 문서는 `cpu_id_start`가 더 이상 현재 CPU 번호를 담는다고 믿을 수 없으므로 “이로 인해 `__rseq_abi.cpu_id_start`는 원래 목적에 사용할 수 없게 된다”고 조언한다. 다시 말해 TCMalloc을 사용하는 스레드 안에서 실행되는 다른 어떤 코드도 restartable sequences를 사용하면서 제대로 동작하리라 기대할 수 없다. 이 기능의 또 다른 사용자가 버전 2.35부터 GNU C Library(glibc)라는 점을 고려하면 이는 다소 곤란하다. 2022년에 TCMalloc 이슈 트래커에 [이 문제가 보고되었고](https://github.com/google/tcmalloc/issues/144) 동작 변경이 요청되었지만, 상당한 논의에도 불구하고 변경은 이뤄지지 않았다. 그 결과 TCMalloc을 사용하는 코드는 glibc가 restartable sequences를 사용하려 하지 못하게 하는 환경 변수를 설정한 채 실행해야 한다.

커널 개발자들은 한동안 이 동작을 좋지 않게 보아 왔다. 당연하게도, 6.19 릴리스가 TCMalloc을 완전히 깨뜨렸다는 사용자 불만이 나오자 그 시선은 더욱 싸늘해졌다. 위에서 설명한 동작은 문서화된 restartable-sequences ABI를 위반하며 다른 누구도 이 기능을 사용할 수 없게 만든다. 커널의 디버깅 기능이 있었다면 이를 감지했겠지만, 그 기능이 TCMalloc과 함께 사용된 적은 명백히 없었다. 사용되었다면 문제를 일으킨 스레드가 즉시 종료되었을 것이기 때문이다. 이슈 논의에서 커널 개발자들은 TCMalloc이 `cpu_id_start`를 덮어쓰지 않도록 할 수 있는 restartable sequences [확장 기능을 제안했지만](https://github.com/google/tcmalloc/issues/144#issuecomment-2306880781), 그 제안은 받아들여지지 않았다. 그 결과를 Thomas Gleixner는 “모두가 곤란한 처지에 빠졌고 노도 없이 개울 위에 떠 있는 상황”이라고 [묘사했다](https://lwn.net/ml/all/87cxzp1tn6.ffs@tglx).

Gleixner는 문서화된 ABI 보장은 여전히 커널이 지키고 있고 디버깅 기능이 몇 년 전에 문제를 잡아냈을 것이므로, TCMalloc의 어려움을 커널 회귀로 간주해서는 안 된다고 생각한다는 점을 분명히 했다. 그러나 Linus Torvalds도 한때 동작하던 프로그램이 커널 변경의 결과로 동작하지 않게 되었다는 점만이 중요하다고 [마찬가지로 분명히 했다](https://lwn.net/ml/all/CAHk-=wjsEqWJxXArS-P5+ksSY2Apaox8u6FtUrtyWSBEOL4Q2Q@mail.gmail.com). “이것은 어떤 종류의 회색 지대도 아닙니다. 명백히 우리의 회귀 규칙을 위반합니다.”

이 반응은 Gleixner가 분명 예상했던 것이지만, [그는 여전히 마음에 들어 하지 않았다](https://lwn.net/ml/all/874il11jac.ffs@tglx). “그것을 강제하는 것은 자유지만, 그렇게 함으로써 단 하나의 남용자가 커널의 일반 공유 인터페이스를 영원히 정당하게 소유하고 다른 모두가 포기하도록 강제할 수 있다는 선례를 세운다는 점을 알아두십시오.” Glibc 개발자 Florian Weimer도 TCMalloc의 사용 방식이 restartable-sequences ABI의 모듈식 설계를 깨뜨린다고 지적하며 [불만을 나타냈다](https://lwn.net/ml/all/lhuqzo051cq.fsf@oldenburg.str.redhat.com). 그러나 Torvalds는 해결책을 찾아야 한다고 [완강했다](https://lwn.net/ml/all/CAHk-=wiLdmz92CCfu2+-9_UrGSn6Pu6sUVvLs5gjyhGaEov-BA@mail.gmail.com).

#### 이제 어떻게 할 것인가?

여러 수정 선택지가 논의되었다. Stearn은 단순하고 저비용인 선택지를 [작업 중이었지만](https://lwn.net/ml/all/CAHnCjA3aR1hLYK3DsXZV5AaLWe56+zLOS8ffpAMv9TBEkT-3nA@mail.gmail.com), 겉보기에는 잘 풀리지 않은 듯하다. 물론 다른 선택지는 단순히 `cpu_id_start`를 항상 갱신하는 방식으로 되돌아가 관련 성능 비용을 받아들이는 것이다. 커널 커뮤니티에서 이 접근법을 지지하는 사람은 많지 않다. 이 글을 쓰는 시점에서 가장 가능성이 높은 수정은 [Gleixner의 이 패치](https://lwn.net/ml/all/87jyttz8cf.ffs@tglx)에 기반한 무언가로, 일부 환경에서 성능 비용이 있기는 하지만 TCMalloc이나 glibc 어느 쪽에도 변경을 요구하지 않고 동작한다.

최근의 많은 시스템 호출과 같은 패턴으로, `rseq()`는 호출자가 `struct rseq`에 대한 포인터와 그 구조체의 크기를 모두 전달하도록 요구한다. 이렇게 하면 앞으로 그 크기를 늘리는 방식으로 호환성을 유지하며 확장할 수 있다. Gleixner는 현재 32바이트인 크기를 33바이트로 늘릴 것을 제안하는데, 이는 구조체에 64바이트 정렬을 강제하는 효과도 낸다. 32바이트 `struct rseq`를 제시하거나 구조체를 제대로 정렬하지 못하는 호출자는 6.19 이전 동작, 즉 `cpu_id_start`의 무조건 갱신을 보게 된다. time-slice extension 같은 더 최근 관련 기능도 사용할 수 없게 된다. 반대로 호출자가 33바이트이고 64바이트로 정렬된 `rseq` 구조체를 제공하면, 커널은 완전한 성능을 갖춘 6.19 동작을 제공한다.[^art1a-note5]

그 결과는 완전히 호환되는 변경이어야 한다. 기존 TCMalloc 설치는 더 오래된 구조체 크기를 사용할 것이다. 또한 이 라이브러리가 쓰는 overlay 요령은 구조체의 64바이트 정렬도 막는다. 따라서 TCMalloc에는 그것이 의존하는 예전 동작이 주어진다. 최신 glibc 버전은 [`getauxval()`](https://man7.org/linux/man-pages/man3/getauxval.3.html)을 사용해 예상 구조체 크기를 질의하며, glibc 업데이트 없이도 더 높은 성능과 전체 기능을 보상으로 얻게 된다.

하지만 더 오래된 glibc 버전(2.41 이전)은 성능 비용에 묶이게 된다. Weimer는 그 버전들을 업데이트하는 일이 쉽지 않을 것이라고 [시사했다](https://lwn.net/ml/all/lhujyts4zr8.fsf@oldenburg.str.redhat.com). Mathieu Desnoyers는 `rseq()`에 “나는 TCMalloc이 아니다”라는 표시로 전달할 수 있는 플래그를 추가해 더 빠른 동작을 얻도록 하자고 [제안했다](https://lwn.net/ml/all/7f8783a6-1a48-4c92-850c-d285a788b491@efficios.com). 그 플래그를 추가하는 것은 오래된 glibc 버전에 훨씬 쉽게 백포트할 수 있을 것이다. 그러나 Gleixner는 그것이 코드에 불필요한 복잡성을 초래하고, 어쨌든 하나의 애플리케이션 안에 restartable sequences 사용자가 여러 명 있는 경우 문제가 될 것이라며 [그 생각을 일축했다](https://lwn.net/ml/all/87bjf4yuym.ffs@tglx).

이 해법은 초기 테스트를 통과한 것으로 보이며, 이를 필요하게 만든 사람들을 향한 날카로운 말과 함께 [정식 패치 시리즈](https://lwn.net/ml/all/20260428221058.149538293@kernel.org)로 구성되었다.

> Linus가 명한 대로 책임은 원래 RSEQ 커널 구현에서 ABI 준수 강제가 부족했던 데 있으며, 영리한 남용은 괜찮다는 것입니다. 기술적으로는 맞지만, 더 큰 생태계의 맥락에서는 근본적으로 결함 있는 결정입니다. 다만 이는 오픈소스 생태계 전반의 장기 지속 가능성과, 그 생태계를 인질로 잡고 자신들에게 운영 기반을 제공하는 사람들에게 발전을 위해 무리하게 나서라고 강제할 공식 권리를 얻게 되는 악의적 행위자로부터 생태계를 보호할 능력에 영향을 주는, 완전히 별개의 논의입니다.

불평은 제쳐두고, 하이럼의 법칙을 보여주는 이 특정 사례에 대한 해법의 형태는 정리된 듯하다. 이상한 일을 하는 다른 사용자가 없다면, 기존 사용자를 깨뜨리지 않으면서 지금까지 이루어진 모든 개선을 보존하고 앞으로 나아갈 수 있을 것이다. restartable sequences 사용자가 많지 않기 때문에 다른 놀라움이 없을 가능성은 꽤 높아 보인다. 결국 상황은 분명 더 나쁠 수도 있었다.

그렇다고 해도 이번 사건은 앞으로 비슷한 호환성 문제를 만들 수 있는 기능을 노출하는 일을 두려워하는 개발자들에게 안심을 주지는 못할 것이다. 새 인터페이스 추가에 대한 많은 논의가 바로 그 지점에서 좌초해 왔다. 예를 들어 BPF 프로그램이 메모리 관리의 더 많은 측면을 제어하도록 허용하자는 아이디어에 대해 David Hildenbrand가 보인 [이 응답](https://lwn.net/ml/all/014f3c0a-7c6f-4f64-95cd-b7b69d804880@kernel.org)을 보라. 하이럼이 구석에 숨어서, 커널이 우연히 노출한 어떤 동작을 굳혀 버릴 기회만 기다리고 있는 모습을 쉽게 떠올릴 수 있다.[^art1a-note6]

[댓글(34개 게시됨)](https://lwn.net/Articles/1070072/#Comments)

[^art1a-note1]: 조율된 공개(coordinated disclosure)는 취약점 보고자, 업스트림 프로젝트, 벤더, 배포판이 일정 기간 비공개로 수정과 배포 준비를 맞춘 뒤 공개하는 관행이다. 공개 LLM 서비스에 취약점 세부 정보가 입력되거나 여러 연구자가 같은 모델·프롬프트로 같은 결함을 찾는 경우, “비공개로 준비할 시간”이라는 전제가 약해진다.

[^art1a-note2]: 로컬 권한 상승(local privilege escalation)은 원격 침입 자체를 가능하게 하지는 않더라도, 이미 낮은 권한으로 시스템에 들어온 공격자나 악성 로컬 사용자가 관리자 권한(root)을 얻는 데 쓰일 수 있다. 컨테이너 호스트, 다중 사용자 서버, CI 러너처럼 신뢰 수준이 다른 코드가 함께 실행되는 환경에서는 특히 큰 위험이 된다.

[^art1a-note3]: CVSS 점수와 CVE 목록은 취약점의 우선순위를 정하는 출발점일 뿐이다. 실제 운영에서는 익스플로잇 공개 여부, 악용 난이도, 노출된 자산 수, 패치 가용성, 배포판 백포트 상태가 함께 고려되어야 하며, LLM으로 보고량이 늘수록 이 선별 작업의 자동화와 사람 검토가 모두 중요해진다.

[^art1a-note4]: Linux 커널의 회귀 금지 원칙은 “사용자 공간을 깨뜨리지 말라”는 정책의 실무적 표현이다. 프로그램이 문서화된 인터페이스를 깔끔하게 사용했는지와 별개로, 실제로 널리 배포된 프로그램이 커널 변경 뒤 동작하지 않으면 커널 쪽에서 우회책을 찾는 경우가 많다.

[^art1a-note5]: `rseq()`는 스레드별(per-thread) 빠른 경로 최적화를 위해 설계된 인터페이스다. 할당자(allocator), 런타임, C 라이브러리처럼 프로세스 안에서 동시에 존재하는 구성요소들이 같은 `struct rseq`를 공유하거나 가정할 수 있으므로, ABI 크기·정렬 같은 작은 세부 사항도 장기 호환성 장치로 사용된다.

[^art1a-note6]: 하이럼의 법칙은 커널 ABI뿐 아니라 성능 특성, 오류 코드, 타이밍, 디버그 부작용에도 적용될 수 있다. 따라서 커널 개발자는 새 기능을 내보낼 때 “문서화한 계약”뿐 아니라 “관찰 가능한 구현 세부 사항”이 훗날 사실상의 계약으로 굳어질 가능성까지 고려해야 한다.

---

### [버그 모니터링 기대치와 Fedora GNOME 패키지](https://lwn.net/Articles/1070006/)

#### 요약

- Fedora의 여러 GNOME 패키지 버그에는 “적극적으로 모니터링되지 않는다”는 자동 응답이 붙어 왔고, 이는 패키지 관리자가 버그를 제때 처리해야 한다는 Fedora 정책과 충돌할 수 있다는 문제를 낳았다.
- GNOME 유지관리자들은 Bugzilla에 쌓이는 버그 수가 너무 많아 현실적으로 처리하기 어렵다며, 사용자가 GNOME 업스트림(upstream)에 직접 보고하는 편이 더 효과적이라고 주장해 왔다.
- 반대 측은 Fedora가 사용자와 업스트림 사이의 “깔때기” 역할을 포기하면 배포판의 가치가 줄어들고, Fedora에만 해당하는 패키징 문제를 놓칠 수 있다고 지적했다.
- FESCo는 2026년 4월 28일 자동 응답에서 “적극적으로 모니터링되지 않는다”는 문장을 삭제하기로 했지만, 버그 처리 책임 자체에 대한 근본 해법은 아직 정하지 않았다.
- 향후 Fedora가 Forgejo/Fedora Forge 기반 버그 추적으로 옮겨 가면, 사용자가 Fedora 버그를 열기 전에 업스트림 보고가 적절한지 안내하는 템플릿이 절충안이 될 수 있다.

글쓴이

Joe Brockmeier

2026년 5월 4일

수년 동안 Fedora의 GNOME 패키지에 대해 버그 보고서를 제출한 사용자들은, 그 보고서가 적극적으로 모니터링되지 않는다는 자동 응답을 받아 왔다. 대신 사용자는 GNOME 업스트림(upstream)에 버그를 제출하라는 권고를 받았다. 그러나 이 관행은 패키지 관리자가 “보고된 버그를 적시에 처리해야 한다”고 명시한 [Fedora Engineering Steering Committee](https://docs.fedoraproject.org/en-US/fesco/)(FESCo)[^art1b-note1]의 [정책](https://docs.fedoraproject.org/en-US/fesco/Package_maintainer_responsibilities/#_deal_with_bugs)과 충돌하는 듯 보인다. 4월 28일 FESCo는 실제 관행과 정책 사이의 괴리를 논의했지만, 지금까지는 자동 응답 문구를 조금 손보는 데 그쳤다.

Fedora의 많은 GNOME 패키지는 Red Hat 데스크톱 팀 구성원들이 유지관리한다. [`gnome-disk-utility`](https://packages.fedoraproject.org/pkgs/gnome-disk-utility/), [`gnome-session`](https://packages.fedoraproject.org/pkgs/gnome-session/), [`nautilus`](https://packages.fedoraproject.org/pkgs/nautilus/) 같은 일부 패키지에 제출된 버그는 Bugzilla 버그 추적기(bug tracker)[^art1b-note2]에서 자동으로 “gnome-sig” 별칭(alias)에 배정된다. 이 그룹에는 21명의 구성원이 있지만, 그들이 모두 현재 활동 중인지는 분명하지 않다.

이 글을 쓰는 시점에 gnome-sig에 배정된 버그는 거의 [750개](https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&columnlist=product%2Ccomponent%2Cassigned_to%2Cstatus%2Csummary%2Clast_change_time%2Cseverity%2Cpriority&email1=gnome-sig%40lists.fedoraproject.org&emailassigned_to1=1&emailtype1=substring&list_id=13669429&order=status%2C%20priority%2C%20assigned_to%2C%20id%2C%20&query_format=advanced)에 달한다. 다만 그중 일부 버그는 10년도 더 전에 열린 것이며, 어느 시점에 패키지 소유권이 바뀌면서 이 그룹에 재배정된 것이다. 아마 패키지가 “고아(orphaned)”가 되었고 다른 패키저가 이를 맡겠다고 나서지 않았기 때문일 가능성이 크다. 버그가 gnome-sig에 배정되면 다음과 같은 내용의 자동 응답을 받는다.

> Red Hat Bugzilla에서 이 구성 요소에 대한 버그 보고서는 적극적으로 모니터링되지 않습니다. 문제가 해결될 가능성을 높이려면 https://gitlab.gnome.org/GNOME/ 에서 GNOME에 직접 문제를 보고하는 것을 고려해 주십시오.

2월에 Carl George는 이 자동 응답에 대해 FESCo에 [티켓을 열었다](https://pagure.io/fesco/issue/3568). 그는 “업스트림 프로젝트와의 협업을 장려하는 것은 전적으로 합리적”이라고 했지만, 그 응답은 버그가 전혀 모니터링되지 않는다는 인상을 주며, 이는 패키지 관리자가 Fedora 정책상 책임을 다하지 않는다는 뜻이 될 수 있다고 말했다. “FESCo가 이 문제를 어떻게 다루어야 하는지 지침을 제공할 수 있을까요?”

#### 버그가 너무 많다

FESCo 구성원 Kevin Fenzi는 자동 응답으로 이어진 2020년 Fedora Workstation 논의 링크를 달아 [답변했다](https://pagure.io/fesco/issue/3568#comment-1004791). Michael Catanzaro는 그 [대화](https://forge.fedoraproject.org/workstation/tickets/issues/131)를 시작하며, Fedora의 GNOME 개발자 대부분이 Bugzilla를 포기했다고 생각한다고 말했다. “현재 그곳은 심각한 버그까지 포함해 버그가 무시되고 아무 응답도 받지 못하는 곳입니다. 이런 현상 유지는 사용자에게 공정하지 않습니다.” Fedora GNOME 개발자들은 자신들이 소유한 패키지를 “대략적으로만” 알고 있었다. “다른 GNOME 유지관리자 몇 명에게 얼마나 많은 버그가 배정되어 있는지 확인해 보니 260개, 182개, 420개, 511개, 372개였습니다.” 그는 버그 수가 더 적었지만, “수십 개의 패키지”를 유지관리하는 대부분의 GNOME 유지관리자보다 소유한 패키지도 더 적었다.

Catanzaro는 처리하기에 버그가 너무 많다고 말했다. 이를 업스트림으로 옮기는 일도 시간이 너무 오래 걸렸다. “버그를 옮기는 데 너무 많은 시간을 쓰느라 다른 일을 아무것도 못 하게 될 것입니다.” 애초에 업스트림에 버그가 제출된다면, 버그가 “올바른 개발자에게 곧장” 가기 때문에 “버그 보고서가 무시되지 않을 가능성이 꽤 있다.” Allan Day는 GNOME만 Fedora 버그 관리 문제를 겪는 업스트림인지 [궁금해했다](https://forge.fedoraproject.org/workstation/tickets/issues/131#issuecomment-368133). Neal Gompa는 KDE도 어려움을 겪고 있다고 [답했지만](https://forge.fedoraproject.org/workstation/tickets/issues/131#issuecomment-368134), 업스트림 프로젝트와 Fedora 양쪽에 버그를 모두 제출하는 편이 더 타당하다고 보았다. “그렇게 하면 Fedora 절차는 계속 작동하고, GNOME/KDE 사람들은 업스트림 보고에 집중할 수 있습니다.”

FESCo 구성원 Fabio Valentini는 GNOME 변경 사항이 Fedora에서는 문제를 일으키지만 업스트림 버그로는 인정되지 않는 경우가 많다고 [지적했다](https://forge.fedoraproject.org/workstation/tickets/issues/131#issuecomment-368136). 예를 들어 GNOME이 D-Bus 인터페이스를 변경하면, [elementary OS](https://elementary.io/)용으로 개발되어 Fedora에 패키징된 [Pantheon](https://en.wikipedia.org/wiki/Elementary_OS#Pantheon_desktop_environment) 데스크톱 환경에서 충돌(crash)이 발생할 수 있다. 그는 그런 문제를 GNOME의 GitLab 인스턴스에 보고하는 것은 잘못된 곳이라는 말을 들었다. 그 문제들은 “그저 ‘버그가 아니라 기능(features, not bugs)’”이기 때문이라는 것이다.

Owen Taylor는 자신에게 배정된 수백 개의 버그를 무시했던 Fedora 유지관리자 중 한 명임을 [인정했다](https://forge.fedoraproject.org/workstation/tickets/issues/131#issuecomment-368145). Fedora Bugzilla에서 버그를 살펴보면 때때로 업스트림 버그 수정으로 이어지는 “흥미롭고 호기심을 끄는 것”이 많이 나오지만, “Bugzilla를 어느 정도 깨끗한 상태에 가깝게 만들려면 거의 전업 Bugzilla 분류 담당자(triager)가 되어야 했고, 다른 일은 아무것도 못 했을 것”이라고 했다. 그는 Fedora의 [Automatic Bug-Reporting Tool](https://github.com/abrt/abrt#abrt)(ABRT)[^art1b-note3]이 GNOME 버그를 업스트림에 보고하도록 가르치고 싶어 했다. 다만 그것은 애플리케이션 충돌이 감지되어 새로 열리는 버그에만 적용될 수 있었다. 또한 그는 문제가 패키징과 관련되어 있거나 배포판에 고유한 것으로 보이지 않는 한, 사용자에게 업스트림에 버그를 보고하라는 제안을 보여 주고 싶어 했다.

논의는 계속되었고, 일종의 해법이 마침내 나왔다. 2023년 6월 Tomas Popela는 사용자가 버그를 제출한 *뒤에*, 그 버그가 패키징이나 Fedora 릴리스 절차와 관련된 것이 아니라면(예: 버그가 Fedora 릴리스를 막는 경우가 아니라면) 업스트림에 버그를 보고해야 한다는 댓글을 자동으로 추가하는 Bugzilla 규칙을 만들겠다고 [말했다](https://forge.fedoraproject.org/workstation/tickets/issues/131#issuecomment-368177). 그 규칙은 2023년 11월 [구현되었다](https://forge.fedoraproject.org/workstation/tickets/issues/131#issuecomment-368190).

ABRT는 버그를 업스트림에 보고하는 방법을 배우지 못했고, 수년간 방치된 끝에 현재 [퇴역 절차](https://discussion.fedoraproject.org/t/last-call-to-save-abrt/188901)를 밟고 있다. Catanzaro는 Red Hat이 ABRT 작업에 개발자를 더 이상 배정하지 않고 있으며, 커뮤니티에서도 이를 유지관리하겠다고 나선 사람이 없다고 말했다. ABRT의 그래픽 사용자 인터페이스 구성 요소는 Fedora 44에서 제거되었고, Fedora 45 이전에 [전체를 제거](https://forge.fedoraproject.org/workstation/tickets/issues/503)하는 것이 계획이다.

#### 커뮤니티 논의

FESCo는 2월 17일 회의에서, 모니터링되지 않는 버그 보고서에 대한 커뮤니티 의견을 얻기 위해 Fedora 포럼에 논의를 열기로 [결정했다](https://pagure.io/fesco/issue/3568#comment-1005192). Valentini는 [스레드를 시작한](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434) 뒤, 이 주제에 대한 자신의 의견으로 [후속 글](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434/2)을 올렸다. 그는 일부 GNOME 구성 요소에 터무니없이 많은 버그가 제출되고 있다는 점에는 동의했지만, 자동 응답은 도움이 되지 않는다고 보았다. 그는 일단 버그가 제출되면 사람들은 자신이 해야 할 일을 끝냈다고 느끼는데, “그러고 나서 그 모든 일을 다른 곳에서 *다시* 하라는 요청을 받는다”고 말했다.

George는 정책상 유지관리자가 버그를 제때 처리해야 하므로, 정책을 바꾸거나 Fedora 정책과 일치하도록 응답을 바꾸어야 한다고 [답했다](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434/4). Gompa는 Fedora KDE 유지관리자들도 “매우 무거운 버그 보고 부담”을 안고 있지만 특별 대우를 요청하지는 않았다고 [말했다](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434/5). 그는 팀이 “닫아야 할 버그 보고서에 태그를 붙이는 데 상당히 서툴다”는 점은 인정했지만, 사용자에게 버그 보고서가 기본적으로 무시된다는 메시지를 전달하는 것은 좋은 생각이 아니라고 느꼈다.

> 제게는 이런 행동이 Fedora가 사용자나 업스트림에 가치를 제공하지 않는 것처럼 느끼게 합니다. 유지관리자들이 그런 깔때기 역할을 하거나, 자신들이 유지관리하는 구성 요소의 품질 향상을 돕기 위해 공유 인프라를 활용하지 않는다면, 그들이 무엇을 하고 있는지 모르겠습니다.

Fedora는 현재 협업 개발 플랫폼으로 [Forgejo 도입](https://fedoramagazine.org/fedora-moves-towards-forgejo-a-unified-decision/)을 진행 중이며, 이는 (언젠가는) 버그 보고 추적에 Bugzilla 대신 [Fedora Forge](https://forge.fedoraproject.org/)를 사용하는 것까지 포함할 것이다.[^art1b-note4] Catanzaro는 그런 일이 일어나면 사용자는 Fedora 프로젝트에 버그를 열기 전에 업스트림으로 안내하는 보고서 템플릿을 보게 될 것이라고 [말했다](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434/6). 그는 Fedora가 버그가 올바른 곳에 보고되도록 보장하기 위해 버그 추적기와 버그 보고 도구를 고치는 데 집중해야 한다고 제안했다. “패키저가 다운스트림(downstream) 버그 보고서를 읽을 것으로 기대하는 것은 정말 현실적이지 않다고 생각합니다.”

Gompa는 사용자에게 업스트림으로 가라고 말하는 것은 여러 이유에서 나쁜 생각이라고 [주장했다](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434/8). Fedora와 GNOME 사이에는 구성 요소의 일대일 대응이 없으며, 사용자는 수정이 얼마나 빨리 전달될 수 있는지에 영향을 줄 수도 있고 그렇지 않을 수도 있는 개발자들과 상호작용하게 된다. George는 그것이 현실적인지 여부와 상관없이, Fedora의 현 정책은 패키저가 버그 보고서를 읽고 응답하도록 요구한다고 [답했다](https://discussion.fedoraproject.org/t/package-maintainer-responsiblities-vs-unmonitored-bugzilla-components-for-gnome-packages/181434/11).

#### 메시지를 바꾸다

공개 논의가 잦아들 시간을 가진 뒤, FESCo는 4월 28일 회의에서 이 주제를 다시 다루었다([로그](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-04-28/fesco.2026-04-28-17.00.log.html)). FESCo는 자동 응답의 첫 문장(“Red Hat Bugzilla에서 이 구성 요소에 대한 버그 보고서는 적극적으로 모니터링되지 않습니다”)을 삭제하기로 [결정했다](https://pagure.io/fesco/issue/3568#comment-1015450). 이는 4월 29일 [구현되었다](https://pagure.io/fesco/issue/3568#comment-1015513).

이것이 버그 보고서가 이전보다 더 적극적으로 모니터링된다는 뜻은 아니라는 점에 유의해야 한다. 메시지는 바뀌었지만, FESCo는 다음에 무엇을 해야 하는지에 대한 지침을 아직 내놓지 않았다. FESCo는 추가 논의(그리고 어쩌면 조치)가 필요하다고 결론내렸다. Valentini가 회의 요약에 썼듯이, “Bugzilla의 버그를 의도적으로 모니터링하지 않는 것은 패키지 유지관리자 책임에 관한 지침과 긴장 관계에 있다(충돌하지 않는다고 해도).”

FESCo 구성원 Stephen Gallagher는 Catanzaro 및 Matthias Clasen과 후속 논의를 했으며, 그들이 다음 FESCo 회의에 참석할 예정이라고 [말했다](https://pagure.io/fesco/issue/3568#comment-1015514). 그는 Workstation 워킹 그룹이 사용자가 버그 보고서를 제출하기 전에 업스트림으로 안내하는 이슈 템플릿을 채택한다면, “정책과 현실 사이의 합리적 절충안으로 받아들여질 것”이라고 생각했다.

그 회의 결과가 무엇이든, Fedora의 GNOME 패키지 유지관리자들에게 감당하기 어려울 만큼 일이 많아 보인다는 핵심 문제를 다룰 가능성은 낮아 보인다. 그 일을 할 사람이 충분하지 않다면 버그가 *어디에* 제출되는지는 별로 중요하지 않다.

[댓글(23개 게시됨)](https://lwn.net/Articles/1070006/#Comments)

### [Prolly 트리를 사용한 버전 관리 데이터베이스](https://lwn.net/Articles/1068864/)

#### 요약

- Dolt는 B-tree의 변형인 Prolly tree를 사용해 데이터베이스 전체에 Git과 비슷한 버전 관리 기능을 제공하는 Apache 2.0 라이선스 프로젝트다.
- 버전 관리 데이터베이스는 과거 커밋 복원, 과거 상태에서의 브랜치 생성, 변경 검토 후 병합 같은 작업을 SQL 데이터에 적용할 수 있게 한다.
- 일반 B-tree는 삽입·삭제 순서에 따라 내부 노드 모양이 달라질 수 있어 스냅샷 간 효율적인 diff에 불리하다.
- Prolly tree는 해시 기반 확률적 경계를 사용해 같은 항목 집합이면 삽입 순서와 무관하게 같은 트리 구조를 만들도록 설계된다.
- 이 구조는 콘텐츠 주소 지정 저장소(content-addressed storage)와 잘 맞지만, 저장 공간·간접 참조 비용과 확률 조정에 따른 성능 특성이라는 절충도 있다.
- 저자는 Prolly tree가 데이터베이스뿐 아니라 스냅샷을 많이 사용하는 파일시스템(filesystem)에도 응용될 가능성이 있다고 본다.

글쓴이

Daroc Alden

2026년 5월 1일

현대의 데이터베이스와 파일시스템(filesystem)은 정렬된 키와 값 목록을 블록 장치(block device)에 저장하도록 최적화된 트리 구조인 [B-tree](https://en.wikipedia.org/wiki/B-tree)를 광범위하게 사용한다.[^art1b-note5] [Dolt](https://github.com/dolthub/dolt#dolt-is-git-for-data)는 데이터베이스 전체에 대한 효율적인 버전 관리를 지원하기 위해 B-tree 변형을 영리하게 활용하는 Apache 2.0 라이선스 프로젝트다. Dolt가 사용하는 자료구조는 다른 프로젝트에도 상당히 흥미로울 수 있다.

Dolt의 배후 회사인 [DoltHub](https://www.dolthub.com/)는 Apache 라이선스 오픈소스 프로젝트 세 가지, 즉 Dolt, [Doltgres](https://github.com/dolthub/doltgresql#doltgres-is-dolt-for-postgres), [DoltLite](https://github.com/dolthub/doltlite/tree/master#doltlite)의 호스팅 버전을 판매해 수익을 낸다. 이 프로젝트들은 각각 MySQL, PostgreSQL, SQLite의 드롭인 대체품(drop-in replacement)이 되는 것을 목표로 한다. 서로 다른 SQL 방언(dialect)을 위한 별도 프런트엔드가 있지만, 세 프로젝트는 버전 관리 작업을 지원하는 공통 저장소 백엔드(storage backend)를 공유한다.

실제로 이는 프로젝트들이 Git과 비슷한 작업을 사용자 정의 SQL 함수로 노출할 수 있게 한다.

```

    -- 데이터베이스 수정
    INSERT INTO users VALUES (...);
    -- 테이블의 변경 사항을 스테이징에 추가
    SELECT dolt_add('users');
    -- 커밋
    SELECT dolt_commit('-m', 'Add Joe to users');
    -- 결과 diff 확인
    SELECT * from dolt_diff_users('HEAD~1', 'HEAD');
```

어느 시점이든 데이터베이스에는 Git과 마찬가지로 현재 HEAD 커밋, 스테이징 영역(staging area)의 일정 수의 변경 사항, 작업 영역(working area)의 일정 수의 변경 사항이 있다. 이런 의도적인 유사성은 이 프로젝트들의 중요한 판매 포인트다. 회사 홈페이지에는 “당신은 이미 Dolt 사용법을 알고 있습니다”라고 쓰여 있다. 이는 과장일 수 있지만, Git과 SQL에 대한 기본 지식만 있으면 Dolt를 사용하기 시작하기에 충분해 보인다는 점은 사실이다.

버전 관리되는 데이터베이스를 어디에 쓰는지는 덜 명확할 수 있다. 커밋을 만드는 것만으로는 기존의 데이터베이스 트랜잭션(transaction) 개념보다 훨씬 더 강력해지는 것은 아니다. Dolt의 진짜 효용은 오래된 커밋을 복원하고, 데이터베이스의 과거 상태를 포크(fork)하며, 검토 후 변경 사항을 병합할 수 있는 능력에서 나온다.[^art1b-note6] 예를 들어 프로그래머는 특정 날짜 기준으로 어떤 결과가 보고되었을지를 확인하기 위해 데이터베이스의 오래된 상태를 대상으로 분석을 실행하고 싶을 수 있다. 그들은 과거 커밋을 가리키는 새 브랜치를 만들고, 그 분석에 필요한 스키마 변경을 체리픽(cherry-pick)한 뒤 실행할 수 있다.

또 다른 잠재적 용도는 자동화 도구에 작업할 수 있는 “진짜” 데이터베이스를 제공하되, 프로덕션 데이터베이스를 완전히 망가뜨릴 능력은 주지 않는 것이다. 모든 변경 사항은 별도로 조사할 수 있고, 아무것도 망가뜨리지 않는다는 점이 분명해진 뒤에만 병합할 수 있다. Dolt는 일반 MySQL 클라이언트와 완전히 호환된다. 차이는 연결 문자열(connection string)에만 있으므로, 도구들은 자신이 실제 프로덕션 데이터베이스와 대화하고 있지 않다고 생각할 이유가 없다.

```

    -- 일반 db에 연결
    mysql://db-server:3306/mydb
    -- 이름 있는 브랜치에 연결
    mysql://db-server:3306/mydb/branch-name
    -- 읽기 전용 과거 커밋에 연결
    mysql://db-server:3306/mydb/ia1ibijq8hq1llr7u85uivsi5lh3310p
```

세 프로젝트 중 Dolt가 가장 성숙하다. Doltgres는 최근 [베타에 들어갔고](https://www.dolthub.com/blog/2025-04-16-doltgres-goes-beta/), DoltLite는 그 중간쯤에 있다. SQLite에서 가져와 적응시킨 구성 요소들은 원래 맥락에서 충분히 테스트되었지만, 프로젝트 자체는 아직 0.8.1 버전이다. Dolt에 대한 회사의 성능 테스트는 그 속도가 MySQL과 비슷하다고 [시사하지만](https://docs.dolthub.com/sql-reference/benchmarks/latency), 정밀한 벤치마킹이 어렵다는 일반적인 단서가 적용된다.

이런 경쟁력 있는 성능은 Dolt가 데이터베이스의 저장 계층(storage layer)만 바꾸기 때문에 가능하다. 쿼리 플래너(query planner), 인덱스 유지관리 등은 모두 MySQL, PostgreSQL, SQLite의 기존 구현을 재사용한다. 이 데이터베이스들은 모두 B-tree를 사용한다. Dolt는 효율적인 diff를 가능하게 하고 거의 동일한 버전들 사이에서 저장 공간을 공유할 수 있게 하는 B-tree의 약간 변형된 형태를 사용한다.

#### B-tree

B-tree는 더 단순한 사촌인 이진 트리(binary tree)와 공통점이 많다. 이진 트리에서 각 노드는 키, 값, 그리고 두 개의(비어 있을 수도 있는) 하위 트리(sub-tree)를 가진다. 더 낮은 값을 가진 키는 왼쪽 하위 트리에, 더 높은 값을 가진 키는 오른쪽 하위 트리에 저장된다. 트리를 균형 있게 유지하기 위한 어떤 방식(예컨대 [커널의 레드-블랙 트리 사용](https://lwn.net/Articles/500355/))이 쓰이는 한, 이는 비교 기반 검색을 상당히 효율적으로 만든다. 각 비교가 남은 후보의 대략 절반을 제거하기 때문이다. 키 조회 시간은 트리에 있는 노드 수의 밑이 2인 로그에 비례한다.

B-tree는 이 핵심 개념을 가져와 다수의 포인터 간접 참조(pointer indirection)를 없앤다. B-tree의 각 노드는 키, 값, 하위 트리를 가리키는 포인터의 배열을 가진다. 보통 배열 크기는 하나의 노드가 기반 저장소의 한 섹터(sector)나 페이지(page)에 맞도록 선택된다. B-tree에서 항목을 찾으려면 컴퓨터는 배열을 훑어 키를 직접 찾거나, 목표 키가 그 사이에 있어야 하는 두 키를 찾은 뒤 해당 하위 트리를 확인하러 내려간다. 이 구조는 트리의 레벨 수와 포인터 간접 참조 수를 크게 줄여, 실제 접근에서 전체 구조를 더 빠르게 만든다. 예를 들어 노드당 16개의 키가 있는 B-tree에서는 키 검색에 관여하는 노드 수가 이진 트리와 비교해 4분의 1에 불과하다.

> ![[작은 B-tree 다이어그램. 'CyHawk'가 만들고 CC-BY-SA 라이선스로 공유함]](https://static.lwn.net/images/2026/B-tree.png)

이 점 때문에 B-tree는 특정 항목에 대한 효율적 검색, 범위 안 항목에 대한 순서 유지 스캔(in-order scan), 기반 저장소 접근 사이에서 균형을 잡아야 하는 데이터베이스에 매우 잘 맞는다. 여러 데이터베이스는 약간의 속도 향상을 제공하는 다양한 B-tree 변형을 사용한다. 예를 들어 모든 값을 리프 노드(leaf node)로 옮기고 트리의 내부 노드(interior node)에는 키만 저장하면 내부 노드당 더 많은 키를 담을 수 있어 트리가 더 넓고 낮아진다. 이 아이디어의 확장은 각 리프 노드에 “next” 포인터를 추가해, 순서 유지 순회가 내부 노드를 로드할 필요 없이 리프를 따라 진행될 수 있게 한다. 아래에서 설명하는 Dolt의 핵심 자료구조는 이 두 최적화를 모두 포함한다.

평범한 B-tree의 문제, 그리고 Dolt가 흥미로운 이유는 전체 B-tree를 *비교*하는 비용이 크다는 점이다. 항목이 삽입되고 삭제되는 순서는 B-tree의 내부 노드 구조에 영향을 줄 수 있다. 이는 두 B-tree를 비교하는 유일한 방법이 두 트리 전체를 모두 순회하는 것임을 뜻한다. 이 단점은 전통적인 데이터베이스에는 그다지 중요하지 않지만, 버전 관리 시스템에는 실질적인 문제를 일으킨다.

Git 같은 스냅샷 기반 버전 관리 시스템은 어떤 소스 트리의 여러 스냅샷을 저장한다고 생각할 수 있다. 각 커밋은 논리적으로 독립적이며, 이론상 그대로 저장될 수도 있다. 실제로 대부분의 Git 저장소는 커밋 사이에 완전히 바뀌지 않으므로, 스냅샷 자체가 아니라 연속된 스냅샷 사이의 차이를 저장하는 편이 더 효율적이다.

전체 디렉터리 트리를 다루는 Git은 실제 변경 사항만 포함하는 압축된 diff를 만들기 위해, 특정 하위 트리가 바뀌었는지 빠르게 확인할 수 있어야 한다. B-tree는 같은 논리적 키·값 목록이 서로 다른 두 B-tree로 표현될 수 있기 때문에 이런 종류의 알고리즘과 잘 맞지 않는다. diff 알고리즘을 순진하게 B-tree에 적용하면 내부 노드 표현 사이에 비효율적인 변경 소음(churn)이 많이 생길 수 있다.

문제는 항목이 추가되고 제거될 때 B-tree가 노드를 분할하고 병합하는 방식에서 나온다. B-tree 노드가 가득 차면 각각 절반쯤 찬 두 개의 더 작은 노드로 분할된다. B-tree 노드가 충분히 차 있지 않으면(구현마다 다르지만 보통 절반보다 약간 낮은 임계값), 그 자식들이 병합되어 더 꽉 찬 노드를 만든다. 올바르게 구현되면 이는 B-tree의 균형을 유지하고 노드가 저장 공간을 낭비하는 일을 막는다. 하지만 이는 분할과 병합 결정이 트리에 삽입된 순서에 의존한다는 뜻이기도 하다.

#### Prolly tree

[확률적 B-tree](https://docs.dolthub.com/architecture/storage-engine/prolly-tree)(Probabilistic B-tree, 줄여서 Prolly tree)는 이 문제에 대한 Dolt의 답이다.[^art1b-note7] Prolly tree는 B-tree와 거의 동일하지만, 항목을 삽입하고 제거하는 로직이 바뀌어 같은 항목을 담은 두 트리는 항목이 어떤 순서로 삽입되었든 완전히 동일해진다. 같은 성질은 개별 하위 트리에도 적용되므로, 두 Prolly tree를 비교하는 일은 훨씬 단순해진다. 두 버전 사이에서 하위 트리가 바뀌지 않았다면, 어떤 항목이 삽입되었다가 제거되었더라도 같은 해시(hash)를 가질 것이다.

이를 달성하려면 Prolly tree는 트리의 내부 상태가 아니라 오직 내용에 기반해 각 노드가 어느 크기여야 하는지를 결정할 수 있어야 한다. 처음에는 저장 공간 사용을 극대화하기 위해 모든 노드가 가능한 한 꽉 차야 한다고 말하고 싶을 수 있다. 하지만 그러려면 때때로 트리의 같은 레벨에 있는 노드들을 부모들 사이에서 앞뒤로 옮겨야 하고, 이는 B-tree의 좋은 성질 일부를 깨뜨리며 버전 사이의 추가 변경 소음을 유발할 것이다. 삽입과 삭제를 효율적으로 유지하려면 평균적인 노드는 단일 항목의 삽입이나 삭제가 분할 또는 병합을 촉발해야 할 만큼 너무 꽉 차 있거나 너무 비어 있어서는 안 된다.

이 문제의 해법은 해시 함수를 사용해, 특정 노드가 우연히 얼마나 차 있는지가 아니라 데이터에만 의존하는 방식으로 결정을 내리는 것이다. 해시는 사실상 임계값과 비교해 무작위화된 결정을 내릴 수 있는 결정적 의사난수(deterministic pseudorandom number)이며, 여기서 Prolly tree의 “확률적(probabilistic)” 부분이 나온다. 노드에 새 값을 삽입하려면, 구현은 그 값을 (키를 기준으로) 배열의 올바른 위치에 넣은 뒤, 항목들의 해시에 기반해 이 노드와 형제 노드(sibling) 사이의 경계가 어디에 있어야 하는지 다시 계산한다. 각 해시는 선택된 컷오프 값(임계값)과 비교되어, 노드가 그 항목에서 끝나야 하는지 결정한다. 해시 값들이 서로 독립적이므로 노드 사이 경계를 어디에 둘지에 관한 결정도 독립적이다. 따라서 대부분의 경우 항목을 추가해도 새 경계는 생기지 않는다. 그 항목의 해시 값이 임계값보다 높을 것이고, 노드는 여전히 같은 위치(해시 값이 낮은 기존 항목)에서 끝날 것이다. 가끔 삽입된 항목의 해시 값이 낮으면 노드가 둘로 분할되어 전체 노드 크기가 균형을 유지한다.

이 그림은 성능 고려 때문에 약간 더 복잡해진다. 노드 크기를 최적으로 유지하기 위해 실제로 사용되는 임계값은 동적이며, 노드 안에서 주어진 키 앞에 있는 항목 수를 바탕으로 한다. 그래도 노드 사이 경계를 어디에 놓을지에 대한 실제 결정이 트리의 기존 구조와 독립적으로 이루어진다는 점은 변하지 않는다. 경계의 위치는 트리에 저장된 항목들의 해시에만 의존하며, 그 해시는 항목이 어떤 순서로 삽입되었든 같다.

이 삽입 로직은, 특히 구현이 성능에 맞게 최적화되어 있다면 다소 복잡하지만, 그래도 꽤 간결하다.

```

    # 최적화되지 않은 Python 예제 코드
    # 이 함수는 어떤 내부 노드가 자신의 자식 노드 중 하나를 갱신하기 위해 호출한다.
    # 반환값은 내부 노드를 갱신하는 데 사용된다.
    def insert_into_node(node, new_items):
        sibling = node.next_sibling
        new_items = sorted(new_items + node.items)
        collected = []
        nodes = []
        
        while new_items:
            next = new_items.pop(0)
            collected.append(next)
            if hash(next.key) < threshold(len(collected)) \
               or len(collected) >= max_node_length:
                nodes.append(Node(items=collected))
                collected = []

        if collected:
            # while 루프가 자연스러운 경계에서 끝나지 않았다
            if node.next_sibling is not None:
                new_nodes, sibling = insert_into_node(node.next_sibling, collected)
                nodes += new_nodes
            else:
                nodes.append(Node(items=collected))
            
        for i in range(1, len(nodes)):
            nodes[i - 1].next_sibling = nodes[i]
        nodes[-1].next_sibling = sibling
        
        return nodes, nodes[0]
```

적절히 선택된 임계값을 사용하면 평균적인 삽입은 새 노드를 만들지 않으므로, 트리의 각 레벨에서 하나의 노드만 갱신하면 된다. 이론적으로는 단일 항목을 추가하는 일이 그 뒤에 있는 모든 노드가 서로 다르게 분할되도록 만들 수 있지만, 그런 가능성은 극히 작다. 항목들의 해시 값이 통계적으로 독립적이기 때문이다. 그런 종류의 재정렬이 일어나려면 기존 항목들의 해시 값이 모두 임계값을 간신히 빗나가야 하므로, 실제 성능 문제는 아니다. 항목을 노드에 배치하는 결정은 데이터에만 의존하므로, 같은 노드들이 매번 만들어진다.

B-tree 대신 Prolly tree를 사용할 때의 단점도 있다. 예를 들어 노드는 하위 트리의 해시를 저장해야 하며, 이는 해시를 주소로 바꾸기 위해 더 많은 저장 공간이나 콘텐츠 주소 지정 블록 저장소(content-addressed block store)를 통한 추가 간접 참조가 필요하다는 뜻이다. 콘텐츠 주소 지정 저장소(content-addressed storage)는 많은 버전 관리 시스템이 데이터 중복 제거(deduplication)에 사용하는 방식이다. 특정 diff나 다른 객체는 그 내용의 해시에 기반한 위치에 저장된다. 이렇게 하면 중복 항목이 같은 저장 공간을 재사용하게 된다. 버전 관리 시스템의 일부로 구현된 Prolly tree는 블록을 위해 기존 콘텐츠 주소 지정 객체 저장소를 재사용하고, 블록을 해시로 참조해 더 작은 내부 노드를 만들 수 있다. 다른 시스템은 자체 해법이 필요하다.[^art1b-note8]

또 다른 문제는 트리 성능이 분할 확률을 어떻게 조정하느냐에 매우 민감하다는 것이다. 일정한 확률을 사용하면 평균 노드는 절반쯤 차지만, 중앙값 노드는 항목을 하나 또는 두 개만 담게 된다. 이에 대처하기 위해 Prolly tree는 노드가 채워질수록 증가하는 동적 임계값을 사용해, 노드 크기가 정규분포를 따르도록 만든다. 물론 어떤 애플리케이션은 평균적인 성능보다 최악의 경우(worst-case) 성능을 실제로 요구하며, 이는 Prolly tree의 무작위화된 레이아웃과 양립하지 않는다.

이런 결점에도 불구하고, Prolly tree는 트리 스냅샷을 비교할 수 있어야 하거나 트리를 콘텐츠 주소 지정 방식으로 저장할 수 있어야 하는 애플리케이션에 유용한 자료구조가 될 수 있다.

#### 역사와 미래

Prolly tree는 이제는 사라진 [Noms 데이터베이스](https://github.com/attic-labs/noms#warning---this-project-is-not-active)를 위해 Aaron Boodman이 발명했다. 이후 [InterPlanetary Linked Data](https://github.com/ipld/ipld#ipld)(IPLD) 프로젝트와 DoltHub가 이를 채택했다. Dolt에서 사용되는 저장소 백엔드는 Noms의 포크(fork) 버전이지만, 그 이후 프로젝트에는 상당한 수의 변경과 최적화가 이루어졌다. Prolly tree의 다른 구현들도 라이브러리 형태로 존재하지만, 이를 데이터베이스에 적용하는 것은 없다.

Dolt는 전통적인 데이터베이스 설계의 매력적인 진화를 보여 준다. 하지만 개인적으로는 이 아이디어가 파일시스템처럼 B-tree를 사용하는 다른 프로그램에 어떻게 적용될 수 있을지 보는 것이 기대된다. Prolly tree가 B-tree의 모든 용도에 적합한 것은 분명 아니지만, 파일시스템은 데이터베이스와 마찬가지로 순서 유지 순회, 임의 접근(random access), 스냅샷 생성의 용이성 사이에서 많은 동일한 절충을 공유한다.[^art1b-note9] 어쩌면 Prolly tree는 크고 자주 수정되는 파일의 공간 효율적인 스냅샷에 도움이 될 수 있다.

[댓글(20개 게시됨)](https://lwn.net/Articles/1068864/#Comments)

[^art1b-note1]: FESCo(Fedora Engineering Steering Committee)는 Fedora 배포판의 기술 정책과 패키징 방향을 결정하는 선출 기구다. “정책상 책임”이라는 말은 단순한 권고가 아니라 Fedora 패키지 유지관리자가 따르도록 기대되는 운영 기준을 뜻한다.

[^art1b-note2]: Bugzilla는 오래된 웹 기반 버그 추적 시스템으로, Red Hat과 Fedora가 오랫동안 패키지 버그 관리에 사용해 왔다. 하지만 대규모 프로젝트에서는 담당자 자동 배정, 중복 보고, 오래된 미처리 티켓이 누적되기 쉬워 실제 유지관리 업무량을 과소평가하게 만들 수 있다.

[^art1b-note3]: ABRT(Automatic Bug-Reporting Tool)는 Fedora에서 프로그램 충돌을 감지해 진단 정보를 모으고 버그 보고를 돕는 도구였다. 이 도구가 사라지면 사용자가 충돌 보고서를 어디로 어떻게 보낼지 안내하는 별도의 흐름이 더 중요해진다.

[^art1b-note4]: Forgejo는 Gitea에서 갈라져 나온 오픈소스 코드 호스팅·협업 플랫폼이다. Fedora가 Bugzilla에서 Forgejo/Fedora Forge로 이슈 추적을 옮기면, 패키지별 템플릿·권한·자동화로 “Fedora에 보고할 문제인지 업스트림에 보고할 문제인지”를 더 일찍 분기할 수 있다.

[^art1b-note5]: B-tree는 디스크나 SSD처럼 큰 블록 단위로 읽고 쓰는 저장 장치에서 특히 유리하다. 노드 하나에 여러 키를 넣어 트리 높이를 낮추면, 검색 한 번에 필요한 I/O 횟수가 줄어 데이터베이스 인덱스와 파일시스템 메타데이터에 널리 쓰인다.

[^art1b-note6]: 데이터베이스 트랜잭션은 보통 짧은 시간의 원자적 변경을 보장하지만, Dolt식 버전 관리는 “며칠 전 상태에서 브랜치를 따고, 변경을 검토해 병합한다”는 협업 워크플로를 데이터 자체에 적용한다는 점이 다르다.

[^art1b-note7]: Prolly tree의 핵심 실용 효과는 같은 내용이면 같은 구조와 같은 해시가 나오도록 만들어, 대규모 데이터셋의 두 버전 사이에서 바뀌지 않은 부분을 빠르게 건너뛸 수 있게 한다는 점이다. 이는 Git이 디렉터리 트리에서 해시를 활용해 변경되지 않은 하위 트리를 재사용하는 방식과 닮았다.

[^art1b-note8]: 콘텐츠 주소 지정 저장소에서는 “어디에 저장했는가”보다 “내용의 해시가 무엇인가”가 식별자가 된다. 덕분에 같은 블록은 한 번만 저장해도 되지만, 해시 계산 비용과 해시에서 실제 저장 위치를 찾는 인덱스 관리 비용이 추가된다.

[^art1b-note9]: 파일시스템 스냅샷은 특정 시점의 파일과 메타데이터 상태를 보존한다. Prolly tree 같은 구조가 적용된다면 자주 바뀌는 큰 파일이나 디렉터리 트리에서 변경되지 않은 블록을 더 잘 공유할 가능성이 있지만, 최악의 경우 지연시간과 복구 도구의 복잡성 같은 운영상 고려가 뒤따른다.

---

### [s390을 위한 하드웨어 지원 Arm VM](https://lwn.net/Articles/1069954/)

#### 요약

- Steffen Eiden 등의 패치 세트는 s390 CPU에서 Arm CPU를 하드웨어 지원 방식으로 에뮬레이션하기 위한 토대를 마련한다.
- 핵심은 s390의 새 명령어인 “Start Arm Execution”(SAE) 지원으로, Arm 명령어 블록을 가상 CPU 컨텍스트로 실행하게 한다.
- Arm VM이 수정 없이 s390 호스트에서 동작하려면 s390 KVM이 Arm 하이퍼콜과 게스트 API를 해석·추적해야 한다.
- Arm 유지관리자들은 방향에는 찬성했지만, Arm 전용 코드를 공유 위치로 옮길 때의 유지보수성과 교차 검토 체계를 논의했다.
- 양측은 문서화, 테스트, CI, MAINTAINERS 교차 리뷰어 추가를 통해 아키텍처 간 협업 부담을 줄이려 하고 있다.

작성자

Daroc Alden

2026년 5월 5일

Steffen Eiden 등은 최근 [패치 세트](https://lwn.net/ml/all/20260402042125.3948963-1-seiden@linux.ibm.com/)를 통해 s390 CPU에서 Arm CPU를 하드웨어 지원 방식으로 에뮬레이션할 수 있게 하는 기반을 마련했다.[^art1c-note1] 게시물의 [두 번째 버전](https://lwn.net/ml/all/20260428155622.1361364-1-seiden@linux.ibm.com/)은 몇 가지 작은 문제를 고쳤지만, 전체 내용은 크게 다르지 않다. 이 패치들은 Arm 유지관리자들에게 환영받았지만, Arm 쪽에서 유지보수 문제가 생기지 않도록 아키텍처 간 협업 구조를 어떻게 잡을지에 대한 논의가 남아 있다. 그런 세부 사항이 해결되면, 이 패치들은 Arm 기반 가상 머신(VM)을 s390 호스트에서 네이티브 또는 거의 네이티브에 가까운 속도로 투명하게 실행하는 길을 열 수 있다.

이 기능의 핵심은 “Start Arm Execution”(SAE)이라는 새 s390 명령어 지원을 추가하는 [패치](https://lwn.net/ml/all/20260402042125.3948963-20-seiden@linux.ibm.com/)다. 이 명령은 s390에서 이미 하드웨어 지원 VM에 진입할 때 쓰이는 “[Start Interpretive Execution](https://www.qemu.org/docs/master/system/s390x/vfio-ap.html#start-interpretive-execution-sie-instruction)” 명령과 비슷한 역할을 하며, 가상 CPU 상태를 호스트 CPU와 분리해 유지한다.[^art1c-note2] 두 명령 모두 가상 CPU를 어떻게 설정하고 진입할지를 설명하는 “control block”에 대한 포인터를 받는다. 차이는 SAE 명령의 control block이 명령어 포인터를 Arm 명령어가 들어 있는 메모리 블록으로 설정하고, 이를 s390 명령어가 아니라 Arm 명령어로 해석한다는 점이다.

이론적으로는 이 기능을 지원할 만큼 새로운 s390 CPU를 가진 사람이 Arm VM을 직접 실행할 수 있게 된다. 어느 시점에서는 분명 Arm 머신 코드를 s390 머신 코드로 변환해야 하지만, CPU가 그 일을 내부적으로 처리한다. 정확히 어떻게 처리하는지는 이 패치 세트만으로는 명확하지 않다.

커널 쪽에서는 아이디어 자체는 단순하지만 구현은 조금 더 복잡하다. 가상 머신이 하이퍼바이저를 호출할 때는 아키텍처별 인터페이스를 사용한다.[^art1c-note3] Arm VM을 수정하지 않은 채 s390에서 실행하려면, s390 커널의 KVM 코드가 Arm 하이퍼콜을 해석할 수 있어야 한다. 이를 지원하기 위해 Eiden의 패치 세트는 인터페이스 정의와 관련 헤더 파일을 `include/uapi/arch/arm64/`로 옮겨 다른 아키텍처가 이를 참조할 수 있게 한다. 흥미롭게도 이 과정에서 중복 코드도 정리할 수 있었고, 결과적으로 패치들은 추가한 줄보다 더 많은 코드 줄을 제거했다.

하지만 이 패치들이 병합된 뒤에도 할 일은 더 남아 있다. s390 아키텍처에는 Arm 레지스터 조작, 인터럽트 처리 등을 위한 명령어도 추가되고 있다. Eiden은 앞으로 몇 달 동안 나머지 s390 개발자들과 함께 그런 명령어들에 대한 지원을 추가하고자 한다.

이 패치 세트에 대한 피드백은 비교적 적었지만, Marc Zyngier는 Will Deacon과 상의해 작성한 [긴 답변](https://lwn.net/ml/all/86o6jd2925.wl-maz@kernel.org/)을 보냈다. 그들은 이 작업을 지지했지만, Arm 전용 코드 일부를 공유 디렉터리로 옮기는 방식이 깔끔하지 않고 코드 유지보수성을 해칠 수 있다고 우려했다. 이들은 심볼릭 링크, 상대 경로, 코드 생성을 사용하면 기존 Arm 코드가 익숙한 위치에 그대로 남아 있으면서도 s390 코드가 과도하게 제한되지 않을 수 있다고 제안했다.

Eiden의 [답변](https://lwn.net/ml/all/20260423122549.361343-A-seiden@linux.ibm.com/)은 원래 헤더 파일에 심볼릭 링크를 사용하는 방식을 시도했지만, 다소 지저분해 보여 지지를 얻지 못할까 봐 우려했다고 설명했다. 일부 코드는 Arm 코드의 Makefile 규칙을 재사용해 자동으로 생성되기도 한다. 그러나 그는 심볼릭 링크를 사용하는 대안을 프로토타입으로 만들어 비교용으로 게시하는 데 동의했다. 그 패치 세트는 [4월 28일에 발송](https://lwn.net/ml/all/20260428160527.1378085-1-seiden@linux.ibm.com/)되었으며, 이 글을 쓰는 시점까지는 아직 리뷰를 받지 못했다.

더 심각한 우려는 아직 진화 중인 Arm 가상 머신 게스트 API의 변화에 s390이 어떻게 따라갈 것인가였다. Zyngier의 설명에 따르면, 예를 들어 일부 CPU 취약점 완화책은 게스트의 협력이 필요하다.[^art1c-note4] 새 취약점이 발견되면 Arm은 필요한 새 인터페이스에 하이퍼콜 함수 번호를 할당하고, KVM은 이를 구현한다. s390 코드도 새로운 Arm 전용 완화책에 대한 스텁을 추가하고, 필요한 s390 전용 인터페이스를 추가하기 위해 Arm 쪽과 협력하는 등 비슷한 작업이 필요할 것으로 보인다. 다만 이런 추가는 완화책에 한정되어야 한다. Arm KVM 코드는 “구현별 명령어나 시스템 레지스터의 사용을 일절 금지하는 것을 원칙으로 삼고” 있으며, Zyngier는 s390 코드도 같은 방침을 따를 것으로 기대하기 때문이다.

Eiden은 이 문제를 크게 걱정하지 않았다. 그는 이 프로젝트의 주된 목표가 수정되지 않은 Arm 게스트를 실행할 수 있게 하는 것이므로, 자신과 동료 s390 개발자들은 Arm 코드를 진실의 원천(source of truth)으로 취급할 것이라고 말했다. 따라서 그들은 s390 전용 기능을 도입하거나 통상적인 절차를 무시할 계획이 없었다.

Zyngier와 다른 Arm 유지관리자들은 당연히 s390의 세부 사항에 익숙하지 않다. 그래서 Zyngier와 Deacon은 Arm 코드 변경이 s390에 나쁜 영향을 주지 않도록 문서화, 테스트, 디버깅에 대한 도움도 요청했다.

> 마지막으로, 두 프로젝트 모두에게 도움이 되도록 포로 교환을 해서 MAINTAINERS에 교차 리뷰어를 두는 것이 좋겠다고 생각합니다. 즉 KVM/arm64에는 s390 리뷰어를 추가하고, KVM/s390에는 arm64 리뷰어를 추가하는 방식입니다.

Eiden은 흔쾌히 동의했고, 테스트의 출발점으로 s390용 커널 교차 컴파일이 좋겠다고 제안했다. 또한 네이티브 빌드를 수행할 수 있도록 IBM이 호스팅하는 s390 VM에 대한 접근도 제공하겠다고 했다. Eiden은 파손을 조기에 잡아내기 위해 Arm의 지속적 통합 테스트 브랜치를 s390 빌드 인프라에 추가할 계획이다.[^art1c-note5] 그는 유지관리자를 서로 교환하는 것도 타당하다고 보았고, 패치 시리즈의 두 번째 리비전에서 자신을 Arm KVM 리뷰어로 [추가했다](https://lwn.net/ml/all/20260428155622.1361364-15-seiden@linux.ibm.com/).

Eiden과 Zyngier는 Linux Plumbers Conference의 Linux Storage, Filesystem, Memory Management, and BPF Summit에서 다른 s390 및 Arm 커널 개발자들과 만나기로 했다. 남은 세부 사항을 정리하는 데 대면 회의가 충분하기를 바라며, 모두가 이 변화에 꽤 만족해 보이므로 그럴 가능성은 높다.

[ 이 주제를 알려 준 Andi Holmes에게 감사드립니다. ]

[댓글(31개 게시됨)](https://lwn.net/Articles/1069954/#Comments)

**페이지 편집자**: Joe Brockmeier

[^art1c-note1]: s390은 IBM Z 계열 메인프레임의 64비트 아키텍처를 가리키며, 대규모 I/O, 신뢰성, 가상화 기능을 강점으로 삼는다. 여기서의 의의는 “Arm 바이너리를 QEMU 같은 순수 소프트웨어 에뮬레이션으로 느리게 돌리는 것”이 아니라, CPU가 직접 보조하는 형태로 Arm 게스트 실행을 가속할 수 있다는 점이다.

[^art1c-note2]: s390의 SIE(Start Interpretive Execution)는 KVM/s390 가상화의 핵심 하드웨어 메커니즘이다. 게스트 CPU 상태를 기술하는 control block을 하드웨어에 넘겨 실행하게 함으로써, 커널이 모든 게스트 명령어를 소프트웨어로 해석하지 않아도 된다.

[^art1c-note3]: 하이퍼콜(hypercall)은 게스트 OS가 하이퍼바이저에 서비스를 요청하는 호출로, 일반 애플리케이션이 커널에 시스템 콜을 하는 것과 비슷한 위치에 있다. Arm 게스트를 “수정 없이” 실행하려면 이 호출 규약과 번호 체계까지 Arm 쪽 기대와 맞아야 한다.

[^art1c-note4]: CPU 취약점 완화책은 종종 게스트가 특정 기능을 사용하지 않거나, 하이퍼바이저가 노출하는 새 호출을 통해 상태를 동기화해야 제대로 동작한다. 따라서 Arm 게스트 API의 변경을 s390 쪽 KVM이 늦게 반영하면 보안 또는 호환성 문제가 생길 수 있다.

[^art1c-note5]: 교차 컴파일은 빌드 자체가 깨지는 문제를 빠르게 잡는 데 유용하지만, 실제 런타임 동작까지 보장하지는 않는다. 그래서 IBM 호스팅 s390 VM을 이용한 네이티브 빌드와 실행 테스트, Arm CI 브랜치 추적을 결합하는 접근이 중요하다.

---

# 간단 소식

## 보안

### [Eden: NHS goes to war against open source](https://lwn.net/Articles/1070864/)

#### 요약

- Terence Eden은 영국 [National Health Service](https://en.wikipedia.org/wiki/National_Health_Service)(NHS)가 LLM 기반 취약점 탐지 도구의 발전을 이유로 대부분의 [오픈소스 저장소](https://github.com/nhsuk/)를 닫으려 한다고 전했다.
- 그는 NHS 저장소 대부분이 데이터셋, 내부 도구, 지침, 연구 도구, 프런트엔드 디자인 등이라며 실제 보안 사고로 이어질 가능성이 낮다고 반박했다.
- 팬데믹 당시 NHSX가 코로나 접촉 추적 앱을 공개했지만, 코드·아키텍처·문서 공개가 보안 사고를 일으키지 않았다는 사례도 들었다.
- 이번 방침은 영국 정부의 기술 실행 규범 중 “개방하고 오픈소스를 사용하라”는 원칙과도 충돌한다고 지적했다.

Terence Eden은 Anthropic의 Mythos 같은 LLM 도구가 보안 취약점을 더 정교하게 찾아낼 수 있게 된 데 대한 대응으로, 영국 [National Health Service](https://en.wikipedia.org/wiki/National_Health_Service)(NHS)가 거의 모든 [오픈소스 저장소](https://github.com/nhsuk/)를 닫을 준비를 하고 있다고 [보고했다](https://shkspr.mobi/blog/2026/05/nhs-goes-to-war-against-open-source/). 완곡하게 말해도, 그는 그 결정에 동의하지 않는다.[^art2-note1]

> [NHS가 공개한 코드 저장소](https://github.com/nhsuk/)의 대다수는 보안 스캐닝의 어떤 발전에도 실질적인 영향을 받지 않는다. 대부분은 데이터셋, 내부 도구, 지침, 연구 도구, 프런트엔드 디자인 같은 것들이다. 그 안에는 현실적으로 보안 사고로 이어질 만한 것이 *아무것도* 없다.
>
> 팬데믹 기간에 내가 NHSX에서 일할 때, 우리는 오픈소스의 안전성과 필요성을 매우 확신했기 때문에 [Covid Contact Tracing 앱을 대중에게 제공되는 즉시 오픈소스로 공개하도록 했다](http://web.archive.org/web/20230122050346/https://transform.england.nhs.uk/blogs/code-behind-nhs-covid-19-app/). 그것은 국가적으로 의무화된 앱이었고, 수백만 대의 휴대전화에 설치되었으며, 적대적인 세력의 강도 높은 감시 대상이었다. 그런데도 코드, 아키텍처, 문서를 공개했음에도 오픈소스 코드는 보안 사고를 **단 한 건도** 일으키지 않았다.
>
> 게다가 이 새 지침은 코드를 공개해야 한다고 요구하는 영국의 [Tech Code of Practice 3번 항목 “Be open and use open source”](https://www.gov.uk/guidance/the-technology-code-of-practice#be-open-and-use-open-source)와 정면으로 모순된다.[^art2-note2]

[댓글(15개 게시)](https://lwn.net/Articles/1070864/#Comments)

## 커널 개발

### [Kernel release status](https://lwn.net/Articles/1071413/)

#### 요약

- 현재 개발 커널은 5월 3일에 공개된 7.1-rc2다.
- Linus는 7.0 때와 비슷하게, 아마 AI 도구의 영향으로 평소보다 패치 수가 많아지는 양상이 이어지는 것 같다고 말했다.
- 7.1 개발 주기는 -rc2 시점까지 2,066명의 개발자로부터 13,417개의 비병합(non-merge) 커밋을 받았다.
- 이 중 355명은 처음으로 커널에 기여한 개발자다.
- 4월 30일에는 여러 안정판 업데이트가 나왔고, 일부 장기 안정판에는 최근 공개된 AEAD 소켓 취약점 수정이 백포트되었다.

현재 개발 커널은 5월 3일에 릴리스된 7.1-rc2다. Linus는 이렇게 말했다. “작지는 않다. 아직 확실히 말하기에는 조금 이르지만, 7.0에서 보았던 것처럼 평소보다 더 많은 패치가 들어오는 패턴이 계속되는 것 같다고 의심한다. 아마 AI 도구 때문일 것이다.”[^art2-note3]

-rc2 기준으로 7.1 개발 주기에는 2,066명의 개발자로부터 13,417개의 비병합 커밋(non-merge commits)이 들어왔으며, 그중 355명은 처음으로 커널에 기여한 개발자다. 릴리스 이력은 다음과 같다.[^art2-note4]

> | RC | 날짜 | 커밋 |  |
> | --- | --- | --- | --- |
> | **v7.1-rc1** | 2026-04-26 | 13963 | 13963 |
> | **v7.1-rc2** | 2026-05-03 | 475 | 475 |

자세한 내용은 [KSDB 7.1 페이지](https://lwn.net/ksdb/releases/v7.1/)를 보라.

**안정판 업데이트**: [7.0.3](https://lwn.net/Articles/1070642/), [6.18.26](https://lwn.net/Articles/1070643/), [6.12.85](https://lwn.net/Articles/1070644/), [6.6.137](https://lwn.net/Articles/1070645/), [6.1.170](https://lwn.net/Articles/1070646/), [5.15.204](https://lwn.net/Articles/1070647/), [5.10.254](https://lwn.net/Articles/1070647/)가 4월 30일에 릴리스되었다. 7.0.3과 6.18.26 커널에는 Xen 사용자를 위해 필요한 수정만 들어 있다. 반면 다른 안정판에는 최근 공개된 [AEAD 소켓 취약점](https://lwn.net/Articles/1070454/)에 대한 수정이 백포트되었다.[^art2-note5]

[댓글(아직 없음)](https://lwn.net/Articles/1071413/#Comments)

### [Quotes of the week](https://lwn.net/Articles/1070747/)

#### 요약

- Greg Kroah-Hartman은 오늘날 취약점 “조율된 공개”가 실제로 가능한지에 회의적인 견해를 보였다.
- 그는 조기 공개 목록은 본질적으로 유출 경로가 될 수 있으며, 오픈소스가 전 세계를 움직인다면 통지 대상도 전 세계가 되어야 하는지 묻는다.
- Eric Biggers는 Linux 커널의 오래된 암호화 UAPI가 사용자 공간 호환성 때문에 제거되기 어렵다고 설명했다.
- AF_ALG의 MD4나 `KEYCTL_PKEY_*`의 SHA-1 같은 사례는 “사용자 공간을 깨지 않는다”는 원칙과 보안 유지 비용 사이의 긴장을 보여준다.

> 사람들이 “취약점 조율(coordination of vulnerabilities)”이라는 것이 요즘 실제로 가능하다고 생각하는 모습을 보면 재미있다. 문제의 소프트웨어를 누가 쓰는지, 누가 그런 “조기 공개 알림” 목록에 있어야 하고 없어야 하는지 생각해 보라.
>
> 내가 꽤 오래 전부터 말해왔듯이, 모든 조기 공개 목록은 유출이다. 그렇지 않다면 왜 당신의 정부가 그런 목록이 존재하도록 허용하겠는가?
>
> 소프트웨어, 특히 오픈소스 소프트웨어는 세상을 움직인다. 그렇다면 전 세계가 그 알림 목록에 들어가야 하는가? :)[^art2-note6]

—

Greg Kroah-Hartman

> 우리는 가끔 AF_ALG에서 알고리즘을 제거하기도 하지만, iwd가 여전히 사용하는 MD4(그렇다, 그 MD4) 같은 것은 제거하지 못했다.
>
> https://lore.kernel.org/linux-crypto/946591db-36aa-23db-a5c4-808546eab762@gmail.com/
>
> 마찬가지로 `KEYCTL_PKEY_*`에서 SHA-1 지원을 제거하는 문제도 그렇다.
>
> https://lore.kernel.org/linux-crypto/f0492c92-1015-48e3-bfce-598c7a4843d1@quicinc.com/
>
> 사람들은 Linus의 “우리는 단순히 사용자 공간을 깨지 않는다(we simply do not break user space)”라는 인용문까지 올린다.
>
> 안타깝게도, 이 작은 사용자 공간 프로그램 집합의 개발자와 사용자들은 Linux 커뮤니티의 나머지 사람들이 이 UAPI들을 유지하고 끊임없이 이어지는 취약점 흐름에 대응하기 위해 들이는 엄청난 시간과 노력으로부터 단절되어 있다.
>
> 그들에게 이것들은 그저 사용 가능하고 작동하는 API일 뿐이다.[^art2-note7]

—

Eric Biggers

[댓글(아직 없음)](https://lwn.net/Articles/1070747/#Comments)

## 배포판

### [Alpine Linux systems currently offline](https://lwn.net/Articles/1071176/)

#### 요약

- fosstodon.org의 Alpine Linux 계정은 Linode에서 호스팅되는 모든 시스템이 청구 문제로 일시 중단되었다고 알렸다.
- 영향 대상에는 Alpine의 GitLab 인스턴스도 포함되었다.
- Alpine 측은 문제 해결을 진행 중이라고 밝혔고, 그 동안 서비스들이 모두 중단된 것으로 보였다.
- 이후 업데이트에서 Alpine Linux 서버가 다시 온라인 상태가 되었다고 공지했다.

fosstodon.org의 Alpine Linux 계정은 GitLab 인스턴스를 포함해 Linode에서 호스팅되는 모든 시스템이 “어떤 청구 문제 때문에 현재 일시 중단되어 있다”고 [보고했다](https://fosstodon.org/@alpinelinux/116516953669188535). Alpine 측은 해결을 위해 작업 중이지만, 그 동안에는 모든 서비스가 내려간 것으로 보인다.[^art2-note8]

**업데이트**: Alpine Linux의 [서버가 다시 온라인 상태가 되었다](https://fosstodon.org/@alpinelinux/116517090251692139).

[댓글(아직 없음)](https://lwn.net/Articles/1071176/)

### [Distributions quote of the week](https://lwn.net/Articles/1071468/)

#### 요약

- Gerald Pfeifer는 openSUSE Board 의장으로 지낸 2,442일을 돌아보며 의장직에서 물러난다고 밝혔다.
- 그의 임기 동안 SUSE와 openSUSE의 분리, 팬데믹, SUSE의 상장과 비공개화, 여러 인수·조직 변화가 있었다.
- 프로젝트 로고와 이름 논의, Geeko Foundation 설립, 공개 이사회, 웹사이트 개편, 배포판과 도구의 성장도 언급했다.
- 그는 개방적이고 비폭력적인 의사소통, 신뢰, 그리고 상대의 선의를 가정하는 “자선의 원칙(PRINCIPLE OF CHARITY)”을 강조했다.

> 2,442일은 꽤 긴 시간이고, 이 글을 쓰기 시작했을 때 내가 openSUSE Board의 의장으로 있었던 시간이 바로 그만큼이었다.
>
> 그 여정은 2019년 8월 19일에 시작되었고, 내가 openSUSE Board 의장직에서 물러나는 오늘 끝난다.
>
> 그 대부분은 강렬한 시간이었다. 지난 1년 반 정도만 조금 조용했다. 기쁨과 좌절의 시간이었고, 가끔은 분노도 있었으며, 그보다 더 자주 보람이 있었다.
>
> 그 세월 동안 우리는 SUSE와 openSUSE가 Micro Focus에서 분리되는 과정(IT 측면의 에스컬레이션 포함), 전 세계적 팬데믹, SUSE의 상장과 다시 비공개 회사로 돌아가는 과정, Rancher·NeuVector·Losant의 합류, 네 명의 CIO와 네 명(그리고 사실상 그 이상)의 SUSE Linux 총괄 관리자, 우리 프로젝트의 로고와 이름에 대한 반복적인 논의, Geeko Foundation의 설립, 떠나는 사람들과 새로 나서는 사람들, 일곱 번의 이사회 선거, 이사회 회의의 공개화, 열정적인 논쟁과 성장통, 웹사이트 개편, 배포판 수와 그 주변 도구들의 성장과 진화, 그리고 그보다 훨씬 더 많은 일을 보았다.
>
> 내가 한 가지 조언을 남길 수 있다면, 그것은 개방적이고 비폭력적인 의사소통과 신뢰를 받아들이라는 것이다. 신뢰는 주는 것이기도 하고 받는 것이기도 하다.
>
> 나는 openSUSE를 이루는 여러 셀과 조직 사이에서 성과, 변화, 과제, 협업 요청을 더 수평적으로 공유할 것을 권한다. 무엇보다도 자선의 원칙(PRINCIPLE OF CHARITY)을 적용하기를 권한다. 즉, 다른 사람에게 의심의 이익을 주고, 좋은 의도를 가정하며, 그들의 관점에서 실제 가치를 찾으라는 뜻이다.
>
> 그것이 언제나 쉬운가? 전혀 그렇지 않다. 차이를 만들어 내는가? 아주 많이 그렇다.[^art2-note9]

—

Gerald Pfeifer

[댓글(아직 없음)](https://lwn.net/Articles/1071468/#Comments)

## 개발

### [GCC 16.1 released](https://lwn.net/Articles/1070649/)

#### 요약

- GNU Compiler Collection(GCC) [16.1 버전](https://lwn.net/ml/all/170o3r2r-3r4s-opp9-q8or-2no672o6q390%40fhfr.qr/)이 릴리스되었다.
- C++ 프런트엔드는 이제 기본값으로 GNU C++20 방언을 사용한다.
- 표준 라이브러리의 관련 C++20 부분은 더 이상 실험적 기능으로 취급되지 않는다.
- C++26 기능 중 Reflection, Contracts, expansion statements, `std::simd` 등에 대한 실험적 지원도 추가되었다.
- Algol68 실험적 프런트엔드와 HTML 형식 GCC 진단 출력 기능도 포함되었다.

GNU Compiler Collection(GCC) [16.1 버전](https://lwn.net/ml/all/170o3r2r-3r4s-opp9-q8or-2no672o6q390%40fhfr.qr/)이 릴리스되었다.[^art2-note10]

> C++ 프런트엔드는 이제 기본적으로 GNU C++20 방언을 사용하며, 표준 라이브러리의 해당 부분은 더 이상 실험적 기능이 아니다. Reflection(
>
> `-freflection`
>
> ), Contracts, expansion statements,
>
> `std::simd`
>
> 등을 포함해 여러 C++26 기능이 실험적으로 지원된다.

그 밖의 변경 사항으로는 [Algol68](https://en.wikipedia.org/wiki/ALGOL_68) 언어를 위한 실험적 컴파일러 프런트엔드 도입, GCC 진단(diagnostics)을 HTML 형식으로 출력하는 기능 등이 있다.[^art2-note11]

[댓글(9개 게시)](https://lwn.net/Articles/1070649/)

### [Incus 7.0 LTS released](https://lwn.net/Articles/1071469/)

#### 요약

- 컨테이너 및 가상 머신 관리 시스템 Incus의 [7.0 버전](https://discuss.linuxcontainers.org/t/incus-7-0-lts-has-been-released/26641)이 릴리스되었다.
- 이번 릴리스에는 저수준 백업 API가 포함되었다.
- 유지보수되지 않는 MinIO 프로젝트를 대체하기 위해 Incus 내부에 기본 S3 작업 기능이 추가되었다.
- cgroups v1과 xtables(`iptables`/`ip6tables`/`ebtables`) 지원은 제거되었다.
- Incus 7.0은 2031년 6월까지 지원되는 장기 지원(LTS) 릴리스다.

Incus 컨테이너 및 가상 머신 관리 시스템의 [7.0 버전](https://discuss.linuxcontainers.org/t/incus-7-0-lts-has-been-released/26641)이 릴리스되었다. 이번 릴리스의 주요 변경 사항에는 저수준 백업 API 포함, 현재 유지보수되지 않는 MinIO 프로젝트를 대체하기 위해 Incus 내부에 [기본 S3 작업 추가](https://discuss.linuxcontainers.org/t/incus-7-0-lts-has-been-released/26641#p-90660-minio-replaced-by-built-in-s3-listener-5), cgroups v1 및 xtables(`iptables`/`ip6tables`/`ebtables`) 지원 제거 등이 있다. 이는 2031년 6월까지 지원되는 장기 지원(LTS) 릴리스다.[^art2-note12]

> 첫 2년 동안은 버그 및 보안 수정과 소규모 사용성 개선이 간헐적인 포인트 릴리스(7.0.x)를 통해 제공된다. 그 초기 2년이 지난 뒤에는 Incus 7.0 LTS가 남은 5년 지원 기간 동안 보안 전용 유지보수로 전환된다.
>
> 6.0 LTS와 7.0 LTS 릴리스 사이에 총 204명이 Incus에 기여했으며, 6.23과 7.0 LTS 릴리스 사이에는 45명이 기여했다.[^art2-note13]

[댓글(아직 없음)](https://lwn.net/Articles/1071469/#Comments)

### [NetHack 5.0.0 released](https://lwn.net/Articles/1071175/)

#### 요약

- [NetHack](https://nethack.org/index.html) 던전 탐험 게임의 [5.0.0 버전](https://nethack.org/v500/release.html)이 릴리스되었다.
- NetHack은 [Rogue](https://en.wikipedia.org/wiki/Rogue_(video_game)) 및 [Hack](https://en.wikipedia.org/wiki/Hack_(video_game))의 먼 친척 격인 고전 로그라이크다.
- NetHack 코드는 이제 C99 표준을 준수한다.
- 이번 릴리스에는 3,100건이 넘는 버그 수정과 변경 사항이 포함되며, 자세한 내용은 `doc/fixes5-0-0.txt`에 정리되어 있다.
- 이전 버전의 저장 게임은 NetHack 5.0.0에서 작동하지 않는다.

[Rogue](https://en.wikipedia.org/wiki/Rogue_(video_game))와 [Hack](https://en.wikipedia.org/wiki/Hack_(video_game))의 먼 친척인 [NetHack](https://nethack.org/index.html) 던전 탐험 게임의 [5.0.0 버전](https://nethack.org/v500/release.html)이 릴리스되었다. NetHack의 코드는 이제 C99 표준을 준수하며, 이번 릴리스에는 3,100건이 넘는 버그 수정과 변경 사항이 포함되어 있다. 자세한 내용은 [`doc/fixes5-0-0.txt`](https://github.com/NetHack/NetHack/blob/NetHack-5.0/doc/fixes5-0-0.txt)에 있다(게임 스포일러가 포함될 수 있음). 이전 버전의 저장 게임은 NetHack 5.0.0에서 작동하지 않는다.[^art2-note14]

[댓글(4개 게시)](https://lwn.net/Articles/1071175/)

### [The retirement of the PHP license](https://lwn.net/Articles/1071253/)

#### 요약

- PHP 프로젝트는 Zend Engine License가 적용되는 부분을 제외하고 오랫동안 자체 PHP License로 배포되어 왔다.
- 이제 PHP License는 폐지되었고, PHP 코드는 3조항 BSD 라이선스(three-clause BSD license)로 재라이선스되었다.
- 변경을 위해서는 원래 PHP Group 구성원들의 서면 동의와 Zend Technologies의 후신인 Perforce Software의 승인도 필요했다.
- 제안은 법률 검토와 6개월의 커뮤니티 논의 기간을 거쳤고, 투표에서 만장일치로 통과되었다.
- LWN은 이 라이선스 변경 절차를 3월에 다룬 바 있다.

PHP 프로젝트는 Zend Engine License가 적용되는 부분을 제외하고 오랫동안 자체 라이선스로 배포되어 왔다. PHP 프로젝트는 이제 PHP License가 폐지되었고 PHP 코드가 3조항 BSD 라이선스(three-clause BSD license)로 재라이선스되었다고 발표했다. 자세한 내용은 해당 블로그 글을 보라.[^art2-note15]

> 여기까지 오려면 RFC를 작성하는 것 이상이 필요했다. PHP License는 PHP Group에 이를 변경할 권한을 부여했는데, 이는 원래 PHP Group 구성원 각각을 찾아내 서면 동의를 받아야 한다는 뜻이었다. 각 구성원은 제안을 승인했다. Zend Technologies의 후신인 Perforce Software도 Zend Engine 쪽에서 승인해야 했다. 그들은 변경에 대한 완전한 권한과 지지를 확인하는 공식 서한을 제공했다. 나는 논의 기간 동안 제기될 수 있는 법적 질문에 대한 조언을 받기 위해 변호사를 고용해 제안을 검토하게 했다. 그 논의 기간에 대해 말하자면, 투표에 앞서 6개월의 커뮤니티 논의 기간을 두었고, 투표는 만장일치로 통과되었다.[^art2-note16]

LWN은 지난 3월에 라이선스 변경 절차를 [다룬 바 있다](https://lwn.net/Articles/1063993/).

[댓글(4개 게시)](https://lwn.net/Articles/1071253/#Comments)

### [Development quote of the week](https://lwn.net/Articles/1070684/)

#### 요약

- 이번 개발 분야 인용문은 [OpenAI 연구](https://openai.com/index/where-the-goblins-came-from/)에서 가져온 것이다.
- 당시에는 “고블린(goblins)”의 출현 빈도가 특별히 경고할 만해 보이지 않았다고 회고한다.
- 몇 달 뒤 그 현상은 훨씬 더 구체적이고 재현 가능한 형태로 다시 나타났다고 한다.
- 짧은 인용문이지만, 머신러닝 시스템에서 초기에는 사소해 보이는 이상 현상이 나중에 반복 가능한 문제로 드러날 수 있음을 시사한다.

> 당시에는 고블린(goblins)의 만연이 특별히 경고할 만해 보이지 않았다. 몇 달 뒤, 그 고블린들은 훨씬 더 구체적이고 재현 가능한 형태로 돌아와 우리를 괴롭혔다.[^art2-note17]

— [OpenAI research](https://openai.com/index/where-the-goblins-came-from/)

[댓글(아직 없음)](https://lwn.net/Articles/1070684/)

**페이지 편집자**: Daroc Alden

[^art2-note1]: 공공기관의 저장소 공개 여부는 단순한 “코드 노출” 문제가 아니라 투명성, 외부 감사, 재현 가능한 빌드와 취약점 대응 체계까지 연결된다. LLM 기반 보안 도구가 공격자와 방어자 모두에게 더 강력한 분석 능력을 제공하는 상황에서는 저장소를 닫는 것이 실제 위험을 줄이는지, 아니면 외부 검토 기회를 줄이는지 따져야 한다.

[^art2-note2]: 오픈소스 정책은 보안상 민감한 비밀을 저장소에 넣지 않는다는 전제를 필요로 한다. 코드 공개 자체보다 비밀 관리(secret management), 의존성 패치, 위협 모델링, 책임 있는 취약점 공개 절차가 실무 보안에 더 직접적인 영향을 준다.

[^art2-note3]: Linux 커널의 `-rc` 릴리스는 최종 릴리스 전의 후보판으로, 병합 창 이후 버그 수정과 안정화가 집중된다. 패치 수 증가가 AI 도구 때문이라는 관찰은 코드 생성·수정 도구가 커널 개발 워크플로에 이미 영향을 주고 있음을 시사하지만, 리뷰 부담과 품질 관리 문제도 함께 키울 수 있다.

[^art2-note4]: 비병합 커밋 수는 실제 코드·문서·설정 변경량을 더 잘 보여주는 지표다. 첫 기여자 수가 많다는 것은 커뮤니티 유입이 활발하다는 긍정적 신호이지만, 커널처럼 회귀(regression)에 민감한 프로젝트에서는 유지관리자 리뷰와 자동 테스트 인프라의 중요성도 커진다.

[^art2-note5]: 안정판(stable) 커널의 백포트는 최신 커널에 들어간 보안·버그 수정을 장기 사용 중인 배포판 커널에도 적용하는 절차다. AEAD(Authenticated Encryption with Associated Data) 소켓 취약점처럼 암호화 API와 관련된 문제는 네트워크 서비스, 컨테이너 호스트, 가상화 환경에서 권한 상승이나 정보 노출 위험으로 이어질 수 있어 빠른 업데이트가 중요하다.

[^art2-note6]: 조기 취약점 공개 목록은 배포판, 클라우드 사업자, 대형 사용자에게 패치 준비 시간을 주기 위한 장치지만, 목록이 넓어질수록 유출 가능성도 커진다. 오픈소스가 기반 인프라로 쓰이는 규모를 고려하면 “누구에게 먼저 알려야 하는가”라는 질문 자체가 정치적·운영상 난제가 된다.

[^art2-note7]: `AF_ALG`는 Linux 커널의 암호화 알고리즘을 사용자 공간에서 소켓 인터페이스로 사용할 수 있게 하는 API이고, `KEYCTL_PKEY_*`는 키 관리 서브시스템의 공개키 연산 인터페이스다. 오래된 MD4·SHA-1 같은 알고리즘은 보안상 제거하고 싶지만, Linux의 강한 사용자 공간 ABI 호환성 원칙 때문에 실제 제거는 기존 프로그램을 깨뜨릴 수 있어 어렵다.

[^art2-note8]: 배포판 인프라가 단일 호스팅 사업자나 청구 계정에 크게 의존하면, 기술적 장애가 아니어도 패키지 빌드, 이슈 추적, 소스 저장소, 미러 운영이 한꺼번에 영향을 받을 수 있다. 실무적으로는 다중 호스팅, 오프사이트 백업, DNS·미러 장애 대응 계획이 중요하다.

[^art2-note9]: 배포판 프로젝트의 거버넌스는 기술 결정뿐 아니라 상표, 재단, 기업 후원, 커뮤니티 대표성까지 포괄한다. openSUSE처럼 기업 SUSE와 밀접하게 연결된 프로젝트에서는 신뢰와 공개적 의사소통이 기여자 유지와 장기적인 프로젝트 독립성에 직접적인 영향을 준다.

[^art2-note10]: GCC는 Linux 배포판과 임베디드 툴체인의 핵심 컴파일러다. 기본 C++ 방언이 C++20으로 올라가면 새 프로젝트에는 현대 언어 기능이 더 자연스럽게 쓰이지만, 오래된 코드베이스에서는 경고, ABI, 표준 라이브러리 동작 차이를 점검해야 한다.

[^art2-note11]: 컴파일러 진단을 HTML로 출력하면 CI 시스템과 코드 리뷰 도구에서 오류·경고를 더 읽기 쉽게 표시할 수 있다. Algol68 프런트엔드는 주류 기능은 아니지만 GCC의 프런트엔드 아키텍처가 여러 언어를 수용할 수 있음을 보여주는 사례다.

[^art2-note12]: Incus는 LXD에서 갈라져 나온 컨테이너·VM 관리 프로젝트로, 서버 가상화와 개발 환경 운영에 쓰인다. cgroups v1과 xtables 제거는 Linux 배포판들이 cgroups v2와 nftables 기반 방화벽으로 이동하는 흐름을 반영하며, 오래된 호스트나 방화벽 스크립트를 쓰는 운영자는 업그레이드 전에 호환성을 확인해야 한다.

[^art2-note13]: LTS 릴리스의 지원 단계가 “초기 2년은 버그·보안·사용성 개선, 이후는 보안 전용”으로 나뉘면 운영자는 기능 업데이트 기대치를 명확히 잡을 수 있다. 장기 운영 환경에서는 이 주기에 맞춰 테스트, 마이그레이션, 백업 정책을 세우는 것이 중요하다.

[^art2-note14]: C99 준수는 오래된 C 코드베이스가 현대 컴파일러와 정적 분석 도구에서 더 일관되게 빌드될 수 있음을 뜻한다. 저장 게임 호환성 중단은 사용자에게는 불편하지만, 내부 데이터 구조와 게임 로직을 정리하는 대규모 변경을 가능하게 하는 경우가 많다.

[^art2-note15]: 3조항 BSD 라이선스는 짧고 널리 이해되는 허용적(permissive) 라이선스다. PHP 고유 라이선스를 폐지하면 배포판, 기업 사용자, 법무 검토 담당자가 라이선스 호환성을 판단하기 쉬워지고, Zend Engine과 PHP 본체 사이의 라이선스 복잡성도 줄어든다.

[^art2-note16]: 오래된 프로젝트의 재라이선스는 코드 저작권자와 라이선스 변경 권한을 확인해야 하므로 기술 작업보다 법적·조직적 작업이 더 클 수 있다. 만장일치와 장기간 공개 논의는 나중의 라이선스 분쟁 가능성을 줄이고 downstream 배포자에게 신뢰를 준다.

[^art2-note17]: 머신러닝 연구에서 “고블린” 같은 특이한 출력 패턴은 데이터 오염, 토큰화, 평가 프롬프트, 강화학습 후처리 등 여러 원인에서 생길 수 있다. 초기에 드문 현상으로 보이더라도 재현 가능한 형태가 확인되면 모델 안전성, 평가 방법, 제품 배포 기준에 영향을 줄 수 있다.

---

# 공지

## 뉴스레터

### 커널 개발

#### 요약

- 커널 행동 강령 위원회 보고서가 포함된 주간 공지 항목입니다.[^art3-note1]
- 커뮤니티 거버넌스와 기여자 상호작용에 관한 절차적 업데이트를 추적할 수 있습니다.
- 기술 패치 자체보다는 개발 문화와 유지보수 프로세스에 초점을 둔 링크입니다.

요약(원문 설명 없음)

Kernel code of conduct committee report

4월 30일

### 배포판과 시스템 관리

#### 요약

- DistroWatch, Linux Mint, SparkyLinux, Ubuntu 등 배포판별 주간·월간 소식 링크입니다.
- 관리자는 배포판별 패키징, 릴리스, 업그레이드 공지를 한곳에서 확인할 수 있습니다.[^art3-note2]
- 각 항목은 원문 링크 제목과 발행일을 보존해 추적 가능성을 유지합니다.

요약(원문 설명 없음)

DistroWatch Weekly

5월 4일

요약(원문 설명 없음)

Linux Mint Monthly News

4월

요약(원문 설명 없음)

SparkyLinux News

5월 1일

요약(원문 설명 없음)

Ubuntu Weekly News

4월 27일

### 개발

#### 요약

- Emacs, Firefox, GCC, Git, GNOME, LLVM, Matrix, Rust 등 개발 생태계 뉴스레터 목록입니다.
- 컴파일러, 런타임, 데스크톱, 언어별 커뮤니티 동향을 빠르게 훑기 위한 색인입니다.[^art3-note3]
- 프로젝트명과 원문 뉴스레터명은 검색과 인용을 위해 영어 표기를 유지했습니다.

요약(원문 설명 없음)

Emacs News

5월 4일

요약(원문 설명 없음)

These Weeks in Firefox

4월 30일

요약(원문 설명 없음)

GCC 14.3.1 Status Report

5월 4일

요약(원문 설명 없음)

GCC 15.2.1 Status Report

5월 4일

요약(원문 설명 없음)

What's cooking in git.git

5월 3일

요약(원문 설명 없음)

Git Rev News

4월 30일

요약(원문 설명 없음)

This Week in GNOME

5월 1일

요약(원문 설명 없음)

GNU Tools Weekly News

5월 3일

요약(원문 설명 없음)

Golang Weekly

5월 1일

요약(원문 설명 없음)

Koha Community Newsletter

4월

요약(원문 설명 없음)

Last Week in Kubernetes Development

4월 30일

요약(원문 설명 없음)

LibreOffice project and community recap

5월 4일

요약(원문 설명 없음)

LLVM Weekly

5월 4일

요약(원문 설명 없음)

This Week in Matrix

5월 4일

요약(원문 설명 없음)

OCaml Weekly News

5월 5일

요약(원문 설명 없음)

This week in the Perl Steering Committee

5월 5일

요약(원문 설명 없음)

Perl Weekly

5월 4일

요약(원문 설명 없음)

This Week in Plasma

5월 2일

요약(원문 설명 없음)

PyCoder's Weekly

5월 5일

요약(원문 설명 없음)

Weekly Rakudo News

5월 4일

요약(원문 설명 없음)

Ruby Weekly News

4월 30일

요약(원문 설명 없음)

This Week in Rust

4월 29일

요약(원문 설명 없음)

Wikimedia Tech News

5월 4일

### 회의록

#### 요약

- Fedora FESCo와 openSUSE 릴리스 엔지니어링 회의록 링크입니다.
- 배포판 의사결정, 릴리스 일정, 정책 변경을 추적하는 데 유용합니다.
- 운영 환경에 영향을 줄 수 있는 패키징·릴리스 정책 변화를 조기에 확인할 수 있습니다.

요약(원문 설명 없음)

Fedora FESCo meeting minutes

5월 5일

요약(원문 설명 없음)

openSUSE Release Engineering minutes

4월 29일

### 기타

#### 요약

- 주요 범주에 들어가지 않는 자유 소프트웨어 커뮤니티 소식을 모은 항목입니다.
- Free Software Supporter 같은 일반 커뮤니티 뉴스레터가 포함됩니다.
- 커널 패치 섹션의 기타 항목에서는 Rust 매크로와 perf 도구 개선처럼 범주가 넓은 개발 항목을 다룹니다.[^art3-note15]

요약(원문 설명 없음)

Free Software Supporter

5월

## 발표 제안 요청(CFP)

### CFP 마감: 2026년 5월 7일~2026년 7월 6일

#### 요약

- 향후 오픈소스·리눅스 관련 행사들의 발표 제안(CFP) 마감일 목록입니다.
- DebConf, Open Tech Day, All Systems Go!, ELC Europe, Open Source Summit Europe 등이 포함됩니다.[^art3-note4]
- 마감일·행사 기간·행사명·장소의 표 구조와 원문 URL을 유지했습니다.

다음 CFP 마감 목록은 LWN.net CFP Calendar에서 가져온 것입니다.[^art3-note4]

| 마감일 | 행사 날짜 | 행사 | 장소 |
| --- | --- | --- | --- |
| 5월 25일 | 7월 20일 7월 25일 | [DebConf 26](https://debconf26.debconf.org/cfp/) | Santa Fe, Argentina |
| 5월 31일 | 10월 1일 | [Open Tech Day | Software-defined Storage](https://opentechday.de/propose/) | Nuremberg, Germany |
| 6월 14일 | 6월 14일 | [Neocypherpunk Summit](https://luma.com/f47k4xnd) | Berlin, Germany |
| 6월 14일 | 9월 30일 10월 1일 | [All Systems Go! 2026](https://cfp.all-systems-go.io/all-systems-go-2026/cfp) | Berlin, Germany |
| 6월 24일 | 10월 7일 10월 9일 | [Embedded Linux Conference Europe](https://events.linuxfoundation.org/embedded-linux-conference-europe/program/cfp/) | Prague, Czech Republic |
| 6월 24일 | 10월 7일 10월 9일 | [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/program/cfp/) | Prague, Czech Republic |
| 6월 30일 | 11월 17일 11월 19일 | [Open Source Monitoring Conference](https://osmc.de/call-for-papers/) | Nuremberg, Germany |

행사의 CFP 마감일이 여기에 없다면 [알려 주세요](https://lwn.net/Calendar/new/).

## 예정 행사

### 행사: 2026년 5월 7일~2026년 7월 6일

#### 요약

- LWN.net Calendar에서 가져온 예정 행사 목록입니다.
- PyCon US, RustWeek, Open Source Summit, Linux Security Summit, RISC-V Summit 등 다양한 기술 행사가 포함됩니다.
- 참석·발표·릴리스 일정 조율에 필요한 날짜와 장소 정보를 표로 보존했습니다.[^art3-note5]

다음 행사 목록은 LWN.net Calendar에서 가져온 것입니다.[^art3-note5]

| 날짜 | 행사 | 장소 |
| --- | --- | --- |
| 5월 4일 5월 11일 | [MiniDebConf Hamburg 2026](https://hamburg2026.mini.debconf.org/) | Hamburg, Germany |
| 5월 15일 5월 17일 | [PyCon US](https://us.pycon.org/2026/) | Long Beach, California, US |
| 5월 16일 5월 17일 | [Lomiri Tech Meeting](https://os-sci.nl/event/lomiri-tech-meeting-24/register) | Tilburg, The Netherlands |
| 5월 18일 5월 23일 | [RustWeek 2026](https://2026.rustweek.org/) | Utrecht, Netherlands |
| 5월 18일 5월 20일 | [Open Source Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/) | Minneapolis, Minnesota, US |
| 5월 21일 5월 22일 | [Linux Security Summit North America](https://events.linuxfoundation.org/linux-security-summit-north-america/) | Minneapolis, Minnesota, US |
| 5월 23일 5월 24일 | [Curl up](https://github.com/curl/curl-up/wiki/2026) | Prague, Czechia |
| 5월 26일 | [Media Summit](https://lwn.net/ml/all/92e24f36-d189-4ba8-ad0b-43277bc1aabd@kernel.org) | Nice, France |
| 5월 27일 5월 28일 | [Embedded Recipes](https://embedded-recipes.org/2026/) | Nice, France |
| 5월 29일 | [Yocto Project Developer Day](https://pretalx.com/yocto-embedded-recipes-2026/) | Nice, France |
| 5월 29일 | [libcamera workshop](https://lwn.net/ml/all/20260315221126.GA520505@killaraus.ideasonboard.com) | Nice, France |
| 5월 30일 5월 31일 | [Journées du Logiciel Libre 2026](https://jdll.org/) | Lyon, France |
| 6월 6일 | [Hong Kong Open Source Conference](https://hkoscon.org) | Hong Kong |
| 6월 8일 6월 12일 | [RISC-V Summit Europe 2026](https://riscv-europe.org/summit/2026/) | Bologna, Italy |
| 6월 12일 6월 14일 | [Southeast Linuxfest](https://southeastlinuxfest.org/) | Charlotte, NC, US |
| 6월 14일 | [Neocypherpunk Summit](https://s26ber.web3privacy.info/) | Berlin, Germany |
| 6월 14일 6월 16일 | [Flock to Fedora](https://fedoramagazine.org/flock-to-fedora-2026-prague/) | Prague, Czechia |
| 6월 16일 6월 17일 | [Open Source Summit India](https://events.linuxfoundation.org/open-source-summit-india/) | Mumbai, India |
| 6월 18일 6월 20일 | [Linux Audio Conference](https://lac26.mucs.club/) | Maynooth, Ireland |

행사가 여기에 없다면 [알려 주세요](https://lwn.net/Calendar/new/).

## 보안 업데이트

### [2026년 4월 30일~2026년 5월 6일 경보 요약](https://lwn.net/Articles/1071467/)

#### 요약

- AlmaLinux, Debian, Fedora, Oracle, Red Hat, SUSE, Ubuntu 등 배포판 보안 권고를 모은 표입니다.
- 커널, OpenSSH, systemd, sudo, Java, 브라우저, 컨테이너 도구 등 운영상 중요한 패키지가 다수 포함됩니다.[^art3-note6]
- 권고 ID와 LWN 링크, 배포판 릴리스, 패키지명, 공개 날짜를 원문과 같은 표 구조로 유지했습니다.
- 보안 담당자는 이 목록을 패치 우선순위와 영향 범위 확인의 출발점으로 사용할 수 있습니다.

| 배포판 | ID | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:13284](https://lwn.net/Articles/1071286/) | 8 | LibRaw | 2026-05-05 |
| AlmaLinux | [ALSA-2026:11360](https://lwn.net/Articles/1070579/) | 9 | LibRaw | 2026-04-29 |
| AlmaLinux | [ALSA-2026:8863](https://lwn.net/Articles/1070580/) | 8 | OpenEXR | 2026-04-30 |
| AlmaLinux | [ALSA-2026:11635](https://lwn.net/Articles/1070582/) | 8 | PackageKit | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11504](https://lwn.net/Articles/1070581/) | 9 | PackageKit | 2026-04-30 |
| AlmaLinux | [ALSA-2026:10135](https://lwn.net/Articles/1070565/) | 9 | buildah | 2026-04-30 |
| AlmaLinux | [ALSA-2026:13657](https://lwn.net/Articles/1071428/) | 8 | corosync | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13830](https://lwn.net/Articles/1071429/) | 8 | dovecot | 2026-05-05 |
| AlmaLinux | [ALSA-2026:12176](https://lwn.net/Articles/1070762/) | 8 | fence-agents | 2026-04-30 |
| AlmaLinux | [ALSA-2026:10767](https://lwn.net/Articles/1070566/) | 10 | firefox | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10757](https://lwn.net/Articles/1070567/) | 9 | firefox | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10707](https://lwn.net/Articles/1070569/) | 10 | gdk-pixbuf2 | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10708](https://lwn.net/Articles/1070568/) | 9 | gdk-pixbuf2 | 2026-04-30 |
| AlmaLinux | [ALSA-2026:8861](https://lwn.net/Articles/1070571/) | 8 | giflib | 2026-04-30 |
| AlmaLinux | [ALSA-2026:8859](https://lwn.net/Articles/1070570/) | 9 | giflib | 2026-04-30 |
| AlmaLinux | [ALSA-2026:10223](https://lwn.net/Articles/1070573/) | 10 | grafana | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10226](https://lwn.net/Articles/1070572/) | 9 | grafana | 2026-04-30 |
| AlmaLinux | [ALSA-2026:1838](https://lwn.net/Articles/1071430/) | 10 | image-builder | 2026-05-06 |
| AlmaLinux | [ALSA-2026:3840](https://lwn.net/Articles/1071431/) | 10 | image-builder | 2026-05-06 |
| AlmaLinux | [ALSA-2026:3839](https://lwn.net/Articles/1071432/) | 9 | image-builder | 2026-05-05 |
| AlmaLinux | [ALSA-2026:13671](https://lwn.net/Articles/1071433/) | 9 | image-builder | 2026-05-05 |
| AlmaLinux | [ALSA-2026:9683](https://lwn.net/Articles/1070575/) | 8 | java-1.8.0-openjdk | 2026-04-30 |
| AlmaLinux | [ALSA-2026:9683](https://lwn.net/Articles/1070574/) | 9 | java-1.8.0-openjdk | 2026-04-30 |
| AlmaLinux | [ALSA-2026:9689](https://lwn.net/Articles/1070577/) | 10 | java-21-openjdk | 2026-04-30 |
| AlmaLinux | [ALSA-2026:9689](https://lwn.net/Articles/1070578/) | 8 | java-21-openjdk | 2026-04-30 |
| AlmaLinux | [ALSA-2026:9689](https://lwn.net/Articles/1070576/) | 9 | java-21-openjdk | 2026-04-30 |
| AlmaLinux | [ALSA-2026:A003](https://lwn.net/Articles/1071053/) | 10 | kernel | 2026-05-01 |
| AlmaLinux | [ALSA-2026:13577](https://lwn.net/Articles/1071283/) | 8 | kernel | 2026-05-05 |
| AlmaLinux | [ALSA-2026:A001](https://lwn.net/Articles/1071051/) | 8 | kernel | 2026-05-01 |
| AlmaLinux | [ALSA-2026:A002](https://lwn.net/Articles/1071052/) | 9 | kernel | 2026-05-01 |
| AlmaLinux | [ALSA-2026:13578](https://lwn.net/Articles/1071284/) | 8 | kernel-rt | 2026-05-05 |
| AlmaLinux | [ALSA-2026:12423](https://lwn.net/Articles/1071055/) | 10 | libcap | 2026-05-01 |
| AlmaLinux | [ALSA-2026:13285](https://lwn.net/Articles/1071285/) | 8 | libcap | 2026-05-04 |
| AlmaLinux | [ALSA-2026:12441](https://lwn.net/Articles/1071054/) | 9 | libcap | 2026-05-01 |
| AlmaLinux | [ALSA-2026:12265](https://lwn.net/Articles/1071057/) | 10 | libtiff | 2026-05-01 |
| AlmaLinux | [ALSA-2026:12271](https://lwn.net/Articles/1071056/) | 9 | libtiff | 2026-05-01 |
| AlmaLinux | [ALSA-2026:13380](https://lwn.net/Articles/1071289/) | 10 | openssh | 2026-05-04 |
| AlmaLinux | [ALSA-2026:13383](https://lwn.net/Articles/1071288/) | 8 | openssh | 2026-05-04 |
| AlmaLinux | [ALSA-2026:13381](https://lwn.net/Articles/1071287/) | 9 | openssh | 2026-05-05 |
| AlmaLinux | [ALSA-2026:10713](https://lwn.net/Articles/1070584/) | 10 | pcs | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10710](https://lwn.net/Articles/1070583/) | 9 | pcs | 2026-04-29 |
| AlmaLinux | [ALSA-2026:13670](https://lwn.net/Articles/1071434/) | 9 | python-tornado | 2026-05-06 |
| AlmaLinux | [ALSA-2026:10774](https://lwn.net/Articles/1070585/) | 9 | python3.11 | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10711](https://lwn.net/Articles/1070586/) | 10 | python3.12 | 2026-04-30 |
| AlmaLinux | [ALSA-2026:10745](https://lwn.net/Articles/1070587/) | 9 | python3.12 | 2026-04-29 |
| AlmaLinux | [ALSA-2026:10949](https://lwn.net/Articles/1070588/) | 9 | python3.9 | 2026-04-29 |
| AlmaLinux | [ALSA-2026:13902](https://lwn.net/Articles/1071435/) | 8 | resource-agents | 2026-05-06 |
| AlmaLinux | [ALSA-2026:10758](https://lwn.net/Articles/1070589/) | 10 | sudo | 2026-04-29 |
| AlmaLinux | [ALSA-2026:12310](https://lwn.net/Articles/1071058/) | 9 | sudo | 2026-05-01 |
| AlmaLinux | [ALSA-2026:13651](https://lwn.net/Articles/1071436/) | 10 | systemd | 2026-05-06 |
| AlmaLinux | [ALSA-2026:13677](https://lwn.net/Articles/1071437/) | 9 | systemd | 2026-05-05 |
| AlmaLinux | [ALSA-2026:12285](https://lwn.net/Articles/1071059/) | 10 | thunderbird | 2026-05-03 |
| AlmaLinux | [ALSA-2026:13537](https://lwn.net/Articles/1071290/) | 8 | thunderbird | 2026-05-05 |
| AlmaLinux | [ALSA-2026:13414](https://lwn.net/Articles/1071291/) | 8 | tigervnc | 2026-05-05 |
| AlmaLinux | [ALSA-2026:10739](https://lwn.net/Articles/1070590/) | 9 | tigervnc | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11389](https://lwn.net/Articles/1070592/) | 10 | vim | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11509](https://lwn.net/Articles/1070591/) | 8 | vim | 2026-04-30 |
| AlmaLinux | [ALSA-2026:11510](https://lwn.net/Articles/1070593/) | 9 | vim | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11692](https://lwn.net/Articles/1070594/) | 8 | xorg-x11-server | 2026-04-30 |
| AlmaLinux | [ALSA-2026:11388](https://lwn.net/Articles/1070595/) | 9 | xorg-x11-server | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11352](https://lwn.net/Articles/1070598/) | 10 | xorg-x11-server-Xwayland | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11656](https://lwn.net/Articles/1070596/) | 8 | xorg-x11-server-Xwayland | 2026-04-30 |
| AlmaLinux | [ALSA-2026:11369](https://lwn.net/Articles/1070597/) | 9 | xorg-x11-server-Xwayland | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11413](https://lwn.net/Articles/1070599/) | 10 | yggdrasil | 2026-04-29 |
| AlmaLinux | [ALSA-2026:11412](https://lwn.net/Articles/1070600/) | 10 | yggdrasil-worker-package-manager | 2026-04-29 |
| Debian | [DLA-4554-1](https://lwn.net/Articles/1070601/) | LTS | calibre | 2026-04-30 |
| Debian | [DSA-6239-1](https://lwn.net/Articles/1070763/) | stable | chromium | 2026-05-01 |
| Debian | [DLA-4556-1](https://lwn.net/Articles/1070764/) | LTS | dovecot | 2026-05-01 |
| Debian | [DSA-6197-3](https://lwn.net/Articles/1071060/) | stable | dovecot | 2026-05-01 |
| Debian | [DLA-4555-1](https://lwn.net/Articles/1070602/) | LTS | firefox-esr | 2026-04-30 |
| Debian | [DSA-6236-1](https://lwn.net/Articles/1070603/) | stable | firefox-esr | 2026-04-29 |
| Debian | [DLA-4559-1](https://lwn.net/Articles/1071062/) | LTS | imagemagick | 2026-05-01 |
| Debian | [DSA-6245-1](https://lwn.net/Articles/1071061/) | stable | imagemagick | 2026-05-03 |
| Debian | [DSA-6240-1](https://lwn.net/Articles/1071063/) | stable | imagemagick | 2026-05-01 |
| Debian | [DSA-6244-1](https://lwn.net/Articles/1071064/) | stable | incus | 2026-05-02 |
| Debian | [DLA-4560-1](https://lwn.net/Articles/1071065/) | LTS | kernel | 2026-05-02 |
| Debian | [DSA-6238-1](https://lwn.net/Articles/1070765/) | stable | kernel | 2026-04-30 |
| Debian | [DSA-6243-1](https://lwn.net/Articles/1071066/) | stable | kernel | 2026-05-01 |
| Debian | [DLA-4563-1](https://lwn.net/Articles/1071292/) | LTS | libarchive | 2026-05-05 |
| Debian | [DLA-4558-1](https://lwn.net/Articles/1071067/) | LTS | libexif | 2026-05-01 |
| Debian | [DLA-4561-1](https://lwn.net/Articles/1071068/) | LTS | linux-6.1 | 2026-05-02 |
| Debian | [DSA-6247-1](https://lwn.net/Articles/1071293/) | stable | lxd | 2026-05-04 |
| Debian | [DLA-4566-1](https://lwn.net/Articles/1071438/) | LTS | openjdk-11 | 2026-05-06 |
| Debian | [DLA-4565-1](https://lwn.net/Articles/1071439/) | LTS | openjdk-17 | 2026-05-06 |
| Debian | [DSA-6237-1](https://lwn.net/Articles/1070604/) | stable | openjdk-17 | 2026-04-29 |
| Debian | [DSA-6246-1](https://lwn.net/Articles/1071069/) | stable | openjdk-25 | 2026-05-03 |
| Debian | [DLA-4557-1](https://lwn.net/Articles/1071070/) | LTS | pyasn1 | 2026-05-01 |
| Debian | [DLA-4564-1](https://lwn.net/Articles/1071440/) | LTS | pyjwt | 2026-05-05 |
| Debian | [DSA-6241-1](https://lwn.net/Articles/1071071/) | stable | python-aiohttp | 2026-05-01 |
| Debian | [DLA-4562-1](https://lwn.net/Articles/1071072/) | LTS | thunderbird | 2026-05-04 |
| Debian | [DSA-6242-1](https://lwn.net/Articles/1071073/) | stable | thunderbird | 2026-05-01 |
| Fedora | [FEDORA-2026-fdbf3705cc](https://lwn.net/Articles/1071077/) | F43 | GitPython | 2026-05-02 |
| Fedora | [FEDORA-2026-9342da13e0](https://lwn.net/Articles/1071078/) | F44 | GitPython | 2026-05-02 |
| Fedora | [FEDORA-2026-98decbde87](https://lwn.net/Articles/1070607/) | F42 | asterisk | 2026-04-30 |
| Fedora | [FEDORA-2026-80b21debe7](https://lwn.net/Articles/1070606/) | F43 | asterisk | 2026-04-30 |
| Fedora | [FEDORA-2026-38d71393c1](https://lwn.net/Articles/1070605/) | F44 | asterisk | 2026-04-30 |
| Fedora | [FEDORA-2026-3831e11232](https://lwn.net/Articles/1070609/) | F42 | binaryen | 2026-04-30 |
| Fedora | [FEDORA-2026-fb3e461878](https://lwn.net/Articles/1070608/) | F43 | binaryen | 2026-04-30 |
| Fedora | [FEDORA-2026-156e6bfb27](https://lwn.net/Articles/1070610/) | F42 | buildah | 2026-04-30 |
| Fedora | [FEDORA-2026-36fb406407](https://lwn.net/Articles/1071074/) | F42 | chromium | 2026-05-04 |
| Fedora | [FEDORA-2026-2a5d3e5194](https://lwn.net/Articles/1070766/) | F42 | chromium | 2026-05-01 |
| Fedora | [FEDORA-2026-af3f470d38](https://lwn.net/Articles/1071294/) | F43 | chromium | 2026-05-05 |
| Fedora | [FEDORA-2026-f5ed344d5c](https://lwn.net/Articles/1071075/) | F44 | chromium | 2026-05-03 |
| Fedora | [FEDORA-2026-511c8bd939](https://lwn.net/Articles/1070612/) | F43 | dokuwiki | 2026-04-30 |
| Fedora | [FEDORA-2026-e1f1cff72a](https://lwn.net/Articles/1070611/) | F44 | dokuwiki | 2026-04-30 |
| Fedora | [FEDORA-2026-ad17a2db6c](https://lwn.net/Articles/1070769/) | F42 | dotnet10.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-eadd724963](https://lwn.net/Articles/1070767/) | F43 | dotnet10.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-fc2112cdd4](https://lwn.net/Articles/1070768/) | F44 | dotnet10.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-02b2a30c02](https://lwn.net/Articles/1070772/) | F42 | dotnet8.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-a1302c450c](https://lwn.net/Articles/1070770/) | F43 | dotnet8.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-edca75e401](https://lwn.net/Articles/1070771/) | F44 | dotnet8.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-ac43e01af9](https://lwn.net/Articles/1070775/) | F42 | dotnet9.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-97fbaaef10](https://lwn.net/Articles/1070773/) | F43 | dotnet9.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-e1d2833798](https://lwn.net/Articles/1070774/) | F44 | dotnet9.0 | 2026-05-01 |
| Fedora | [FEDORA-2026-52dad6273a](https://lwn.net/Articles/1070778/) | F42 | emacs | 2026-05-01 |
| Fedora | [FEDORA-2026-290753da75](https://lwn.net/Articles/1070776/) | F43 | emacs | 2026-05-01 |
| Fedora | [FEDORA-2026-49b8ca7981](https://lwn.net/Articles/1070777/) | F44 | emacs | 2026-05-01 |
| Fedora | [FEDORA-2026-c0a4f03150](https://lwn.net/Articles/1071076/) | F43 | firefox | 2026-05-03 |
| Fedora | [FEDORA-2026-4b7780802c](https://lwn.net/Articles/1071079/) | F43 | glibc | 2026-05-03 |
| Fedora | [FEDORA-2026-ced72ab158](https://lwn.net/Articles/1071080/) | F44 | glibc | 2026-05-02 |
| Fedora | [FEDORA-2026-9d0e7df23a](https://lwn.net/Articles/1070781/) | F42 | glow | 2026-05-01 |
| Fedora | [FEDORA-2026-6d67b00ef1](https://lwn.net/Articles/1070779/) | F43 | glow | 2026-05-01 |
| Fedora | [FEDORA-2026-423a143483](https://lwn.net/Articles/1070780/) | F44 | glow | 2026-05-01 |
| Fedora | [FEDORA-2026-ce402e1f82](https://lwn.net/Articles/1071082/) | F42 | insight | 2026-05-03 |
| Fedora | [FEDORA-2026-e0f5e87dd6](https://lwn.net/Articles/1071081/) | F43 | insight | 2026-05-03 |
| Fedora | [FEDORA-2026-f72d44d09e](https://lwn.net/Articles/1071295/) | F44 | insight | 2026-05-05 |
| Fedora | [FEDORA-2026-6b87863841](https://lwn.net/Articles/1070782/) | F44 | jfrog-cli | 2026-05-01 |
| Fedora | [FEDORA-2026-8b43ea2f82](https://lwn.net/Articles/1071083/) | F44 | krb5 | 2026-05-02 |
| Fedora | [FEDORA-2026-69743812a7](https://lwn.net/Articles/1070615/) | F42 | lemonldap-ng | 2026-04-30 |
| Fedora | [FEDORA-2026-38914f4e04](https://lwn.net/Articles/1070614/) | F43 | lemonldap-ng | 2026-04-30 |
| Fedora | [FEDORA-2026-6c8dcaf023](https://lwn.net/Articles/1070613/) | F44 | lemonldap-ng | 2026-04-30 |
| Fedora | [FEDORA-2026-b01307dc4d](https://lwn.net/Articles/1070616/) | F42 | libexif | 2026-04-30 |
| Fedora | [FEDORA-2026-8409145c11](https://lwn.net/Articles/1070618/) | F43 | libgcrypt | 2026-04-30 |
| Fedora | [FEDORA-2026-9a79c58afd](https://lwn.net/Articles/1070617/) | F44 | libgcrypt | 2026-04-30 |
| Fedora | [FEDORA-2026-2e8a8fd35b](https://lwn.net/Articles/1070621/) | F42 | miniupnpd | 2026-04-30 |
| Fedora | [FEDORA-2026-5f908cb040](https://lwn.net/Articles/1070620/) | F43 | miniupnpd | 2026-04-30 |
| Fedora | [FEDORA-2026-f933979509](https://lwn.net/Articles/1070619/) | F44 | miniupnpd | 2026-04-30 |
| Fedora | [FEDORA-2026-3111ffa11a](https://lwn.net/Articles/1071084/) | F44 | nano | 2026-05-03 |
| Fedora | [FEDORA-2026-9dc3a61ad8](https://lwn.net/Articles/1071296/) | F43 | nodejs20 | 2026-05-05 |
| Fedora | [FEDORA-2026-c99f9dc3b1](https://lwn.net/Articles/1071297/) | F44 | nodejs20 | 2026-05-05 |
| Fedora | [FEDORA-2026-c0a4f03150](https://lwn.net/Articles/1071085/) | F43 | nss | 2026-05-03 |
| Fedora | [FEDORA-2026-c008e6a5da](https://lwn.net/Articles/1070785/) | F42 | openbao | 2026-05-01 |
| Fedora | [FEDORA-2026-41918b2b57](https://lwn.net/Articles/1070783/) | F43 | openbao | 2026-05-01 |
| Fedora | [FEDORA-2026-c7450bfed6](https://lwn.net/Articles/1070784/) | F44 | openbao | 2026-05-01 |
| Fedora | [FEDORA-2026-d08c298940](https://lwn.net/Articles/1071086/) | F42 | openssh | 2026-05-02 |
| Fedora | [FEDORA-2026-ddc5696c20](https://lwn.net/Articles/1071087/) | F42 | openvpn | 2026-05-02 |
| Fedora | [FEDORA-2026-086acf3001](https://lwn.net/Articles/1070622/) | F44 | openvpn | 2026-04-30 |
| Fedora | [FEDORA-2026-f416c4ba87](https://lwn.net/Articles/1071441/) | F44 | pdns | 2026-05-06 |
| Fedora | [FEDORA-2026-bc5090f99b](https://lwn.net/Articles/1071089/) | F42 | perl-CryptX | 2026-05-02 |
| Fedora | [FEDORA-2026-3e1f671a17](https://lwn.net/Articles/1071088/) | F43 | perl-CryptX | 2026-05-02 |
| Fedora | [FEDORA-2026-f533fcc0b6](https://lwn.net/Articles/1071090/) | F44 | perl-CryptX | 2026-05-02 |
| Fedora | [FEDORA-2026-156e6bfb27](https://lwn.net/Articles/1070623/) | F42 | podman | 2026-04-30 |
| Fedora | [FEDORA-2026-05d463c932](https://lwn.net/Articles/1071442/) | F44 | pyOpenSSL | 2026-05-06 |
| Fedora | [FEDORA-2026-91671b8061](https://lwn.net/Articles/1070788/) | F42 | pyp2spec | 2026-05-01 |
| Fedora | [FEDORA-2026-1f68c09a18](https://lwn.net/Articles/1070786/) | F43 | pyp2spec | 2026-05-01 |
| Fedora | [FEDORA-2026-4a8ed954a6](https://lwn.net/Articles/1070787/) | F44 | pyp2spec | 2026-05-01 |
| Fedora | [FEDORA-2026-97a8eb204a](https://lwn.net/Articles/1071091/) | F43 | python3.14 | 2026-05-04 |
| Fedora | [FEDORA-2026-c1ca370c1a](https://lwn.net/Articles/1070791/) | F42 | python3.6 | 2026-05-01 |
| Fedora | [FEDORA-2026-f08d5a8191](https://lwn.net/Articles/1070789/) | F43 | python3.6 | 2026-05-01 |
| Fedora | [FEDORA-2026-a335d04675](https://lwn.net/Articles/1070790/) | F44 | python3.6 | 2026-05-01 |
| Fedora | [FEDORA-2026-60a694a385](https://lwn.net/Articles/1070626/) | F42 | python3.9 | 2026-04-30 |
| Fedora | [FEDORA-2026-7986d7f994](https://lwn.net/Articles/1070625/) | F43 | python3.9 | 2026-04-30 |
| Fedora | [FEDORA-2026-85cf3694d8](https://lwn.net/Articles/1070624/) | F44 | python3.9 | 2026-04-30 |
| Fedora | [FEDORA-2026-76f57efeef](https://lwn.net/Articles/1071093/) | F42 | rust-openssl | 2026-05-02 |
| Fedora | [FEDORA-2026-16a3cea414](https://lwn.net/Articles/1071092/) | F43 | rust-openssl | 2026-05-02 |
| Fedora | [FEDORA-2026-fc9d4b5520](https://lwn.net/Articles/1071094/) | F44 | rust-openssl | 2026-05-02 |
| Fedora | [FEDORA-2026-76f57efeef](https://lwn.net/Articles/1071096/) | F42 | rust-openssl-sys | 2026-05-02 |
| Fedora | [FEDORA-2026-16a3cea414](https://lwn.net/Articles/1071095/) | F43 | rust-openssl-sys | 2026-05-02 |
| Fedora | [FEDORA-2026-fc9d4b5520](https://lwn.net/Articles/1071097/) | F44 | rust-openssl-sys | 2026-05-02 |
| Fedora | [FEDORA-2026-a80c26d6f3](https://lwn.net/Articles/1070628/) | F43 | rust-rpm-sequoia | 2026-04-30 |
| Fedora | [FEDORA-2026-a15009ab19](https://lwn.net/Articles/1070627/) | F44 | rust-rpm-sequoia | 2026-04-30 |
| Fedora | [FEDORA-2026-204499102d](https://lwn.net/Articles/1070794/) | F42 | rust-rustls-webpki | 2026-05-01 |
| Fedora | [FEDORA-2026-bea616fc84](https://lwn.net/Articles/1070792/) | F43 | rust-rustls-webpki | 2026-05-01 |
| Fedora | [FEDORA-2026-8f36b2341e](https://lwn.net/Articles/1070793/) | F44 | rust-rustls-webpki | 2026-05-01 |
| Fedora | [FEDORA-2026-6f64d2e143](https://lwn.net/Articles/1071099/) | F42 | rust-sequoia-git | 2026-05-03 |
| Fedora | [FEDORA-2026-95ac9001e8](https://lwn.net/Articles/1071098/) | F43 | rust-sequoia-git | 2026-05-03 |
| Fedora | [FEDORA-2026-0a72408e1b](https://lwn.net/Articles/1071298/) | F44 | rust-sequoia-git | 2026-05-05 |
| Fedora | [FEDORA-2026-156e6bfb27](https://lwn.net/Articles/1070629/) | F42 | skopeo | 2026-04-30 |
| Fedora | [FEDORA-2026-c0590bd498](https://lwn.net/Articles/1071443/) | F44 | squid | 2026-05-06 |
| Fedora | [FEDORA-2026-57515ed8b1](https://lwn.net/Articles/1071299/) | F44 | uriparser | 2026-05-05 |
| Fedora | [FEDORA-2026-795b0d0367](https://lwn.net/Articles/1070797/) | F42 | vhs | 2026-05-01 |
| Fedora | [FEDORA-2026-7646f2a691](https://lwn.net/Articles/1070795/) | F43 | vhs | 2026-05-01 |
| Fedora | [FEDORA-2026-94fbf80bec](https://lwn.net/Articles/1070796/) | F44 | vhs | 2026-05-01 |
| Fedora | [FEDORA-2026-adc66b374a](https://lwn.net/Articles/1070630/) | F42 | xdg-dbus-proxy | 2026-04-30 |
| Fedora | [FEDORA-2026-78cd69d9ae](https://lwn.net/Articles/1070798/) | F43 | xen | 2026-05-01 |
| Fedora | [FEDORA-2026-883e88db68](https://lwn.net/Articles/1071100/) | F44 | xen | 2026-05-02 |
| Mageia | [MGASA-2026-0108](https://lwn.net/Articles/1071300/) | 9 | kernel, kmod-virtualbox | 2026-05-04 |
| Oracle | [ELSA-2026-11635](https://lwn.net/Articles/1070804/) | OL8 | PackageKit | 2026-04-30 |
| Oracle | [ELSA-2026-11504](https://lwn.net/Articles/1070805/) | OL9 | PackageKit | 2026-04-30 |
| Oracle | [ELSA-2026-50249](https://lwn.net/Articles/1071107/) |  | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-50251](https://lwn.net/Articles/1071101/) | OL8 | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-50250](https://lwn.net/Articles/1071102/) | OL8 | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-50251](https://lwn.net/Articles/1071103/) | OL8 | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-50250](https://lwn.net/Articles/1071104/) | OL9 | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-50250](https://lwn.net/Articles/1071105/) | OL9 | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-50249](https://lwn.net/Articles/1071106/) | OL9 | dtrace | 2026-05-01 |
| Oracle | [ELSA-2026-12176](https://lwn.net/Articles/1071108/) | OL8 | fence-agents | 2026-05-01 |
| Oracle | [ELSA-2026-11712](https://lwn.net/Articles/1070801/) | OL10 | grafana | 2026-04-30 |
| Oracle | [ELSA-2026-11507](https://lwn.net/Articles/1070799/) | OL8 | grafana | 2026-04-30 |
| Oracle | [ELSA-2026-11711](https://lwn.net/Articles/1070800/) | OL9 | grafana | 2026-04-30 |
| Oracle | [ELSA-2026-11881](https://lwn.net/Articles/1071109/) | OL10 | grafana-pcp | 2026-05-01 |
| Oracle | [ELSA-2026-11514](https://lwn.net/Articles/1070802/) | OL8 | grafana-pcp | 2026-04-30 |
| Oracle | [ELSA-2026-11704](https://lwn.net/Articles/1070803/) | OL9 | grafana-pcp | 2026-04-30 |
| Oracle | [ELSA-2026-50255](https://lwn.net/Articles/1071307/) | OL7 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-50255](https://lwn.net/Articles/1071305/) | OL8 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-50255](https://lwn.net/Articles/1071306/) | OL8 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-50253](https://lwn.net/Articles/1071304/) | OL8 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-50254](https://lwn.net/Articles/1071301/) | OL9 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-50253](https://lwn.net/Articles/1071302/) | OL9 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-50253](https://lwn.net/Articles/1071303/) | OL9 | kernel | 2026-05-04 |
| Oracle | [ELSA-2026-12423](https://lwn.net/Articles/1071308/) | OL10 | libcap | 2026-05-04 |
| Oracle | [ELSA-2026-12441](https://lwn.net/Articles/1071110/) | OL9 | libcap | 2026-05-01 |
| Oracle | [ELSA-2026-12265](https://lwn.net/Articles/1071112/) | OL10 | libtiff | 2026-05-01 |
| Oracle | [ELSA-2026-12271](https://lwn.net/Articles/1071111/) | OL9 | libtiff | 2026-05-01 |
| Oracle | [ELSA-2026-11521](https://lwn.net/Articles/1070806/) | OL8 | sudo | 2026-04-30 |
| Oracle | [ELSA-2026-12310](https://lwn.net/Articles/1071113/) | OL9 | sudo | 2026-05-01 |
| Oracle | [ELSA-2026-12285](https://lwn.net/Articles/1071309/) | OL10 | thunderbird | 2026-05-04 |
| Oracle | [ELSA-2026-50254](https://lwn.net/Articles/1071310/) |  | uek-kernel | 2026-05-04 |
| Oracle | [ELSA-2026-11509](https://lwn.net/Articles/1070807/) | OL8 | vim | 2026-04-30 |
| Oracle | [ELSA-2026-11510](https://lwn.net/Articles/1070808/) | OL9 | vim | 2026-04-30 |
| Oracle | [ELSA-2026-11692](https://lwn.net/Articles/1070809/) | OL8 | xorg-x11-server | 2026-04-30 |
| Oracle | [ELSA-2026-11656](https://lwn.net/Articles/1071114/) | OL8 | xorg-x11-server-Xwayland | 2026-05-01 |
| Red Hat | [RHSA-2026:8467-01](https://lwn.net/Articles/1071273/) | EL10 | .NET 10.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8473-01](https://lwn.net/Articles/1071267/) | EL8 | .NET 10.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8471-01](https://lwn.net/Articles/1071269/) | EL9 | .NET 10.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8470-01](https://lwn.net/Articles/1071271/) | EL10 | .NET 8.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:13281-01](https://lwn.net/Articles/1071277/) | EL10.0 | .NET 8.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8468-01](https://lwn.net/Articles/1071272/) | EL8 | .NET 8.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8469-01](https://lwn.net/Articles/1071268/) | EL9 | .NET 8.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:13693-01](https://lwn.net/Articles/1071274/) | EL9.4 | .NET 8.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:13283-01](https://lwn.net/Articles/1071276/) | EL9.6 | .NET 8.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8472-01](https://lwn.net/Articles/1071270/) | EL10 | .NET 9.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:13280-01](https://lwn.net/Articles/1071278/) | EL10.0 | .NET 9.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8475-01](https://lwn.net/Articles/1071265/) | EL8 | .NET 9.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:8474-01](https://lwn.net/Articles/1071266/) | EL9 | .NET 9.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:13282-01](https://lwn.net/Articles/1071275/) | EL9.6 | .NET 9.0 | 2026-05-05 |
| Red Hat | [RHSA-2026:13284-01](https://lwn.net/Articles/1071044/) | EL8 | LibRaw | 2026-05-04 |
| Red Hat | [RHSA-2026:10135-01](https://lwn.net/Articles/1070563/) | EL9 | buildah | 2026-04-30 |
| Red Hat | [RHSA-2026:12030-01](https://lwn.net/Articles/1071000/) | EL9.4 | buildah | 2026-05-04 |
| Red Hat | [RHSA-2026:11749-01](https://lwn.net/Articles/1071001/) | EL9.6 | buildah | 2026-05-04 |
| Red Hat | [RHSA-2026:1905-01](https://lwn.net/Articles/1071040/) | EL10 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2309-01](https://lwn.net/Articles/1071036/) | EL10.0 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:1906-01](https://lwn.net/Articles/1071041/) | EL8 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:12176-01](https://lwn.net/Articles/1071282/) | EL8 | fence-agents | 2026-05-05 |
| Red Hat | [RHSA-2026:2483-01](https://lwn.net/Articles/1071032/) | EL8.4 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2486-01](https://lwn.net/Articles/1071031/) | EL8.6 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2221-01](https://lwn.net/Articles/1071039/) | EL8.8 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:1903-01](https://lwn.net/Articles/1071042/) | EL9 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:13672-01](https://lwn.net/Articles/1071281/) | EL9 | fence-agents | 2026-05-05 |
| Red Hat | [RHSA-2026:2303-01](https://lwn.net/Articles/1071033/) | EL9.0 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2300-01](https://lwn.net/Articles/1071038/) | EL9.2 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2302-01](https://lwn.net/Articles/1071035/) | EL9.4 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2299-01](https://lwn.net/Articles/1071043/) | EL9.6 | fence-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:11805-01](https://lwn.net/Articles/1071015/) | EL8.2 | firefox | 2026-05-04 |
| Red Hat | [RHSA-2026:10707-01](https://lwn.net/Articles/1070562/) | EL10 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:11325-01](https://lwn.net/Articles/1070559/) | EL10.0 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:12114-01](https://lwn.net/Articles/1070553/) | EL7 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:10741-01](https://lwn.net/Articles/1070560/) | EL8 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:11806-01](https://lwn.net/Articles/1070555/) | EL8.2 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:12115-01](https://lwn.net/Articles/1070552/) | EL8.6 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:12060-01](https://lwn.net/Articles/1070551/) | EL8.8 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:10708-01](https://lwn.net/Articles/1070561/) | EL9 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:12061-01](https://lwn.net/Articles/1070554/) | EL9.0 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:11326-01](https://lwn.net/Articles/1070558/) | EL9.2 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:11328-01](https://lwn.net/Articles/1070557/) | EL9.4 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:11327-01](https://lwn.net/Articles/1070556/) | EL9.6 | gdk-pixbuf2 | 2026-04-30 |
| Red Hat | [RHSA-2026:9254-01](https://lwn.net/Articles/1071007/) | EL7 | java-11-openjdk with Extended Lifecycle Support | 2026-05-04 |
| Red Hat | [RHSA-2026:7675-01](https://lwn.net/Articles/1071050/) | EL10 | nodejs24 | 2026-05-04 |
| Red Hat | [RHSA-2026:9711-01](https://lwn.net/Articles/1070550/) | EL9.4 | nodejs:20 | 2026-04-30 |
| Red Hat | [RHSA-2026:9874-01](https://lwn.net/Articles/1070549/) | EL9.6 | nodejs:20 | 2026-04-30 |
| Red Hat | [RHSA-2026:7670-01](https://lwn.net/Articles/1071049/) | EL8 | nodejs:24 | 2026-05-04 |
| Red Hat | [RHSA-2026:7350-01](https://lwn.net/Articles/1071048/) | EL9 | nodejs:24 | 2026-05-04 |
| Red Hat | [RHSA-2026:13380-01](https://lwn.net/Articles/1071046/) | EL10 | openssh | 2026-05-04 |
| Red Hat | [RHSA-2026:12389-01](https://lwn.net/Articles/1071047/) | EL10.0 | openssh | 2026-05-04 |
| Red Hat | [RHSA-2026:13383-01](https://lwn.net/Articles/1071045/) | EL8 | openssh | 2026-05-04 |
| Red Hat | [RHSA-2026:3354-01](https://lwn.net/Articles/1071029/) | EL10 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4138-01](https://lwn.net/Articles/1071023/) | EL10.0 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4148-01](https://lwn.net/Articles/1071016/) | EL7 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4146-01](https://lwn.net/Articles/1071019/) | EL8 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4145-01](https://lwn.net/Articles/1071020/) | EL8.2 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4147-01](https://lwn.net/Articles/1071017/) | EL8.4 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4144-01](https://lwn.net/Articles/1071018/) | EL8.6 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4139-01](https://lwn.net/Articles/1071026/) | EL8.8 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:3359-01](https://lwn.net/Articles/1071027/) | EL9 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4140-01](https://lwn.net/Articles/1071025/) | EL9.0 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4142-01](https://lwn.net/Articles/1071024/) | EL9.2 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4143-01](https://lwn.net/Articles/1071021/) | EL9.4 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:4141-01](https://lwn.net/Articles/1071022/) | EL9.6 | python-pyasn1 | 2026-05-04 |
| Red Hat | [RHSA-2026:2758-01](https://lwn.net/Articles/1071028/) | EL7 | resource-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2712-01](https://lwn.net/Articles/1071030/) | EL8.4 | resource-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2453-01](https://lwn.net/Articles/1071034/) | EL8.6 | resource-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:2460-01](https://lwn.net/Articles/1071037/) | EL8.8 | resource-agents | 2026-05-04 |
| Red Hat | [RHSA-2026:10107-01](https://lwn.net/Articles/1070761/) | EL8 | rhc | 2026-05-01 |
| Red Hat | [RHSA-2026:10706-01](https://lwn.net/Articles/1070759/) | EL9 | rhc | 2026-05-01 |
| Red Hat | [RHSA-2026:10705-01](https://lwn.net/Articles/1070760/) | EL9.6 | rhc | 2026-05-01 |
| Red Hat | [RHSA-2026:10758-01](https://lwn.net/Articles/1071264/) | EL10 | sudo | 2026-05-05 |
| Red Hat | [RHSA-2026:11521-01](https://lwn.net/Articles/1071263/) | EL8 | sudo | 2026-05-05 |
| Red Hat | [RHSA-2026:12310-01](https://lwn.net/Articles/1071262/) | EL9 | sudo | 2026-05-05 |
| Red Hat | [RHSA-2026:13731-01](https://lwn.net/Articles/1071261/) | EL9.0 | sudo | 2026-05-05 |
| Red Hat | [RHSA-2026:13651-01](https://lwn.net/Articles/1071280/) | EL10 | systemd | 2026-05-05 |
| Red Hat | [RHSA-2026:13677-01](https://lwn.net/Articles/1071279/) | EL9 | systemd | 2026-05-05 |
| Red Hat | [RHSA-2026:9638-01](https://lwn.net/Articles/1071008/) | EL10 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:11813-01](https://lwn.net/Articles/1071014/) | EL10.0 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:9345-01](https://lwn.net/Articles/1071010/) | EL8 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:8459-01](https://lwn.net/Articles/1071009/) | EL9 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:12264-01](https://lwn.net/Articles/1071013/) | EL9.0 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:13412-01](https://lwn.net/Articles/1071011/) | EL9.2 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:13342-01](https://lwn.net/Articles/1071012/) | EL9.6 | thunderbird | 2026-05-04 |
| Red Hat | [RHSA-2026:13414-01](https://lwn.net/Articles/1071002/) | EL8 | tigervnc | 2026-05-04 |
| Red Hat | [RHSA-2026:11692-01](https://lwn.net/Articles/1071004/) | EL8 | xorg-x11-server | 2026-05-04 |
| Red Hat | [RHSA-2026:11388-01](https://lwn.net/Articles/1071005/) | EL9 | xorg-x11-server | 2026-05-04 |
| Red Hat | [RHSA-2026:11656-01](https://lwn.net/Articles/1071003/) | EL8 | xorg-x11-server-Xwayland | 2026-05-04 |
| Red Hat | [RHSA-2026:11369-01](https://lwn.net/Articles/1071006/) | EL9 | xorg-x11-server-Xwayland | 2026-05-04 |
| Slackware | [SSA:2026-124-01](https://lwn.net/Articles/1071311/) |  | httpd | 2026-05-04 |
| Slackware | [SSA:2026-125-01](https://lwn.net/Articles/1071444/) |  | hunspell | 2026-05-05 |
| Slackware | [SSA:2026-121-01](https://lwn.net/Articles/1071115/) |  | mozilla | 2026-05-01 |
| SUSE | [SUSE-SU-2026:21412-1](https://lwn.net/Articles/1070827/) | SLE-m6.0 | Mesa | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1701-1](https://lwn.net/Articles/1071457/) | SLE12 | PackageKit | 2026-05-06 |
| SUSE | [SUSE-SU-2026:1700-1](https://lwn.net/Articles/1071456/) | SLE15 oS15.4 | PackageKit | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21427-1](https://lwn.net/Articles/1071156/) | SLE16.0 | PackageKit | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10669-1](https://lwn.net/Articles/1071445/) | TW | alloy | 2026-05-05 |
| SUSE | [SUSE-SU-2026:21417-1](https://lwn.net/Articles/1070810/) | SLE-m6.0 | avahi | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21445-1](https://lwn.net/Articles/1071116/) | SLE-m6.1 | avahi | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10670-1](https://lwn.net/Articles/1071446/) | TW | avahi | 2026-05-05 |
| SUSE | [SUSE-SU-2026:21404-1](https://lwn.net/Articles/1070811/) | SLE16 | bouncycastle | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10671-1](https://lwn.net/Articles/1071447/) | TW | bubblewrap | 2026-05-05 |
| SUSE | [openSUSE-SU-2026:0161-1](https://lwn.net/Articles/1070812/) | osB15 | chromium | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:10672-1](https://lwn.net/Articles/1071448/) | TW | cmctl | 2026-05-05 |
| SUSE | [SUSE-SU-2026:21405-1](https://lwn.net/Articles/1070813/) | SLE16 | container-suseconnect | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10673-1](https://lwn.net/Articles/1071449/) | TW | coredns | 2026-05-05 |
| SUSE | [SUSE-SU-2026:21452-1](https://lwn.net/Articles/1071117/) | SLE-m6.1 | curl | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10674-1](https://lwn.net/Articles/1071450/) | TW | curl | 2026-05-05 |
| SUSE | [openSUSE-SU-2026:10632-1](https://lwn.net/Articles/1070631/) | TW | dnsdist | 2026-04-29 |
| SUSE | [openSUSE-SU-2026:10675-1](https://lwn.net/Articles/1071451/) | TW | dpkg | 2026-05-05 |
| SUSE | [openSUSE-SU-2026:10668-1](https://lwn.net/Articles/1071452/) | TW | firefox | 2026-05-05 |
| SUSE | [SUSE-SU-2026:21418-1](https://lwn.net/Articles/1070814/) | SLE-m6.0 | firewalld | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21446-1](https://lwn.net/Articles/1071118/) | SLE-m6.1 | freeipmi | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21436-1](https://lwn.net/Articles/1071119/) | SLE16.0 | freerdp | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20657-1](https://lwn.net/Articles/1071312/) | oS16.0 | freerdp | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21411-1](https://lwn.net/Articles/1070815/) | SLE-m6.0 | gdk-pixbuf | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10676-1](https://lwn.net/Articles/1071453/) | TW | golang-github-prometheus-prometheus | 2026-05-05 |
| SUSE | [openSUSE-SU-2026:10654-1](https://lwn.net/Articles/1071120/) | TW | google-guest-agent | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:10655-1](https://lwn.net/Articles/1071121/) | TW | google-osconfig-agent | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:10677-1](https://lwn.net/Articles/1071454/) | TW | grafana | 2026-05-05 |
| SUSE | [openSUSE-SU-2026:20654-1](https://lwn.net/Articles/1070816/) | oS16.0 | grafana | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10652-1](https://lwn.net/Articles/1071122/) | TW | gvim | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:20662-1](https://lwn.net/Articles/1071313/) | oS16.0 | hauler | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21461-1](https://lwn.net/Articles/1071124/) | SLE-m6.2 | helm | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21434-1](https://lwn.net/Articles/1071123/) | SLE16.0 | helm | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20655-1](https://lwn.net/Articles/1071314/) | oS16.0 | helm | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21437-1](https://lwn.net/Articles/1071125/) | SLE16.0 | himmelblau | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20658-1](https://lwn.net/Articles/1071315/) | oS16.0 | himmelblau | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10656-1](https://lwn.net/Articles/1071126/) | TW | java-1_8_0-openjdk | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:10639-1](https://lwn.net/Articles/1070817/) | TW | java-25-openjdk | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1672-1](https://lwn.net/Articles/1071134/) | MP4.3 SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21443-1](https://lwn.net/Articles/1071137/) | SLE-m6.0 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21459-1](https://lwn.net/Articles/1071143/) | SLE-m6.0 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21454-1](https://lwn.net/Articles/1071145/) | SLE-m6.0 SLE-m6.1 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1668-1](https://lwn.net/Articles/1071147/) | SLE12 | kernel | 2026-05-01 |
| SUSE | [SUSE-SU-2026:1669-1](https://lwn.net/Articles/1071130/) | SLE12 SLE15 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1661-1](https://lwn.net/Articles/1070818/) | SLE15 | kernel | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1678-1](https://lwn.net/Articles/1071128/) | SLE15 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1674-1](https://lwn.net/Articles/1071133/) | SLE15 SLE5.2 SLE-m5.2 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1677-1](https://lwn.net/Articles/1071129/) | SLE15 SLE5.2 SLE-m5.2 oS15.3 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1675-1](https://lwn.net/Articles/1071132/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1670-1](https://lwn.net/Articles/1071136/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1676-1](https://lwn.net/Articles/1071131/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1671-1](https://lwn.net/Articles/1071135/) | SLE15 oS15.6 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1671-2](https://lwn.net/Articles/1071316/) | SLE15 oS15.6 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21421-1](https://lwn.net/Articles/1071127/) | SLE16.0 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21439-1](https://lwn.net/Articles/1071139/) | SLE16.0 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21463-1](https://lwn.net/Articles/1071141/) | SLE16.0 SLE-m6.2 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21460-1](https://lwn.net/Articles/1071142/) | SLE16.0 SLE-m6.2 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21442-1](https://lwn.net/Articles/1071138/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21458-1](https://lwn.net/Articles/1071144/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21453-1](https://lwn.net/Articles/1071146/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21465-1](https://lwn.net/Articles/1071140/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10657-1](https://lwn.net/Articles/1071148/) | TW | krb5-appl-clients | 2026-05-01 |
| SUSE | [SUSE-SU-2026:1660-1](https://lwn.net/Articles/1070632/) | SLE15 | libheif | 2026-04-29 |
| SUSE | [openSUSE-SU-2026:10641-1](https://lwn.net/Articles/1070819/) | TW | libixml11 | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10642-1](https://lwn.net/Articles/1070820/) | TW | libmozjs-140-0 | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10640-1](https://lwn.net/Articles/1070821/) | TW | libpng12-0 | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1702-1](https://lwn.net/Articles/1071455/) | SLE12 | libpng12 | 2026-05-06 |
| SUSE | [SUSE-SU-2026:21393-1](https://lwn.net/Articles/1070822/) | SLE-m6.2 | libsodium | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21422-1](https://lwn.net/Articles/1071149/) | SLE16.0 | libsodium | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20642-1](https://lwn.net/Articles/1070823/) | oS16.0 | libsodium | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:20659-1](https://lwn.net/Articles/1071317/) | oS16.0 | libspectre | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21396-1](https://lwn.net/Articles/1070824/) | SLE-m6.2 | libssh | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21428-1](https://lwn.net/Articles/1071150/) | SLE16.0 | libssh | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20647-1](https://lwn.net/Articles/1070825/) | oS16.0 | libssh | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10650-1](https://lwn.net/Articles/1071151/) | TW | libtiff-devel-32bit | 2026-05-01 |
| SUSE | [SUSE-SU-2026:21407-1](https://lwn.net/Articles/1070826/) | SLE16 | mariadb | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21432-1](https://lwn.net/Articles/1071152/) | SLE16.0 | ntfs-3g_ntfsprogs | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20651-1](https://lwn.net/Articles/1070828/) | oS16.0 | ntfs-3g_ntfsprogs | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1658-1](https://lwn.net/Articles/1070633/) | SLE-m5.5 oS15.5 | openCryptoki | 2026-04-29 |
| SUSE | [SUSE-SU-2026:21419-1](https://lwn.net/Articles/1070829/) | SLE-m6.0 | openCryptoki | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21455-1](https://lwn.net/Articles/1071153/) | SLE-m6.1 | openCryptoki | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21433-1](https://lwn.net/Articles/1071154/) | SLE16.0 | openexr | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20652-1](https://lwn.net/Articles/1070830/) | oS16.0 | openexr | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21440-1](https://lwn.net/Articles/1071155/) | SLE-m6.0 SLE-m6.1 | ovmf | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20646-1](https://lwn.net/Articles/1070831/) | oS16.0 | packagekit | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1655-1](https://lwn.net/Articles/1070634/) | SLE-m5.2 SLE-m5.3 SLE-m5.4 | polkit | 2026-04-29 |
| SUSE | [openSUSE-SU-2026:10644-1](https://lwn.net/Articles/1070832/) | TW | prometheus-postgres_exporter | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21426-1](https://lwn.net/Articles/1071158/) | SLE16.0 | python-Mako | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21431-1](https://lwn.net/Articles/1071159/) | SLE16.0 | python-PyNaCl | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1666-1](https://lwn.net/Articles/1070836/) | MP4.3 SLE15 oS15.4 oS15.6 | python-Pygments | 2026-05-01 |
| SUSE | [SUSE-SU-2026:1667-1](https://lwn.net/Articles/1070835/) | SLE15 oS15.3 | python-Pygments | 2026-05-01 |
| SUSE | [SUSE-SU-2026:21425-1](https://lwn.net/Articles/1071157/) | SLE16.0 | python-jwcrypto | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:20644-1](https://lwn.net/Articles/1070833/) | oS16.0 | python-jwcrypto | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:20645-1](https://lwn.net/Articles/1070834/) | oS16.0 | python-mako | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:20650-1](https://lwn.net/Articles/1070837/) | oS16.0 | python-pynacl | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21415-1](https://lwn.net/Articles/1070838/) | SLE-m6.0 | python311 | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21447-1](https://lwn.net/Articles/1071160/) | SLE-m6.1 | python311 | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10646-1](https://lwn.net/Articles/1070839/) | TW | python311-pyOpenSSL | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:10658-1](https://lwn.net/Articles/1071161/) | TW | python311-pypdf | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:10648-1](https://lwn.net/Articles/1070840/) | TW | python315 | 2026-04-30 |
| SUSE | [openSUSE-SU-2026:20653-1](https://lwn.net/Articles/1070841/) | oS16.0 | radare2 | 2026-04-30 |
| SUSE | [SUSE-SU-2026:1659-1](https://lwn.net/Articles/1070635/) | SLE-m5.2 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.3 | sed | 2026-04-29 |
| SUSE | [SUSE-SU-2026:21413-1](https://lwn.net/Articles/1070842/) | SLE-m6.0 | sed | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21448-1](https://lwn.net/Articles/1071162/) | SLE-m6.1 | sed | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1699-1](https://lwn.net/Articles/1071458/) | SLE12 | sed | 2026-05-06 |
| SUSE | [openSUSE-SU-2026:10649-1](https://lwn.net/Articles/1071163/) | TW | sed | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:20664-1](https://lwn.net/Articles/1071318/) | oS16.0 | thunderbird | 2026-05-04 |
| SUSE | [openSUSE-SU-2026:10651-1](https://lwn.net/Articles/1071164/) | TW | trivy | 2026-05-01 |
| SUSE | [openSUSE-SU-2026:0163-1](https://lwn.net/Articles/1071319/) | osB15 | trivy | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21414-1](https://lwn.net/Articles/1070843/) | SLE-m6.0 | vim | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21398-1](https://lwn.net/Articles/1070844/) | SLE-m6.0 | vim | 2026-04-30 |
| SUSE | [SUSE-SU-2026:21450-1](https://lwn.net/Articles/1071166/) | SLE-m6.1 | vim | 2026-05-04 |
| SUSE | [SUSE-SU-2026:21464-1](https://lwn.net/Articles/1071165/) | SLE-m6.1 | vim | 2026-05-04 |
| SUSE | [SUSE-SU-2026:1657-1](https://lwn.net/Articles/1070636/) | SLE15 SLE-m5.5 oS15.5 | xen | 2026-04-29 |
| SUSE | [SUSE-SU-2026:1692-1](https://lwn.net/Articles/1071459/) | SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | xen | 2026-05-05 |
| SUSE | [openSUSE-SU-2026:10660-1](https://lwn.net/Articles/1071320/) | TW | xen | 2026-05-04 |
| Ubuntu | [USN-8227-1](https://lwn.net/Articles/1071321/) | 22.04 24.04 25.10 26.04 | curl | 2026-05-04 |
| Ubuntu | [USN-8230-1](https://lwn.net/Articles/1071460/) | 20.04 22.04 24.04 26.04 | docker.io-app | 2026-05-06 |
| Ubuntu | [USN-8228-1](https://lwn.net/Articles/1071322/) | 22.04 24.04 25.10 26.04 | exim4 | 2026-05-04 |
| Ubuntu | [USN-8226-2](https://lwn.net/Articles/1070846/) | 14.04 16.04 18.04 20.04 | kmod | 2026-04-30 |
| Ubuntu | [USN-8226-1](https://lwn.net/Articles/1070845/) | 22.04 24.04 25.10 | kmod | 2026-04-30 |
| Ubuntu | [USN-8224-1](https://lwn.net/Articles/1070637/) | 20.04 | linux-bluefield | 2026-04-29 |
| Ubuntu | [USN-8233-1](https://lwn.net/Articles/1071461/) | 16.04 18.04 20.04 22.04 24.04 25.10 | nghttp2 | 2026-05-05 |
| Ubuntu | [USN-8232-1](https://lwn.net/Articles/1071462/) | 22.04 24.04 25.10 26.04 | python-django | 2026-05-05 |
| Ubuntu | [USN-8234-1](https://lwn.net/Articles/1071463/) | 16.04 18.04 20.04 22.04 24.04 25.10 26.04 | python-mako | 2026-05-05 |
| Ubuntu | [USN-8225-1](https://lwn.net/Articles/1070638/) | 18.04 20.04 22.04 24.04 26.04 | python-marshmallow | 2026-04-30 |
| Ubuntu | [USN-8223-1](https://lwn.net/Articles/1070639/) | 16.04 18.04 20.04 22.04 24.04 | roundcube | 2026-04-29 |
| Ubuntu | [USN-8229-1](https://lwn.net/Articles/1071323/) | 22.04 24.04 25.10 26.04 | sed | 2026-05-04 |
| Ubuntu | [USN-8218-1](https://lwn.net/Articles/1070847/) | 18.04 20.04 22.04 24.04 | zulucrypt | 2026-04-30 |

전체 기사

(

댓글: 없음

)

## 주목할 만한 커널 패치

### 커널 릴리스

#### 요약

- Linus Torvalds와 Greg Kroah-Hartman의 메인라인 및 안정(stable) 커널 릴리스 공지 목록입니다.
- Linux 7.1-rc2와 여러 안정·장기 유지보수 계열 업데이트가 포함됩니다.[^art3-note7]
- 운영 커널을 추적하는 배포판·어플라이언스·클라우드 팀에 릴리스 기준점을 제공합니다.

Linus Torvalds

Linux 7.1-rc2

5월 3일

Greg Kroah-Hartman

Linux 7.0.3

4월 30일

Greg Kroah-Hartman

Linux 6.18.26

4월 30일

Greg Kroah-Hartman

Linux 6.12.85

4월 30일

Greg Kroah-Hartman

Linux 6.6.137

4월 30일

Greg Kroah-Hartman

Linux 6.1.170

4월 30일

Greg Kroah-Hartman

Linux 5.15.204

4월 30일

### 아키텍처별 변경

#### 요약

- x86, ARM64, m68k, RISC-V 등 아키텍처별 최적화와 기능 추가 패치 목록입니다.
- BPF JIT, PMU 분할, resctrl, VDSO, LAM 등 하드웨어 밀접 기능이 포함됩니다.[^art3-note8]
- 아키텍처별 ABI·성능·관측성 변화는 드라이버와 배포판 커널 구성에 직접적인 영향을 줄 수 있습니다.

Yang Shi

최적화: this_cpu_*() ops for non-x86 (ARM64 for this series)

4월 29일

Colton Lewis

ARM64 PMU Partitioning

5월 4일

Kuan-Wei Chiu

m68k, bpf: 추가: 초기 BPF JIT compiler 지원:

5월 3일

Kuan-Wei Chiu

riscv, bpf: 수정: signed operations 및 추가: 32 bit atomics

4월 29일

Maciej Wieczor-Retman

x86: 단순화: LAM

4월 29일

Reinette Chatre

x86,fs/resctrl: 개선: resctrl 품질과 일관성

4월 29일

Tony Luck

허용: AET to use PMT as 로드 가능 모듈

4월 29일

Babu Moger

[PATCH v3 00/12] x86/resctrl: 추가: 커널 모드 (e.g., PLZA) 지원: to the resctrl subsystem

4월 30일

Valentin Schneider

x86: 지연: some IPIs until a 사용자->커널 전환

5월 5일

Jens Remus

x86/vdso: VDSO 업데이트와 수정 for sframes

5월 5일

### 빌드 시스템

#### 요약

- objtool과 klp-build 관련 수정·개선 패치가 나열되어 있습니다.
- 커널 빌드 검증, 라이브패칭(live patching), 대체 명령어 주소 처리의 신뢰성과 관련됩니다.[^art3-note9]
- 빌드 시스템 변경은 배포판 CI와 out-of-tree 모듈 빌드 실패를 줄이는 데 중요합니다.

Josh Poimboeuf

objtool/klp: Some klp-build 수정과 개선

4월 30일

Sathvika Vasireddy

objtool: 수정: alternate 기능 relative addresses

5월 5일

### 코어 커널

#### 요약

- io_uring, sched_ext, ring-buffer, workqueue, membarrier, Rust SRCU 등 코어 서브시스템 패치가 포함됩니다.
- 스케줄링, 추적, 부팅, 동기화, 비동기 I/O 같은 공통 경로의 성능과 안정성을 겨냥합니다.[^art3-note10]
- 이 영역의 변화는 파일시스템·네트워크·드라이버를 포함한 전체 커널 동작에 파급될 수 있습니다.

Pavel Begunkov

추가: dmabuf read/write via io_uring

4월 29일

Tejun Heo

sched_ext: Topological CPU IDs 및 cid-form struct_ops

4월 29일

Masami Hiramatsu (Google)

ring-buffer: 만들기: 영속 ring buffers 견고하게

4월 30일

Pratyush Yadav

kho: 만들기: 부팅 시 huge page 할당 원활히 동작 with KHO

4월 29일

Yuri Andriaccio

Hierarchical Constant Bandwidth Server

4월 30일

Cris Jacob Maamor

liveupdate: 복원된 항목 검증 LUO metadata

5월 1일

Onur Özkan

rust: 추가: SRCU 추상화

5월 2일

Aniket Gattani

sched/membarrier: Use per-CPU mutexes for 대상 지정 명령

5월 3일

Qais Yousef

sched/fair/schedutil: 더 잘 관리: 시스템 응답 시간

5월 4일

Jens Remus

unwind_deferred: 구현: sframe 처리

5월 5일

Marco Crivellari

추가: WQ_PERCPU to alloc_workqueue 사용자 및 workqueue 대체

5월 5일

### 개발 도구

#### 요약

- selftests, KUnit, kallsyms, tracepoint, VFIO selftest 등 커널 개발·검증 도구 패치입니다.
- 테스트 범위와 디버깅 정보를 넓혀 회귀(regression)를 더 빨리 찾도록 돕습니다.[^art3-note11]
- 배포판 커널 CI와 하드웨어 벤더 검증 자동화에 실용적 가치가 큽니다.

Ricardo B. Marlière

selftests/bpf: Tolerate 부분 빌드 across 커널 구성

4월 29일

Bart Van Assche

활성화: 락 컨텍스트 분석 for the SCSI subsystem

4월 30일

Minxi Hou

selftests: openvswitch: 추가: vlan() 및 encap() flow string parsing

5월 1일

Minxi Hou

selftests: openvswitch: 추가: pop_vlan test

5월 1일

Albert Esteve

kunit: 지원 추가: suppressing 경고 백트레이스

5월 4일

Albert Esteve

cgroup: dmem: 추가: selftest helper, coverage, 및 VM runner

5월 4일

Thomas Weißschuh

kunit: 도입: UAPI testing 프레임워크

5월 4일

Sasha Levin

kallsyms: embed 소스 파일:행 정보 in 커널 스택 트레이스

5월 4일

Abhishek Bapat

alloc_tag: 도입: IOCTL-based 필터링 for MAP

5월 4일

Allison Henderson

selftests: rds: 로그 수집, TAP 준수 및 정리

5월 3일

Dmitry Ilvokhin

locking: contended_release tracepoint 계측

5월 5일

Raghavendra Rao Ananta

vfio: selftest: 추가: SR-IOV UAPI test

5월 5일

### 장치 드라이버

#### 요약

- RISC-V, Qualcomm, MediaTek, Renesas, 네트워크, DRM, IIO, USB, GPU 등 광범위한 드라이버 패치 목록입니다.
- 새 SoC·센서·네트워크 칩·디스플레이·전원관리 하드웨어 지원이 대거 포함됩니다.[^art3-note12]
- 하드웨어 지원 패치는 임베디드 제품, 노트북, 서버 NIC, 가속기 플랫폼의 커널 채택 가능성을 넓힙니다.

Anup Patel

Linux RISC-V trace 프레임워크 및 드라이버

4월 29일

Marius Cristea

지원 추가: Microchip EMC1812

4월 29일

Komal Bajaj

pinctrl: qcom: 지원 추가: Qualcomm Shikra SoC

4월 29일

Muchamad Coirul Anwar

iio: position: 추가: Rust 드라이버 for ams AS5600

4월 29일

Andre Przywara

arm_mpam: 추가: MPAM-Fb firmware 지원:

4월 29일

Ivan Vecera

dpll: rework fractional frequency offset reporting

4월 29일

Kathiravan Thirumoorthy

추가: minimal boot 지원: for Qualcomm IPQ9650 SoC

4월 29일

Bartosz Golaszewski

nvmem: rework nvmem core 및 allow unbinding with active consumers

4월 29일

Prabhakar

추가: DU 지원: for RZ/T2H 및 RZ/N2H SoCs

4월 29일

Birger Koblitz

r8152: 지원 추가: the RTL8159 10Gbit USB Ethernet chip

4월 29일

Viken Dadhaniya

추가: QSPI 지원: for QCS615 및 개선: interconnect 처리

4월 29일

Radhey Shyam Pandey

usb: dwc3: xilinx: 추가: Versal2 MMI USB 3.2 controller 지원:

4월 29일

Rahul Sharma

추가: runtime PM 지원: to K3 UDMA 및 K3 INTA

4월 29일

Miquel Raynal

mtd: spinand: Winbond continuous read 지원:

4월 29일

Adrián Larumbe

지원: sparse mappings in Panthor

4월 29일

Stefan Dösinger

지원 추가: ZTE zx297520v3

4월 29일

Long Li

net: mana: Per-vPort EQ 및 MSI-X interrupt management

4월 29일

Alexey Klimov

Exynos-pmu: 일반화: cpu{hotplug,idle},PMU intr gen 및 추가: Exynos850 CPU hotplug

4월 30일

Cyril Chao

ASoC: mediatek: 지원 추가: MT8196 SoC

4월 30일

Wei Fang

추가: preliminary NETC switch 지원: for i.MX94

4월 30일

Colin Huang via B4 Relay

지원 추가: Delta E50SN12051

4월 30일

Linlin Zhang

soc: qcom: ice: 활성화: firmware managed resource

4월 29일

Nuno Sá via B4 Relay

hwmon: 지원 추가: the LTC4283 Hot Swap Controller

4월 29일

William Bright

drm/panel: 지원 추가: TSD TST070WSBE-196C 8" MIPI-DSI panel

4월 27일

Luca Weiss

추가: LPASS LPI pin controller 지원: for SM6350

4월 30일

Svyatoslav Ryhel

power: supply: 지원 추가: Surface RT battery 및 charger

4월 30일

Neil Armstrong

regulator: 지원 추가: SGM3804 Dual Output 드라이버

4월 30일

Biju

추가: Renesas RZ/G3L PINCONTROL 지원:

4월 30일

Jens Emil Schulz Østergaard

net: dsa: 추가: DSA 지원: for the LAN9645x switch chip family

4월 30일

Neil Armstrong

backlight: 추가: SY7758 6-channel High Efficiency LED Driver 지원:

4월 30일

Benoît Monin

dmaengine: fsl-edma: Scatter/gather 개선

4월 30일

syyang@lontium.com

추가: Lontium LT7911EXC eDP to MIPI DSI bridge

4월 30일

Grzegorz Nitka

dpll/ice: 추가: generic DPLL type 및 전체 TX reference clock control for E825

4월 30일

Radu Sabau via B4 Relay

iio: adc: ad4691: 추가: 드라이버 for AD4691 multichannel SAR ADC family

4월 30일

Charles Keepax

개선: SDCA 지원: for duplicated features

4월 30일

Meghana Malladi

추가: Frame Preemption MAC Merge 지원: for ICSSG

4월 30일

David Yang

net: dsa: yt921x: 추가: port police 지원:

4월 30일

Niranjan H Y

ASoC: 추가: TI TAC5XX2 SoundWire codec 드라이버 지원:

4월 30일

Tycho Andersen

구현: SNP DOWNLOAD_FIRMWARE_EX 지원:

4월 30일

Devarsh Thakkar

추가: DRM 드라이버 for Solomon SSD16xx e-paper display controllers

5월 1일

Sebastian Reichel

Synopsys DisplayPort Controller 개선 for Rockchip platforms

5월 1일

Tariq Toukan

net/mlx5: 개선: representor lifecycle 및 allow switchdev by default

5월 1일

Luca Weiss

MDSS / DPU bringup for Milos

5월 1일

Junyang Han

추가: ZTE DingHai Ethernet PF 드라이버

4월 30일

Jason Gunthorpe

mlx5 지원: for VFIO self test

4월 30일

Hendrik Noack

지원 추가: Wacom W9000-series penabled touchscreens

5월 1일

Luca Weiss

추가: Novatek NT37705 panel 드라이버 for Fairphone (Gen. 6)

5월 1일

Tanmay Shah

remoteproc: xlnx: 추가: auto-boot 지원:

5월 1일

Alex Elder

net: 활성화: TC956x 지원:

5월 1일

Elson Serrao

개선: Qualcomm EUD 드라이버 및 platform 지원:

5월 1일

Joel Fernandes

gpu: nova-core: 추가: INTR_CTRL interrupt controller 및 CPU doorbell self-test

5월 1일

David E. Box

추가: ACPI-based PMT discovery 지원: for Intel PMC

5월 1일

Alexander Koskovich

지원 추가: Adreno 810 GPU

5월 2일

Richard Acayan

SDM660 sound card 및 internal MI2S 지원:

5월 1일

Chris Morgan

추가: Invensense ICM42607

5월 1일

Inochi Amaoto

riscv: spacemit: 추가: PCIe RC controller 지원: for K3

5월 2일

Salih Erim

iio: adc: 추가: AMD/Xilinx Versal SysMon 드라이버

5월 2일

Svyatoslav Ryhel

mfd: 지원 추가: Asus Transformer embedded controller

5월 2일

Guodong Xu

spi: 지원: the SpacemiT K1 SPI controller

5월 2일

David Yang

net: dsa: yt921x: 추가: port qdisc tbf 지원:

5월 3일

Ciprian Regus via B4 Relay

net: 추가: ADIN1140 지원:

5월 3일

Luiz Angelo Daros de Luca

net: dsa: realtek: rtl8365mb: bridge offloading 및 VLAN 지원:

5월 3일

James Ye

HID: asus: 지원 추가: T3304 keyboard

5월 3일

Satish Kharat

enic: SR-IOV V2 admin channel 및 MBOX protocol

5월 3일

Piyush Patle

iio: adc: hx711: 추가: HX710B 지원:

5월 3일

Rudraksha Gupta via B4 Relay

Samsung Expressatt: Camera Flash

5월 3일

Niklas Söderlund

media: 지원 추가: R-Car ISP using Dreamchip RPPX1 ISP

5월 4일

Tzu-Hao Wei

추가: eMMC PHY 지원: for Axiado AX3000 SoC

5월 4일

Mikhail Kalashnikov

Allwinner: A523: 지원 추가: A523 THS0/1 controllers

5월 4일

Subbaraya Sundeep

octeontx2: CN20K NPA Halo context 지원:

5월 4일

Crescent Hsieh

serial: 8250: 추가: MUEx50 지원: for Moxa PCIe boards

5월 4일

Raviteja Laggyshetty

추가: interconnect 지원: for Qualcomm Shikra SoC

5월 4일

Joshua Crofts via B4 Relay

iio: magnetometer: ak8975: modernize 및 정리 드라이버

5월 4일

Avinash Bhatt

wifi: iwlwifi: 추가: Device Tree hardware integration information

5월 4일

Bartosz Golaszewski

pinctrl: qcom: 지원 추가: the TLMM controller on Nord platforms

5월 4일

Adrian Hunter

i3c: mipi-i3c-hci: DMA abort, recovery 및 related 개선

5월 4일

Khristine Andreea Barbulescu

gpio: siul2-s32g2: 추가: 초기 GPIO 드라이버

5월 4일

Sumit Garg

firmware: qcom: 추가: OP-TEE PAS service 지원:

5월 4일

Daniel Machon

net: lan966x: 지원 추가: PCIe FDMA

5월 4일

Angelo Dureghello

추가: mcf54415 DAC 드라이버

5월 4일

Roman Vivchar via B4 Relay

추가: AUXADC, EFUSE 및 thermal 드라이버 for the MediaTek mt6323 PMIC

5월 4일

Rob Clark

drm/msm: 추가: PERFCNTR_CONFIG ioctl

5월 4일

Jonas Karlman

drm: bridge: dw_hdmi: Misc 활성화:/disable, CEC 및 EDID 정리

5월 4일

Frank Li

pinctrl: 추가: generic pinctrl for board-level mux chips

5월 4일

Cheng Ming Lin

mtd: spi-nand: 지원 추가: randomizer 기능

5월 5일

Xi Pardee

활성화: NVL 지원: in intel_pmc_core

5월 4일

Kate Hsuan

추가: Sony IMX471 camera sensor 드라이버

5월 5일

Vishnu Reddy

media: iris: 지원 추가: glymur platform

5월 5일

Biju

clk: renesas: r9a08g046: 추가: {RSCI,RSPI,SSIF-2} clk/resets

5월 5일

Gregor Herburger

nvmem: 추가: Raspberry Pi OTP nvmem 드라이버

5월 5일

Maciek Machnikowski

구현: PTP 지원: in netdevsim

5월 3일

Michael Chan

bnxt_en: 추가: kTLS TX offload 지원:

5월 4일

Varadarajan Narayanan

추가: new 드라이버 for WCSS secure PIL loading

5월 5일

Umang Chheda

ras: aest: 확장: AEST 지원: to Device Tree frontend

5월 5일

Lizhi Hou

SR-IOV Virtual Function 지원: for AIE4 platform

5월 5일

Heiko Stuebner

rockchip: 추가: USB 2.0 지원: for RK3528

5월 5일

Terry Bowman

활성화: CXL PCIe Port Protocol Error 처리 및 logging

5월 5일

Christian Marangi

net: pcs: 도입: 지원: for fwnode PCS

5월 5일

Farhan Ali

Error recovery for vfio-pci devices on s390x

5월 5일

Erikas Bitovtas

media: qcom: venus: 추가: MSM8939 지원:

5월 6일

LiangCheng Wang

지원 추가: PIXPAPER 4.26 monochrome e-ink panel

5월 6일

Billy Tsai

pinctrl: aspeed: 추가: AST2700 SoC0 지원:

5월 6일

javen

r8169: 추가: RSS 지원: for RTL8127

5월 6일

Qiang Yu

clk: qcom: 추가: common clkref 지원: 및 migrate Glymur

5월 6일

Bin Du

추가: AMD ISP4 드라이버

5월 6일

### 장치 드라이버 인프라

#### 요약

- 드라이버 코어, Rust 바인딩, Generic PHY, RDMA umem, V4L2, remoteproc 등 공통 인프라 변경입니다.
- 개별 드라이버가 공유하는 API를 다듬어 중복 구현과 수명주기 오류를 줄이는 데 초점을 둡니다.[^art3-note13]
- 인프라 패치는 장기적으로 드라이버 유지보수성과 Rust-for-Linux 확장성에 영향을 줍니다.

Daniel Lezcano

지원: 냉각 장치 with ID in the OF

4월 29일

David Jeffery

장치를 비동기로 종료

4월 29일

Markus Probst

rust: leds: 추가: led classdev 추상화

4월 29일

Markus Probst via B4 Relay

rust: 추가: 기본 serial device bus 추상화

4월 29일

Sanjay Chitroda

iio: 도입: devm_ API for hid sensro setup 및 정리

4월 29일

Markus Fritsche

media: videobuf2: opt-in dma_resv producer fences for V4L2 dmabuf exports

4월 29일

Vladimir Oltean

분리: Generic PHY consumer 및 provider

4월 30일

Troy Mitchell

ASoC: 추가: shared BCLK rate constraint for cross-DAI coordination

4월 30일

Thomas Weißschuh

드라이버 core: 허용: the constification of 장치 속성

5월 4일

Jiri Pirko

RDMA: 도입: generic 버퍼 디스크립터 인프라 for umem

5월 4일

Manos Pitsidianakis

추가: Rust virtio bindings 및 샘플 장치

5월 5일

Vladimir Oltean

분리: Generic PHY consumer 및 provider API

5월 5일

Jacopo Mondi

media: v4l2-isp: 지원 추가: extensible 통계

5월 5일

Mukesh Ojha

분리: 리소스 테이블 정의 from remoteproc

5월 6일

Conor Dooley

generic pinmux dt_node_to_map implementation

5월 6일

### 문서화

#### 요약

- 보안 버그 처리와 유지보수자 문서 출력 개선에 관한 문서 패치입니다.
- 취약점 triage와 AI 관련 안내처럼 프로세스 문서가 커널 보안 대응에 직접 관여합니다.[^art3-note14]
- 정확한 문서는 외부 보고자, 배포판 보안팀, 유지보수자 간의 오해를 줄입니다.

Willy Tarreau

Documentation: security-bugs: 다루는 새 업데이트: triage 및 AI

5월 3일

Mauro Carvalho Chehab

개선: process/maintainers 출력

5월 4일

### 파일시스템과 블록 계층

#### 요약

- Ceph, VFS, XFS, exFAT, dm-inlinecrypt, BPF 기반 I/O 스케줄러 관련 패치입니다.
- 파일 조회, inode 회수, 블록 암호화, fallocate 동작, I/O 스케줄링의 성능·무결성과 관련됩니다.[^art3-note16]
- 스토리지 워크로드와 데이터 무결성 요구가 큰 서버에서 실질적인 운영 영향이 있을 수 있습니다.

Alex Markuze

ceph: 수동 클라이언트 세션 재설정

4월 29일

NeilBrown

VFS: Prepare to lift lookup out of exclusive lock for directory ops

4월 30일

Chuck Lever

Exposing 대소문자 접기 동작

4월 29일

Jan Kara

fs: 지연 inode 회수

4월 29일

Linlin Zhang

dm-inlinecrypt: 추가: target for 인라인 블록 장치 암호화

4월 30일

Pankaj Raghav

추가: FALLOC_FL_WRITE_ZEROES 지원: to xfs

5월 1일

Kaitao cheng

block: 도입: a BPF-based I/O scheduler

5월 3일

David Timber

exfat: 메모리 최적화 및 stringent 무결성 검사 for 대문자 변환 테이블

5월 5일

### 메모리 관리

#### 요약

- THP/mTHP, per-VMA lock, mmap_lock 경합, DAMON, page_owner, MGLRU, reclaim 등 메모리 패치 목록입니다.
- 대형 folio, 페이지 폴트, COW, 스왑, 장치 페이지 마이그레이션 개선이 포함됩니다.[^art3-note17]
- 메모리 관리 변화는 데이터베이스, 브라우저, VM, GPU 워크로드의 지연시간과 처리량에 영향을 줄 수 있습니다.

Zi Yan

제거: CONFIG_READ_ONLY_THP_FOR_FS 및 활성화: file THP for 쓰기 가능 파일

4월 29일

Dave Hansen

mm: Make per-VMA locks 모든 빌드에서 사용 가능

4월 29일

Barry Song (Xiaomi)

mm: reduce mmap_lock 경합 및 개선: 페이지 폴트 성능

4월 30일

gutierrez.asier@huawei-partners.com

mm/damon: 도입: a huge page collapsing mechanism using 자동 튜닝

4월 30일

Zhen Ni

mm/page_owner: 추가: 필터 인프라 for print_mode 및 NUMA 필터링

5월 1일

Rik van Riel

1GB superpageblock 메모리 할당

4월 30일

Luka Bai

mm: 지원: selecting doing direct COW for anonymous pmd entry

5월 1일

Jeff Layton

mm: 개선: write 성능 with RWF_DONTCACHE

5월 1일

Luiz Capitulino

mm: thp: always 활성화: mTHP 지원:

5월 1일

Kairui Song via B4 Relay

mm/mglru: MGLRU-FG 및 refault distance 지원:

5월 2일

Vernon Yang

mm: 도입: mthp_ext via cgroup-bpf to 만들기: mTHP more 투명하게

5월 4일

Bharata B Rao

mm: hot page 추적 및 승격 인프라

5월 4일

mpenttil@redhat.com

Migrate on fault for device pages

5월 5일

Nhat Pham

가상 스왑 공간

5월 5일

Matthew Brost

mm, drm/ttm, drm/xe: Avoid 회수/eviction 루프 under 단편화

5월 5일

Dev Jain

최적화: 익명 large folio unmapping

5월 6일

Nicolas Frattaroli

Let 사용자 공간이 명시적으로 메모리 회수를 트리거

5월 6일

### 네트워킹

#### 요약

- TLS, PTP, mac80211, bridge, netlink, SRv6, XFRM, IPv6 확장 헤더 등 네트워크 패치입니다.
- 하드웨어 오프로딩, 터널링, 시간 동기화, DoS 완화, 모바일 사용자 평면 지원이 포함됩니다.[^art3-note18]
- 네트워크 스택 변경은 클라우드, 통신망, 컨테이너 네트워킹, 보안 장비에서 중요합니다.

nmreadelf

netns: 선택적으로 상속 IPv4 TCP sysctls from old net

4월 30일

Rishikesh Jethwani

tls: 추가: TLS 1.3 하드웨어 오프로딩 지원:

4월 29일

Chuck Lever

TLS read_sock 성능 확장성

4월 29일

Arthur Kiyanovski

ptp: 추가: PHC 타임스탬프 품질 속성

4월 30일

Miri Korenblit

wifi: mac80211: more NAN patches

4월 29일

Ujjal Roy

net: bridge: mcast: 지원: 지수 필드 인코딩

5월 1일

Breno Leitao

net: 전환: AF_NETLINK 및 AF_VSOCK to getsockopt_iter API

5월 1일

Wei Wang

psp: 지원 추가: dev-assoc/disassoc

5월 1일

Kuniyuki Iwashima

udp_tunnel: Speed up UDP tunnel 장치 파괴 (Part I)

5월 2일

Danielle Ratson

bridge: 추가: 선택적 포워딩 of gratuitous neighbor announcement

5월 3일

Yuya Kusakabe

seg6: 추가: SRv6 Mobile User Plane (RFC 9433) 동작

5월 4일

Antony Antony

xfrm: XFRM_MSG_MIGRATE_STATE new netlink message

5월 5일

Tom Herbert

ipv6: Address ext hdr DoS 취약점

5월 4일

Yuya Kusakabe

seg6: SRv6 Mobile User Plane (RFC 9433)

5월 4일

Lorenzo Bianconi

추가: IPv4 over IPv6 flowtable SW acceleration

5월 5일

### 보안 관련

#### 요약

- IMA, LSM, Landlock, seccomp, AF_ALG, 모듈 무결성, pkeys 기반 page table hardening 패치입니다.
- 접근 제어, 샌드박싱, 커널 모듈 검증, 암호 API의 공격 표면 축소와 관련됩니다.[^art3-note19]
- 보안 패치는 배포판 기본 정책과 컨테이너 격리, 고신뢰 시스템 설계에 직접적인 영향을 줄 수 있습니다.

Roberto Sassu

ima: 도입: 스테이징 메커니즘

4월 29일

Blaise Boscaccy

재도입: Hornet LSM

4월 29일

Song Liu

lsm: 대체: security_sb_mount with granular mount hooks

4월 29일

Matthieu Buffet

landlock: 추가: UDP 접근 제어 지원:

5월 2일

Cong Wang

seccomp: SECCOMP_IOCTL_NOTIF_PIN_ARGS for race-free unotify

5월 3일

Eric Biggers

crypto: af_alg - 제거: zero-copy 지원: from AF_ALG

5월 3일

Thomas Weißschuh

모듈: 도입: hash-based 무결성 검사

5월 5일

Kevin Brodsky

pkeys-based 페이지 테이블 강화

5월 5일

### 가상화와 컨테이너

#### 요약

- Hyper-V PCI passthrough, KVM MBEC/GMET, dirty-bit 가속, arm64 pKVM, s390 fast inject 패치입니다.
- 게스트 격리, 장치 직접 할당, 가상화 성능과 보안 경계를 개선하는 항목입니다.[^art3-note20]
- 클라우드와 가상화 플랫폼 운영자는 하드웨어 기능 노출 방식과 마이그레이션 비용을 주시해야 합니다.

Mukesh R

PCI passthrough on Hyper-V (Part II)

4월 29일

Paolo Bonzini

KVM: 통합 패치셋 for MBEC/GMET 지원:

4월 30일

Leonardo Bras

KVM Dirty-bit 정리 가속기 (HACDBS)

4월 30일

Yosry Ahmed

KVM: x86/pmu: 지원 추가: AMD Host-Only/Guest-Only bits

4월 30일

Mukesh R

PCI passthrough on Hyper-V (Part I)

4월 30일

Mostafa Saleh

KVM: arm64: SMMUv3 드라이버 for pKVM (trap 및 emulate)

5월 1일

Douglas Freimuth

KVM: s390: Introducing kvm_arch_set_irq_inatomic Fast Inject

5월 5일

### 기타

#### 요약

- 주요 범주에 들어가지 않는 자유 소프트웨어 커뮤니티 소식을 모은 항목입니다.
- Free Software Supporter 같은 일반 커뮤니티 뉴스레터가 포함됩니다.
- 커널 패치 섹션의 기타 항목에서는 Rust 매크로와 perf 도구 개선처럼 범주가 넓은 개발 항목을 다룹니다.[^art3-note15]

Alexandre Courbot

rust: 추가: `bitfield!` macro

5월 1일

Ian Rogers

perf tools: 추가: inject --aslr 기능 및 prerequisite 견고성 수정

5월 5일

**페이지 편집자**: Joe Brockmeier

[^art3-note1]: 커널 행동 강령(Code of Conduct) 관련 보고서는 코드 변경은 아니지만, 유지보수자와 기여자 간의 협업 규칙을 정리한다. 대규모 오픈소스 커널에서는 사회적 절차가 패치 리뷰 품질과 신규 기여자 유입에 실제 영향을 준다.
[^art3-note2]: 배포판 뉴스레터는 커널·사용자 공간 패키지를 어떻게 조합해 릴리스하는지 보여준다. 운영자는 같은 upstream 취약점이라도 배포판별 백포트와 지원 기간이 다르다는 점을 확인해야 한다.
[^art3-note3]: GCC, LLVM, Rust, Go, Firefox 같은 프로젝트의 변화는 ABI, 빌드 옵션, 런타임 성능, 보안 정책에 영향을 줄 수 있다. 배포판과 CI 시스템은 이런 변화에 맞춰 테스트 매트릭스를 조정한다.
[^art3-note4]: CFP(Call for Presentations)는 커뮤니티가 어떤 기술 의제를 공개적으로 논의할지 정하는 창구다. 커널, 스토리지, 임베디드, systemd 계열 주제는 이후 설계 결정과 표준화 논의로 이어질 수 있다.
[^art3-note5]: 행사 일정은 개발자 회의, 미니 컨퍼런스, 보안 서밋이 겹치는지를 판단하는 데 중요하다. 커널 서브시스템별 maintainer가 같은 장소에서 만나면 복잡한 설계 논의가 메일링리스트보다 빠르게 진전되기도 한다.
[^art3-note6]: 보안 권고 표는 CVE 세부 설명이 아니라 패치 대상과 배포판 범위를 요약한다. 실제 대응에서는 권고 링크를 따라 영향받는 버전, 재시작 필요 여부, 커널 라이브패치 가능성, 서비스 노출 상태를 함께 확인해야 한다.
[^art3-note7]: -rc 릴리스는 다음 메인라인 커널의 회귀 테스트 창을 의미하고, stable 릴리스는 이미 배포된 커널 계열의 버그·보안 수정 묶음이다. 운영 환경에서는 기능보다 안정성 검증과 드라이버 호환성 확인이 우선이다.
[^art3-note8]: 아키텍처별 패치는 특정 CPU 기능, 예외 처리, 성능 카운터, 메모리 태깅 등 하드웨어 의존 경로를 바꾼다. 같은 커널 버전이라도 x86, ARM64, RISC-V에서 체감 성능과 보안 기능이 달라질 수 있다.
[^art3-note9]: objtool은 커널 오브젝트를 분석해 스택 검증, ORC unwind, 대체 명령어 같은 저수준 속성을 확인한다. klp-build와 함께 쓰이면 라이브패치가 안전하게 적용될 수 있는지 판단하는 기반이 된다.
[^art3-note10]: 코어 커널 패치는 스케줄러, 동기화, 추적 버퍼, io_uring 같은 공통 경로를 다룬다. 이 계층의 작은 변경도 시스템 전체 지연시간, 처리량, 디버깅 가능성에 넓게 영향을 미친다.
[^art3-note11]: selftests와 KUnit은 커널 내부 API와 UAPI가 의도대로 동작하는지 자동 검증하는 도구다. 배포판 커널은 다양한 구성 옵션으로 빌드되므로 부분 빌드와 구성 차이를 견디는 테스트가 중요하다.
[^art3-note12]: 드라이버 패치는 새 하드웨어 enablement의 핵심이다. SoC, 센서, NIC, GPU, 패널 지원이 upstream에 들어가면 벤더 커널 의존도를 낮추고 장기 유지보수 비용을 줄일 수 있다.
[^art3-note13]: 드라이버 인프라 변경은 개별 장치 지원보다 느리게 보이지만 장기적인 API 안정성과 코드 중복 제거에 중요하다. Rust 추상화와 공통 PHY/RDMA/V4L2 API는 새 드라이버 작성 방식에 영향을 준다.
[^art3-note14]: 커널 보안 문서는 취약점 보고, triage, 공개 시점 조율, AI 도구 사용 같은 절차를 명확히 한다. 절차가 불명확하면 패치 공개 전 정보 노출이나 배포판 간 대응 불균형이 생길 수 있다.
[^art3-note15]: perf 도구와 Rust 매크로 같은 기타 항목은 특정 서브시스템에 묶기 어렵지만 개발자 생산성과 관측성에 영향을 준다. 예를 들어 perf inject의 ASLR 기능은 프로파일링 데이터를 더 정확히 해석하는 데 도움이 된다.
[^art3-note16]: 파일시스템과 블록 계층은 데이터 일관성, 지연시간, 암호화, 캐시 동작을 좌우한다. VFS 잠금 구조나 BPF 기반 I/O 스케줄러 같은 변화는 고성능 스토리지와 멀티테넌트 시스템에서 특히 중요하다.
[^art3-note17]: THP, mTHP, MGLRU, DAMON, reclaim 정책은 메모리 압박 상황에서 애플리케이션 성능을 크게 바꾼다. 데이터베이스와 VM처럼 메모리 접근 패턴이 큰 워크로드는 커널 업그레이드 전 회귀 테스트가 필요하다.
[^art3-note18]: 네트워크 스택 패치는 TLS 오프로딩, SRv6, XFRM, bridge, IPv6 확장 헤더 처리처럼 성능과 보안 경계가 만나는 영역을 다룬다. 클라우드 네트워킹에서는 기능 추가뿐 아니라 DoS 완화와 netlink UAPI 안정성이 중요하다.
[^art3-note19]: LSM, Landlock, seccomp, IMA, 모듈 무결성 검사는 커널의 방어층을 구성한다. 정책이 강해질수록 보안은 향상될 수 있지만 기존 애플리케이션이나 컨테이너 런타임과의 호환성 확인이 필요하다.
[^art3-note20]: 가상화 패치는 게스트가 하드웨어 기능을 얼마나 안전하고 빠르게 사용할 수 있는지를 바꾼다. PCI passthrough, pKVM, dirty-bit 가속은 성능과 격리 사이의 균형을 조정하는 핵심 요소다.
