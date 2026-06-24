# h8mail

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | osint — OSINT |
| **Binary** | `h8mail` ❌ missing |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `localhost` |

## Official Purpose
Email breach search

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
h8mail -t test@localhost
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
command not found: h8mail
```

## What I Learned / Edge Cases / Gotchas
- `h8mail` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `h8mail -t test@{host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `h8mail --help` and tune `h8mail -t test@{host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:34.688517+00:00*
