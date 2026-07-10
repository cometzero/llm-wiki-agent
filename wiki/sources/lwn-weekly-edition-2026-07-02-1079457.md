---
title: "LWN.net Weekly Edition for July 2, 2026"
type: source
tags: [lwn, linux, kernel, debian, git, bpf, security, storage]
date: 2026-07-02
source_file: raw/lwn-weekly/lwn-weekly-edition-2026-07-02-1079457.md
source_hash: 77aa18050d628c383e5deda9326064322563675035b959c809cb0c527b0e1ce8
source_url: https://lwn.net/Articles/1079457/bigpage
article_id: "1079457"
---

## Summary
이번 LWN Weekly Edition은 [[DebianProtestware]], [[Git255]], [[RhombusMetaprogramming]], [[KernelHardening]], [[KernelWriteback]], [[BPFLocalStorage]], [[LinuxKernel72]], [[SecureBootCertificateExpiration]], [[ObjectStorageAlternatives]], [[OSPM2026]]를 한 호에 묶어 배포판 신뢰 체인, 개발 도구, 언어 설계, 커널 보안·I/O·BPF, 스토리지 운영, 전력·스케줄링 이슈를 종합한다. 공개 bigpage 전체를 한국어로 번역한 raw 문서를 출처로 삼았으며, 보안 업데이트 표와 커널 패치 목록은 추적성을 위해 원문 식별자를 보존했다.

## Key Claims
- [[DebianProtestware]] 논란은 패키지 기능이 사용자 로케일에 따라 정치적 메시지를 노출할 때, 배포판 자유 소프트웨어 기준과 사용자 신뢰가 어떻게 충돌하는지 보여 준다.
- [[Git255]]는 대규모 저장소와 자동화 워크플로에서 체감될 수 있는 Git 2.55의 기능·성능·UX 변경을 정리한다.
- [[RhombusMetaprogramming]]은 Racket 계열의 매크로와 Python 유사 문법을 결합해 언어 확장성과 실용 문법 사이의 절충을 탐색한다.
- [[KernelHardening]] 기사는 allocation token과 bootpatch-SLR을 통해 커널 메모리 버그 악용을 어렵게 만드는 방향을 다룬다.
- [[KernelWriteback]]과 [[BPFLocalStorage]] 보도는 LSFMM+BPF 2026에서 제기된 I/O 시작 시점, 객체별 BPF 상태, verifier/성능 trade-off를 연결한다.
- [[LinuxKernel72]] merge window 후반부는 다음 커널 릴리스의 아키텍처, 드라이버, 파일시스템, 네트워킹, 보안 변경 흐름을 보완한다.
- [[SecureBootCertificateExpiration]]은 UEFI Secure Boot 인증서 만료가 shim, 설치 이미지, 오래된 장비 지원에 주는 운영 리스크를 설명한다.
- [[ObjectStorageAlternatives]]는 MinIO 이후 Ceph와 Garage를 비교하며 S3 호환성만으로는 스토리지 선택을 판단할 수 없음을 보여 준다.
- [[OSPM2026]] 셋째 날 리포트는 Linux 전력 관리와 scheduler 논의가 latency, thermal pressure, energy model, heterogeneous CPU 배치 문제와 맞물려 있음을 보여 준다.

## Key Quotes
> "Should distributions allow software whose behavior changes unexpectedly due to the user's locale setting?" — [[DebianProtestware]] 기사 문제 제기

> Secure Boot certificate expiration is here — [[SecureBootCertificateExpiration]] 기사 맥락

## Connections
- [[BPF]] — local storage, LSFMM+BPF 보도, 7.2 merge window 기능 확장과 연결된다.
- [[LinuxKernel]] — merge window, stable release, patch stream, hardening, writeback 보도와 연결된다.
- [[OSPM2026]] — 이전 LWN 2026-06-25호의 OSPM 1·2일 차 보도에 이어 3일 차를 보완한다.
- [[SupplyChainSecurity]] — Debian protestware와 보안 업데이트 표를 배포판 신뢰 체인 관점으로 연결한다.

## Contradictions
- 기존 wiki 내용과 직접 충돌하는 주장 없음. `tools/ingest.py`가 NVIDIA JSON 응답 파싱 실패로 중단되어 source page와 class-level concept pages를 수동 materialization했다.
