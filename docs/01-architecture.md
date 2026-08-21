# System Architecture

## Overview

The Shizuku Platform follows a service-oriented architecture with strict sandbox isolation for all executable content.

## Component Architecture

```
                    ┌─────────────────────┐
                    │   Client (Browser)   │
                    └──────────┬──────────┘
                               │ HTTPS
                    ┌──────────▼──────────┐
                    │    Cloudflare Edge   │
                    │  (WAF, DDoS, CDN)   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   nginx Reverse Proxy │
                    │  (TLS, Routing, Static)│
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
┌─────────▼──────┐  ┌─────────▼──────┐  ┌─────────▼──────┐
│  Next.js (SSR)  │  │  Rust/C++ Svc  │  │  WASM Sandbox   │
│  Web + API      │  │  Transcode     │  │  Game Runtime    │
└─────────┬──────┘  └─────────┬──────┘  └─────────┬──────┘
          │                    │                    │
┌─────────▼──────┐  ┌─────────▼──────┐             │
│  PostgreSQL    │  │  Redis (Cache)  │             │
└────────────────┘  └────────────────┘             │
                                        ┌─────────▼──────┐
                                        │  Cloudflare R2  │
                                        │  (File Storage)  │
                                        └────────────────┘
```

## Service Dependencies

| Service        | Dependencies                    |
|---------------|---------------------------------|
| Auth Service   | Redis (session), PostgreSQL     |
| Content Service | PostgreSQL, R2, WASM Runtime   |
| Media Service  | Rust/C++ Transcode, R2, PostgreSQL |
| WASM Runtime   | PostgreSQL (binary storage), R2 |

## Deployment Architecture

- Rolling + Blue-Green + Canary deployment
- PostgreSQL streaming replication + R2 backup
- Redis sentinel + AOF persistence
- R2 multi-region replication

## Security

- Cloudflare WAF + DDoS protection
- WASM unprivileged sandbox
- OAuth 2.0 + Session-based auth (Redis)
- PostgreSQL prepared parameterization
- Content Security Policy (CSP)
- XSS protection via Next.js defaults

---

*See [08-deployment.md](08-deployment.md) for detailed deployment architecture.*
