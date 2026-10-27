<!-- BEGIN ZUKU OFFICIAL BRAND -->
<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://docs.zuzunza.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)"
        srcset="docs/branding/zuku-logo-dark.png">
      <img src="docs/branding/zuku-logo-light.png"
        alt="ZUKU" width="320">
    </picture>
  </a>
</p>
<p align="center">ZUKU - 내가 불러 일으키는 새로운 창작.</p>
<!-- markdownlint-enable MD033 MD041 -->
<!-- END ZUKU OFFICIAL BRAND -->

# ZUKU 공개 개발 개요

![version](https://img.shields.io/badge/version-v27.26102701-informational)

## 개요

ZUKU는 Trecillo(트레실로)가 만드는 창작·미디어 플랫폼입니다. 이 저장소는 개발
문서의 길잡이입니다. 파일 형식과 API 필드의 기준은 각 저장소의 명세입니다.

| 찾는 내용            | 시작할 곳                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 개발 문서 전체       | [ZUKU 개발자 문서](https://github.com/zukuapp/.github/blob/main/docs/README.md)                                                                        |
| HTML5 게임 패키징    | [`zwf` 5분 입문](https://github.com/zukuapp/.github/blob/main/docs/getting-started.md) · [ZWF2 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| Jump 게임 메타데이터 | [`zuku-engine-next2d` 매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json)                    |
| 공개 API 모델        | [`zuku-api` OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)                                                     |
| ZUKBOX 바이너리      | [`zukbox-runtime` 형식 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md)                                           |

## 사용법

### 이 저장소의 문서

| 문서                                            | 내용                                    |
| ----------------------------------------------- | --------------------------------------- |
| [문서 목차](docs/README.md)                     | 읽는 순서                               |
| [플랫폼 개요](docs/00-overview.md)              | 공개 제품과 개발 경로                   |
| [공개 아키텍처](docs/01-architecture.md)        | ZWF2, ZUKBOX ZWF1, API 계약의 경계      |
| [공개 작업 방식](docs/02-project-management.md) | 변경 제안과 명세 갱신                   |
| [데이터 모델](docs/05-database.md)              | OpenAPI 데이터 모델                     |
| [API 안내](docs/06-api.md)                      | OpenAPI 명세를 읽는 방법                |
| [브랜드 안내](docs/07-frontend-design.md)       | 현행 Trecillo 로고와 ZUKU 색상          |
| [CI와 저장소별 검사](docs/08-deployment.md)     | 저장소별 검사 방법                      |

### 형식과 도구

`zwf`는 HTML5 ZIP을 ZWF2로 컴파일하고 검사하는 공개 도구입니다. ZUKBOX의
ZWF1은 같은 `.zwf` 확장자를 쓰지만 별도 바이너리 형식입니다. 한 형식의 도구로
다른 형식을 읽지 않습니다.

[`zukujs-cli`](https://github.com/zukuapp/zukujs-cli)의 `zuku`와 `zukujs`는
같은 진입점·Agent Core·설정·인증을 사용하는 두 별칭입니다. 사용법은 해당
저장소의 문서에 있습니다.

## 이름과 기여

사용자에게 표시하는 이름은 ZUKU, 회사명은 Trecillo(트레실로)입니다.
`Shizuku`는 이 저장소에 남아 있는 이전 프로젝트명입니다. 현행 로고와 표기법은
[브랜드 문서](docs/07-frontend-design.md)를 따릅니다.

문서 수정 절차는 [기여 안내](CONTRIBUTING.md)에 있습니다. 취약점은 공개 Issue
대신 [보안 정책](https://github.com/zukuapp/.github/blob/main/SECURITY.md)에
따라 비공개로 제보합니다.

## 변경 이력

[CHANGELOG](CHANGELOG.md)에 버전별 변경 사항을 기록합니다.
