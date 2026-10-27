# CI와 저장소별 검사

[`shizuku` CI](../.github/workflows/ci.yml)는 `main` 푸시와 PR에서 Markdown 검사
및 링크 검사를 수행합니다.

## 저장소별 확인 경로

| 대상             | 확인 방법                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------- |
| 조직 개발 문서   | [`.github` 저장소](https://github.com/zukuapp/.github)의 Markdown과 이미지 자산              |
| 기업 소개 사이트 | [`zukuapp.github.io`](https://github.com/zukuapp/zukuapp.github.io)의 Pages 설정과 정적 파일 |
| ZWF2 컴파일러    | [`zwf`](https://github.com/zukuapp/zwf)의 테스트와 명세                                      |
| ZUKBOX 런타임    | [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime)의 Rust·WASM·JS 테스트          |
