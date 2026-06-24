# docker-bench

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | cloud — Cloud & Container Security |
| **Binary** | `docker-bench-security` ❌ missing |
| **Agent** | cloud |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Docker CIS benchmark

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
docker-bench-security
```

| Metric | Value |
|--------|-------|
| Duration | 0.0s |
| Exit code | 127 |
| Effectiveness | **1/10** — Tool binary not installed |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
command not found: docker-bench-security
```

## What I Learned / Edge Cases / Gotchas
- `docker-bench-security` not found — run `scripts/kali-full-bootstrap.sh`
- Cloud tools may need API credentials; container scans work offline with trivy/grype
- Registry template: `docker-bench-security {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `docker-bench-security --help` and tune `docker-bench-security {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:29.049994+00:00*
