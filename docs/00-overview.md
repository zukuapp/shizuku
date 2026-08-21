# Shizuku Platform — Master Overview

> **Brand**: Shizuku | **Abbreviation**: **zuku (즈쿠)** | **Domain**: zuzunza.com
> **GitHub Organization**: [github.com/zukuapp](https://github.com/zukuapp)

## What is Shizuku (zuku)?

Shizuku (abbreviation: zuku, Korean: 즈쿠) is a modern interactive UGC media platform inspired by the JujeonJi.com (주전자닷컴) spirit. All interactive and game content runs inside an unprivileged sandbox using WebAssembly (WASM) containers, ensuring safety without sacrificing performance.

### Media Types

| Type  | Format     | Description                                   |
|-------|-----------|-----------------------------------------------|
| Hype  | MP4 + Image + WASM | Interactive long-form horizontal media  |
| Swipe | MP4 (9:16) | Short-form vertical video feed               |
| Jump  | WASM/HTML5  | Browser-based interactive games              |

## Technology Stack

| Layer         | Technology                           |
|---------------|-------------------------------------|
| Runtime       | WebAssembly (unprivileged sandbox)  |
| Backend       | Rust / C++ (Mediapipe)              |
| Web/SSR       | Next.js (React)                     |
| Database      | PostgreSQL + Redis                  |
| Edge/CDN      | Cloudflare (WAF, DDoS, TLS, CDN)    |
| Storage       | Cloudflare R2                       |

## Architecture

```
Client (Browser / Mobile)
    |
Cloudflare (WAF + DDoS + SSL + CDN)
    |
nginx (TLS Termination + Static + Routing)
    |
+-----------+------------------+-----------------+
|           |                  |                 |
Next.js SSR  Rust/C++ Backend  WASM Runtime     |
(Web/API)    (Transcode/Core)   (Sandboxed)     |
    |           |                  |              |
PostgreSQL    Redis    Cloudflare R2 (Storage)   |
```

## Sandbox Philosophy

All executable content runs inside an unprivileged sandbox boundary with:
- Resource limits (CPU, memory, PID, FD)
- Syscall filtering
- Memory accounting

Internal syscall filter rules and memory counting logic are proprietary and not publicly disclosed. Only boundary, limits, and interface contracts are published.

## Documentation Index

- `00-overview.md` — This file (master overview)
- `01-architecture.md` — System architecture details
- `02-project-management.md` — Development process
- `05-database.md` — Database schema
- `06-api.md` — API design
- `07-frontend-design.md` — UI/UX and brand guide
- `08-deployment.md` — Deployment architecture

## License

Shizuku Open License (SOL) — Based on Apache 2.0 with attribution requirements.
See [LICENSE.md](../LICENSE.md) for details.

---

*Shizuku Platform — Building the next generation of interactive UGC media.*
