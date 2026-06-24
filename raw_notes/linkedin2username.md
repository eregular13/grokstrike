# linkedin2username

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | osint — OSINT |
| **Binary** | `linkedin2username` ❌ missing |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `localhost` |

## Official Purpose
LinkedIn username enum

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
linkedin2username -c 'Company'
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
command not found: linkedin2username
```

## What I Learned / Edge Cases / Gotchas
- `linkedin2username` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `linkedin2username -c 'Company' {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `linkedin2username --help` and tune `linkedin2username -c 'Company' {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:36.069870+00:00*
