---
title: "Python pathlib"
type: concept
tags: [python, standard-library, filesystem, api-design]
sources: [lwn-weekly-edition-2026-08-20-1088565]
last_updated: 2026-08-28
---

## Summary

[[PythonPathlib|Python pathlib]]는 파일 경로를 문자열로 직접 결합하는 대신 `Path` 객체와 path-like protocol로 표현하는 Python 표준 라이브러리다. `/` 연산자·`joinpath()`·`__fspath__()`는 표현의 가독성과 API 호환성을 높이지만, hot path의 대규모 객체 생성 비용과 filesystem 의미론은 별도로 측정해야 한다.

## Connections

- [[lwn-weekly-edition-2026-08-20-1088565]] — `pathlib`의 설계, 확장, 성능 논의를 다룬다.
