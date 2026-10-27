# 공개 아키텍처와 실행 경계

## HTML5 게임: ZWF2

```text
HTML5 게임 파일 → ZIP → zwf 컴파일러 → ZWF2 .zwf
                                      └→ inspect 검사
ZWF2 .zwf → 호환 플레이어 검증 → 격리된 iframe 실행
```

[`zwf/SPEC.md`](https://github.com/zukuapp/zwf/blob/main/SPEC.md)는 `ZWF2` 헤더,
JSON 매니페스트, ZIP 페이로드와 파일별 SHA-256을 정의합니다. 호환 플레이어의
필수 조건은 다음과 같습니다.

- 불투명 출처의 iframe
- 제한된 `sandbox` 속성
- 응답 헤더의 CSP
- 민감 권한 거부

해시는 파일 손상 확인용이며 제작자 서명이 아닙니다.

브라우저 격리는 계정 데이터와 게임의 접근 권한을 나누는 경계입니다. 플레이어
요구 사항과 한계는
[ZWF2 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md#mandatory-player-behavior)를
따릅니다.

## ZUKBOX 저작물: ZWF1

```text
ZUKBOX 에디터 → ZWF1 .zwf → zukbox-runtime (WASM 파싱·타임라인)
                                     └→ zukbox-player (화면 렌더링)
```

[`zukbox-runtime`의 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md)은
`ZWF1` 청크 기반 바이너리를 다룹니다. 런타임은 파일을 읽고 렌더 목록을 만듭니다.
픽셀 렌더링은 플레이어가 담당합니다. 스크립트 실행과 신뢰되지 않은 콘텐츠의
격리는 호스트가 담당합니다. 런타임은 `SIGN` 서명 검증 등 초안의 일부
기능을 구현하지 않습니다.

ZWF1과 ZWF2는 같은 확장자를 쓰므로 매직 바이트와 해당 명세로 형식을
식별합니다. 한쪽 형식의 파일을 다른 형식의 도구에 넣지 않습니다.

## API와 서비스

[`zuku-api` OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)는
공개 경로와 데이터 모델의 출처입니다. 요청의 인증·입력·응답은 명세의 각 작업에
정의돼 있습니다.

추가 공개 계약은
[조직 개발 문서의 공개 아키텍처](https://github.com/zukuapp/.github/blob/main/docs/architecture.md)와
[저장소 지도](https://github.com/zukuapp/.github/blob/main/docs/repository-map.md)에
있습니다.
