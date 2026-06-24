# sslyze

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `sslyze` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
SSL/TLS analyzer

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
sslyze aegis-target
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
command not found: sslyze
```

## What I Learned / Edge Cases / Gotchas
- `sslyze` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `sslyze {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `sslyze --help` and tune `sslyze {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:41.616462+00:00*
