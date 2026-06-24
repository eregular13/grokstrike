# pacu

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | cloud — Cloud & Container Security |
| **Binary** | `pacu` ❌ missing |
| **Agent** | cloud |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
AWS exploitation framework

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
pacu
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
command not found: pacu
```

## What I Learned / Edge Cases / Gotchas
- `pacu` not found — run `scripts/kali-full-bootstrap.sh`
- Cloud tools may need API credentials; container scans work offline with trivy/grype
- Registry template: `pacu {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `pacu --help` and tune `pacu {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:29.355479+00:00*
