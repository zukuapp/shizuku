# 공개 문서와 배포 정보의 범위

이 저장소는 서비스 배포를 실행하지 않습니다.
[`shizuku` CI](../.github/workflows/ci.yml)는 `main` 푸시와 PR에서 Markdown 검사
및 링크 검사를 수행합니다. 검사 결과는 해당 변경의 GitHub Actions 실행 기록에
남습니다.

## 공개 저장소별 확인 경로

| 대상             | 공개된 확인 방법                                                                             |
| ---------------- | -------------------------------------------------------------------------------------------- |
| 조직 개발 문서   | [`.github` 저장소](https://github.com/zukuapp/.github)의 Markdown과 이미지 자산              |
| 기업 소개 사이트 | [`zukuapp.github.io`](https://github.com/zukuapp/zukuapp.github.io)의 Pages 설정과 정적 파일 |
| ZWF2 컴파일러    | [`zwf`](https://github.com/zukuapp/zwf)의 테스트와 명세                                      |
| ZUKBOX 런타임    | [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime)의 Rust·WASM·JS 테스트          |

공개 웹사이트는 비공개 서비스의 배포 토폴로지, 데이터베이스 복제, 롤백 절차,
자원 한도, 가동률을 증명하지 않습니다. 이 저장소의 문서는 이 운영 정보를 다루지
않습니다.

제품 상태와 서비스 이용 문의는
[지원 안내](https://github.com/zukuapp/.github/blob/main/SUPPORT.md)를 따릅니다.
취약점은 [보안 정책](https://github.com/zukuapp/.github/blob/main/SECURITY.md)에
따라 비공개로 신고합니다.
