# shizuku

ZUKU(즈쿠) 플랫폼의 **공개 홈·문서 인덱스** 저장소입니다.  
브랜드명 Shizuku · 약칭 **zuku (즈쿠)** · 도메인 [zuzunza.com](https://zuzunza.com).

> GitHub 조직: [zukuapp](https://github.com/zukuapp) · 설계도 SSOT: [`zuku-docs`](https://github.com/zukuapp/zuku-docs)

## 미디어 · 제품

| | 포맷 | 설명 |
|---|------|------|
| **Thread** | SNS/포럼 | `www` 홈 · 미디어는 ≤30초 미리보기 + 딥링크 |
| **Hype** | 롱폼 · 가로 영상 · 사진 | 창작 커뮤니티 |
| **Swipe** | 세로 숏폼 | 스튜디오 없음 · Swipe→Hype 배급 금지 |
| **Jump** | WASM/HTML5 | 게임 허브 + Jump Studio |
| **Aist** | 생성 전용 | → Jump Studio draft |

## 스택

Next.js · WebAssembly · Rust · PostgreSQL · Redis · nginx · Cloudflare

## 아키텍처 (요약)

```
Client (Browser / Mobile)
    │
Cloudflare (WAF · CDN)
    │
nginx
    │
Next.js SSR  ·  Rust 백엔드  ·  WASM 런타임(샌드박스 경계)
    │
PostgreSQL · Redis · R2
```

인터랙티브 콘텐츠는 **unprivileged 샌드박스 경계**와 계약된 리소스 한도 안에서 실행됩니다.  
핵심 내부 구현은 공개하지 않습니다.

## 문서

| 경로 | 내용 |
|------|------|
| `docs/` | 공개용 설계·가이드 인덱스 |
| [`zuku-docs`](https://github.com/zukuapp/zuku-docs) | 전체 설계도 (SSOT) |

## 공개 Jump 도구

| 저장소 | 역할 |
|--------|------|
| [zuku-engine-next2d](https://github.com/zukuapp/zuku-engine-next2d) | Jump 엔진·매니페스트 |
| [zuku-cli](https://github.com/zukuapp/zuku-cli) | 검증·패키징 CLI |
| [zuku-api](https://github.com/zukuapp/zuku-api) | OpenAPI 계약 |

## 네이밍

| 표기 | 용도 |
|------|------|
| Shizuku | 브랜드·엔진 코드명 |
| **zuku / 즈쿠** | 공식 약칭 |
| Tresillo | 회사 |

> “시즈쿠” 표기는 사용하지 않습니다.

---

**ZUKU (즈쿠)** · Tresillo · [zuzunza.com](https://zuzunza.com)
