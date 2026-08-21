# Shizuku Platform

> **Brand**: Shizuku | **Abbreviation**: **zuku (즈쿠)** | **Domain**: [zuzunza.com](https://zuzunza.com)
> **GitHub Organization**: [github.com/zukuapp](https://github.com/zukuapp)

Shizuku is a modern interactive UGC media platform inspired by the JujeonJi.com (주전자닷컴) spirit. Built with an open-source stack centered around Next.js (SSR), WebAssembly (WASM) runtime, Rust/C++ backend services, PostgreSQL, and Redis.

## Media Types

| Type   | Format         | Description                                    |
|--------|---------------|------------------------------------------------|
| Hype   | MP4 / Image    | Interactive long-form horizontal media          |
| Swipe  | MP4 (Vertical) | Short-form vertical video feed                 |
| Jump   | WASM/HTML5     | Browser-based interactive games & experiences  |

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

All Jump game content runs inside an **unprivileged WASM sandbox** with syscall filtering and resource limits (CPU, memory, PID, FD).

## Documentation

This repository contains the public design documentation for the Shizuku Platform.

| Category | Description |
|----------|-------------|
| [00-overview](docs/00-overview.md) | Master overview and platform vision |
| [01-architecture](docs/01-architecture.md) | System architecture and component design |
| [02-project-management](docs/02-project-management.md) | Project process and methodology |
| [05-database](docs/05-database.md) | Database schema and data modeling |
| [06-api](docs/06-api.md) | API design and specification |
| [07-frontend-design](docs/07-frontend-design.md) | UI/UX design system and brand guide |
| [08-deployment](docs/08-deployment.md) | Deployment and infrastructure |

## Technology Stack

| Layer     | Technology                              |
|-----------|----------------------------------------|
| Runtime   | WebAssembly (unprivileged sandbox)      |
| Backend   | Rust / C++ (Mediapipe)                  |
| Web/SSR   | Next.js (React)                         |
| Database  | PostgreSQL + Redis                      |
| Edge/CDN  | Cloudflare (WAF, DDoS, TLS, CDN) + R2   |
| Reverse Proxy | nginx                               |

## Sandbox Philosophy

All executable content (WASM/containers) runs inside an **unprivileged sandbox boundary**. The sandbox enforces:
- **Resource limits**: CPU, memory, PID, FD caps
- **Syscall filtering**: Only allowed syscalls are permitted
- **Memory accounting**: Per-runtime memory tracking

The internal syscall filter rules and memory counting logic are **proprietary (SEL/Private)** and not disclosed in public documentation. Only the boundary, resource limits, and interface contracts are published.

## Licensing

Shizuku Platform uses a **Dual Licensing Model**:
- **Shizuku Open License (SOL)** — Apache 2.0 + attribution requirements for open-source use
- **Shizuku Enterprise License (SEL)** — Commercial license for enterprise features

See [LICENSE.md](LICENSE.md) for details.

## Related Repositories

| Repository | Description |
|-----------|-------------|
| [zuku-api](https://github.com/zukuapp/zuku-api) | OpenAPI spec & SDK package |
| [zuku-engine-next2d](https://github.com/zukuapp/zuku-engine-next2d) | Jump game engine |
| [zuku-cli](https://github.com/zukuapp/zuku-cli) | CLI tools |

## Brand Assets

Logo files are available in the [assets/](assets/) directory.

---

*Shizuku Platform — Building the next generation of interactive UGC media.*
